# 把 PDF 页渲染成 PNG，用 Windows 自带的 Windows.Data.Pdf（WinRT），不需要装东西。
# - PowerShell 7：.NET 5+ 没有 WinRT 投影，用 COM 互操作按 vtable 槽位直接调用（IID 和槽位来自 C:\Windows\System32\WinMetadata）。
#   初始化失败时自动转交 Windows PowerShell 5.1；-Legacy 强制转交。
# - Windows PowerShell 5.1：用内置的 WinRT 投影。
# - 渲染总在子进程（-Worker）里做：渲染会建硬件 D3D 设备，有的显卡驱动（实测 AMD atidxx64.dll）在进程退出卸载时
#   访问冲突（0xC0000005），图已经写好，退出码却是崩溃码。子进程写完输出后直接 TerminateProcess，跳过 DLL 卸载；
#   调用方的进程不加载渲染组件，用 & 在当前会话里调用也不会在会话退出时崩。
# -Page：从 0 开始；可写 2、0-4、"0,3,5-7"、all。多页时文件名是 -OutName 加 _pNN，或在 -OutName 里写 {0:D2} 自定。
param([string]$PdfPath, [string[]]$Page = @('0'), [int]$Width = 3000, [string]$OutDir, [string]$OutName, [switch]$Legacy, [switch]$Worker)
$ErrorActionPreference = 'Stop'
$PdfPath = (Resolve-Path -LiteralPath $PdfPath).ProviderPath
$OutDir = (Resolve-Path -LiteralPath $OutDir).ProviderPath

# 子进程的 stdout 原样输出；退出码放 $script:workerCode，stderr 放 $script:workerErrors
function Invoke-Worker([string]$Exe) {
    $a = @('-NoProfile', '-ExecutionPolicy', 'Bypass', '-File', $PSCommandPath, '-PdfPath', $PdfPath,
        '-Page', ($Page -join ','), '-Width', $Width, '-OutDir', $OutDir, '-Worker')
    if ($OutName) { $a += @('-OutName', $OutName) }
    # 5.1 里 Stop 会把原生命令的 stderr 当成终止错误，这里先收集，失败时一起抛出
    $ErrorActionPreference = 'Continue'
    $script:workerErrors = @()
    & $Exe @a 2>&1 | ForEach-Object {
        if ($_ -is [System.Management.Automation.ErrorRecord]) { $script:workerErrors += $_.ToString() } else { $_ }
    }
    $script:workerCode = $LASTEXITCODE
}

# 子进程退出：先刷新输出，再 TerminateProcess 跳过 DLL 卸载（见文件头）
function Exit-Worker([int]$Code) {
    [Console]::Out.Flush(); [Console]::Error.Flush()
    if (-not ('PdfRenderExit' -as [type])) {
        Add-Type -TypeDefinition 'using System; using System.Runtime.InteropServices; public static class PdfRenderExit { [DllImport("kernel32.dll")] public static extern IntPtr GetCurrentProcess(); [DllImport("kernel32.dll")] public static extern bool TerminateProcess(IntPtr h, uint code); }'
    }
    [void][PdfRenderExit]::TerminateProcess([PdfRenderExit]::GetCurrentProcess(), [uint32]$Code)
}

if (-not $Worker) {
    $exe = if ($Legacy -or $PSVersionTable.PSEdition -ne 'Core') { 'powershell.exe' } else { (Get-Process -Id $PID).Path }
    Invoke-Worker $exe
    if ($script:workerCode -ne 0) {
        $msg = ($script:workerErrors -join "`n").Trim()
        if (-not $msg) { $msg = "渲染子进程退出码 $script:workerCode" }
        throw $msg
    }
    exit 0
}

# trap 对整个脚本作用域生效，和写在哪一行无关：父进程里的错误要 break 交还给调用方，不能结束进程
trap {
    if (-not $Worker) { break }
    [Console]::Error.WriteLine($_.Exception.Message); Exit-Worker 1
}

