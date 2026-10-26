# 其他接口（工作区、客户端/服务器、项目、库、FPGA 等）

来源：Altium Designer 23.1.1.15 的 `System\ScriptingSystem.dll`（脚本引擎的注册表，2026-10-25 提取）。由 `scripts/gen_docs.py` 生成，不要手改。

每节列出该接口**自己注册的**成员；继承来的成员在父接口那一节（`继承` 一行给出链）。查某个接口的全部成员（含继承）用 `scripts/lookup.py <接口名>`。
属性写成 `read <getter> write <setter>`，没有 `write` 的是只读属性（行尾 `// read-only`），不要赋值（`IPCB_Board.LayerColor` 赋值实测会卡死执行器）。getter/setter 本身也是注册过的方法，可以直接调用。

## IAbstractSynthesizer
继承：IAbstractSynthesizer → IInterface ｜ 单元：Rt_VHDLSynthesis ｜ 自有 1 个方法、0 个属性

function GetSynthesisConstraintsFileName: WideString;

## IAbstractVHDLProject
继承：IAbstractVHDLProject → IProject → IDMObject → IInterface ｜ 单元：RT_Workspace ｜ 自有 14 个方法、0 个属性

procedure DM_Abort;
function DM_GenerateHDL(Parameters: WideString; ARebuild: LongBool): LongBool;
function DM_GetGeneratedHDLFilenames(ConfigurationName: WideString): WideString;
function DM_GetHarnessDefinitionList: IHarnessDefinitionList;
function DM_GetRequiresHDLGeneration: LongBool;
function DM_GetSchematicNetlister: TSchematicNetlister;
function DM_GetTargetDeviceName(ConfigurationName: WideString): WideString;
function DM_GetVerilog95: LongBool;
function DM_GetVHDL87: LongBool;
function DM_IncludePath(Index: Integer): WideString;
function DM_IncludePathCount: Integer;
function DM_MacroCount: Integer;
function DM_MacroName(Index: Integer): WideString;
function DM_MacroValue(Index: Integer): WideString;

## IAltiumLibrary
继承：IAltiumLibrary → IInterface ｜ 单元：Rt_AltiumLibrary ｜ 自有 5 个方法、1 个属性

property Name: WideString read GetState_Name;  // read-only
function GetAttributes(APath: WideString; const AAttrs: IDispatch; AFields: Int64): LongBool;
function GetState_Name: WideString;
function LoadData(APath: WideString; AStream: IStream): LongBool;
function PathExists(APath: WideString): LongBool;
function SaveData(APath: WideString; AStream: IStream): LongBool;

## IAltiumLibraryManager
继承：IAltiumLibraryManager → IInterface ｜ 单元：Rt_AltiumLibrary ｜ 自有 2 个方法、0 个属性

function FindActivatedAltiumLibraryByFileName(AFileName: WideString): IAltiumLibrary;
function GetDItemRevisionByDesignItemId(ALibIdentifierKind: TLibIdentifierKind; const ALibraryIdentifier: WideString; const ADesignItemId: WideString): IDItemRevision;

## IAltiumPortalNotification
继承：IAltiumPortalNotification → INotification → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 3 个方法、3 个属性

property ApplicationName: WideString read GetApplicationName;  // read-only
property Code: Integer read GetCode;  // read-only
property ParameterList: IInterfaceList read GetParameterList;  // read-only
function GetApplicationName: WideString;
function GetCode: Integer;
function GetParameterList: IInterfaceList;

## IAltiumVHDLSimulatorEngine
继承：IAltiumVHDLSimulatorEngine → IInterface ｜ 单元：Rt_VHDL ｜ 自有 34 个方法、0 个属性

function AddBreakPoint(FileName: PWideChar; LineNumber: Cardinal): Boolean;
procedure AddRegisteredModule(AName: PWideChar);
function AtBreakPoint: Boolean;
procedure DeleteAllBreakpoints;
function DeleteBreakPoint(FileName: PWideChar; LineNumber: Cardinal): Boolean;
function GetCurrentBreakPoint(FileName: PWideChar; var LineNumber: Cardinal): Boolean;
function GetDeltaCount: Integer;
function GetDesignName: PWideChar;
function GetModule(Index: Integer): PWideChar;
function GetModuleCount: Integer;
function GetPercentage: Integer;
function GetStatus: TVHDLStatus;
function GetTimeUnits: PWideChar;
function GetTranscript: IVHDLTranscript;
function GetValidBreakpoint(FileName: PWideChar; Index: Integer): Integer;
function GetValidBreakpointCount(FileName: PWideChar): Integer;
function GetWatch(Index: Integer): ISimWatch;
function GetWatchCount: Integer;
function Load: Boolean;
function Reset: Boolean;
function Run: Boolean;
function RunForever: Boolean;
function RunToBreakpoint(FileName: PWideChar; LineNumber: Cardinal): Boolean;
procedure SetBinFile(ABinFile: PWideChar);
procedure SetLineInput(ALine: PWideChar);
procedure SetLoadDir(AValue: PWideChar);
procedure SetSeverity(AValue: Integer);
procedure SetTimeUnits(ATime: PWideChar);
function StepDebug: Boolean;
function StepDelta: Boolean;
function StepInto: Boolean;
function StepOver: Boolean;
function StepTime: Boolean;
function Stop: Boolean;

## IAnnotationManager
继承：IAnnotationManager → IInterface ｜ 单元：RT_Workspace ｜ 自有 4 个方法、0 个属性

function GetDesignatorRecordCount: Integer;
function GetDesignatorRecords(AIndex: Integer): IDesignatorRecord;
function GetSheetNumberRecordCount: Integer;
function GetSheetNumberRecords(AIndex: Integer): ISheetNumberRecord;

## IAutomaticSheetsNumbers
继承：IAutomaticSheetsNumbers → IInterface ｜ 单元：RT_Workspace ｜ 自有 2 个方法、0 个属性

function GetSheetNumber(SchematicUniqueId: WideString): Integer;
function GetTotalSheetsNumber: Integer;

## IBSDLEntity
继承：IBSDLEntity → IInterface ｜ 单元：Rt_NexusDevices ｜ 自有 32 个方法、0 个属性

function GetBoundaryCell(Index: Integer): IBoundaryCell;
function GetBoundaryCellCount: Integer;
function GetBoundaryLength: Integer;
function GetCompliancePattern: WideString;
function GetConformanceStatement: WideString;
function GetDesignWarning: WideString;
function GetFilename: WideString;
function GetIdCode: Cardinal;
function GetInstruction_BYPASS: Cardinal;
function GetInstruction_CLAMP: Cardinal;
function GetInstruction_EXTEST: Cardinal;
function GetInstruction_HIGHZ: Cardinal;
function GetInstruction_IDCODE: Cardinal;
function GetInstruction_SAMPLE: Cardinal;
function GetInstruction_USERCODE: Cardinal;
function GetInstructionLength: Integer;
function GetInstructionOpcode(Index: Integer): IInstructionOpCode;
function GetInstructionOpcodeCount: Integer;
function GetName: WideString;
function GetPin(Index: Integer): IScanPin;
function GetPin_TCK: IScanPin;
function GetPin_TDI: IScanPin;
function GetPin_TDO: IScanPin;
function GetPin_TMS: IScanPin;
function GetPin_TRST: IScanPin;
function GetPinCount: Integer;
function GetPinMapping(Index: Integer): IPinMapping;
function GetPinMappingCount: Integer;
function GetRegisterAssociation(Index: Integer): IRegisterAssociation;
function GetRegisterAssociationCount: Integer;
function GetScanClockHaltMode: TScanClockHaltMode;
function GetScanClockMaxSpeed: Double;

## IBSDLObject
继承：IBSDLObject → IInterface ｜ 单元：Rt_NexusDevices ｜ 自有 3 个方法、0 个属性

function GetDescription: WideString;
function GetEntity: IBSDLEntity;
function GetShortDescription: WideString;

## IBackForwardNavigator
继承：IBackForwardNavigator → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 4 个方法、2 个属性

property Address: WideString read GetAddress;  // read-only
property Caption: WideString read GetCaption;  // read-only
function GetAddress: WideString;
function GetBackwardHistoryCount: Integer;
function GetCaption: WideString;
function GetForwardHistoryCount: Integer;

## IBaseConfiguration
继承：IBaseConfiguration → IDMObject → IInterface ｜ 单元：RT_Workspace ｜ 自有 2 个方法、0 个属性

function DM_Name: WideString;
procedure DM_SetName(Value: WideString);

## IBaseReport
继承：IBaseReport → IInterface ｜ 单元：RT_Workspace ｜ 自有 9 个方法、0 个属性

function DM_ObjectAdress: Pointer;
procedure EndReport;
procedure EndSection;
procedure EndTable;
procedure StartReport;
procedure StartSection(const SectionName: WideString);
procedure StartTable(const Title: WideString);
procedure StartTableWithHeading(const Title: WideString; const ColumnHeadings: WideString);
function WriteToFile(const Filename: WideString): WideString;

## IBitLevelJTagChannel
继承：IBitLevelJTagChannel → IDeviceChannel → IInterface ｜ 单元：Rt_NexusDevices ｜ 自有 11 个方法、4 个属性

property TCK: Byte read GetTCK write SetTCK;
property TDI: Byte read GetTDI write SetTDI;
property TDO: Byte read GetTDO write SetTDO;
property TMS: Byte read GetTMS write SetTMS;
function BufIO(WData: WideString; WriteOnly: Boolean; Terminate: Boolean): WideString;
function GetTCK: Byte;
function GetTDI: Byte;
function GetTDO: Byte;
function GetTMS: Byte;
procedure Read;
procedure SetTCK(N: Byte);
procedure SetTDI(N: Byte);
procedure SetTDO(N: Byte);
procedure SetTMS(N: Byte);
procedure Write;

## IBitLevelJTagChannel_Hard
继承：IBitLevelJTagChannel_Hard → IBitLevelJTagChannel → IDeviceChannel → IInterface ｜ 单元：Rt_NexusDevices ｜ 自有 0 个方法、0 个属性


## IBlanket
继承：IBlanket → IDMObject → IInterface ｜ 单元：RT_Workspace ｜ 自有 6 个方法、0 个属性

function DM_LineCount: Integer;
function DM_Lines(AIndex: Integer): ILine;
function DM_NetItemCount: Integer;
function DM_NetItems(AIndex: Integer): INetItem;
function DM_SheetSymbolCount: Integer;
function DM_SheetSymbols(AIndex: Integer): ISheetSymbol;

## IBoardProject
继承：IBoardProject → IProject → IDMObject → IInterface ｜ 单元：RT_Workspace ｜ 自有 6 个方法、0 个属性

procedure DM_CleanUpConfigurations;
function DM_GetCustomConfigurations: IInterfaceList;
function DM_GetHarnessDefinitionList: IHarnessDefinitionList;
function DM_GetOrCreateAssemblyConfigurations: IInterfaceList;
function DM_GetOrCreateFabricationConfigurations: IInterfaceList;
function DM_GetOrCreateSourceConfigurations: IInterfaceList;

## IBoundaryCell
继承：IBoundaryCell → IBSDLObject → IInterface ｜ 单元：Rt_NexusDevices ｜ 自有 12 个方法、0 个属性

function GetCellFunction: TCellFunction;
function GetCellKind: TCellKind;
function GetCellNumber: Integer;
function GetControlCell: IBoundaryCell;
function GetControlCellNumber: Integer;
function GetCurrentValue: Integer;
function GetDisableResult: TDisableResult;
function GetDisableValue: TBitValue;
function GetPin: IScanPin;
function GetPortId: WideString;
function GetSafeBit: TBitValue;
function GetTargetCell: IBoundaryCell;

## IBreakpoint
继承：IBreakpoint → IInterface ｜ 单元：RT_Debugger ｜ 自有 9 个方法、4 个属性

property Enabled: Boolean read GetEnabled write SetEnabled;
property FileName: WideString read GetFileName write SetFileName;
property Line: Integer read GetLine write SetLine;
property Valid: Boolean read GetValid write SetValid;
function GetEnabled: Boolean;
function GetFileName: WideString;
function GetLine: Integer;
function GetValid: Boolean;
procedure SetEnabled(anEnabled: Boolean);
procedure SetFileName(aFileName: WideString);
procedure SetFocus;
procedure SetLine(aLine: Integer);
procedure SetValid(aValid: Boolean);

## IBreakpointMonitor
继承：IBreakpointMonitor → IInterface ｜ 单元：RT_Debugger ｜ 自有 6 个方法、0 个属性

procedure Changed(aBreakpoint: IBreakpoint);
procedure EnabledChanged(aBreakpoint: IBreakpoint);
procedure Focused(aBreakpoint: IBreakpoint);
procedure Moved(aBreakpoint: IBreakpoint; OldFileName: WideString; OldLine: Integer);
procedure Remove(aBreakpoint: IBreakpoint);
procedure ValidChanged(aBreakpoint: IBreakpoint);

## IBus
继承：IBus → IDMObject → IInterface ｜ 单元：RT_Workspace ｜ 自有 18 个方法、0 个属性

function DM_BusKind: TBusKind;
function DM_BusName: WideString;
function DM_BusRange1: WideString;
function DM_BusRange2: WideString;
function DM_BusRangeValue1: Integer;
function DM_BusRangeValue2: Integer;
function DM_BusWidth: Integer;
function DM_Electric: TPinElectrical;
function DM_FullBusName: WideString;
function DM_HasItemOnDocument(Document: IDocument): Boolean;
function DM_IsLocal: Boolean;
function DM_RangeDefinedByValue: Boolean;
function DM_Scope: TNetScope;
function DM_SectionCount: Integer;
function DM_Sections(Index: Integer): INet;
function DM_SignalType: WideString;
function DM_WireCount: Integer;
function DM_Wires(Index: Integer): INet;

## ICapabilityList
继承：ICapabilityList → IInterface ｜ 单元：RT_Workspace ｜ 自有 15 个方法、3 个属性

property Capability[i: Integer]: WideString read GetCapability;  // read-only
property Count: Integer read GetCount;  // read-only
property Objects[i: Integer]: IInterface read GetObject;  // read-only
procedure AddFromOther(const aList: ICapabilityList);
procedure AddFromString(const aString: WideString);
procedure AddObject(const aString: WideString; aObject: IInterface);
function Contains(const aCapability: WideString): Boolean;
function ContainsAll(const aCapabilityList: ICapabilityList): Boolean;
function ContainsAny(const aCapabilityList: ICapabilityList): Boolean;
procedure FromOther(const aList: ICapabilityList);
procedure FromString(const aString: WideString);
function GetCapability(i: Integer): WideString;
function GetCount: Integer;
function GetObject(i: Integer): IInterface;
function IsReadOnly: Boolean;
procedure Remove(const aCapability: WideString);
procedure RemoveOthers(const aList: ICapabilityList);
function ToString: WideString;

## ICategorizedServerView
继承：ICategorizedServerView → IServerView → IExternalForm → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 2 个方法、2 个属性

property Category: WideString read GetCategory;  // read-only
property SubCategory: WideString read GetSubCategory;  // read-only
function GetCategory: WideString;
function GetSubCategory: WideString;

## IChangeManager
继承：IChangeManager → IInterface ｜ 单元：RT_Workspace ｜ 自有 32 个方法、2 个属性

property ModificationCount: Integer read GetModificationCount;  // read-only
property SilentMode: Boolean read GetSilentMode write SetSilentMode;
procedure CreateECO_AddMember(const ATargetDocument: IDocument; const AReferenceMember: IDMObject; const AReferenceParent: IDMObject; const ATargetParent: IDMObject);
procedure CreateECO_AddMember_2(const ATargetDocument: IDocument; const AReferenceMember: IDMObject; const AReferenceParent: IDMObject; const ATargetParent: IDMObject; AModificationKind: TModificationKind);
procedure CreateECO_AddObject(const ATargetDocument: IDocument; const AReferenceObject: IDMObject);
procedure CreateECO_AddParameterVariation(const ATargetDocument: IDocument; const AReferenceMember: IDMObject; const AReferenceParent: IDMObject; const ATargetParent: IDMObject);
procedure CreateECO_ChangeComponentParameters(const ATargetDocument: IDocument; AModificationKind: TModificationKind; const AObjectToChange: IDMObject; const AReferenceObject: IDMObject; const AChanges: IInterfaceList);
procedure CreateECO_ChangeComponentVariation(const ATargetDocument: IDocument; AModificationKind: TModificationKind; const AObjectToChange: IDMObject; const AReferenceObject: IDMObject);
procedure CreateECO_ChangeFootprintParameters(const ATargetDocument: IDocument; AModificationKind: TModificationKind; const AObjectToChange: IDMObject; const AReferenceObject: IDMObject; const AAffectedParameters: IInterfaceList);
procedure CreateECO_ChangeObject(const ATargetDocument: IDocument; AModificationKind: TModificationKind; const AObjectToChange: IDMObject; const AReferenceObject: IDMObject);
procedure CreateECO_ChangeParameterVariation(const ATargetDocument: IDocument; AModificationKind: TModificationKind; const AObjectToChange: IDMObject; const AReferenceObject: IDMObject);
procedure CreateECO_RemoveMember(const ATargetDocument: IDocument; const AMemberObject: IDMObject; const AParentObject: IDMObject);
procedure CreateECO_RemoveMember_2(const ATargetDocument: IDocument; const AMemberObject: IDMObject; const AParentObject: IDMObject; AModificationKind: TModificationKind);
procedure CreateECO_RemoveObject(const ATargetDocument: IDocument; const AObjectToRemove: IDMObject);
procedure CreateECO_RemoveParameterVariation(const ATargetDocument: IDocument; const AMemberObject: IDMObject; const AParentObject: IDMObject);
procedure DM_CreateECO_AddMember(const ATargetDocument: IDocument; const AReferenceMember: IDMObject; const AReferenceParent: IDMObject; const ATargetParent: IDMObject);
procedure DM_CreateECO_ChangeObject(const ATargetDocument: IDocument; AModificationKind: TModificationKind; const AObjectToChange: IDMObject; const AReferenceObject: IDMObject);
procedure DM_CreateECO_RemoveMember(const ATargetDocument: IDocument; const AMemberObject: IDMObject; const AParentObject: IDMObject);
procedure DM_CreateECO_SwapPin(const TargetDocument: IDocument; const TargetComponent: IComponent; const TargetPin: INetItem; const NewPinNumber: WideString; const OldPinNet: WideString; const NewPinNet: WideString);
function DM_DoEditProperties: Boolean;
function DM_ExecuteChanges(IsSilent: LongBool): LongBool;
procedure DM_SetIsApply(AValue: Boolean);
procedure DM_SetProject1(const AProject: IProject);
procedure DM_SetProject2(const AProject: IProject);
function DoEditProperties: Boolean;
function ExecuteChanges(IsSilent: LongBool): LongBool;
function GetModification(AIndex: Integer): IModification;
function GetModificationCount: Integer;
function GetSilentMode: Boolean;
function HasPerformedAction: Boolean;
procedure NormalizePinSwaps(const AProject1: IProject; const AProject2: IProject);
function PerformActions: Boolean;
procedure SetIsApply(AValue: Boolean);
procedure SetSilentMode(AValue: Boolean);

## IChangeManagerFactory
继承：IChangeManagerFactory → IInterface ｜ 单元：RT_Workspace ｜ 自有 1 个方法、0 个属性

function CreateChangeManager(const AProject1: IProject; const AProject2: IProject; const AUpdateParamOptions: IUpdateParameterOptions; ADisplayCompilationErrors: Boolean): IChangeManager;

## IChangeNotifier
继承：IChangeNotifier → IInterface ｜ 单元：Vcl.Graphics ｜ 自有 1 个方法、0 个属性

procedure Changed;

## IChannelClass
继承：IChannelClass → IObjectClass → IDMObject → IInterface ｜ 单元：RT_Workspace ｜ 自有 0 个方法、0 个属性


## IClient
继承：IClient → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 137 个方法、24 个属性

property AccessFeaturesInDevelopment: Boolean read GetState_AccessFeaturesInDevelopment;  // read-only
property ApplicationHandle: Integer read GetApplicationHandle;  // read-only
property ClientAPI: IClientAPI_Interface read GetClientAPI;  // read-only
property CommandLauncher: ICommandLauncher read GetCommandLauncher;  // read-only
property Count: Integer read GetCount;  // read-only
property CurrentView: IServerDocumentView read GetCurrentView write SetCurrentView;
property DocumentPreviewHint: IDocumentPreviewHint read GetDocumentPreviewHint;  // read-only
property DocumentPreviewManager: IDocumentPreviewManager read GetDocumentPreviewManager;  // read-only
property DXPAltiumPortal: IDXPAltiumPortal read GetDXPAltiumPortal;  // read-only
property GUIManager: IGUIManager read GetGUIManager;  // read-only
property LabsManager: ILabsManager read GetLabsManager;  // read-only
property MainWindowHandle: HWND read GetMainWindowHandle;  // read-only
property NavigationSystem: INavigationSystem read GetNavigationSystem;  // read-only
property OptionsManager: IOptionsManager read GetOptionsManager;  // read-only
property PluginsRegistry: IPluginsRegistry read GetPluginsRegistry;  // read-only
property ProcessControl: IProcessControl read GetProcessControl;  // read-only
property RibbonManager: IRibbonManager read GetRibbonManager;  // read-only
property SearchManager: ISearchManager read GetSearchManager;  // read-only
property SecurityManager: ISecurityManager read GetSecurityManager;  // read-only
property SecurityServerManager: ISecurityServerManager read GetSecurityServerManager;  // read-only
property ServerModule[Index: Integer]: IServerModule read GetServerModule;  // read-only
property ServerModuleByName[const AModuleName: WideString]: IServerModule read GetServerModuleByName;  // read-only
property TimerManager: ITimerManager read GetTimerManager;  // read-only
property UpdatesManager: IUpdatesManager read GetUpdatesManager;  // read-only
procedure AddServerView(const AView: IServerView);
function AddViewToFavorites(const AView: IServerDocumentView; AIsSnippet: Boolean): Boolean;
procedure ApplicationIdle;
function ArePreferencesReadOnly(const AServerName: WideString; const AFormName: WideString): LongBool;
procedure BeginDisableInterface;
procedure BeginDocumentLoad;
procedure BeginRecoverySave;
procedure BeginTransaction;
procedure BroadcastNotification(ANotification: INotification);
procedure BroadcastNotificationAsynchronously(ANotification: INotification);
procedure ClearMemorySnapshots;
procedure CloseDocument(const ADocument: IServerDocument);
procedure CreateMemoryShapshot(const ASnapshotName: WideString);
procedure DisableServerNotificationHandler(const Handler: IServerModule);
procedure DispatchDocumentNotification(const ServerDocument: IServerDocument; const Notification: INotification);
procedure DispatchNotification(const AServerModule: IServerModule; const ANotification: INotification);
procedure DisplayDocsTogetherForCompare;
procedure DisplaySplashScreen(AImagePath: WideString; AFadeInMillis: Integer; ADisplayMillis: Integer; AFadeOutMillis: Integer; AAlphaStep: Integer);
procedure EndDisableInterface;
procedure EndDocumentLoad(AShow: LongBool);
procedure EndRecoverySave;
procedure EndTransaction;
function GetApplicationHandle: Integer;
function GetClientAPI: IClientAPI_Interface;
function GetCommandLauncher: ICommandLauncher;
function GetCount: Integer;
function GetCurrentView: IServerDocumentView;
function GetDefaultExtensionForDocumentKind(const DocumentKind: WideString): WideString;
function GetDocumentByPath(const AFilePath: WideString): IServerDocument;
function GetDocumentCaptionFromDocumentKind(const ADocumentKind: WideString): WideString;
function GetDocumentCaptionFromDocumentPath(const APath: WideString): WideString;
function GetDocumentKindFromDocumentFileName(const Path: WideString; CheckForTextFiles: Boolean): WideString;
function GetDocumentKindFromDocumentPath(const Path: WideString): WideString;
function GetDocumentKindFromDocumentPathEx(const Path: WideString; var DocSubKind: WideString): WideString;
function GetDocumentPreviewHint: IDocumentPreviewHint;
function GetDocumentPreviewManager: IDocumentPreviewManager;
function GetDotNetObjectInterface(const AModuleName: WideString): IInterface;
function GetDXPAltiumPortal: IDXPAltiumPortal;
function GetDXPSplash: IDXPSplash;
function GetDXPUrlCommandData(const Url: WideString; out Command: WideString; out Params: WideString): Boolean;
function GetDXPWorkspace: IDXPWorkSpace;
function GetDynamicHelpManager: IDynamicHelpManager;
function GetGlobalPreferencesRevisionGUID: WideString;
function GetGlobalPreferencesVaultGUID: WideString;
function GetGUIManager: IGUIManager;
function GetInternalOptions: IInternalOptions;
function GetInternalOptionsManager: IServerInternalOptionsManager;
function GetIsUpdateRequired: Boolean;
function GetLabsManager: ILabsManager;
function GetLayoutSaveLoadManager: ISaveLoadLayout;
function GetLicenseManager: ILicenseManager;
function GetLocalSnippetManager: ILocalSnippetManager;
function GetMacroManager: IMacroManager;
function GetMainWindowHandle: HWND;
function GetNavigationSystem: INavigationSystem;
function GetOptionsManager: IOptionsManager;
function GetOptionsSet(Index: Integer): IDocumentOptionsSet;
function GetOptionsSetByName(const AName: WideString): IDocumentOptionsSet;
function GetOptionsSetCount: Integer;
function GetPanelInfoByName(const APanelName: WideString): IServerPanelInfo;
function GetPluginsRegistry: IPluginsRegistry;
function GetPreferencesChanged: Boolean;
function GetProcessControl: IProcessControl;
function GetProductName: WideString;
function GetProductVersion: WideString;
function GetRealMainWindowHandle: NativeUInt;
function GetRibbonManager: IInterface;
function GetSceneManager: ISceneManager;
function GetSearchManager: ISearchManager;
function GetSecurityManager: ISecurityManager;
function GetSecurityServerManager: ISecurityServerManager;
function GetServerModule(Index: Integer): IServerModule;
function GetServerModuleByName(const AModuleName: WideString): IServerModule;
function GetServerNameByPLID(const APLID: WideString): WideString;
function GetServerRecord(Index: Integer): IServerRecord;
function GetServerRecordByFeature(const AFeature: WideString): IServerRecord;
function GetServerRecordByName(const AModuleName: WideString): IServerRecord;
function GetServerRecordCount: Integer;
function GetServerViewFromName(const ViewName: WideString): IServerView;
function GetStackTraceForLiveObjects(const AServerName: WideString; const AClassName: WideString): IStrings;
function GetState_AccessFeaturesInDevelopment: Boolean;
function GetTechnologySets(var ValidAtTimestamp: Cardinal): WideString;
function GetTechnologySubscriptionExpirationDate(const ATechnologySet: WideString): TDateTime;
function GetTimerManager: ITimerManager;
function GetUpdatesManager: IUpdatesManager;
function GetVersion: WideString;
function GetVersionHelper: IVersionHelper;
function GetWindowKindByName(const AWindowKindName: WideString): IServerWindowKind;
procedure HandleException(const AMessage: WideString);
procedure HideDocument(const ADocument: IServerDocument);
function InRecoverySave: LongBool;
function InTestMode: Boolean;
function InvokeCustomDialog(const DialogName: string; var Params: WideString): Integer;
function IsDocumentOfKind(const Path: WideString; const DocKind: WideString): Boolean;
function IsDocumentOpen(const AFilePath: WideString): LongBool;
function IsInitialized: LongBool;
function IsQuitting: Boolean;
function LastActiveDocumentOfType(const AType: WideString): IServerDocument;
function LicenseInfoStillValid(const RetrievedAt: Cardinal): LongBool;
procedure LoadCustomizationsFromFile(ARCSFileName: WideString);
procedure LoadCustomizationsFromFileByMode(ARCSFileName: WideString; ARemoveAllUserResources: Boolean);
procedure LoadCustomizationsFromPath(ARCSFilePath: WideString);
procedure LoadGlobalPreferencesFromVault(const VaultGuid: WideString; const ItemRevisionGUID: WideString);
procedure LoadPreferencesFromVault(const AVaultGuid: WideString; const AItemRevisionGuid: WideString; AIsSilent: Boolean);
function OpenDocument(const AKind: WideString; const AFileName: WideString): IServerDocument;
function OpenDocumentShowOrHide(const AKind: WideString; const AFileName: WideString; AShowInTree: Boolean): IServerDocument;
function OpenNewDocument(const AKind: WideString; const AFileName: WideString; const ANewName: WideString; ReuseExisting: Boolean): IServerDocument;
procedure PreloadImage(const AFileName: WideString);
procedure PreparePreferencesToRelease(const AFileName: WideString; out AFolderName: WideString);
function ProductInfo: IProductInfo;
procedure QuerySystemFont(QueryMode: TFontQueryMode; var AUseSysFont: Boolean; var AFontName: WideString; var AFontSize: Integer; var AFontStyle: TFontStyles; var AFontColor: TColor; var AFontCharset: TFontCharset);
procedure RegisterCustomDialog(const DialogName: string; Dialog: ICustomDialog);
procedure RegisterCustomDialogIfNotExists(const DialogName: string; Dialog: ICustomDialog);
procedure RegisterDocumentNotificationHandler(const ServerDocument: IServerDocument; const Handler: INotificationHandler; const NotificationFilter: WideString);
procedure RegisterDotNetObjectInterface(const AModuleName: WideString; const AInterface: IInterface);
procedure RegisterFilteredNotificationHandler(const Handler: INotificationHandler; const NotificationFilter: WideString);
procedure RegisterNotificationHandler(const Handler: INotificationHandler);
procedure RegisterServerNotificationHandler(const ServerModule: IServerModule; const Handler: INotificationHandler; const NotificationFilter: WideString);
procedure ReleaseGlobalPreferencesToVault(const VaultGuid: WideString; const ItemGUID: WideString);
procedure RemoveServerView(const AView: IServerView);
function SaveCustomizationsForExport: WideString;
procedure SetCurrentView(const Value: IServerDocumentView);
procedure SetIsUpdateRequired(AValue: Boolean);
procedure SetPreferencesChanged(Value: Boolean);
procedure ShowDocument(const ADocument: IServerDocument);
procedure ShowDocumentDontFocus(const ADocument: IServerDocument);
procedure ShowMemoryReport;
procedure ShowMemorySnapshotDifference(const ASnapshotName: WideString);
function StartServer(const AModuleName: WideString): Boolean;
procedure StartStackTraceCollection(const AClassName: WideString);
procedure StartSuspendTestMode;
function StopServer(const AModuleName: WideString; UnloadDLL: Boolean): Boolean;
procedure StopStackTraceCollection(const AClassName: WideString);
procedure StopSuspendTestMode;
procedure UnregisterDocumentNotificationHandler(const ServerDocument: IServerDocument; const Handler: INotificationHandler);
procedure UnregisterNotificationHandler(const Handler: INotificationHandler);
procedure UnregisterServerNotificationHandler(const ServerModule: IServerModule; const Handler: INotificationHandler);

## IClientAPI_Interface
继承：IClientAPI_Interface → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 199 个方法、0 个属性

procedure AddShutdownMessage(S: WideString);
procedure AddStartupMessage(S: WideString);
procedure BeginExceptionHandling;
procedure CheckSynchronize;
procedure ClearErrorInfo;
function ConvertFileNameToExeFileName(Name: WideString): WideString;
function ConvertFileNameToWildCard(Path: WideString): WideString;
procedure EndCursor;
procedure EndExceptionHandling;
procedure EraseFile(FName: WideString);
function ExistSpecific(FileName: WideString): Boolean;
function ExtractFileDirFromPath(Path: WideString): WideString;
function ExtractFileExtFromPath(Path: WideString): WideString;
function ExtractFileNameFromPath(Path: WideString): WideString;
function ExtractWholeFileNameFromPath(Path: WideString): WideString;
function FilePathInShort(Path: WideString): WideString;
function ForceFileNameExtension(Name: WideString; Ext: WideString): WideString;
function GetActivateLastActiveOnClose: Boolean;
function GetAlwaysShowNavBarInTasks: Boolean;
function GetAnalyticsMonitor: IAnalyticsMonitor;
function GetAutoHideDocumentsBar: Boolean;
function GetAutoShowComponentSymbols: Boolean;
function GetBuiltInNavigationBar: Boolean;
function GetContractedEnvironmentPath(Path: WideString): WideString;
function GetCurrentInstallationUniqueID: WideString;
function GetCurrentOutputGenerator: IInterface;
function GetCurrentProductFullBuild: WideString;
function GetDialogsSizeRegKeyName: WideString;
function GetDpiScalingSuffix: WideString;
function GetDxpNavigator: IDXPNavigator;
function GetEqualButtonsInDocumentsBar: Boolean;
function GetExpandedEnvironmentPath(Path: WideString): WideString;
function GetFavoritesThumbnailSize: IDispatch;
function GetFeatureChecker: IFeatureChecker;
function GetFileSize(FName: WideString): Integer;
function GetGroupingInDocumentsBar: TDocumentsBarGrouping;
function GetHelpTopic(const AHelpTopicID: WideString; out HelpTopicName: WideString): Boolean;
function GetIntegratedHelpSystem: Boolean;
function GetInternalOptions: IInternalOptions;
function GetLogManager: ILogManager;
function GetMiddleClickClosesDocumentTab: Boolean;
function GetMultilineDocumentsBar: Boolean;
function GetNetworkActivityMonitor: INetworkActivityMonitor;
function GetOptionsManager: IOptionsManager;
function GetPrefAnimatedPanels: Boolean;
function GetPrefAnimationSpeed: Integer;
function GetPrefAutoTransparency: Boolean;
function GetPrefConnectivityInsightClickPreview: Boolean;
function GetPrefConnectivityInsightClickTextHint: Boolean;
function GetPrefConnectivityInsightClickTree: Boolean;
function GetPrefConnectivityInsightHoverDelay: Integer;
function GetPrefConnectivityInsightHoverPreview: Boolean;
function GetPrefConnectivityInsightHoverTextHint: Boolean;
function GetPrefConnectivityInsightHoverTree: Boolean;
function GetPrefDynamicAutoTransparency: Boolean;
function GetPrefEnableConnectivityInsight: Boolean;
function GetPrefEnableDocumentInsight: Boolean;
function GetPrefEnableHyperlinkInsight: Boolean;
function GetPrefEnableProjectInsight: Boolean;
function GetPrefEnableSupplyChainInsight: Boolean;
function GetPrefHideBinderViewTabs: Boolean;
function GetPrefHideDelay: Integer;
function GetPrefHideFloatingPanels: Boolean;
function GetPrefHyperlinkInsightClickEnabled: Boolean;
function GetPrefHyperlinkInsightHoverEnabled: Boolean;
function GetPrefNoRestoreKind(Index: Integer): WideString;
function GetPrefNoRestoreKindCount: Integer;
function GetPrefOpenTasksIfNothingOpen: Boolean;
function GetPrefPathInTitleBar: Boolean;
function GetPrefPopupDelay: Integer;
function GetPrefRememberFormForDocKind: Boolean;
function GetPrefRestoreOpenDocuments: Boolean;
function GetPrefSaveToolsLayout: Boolean;
function GetPrefSuppressStartupScreen: Boolean;
function GetPrefTransparencyForce: Integer;
function GetPrefTransparencyHighest: Integer;
function GetPrefTransparencyLowest: Integer;
function GetPrefUseLuna: Boolean;
function GetPrefUseShadow: Boolean;
function GetPrevSettings_SpecialFolder_AltiumApplicationData(AIndex: Integer): WideString;
function GetPrevSettings_SpecialKey_SoftwareAltiumAppDXP(AIndex: Integer): WideString;
function GetRecentLayout(AIndex: Integer): WideString;
function GetRecentLayoutCount: Integer;
function GetReloadDocumentsModifiedOutside: TConfirmationOption;
function GetResourceMonitor: IResourceMonitor;
function GetServerName(const ADllName: WideString; out ServerName: WideString): Boolean;
function GetStringFromFile(FileName: WideString; UserID: WideString): WideString;
function GetTranslationManager: ITranslationManager;
function GetUIDialogManager: IUIDialogManager;
function GetUseExternalWebBrowser: Boolean;
function GetUseLocalizedDialogs: Boolean;
function GetUseLocalizedResources: Boolean;
function GetUseSystemLocaleLanguage: Boolean;
function GetVSStyleCtrlTab: Boolean;
function GetWin7TaskbarJumpLists: Boolean;
function GetWin7TaskbarProgress: Boolean;
function GetWin7TaskbarThumbnails: Boolean;
procedure HandleException(const Message: WideString);
procedure HideProductStartup;
function IsAltiumViewer: Boolean;
function IsErrorInfoSet: WordBool;
function IsFileReadOnly(S: WideString): Boolean;
procedure MakeNewBackUp(FileName: WideString);
function RemoveModuleFromMemory(S: WideString): Integer;
procedure RemoveSynchronize(const ASync: IThreadSynchronize);
function SameFileName(S1: WideString; S2: WideString; MatchFileNameKind: TMatchFileNameKind): Boolean;
procedure SetActivateLastActiveOnClose(Value: Boolean);
procedure SetAlwaysShowNavBarInTasks(Value: Boolean);
procedure SetAutoHideDocumentsBar(Value: Boolean);
procedure SetAutoShowComponentSymbols(Value: Boolean);
procedure SetBuiltInNavigationBar(Value: Boolean);
procedure SetCurrentOutputGenerator(const Generator: IInterface);
procedure SetEqualButtonsInDocumentsBar(Value: Boolean);
procedure SetErrorInfo(const ErrorMsg: WideString; const ErrorReport: WideString; ErrorAddr: Int64);
procedure SetFavoritesThumbnailSize(const Value: IDispatch);
procedure SetFileFromString(FileName: WideString; UserID: WideString; Data: WideString);
procedure SetGroupingInDocumentsBar(Value: TDocumentsBarGrouping);
procedure SetIntegratedHelpSystem(Value: Boolean);
procedure SetMiddleClickClosesDocumentTab(Value: Boolean);
procedure SetMultilineDocumentsBar(Value: Boolean);
procedure SetPrefAnimatedPanels(Value: Boolean);
procedure SetPrefAnimationSpeed(Value: Integer);
procedure SetPrefAutoTransparency(Value: Boolean);
procedure SetPrefConnectivityInsightClickPreview(Value: Boolean);
procedure SetPrefConnectivityInsightClickTextHint(Value: Boolean);
procedure SetPrefConnectivityInsightClickTree(Value: Boolean);
procedure SetPrefConnectivityInsightHoverDelay(Value: Integer);
procedure SetPrefConnectivityInsightHoverPreview(Value: Boolean);
procedure SetPrefConnectivityInsightHoverTextHint(Value: Boolean);
procedure SetPrefConnectivityInsightHoverTree(Value: Boolean);
procedure SetPrefDynamicAutoTransparency(Value: Boolean);
procedure SetPrefEnableConnectivityInsight(Value: Boolean);
procedure SetPrefEnableDocumentInsight(Value: Boolean);
procedure SetPrefEnableHyperlinkInsight(Value: Boolean);
procedure SetPrefEnableProjectInsight(Value: Boolean);
procedure SetPrefEnableSupplyChainInsight(Value: Boolean);
procedure SetPrefHideBinderViewTabs(Value: Boolean);
procedure SetPrefHideDelay(Value: Integer);
procedure SetPrefHideFloatingPanels(Value: Boolean);
procedure SetPrefHyperlinkInsightClickEnabled(Value: Boolean);
procedure SetPrefHyperlinkInsightHoverEnabled(Value: Boolean);
procedure SetPrefNoRestoreKindAdd(Value: WideString);
procedure SetPrefNoRestoreKindClear;
procedure SetPrefOpenTasksIfNothingOpen(Value: Boolean);
procedure SetPrefPathInTitleBar(Value: Boolean);
procedure SetPrefPopupDelay(Value: Integer);
procedure SetPrefRememberFormForDocKind(Value: Boolean);
procedure SetPrefRestoreOpenDocuments(Value: Boolean);
procedure SetPrefSaveToolsLayout(Value: Boolean);
procedure SetPrefSuppressStartupScreen(Value: Boolean);
procedure SetPrefTransparencyForce(Value: Integer);
procedure SetPrefTransparencyHighest(Value: Integer);
procedure SetPrefTransparencyLowest(Value: Integer);
procedure SetPrefUseLuna(Value: Boolean);
procedure SetPrefUseShadow(Value: Boolean);
procedure SetReloadDocumentsModifiedOutside(Value: TConfirmationOption);
procedure SetSoftErrorInfo(const ErrorMsg: WideString);
procedure SetUIDialogManager(const Value: IUIDialogManager);
procedure SetUseExternalWebBrowser(Value: Boolean);
procedure SetUseLocalizedDialogs(Value: Boolean);
procedure SetUseLocalizedResources(Value: Boolean);
procedure SetUseSystemLocaleLanguage(Value: Boolean);
procedure SetVSStyleCtrlTab(Value: Boolean);
procedure SetWin7TaskbarJumpLists(Value: Boolean);
procedure SetWin7TaskbarProgress(Value: Boolean);
procedure SetWin7TaskbarThumbnails(Value: Boolean);
procedure ShowHelpTopic(ATopicName: WideString);
procedure ShowProductStartup(aBitmap: WideString);
function SpecialFolder_AllUserDocuments: WideString;
function SpecialFolder_AltiumAllUserApplicationData: WideString;
function SpecialFolder_AltiumAllUserDocuments: WideString;
function SpecialFolder_AltiumApplicationData: WideString;
function SpecialFolder_AltiumConstraintFiles: WideString;
function SpecialFolder_AltiumDesignExplorer: WideString;
function SpecialFolder_AltiumEmbeddedConstraintFiles: WideString;
function SpecialFolder_AltiumExtensions: WideString;
function SpecialFolder_AltiumHelp: WideString;
function SpecialFolder_AltiumLibrary: WideString;
function SpecialFolder_AltiumLibraryEDIF: WideString;
function SpecialFolder_AltiumLocalApplicationData: WideString;
function SpecialFolder_AltiumLocalHelp: WideString;
function SpecialFolder_AltiumSecurityAllUserApplicationData: WideString;
function SpecialFolder_AltiumSystem: WideString;
function SpecialFolder_AltiumSystemButtons: WideString;
function SpecialFolder_AltiumSystemDocumentImages: WideString;
function SpecialFolder_AltiumSystemLibrary: WideString;
function SpecialFolder_AltiumSystemTemplates: WideString;
function SpecialFolder_AltiumSystemWizardImages: WideString;
function SpecialFolder_AltiumTaskingApplicationData: WideString;
function SpecialFolder_CommonDocumnetTemplates: WideString;
function SpecialFolder_DesignTemplates: WideString;
function SpecialFolder_ExportPreferences: WideString;
function SpecialFolder_MyDesigns: WideString;
function SpecialFolder_MyDocuments: WideString;
function SpecialFolder_TemplatesForAllUsers: WideString;
function SpecialKey_SoftwareAltiumApp: WideString;
function SpecialKey_SoftwareAltiumAppDXP: WideString;
procedure Synchronize(const ASync: IThreadSynchronize);
function UpdateFont(const Font: IDispatch): LongBool;

## IClientAPI_Interface2
继承：IClientAPI_Interface2 → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 3 个方法、0 个属性

function GetLastErrorMessage: WideString;
function GetLastErrorReport: WideString;
function GetProfilerManager: IProfilerManager;

## IClientWebSocket
继承：IClientWebSocket → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 7 个方法、2 个属性

property CanReceiveOrSend: Boolean read GetCanReceiveOrSend;  // read-only
property FullDataProcess: Boolean read GetFullDataProcess write SetFullDataProcess;
procedure Close(ACloseCode: Integer; const ACloseReason: WideString);
function GetCanReceiveOrSend: Boolean;
function GetFullDataProcess: Boolean;
procedure Send(const AMessage: WideString);
procedure SetCallBackManager(const ACallBackManager: IClientWebSocketCallBackManager);
procedure SetFullDataProcess(AValue: Boolean);
procedure Start;

## IClientWebSocketCallBackManager
继承：IClientWebSocketCallBackManager → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 5 个方法、0 个属性

procedure HandleOnClose(ACloseCode: Integer; const ACloseReason: WideString; AIsTerminated: Boolean);
procedure HandleOnOpen;
procedure HandleOnRead(const AData: WideString);
procedure HandleOnTimeout;
procedure ResetHandlers;

## IClientWebSocketFactory
继承：IClientWebSocketFactory → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 1 个方法、0 个属性

function GetNewClientWebSocketProvider(const AClient: IClient; const aURI: WideString; const ASessionId: WideString; const AClientId: WideString; const ACallBackManager: IClientWebSocketCallBackManager): IClientWebSocket;

## IClientsStack
继承：IClientsStack → IInterface ｜ 单元：RT_Workspace ｜ 自有 6 个方法、0 个属性

function NewCompilationEnabled: Boolean;
function NewCompilationEnabledOnlyFor(Clients: TUdmClientsSet): Boolean;
function ObjectProviderFor(ClientId: TUdmClient): IObjectsProviderSetter;
procedure PopClient(ClientId: TUdmClient);
procedure PushClient(ClientId: TUdmClient);
procedure ReloadCache;

## IClipboardDocument
继承：IClipboardDocument → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 3 个方法、0 个属性

function Clipboard_GetFormat(Index: Integer): Cardinal;
function Clipboard_GetFormatCount: Integer;
function Clipboard_PasteFormat(Format: Cardinal): LongBool;

## IClockCore
继承：IClockCore → IInterface ｜ 单元：Rt_NexusDevices ｜ 自有 1 个方法、0 个属性

function FindClockConstraintByName(const AName: WideString): IClockModifierData;

## IClockCoreGenerator
继承：IClockCoreGenerator → IInterface ｜ 单元：Rt_NexusDevices ｜ 自有 1 个方法、0 个属性

function ValidateConfig(const AClockCore: IClockCore): LongBool;

## IClockCoreTemplate
继承：IClockCoreTemplate → IInterface ｜ 单元：Rt_NexusDevices ｜ 自有 10 个方法、0 个属性

procedure AddCustomVars;
function InternalActual(Index: Integer): IClockOutputActual;
function InternalActualCount: Integer;
function OutputActual(Index: Integer): IClockOutputActual;
function OutputActualCount: Integer;
function TargetInput(Index: Integer): IClockModifierTarget;
function TargetInputCount: Integer;
function TargetOutput(Index: Integer): IClockModifierTarget;
function TargetOutputCount: Integer;
procedure VarAdd(const AName: WideString; AIncludeIf: LongBool; const AReplaceWith: WideString);

## IClockCoreTemplateGenerator
继承：IClockCoreTemplateGenerator → IInterface ｜ 单元：Rt_NexusDevices ｜ 自有 1 个方法、0 个属性

function PreProcess(const AClockCoreTemplate: IClockCoreTemplate): LongBool;

## IClockModifierData
继承：IClockModifierData → IInterface ｜ 单元：Rt_NexusDevices ｜ 自有 9 个方法、9 个属性

property CurDiv: Double read GetCurDiv;  // read-only
property CurMul: Double read GetCurMul;  // read-only
property CurPhase: Double read GetCurPhase;  // read-only
property InFreq: Double read GetInFreq;  // read-only
property InPhase: Double read GetInPhase;  // read-only
property Name: WideString read GetName;  // read-only
property OutFreq: Double read GetOutFreq;  // read-only
property OutPhase: Double read GetOutPhase;  // read-only
property Score: Double read GetScore;  // read-only
function GetCurDiv: Double;
function GetCurMul: Double;
function GetCurPhase: Double;
function GetInFreq: Double;
function GetInPhase: Double;
function GetName: WideString;
function GetOutFreq: Double;
function GetOutPhase: Double;
function GetScore: Double;

## IClockModifierTarget
继承：IClockModifierTarget → IInterface ｜ 单元：Rt_NexusDevices ｜ 自有 9 个方法、9 个属性

property FreqMax: Double read GetFreqMax;  // read-only
property FreqMin: Double read GetFreqMin;  // read-only
property FreqStep: Double read GetFreqStep;  // read-only
property Ignore: LongBool read GetIgnore;  // read-only
property Last: LongBool read GetLast;  // read-only
property Name: WideString read GetName;  // read-only
property Outputs: LongWord read GetOutputs;  // read-only
property Phase: Double read GetPhase;  // read-only
property PostDivider: Double read GetPostDivider;  // read-only
function GetFreqMax: Double;
function GetFreqMin: Double;
function GetFreqStep: Double;
function GetIgnore: LongBool;
function GetLast: LongBool;
function GetName: WideString;
function GetOutputs: Cardinal;
function GetPhase: Double;
function GetPostDivider: Double;

## IClockOutputActual
继承：IClockOutputActual → IInterface ｜ 单元：Rt_NexusDevices ｜ 自有 6 个方法、6 个属性

property Divider: Double read GetDivider;  // read-only
property Multipler: Double read GetMultipler;  // read-only
property Name: WideString read GetName;  // read-only
property OutFreq: Double read GetOutFreq;  // read-only
property OutPhase: Double read GetOutPhase;  // read-only
property OutputMap: Integer read GetOutputMap;  // read-only
function GetDivider: Double;
function GetMultipler: Double;
function GetName: WideString;
function GetOutFreq: Double;
function GetOutPhase: Double;
function GetOutputMap: Integer;

## ICommandGetState
继承：ICommandGetState → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 1 个方法、0 个属性

procedure GetState(AProcess: PWideChar; AParameters: PWideChar; const AContext: IServerDocumentView; var Enabled: LongBool; var Checked: LongBool; var Visible: LongBool; Caption: PWideChar; ImageFile: PWideChar);

## ICommandLauncher
继承：ICommandLauncher → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 2 个方法、0 个属性

procedure GetCommandState(ACommandName: PWideChar; AParameters: PWideChar; const AContext: IServerDocumentView; var Enabled: LongBool; var Checked: LongBool; var Visible: LongBool; Caption: PWideChar; ImageFile: PWideChar);
procedure LaunchCommand(ACommandName: PWideChar; AParameters: PWideChar; MaxParameterSize: Integer; const AContext: IServerDocumentView);

## ICommentedDocument
继承：ICommentedDocument → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 8 个方法、0 个属性

procedure AddCommentThread(const ACommentThread: IEDMS_CommentThreadHolder);
procedure ClearCommentThreads;
function GetActiveCommentThread: IEDMS_CommentThreadHolder;
function GetCommentThread(const AIndex: Integer): IEDMS_CommentThreadHolder;
function GetCommentThreadByGUID(const AThreadGUID: WideString): IEDMS_CommentThreadHolder;
function GetCommentThreadsCount: Integer;
function SelectCommentThread(const ACommentThread: IEDMS_CommentThreadHolder): Boolean;
procedure SetActiveCommentThread(const ACommentThread: IEDMS_CommentThreadHolder);

## IComponent
继承：IComponent → IPart → IDMObject → IInterface ｜ 单元：RT_Workspace ｜ 自有 12 个方法、0 个属性

procedure DM_DoCrossProbe;
procedure DM_IncrementallyUpdatePhysicalDesignators(NewHasDesignatorRecord: LongBool; NewDesignatorLocked: LongBool; NewPhysicalDesignator: WideString);
function DM_NexusDeviceId: WideString;
function DM_PhysicalComponentCount: Integer;
function DM_PhysicalComponents(Index: Integer): IComponent;
function DM_PhysicalPath: WideString;
function DM_SubPartCount: Integer;
function DM_SubParts(Index: Integer): IPart;
function DM_UniqueId: WideString;
function DM_UniqueIdFromFlatComponent: WideString;
function DM_UniqueIdName: WideString;
function DM_UniqueIdPath: WideString;

## IComponentClass
继承：IComponentClass → IObjectClass → IDMObject → IInterface ｜ 单元：RT_Workspace ｜ 自有 0 个方法、0 个属性


## IComponentConfigurator
继承：IComponentConfigurator → IInterface ｜ 单元：RT_ComponentConfigurator ｜ 自有 16 个方法、1 个属性

property ConfiguratorName: WideString read GetState_ConfiguratorName;  // read-only
function AreConfigurableParametersEquivalent(AEncodedParamString: WideString; BEncodedParamString: WideString): Boolean;
function ConfigureComponent(const ASchComponent: ISch_Component): Boolean;
function ConfigureComponentParametrically(const ASchComponent: ISch_Component; const AParamString: WideString): Boolean;
function GenerateNetlist(const AParameters: WideString; const AFileName: WideString): Boolean;
function GenerateReport(const ASchComponent: ISch_Component): WideString;
function GenerateSoftwareCode(const AInstanceName: WideString; const AConfigurationValues: WideString; AHeaderFile: IEmbeddedCode; ASourceFile: IEmbeddedCode): Boolean;
function GetConfigurationValues(const ASchComponent: ISch_Component): WideString;
function GetParameters(const ASchComponent: ISch_Component): WideString;
function GetParametersFromPart(const APart: IPart): WideString;
function GetState_ConfiguratorName: WideString;
procedure Import_FromDialog(var AEncodedParamString: WideString);
function IsChildCoreUsed(const AChildCoreName: WideString; const ASchComponent: ISch_Component): Boolean;
function IsChildCoreUsedByPart(const AChildCoreName: WideString; const APart: IPart): Boolean;
function IsVerilogSupported: Boolean;
procedure SetConfigurationParametersToDefault(const ASchComponent: ISch_Component);
function UpdateSymbol(const ASchComponent: ISch_Component): Boolean;

## IComponentImplementation
继承：IComponentImplementation → IDMObject → IInterface ｜ 单元：RT_Workspace ｜ 自有 22 个方法、0 个属性

function DM_DatafileCount: Integer;
function DM_DatafileEntity(Index: Integer): WideString;
function DM_DatafileFullPath(Index: Integer; EntityName: WideString; FileKind: WideString; var FoundIn: WideString): WideString;
function DM_DatafileKind(Index: Integer): WideString;
function DM_DatafileLibIdentifierKind(Index: Integer): TLibIdentifierKind;
function DM_DatafileLibraryIdentifier(Index: Integer): WideString;
function DM_DatafileLocation(Index: Integer): WideString;
function DM_DatalinksLocked: Boolean;
function DM_Description: WideString;
function DM_IntegratedModel: Boolean;
function DM_IsCurrent: Boolean;
function DM_ModelName: WideString;
function DM_ModelType: WideString;
function DM_Part: IPart;
function DM_PortMap: WideString;
function DM_PortMapList: WideString;
procedure DM_SetDatafileCount(ACount: Integer);
procedure DM_SetDatafileEntity(Index: Integer; AEntity: WideString);
procedure DM_SetDatafileKind(Index: Integer; AKind: WideString);
procedure DM_SetDatafileLocation(Index: Integer; ALocation: WideString);
procedure DM_SetUseComponentLibrary(AValue: Boolean);
function DM_UseComponentLibrary: Boolean;

## IComponentLibraryLink
继承：IComponentLibraryLink → IInterface ｜ 单元：RT_Workspace ｜ 自有 33 个方法、0 个属性

function DM_AsDisplayString: WideString;
function DM_DatabaseTableName: WideString;
function DM_DesignItemID: WideString;
function DM_Equal(const AnotherLink: IComponentLibraryLink): LongBool;
function DM_Footprint: WideString;
function DM_IsCompatibleFootprint(const AFootprintName: WideString): Boolean;
function DM_IsLinkedToVault: LongBool;
function DM_IsSameFootprint: LongBool;
function DM_IsValid: LongBool;
function DM_ItemGUID: WideString;
function DM_LibIdentifierKind: TLibIdentifierKind;
function DM_LibraryIdentifier: WideString;
function DM_RevisionGUID: WideString;
procedure DM_SetDatabaseTableName(const AValue: WideString);
procedure DM_SetDesignItemID(const AValue: WideString);
procedure DM_SetFootprint(const AValue: WideString);
procedure DM_SetIsSameFootprint(const AValue: LongBool);
procedure DM_SetItemGUID(const AValue: WideString);
procedure DM_SetLibIdentifierKind(const AValue: TLibIdentifierKind);
procedure DM_SetLibraryIdentifier(const AValue: WideString);
procedure DM_SetRevisionGUID(const AValue: WideString);
procedure DM_SetSourceLibraryName(const AValue: WideString);
procedure DM_SetState_Component(const AComponent: IPart);
procedure DM_SetState_Default;
procedure DM_SetSymbolReference(const AValue: WideString);
procedure DM_SetUseDBTableName(const AValue: LongBool);
procedure DM_SetUseLibraryName(const AValue: LongBool);
procedure DM_SetVaultGUID(const AValue: WideString);
function DM_SourceLibraryName: WideString;
function DM_SymbolReference: WideString;
function DM_UseDBTableName: LongBool;
function DM_UseLibraryName: LongBool;
function DM_VaultGUID: WideString;

## IComponentMappings
继承：IComponentMappings → IDMObject → IInterface ｜ 单元：RT_Workspace ｜ 自有 7 个方法、0 个属性

function DM_MatchedComponentCount: Integer;
function DM_MatchedSourceComponent(Index: Integer): IComponent;
function DM_MatchedTargetComponent(Index: Integer): IComponent;
function DM_UnmatchedSourceComponent(Index: Integer): IComponent;
function DM_UnmatchedSourceComponentCount: Integer;
function DM_UnmatchedTargetComponent(Index: Integer): IComponent;
function DM_UnmatchedTargetComponentCount: Integer;

## IComponentVariation
继承：IComponentVariation → IDMObject → IInterface ｜ 单元：RT_Workspace ｜ 自有 20 个方法、0 个属性

function DM_AddParameterVariation: IParameterVariation;
function DM_AlternateLibraryLink: IComponentLibraryLink;
function DM_AlternatePart: WideString;
function DM_CalculatedAlternatePart(const Component: IComponent): WideString;
function DM_EditAlternateLibraryLink(const ASchComponent: IInterface): LongBool;
function DM_FindParameterVariation(const AName: WideString): IParameterVariation;
function DM_PhysicalDesignator: WideString;
function DM_ProjectVariant: IProjectVariant;
function DM_ReferenceGroupOption: WideString;
procedure DM_RemoveParameterVariation(Index: Integer);
procedure DM_SetAlternatePart(const Value: WideString);
procedure DM_SetPhysicalDesignator(const Value: WideString);
procedure DM_SetReferenceGroupOption(const Id: WideString);
procedure DM_SetUniqueId(const Value: WideString);
procedure DM_SetVariationKind(const Value: TVariationKind);
procedure DM_SetVariationKindWithNoCompilation(const Value: TVariationKind);
function DM_UniqueId: WideString;
function DM_VariationCount: Integer;
function DM_VariationKind: TVariationKind;
function DM_Variations(Index: Integer): IParameterVariation;

## IConfiguration
继承：IConfiguration → IBaseConfiguration → IDMObject → IInterface ｜ 单元：RT_Workspace ｜ 自有 6 个方法、0 个属性

procedure DM_AddConstraintFile(AConstraintFilePath: WideString);
function DM_ConstraintGroupCount: Integer;
function DM_ConstraintGroups(Index: Integer): IConstraintGroup;
function DM_ConstraintsFileCount: Integer;
function DM_ConstraintsFilePath(Index: Integer): WideString;
function DM_GetTargetDeviceName: WideString;

## IConfigurationReleaseManager
继承：IConfigurationReleaseManager → IInterface ｜ 单元：RT_Workspace ｜ 自有 1 个方法、0 个属性

function DM_CurrentConfiguration: IVaultConfiguration;

## IConfiguratorManager
继承：IConfiguratorManager → IInterface ｜ 单元：RT_ComponentConfigurator ｜ 自有 0 个方法、0 个属性


## IConfiguratorTest
继承：IConfiguratorTest → IInterface ｜ 单元：RT_ComponentConfigurator ｜ 自有 1 个方法、0 个属性

function RunCommand(Parameters: TStringList): Boolean;

## IConstraint
继承：IConstraint → IDMObject → IInterface ｜ 单元：RT_Workspace ｜ 自有 2 个方法、0 个属性

function DM_Data: WideString;
function DM_Kind: WideString;

## IConstraintGroup
继承：IConstraintGroup → IDMObject → IInterface ｜ 单元：RT_Workspace ｜ 自有 6 个方法、0 个属性

function DM_ConstraintCount: Integer;
function DM_Constraints(Index: Integer): IConstraint;
function DM_SourceId: WideString;
function DM_SourceKindString: WideString;
function DM_TargetId: WideString;
function DM_TargetKindString: WideString;

## IContextServerView
继承：IContextServerView → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 1 个方法、0 个属性

function SupportsContext(const ADocumentKind: WideString; const AProjectKind: WideString): Boolean;

## IControlValueObserver
继承：IControlValueObserver → IInterface ｜ 单元：System.Classes ｜ 自有 2 个方法、0 个属性

procedure ValueModified;
procedure ValueUpdate;

## ICookieSetter
继承：ICookieSetter → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 3 个方法、0 个属性

procedure ClearCookies;
function SetCookie(const AURL: WideString; const AName: WideString; const AValue: WideString; AIsSecure: LongBool; AIsHttpOnly: LongBool; AIsSession: LongBool; AExpiry: Int64): LongBool;
procedure SetCookies(const AURL: WideString; const ACookies: WideString);

## ICoreGenerator
继承：ICoreGenerator → IInterface ｜ 单元：Rt_CoreGenerator ｜ 自有 1 个方法、0 个属性

function GenerateModule(Params: WideString): LongBool;

## ICoreProject
继承：ICoreProject → IAbstractVHDLProject → IProject → IDMObject → IInterface ｜ 单元：RT_Workspace ｜ 自有 2 个方法、0 个属性

function DM_CreateSymbolGenerator: ISymbolGenerator;
function DM_GetIncludeModelsInArchive: LongBool;

## ICrossSheet
继承：ICrossSheet → INetItem → IDMObject → IInterface ｜ 单元：RT_Workspace ｜ 自有 0 个方法、0 个属性


## ICrosspointSwitchInstrument
继承：ICrosspointSwitchInstrument → IScriptedInstrument → IInterface ｜ 单元：RT_CrosspointSwitch ｜ 自有 12 个方法、0 个属性

function AddConnection(const AInputName: WideString; const AOutputName: WideString): LongBool;
procedure BeginReconnect;
function ConnectionExists(const AInputName: WideString; const AOutputName: WideString): LongBool;
procedure EndReconnect;
procedure GetConnection(Index: Integer; var AInputName: WideString; var AOutputName: WideString);
function GetConnectionCount: Integer;
function GetInputCount: Integer;
function GetInputName(Index: Integer): WideString;
function GetOutputCount: Integer;
function GetOutputName(Index: Integer): WideString;
function IsSynchronized: LongBool;
function RemoveConnection(const AInputName: WideString; const AOutputName: WideString): LongBool;

## ICrosspointSwitchInstrumentManager
继承：ICrosspointSwitchInstrumentManager → IScriptedInstrumentManager → IInterface ｜ 单元：RT_CrosspointSwitch ｜ 自有 4 个方法、0 个属性

function GetInstrument(Index: Integer): ICrosspointSwitchInstrument;
function GetInstrumentByDesignator(const ADesignator: WideString): ICrosspointSwitchInstrument;
function GetInstrumentByJtagIndex(AJtagIndex: Integer): ICrosspointSwitchInstrument;
function GetInstrumentCount: Integer;

## ICustomClipboardFormat
继承：ICustomClipboardFormat → IInterface ｜ 单元：RT_Workspace ｜ 自有 1 个方法、0 个属性

function RegisterCustomClipboardFormat(const AFormatName: WideString): Cardinal;

## ICustomCore
继承：ICustomCore → IInterface ｜ 单元：Rt_NexusDevices ｜ 自有 4 个方法、2 个属性

property DoSoftError: LongBool read GetDoSoftError write SetDoSoftError;
property Info: WideString read GetInfo write SetInfo;
function GetDoSoftError: LongBool;
function GetInfo: WideString;
procedure SetDoSoftError(Value: LongBool);
procedure SetInfo(Value: WideString);

## ICustomCoreGenerator
继承：ICustomCoreGenerator → IInterface ｜ 单元：Rt_NexusDevices ｜ 自有 1 个方法、0 个属性

function CreateTarget(const AParameters: WideString): ICustomCore;

## ICustomDialog
继承：ICustomDialog → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 1 个方法、0 个属性

function Invoke(var Params: WideString): Integer;

## IDBApplication
继承：IDBApplication → IInterface ｜ 单元：Data.DB ｜ 自有 3 个方法、1 个属性

property Title: String read GetTitle write SetTitle;
function GetTitle: string;
procedure ProcessMessages;
procedure SetTitle(const Value: string);

## IDBScreen
继承：IDBScreen → IInterface ｜ 单元：Data.DB ｜ 自有 2 个方法、1 个属性

property Cursor: TDBScreenCursor read GetCursor write SetCursor;
function GetCursor: TDBScreenCursor;
procedure SetCursor(Cursor: TDBScreenCursor);

## IDBSession
继承：IDBSession → IInterface ｜ 单元：Data.DB ｜ 自有 3 个方法、0 个属性

procedure AddPassword(const APassword: string);
procedure RemoveAllPasswords;
procedure RemovePassword(const APassword: string);

## IDDMBoardProject
继承：IDDMBoardProject → IDDMProjectBase → IInterface ｜ 单元：RT_Workspace ｜ 自有 22 个方法、0 个属性

procedure AddMissingAutoCrossRefs;
procedure ClearAllNetColors;
procedure ClearViolations;
function Compile(PopulateMessagesManager: LongBool): LongBool;
function ForceCompilationOnMainThread: Boolean;
function GetAutomaticSheetsNumbers: IAutomaticSheetsNumbers;
function GetHierarchyModeForCompile: TFlattenMode;
function GetNetColorByName(const ANetName: WideString): TColor;
function GetNetInfosToExportCount: Integer;
function GetNetInfoToExport(Index: Integer): WideString;
function GetViolation(Index: Integer): IViolation;
function GetViolationsCount: Integer;
function GetVirtualParametersManager: IVirtualParametersManager;
function IsInCompilationState: Boolean;
function NeedsCompile: LongBool;
function ResumeContinuousCompilation: Boolean;
procedure SetConnectedNetsColor(const Net: INet; Color: TColor);
procedure SetErrorLevels(ErrorKind: TErrorKind; ErrorLevel: TErrorLevel);
procedure SetErrorLevelsForConnections(Row: TConnectionCode; Column: TConnectionCode; ErrorLevel: TErrorLevel);
procedure SetNetColorByName(const ANetName: WideString; AColor: TColor);
function SuspendContinuousCompilation: Boolean;
procedure Validate;

## IDDMHarnessProject
继承：IDDMHarnessProject → IDDMProjectBase → IInterface ｜ 单元：RT_Workspace ｜ 自有 2 个方法、0 个属性

function GetHarnessDocumentFlattened: IDocument;
procedure PerformSpatialAnalysis(const ADocumentFilePath: WideString);

## IDDMObserver
继承：IDDMObserver → IInterface ｜ 单元：RT_Workspace ｜ 自有 6 个方法、0 个属性

procedure BeginUpdate(const ProjectPath: WideString);
procedure Compiled(const ProjectPath: WideString; const FlattenedDoc: IDocument);
procedure EndUpdate;
procedure ObjectAdded(const aObject: IDMObject);
procedure ObjectRemoved(ObjectAddress: Pointer);
procedure ObjectUpdated(const aObject: IDMObject);

## IDDMProjectBase
继承：IDDMProjectBase → IInterface ｜ 单元：RT_Workspace ｜ 自有 9 个方法、0 个属性

function GetDocumentByDocumentId(const ADocumentUniqueId: WideString): IDocument;
function GetDocumentByName(const ADocumentFileName: WideString): IDocument;
function GetDocumentByPath(const ADocumentFilePath: WideString): IDocument;
function GetDocumentFlattened: IDocument;
function GetPhysicalDocument(AIndex: Integer): IDocument;
function GetPhysicalDocumentsCount: Integer;
function GetScrapDocument(const ADocumentFilePath: WideString): IDocument;
function GetTopLevelLogicalDocument: IDocument;
function GetTopLevelPhysicalDocument: IDocument;

## IDItemModel
继承：IDItemModel → IInterface ｜ 单元：Rt_AltiumLibrary ｜ 自有 0 个方法、0 个属性


## IDItemRevision
继承：IDItemRevision → IInterface ｜ 单元：Rt_AltiumLibrary ｜ 自有 18 个方法、13 个属性

property Category: WideString read GetState_Category;  // read-only
property Comment: WideString read GetState_Comment;  // read-only
property Description: WideString read GetState_Description;  // read-only
property DeviceSheet: IDeviceSheet read GetState_DeviceSheet;  // read-only
property LibIdentifierKind: TLibIdentifierKind read GetState_LibIdentifierKind;  // read-only
property LibraryIdentifier: WideString read GetState_LibraryIdentifier;  // read-only
property Name: WideString read GetState_Name;  // read-only
property ParameterCount: Integer read GetState_ParametersCount;  // read-only
property Parameters[Index: Integer]: IItemParameter read GetState_ParameterAt;  // read-only
property SourceRelationship[Index: Integer]: ISourceRelationship read GetState_SourceRelationshipAt;  // read-only
property SourceRelationshipCount: Integer read GetState_SourceRelationshipCount;  // read-only
property SymbolLibraryFullPath: WideString read GetState_SymbolLibraryFullPath;  // read-only
property SymbolName: WideString read GetState_SymbolName;  // read-only
procedure DeleteParameter(Index: Integer);
function GetParameterByName(AName: WideString): IItemParameter;
function GetParameterValueByName(AName: WideString): WideString;
function GetState_Category: WideString;
function GetState_Comment: WideString;
function GetState_Description: WideString;
function GetState_DeviceSheet: IDeviceSheet;
function GetState_LibIdentifierKind: TLibIdentifierKind;
function GetState_LibraryIdentifier: WideString;
function GetState_Name: WideString;
function GetState_ParameterAt(Index: Integer): IItemParameter;
function GetState_ParametersCount: Integer;
function GetState_SourceRelationshipAt(Index: Integer): ISourceRelationship;
function GetState_SourceRelationshipCount: Integer;
function GetState_SymbolLibraryFullPath: WideString;
function GetState_SymbolName: WideString;
procedure Load;
procedure SetParameterValueByName(AName: WideString; AValue: WideString);

## IDMObject
继承：IDMObject → IInterface ｜ 单元：RT_Workspace ｜ 自有 47 个方法、1 个属性

property VCSProject: IInterface read DM_GetVCSProject write DM_SetVCSProject;
procedure DM_AddParameterBase(AName: WideString; AValue: WideString);
function DM_BoundingRectangle: IDispatch;
function DM_BoundingRectangle_Designator: IDispatch;
function DM_BoundingRectangle_Full: IDispatch;
function DM_CalculateParameterValue(AParameter: IParameter): WideString;
function DM_CurrentSheetInstanceNumber: Integer;
procedure DM_DoCrossProbeBase;
function DM_FullCrossProbeString: WideString;
function DM_GeneralField: Integer;
function DM_GetParameterByName(const AParameterName: WideString): IParameter;
function DM_GetStringParameterValue(const AParameterName: WideString): WideString;
function DM_GetVCSProject: IInterface;
function DM_ImageIndex: Integer;
function DM_IsDDMHarnessObject: Boolean;
function DM_IsDDMObject: Boolean;
function DM_IsFormulaString(AFormula: WideString): Boolean;
function DM_IsInferredObject: Boolean;
function DM_IsObjectDestroyed: Boolean;
function DM_LocationString: WideString;
function DM_LocationX: Integer;
function DM_LocationY: Integer;
function DM_LongDescriptorString: WideString;
function DM_NetIndex_Flat: Integer;
function DM_NetIndex_Sheet: Integer;
function DM_NetIndex_SubNet: Integer;
function DM_ObjectAdress: Pointer;
function DM_ObjectKind: TWorkspaceObjectId;
function DM_ObjectKindString: WideString;
function DM_ObjectKindStringForCrossProbe: WideString;
function DM_OwnerDocument: IDocument;
function DM_OwnerDocumentFullPath: WideString;
function DM_OwnerDocumentName: WideString;
procedure DM_ParameterChangesClear;
function DM_ParameterCount: Integer;
function DM_Parameters(Index: Integer): IParameter;
function DM_PcbHandle: WideString;
function DM_PCBObjectHandle: Pointer;
function DM_PrimaryCrossProbeString: WideString;
function DM_SchHandle: WideString;
function DM_SCHObjectHandle: Pointer;
function DM_SecondaryCrossProbeString: WideString;
procedure DM_SetVCSProject(const Value: IInterface);
function DM_SheetIndex_Logical: Integer;
function DM_SheetIndex_Physical: Integer;
function DM_ShortDescriptorString: WideString;
function DM_ValidForNavigation: Boolean;
function DM_VHDLEntity: IVHDLEntity;

## IDM_FSMState
继承：IDM_FSMState → IDMObject → IInterface ｜ 单元：RT_Workspace ｜ 自有 8 个方法、0 个属性

function DM_Actions: WideString;
function DM_DelayedClock: Integer;
function DM_DelayedEnable: Boolean;
function DM_IsDefault: LongBool;
function DM_Name: WideString;
function DM_OutputTransition(Index: Integer): IDM_FSMTransition;
function DM_OutputTransitionCount: Integer;
function DM_UniqueId: WideString;

## IDM_FSMTransition
继承：IDM_FSMTransition → IDMObject → IInterface ｜ 单元：RT_Workspace ｜ 自有 9 个方法、0 个属性

function DM_Actions: WideString;
function DM_Condition_Verilog: WideString;
function DM_Condition_VHDL: WideString;
function DM_FromState: IDM_FSMState;
function DM_FromStateID: WideString;
function DM_Priority: Integer;
function DM_ToState: IDM_FSMState;
function DM_ToStateID: WideString;
function DM_UniqueId: WideString;

## IDXPAltiumPortal
继承：IDXPAltiumPortal → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 18 个方法、0 个属性

procedure AddAltiumPortalEvent(AEventType: WideString);
function FullName: WideString;
function GetContentVaultServiceUrl: WideString;
function GetGlobalIDSServiceUrl: WideString;
procedure GetOperatorDetails;
function GetPRT_GlobalServiceUrl(const ServiceName: WideString): WideString;
function IsBusy: Boolean;
function LoggedIn: Boolean;
function LoggingIn: Boolean;
procedure LoginBySessionID(AWaitForResult: Boolean; ASessionHandle: WideString);
function Logout: Boolean;
function OperatorAccountName: WideString;
function Password: WideString;
function PortalSecureSessionHandle: WideString;
function PortalSessionHandle: WideString;
function ProfilePicture: WideString;
procedure ResetPassWord;
function UserName: WideString;

## IDXPAltiumPortalUIFactory
继承：IDXPAltiumPortalUIFactory → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 2 个方法、0 个属性

function SavedLogin: WideString;
function ShowPortalSigninDialog(var ASessionId: WideString): Boolean;

## IDXPDashboardServerView
继承：IDXPDashboardServerView → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 0 个方法、0 个属性


## IDXPDocument
继承：IDXPDocument → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 7 个方法、0 个属性

function DM_DocumentIsLoaded: Boolean;
function DM_DocumentIsTextual: Boolean;
function DM_DocumentKind: WideString;
function DM_FileName: WideString;
function DM_FullPath: WideString;
function DM_IsVirtualDocument: Boolean;
function DM_Project: IDXPProject;

## IDXPExtensionManager
继承：IDXPExtensionManager → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 1 个方法、1 个属性

property Settings: IDXPExtensionManagerSettings read GetState_Settings;  // read-only
function GetState_Settings: IDXPExtensionManagerSettings;

## IDXPExtensionManagerSettings
继承：IDXPExtensionManagerSettings → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 4 个方法、1 个属性

property CheckFrequency: TUpdateCheckFrequency read GetState_CheckFrequency write SetState_CheckFrequency;
function GetState_CheckFrequency: TUpdateCheckFrequency;
procedure Load;
procedure Save;
procedure SetState_CheckFrequency(AValue: TUpdateCheckFrequency);

## IDXPLocalComparisonCallback
继承：IDXPLocalComparisonCallback → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 1 个方法、0 个属性

procedure Handle(const aResult: IDXPLocalComparisonResult);

## IDXPLocalComparisonResult
继承：IDXPLocalComparisonResult → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 4 个方法、3 个属性

property ErrorMessage: WideString read GetErrorMessage;  // read-only
property IsDone: Boolean read GetIsDone;  // read-only
property IsSuccess: Boolean read GetIsSuccess;  // read-only
function GetErrorMessage: WideString;
function GetIsDone: Boolean;
function GetIsSuccess: Boolean;
procedure Terminate;

## IDXPMessageItem
继承：IDXPMessageItem → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 18 个方法、18 个属性

property CallBackParameters: WideString read GetCallBackParameters;  // read-only
property CallBackParameters2: WideString read GetCallBackParameters2;  // read-only
property CallBackProcess: WideString read GetCallBackProcess;  // read-only
property CallBackProcess2: WideString read GetCallBackProcess2;  // read-only
property Details: IDXPMessageItemDetails read GetDetails;  // read-only
property Document: WideString read GetDocument;  // read-only
property HelpFileID: WideString read GetHelpFileID;  // read-only
property HelpFileName: WideString read GetHelpFileName;  // read-only
property ImageIndex: Integer read GetImageIndex;  // read-only
property MsgClass: WideString read GetMsgClass;  // read-only
property MsgColor: Integer read GetMsgColor;  // read-only
property MsgDateTime: TDateTime read GetMsgDateTime;  // read-only
property MsgIndex: Integer read GetMsgIndex;  // read-only
property Pinned: Boolean read GetPinned;  // read-only
property Selected: Boolean read GetSelected;  // read-only
property Source: WideString read GetSource;  // read-only
property Text: WideString read GetText;  // read-only
property UserID: WideString read GetUserId;  // read-only
function GetCallBackParameters: WideString;
function GetCallBackParameters2: WideString;
function GetCallBackProcess: WideString;
function GetCallBackProcess2: WideString;
function GetDetails: IDXPMessageItemDetails;
function GetDocument: WideString;
function GetHelpFileID: WideString;
function GetHelpFileName: WideString;
function GetImageIndex: Integer;
function GetMsgClass: WideString;
function GetMsgColor: Integer;
function GetMsgDateTime: TDateTime;
function GetMsgIndex: Integer;
function GetPinned: Boolean;
function GetSelected: Boolean;
function GetSource: WideString;
function GetText: WideString;
function GetUserId: WideString;

## IDXPMessageItemDetails
继承：IDXPMessageItemDetails → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 1 个方法、1 个属性

property RootItem: IDXPMessageSubItem read GetRootItem;  // read-only
function GetRootItem: IDXPMessageSubItem;

## IDXPMessageSubItem
继承：IDXPMessageSubItem → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 7 个方法、6 个属性

property CallBackParameters: WideString read GetCallBackParameters;  // read-only
property CallBackProcess: WideString read GetCallBackProcess;  // read-only
property Count: Integer read GetCount;  // read-only
property ImageIndex: Integer read GetImageIndex;  // read-only
property Item[Index: Integer]: IDXPMessageSubItem read GetItem;  // read-only
property Text: WideString read GetText;  // read-only
procedure AddSubItem(AText: WideString; AImageIndex: Integer; ACallBackProcess: WideString; ACallBackParameters: WideString);
function GetCallBackParameters: WideString;
function GetCallBackProcess: WideString;
function GetCount: Integer;
function GetImageIndex: Integer;
function GetItem(Index: Integer): IDXPMessageSubItem;
function GetText: WideString;

## IDXPMessagesManager
继承：IDXPMessagesManager → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 21 个方法、0 个属性

procedure AddMessage(const MessageClass: WideString; const MessageText: WideString; const MessageSource: WideString; const MessageDocument: WideString; const MessageCallBackProcess: WideString; const MessageCallBackParameters: WideString; ImageIndex: Integer; ReplaceLastMessageIfSameClass: Boolean);
procedure AddMessage2(const MessageClass: WideString; const MessageText: WideString; const MessageSource: WideString; const MessageDocument: WideString; const MessageCallBackProcess: WideString; const MessageCallBackParameters: WideString; ImageIndex: Integer; ReplaceLastMessageIfSameClass: Boolean; const MessageCallBackProcess2: WideString; const MessageCallBackParameters2: WideString; const Details: IDXPMessageItemDetails);
procedure AddMessageParametric(MessageParams: PWideChar; MessageCallBackParameters: PWideChar);
procedure BeginPinCriticalMessages(AErrorLevel: TErrorLevel);
procedure BeginPreserve;
procedure BeginUpdate;
procedure ClearMessageByIndex(AIndex: Integer);
procedure ClearMessages;
procedure ClearMessagesForDocument(const DocumentPath: WideString);
procedure ClearMessagesOfClass(const AMsgClass: WideString);
procedure ClearPinnedMessages;
function CreateMesssageItemDetails: IDXPMessageItemDetails;
procedure EndPinCriticalMessages;
procedure EndPreserve;
procedure EndUpdate;
function GetMaxErrorLevel: TErrorLevel;
function Messages(Index: Integer): IDXPMessageItem;
function MessagesCount: Integer;
function SelectedMessages(Index: Integer): IDXPMessageItem;
function SelectedMessagesCount: Integer;
procedure UpdateWindow;

## IDXPNavigator
继承：IDXPNavigator → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 3 个方法、0 个属性

function DXPFavoritesNavigateTo(const Target: WideString): Boolean;
function DXPNavigateInNewWindow(const Target: WideString): Boolean;
function DXPNavigateTo(const Target: WideString): Boolean;

## IDXPProductBranding
继承：IDXPProductBranding → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 3 个方法、0 个属性

function VaultAllowSwitch: Boolean;
function VaultCaption: WideString;
function VaultImage: WideString;

## IDXPProject
继承：IDXPProject → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 44 个方法、1 个属性

property VCSProject: IInterface read DM_GetVCSProject write DM_SetVCSProject;
procedure DM_AddControlPanel(FileName: WideString);
procedure DM_AddGeneratedDocument(FileName: WideString);
procedure DM_AddParameter(const AName: WideString; const AValue: WideString);
procedure DM_AddSourceDocument(FileName: WideString);
procedure DM_AddToVCSPostProcess(AIsInternalRepository: Boolean);
procedure DM_AddToVCSPreProcess(const ARepositoryGUID: WideString; const ARepositoryPath: WideString; AIsInternalRepository: Boolean);
function DM_ExternalFiles(ASearchInDocuments: Boolean; ACheckForExistence: Boolean): IExternalFiles;
function DM_GeneratedDocumentCount: Integer;
function DM_GeneratedDocuments(Index: Integer): IDXPDocument;
function DM_GetDocumentByDocumentId(const ADocumentId: WideString): IDXPDocument;
function DM_GetDocumentFromPath(DocumentPath: WideString): IDXPDocument;
function DM_GetIsEnabledOnlineSynchronization: Boolean;
function DM_GetOutputPath: WideString;
function DM_GetParameterCount: Integer;
function DM_GetParameterExist(const AName: WideString): Boolean;
function DM_GetParameterName(const AIndex: Integer): WideString;
function DM_GetParameterValue(const AIndex: Integer): WideString;
function DM_GetVCSProject: IInterface;
function DM_IsActive: Boolean;
function DM_IsHidden: Boolean;
function DM_IsLinkedToVault: Boolean;
function DM_IsReuseBlock: Boolean;
function DM_IsSharedWithMe: Boolean;
function DM_ItemGUID: WideString;
function DM_LogicalDocumentCount: Integer;
function DM_LogicalDocuments(Index: Integer): IDXPDocument;
function DM_ManagedProjectGUID: WideString;
function DM_OfflineProjectGUID: WideString;
function DM_OptionsStorage: IOptionsStorage;
function DM_OwnedProjectCount: Integer;
function DM_OwnedProjects(Index: Integer): IDXPProject;
function DM_ProjectFileName: WideString;
function DM_ProjectFullPath: WideString;
procedure DM_RefreshInWorkspaceForm;
procedure DM_RemoveParameter(const AIndex: Integer);
procedure DM_RemoveSourceDocument(FileName: WideString);
function DM_RevisionGUID: WideString;
function DM_ServerDocument: IServerDocument;
procedure DM_SetParameter(const AName: WideString; const AValue: WideString);
procedure DM_SetVCSProject(const Value: IInterface);
procedure DM_UnlinkFromVault;
function DM_VaultGUID: WideString;
function DM_VaultHRID: WideString;
function DM_WriteAccessState: TWriteAccessState;

## IDXPSVNDatabaseLibDocument
继承：IDXPSVNDatabaseLibDocument → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 3 个方法、0 个属性

function GetFileName: WideString;
function GetLibrarySearchPath: WideString;
function GetRepositoryURL: WideString;

## IDXPServer_Notification
继承：IDXPServer_Notification → ITypedNotification → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 0 个方法、0 个属性


## IDXPSplash
继承：IDXPSplash → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 4 个方法、0 个属性

procedure AddMessage(const Msg: WideString);
procedure HideSplash;
procedure SetParam(const ParamName: WideString; const ParamValue: WideString);
procedure ShowSplash(const IsStartup: Boolean);

## IDXPWorkSpace
继承：IDXPWorkSpace → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 26 个方法、0 个属性

procedure DM_ClearOutputLines;
function DM_CreateNewDocument(ADocKind: WideString): WideString;
procedure DM_FileOwnership_BulkWarnEnd(AWarningLevel: TFileOwnershipWarningLevel);
function DM_FileOwnership_BulkWarnRegister(AFileName: string): Boolean;
procedure DM_FileOwnership_BulkWarnStart;
function DM_FocusedDocument: IDXPDocument;
function DM_FocusedProject: IDXPProject;
function DM_FreeDocumentsProject: IDXPProject;
function DM_GetDocumentFromPath(DocumentPath: WideString): IDXPDocument;
function DM_GetManagedDocumentImageIndex(const AFilePath: WideString): Integer;
function DM_GetOutputLine(Index: Integer): WideString;
function DM_GetOutputLineCount: Integer;
function DM_GetProjectFromPath(ProjectPath: WideString): IDXPProject;
function DM_IsReferencedAsDeviceSheet(const AFilePath: WideString): Boolean;
function DM_LoadProjectHidden(const ProjectPath: WideString): IDXPProject;
function DM_LocalHistoryManager: ILocalHistoryManager;
function DM_MessagesManager: IDXPMessagesManager;
function DM_Preferences: IDXPWorkspacePreferences;
function DM_ProductBranding: IDXPProductBranding;
function DM_ProjectCount: Integer;
function DM_Projects(Index: Integer): IDXPProject;
procedure DM_ShowMessageView;
procedure DM_UpdateOutputWindow;
function DM_UseItemRevision(const AVaultGuid: WideString; const AItemGUID: WideString; const ARevisionGUID: WideString; const AParams: WideString): Boolean;
function DM_WorkspaceFileName: WideString;
function GetProjectsByGUID(const APath: WideString; const AManagedProjectGUID: WideString; const AProjectType: WideString): IStrings;

## IDXPWorkspace2
继承：IDXPWorkspace2 → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 1 个方法、0 个属性

function DM_UseItemRevision_ExtPcb(const AVaultGuid: WideString; const AItemGUID: WideString; const ARevisionGUID: WideString; const ASelectedItemGUID: WideString; const ASelectedItemRevisionGUID: WideString; const AParams: WideString): Boolean;

## IDXPWorkspaceHelper
继承：IDXPWorkspaceHelper → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 2 个方法、0 个属性

function CompareLocalProjectWithLastRevision(const AProjectPath: WideString; ARevisionType: TLocalComparisonRevisionType; ADocumentType: TLocalComparisonDocumentType; AShowPrepareDialog: Boolean; const ACallback: IDXPLocalComparisonCallback): IDXPLocalComparisonResult;
function CompareLocalProjectWithSpecificRevision(const AProjectPath: WideString; ARevisionType: TLocalComparisonRevisionType; const ARevisionID: WideString; ADocumentType: TLocalComparisonDocumentType; AShowPrepareDialog: Boolean; const ACallback: IDXPLocalComparisonCallback): IDXPLocalComparisonResult;

## IDXPWorkspacePreferences
继承：IDXPWorkspacePreferences → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 16 个方法、9 个属性

property DefaultDocumentPath: WideString read GetDefaultDocumentPath;  // read-only
property FileOwnership_Enabled: Boolean read GetFileOwnership_Enabled write SetFileOwnership_Enabled;
property FileOwnership_EnabledOutputDirectory: Boolean read GetFileOwnership_EnabledOutputDirectory write SetFileOwnership_EnabledOutputDirectory;
property FileOwnership_WarningLevelOpen: TFileOwnershipWarningLevel read GetFileOwnership_WarningLevelOpen write SetFileOwnership_WarningLevelOpen;
property FileOwnership_WarningLevelSave: TFileOwnershipWarningLevel read GetFileOwnership_WarningLevelSave write SetFileOwnership_WarningLevelSave;
property ReleasesTemporaryFolder: WideString read GetReleasesTemporaryFolder write SetReleasesTemporaryFolder;
property ReleasesTemporaryFolderCleanUp: Boolean read GetReleasesTemporaryFolderCleanUp write SetReleasesTemporaryFolderCleanUp;
property ReleasesTemporaryFolderNotExpanded: WideString read GetReleasesTemporaryFolderNotExpanded write SetReleasesTemporaryFolderNotExpanded;
property TemplatePath: WideString read GetTemplatePath;  // read-only
function GetDefaultDocumentPath: WideString;
function GetFileOwnership_Enabled: Boolean;
function GetFileOwnership_EnabledOutputDirectory: Boolean;
function GetFileOwnership_WarningLevelOpen: TFileOwnershipWarningLevel;
function GetFileOwnership_WarningLevelSave: TFileOwnershipWarningLevel;
function GetReleasesTemporaryFolder: WideString;
function GetReleasesTemporaryFolderCleanUp: Boolean;
function GetReleasesTemporaryFolderNotExpanded: WideString;
function GetTemplatePath: WideString;
procedure SetFileOwnership_Enabled(AValue: Boolean);
procedure SetFileOwnership_EnabledOutputDirectory(AValue: Boolean);
procedure SetFileOwnership_WarningLevelOpen(AValue: TFileOwnershipWarningLevel);
procedure SetFileOwnership_WarningLevelSave(AValue: TFileOwnershipWarningLevel);
procedure SetReleasesTemporaryFolder(const AValue: WideString);
procedure SetReleasesTemporaryFolderCleanUp(const AValue: Boolean);
procedure SetReleasesTemporaryFolderNotExpanded(const AValue: WideString);

## IDataBaseLibCommands
继承：IDataBaseLibCommands → IInterface ｜ 单元：RT_Workspace ｜ 自有 11 个方法、0 个属性

function GetCommaDelimitedFieldValues(ATableIndex: Integer; AFieldIndex: Integer): WideString;
function GetDatabaseType: TDatabaseType;
function GetFieldTypeAt(ATableIndex: Integer; AFieldIndex: Integer): TFieldType;
function GetLeftQuote: WideString;
function GetRightQuote: WideString;
function GetTableNameForSQL(ATableIndex: Integer): WideString;
function GetWhereClause(ATableIndex: Integer; const AComponentKeys: WideString): WideString;
function HasComponent(ATableIndex: Integer; const AComponentKeys: WideString): Boolean;
function HasDatafileEntity(ATableIndex: Integer; const ADatafileEntityName: WideString; const ADatafileType: WideString): Boolean;
function HasModel(ATableIndex: Integer; const AComponentKeys: WideString; const AModelName: WideString; const AModelType: WideString): Boolean;
procedure ShowTableBrowser;

## IDataForEDM_UserLoggedInNotification
继承：IDataForEDM_UserLoggedInNotification → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 7 个方法、5 个属性

property CanLogin: LongBool read GetCanLogin write SetCanLogin;
property DenyReason: WideString read GetDenyReason write SetDenyReason;
property Host: WideString read GetHost;  // read-only
property SessionID: WideString read GetSessionID;  // read-only
property UserName: WideString read GetUserName;  // read-only
function GetCanLogin: LongBool;
function GetDenyReason: WideString;
function GetHost: WideString;
function GetSessionID: WideString;
function GetUserName: WideString;
procedure SetCanLogin(const AData: LongBool);
procedure SetDenyReason(const AData: WideString);

## IDataSetCommandSupport
继承：IDataSetCommandSupport → IInterface ｜ 单元：Data.DB ｜ 自有 2 个方法、0 个属性

procedure ExecuteCommand(const ACommand: string; const Args: array of TVarRec);
function GetCommandStates(const ACommand: string): TDataSetCommandStates;

## IDatabaseLibDocument
继承：IDatabaseLibDocument → IInterface ｜ 单元：RT_Workspace ｜ 自有 42 个方法、0 个属性

procedure ClearDatabaseTypeFields;
procedure CreateTableInDatabase(ATableName: WideString; APrimaryKeyColumnName: WideString);
procedure DisposeIfNotShowing;
function DocumentObject: Pointer;
function ExportNewRecordFromIntLib(ATableName: WideString; AFieldParameters: WideString): WideString;
procedure FinaliseExportFromDatabase;
procedure GetAllComponentKeys(ATableIndex: Integer; AResults: IStrings);
function GetCommandString(ATableIndex: Integer; AFilterText: WideString; ASQLWhereClause: WideString): WideString;
function GetConnectionString: WideString;
function GetDatafilePath(AName: WideString; AType: WideString; ATableName: WideString; AComponentKeys: WideString): WideString;
function GetDesignParameterName(ATableIndex: Integer; const AFieldName: WideString): WideString;
function GetFieldCount(ATableIndex: Integer): Integer;
function GetFieldNameAt(ATableIndex: Integer; AFieldIndex: Integer): WideString;
function GetFileName: WideString;
function GetFilterText(ATableIndex: Integer; AFilterColumnNames: WideString; AFilterValue: WideString): WideString;
function GetItemCount(ACommand: WideString; var AnError: WideString): Integer;
function GetKeyField(AParameterName: Boolean; ATableIndex: Integer; AKeyIndex: Integer): WideString;
function GetKeyFieldCount(ATableIndex: Integer): Integer;
function GetLibraryPathFieldName(ATableIndex: Integer): WideString;
function GetLibraryRefFieldName(ATableIndex: Integer; var AOrcadLibrary: Boolean): WideString;
function GetLibrarySearchPath: WideString;
procedure GetModelFieldNamesAt(AnIndex: Integer; ATableIndex: Integer; AModelType: WideString; var AModelPathName: WideString; var AModelRefName: WideString; var AOrcadModel: Boolean);
procedure GetOrcadLibraryDetails(AParseString: WideString; var LibRef: WideString; var LibPath: WideString);
function GetParameterNameAt(ATableIndex: Integer; AFieldIndex: Integer): WideString;
function GetParametersForComponent(ATableIndex: Integer; AComponentKeys: WideString): WideString;
function GetSchLibPathForComponent(ATableIndex: Integer; AComponentKeys: WideString): WideString;
function GetSchLibRefForComponent(ATableIndex: Integer; AComponentKeys: WideString): WideString;
function GetSearchSubDirectories: Boolean;
function GetTableCount: Integer;
function GetTableIndex(ATableName: WideString): Integer;
function GetTableNameAt(AnIndex: Integer): WideString;
function InitialiseExportFromIntLib(ATableName: WideString): WideString;
procedure InitialiseExportToDatabase(ADatabaseFileName: WideString);
function IsParameterDatabaseKey(ATableIndex: Integer; AParameterName: WideString): Boolean;
function IsValidSQLStatementForTable(ATableName: WideString; AQuery: WideString): Boolean;
function LoadAllRecordsLimit: Integer;
function ObjectAddress: Pointer;
function OrcadDelimiter: Char;
procedure SetConnectionString(AConnectionString: WideString);
function TableContainsColumn(ATableIndex: Integer; AColumnName: WideString): Boolean;
function TableEnabled(AnIndex: Integer): Boolean;
function ValidateSQLQuery(ASqlQuery: WideString): WideString;

## IDatabaseLinkDocument
继承：IDatabaseLinkDocument → IInterface ｜ 单元：RT_Workspace ｜ 自有 7 个方法、0 个属性

procedure ClearDbCache;
function GetConnectionString: WideString;
function LookUpValues(const APart: IPart; var ACancelled: Boolean): ITableLink;
function LookUpValues_Comp(const AComponent: IComponent; const AVariation: IComponentVariation; var ACancelled: Boolean): ITableLink;
function LookUpValues_NoDBLib(const APart: IPart; var ACancelled: Boolean; ATableName: WideString): ITableLink;
function TableLinkCount: Integer;
function TableLinks(Index: Integer): ITableLink;

## IDebugStatusMonitor
继承：IDebugStatusMonitor → IInterface ｜ 单元：RT_Debugger ｜ 自有 1 个方法、0 个属性

procedure StateChanged;

## IDebuggable
继承：IDebuggable → IInterface ｜ 单元：RT_Debugger ｜ 自有 1 个方法、0 个属性

function GetDebugger: IDebugger;

## IDebugger
继承：IDebugger → IInterface ｜ 单元：RT_Debugger ｜ 自有 45 个方法、0 个属性

function BreakPoint_Add(aFileName: WideString; aLine: Integer): IBreakpoint;
function BreakPoint_At(anIndex: Integer): IBreakpoint;
function BreakPoint_AtForFile(aFileName: WideString; anIndex: Integer): IBreakpoint;
procedure Breakpoint_Changed(aBreakpoint: IBreakpoint);
function BreakPoint_Count: Integer;
function BreakPoint_CountForFile(aFileName: WideString): Integer;
procedure Breakpoint_EnabledChanged(aBreakpoint: IBreakpoint);
function BreakPoint_Find(aFileName: WideString; aLine: Integer): IBreakpoint;
procedure Breakpoint_Focused(aBreakpoint: IBreakpoint);
procedure BreakPoint_Moved(aBreakpoint: IBreakpoint; aOldFileName: WideString; aOldLine: Integer);
procedure BreakPoint_Remove(aFileName: WideString; aLine: Integer);
procedure Breakpoint_ValidChanged(aBreakpoint: IBreakpoint);
function CodePoint_At(aFileName: WideString; anIndex: Integer): Integer;
function CodePoint_Count(aFileName: WideString): Integer;
function CodePoint_IsCodePoint(aFileName: WideString; aLine: Integer): Boolean;
procedure Configure;
function CurrentSourceFullPath: WideString;
procedure Execution_Break;
function Execution_GetExectionPoint(var aFileName: WideString; var aLine: Integer): Boolean;
procedure Execution_Reset;
procedure Execution_Run;
procedure Execution_RunTo(AFile: WideString; aLine: Integer);
procedure Execution_ShowExecutionPoint;
procedure Execution_StepInto;
procedure Execution_StepOver;
function Previous_State: TDebuggerState;
procedure Session_Begin;
procedure Session_End;
function State: TDebuggerState;
procedure View_AttachBreakpointMonitor(aMonitor: IBreakpointMonitor);
procedure View_AttachStatusMonitor(aMonitor: IDebugStatusMonitor);
procedure View_AttachWatchMonitor(aMonitor: IWatchMonitor);
procedure View_DetachBreakpointMonitor(aMonitor: IBreakpointMonitor);
procedure View_DetachStatusMonitor(aMonitor: IDebugStatusMonitor);
procedure View_DetachWatchMonitor(aMonitor: IWatchMonitor);
function Watch_Add(aExpression: WideString): IWatch;
procedure Watch_Add_BeginUpdate;
procedure Watch_Add_EndUpdate;
function Watch_Add_Ext(aExpression: WideString; aFullPath: WideString; aLineNumber: Integer): IWatch;
function Watch_At(anIndex: Integer): IWatch;
procedure Watch_ClearAll;
function Watch_Count: Integer;
function Watch_Find(aExpression: WideString): IWatch;
procedure Watch_Remove(aExpression: WideString);
procedure Watch_UpdateAllValues;

## IDefaultPrimitivesOptionsPageParams
继承：IDefaultPrimitivesOptionsPageParams → IOptionPageParams → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 6 个方法、0 个属性

function GetCount: Integer;
function GetIsModified: LongBool;
function GetIsPermanent: LongBool;
function GetItem(const AIndex: Integer): IPrimitiveDefaultsItem;
procedure SetIsModified(AIsModified: LongBool);
procedure SetIsPermanent(const AIsPermanent: LongBool);

## IDependsOnDisplayStyle
继承：IDependsOnDisplayStyle → IInterface ｜ 单元：InstrumentPanels ｜ 自有 1 个方法、0 个属性

procedure UpdateFromDisplayStyle(AStyle: TDisplayStyle);

## IDependsOnPanelStyle
继承：IDependsOnPanelStyle → IInterface ｜ 单元：InstrumentPanels ｜ 自有 1 个方法、0 个属性

procedure UpdateFromPanelStyle(AStyle: TInstrumentPanelStyle);

## IDesignatorRecord
继承：IDesignatorRecord → IInterface ｜ 单元：RT_Workspace ｜ 自有 7 个方法、0 个属性

function GetChannelName: WideString;
function GetDocumentName: WideString;
function GetLogicalDesignator: WideString;
function GetLogicalPartID: Integer;
function GetPhysicalDesignator: WideString;
function GetPhysicalDesignatorLocked: Boolean;
function GetUniqueID: WideString;

## IDesignerHook
继承：IDesignerHook → IDesignerNotify → IInterface ｜ 单元：Vcl.Forms ｜ 自有 10 个方法、2 个属性

property Form: TCustomForm read GetCustomForm write SetCustomForm;
property IsControl: Boolean read GetIsControl write SetIsControl;
function GetCustomForm: TCustomForm;
function GetIsControl: Boolean;
function GetRoot: TComponent;
function IsDesignMsg(Sender: TControl; const Message: IDispatch): Boolean;
procedure PaintGrid;
procedure PaintMenu;
procedure SetCustomForm(Value: TCustomForm);
procedure SetIsControl(Value: Boolean);
function UniqueName(const BaseName: string): string;
procedure ValidateRename(AComponent: TComponent; const CurName: string; const NewName: string);

## IDesignerNotify
继承：IDesignerNotify → IInterface ｜ 单元：System.Classes ｜ 自有 3 个方法、0 个属性

procedure CanInsertComponent(AComponent: TComponent);
procedure Modified;
procedure Notification(AnObject: TPersistent; Operation: TOperation);

## IDevice
继承：IDevice → IInterface ｜ 单元：Rt_NexusDevices ｜ 自有 0 个方法、0 个属性


## IDeviceChannel
继承：IDeviceChannel → IInterface ｜ 单元：Rt_NexusDevices ｜ 自有 2 个方法、0 个属性

procedure CloseChannel;
function OpenChannel: LongBool;

## IDeviceDebugManager
继承：IDeviceDebugManager → IInterface ｜ 单元：Rt_NexusDevices ｜ 自有 29 个方法、2 个属性

property HardBreakpoints[Index: Integer]: IHardBreakpoint read GetAllocatedHardBreakpointByIndex;  // read-only
property SoftBreakpoints[Index: Integer]: ISoftBreakpoint read GetAllocatedSoftBreakpointByIndex;  // read-only
function AddHardBreakPoint(const ANewBP: IHardBreakpoint): Cardinal;
function AddressSupportsSoftBreakpoints(AMemorySpace: Integer; AAddress: Int64): LongBool;
procedure DisableAllAllocatedBreakpoints;
procedure DisableAllocatedHardBreakpoints;
procedure DisableAllocatedSoftBreakpoints;
procedure EnableAllAllocatedBreakpoints;
procedure EnableAllocatedHardBreakpoints;
procedure EnableAllocatedSoftBreakpoints;
function GetAllocatedHardBreakpointByIndex(Index: Integer): IHardBreakpoint;
function GetAllocatedHardBreakPointCount: Integer;
function GetAllocatedSoftBreakpointByIndex(Index: Integer): ISoftBreakpoint;
function GetAllocatedSoftBreakPointCount: Integer;
function GetBreakpointByAddress(AMemorySpace: Integer; AAddress: Int64): ISoftBreakpoint;
function GetBreakpointByData(AData: Int64): IHardBreakpoint;
function GetBreakpointMode: TBreakpointMode;
function GetDebuggerMode: TDebuggerMode;
function GetHardBreakpointCount: Integer;
function GetNewBreakpoint(AMemorySpace: Integer; AAddress: Int64): ISoftBreakpoint;
function GetNewHardBreakpoint: IHardBreakpoint;
function GetNewSoftBreakpoint: ISoftBreakpoint;
function GetSoftBreakpointsRequireHardware: LongBool;
function GetSystemBreakpoint: IHardBreakpoint;
procedure ReleaseAllBreakpoints;
procedure ReleaseAllocatedHardBreakpoints;
procedure ReleaseAllocatedSoftBreakpoints;
procedure ReleaseBreakpoint(const ABreakpoint: ISoftBreakpoint);
function SetBreakpointMode(ANewMode: TBreakpointMode): LongBool;
procedure SetDebuggerMode(ANewMode: TDebuggerMode);
procedure SetSoftbreakpointsRequireHardware(AValue: LongBool);

## IDeviceFamily
继承：IDeviceFamily → IInterface ｜ 单元：Rt_DeviceFamilies ｜ 自有 13 个方法、0 个属性

function GetBooleanKey(Index: Integer): WideString;
function GetBooleanKeyCount: Integer;
function GetBooleanValueByKey(Key: string): Boolean;
function GetFamilyName: WideString;
function GetIntegerKey(Index: Integer): WideString;
function GetIntegerKeyCount: Integer;
function GetIntegerValueByKey(Key: string): Integer;
function GetStringKey(Index: Integer): WideString;
function GetStringKeyCount: Integer;
function GetStringValueByKey(Key: string): WideString;
function IsKeyValidForBoolean(Key: string): Boolean;
function IsKeyValidForInteger(Key: string): Boolean;
function IsKeyValidForString(Key: string): Boolean;

## IDeviceFamilyManager
继承：IDeviceFamilyManager → IInterface ｜ 单元：Rt_DeviceFamilies ｜ 自有 4 个方法、0 个属性

function FamilyCount: Integer;
function GetFamily(FamilyName: string): IDeviceFamily;
function GetFamilyByIndex(Index: Integer): IDeviceFamily;
function GetListOfFamilies: WideString;

## IDeviceIOStandard
继承：IDeviceIOStandard → IInterface ｜ 单元：Rt_NexusDevices ｜ 自有 6 个方法、0 个属性

function GetDisplayName: WideString;
function GetDriveCount: Integer;
function GetDriveStrength(Index: Integer): WideString;
function GetParamName: WideString;
function GetSlewCount: Integer;
function GetSlewValue(Index: Integer): WideString;

## IDeviceInformation
继承：IDeviceInformation → IInterface ｜ 单元：Rt_NexusDevices ｜ 自有 46 个方法、0 个属性

function GetBaseName: WideString;
function GetBSDLEntity: IBSDLEntity;
function GetBSDLFilename: WideString;
function GetClockManagerCount: Integer;
function GetConfigMemorySize: Integer;
function GetDeviceDescription: WideString;
function GetDeviceDisplayName: WideString;
function GetDeviceIOCount: Integer;
function GetDeviceName: WideString;
function GetDeviceParameter(ParameterName: WideString): WideString;
function GetDevicePin(Index: Integer): IDevicePin;
function GetDevicePinCount: Integer;
function GetDiffPairCount: Integer;
function GetDownloadFileExtensions: WideString;
function GetDSPMultiplierCount: Integer;
function GetEquivalentGatesForBase: Integer;
function GetFamilyDescription: WideString;
function GetFamilyName: WideString;
function GetGlobalClockCount: Integer;
function GetHighSpeedDiffPairCount: Integer;
function GetIdCode: Cardinal;
function GetInstructionLength: Integer;
function GetIOStandard(Index: Integer): IDeviceIOStandard;
function GetIOStandardCount: Integer;
function GetLibraryName: WideString;
function GetMaxIOForBase: Integer;
function GetMemorySize: Integer;
function GetOptionDesignatorDescription: WideString;
function GetOptionDesignatorId: WideString;
function GetOptionDesignatorName: WideString;
function GetPackageDescription: WideString;
function GetPackageDimensions: WideString;
function GetPackageId: WideString;
function GetPackageName: WideString;
function GetPackageTypeDescription: WideString;
function GetPackageTypeId: WideString;
function GetPackageTypeName: WideString;
function GetSpeedGradeDescription: WideString;
function GetSpeedGradeId: WideString;
function GetSpeedGradeName: WideString;
function GetTemperatureGradeDescription: WideString;
function GetTemperatureGradeId: WideString;
function GetTemperatureGradeName: WideString;
function GetTerminationSupport: Boolean;
function GetVendorName: WideString;
function GetVendorPrimitiveLibraryName: WideString;

## IDeviceLink
继承：IDeviceLink → IInterface ｜ 单元：Rt_NexusWorkspace ｜ 自有 18 个方法、0 个属性

function AnyFlowsRunning: Boolean;
function DownloadFlow: IProcessFlow;
function GetConfiguration: WideString;
function GetDeviceName: WideString;
function GetFPGAProject: IProject;
function GetIndex: Integer;
function GetJTAGDevice: IJTagDevice;
function GetJTAGIndex: Integer;
function GetNexusCore: INexusCore;
function GetNexusDevice: INexusDevice;
function GetProject: IProject;
function GetShortDescription: WideString;
function GetUniqueDescription: WideString;
function ProcessFlow: IProcessFlow;
procedure SetDeviceName(const ADeviceName: WideString);
function SubversionFlow: IProcessFlow;
function VaultFlow: IProcessFlow;
function VerifyFlow: IProcessFlow;

## IDeviceManager
继承：IDeviceManager → IInterface ｜ 单元：Rt_NexusDevices ｜ 自有 23 个方法、2 个属性

property Count: Integer read GetCount;  // read-only
property Names[Index: Integer]: WideString read GetNames;  // read-only
function AreDevicesPinCompatible(DeviceName1: WideString; DeviceName2: WideString): LongBool;
function CanGetDevice(DeviceName: WideString): Boolean;
function ChoosePhysicalDevice(DeviceName: WideString; FilterParameters: PWideChar): WideString;
function CompareIdCodes(IdCodeA: Cardinal; IdCodeB: Cardinal): Boolean;
procedure Finalize;
function GetAllVendors: WideString;
function GetConfigurator(const AConfiguratorName: WideString): IComponentConfigurator;
function GetCount: Integer;
function GetDefaultDevice: WideString;
function GetDevice(DeviceName: WideString): INexusDevice;
function GetDeviceCachedInfo(const ADeviceName: WideString; const AInformation: IDispatch): Boolean;
function GetDeviceFamilyManager: IDeviceFamilyManager;
function GetDeviceFromDeviceId(AnId: WideString): INexusDevice;
function GetDeviceInformation(DeviceName: WideString): IDeviceInformation;
function GetDeviceNamesForIdCode(IdCode: Cardinal): WideString;
function GetDevicesForFamily(const Family: WideString): WideString;
function GetFamiliesForDeviceType(const ADeviceType: WideString): WideString;
function GetFamiliesForVendor(const Vendor: WideString): WideString;
function GetGenericDeviceManager: IGenericDeviceManager;
function GetNames(Index: Integer): WideString;
function Initialize: LongBool;
procedure ReleaseDevice(NexusDevice: INexusDevice);
procedure SetDefaultDevice(DeviceName: WideString);

## IDeviceMemoryArchitectureSection
继承：IDeviceMemoryArchitectureSection → IInterface ｜ 单元：Rt_NexusDevices ｜ 自有 21 个方法、9 个属性

property AddressWidth: LongWord read GetAddressWidth write SetAddressWidth;
property BusName: TDynamicString read GetBusName write SetBusName;
property BusType: TDynamicString read GetBusType write SetBusType;
property Description: TDynamicString read GetDescription write SetDescription;
property Designator: TDynamicString read GetDesignator write SetDesignator;
property DeviceMemoryIndex: LongWord read GetDeviceMemoryIndex write SetDeviceMemoryIndex;
property IsMappedIO: Boolean read GetIsMappedIO write SetIsMappedIO;
property Size: LongWord read GetSize write SetSize;
property StartAddress: LongWord read GetStartAddress write SetStartAddress;
function AddLogicalSection(ANewMap: IDeviceMemoryLogicalSection): Integer;
function GetAddressWidth: Cardinal;
function GetBusName: string;
function GetBusType: string;
function GetChildMap(AIndex: Cardinal): IDeviceMemoryLogicalSection;
function GetChildMapCount: Cardinal;
function GetDescription: string;
function GetDesignator: string;
function GetDeviceMemoryIndex: Cardinal;
function GetIsMappedIO: Boolean;
function GetSize: Cardinal;
function GetStartAddress: Cardinal;
procedure SetAddressWidth(AValue: Cardinal);
procedure SetBusName(AValue: string);
procedure SetBusType(AValue: string);
procedure SetDescription(AValue: string);
procedure SetDesignator(AValue: string);
procedure SetDeviceMemoryIndex(AValue: Cardinal);
procedure SetIsMappedIO(AValue: Boolean);
procedure SetSize(AValue: Cardinal);
procedure SetStartAddress(AValue: Cardinal);

## IDeviceMemoryInformation
继承：IDeviceMemoryInformation → IInterface ｜ 单元：Rt_NexusDevices ｜ 自有 10 个方法、0 个属性

function AddArchitectureSection(ANewMap: IDeviceMemoryArchitectureSection): Integer;
function AddDefaultSection(ANewMap: IDeviceMemoryLogicalSection): Integer;
function AddLogicalSection(ANewMap: IDeviceMemoryLogicalSection): Integer;
function GetArchitectureSection(AIndex: Cardinal): IDeviceMemoryArchitectureSection;
function GetArchitectureSectionCount: Cardinal;
function GetDefaultFlashLogicalSection: IDeviceMemoryLogicalSection;
function GetDefaultRAMLogicalSection: IDeviceMemoryLogicalSection;
function GetDefaultROMLogicalSection: IDeviceMemoryLogicalSection;
function GetLogicalSection(AIndex: Cardinal): IDeviceMemoryLogicalSection;
function GetLogicalSectionCount: Cardinal;

## IDeviceMemoryLogicalSection
继承：IDeviceMemoryLogicalSection → IInterface ｜ 单元：Rt_NexusDevices ｜ 自有 26 个方法、13 个属性

property BusName: TDynamicString read GetBusName write SetBusName;
property BusType: TDynamicString read GetBusType write SetBusType;
property Designator: TDynamicString read GetDesignator write SetDesignator;
property DeviceMemoryIndex: LongWord read GetDeviceMemoryIndex write SetDeviceMemoryIndex;
property IsDefault: Boolean read GetIsDefault write SetIsDefault;
property IsExternal: Boolean read GetIsExternal write SetIsExternal;
property MAU: LongWord read GetMAU write SetMAU;
property MemConfig: TDynamicString read GetMemConfig write SetMemConfig;
property ParentMap: IDeviceMemoryArchitectureSection read GetParentMap write SetParentMap;
property PhysicalType: TDynamicString read GetPhysicalType write SetPhysicalType;
property Size: LongWord read GetSize write SetSize;
property StartAddress: LongWord read GetStartAddress write SetStartAddress;
property UsageType: TDynamicString read GetUsageType write SetUsageType;
function GetBusName: string;
function GetBusType: string;
function GetDesignator: string;
function GetDeviceMemoryIndex: Cardinal;
function GetIsDefault: Boolean;
function GetIsExternal: Boolean;
function GetMAU: Cardinal;
function GetMemConfig: string;
function GetParentMap: IDeviceMemoryArchitectureSection;
function GetPhysicalType: string;
function GetSize: Cardinal;
function GetStartAddress: Cardinal;
function GetUsageType: string;
procedure SetBusName(AValue: string);
procedure SetBusType(AValue: string);
procedure SetDesignator(AValue: string);
procedure SetDeviceMemoryIndex(AValue: Cardinal);
procedure SetIsDefault(AValue: Boolean);
procedure SetIsExternal(AValue: Boolean);
procedure SetMAU(AValue: Cardinal);
procedure SetMemConfig(AValue: string);
procedure SetParentMap(AValue: IDeviceMemoryArchitectureSection);
procedure SetPhysicalType(AValue: string);
procedure SetSize(AValue: Cardinal);
procedure SetStartAddress(AValue: Cardinal);
procedure SetUsageType(AValue: string);

## IDevicePin
继承：IDevicePin → IInterface ｜ 单元：Rt_NexusDevices ｜ 自有 25 个方法、0 个属性

function GetClkDifferentialId: WideString;
function GetDifferentialId: WideString;
function GetIOBank: WideString;
function GetIOStandard(Index: Integer): IDeviceIOStandard;
function GetIOStandardCount: Integer;
function GetIsClkDiffN_Pin: Boolean;
function GetIsClkDiffP_Pin: Boolean;
function GetIsCLKPin: Boolean;
function GetIsDCIN_Pin: Boolean;
function GetIsDCIP_Pin: Boolean;
function GetIsDiffN_Pin: Boolean;
function GetIsDiffP_Pin: Boolean;
function GetIsDLLPin: Boolean;
function GetIsHDiffN_Pin: Boolean;
function GetIsHDiffP_Pin: Boolean;
function GetIsInputOnlyPin: Boolean;
function GetIsIOPin: Boolean;
function GetIsNegPinOfDiffPair: Boolean;
function GetIsPosPinOfDiffPair: Boolean;
function GetIsReceiveDiffPin: Boolean;
function GetIsSpecialPin: Boolean;
function GetIsTransmitDiffPin: Boolean;
function GetIsVREFPin: Boolean;
function GetPinNumber: WideString;
function GetUniqueDifferentialID: WideString;

## IDeviceProcessorInformation
继承：IDeviceProcessorInformation → IInterface ｜ 单元：Rt_NexusDevices ｜ 自有 5 个方法、0 个属性

function GetDeviceProcessorArchString: WideString;
function GetDeviceProcessorCoreString: WideString;
function GetDeviceProcessorFamilyString: WideString;
function GetDeviceProcessorToolChainString: WideString;
function GetDeviceProcessorToolChainTargetString: WideString;

## IDeviceSheet
继承：IDeviceSheet → IInterface ｜ 单元：Rt_AltiumLibrary ｜ 自有 1 个方法、1 个属性

property FilePath: WideString read Get_FilePath;  // read-only
function Get_FilePath: WideString;

## IDeviceSheetFolder
继承：IDeviceSheetFolder → IDMObject → IInterface ｜ 单元：RT_Workspace ｜ 自有 2 个方法、0 个属性

function DM_FolderPath: WideString;
function DM_IncludeSubFolders: Boolean;

## IDeviceSheetManager
继承：IDeviceSheetManager → IInterface ｜ 单元：RT_IntegratedLibrary ｜ 自有 16 个方法、0 个属性

function AddDeviceFolder(const AFolderPath: WideString; ASearchSubfolder: Boolean): Boolean;
function BrowseDeviceSheet(var AFileName: WideString; out AFilePath: WideString): Boolean;
function ChooseDeviceFolder(var AFolderPath: WideString): Boolean;
procedure ClearFolders;
function ConvertDeviceSheetPathToName(const AFilePath: WideString): WideString;
procedure DeleteFolder(AIndex: Integer);
procedure EditDeviceFolderList;
function FindAllDeviceSheetPaths(const AFileName: WideString; out AOtherMatchingPaths: WideString): WideString;
function FindDeviceSheetPath(const AFileName: WideString): WideString;
function GetCurrentProject: IProject;
function GetFolders_FolderPath(AIndex: Integer): WideString;
function GetFolders_SearchSubFolders(AIndex: Integer): Boolean;
function GetFoldersCount: Integer;
procedure MakeCurrentProject(AProject: IProject);
procedure SetDeviceFolder(AIndex: Integer; const AFolderPath: WideString; ASearchSubfolder: Boolean);
function WillSearchDeviceFolder(const AFolderPath: WideString): Boolean;

## IDifferentialPair
继承：IDifferentialPair → IObjectClass → IDMObject → IInterface ｜ 单元：RT_Workspace ｜ 自有 2 个方法、0 个属性

function DM_NegativeNet: INet;
function DM_PositiveNet: INet;

## IDifferentialPairClass
继承：IDifferentialPairClass → IObjectClass → IDMObject → IInterface ｜ 单元：RT_Workspace ｜ 自有 0 个方法、0 个属性


## IDispatch
继承：IDispatch → IInterface ｜ 单元：System ｜ 自有 2 个方法、0 个属性

function GetTypeInfo(Index: Integer; LocaleID: Integer; out TypeInfo): HRESULT;
function GetTypeInfoCount(out Count: Integer): HRESULT;

## IDocHostUIHandler
继承：IDocHostUIHandler → IInterface ｜ 单元：XPExtCtrls ｜ 自有 10 个方法、0 个属性

function EnableModeless(const fEnable: LongBool): HRESULT;
function FilterDataObject(const pDO: IDataObject; out ppDORet: IDataObject): HRESULT;
function GetDropTarget(const pDropTarget: IDropTarget; out ppDropTarget: IDropTarget): HRESULT;
function GetExternal(out ppDispatch: IDispatch): HRESULT;
function GetHostInfo(const pInfo: IDispatch): HRESULT;
function HideUI: HRESULT;
function OnDocWindowActivate(const fActivate: LongBool): HRESULT;
function OnFrameWindowActivate(const fActivate: LongBool): HRESULT;
function ShowUI(const dwID: Cardinal; const pActiveObject: IOleInPlaceActiveObject; const pCommandTarget: IOleCommandTarget; const pFrame: IOleInPlaceFrame; const pDoc: IOleInPlaceUIWindow): HRESULT;
function UpdateUI: HRESULT;

## IDockManager
继承：IDockManager → IInterface ｜ 单元：Vcl.Controls ｜ 自有 11 个方法、0 个属性

procedure BeginUpdate;
procedure EndUpdate;
procedure GetControlBounds(Control: TControl; const CtlBounds: IDispatch);
procedure InsertControl(Control: TControl; InsertAt: TAlign; DropCtl: TControl);
procedure LoadFromStream(Stream: TStream);
procedure PaintSite(DC: HDC);
procedure PositionDockRect(Client: TControl; DropCtl: TControl; DropAlign: TAlign; const DockRect: IDispatch);
procedure RemoveControl(Control: TControl);
procedure ResetBounds(Force: Boolean);
procedure SaveToStream(Stream: TStream);
procedure SetReplacingControl(Control: TControl);

## IDocument
继承：IDocument → IDMObject → IInterface ｜ 单元：RT_Workspace ｜ 自有 117 个方法、0 个属性

function DM_AnnotationOptions: IDocumentAnnotationOptions;
function DM_BlanketCount: Integer;
function DM_Blankets(Index: Integer): IBlanket;
function DM_BusCount: Integer;
function DM_Buses(Index: Integer): IBus;
function DM_ChannelClassCount: Integer;
function DM_ChannelClasses(Index: Integer): IChannelClass;
function DM_ChannelIndex: Integer;
function DM_ChannelPrefix: WideString;
function DM_ChannelRoomNamingStyle: TChannelRoomNamingStyle;
function DM_ChildDocumentCount: Integer;
function DM_ChildDocumentCountIgnoreScope: Integer;
function DM_ChildDocuments(Index: Integer): IDocument;
function DM_ChildDocumentsIgnoreScope(Index: Integer): IDocument;
function DM_ClassClusterCount: Integer;
function DM_ClassClusters(Index: Integer): IObjectClassCluster;
function DM_Compile: LongBool;
function DM_ComponentClassCount: Integer;
function DM_ComponentClasses(Index: Integer): IComponentClass;
function DM_ComponentCount: Integer;
function DM_Components(Index: Integer): IComponent;
function DM_ConstraintGroupCount: Integer;
function DM_ConstraintGroups(Index: Integer): IConstraintGroup;
function DM_CreateViolation(AErrorKind: TErrorKind; AErrorString: WideString): IViolation;
function DM_CrossSheetConnectorCount: Integer;
function DM_CrossSheetConnectors(Index: Integer): ICrossSheet;
function DM_CurrentInstanceNumber: Integer;
function DM_DifferentialPairClassCount: Integer;
function DM_DifferentialPairClasses(Index: Integer): IDifferentialPairClass;
function DM_DifferentialPairCount: Integer;
function DM_DifferentialPairs(Index: Integer): IDifferentialPair;
function DM_DocumentID: WideString;
function DM_DocumentIsLoaded: Boolean;
function DM_DocumentIsTextual: Boolean;
function DM_DocumentKind: WideString;
procedure DM_DocumentLoaded;
function DM_FileName: WideString;
function DM_FSMClockPort: INetItem;
function DM_FSMResetPort: INetItem;
function DM_FSMState(Index: Integer): IDM_FSMState;
function DM_FSMStateCount: Integer;
function DM_FSMTransition(Index: Integer): IDM_FSMTransition;
function DM_FSMTransitionCount: Integer;
function DM_FullPath: WideString;
function DM_GetDocumentForECO: IDocument;
function DM_GetItemRevisionGUID: WideString;
function DM_GetNet(const ObjectHandle: WideString): INet;
function DM_GetNetProperties(const ObjectHandle: WideString): INetProperties;
function DM_GetReferenceObjectManager: IReferenceObjectManager;
function DM_GetRequiredCapabilities(ACapabilities: ICapabilityList): Boolean;
function DM_GetState_DocDisplayName: WideString;
function DM_HarnessConnectorCount: Integer;
function DM_HarnessConnectors(Index: Integer): ISheetSymbol;
function DM_HarnessNetCount: Integer;
function DM_HarnessNets(Index: Integer): INet;
function DM_IndentLevel: Integer;
function DM_IsDeviceSheet: Boolean;
function DM_IsDocumentFileLessEditing: Boolean;
function DM_IsPhysicalDocument: Boolean;
function DM_IsPrimaryImplementationDocument: Boolean;
function DM_IsRequired: Boolean;
function DM_IsVirtualDocument: Boolean;
function DM_LoadDocument: Boolean;
function DM_LogicalDocument: IDocument;
function DM_ModelKind: WideString;
function DM_NeedsScrapCompile: Boolean;
function DM_NetClassCount: Integer;
function DM_NetClasses(Index: Integer): INetClass;
function DM_NetCount: Integer;
function DM_Nets(Index: Integer): INet;
function DM_NoteCount: Integer;
function DM_Notes(Index: Integer): INote;
function DM_ObjectRevisionId: WideString;
function DM_OpenAndFocusDocument: Boolean;
function DM_ParentDocumentCount: Integer;
function DM_ParentDocuments(Index: Integer): IDocument;
function DM_ParentSheetSymbolCount: Integer;
function DM_ParentSheetSymbols(Index: Integer): ISheetSymbol;
function DM_PartAnnotateCount: Integer;
function DM_PartCount: Integer;
function DM_Parts(Index: Integer): IPart;
function DM_PartsAnnotate(Index: Integer): IPart;
function DM_PhysicalDocument(Index: Integer): IDocument;
function DM_PhysicalDocumentCount: Integer;
function DM_PhysicalDocumentParent: IDocument;
function DM_PhysicalInstanceName: WideString;
function DM_PhysicalInstancePath: WideString;
function DM_PhysicalRoomName: WideString;
function DM_PortCount: Integer;
function DM_Ports(Index: Integer): INetItem;
function DM_Project: IProject;
function DM_ReuseBlocks: IReuseBlocks;
function DM_RoomCount: Integer;
function DM_Rooms(Index: Integer): IRoom;
function DM_RuleCount: Integer;
function DM_Rules(Index: Integer): IRule;
function DM_ScrapCompile(ForceCompile: Boolean): LongBool;
function DM_ScrapCompileWithOptions(ForceCompile: Boolean; AOptions: WideString): LongBool;
function DM_ServerDocument: IServerDocument;
procedure DM_SetItemRevisionGUID(S: WideString);
function DM_SheetSizeX: Integer;
function DM_SheetSizey: Integer;
function DM_SheetSymbolCount: Integer;
function DM_SheetSymbols(Index: Integer): ISheetSymbol;
function DM_SignalManager: ISignalManager;
function DM_SmartLoad: Boolean;
function DM_SpatialAnalysis(Force: Boolean; AllowAbort: Boolean; AbortOnMouseMove: Boolean): Boolean;
function DM_SpatialAnalysisForTest: Integer;
function DM_TextFrameCount: Integer;
function DM_TextFrames(Index: Integer): ITextFrame;
function DM_UniqueComponentCount: Integer;
function DM_UniqueComponents(Index: Integer): IComponent;
function DM_UniquePartCount: Integer;
function DM_UniqueParts(Index: Integer): IPart;
procedure DM_UpdateDateModified;
function DM_VHDLEntities(Index: Integer): IVHDLEntity;
function DM_VHDLEntityCount: Integer;

## IDocumentAnnotationOptions
继承：IDocumentAnnotationOptions → IInterface ｜ 单元：RT_Workspace ｜ 自有 12 个方法、6 个属性

property AnnotationEnabled: Boolean read GetAnnotationEnabled write SetAnnotationEnabled;
property AnnotationIndexControlEnabled: Boolean read GetAnnotationIndexControlEnabled write SetAnnotationIndexControlEnabled;
property AnnotationOrder: Integer read GetAnnotationOrder write SetAnnotationOrder;
property AnnotationScope: TDocAnnotationScope read GetAnnotationScope write SetAnnotationScope;
property AnnotationStartValue: Integer read GetAnnotationStartValue write SetAnnotationStartValue;
property AnnotationSuffix: WideString read GetAnnotationSuffix write SetAnnotationSuffix;
function GetAnnotationEnabled: Boolean;
function GetAnnotationIndexControlEnabled: Boolean;
function GetAnnotationOrder: Integer;
function GetAnnotationScope: TDocAnnotationScope;
function GetAnnotationStartValue: Integer;
function GetAnnotationSuffix: WideString;
procedure SetAnnotationEnabled(AValue: Boolean);
procedure SetAnnotationIndexControlEnabled(AValue: Boolean);
procedure SetAnnotationOrder(AValue: Integer);
procedure SetAnnotationScope(AValue: TDocAnnotationScope);
procedure SetAnnotationStartValue(AValue: Integer);
procedure SetAnnotationSuffix(const AValue: WideString);

## IDocumentClassGenerationOptions
继承：IDocumentClassGenerationOptions → IInterface ｜ 单元：RT_Workspace ｜ 自有 9 个方法、4 个属性

property CompClassAutoEnabled: Boolean read GetCompClassAutoEnabled write SetCompClassAutoEnabled;
property CompClassAutoRoomEnabled: Boolean read GetCompClassAutoRoomEnabled write SetCompClassAutoRoomEnabled;
property GenerateClassCluster: Boolean read GetGenerateClassCluster write SetGenerateClassCluster;
property NetClassAutoScope: TDocAutoNetClassScope read GetNetClassAutoScope write SetNetClassAutoScope;
function GetCompClassAutoEnabled: Boolean;
function GetCompClassAutoRoomEnabled: Boolean;
function GetGenerateClassCluster: Boolean;
function GetNetClassAutoScope: TDocAutoNetClassScope;
procedure ResetToDefaultState;
procedure SetCompClassAutoEnabled(AValue: Boolean);
procedure SetCompClassAutoRoomEnabled(AValue: Boolean);
procedure SetGenerateClassCluster(AValue: Boolean);
procedure SetNetClassAutoScope(AValue: TDocAutoNetClassScope);

## IDocumentDragDropInfo
继承：IDocumentDragDropInfo → IDragDropObject ｜ 单元：RT_ClientServerInterface ｜ 自有 2 个方法、0 个属性

function GetDocumentKind: WideString;
function GetDocumentPath: WideString;

## IDocumentFormNotification
继承：IDocumentFormNotification → INotification → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 2 个方法、2 个属性

property Code: Integer read GetCode;  // read-only
property Handle: THandle read GetHandle;  // read-only
function GetCode: Integer;
function GetHandle: NativeUInt;

## IDocumentFormNotification2
继承：IDocumentFormNotification2 → IDocumentFormNotification → INotification → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 1 个方法、1 个属性

property FormId: Integer read GetFormId;  // read-only
function GetFormId: Integer;

## IDocumentNotification
继承：IDocumentNotification → INotification → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 3 个方法、3 个属性

property Code: Integer read GetCode;  // read-only
property OldFileName: WideString read GetFileName;  // read-only
property ServerDocument: IServerDocument read GetServerDocument;  // read-only
function GetCode: Integer;
function GetFileName: WideString;
function GetServerDocument: IServerDocument;

## IDocumentOptionsSet
继承：IDocumentOptionsSet → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 6 个方法、0 个属性

function GetHostServer: WideString;
function GetSetName: WideString;
function GetSortName: WideString;
function IsAllDocuments: Boolean;
function IsAllProjects: Boolean;
function IsForDocumentKind(const AKind: WideString): Boolean;

## IDocumentOptionsView
继承：IDocumentOptionsView → IExternalForm → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 7 个方法、0 个属性

function CanClose: Boolean;
function GetControlState(AId: string): string;
procedure Initialize(const ADocumentPath: WideString);
procedure Save;
procedure SetControlState(AId: string; AValue: string);
procedure SetState_Default;
function SupportsDefaults: Boolean;

## IDocumentPreviewHint
继承：IDocumentPreviewHint → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 6 个方法、2 个属性

property ActivatedPath: WideString read Get_ActivatedPath;  // read-only
property ActivatedPos: TPoint read Get_ActivatedPos;  // read-only
procedure ActivateDocumentChooser(const AProjectPath: WideString; const APos: IDispatch);
procedure ActivateDocumentPath(const ADocumentPath: WideString; const APos: IDispatch);
procedure ActivateDocumentPreview(const ADocumentPath: WideString; const APos: IDispatch; AMouseGap: Integer);
procedure DeActivate(AImmediate: Boolean);
function Get_ActivatedPath: WideString;
function Get_ActivatedPos: IDispatch;

## IDocumentPreviewManager
继承：IDocumentPreviewManager → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 4 个方法、0 个属性

function CreatePreviewImage: IPreviewImage;
function FindPreview(const ADocumentPath: WideString; AForceGeneration: Boolean): IPreviewImage;
procedure InvalidatePreview(const AServerDocument: IServerDocument);
procedure SavePreview(const AServerDocument: IServerDocument; AForceGeneration: Boolean);

## IDocumentRenamedNotification
继承：IDocumentRenamedNotification → IDocumentNotification → INotification → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 2 个方法、2 个属性

property NewFileName: WideString read GetNewFileName;  // read-only
property ProjectFileName: WideString read GetProjectFileName;  // read-only
function GetNewFileName: WideString;
function GetProjectFileName: WideString;

## IDocumentRequest
继承：IDocumentRequest → INotification → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 4 个方法、3 个属性

property Code: Integer read GetCode;  // read-only
property RequestResult: Integer read GetRequestResult write SetRequestResult;
property ServerDocument: IServerDocument read GetServerDocument;  // read-only
function GetCode: Integer;
function GetRequestResult: Integer;
function GetServerDocument: IServerDocument;
procedure SetRequestResult(aResult: Integer);

## IDocumentStructure
继承：IDocumentStructure → IInterface ｜ 单元：RT_Workspace ｜ 自有 8 个方法、0 个属性

function DM_GetDesignItemId: WideString;
function DM_GetDocStructureForPath(const Path: WideString): IDocumentStructure;
function DM_GetDocument: IDocument;
function DM_GetLogicalSubStructure(Index: Integer): IDocumentStructure;
function DM_GetLogicalSubStructureCount: Integer;
function DM_GetSourceDocument(Index: Integer): IDocument;
function DM_GetSourceDocumentCount: Integer;
function DM_GetSourceLibraryName: WideString;

## IDocumentViewChangeFocus
继承：IDocumentViewChangeFocus → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 1 个方法、0 个属性

procedure SetFocusTo(const ActivityName: WideString);

## IDragDropDataSheets
继承：IDragDropDataSheets → IDragDropObject ｜ 单元：RT_SupplierManager ｜ 自有 2 个方法、1 个属性

property DataSheetURL[I: Integer]: WideString read GetDataSheetURL;  // read-only
function DataSheetCount: Integer;
function GetDataSheetURL(I: Integer): WideString;

## IDragDropNotification
继承：IDragDropNotification → INotification → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 2 个方法、0 个属性

function GetCode: Integer;
function GetDragDropObject: IDragDropObject;

## IDragDropParameters
继承：IDragDropParameters → IDragDropObject ｜ 单元：RT_SupplierManager ｜ 自有 2 个方法、1 个属性

property Parameter[I: Integer]: IItemParameter read GetParameter;  // read-only
function GetParameter(I: Integer): IItemParameter;
function ParameterCount: Integer;

## IDragDropSupplierSourceRelationships
继承：IDragDropSupplierSourceRelationships → IDragDropObject ｜ 单元：RT_SupplierManager ｜ 自有 2 个方法、1 个属性

property SupplierSourceRelationship[I: Integer]: ISupplierSourceRelationship read GetSupplierSourceRelationship;  // read-only
function GetSupplierSourceRelationship(I: Integer): ISupplierSourceRelationship;
function SupplierSourceRelationshipCount: Integer;

## IDrillPairInfo
继承：IDrillPairInfo → IInterface ｜ 单元：Rt_LayerStackManager.Interfaces ｜ 自有 5 个方法、0 个属性

function GetState_IsBackDrill: Boolean;
function GetState_IsMicroVia: Boolean;
function GetState_Name: WideString;
function GetState_StartLayerId: Integer;
function GetState_StopLayerId: Integer;

## IDriverManager
继承：IDriverManager → IInterface ｜ 单元：Rt_NexusDevices ｜ 自有 2 个方法、0 个属性

function GetAllDevices: IInterfaceList;
function GetDeviceInterface(DeviceName: WideString): INexusDevice;

## IDynamicHelpManager
继承：IDynamicHelpManager → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 5 个方法、0 个属性

function AddCustomContent(const ASectionName: WideString; const ASectionBody: WideString): NativeInt;
function GetCustomSectionBody(Index: Integer): WideString;
function GetCustomSectionName(Index: Integer): WideString;
function GetCustomSectionsCount: Integer;
procedure RemoveCustomContent(AnID: NativeInt);

## IECO
继承：IECO → IInterface ｜ 单元：RT_Workspace ｜ 自有 6 个方法、0 个属性

function DM_AddMemberToObject(Mode: TECO_Mode; ReferenceMember: IDMObject; ReferenceParent: IDMObject; TargetParent: IDMObject): Boolean;
function DM_AddObject(Mode: TECO_Mode; ReferenceObject: IDMObject): Boolean;
procedure DM_Begin;
procedure DM_End;
function DM_RemoveMemberFromObject(Mode: TECO_Mode; MemberObject: IDMObject; ParentObject: IDMObject): Boolean;
function DM_RemoveObject(Mode: TECO_Mode; ObjectToRemove: IDMObject): Boolean;

## IEDMS_CommentThreadHolder
继承：IEDMS_CommentThreadHolder → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 5 个方法、5 个属性

property CommentThreadData: WideString read GetCommentThreadData;  // read-only
property CommentThreadGUID: WideString read GetCommentThreadGUID;  // read-only
property IsSharedWithMeProject: LongBool read GetIsSharedWithMeProject;  // read-only
property ManagedProjectGUID: WideString read GetManagedProjectGUID;  // read-only
property ServerGUID: WideString read GetServerGUID;  // read-only
function GetCommentThreadData: WideString;
function GetCommentThreadGUID: WideString;
function GetIsSharedWithMeProject: LongBool;
function GetManagedProjectGUID: WideString;
function GetServerGUID: WideString;

## IEDM_Notification
继承：IEDM_Notification → INotification → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 4 个方法、4 个属性

property Code: Integer read GetCode;  // read-only
property ContentTypeGUID: WideString read GetContentTypeGUID;  // read-only
property DItemGUID: WideString read GetDItemGUID;  // read-only
property DItemRevisionGUID: WideString read GetDItemRevisionGUID;  // read-only
function GetCode: Integer;
function GetContentTypeGUID: WideString;
function GetDItemGUID: WideString;
function GetDItemRevisionGUID: WideString;

## IEditComponentVariantDialog
继承：IEditComponentVariantDialog → IInterface ｜ 单元：RT_Workspace ｜ 自有 1 个方法、0 个属性

function Run(ALibraryLink: IComponentLibraryLink; var AVariationKind: TVariationKind; const ATestSchComp: IInterface; ALibLinkOnly: Boolean): Boolean;

## IEditGridLinkObserver
继承：IEditGridLinkObserver → IEditLinkObserver → ISingleCastObserver → IObserver → IInterface ｜ 单元：System.Classes ｜ 自有 1 个方法、1 个属性

property Current: TVarRec read GetCurrent;  // read-only
function GetCurrent: IDispatch;

## IEditLinkObserver
继承：IEditLinkObserver → ISingleCastObserver → IObserver → IInterface ｜ 单元：System.Classes ｜ 自有 13 个方法、3 个属性

property IsEditing: Boolean read GetIsEditing;  // read-only
property IsReadOnly: Boolean read GetIsReadOnly write SetIsReadOnly;
property Updating: Boolean read GetUpdating;  // read-only
procedure BeginUpdate;
function Edit: Boolean;
procedure EndUpdate;
function GetIsEditing: Boolean;
function GetIsReadOnly: Boolean;
function GetUpdating: Boolean;
function IsModified: Boolean;
function IsRequired: Boolean;
function IsValidChar(AKey: Char): Boolean;
procedure Modified;
procedure Reset;
procedure SetIsReadOnly(Value: Boolean);
procedure Update;

## IEditVHDLWaveNotify
继承：IEditVHDLWaveNotify → IInterface ｜ 单元：Rt_VHDL ｜ 自有 2 个方法、0 个属性

function DocumentClosing: Boolean;
function RemoveFromWave(SignalName: PWideChar): Boolean;

## IEmbeddableDocument
继承：IEmbeddableDocument → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 6 个方法、3 个属性

property FileNameForSave: WideString read GetFileNameForSave write SetFileNameForSave;
property LibReferences: WideString read GetLibReferences write SetLibReferences;
property ParentDocumentFileName: WideString read GetParentDocumentFileName write SetParentDocumentFileName;
function GetFileNameForSave: WideString;
function GetLibReferences: WideString;
function GetParentDocumentFileName: WideString;
procedure SetFileNameForSave(const FileName: WideString);
procedure SetLibReferences(const Value: WideString);
procedure SetParentDocumentFileName(const FileName: WideString);

## IEmbeddedConfiguration
继承：IEmbeddedConfiguration → IVaultConfiguration → IConfiguration → IBaseConfiguration → IDMObject → IInterface ｜ 单元：RT_Workspace ｜ 自有 5 个方法、0 个属性

procedure DM_CreateStorageConstraintFile;
function DM_DeviceFullName: WideString;
function DM_DeviceMemory: WideString;
function DM_DeviceName: WideString;
function DM_OptionsStorage: IOptionsStorage;

## IEmbeddedDebugConsole
继承：IEmbeddedDebugConsole → IInterface ｜ 单元：RT_Debugger ｜ 自有 2 个方法、0 个属性

function Command_ExecuteInternal(aCommand: WideString): WideString;
function WaitForDebugger(aMilliseconds: Cardinal): Boolean;

## IEmbeddedDebugger
继承：IEmbeddedDebugger → IDebugger → IInterface ｜ 单元：RT_Debugger ｜ 自有 4 个方法、0 个属性

function Session_DeviceIsRunning(const ADeviceID: WideString): Boolean;
function Session_IsDebugging(const AProjectSource: WideString): Boolean;
function Session_IsRunning(const AProjectSource: WideString; const ADeviceID: WideString; AIsSimulation: Boolean): Boolean;
function Session_ProjectIsRunning(const AProjectSource: WideString): Boolean;

## IEmbeddedParser
继承：IEmbeddedParser → IInterface ｜ 单元：RT_Debugger ｜ 自有 1 个方法、0 个属性

function GetModuleInfo(const aFileName: WideString): IModuleInfo;

## IEmbeddedProject
继承：IEmbeddedProject → IProject → IDMObject → IInterface ｜ 单元：RT_Workspace ｜ 自有 10 个方法、0 个属性

procedure DM_Abort;
function DM_CompileASP(ARebuild: LongBool): LongBool;
function DM_CompileAspWithParameters(const Parameters: WideString; ARebuild: LongBool): LongBool;
function DM_GetDeviceMemory: WideString;
function DM_GetDeviceName: WideString;
function DM_GetEmbeddedStackPath: WideString;
function DM_GetToolchain: WideString;
function DM_GetToolchainManager: IInterface;
procedure DM_InvalidateToolchain;
procedure DM_SetDeviceName(const ADeviceName: WideString);

## IEntityPort
继承：IEntityPort → ISignalNode → IDMObject → IInterface ｜ 单元：RT_Workspace ｜ 自有 0 个方法、0 个属性


## IEvent
继承：IEvent → IInterface ｜ 单元：Rt_VHDL ｜ 自有 1 个方法、0 个属性

function GetLogicSimValue: Pointer;

## IEventNavigated
继承：IEventNavigated → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 2 个方法、2 个属性

property Code: Integer read GetCode;  // read-only
property Wnd: THandle read GetWnd;  // read-only
function GetCode: Integer;
function GetWnd: NativeUInt;

## IExportDocument
继承：IExportDocument → IInterface ｜ 单元：RT_Workspace ｜ 自有 1 个方法、0 个属性

function FileExport(const AFileName: WideString; const AFormat: WideString): LongBool;

## IExternalActionItem
继承：IExternalActionItem → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 0 个方法、0 个属性


## IExternalActionItemList
继承：IExternalActionItemList → IInterfaceList → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 6 个方法、2 个属性

property ActionItem[AIndex: Integer]: IExternalActionItem read GetActionItem;  // read-only
property ActionItemCount: Integer read GetActionItemCount;  // read-only
function Execute: LongBool;
function GetActionItem(AIndex: Integer): IExternalActionItem;
function GetActionItemCount: Integer;
function GetCaption: WideString;
function GetEnabled: LongBool;
function GetVisible: LongBool;

## IExternalFileInfo
继承：IExternalFileInfo → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 2 个方法、0 个属性

function FileName: WideString;
function UsedIn: WideString;

## IExternalFiles
继承：IExternalFiles → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 2 个方法、0 个属性

function Count: Integer;
function GetFileInfo(AIndex: Integer): IExternalFileInfo;

## IExternalForm
继承：IExternalForm → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 11 个方法、2 个属性

property Caption: WideString read GetCaption;  // read-only
property Handle: HWND read GetHandle;  // read-only
procedure FocusFirstTabStop;
procedure GetBounds(var ALeft: Integer; var ATop: Integer; var AWidth: Integer; var AHeight: Integer);
function GetCaption: WideString;
function GetHandle: HWND;
procedure Hide;
procedure ParentWindowCreated;
procedure ParentWindowDestroyed;
procedure SetBounds(ALeft: Integer; ATop: Integer; AWidth: Integer; AHeight: Integer);
procedure SetFocus;
procedure SetParentWindow(const ParentWindow: IExternalFormHolder);
procedure Show;

## IExternalForm2
继承：IExternalForm2 → IExternalForm → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 2 个方法、1 个属性

property OwnerId: Integer read GetOwnerId write SetOwnerId;
function GetOwnerId: Integer;
procedure SetOwnerId(AOwnerId: Integer);

## IExternalFormHolder
继承：IExternalFormHolder → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 3 个方法、0 个属性

function GetParentWindow: NativeUInt;
procedure SetDialogHandle(AHandle: NativeUInt);
procedure UpdateCaption;

## IExternalFormHolderControl
继承：IExternalFormHolderControl → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 2 个方法、1 个属性

property Visible: Boolean read GetVisible write SetVisible;
function GetVisible: Boolean;
procedure SetVisible(AValue: Boolean);

## IExternalPaint
继承：IExternalPaint → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 2 个方法、0 个属性

function GetIconName: WideString;
function PaintThumbnail(ADC: HDC): Boolean;

## IExternalParameter
继承：IExternalParameter → IInterface ｜ 单元：RT_Workspace ｜ 自有 4 个方法、0 个属性

function DM_GetName: WideString;
function DM_GetSection: WideString;
function DM_GetValue: WideString;
procedure DM_SetValue(AValue: WideString);

## IFPGAProject
继承：IFPGAProject → IAbstractVHDLProject → IProject → IDMObject → IInterface ｜ 单元：RT_Workspace ｜ 自有 1 个方法、0 个属性

function DM_GetTargetBoardName(ConfigurationName: WideString): WideString;

## IFeatureChecker
继承：IFeatureChecker → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 2 个方法、0 个属性

procedure CheckFeature(const AData: WideString);
function IsEnabled: Boolean;

## IFieldLink
继承：IFieldLink → IInterface ｜ 单元：RT_Workspace ｜ 自有 11 个方法、0 个属性

function GetAddMode: TParameterAddMode;
function GetDataType: TFieldType;
function GetFieldName: WideString;
function GetFieldType: TFieldKeyType;
function GetLookupValue: WideString;
function GetParameterName: WideString;
function GetRemoveMode: TParameterRemoveMode;
function GetUpdateMode: TParameterUpdateMode;
function GetVisibleOnAdd: Boolean;
function IsDefault: Boolean;
function IsSystemParameter: Boolean;

## IFileLessViolationDescription
继承：IFileLessViolationDescription → IInterface ｜ 单元：RT_Workspace ｜ 自有 15 个方法、7 个属性

property Description: WideString read GetDescription write SetDescription;
property Group: TFileLessViolationGroup read GetGroup write SetGroup;
property GUID: WideString read GetGUID write SetGUID;
property Implementer: WideString read GetImplementer write SetImplementer;
property IsExternal: Boolean read GetIsExternal write SetIsExternal;
property Kind: TFileLessViolationKind read GetKind write SetKind;
property Level: TErrorLevel read GetLevel write SetLevel;
function Clone: IFileLessViolationDescription;
function GetDescription: WideString;
function GetGroup: TFileLessViolationGroup;
function GetGUID: WideString;
function GetImplementer: WideString;
function GetIsExternal: Boolean;
function GetKind: TFileLessViolationKind;
function GetLevel: TErrorLevel;
procedure SetDescription(const AValue: WideString);
procedure SetGroup(AValue: TFileLessViolationGroup);
procedure SetGUID(const AValue: WideString);
procedure SetImplementer(const AValue: WideString);
procedure SetIsExternal(AValue: Boolean);
procedure SetKind(AValue: TFileLessViolationKind);
procedure SetLevel(AValue: TErrorLevel);

## IFloatingWindow
继承：IFloatingWindow → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 5 个方法、0 个属性

procedure DoneTransparent;
function GetHandle: NativeUInt;
function GetVisible: Boolean;
procedure InitTransparent;
procedure SetTransparencyLevel(Value: Integer);

## IFootprintConfigurator
继承：IFootprintConfigurator → IInterface ｜ 单元：RT_ComponentConfigurator ｜ 自有 0 个方法、0 个属性


## IFreeDocumentsProject
继承：IFreeDocumentsProject → IProject → IDMObject → IInterface ｜ 单元：RT_Workspace ｜ 自有 1 个方法、0 个属性

function DM_GetHarnessDefinitionList: IHarnessDefinitionList;

## IFrequencyCounterChannel
继承：IFrequencyCounterChannel → IInterface ｜ 单元：RT_FrequencyCounter ｜ 自有 11 个方法、5 个属性

property EdgePolarity: TEdgePolarity read GetEdgePolarity write SetEdgePolarity;
property Gating: Double read GetGating write SetGating;
property Measured: Double read GetMeasured;  // read-only
property MeasureMode: TMeasureMode read GetMeasureMode write SetMeasureMode;
property Suspended: LongBool read GetSuspended write SetSuspended;
function GetEdgePolarity: TEdgePolarity;
function GetGating: Double;
function GetMeasured: Double;
function GetMeasureMode: TMeasureMode;
function GetSuspended: LongBool;
function IsReset: LongBool;
procedure Reset;
procedure SetEdgePolarity(AValue: TEdgePolarity);
procedure SetGating(AValue: Double);
procedure SetMeasureMode(AValue: TMeasureMode);
procedure SetSuspended(AValue: LongBool);

## IFrequencyCounterInstrument
继承：IFrequencyCounterInstrument → IScriptedInstrument → IInterface ｜ 单元：RT_FrequencyCounter ｜ 自有 4 个方法、3 个属性

property ChannelA: IFrequencyCounterChannel read GetChannelA;  // read-only
property ChannelB: IFrequencyCounterChannel read GetChannelB;  // read-only
property TimeBase: Cardinal read GetTimeBase write SetTimeBase;
function GetChannelA: IFrequencyCounterChannel;
function GetChannelB: IFrequencyCounterChannel;
function GetTimeBase: Cardinal;
procedure SetTimeBase(AValue: Cardinal);

## IFrequencyCounterInstrumentManager
继承：IFrequencyCounterInstrumentManager → IScriptedInstrumentManager → IInterface ｜ 单元：RT_FrequencyCounter ｜ 自有 4 个方法、0 个属性

function GetInstrument(Index: Integer): IFrequencyCounterInstrument;
function GetInstrumentByDesignator(const ADesignator: WideString): IFrequencyCounterInstrument;
function GetInstrumentByJtagIndex(AJtagIndex: Integer): IFrequencyCounterInstrument;
function GetInstrumentCount: Integer;

## IFrequencyGeneratorInstrument
继承：IFrequencyGeneratorInstrument → IScriptedInstrument → IInterface ｜ 单元：RT_FrequencyGenerator ｜ 自有 7 个方法、3 个属性

property Frequency: Double read GetFrequency write SetFrequency;
property Suspended: LongBool read GetSuspended write SetSuspended;
property TimeBase: Cardinal read GetTimeBase write SetTimeBase;
function GetFrequency: Double;
function GetSuspended: LongBool;
function GetTimeBase: Cardinal;
procedure SetFrequency(AValue: Double);
procedure SetSuspended(AValue: LongBool);
procedure SetTimeBase(AValue: Cardinal);
procedure SetTimeBaseEx(AValue: Cardinal; AEvenDutyCycle: LongBool);

## IFrequencyGeneratorInstrumentManager
继承：IFrequencyGeneratorInstrumentManager → IScriptedInstrumentManager → IInterface ｜ 单元：RT_FrequencyGenerator ｜ 自有 4 个方法、0 个属性

function GetInstrument(Index: Integer): IFrequencyGeneratorInstrument;
function GetInstrumentByDesignator(const ADesignator: WideString): IFrequencyGeneratorInstrument;
function GetInstrumentByJtagIndex(AJtagIndex: Integer): IFrequencyGeneratorInstrument;
function GetInstrumentCount: Integer;

## IGPIOChannel
继承：IGPIOChannel → IDeviceChannel → IInterface ｜ 单元：Rt_NexusDevices ｜ 自有 3 个方法、0 个属性

function GPIO_GetValue(APort: Integer): Byte;
procedure GPIO_SetPinsDir(APort: Integer; APinsDir: Byte);
procedure GPIO_SetValue(APort: Byte; AValue: Byte);

## IGUIManager
继承：IGUIManager → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 62 个方法、0 个属性

function AddKeyStrokeAndLaunch(AKey: Word): LongBool;
function AddKeyToBuffer(KeyId: Integer; Alt: LongBool; Shift: LongBool; Ctrl: LongBool): LongBool;
procedure BeginBulkClose;
procedure BeginDragDrop(ADragDropInfo: IDragDropObject);
function CanMovePanel(const AViewName: WideString): LongBool;
function CanResizePanel(const AViewName: WideString): LongBool;
function CurrentProcessLauncherAvailable: LongBool;
procedure DoneTransparentToolbars;
function Dragging: LongBool;
function DraggingAny: LongBool;
function DXPShortcutToDelphiShortcut(const AShortcutText: WideString): WideString;
function EditorVisibleForDocument(const ADocument: IServerDocument): Boolean;
procedure EndBulkClose;
function GetActionListFromTree(const TreeID: WideString): IExternalActionItemList;
function GetActivePLByCommand(const DocumentKind: WideString; const ACommand: WideString; const AParams: WideString): IProcessLauncherInfo;
procedure GetAllAvailableHotkeys(out Hotkeys: WideString; out Descriptions: WideString);
function GetCurrentFormHandle: HWND;
function GetFocusedPanelName: WideString;
function GetInUseUserRect(const AView: IServerDocumentView; const AUserId: WideString): IDispatch;
function GetNodeInfoByID(const ANodeName: WideString): WideString;
function GetPanelDockedHeight(const AViewName: WideString): Integer;
function GetPanelDockedWidth(const AViewName: WideString): Integer;
function GetPanelIsOpen(const AViewName: WideString): LongBool;
function GetPanelIsOpenInAnyForm(const AViewName: WideString): LongBool;
function GetPanelIsVisibleInAnyForm(const AViewName: WideString): LongBool;
function GetProcessLauncherInfoByID(const PLID: WideString): IProcessLauncherInfo;
function GetShortcutTextForPLID(const PLID: WideString): WideString;
function HasTreeShownAsPopup: LongBool;
procedure HideDragImage;
procedure InitTransparentToolbars(const ViewRect: IDispatch);
function IsPanelPinned(const AViewName: WideString): LongBool;
function IsPanelValidInCurrentForm(const AViewName: WideString): LongBool;
function IsPanelVisibleInCurrentForm(const AViewName: WideString): LongBool;
function IsSysLevelHotKey(KeyId: Integer; Alt: LongBool; Shift: LongBool; Ctrl: LongBool): LongBool;
procedure LaunchCurrentHotkey;
procedure MovePanelTo(const AViewName: WideString; ALeft: Integer; ATop: Integer);
function ProcessMessage(const Msg: IDispatch): LongBool;
procedure RegisterFloatingWindow(const FloatingWindow: IFloatingWindow);
function RegisterUserProcessLauncher(const APreferredID: WideString; const AServerCommand: WideString; const AParameters: WideString; const ACaption: WideString; const ADescription: WideString; const AImageFile: WideString; const AShortcutText: WideString; const AShortcut2Text: WideString): IProcessLauncherInfo;
procedure ResizePanel(const AViewName: WideString; AWidth: Integer; AHeight: Integer);
procedure SetFocusLock(Locked: LongBool);
procedure SetPanelActiveInCurrentForm(const AViewName: WideString);
procedure SetPanelDockedHeight(const AViewName: WideString; AHeight: Integer);
procedure SetPanelDockedWidth(const AViewName: WideString; AWidth: Integer);
procedure SetPanelPinned(const AViewName: WideString; AIsPinned: LongBool);
procedure SetPanelVisibleInCurrentForm(const AViewName: WideString; IsVisible: LongBool);
procedure SetTitleBarErrorMessage(const ErrorMessage: WideString);
procedure SetTransparentToolbarsSettings(const ABarNameList: WideString; AFullTransparent: LongBool);
function ShowCurrentProcessLauncherHelp: LongBool;
procedure ShowDragImage;
function ShowProcessLauncherHelp(const APLID: WideString): LongBool;
procedure ShowStandardMenuAsPopup(const AMenuWrapper: IMenuWrapper; const APosition: IDispatch);
procedure ShowTreeAsPopup(const TreeID: WideString);
procedure ShowTreeAsPopupAt(const TreeID: WideString; const Position: IDispatch);
function StatusBar_GetState(Index: Integer): WideString;
procedure StatusBar_SetState(Index: Integer; const S: WideString);
function StatusBarManager: IStatusBarManager;
procedure SwitchDocumentActiveView(const ADocument: IServerDocument; const AOldView: IExternalForm; const ANewView: IExternalForm);
procedure UnregisterFloatingWindow(const FloatingWindow: IFloatingWindow);
procedure UnregisterUserProcessLauncher(const APLID: WideString);
procedure UpdateInterfaceState;
procedure UpdateTransparentToolbars;

## IGUIManager2
继承：IGUIManager2 → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 5 个方法、0 个属性

procedure ContinueUpdateActions;
function CreatePreferencesEditorView(const AOwnerDocument: IServerDocument): IServerDocumentView;
procedure ForceUpdateRibbonActions;
procedure PauseUpdateActions;
procedure ViewAvailabilityChanged(const AView: IServerView; AAvailable: Boolean);

## IGUIManagerNotification
继承：IGUIManagerNotification → INotification → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 2 个方法、2 个属性

property Code: Integer read GetCode;  // read-only
property Data: IStrings read GetData;  // read-only
function GetCode: Integer;
function GetData: IStrings;

## IGeneralReport
继承：IGeneralReport → IBaseReport → IInterface ｜ 单元：RT_Workspace ｜ 自有 1 个方法、0 个属性

procedure WriteRow(const Values: WideString; const HtmlStyles: WideString);

## IGenerateReport
继承：IGenerateReport → IInterface ｜ 单元：RT_IntegratedLibrary ｜ 自有 1 个方法、0 个属性

procedure GenerateComponentReportAdvanced(const GetLibInfo: IGetLibraryReportInfo; const FileName: WideString; const LibType: WideString);

## IGenericDeviceManager
继承：IGenericDeviceManager → IInterface ｜ 单元：Rt_NexusDevices ｜ 自有 9 个方法、0 个属性

function GetAssociatedBSDLFileName(AIdCode: Cardinal; AJTagIndex: Integer): WideString;
function GetAssociatedDeviceSettingsDescription(AIdCode: Cardinal; AJTagIndex: Integer): WideString;
function GetAssociatedLibraryFileName(AIdCode: Cardinal; AJTagIndex: Integer): WideString;
function GetAssociatedLibraryReference(AIdCode: Cardinal; AJTagIndex: Integer): WideString;
function GetInstructionLength(AIdCode: Cardinal): Integer;
function GetNonAssociatedBSDLFileNamesForIdCode(AIdCode: Cardinal; AJTagIndex: Integer): WideString;
procedure Import_FromUser_JTAGIdMapping(AIdCode: Cardinal);
procedure SetAssociatedBSDLFileName(AIdCode: Cardinal; AJTagIndex: Integer; ABSDLFileName: WideString);
procedure SetInstructionLength(AIdCode: Cardinal; AInstructionLength: Integer);

## IGetImplementor
继承：IGetImplementor → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 1 个方法、0 个属性

function GetImplementor: TObject;

## IGetLibraryReportInfo
继承：IGetLibraryReportInfo → IInterface ｜ 单元：RT_IntegratedLibrary ｜ 自有 5 个方法、0 个属性

function GetLibraryReportInfo(const AFilePath: WideString; const ALibType: WideString): ILibraryReportInfo;
function GetModelReportInfo(const ACompFilePath: WideString; const ACompLibRef: WideString; const AModelFilePath: WideString; const AModelName: WideString): ILibObjectReportInfo;
function GetReportSettings(const ALibType: WideString): ILibraryReportExternalSettings;
procedure ReleaseReportSettings;
procedure UseReportSettings(const ASettings: ILibraryReportExternalSettings);

## IHDLDocument
继承：IHDLDocument → IInterface ｜ 单元：Rt_VHDL ｜ 自有 1 个方法、0 个属性

procedure HighLight_Port(AHDLEntity: WideString; APortName: WideString);

## IHDLLibDocument
继承：IHDLLibDocument → IInterface ｜ 单元：Rt_VHDL ｜ 自有 11 个方法、0 个属性

procedure AddDocument(ADocument: WideString; ACategory: THDLLibCategory);
function Compile: LongBool;
function FileReallyExists(AFileName: WideString): LongBool;
function GetAllDocuments(AIndex: Integer): WideString;
function GetAllDocumentsCount: Integer;
function GetDocument(ACategory: THDLLibCategory; AIndex: Integer): WideString;
function GetDocumentCount(ACategory: THDLLibCategory): Integer;
function GetFileName: WideString;
procedure ProcessCommand(ACommand: THDLLibCommand; Parameters: WideString);
procedure RemoveDocument(ADocument: WideString);
procedure SetModified(const Value: LongBool);

## IHTMLViewExternalForm
继承：IHTMLViewExternalForm → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 5 个方法、2 个属性

property AlwaysInNewWindow: LongBool read GetAlwaysInNewWindow write SetAlwaysInNewWindow;
property CtrlClickInNewWindow: LongBool read GetCtrlClickInNewWindow write SetCtrlClickInNewWindow;
function GetAlwaysInNewWindow: LongBool;
function GetCtrlClickInNewWindow: LongBool;
procedure NavigateTo(const Url: WideString);
procedure SetAlwaysInNewWindow(Value: LongBool);
procedure SetCtrlClickInNewWindow(Value: LongBool);

## IHTMLViewJavascriptMessageReceivedEvent
继承：IHTMLViewJavascriptMessageReceivedEvent → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 1 个方法、0 个属性

procedure Invoke(const AType: WideString; out AAction: TJavascriptAction; out AName: WideString; out AData: WideString);

## IHTMLViewLoadingStateChangedEvent
继承：IHTMLViewLoadingStateChangedEvent → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 1 个方法、0 个属性

procedure Invoke(const ALoadingState: Boolean);

## IHTMLViewLocationChangeEvent
继承：IHTMLViewLocationChangeEvent → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 1 个方法、0 个属性

procedure Invoke(const ANewLocation: WideString);

## IHTMLViewSetOnResourceResponseEvent
继承：IHTMLViewSetOnResourceResponseEvent → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 1 个方法、0 个属性

procedure Invoke(const AResponseCode: Integer);

## IHTMLViewWithEvents
继承：IHTMLViewWithEvents → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 4 个方法、0 个属性

procedure SetOnJavascriptMessageReceived(const AValue: IHTMLViewJavascriptMessageReceivedEvent);
procedure SetOnLoadingStateChanged(const AValue: IHTMLViewLoadingStateChangedEvent);
procedure SetOnLocationChange(const AValue: IHTMLViewLocationChangeEvent);
procedure SetOnResourceResponse(const AValue: IHTMLViewSetOnResourceResponseEvent);

## IHardBreakpoint
继承：IHardBreakpoint → ISoftBreakpoint → IInterface ｜ 单元：Rt_NexusDevices ｜ 自有 10 个方法、5 个属性

property AddressMask: TMemoryAddress read GetAddressMask write SetAddressMask;
property Control: TMemoryAddress read GetControl write SetControl;
property ControlMask: TMemoryAddress read GetControlMask write SetControlMask;
property Data: TMemoryAddress read GetData write SetData;
property DataMask: TMemoryAddress read GetDataMask write SetDataMask;
function GetAddressMask: Int64;
function GetControl: Int64;
function GetControlMask: Int64;
function GetData: Int64;
function GetDataMask: Int64;
procedure SetAddressMask(Value: Int64);
procedure SetControl(Value: Int64);
procedure SetControlMask(Value: Int64);
procedure SetData(Value: Int64);
procedure SetDataMask(Value: Int64);

## IHardDeviceLink
继承：IHardDeviceLink → IInterface ｜ 单元：Rt_NexusWorkspace ｜ 自有 1 个方法、0 个属性

procedure SetHardDeviceProject(Project: IProject; Configuration: WideString);

## IHarnessCoreAccess
继承：IHarnessCoreAccess → IInterface ｜ 单元：RT_Workspace ｜ 自有 4 个方法、0 个属性

function GetDDMProject(const AProjectFilePath: WideString): IDDMHarnessProject;
function GetDMObjectHelper: IInterface;
function GetHarnessUtils: IInterface;
procedure SetOriginalProject(const AProjectFilePath: WideString; const AOriginalProject: IProject);

## IHarnessDefinition
继承：IHarnessDefinition → IInterface ｜ 单元：RT_Workspace ｜ 自有 4 个方法、0 个属性

function DM_GetState_Entry(AIndex: Integer): WideString;
function DM_GetState_EntryCount: Integer;
function DM_GetState_HarnessID: WideString;
function DM_ObjectAddress: Pointer;

## IHarnessDefinitionList
继承：IHarnessDefinitionList → IInterface ｜ 单元：RT_Workspace ｜ 自有 7 个方法、0 个属性

function DM_AdaptedObjectAddress: Pointer;
function DM_GetState_HarnessDefinition_ByIndex(AIndex: Integer): IHarnessDefinition;
function DM_GetState_HarnessDefinition_ByType(AType: WideString): IHarnessDefinition;
function DM_GetState_HarnessDefinitionCount: Integer;
function DM_GetState_Name: WideString;
procedure DM_LoadHarnessDefinitions;
function DM_ObjectAddress: Pointer;

## IHighlightedDocument
继承：IHighlightedDocument → IServerDocument → IInterface ｜ 单元：RT_Workspace ｜ 自有 24 个方法、1 个属性

property HL_HighlightedNet: INet read HL_GetHighlightedNet write HL_SetHighlightedNet;
procedure HL_Begin;
function HL_ChooseObjectGraphically(var ADMObject: IDMObject): Boolean;
procedure HL_End;
function HL_GetHighlightedNet: INet;
function HL_GetLinkedObject(const ADMObject: IDMObject): IDMObject;
procedure HL_HighlightMethod_Add(AHighlightMethod: THighlightMethod);
procedure HL_HighlightMethod_Clear(AHighlightMethod: THighlightMethod);
function HL_HighlightMethod_IsApplicable(AHighlightMethod: THighlightMethod): Boolean;
procedure HL_HighlightMethod_Remove(AHighlightMethod: THighlightMethod);
function HL_ObjectCount: Integer;
function HL_Objects(AnIndex: Integer): IDMObject;
procedure HL_Perform;
procedure HL_Register_Area(const AnArea: IDispatch);
procedure HL_Register_Bus(const ABus: IBus);
procedure HL_Register_Component(const AComponent: IComponent);
procedure HL_Register_DMObject(const AnObject: IDMObject);
procedure HL_Register_Net(const ANet: INet);
procedure HL_Register_NetItem(const ANetItem: INetItem);
procedure HL_Register_Part(const APart: IPart);
procedure HL_Register_VHDLEntity(const AVHDLEntity: IVHDLEntity);
procedure HL_SetHighlightedNet(const ANet: INet);
procedure HL_UnRegister_AllObjects;
procedure HL_UnRegister_Object(const AnObject: IDMObject);
function HL_XProbeChooseObject(var ADMObject: IDMObject): Boolean;

## IHighlightedModelEditor
继承：IHighlightedModelEditor → IModelEditor → IInterface ｜ 单元：RT_IntegratedLibrary ｜ 自有 5 个方法、0 个属性

procedure DrawModel_PinsSelected(AExternalForm: IExternalForm; AModelName: WideString; ADatafilePath: WideString; APinNameList: WideString);
procedure HighlightComponentPins(AExternalForm: IExternalForm; APinNameList: WideString; AHighlightColor: TColor; ANonHighlightColor: TColor);
procedure RegisterListener(AExternalForm: IExternalForm; AListener: IModelEditorSelectionListener);
procedure ShowPinsAsSelected(AExternalForm: IExternalForm; APinNameList: WideString);
procedure ShowSpecifiedPinsOnly(AExternalForm: IExternalForm; APinNameList: WideString);

## IIOSignal
继承：IIOSignal → IInterface ｜ 单元：RT_Digital_IO ｜ 自有 6 个方法、3 个属性

property Name: WideString read GetName;  // read-only
property Value: TSignalValueType read GetValue write SetValue;
property Width: Integer read GetWidth;  // read-only
procedure ForceGetSetValue;
function GetName: WideString;
function GetSignalInstrument: ISignalInstrument;
function GetValue: Cardinal;
function GetWidth: Integer;
procedure SetValue(AValue: Cardinal);

## IIdleHandler
继承：IIdleHandler → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 1 个方法、0 个属性

procedure Invoke;

## IIdleHandlerRegistrator
继承：IIdleHandlerRegistrator → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 2 个方法、0 个属性

procedure RegisterHandler(const AHandler: IIdleHandler);
procedure RemoveHandler;

## IImplementationFile
继承：IImplementationFile → IInterface ｜ 单元：RT_IntegratedLibrary ｜ 自有 24 个方法、10 个属性

property Description: WideString read GetDescription write SetDescription;
property ItemRevisionGUID: WideString read GetItemRevisionGUID write SetItemRevisionGUID;
property ModelFilename: WideString read GetModelFilename write SetModelFilename;
property ModelName: WideString read GetModelName write SetModelName;
property ModelType: WideString read GetModelType write SetModelType;
property ParameterCount: Integer read GetParameterCount;  // read-only
property ParameterName[Index: Integer]: WideString read GetParameterName;  // read-only
property ParameterValue[Index: Integer]: WideString read GetParameterValue;  // read-only
property ReleaseItemGUID: WideString read GetReleaseItemGUID write SetReleaseItemGUID;
property ReleaseVaultGUID: WideString read GetReleaseVaultGUID write SetReleaseVaultGUID;
procedure ClearParameters;
procedure DeleteParameter(Index: Integer);
procedure DeleteParameterByName(AName: WideString);
function GetDescription: WideString;
function GetItemRevisionGUID: WideString;
function GetModelFilename: WideString;
function GetModelName: WideString;
function GetModelType: WideString;
function GetParameterByName(AName: WideString): IItemParameter;
function GetParameterCount: Integer;
function GetParameterName(Index: Integer): WideString;
function GetParameterValue(Index: Integer): WideString;
function GetParameterValueByName(AName: WideString): WideString;
function GetReleaseItemGUID: WideString;
function GetReleaseVaultGUID: WideString;
function SaveToFile(AFileName: WideString): Boolean;
procedure SetDescription(AValue: WideString);
procedure SetItemRevisionGUID(Value: WideString);
procedure SetModelFilename(AValue: WideString);
procedure SetModelName(AValue: WideString);
procedure SetModelType(AValue: WideString);
procedure SetParameterValueByName(AName: WideString; AValue: WideString);
procedure SetReleaseItemGUID(Value: WideString);
procedure SetReleaseVaultGUID(Value: WideString);

## IImportDocument
继承：IImportDocument → IInterface ｜ 单元：RT_Workspace ｜ 自有 1 个方法、0 个属性

function FileImport(const AFileName: WideString; const AFormat: WideString): LongBool;

## IInstalledConstraintFiles
继承：IInstalledConstraintFiles → IInterface ｜ 单元：RT_Workspace ｜ 自有 5 个方法、0 个属性

function ConstraintFileIsInstalled(APath: WideString): LongBool;
function DefaultConstraintFile: WideString;
function EditInstalledConstraintFiles: LongBool;
function InstalledConstraintFile(AIndex: Integer): WideString;
function InstalledConstraintFileCount: Integer;

## IInstance
继承：IInstance → IDMObject → IInterface ｜ 单元：RT_Workspace ｜ 自有 6 个方法、0 个属性

function DM_Designator: WideString;
function DM_InstanceType: WideString;
function DM_Part: IPart;
function DM_PortCount: Integer;
function DM_Ports(Index: Integer): IInstancePort;
function DM_SheetSymbol: ISheetSymbol;

## IInstancePort
继承：IInstancePort → ISignalNode → IDMObject → IInterface ｜ 单元：RT_Workspace ｜ 自有 0 个方法、0 个属性


## IInstancesFactory
继承：IInstancesFactory → IInterface ｜ 单元：RT_Workspace ｜ 自有 3 个方法、0 个属性

function CreateLibraryPart(const ASheet: IDocument; const AReferencePart: IPart): IPart;
function CreatePart(const ADocument: IDocument; const APartType: WideString; const ADesignitemID: WideString; const ASourceLibraryName: WideString; const AVaultGUID: WideString; const AItemGUID: WideString; const ARevisionGUID: WideString): IPart;
function CreateSheetSymbol(const ADocument: IDocument; const ARawSheetSymbolFileName: WideString; const ASheetSymbolFileName: WideString; const ADesignitemID: WideString; const ASourceLibraryName: WideString; const AVaultGUID: WideString; const AItemGUID: WideString; const ARevisionGUID: WideString): ISheetSymbol;

## IInstructionOpCode
继承：IInstructionOpCode → IBSDLObject → IInterface ｜ 单元：Rt_NexusDevices ｜ 自有 2 个方法、0 个属性

function GetInstructionName: WideString;
function GetOpCodePattern: WideString;

## IInstrumentView
继承：IInstrumentView → IExternalForm → IInterface ｜ 单元：Rt_NexusDevices ｜ 自有 8 个方法、0 个属性

procedure GetInstrumentBounds(out ALeft: Integer; out ATop: Integer; out AWidth: Integer; out AHeight: Integer);
procedure GetProjectDetails(out AProjectPath: WideString; out ATarget: WideString);
procedure Hidden;
function LiveUpdateNet(const ANet: INet; AUpdateEnabled: Boolean): Boolean;
procedure ReceiveNotification(const ANotification: INotification);
procedure SetInstrumentBounds(ALeft: Integer; ATop: Integer; AWidth: Integer; AHeight: Integer);
procedure SetProjectDetails(const AProjectPath: WideString; const ATarget: WideString);
procedure UpdateDisplay;

## IIntegratedLibraryManager
继承：IIntegratedLibraryManager → IInterface ｜ 单元：RT_IntegratedLibrary ｜ 自有 78 个方法、0 个属性

procedure AddRemoveLibraries;
function AvailableLibraryCount: Integer;
function AvailableLibraryPath(LibraryIndex: Integer): WideString;
function AvailableLibraryType(LibraryIndex: Integer): TLibraryType;
function BrowseComponent(ALibIdentifierKind: TLibIdentifierKind; var ALibraryIdentifier: WideString; var ADesignItemID: WideString; var APartID: Integer; out ASymbolReference: WideString; out ASymbolLibraryPath: WideString; var AModelName: WideString; const AModelType: WideString; out AModelLibraryPath: WideString): Boolean;
function BrowseDatafileEntity(ALibIdentifierKind: TLibIdentifierKind; var ALibraryIdentifier: WideString; var ADatafileEntityName: WideString; const ADatafileType: WideString; out ADatafilePath: WideString): Boolean;
function BrowseDatafileEntityInDatafile(ALibIdentifierKind: TLibIdentifierKind; var ALibraryIdentifier: WideString; var ADatafileEntityName: WideString; const ADatafileType: WideString; out ADatafilePath: WideString; AUseIntAndDBLibrary: Boolean): Boolean;
procedure BrowseForComponent(ALibReference: PWideChar; ASCHLibraryPath: PWideChar; SelModelName: PWideChar; SelModelLib: PWideChar; LibPath: PWideChar; ModelType: PWideChar);
procedure BrowseForComponentAndPart(ALibReference: PWideChar; ASCHLibraryPath: PWideChar; SelModelName: PWideChar; SelModelLib: PWideChar; LibPath: PWideChar; ModelType: PWideChar; var PartID: Integer);
procedure BrowseForComponentAndPartCheckDBLibs(ALibReference: PWideChar; ASCHLibraryPath: PWideChar; SelModelName: PWideChar; SelModelLib: PWideChar; LibPath: PWideChar; ModelType: PWideChar; ADatabaseTableName: PWideChar; ADatabaseKeys: PWideChar; var PartID: Integer);
procedure BrowseForComponentCheckDBLibs(ALibReference: PWideChar; ASCHLibraryPath: PWideChar; SelModelName: PWideChar; SelModelLib: PWideChar; LibPath: PWideChar; ModelType: PWideChar; ADatabaseTable: PWideChar; ADatabaseKeys: PWideChar);
procedure BrowseForDatafile(AModelName: PWideChar; AModelPath: PWideChar; LibPath: PWideChar; ModelType: PWideChar; ForComponentInstance: LongBool);
function BrowseModel(ALibIdentifierKind: TLibIdentifierKind; var ALibraryIdentifier: WideString; var ADesignItemID: WideString; var AModelName: WideString; const AModelType: WideString; out AModelLibraryPath: WideString): Boolean;
function BrowseSimModel(ALibIdentifierKind: TLibIdentifierKind; var ALibraryIdentifier: WideString; var ADatafileEntityName: WideString; var ADatafileModelType: Integer; const ADatafileType: WideString; out ADatafilePath: WideString; AUseIntAndDBLibrary: Boolean; AGenericLibrary: Boolean): Boolean;
function BrowseSimModelFromFile(ADatafilePath: WideString; var ADatafileEntityName: WideString; var ADatafileModelType: Integer; const ADatafileType: WideString): Boolean;
function BrowseSymbol(ALibIdentifierKind: TLibIdentifierKind; var ALibraryIdentifier: WideString; var ADesignItemID: WideString; out ASymbolReference: WideString; out ASymbolLibraryPath: WideString): Boolean;
function BrowseSymbolRevision(ALibIdentifierKind: TLibIdentifierKind; const ALibraryIdentifier: WideString; var ADesignItemID: WideString; out ASymbolReference: WideString; out ASymbolLibraryPath: WideString; out ARevisionStatus: WideString): Boolean;
procedure CheckModelPathAndPattern(var ALibraryPath: WideString; var AModelName: WideString);
function ComponentHasModelOfType(LibraryPath: WideString; ComponentIndex: Integer; AModelType: WideString): Boolean;
procedure CreateIntegratedLibrary(AProject: IProject; AnOutputPath: WideString; Install: Boolean);
procedure ExtractSources(ALibraryPath: WideString);
function ExtractSourcesToDatabaseLib(ALibraryPath: WideString; ADatabaseLib: IDatabaseLibDocument; AnAbsoluteOutputPath: WideString; ARelativeOutputPath: WideString): WideString;
function ExtractSourcesToDesignItemManager(ALibraryPath: WideString; ADestinationPath: WideString; out Parameters: WideString): WideString;
procedure ExtractSourcesToPath(ALibraryPath: WideString; ADestinationPath: WideString);
function FindComponentDesignItemDeviceSheet(ALibIdentifierKind: TLibIdentifierKind; const ALibraryIdentifier: WideString; const ADesignItemID: WideString; out ADeviceSheetPath: WideString): Boolean;
function FindComponentDisplayPath(ALibIdentifierKind: TLibIdentifierKind; const ALibraryIdentifier: WideString; const ADesignItemID: WideString): WideString;
function FindComponentDisplayPathEx(ALibIdentifierKind: TLibIdentifierKind; const ALibraryIdentifier: WideString; const ADesignItemID: WideString; AIgnoreNotLoadedLibs: Boolean): WideString;
function FindComponentLibraryPath(ALibIdentifierKind: TLibIdentifierKind; const ALibraryIdentifier: WideString; const ADesignItemID: WideString): WideString;
function FindComponentSymbol(ALibIdentifierKind: TLibIdentifierKind; const ALibraryIdentifier: WideString; const ADesignItemID: WideString; out ASymbolLibraryPath: WideString; out ASymbolReference: WideString): Boolean;
function FindDatafileEntityDatafilePath(ALibIdentifierKind: TLibIdentifierKind; const ALibraryIdentifier: WideString; const ADatafileEntityName: WideString; const ADatafileType: WideString; AUseIntAndDBLibrary: Boolean): WideString;
function FindDatafileEntityDatafilePathEx(ALibIdentifierKind: TLibIdentifierKind; const ALibraryIdentifier: WideString; const ADatafileEntityName: WideString; const ADatafileType: WideString; AUseIntAndDBLibrary: Boolean; AIgnoreNotLoadedLibs: Boolean): WideString;
function FindDatafileEntityLibraryPath(ALibIdentifierKind: TLibIdentifierKind; const ALibraryIdentifier: WideString; const ADatafileEntityName: WideString; const ADatafileType: WideString): WideString;
function FindDatafileEntitySourceDatafilePath(ALibIdentifierKind: TLibIdentifierKind; const ALibraryIdentifier: WideString; const ADatafileEntityName: WideString; const ADatafileType: WideString; AUseIntAndDBLibrary: Boolean): WideString;
function FindDatafileEntitySourceDatafilePathEx(ALibIdentifierKind: TLibIdentifierKind; const ALibraryIdentifier: WideString; const ADatafileEntityName: WideString; const ADatafileType: WideString; AUseIntAndDBLibrary: Boolean; AIgnoreNotLoadedLibs: Boolean): WideString;
function FindDatafileEntitySourceLibraryPath(ALibIdentifierKind: TLibIdentifierKind; const ALibraryIdentifier: WideString; const ADatafileEntityName: WideString; const ADatafileType: WideString): WideString;
function FindDatafileInStandardLibs(ADatafileEntityName: WideString; ADatafileType: WideString; ADatafileLocation: WideString; ForComponentInstance: Boolean; var FoundInLibraryPath: WideString): WideString;
function FindDeviceSheetByFileName(const AFileName: WideString; out ADesignItemID: WideString; out ALibraryIdentifier: WideString): Boolean;
function FindLibraryInformation(ALibIdentifierKind: TLibIdentifierKind; const ALibraryIdentifier: WideString; const ADesignItemID: WideString; out ALibraryPath: WideString; out ADBTableName: WideString): Boolean;
function FindModelLibraryPath(ALibIdentifierKind: TLibIdentifierKind; const ALibraryIdentifier: WideString; const ADesignItemID: WideString; const AModelName: WideString; const AModelType: WideString): WideString;
function FindModelLibraryPathEx(ALibIdentifierKind: TLibIdentifierKind; const ALibraryIdentifier: WideString; const ADesignItemID: WideString; const AModelName: WideString; const AModelType: WideString; AIgnoreNotLoadedLibs: Boolean): WideString;
function GetAllParametersFromSourceLib(ALibraryPath: WideString): WideString;
function GetAvailableDBLibDocAtPath(ALibraryPath: WideString): IDatabaseLibDocument;
function GetCachedFullFilePathFromExplicitFileName(ARepositoryURL: WideString; AExplicitFileName: WideString; var ACachedFileName: WideString): Boolean;
function GetComponentCount(LibraryPath: WideString): Integer;
function GetComponentDatafileLocation(DatafileIndex: Integer; AModelName: WideString; AModelType: WideString; AComponentName: WideString; AComponentLibraryName: WideString; var FoundInLibraryPath: WideString): WideString;
function GetComponentLocation(ALibraryName: WideString; AComponentName: WideString; var FoundInLibraryPath: WideString): WideString;
function GetComponentLocationFromDatabase(ALibraryName: WideString; ATableName: WideString; ADatabaseKeys: WideString; var FoundInLibraryPath: WideString): WideString;
function GetComponentName(LibraryPath: WideString; ComponentIndex: Integer): WideString;
function GetComponentPlacementParameters(ALibIdentifierKind: TLibIdentifierKind; const ALibraryIdentifier: WideString; const ADesignItemID: WideString): WideString;
function GetDatabaseDatafileLocation(ADatafileIndex: Integer; AModelName: WideString; AModelType: WideString; AComponentKeys: WideString; ATableName: WideString; ADatabaseLibraryName: WideString; var FoundInLibraryPath: WideString): WideString;
function GetDatabaseModelFullLibPath(const ADatabaseLibraryPath: WideString; const ALibPath: WideString; const AModelName: WideString; const AModelType: WideString): WideString;
function GetDatafileEntityCount(LibraryPath: WideString; ComponentIndex: Integer; ModelIndex: Integer): Integer;
function GetDatafilePath(LibraryPath: WideString; ComponentIndex: Integer; ModelIndex: Integer; DatafileIndex: Integer): WideString;
function GetFirstLibraryFullPathForLibRef(ADirectory: WideString; ALibRef: WideString; AExtension: WideString): WideString;
function GetLifeCycleState(ALibIdentifierKind: TLibIdentifierKind; const ALibraryIdentifier: WideString; const ADesignItemID: WideString): WideString;
function GetModel(LibraryPath: WideString; ComponentIndex: Integer; ModelIndex: Integer): IModel;
function GetModelCount(LibraryPath: WideString; ComponentIndex: Integer): Integer;
function GetModelName(LibraryPath: WideString; ComponentIndex: Integer; ModelIndex: Integer): WideString;
function GetModelType(LibraryPath: WideString; ComponentIndex: Integer; ModelIndex: Integer): IModelType;
function GetOrderedRevisionList(const ALibIdentifierKind: TLibIdentifierKind; const ALibraryIdentifier: WideString; const ADesignItemID: WideString; out ACommaTextList: WideString): Boolean;
function GetParameterCount(LibraryPath: WideString; ComponentIndex: Integer): Integer;
function GetParameterName(LibraryPath: WideString; ComponentIndex: Integer; ParameterIndex: Integer): WideString;
function GetParametersForDBComponent(ALibraryName: WideString; ATableName: WideString; ADatabaseKeys: WideString): WideString;
function GetParameterValue(LibraryPath: WideString; ComponentIndex: Integer; ParameterIndex: Integer): WideString;
function GetSchLibPathForDBComponent(ALibraryPath: WideString; ATableName: WideString; ADatabaseKeys: WideString): WideString;
function GetSchLibRefForDBComponent(ALibraryPath: WideString; ATableName: WideString; ADatabaseKeys: WideString): WideString;
function GetWorkingFileNameFromCacheFileName(ACacheFileName: WideString): WideString;
function InstalledLibraryCount: Integer;
function InstalledLibraryPath(AnIndex: Integer): WideString;
procedure InstallLibrary(ALibraryPath: WideString);
function IsParameterDatabaseKey(ALibraryPath: WideString; ADatabaseTableName: WideString; AParameterName: WideString): Boolean;
procedure MakeCurrentProject(AProject: IProject);
function ModelCount(AComponentName: WideString; AComponentLibraryName: WideString; AModelType: WideString): Integer;
function ModelName(AComponentName: WideString; AComponentLibraryName: WideString; AModelType: WideString; AnIndex: Integer): WideString;
function ParseDatabaseKeys(AKeys: WideString; ADelimiter: WideString): WideString;
function PlaceLibraryComponent(ALibReference: PWideChar; ALibraryPath: PWideChar; Parameters: PWideChar): Boolean;
procedure UninstallLibrary(ALibraryPath: WideString);
procedure UpdateCachedFileIfNecessary(ACachedLibraryPath: WideString);

## IIntegratedLibraryProject
继承：IIntegratedLibraryProject → IProject → IDMObject → IInterface ｜ 单元：RT_Workspace ｜ 自有 0 个方法、0 个属性


## IInterface
继承：IInterface ｜ 单元：System ｜ 自有 0 个方法、0 个属性


## IInterfaceComponentReference
继承：IInterfaceComponentReference → IInterface ｜ 单元：System.Classes ｜ 自有 1 个方法、0 个属性

function GetComponent: TComponent;

## IInterfaceList
继承：IInterfaceList → IInterface ｜ 单元：System.Classes ｜ 自有 15 个方法、3 个属性

property Capacity: Integer read GetCapacity write SetCapacity;
property Count: Integer read GetCount write SetCount;
property Items[Index: Integer]: IInterface read Get write Put;
procedure Clear;
procedure Delete(Index: Integer);
procedure Exchange(Index1: Integer; Index2: Integer);
function First: IInterface;
function Get(Index: Integer): IInterface;
function GetCapacity: Integer;
function GetCount: Integer;
function IndexOf(const Item: IInterface): Integer;
procedure Insert(Index: Integer; const Item: IInterface);
function Last: IInterface;
procedure Put(Index: Integer; const Item: IInterface);
function Remove(const Item: IInterface): Integer;
procedure SetCapacity(NewCapacity: Integer);
procedure SetCount(NewCount: Integer);
procedure Unlock;

## IInterfaceListEx
继承：IInterfaceListEx → IInterfaceList → IInterface ｜ 单元：System.Classes ｜ 自有 1 个方法、0 个属性

function GetEnumerator: TInterfaceListEnumerator;

## IInternalOptionRegistry
继承：IInternalOptionRegistry → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 0 个方法、0 个属性


## IInternalOptionRegistryBoolean
继承：IInternalOptionRegistryBoolean → IInternalOptionRegistry → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 0 个方法、0 个属性


## IInternalOptionRegistryDouble
继承：IInternalOptionRegistryDouble → IInternalOptionRegistry → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 0 个方法、0 个属性


## IInternalOptionRegistryInteger
继承：IInternalOptionRegistryInteger → IInternalOptionRegistry → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 3 个方法、0 个属性

function WithMaxValue(AValue: Integer): IInternalOptionRegistryInteger;
function WithMinValue(AValue: Integer): IInternalOptionRegistryInteger;
function WithRange(AMinValue: Integer; AMaxValue: Integer): IInternalOptionRegistryInteger;

## IInternalOptionRegistryString
继承：IInternalOptionRegistryString → IInternalOptionRegistry → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 0 个方法、0 个属性


## IInternalOptions
继承：IInternalOptions → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 21 个方法、0 个属性

function InDevelopment(const ValueName: WideString): Boolean;
function IsBetaFeaturesEnabled: Boolean;
function IsDevFeaturesEnabled: Boolean;
function IsOptionInBetaStage(const ValueName: WideString): Boolean;
function IsReleased(const ValueName: WideString): Boolean;
function OptionExists(const ValueName: WideString): Boolean;
function OptionVisible(const ValueName: WideString): Boolean;
function ReadBoolean(const ValueName: WideString): LongBool;
function ReadDouble(const ValueName: WideString): Double;
function ReadFeatureBoolean(const AName: WideString; const ADefaultValue: LongBool): LongBool;
function ReadFeatureDouble(const AName: WideString; const ADefaultValue: Double): Double;
function ReadFeatureInteger(const AName: WideString; const ADefaultValue: Integer): Integer;
function ReadFeatureState(const AName: WideString; const ADefaultValue: TStateOfFeature): TStateOfFeature;
function ReadFeatureString(const AName: WideString; const ADefaultValue: WideString): WideString;
function ReadInteger(const ValueName: WideString): Integer;
function ReadString(const ValueName: WideString): WideString;
procedure RemoveFeature(const AName: WideString);
procedure WriteBoolean(const ValueName: WideString; Value: LongBool);
procedure WriteDouble(const ValueName: WideString; Value: Double);
procedure WriteInteger(const ValueName: WideString; Value: Integer);
procedure WriteString(const ValueName: WideString; const Value: WideString);

## IInternalOptionsReader
继承：IInternalOptionsReader → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 11 个方法、0 个属性

function GetOptionDescription(const ValueName: WideString): WideString;
function GetOptions: IStrings;
function GetOptionType(const ValueName: WideString): WideString;
function ReadBoolean(const ValueName: WideString): LongBool;
function ReadDefaultBoolean(const ValueName: WideString): LongBool;
function ReadDefaultDouble(const ValueName: WideString): Double;
function ReadDefaultInteger(const ValueName: WideString): Integer;
function ReadDefaultString(const ValueName: WideString): WideString;
function ReadDouble(const ValueName: WideString): Double;
function ReadInteger(const ValueName: WideString): Integer;
function ReadString(const ValueName: WideString): WideString;

## IInternalOptionsWriter
继承：IInternalOptionsWriter → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 4 个方法、0 个属性

procedure WriteBoolean(const ValueName: WideString; Value: LongBool);
procedure WriteDouble(const ValueName: WideString; Value: Double);
procedure WriteInteger(const ValueName: WideString; Value: Integer);
procedure WriteString(const ValueName: WideString; const Value: WideString);

## IItemManagerFactory
继承：IItemManagerFactory → IInterface ｜ 单元：RT_Workspace ｜ 自有 1 个方法、0 个属性

procedure RunItemManagerSilently(const AProject: IProject; const ADocument: IDocument; const AParameters: WideString);

## IItemParameter
继承：IItemParameter → IInterface ｜ 单元：Rt_AltiumLibrary ｜ 自有 3 个方法、3 个属性

property Name: WideString read GetState_Name;  // read-only
property ParameterUnit: WideString read GetState_Unit;  // read-only
property Value: WideString read GetState_Value;  // read-only
function GetState_Name: WideString;
function GetState_Unit: WideString;
function GetState_Value: WideString;

## IJTagChannel
继承：IJTagChannel → IDeviceChannel → IInterface ｜ 单元：Rt_NexusDevices ｜ 自有 34 个方法、0 个属性

procedure AddJtagDelay(AValue: Byte);
function CurrentTapState: TTapState;
function DeviceOnline(ADeviceIndex: Integer): LongBool;
procedure FlushJTAGBuffer;
procedure ForceToState(AState: TTapState);
function GetChainLength: Integer;
function GetDevice(AIndex: Integer): IJTagDevice;
function GetDeviceCount: Integer;
function GetOwnerJtagPort: IJtagPort;
function GetStringForDevicesOnChain: WideString;
procedure LoadDR_In(AData: Cardinal; ABitCount: Integer; ADeviceIndex: Integer);
function LoadDR_InOut(AData: Cardinal; ABitCount: Integer; ADeviceIndex: Integer): Cardinal;
function LoadDR_Out(ARepeatBit: Cardinal; ABitCount: Integer; ADeviceIndex: Integer): WideString;
procedure LoadIR_In(AInstruction: Cardinal; ADeviceIndex: Integer);
function LoadIR_InOut(AInstruction: Cardinal; ADeviceIndex: Integer): Cardinal;
function LoadIR_Out(ARepeatBit: Cardinal; ADeviceIndex: Integer): WideString;
procedure MoveFromStateToState(AStateFrom: TTapState; AStateTo: TTapState);
procedure MoveToState(AState: TTapState);
procedure NextState(ATMS: Integer);
procedure PlaceAllDevicesInBypass;
procedure RescanChain;
procedure ResetTAP;
procedure ScanChain;
procedure SelectChain(AMode: TSelectMode);
function ShiftDR_Out(ARepeatBit: Cardinal; ABitCount: Integer; ADeviceIndex: Integer): WideString;
procedure ShiftDR_String_In(AData: WideString; ADeviceIndex: Integer);
function ShiftDR_String_InOut(AData: WideString; ADeviceIndex: Integer): WideString;
procedure ShiftDR_Word_In(AData: Cardinal; ABitCount: Integer; ADeviceIndex: Integer);
function ShiftDR_Word_InOut(AData: Cardinal; ABitCount: Integer; ADeviceIndex: Integer): Cardinal;
function ShiftIR_Out(ARepeatBit: Cardinal; ADeviceIndex: Integer): WideString;
procedure ShiftIR_String_In(AInstruction: WideString; ADeviceIndex: Integer);
function ShiftIR_String_InOut(AInstruction: WideString; ADeviceIndex: Integer): WideString;
procedure ShiftIR_Word_In(AInstruction: Cardinal; ADeviceIndex: Integer);
function ShiftIR_Word_InOut(AInstruction: Cardinal; ADeviceIndex: Integer): Cardinal;

## IJTagDevice
继承：IJTagDevice → IDevice → IInterface ｜ 单元：Rt_NexusDevices ｜ 自有 23 个方法、0 个属性

function GetBoundaryCell(AIndex: Integer): IBoundaryCell;
function GetBoundaryCellCount: Integer;
function GetBoundaryLength: Integer;
function GetBSDL: IBSDLEntity;
function GetCurrentDeviceName: WideString;
function GetDeviceInformation: IDeviceInformation;
function GetFilename: WideString;
function GetIdCodeFromBSDL: Cardinal;
function GetIdCodeFromDevice: Cardinal;
function GetIndex: Integer;
function GetInstructionLength: Integer;
function GetInstructionOpcode(AIndex: Integer): IInstructionOpCode;
function GetInstructionOpcodeCount: Integer;
function GetPin(AIndex: Integer): IScanPin;
function GetPinCount: Integer;
function GetPinMapping(AIndex: Integer): IPinMapping;
function GetPinMappingCount: Integer;
function GetRegisterAssociation(AIndex: Integer): IRegisterAssociation;
function GetRegisterAssociationCount: Integer;
function ReadPinStatesFromChain(ABSDLEntity: IBSDLEntity): LongBool;
procedure ReloadBSDL;
procedure SetIndex(AIndex: Integer);
function UpdateWithPreferredDeviceName(ANewName: WideString): LongBool;

## IJlinkDriver
继承：IJlinkDriver → IInterface ｜ 单元：Rt_NexusDevices ｜ 自有 1 个方法、0 个属性

function GetJlinkHandle: Cardinal;

## IJlinkPort
继承：IJlinkPort → IJtagPort → IInterface ｜ 单元：Rt_NexusDevices ｜ 自有 1 个方法、0 个属性

function GetJlinkDriver: IJlinkDriver;

## IJtagParallelPort
继承：IJtagParallelPort → IJtagPort → IInterface ｜ 单元：Rt_NexusDevices ｜ 自有 1 个方法、0 个属性

function GetParallelPort: IParallelPort;

## IJtagParallelPort_ChannelMapping
继承：IJtagParallelPort_ChannelMapping → IInterface ｜ 单元：Rt_NexusDevices ｜ 自有 4 个方法、4 个属性

property Mask_TCK: Integer read GetMask_TCK;  // read-only
property Mask_TDI: Integer read GetMask_TDI;  // read-only
property Mask_TDO: Integer read GetMask_TDO;  // read-only
property Mask_TMS: Integer read GetMask_TMS;  // read-only
function GetMask_TCK: Integer;
function GetMask_TDI: Integer;
function GetMask_TDO: Integer;
function GetMask_TMS: Integer;

## IJtagPort
继承：IJtagPort → IInterface ｜ 单元：Rt_NexusDevices ｜ 自有 18 个方法、4 个属性

property BoardMask_TCK: Integer read GetBoardChannelMask_TCK;  // read-only
property BoardMask_TDI: Integer read GetBoardChannelMask_TDI;  // read-only
property BoardMask_TDO: Integer read GetBoardChannelMask_TDO;  // read-only
property BoardMask_TMS: Integer read GetBoardChannelMask_TMS;  // read-only
procedure EPM_CyclePort;
function GetBoardChannelMask_TCK: Integer;
function GetBoardChannelMask_TDI: Integer;
function GetBoardChannelMask_TDO: Integer;
function GetBoardChannelMask_TMS: Integer;
function GetGPIOChannel: IGPIOChannel;
function GetJTagChannel_Board: IJTagChannel;
function GetJTagChannel_Hard: IJTagChannel;
function GetJTagChannel_Soft: IJTagChannel;
function GetLongDescription: WideString;
function GetShortDescription: WideString;
function GetSPIChannel: ISPIChannel;
function GetSPROMChannel: ISPROMChannel;
function GetUniqueId: WideString;
function InitializeJTagPort: LongBool;
function IsConfigured: LongBool;
function IsConnected: LongBool;
function Scan(ForceFullScan: Boolean): LongBool;

## IJtagProxyPort
继承：IJtagProxyPort → IJtagPort → IInterface ｜ 单元：Rt_NexusDevices ｜ 自有 0 个方法、0 个属性


## IJtagUsbPort
继承：IJtagUsbPort → IJtagPort → IInterface ｜ 单元：Rt_NexusDevices ｜ 自有 0 个方法、0 个属性


## IKeywordHighlight
继承：IKeywordHighlight → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 1 个方法、0 个属性

procedure SetKeywords(const ACommaList: WideString);

## ILayerInfo
继承：ILayerInfo → IInterface ｜ 单元：Rt_LayerStackManager.Interfaces ｜ 自有 10 个方法、0 个属性

function GetState_CustomProperty(APropertyName: WideString): WideString;
function GetState_DielectricConstant: WideString;
function GetState_Enabled: Boolean;
function GetState_GUID: WideString;
function GetState_Id: Integer;
function GetState_Material: WideString;
function GetState_Name: WideString;
function GetState_Number: WideString;
function GetState_Thickness: Integer;
function GetState_TypeId: WideString;

## ILayerStackDocument
继承：ILayerStackDocument → IInterface ｜ 单元：Rt_LayerStackManager.Interfaces ｜ 自有 10 个方法、1 个属性

property Stackup: ILsmSdkStackup read GetState_Stackup;  // read-only
procedure ApplyToPcb(const BoardPath: WideString);
procedure CloseDialog;
procedure ComputeImpedance;
function GetDocumentEditor: ILsmSdkDocumentEditor;
function GetState_Stackup: ILsmSdkStackup;
procedure LoadFromFile(const Path: WideString; const Format: TLayerStackDocumentFormat);
procedure LoadFromPcb(const BoardPath: WideString);
procedure SaveToFile(const Path: WideString; const Format: TLayerStackDocumentFormat);
function SerializeToString(const Format: TLayerStackDocumentFormat): WideString;
procedure ShowDialog;

## ILayerStackFeatureInfo
继承：ILayerStackFeatureInfo → IInterface ｜ 单元：Rt_LayerStackManager.Interfaces ｜ 自有 4 个方法、0 个属性

function GetState_GUID: WideString;
function GetState_IsDefault: Boolean;
function GetState_IsHidden: Boolean;
function GetState_Name: WideString;

## ILayerStackInfo
继承：ILayerStackInfo → IInterface ｜ 单元：Rt_LayerStackManager.Interfaces ｜ 自有 9 个方法、0 个属性

function GetDrillPairCount: Integer;
function GetDrillPairInfo(const ADrillNum: Integer): IDrillPairInfo;
function GetLayerInfo(const ALayerNum: Integer): ILayerInfo;
function GetLayerPropertiesCount: Integer;
function GetLayerProperty(APropertyNum: Integer): WideString;
function GetLayersCount: Integer;
function GetState_Name: WideString;
function GetState_TotalThickness: Integer;
function IsLayerInLayerStack(const ALayerInfo: ILayerInfo): Boolean;

## ILayerStackManager
继承：ILayerStackManager → IInterface ｜ 单元：Rt_LayerStackManager.Interfaces ｜ 自有 5 个方法、0 个属性

function CreateDocument: ILayerStackDocument;
function CreateLayerStackPainterView: IPCB_LayerStackupDocumentPainterView;
function GetLayerStackProvider(const ABoard: IPCB_Board): ILayerStackProvider;
function OpenDocumentFromPcb(const ABoard: IPCB_Board): ILayerStackDocument;
procedure RemoveLayerStackProvider(const ABoard: IPCB_Board);

## ILayerStackProvider
继承：ILayerStackProvider → IInterface ｜ 单元：Rt_LayerStackManager.Interfaces ｜ 自有 10 个方法、0 个属性

procedure ExportLayerStackToImage(const AHeight: Integer; const APath: WideString; const ASettings: IBoardStackReportSettings);
procedure ExportToFile(const APath: WideString; const AFormat: TLayerStackDocumentFormat; ImperialPrecision: Integer; MetricPrecision: Integer);
function ExportToString(const AFormat: TLayerStackDocumentFormat; ImperialPrecision: Integer; MetricPrecision: Integer): WideString;
procedure ExportToXLSX(const APath: WideString; const ASettings: IBoardStackReportSettings);
function GetDefaultStack: ILayerStackInfo;
function GetLayerStackFeatures(AFeatureNum: Integer): ILayerStackFeatureInfo;
function GetLayerStackFeaturesCount: Integer;
function GetLayerStackInfo(AStackNum: Integer): ILayerStackInfo;
function GetLayerStacksCount: Integer;
procedure PopulateLayerStackColumns(const ASettings: IBoardStackReportSettings);

## ILayerStackServerDocument
继承：ILayerStackServerDocument → IInterface ｜ 单元：Rt_LayerStackManager.Interfaces ｜ 自有 1 个方法、0 个属性

procedure ComputeImpedance;

## ILayerStackServerDocumentHelper
继承：ILayerStackServerDocumentHelper → IInterface ｜ 单元：Rt_LayerStackManager.Interfaces ｜ 自有 4 个方法、0 个属性

procedure AddToDxpWorkspace;
function GetBoard: IPCB_Board;
function GetParentPcbDocument: IServerDocument;
procedure RemoveDocumentFromWorkspace;

## ILibObjectIterator
继承：ILibObjectIterator → IInterface ｜ 单元：RT_IntegratedLibrary ｜ 自有 2 个方法、0 个属性

function GetFirstLibObject(out AInfo: ILibObjectReportInfo): Boolean;
function GetNextLibObject(out AInfo: ILibObjectReportInfo): Boolean;

## ILibObjectReportInfo
继承：ILibObjectReportInfo → IReportParameters → IInterface ｜ 单元：RT_IntegratedLibrary ｜ 自有 4 个方法、0 个属性

function GetChildrenIterator: ILibObjectIterator;
function GetChildrenTitle: WideString;
function GetTableCount: Integer;
function GetTableInfo(AIndex: Integer): IReportTableInfo;

## ILibObjectReportPaint
继承：ILibObjectReportPaint → IInterface ｜ 单元：RT_IntegratedLibrary ｜ 自有 3 个方法、0 个属性

function GetPreviewCount: Integer;
function GetPreviewName(AIndex: Integer): WideString;
procedure PaintPreviewToMetafile(AIndex: Integer; const AFileName: WideString; APaintColorMode: TPaintColorMode; APaintScaleMode: TPaintScaleMode);

## ILibraryComponent
继承：ILibraryComponent → IInterface ｜ 单元：RT_IntegratedLibrary ｜ 自有 4 个方法、4 个属性

property LibIdentifierKind: TLibIdentifierKind read Get_LibIdentifierKind;  // read-only
property LibraryIdentifier: WideString read Get_LibraryIdentifier;  // read-only
property LibraryName: WideString read Get_LibraryName;  // read-only
property LibReference: WideString read Get_LibReference;  // read-only
function Get_LibIdentifierKind: TLibIdentifierKind;
function Get_LibraryIdentifier: WideString;
function Get_LibraryName: WideString;
function Get_LibReference: WideString;

## ILibraryComponentData
继承：ILibraryComponentData → IInterface ｜ 单元：RT_IntegratedLibrary ｜ 自有 17 个方法、0 个属性

function CanEditPCBModels: Boolean;
function CanEditSCHSymbol: Boolean;
procedure EditPCBModel(const AModelGuid: WideString);
procedure EditSCHSymbol;
function GetModel(const AIndex: Integer): ILibraryModelData;
function GetParameter(const AIndex: Integer): ILibraryParameterData;
function GetParametersAsString: WideString;
function GetPart(const AIndex: Integer): ILibraryPartData;
function GUID: WideString;
function IsLoaded: Boolean;
procedure Load;
function ModelCount: Integer;
function Name: WideString;
function ParamCount: Integer;
function PartCount: Integer;
function SymbolName: WideString;
function SymbolPath: WideString;

## ILibraryData
继承：ILibraryData → IInterface ｜ 单元：RT_IntegratedLibrary ｜ 自有 12 个方法、0 个属性

function Activated: Boolean;
function FilePath: WideString;
function FindComponentByGUID(const AGUID: WideString): ILibraryComponentData;
function First: ILibraryComponentData;
function GetKeyField(const AIndex: Integer): WideString;
function GetVisibleColumns: WideString;
function GUID: WideString;
function KeyFieldCount: Integer;
function Kind: TLibraryType;
function Name: WideString;
function Next: ILibraryComponentData;
function SubLibraryList: ISubLibraryDataList;

## ILibraryDataReader
继承：ILibraryDataReader → IInterface ｜ 单元：RT_IntegratedLibrary ｜ 自有 18 个方法、0 个属性

function AdvancedSearchComponents(var ASearchType: WideString; const AInterruptor: IInterruptor; const AEventHandler: ISearchLibraryEventHandler): Boolean;
function Count: Integer;
function CreateLibraryLoadContext: ILibraryLoadContext;
function ExportVFSFile(const ASourceFilePath: WideString; const ADestinationFilePath: WideString): Boolean;
function Get(const AIndex: Integer): ILibraryData;
function GetComponentByDesignItemID(const ALibraryName: WideString; const ASubLibraryName: WideString; const ADesignItemID: WideString; AForceLoadLibrary: LongBool): ILibraryComponentData;
function GetComponentSymbolExtParameters(const ALibraryGUID: WideString; const AComponentGUID: WideString): WideString;
function GetMetadata(const AIndex: Integer): ILibraryMetadata;
function GetMetadataByGUID(const AGUID: WideString): ILibraryMetadata;
function GetSpiceComponentPosition(const ALibraryGUID: WideString; const AComponentName: WideString; out AFileName: WideString; out APrevComponentPosition: Int64; out APosition: Int64): Boolean;
function IsVFSFile(const AFilePath: WideString): Boolean;
function LoadLibrary(const AFullFileName: WideString): ILibraryData;
function LoadLibraryWithContext(const AFullFileName: WideString; const AContext: ILibraryLoadContext): ILibraryData;
procedure Refresh;
function RegisterLibrary(const AFullFileName: WideString): ILibraryData;
function SearchComponents(const ALibraryGUIDs: WideString; const AText: WideString): ISearchComponentResultList;
function SearchComponentsEx(const ALibraryGUIDs: WideString; const AText: WideString; const AParameters: WideString): ISearchComponentResultList;
procedure UnregisterLibrary(const AGUID: WideString);

## ILibraryLoadContext
继承：ILibraryLoadContext → IInterface ｜ 单元：RT_IntegratedLibrary ｜ 自有 3 个方法、0 个属性

procedure Clear;
function FindEntityDatafilePath(const ASourceLibraryPath: WideString; const ASourceComponentName: WideString; ALibIdentifierKind: TLibIdentifierKind; const ALibraryIdentifier: WideString; const AEntityName: WideString; const ADatafileType: WideString): WideString;
function RegisterLibrary(const AFilePath: WideString): Boolean;

## ILibraryMetadata
继承：ILibraryMetadata → IInterface ｜ 单元：RT_IntegratedLibrary ｜ 自有 7 个方法、0 个属性

function Activated: Boolean;
function FilePath: WideString;
function GetKeyField(const AIndex: Integer): WideString;
function GUID: WideString;
function KeyFieldCount: Integer;
function Kind: TLibraryType;
function Name: WideString;

## ILibraryModelData
继承：ILibraryModelData → IInterface ｜ 单元：RT_IntegratedLibrary ｜ 自有 12 个方法、0 个属性

function Description: WideString;
function DisplayFilePath: WideString;
function ExportVFSDataToFile(const AFilePath: WideString): Boolean;
function FilePath: WideString;
function GUID: WideString;
function IsDefault: Boolean;
function IsVFSFile: Boolean;
function Kind: WideString;
function Location: WideString;
function LocationType: TLibIdentifierKind;
function Name: WideString;
function Parameters: WideString;

## ILibraryParameterData
继承：ILibraryParameterData → IInterface ｜ 单元：RT_IntegratedLibrary ｜ 自有 3 个方法、0 个属性

function IsVisible: Boolean;
function Name: WideString;
function Value: WideString;

## ILibraryPartData
继承：ILibraryPartData → IInterface ｜ 单元：RT_IntegratedLibrary ｜ 自有 1 个方法、0 个属性

function Name: WideString;

## ILibraryReportExternalSettings
继承：ILibraryReportExternalSettings → IExternalForm → IInterface ｜ 单元：RT_IntegratedLibrary ｜ 自有 5 个方法、1 个属性

property DrawPreviews: Boolean read GetDrawPreviews write SetDrawPreviews;
function GetDrawPreviews: Boolean;
function GetLibraryType: WideString;
procedure GetStateControls;
procedure SetDrawPreviews(Value: Boolean);
procedure SetStateControls;

## ILibraryReportInfo
继承：ILibraryReportInfo → IReportParameters → IInterface ｜ 单元：RT_IntegratedLibrary ｜ 自有 4 个方法、0 个属性

function GetComponentCount: Integer;
function GetComponentList: WideString;
function GetLibraryIterator: ILibObjectIterator;
function GetTitle: WideString;

## ILibraryServer
继承：ILibraryServer → IInterface ｜ 单元：RT_IntegratedLibrary ｜ 自有 5 个方法、0 个属性

function GetDataReader: ILibraryDataReader;
function GetDragDropLibraryComponent(const AParams: WideString; const AModelKind: WideString): IDragDropLibraryComponent;
function GetDragDropLibraryComponent2(const ASymbolParams: WideString; const AFootprintParams: WideString): IDragDropLibraryComponent;
function GetDragDropOfflineVaultComponent: IDragDropOfflineVaultComponent;
function GetDragDropVaultComponent(const AVaultGUID: WideString; const AItemGUID: WideString; const AItemHRID: WideString; const ARevisionGUID: WideString; const ARevisionHRID: WideString; const AContentTypeGUID: WideString; ASelectedItems: IInterfaceList; ASelectedRevisions: IInterfaceList): IDragDropVaultComponent;

## ILicense
继承：ILicense → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 4 个方法、3 个属性

property CanRoam: LongBool read GetCanRoam;  // read-only
property LicenseType: Integer read GetLicenseType;  // read-only
property SerialNumber: Int64 read GetSerialNumber;  // read-only
function CanbeUsedWithThisBuild: LongBool;
function GetCanRoam: LongBool;
function GetLicenseType: Integer;
function GetSerialNumber: Int64;

## ILicenseExpirationInfo
继承：ILicenseExpirationInfo → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 2 个方法、2 个属性

property DaysLeft: Integer read GetDaysLeft;  // read-only
property RightName: WideString read GetRightName;  // read-only
function GetDaysLeft: Integer;
function GetRightName: WideString;

## ILicenseManager
继承：ILicenseManager → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 11 个方法、0 个属性

procedure ChangeToNetwork(const ServerName: WideString);
procedure ChangeToStandalone;
procedure GetCurrentLicenseInfo(out ALicenseIds: WideString; out ALicenseNames: WideString);
procedure GetLicenses(Licenses: TList);
function IsSubscriptionCurrent: Boolean;
procedure ReleaseLicense(const LicenseFileName: WideString);
procedure ReturnLeasedEVSLicensesOnLogout;
procedure ReturnLeasedLicensesOnLogout;
function SubscriptionExpiryDate: TDateTime;
procedure UseLicense(const LicenseFileName: WideString);
procedure UseLicenseByName(const LicenseName: WideString);

## ILine
继承：ILine → IDMObject → IInterface ｜ 单元：RT_Workspace ｜ 自有 5 个方法、0 个属性

function DM_HX: Integer;
function DM_HY: Integer;
function DM_IsInferredFromHarness: Boolean;
function DM_LX: Integer;
function DM_LY: Integer;

## ILocalSnippet
继承：ILocalSnippet → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 5 个方法、5 个属性

property DataFullFileName: WideString read GetDataFullFileName;  // read-only
property Description: WideString read GetDescription;  // read-only
property Kind: TSnippetKind read GetKind;  // read-only
property Name: WideString read GetName;  // read-only
property PreviewFullFileName: WideString read GetPreviewFullFileName;  // read-only
function GetDataFullFileName: WideString;
function GetDescription: WideString;
function GetKind: TSnippetKind;
function GetName: WideString;
function GetPreviewFullFileName: WideString;

## ILocalSnippetFolder
继承：ILocalSnippetFolder → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 8 个方法、6 个属性

property Name: WideString read GetName;  // read-only
property Path: WideString read GetPath;  // read-only
property Snippet[AIndex: Integer]: ILocalSnippet read GetSnippet;  // read-only
property SnippetCount: Integer read GetSnippetCount;  // read-only
property SubFolder[AIndex: Integer]: ILocalSnippetFolder read GetSubFolder;  // read-only
property SubFolderCount: Integer read GetSubFolderCount;  // read-only
procedure AddSnippet(const ASnippet: ILocalSnippet);
procedure AddSubFolder(const AFolder: ILocalSnippetFolder);
function GetName: WideString;
function GetPath: WideString;
function GetSnippet(AIndex: Integer): ILocalSnippet;
function GetSnippetCount: Integer;
function GetSubFolder(AIndex: Integer): ILocalSnippetFolder;
function GetSubFolderCount: Integer;

## ILocalSnippetManager
继承：ILocalSnippetManager → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 11 个方法、3 个属性

property DefaultPath: WideString read GetDefaultPath;  // read-only
property Folder[AIndex: Integer]: ILocalSnippetFolder read GetFolder;  // read-only
property FolderCount: Integer read GetFolderCount;  // read-only
function CanPlaceSnippet(const ADataFullFileName: WideString): Boolean;
function ChooseFolder(const ABasePath: WideString): WideString;
function ConfigFolders: Boolean;
function CreateSnippet(const AName: WideString; const ADescription: WideString; const APath: WideString): Boolean;
function DeleteSnippet(const ADataFullFileName: WideString): Boolean;
function EditSnippet(const ADataFullFileName: WideString; const AName: WideString; const AComment: WideString; const APath: WideString): Boolean;
function GetDefaultPath: WideString;
function GetFolder(AIndex: Integer): ILocalSnippetFolder;
function GetFolderCount: Integer;
procedure PlaceSnippet(const ADataFullFileName: WideString; APlaceAsBlock: Boolean);
procedure RefreshFoldersStructure;

## ILogicSimType
继承：ILogicSimType → IInterface ｜ 单元：Rt_VHDL ｜ 自有 18 个方法、0 个属性

function Sim_GetArrayLeftBound(Value: Pointer): Integer;
function Sim_GetArrayRightBound(Value: Pointer): Integer;
function Sim_GetAsString(Value: Pointer; Radix: TLogicSimRadix): WideString;
function Sim_GetDynamicTypeSize(Value: Pointer): Integer;
function Sim_GetElement(Index: Integer; Value: Pointer): Pointer;
function Sim_GetElementCount(Value: Pointer): Integer;
function Sim_GetElementName(Index: Integer): WideString;
function Sim_GetElementString(Index: Integer; Value: Pointer; Radix: TLogicSimRadix): WideString;
function Sim_GetElementType(Index: Integer; Value: Pointer): ILogicSimType;
function Sim_GetEnum(Index: Integer): WideString;
function Sim_GetEnumCount: Integer;
function Sim_GetModelSimString(Value: Pointer): WideString;
function Sim_GetModelSimStringLength(Value: Pointer): Integer;
function Sim_GetName: PWideChar;
function Sim_GetStaticTypeSize: Integer;
function Sim_GetTypeID: TLogicSimDataTypeID;
function Sim_IsConstrained: Boolean;
function Sim_IsWaveConstrained: Boolean;

## ILsmSdkDocumentEditor
继承：ILsmSdkDocumentEditor → IInterface ｜ 单元：Rt_LayerStackManager.Interfaces ｜ 自有 3 个方法、0 个属性

function GetLayerEditor: ILsmSdkLayerEditor;
function GetLayerStackEditor: ILsmSdkLayerStackEditor;
function GetStackupEditor: ILsmSdkStackupEditor;

## ILsmSdkDrillSpan
继承：ILsmSdkDrillSpan → IInterface ｜ 单元：Rt_LayerStackManager.Interfaces ｜ 自有 5 个方法、5 个属性

property AutoName: WideString read GetState_AutoName;  // read-only
property CustomName: WideString read GetState_CustomName;  // read-only
property DrillSpanType: TLsmSdkDrillSpanType read GetState_Type;  // read-only
property Id: WideString read GetState_Id;  // read-only
property IsSymmetric: Boolean read GetState_IsSymmetric;  // read-only
function GetState_AutoName: WideString;
function GetState_CustomName: WideString;
function GetState_Id: WideString;
function GetState_IsSymmetric: Boolean;
function GetState_Type: TLsmSdkDrillSpanType;

## ILsmSdkDrillSpanCollection
继承：ILsmSdkDrillSpanCollection → IInterface ｜ 单元：Rt_LayerStackManager.Interfaces ｜ 自有 3 个方法、3 个属性

property Count: Integer read GetCount;  // read-only
property Items[const AIndex: Integer]: ILsmSdkDrillSpan read GetItem;  // read-only
property ItemsById[const AId: WideString]: ILsmSdkDrillSpan read GetItemById;  // read-only
function GetCount: Integer;
function GetItem(const AIndex: Integer): ILsmSdkDrillSpan;
function GetItemById(const AId: WideString): ILsmSdkDrillSpan;

## ILsmSdkImpedanceProfile
继承：ILsmSdkImpedanceProfile → IInterface ｜ 单元：Rt_LayerStackManager.Interfaces ｜ 自有 6 个方法、6 个属性

property AutoName: WideString read GetState_AutoName;  // read-only
property CustomName: WideString read GetState_CustomName;  // read-only
property Id: WideString read GetState_Id;  // read-only
property Impedance_ohm: Double read GetState_Impedance_ohm;  // read-only
property ImpedanceProfileType: TLsmSdkImpedanceProfileType read GetState_Type;  // read-only
property TolerancePercent: Double read GetState_TolerancePercent;  // read-only
function GetState_AutoName: WideString;
function GetState_CustomName: WideString;
function GetState_Id: WideString;
function GetState_Impedance_ohm: Double;
function GetState_TolerancePercent: Double;
function GetState_Type: TLsmSdkImpedanceProfileType;

## ILsmSdkImpedanceProfileCollection
继承：ILsmSdkImpedanceProfileCollection → IInterface ｜ 单元：Rt_LayerStackManager.Interfaces ｜ 自有 3 个方法、3 个属性

property Count: Integer read GetCount;  // read-only
property Items[const AIndex: Integer]: ILsmSdkImpedanceProfile read GetItem;  // read-only
property ItemsById[const AId: WideString]: ILsmSdkImpedanceProfile read GetItemById;  // read-only
function GetCount: Integer;
function GetItem(const AIndex: Integer): ILsmSdkImpedanceProfile;
function GetItemById(const AId: WideString): ILsmSdkImpedanceProfile;

## ILsmSdkLayer
继承：ILsmSdkLayer → IXLibEntity ｜ 单元：Rt_LayerStackManager.Interfaces ｜ 自有 27 个方法、14 个属性

property Comment: WideString read GetState_Comment write SetState_Comment;
property ComponentPlacement: TLsmSdkComponentPlacement read GetState_ComponentPlacement write SetState_ComponentPlacement;
property CopperOrientation: TLsmSdkCopperOrientation read GetState_CopperOrientation write SetState_CopperOrientation;
property CoverlayExpansion: TLsmSdkLengthValue read GetState_CoverlayExpansion write SetState_CoverlayExpansion;
property DielectricConstant: TLsmSdkNullableDouble read GetState_DielectricConstant write SetState_DielectricConstant;
property HasPrimitives: Boolean read GetState_HasPrimitives;  // read-only
property IsEnabled: Boolean read GetState_IsEnabled;  // read-only
property LossTangent: TLsmSdkNullableDouble read GetState_LossTangent write SetState_LossTangent;
property MaterialName: WideString read GetState_MaterialName write SetState_MaterialName;
property Name: WideString read GetState_Name;  // read-only
property Note: WideString read GetState_Note write SetState_Note;
property ParentStack: ILsmSdkLayerStack read GetState_ParentStack;  // read-only
property PullbackDistance: TLsmSdkLengthValue read GetState_PullbackDistance write SetState_PullbackDistance;
property Thickness: TLsmSdkLengthValue read GetState_Thickness write SetState_Thickness;
function GetState_Comment: WideString;
function GetState_ComponentPlacement: TLsmSdkComponentPlacement;
function GetState_CopperOrientation: TLsmSdkCopperOrientation;
function GetState_CoverlayExpansion: IDispatch;
function GetState_DielectricConstant: IDispatch;
function GetState_HasPrimitives: Boolean;
function GetState_IsEnabled: Boolean;
function GetState_LossTangent: IDispatch;
function GetState_MaterialName: WideString;
function GetState_Name: WideString;
function GetState_Note: WideString;
function GetState_ParentStack: ILsmSdkLayerStack;
function GetState_PositionInStack: Integer;
function GetState_PullbackDistance: IDispatch;
function GetState_Thickness: IDispatch;
procedure SetState_Comment(const AValue: WideString);
procedure SetState_ComponentPlacement(const AValue: TLsmSdkComponentPlacement);
procedure SetState_CopperOrientation(const AValue: TLsmSdkCopperOrientation);
procedure SetState_CoverlayExpansion(const AValue: IDispatch);
procedure SetState_DielectricConstant(const AValue: IDispatch);
procedure SetState_IsEnabled(const AValue: Boolean);
procedure SetState_LossTangent(const AValue: IDispatch);
procedure SetState_MaterialName(const AValue: WideString);
procedure SetState_Name(const AValue: WideString);
procedure SetState_Note(const AValue: WideString);
procedure SetState_PullbackDistance(const AValue: IDispatch);
procedure SetState_Thickness(const AValue: IDispatch);

## ILsmSdkLayerCollection
继承：ILsmSdkLayerCollection → IInterface ｜ 单元：Rt_LayerStackManager.Interfaces ｜ 自有 3 个方法、3 个属性

property Count: Integer read GetCount;  // read-only
property Items[const AIndex: Integer]: ILsmSdkLayer read GetItem;  // read-only
property ItemsById[const AId: WideString]: ILsmSdkLayer read GetItemById;  // read-only
function GetCount: Integer;
function GetItem(const AIndex: Integer): ILsmSdkLayer;
function GetItemById(const AId: WideString): ILsmSdkLayer;

## ILsmSdkLayerEditor
继承：ILsmSdkLayerEditor → IInterface ｜ 单元：Rt_LayerStackManager.Interfaces ｜ 自有 18 个方法、0 个属性

function CanDeleteLayer(const LayerId: WideString; const StackId: WideString): Boolean;
function CanInsertDefaultLayer(const LayerTypeId: WideString; const StackId: WideString; const RefLayerId: WideString; InsertBefore: Boolean): Boolean;
function CanInsertLayer(const Layer: ILsmSdkLayer; const StackId: WideString; const RefLayerId: WideString; InsertBefore: Boolean): Boolean;
function CanIntelliAddLayer(const LayerTypeId: WideString; const StackId: WideString; const RefLayerId: WideString): Boolean;
function CanIntelliMoveLayerDown(const LayerId: WideString; const StackId: WideString): Boolean;
function CanIntelliMoveLayerUp(const LayerId: WideString; const StackId: WideString): Boolean;
function CanMoveLayer(const LayerId: WideString; const StackId: WideString; const RefLayerId: WideString; InsertBefore: Boolean): Boolean;
function CanMoveLayerOnePositionDown(const LayerId: WideString; const StackId: WideString): Boolean;
function CanMoveLayerOnePositionUp(const LayerId: WideString; const StackId: WideString): Boolean;
procedure DeleteLayer(const LayerId: WideString; const StackId: WideString);
procedure InsertLayer(const Layer: ILsmSdkLayer; const StackId: WideString; const RefLayerId: WideString; InsertBefore: Boolean);
function IntelliAddLayer(const LayerTypeId: WideString; const StackId: WideString; const RefLayerId: WideString): ILsmSdkLayer;
procedure IntelliMoveLayerDown(const LayerId: WideString; const StackId: WideString);
procedure IntelliMoveLayerUp(const LayerId: WideString; const StackId: WideString);
procedure MoveLayer(const LayerId: WideString; const StackId: WideString; const RefLayerId: WideString; InsertBefore: Boolean);
procedure MoveLayerOnePositionDown(const LayerId: WideString; const StackId: WideString);
procedure MoveLayerOnePositionUp(const LayerId: WideString; const StackId: WideString);
procedure UpdateLayer(const Layer: ILsmSdkLayer; const StackId: WideString);

## ILsmSdkLayerStack
继承：ILsmSdkLayerStack → IInterface ｜ 单元：Rt_LayerStackManager.Interfaces ｜ 自有 12 个方法、9 个属性

property DrillSpans: ILsmSdkDrillSpanCollection read GetState_DrillSpans;  // read-only
property Id: WideString read GetState_Id;  // read-only
property IsFlex: Boolean read GetState_IsFlex;  // read-only
property IsManaged: Boolean read GetState_IsManaged;  // read-only
property IsSymmetric: Boolean read GetState_IsSymmetric;  // read-only
property Layers: ILsmSdkLayerCollection read GetState_Layers;  // read-only
property LayerStackType: TLayerStackType read GetState_Type;  // read-only
property Name: WideString read GetState_Name;  // read-only
property ViaSpans: ILsmSdkViaSpanCollection read GetState_ViaSpans;  // read-only
function GetState_DrillSpans: ILsmSdkDrillSpanCollection;
function GetState_Id: WideString;
function GetState_IsFlex: Boolean;
function GetState_IsManaged: Boolean;
function GetState_IsSymmetric: Boolean;
function GetState_Layers: ILsmSdkLayerCollection;
function GetState_Name: WideString;
function GetState_Type: TLayerStackType;
function GetState_ViaSpans: ILsmSdkViaSpanCollection;
procedure SetState_IsFlex(const AValue: Boolean);
procedure SetState_IsSymmetric(const AValue: Boolean);
procedure SetState_Name(const AName: WideString);

## ILsmSdkLayerStackCollection
继承：ILsmSdkLayerStackCollection → IInterface ｜ 单元：Rt_LayerStackManager.Interfaces ｜ 自有 3 个方法、3 个属性

property Count: Integer read GetCount;  // read-only
property Items[const AIndex: Integer]: ILsmSdkLayerStack read GetItem;  // read-only
property ItemsById[const AId: WideString]: ILsmSdkLayerStack read GetItemById;  // read-only
function GetCount: Integer;
function GetItem(const AIndex: Integer): ILsmSdkLayerStack;
function GetItemById(const AId: WideString): ILsmSdkLayerStack;

## ILsmSdkLayerStackEditor
继承：ILsmSdkLayerStackEditor → IInterface ｜ 单元：Rt_LayerStackManager.Interfaces ｜ 自有 9 个方法、0 个属性

function CanDeleteStack(const StackId: WideString): Boolean;
function CanInsertDefaultStack(const RefStackId: WideString; InsertBefore: Boolean): Boolean;
function CanInsertStack(const LayerStack: ILsmSdkLayerStack; const RefStackId: WideString; InsertBefore: Boolean): Boolean;
function CanMoveStack(const StackId: WideString; const RefStackId: WideString; InsertBefore: Boolean): Boolean;
function CanUpdateStack(const LayerStack: ILsmSdkLayerStack): Boolean;
procedure DeleteStack(const StackId: WideString);
function InsertStack(const LayerStack: ILsmSdkLayerStack; const RefStackId: WideString; InsertBefore: Boolean): ILsmSdkLayerStack;
procedure MoveStack(const StackId: WideString; const RefStackId: WideString; InsertBefore: Boolean);
procedure UpdateStack(const LayerStack: ILsmSdkLayerStack);

## ILsmSdkStackup
继承：ILsmSdkStackup → IInterface ｜ 单元：Rt_LayerStackManager.Interfaces ｜ 自有 8 个方法、8 个属性

property ImpedanceProfiles: ILsmSdkImpedanceProfileCollection read GetState_ImpedanceProfiles;  // read-only
property IsSymmetric: Boolean read GetState_IsSymmetric;  // read-only
property RoughnessFactorModelRFPercent: Double read GetState_RoughnessFactorModelRFPercent;  // read-only
property RoughnessFactorModelSR_mm: Double read GetState_RoughnessFactorModelSR_mm;  // read-only
property RoughnessModelType: TLsmSdkRoughnessModelType read GetState_RoughnessModelType;  // read-only
property Stacks: ILsmSdkLayerStackCollection read GetState_Stacks;  // read-only
property StackupType: TLsmSdkStackupType read GetState_Type;  // read-only
property TransmissionLines: ILsmSdkTransmissionLineCollection read GetState_TransmissionLines;  // read-only
function GetState_ImpedanceProfiles: ILsmSdkImpedanceProfileCollection;
function GetState_IsSymmetric: Boolean;
function GetState_RoughnessFactorModelRFPercent: Double;
function GetState_RoughnessFactorModelSR_mm: Double;
function GetState_RoughnessModelType: TLsmSdkRoughnessModelType;
function GetState_Stacks: ILsmSdkLayerStackCollection;
function GetState_TransmissionLines: ILsmSdkTransmissionLineCollection;
function GetState_Type: TLsmSdkStackupType;

## ILsmSdkStackupEditor
继承：ILsmSdkStackupEditor → IInterface ｜ 单元：Rt_LayerStackManager.Interfaces ｜ 自有 3 个方法、0 个属性

function CanUpdateStackup(const Stackup: ILsmSdkStackup): Boolean;
procedure MakeStackupSymmetric(const Stackup: ILsmSdkStackup; SymmetricOptions: TLsmSdkStackupSymmetricOptions);
procedure UpdateStackup(const Stackup: ILsmSdkStackup);

## ILsmSdkTransmissionLine
继承：ILsmSdkTransmissionLine → IInterface ｜ 单元：Rt_LayerStackManager.Interfaces ｜ 自有 19 个方法、19 个属性

property BottomRefLayerId: WideString read GetState_BottomRefLayerId;  // read-only
property CalcMode: TLsmSdkTLCalcMode read GetState_CalcMode;  // read-only
property ClearanceToPlane_mm: TLsmSdkNullableDouble read GetState_ClearanceToPlane_mm;  // read-only
property CoatedHeight1_mm: TLsmSdkNullableDouble read GetState_CoatedHeight1_mm;  // read-only
property CoatedHeight2_mm: TLsmSdkNullableDouble read GetState_CoatedHeight2_mm;  // read-only
property CoatedLayerId: WideString read GetState_CoatedLayerId;  // read-only
property ElectricParameters: TLsmSdkTLElectricParams read GetState_ElectricParameters;  // read-only
property EtchFactor: TLsmSdkNullableDouble read GetState_EtchFactor;  // read-only
property HasPlating: Boolean read GetState_HasPlating;  // read-only
property Id: TLsmSdkTLId read GetState_Id;  // read-only
property ImpedanceErrorPercent: TLsmSdkNullableDouble read GetState_ImpedanceErrorPercent;  // read-only
property IsCoated: Boolean read GetState_IsCoated;  // read-only
property IsCoplanar: Boolean read GetState_IsCoplanar;  // read-only
property IsDifferential: Boolean read GetState_IsDifferential;  // read-only
property IsEnabled: Boolean read GetState_IsEnabled;  // read-only
property TLTypeName: WideString read GetState_TLTypeName;  // read-only
property TopRefLayerId: WideString read GetState_TopRefLayerId;  // read-only
property TraceGap_mm: TLsmSdkNullableDouble read GetState_TraceGap_mm;  // read-only
property TraceWidth_mm: TLsmSdkNullableDouble read GetState_TraceWidth_mm;  // read-only
function GetState_BottomRefLayerId: WideString;
function GetState_CalcMode: TLsmSdkTLCalcMode;
function GetState_ClearanceToPlane_mm: IDispatch;
function GetState_CoatedHeight1_mm: IDispatch;
function GetState_CoatedHeight2_mm: IDispatch;
function GetState_CoatedLayerId: WideString;
function GetState_ElectricParameters: IDispatch;
function GetState_EtchFactor: IDispatch;
function GetState_HasPlating: Boolean;
function GetState_Id: IDispatch;
function GetState_ImpedanceErrorPercent: IDispatch;
function GetState_IsCoated: Boolean;
function GetState_IsCoplanar: Boolean;
function GetState_IsDifferential: Boolean;
function GetState_IsEnabled: Boolean;
function GetState_TLTypeName: WideString;
function GetState_TopRefLayerId: WideString;
function GetState_TraceGap_mm: IDispatch;
function GetState_TraceWidth_mm: IDispatch;

## ILsmSdkTransmissionLineCollection
继承：ILsmSdkTransmissionLineCollection → IInterface ｜ 单元：Rt_LayerStackManager.Interfaces ｜ 自有 3 个方法、3 个属性

property Count: Integer read GetCount;  // read-only
property Items[const AIndex: Integer]: ILsmSdkTransmissionLine read GetItem;  // read-only
property ItemsById[const AId: IDispatch]: ILsmSdkTransmissionLine read GetItemById;  // read-only
function GetCount: Integer;
function GetItem(const AIndex: Integer): ILsmSdkTransmissionLine;
function GetItemById(const AId: IDispatch): ILsmSdkTransmissionLine;

## ILsmSdkViaSpan
继承：ILsmSdkViaSpan → IInterface ｜ 单元：Rt_LayerStackManager.Interfaces ｜ 自有 5 个方法、5 个属性

property AutoName: WideString read GetState_AutoName;  // read-only
property CustomName: WideString read GetState_CustomName;  // read-only
property Id: WideString read GetState_Id;  // read-only
property IsSymmetric: Boolean read GetState_IsSymmetric;  // read-only
property ViaSpanType: TLsmSdkViaSpanType read GetState_Type;  // read-only
function GetState_AutoName: WideString;
function GetState_CustomName: WideString;
function GetState_Id: WideString;
function GetState_IsSymmetric: Boolean;
function GetState_Type: TLsmSdkViaSpanType;

## ILsmSdkViaSpanCollection
继承：ILsmSdkViaSpanCollection → IInterface ｜ 单元：Rt_LayerStackManager.Interfaces ｜ 自有 3 个方法、3 个属性

property Count: Integer read GetCount;  // read-only
property Items[const AIndex: Integer]: ILsmSdkViaSpan read GetItem;  // read-only
property ItemsById[const AId: WideString]: ILsmSdkViaSpan read GetItemById;  // read-only
function GetCount: Integer;
function GetItem(const AIndex: Integer): ILsmSdkViaSpan;
function GetItemById(const AId: WideString): ILsmSdkViaSpan;

## IMBA_ServerDocument
继承：IMBA_ServerDocument → IServerDocument → IInterface ｜ 单元：RT_MBA ｜ 自有 18 个方法、6 个属性

property Controller: IMBA_DocumentController read GetState_Controller;  // read-only
property DataModel: IMBA_DocumentDataModel read GetState_DataModel;  // read-only
property DocumentID: Integer read GetState_DocumentID write SetState_DocumentID;
property NotificationPublisher: IMBA_NotificationPublisher read GetState_NotificationPublisher;  // read-only
property UniqueID: WideString read GetState_UniqueID write SetState_UniqueID;
property ViewConfiguration: IMBA_ViewConfiguration read GetState_ViewConfiguration;  // read-only
procedure BeginCompilationLock;
procedure EndCompilationLock;
procedure Export3D(const AFileName: WideString; AFormat: TMBAExport3DFormat);
procedure ExportMbaBin(const AFileName: WideString);
function ExportPartToGraphite(AUid: Integer; const AFileName: WideString): Boolean;
function GetState_Controller: IMBA_DocumentController;
function GetState_DataModel: IMBA_DocumentDataModel;
function GetState_DocumentID: Integer;
function GetState_NotificationPublisher: IMBA_NotificationPublisher;
function GetState_UniqueID: WideString;
function GetState_ViewConfiguration: IMBA_ViewConfiguration;
function HasUniqueIDLoadedFromFile: Boolean;
procedure InvalidateDataModel;
function LoadPCBModel(const FileName: WideString): IMBA_PartDataModel;
function LoadStepModel(const FileName: WideString; NeedToCache: Boolean): IMBA_PartDataModel;
procedure SetState_DocumentID(const AValue: Integer);
procedure SetState_UniqueID(const AValue: WideString);
procedure ToggleMeasurementSystem;

## IMBA_ServerDocumentStates
继承：IMBA_ServerDocumentStates → IInterface ｜ 单元：RT_MBA ｜ 自有 1 个方法、0 个属性

function GetServerDocumentState(AState: TMBA_ServerDocumentStates): TMBA_ServerDocumentStateResult;

## IMBA_ServerModule
继承：IMBA_ServerModule → IServerModule → IInterface ｜ 单元：RT_MBA ｜ 自有 7 个方法、2 个属性

property GlobalGeneralConfiguration: IMBA_GeneralConfiguration read GetState_GlobalGeneralConfiguration;  // read-only
property GlobalViewConfiguration: IMBA_ViewConfiguration read GetState_GlobalViewConfiguration;  // read-only
function CreateDataModelFactory: IMBA_DataModelFactory;
function CreateDocumentFromDataModel(const ADataModel: IMBA_DocumentDataModel): IMBA_ServerDocument;
function GetAssemblyByDocumentId(const ADocumentID: Integer): IMBA_ServerDocument;
function GetAssemblyByPath(const AFullPath: WideString): IMBA_ServerDocument;
function GetState_GlobalGeneralConfiguration: IMBA_GeneralConfiguration;
function GetState_GlobalViewConfiguration: IMBA_ViewConfiguration;
function LoadAssemblyByPath(const AFullPath: WideString): IMBA_ServerDocument;

## IMacroEventListener
继承：IMacroEventListener → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 2 个方法、0 个属性

procedure AfterRecordPlayback(const ARecordId: WideString);
procedure BeforeRecordPlayback(const ARecordId: WideString);

## IMacroManager
继承：IMacroManager → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 6 个方法、1 个属性

property State: TMacroManagerState read GetState write SetState;
function AddRecord(const AServer: WideString; const ACode: WideString; const AData: WideString): Integer;
procedure ExportToPlaybackFile(const AFile: WideString);
function GetState: TMacroManagerState;
procedure Poke;
procedure SetState(Astate: TMacroManagerState);
procedure UpdateRecord(ID: Integer; const ACode: WideString; const AData: WideString);

## IMacroManager2
继承：IMacroManager2 → IMacroManager → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 9 个方法、0 个属性

function AddRecordEx(const AServer: WideString; const ACode: WideString; const AData: WideString; const AComment: WideString): Integer;
procedure ClearRecords;
procedure DeleteRecord(AIndex: Integer);
procedure ExportToPlaybackFileEx(const AFile: WideString; ASavePreferences: Boolean);
procedure GetRecord(AIndex: Integer; var ALineNumber: Integer; var ADelay: Cardinal; var AServer: WideString; var ACode: WideString; var AData: WideString; var AComment: WideString);
function GetRecordCount: Integer;
function GetRecordIndex: Integer;
procedure SetRecordIndex(AIndex: Integer);
procedure UpdateRecordEx(AIndex: Integer; ALineNumber: Integer; ADelay: Cardinal; AServer: WideString; ACode: WideString; AData: WideString; AComment: WideString);

## IMacroProcessor
继承：IMacroProcessor → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 1 个方法、0 个属性

procedure PlayRecord(const ACode: WideString; const AData: WideString);

## IMemoryAccess
继承：IMemoryAccess → IInterface ｜ 单元：Rt_NexusDevices ｜ 自有 0 个方法、0 个属性


## IMemoryInstrument
继承：IMemoryInstrument → IScriptedInstrument → IInterface ｜ 单元：RT_MemoryInstrument ｜ 自有 16 个方法、0 个属性

procedure LoadFromFile(const AFileName: WideString; AStartAddress: Cardinal; ALength: Cardinal);
procedure Read(Buffer: PByte; Address: Cardinal; Length: Integer);
function ReadInt16(AAddress: Cardinal; ABigEndian: LongBool): SmallInt;
function ReadInt32(AAddress: Cardinal; ABigEndian: LongBool): Integer;
function ReadInt8(AAddress: Cardinal; ABigEndian: LongBool): ShortInt;
function ReadUInt16(AAddress: Cardinal; ABigEndian: LongBool): Word;
function ReadUInt32(AAddress: Cardinal; ABigEndian: LongBool): Cardinal;
function ReadUInt8(AAddress: Cardinal; ABigEndian: LongBool): Byte;
procedure SaveToFile(const AFileName: WideString; AStartAddress: Cardinal; ALength: Cardinal);
procedure Write(Buffer: PByte; Address: Cardinal; Length: Integer);
procedure WriteInt16(AAddress: Cardinal; ABigEndian: LongBool; AValue: SmallInt);
procedure WriteInt32(AAddress: Cardinal; ABigEndian: LongBool; AValue: Integer);
procedure WriteInt8(AAddress: Cardinal; ABigEndian: LongBool; AValue: ShortInt);
procedure WriteUInt16(AAddress: Cardinal; ABigEndian: LongBool; AValue: Word);
procedure WriteUInt32(AAddress: Cardinal; ABigEndian: LongBool; AValue: Cardinal);
procedure WriteUInt8(AAddress: Cardinal; ABigEndian: LongBool; AValue: Byte);

## IMemoryInstrumentManager
继承：IMemoryInstrumentManager → IScriptedInstrumentManager → IInterface ｜ 单元：RT_MemoryInstrument ｜ 自有 4 个方法、0 个属性

function GetMemoryInstrument(Index: Integer): IMemoryInstrument;
function GetMemoryInstrumentByDesignator(const ADesignator: WideString): IMemoryInstrument;
function GetMemoryInstrumentByJtagIndex(AJtagIndex: Integer): IMemoryInstrument;
function GetMemoryInstrumentCount: Integer;

## IMemorySpace
继承：IMemorySpace → IInterface ｜ 单元：Rt_NexusDevices ｜ 自有 10 个方法、0 个属性

function FinishDownload: Boolean;
function GetBytesPerUnit: Integer;
function GetIndex: Integer;
function GetKind: TMemoryKind;
function GetLength: Int64;
function GetName: WideString;
function GetNexusDevice: INexusDevice;
function GetShortName: WideString;
function GetWidth: Integer;
function InitDownload: Boolean;

## IMenuItemInvoke
继承：IMenuItemInvoke → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 1 个方法、0 个属性

procedure InvokeItem;

## IMenuItemWrapper
继承：IMenuItemWrapper → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 14 个方法、11 个属性

property AutoCheck: LongBool read GetAutoCheck;  // read-only
property Bitmap: HBITMAP read GetBitmap;  // read-only
property Caption: WideString read GetCaption;  // read-only
property Checked: LongBool read GetChecked write SetChecked;
property Enabled: LongBool read GetEnabled;  // read-only
property GroupIndex: Integer read GetGroupIndex;  // read-only
property Hint: WideString read GetHint;  // read-only
property ImageIndex: Integer read GetImageIndex;  // read-only
property OnInvoke: IMenuItemInvoke read GetOnInvoke;  // read-only
property ShortCut: Word read GetShortCut;  // read-only
property Visible: LongBool read GetVisible;  // read-only
function GetAutoCheck: LongBool;
function GetBitmap: HBITMAP;
function GetCaption: WideString;
function GetChecked: LongBool;
function GetEnabled: LongBool;
function GetGroupIndex: Integer;
function GetHint: WideString;
function GetImageIndex: Integer;
function GetOnInvoke: IMenuItemInvoke;
function GetShortCut: Word;
function GetVisible: LongBool;
function Item(Index: Integer): IMenuItemWrapper;
function ItemCount: Integer;
procedure SetChecked(Value: LongBool);

## IMenuWrapper
继承：IMenuWrapper → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 3 个方法、0 个属性

function ImageListHandle: NativeUInt;
function Item(Index: Integer): IMenuItemWrapper;
function ItemCount: Integer;

## IMessageView
继承：IMessageView → IInterface ｜ 单元：RT_Workspace ｜ 自有 3 个方法、0 个属性

function CanRunActionFromParameters(const Parameters: WideString; var ACaption: WideString; var AImage: WideString): ByteBool;
function MessageGrouping: WideString;
procedure RunActionFromParameters(const Parameters: WideString);

## IMessagesNotification
继承：IMessagesNotification → INotification → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 1 个方法、1 个属性

property Code: Integer read GetCode;  // read-only
function GetCode: Integer;

## IModel
继承：IModel → IInterface ｜ 单元：RT_IntegratedLibrary ｜ 自有 21 个方法、12 个属性

property DataFileEntityCount: Integer read Get_DataFileEntityCount;  // read-only
property DataFileEntityLocation[Index: Integer]: WideString read Get_DataFileEntityLocation;  // read-only
property DataFileEntityName[Index: Integer]: WideString read Get_DataFileEntityName;  // read-only
property ModelDescription: WideString read Get_ModelDescription write Set_ModelDescription;
property ModelMapAsString: WideString read Get_ModelMapAsString write Set_ModelMapAsString;
property ModelName: WideString read Get_ModelName write Set_ModelName;
property ModelParameterCount: Integer read Get_ModelParameterCount;  // read-only
property ModelParameterName[Index: Integer]: WideString read Get_ModelParameterName;  // read-only
property ModelParameters[Index: Integer]: IItemParameter read Get_ModelParameter;  // read-only
property ModelParameterValue[Index: Integer]: WideString read Get_ModelParameterValue;  // read-only
property Owner: ILibraryComponent read Get_Owner;  // read-only
property UseComponentLibrary: Boolean read Get_UseComponentLibrary write Set_UseComponentLibrary;
procedure DeleteModelParameter(Index: Integer);
procedure DeleteModelParameterByName(AName: WideString);
function Get_DataFileEntityCount: Integer;
function Get_DataFileEntityLocation(Index: Integer): WideString;
function Get_DataFileEntityName(Index: Integer): WideString;
function Get_ModelDescription: WideString;
function Get_ModelMapAsString: WideString;
function Get_ModelName: WideString;
function Get_ModelParameter(Index: Integer): IItemParameter;
function Get_ModelParameterCount: Integer;
function Get_ModelParameterName(Index: Integer): WideString;
function Get_ModelParameterValue(Index: Integer): WideString;
function Get_Owner: ILibraryComponent;
function Get_UseComponentLibrary: Boolean;
function GetModelParameterByName(AName: WideString): IItemParameter;
function GetModelParameterValueByName(AName: WideString): WideString;
procedure Set_ModelDescription(Value: WideString);
procedure Set_ModelMapAsString(Value: WideString);
procedure Set_ModelName(Value: WideString);
procedure Set_UseComponentLibrary(Value: Boolean);
procedure SetModelParameterValueByName(AName: WideString; AValue: WideString);

## IModelDatafile
继承：IModelDatafile → IInterface ｜ 单元：RT_IntegratedLibrary ｜ 自有 4 个方法、1 个属性

property EntityNames[AnIndex: Integer]: WideString read EntityName;  // read-only
procedure AddEntity(AName: WideString);
function EntityCount: Integer;
function EntityName(AnIndex: Integer): WideString;
function FullPath: WideString;

## IModelDatafileType
继承：IModelDatafileType → IInterface ｜ 单元：RT_IntegratedLibrary ｜ 自有 6 个方法、0 个属性

function Description: PWideChar;
function EntityType: PWideChar;
function ExtensionFilter: PWideChar;
function FileKind: PWideChar;
function ModelType: IModelType;
function SupportsParameters: Boolean;

## IModelEditor
继承：IModelEditor → IInterface ｜ 单元：RT_IntegratedLibrary ｜ 自有 16 个方法、0 个属性

function CreateDatafile(ADatafilePath: PWideChar): IModelDatafile;
function CreateServerModel(AModel: IComponentImplementation): IServerModel;
procedure CrossProbeEntity(AEntityName: WideString; ADatafilePath: WideString);
procedure DrawModel(AExternalForm: IExternalForm; AModelName: PWideChar; ADatafilePath: PWideChar);
function DrawModel_FromModel(AExternalForm: IExternalForm; AModel: IModel): Boolean;
function DrawModel_FromSchImpl(AExternalForm: IExternalForm; ASchComp: ISch_Component; ASchImpl: ISch_Implementation): Boolean;
function DrawModel_FromStepFile(AExternalForm: IExternalForm; AStepFilePath: WideString): Boolean;
procedure DrawModelToMetaFile(const AFileName: WideString; const AModelName: WideString; const ADatafilePath: WideString; APaintColorMode: TPaintColorMode; APaintScaleMode: TPaintScaleMode);
function EditModel(SchModel: ISch_Implementation; SchComp: ISch_Component; Context: TModelEditContext): Boolean;
function EditModelMap(const AModelRevision: IULB_ItemRevision; const AVault: IEDMS_Vault; const ASchComp: ISch_Component; var AMapAsString: WideString; var AExcludedParts: WideString): Boolean;
procedure FinishedLibraryCompile;
function GetEntityParameters(AEntityName: WideString; ADatafilePath: WideString): WideString;
function GetExternalForm: IExternalForm;
function PrepareModel(AModel: IComponentImplementation): Boolean;
function SetDefaultModelState(SchModel: ISch_Implementation; SchComp: ISch_Component; IsLibrary: Boolean): Boolean;
procedure StartingLibraryCompile;

## IModelEditor2
继承：IModelEditor2 → IInterface ｜ 单元：RT_IntegratedLibrary ｜ 自有 3 个方法、0 个属性

procedure Config(AExternalForm: IExternalForm; Parameters: WideString);
procedure DrawModel_FromHandle(AExternalForm: IExternalForm; AComponentHandle: Pointer);
procedure DrawModel_FromPCBPrimitive(AExternalForm: IExternalForm; APCBPrimitive: IInterface);

## IModelEditor3
继承：IModelEditor3 → IInterface ｜ 单元：RT_IntegratedLibrary ｜ 自有 3 个方法、0 个属性

function EditModel_ReadOnly(SchModel: ISch_Implementation; SchComp: ISch_Component; Context: TModelEditContext): Boolean;
function GetEntityParametersSkipModels(AEntityName: WideString; ADatafilePath: WideString): WideString;
function ReadComponentParamsTOCFromLibraryFile(const ADatafilePath: WideString): WideString;

## IModelEditor4
继承：IModelEditor4 → IInterface ｜ 单元：RT_IntegratedLibrary ｜ 自有 1 个方法、0 个属性

function InitModel(SchModel: ISch_Implementation; SchComp: ISch_Component): Boolean;

## IModelEditorSelectionListener
继承：IModelEditorSelectionListener → IInterface ｜ 单元：RT_IntegratedLibrary ｜ 自有 1 个方法、0 个属性

procedure PinSelectionChanged(NewSelectedPins: WideString);

## IModelEditorSelectionManager
继承：IModelEditorSelectionManager → IInterface ｜ 单元：RT_IntegratedLibrary ｜ 自有 5 个方法、0 个属性

procedure ClearPinSelection;
procedure NotifyPinSelectionChanged(const ANewSelectedPins: WideString; const AModelID: WideString);
procedure RegisterSelectionListener(const AListener: IModelEditorSelectionListener; const AModelID: WideString);
procedure Reset;
procedure UnregisterSelectionListener(const AListener: IModelEditorSelectionListener);

## IModelEditorSelectionManagerController
继承：IModelEditorSelectionManagerController → IInterface ｜ 单元：RT_IntegratedLibrary ｜ 自有 2 个方法、0 个属性

procedure ResetManager;
procedure SetManager(const AManager: IModelEditorSelectionManager);

## IModelType
继承：IModelType → IInterface ｜ 单元：RT_IntegratedLibrary ｜ 自有 10 个方法、0 个属性

function Description: PWideChar;
function DescriptionW: WideString;
function Editor: IModelEditor;
function Highlightable: Boolean;
function Name: PWideChar;
function NameW: WideString;
function PortDescriptor: PWideChar;
function Previewable: Boolean;
function ServerName: PWideChar;
function ViewableDocKind: PWideChar;

## IModelTypeManager
继承：IModelTypeManager → IInterface ｜ 单元：RT_IntegratedLibrary ｜ 自有 7 个方法、2 个属性

property ModelDatafileTypes[AnIndex: Integer]: IModelDatafileType read ModelDatafileTypeAt;  // read-only
property ModelTypes[AnIndex: Integer]: IModelType read ModelTypeAt;  // read-only
function ModelDatafileTypeAt(AnIndex: Integer): IModelDatafileType;
function ModelDatafileTypeCount: Integer;
function ModelDatafileTypeFromKind(AKind: PWideChar): IModelDatafileType;
function ModelTypeAt(AnIndex: Integer): IModelType;
function ModelTypeCount: Integer;
function ModelTypeFromName(AName: PWideChar): IModelType;
function ModelTypeFromServerName(AName: PWideChar): IModelType;

## IModification
继承：IModification → IInterface ｜ 单元：RT_Workspace ｜ 自有 24 个方法、6 个属性

property Enabled: Boolean read GetEnabled write SetEnabled;
property ModificationKind: TModificationKind read GetModificationKind write SetModificationKind;
property OwnerDocument: IDocument read GetOwnerDocument;  // read-only
property Status: TModificationStatus read GetStatus write SetStatus;
property TargetDocument: IDocument read GetTargetDocument;  // read-only
property Used: Boolean read GetUsed write SetUsed;
function ECO_Action(AMode: TECO_Mode): Boolean;
function GetEnabled: Boolean;
function GetModificationKind: TModificationKind;
function GetOwnerDocument: IDocument;
function GetState_AffectedDocumentDescriptorString: string;
function GetState_AffectedObjectDescriptorString: string;
function GetState_CrossProbeDescriptor1: string;
function GetState_CrossProbeDescriptor2: string;
function GetState_CrossProbeDescriptor3: string;
function GetState_CrossProbeObject1: IDMObject;
function GetState_CrossProbeObject2: IDMObject;
function GetState_CrossProbeObject3: IDMObject;
function GetState_DirectionDescriptorString: string;
function GetState_ModificationDetails: string;
function GetState_VerbString: string;
function GetStatus: TModificationStatus;
function GetTargetDocument: IDocument;
function GetUsed: Boolean;
function ImageIndex: Integer;
procedure LoadDocument(AMode: TECO_Mode; const ARefObject: IDMObject);
procedure SetEnabled(AValue: Boolean);
procedure SetModificationKind(AValue: TModificationKind);
procedure SetStatus(AValue: TModificationStatus);
procedure SetUsed(AValue: Boolean);

## IModuleNotification
继承：IModuleNotification → INotification → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 2 个方法、2 个属性

property Code: Integer read GetCode;  // read-only
property ModuleName: WideString read GetModuleName;  // read-only
function GetCode: Integer;
function GetModuleName: WideString;

## IMotionBlurredPaint
继承：IMotionBlurredPaint → IInterface ｜ 单元：InstrumentPanels ｜ 自有 1 个方法、0 个属性

procedure PaintOnPanel(APanel: TCustomInstrumentBackgroundPanel);

## IMultiCastObserver
继承：IMultiCastObserver → IObserver → IInterface ｜ 单元：System.Classes ｜ 自有 0 个方法、0 个属性


## IMultiboardAssemblyPanelFactory
继承：IMultiboardAssemblyPanelFactory → IInterface ｜ 单元：RT_MBA ｜ 自有 1 个方法、0 个属性

function GetTreeViewPanel: IServerView;

## INanoBoardController
继承：INanoBoardController → IInterface ｜ 单元：Rt_NexusNanoBoard ｜ 自有 1 个方法、0 个属性

procedure SetFrequency(Frequency: Double);

## INavigateAttributes
继承：INavigateAttributes → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 4 个方法、2 个属性

property Address: WideString read GetAddress;  // read-only
property Caption: WideString read GetCaption;  // read-only
function GetAddress: WideString;
function GetCaption: WideString;
function IsSameAddress(const AnAddress: WideString): Boolean;
function SupportsProtocol(const AProtocol: WideString): Boolean;

## INavigationDocument
继承：INavigationDocument → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 1 个方法、0 个属性

function GetDocumentScene: IExternalForm;

## INavigationHistory
继承：INavigationHistory → IInterface ｜ 单元：RT_Workspace ｜ 自有 4 个方法、0 个属性

function CanMoveBackward: LongBool;
function CanMoveForward: LongBool;
procedure MoveBackward;
procedure MoveForward;

## INavigationProvider
继承：INavigationProvider → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 1 个方法、0 个属性

function NavigateTo(const Protocol: WideString; const Target: WideString; const Parameters: WideString; const SourceView: IExternalForm; out TargetView: IExternalForm; out TargetHeaderView: IExternalForm): LongBool;

## INavigationSystem
继承：INavigationSystem → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 11 个方法、0 个属性

procedure DisableHistory;
procedure EnableHistory;
procedure ExpandTargets(var Target: WideString);
function IsHistoryEnabled: Boolean;
function IsProtocolSupported(const Protocol: WideString): LongBool;
function NavigateTo(const CurrentView: IExternalForm; var Destination: WideString; out TargetView: IExternalForm): LongBool;
function NavigateToScene(const CurrentView: IExternalForm; var Destination: WideString; out TargetView: IExternalForm; out TargetHeaderView: IExternalForm): LongBool;
procedure ParseDestinationString(const Destination: WideString; var Protocol: WideString; var Target: WideString; var Parameters: WideString);
function RegisterNavigationProvider(const ProtocolName: WideString; const NavigationProvider: INavigationProvider): NativeUInt;
procedure UnregisterNavigationProtocol(const Protocol: WideString; Handle: NativeUInt);
function ValidatedTarget(Target: WideString): WideString;

## INavigator
继承：INavigator → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 1 个方法、0 个属性

function NavigateTo(const AnAddress: WideString): LongBool;

## INavigatorView
继承：INavigatorView → IExternalForm → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 4 个方法、0 个属性

procedure Close;
function GetAddress: WideString;
procedure Refresh;
procedure Stop;

## INet
继承：INet → IDMObject → IInterface ｜ 单元：RT_Workspace ｜ 自有 57 个方法、0 个属性

function DM_AllNetItemCount: Integer;
function DM_AllNetItems(Index: Integer): INetItem;
function DM_AutoNumber: Integer;
function DM_BusIndex: Integer;
function DM_BusKind: TBusKind;
function DM_BusPrefix: WideString;
function DM_BusRange1: WideString;
function DM_BusRange2: WideString;
function DM_BusRangeValue1: Integer;
function DM_BusRangeValue2: Integer;
function DM_BusSectionParent: INet;
function DM_BusWidth: Integer;
function DM_CalculatedNetName: WideString;
function DM_CountOfElectricalType(AElectric: TPinElectrical): Integer;
function DM_CountOfNonPinItems: Integer;
function DM_CrossSheetConnectorCount: Integer;
function DM_CrossSheetConnectors(Index: Integer): ICrossSheet;
function DM_DirectiveCount: Integer;
function DM_Directives(Index: Integer): INetItem;
procedure DM_DoCrossProbe;
function DM_Electric: TPinElectrical;
function DM_ElectricalString: WideString;
function DM_FullNetName: WideString;
function DM_HarnessType: WideString;
function DM_HasItemOnDocument(Document: IDocument): Boolean;
function DM_HiddenNetName: WideString;
function DM_IsAutoGenerated: Boolean;
function DM_IsBusElement: Boolean;
function DM_IsBusMember: Boolean;
function DM_IsBusSection: Boolean;
function DM_IsLocal: Boolean;
function DM_LineCount: Integer;
function DM_Lines(Index: Integer): ILine;
function DM_NetColor: TColor;
function DM_NetLabelCount: Integer;
function DM_NetLabels(Index: Integer): INetItem;
function DM_NetName: WideString;
function DM_NetNumber: WideString;
function DM_PinCount: Integer;
function DM_Pins(Index: Integer): INetItem;
function DM_PortCount: Integer;
function DM_Ports(Index: Integer): INetItem;
function DM_PowerObjectCount: Integer;
function DM_PowerObjects(Index: Integer): INetItem;
function DM_RangeDefinedByValue: Boolean;
function DM_RemovedHarnessEntries(Index: Integer): INetItem;
function DM_RemovedHarnessEntryCount: Integer;
function DM_RemovedNetItemCount: Integer;
function DM_RemovedNetItems(Index: Integer): INetItem;
function DM_Scope: TNetScope;
function DM_SheetEntryCount: Integer;
function DM_SheetEntrys(Index: Integer): INetItem;
function DM_SignalType: WideString;
function DM_SubWireCount: Integer;
function DM_SubWires(Index: Integer): INet;
function DM_SuppressERC: Boolean;
function DM_TooltipText(PhysicalRoomName: WideString): WideString;

## INetClass
继承：INetClass → IObjectClass → IDMObject → IInterface ｜ 单元：RT_Workspace ｜ 自有 0 个方法、0 个属性


## INetItem
继承：INetItem → IDMObject → IInterface ｜ 单元：RT_Workspace ｜ 自有 61 个方法、0 个属性

function DM_BusIndex: Integer;
function DM_BusKind: TBusKind;
function DM_BusPrefix: WideString;
function DM_BusRange1: WideString;
function DM_BusRange2: WideString;
function DM_BusRangeValue1: Integer;
function DM_BusRangeValue2: Integer;
function DM_BusWidth: Integer;
function DM_ComponentUniqueId: WideString;
function DM_CrossSheetText: WideString;
function DM_DisplayMode: Byte;
function DM_Electric: TPinElectrical;
function DM_Electrical: TPinElectrical;
function DM_ElectricalString: WideString;
function DM_FlattenedNetName: WideString;
function DM_Footprint: WideString;
function DM_FullLogicalPartDesignator: WideString;
function DM_FullPhysicalPartDesignator: WideString;
function DM_FullPinName: WideString;
function DM_FullUniqueId: WideString;
function DM_Id: WideString;
function DM_IsAutoGenerated: Boolean;
function DM_IsBusElement: Boolean;
function DM_IsBusMember: Boolean;
function DM_IsBusSection: Boolean;
function DM_IsHidden: Boolean;
function DM_IsInferredFromHarness: Boolean;
function DM_LinkObject: INetItem;
function DM_LogicalPartDesignator: WideString;
function DM_MatchesPadName(const PadName: WideString): Boolean;
function DM_NetLabelText: WideString;
function DM_NetName: WideString;
function DM_NetNumber: WideString;
function DM_OwnerNetLogical: INet;
function DM_OwnerNetPhysical: INet;
function DM_OwnerPartID: Integer;
function DM_PairSwapId: WideString;
function DM_ParentID: WideString;
function DM_ParentSheetSymbolName: WideString;
function DM_ParentSheetSymbolSheetName: WideString;
function DM_Part: IPart;
function DM_PartID: Integer;
function DM_PartPinSwapId: WideString;
function DM_PartSwapId: WideString;
function DM_PartType: WideString;
function DM_PartUniqueId: WideString;
function DM_PhysicalPartDesignator: WideString;
function DM_PinName: WideString;
function DM_PinNameNoPartId: WideString;
function DM_PinNumber: WideString;
function DM_PinPackageLength: Integer;
function DM_PinPropagationDelay: Double;
function DM_PinSwapId: WideString;
function DM_PortName: WideString;
function DM_PowerText: WideString;
function DM_PrintableNetName(out ShouldBeUsed: Boolean): WideString;
function DM_RangeDefinedByValue: Boolean;
function DM_SheetName: WideString;
function DM_SheetSymbol: ISheetSymbol;
function DM_SignalType: WideString;
function DM_UniqueIdName: WideString;

## INetworkConnector
继承：INetworkConnector → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 1 个方法、0 个属性

function CreateMessageToServer: INetworkMessage;

## INetworkMessage
继承：INetworkMessage → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 2 个方法、0 个属性

procedure Send(FreeAfterSent: LongBool);
procedure WriteString(const Data: AnsiString);

## INexusBreakpoint
继承：INexusBreakpoint → IInterface ｜ 单元：Rt_NexusDevices ｜ 自有 22 个方法、0 个属性

procedure Export_ToCore;
function GetAddressHigh: Word;
function GetAddressLow: Word;
function GetBreakOnRead: LongBool;
function GetBreakOnWrite: LongBool;
function GetData: Byte;
function GetDataMask: Byte;
function GetDescription: WideString;
function GetEnabled: LongBool;
function GetIndex: Integer;
function GetKind: TNexusBreakpointKind;
function GetNexusDevice: INexusDevice;
function GetStopped: LongBool;
procedure Import_FromCore;
procedure SetAddressHigh(Value: Word);
procedure SetAddressLow(Value: Word);
procedure SetBreakOnRead(Value: LongBool);
procedure SetBreakOnWrite(Value: LongBool);
procedure SetData(Value: Byte);
procedure SetDataMask(Value: Byte);
procedure SetEnabled(Value: LongBool);
procedure SetKind(Value: TNexusBreakpointKind);

## INexusCore
继承：INexusCore → IInterface ｜ 单元：Rt_NexusWorkspace ｜ 自有 40 个方法、0 个属性

procedure CrossProbe;
procedure DownloadProgramMemory(NexusDevice: INexusDevice);
procedure Export_CoreGenParameters(Parameters: PWideChar);
function Export_CoreGenParametersToString: WideString;
procedure Export_ToParameters(Parameters: PWideChar);
function Export_ToParameterString: WideString;
function FindFileInProjectPaths(FileName: WideString): WideString;
function GetAspComponentDesignator: WideString;
function GetBaseComponentDesignator: WideString;
function GetChildCore(Index: Integer): INexusCore;
function GetChildCoreCount: Integer;
function GetChildCoreDesignator(Index: Integer): WideString;
function GetChildProgramMemoryCoreCount: Integer;
function GetComponentDesignator: WideString;
function GetComponentDocumentPath: WideString;
function GetCoreKind: TNexusCoreKind;
function GetCrossViewProcessId: Integer;
function GetDescription: WideString;
function GetDeviceName: WideString;
function GetEmbeddedProject: IProject;
function GetEmbeddedProjectPath: WideString;
function GetFPGAProject: IProject;
function GetFPGAProjectPath: WideString;
function GetHexFileEndianness: WideString;
function GetHexFilename: WideString;
function GetHexFilePath: WideString;
function GetHexFileState: TFlowState;
function GetJTagIndex_FromCore: Integer;
function GetLibraryReference: WideString;
function GetNexusWorkbench: INexusWorkbench;
function GetParameterValue(Name: WideString): WideString;
function GetUniqueId: WideString;
procedure Import_FromParameters(Parameters: PWideChar);
procedure Import_FromParameterString(const Parameters: WideString);
function MatchesOtherCore(ACore: INexusCore): Boolean;
procedure SetCrossViewProcessId(ProcessID: NativeUInt);
procedure SetEmbeddedProjectPath(AProjectPath: WideString);
function SupportsParameter(Name: WideString): Boolean;
procedure UpdateHexFileState;
procedure VerifyProgramMemory(NexusDevice: INexusDevice);

## INexusDevice
继承：INexusDevice → IDeviceInformation → IInterface ｜ 单元：Rt_NexusDevices ｜ 自有 71 个方法、0 个属性

function AddSoftBreakpoint(MemorySpace: Integer; Address: Int64): ISoftBreakpoint;
function BitmapHandle: NativeUInt;
procedure ClearAllSoftBreakpoints;
function ConfigureFpgaProject(const AProject: IProject): Boolean;
procedure ContinueFromTemporarySuspend;
procedure ContinueProcessor;
function CoreGen_OutputExtension: WideString;
function CreateViewer: Boolean;
procedure CustomAction_Execute(Index: Integer);
procedure CustomAction_GetState(Index: Integer; var Enabled: LongBool; var Checked: LongBool; var Visible: LongBool; Caption: PWideChar; ImageFile: PWideChar);
function EPM_Download(Address: string; Filename: string; Location: string): Boolean;
function EPM_GetTestResult(TestReg: Integer): Integer;
function EPM_InititateTest: Boolean;
procedure EPM_SetPercentCallBack(const ACallBack: IPercentCallback);
procedure Flash_Configure;
function Flash_Program(BitFilename: WideString): Integer;
function Flash_Reset: LongBool;
function Flash_ResetForBitStream: LongBool;
function FlowStage_Build: IProcessFlow;
function FlowStage_Download: IProcessFlow;
function GetDeviceState: TDeviceState;
function GetDriverStatus: TNexusDriverStatus;
function GetHexFilePath: WideString;
function GetMemorySpace(Index: Integer): IMemorySpace;
function GetMemorySpace_Program: IMemorySpace;
function GetProcessorRegister(Index: Integer): IProcessorRegister;
function GetProcessorRegister_PC: IProcessorRegister;
function GetProcessorRegister_SP: IProcessorRegister;
function GetSoftBreakpoint(MemorySpace: Integer; Address: Int64): ISoftBreakpoint;
function GetUniqueId: WideString;
function GetViewer: IInstrumentView;
function InvalidateResources: Boolean;
function JTagChannel: IJTagChannel;
function JTagIndex: Integer;
function JtagPort: IJtagPort;
function LittleEndian: LongBool;
function MemorySpaceCount: Integer;
function NexusDriver: INexusDriver;
procedure PauseProcessor;
function ProcessorIsPaused: LongBool;
function ProcessorIsReset: LongBool;
function ProcessorIsRunning: LongBool;
function ProcessorRegisterCount: Integer;
function ProgramDevice(BitFilename: WideString): Integer;
function ReadNexusRegisterAtAddress(Address: Byte; BitCount: Integer): Cardinal;
function ReadStringNexusRegisterAtAddress(Address: Byte; BitCount: Integer): WideString;
function ReadUserCode: Cardinal;
procedure ReleaseResources;
function RemoveSoftBreakpoint(MemorySpace: Integer; Address: Int64): LongBool;
function ResetDevice: LongBool;
procedure ResetNexusRegisters;
procedure ResetProcessor;
function RunDiagnostic: LongBool;
procedure RunSingleStepInSubstitutionRegister;
procedure RunSteps(StepCount: Integer);
procedure SetJTagChannel(const AJTagChannel: IJTagChannel);
procedure SetJTagIndex(AJTagIndex: Integer);
procedure SetJtagPort(const APort: IJtagPort);
procedure ShowAboutDialog;
function ShowConfiguration: Boolean;
procedure ShowCurrentSensePanel;
procedure SingleStepProcessor;
function SoftBreakpointCount: Integer;
function StatusString: WideString;
function Supports(Action: PWideChar): LongBool;
procedure TemporarySuspend;
function VendorToolsDescriptor: WideString;
function VendorToolsPresent: LongBool;
function VendorToolsUpToDate: LongBool;
procedure WriteNexusRegisterAtAddress(Address: Byte; BitCount: Integer; Data: Cardinal);
procedure WriteStringNexusRegisterAtAddress(Address: Byte; Data: WideString);

## INexusDeviceConfigurator
继承：INexusDeviceConfigurator → IInterface ｜ 单元：RT_ComponentConfigurator ｜ 自有 1 个方法、0 个属性

function GetDeviceName(AConfiguratorString: WideString): WideString;

## INexusDevicesView
继承：INexusDevicesView → IServerDocumentView → IServerView → IExternalForm → IInterface ｜ 单元：Rt_NexusWorkspace ｜ 自有 0 个方法、0 个属性


## INexusDongle
继承：INexusDongle → IInterface ｜ 单元：Rt_NexusDevices ｜ 自有 8 个方法、0 个属性

function ND_FlushWrite(WantTdo: Boolean): HRESULT;
procedure ND_InitWithDriver(Driver: INexusFTDIDriver);
function ND_JTAG_ReadBit(var ATDO: Byte): HRESULT;
function ND_JTAG_ReadBuf(var Data: WideString): HRESULT;
function ND_JTAG_Write(TCK: Byte; TMS: Byte; TDI: Byte; ReadTdo: Boolean): HRESULT;
function ND_JTAG_WriteBuf(const Data: WideString): HRESULT;
procedure ND_SelectJtagChain(AJTAGChain: Integer);
procedure ND_SetJtagTicks(AJtagTicks: Integer);

## INexusDriver
继承：INexusDriver → IDeviceInformation → IInterface ｜ 单元：Rt_NexusDevices ｜ 自有 79 个方法、0 个属性

function AddSoftBreakpoint(MemorySpace: Integer; Address: Int64): Cardinal;
function ClockCoreGenerator: IClockCoreGenerator;
function ClockCoreTemplateGenerator: IClockCoreTemplateGenerator;
function ClockGeneratorTargetCore: ITargetCoreGenerator;
function ConfigureFpgaProject(const Project: IProject): Boolean;
procedure ContinueProcessor;
function CoreGen_OutputExtension: WideString;
procedure CreateRackViewer;
procedure CustomAction_Execute(Index: Integer);
procedure CustomAction_GetState(Index: Integer; var Enabled: LongBool; var Checked: LongBool; var Visible: LongBool; Caption: PWideChar; ImageFile: PWideChar);
function CustomCoreGenerator(AModuleType: TModuleType): ICustomCoreGenerator;
function EPM_Download(Address: string; Filename: string; Location: string): Boolean;
function EPM_GetTestResult(TestReg: Integer): Integer;
function EPM_InititateTest: Boolean;
procedure EPM_SetPercentCallBack(const ACallBack: IPercentCallback);
function Finalize: LongBool;
function FinishDownload(MemorySpaceIndex: Integer): LongBool;
procedure Flash_Configure;
function Flash_Program(Filename: WideString): Integer;
function Flash_Reset: LongBool;
function Flash_ResetForBitStream: LongBool;
function FlowStage_Build: IProcessFlow;
function FlowStage_Download: IProcessFlow;
function GetBitmapHandle: NativeUInt;
function GetDeviceState: TDeviceState;
function GetDeviceTypeForLicenseCheck: WideString;
function GetEmbeddedConstraintFile: WideString;
function GetFolder_Library: WideString;
function GetMemorySpace_Program: Integer;
function GetMemorySpaceBytesPerUnit(MemorySpaceIndex: Integer): Cardinal;
function GetMemorySpaceCount: Integer;
function GetMemorySpaceKind(MemorySpaceIndex: Integer): TMemoryKind;
function GetMemorySpaceLength(MemorySpaceIndex: Integer): Int64;
function GetMemorySpaceName(MemorySpaceIndex: Integer): WideString;
function GetMemorySpaceShortName(MemorySpaceIndex: Integer): WideString;
function GetMemorySpaceWidth(MemorySpaceIndex: Integer): Cardinal;
function GetNexusDevice: INexusDevice;
function GetProcessorRegisterCount: Integer;
function GetProcessorRegisterName(RegisterIndex: Integer): WideString;
function GetProcessorRegisterShortName(RegisterIndex: Integer): WideString;
function GetProcessorRegisterValue(RegisterIndex: Integer): Cardinal;
function GetProcessorRegisterWideValue(RegisterIndex: Integer): WideString;
function GetProcessorRegisterWidth(RegisterIndex: Integer): Cardinal;
function GetRackViewer: IInstrumentView;
function GetRegisterIndex_PC: Integer;
function GetRegisterIndex_SP: Integer;
function GetSoftBreakpointAddressByteAlign: Integer;
function InitDownload(MemorySpaceIndex: Integer): LongBool;
function InvalidateResources: Boolean;
function LittleEndian: LongBool;
procedure PauseProcessor;
function ProcessorIsPaused: LongBool;
function ProcessorIsReset: LongBool;
function ProcessorIsRunning: LongBool;
function ProcessorIsUsingReducedInstructionSet: LongBool;
function ProgramDevice(Filename: WideString): Integer;
function ReadUserCode: Cardinal;
procedure ReleaseResources;
function RemoveSoftBreakpoint(MemorySpace: Integer; Address: Int64; Replaced: Cardinal): LongBool;
function ResetDevice: LongBool;
procedure ResetNexusRegisters;
procedure ResetProcessor;
function RestoreProcessorState: LongBool;
function RunDiagnostic: LongBool;
procedure RunSingleStepInSubstitutionRegister;
procedure RunSteps(StepCount: Integer);
function SaveProcessorState: LongBool;
procedure SetEmbeddedConstraintFile(AConstraintFile: WideString);
function SetNexusDevice(ANexusDevice: INexusDevice): LongBool;
function SetProcessorRegisterValue(RegisterIndex: Integer; Value: Cardinal): LongBool;
function SetProcessorRegisterWideValue(RegisterIndex: Integer; const Value: WideString): LongBool;
procedure ShowAboutDialog;
function ShowConfiguration: Boolean;
procedure ShowCurrentSensePanel;
procedure SingleStepProcessor;
function Supports(Action: PWideChar): LongBool;
function VendorToolsDescriptor: WideString;
function VendorToolsPresent: LongBool;
function VendorToolsUpToDate: LongBool;

## INexusFTDIDriver
继承：INexusFTDIDriver → IInterface ｜ 单元：Rt_NexusDevices ｜ 自有 8 个方法、0 个属性

function ND_FT_GetDriverParam(Param: Integer; var Data: WideString): HRESULT;
function ND_FT_GetQueueStatus(var QueueCount: Integer): HRESULT;
function ND_FT_Purge(Mask: Cardinal): HRESULT;
function ND_FT_Read(Size: Integer; var Data: WideString): HRESULT;
function ND_FT_ResetDevice: HRESULT;
function ND_FT_SetBaudRate(Rate: Cardinal): HRESULT;
function ND_FT_SetLatencyTimer(Latency: Byte): HRESULT;
function ND_FT_Write(const Data: WideString): HRESULT;

## INexusNotification
继承：INexusNotification → INotification → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 1 个方法、1 个属性

property Code: Integer read GetCode;  // read-only
function GetCode: Integer;

## INexusNotificationWithInterface
继承：INexusNotificationWithInterface → INexusNotification → INotification → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 0 个方法、0 个属性


## INexusNotificationWithObject
继承：INexusNotificationWithObject → INexusNotification → INotification → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 1 个方法、1 个属性

property Data: TObject read GetData;  // read-only
function GetData: IInterface;
function GetData: TObject;

## INexusPort
继承：INexusPort → IInterface ｜ 单元：Rt_NexusWorkspace ｜ 自有 11 个方法、9 个属性

property BoardDeviceCount: Integer read GetBoardDeviceCount;  // read-only
property BoardDevices[Index: Integer]: IDeviceLink read GetBoardDevice;  // read-only
property HardDeviceCount: Integer read GetHardDeviceCount;  // read-only
property HardDevices[Index: Integer]: IDeviceLink read GetHardDevice;  // read-only
property JtagPort: IJtagPort read GetJtagPort;  // read-only
property ProcessorDeviceCount: Integer read GetProcessorDeviceCount;  // read-only
property ProcessorDevices[Index: Integer]: IDeviceLink read GetProcessorDevice;  // read-only
property SoftDeviceCount: Integer read GetSoftDeviceCount;  // read-only
property SoftDevices[Index: Integer]: IDeviceLink read GetSoftDevice;  // read-only
function GetBoardDevice(Index: Integer): IDeviceLink;
function GetBoardDeviceCount: Integer;
function GetHardDevice(Index: Integer): IDeviceLink;
function GetHardDeviceCount: Integer;
function GetJtagPort: IJtagPort;
function GetProcessorDevice(Index: Integer): IDeviceLink;
function GetProcessorDeviceCount: Integer;
function GetShortDescription: WideString;
function GetSoftDevice(Index: Integer): IDeviceLink;
function GetSoftDeviceCount: Integer;
function GetUniqueId: WideString;

## INexusWorkbench
继承：INexusWorkbench → IInterface ｜ 单元：Rt_NexusWorkspace ｜ 自有 17 个方法、8 个属性

property JtagPortCount: Integer read GetJtagPortCount;  // read-only
property JtagPorts[Index: Integer]: IJtagPort read GetJtagPort;  // read-only
property NexusPortCount: Integer read GetNexusPortCount;  // read-only
property NexusPorts[Index: Integer]: INexusPort read GetNexusPort;  // read-only
property PCBProjectLinkCount: Integer read GetPCBProjectLinkCount;  // read-only
property PCBProjectLinks[Index: Integer]: IPCBProjectLink read GetPCBProjectLink;  // read-only
property ProjectLinkCount: Integer read GetProjectLinkCount;  // read-only
property ProjectLinks[Index: Integer]: IProjectLink read GetProjectLink;  // read-only
function GetCoreFromDesignator(const Designator: WideString; const Project: IProject): INexusCore;
function GetCoreFromDevice(const ANexusDevice: INexusDevice): INexusCore;
function GetIsConnected: LongBool;
function GetJtagPort(Index: Integer): IJtagPort;
function GetJtagPortCount: Integer;
function GetNexusPort(Index: Integer): INexusPort;
function GetNexusPortCount: Integer;
function GetPCBProjectLink(Index: Integer): IPCBProjectLink;
function GetPCBProjectLinkCount: Integer;
function GetProcessorDeviceFromDeviceId(const AnId: WideString): IDeviceLink;
function GetProjectFromDevice(const ANexusDevice: INexusDevice): IProject;
function GetProjectLink(Index: Integer): IProjectLink;
function GetProjectLinkCount: Integer;
function GetSoftDeviceFromDeviceId(const AnId: WideString): IDeviceLink;
function Preferences: INexusWorkbenchPreferences;
function ProcessFlowRunner: IProcessFlowRunner;
procedure SynthesizeCoresForProject(const Project: IAbstractVHDLProject; const Configuration: WideString);

## INexusWorkbenchPreferences
继承：INexusWorkbenchPreferences → IInterface ｜ 单元：Rt_NexusWorkspace ｜ 自有 7 个方法、3 个属性

property GoLiveAtStartup: Boolean read GetGoLiveAtStartup write SetGoLiveAtStartup;
property Live: Boolean read GetLive write SetLive;
property Release: Boolean read GetRelease write SetRelease;
function GetGoLiveAtStartup: Boolean;
function GetLive: Boolean;
function GetParameter(const ParamName: WideString): WideString;
function GetRelease: Boolean;
procedure SetGoLiveAtStartup(AValue: Boolean);
procedure SetLive(AValue: Boolean);
procedure SetRelease(AValue: Boolean);

## INoRefCountedObj
继承：INoRefCountedObj → IInterface ｜ 单元：Rt_NexusDevices ｜ 自有 1 个方法、0 个属性

function GetObject: Pointer;

## INote
继承：INote → ITextFrame → IDMObject → IInterface ｜ 单元：RT_Workspace ｜ 自有 0 个方法、0 个属性


## INotification
继承：INotification → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 0 个方法、0 个属性


## INotificationCodeList
继承：INotificationCodeList → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 1 个方法、0 个属性

procedure AddNotificationCode(ACode: Integer);

## INotificationContext
继承：INotificationContext → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 1 个方法、0 个属性

function GetParameters: WideString;

## INotificationHandler
继承：INotificationHandler → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 1 个方法、0 个属性

procedure HandleNotification(const ANotification: INotification);

## IObjectClass
继承：IObjectClass → IDMObject → IInterface ｜ 单元：RT_Workspace ｜ 自有 3 个方法、0 个属性

function DM_MemberCount: Integer;
function DM_Members(Index: Integer): WideString;
function DM_Name: WideString;

## IObjectClassCluster
继承：IObjectClassCluster → IDMObject → IInterface ｜ 单元：RT_Workspace ｜ 自有 6 个方法、0 个属性

function DM_MemberCount(Kind: TPCBClassMemberKind): Integer;
function DM_MemberCountAllKinds: Integer;
function DM_MemberObjects(Kind: TPCBClassMemberKind; Index: Integer): IDMObject;
function DM_Members(Kind: TPCBClassMemberKind; Index: Integer): WideString;
function DM_Name: WideString;
function DM_SameAs(Other: IObjectClassCluster): Boolean;

## IObjectsProviderSetter
继承：IObjectsProviderSetter → IInterface ｜ 单元：RT_Workspace ｜ 自有 0 个方法、0 个属性


## IObserver
继承：IObserver → IInterface ｜ 单元：System.Classes ｜ 自有 3 个方法、1 个属性

property Active: Boolean read GetActive write SetActive;
function GetActive: Boolean;
procedure Removed;
procedure SetActive(Value: Boolean);

## IObserverTrack
继承：IObserverTrack → IInterface ｜ 单元：System.Classes ｜ 自有 1 个方法、1 个属性

property Track: Boolean read GetTrack;  // read-only
function GetTrack: Boolean;

## IOleForm
继承：IOleForm → IInterface ｜ 单元：Vcl.Forms ｜ 自有 2 个方法、0 个属性

procedure OnDestroy;
procedure OnResize;

## IOpenBusComponentConfigurator
继承：IOpenBusComponentConfigurator → IInterface ｜ 单元：RT_ComponentConfigurator ｜ 自有 1 个方法、0 个属性

procedure AutoUpdateConfiguration(const ASchComponent: ISch_Component);

## IOptionPageActions
继承：IOptionPageActions → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 8 个方法、0 个属性

procedure Apply;
function GetDataManager: IOptionsFormDataManager;
function GetOptionPageParams: IOptionPageParams;
procedure Load(const AFileName: WideString);
procedure ResetToDefault;
procedure Save(const AFileName: WideString);
procedure SetInitialState;
procedure UpdateDefaultPrimitivesBoard;

## IOptionPageParams
继承：IOptionPageParams → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 0 个方法、0 个属性


## IOptionsFormDataManager
继承：IOptionsFormDataManager → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 3 个方法、0 个属性

procedure LoadSettingsFromPreR10DXPPrefs(const ARegistryPath: WideString; const AExtractedPath: WideString);
procedure LoadSettingsFromPreviousVersion(APreviousVersionIndex: Integer);
procedure SaveSettingsToFiles(const ASettingsFiles: IStrings);

## IOptionsFormDataManagerExt
继承：IOptionsFormDataManagerExt → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 1 个方法、0 个属性

procedure LoadSettingsFromFilesByMode(const ASettingsFiles: IStrings; const ADocumentsInstallPath: WideString; AImportMode: TOptionsRecImportMode);

## IOptionsManager
继承：IOptionsManager → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 10 个方法、0 个属性

function GetGlobalOptionsReader(const AServerName: WideString): IOptionsReader;
function GetGlobalOptionsWriter(const AServerName: WideString): IOptionsWriter;
function GetOptionsReader(const ServerName: WideString; const OldSettingsPath: WideString): IOptionsReader;
function GetOptionsReader_FromIniFile(const AFullPath: WideString): IOptionsReader;
function GetOptionsReader_FromRegistry(const AKey: WideString): IOptionsReader;
function GetOptionsWriter(const ServerName: WideString): IOptionsWriter;
function GetOptionsWriter_ForIniFile(const AFullPath: WideString): IOptionsWriter;
function OptionsExist(const ServerName: WideString; const OldSettingsPath: WideString): LongBool;
procedure RegisterMessageListenerIntf(ListenerId: Integer; MessageCode: Integer; const CallbackRecv: IOptionsMessageCallbackRecv);
procedure UnregisterMessageListener(ListenerId: Integer; MessageCode: Integer);

## IOptionsMessageCallbackRecv
继承：IOptionsMessageCallbackRecv → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 1 个方法、0 个属性

procedure Notify(SenderId: Integer; MessageCode: Integer; const Parameters: WideString);

## IOptionsPage
继承：IOptionsPage → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 9 个方法、1 个属性

property Modified: Boolean read GetModified write SetModified;
function GetModified: Boolean;
function GetNotificationCode: Integer;
procedure GetStateControls;
function OptionsFormDataManager: IOptionsFormDataManager;
procedure PostEditControls;
procedure SetDefaultState;
procedure SetModified(Value: Boolean);
procedure SetStateControls;
function TryApplyFormOptions: Boolean;

## IOptionsPage2
继承：IOptionsPage2 → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 2 个方法、1 个属性

property StatusChecker: IOptionsStatusChecker read GetStatusChecker write SetStatusChecker;
function GetStatusChecker: IOptionsStatusChecker;
procedure SetStatusChecker(const AValue: IOptionsStatusChecker);

## IOptionsPageFactory
继承：IOptionsPageFactory → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 1 个方法、0 个属性

function CreateOptionsPage(const AServerName: WideString; const AOptionsPageName: WideString; const AOptionsPageActions: IOptionPageActions): IOptionsPage;

## IOptionsReader
继承：IOptionsReader → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 9 个方法、0 个属性

function GetSections(const Path: WideString): IStrings;
function ReadAllValues(const SectionName: WideString): IStrings;
function ReadBoolean(const SectionName: WideString; const ValueName: WideString; DefaultValue: LongBool): LongBool;
function ReadDouble(const SectionName: WideString; const ValueName: WideString; DefaultValue: Double): Double;
function ReadInteger(const SectionName: WideString; const ValueName: WideString; DefaultValue: Integer): Integer;
function ReadSection(const SectionName: WideString): WideString;
function ReadString(const SectionName: WideString; const ValueName: WideString; const DefaultValue: WideString): WideString;
function SectionExists(const SectionName: WideString): LongBool;
function ValueExists(const SectionName: WideString; const ValueName: WideString): LongBool;

## IOptionsStatusChecker
继承：IOptionsStatusChecker → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 1 个方法、1 个属性

property Modified: Boolean read GetModified;  // read-only
function GetModified: Boolean;

## IOptionsStorage
继承：IOptionsStorage → IInterface ｜ 单元：RT_CommonInterfaces ｜ 自有 0 个方法、0 个属性


## IOptionsWriter
继承：IOptionsWriter → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 5 个方法、0 个属性

procedure EraseSection(const SectionName: WideString);
procedure WriteBoolean(const SectionName: WideString; const ValueName: WideString; Value: LongBool);
procedure WriteDouble(const SectionName: WideString; const ValueName: WideString; Value: Double);
procedure WriteInteger(const SectionName: WideString; const ValueName: WideString; Value: Integer);
procedure WriteString(const SectionName: WideString; const ValueName: WideString; const Value: WideString);

## IOutputJob
继承：IOutputJob → IDMObject → IInterface ｜ 单元：RT_Workspace ｜ 自有 3 个方法、0 个属性

function DM_JobName: WideString;
function DM_Outputer(Index: Integer): IOutputer;
function DM_OutputerCount: Integer;

## IOutputManager
继承：IOutputManager → IInterface ｜ 单元：RT_Workspace ｜ 自有 1 个方法、0 个属性

function DM_GetPredefinedOutputForCategory(Category: TOutputCategory; Index: Integer): IPredefinedOutput;

## IOutputMedium
继承：IOutputMedium → IDMObject → IInterface ｜ 单元：RT_Workspace ｜ 自有 11 个方法、3 个属性

property Name: WideString read GetState_Name;  // read-only
property OutputPath: WideString read GetState_OutputPath write SetState_OutputPath;
property TypeString: WideString read GetState_TypeString;  // read-only
procedure BeginRunCategories;
function CanBeReleaseManaged: Boolean;
procedure EndRunCategories;
function FindConfiguration: IOutputer;
function GetOutputPathByOutputer(AOutputer: IOutputer): WideString;
function GetState_Name: WideString;
function GetState_OutputPath: WideString;
function GetState_TypeString: WideString;
procedure PredictOutputFileNames(AConfigurations: IInterfaceList; AOutJobFileName: WideString; AFiles: IStrings);
function ReleaseManaged: Boolean;
procedure SetState_OutputPath(AOutputpath: WideString);

## IOutputRunner
继承：IOutputRunner → IInterface ｜ 单元：RT_Workspace ｜ 自有 4 个方法、0 个属性

procedure AddOutputConfiguration(AOutputConfiguration: IOutputer);
procedure GetLastOutputFileNames(Strings: IStrings);
function GetLastRunResult: TOutputResult;
function Run: TOutputResult;

## IOutputView
继承：IOutputView → IInterface ｜ 单元：RT_Workspace ｜ 自有 9 个方法、1 个属性

property Lines[AIndex: Integer]: WideString read GetLine write SetLine;
procedure Clear;
function Count: Integer;
function GetLine(AIndex: Integer): WideString;
function GetText: WideString;
function HandleAllocated: ByteBool;
procedure HighlightCharLine(CharNum: Integer);
procedure ScrollToChar(CharNum: Integer);
procedure SetLine(AIndex: Integer; const AValue: WideString);
procedure UpdateWindow;

## IOutputer
继承：IOutputer → IDMObject → IInterface ｜ 单元：RT_Workspace ｜ 自有 25 个方法、1 个属性

property VariantName: WideString read DM_GetState_VariantName write DM_SetState_VariantName;
procedure DM_AddParameter(AName: WideString; AValue: WideString);
procedure DM_ClearConfigurationLevelVariant;
procedure DM_ClearParameters;
procedure DM_DeleteParameter(Index: Integer);
function DM_EditProperties: Boolean;
function DM_Generate_OutputFiles(AGeneratedFilename: PWideChar): Boolean;
function DM_Generate_OutputFilesTo(OutputDirectory: WideString; ParameterOverrides: PWideChar): Boolean;
function DM_Generate_Report(var AGeneratedFilename: WideString; var ATemplateFilename: WideString): Boolean;
function DM_GeneratorName: WideString;
function DM_GetDescription: WideString;
function DM_GetDocumentKind: WideString;
function DM_GetDocumentPath: WideString;
function DM_GetOutputCategory: TOutputCategory;
function DM_GetState_VariantName: WideString;
function DM_GetViewName: WideString;
function DM_PredefinedOutput: IPredefinedOutput;
procedure DM_SetConfigurationLevelVariant(AVariant: WideString);
procedure DM_SetDocumentPath(ADocPath: WideString);
procedure DM_SetPrintMode(AFitPrintToPage: Boolean);
procedure DM_SetPrintScale(APrintScale: Double);
procedure DM_SetState_VariantName(const AValue: WideString);
procedure DM_SetViewName(const AValue: WideString);
function DM_SharedConfiguration: WideString;
function DM_SupportsVariants: Boolean;
function DM_ViewName: WideString;

## IPCBConfiguration
继承：IPCBConfiguration → IBaseConfiguration → IDMObject → IInterface ｜ 单元：RT_Workspace ｜ 自有 8 个方法、0 个属性

function DM_CurrentRevision: IULB_ItemRevision;
function DM_DefaultContentTypeGUID: WideString;
function DM_GetConfigurationType: WideString;
function DM_GetLocalReleaseTarget: WideString;
function DM_ReleaseItem: IULB_Item;
procedure DM_SetConfigurationType(AValue: WideString);
procedure DM_SetLocalReleaseTarget(AValue: WideString);
function DM_SupportedContentTypes: WideString;

## IPCBProjectLink
继承：IPCBProjectLink → IInterface ｜ 单元：Rt_NexusWorkspace ｜ 自有 7 个方法、0 个属性

function ContainsProjectLink(AProjectLink: IProjectLink): Boolean;
procedure CrossProbe;
function DocumentKind: WideString;
function GetProject: IProject;
function GetProjectFullPath: WideString;
function GetSchComponentLink(Index: Integer): ISchComponentLink;
function GetSchComponentLinkCount: Integer;

## IParamObject
继承：IParamObject → IInterface ｜ 单元：Data.DB ｜ 自有 1 个方法、0 个属性

function GetDataType: TFieldType;

## IParamStreamObject
继承：IParamStreamObject → IParamObject → IInterface ｜ 单元：Data.DB ｜ 自有 2 个方法、0 个属性

function GetBytes: TArray<System.Byte>;
procedure SetKnownSize(KnownSize: Integer);

## IParameter
继承：IParameter → IDMObject → IInterface ｜ 单元：RT_Workspace ｜ 自有 25 个方法、0 个属性

function DM_AreVariedValuesEqual(const Other: IParameter): Boolean;
function DM_CalculatingFormula: Boolean;
function DM_ConfigurationName: WideString;
function DM_Description: WideString;
function DM_FullName: WideString;
function DM_GetAllowDatabaseSynchronize: Boolean;
function DM_GetAllowLibrarySynchronize: Boolean;
function DM_IsSystemParameter: Boolean;
function DM_IsVirtual: Boolean;
function DM_Kind: TParameterKind;
function DM_Name: WideString;
function DM_NewName: WideString;
function DM_NewValue: WideString;
function DM_OriginalOwner: IDMObject;
function DM_RawText: WideString;
procedure DM_SetCalculatingFormula(AValue: Boolean);
procedure DM_SetName(const AName: WideString);
procedure DM_SetNewName(const AValue: WideString);
procedure DM_SetNewValue(const AValue: WideString);
procedure DM_SetValue(const Value: WideString);
function DM_UniqueId: WideString;
function DM_Value: WideString;
function DM_VariedValueItemCount: Integer;
function DM_VariedValueItems(Index: Integer): IVariedValueItem;
function DM_Visible: Boolean;

## IParameterChange
继承：IParameterChange → IInterface ｜ 单元：RT_Workspace ｜ 自有 30 个方法、10 个属性

property Enabled: Boolean read GetEnabled write SetEnabled;
property IsSystem: Boolean read GetIsSystem write SetIsSystem;
property NewExists: Boolean read GetNewExists write SetNewExists;
property NewName: WideString read GetNewName write SetNewName;
property NewValue: WideString read GetNewValue write SetNewValue;
property OrigExists: Boolean read GetOrigExists write SetOrigExists;
property OrigName: WideString read GetOrigName write SetOrigName;
property OrigValue: WideString read GetOrigValue write SetOrigValue;
property Parameter: IParameter read GetParameter;  // read-only
property VisibleOnAdd: Boolean read GetVisibleOnAdd write SetVisibleOnAdd;
function Exists: Boolean;
function GetEnabled: Boolean;
function GetIsSystem: Boolean;
function GetNewExists: Boolean;
function GetNewName: WideString;
function GetNewValue: WideString;
function GetOrigExists: Boolean;
function GetOrigName: WideString;
function GetOrigValue: WideString;
function GetParameter: IParameter;
function GetVisibleOnAdd: Boolean;
function IsAdd: Boolean;
function IsDisabledAdd: Boolean;
function IsDisabledRemove: Boolean;
function IsDisabledValueChange: Boolean;
function IsNull: Boolean;
function IsRemove: Boolean;
function IsRename: Boolean;
function IsValueChange: Boolean;
procedure Revert;
procedure SetEnabled(AValue: Boolean);
procedure SetIsSystem(AValue: Boolean);
procedure SetNewExists(AValue: Boolean);
procedure SetNewName(const AValue: WideString);
procedure SetNewValue(const AValue: WideString);
procedure SetOrigExists(AValue: Boolean);
procedure SetOrigName(const AValue: WideString);
procedure SetOrigValue(const AValue: WideString);
procedure SetVisibleOnAdd(AValue: Boolean);
function Value: WideString;

## IParameterChanges
继承：IParameterChanges → IInterface ｜ 单元：RT_Workspace ｜ 自有 6 个方法、0 个属性

procedure AddChange(const OrigName: WideString; const NewName: WideString; const NewValue: WideString; NewExists: Boolean; Enabled: Boolean; VisibleOnAdd: Boolean);
function ChangeForOrigName(const OrigName: WideString): IParameterChange;
function ChangesCount: Integer;
procedure Clear;
function GetChange(AIndex: Integer): IParameterChange;
function NonNullChangesCount: Integer;

## IParameterVariation
继承：IParameterVariation → IDMObject → IInterface ｜ 单元：RT_Workspace ｜ 自有 5 个方法、0 个属性

function DM_CalculatedValue(const Component: IComponent; const ComponentVariation: IComponentVariation): WideString;
function DM_ParameterName: WideString;
procedure DM_SetParameterName(const Value: WideString);
procedure DM_SetVariedValue(const Value: WideString);
function DM_VariedValue: WideString;

## IParametricView
继承：IParametricView → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 1 个方法、0 个属性

procedure InitFromParameters(const Parameters: WideString);

## IParametricViewRaw
继承：IParametricViewRaw → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 1 个方法、0 个属性

procedure InitFromParameters(const Parameters: WideString);

## IPart
继承：IPart → IDMObject → IInterface ｜ 单元：RT_Workspace ｜ 自有 63 个方法、0 个属性

procedure DM_AddConfigurationParameters;
function DM_AllPinCount: Integer;
function DM_AssignedDesignator: WideString;
function DM_CalculatedDesignator: WideString;
function DM_CenterLocationX: Integer;
function DM_CenterLocationY: Integer;
function DM_ChannelOffset: Integer;
function DM_ChildProjectSheet: IDocument;
function DM_ChildVHDLEntity: WideString;
function DM_Comment: WideString;
function DM_ComponentKind: TComponentKind;
function DM_ConfigurationParameters: WideString;
function DM_ConfiguratorName: WideString;
function DM_CurrentImplementation(AType: WideString): IComponentImplementation;
function DM_DatabaseTableName: WideString;
function DM_Description: WideString;
function DM_DesignatorLocationX: Integer;
function DM_DesignatorLocationY: Integer;
function DM_DesignatorLocked: Boolean;
function DM_DisplayMode: Byte;
function DM_ExternalPartHandle: WideString;
function DM_FirstPinLocationX: Integer;
function DM_FirstPinLocationY: Integer;
function DM_Footprint: WideString;
function DM_FullLogicalDesignator: WideString;
function DM_FullLogicalDesignatorForDisplay: WideString;
function DM_FullPhysicalDesignator: WideString;
function DM_FullPhysicalDesignatorForDisplay: WideString;
function DM_Height: Integer;
function DM_ImplementationCount: Integer;
function DM_Implementations(Index: Integer): IComponentImplementation;
function DM_InstanceCount: Integer;
function DM_Layer: WideString;
function DM_LibraryReference: WideString;
function DM_LogicalDesignator: WideString;
function DM_LogicalOwnerDocument: IDocument;
function DM_MaxPartCount: Integer;
function DM_NewDesignator: WideString;
function DM_NewPartId: Integer;
function DM_OldPartId: Integer;
function DM_PartID: Integer;
function DM_PartIdLocked: Boolean;
function DM_PartType: WideString;
function DM_PhysicalDesignator: WideString;
function DM_PinCount: Integer;
function DM_Pins(Index: Integer): INetItem;
function DM_ReferenceLocationX: Integer;
function DM_ReferenceLocationY: Integer;
function DM_Replicate(const ADocument: IDMObject): IPart;
function DM_Rotation: Double;
procedure DM_SetExternalPartHandle(APCBComponentHandle: WideString);
procedure DM_SetFootprintItemGUID(const AValue: WideString);
procedure DM_SetFootprintRevisionGUID(const AValue: WideString);
procedure DM_SetNewPartId(Value: Integer);
procedure DM_SetOldPartId(Value: Integer);
function DM_SourceDesignator: WideString;
function DM_SourceHierarchicalPath: WideString;
function DM_SourceLibraryName: WideString;
function DM_SourceUniqueId: WideString;
function DM_SubProject: WideString;
function DM_UniqueId: WideString;
function DM_UniqueIdName: WideString;
function DM_UniqueIdPath: WideString;

## IPartProperties
继承：IPartProperties → IDMObject → IInterface ｜ 单元：RT_Workspace ｜ 自有 18 个方法、0 个属性

function DM_DesignItemID: WideString;
function DM_FootprintItemGUID: WideString;
function DM_FootprintRevisionGUID: WideString;
function DM_IsGenericComponent: Boolean;
function DM_ItemGUID: WideString;
function DM_LibIdentifierKind: TLibIdentifierKind;
function DM_LibraryIdentifier: WideString;
function DM_NewHasDesignatorRecord: Boolean;
function DM_NewPhysicalDesignator: WideString;
function DM_RevisionGUID: WideString;
procedure DM_SetNewDesignatorLocked(AValue: Boolean);
procedure DM_SetNewHasDesignatorRecord(AValue: Boolean);
procedure DM_SetNewPhysicalDesignator(AValue: WideString);
function DM_SymbolReference: WideString;
function DM_UseDBTableName: Boolean;
function DM_UseLibraryName: Boolean;
function DM_VariationUniqueID: WideString;
function DM_VaultGUID: WideString;

## IPartSearch
继承：IPartSearch → IInterface ｜ 单元：RT_SupplierManager ｜ 自有 1 个方法、0 个属性

function GetSelectedSupplierLinks: ISupplierSourceRelationshipList;

## IPercentState
继承：IPercentState → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 6 个方法、4 个属性

property CurrentPercentCount: Integer read GetCurrentPercentCount write SetCurrentPercentCount;
property Marquee: Boolean read GetMarquee;  // read-only
property OldPercent: Integer read GetOldPercent write SetOldPercent;
property TotalPercentCount: Integer read GetTotalPercentCount;  // read-only
function GetCurrentPercentCount: Integer;
function GetMarquee: Boolean;
function GetOldPercent: Integer;
function GetTotalPercentCount: Integer;
procedure SetCurrentPercentCount(Value: Integer);
procedure SetOldPercent(Value: Integer);

## IPinMapping
继承：IPinMapping → IBSDLObject → IInterface ｜ 单元：Rt_NexusDevices ｜ 自有 3 个方法、0 个属性

function GetPinName: WideString;
function GetPinNumber: WideString;
function GetScanPin: IScanPin;

## IPluginsPlatformVersions
继承：IPluginsPlatformVersions → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 5 个方法、3 个属性

property Count: Integer read GetCount;  // read-only
property Platforms[Index: Integer]: WideString read GetPlatform;  // read-only
property Versions[const PlatformName: WideString]: WideString read GetVersion write SetVersion;
procedure Clear;
function GetCount: Integer;
function GetPlatform(Index: Integer): WideString;
function GetVersion(const PlatformName: WideString): WideString;
procedure SetVersion(const PlatformName: WideString; const Value: WideString);

## IPluginsRegistry
继承：IPluginsRegistry → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 10 个方法、2 个属性

property Count: Integer read GetCount;  // read-only
property Items[AIndex: Integer]: IPluginsRegistryItem read GetItem;  // read-only
procedure AddItem(const APluginRegistryItem: IPluginsRegistryItem);
function CreatePluginsRegistryItem: IPluginsRegistryItem;
function FindItemByGuid(const AGuid: WideString): IPluginsRegistryItem;
function FindItemByHRID(const HRID: WideString): IPluginsRegistryItem;
function GetCount: Integer;
function GetItem(AIndex: Integer): IPluginsRegistryItem;
procedure RemoveItem(const APluginRegistryItem: IPluginsRegistryItem);
procedure Save;
procedure Unlock;
procedure UpdateItem(const APluginRegistryItem: IPluginsRegistryItem);

## IPluginsRegistryItem
继承：IPluginsRegistryItem → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 47 个方法、23 个属性

property CategoryGuid: WideString read GetCategoryGuid write SetCategoryGuid;
property CategoryName: WideString read GetCategoryName write SetCategoryName;
property CreatedBy: WideString read GetCreatedBy write SetCreatedBy;
property DateInstalled: TDateTime read GetDateInstalled write SetDateInstalled;
property GUID: WideString read GetGUID write SetGuid;
property Help: WideString read GetHelp write SetHelp;
property HRID: WideString read GetHRid write SetHRid;
property IsSystem: Boolean read GetIsSystem write SetIsSystem;
property LargeImage: WideString read GetLargeImage write SetLargeImage;
property LongDescription: WideString read GetLongDescription write SetLongDescription;
property Path: WideString read GetPath write SetPath;
property PlatformVersions: IPluginsPlatformVersions read GetPlatformVersions;  // read-only
property ReadMe: WideString read GetReadMe write SetReadMe;
property ReleasedDate: TDateTime read GetReleasedDate write SetReleasedDate;
property ReleaseNotes: WideString read GetReleaseNotes write SetReleaseNotes;
property Requirements: WideString read GetRequirements write SetRequirements;
property ShortDescription: WideString read GetShortDescription write SetShortDescription;
property SmallImage: WideString read GetSmallImage write SetSmallImage;
property Status: TPluginsStatus read GetStatus write SetStatus;
property Title: WideString read GetTitle write SetTitle;
property VaultGuid: WideString read GetVaultGuid write SetVaultGuid;
property Version: WideString read GetVersion write SetVersion;
property VersionGuid: WideString read GetVersionGuid write SetVersionGuid;
function GetCategoryGuid: WideString;
function GetCategoryName: WideString;
function GetCreatedBy: WideString;
function GetDateInstalled: TDateTime;
function GetGUID: WideString;
function GetHelp: WideString;
function GetHRid: WideString;
function GetIsSystem: Boolean;
function GetLargeImage: WideString;
function GetLongDescription: WideString;
function GetPath: WideString;
function GetPlatformVersions: IPluginsPlatformVersions;
function GetReadMe: WideString;
function GetReleasedDate: TDateTime;
function GetReleaseNotes: WideString;
function GetRequirements: WideString;
function GetShortDescription: WideString;
function GetSmallImage: WideString;
function GetStatus: TPluginsStatus;
function GetTitle: WideString;
function GetVaultGuid: WideString;
function GetVersion: WideString;
function GetVersionGuid: WideString;
procedure SetCategoryGuid(const Value: WideString);
procedure SetCategoryName(const Value: WideString);
procedure SetCreatedBy(const Value: WideString);
procedure SetDateInstalled(Value: TDateTime);
procedure SetGuid(const Value: WideString);
procedure SetHelp(const Value: WideString);
procedure SetHRid(const Value: WideString);
procedure SetIsSystem(Value: Boolean);
procedure SetLargeImage(const Value: WideString);
procedure SetLongDescription(const Value: WideString);
procedure SetPath(const Value: WideString);
procedure SetReadMe(const Value: WideString);
procedure SetReleasedDate(Value: TDateTime);
procedure SetReleaseNotes(const Value: WideString);
procedure SetRequirements(const Value: WideString);
procedure SetShortDescription(const Value: WideString);
procedure SetSmallImage(const Value: WideString);
procedure SetStatus(Value: TPluginsStatus);
procedure SetTitle(const Value: WideString);
procedure SetVaultGuid(const Value: WideString);
procedure SetVersion(const Value: WideString);
procedure SetVersionGuid(const Value: WideString);
procedure StartAutoRun(AutoRunAction: TPluginAutoRunAction);
procedure Validate;

## IPositionLinkObserver
继承：IPositionLinkObserver → IPositionLinkObserver170 → IInterface ｜ 单元：System.Classes ｜ 自有 1 个方法、0 个属性

procedure PosChanging;

## IPositionLinkObserver170
继承：IPositionLinkObserver170 → IInterface ｜ 单元：System.Classes ｜ 自有 1 个方法、0 个属性

procedure PosChanged;

## IPredefinedOutput
继承：IPredefinedOutput → IInterface ｜ 单元：RT_Workspace ｜ 自有 6 个方法、0 个属性

function DM_GroupOrder: WideString;
function DM_SetCaption: WideString;
function DM_SetCategory: TOutputCategory;
function DM_SetName: WideString;
function DM_SortOrder: WideString;
function DM_VisibleOrder: WideString;

## IPreferencesView
继承：IPreferencesView → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 1 个方法、0 个属性

procedure Apply;

## IPreviewImage
继承：IPreviewImage → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 8 个方法、0 个属性

procedure BuildAllImagesFromFullsizePicture;
procedure BuildLargeImageFromFullsizePicture;
procedure BuildMediumImageFromFullsizePicture;
procedure BuildSmallImageFromFullsizePicture;
function CreateFullsizePictureBitmap: HBITMAP;
procedure DrawLargeImageProportional(ADC: HDC; const ARect: IDispatch);
procedure FinalizeFullsizeDrawing;
function InitializeFullsizeDrawing(AMetaMMWidth: Integer; AMetaMMHeight: Integer): HDC;

## IPreviewableDocument
继承：IPreviewableDocument → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 2 个方法、1 个属性

property FileName: WideString read GetFileName;  // read-only
function GenerateDocumentPreview(const APreviewImage: IPreviewImage): Boolean;
function GetFileName: WideString;

## IPrimitiveDefaultItemSupportMeasureUnits
继承：IPrimitiveDefaultItemSupportMeasureUnits → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 1 个方法、0 个属性

function GetMeasureUnit: Integer;

## IPrimitiveDefaultsItem
继承：IPrimitiveDefaultsItem → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 4 个方法、0 个属性

function GetCaption: WideString;
function GetGroupName: WideString;
function GetImageSource: WideString;
function GetPrimitive: IInterface;

## IProcessControl
继承：IProcessControl → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 4 个方法、1 个属性

property ProcessDepth: Integer read GetProcessDepth write SetProcessDepth;
function GetProcessDepth: Integer;
procedure PostProcess(const AContext: IInterface; AParameters: PWideChar);
procedure PreProcess(const AContext: IInterface; AParameters: PWideChar);
procedure SetProcessDepth(Value: Integer);

## IProcessFlow
继承：IProcessFlow → IInterface ｜ 单元：Rt_NexusDevices ｜ 自有 35 个方法、0 个属性

procedure AddChildStage(AStage: IProcessFlow);
procedure AddDependency(AStage: IProcessFlow);
function CanEditProperties: LongBool;
function CanRun: LongBool;
procedure ClearChildren;
procedure ClearDependencies;
procedure ClearLastRunResult;
procedure EditProperties;
function FlowState: TProcessFlowState;
function GetBasePath: WideString;
function GetChildStage(AIndex: Integer): IProcessFlow;
function GetChildStageCount: Integer;
function GetDependenciesCount: Integer;
function GetDependency(AIndex: Integer): IProcessFlow;
function GetParentStage: IProcessFlow;
function InputDescription: WideString;
function IsCategory: LongBool;
function IsRunning: LongBool;
function LastRunResult: TFlowRunResult;
function OutputDescription: WideString;
procedure ProjectChanged(AProjectPath: WideString);
function ReportCount: Integer;
function ReportPath(AIndex: Integer): WideString;
function Run(ARunner: IProcessFlowRunner): TFlowRunResult;
function RunAll(ARunner: IProcessFlowRunner): TFlowRunResult;
function RunIfOutOfDate(ARunner: IProcessFlowRunner): TFlowRunResult;
function RunningStage: IProcessFlow;
function RunWholeStage(ARunner: IProcessFlowRunner): TFlowRunResult;
procedure SetBasePath(aPath: WideString);
procedure SetParentStage(AStage: IProcessFlow);
function StageCaption: WideString;
function StageDescription: WideString;
function StageName: WideString;
procedure Stop;
function UpdateFlowState: LongBool;

## IProcessFlowRunner
继承：IProcessFlowRunner → IInterface ｜ 单元：Rt_NexusDevices ｜ 自有 8 个方法、1 个属性

property CurrentHardDevice: IInterface read GetCurrentHardDevice write SetCurrentHardDevice;
procedure AddError(AType: WideString; AFullErrorText: WideString);
procedure AddSummaryLine(ASection: WideString; AKey: WideString; AValue: WideString; AReportPath: WideString);
function FlowRunning: LongBool;
procedure FlowStageStarting(AStage: IProcessFlow);
function GetCurrentHardDevice: IInterface;
procedure RunEnded;
procedure RunStarted;
procedure SetCurrentHardDevice(const AHardDevice: IInterface);

## IProcessLauncher
继承：IProcessLauncher → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 3 个方法、0 个属性

procedure GetCommandState(AProcess: PWideChar; AParameters: PWideChar; const AContext: IServerDocumentView; var Enabled: LongBool; var Checked: LongBool; var Visible: LongBool; Caption: PWideChar; ImageFile: PWideChar);
procedure PostMessage(AProcess: PWideChar; AParameters: PWideChar; MaxParameterSize: Integer; const AContext: IServerDocumentView);
procedure SendMessage(AProcess: PWideChar; AParameters: PWideChar; MaxParameterSize: Integer; const AContext: IServerDocumentView);

## IProcessLauncher2
继承：IProcessLauncher2 → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 1 个方法、0 个属性

procedure SetCommandGetStateCallback(const AProcess: WideString; const AGetStateCallback: ICommandGetState);

## IProcessLauncherInfo
继承：IProcessLauncherInfo → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 10 个方法、10 个属性

property Caption: WideString read GetCaption;  // read-only
property Description: WideString read GetDescription;  // read-only
property ImageFile: WideString read GetImageFile;  // read-only
property Key: Integer read GetKey;  // read-only
property Key2: Integer read GetKey2;  // read-only
property Parameters: WideString read GetParameters;  // read-only
property ServerCommand: WideString read GetServerCommand;  // read-only
property Shift: TShiftState read GetShift;  // read-only
property Shift2: TShiftState read GetShift2;  // read-only
property ShortcutText: WideString read GetShortcutText;  // read-only
function GetCaption: WideString;
function GetDescription: WideString;
function GetImageFile: WideString;
function GetKey: Integer;
function GetKey2: Integer;
function GetParameters: WideString;
function GetServerCommand: WideString;
function GetShift: TShiftState;
function GetShift2: TShiftState;
function GetShortcutText: WideString;

## IProcessorRegister
继承：IProcessorRegister → IInterface ｜ 单元：Rt_NexusDevices ｜ 自有 15 个方法、0 个属性

procedure Export_ToCore;
function GetByte0: Byte;
function GetByte1: Byte;
function GetByte2: Byte;
function GetByte3: Byte;
function GetIndex: Integer;
function GetName: WideString;
function GetNexusDevice: INexusDevice;
function GetShortName: WideString;
function GetValue: Cardinal;
function GetWideValue: WideString;
function GetWidth: Integer;
procedure Import_FromCore;
procedure SetValue(NewValue: Cardinal);
procedure SetWideValue(const NewValue: WideString);

## IProductInfo
继承：IProductInfo → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 8 个方法、0 个属性

function CustomSplash: IDXPSplash;
function GetLicenseExpirationInfo(const ALicenseExpirationList: IInterfaceList; out AMinDaysLeft: Integer; out AInfo: WideString): LongBool;
function GetPCBDocumentKind: WideString;
function GetValue(const ASectionName: WideString; const AValueName: WideString): WideString;
function ImplementingServerName: WideString;
function MainImageListHandle: NativeUInt;
function SupportsOptionsPage(const APageName: WideString; ADefault: Boolean): LongBool;
function TryGetValue(const ASectionName: WideString; const AValueName: WideString; out AValue: WideString): LongBool;

## IProject
继承：IProject → IDMObject → IInterface ｜ 单元：RT_Workspace ｜ 自有 214 个方法、0 个属性

function DM_AddAsDeviceSheet(const ADocumentPath: WideString): IDocument;
function DM_AddConfiguration(Configuration: WideString): IConfiguration;
procedure DM_AddConfigurationParameters(Configuration: WideString);
procedure DM_AddConfigurationParameters_Physical(Configuration: WideString);
procedure DM_AddControlPanel(Filename: WideString);
procedure DM_AddDeviceSheetFolder(FolderPath: WideString; IncludeSubFolders: Boolean);
procedure DM_AddGeneratedDocument(Filename: WideString);
procedure DM_AddMissingAutoCrossRefs;
procedure DM_AddOrSetUniqueIdMapping(const ASchHandle: WideString; const AUniqueIdMapping: WideString);
procedure DM_AddParameter(AName: WideString; AValue: WideString);
function DM_AddProjectVariant: IProjectVariant;
procedure DM_AddSearchPath(SearchPath: WideString; IncludeSubFolders: Boolean);
procedure DM_AddSourceDocument(Filename: WideString);
procedure DM_AddSubManagedProject(ProjectGUID: WideString; RevisionGUID: WideString; LocalPath: WideString);
procedure DM_AddVirtualDocument(const APath: WideString);
function DM_AvailableDatabaseLinks: Boolean;
procedure DM_BeginUpdate;
function DM_ChannelDesignatorFormat: WideString;
function DM_ChannelRoomLevelSeperator: WideString;
function DM_ChannelRoomNamingStyle: TChannelRoomNamingStyle;
procedure DM_ClearAllNetColors;
procedure DM_ClearSchematicObjectsErrorFields(const SchematicId: WideString);
procedure DM_ClearViolations;
function DM_Compile: LongBool;
function DM_CompileEx(All: LongBool; var Cancelled: LongBool): LongBool;
function DM_CompileProjectOrDocument(ADocument: IDocument): Boolean;
function DM_ComponentMappings(AnImplementationDocument: WideString): IComponentMappings;
function DM_ConfigurationCount: Integer;
function DM_Configurations(Index: Integer): IConfiguration;
function DM_CrossRefCrossSheets: Boolean;
function DM_CrossRefLocationStyle: TCrossRefLocationStyle;
function DM_CrossRefPorts: TCrossRefPorts;
function DM_CrossRefSheetEntries: Boolean;
function DM_CrossRefSheetStyle: TCrossRefSheetStyle;
function DM_CurrentProjectVariant: IProjectVariant;
function DM_DataModel: IUnifiedDataModel;
function DM_DeviceSheetFolderCount: Integer;
function DM_DeviceSheetFolders(Index: Integer): IDeviceSheetFolder;
procedure DM_DeviceSheetRemoved(const Filename: WideString);
function DM_DiffPairSuffixCount: Integer;
procedure DM_DiffPairSuffixes(Index: Integer; var Positive: WideString; var Negative: WideString);
procedure DM_DisableOnlineSynchronization(AUpdateParameters: Boolean);
procedure DM_DoCrossSelection;
function DM_DocumentBackups: IDocumentBackups;
function DM_DocumentClassGenerationOptions(const ADocumentPath: WideString): IDocumentClassGenerationOptions;
function DM_DocumentFlattened: IDocument;
function DM_DocumentIsGenerated(const ADocumentFileName: WideString): Boolean;
function DM_EditConfigurations: LongBool;
function DM_EditOptions(DefaultPage: WideString): LongBool;
procedure DM_EndUpdate;
procedure DM_EnsureAllCachedManagedOutputJobs;
procedure DM_EnsureStandardConfigurations;
function DM_ErrorLevels(AErrorKind: TErrorKind): TErrorLevel;
procedure DM_Export_ToFile(const AFileName: WideString);
function DM_FindProjectVariant(ADescription: WideString): IProjectVariant;
procedure DM_FixDesignatorAnnotationAfterUniqueIdChange(const AOldUniqueId: WideString; const ANewUniqueId: WideString; const ALogicalDesignator: WideString; ARemoveOriginal: Boolean);
procedure DM_FixSheetNumberAnnotationAfterUniqueIdChange(const AOldUniqueId: WideString; const ANewUniqueId: WideString; const ADocumentFileName: WideString; ARemoveOriginal: Boolean);
procedure DM_FixVariationAfterUniqueIdChange(const AOldUniqueId: WideString; const ANewUniqueId: WideString; const APhysicalDesignator: WideString; const AProjectVariantUniqueId: WideString; const AProjectVariantDescription: WideString; ARemoveOriginal: Boolean);
procedure DM_ForceIncludeRequiredOutJobs(const AConfigurationManager: IDMS_ConfigurationManager; const AVaultGUID: WideString);
function DM_FSMCodingStyle: TFSMCodingStyle_DropDownList;
function DM_FSMEncodingStyle: TFSMEncodingStyle_DropDownList;
function DM_GeneratedDocumentCount: Integer;
function DM_GeneratedDocuments(Index: Integer): IDocument;
function DM_GetAllowPortNetNames: Boolean;
function DM_GetAllowSheetEntryNetNames: Boolean;
function DM_GetAnnotationManager: IAnnotationManager;
function DM_GetAppendSheetNumberToLocalNets: Boolean;
function DM_GetAutomaticSheetsNumbers: IAutomaticSheetsNumbers;
function DM_GetConfigurationByName(Configuration: WideString): IConfiguration;
function DM_GetDefaultConfiguration: IConfiguration;
function DM_GetDefaultConfigurationName: WideString;
function DM_GetDefaultPcbType: WideString;
function DM_GetDocumentByDocumentId(const ADocumentId: WideString): IDocument;
function DM_GetDocumentFromName(DocumentName: WideString): IDocument;
function DM_GetDocumentFromPath(DocumentPath: WideString): IDocument;
function DM_GetECOInterface: IECO;
function DM_GetHasWriteAccessAsync: Boolean;
function DM_GetIncludeDesignInRelease: Boolean;
function DM_GetIsActiveOnlineSynchronization: Boolean;
function DM_GetLinkedManagedProjectGUID: WideString;
function DM_GetNetColorByName(const ANetName: WideString): TColor;
function DM_GetNetInfosToExportCount: Integer;
function DM_GetNetInfoToExport(AIndex: Integer): WideString;
function DM_GetNotificationService: IEDMS_NotificationService;
function DM_GetOriginalDocumentFromPath(const ADocumentPath: WideString): IDocument;
function DM_GetOutputPath: WideString;
function DM_GetPinSwapBy_Netlabel: Boolean;
function DM_GetPinSwapBy_Pin: Boolean;
function DM_GetProjectClassGenerationOptions: IProjectClassGenerationOptions;
function DM_GetRelativeOutputPath: WideString;
function DM_GetReleaseFolderPath: WideString;
function DM_GetReleaseMode: TProjectReleaseMode;
function DM_GetReleaseNamings: WideString;
function DM_GetReleaseVaultGUID: WideString;
function DM_GetReleaseZipPath: WideString;
function DM_GetReportFactory: IReportFactory;
function DM_GetRequiredCapabilities(ACapabilities: ICapabilityList): Boolean;
function DM_GetScrapDocument(DocumentPath: WideString): IDocument;
function DM_GetTemplateLink: WideString;
function DM_GetTimeStampedOutputFolder: Boolean;
function DM_GetTopLevelDocumentStructure: IDocumentStructure;
function DM_GetVariantSchLibrary: WideString;
function DM_GetVirtualParametersManager: IVirtualParametersManager;
function DM_GetWebURL(const APage: WideString; const AOpenedFrom: WideString; AIncludeAuthToken: Boolean): WideString;
function DM_GlobalPreferencesRevisionGUID: WideString;
function DM_GlobalPreferencesVaultGUID: WideString;
function DM_HarnessDocumentFlattened: IDocument;
function DM_HierarchyMode: TFlattenMode;
function DM_HierarchyModeForCompile: TFlattenMode;
function DM_InCompilation: Boolean;
function DM_IndexOfSourceDocument(Filename: WideString): Integer;
function DM_InitializeOutputPath(AnOutputType: WideString): WideString;
function DM_IsActive: Boolean;
function DM_IsConnectiveSelectedNow(AConnective: IDMObject): Boolean;
function DM_IsCrossRefAddedToProject: Boolean;
function DM_IsHidden: Boolean;
function DM_IsManagedDocument(ADocument: IDocument): Boolean;
function DM_IsReuseBlock: Boolean;
function DM_IsSharedWithMe: Boolean;
function DM_IsVaultFileLessEditing: Boolean;
procedure DM_LoadAllLogicalDocuments;
procedure DM_LoadManagedParameters;
function DM_LogicalDocumentCount: Integer;
function DM_LogicalDocuments(Index: Integer): IDocument;
function DM_LogicalDocumentsIsDeviceSheet(const ADocument: IDocument): Boolean;
function DM_ManagedParameterCount: Integer;
function DM_ManagedParameters(Index: Integer): IParameter;
function DM_ManagedProjectGUID: WideString;
procedure DM_MoveSourceDocument(Filename: WideString; NewIndex: Integer);
function DM_NeedsCompile: LongBool;
function DM_OfflineProjectGUID: WideString;
function DM_OptionsStorage: IOptionsStorage;
function DM_Outputers(Name: WideString): IOutputer;
function DM_OwnedProjectCount: Integer;
function DM_OwnedProjects(Index: Integer): IProject;
function DM_PhysicalDocumentCount: Integer;
function DM_PhysicalDocuments(Index: Integer): IDocument;
function DM_PrimaryImplementationDocument: IDocument;
function DM_ProjectContainsOutputJobs: Boolean;
function DM_ProjectFileName: WideString;
function DM_ProjectFullPath: WideString;
procedure DM_ProjectStructureChanged;
function DM_ProjectTemplateLocation: WideString;
function DM_ProjectVariantCount: Integer;
function DM_ProjectVariants(Index: Integer): IProjectVariant;
procedure DM_RefreshHarnessDefinitions;
procedure DM_RefreshInWorkspaceForm;
function DM_ReleaseProjectCopy: IProject;
function DM_RemoveAllConfigurations: Boolean;
function DM_RemoveConfigurationByName(Configuration: WideString): Boolean;
procedure DM_RemoveHarnessFile(const HarnessFileFullPath: WideString);
procedure DM_RemoveParameter(const AParameter: IParameter);
procedure DM_RemoveParameterByName(const AParameterName: WideString);
procedure DM_RemoveProjectVariant(Index: Integer);
procedure DM_RemoveSourceDocument(Filename: WideString);
procedure DM_RemoveSubManagedProject(ProjectGUID: WideString; RevisionGUID: WideString; LocalPath: WideString);
procedure DM_RemoveVirtualDocument(const APath: WideString);
function DM_ReportSuppressedErrorsInMessages: Boolean;
procedure DM_ResetLastCompileTimeForAllDocuments;
procedure DM_ResetReleaseProject;
function DM_ResumeContinuousCompilation: Boolean;
function DM_SearchPathCount: Integer;
function DM_SearchPaths(Index: Integer): ISearchPath;
function DM_ServerDocument: IServerDocument;
procedure DM_SetAllowPortNetNames(AAllow: Boolean);
procedure DM_SetAllowSheetEntryNetNames(AAllow: Boolean);
procedure DM_SetAppendSheetNumberToLocalNets(AAppend: Boolean);
procedure DM_SetAsCurrentProject;
procedure DM_SetConnectedNetsColor(const ANet: INet; AColor: TColor);
procedure DM_SetCurrentProjectVariant(AProjVariant: IProjectVariant);
procedure DM_SetCurrentProjectVariantSilent(AProjectVariant: IProjectVariant);
procedure DM_SetDefaultConfigurationName(Configuration: WideString);
procedure DM_SetDefaultPcbType(PcbType: WideString);
procedure DM_SetErrorLevels(AErrorKind: TErrorKind; AErrorLevel: TErrorLevel);
procedure DM_SetGlobalPreferencesRevisionGUID(AValue: WideString);
procedure DM_SetGlobalPreferencesVaultGUID(AValue: WideString);
procedure DM_SetHierarchyMode(AFlatten: TFlattenMode);
procedure DM_SetIncludeDesignInRelease(AValue: Boolean);
procedure DM_SetLinkedManagedProjectGUID(const AValue: WideString);
procedure DM_SetManagedProjectGUID(const AValue: WideString);
procedure DM_SetModified;
procedure DM_SetNetColorByName(const ANetName: WideString; AColor: TColor);
procedure DM_SetOfflineProjectGUID(const AValue: WideString);
procedure DM_SetOutputPath(AnOutputPath: WideString);
procedure DM_SetPinSwapBy_Netlabel(AAllow: Boolean);
procedure DM_SetPinSwapBy_Pin(AAllow: Boolean);
procedure DM_SetRelativeOutputPath(AValue: WideString);
procedure DM_SetReleaseFolderPath(AValue: WideString);
procedure DM_SetReleaseMode(AValue: TProjectReleaseMode);
procedure DM_SetReleaseNamings(const AValue: WideString);
procedure DM_SetReleaseProjectCopy(AProject: IProject);
procedure DM_SetReleaseVaultGUID(Value: WideString);
procedure DM_SetReleaseZipPath(AValue: WideString);
procedure DM_SetTimeStampedOutputFolder(AValue: Boolean);
function DM_ShowVariantsDrawingStylesDialog(const AValue: IVariantOption): IVariantOption;
procedure DM_StartCrossProbing(CtrlDoesSwitch: Boolean);
procedure DM_StartNavigation;
function DM_SuspendContinuousCompilation: Boolean;
function DM_ToDoManager: IToDoManager;
function DM_TopLevelLogicalDocument: IDocument;
function DM_TopLevelPhysicalDocument: IDocument;
function DM_TryToResolveDocumentSpecialString(const AName: WideString; const ADocumentFileName: WideString; out AValue: WideString): Boolean;
function DM_TryToResolveSpecialString(const AName: WideString; out AValue: WideString): Boolean;
function DM_UpdateConstraints: LongBool;
procedure DM_UpdateSchObjectErrorFields(const SchHandle: WideString; ErrorKind: TErrorKind; Suppressed: Boolean);
function DM_UserID: WideString;
procedure DM_Validate;
function DM_ValidateManagedOutputJobs: Boolean;
function DM_VariantManager: IVariantManager;
function DM_Vault: IEDMS_Vault;
function DM_VaultGUID: WideString;
function DM_ViolationCount: Integer;
function DM_Violations(Index: Integer): IViolation;
function GetNavigationHistory: INavigationHistory;

## IProjectClassGenerationOptions
继承：IProjectClassGenerationOptions → IInterface ｜ 单元：RT_Workspace ｜ 自有 15 个方法、7 个属性

property CompClassManualEnabled: Boolean read GetCompClassManualEnabled write SetCompClassManualEnabled;
property CompClassManualRoomEnabled: Boolean read GetCompClassManualRoomEnabled write SetCompClassManualRoomEnabled;
property NetClassAutoBusEnabled: Boolean read GetNetClassAutoBusEnabled write SetNetClassAutoBusEnabled;
property NetClassAutoCompEnabled: Boolean read GetNetClassAutoCompEnabled write SetNetClassAutoCompEnabled;
property NetClassAutoNamedHarnessEnabled: Boolean read GetNetClassAutoNamedHarnessEnabled write SetNetClassAutoNamedHarnessEnabled;
property NetClassManualEnabled: Boolean read GetNetClassManualEnabled write SetNetClassManualEnabled;
property NetClassSeparateForBusSections: Boolean read GetNetClassSeparateForBusSections write SetNetClassSeparateForBusSections;
function GetCompClassManualEnabled: Boolean;
function GetCompClassManualRoomEnabled: Boolean;
function GetNetClassAutoBusEnabled: Boolean;
function GetNetClassAutoCompEnabled: Boolean;
function GetNetClassAutoNamedHarnessEnabled: Boolean;
function GetNetClassManualEnabled: Boolean;
function GetNetClassSeparateForBusSections: Boolean;
procedure ResetToDefaultState;
procedure SetCompClassManualEnabled(AValue: Boolean);
procedure SetCompClassManualRoomEnabled(AValue: Boolean);
procedure SetNetClassAutoBusEnabled(AValue: Boolean);
procedure SetNetClassAutoCompEnabled(AValue: Boolean);
procedure SetNetClassAutoNamedHarnessEnabled(AValue: Boolean);
procedure SetNetClassManualEnabled(AValue: Boolean);
procedure SetNetClassSeparateForBusSections(AValue: Boolean);

## IProjectLink
继承：IProjectLink → IInterface ｜ 单元：Rt_NexusWorkspace ｜ 自有 12 个方法、2 个属性

property NexusCores_All[Index: Integer]: INexusCore read GetNexusCore_All;  // read-only
property NexusCores_Instrument[Index: Integer]: INexusCore read GetNexusCore_Instrument;  // read-only
function ContainsEmbeddedProject(AProjectPath: WideString): Boolean;
procedure CrossProbe;
function DocumentKind: WideString;
function GetCoreFromDesignator(Designator: WideString): INexusCore;
function GetEmbeddedProject: IEmbeddedProject;
function GetFPGAProject: IFPGAProject;
function GetNexusCore_All(Index: Integer): INexusCore;
function GetNexusCore_Instrument(Index: Integer): INexusCore;
function GetNexusCoreCount_All: Integer;
function GetNexusCoreCount_Instrument: Integer;
function GetProject: IProject;
function GetProjectFullPath: WideString;

## IProjectPackagerConfig
继承：IProjectPackagerConfig → IInterface ｜ 单元：RT_Workspace ｜ 自有 18 个方法、9 个属性

property ArchiveEDIF: Boolean read GetArchiveEDIF write SetArchiveEDIF;
property ArchiveEntireProjectTree: Boolean read GetArchiveEntireProjectTree write SetArchiveEntireProjectTree;
property ArchiveFileName: WideString read GetArchiveFileName write SetArchiveFileName;
property ArchiveGenerated: Boolean read GetArchiveGenerated write SetArchiveGenerated;
property ArchiveHistory: Boolean read GetArchiveHistory write SetArchiveHistory;
property ArchiveOutputFolder: Boolean read GetArchiveOutputFolder write SetArchiveOutputFolder;
property CopyFilesInDiffDrive: Boolean read GetCopyFilesInDiffDrive write SetCopyFilesInDiffDrive;
property UnlinkFromServer: Boolean read GetUnlinkFromServer write SetUnlinkFromServer;
property UseAbsolutePaths: Boolean read GetUseAbsolutePaths write SetUseAbsolutePaths;
function GetArchiveEDIF: Boolean;
function GetArchiveEntireProjectTree: Boolean;
function GetArchiveFileName: WideString;
function GetArchiveGenerated: Boolean;
function GetArchiveHistory: Boolean;
function GetArchiveOutputFolder: Boolean;
function GetCopyFilesInDiffDrive: Boolean;
function GetUnlinkFromServer: Boolean;
function GetUseAbsolutePaths: Boolean;
procedure SetArchiveEDIF(AValue: Boolean);
procedure SetArchiveEntireProjectTree(AValue: Boolean);
procedure SetArchiveFileName(const AValue: WideString);
procedure SetArchiveGenerated(AValue: Boolean);
procedure SetArchiveHistory(AValue: Boolean);
procedure SetArchiveOutputFolder(AValue: Boolean);
procedure SetCopyFilesInDiffDrive(AValue: Boolean);
procedure SetUnlinkFromServer(AValue: Boolean);
procedure SetUseAbsolutePaths(AValue: Boolean);

## IProjectParameter
继承：IProjectParameter → IInterface ｜ 单元：RT_Workspace ｜ 自有 4 个方法、2 个属性

property Name: WideString read GetName write SetName;
property Value: WideString read GetValue write SetValue;
function GetName: WideString;
function GetValue: WideString;
procedure SetName(const AValue: WideString);
procedure SetValue(const AValue: WideString);

## IProjectProperties
继承：IProjectProperties → IDMObject → IInterface ｜ 单元：RT_Workspace ｜ 自有 35 个方法、0 个属性

function DM_Compare(DocumentPath: WideString; ReportFileName: WideString): LongBool;
procedure DM_DesignatorRecord_ECOAnnotatePhysicalComponent(const APart: IPart);
procedure DM_DesignatorRecord_ECOBegin;
procedure DM_DesignatorRecord_ECOChangeComponentDesignator(const AReferenceComponent: IComponent; const ATargetComponent: IComponent);
procedure DM_DesignatorRecord_ECOEnd;
function DM_DeviceSheetCount: Integer;
function DM_DeviceSheets(Index: Integer): IDocument;
function DM_ErrorLevelsForConnections(H: TConnectionCode; V: TConnectionCode): TErrorLevel;
function DM_GetAutoCrossReferences: Integer;
function DM_GetAutoSheetNumbering: Boolean;
function DM_GetDifferenceLevel(DifferenceKind: TDifferenceKind): TDifferenceCheckLevel;
function DM_GetItemRevisionGUID: WideString;
function DM_GetLogFolderPath: WideString;
function DM_GetManagedSheetsPath: WideString;
function DM_GetNameNetsHierarchically: Boolean;
function DM_GetNetlistSinglePinNets: Boolean;
function DM_GetNewIndexingOfSheetSymbols: Boolean;
function DM_GetNoChannelIndex: Integer;
function DM_GetPowerPortNamesTakePriority: Boolean;
function DM_InitializeLogFolderPath: WideString;
function DM_ProjectDocumentCount: Integer;
function DM_ProjectDocuments(Index: Integer): IDocument;
function DM_RunComponentVariationForm(Sch_Component: IInterface; PhysicalSheetName: WideString): Boolean;
function DM_RunDesignatorAnnotationForm(Sch_Designator: IInterface; PhysicalSheetName: WideString): Boolean;
function DM_RunParameterVariationForm(Sch_Parameter: IInterface; PhysicalSheetName: WideString): Boolean;
function DM_RunProjectDistributorWizard(PartSet: TReleaseDistributionPartSet): Boolean;
procedure DM_SetAutoCrossReferences(AValue: Integer);
procedure DM_SetAutoSheetNumbering(AValue: Boolean);
procedure DM_SetDifferenceLevel(DifferenceKind: TDifferenceKind; Value: TDifferenceCheckLevel);
procedure DM_SetErrorLevelsForConnections(H: TConnectionCode; V: TConnectionCode; ErrorLevel: TErrorLevel);
procedure DM_SetItemRevisionGUID(S: WideString);
procedure DM_SetLogFolderPath(ALogFolderPath: WideString);
procedure DM_SetNetlistSinglePinNets(AValue: Boolean);
function DM_UpdateBOMDocument(const BOMDocumentFullPath: string; const ReportFileName: string; const BOMToSynch: TBOMTypeSet): Boolean;
function DM_UpdateBOMFromDatabase(const BOMDocumentFullPath: string; const BOMToSynch: TBOMTypeSet; const CompileBOMDoc: Boolean): Boolean;

## IProjectVariant
继承：IProjectVariant → IDMObject → IInterface ｜ 单元：RT_Workspace ｜ 自有 20 个方法、0 个属性

function DM_AddComponentVariation: IComponentVariation;
procedure DM_AddParameter(AName: WideString; AValue: WideString);
function DM_AllowFabricationOutputs: Boolean;
function DM_AllowVariationPastMask: Boolean;
function DM_Description: WideString;
function DM_FindComponentVariationByDesignator(const ADesignator: WideString): IComponentVariation;
function DM_FindComponentVariationByUniqueId(const AUniqueId: WideString): IComponentVariation;
function DM_FindComponentVariationByUniqueIdName(const AUniqueId: WideString): IComponentVariation;
function DM_Name: WideString;
function DM_Project: IProject;
procedure DM_RemoveComponentVariation(Index: Integer);
procedure DM_RemoveParameter(const AParameter: IParameter);
procedure DM_RemoveParameterByName(const AParameterName: WideString);
procedure DM_SetAllowFabricationOutputs(const Value: Boolean);
procedure DM_SetAllowVariationPastMask(const Value: Boolean);
procedure DM_SetDescription(const Value: WideString);
procedure DM_SetName(const Value: WideString);
function DM_UniqueId: WideString;
function DM_VariationCount: Integer;
function DM_Variations(Index: Integer): IComponentVariation;

## IProviderSupport
继承：IProviderSupport → IInterface ｜ 单元：Data.DB ｜ 自有 19 个方法、0 个属性

procedure PSEndTransaction(Commit: Boolean);
procedure PSExecute;
procedure PSGetAttributes(List: TList);
function PSGetCommandText: string;
function PSGetCommandType: TPSCommandType;
function PSGetDefaultOrder: TIndexDef;
function PSGetKeyFields: string;
function PSGetParams: TParams;
function PSGetQuoteChar: string;
function PSGetTableName: string;
function PSGetUpdateException(E: Exception; Prev: EUpdateError): EUpdateError;
function PSInTransaction: Boolean;
function PSIsSQLBased: Boolean;
function PSIsSQLSupported: Boolean;
procedure PSReset;
procedure PSSetCommandText(const CommandText: string);
procedure PSSetParams(AParams: TParams);
procedure PSStartTransaction;
function PSUpdateRecord(UpdateKind: TUpdateKind; Delta: TDataSet): Boolean;

## IProviderSupportNG
继承：IProviderSupportNG → IInterface ｜ 单元：Data.DB ｜ 自有 20 个方法、0 个属性

procedure PSEndTransaction(Commit: Boolean);
procedure PSExecute;
function PSExecuteStatement(const ASQL: string; AParams: TParams): Integer;
procedure PSGetAttributes(List: TList);
function PSGetCommandText: string;
function PSGetCommandType: TPSCommandType;
function PSGetDefaultOrder: TIndexDef;
function PSGetKeyFields: string;
function PSGetParams: TParams;
function PSGetQuoteChar: string;
function PSGetTableName: string;
function PSGetUpdateException(E: Exception; Prev: EUpdateError): EUpdateError;
function PSInTransaction: Boolean;
function PSIsSQLBased: Boolean;
function PSIsSQLSupported: Boolean;
procedure PSReset;
procedure PSSetCommandText(const CommandText: string);
procedure PSSetParams(AParams: TParams);
procedure PSStartTransaction;
function PSUpdateRecord(UpdateKind: TUpdateKind; Delta: TDataSet): Boolean;

## IPublisher
继承：IPublisher → IInterface ｜ 单元：RT_Workspace ｜ 自有 3 个方法、0 个属性

function AppendPage(MetafileHandle: NativeUInt; PageNumber: Integer; PageCount: Integer; Subtitle: WideString; Flags: TPublisherPageFlags): LongBool;
function AppendPDFObject(ObjFile: WideString): LongBool;
function AppendU3D(const ModelPage: IU3DModelPage): LongBool;

## IReadWriteSync
继承：IReadWriteSync → IInterface ｜ 单元：System.SysUtils ｜ 自有 4 个方法、0 个属性

procedure BeginRead;
function BeginWrite: Boolean;
procedure EndRead;
procedure EndWrite;

## IReadonlySupportDocument
继承：IReadonlySupportDocument → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 2 个方法、0 个属性

function GetReadOnly: Boolean;
procedure SetReadOnly(const Value: Boolean);

## IRecentFilesManager
继承：IRecentFilesManager → IInterface ｜ 单元：RT_Workspace ｜ 自有 3 个方法、0 个属性

function GetRecentDocumentPath(Index: Integer): WideString;
function GetRecentProjectGroupPath(Index: Integer): WideString;
function GetRecentProjectPath(Index: Integer): WideString;

## IRecoverySave
继承：IRecoverySave → IInterface ｜ 单元：RT_Workspace ｜ 自有 2 个方法、1 个属性

property SaveRecovery: Boolean read GetSaveRecovery write SetSaveRecovery;
function GetSaveRecovery: Boolean;
procedure SetSaveRecovery(const AValue: Boolean);

## IReferenceObject
继承：IReferenceObject → IInterface ｜ 单元：RT_Workspace ｜ 自有 2 个方法、0 个属性

function DmObject(const Project: IProject): IDMObject;
function SchHandle: WideString;

## IReferenceObjectManager
继承：IReferenceObjectManager → IInterface ｜ 单元：RT_Workspace ｜ 自有 7 个方法、0 个属性

function GetAvailableObjectType(Index: Integer): TWorkspaceObjectId;
function GetAvailableObjectTypesCount: Integer;
function GetJsonByReferenceObject(const ReferenceObject: IReferenceObject): WideString;
function GetReferenceObject(ReferenceObjectTypeId: TWorkspaceObjectId; Index: Integer): IReferenceObject;
function GetReferenceObjectByJson(const Json: WideString): IReferenceObject;
function GetReferenceObjectsCount(ReferenceObjectTypeId: TWorkspaceObjectId): Integer;
procedure JumpToObject(const Json: WideString);

## IRegisterAssociation
继承：IRegisterAssociation → IBSDLObject → IInterface ｜ 单元：Rt_NexusDevices ｜ 自有 4 个方法、0 个属性

function GetInstructionOpcode(Index: Integer): IInstructionOpCode;
function GetInstructionOpcodeCount: Integer;
function GetRegisterLength: Integer;
function GetRegisterName: WideString;

## IReleaseManager
继承：IReleaseManager → IInterface ｜ 单元：RT_Workspace ｜ 自有 5 个方法、0 个属性

function CurrentBaseConfiguration: IBaseConfiguration;
function CurrentReleaseName: WideString;
function GetAllReleasesBasePath(AProject: IProject): WideString;
function IsReleaseRunning: LongBool;
procedure Log_OutputerMessage(AMessage: WideString);

## IReleaseResources
继承：IReleaseResources → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 2 个方法、0 个属性

procedure ReleaseResources(AForceRelease: LongBool);
function SupportReleaseResources: LongBool;

## IReleaseViewDocument
继承：IReleaseViewDocument → IInterface ｜ 单元：RT_Workspace ｜ 自有 1 个方法、0 个属性

function DM_ConfigurationReleaseManager: IConfigurationReleaseManager;

## IReleasesDocument
继承：IReleasesDocument → IInterface ｜ 单元：RT_Workspace ｜ 自有 1 个方法、0 个属性

procedure Refresh;

## IReportFactory
继承：IReportFactory → IInterface ｜ 单元：RT_Workspace ｜ 自有 2 个方法、0 个属性

function BuildGeneralReport(const AReportName: WideString): IGeneralReport;
procedure DestroyReport(const AReport: IBaseReport);

## IReportParameters
继承：IReportParameters → IInterface ｜ 单元：RT_IntegratedLibrary ｜ 自有 3 个方法、0 个属性

function GetParameterCount: Integer;
function GetParameterName(AIndex: Integer): WideString;
function GetParameterValue(AIndex: Integer): WideString;

## IReportTableInfo
继承：IReportTableInfo → IInterface ｜ 单元：RT_IntegratedLibrary ｜ 自有 5 个方法、0 个属性

function GetColumnCount: Integer;
function GetCurRowCell(AColumn: Integer): WideString;
function GetTitle: WideString;
function SetFirstRow: Boolean;
function SetNextRow: Boolean;

## IResourceCounter
继承：IResourceCounter → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 4 个方法、0 个属性

function Decrement(const AResourceName: WideString; AValue: Integer): Integer;
function GetValue(const AResourceName: WideString): Integer;
function Increment(const AResourceName: WideString; AValue: Integer): Integer;
procedure SetValue(const AResourceName: WideString; AValue: Integer);

## IResourceMonitor
继承：IResourceMonitor → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 5 个方法、0 个属性

function GetCommitSizeMB: Cardinal;
function GetGdiHandlesCount: Cardinal;
function GetGlobaAtomsCount: Integer;
function GetResourceCounter: IResourceCounter;
function GetSessionAtoms: Integer;

## IReuseBlock
继承：IReuseBlock → IDMObject → IInterface ｜ 单元：RT_Workspace ｜ 自有 10 个方法、0 个属性

function DM_BlockID: WideString;
function DM_BlockItemGUID: WideString;
function DM_BlockItemRevisionGUID: WideString;
function DM_BlockVaultGUID: WideString;
function DM_FindReuseComponent(const AComponent: IComponent): IReuseComponent;
function DM_GetReuseComponentByIndex(AIndex: Integer): IReuseComponent;
function DM_GetReuseComponentCount: Integer;
function DM_SelectedPCBItemGUID: WideString;
function DM_SelectedPCBItemRevisionGUID: WideString;
function DM_SelectedPCBVaultGUID: WideString;

## IReuseBlocks
继承：IReuseBlocks → IDMObject → IInterface ｜ 单元：RT_Workspace ｜ 自有 4 个方法、0 个属性

function DM_FindReuseBlockByComponent(const AComponent: IComponent): IReuseBlock;
function DM_FindReuseBlockByID(const ABlockID: WideString): IReuseBlock;
function DM_GetReuseBlockByIndex(AIndex: Integer): IReuseBlock;
function DM_GetReuseBlockCount: Integer;

## IReuseComponent
继承：IReuseComponent → IDMObject → IInterface ｜ 单元：RT_Workspace ｜ 自有 2 个方法、0 个属性

function DM_Component: IComponent;
function DM_SnippetComponentUniqueID: WideString;

## IRevisionSchemeDocument
继承：IRevisionSchemeDocument → IInterface ｜ 单元：RT_Workspace ｜ 自有 1 个方法、0 个属性

procedure Refresh;

## IRevisionsView
继承：IRevisionsView → IExternalForm → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 1 个方法、0 个属性

function Refresh(const AFileName: string): HRESULT;

## IRibbonContext
继承：IRibbonContext → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 1 个方法、0 个属性

function GetRibbonContext: WideString;

## IRoom
继承：IRoom → IDMObject → IInterface ｜ 单元：RT_Workspace ｜ 自有 8 个方法、0 个属性

function DM_HX: Integer;
function DM_HY: Integer;
function DM_Layer: Integer;
function DM_LX: Integer;
function DM_LY: Integer;
function DM_RoomName: WideString;
function DM_Scope1Expression: WideString;
procedure DM_SetRoomPCBHandle(APCBRoomHandle: IInterface);

## IRule
继承：IRule → IDMObject → IInterface ｜ 单元：RT_Workspace ｜ 自有 20 个方法、0 个属性

function DM_Attributes: WideString;
function DM_Description: WideString;
function DM_MaxViaHole: Integer;
function DM_MaxViaWidth: Integer;
function DM_MaxWidth: Integer;
function DM_MinViaHole: Integer;
function DM_MinViaWidth: Integer;
function DM_MinWidth: Integer;
function DM_PreferedWidth: Integer;
function DM_Priority: Integer;
function DM_RoutingLayers(IndexLayer: Integer): Integer;
function DM_RuleKind: Integer;
function DM_RuleName: WideString;
function DM_Scope1Expression: WideString;
function DM_Scope2Expression: WideString;
function DM_Topology: Integer;
function DM_UniqueId: WideString;
function DM_ViaHole: Integer;
function DM_ViaStyle: Integer;
function DM_ViaWidth: Integer;

## ISPIChannel
继承：ISPIChannel → IDeviceChannel → IInterface ｜ 单元：Rt_NexusDevices ｜ 自有 13 个方法、0 个属性

procedure SPI_BitDelay;
function SPI_GetDataPin: Byte;
function SPI_SelectDevice(ABoardAddress: Byte; ADeviceAddress: Byte): LongBool;
procedure SPI_SendAddress24(AAddress: Integer);
procedure SPI_SendAddress32(AAddress: Integer);
procedure SPI_SendByte(ADataByte: Byte);
procedure SPI_SendData(AData: Pointer; ALength: Integer);
procedure SPI_SendReceiveBits(ACmdBuffer: Pointer; ACmdLength: Integer; ADataBuffer: Pointer; ADataLength: Integer);
function SPI_SendReceiveByte(ADataByte: Byte): Byte;
procedure SPI_SendReceiveData(AData: Pointer; ALength: Integer);
procedure SPI_SetClockPin(N: Byte);
procedure SPI_SetDataPin(N: Byte);
procedure SPI_SetSelectPin(N: Byte);

## ISPIDevice
继承：ISPIDevice → IDevice → IInterface ｜ 单元：Rt_NexusDevices ｜ 自有 0 个方法、0 个属性


## ISPROMChannel
继承：ISPROMChannel → IDeviceChannel → IInterface ｜ 单元：Rt_NexusDevices ｜ 自有 6 个方法、0 个属性

function SPROM_PageSize: Integer;
function SPROM_ReadByte(AAddress: Integer): Byte;
procedure SPROM_ReadPage(AAddress: Integer; ABuffer: Pointer);
function SPROM_SelectDevice(ABoardAddress: Byte; ADeviceAddress: Byte): LongBool;
procedure SPROM_WriteByte(AAddress: Integer; AData: Byte);
procedure SPROM_WritePage(AAddress: Integer; ABuffer: Pointer);

## ISVNDatabaseLibDocument
继承：ISVNDatabaseLibDocument → IDatabaseLibDocument → IInterface ｜ 单元：RT_Workspace ｜ 自有 1 个方法、0 个属性

function GetRepositoryURL: WideString;

## ISaveLoadLayout
继承：ISaveLoadLayout → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 8 个方法、0 个属性

procedure RestoreLayout_Default;
procedure RestoreLayout_FromFile(ATLTFileName: WideString);
procedure RestoreLayout_FromPreviousVersion(APreviousVersionIndex: Integer);
procedure RestoreLayout_QueryFile;
procedure RestoreLayout_RecentLayout(ARecentLayoutIndex: Integer);
procedure RestoreLayout_Startup;
procedure SaveLayout_QueryFile;
function SaveLayout_ToFileForExport: WideString;

## IScanPin
继承：IScanPin → IBSDLObject → IInterface ｜ 单元：Rt_NexusDevices ｜ 自有 8 个方法、0 个属性

function GetBoundaryCell(Index: Integer): IBoundaryCell;
function GetBoundaryCellCount: Integer;
function GetCurrentValue: Integer;
function GetDirection: TPinElectrical;
function GetKind: TScanPinKind;
function GetPinMapping: IPinMapping;
function GetPinName: WideString;
function GetPinNumber: WideString;

## IScene
继承：IScene → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 3 个方法、3 个属性

property SceneCaption: WideString read GetSceneCaption;  // read-only
property SceneCategory: WideString read GetSceneCategory;  // read-only
property SceneId: WideString read GetSceneId;  // read-only
function GetSceneCaption: WideString;
function GetSceneCategory: WideString;
function GetSceneId: WideString;

## ISceneManager
继承：ISceneManager → INavigationProvider → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 3 个方法、0 个属性

procedure GetCategorySceneIds(const SceneCategory: WideString; const CategorySceneIds: IStrings);
function GetSceneById(const SceneId: WideString): IScene;
procedure GetSceneCategories(const SceneCategories: IStrings);

## ISceneView
继承：ISceneView → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 2 个方法、0 个属性

function CanClose: LongBool;
function CanCloseView: LongBool;

## ISchCompilator
继承：ISchCompilator → IInterface ｜ 单元：RT_Workspace ｜ 自有 14 个方法、0 个属性

function GetDDMProject(const ProjectFullPath: WideString): IDDMBoardProject;
function GetDMObject(ObjectAddress: Pointer; const ProjectFullPath: WideString): IDMObject;
function GetDynamicCompilator: IInterface;
function GetIDMObjectHelper: IInterface;
function GetSchDataModelUtils: IInterface;
procedure LogDebug(const Debug: WideString);
procedure LogError(const Error: WideString);
procedure LogInfo(const Info: WideString);
procedure LogWarn(const Warn: WideString);
function RegisterObserver(const DDMObserver: IDDMObserver; ObjectTypes: TWorkspaceObjectIdSet; ClientId: TUdmClient): Integer;
function ResumeContinuousCompilation(const ProjectFullPath: WideString): Boolean;
procedure SetOriginalProject(const ProjectFullPath: WideString; const OrgProject: IProject);
function SuspendContinuousCompilation(const ProjectFullPath: WideString): Boolean;
procedure UnregisterObserver(ObserverId: Integer);

## ISchCompilatorFactory
继承：ISchCompilatorFactory → IInterface ｜ 单元：RT_Workspace ｜ 自有 1 个方法、0 个属性

function CreateSchCompilator: ISchCompilator;

## ISchComponentLink
继承：ISchComponentLink → IInterface ｜ 单元：Rt_NexusWorkspace ｜ 自有 9 个方法、0 个属性

procedure CrossProbe;
function GetComponentDesignator: WideString;
function GetComponentDocumentPath: WideString;
function GetDescription: WideString;
function GetLibraryReference: WideString;
function GetProjectLink: IProjectLink;
function GetProjectPath: WideString;
function GetSubProjectPath: WideString;
procedure SetSubProjectPath(AProjectPath: WideString);

## IScriptedInstrument
继承：IScriptedInstrument → IInterface ｜ 单元：RT_ScriptedInstrument ｜ 自有 1 个方法、0 个属性

function GetDesignator: WideString;

## IScriptedInstrumentManager
继承：IScriptedInstrumentManager → IInterface ｜ 单元：RT_ScriptedInstrument ｜ 自有 0 个方法、0 个属性


## ISdComponent
继承：ISdComponent → ISdParametrizedObject → ISdObject → IInterface ｜ 单元：Rt_SystemDesign.Interfaces ｜ 自有 4 个方法、3 个属性

property Comment: WideString read GetComment;  // read-only
property Designator: WideString read GetDesignator;  // read-only
property Pins: ISdPinList read GetPins;  // read-only
function GetComment: WideString;
function GetDesignator: WideString;
function GetEntries: ISdEntryList;
function GetPins: ISdPinList;

## ISdConflict
继承：ISdConflict → ISdObject → IInterface ｜ 单元：Rt_SystemDesign.Interfaces ｜ 自有 4 个方法、4 个属性

property ConflictKind: TSdConflictKind read GetConflictKind;  // read-only
property IsResolved: Boolean read GetIsResolved;  // read-only
property IsValid: Boolean read GetIsValid;  // read-only
property RelatedObject: ISdObject read GetRelatedObject;  // read-only
function GetConflictKind: TSdConflictKind;
function GetIsResolved: Boolean;
function GetIsValid: Boolean;
function GetRelatedObject: ISdObject;

## ISdConnection
继承：ISdConnection → ISdParametrizedObject → ISdObject → IInterface ｜ 单元：Rt_SystemDesign.Interfaces ｜ 自有 11 个方法、7 个属性

property ComponentCount: Integer read GetComponentCount;  // read-only
property ConnectionType: TSdConnectionType read GetConnectionType;  // read-only
property Designator: WideString read GetDesignator;  // read-only
property EntryCount: Integer read GetEntryCount;  // read-only
property InternalConnectionCount: Integer read GetInternalConnectionCount;  // read-only
property PhysicalConnectionCount: Integer read GetPhysicalConnectionCount;  // read-only
property Source: WideString read GetSource;  // read-only
function GetComponent(Index: Integer): ISdComponent;
function GetComponentCount: Integer;
function GetConnectionType: TSdConnectionType;
function GetDesignator: WideString;
function GetEntry(Index: Integer): ISdEntry;
function GetEntryCount: Integer;
function GetInternalConnection(Index: Integer): ISdInternalConnection;
function GetInternalConnectionCount: Integer;
function GetPhysicalConnection(Index: Integer): ISdPhysicalConnection;
function GetPhysicalConnectionCount: Integer;
function GetSource: WideString;

## ISdConnectionEntry
继承：ISdConnectionEntry → ISdEntry → ISdParametrizedObject → ISdObject → IInterface ｜ 单元：Rt_SystemDesign.Interfaces ｜ 自有 0 个方法、0 个属性


## ISdDocument
继承：ISdDocument → ISdParametrizedObject → ISdObject → IInterface ｜ 单元：Rt_SystemDesign.Interfaces ｜ 自有 10 个方法、6 个属性

property ConflictCount: Integer read GetConflictCount;  // read-only
property ConnectionCount: Integer read GetConnectionCount;  // read-only
property DocumentId: Integer read GetDocumentId;  // read-only
property DocumentPath: WideString read GetDocumentPath;  // read-only
property ModuleCount: Integer read GetModuleCount;  // read-only
property UniqueId: WideString read GetUniqueId write SetUniqueId;
function GetConflict(Index: Integer): ISdConflict;
function GetConflictCount: Integer;
function GetConnection(Index: Integer): ISdConnection;
function GetConnectionCount: Integer;
function GetDocumentId: Integer;
function GetDocumentPath: WideString;
function GetModule(Index: Integer): ISdModule;
function GetModuleCount: Integer;
function GetUniqueId: WideString;
procedure SetUniqueId(const Value: WideString);

## ISdEntry
继承：ISdEntry → ISdParametrizedObject → ISdObject → IInterface ｜ 单元：Rt_SystemDesign.Interfaces ｜ 自有 5 个方法、5 个属性

property Comment: WideString read GetComment;  // read-only
property Designator: WideString read GetDesignator;  // read-only
property EntryType: TSdEntryType read GetEntryType;  // read-only
property MatedEntry: ISdEntry read GetMatedEntry;  // read-only
property Pins: ISdPinList read GetPins;  // read-only
function GetComment: WideString;
function GetDesignator: WideString;
function GetEntryType: TSdEntryType;
function GetMatedEntry: ISdEntry;
function GetPins: ISdPinList;

## ISdEntryList
继承：ISdEntryList → IInterface ｜ 单元：Rt_SystemDesign.Interfaces ｜ 自有 2 个方法、2 个属性

property Count: Integer read GetCount;  // read-only
property Items[Index: Integer]: ISdEntry read Get;  // read-only
function Get(Index: Integer): ISdEntry;
function GetCount: Integer;

## ISdFunctionalBlock
继承：ISdFunctionalBlock → ISdParametrizedObject → ISdObject → IInterface ｜ 单元：Rt_SystemDesign.Interfaces ｜ 自有 3 个方法、3 个属性

property Designator: WideString read GetDesignator;  // read-only
property Source: WideString read GetSource;  // read-only
property Title: WideString read GetTitle;  // read-only
function GetDesignator: WideString;
function GetSource: WideString;
function GetTitle: WideString;

## ISdInternalConnection
继承：ISdInternalConnection → ISdPinToPinConnection → ISdPhysicalConnection → ISdParametrizedObject → ISdObject → IInterface ｜ 单元：Rt_SystemDesign.Interfaces ｜ 自有 0 个方法、0 个属性


## ISdModule
继承：ISdModule → ISdParametrizedObject → ISdObject → IInterface ｜ 单元：Rt_SystemDesign.Interfaces ｜ 自有 12 个方法、9 个属性

property BoardFileName: WideString read GetBoardFileName;  // read-only
property ComponentCount: Integer read GetComponentCount;  // read-only
property Designator: WideString read GetDesignator;  // read-only
property EntryCount: Integer read GetEntryCount;  // read-only
property FunctionalBlockCount: Integer read GetFunctionalBlockCount;  // read-only
property IsSystem: Boolean read GetIsSystem;  // read-only
property Source: WideString read GetSource;  // read-only
property SourceGUID: WideString read GetSourceGUID;  // read-only
property Title: WideString read GetTitle;  // read-only
function GetBoardFileName: WideString;
function GetComponent(Index: Integer): ISdComponent;
function GetComponentCount: Integer;
function GetDesignator: WideString;
function GetEntry(Index: Integer): ISdModuleEntry;
function GetEntryCount: Integer;
function GetFunctionalBlock(Index: Integer): ISdFunctionalBlock;
function GetFunctionalBlockCount: Integer;
function GetIsSystem: Boolean;
function GetSource: WideString;
function GetSourceGUID: WideString;
function GetTitle: WideString;

## ISdModuleEntry
继承：ISdModuleEntry → ISdEntry → ISdParametrizedObject → ISdObject → IInterface ｜ 单元：Rt_SystemDesign.Interfaces ｜ 自有 1 个方法、1 个属性

property IsSystem: Boolean read GetIsSystem;  // read-only
function GetIsSystem: Boolean;

## ISdNet
继承：ISdNet → ISdParametrizedObject → ISdObject → IInterface ｜ 单元：Rt_SystemDesign.Interfaces ｜ 自有 3 个方法、3 个属性

property DefinedName: WideString read GetDefinedName;  // read-only
property Name: WideString read GetName;  // read-only
property Pins: ISdPinList read GetPins;  // read-only
function GetDefinedName: WideString;
function GetName: WideString;
function GetPins: ISdPinList;

## ISdObject
继承：ISdObject → IInterface ｜ 单元：Rt_SystemDesign.Interfaces ｜ 自有 2 个方法、2 个属性

property Id: WideString read GetId;  // read-only
property Path: WideString read GetPath;  // read-only
function GetId: WideString;
function GetPath: WideString;

## ISdParameter
继承：ISdParameter → ISdObject → IInterface ｜ 单元：Rt_SystemDesign.Interfaces ｜ 自有 3 个方法、2 个属性

property Name: WideString read GetName;  // read-only
property Value: WideString read GetValue write SetValue;
function GetName: WideString;
function GetValue: WideString;
procedure SetValue(const Value: WideString);

## ISdParametrizedObject
继承：ISdParametrizedObject → ISdObject → IInterface ｜ 单元：Rt_SystemDesign.Interfaces ｜ 自有 2 个方法、1 个属性

property ParameterCount: Integer read GetParameterCount;  // read-only
function GetParameter(Index: Integer): ISdParameter;
function GetParameterCount: Integer;

## ISdPhysicalConnection
继承：ISdPhysicalConnection → ISdParametrizedObject → ISdObject → IInterface ｜ 单元：Rt_SystemDesign.Interfaces ｜ 自有 4 个方法、4 个属性

property Designator: WideString read GetDesignator;  // read-only
property Entry1: ISdEntry read GetEntry1;  // read-only
property Entry2: ISdEntry read GetEntry2;  // read-only
property Net: ISdNet read GetNet;  // read-only
function GetDesignator: WideString;
function GetEntry1: ISdEntry;
function GetEntry2: ISdEntry;
function GetNet: ISdNet;

## ISdPin
继承：ISdPin → ISdParametrizedObject → ISdObject → IInterface ｜ 单元：Rt_SystemDesign.Interfaces ｜ 自有 6 个方法、6 个属性

property Component: ISdComponent read GetComponent;  // read-only
property MatedPin: ISdPin read GetMatedPin;  // read-only
property Name: WideString read GetName;  // read-only
property Net: ISdNet read GetNet;  // read-only
property Number: WideString read GetNumber;  // read-only
property PinId: WideString read GetPinId;  // read-only
function GetComponent: ISdComponent;
function GetMatedPin: ISdPin;
function GetName: WideString;
function GetNet: ISdNet;
function GetNumber: WideString;
function GetPinId: WideString;

## ISdPinList
继承：ISdPinList → IInterface ｜ 单元：Rt_SystemDesign.Interfaces ｜ 自有 2 个方法、2 个属性

property Count: Integer read GetCount;  // read-only
property Items[Index: Integer]: ISdPin read Get;  // read-only
function Get(Index: Integer): ISdPin;
function GetCount: Integer;

## ISdPinNetNameConflict
继承：ISdPinNetNameConflict → ISdConflict → ISdObject → IInterface ｜ 单元：Rt_SystemDesign.Interfaces ｜ 自有 2 个方法、2 个属性

property CurrentValue: WideString read GetCurrentValue;  // read-only
property OldValue: WideString read GetOldValue;  // read-only
function GetCurrentValue: WideString;
function GetOldValue: WideString;

## ISdPinToPinConnection
继承：ISdPinToPinConnection → ISdPhysicalConnection → ISdParametrizedObject → ISdObject → IInterface ｜ 单元：Rt_SystemDesign.Interfaces ｜ 自有 0 个方法、0 个属性


## ISdWire
继承：ISdWire → ISdPinToPinConnection → ISdPhysicalConnection → ISdParametrizedObject → ISdObject → IInterface ｜ 单元：Rt_SystemDesign.Interfaces ｜ 自有 0 个方法、0 个属性


## ISearchComponentResult
继承：ISearchComponentResult → IInterface ｜ 单元：RT_IntegratedLibrary ｜ 自有 2 个方法、0 个属性

function ComponentData: ILibraryComponentData;
function LibraryGUID: WideString;

## ISearchComponentResultList
继承：ISearchComponentResultList → IInterfaceList → IInterface ｜ 单元：RT_IntegratedLibrary ｜ 自有 1 个方法、1 个属性

property Items[I: Integer]: ISearchComponentResult read GetSearchComponentResult;  // read-only
function GetSearchComponentResult(I: Integer): ISearchComponentResult;

## ISearchLibraryEventHandler
继承：ISearchLibraryEventHandler → IInterface ｜ 单元：RT_IntegratedLibrary ｜ 自有 2 个方法、0 个属性

procedure HandleProgress(const AResult: ISearchComponentResultList; const AMessage: WideString);
procedure HandleStart;

## ISearchPath
继承：ISearchPath → IDMObject → IInterface ｜ 单元：RT_Workspace ｜ 自有 4 个方法、0 个属性

function DM_AbsolutePath: WideString;
function DM_IncludeSubFolders: Boolean;
function DM_Path: WideString;
function DM_Project: IProject;

## ISecurityManager
继承：ISecurityManager → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 22 个方法、1 个属性

property LicenseCount: Integer read GetLicenseCount;  // read-only
function AbsoluteSubscriptionActivationCode: WideString;
function AbsoluteSubscriptionExpiryDate: TDateTime;
function AnyUnsupportedLicenseForThisBuild: LongBool;
function AnyValidLicenses: LongBool;
function GetClientVersion: WideString;
function GetHardwareDescriptionString: WideString;
function GetLicenseByLicenseAssignment(const LicenseAssignmentId: WideString): ILicense;
function GetLicenseBySerialNumber(SerialNumber: Int64): ILicense;
function GetLicenseCount: Integer;
function GetLicensedState: WideString;
function GetLicenseUsage: WideString;
function GetMaxTrialDateForTechnology(const ATechnologyName: WideString): TDateTime;
function GetSerialNumberFromLicenseID(const LicenseId: WideString): WideString;
function GetSubscriptionExpirationDate(const ATechnologyName: WideString): TDateTime;
function GetTimeZoneOffset: Double;
function IsSubscriptionCurrent: LongBool;
function IsTrial: LongBool;
function IsTrialStart: LongBool;
procedure RefreshLicenseInformation;
procedure RefreshLicensesInformation;
procedure ReturnLease(const License: ILicense);
procedure UseLicense(const SerialNumber: Int64);

## ISecurityServerManager
继承：ISecurityServerManager → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 16 个方法、3 个属性

property IsFreeLicenseMode: Boolean read GetIsFreeLicenseMode;  // read-only
property LicenseCount: Integer read GetLicenseCount;  // read-only
property ServerLicenses[Index: Integer]: IServerLicense read GetServerLicenses;  // read-only
function ActivateStandaloneLicense(const LicenseId: WideString): IServerLicense;
function AddLicenseFile(AReplaceExisting: Boolean): IServerLicense;
procedure AutoLeaseNewOnDemandLicensesByTimer(AValue: Boolean);
procedure ClearLicenses;
procedure DeactivateAndRemoveLeasedLicense_BySerialNumber(SerialNumber: Int64; ASilentMode: LongBool);
procedure FreeAllLicenses;
function GetIsFreeLicenseMode: Boolean;
function GetLicenseByLicenseAssignment(const LicenseAssignmentId: WideString): IServerLicense;
function GetLicenseBySerialNumber(SerialNumber: Int64): IServerLicense;
function GetLicenseCount: Integer;
function GetServerLicenses(Index: Integer): IServerLicense;
function HasActiveSubscription: Boolean;
procedure ResetRenewLicensesOnSignIn;
procedure SaveLicenseFile(SerialNumber: Int64);
procedure UseAvailableOnDemandLicenses(AIsForceLease: Boolean);
function UseOnDemandLicense(const LicenseAssignmentGUID: WideString; const LeaseKind: WideString; AMaxBorrowDuration: Integer): IServerLicense;

## IServerDocument
继承：IServerDocument → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 43 个方法、11 个属性

property BeingClosed: LongBool read GetBeingClosed write SetBeingClosed;
property CanClose: LongBool read GetCanClose;  // read-only
property Count: Integer read GetCount;  // read-only
property DocumentModifiedDate: TDateTime read GetDocumentModifiedDate;  // read-only
property FileName: WideString read GetFileName;  // read-only
property IsShown: LongBool read GetIsShown write SetIsShown;
property Kind: WideString read GetKind;  // read-only
property Modified: LongBool read GetModified write SetModified;
property ServerModule: IServerModule read GetServerModule;  // read-only
property SupportsOwnSave: LongBool read GetSupportsOwnSave;  // read-only
property View[Index: Integer]: IServerDocumentView read GetView;  // read-only
procedure AcquireDataFileHandle;
procedure AcquireFileOwnership;
procedure AddView(const AView: IServerDocumentView);
function CanCreateSnippet(const AView: IServerDocumentView; AMode: TSnippetCreationMode; AContextSensitive: Boolean): Boolean;
function CanPlaceSnippet(const ASnippetPath: WideString): Boolean;
function CompareWithShadow(AShadowDoc: IServerDocument; ACompareView: IServerView): LongBool;
function CreateSnippetFile(const AView: IServerDocumentView; ASnippetFilePath: WideString; AMode: TSnippetCreationMode; AContextSensitive: Boolean): Boolean;
procedure DocumentDirectoryChanged;
function DoFileLoad: LongBool;
function DoFileSave(const AKind: WideString): LongBool;
function DoSafeChangeFileNameAndSave(const ANewFileName: WideString; const AKind: WideString): LongBool;
function DoSafeFileSave(const AKind: WideString): LongBool;
procedure Focus;
function GetBeingClosed: LongBool;
function GetCanClose: LongBool;
function GetContextHelpTopicName: WideString;
function GetCount: Integer;
function GetDocumentModifiedDate: TDateTime;
function GetExternalFiles(ACheckForExistence: Boolean): IExternalFiles;
function GetFileModifiedDate: TDateTime;
function GetFileName: WideString;
function GetIsShown: LongBool;
function GetKind: WideString;
function GetModified: LongBool;
function GetServerModule: IServerModule;
function GetSnippetView: IServerDocumentView;
function GetSupportsOwnSave: LongBool;
function GetView(Index: Integer): IServerDocumentView;
function GetViewByName(const ViewName: WideString): IServerDocumentView;
procedure NotifyViews(ANotification: INotification);
function OwnsFile: Boolean;
procedure PlaceSnippet(ASnippetAddress: WideString; const AView: IServerDocumentView);
procedure ReleaseDataFileHandle;
procedure ReleaseFileOwnership;
procedure SetBeingClosed(const Value: LongBool);
procedure SetFileModifiedDate(const AValue: TDateTime);
function SetFileName(const AFileName: WideString): WideString;
procedure SetIsShown(const Value: LongBool);
procedure SetModified(const Value: LongBool);
function SupportsReload: LongBool;
procedure UpdateModifiedDate;
function WarnIfOwnedByOther(AWarningLevel: TFileOwnershipWarningLevel): LongBool;
procedure ZoomSnippetContents;

## IServerDocument2
继承：IServerDocument2 → IServerDocument → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 3 个方法、2 个属性

property DisplayName: WideString read GetDisplayName write SetDisplayName;
property OpenDocumentId: WideString read GetOpenDocumentId;  // read-only
function GetDisplayName: WideString;
function GetOpenDocumentId: WideString;
procedure SetDisplayName(const AValue: WideString);

## IServerDocumentEx
继承：IServerDocumentEx → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 2 个方法、0 个属性

procedure PlaceSnippetAsBlock(const ASnippetAddress: WideString; const AView: IServerDocumentView);
procedure RemoveViewByName(const ViewName: WideString);

## IServerDocumentSaveStatusSupport
继承：IServerDocumentSaveStatusSupport → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 2 个方法、0 个属性

function CanSaveDocument: LongBool;
function CanSaveDocumentCopy: LongBool;

## IServerDocumentView
继承：IServerDocumentView → IServerView → IExternalForm → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 3 个方法、1 个属性

property OwnerDocument: IServerDocument read GetOwnerDocument;  // read-only
function GetOwnerDocument: IServerDocument;
procedure PerformAutoZoom;
procedure UpdateStatusBar;

## IServerDocumentViewRegistry
继承：IServerDocumentViewRegistry → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 3 个方法、0 个属性

function Count: Integer;
function Get(AIndex: Integer): IServerDocumentView;
procedure Init(AClient: IClient; AServer: IServerDocument);

## IServerEventHandler
继承：IServerEventHandler → IInterface ｜ 单元：RT_Workspace ｜ 自有 3 个方法、0 个属性

procedure HandleConnectToServer;
procedure HandleDisconnectFromServer;
procedure HandleReleaseCommited(const AContentTypeGUID: WideString);

## IServerInternalOptions
继承：IServerInternalOptions → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 1 个方法、0 个属性

function GetOptionsManager: IServerInternalOptionsManager;

## IServerInternalOptionsManager
继承：IServerInternalOptionsManager → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 3 个方法、0 个属性

function GetPageName: WideString;
procedure LoadSettingsFromFiles(const ASettingsFiles: IStrings; const ADocumentsInstallPath: WideString);
procedure SaveSettingsToFiles(const ASettingsFiles: IStrings);

## IServerLicense
继承：IServerLicense → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 13 个方法、13 个属性

property ActivationCode: WideString read GetActivationCode;  // read-only
property CanRoam: LongBool read GetCanRoam;  // read-only
property EndDate: TDateTime read GetEndDate;  // read-only
property Expired: LongBool read GetExpired;  // read-only
property LeaseExpiryTime: TDateTime read GetLeaseExpiryTime;  // read-only
property LicenseAssignmentGUID: WideString read GetLicenseAssignmentGUID;  // read-only
property LicenseGUID: WideString read GetLicenseGUID;  // read-only
property LicenseType: Integer read GetLicenseType;  // read-only
property LicenseUsageId: WideString read GetLicenseUsageId;  // read-only
property ProductName: WideString read GetProductName;  // read-only
property RightToUpgradeExpiryDate: TDateTime read GetRightToUpgradeExpiryDate;  // read-only
property SerialNumber: Int64 read GetSerialNumber;  // read-only
property StatusText: WideString read GetStatusText;  // read-only
function GetActivationCode: WideString;
function GetCanRoam: LongBool;
function GetEndDate: TDateTime;
function GetExpired: LongBool;
function GetLeaseExpiryTime: TDateTime;
function GetLicenseAssignmentGUID: WideString;
function GetLicenseGUID: WideString;
function GetLicenseType: Integer;
function GetLicenseUsageId: WideString;
function GetProductName: WideString;
function GetRightToUpgradeExpiryDate: TDateTime;
function GetSerialNumber: Int64;
function GetStatusText: WideString;

## IServerModel
继承：IServerModel → IInterface ｜ 单元：RT_IntegratedLibrary ｜ 自有 6 个方法、1 个属性

property PortNames[AnIndex: Integer]: PChar read PortName;  // read-only
procedure AddPort(AName: PWideChar);
function CheckModelPins: Boolean;
function CheckSchPins: Boolean;
function Name: PWideChar;
function PortCount: Integer;
function PortName(AnIndex: Integer): PWideChar;

## IServerModel2
继承：IServerModel2 → IInterface ｜ 单元：RT_IntegratedLibrary ｜ 自有 2 个方法、1 个属性

property Parameters: WideString read GetState_Parameters write SetState_Parameters;
function GetState_Parameters: WideString;
procedure SetState_Parameters(AValue: WideString);

## IServerModule
继承：IServerModule → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 20 个方法、9 个属性

property Client: IClient read GetClient;  // read-only
property CommandLauncher: ICommandLauncher read GetCommandLauncher;  // read-only
property DocumentCount: Integer read GetDocumentCount;  // read-only
property Documents[Index: Integer]: IServerDocument read GetDocuments;  // read-only
property Handle: THandle read GetHandle;  // read-only
property ModuleName: WideString read GetModuleName;  // read-only
property ProcessControl: IProcessControl read GetProcessControl;  // read-only
property ViewCount: Integer read GetViewCount;  // read-only
property Views[Index: Integer]: IServerView read GetViews;  // read-only
procedure AddServerView(const AView: IServerView);
procedure ApplicationIdle;
function CreateDocument(const AKind: WideString; const AFileName: WideString): IServerDocument;
function CreateDocumentShowOrHide(const AKind: WideString; const AFileName: WideString; AShowInTree: Boolean): IServerDocument;
function CreateOptionsView(const AName: WideString): IDocumentOptionsView;
function CreateServerDocView(const AName: WideString; const ADocument: IServerDocument): IServerDocumentView;
function CreateServerView(const AName: WideString): IServerView;
procedure DestroyDocument(const ADocument: IServerDocument);
function GetClient: IClient;
function GetCommandLauncher: ICommandLauncher;
function GetDocumentCount: Integer;
function GetDocuments(Index: Integer): IServerDocument;
function GetHandle: NativeUInt;
function GetModuleName: WideString;
function GetProcessControl: IProcessControl;
function GetShadowDocument(const AFileName: WideString): IServerDocument;
function GetViewCount: Integer;
function GetViews(Index: Integer): IServerView;
procedure ReceiveNotification(const ANotification: INotification);
procedure RemoveServerView(const AView: IServerView);

## IServerModuleActionsSupport
继承：IServerModuleActionsSupport → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 1 个方法、0 个属性

procedure SetServerDocumentView(const Value: IServerDocumentView);

## IServerModuleOptions
继承：IServerModuleOptions → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 1 个方法、0 个属性

function IsRelatedToServer(const AOptionsPageName: WideString): LongBool;

## IServerOptions
继承：IServerOptions → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 3 个方法、0 个属性

function CreateOptionsPageByName(const OptionsPageName: WideString): IOptionsPage;
procedure FlushOptions;
procedure ReloadOptions;

## IServerPanelInfo
继承：IServerPanelInfo → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 16 个方法、4 个属性

property DocumentKindCount: Integer read GetDocumentKindCount;  // read-only
property DocumentKinds[Index: Integer]: WideString read GetDocumentKinds;  // read-only
property ProjectKindCount: Integer read GetProjectKindCount;  // read-only
property ProjectKinds[Index: Integer]: WideString read GetProjectKinds;  // read-only
function GetBitmap: WideString;
function GetButtonVisible: Boolean;
function GetCanDockHorizontal: Boolean;
function GetCanDockVertical: Boolean;
function GetCategory: WideString;
function GetCreationClassName: WideString;
function GetDocumentKindCount: Integer;
function GetDocumentKinds(Index: Integer): WideString;
function GetHasCloudFeatures: Boolean;
function GetHotkey: WideString;
function GetMultipleCreation: Boolean;
function GetName: WideString;
function GetProjectKindCount: Integer;
function GetProjectKinds(Index: Integer): WideString;
function SupportsDocumentKind(const AKind: WideString): Boolean;
function SupportsProjectKind(const AKind: WideString): Boolean;

## IServerProcess
继承：IServerProcess → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 4 个方法、0 个属性

function GetLongSummary: WideString;
function GetOriginalId: WideString;
function GetParameter(Index: Integer): WideString;
function GetParameterCount: Integer;

## IServerRecord
继承：IServerRecord → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 27 个方法、0 个属性

function GetCommand(Index: Integer): IServerProcess;
function GetCommandCount: Integer;
function GetCopyRight: WideString;
function GetDate: WideString;
function GetDescription: WideString;
procedure GetDocumentFilter(Index: Integer; out Kind: WideString; out Filter: WideString);
function GetDocumentFilterCount: Integer;
function GetExePath: WideString;
function GetGeneralInfo: WideString;
function GetInsPath: WideString;
function GetIsDocumentWizard: LongBool;
function GetName: WideString;
procedure GetOutputHandler(Index: Integer; out Format: WideString; out DocKind: WideString; out ServerName: WideString; out Command: WideString);
function GetOutputHandlerCount: Integer;
function GetPanelInfo(Index: Integer): IServerPanelInfo;
function GetPanelInfoByName(const Name: WideString): IServerPanelInfo;
function GetPanelInfoCount: Integer;
function GetRCSFilePath: WideString;
function GetServerFileExist: LongBool;
function GetShowOnSplashScreen: Boolean;
function GetSupportsDDBRead: LongBool;
function GetSupportsDDBWrite: LongBool;
function GetSystemExtension: LongBool;
function GetVersion: WideString;
function GetWindowKind(Index: Integer): IServerWindowKind;
function GetWindowKindByName(const Name: WideString): IServerWindowKind;
function GetWindowKindCount: Integer;

## IServerSecurity
继承：IServerSecurity → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 1 个方法、0 个属性

function IsTechnologySetSupported(const ATechnologySet: WideString): Boolean;

## IServerView
继承：IServerView → IExternalForm → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 7 个方法、2 个属性

property IsPanel: LongBool read GetIsPanel;  // read-only
property ViewName: WideString read GetViewName;  // read-only
function GetFavoritesViewState(const AAddFavoriteView: LongBool): WideString;
function GetIsPanel: LongBool;
function GetViewName: WideString;
function GetViewState: WideString;
procedure ReceiveNotification(const ANotification: INotification);
procedure SetFavoritesViewState(const Astate: WideString);
procedure SetViewState(const Astate: WideString);

## IServerViewRegistry
继承：IServerViewRegistry → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 3 个方法、0 个属性

function Count: Integer;
function Get(AIndex: Integer): IServerView;
procedure Init(AClient: IClient; AServer: IServerModule);

## IServerWindowKind
继承：IServerWindowKind → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 19 个方法、0 个属性

function FileExportDescriptionCount: Integer;
function FileImportDescriptionCount: Integer;
function FileLoadDescriptionCount: Integer;
function FileSaveDescriptionCount: Integer;
function GetFileExportDescription(Index: Integer): WideString;
function GetFileImportDescription(Index: Integer): WideString;
function GetFileLoadDescription(Index: Integer): WideString;
function GetFileSaveDescription(Index: Integer): WideString;
function GetIconName: WideString;
function GetIsDocumentEditor: Boolean;
function GetIsDomain: LongBool;
function GetName: WideString;
function GetNewWindowCaption: WideString;
function GetNewWindowExtension: WideString;
function GetServerRecord: IServerRecord;
function GetWindowKindClass(Index: Integer): WideString;
function GetWindowKindClassCount: Integer;
function GetWindowKindDescription: WideString;
function IsOfWindowKindClass(const AClass: WideString): Boolean;

## ISheetNumberRecord
继承：ISheetNumberRecord → IInterface ｜ 单元：RT_Workspace ｜ 自有 3 个方法、0 个属性

function GetDocumentName: WideString;
function GetSheetNumber: WideString;
function GetUniqueIDPath: WideString;

## ISheetSymbol
继承：ISheetSymbol → IDMObject → IInterface ｜ 单元：RT_Workspace ｜ 自有 17 个方法、0 个属性

function DM_CalculatedDesignator: WideString;
function DM_ChildSheet(Index: Integer): IDocument;
function DM_ChildSheetCount: Integer;
function DM_DesignItemID: WideString;
function DM_ItemGUID: WideString;
function DM_LogicalDesignator: WideString;
function DM_PhysicalDesignator: WideString;
function DM_RawSheetSymbolFileName: WideString;
function DM_Replicate(const ADocument: IDMObject): ISheetSymbol;
function DM_RevisionGUID: WideString;
function DM_SheetEntries(Index: Integer): INetItem;
function DM_SheetEntryCount: Integer;
function DM_SheetSymbolFileName: WideString;
function DM_SourceLibraryName: WideString;
function DM_SymbolType: Integer;
function DM_UniqueId: WideString;
function DM_VaultGUID: WideString;

## ISignal
继承：ISignal → IDMObject → IInterface ｜ 单元：RT_Workspace ｜ 自有 24 个方法、0 个属性

function DM_BusKind: TBusKind;
function DM_DriverBitCount(BitNo: Integer): Integer;
function DM_DriverBits(BitNo: Integer; Index: Integer): ISignalNode;
function DM_DriverLinkCount: Integer;
function DM_DriverLinks(Index: Integer): ISignalLink;
function DM_NamerCount: Integer;
function DM_Namers(Index: Integer): ISignalNode;
function DM_PowerName: WideString;
function DM_PowerNode: ISignalNode;
function DM_Prefix: WideString;
function DM_PrimaryNode: ISignalNode;
function DM_Range1: WideString;
function DM_Range2: WideString;
function DM_RangeMax: Integer;
function DM_RangeMin: Integer;
function DM_RangeValue1: Integer;
function DM_RangeValue2: Integer;
function DM_SubNetCount: Integer;
function DM_SubNets(Index: Integer): ISubNet;
function DM_TargetBitCount(BitNo: Integer): Integer;
function DM_TargetBits(BitNo: Integer; Index: Integer): ISignalNode;
function DM_TargetLinkCount: Integer;
function DM_TargetLinks(Index: Integer): ISignalLink;
function DM_Width: Integer;

## ISignalHarnessProject
继承：ISignalHarnessProject → IInterface ｜ 单元：RT_Workspace ｜ 自有 1 个方法、0 个属性

function DM_GetHarnessDefinitionList: IHarnessDefinitionList;

## ISignalInstrument
继承：ISignalInstrument → IScriptedInstrument → IInterface ｜ 单元：RT_Digital_IO ｜ 自有 9 个方法、0 个属性

procedure BeginUpdate;
procedure EndUpdate;
function GetInputSignal(Index: Integer): IIOSignal;
function GetInputSignalCount: Integer;
function GetOutputSignal(Index: Integer): IIOSignal;
function GetOutputSignalCount: Integer;
function GetSignalByName(const ASignalName: WideString): IIOSignal;
function IsInUpdate: LongBool;
procedure UpdateSignals(AInput: LongBool; AOutput: LongBool);

## ISignalInstrumentEventHandler
继承：ISignalInstrumentEventHandler → IInterface ｜ 单元：RT_Digital_IO ｜ 自有 1 个方法、0 个属性

procedure Handle_OnPoll;

## ISignalInstrumentManager
继承：ISignalInstrumentManager → IScriptedInstrumentManager → IInterface ｜ 单元：RT_Digital_IO ｜ 自有 13 个方法、2 个属性

property AutoPolling: LongBool read GetAutoPolling write SetAutoPolling;
property PollingInterval: Cardinal read GetPollingInterval write SetPollingInterval;
procedure BeginUpdate;
procedure EndUpdate;
function GetAutoPolling: LongBool;
function GetPollingInterval: Cardinal;
function GetSignalInstrument(Index: Integer): ISignalInstrument;
function GetSignalInstrumentByDesignator(const ADesignator: WideString): ISignalInstrument;
function GetSignalInstrumentByJtagIndex(AJtagIndex: Integer): ISignalInstrument;
function GetSignalInstrumentCount: Integer;
procedure RegisterEventHandler(const AEventHandler: ISignalInstrumentEventHandler);
procedure SetAutoPolling(AValue: LongBool);
procedure SetPollingInterval(AValue: Cardinal);
procedure UnregisterEventHandler(const AEventHandler: ISignalInstrumentEventHandler);
procedure UpdateSignals(AInput: LongBool; AOutput: LongBool);

## ISignalLink
继承：ISignalLink → IDMObject → IInterface ｜ 单元：RT_Workspace ｜ 自有 16 个方法、0 个属性

function DM_DriverNode: ISignalNode;
function DM_DriverNodeRange1: WideString;
function DM_DriverNodeRange2: WideString;
function DM_DriverNodeRangeValue1: Integer;
function DM_DriverNodeRangeValue2: Integer;
function DM_DriverRangeMax: Integer;
function DM_DriverRangeMin: Integer;
function DM_DriverSignal: ISignal;
function DM_TargetNode: ISignalNode;
function DM_TargetNodeRange1: WideString;
function DM_TargetNodeRange2: WideString;
function DM_TargetNodeRangeValue1: Integer;
function DM_TargetNodeRangeValue2: Integer;
function DM_TargetRangeMax: Integer;
function DM_TargetRangeMin: Integer;
function DM_TargetSignal: ISignal;

## ISignalManager
继承：ISignalManager → IDMObject → IInterface ｜ 单元：RT_Workspace ｜ 自有 10 个方法、0 个属性

function DM_EntityPortCount: Integer;
function DM_EntityPorts(Index: Integer): IEntityPort;
function DM_InstanceCount: Integer;
function DM_InstanceKindCount: Integer;
function DM_InstanceKinds(Index: Integer): IInstance;
function DM_Instances(Index: Integer): IInstance;
function DM_SignalCount: Integer;
function DM_Signals(Index: Integer): ISignal;
function DM_SubNetCount: Integer;
function DM_SubNets(Index: Integer): ISubNet;

## ISignalNode
继承：ISignalNode → IDMObject → IInterface ｜ 单元：RT_Workspace ｜ 自有 21 个方法、0 个属性

function DM_BusIndex: Integer;
function DM_ConstantExpression: WideString;
function DM_Direction: TSignalDirection;
function DM_DriverLinkCount: Integer;
function DM_DriverLinks(Index: Integer): ISignalLink;
function DM_EntityPort: IEntityPort;
function DM_GetDescription: WideString;
function DM_GetName: WideString;
function DM_IsDriver: LongBool;
function DM_NetItem: INetItem;
function DM_Range1: WideString;
function DM_Range2: WideString;
function DM_RangeMax: Integer;
function DM_RangeMin: Integer;
function DM_RangeValue1: Integer;
function DM_RangeValue2: Integer;
function DM_Signal: ISignal;
function DM_SubNet: ISubNet;
function DM_TargetLinkCount: Integer;
function DM_TargetLinks(Index: Integer): ISignalLink;
function DM_Width: Integer;

## ISilentSupport
继承：ISilentSupport → IInterface ｜ 单元：RT_Workspace ｜ 自有 2 个方法、1 个属性

property SilentMode: Boolean read GetSilentMode write SetSilentMode;
function GetSilentMode: Boolean;
procedure SetSilentMode(const Value: Boolean);

## ISimWatch
继承：ISimWatch → IInterface ｜ 单元：Rt_VHDL ｜ 自有 14 个方法、1 个属性

property Enable: Boolean read GetEnable write SetEnable;
procedure Clear;
function GetAllEvents: IInterfaceList;
function GetCurrentData: Pointer;
function GetEnable: Boolean;
function GetEvent(AIndex: Integer): IEvent;
function GetEventCount: Integer;
function GetLastData: Pointer;
function GetLogicType: ILogicSimType;
function GetName: PWideChar;
function GetOwnerKind: PWideChar;
function GetType: PWideChar;
function GetValid: Boolean;
function IsVariable: Boolean;
procedure SetEnable(AEnable: Boolean);

## ISingleCastObserver
继承：ISingleCastObserver → IObserver → IInterface ｜ 单元：System.Classes ｜ 自有 0 个方法、0 个属性


## ISizedControl
继承：ISizedControl → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 2 个方法、2 个属性

property PreferredHeight: Integer read GetPreferredHeight;  // read-only
property PreferredWidth: Integer read GetPreferredWidth;  // read-only
function GetPreferredHeight: Integer;
function GetPreferredWidth: Integer;

## ISoftBreakpoint
继承：ISoftBreakpoint → IInterface ｜ 单元：Rt_NexusDevices ｜ 自有 12 个方法、2 个属性

property Address: TMemoryAddress read GetAddress write SetAddress;
property MemorySpace: Integer read GetMemorySpace write SetMemorySpace;
function Disable: LongBool;
function Enable: LongBool;
procedure Export_ToCore;
function GetAddress: Int64;
function GetMemorySpace: Integer;
function GetNexusDevice: INexusDevice;
function GetReplaced: Cardinal;
procedure Import_FromCore;
procedure Reset;
procedure SetAddress(Value: Int64);
procedure SetMemorySpace(AMemorySpace: Integer);
procedure SetReplaced(Value: Cardinal);

## ISoftDesignNotification
继承：ISoftDesignNotification → INotification → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 6 个方法、4 个属性

property BoardUniqueIdCount: Integer read GetBoardUniqueIdCount;  // read-only
property BoardUniqueIds[AIndex: Integer]: WideString read GetBoardUniqueIds;  // read-only
property Code: Integer read GetCode;  // read-only
property FirmwareVersions[AIndex: Integer]: WideString read GetFirmwareVersions;  // read-only
procedure AddBoardUniqueId(ABoardUniqueId: WideString);
procedure AddFirmwareVersion(AFirmwareVersion: WideString);
function GetBoardUniqueIdCount: Integer;
function GetBoardUniqueIds(AIndex: Integer): WideString;
function GetCode: Integer;
function GetFirmwareVersions(AIndex: Integer): WideString;

## ISourceRelationship
继承：ISourceRelationship → IInterface ｜ 单元：Rt_AltiumLibrary ｜ 自有 12 个方法、12 个属性

property ManufacturerName: WideString read GetState_ManufacturerName;  // read-only
property ManufacturerPartNumber: WideString read GetState_ManufacturerPartNumber;  // read-only
property PartId: WideString read GetState_PartId;  // read-only
property ProviderGUID: WideString read GetState_ProviderGUID;  // read-only
property ProviderName: WideString read GetState_ProviderName;  // read-only
property RoHS: WideString read GetState_RoHS;  // read-only
property SupplierName: WideString read GetState_SupplierName;  // read-only
property SupplierPartNumber: WideString read GetState_SupplierPartNumber;  // read-only
property SupplierPartNumberAlias: WideString read GetState_SupplierPartNumberAlias;  // read-only
property SupplierSource: WideString read GetState_SupplierSource;  // read-only
property SupportingDocumentId[i: Integer]: WideString read GetState_SupportingDocumentIdAt;  // read-only
property SupportingDocumentsIdsCount: Integer read GetState_SupportingDocumentsIdsCount;  // read-only
function GetState_ManufacturerName: WideString;
function GetState_ManufacturerPartNumber: WideString;
function GetState_PartId: WideString;
function GetState_ProviderGUID: WideString;
function GetState_ProviderName: WideString;
function GetState_RoHS: WideString;
function GetState_SupplierName: WideString;
function GetState_SupplierPartNumber: WideString;
function GetState_SupplierPartNumberAlias: WideString;
function GetState_SupplierSource: WideString;
function GetState_SupportingDocumentIdAt(i: Integer): WideString;
function GetState_SupportingDocumentsIdsCount: Integer;

## IStandardPaint
继承：IStandardPaint → IInterface ｜ 单元：InstrumentPanels ｜ 自有 1 个方法、0 个属性

procedure PaintOnPanel(APanel: TCustomInstrumentBackgroundPanel);

## IStatusBarManager
继承：IStatusBarManager → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 7 个方法、2 个属性

property MTPercentWeight: Double read GetMTPercentWeight write SetMTPercentWeight;
property State[Index: Integer]: WideString read GetState write SetState;
function GetMTPercentWeight: Double;
function GetState(Index: Integer): WideString;
function PercentStack_Pop: IPercentState;
procedure PercentStack_Push(const PercentState: IPercentState);
function PercentStack_Top: IPercentState;
procedure SetMTPercentWeight(MTWeight: Double);
procedure SetState(Index: Integer; const S: WideString);

## IStreamPersist
继承：IStreamPersist → IInterface ｜ 单元：System.Classes ｜ 自有 2 个方法、0 个属性

procedure LoadFromStream(Stream: TStream);
procedure SaveToStream(Stream: TStream);

## IString
继承：IString → IInterface ｜ 单元：RT_Workspace ｜ 自有 2 个方法、1 个属性

property Value: WideString read GetValue write SetValue;
function GetValue: WideString;
procedure SetValue(const AValue: WideString);

## IStrings
继承：IStrings → IInterface ｜ 单元：RT_CommonInterfaces ｜ 自有 0 个方法、0 个属性


## IStringsAdapter
继承：IStringsAdapter → IInterface ｜ 单元：System.Classes ｜ 自有 2 个方法、0 个属性

procedure ReferenceStrings(S: TStrings);
procedure ReleaseStrings;

## ISubDataSet
继承：ISubDataSet → IInterface ｜ 单元：Data.DB ｜ 自有 1 个方法、1 个属性

property SubDataSet: TDataSet read GetSubDataSet;  // read-only
function GetSubDataSet: TDataSet;

## ISubLibraryData
继承：ISubLibraryData → IInterface ｜ 单元：RT_IntegratedLibrary ｜ 自有 9 个方法、0 个属性

function FieldCount: Integer;
function FindComponentByGUID(const AGUID: WideString): ILibraryComponentData;
function First: ILibraryComponentData;
function GetField(const AIndex: Integer): WideString;
function GetKeyField(const AIndex: Integer): WideString;
function GUID: WideString;
function KeyFieldCount: Integer;
function Name: WideString;
function Next: ILibraryComponentData;

## ISubLibraryDataList
继承：ISubLibraryDataList → IInterfaceList → IInterface ｜ 单元：RT_IntegratedLibrary ｜ 自有 1 个方法、1 个属性

property Items[I: Integer]: ISubLibraryData read GetSubLibraryData;  // read-only
function GetSubLibraryData(I: Integer): ISubLibraryData;

## ISubNet
继承：ISubNet → IDMObject → IInterface ｜ 单元：RT_Workspace ｜ 自有 21 个方法、0 个属性

function DM_CrossSheetNodeCount: Integer;
function DM_CrossSheetNodes(Index: Integer): ISignalNode;
function DM_LineCount: Integer;
function DM_Lines(Index: Integer): ILine;
function DM_Net: INet;
function DM_NetLabelNodeCount: Integer;
function DM_NetLabelNodes(Index: Integer): ISignalNode;
function DM_NodeCount: Integer;
function DM_Nodes(Index: Integer): ISignalNode;
function DM_PinNodeCount: Integer;
function DM_PinNodes(Index: Integer): ISignalNode;
function DM_PortNodeCount: Integer;
function DM_PortNodes(Index: Integer): ISignalNode;
function DM_PowerObjectNodeCount: Integer;
function DM_PowerObjectNodes(Index: Integer): ISignalNode;
function DM_SheetEntryNodeCount: Integer;
function DM_SheetEntryNodes(Index: Integer): ISignalNode;
function DM_SignalCount: Integer;
function DM_SignalLinkCount: Integer;
function DM_SignalLinks(Index: Integer): ISignalLink;
function DM_Signals(Index: Integer): ISignal;

## ISupplier
继承：ISupplier → IInterface ｜ 单元：RT_Supplier ｜ 自有 23 个方法、5 个属性

property Enabled: LongBool read GetState_Enabled write SetState_Enabled;
property Hidden: LongBool read GetState_Hidden write SetState_Hidden;
property IsReadOnly: LongBool read GetState_IsReadOnly write SetState_IsReadOnly;
property Options: WideString read GetState_Options write SetState_Options;
property OrderPosition: Integer read GetState_OrderPosition write SetState_OrderPosition;
procedure BackgroundGetCategoryParameters(Category: ISupplierCategory; Handle: HWND);
procedure BackgroundSearchByKeyword(Keywords: WideString; RecordCount: Integer; StartRecord: Integer; SearchFilters: TSupplierSearchFilters; Category: ISupplierCategory; ParametricFilters: ISupplierParametricFilters; Handle: HWND);
procedure BackgroundSearchByManufacturerPartNumber(ManufacturerPartNumber: WideString; Handle: HWND);
procedure BackgroundSearchBySupplierPartNumber(SupplierPartNumber: WideString; SkipOptions: TSkipOptionSet; Handle: HWND);
function CreateSupplierCart: ISupplierCart;
function GetCategoryParameters(Category: ISupplierCategory): ISupplierCategoryParameters;
function GetOptionsPage: IOptionsPage;
function GetSearchUrl(const APartNumber: WideString): WideString;
function GetState_Enabled: LongBool;
function GetState_Hidden: LongBool;
function GetState_IsReadOnly: LongBool;
function GetState_Options: WideString;
function GetState_OrderPosition: Integer;
function SearchByKeyword(Keywords: WideString; RecordCount: Integer; StartRecord: Integer; SearchFilters: TSupplierSearchFilters; Category: ISupplierCategory; ParametricFilters: ISupplierParametricFilters): ISupplierSearchResults;
function SearchByManufacturerPartNumber(ManufacturerPartNumber: WideString): ISupplierSearchResults;
function SearchBySupplierPartNumber(SupplierPartNumber: WideString; SkipOptions: TSkipOptionSet): ISupplierSourceRelationship;
procedure SetState_Enabled(Value: LongBool);
procedure SetState_Hidden(Value: LongBool);
procedure SetState_IsReadOnly(Value: LongBool);
procedure SetState_Options(Value: WideString);
procedure SetState_OrderPosition(Value: Integer);
function SourceName: WideString;
function SupportedSearchFilters: TSupplierSearchFilters;

## ISupplier2
继承：ISupplier2 → IInterface ｜ 单元：RT_Supplier ｜ 自有 3 个方法、1 个属性

property SupplierAliases: ISupplierAliasesList read GetSupplierAliases;  // read-only
function GetPartNumberSuggestionList(const AKeyword: WideString): IStrings;
function GetSupplierAliases: ISupplierAliasesList;
function SearchByManufacturerPartNumber2(const ManufacturerPartNumber: WideString; IncludeData: TSupplierIncludeOptionSet): ISupplierSearchResults;

## ISupplierAggregator
继承：ISupplierAggregator → IInterface ｜ 单元：RT_Supplier ｜ 自有 2 个方法、0 个属性

function GetSubSupplierNameList: IStrings;
procedure SetActiveNativeSuppliers(SupplierNames: IStrings);

## ISupplierAliases
继承：ISupplierAliases → IInterface ｜ 单元：RT_Supplier ｜ 自有 2 个方法、2 个属性

property Aliases: IStrings read GetAliases;  // read-only
property SupplierName: WideString read GetSupplierName;  // read-only
function GetAliases: IStrings;
function GetSupplierName: WideString;

## ISupplierAliasesList
继承：ISupplierAliasesList → IInterfaceList → IInterface ｜ 单元：RT_Supplier ｜ 自有 1 个方法、1 个属性

property Items[I: Integer]: ISupplierAliases read GetAliases;  // read-only
function GetAliases(I: Integer): ISupplierAliases;

## ISupplierCart
继承：ISupplierCart → IInterface ｜ 单元：RT_Supplier ｜ 自有 1 个方法、0 个属性

function URL: WideString;

## ISupplierCategory
继承：ISupplierCategory → IInterface ｜ 单元：RT_Supplier ｜ 自有 8 个方法、3 个属性

property Category[I: Integer]: ISupplierCategory read GetState_Category;  // read-only
property CategoryByName[CategoryName: string]: ISupplierCategory read GetState_CategoryByName;  // read-only
property RecordCount: Integer read GetState_RecordCount write SetState_RecordCount;
procedure AddCategory(Category: ISupplierCategory);
function CategoryCount: Integer;
function CategoryName: WideString;
function GetState_Category(I: Integer): ISupplierCategory;
function GetState_CategoryByName(CategoryName: string): ISupplierCategory;
function GetState_RecordCount: Integer;
function I_ObjectAddress: Pointer;
procedure SetState_RecordCount(Value: Integer);

## ISupplierCategoryParameters
继承：ISupplierCategoryParameters → IInterfaceList → IInterface ｜ 单元：RT_Supplier ｜ 自有 1 个方法、1 个属性

property Items[I: Integer]: ISupplierParameterKind read GetParameterKind;  // read-only
function GetParameterKind(I: Integer): ISupplierParameterKind;

## ISupplierImportParameterPref
继承：ISupplierImportParameterPref → IInterface ｜ 单元：RT_SupplierManager ｜ 自有 5 个方法、5 个属性

property Exclude: Boolean read Get_Exclude;  // read-only
property ImportName: WideString read Get_ImportName;  // read-only
property ParameterName: WideString read Get_ParameterName;  // read-only
property Suffix: Boolean read Get_Suffix;  // read-only
property Visible: Boolean read Get_Visible;  // read-only
function Get_Exclude: Boolean;
function Get_ImportName: WideString;
function Get_ParameterName: WideString;
function Get_Suffix: Boolean;
function Get_Visible: Boolean;

## ISupplierItemPainter
继承：ISupplierItemPainter → IInterface ｜ 单元：RT_SupplierManager ｜ 自有 2 个方法、0 个属性

procedure Clear;
procedure Paint(SupplierSourceRelationship: ISupplierSourceRelationship);

## ISupplierLinkDocument
继承：ISupplierLinkDocument → IInterface ｜ 单元：RT_SupplierManager ｜ 自有 10 个方法、0 个属性

procedure AddSupplierDataSheetLinks(ASupplierDataSheets: IDragDropDataSheets);
procedure AddSupplierLinks(ASourceRelationships: IDragDropSupplierSourceRelationships);
procedure AddSupplierLinksAndParameters(ASourceRelationships: IDragDropSupplierSourceRelationships);
procedure AddSupplierParameters(ASupplierParameters: IDragDropParameters);
procedure GetState_AddSupplierDataSheetLinks(ASupplierDataSheets: IDragDropDataSheets; var Enabled: LongBool; var Checked: LongBool; var Visible: LongBool; var ACaption: WideString);
procedure GetState_AddSupplierLinks(ASourceRelationships: IDragDropSupplierSourceRelationships; var Enabled: LongBool; var Checked: LongBool; var Visible: LongBool; var ACaption: WideString);
procedure GetState_AddSupplierLinksAndParameters(ASourceRelationships: IDragDropSupplierSourceRelationships; var Enabled: LongBool; var Checked: LongBool; var Visible: LongBool; var ACaption: WideString);
procedure GetState_AddSupplierParameters(ASupplierParameters: IDragDropParameters; var Enabled: LongBool; var Checked: LongBool; var Visible: LongBool; var ACaption: WideString);
procedure GetState_ImportSupplierSourceRelationships(ASourceRelationships: IDragDropSupplierSourceRelationships; var Enabled: LongBool; var Checked: LongBool; var Visible: LongBool; var ACaption: WideString);
procedure ImportSupplierSourceRelationships(ASourceRelationships: IDragDropSupplierSourceRelationships);

## ISupplierLinksFrame
继承：ISupplierLinksFrame → IInterface ｜ 单元：RT_SupplierManager ｜ 自有 2 个方法、0 个属性

procedure SetListener(Listener: ISupplierLinksListener);
procedure SetState_Controls;

## ISupplierLinksListener
继承：ISupplierLinksListener → IInterface ｜ 单元：RT_SupplierManager ｜ 自有 1 个方法、0 个属性

procedure OnSourceRelationshipsChanged;

## ISupplierManager
继承：ISupplierManager → IInterface ｜ 单元：RT_SupplierManager ｜ 自有 18 个方法、4 个属性

property ImportParameterPreferences[Index: Integer]: ISupplierImportParameterPref read GetImportParameterPreferences;  // read-only
property ImportParameterPreferencesCount: Integer read GetImportParameterPreferencesCount;  // read-only
property SupplierSource[Index: Integer]: ISupplier read GetSupplierSource;  // read-only
property SupplierSourceCount: Integer read GetSupplierSourceCount;  // read-only
procedure BackgroundSearchByManufacturerPartNumber(ManufacturerPartNumber: WideString; Handle: HWND);
function BrowseSupplierLinks(SuggestedKeywords: WideString): ISupplierSourceRelationshipList;
function ConvertCurrency(const AAmount: Extended; const AFromCode: WideString; const AToCode: WideString): Extended;
function CreateSupplierItemPainter: ISupplierItemPainter;
function CreateSupplierLinksFrame(ASchComponent: ISch_Component): ISupplierLinksFrame;
function CreateSupplierSearchFrame: ISupplierSearchFrame;
function EditSupplierLinks(ASchComponent: ISch_Component): Boolean;
function EditSupplierLinksDB(Parameters: WideString; out OutParams: WideString): Boolean;
procedure FillCurrencyList(const AList: IStrings);
function FindImportParameterPreferences(ParameterName: WideString): ISupplierImportParameterPref;
function GetImportParameterPreferences(Index: Integer): ISupplierImportParameterPref;
function GetImportParameterPreferencesCount: Integer;
function GetSourceByName(const AName: WideString): ISupplier;
function GetSuggestedKeywordParameter(Index: Integer): WideString;
function GetSuggestedKeywordParameterCount: Integer;
function GetSupplierSource(Index: Integer): ISupplier;
function GetSupplierSourceBySubSupplierName(const AName: WideString): ISupplier;
function GetSupplierSourceCount: Integer;

## ISupplierParameterKind
继承：ISupplierParameterKind → IInterface ｜ 单元：RT_Supplier ｜ 自有 7 个方法、3 个属性

property ID: Integer read GetID write SetID;
property Name: WideString read GetName write SetName;
property Value[I: Integer]: ISupplierParameterValue read GetValue;  // read-only
procedure AddValue(Value: ISupplierParameterValue);
function GetID: Integer;
function GetName: WideString;
function GetValue(I: Integer): ISupplierParameterValue;
procedure SetID(ID: Integer);
procedure SetName(Name: WideString);
function ValueCount: Integer;

## ISupplierParameterValue
继承：ISupplierParameterValue → IInterface ｜ 单元：RT_Supplier ｜ 自有 4 个方法、2 个属性

property ID: Integer read GetID write SetID;
property Value: WideString read GetValue write SetValue;
function GetID: Integer;
function GetValue: WideString;
procedure SetID(ID: Integer);
procedure SetValue(Value: WideString);

## ISupplierParametricFilter
继承：ISupplierParametricFilter → IInterface ｜ 单元：RT_Supplier ｜ 自有 4 个方法、2 个属性

property ParameterKindID: Integer read GetParameterKindID write SetParameterKindID;
property ParameterValueID: Integer read GetParameterValueID write SetParameterValueID;
function GetParameterKindID: Integer;
function GetParameterValueID: Integer;
procedure SetParameterKindID(ID: Integer);
procedure SetParameterValueID(ID: Integer);

## ISupplierParametricFilters
继承：ISupplierParametricFilters → IInterfaceList → IInterface ｜ 单元：RT_Supplier ｜ 自有 1 个方法、1 个属性

property Items[I: Integer]: ISupplierParametricFilter read GetFilter;  // read-only
function GetFilter(I: Integer): ISupplierParametricFilter;

## ISupplierSearchError
继承：ISupplierSearchError → IInterface ｜ 单元：RT_Supplier ｜ 自有 2 个方法、0 个属性

function ErrorMessage: WideString;
function SupplierName: WideString;

## ISupplierSearchFrame
继承：ISupplierSearchFrame → IInterface ｜ 单元：RT_SupplierManager ｜ 自有 5 个方法、0 个属性

function CollectAllSourceRelationships: IInterfaceList;
function CollectSelectedSourceRelationships: IInterfaceList;
procedure PerformSearch(ASeachText: WideString);
function SearchKeyword: WideString;
procedure SetKeywords(AValue: WideString);

## ISupplierSearchResults
继承：ISupplierSearchResults → IInterfaceList → IInterface ｜ 单元：RT_Supplier ｜ 自有 5 个方法、3 个属性

property Items[I: Integer]: ISupplierSourceRelationship read GetSourceRelationship;  // read-only
property SearchError: ISupplierSearchError read GetSearchError write SetSearchError;
property SearchStatistics: ISupplierSearchStatistics read GetSearchStatistics write SetSearchStatistics;
function GetSearchError: ISupplierSearchError;
function GetSearchStatistics: ISupplierSearchStatistics;
function GetSourceRelationship(I: Integer): ISupplierSourceRelationship;
procedure SetSearchError(Value: ISupplierSearchError);
procedure SetSearchStatistics(Value: ISupplierSearchStatistics);

## ISupplierSearchStatistics
继承：ISupplierSearchStatistics → IInterface ｜ 单元：RT_Supplier ｜ 自有 11 个方法、5 个属性

property Category[I: Integer]: ISupplierCategory read GetState_Category;  // read-only
property CategoryByName[CategoryName: string]: ISupplierCategory read GetState_CategoryByName;  // read-only
property ElapsedTime: Integer read GetState_ElapsedTime write SetState_ElapsedTime;
property RecordCount: Integer read GetState_RecordCount write SetState_RecordCount;
property SearchResultCount: Integer read GetState_SearchResultCount write SetState_SearchResultCount;
procedure AddCategory(Category: ISupplierCategory);
function CategoryCount: Integer;
function GetState_Category(I: Integer): ISupplierCategory;
function GetState_CategoryByName(CategoryName: string): ISupplierCategory;
function GetState_ElapsedTime: Integer;
function GetState_RecordCount: Integer;
function GetState_SearchResultCount: Integer;
procedure SetState_ElapsedTime(Value: Integer);
procedure SetState_RecordCount(Value: Integer);
procedure SetState_SearchResultCount(Value: Integer);
function SupplierName: WideString;

## ISupplierSourceRelationship
继承：ISupplierSourceRelationship → ISourceRelationship → IInterface ｜ 单元：RT_Supplier ｜ 自有 16 个方法、15 个属性

property AvailabilityCount: Integer read GetState_AvailabilityCount;  // read-only
property AvailabilityLeadTime[I: Integer]: WideString read GetState_AvailabilityLeadTime;  // read-only
property AvailabilityQuantity[I: Integer]: Integer read GetState_AvailabilityQuantity;  // read-only
property BreakQuantity[I: Integer]: Integer read GetState_BreakQuantity;  // read-only
property Category: WideString read GetState_Category;  // read-only
property Currency: WideString read GetState_Currency;  // read-only
property Description: WideString read GetState_Description;  // read-only
property Parameter[I: Integer]: IItemParameter read GetState_ParameterAt;  // read-only
property ParameterByName[Name: WideString]: IItemParameter read GetState_ParameterByName;  // read-only
property ParametersCount: Integer read GetState_ParametersCount;  // read-only
property ProductPhotoURL: WideString read GetState_ProductPhotoURL;  // read-only
property QuantityInStock: Integer read GetState_QuantityInStock;  // read-only
property UnitPrice[I: Integer]: WideString read GetState_UnitPrice;  // read-only
property UnitPriceCount: Integer read GetState_UnitPriceCount;  // read-only
property UnitPriceForQuantity[Quantity: Integer]: WideString read GetState_UnitPriceForQuantity;  // read-only
function GetState_AvailabilityCount: Integer;
function GetState_AvailabilityLeadTime(I: Integer): WideString;
function GetState_AvailabilityQuantity(I: Integer): Integer;
function GetState_BreakQuantity(I: Integer): Integer;
function GetState_Category: WideString;
function GetState_Currency: WideString;
function GetState_Description: WideString;
function GetState_ParameterAt(I: Integer): IItemParameter;
function GetState_ParameterByName(Name: WideString): IItemParameter;
function GetState_ParametersCount: Integer;
function GetState_ProductPhotoURL: WideString;
function GetState_QuantityInStock: Integer;
function GetState_UnitPrice(I: Integer): WideString;
function GetState_UnitPriceCount: Integer;
function GetState_UnitPriceForQuantity(Quantity: Integer): WideString;
function I_ObjectAddress: Pointer;

## ISupplierSourceRelationship2
继承：ISupplierSourceRelationship2 → IInterface ｜ 单元：RT_Supplier ｜ 自有 1 个方法、1 个属性

property LastUpdated: WideString read GetState_LastUpdated;  // read-only
function GetState_LastUpdated: WideString;

## ISupplierSourceRelationship3
继承：ISupplierSourceRelationship3 → IInterface ｜ 单元：RT_Supplier ｜ 自有 5 个方法、5 个属性

property LastUpdatedAt: TDateTime read GetState_GetLastUpdatedAt;  // read-only
property LifeCycleStatus: WideString read GetState_LifeCycleStatus;  // read-only
property LifeCycleStatusName: WideString read GetState_LifeCycleStatusName;  // read-only
property ManufacturerAliases: IStrings read GetState_ManufacturerAliases;  // read-only
property SupplierURL: WideString read GetState_SupplierURL;  // read-only
function GetState_GetLastUpdatedAt: TDateTime;
function GetState_LifeCycleStatus: WideString;
function GetState_LifeCycleStatusName: WideString;
function GetState_ManufacturerAliases: IStrings;
function GetState_SupplierURL: WideString;

## ISupplierSourceRelationshipError
继承：ISupplierSourceRelationshipError → ISupplierSourceRelationship → ISourceRelationship → IInterface ｜ 单元：RT_Supplier ｜ 自有 1 个方法、1 个属性

property ErrorCode: Integer read GetState_ErrorCode;  // read-only
function GetState_ErrorCode: Integer;

## ISupplierSourceRelationshipList
继承：ISupplierSourceRelationshipList → IInterfaceList → IInterface ｜ 单元：RT_SupplierManager ｜ 自有 1 个方法、1 个属性

property Items[I: Integer]: ISupplierSourceRelationship read GetSupplierSourceRelationship;  // read-only
function GetSupplierSourceRelationship(I: Integer): ISupplierSourceRelationship;

## ISupportExternalPaint
继承：ISupportExternalPaint → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 0 个方法、0 个属性


## ISupportService
继承：ISupportService → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 1 个方法、0 个属性

function SupportsService(aServiceName: WideString): Boolean;

## ISymbolGenerator
继承：ISymbolGenerator → IInterface ｜ 单元：RT_Workspace ｜ 自有 4 个方法、0 个属性

procedure DM_AddParameter(Name: WideString; Value: WideString);
procedure DM_ClearParameters;
procedure DM_GenerateComponent;
procedure DM_GenerateComponentFromUser;

## ISystemDesignServerDocument
继承：ISystemDesignServerDocument → IInterface ｜ 单元：Rt_SystemDesign.Interfaces ｜ 自有 1 个方法、0 个属性

function GetData: ISdDocument;

## ISystemDesignServerModule
继承：ISystemDesignServerModule → IInterface ｜ 单元：Rt_SystemDesign.Interfaces ｜ 自有 3 个方法、0 个属性

function GetDocumentByPath(const Path: WideString): ISystemDesignServerDocument;
function GetDocumentDataByDocumentId(Id: Integer): ISdDocument;
function GetDocumentDataByPath(const Path: WideString): ISdDocument;

## ISystemNotification
继承：ISystemNotification → INotification → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 1 个方法、1 个属性

property Code: Integer read GetCode;  // read-only
function GetCode: Integer;

## ITableLink
继承：ITableLink → IInterface ｜ 单元：RT_Workspace ｜ 自有 3 个方法、0 个属性

function FieldLinkCount: Integer;
function FieldLinks(Index: Integer): IFieldLink;
function GetTableName: WideString;

## ITargetCore
继承：ITargetCore → ICustomCore → IInterface ｜ 单元：Rt_NexusDevices ｜ 自有 21 个方法、13 个属性

property Clock_Count: Integer read GetClock_Count;  // read-only
property Clock_Enabled[Clock: Char]: Boolean read GetClock_Enabled;  // read-only
property Clock_Index[C: Char]: WideString read GetClock_Index;  // read-only
property Clock_InputFrequency: Double read GetClock_InputFrequency;  // read-only
property Clock_Magnitude[Clock: Char]: Double read GetClock_Magnitude;  // read-only
property Clock_Operation[Clock: Char]: TClockOperationKind read GetClock_Operation;  // read-only
property ComponentName: WideString read GetComponentName;  // read-only
property Endianness: TEndianness read GetEndianness;  // read-only
property Filename: WideString read GetFilename write SetFileName;
property Parameters: WideString read GetParameters;  // read-only
property RWBehavior: TRWBehavior read GetRWBehavior write SetRWBehavior;
property VendorParam_Double[Name: WideString]: Double read GetVendorParam_Double write SetVendorParam_Double;
property VendorParam_String[Name: WideString]: WideString read GetVendorParam_String write SetVendorParam_String;
procedure AddError(S: WideString);
procedure AddInfo(S: WideString);
procedure AddWarning(S: WideString);
procedure DependenciesFile_Add(Value: WideString);
function GetClock_Count: Integer;
function GetClock_Enabled(Clock: Char): Boolean;
function GetClock_Index(C: Char): WideString;
function GetClock_InputFrequency: Double;
function GetClock_Magnitude(Clock: Char): Double;
function GetClock_Operation(Clock: Char): TClockOperationKind;
function GetComponentName: WideString;
function GetEndianness: TEndianness;
function GetFilename: WideString;
function GetParameters: WideString;
function GetRWBehavior: TRWBehavior;
function GetVendorParam_Double(Name: WideString): Double;
function GetVendorParam_String(Name: WideString): WideString;
procedure SetFileName(Value: WideString);
procedure SetRWBehavior(Value: TRWBehavior);
procedure SetVendorParam_Double(Name: WideString; Value: Double);
procedure SetVendorParam_String(Name: WideString; Value: WideString);

## ITargetCoreGenerator
继承：ITargetCoreGenerator → IInterface ｜ 单元：Rt_NexusDevices ｜ 自有 1 个方法、0 个属性

procedure WriteNetlistBody(const ATextFile: ITextFile; const ATargetCore: ITargetCore);

## ITemplateInfo
继承：ITemplateInfo → IInterface ｜ 单元：RT_Workspace ｜ 自有 17 个方法、0 个属性

function Description: WideString;
function DisplayName: WideString;
function FolderGUID: WideString;
function FullFileName: WideString;
function IsApplicable: Boolean;
function ItemGUID: WideString;
function ItemHRID: WideString;
function ItemRevisionGUID: WideString;
function ItemRevisionHRID: WideString;
function ItemRevisionStateGUID: WideString;
function Kind: TTemplateKind;
function Link: WideString;
function Name: WideString;
function Note: WideString;
function Source: TTemplateSource;
function SubKind: WideString;
function VaultGUID: WideString;

## ITemplateManager
继承：ITemplateManager → IInterface ｜ 单元：RT_Workspace ｜ 自有 6 个方法、0 个属性

function CreateLocalTemplate(AKind: TTemplateKind; const AFullFileName: WideString): ITemplateInfo;
function CreateServerTemplate(AKind: TTemplateKind; const AVaultGUID: WideString; const AItemGUID: WideString; const AItemRevisionGUID: WideString; const AItemRevisionHRID: WideString): ITemplateInfo;
function GetOrCreateTemplateFolder(const AVault: IEDMS_Vault; const AContentTypeGUID: WideString): IULB_Folder;
function GetServerTemplate(const AVaultGUID: WideString; const AItemRevisionGUID: WideString): ITemplateInfo;
function GetTemplateList(ASource: TTemplateSource; AKind: TTemplateKind; AForceRefresh: Boolean): IInterfaces;
function GetTemplateListExt(ASource: TTemplateSource; AKinds: TTemplateKindSet; AForceRefresh: Boolean): IInterfaces;

## ITemplateManagerFactory
继承：ITemplateManagerFactory → IInterface ｜ 单元：RT_Workspace ｜ 自有 1 个方法、0 个属性

function CreateTemplateManager: ITemplateManager;

## ITemplateManagerOptions
继承：ITemplateManagerOptions → IInterface ｜ 单元：RT_Workspace ｜ 自有 1 个方法、0 个属性

function GetOptionsPage: IOptionsPage;

## ITerminalInstrument
继承：ITerminalInstrument → IScriptedInstrument → IInterface ｜ 单元：RT_Terminal ｜ 自有 5 个方法、0 个属性

procedure Clear;
function GetContent: string;
procedure PutChar(AValue: Char);
procedure PutString(const AValue: string);
procedure SaveContent(const AFileName: string);

## ITerminalInstrumentManager
继承：ITerminalInstrumentManager → IScriptedInstrumentManager → IInterface ｜ 单元：RT_Terminal ｜ 自有 4 个方法、0 个属性

function GetInstrument(Index: Integer): ITerminalInstrument;
function GetInstrumentByDesignator(const ADesignator: WideString): ITerminalInstrument;
function GetInstrumentByJtagIndex(AJtagIndex: Integer): ITerminalInstrument;
function GetInstrumentCount: Integer;

## ITestDongles
继承：ITestDongles → IJtagPort → IInterface ｜ 单元：Rt_NexusDevices ｜ 自有 0 个方法、0 个属性


## ITextFile
继承：ITextFile → IInterface ｜ 单元：Rt_NexusDevices ｜ 自有 1 个方法、0 个属性

procedure Writeln(const AString: WideString);

## ITextFrame
继承：ITextFrame → IDMObject → IInterface ｜ 单元：RT_Workspace ｜ 自有 3 个方法、0 个属性

function DM_Text: WideString;
function DM_TextReferenceItem(AIndex: Integer): ITextReferenceItem;
function DM_TextReferenceItemsCount: Integer;

## ITextReferenceItem
继承：ITextReferenceItem → IInterface ｜ 单元：RT_Workspace ｜ 自有 8 个方法、0 个属性

function GetState_CrossProbe: WideString;
function GetState_Error: Boolean;
function GetState_IsText: Boolean;
function GetState_ObjectId: TWorkspaceObjectId;
function GetState_Rect: IDispatch;
function GetState_SchHandle: WideString;
function GetState_Text: WideString;
function GetState_TextPos: IDispatch;

## ITimerHandler
继承：ITimerHandler → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 1 个方法、0 个属性

procedure HandleTimerEvent(ID: Cardinal);

## ITimerManager
继承：ITimerManager → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 4 个方法、0 个属性

function GetHandlerEnabled(ID: Cardinal): Boolean;
procedure RemoveHandler(ID: Cardinal);
procedure SetGlobalEnabled(AEnabled: Boolean);
procedure SetHandlerEnabled(ID: Cardinal; AEnabled: Boolean);

## IToDoDocument
继承：IToDoDocument → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 8 个方法、0 个属性

function ToDo_GetCount: Integer;
function ToDo_GetItem(Index: Integer): WideString;
function ToDo_ItemActivate(const AnItem: WideString): LongBool;
function ToDo_ItemCanEdit: LongBool;
function ToDo_ItemEdit(const AnItem: WideString): LongBool;
function ToDo_ItemUpdate(const OldItem: WideString; const NewItem: WideString): LongBool;
function ToDo_ScanBegin: LongBool;
function ToDo_ScanEnd: LongBool;

## IToDoManager
继承：IToDoManager → IInterface ｜ 单元：RT_Workspace ｜ 自有 5 个方法、2 个属性

property Count: Integer read GetCount;  // read-only
property Item[Index: Integer]: WideString read GetItem;  // read-only
function AddItem(const AnItem: WideString): LongBool;
procedure Clear;
function GetCount: Integer;
function GetItem(Index: Integer): WideString;
function RemoveItem(const AnItem: WideString): LongBool;

## ITranscriptMessage
继承：ITranscriptMessage → IInterface ｜ 单元：Rt_VHDL ｜ 自有 5 个方法、0 个属性

function GetCode: PWideChar;
function GetDescription: PWideChar;
function GetFileName: PWideChar;
function GetKind: TMessageKind;
function GetLine: Integer;

## ITranslationManager
继承：ITranslationManager → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 3 个方法、0 个属性

function GetTranslatedProperty(const ComponentName: WideString; const PropName: WideString; out OutValue: WideString): LongBool;
function HasTranslationData: LongBool;
procedure SetComponentToTranslate(const ComponentName: WideString);

## ITypedNotification
继承：ITypedNotification → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 3 个方法、3 个属性

property NotificationCode: Integer read GetNotificationCode;  // read-only
property NotificationData: IInterface read GetNotificationData;  // read-only
property NotificationType: WideString read GetNotificationType;  // read-only
function GetNotificationCode: Integer;
function GetNotificationData: IInterface;
function GetNotificationType: WideString;

## IU3DModelPage
继承：IU3DModelPage → IInterface ｜ 单元：RT_Workspace ｜ 自有 4 个方法、0 个属性

function Count: Integer;
function Data: Pointer;
function Flags: TU3DFlags;
function Size: Integer;

## IUIDialogManager
继承：IUIDialogManager → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 0 个方法、0 个属性


## IUndoRedoSupport
继承：IUndoRedoSupport → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 2 个方法、0 个属性

function GetCommandName_Redo: WideString;
function GetCommandName_Undo: WideString;

## IUpdateParameterOptions
继承：IUpdateParameterOptions → IInterface ｜ 单元：RT_Workspace ｜ 自有 20 个方法、9 个属性

property AddParameters: TAddRemoveParameterOption read GetAddParameters write SetAddParameters;
property IsUpdateParameterMode: Boolean read GetUpdateParameterMode write SetUpdateParameterMode;
property OverridePreserveParameters: Boolean read GetOverridePreserveParameters write SetOverridePreserveParameters;
property PreserveAllParameters: Boolean read GetPreserveAllParameters write SetPreserveAllParameters;
property PreserveParameterLocations: Boolean read GetPreserveParameterLocations write SetPreserveParameterLocations;
property PreserveParameterVisibility: Boolean read GetPreserveParameterVisibility write SetPreserveParameterVisibility;
property PreserveVirtualParameters: Boolean read GetPreserveVirtualParameters write SetPreserveVirtualParameters;
property RemoveParameters: TAddRemoveParameterOption read GetRemoveParameters write SetRemoveParameters;
property UpdateParameters: IStrings read GetUpdateParameters write SetUpdateParameters;
function GetAddParameters: TAddRemoveParameterOption;
function GetOverridePreserveParameters: Boolean;
function GetPreserveAllParameters: Boolean;
function GetPreserveParameterLocations: Boolean;
function GetPreserveParameterVisibility: Boolean;
function GetPreserveVirtualParameters: Boolean;
function GetRemoveParameters: TAddRemoveParameterOption;
function GetUpdateParameterMode: Boolean;
function GetUpdateParameters: IStrings;
function IsParameterExist(Name: WideString): Boolean;
procedure SetAddParameters(Val: TAddRemoveParameterOption);
procedure SetOverridePreserveParameters(Val: Boolean);
procedure SetPreserveAllParameters(Val: Boolean);
procedure SetPreserveParameterLocations(Val: Boolean);
procedure SetPreserveParameterVisibility(Val: Boolean);
procedure SetPreserveVirtualParameters(Val: Boolean);
procedure SetRemoveParameters(Val: TAddRemoveParameterOption);
procedure SetState_Default;
procedure SetUpdateParameterMode(Val: Boolean);
procedure SetUpdateParameters(Val: IStrings);

## IUpdatesManager
继承：IUpdatesManager → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 4 个方法、0 个属性

function GetCurrentSchemaFileName: WideString;
function GetInstalledSchemaFileName: WideString;
procedure SetPendingUpdateFileName(const UpdateExecutableFileName: WideString);
procedure SetReconfigurationRequired(const NewSchemaFileName: WideString);

## IVCLComObject
继承：IVCLComObject → IInterface ｜ 单元：System.Classes ｜ 自有 4 个方法、0 个属性

procedure FreeOnRelease;
function GetTypeInfo(Index: Integer; LocaleID: Integer; out TypeInfo): HRESULT;
function GetTypeInfoCount(out Count: Integer): HRESULT;
function SafeCallException(ExceptObject: TObject; ExceptAddr: Pointer): HRESULT;

## IVCLFrameForm
继承：IVCLFrameForm → IOleInPlaceFrame ｜ 单元：Vcl.OleCtnrs ｜ 自有 4 个方法、0 个属性

procedure AddContainer(Instance: TOleContainer);
procedure ClearBorderSpace;
function Form: TCustomForm;
procedure RemoveContainer(Instance: TOleContainer);

## IVCSNotification
继承：IVCSNotification → INotification → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 5 个方法、5 个属性

property Code: Integer read GetCode;  // read-only
property FileNames: WideString read GetFileNames;  // read-only
property FileNamesExt: WideString read GetFileNamesExt;  // read-only
property VCSProjectGUID: WideString read GetVCSProjectGUID;  // read-only
property VcsRevisionString: WideString read GetVcsRevisionString;  // read-only
function GetCode: Integer;
function GetFileNames: WideString;
function GetFileNamesExt: WideString;
function GetVCSProjectGUID: WideString;
function GetVcsRevisionString: WideString;

## IVHDLCompiler
继承：IVHDLCompiler → IInterface ｜ 单元：Rt_VHDL ｜ 自有 13 个方法、0 个属性

procedure Abort;
procedure AddLibrary(AValue: PWideChar);
function GetPercentage: Integer;
function GetStatus: TVHDLStatus;
function GetTranscript: IVHDLTranscript;
procedure SetLoadDir(AValue: PWideChar);
procedure SetOutputFile(AValue: PWideChar);
procedure SetSmartCompile(AValue: Boolean);
procedure SetSourceFile(AValue: PWideChar);
procedure SetSourceStream(AValue: IStream);
procedure SetVHDL93(AValue: Boolean);
procedure SetWorkDir(AValue: PWideChar);
procedure Start;

## IVHDLEntity
继承：IVHDLEntity → IDMObject → IInterface ｜ 单元：RT_Workspace ｜ 自有 1 个方法、0 个属性

function DM_Name: WideString;

## IVHDLPreferences
继承：IVHDLPreferences → IInterface ｜ 单元：Rt_VHDLSynthesis ｜ 自有 1 个方法、0 个属性

function GetPreference(Name: WideString): WideString;

## IVHDLSynthesizer
继承：IVHDLSynthesizer → IInterface ｜ 单元：Rt_VHDLSynthesis ｜ 自有 16 个方法、0 个属性

function VHDL_GetCoreFileExtension(Project: IProject; AConfig: WideString): WideString;
function VHDL_GetCurrentSynthesizer(Project: IProject): WideString;
function VHDL_GetOutputFileExtension(Project: IProject; AConfig: WideString): WideString;
function VHDL_GetOutputPath(Project: IProject; AConfig: WideString): WideString;
function VHDL_GetReportFile(Project: IProject; AConfig: WideString): WideString;
function VHDL_GetRequiredCapabilities(Project: IProject; ACapabilities: ICapabilityList): LongBool;
function VHDL_GetSynthesizer(const ATool: WideString): IAbstractSynthesizer;
function VHDL_GetToolchainRootPath(Project: IProject): WideString;
function VHDL_GetTopLevelExtension(Project: IProject; AConfig: WideString): WideString;
function VHDL_PublishProject(Project: IProject): LongBool;
procedure VHDL_SetCurrentSynthesizer(Project: IProject; ASynthesizer: WideString);
procedure VHDL_SetOptions(Project: IProject; Parameters: WideString);
procedure VHDL_SynthesizeAbort;
function VHDL_SynthesizeProject(Project: IProject; AConfig: WideString): LongBool;
function VHDL_SynthesizeProjectAllConfigurations(Project: IProject): LongBool;
function VHDL_SynthesizeProjectEx(Project: IProject; AConfig: WideString; Parameters: WideString): LongBool;

## IVHDLTranscript
继承：IVHDLTranscript → IInterface ｜ 单元：Rt_VHDL ｜ 自有 5 个方法、0 个属性

function GetErrorCount: Integer;
function GetMessage(Index: Integer): ITranscriptMessage;
function GetMessageCount: Integer;
function GetWarningCount: Integer;
procedure SetReportLevel(AValue: Integer);

## IVHDLibDocument
继承：IVHDLibDocument → IHDLLibDocument → IInterface ｜ 单元：Rt_VHDL ｜ 自有 0 个方法、0 个属性


## IValidationSupport
继承：IValidationSupport → IInterface ｜ 单元：RT_Workspace ｜ 自有 1 个方法、0 个属性

procedure Validate(AFileLessViolationKinds: TFileLessViolationKinds; AResult: IInterfaceList);

## IVarInstanceReference
继承：IVarInstanceReference → IInterface ｜ 单元：System.Variants ｜ 自有 1 个方法、0 个属性

function GetInstance(const V: IDispatch): TObject;

## IVarInvokeable
继承：IVarInvokeable → IInterface ｜ 单元：System.Variants ｜ 自有 4 个方法、0 个属性

function DoFunction(const Dest: IDispatch; const V: IDispatch; const Name: string; const Arguments: TVarDataArray): Boolean;
function DoProcedure(const V: IDispatch; const Name: string; const Arguments: TVarDataArray): Boolean;
function GetProperty(const Dest: IDispatch; const V: IDispatch; const Name: string): Boolean;
function SetProperty(const V: IDispatch; const Name: string; const Value: IDispatch): Boolean;

## IVarStreamable
继承：IVarStreamable → IInterface ｜ 单元：System.Classes ｜ 自有 2 个方法、0 个属性

procedure StreamIn(const Dest: IDispatch; const Stream: TStream);
procedure StreamOut(const Source: IDispatch; const Stream: TStream);

## IVariantGroup
继承：IVariantGroup → IInterface ｜ 单元：RT_Workspace ｜ 自有 15 个方法、0 个属性

function DM_AddOption(const AName: WideString): IVariantGroupOption;
function DM_FindOptionByName(const AName: WideString): IVariantGroupOption;
function DM_FindOptionByUniqueId(const AUniqueId: WideString): IVariantGroupOption;
function DM_Name: WideString;
function DM_Option(Index: Integer): IVariantGroupOption;
function DM_OptionCount: Integer;
function DM_ReferenceId: WideString;
function DM_ReferenceType: TVaraintGroupSource;
procedure DM_RemoveOption(Index: Integer);
procedure DM_RemoveOptionByName(const AName: WideString);
procedure DM_RemoveOptionByUniqueId(const AUniqueId: WideString);
procedure DM_SetName(const Name: WideString);
procedure DM_SetReferenceId(const Id: WideString);
procedure DM_SetReferenceType(const RefType: TVaraintGroupSource);
function DM_UniqueId: WideString;

## IVariantGroupOption
继承：IVariantGroupOption → IInterface ｜ 单元：RT_Workspace ｜ 自有 9 个方法、0 个属性

function DM_AddComponentVariation: IComponentVariation;
function DM_FindComponentVariationByUniqueId(const AUniqueId: WideString): IComponentVariation;
function DM_Name: WideString;
procedure DM_RemoveComponentVariation(Index: Integer);
procedure DM_RemoveComponentVariationByUniqueId(const AUniqueId: WideString);
procedure DM_SetName(const Value: WideString);
function DM_UniqueId: WideString;
function DM_VariationCount: Integer;
function DM_Variations(Index: Integer): IComponentVariation;

## IVariantManager
继承：IVariantManager → IInterface ｜ 单元：RT_Workspace ｜ 自有 15 个方法、0 个属性

function DM_AddGroup: IVariantGroup;
function DM_AddVariant: IProjectVariant;
function DM_CurrentProjectVariant: IProjectVariant;
function DM_FindGroupByName(const AName: WideString): IVariantGroup;
function DM_FindGroupByUniqueId(const AUniqueId: WideString): IVariantGroup;
function DM_FindProjectVariant(const ADescription: WideString): IProjectVariant;
function DM_Group(AIndex: Integer): IVariantGroup;
function DM_GroupCount: Integer;
procedure DM_RemoveGroup(AIndex: Integer);
procedure DM_RemoveGroupByName(const AName: WideString);
procedure DM_RemoveGroupByUniqueId(const AUniqueId: WideString);
procedure DM_RemoveVariant(AIndex: Integer);
procedure DM_SetCurrentProjectVariant(const AProjVariant: IProjectVariant);
function DM_Variant(AIndex: Integer): IProjectVariant;
function DM_VariantCount: Integer;

## IVariantOption
继承：IVariantOption → IInterface ｜ 单元：RT_Workspace ｜ 自有 38 个方法、0 个属性

function DM_PCBGraphics: TVariantGraphics;
function DM_PCBGraphicsColor: TColor;
function DM_PCBShowComponent: Boolean;
function DM_PCBStrikeThroughDesignator: Boolean;
function DM_PCBText: WideString;
function DM_PCBTextColor: TColor;
function DM_PCBTextHeight: Integer;
function DM_PCBTextStrokeFontName: WideString;
function DM_PCBTextStrokeWidth: Integer;
function DM_PCBTextTTBold: Boolean;
function DM_PCBTextTTFontName: WideString;
function DM_PCBTextTTInverted: Boolean;
function DM_PCBTextTTInvertedBorder: Integer;
function DM_PCBTextTTItalic: Boolean;
function DM_PCBTextUseTTFont: Boolean;
function DM_PCBUseGraphics: Boolean;
function DM_PCBUseText: Boolean;
procedure DM_SaveOptions;
function DM_SCHGraphics: TVariantGraphics;
function DM_SCHParamBold: Boolean;
function DM_SCHParamColor: TColor;
function DM_SCHParamFontName: WideString;
function DM_SCHParamItalic: Boolean;
function DM_SCHParamModifyText: Boolean;
function DM_SCHParamSize: Integer;
function DM_SCHParamStrikeOut: Boolean;
function DM_SCHParamSuffix: WideString;
function DM_SCHParamUnderline: Boolean;
function DM_SCHText: WideString;
function DM_SCHTextBold: Boolean;
function DM_SCHTextColor: TColor;
function DM_SCHTextFontName: WideString;
function DM_SCHTextItalic: Boolean;
function DM_SCHTextSize: Integer;
function DM_SCHTextStrikeOut: Boolean;
function DM_SCHTextUnderline: Boolean;
function DM_SCHUseGraphics: Boolean;
function DM_SCHUseText: Boolean;

## IVariedValueItem
继承：IVariedValueItem → IInterface ｜ 单元：RT_Workspace ｜ 自有 2 个方法、0 个属性

function DM_VariantName: WideString;
function DM_VariedValue: WideString;

## IVaultConfiguration
继承：IVaultConfiguration → IConfiguration → IBaseConfiguration → IDMObject → IInterface ｜ 单元：RT_Workspace ｜ 自有 22 个方法、0 个属性

procedure DM_AddOutputJobDocument(APath: WideString);
function DM_CheckForErrors: WideString;
function DM_CurrentRevision: IULB_ItemRevision;
function DM_GenerateRawBOM: Boolean;
function DM_GetCurrentRevisionGUID: WideString;
function DM_GetReleaseItemGUID: WideString;
function DM_OutputJobDocumentCount: Integer;
function DM_OutputJobDocumentFilePath(Index: Integer): WideString;
function DM_OutputJobDocumentReferenceCount: Integer;
function DM_OutputJobDocumentReferenceCreateItemRevisionLink(AIndex: Integer; AVault: IEDMS_Vault; AParentRevision: IULB_ItemRevision): IULB_ItemRevisionLink;
function DM_OutputJobDocumentReferenceFileDir(Index: Integer): WideString;
function DM_OutputJobDocumentReferenceFileName(Index: Integer): WideString;
procedure DM_OutputJobDocumentReferencesAddDocumentReference(ADocument: IDocument);
procedure DM_OutputJobDocumentReferencesClear;
procedure DM_OutputJobDocumentReferencesCopyFrom(AConfiguration: IVaultConfiguration);
procedure DM_OutputJobDocumentReferencesRemoveByIndex(Index: Integer);
function DM_ReleaseItem: IULB_Item;
procedure DM_ResetCache;
procedure DM_SetCurrentRevisionGUID(Value: WideString);
procedure DM_SetReleaseItemGUID(Value: WideString);
procedure DM_SetVariant(Value: WideString);
function DM_Variant: WideString;

## IVaultConfigurationReleaseManager
继承：IVaultConfigurationReleaseManager → IConfigurationReleaseManager → IInterface ｜ 单元：RT_Workspace ｜ 自有 18 个方法、0 个属性

function DM_CanRelease(FindDependencies: Boolean): Boolean;
function DM_CurrentProject: IProject;
function DM_GetInReleaseMode: Boolean;
procedure DM_Reload(const AProject: IProject; const AConfiguration: IVaultConfiguration);
procedure DM_SetInReleaseMode(Value: Boolean);
procedure DM_VaultCommitRelease;
function DM_VaultCommitSuccess: Boolean;
function DM_VaultGetCurrent: IEDMS_Vault;
function DM_VaultHasReleased: Boolean;
function DM_VaultIsReleasing: Boolean;
procedure DM_VCSCheckOutSnapshot(IncludeAllDependancies: Boolean);
function DM_VCSCheckoutSucess: Boolean;
procedure DM_VCSCommitSnapshot;
function DM_VCSCommitSuccess: Boolean;
function DM_VCSHasReleased: Boolean;
function DM_VCSProjectStatus(AFilesToCommit: IVcsFileNames; AFilesToUpdate: IVcsFileNames): Integer;
procedure DM_VCSShowDialog(AFilesToCommit: IVcsFileNames; AFilesToUpdate: IVcsFileNames);
procedure DM_WaitForDocumentsCommited;

## IVaultFileLessDocumentNotification
继承：IVaultFileLessDocumentNotification → INotification → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 8 个方法、8 个属性

property Code: Integer read GetCode;  // read-only
property DisplayName: WideString read GetDisplayName;  // read-only
property FileName: WideString read GetFileName;  // read-only
property Locked: Boolean read GetLocked;  // read-only
property RevisionGUID: WideString read GetRevisionGUID;  // read-only
property RevisionHRID: WideString read GetRevisionHRID;  // read-only
property VaultGuid: WideString read GetVaultGuid;  // read-only
property VaultHRID: WideString read GetVaultHRID;  // read-only
function GetCode: Integer;
function GetDisplayName: WideString;
function GetFileName: WideString;
function GetLocked: Boolean;
function GetRevisionGUID: WideString;
function GetRevisionHRID: WideString;
function GetVaultGuid: WideString;
function GetVaultHRID: WideString;

## IVaultFileLessReleaseNotification
继承：IVaultFileLessReleaseNotification → INotification → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 5 个方法、0 个属性

function GetFileName: WideString;
function GetOriginalRevisionGUID: WideString;
function GetOriginalVaultGUID: WideString;
function GetTargetRevisionGUID: WideString;
function GetTargetVaultGUID: WideString;

## IVaultPropertiesSupportDocument
继承：IVaultPropertiesSupportDocument → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 2 个方法、0 个属性

function GetHRid: WideString;
procedure SetHRid(const Value: WideString);

## IVerilogLibDocument
继承：IVerilogLibDocument → IHDLLibDocument → IInterface ｜ 单元：Rt_VHDL ｜ 自有 0 个方法、0 个属性


## IVersionHelper
继承：IVersionHelper → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 1 个方法、0 个属性

function StripReleaseFromProductName(const ProductName: string): string;

## IViewNotification
继承：IViewNotification → INotification → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 1 个方法、1 个属性

property Code: Integer read GetCode;  // read-only
function GetCode: Integer;

## IViewWithNotificationFilter
继承：IViewWithNotificationFilter → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 1 个方法、0 个属性

procedure GetNotificationHandlers(ACodeList: INotificationCodeList);

## IViolation
继承：IViolation → IDMObject → IInterface ｜ 单元：RT_Workspace ｜ 自有 12 个方法、0 个属性

procedure DM_AddRelatedObject(AnObject: IDMObject);
function DM_AddToViolationManager: Boolean;
function DM_CompilationStage: TCompilationStage;
function DM_ConnectionCode1: TConnectionCode;
function DM_ConnectionCode2: TConnectionCode;
function DM_DescriptorString: WideString;
function DM_DetailString: WideString;
function DM_ErrorKind: TErrorKind;
function DM_ErrorLevel: TErrorLevel;
function DM_IsSuppressed: Boolean;
function DM_RelatedObjectCount: Integer;
function DM_RelatedObjects(Index: Integer): IDMObject;

## IVirtualParameter
继承：IVirtualParameter → IInterface ｜ 单元：RT_Workspace ｜ 自有 4 个方法、2 个属性

property BackgroundColor: TColor read GetState_BackgroundColor write SetState_BackgroundColor;
property Text: WideString read GetState_Text write SetState_Text;
function GetState_BackgroundColor: TColor;
function GetState_Text: WideString;
procedure SetState_BackgroundColor(AColor: TColor);
procedure SetState_Text(AText: WideString);

## IVirtualParametersManager
继承：IVirtualParametersManager → IInterface ｜ 单元：RT_Workspace ｜ 自有 10 个方法、0 个属性

procedure AddComponentVirtualParameter(PhysicalName: WideString; Text: WideString; Color: TColor);
procedure AddNetVirtualParameter(PhysicalName: WideString; Text: WideString; Color: TColor);
procedure AddPinVirtualParameter(PhysicalName: WideString; Text: WideString; Color: TColor);
procedure ClearVirtualParameters;
procedure SetComponentVirtualParameter(PhysicalName: WideString; Text: WideString; Color: TColor; IsHidden: Boolean);
procedure SetNetVirtualParameter(PhysicalName: WideString; Text: WideString; Color: TColor; IsHidden: Boolean);
procedure SetPinVirtualParameter(PhysicalName: WideString; Text: WideString; Color: TColor; IsHidden: Boolean);
procedure ShowComponentsVirtualParameters(Show: Boolean; PhysicalName: WideString);
procedure ShowNetsVirtualParameters(Show: Boolean; PhysicalName: WideString);
procedure ShowPinsVirtualParameters(Show: Boolean; PhysicalName: WideString);

## IWSM_DialogManager
继承：IWSM_DialogManager → IWSM_DialogManagerEntry → IInterface ｜ 单元：RT_Workspace ｜ 自有 0 个方法、0 个属性


## IWSM_DialogManagerEntry
继承：IWSM_DialogManagerEntry → IInterface ｜ 单元：RT_Workspace ｜ 自有 2 个方法、0 个属性

procedure HandleNotification(const ANotification: INotification);
function ShowLibraryDialog: Boolean;

## IWSM_OutputJobDocument
继承：IWSM_OutputJobDocument → IInterface ｜ 单元：RT_Workspace ｜ 自有 14 个方法、8 个属性

property MediumOutputer[AOutputMedium: IOutputMedium; i: Integer]: IOutputer read GetState_MediumOutputer;  // read-only
property MediumOutputersCount[AOutputMedium: IOutputMedium]: Integer read GetState_MediumOutputersCount;  // read-only
property Outputer[AIndex: Integer]: IOutputer read GetState_Outputer;  // read-only
property OutputerCount: Integer read GetState_OutputerCount;  // read-only
property OutputMedium[AIndex: Integer]: IOutputMedium read GetState_OutputMedium;  // read-only
property OutputMediumCount: Integer read GetState_OutputMediumCount;  // read-only
property VariantName: WideString read GetState_VariantName write SetState_VariantName;
property VariantScope: TOutputJobVariantScope read GetState_VariantScope write SetState_VariantScope;
function BeginModifyOutputer(const AOutputer: IOutputer): Boolean;
function CreateOutputer(const AOutputCategoryName: WideString; const APredefinedOutputName: WideString; const AOutputerName: WideString): IOutputer;
procedure EndModifyOutputer;
function GetState_MediumOutputer(AOutputMedium: IOutputMedium; i: Integer): IOutputer;
function GetState_MediumOutputersCount(AOutputMedium: IOutputMedium): Integer;
function GetState_Outputer(AIndex: Integer): IOutputer;
function GetState_OutputerCount: Integer;
function GetState_OutputMedium(AIndex: Integer): IOutputMedium;
function GetState_OutputMediumCount: Integer;
function GetState_VariantName: WideString;
function GetState_VariantScope: TOutputJobVariantScope;
function RemoveOutputer(const AOutputer: IOutputer): Boolean;
procedure SetState_VariantName(AName: WideString);
procedure SetState_VariantScope(AValue: TOutputJobVariantScope);

## IWatch
继承：IWatch → IInterface ｜ 单元：RT_Debugger ｜ 自有 17 个方法、7 个属性

property Enable: Boolean read GetEnable write SetEnable;
property Expression: WideString read GetExpression write SetExpression;
property FullPath: WideString read GetFullPath write SetFullPath;
property LineNumber: Integer read GetLineNumber write SetLineNumber;
property Valid: Boolean read GetValid;  // read-only
property Value: WideString read GetValue write SetValue;
property WType: WideString read GetType write SetType;
procedure AttachMonitor(aMonitor: IWatchMonitor);
procedure DetachMonitor(aMonitor: IWatchMonitor);
function GetEnable: Boolean;
function GetExpression: WideString;
function GetFullPath: WideString;
function GetLineNumber: Integer;
function GetType: WideString;
function GetValid: Boolean;
function GetValue: WideString;
procedure SetEnable(aEnabled: Boolean);
procedure SetExpression(anExpression: WideString);
procedure SetFullPath(aFullPath: WideString);
procedure SetLineNumber(aLineNumber: Integer);
procedure SetType(aType: WideString);
procedure SetValue(aValue: WideString);
procedure UpdateState;
procedure UpdateValue;

## IWatchMonitor
继承：IWatchMonitor → IInterface ｜ 单元：RT_Debugger ｜ 自有 4 个方法、0 个属性

procedure BeginUpdate;
procedure EndUpdate;
procedure UpdateState(AWatch: IWatch);
procedure UpdateValue(AWatch: IWatch);

## IWaveSimNotification
继承：IWaveSimNotification → INotification → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 2 个方法、2 个属性

property Code: Integer read GetCode;  // read-only
property UniqueId: Integer read GetUniqueId;  // read-only
function GetCode: Integer;
function GetUniqueId: Integer;

## IWebBrowser
继承：IWebBrowser → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 2 个方法、0 个属性

function GetElementAtributeValue(const AElementId: WideString; const AAtrribute: WideString): WideString;
procedure SetElementAttributeValue(const AElementId: WideString; const AAtrribute: WideString; const AValue: WideString);

## IWebBrowserNotification
继承：IWebBrowserNotification → INotification → IInterface ｜ 单元：RT_ClientServerInterface ｜ 自有 4 个方法、4 个属性

property Code: Integer read GetCode;  // read-only
property IsUpdateRequired: Boolean read GetIsUpdateRequired;  // read-only
property SessionID: WideString read GetSessionID;  // read-only
property Url: WideString read GetURL;  // read-only
function GetCode: Integer;
function GetIsUpdateRequired: Boolean;
function GetSessionID: WideString;
function GetURL: WideString;

## IWebDAVPublisher
继承：IWebDAVPublisher → IInterface ｜ 单元：RT_Workspace ｜ 自有 7 个方法、0 个属性

procedure Configure(AUrl: WideString; AUsername: WideString; APasswd: WideString);
function ConfirmOverwrite(AFileNames: WideString): Boolean;
function ConnectionParamsOK: Boolean;
function GetIndexURL: WideString;
function GetLastErrorMessage: WideString;
function Login: Boolean;
function UploadFile(AFileName: WideString): Boolean;

## IWorkspace
继承：IWorkspace → IDMObject → IInterface ｜ 单元：RT_Workspace ｜ 自有 81 个方法、0 个属性

procedure DM_AddDocumentToActiveProject(DocumentPath: WideString);
function DM_ChangeManager: IChangeManager;
function DM_CheckoutManagedProject(AManagedProjectGUID: WideString; AAssemblyRevisionGUID: WideString; out AManagedProjectPath: WideString): Boolean;
procedure DM_ClearOutputLines;
procedure DM_CloseProject(ProjectPath: WideString);
function DM_CreateHarnessDefinitionList_DeviceSheets(AFolderPath: WideString; ARecursive: Boolean): IHarnessDefinitionList;
function DM_CreateNewDocument(ADocKind: WideString): WideString;
function DM_CreateNewDocumentWithoutUsingTemplate(const ADocKind: WideString): WideString;
procedure DM_CreateProjectPackage(const AProjectPath: WideString; const AConfig: IProjectPackagerConfig);
procedure DM_DestroyHarnessDefinitionList(AHarnessDefinitionList: IHarnessDefinitionList);
procedure DM_DisplayNavigationHint(AViewHandle: NativeUInt; X: Integer; Y: Integer; const ADMObject: IDMObject; AViewNavigatedHandle: NativeUInt);
procedure DM_FileOwnership_BulkWarnEnd(AWarningLevel: TFileOwnershipWarningLevel);
function DM_FileOwnership_BulkWarnRegister(AFileName: string): Boolean;
procedure DM_FileOwnership_BulkWarnStart;
function DM_FocusedDocument: IDocument;
function DM_FocusedProject: IProject;
function DM_FreeDocumentsProject: IProject;
function DM_GenerateUniqueID: WideString;
function DM_GetAssemblyRevisions(AManagedProjectGUID: WideString): IInterfaceList;
function DM_GetCurrentProject: IProject;
function DM_GetDefaultPcbType: WideString;
function DM_GetDialogManager: IWSM_DialogManager;
function DM_GetDifferenceTypeDescription(DifferenceKind: TDifferenceKind): WideString;
function DM_GetDocumentFromPath(DocumentPath: WideString): IDocument;
function DM_GetHarnessCoreAccess: IHarnessCoreAccess;
function DM_GetItemManagerFactory: IItemManagerFactory;
function DM_GetOutputCharCount: Integer;
function DM_GetOutputHandler(const AFormat: WideString; out ADocKind: WideString; out AServerName: WideString; out ACommand: WideString): Boolean;
function DM_GetOutputJobDocumentByPath(APath: WideString): IWSM_OutputJobDocument;
function DM_GetOutputLine(Index: Integer): WideString;
function DM_GetOutputLineCount: Integer;
function DM_GetProjectDialogsFactory: IProjectDialogsFactory;
function DM_GetProjectFromPath(ProjectPath: WideString): IProject;
function DM_GetRecentFilesManager: IRecentFilesManager;
function DM_GetRecoveryInterval: Integer;
function DM_GetRecoveryIsEnabled: Boolean;
function DM_GetReleaseManager: IReleaseManager;
function DM_GetSchCompilator(LoadAdvSch: Boolean): ISchCompilator;
function DM_GetTemplateManager: ITemplateManager;
function DM_GetUdmClientStack: IClientsStack;
function DM_GetVaultReleaseManager(AProject: IProject; AConfiguration: IVaultConfiguration): IVaultConfigurationReleaseManager;
function DM_GetWorkspaceDocument: Pointer;
function DM_GetWorkspaceManagerUIFactory: IWorkspaceManagerUIFactory;
procedure DM_HideProject(ProjectPath: WideString);
function DM_ImageIndexForDocumentKind(ADocumentKind: WideString): Integer;
function DM_InstalledLibraries(Index: Integer): IDocument;
function DM_InstalledLibraryCount: Integer;
function DM_IsReferencedAsDeviceSheet(const AFilePath: WideString): Boolean;
function DM_IsSchCompilatorLoaded: Boolean;
function DM_LoadProjectHidden(const ProjectPath: WideString): IProject;
function DM_LocalHistoryManager: ILocalHistoryManager;
function DM_MessagesManager: IDXPMessagesManager;
procedure DM_Navigation_OpenHostDocuments(const AProject: IProject; const AObjectsList: IInterfaceList; ADocumentOpenMode: TDocumentOpenMode);
function DM_NavigationZoomPrecision: Integer;
procedure DM_NotifyObjectNavigated(ACode: Integer; const ADMObject: IDMObject; const ANavigationActionSet: TNavigationActionSet);
procedure DM_NotifyObjectsNavigated(ACode: Integer; const ASourceDMObject: IDMObject; const ANavigationActionSet: TNavigationActionSet; const ADMObjects: IInterfaceList);
function DM_OpenProject(ProjectPath: WideString; const Show: Boolean): IProject;
function DM_OptionsStorage: IOptionsStorage;
function DM_OutputManager: IOutputManager;
function DM_PCBReleaseViewDocument: IReleaseViewDocument;
function DM_Preferences: IWorkspacePreferences;
function DM_ProjectCount: Integer;
function DM_Projects(Index: Integer): IProject;
function DM_PromptForDefaultPcbType(var PcbType: WideString): Boolean;
procedure DM_RegisterDependentDocuments(const ASourceDocKind: WideString; const ADependentExtension: WideString);
function DM_RunOpenDocumentDialog(const Caption: WideString; AllowMultiSelect: LongBool; var Path: WideString; FilterKind: TFilterKind; FilterIndex: Integer; out DocumentPaths: IStrings): LongBool;
function DM_SaveSingleDocument(const ADocument: IServerDocument; const AFileFormat: WideString): Boolean;
function DM_SelectManagedProject(out AManagedProjectGUID: WideString; out AManagedProjectName: WideString; out AManagedProjectType: WideString; out AAssemblyRevisions: IInterfaceList): Boolean;
procedure DM_SetNavigationZoomPrecision(ZoomPrecision: Integer);
procedure DM_SetRecoveryParameters(IsEnabled: Boolean; Interval: Integer);
procedure DM_SetRightClickCompStructure(const AProjectPath: WideString; const ALibReference: WideString; const AUniqueId: WideString);
procedure DM_SetRightClickProject(const AProject: IProject);
procedure DM_ShowMessageView;
procedure DM_ShowProject(ProjectPath: WideString);
procedure DM_ShowToDoList;
procedure DM_SuppressUpdateRecentListAdding(const AValue: Boolean);
procedure DM_UpdateOutputWindow;
function DM_ViolationTypeDescription(ErrorKind: TErrorKind): WideString;
function DM_ViolationTypeGroup(ErrorKind: TErrorKind): TErrorGroup;
function DM_WorkspaceFileName: WideString;
function DM_WorkspaceFullPath: WideString;

## IWorkspaceHelper
继承：IWorkspaceHelper → IInterface ｜ 单元：RT_Workspace ｜ 自有 10 个方法、0 个属性

function AddProjectFileToVcsIfRepositoryExists(const AProjectPath: WideString): Boolean;
function CheckProjectLifecycleDefinition: Boolean;
function CheckProjectRevisionScheme: Boolean;
function ChooseDirectoryDialog(const ACaption: WideString; var ADirectory: WideString): Boolean;
function CoerceProjectWorkingCopyDir(const AManagedProjectGUID: WideString; const AProjectName: WideString; const ADocumentKind: WideString; const AWorkingCopyDir: WideString): WideString;
function GetTemplateManager: ITemplateManager;
function IsForbiddenName(const AName: WideString; out AMessage: WideString): Boolean;
function IsManagedProjectCreationTakenOver: Boolean;
function LoadManagedProjectLocalPath(const AManagedProjectGUID: WideString): WideString;
function TryGetSeparateVCSProjectPath(const AProjectPath: WideString; out ARepositoryName: WideString; out ARepositoryRootPath: WideString; out AProjectRelativePath: WideString): Boolean;

## IWorkspaceManagerUIFactory
继承：IWorkspaceManagerUIFactory → IInterface ｜ 单元：RT_Workspace ｜ 自有 1 个方法、0 个属性

function CreateEditComponentVariantDialog: IEditComponentVariantDialog;

## IWorkspacePreferences
继承：IWorkspacePreferences → IInterface ｜ 单元：RT_Workspace ｜ 自有 49 个方法、30 个属性

property CrossSelectComponents: Boolean read GetCrossSelectComponents;  // read-only
property CrossSelectFocusDocuments: Boolean read GetCrossSelectFocusDocuments write SetCrossSelectFocusDocuments;
property CrossSelectMasking: Boolean read GetCrossSelectMasking;  // read-only
property CrossSelectMode: Boolean read GetCrossSelectMode write SetCrossSelectMode;
property CrossSelectNets: Boolean read GetCrossSelectNets;  // read-only
property CrossSelectPins: Boolean read GetCrossSelectPins;  // read-only
property CrossSelectReposition: Boolean read GetCrossSelectReposition write SetCrossSelectReposition;
property CrossSelectZooming: Boolean read GetCrossSelectZooming;  // read-only
property DefaultDocumentPath: WideString read GetDefaultDocumentPath;  // read-only
property DefaultLibraryPath: WideString read GetDefaultLibraryPath;  // read-only
property DefaultTemplateFile[const ADocKind: WideString]: WideString read GetDefaultTemplateFile write SetDefaultTemplateFile;
property DefaultTemplateFile_NotExpanded[const ADocKind: WideString]: WideString read GetDefaultTemplateFile_NotExpanded write SetDefaultTemplateFile_NotExpanded;
property DefaultTemplateSource[const ADocKind: WideString]: WideString read GetDefaultTemplateSource;  // read-only
property FileOwnership_Enabled: Boolean read GetFileOwnership_Enabled write SetFileOwnership_Enabled;
property FileOwnership_EnabledOutputDirectory: Boolean read GetFileOwnership_EnabledOutputDirectory write SetFileOwnership_EnabledOutputDirectory;
property FileOwnership_WarningLevelOpen: TFileOwnershipWarningLevel read GetFileOwnership_WarningLevelOpen write SetFileOwnership_WarningLevelOpen;
property FileOwnership_WarningLevelSave: TFileOwnershipWarningLevel read GetFileOwnership_WarningLevelSave write SetFileOwnership_WarningLevelSave;
property HighlightConnectedPowerParts: Boolean read GetHighlightConnectedPowerParts;  // read-only
property HighlightMethodSet: THighlightMethodSet read GetHighlightMethodSet;  // read-only
property ObjectsToDisplay: TWorkspaceObjectIdSet read GetObjectsToDisplay;  // read-only
property ReleasesTemporaryFolder: WideString read GetReleasesTemporaryFolder write SetReleasesTemporaryFolder;
property ReleasesTemporaryFolderCleanUp: Boolean read GetReleasesTemporaryFolderCleanUp write SetReleasesTemporaryFolderCleanUp;
property TemplatePath_NotExpanded: WideString read GetTemplatePath_NotExpanded write SetTemplatePath_NotExpanded;
property TemplateSource: TTemplateSource read GetTemplateSource write SetTemplateSource;
property TemporaryReleaseBOMFolder: WideString read GetTemporaryReleaseBOMFolder;  // read-only
property TemporaryReleaseCheckoutFolder: WideString read GetTemporaryReleaseCheckoutFolder;  // read-only
property TemporaryReleaseOutputFolder: WideString read GetTemporaryReleaseOutputFolder;  // read-only
property TemporaryReleaseSnapshotFolder: WideString read GetTemporaryReleaseSnapshotFolder;  // read-only
property UseLeftRightSelection: Boolean read GetUseLeftRightSelection write SetUseLeftRightSelection;
property VariantOption: IVariantOption read GetVariantOption;  // read-only
procedure ClearDefaultTemplateFiles;
function GetCrossSelectComponents: Boolean;
function GetCrossSelectFocusDocuments: Boolean;
function GetCrossSelectMasking: Boolean;
function GetCrossSelectMode: Boolean;
function GetCrossSelectNets: Boolean;
function GetCrossSelectPins: Boolean;
function GetCrossSelectReposition: Boolean;
function GetCrossSelectZooming: Boolean;
function GetCrossSelectZoomOption: TCrossSelectZoomOption;
function GetDefaultDocumentPath: WideString;
function GetDefaultLibraryPath: WideString;
function GetDefaultRecoveryPath: WideString;
function GetDefaultTemplateFile(const ADocKind: WideString): WideString;
function GetDefaultTemplateFile_NotExpanded(const ADocKind: WideString): WideString;
function GetDefaultTemplateInfo(const ADocKind: WideString; out AFileName: WideString; out AVault: IEDMS_Vault; out ARevision: IULB_ItemRevision): Boolean;
function GetDefaultTemplateSource(const ADocKind: WideString): WideString;
function GetFileOwnership_Enabled: Boolean;
function GetFileOwnership_EnabledOutputDirectory: Boolean;
function GetFileOwnership_WarningLevelOpen: TFileOwnershipWarningLevel;
function GetFileOwnership_WarningLevelSave: TFileOwnershipWarningLevel;
function GetHighlightConnectedPowerParts: Boolean;
function GetHighlightMethodSet: THighlightMethodSet;
function GetObjectsToDisplay: TWorkspaceObjectIdSet;
function GetReleasesTemporaryFolder: WideString;
function GetReleasesTemporaryFolderCleanUp: Boolean;
function GetTemplatePath_NotExpanded: WideString;
function GetTemplatePath_Sch: WideString;
function GetTemplateSource: TTemplateSource;
function GetTemporaryReleaseBOMFolder: WideString;
function GetTemporaryReleaseCheckoutFolder: WideString;
function GetTemporaryReleaseOutputFolder: WideString;
function GetTemporaryReleaseSnapshotFolder: WideString;
function GetUseLeftRightSelection: Boolean;
function GetVariantOption: IVariantOption;
procedure SetCrossSelectFocusDocuments(Value: Boolean);
procedure SetCrossSelectMode(Value: Boolean);
procedure SetCrossSelectReposition(Value: Boolean);
procedure SetDefaultTemplateFile(const ADocKind: WideString; const AFileName: WideString);
procedure SetDefaultTemplateFile_NotExpanded(const ADocKind: WideString; const APath: WideString);
procedure SetFileOwnership_Enabled(AValue: Boolean);
procedure SetFileOwnership_EnabledOutputDirectory(AValue: Boolean);
procedure SetFileOwnership_WarningLevelOpen(AValue: TFileOwnershipWarningLevel);
procedure SetFileOwnership_WarningLevelSave(AValue: TFileOwnershipWarningLevel);
procedure SetReleasesTemporaryFolder(const AValue: WideString);
procedure SetReleasesTemporaryFolderCleanUp(const AValue: Boolean);
procedure SetTemplatePath_NotExpanded(const AValue: WideString);
procedure SetTemplateSource(AValue: TTemplateSource);
procedure SetUseLeftRightSelection(Value: Boolean);

## IWorkspaceUtils
继承：IWorkspaceUtils → IInterface ｜ 单元：RT_Workspace ｜ 自有 4 个方法、0 个属性

function ErrorLevelToString(const AErroLevel: TErrorLevel): WideString;
function GetConnectionCodeByShortString(const AShortString: WideString): TConnectionCode;
function GetConnectionNameByShortString(const AShortString: WideString): WideString;
function GetErrorKindFromString(const aString: WideString): TErrorKind;

## IWrapper
继承：IWrapper → IDMObject → IInterface ｜ 单元：RT_Workspace ｜ 自有 2 个方法、0 个属性

function DM_GroupedSchObject(i: Integer): IWrapper;
function DM_GroupedSchObjects_Count: Integer;

## IXPPanelCollapse
继承：IXPPanelCollapse → IInterface ｜ 单元：XPExtCtrls ｜ 自有 3 个方法、1 个属性

property Expanded: Boolean read GetExpanded write SetExpanded;
function GetExpanded: Boolean;
procedure SetExpanded(Value: Boolean);
procedure SwitchHeight(Value: Boolean);