function Get-PageList([string[]]$Spec, [int]$Count) {
    $list = New-Object System.Collections.Generic.List[int]
    foreach ($item in (($Spec -join ',') -split '[,\s]+' | Where-Object { $_ })) {
        if ($item -eq 'all') { if ($Count -gt 0) { 0..($Count - 1) | ForEach-Object { $list.Add($_) } } }
        elseif ($item -match '^(\d+)-(\d+)$') { [int]$Matches[1]..[int]$Matches[2] | ForEach-Object { $list.Add($_) } }
        elseif ($item -match '^\d+$') { $list.Add([int]$item) }
        else { throw "bad -Page item: '$item'" }
    }
    foreach ($p in $list) { if ($p -lt 0 -or $p -ge $Count) { throw "page $p out of range (0..$($Count - 1))" } }
    , $list.ToArray()
}

function Get-OutName([string]$Name, [int]$Index, [bool]$Multi) {
    if (-not $Name) { return 'p{0:D2}.png' -f $Index }
    if ($Name -match '\{0') { return $Name -f $Index }
    if ($Multi) { return [IO.Path]::GetFileNameWithoutExtension($Name) + ('_p{0:D2}' -f $Index) + [IO.Path]::GetExtension($Name) }
    $Name
}

if ($PSVersionTable.PSEdition -eq 'Core') {
    # 改了下面的 C# 要把类名的版本号加一：同一个 PowerShell 会话里不能重新定义同名类型
    $nativeSource = @'
using System;
using System.Collections.Generic;
using System.Runtime.ExceptionServices;
using System.Runtime.InteropServices;
using System.Threading;

public static class PdfRenderNativeV1 {
    [DllImport("combase.dll")] static extern int RoInitialize(int initType);
    [DllImport("combase.dll")] static extern void RoUninitialize();
    [DllImport("combase.dll", CharSet = CharSet.Unicode)] static extern int WindowsCreateString(string src, int len, out IntPtr hstr);
    [DllImport("combase.dll")] static extern int WindowsDeleteString(IntPtr hstr);
    [DllImport("combase.dll")] static extern int RoGetActivationFactory(IntPtr classId, ref Guid iid, out IntPtr factory);
    [DllImport("combase.dll")] static extern int RoActivateInstance(IntPtr classId, out IntPtr instance);
    [DllImport("shlwapi.dll", CharSet = CharSet.Unicode)] static extern int SHCreateStreamOnFileEx(string file, uint mode, uint attr, bool create, IntPtr template, out IntPtr stream);
    [DllImport("shcore.dll")] static extern int CreateRandomAccessStreamOverStream(IntPtr stream, int options, ref Guid riid, out IntPtr ppv);

    static readonly Guid IID_IPdfDocumentStatics   = new Guid("433a0b5f-c007-4788-90f2-08143d922599");
    static readonly Guid IID_IPdfPageRenderOptions = new Guid("3c98056f-b7cf-4c29-9a04-52d90267f425");
    static readonly Guid IID_IRandomAccessStream   = new Guid("905a0fe1-bc53-11df-8c49-001e4fc686da");
    static readonly Guid IID_IClosable             = new Guid("30d5a829-7fa4-4026-83bb-d75bae4ea99e");
    static readonly Guid IID_IAsyncInfo            = new Guid("00000036-0000-0000-c000-000000000046");

    [StructLayout(LayoutKind.Sequential)] public struct Size { public float Width, Height; }
    [UnmanagedFunctionPointer(CallingConvention.StdCall)] delegate int QIFn(IntPtr self, ref Guid iid, out IntPtr ppv);
    [UnmanagedFunctionPointer(CallingConvention.StdCall)] delegate int NoArgFn(IntPtr self);
    [UnmanagedFunctionPointer(CallingConvention.StdCall)] delegate int OutPtrFn(IntPtr self, out IntPtr r);
    [UnmanagedFunctionPointer(CallingConvention.StdCall)] delegate int OutUIntFn(IntPtr self, out uint r);
    [UnmanagedFunctionPointer(CallingConvention.StdCall)] delegate int OutIntFn(IntPtr self, out int r);
    [UnmanagedFunctionPointer(CallingConvention.StdCall)] delegate int OutSizeFn(IntPtr self, out Size r);
    [UnmanagedFunctionPointer(CallingConvention.StdCall)] delegate int UIntFn(IntPtr self, uint a);
    [UnmanagedFunctionPointer(CallingConvention.StdCall)] delegate int UIntOutPtrFn(IntPtr self, uint a, out IntPtr r);
    [UnmanagedFunctionPointer(CallingConvention.StdCall)] delegate int PtrOutPtrFn(IntPtr self, IntPtr a, out IntPtr r);
    [UnmanagedFunctionPointer(CallingConvention.StdCall)] delegate int PtrPtrOutPtrFn(IntPtr self, IntPtr a, IntPtr b, out IntPtr r);

    // 槽位 0..5 是 IUnknown + IInspectable，接口自己的方法从 6 开始，顺序同 WinMD 里的方法顺序
    static T Slot<T>(IntPtr obj, int slot) where T : Delegate {
        IntPtr vtbl = Marshal.ReadIntPtr(obj);
        return Marshal.GetDelegateForFunctionPointer<T>(Marshal.ReadIntPtr(vtbl, slot * IntPtr.Size));
    }
    static void Check(int hr, string what) { if (hr < 0) throw new COMException(what + " 失败", hr); }
    static IntPtr QI(IntPtr obj, Guid iid, string what) {
        IntPtr r; Check(Slot<QIFn>(obj, 0)(obj, ref iid, out r), "QueryInterface " + what); return r;
    }
    static IntPtr Activate(string cls, Guid? factoryIid) {
        IntPtr h, r; Check(WindowsCreateString(cls, cls.Length, out h), "WindowsCreateString");
        try {
            if (factoryIid.HasValue) { Guid iid = factoryIid.Value; Check(RoGetActivationFactory(h, ref iid, out r), "RoGetActivationFactory(" + cls + ")"); }
            else Check(RoActivateInstance(h, out r), "RoActivateInstance(" + cls + ")");
        } finally { WindowsDeleteString(h); }
        return r;
    }
    static void ReleaseAll(List<IntPtr> refs) {
        for (int i = refs.Count - 1; i >= 0; i--) if (refs[i] != IntPtr.Zero) Marshal.Release(refs[i]);
        refs.Clear();
    }

    // 不注册 Completed 回调（那要自己实现 COM 对象），轮询 IAsyncInfo.Status：0 进行中、1 完成、2 取消、3 出错
    static void Wait(IntPtr op, string what) {
        IntPtr info = QI(op, IID_IAsyncInfo, "IAsyncInfo");
        try {
            uint status;
            while (true) {
                Check(Slot<OutUIntFn>(info, 7)(info, out status), "get_Status");
                if (status != 0) break;
                Thread.Sleep(5);
            }
            if (status != 1) {
                int err; Slot<OutIntFn>(info, 8)(info, out err);
                throw new COMException(what + " 异步状态 " + status, err);
            }
        } finally { Marshal.Release(info); }
    }

    // PowerShell 主线程是 STA，换到单独的 MTA 线程做，免得跨套间封送
    static T RunMta<T>(Func<T> body) {
        T result = default(T); Exception error = null;
        var t = new Thread(() => {
            int hr = RoInitialize(1);
            try {
                if (hr < 0 && hr != unchecked((int)0x80010106)) Check(hr, "RoInitialize");
                result = body();
            } catch (Exception e) { error = e; }
            finally { if (hr >= 0) RoUninitialize(); }
        });
        t.SetApartmentState(ApartmentState.MTA);
        t.Start(); t.Join();
        if (error != null) ExceptionDispatchInfo.Capture(error).Throw();
        return result;
    }

    // 文件 -> IStream -> IRandomAccessStream -> PdfDocument（不用 StorageFile，省掉两个异步调用）
    static IntPtr OpenDoc(string pdfPath, List<IntPtr> refs) {
        IntPtr inStm, inRas, loadOp, doc; Guid iidRas = IID_IRandomAccessStream;
        Check(SHCreateStreamOnFileEx(pdfPath, 0x20 /*READ|SHARE_DENY_WRITE*/, 0x80, false, IntPtr.Zero, out inStm), "打开 PDF"); refs.Add(inStm);
        Check(CreateRandomAccessStreamOverStream(inStm, 0, ref iidRas, out inRas), "包装输入流"); refs.Add(inRas);
        IntPtr statics = Activate("Windows.Data.Pdf.PdfDocument", IID_IPdfDocumentStatics); refs.Add(statics);
        Check(Slot<PtrOutPtrFn>(statics, 8)(statics, inRas, out loadOp), "LoadFromStreamAsync"); refs.Add(loadOp);
        Wait(loadOp, "LoadFromStreamAsync");
        Check(Slot<OutPtrFn>(loadOp, 8)(loadOp, out doc), "GetResults(PdfDocument)"); refs.Add(doc);
        return doc;
    }

    public static uint PageCount(string pdfPath) {
        return RunMta(() => {
            var refs = new List<IntPtr>();
            try {
                IntPtr doc = OpenDoc(pdfPath, refs);
                uint n; Check(Slot<OutUIntFn>(doc, 7)(doc, out n), "get_PageCount");
                return n;
            } finally { ReleaseAll(refs); }
        });
    }

    public static Size[] Render(string pdfPath, int[] pages, uint width, string[] outPaths) {
        return RunMta(() => {
            var refs = new List<IntPtr>();
            var sizes = new Size[pages.Length];
            try {
                IntPtr doc = OpenDoc(pdfPath, refs);
                IntPtr insp = Activate("Windows.Data.Pdf.PdfPageRenderOptions", null); refs.Add(insp);
                IntPtr opts = QI(insp, IID_IPdfPageRenderOptions, "IPdfPageRenderOptions"); refs.Add(opts);
                Check(Slot<UIntFn>(opts, 9)(opts, width), "put_DestinationWidth");
                Guid iidRas = IID_IRandomAccessStream;
                for (int i = 0; i < pages.Length; i++) {
                    var pr = new List<IntPtr>();
                    try {
                        IntPtr pg, outStm, outRas, op;
                        Check(Slot<UIntOutPtrFn>(doc, 6)(doc, (uint)pages[i], out pg), "GetPage(" + pages[i] + ")"); pr.Add(pg);
                        Check(Slot<OutSizeFn>(pg, 10)(pg, out sizes[i]), "get_Size");
                        // 输出同样走 IStream -> IRandomAccessStream，默认编码 PNG
                        Check(SHCreateStreamOnFileEx(outPaths[i], 0x1012 /*CREATE|READWRITE|SHARE_EXCLUSIVE*/, 0x80, true, IntPtr.Zero, out outStm), "创建 " + outPaths[i]); pr.Add(outStm);
                        Check(CreateRandomAccessStreamOverStream(outStm, 0, ref iidRas, out outRas), "包装输出流"); pr.Add(outRas);
                        Check(Slot<PtrPtrOutPtrFn>(pg, 7)(pg, outRas, opts, out op), "RenderToStreamAsync"); pr.Add(op);
                        Wait(op, "RenderToStreamAsync");
                        Check(Slot<NoArgFn>(op, 8)(op), "GetResults(render)");
                        IntPtr closable = QI(outRas, IID_IClosable, "IClosable"); pr.Add(closable);
                        Check(Slot<NoArgFn>(closable, 6)(closable), "关闭输出流");
                    } finally { ReleaseAll(pr); }
                }
                return sizes;
            } finally { ReleaseAll(refs); }
        });
    }
}
'@
    $count = $null
    if (-not $Legacy) {
        try {
            if (-not ('PdfRenderNativeV1' -as [type])) { Add-Type -TypeDefinition $nativeSource }
            $count = [PdfRenderNativeV1]::PageCount($PdfPath)
        } catch {
            Write-Warning "原生 WinRT 调用失败，改用 Windows PowerShell 5.1：$($_.Exception.Message)"
        }
    }
    if ($null -eq $count) {
        # 还没渲染过，这个进程没加载显卡驱动，正常退出即可
        Invoke-Worker 'powershell.exe'
        $script:workerErrors | ForEach-Object { [Console]::Error.WriteLine($_) }
        exit $script:workerCode
    }
    "pages: $count"
    $pages = Get-PageList $Page $count
    $outs = [string[]]@(foreach ($p in $pages) { Join-Path $OutDir (Get-OutName $OutName $p ($pages.Count -gt 1)) })
    $sizes = [PdfRenderNativeV1]::Render($PdfPath, $pages, [uint32]$Width, $outs)
    for ($i = 0; $i -lt $pages.Count; $i++) {
        'saved {0} (page {1}, {2:0.##} x {3:0.##})' -f (Split-Path $outs[$i] -Leaf), $pages[$i], $sizes[$i].Width, $sizes[$i].Height
    }
    Exit-Worker 0
}

# Windows PowerShell 5.1：内置 WinRT 投影（这一段的输出只用英文，5.1 经管道输出中文会乱码）
Add-Type -AssemblyName System.Runtime.WindowsRuntime
$null = [Windows.Data.Pdf.PdfDocument, Windows.Data.Pdf, ContentType = WindowsRuntime]
$null = [Windows.Storage.StorageFile, Windows.Storage, ContentType = WindowsRuntime]
$null = [Windows.Storage.StorageFolder, Windows.Storage, ContentType = WindowsRuntime]
$null = [Windows.Storage.Streams.IRandomAccessStream, Windows.Storage.Streams, ContentType = WindowsRuntime]

$methods = [System.WindowsRuntimeSystemExtensions].GetMethods()
$asTaskOp = $methods | Where-Object { $_.Name -eq 'AsTask' -and $_.GetParameters().Count -eq 1 -and $_.GetParameters()[0].ParameterType.Name -eq 'IAsyncOperation`1' } | Select-Object -First 1
$asTaskAct = $methods | Where-Object { $_.Name -eq 'AsTask' -and $_.GetParameters().Count -eq 1 -and $_.GetParameters()[0].ParameterType.Name -eq 'IAsyncAction' } | Select-Object -First 1

function Await($op, [Type]$t) {
    $task = $asTaskOp.MakeGenericMethod($t).Invoke($null, @($op))
    $task.Wait(-1) | Out-Null
    $task.Result
}
function AwaitAction($op) {
    $task = $asTaskAct.Invoke($null, @($op))
    $task.Wait(-1) | Out-Null
}

$file = Await ([Windows.Storage.StorageFile]::GetFileFromPathAsync($PdfPath)) ([Windows.Storage.StorageFile])
$pdf = Await ([Windows.Data.Pdf.PdfDocument]::LoadFromFileAsync($file)) ([Windows.Data.Pdf.PdfDocument])
"pages: $($pdf.PageCount)"
$pages = Get-PageList $Page ([int]$pdf.PageCount)
$opts = New-Object Windows.Data.Pdf.PdfPageRenderOptions
$opts.DestinationWidth = [uint32]$Width
$folder = Await ([Windows.Storage.StorageFolder]::GetFolderFromPathAsync($OutDir)) ([Windows.Storage.StorageFolder])
foreach ($p in $pages) {
    $name = Get-OutName $OutName $p ($pages.Count -gt 1)
    $pg = $pdf.GetPage([uint32]$p)
    $out = Await ($folder.CreateFileAsync($name, [Windows.Storage.CreationCollisionOption]::ReplaceExisting)) ([Windows.Storage.StorageFile])
    $stream = Await ($out.OpenAsync([Windows.Storage.FileAccessMode]::ReadWrite)) ([Windows.Storage.Streams.IRandomAccessStream])
    AwaitAction ($pg.RenderToStreamAsync($stream, $opts))
    $stream.Dispose()
    'saved {0} (page {1}, {2:0.##} x {3:0.##})' -f $name, $p, $pg.Size.Width, $pg.Size.Height
    $pg.Dispose()
}
Exit-Worker 0
