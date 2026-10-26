# 常量和枚举

来源：Altium Designer 23.1.1.15 的 `System\ScriptingSystem.dll`（脚本引擎的注册表，2026-10-25 提取）。由 `scripts/gen_docs.py` 生成，不要手改。

值都是脚本里实际拿到的值。集合常量写成元素序号的集合（如 `[1..32]`）。

## 同名常量冲突

下面这些名字被不同单元注册了不同的值，脚本里只能拿到第一个值（AD23 实测）。不能按枚举定义推断它传给某个函数或属性后的效果：PCB 的 `TUnit` 定义是 eImperial = 1，但实测 `CoordUnitToString(C, eImperial)`（脚本里 eImperial = 0）输出的是 mil，结果正确。用到这些名字时，先在 AD 里用小脚本确认效果。

| 常量 | 脚本里的值 | 来自 | 其他单元里的值 |
|---|---|---|---|
| `arDefault` | 2 | TAutoRefreshFlag (Data.DB) | 4（TListArrangement (Vcl.ComCtrls)） |
| `btNext` | 0 | TUDBtnType (Vcl.ComCtrls) | 3（TMPBtnType (Vcl.MPlayer)） |
| `btPrev` | 1 | TUDBtnType (Vcl.ComCtrls) | 4（TMPBtnType (Vcl.MPlayer)） |
| `dsNormal` | 0 | TBandDrawingStyle (Vcl.ExtCtrls)、TTBDrawingStyle (Vcl.ComCtrls) | 2（TDrawingStyle (Vcl.ImgList)） |
| `eBottom` | 1 | — | 0（TSmartUnionAlignmentType (RT_PCB)） |
| `eBottomAlign` | 2 | — | 5（无枚举） |
| `eIgnore` | 8 | TOrcadFootPrint (Rt_Schematic) | 2（TTestpointValid (RT_PCB)） |
| `eImperial` | 0 | TUnitSystem (Rt_Schematic) | 1（TUnit (RT_PCB)） |
| `eLeftAlign` | 1 | THorizontalAlign (Rt_Schematic) | 2（无枚举） |
| `eMetric` | 1 | TUnitSystem (Rt_Schematic) | 0（TUnit (RT_PCB)） |
| `eRightAlign` | 2 | THorizontalAlign (Rt_Schematic) | 3（无枚举） |
| `eTop` | 3 | — | 1（TSmartUnionAlignmentType (RT_PCB)） |
| `eTopAlign` | 1 | — | 4（无枚举） |
| `iaLeft` | 1 | TIconArrangement (Vcl.ComCtrls) | 0（TImageAlignment (Vcl.StdCtrls)、TcxImageAlign (cxImageComboBox)） |
| `iaTop` | 0 | TIconArrangement (Vcl.ComCtrls) | 2（TImageAlignment (Vcl.StdCtrls)） |
| `Numbers` | [48..57] | — | [0..9]（无枚举） |
| `soHorizontal` | 0 | TPageScrollerOrientation (Vcl.ComCtrls) | 1（TSizingOrientation (Vcl.ToolWin)） |
| `soVertical` | 1 | TPageScrollerOrientation (Vcl.ComCtrls) | 2（TSizingOrientation (Vcl.ToolWin)） |
| `ssHorizontal` | 10 | — | 1（TScrollStyle (System.UITypes)） |

## 枚举类型

只列出至少有一个元素作为常量注册了的枚举。元素后面标 `// 脚本里不可用` 的没注册成常量；标 `// 脚本里是 N` 的名字被别的单元占用了（见上表）。

### EnumDesignStateComplete (Rt_ActelFPGA)

eSETUP_DESIGN = 0
eDEVICE_SELECTION = 1
eNETLIST_IMPORT = 2
eCOMPILE = 3
eLAYOUT = 4
eBACKANNOTATE = 5
ePROGRAMMING_FILE = 6

### IDENTIFIEROption (Data.DBCommon)

idKeepQuotes = 0
idMixCase = 1
idMakeLowerCase = 2
idMakeUpperCase = 3

### T3DModelType (RT_PCB)

e3DModelType_Extruded = 0
e3DModelType_Generic = 1
e3DModelType_Cylinder = 2
e3DModelType_Sphere = 3

### TAccordionMode (RT_PCB)

eAccordionMode_Accordion = 0
eAccordionMode_Trombone = 1
eAccordionMode_Sawtooth = 2
eAccordionMode_Root = 3

### TAccordionStyle (RT_PCB)

asMittered45DegreeLines = 0
asMitteredArcs = 1
asRounded = 2

### TActiveFormBorderStyle (Vcl.Forms)

afbNone = 0
afbSingle = 1
afbSunken = 2
afbRaised = 3

### TAddRemoveParameterOption (RT_Workspace)

eAddRemoveYes = 0
eAddRemoveNo = 1
eAddRemoveBlankConditional = 2

### TADOLockType (Data.Win.ADODB)

ltUnspecified = 0
ltReadOnly = 1
ltPessimistic = 2
ltOptimistic = 3
ltBatchOptimistic = 4

### TAdvancedRouteMode (RT_PCB)

eARIgnoreObstacle = 0
eARWalkAroundObstacle = 1
eARPushObstacle = 2
eARHugAndPushObstacle = 3
eARStopAtFirstObstacle = 4
eARAutoRouteCurrentLayer = 5
eARAutoRouteMultiLayer = 6

### TAdvPCBFileFormatVersion (RT_PCB)

ePCBFileFormatNone = 0
eAdvPCBFormat_Binary_V3 = 1
eAdvPCBFormat_Library_V3 = 2
eAdvPCBFormat_ASCII_V3 = 3
eAdvPCBFormat_Binary_V4 = 4
eAdvPCBFormat_Library_V4 = 5
eAdvPCBFormat_ASCII_V4 = 6
eAdvPCBFormat_Binary_V5 = 7
eAdvPCBFormat_Library_V5 = 8
eAdvPCBFormat_ASCII_V5 = 9
eAdvPCBFormat_Binary_V6 = 10
eAdvPCBFormat_Library_V6 = 11
eAdvPCBFormat_ASCII_V6 = 12
eAdvPCBFormat_Binary_V6_CS = 13
eAdvPCBFormat_Binary_V6_CM = 14
eAdvPCBFormat_Binary_V6_PCBWorks = 15
eAdvPCBFormat_PadViaLibrary_V6 = 16

### TAffectRecords (Data.Win.ADODB)

arCurrent = 0
arFiltered = 1
arAll = 2
arAllChapters = 3

### TAlign (Vcl.Controls)

alNone = 0
alTop = 1
alBottom = 2
alLeft = 3
alRight = 4
alClient = 5
alCustom = 6

### TAlignment (System.Classes)

taLeftJustify = 0
taRightJustify = 1
taCenter = 2

### TAlphaFormat (Vcl.Graphics)

afIgnored = 0
afDefined = 1
afPremultiplied = 2

### TAnchorKind (System.UITypes)

akLeft = 0
akTop = 1
akRight = 2
akBottom = 3

### TAppearanceChange (XPExtCtrls)

acProperty = 0
acState = 1
acSize = 2
acPosition = 3

### TArithmeticException (System.Math)

exInvalidOp = 0
exDenormalized = 1
exZeroDivide = 2
exOverflow = 3
exUnderflow = 4
exPrecision = 5

### TArrowKind (Rt_Schematic)

eArrowKind_RectAndTri = 0
eArrowKind_Triangle = 1
eArrowKind_Arrow = 2
eArrowKind_ArrowTail = 3

### TAttributeType (Vcl.ComCtrls)

atSelected = 0
atDefaultText = 1

### TAutoActivate (Vcl.OleCtnrs)

aaManual = 0
aaGetFocus = 1
aaDoubleClick = 2

### TAutoCompleteOption (Vcl.ComCtrls)

acoAutoSuggest = 0
acoAutoAppend = 1
acoSearch = 2
acoFilterPrefixes = 3
acoUseTab = 4
acoUpDownKeyDropsList = 5
acoRtlReading = 6

### TAutoPanMode (RT_PCB)

eNoAutoPan = 0
eReCentre = 1
eFixedJump = 2
eShiftAccellerator = 3
eShiftDeccellerator = 4
eBallistic = 5
eAdaptive = 6

### TAutoPanStyle (Rt_Schematic)

eAutoPanOff = 0
eAutoPanFixedJump = 1
eAutoPanReCenter = 2

### TAutoPanUnit (RT_PCB)

eAutoPanByMils = 0
eAutoPanByPixels = 1

### TAutoRefreshFlag (Data.DB)

arNone = 0
arAutoInc = 1
arDefault = 2

### TAvoidObstacleMode (RT_PCB)

avIgnore = 0
avAvoidSnap = 1
avAvoid = 2

### TBalloonFlags (Vcl.ExtCtrls)

bfNone = 0
bfInfo = 1
bfWarning = 2
bfError = 3

### TBalloonHintStyle (Vcl.Controls)

bhsStandard = 0
bhsBalloon = 1

### TBandDrawingStyle (Vcl.ExtCtrls)

dsNormal = 0
dsGradient = 1

### TBandPaintOption (Vcl.ExtCtrls)

bpoGrabber = 0
bpoFrame = 1
bpoGradient = 2
bpoRoundRect = 3

### TBarcodeKind (Pcbtypes)

eBarcode39 = 0
eBarCode128 = 1

### TBarcodeKind (RT_PCB)

eBarcode39 = 0
eBarCode128 = 1

### TBarcodeRenderMode (Pcbtypes)

eRender_ByMinWidth = 0
eRender_ByFullWidth = 1

### TBarcodeRenderMode (RT_PCB)

eRender_ByMinWidth = 0
eRender_ByFullWidth = 1

### TBaud (RT_PCB)

eBaud110 = 0
eBaud150 = 1
eBaud300 = 2
eBaud600 = 3
eBaud1200 = 4
eBaud2400 = 5
eBaud4800 = 6
eBaud9600 = 7
eBaud19200 = 8

### TBevelCut (Vcl.Controls)

bvNone = 0
bvLowered = 1
bvRaised = 2
bvSpace = 3

### TBevelEdge (Vcl.Controls)

beLeft = 0
beTop = 1
beRight = 2
beBottom = 3

### TBevelKind (Vcl.Controls)

bkNone = 0
bkTile = 1
bkSoft = 2
bkFlat = 3

### TBevelShape (Vcl.ExtCtrls)

bsBox = 0
bsFrame = 1
bsTopLine = 2
bsBottomLine = 3
bsLeftLine = 4
bsRightLine = 5
bsSpacer = 6

### TBevelStyle (Vcl.ExtCtrls)

bsLowered = 0
bsRaised = 1

### TBGAFanoutDirection (RT_PCB)

eBGAFanoutDirection_Out = 0
eBGAFanoutDirection_NE = 1
eBGAFanoutDirection_SE = 2
eBGAFanoutDirection_SW = 3
eBGAFanoutDirection_NW = 4
eBGAFanoutDirection_In = 5

### TBGAFanoutViaMode (RT_PCB)

eBGAFanoutVia_Closest = 0
eBGAFanoutVia_Centered = 1

### TBiDiMode (System.Classes)

bdLeftToRight = 0
bdRightToLeft = 1
bdRightToLeftNoAlign = 2
bdRightToLeftReadingOnly = 3

### TBitBtnKind (Vcl.Buttons)

bkCustom = 0
bkOK = 1
bkCancel = 2
bkHelp = 3
bkYes = 4
bkNo = 5
bkClose = 6
bkAbort = 7
bkRetry = 8
bkIgnore = 9
bkAll = 10

### TBitmapHandleType (Vcl.Graphics)

bmDIB = 0
bmDDB = 1

### TBitValue (Rt_NexusDevices)

eBit_Undefined = 0
eBit_0 = 1
eBit_1 = 2
eBit_X = 3

### TBlobStreamMode (Data.DB)

bmRead = 0
bmWrite = 1
bmReadWrite = 2

### TBoard3DModelExportComponentOptions (RT_PCB)

eBoard3DModelExportComponentOptions_AllComponents = 0
eBoard3DModelExportComponentOptions_SelectedComponents = 1

### TBoard3DModelExportComponentSuffix (RT_PCB)

eBoard3DModelExportComponentSuffix_None = 0
eBoard3DModelExportComponentSuffix_BoardName = 1
eBoard3DModelExportComponentSuffix_Custom = 2
eBoard3DModelExportComponentSuffix_UniqueID = 3

### TBoard3DModelExportCopperOptions (RT_PCB)

eBoard3DModelExportCopperOptions_CopperNone = 0
eBoard3DModelExportCopperOptions_CopperOnly = 1
eBoard3DModelExportCopperOptions_SelectedCoppers = 2
eBoard3DModelExportCopperOptions_CopperLayer = 3
eBoard3DModelExportCopperOptions_CopperAll = 4

### TBoard3DModelExportFormat (RT_PCB)

eBoard3DModelExportFormat_Step = 0
eBoard3DModelExportFormat_Parasolid = 1

### TBoard3DModelExportHolesOptions (RT_PCB)

eBoard3DModelExportHolesOptions_AllHoles = 0
eBoard3DModelExportHolesOptions_SelectedHoles = 1

### TBoard3DModelExportModelsOptions (RT_PCB)

eBoard3DModelExportModelsOptions_AsStep = 0
eBoard3DModelExportModelsOptions_AsExtruded = 1
eBoard3DModelExportModelsOptions_AsBoth = 2

### TBoardSide (RT_PCB)

eBoardSide_Top = 0
eBoardSide_Bottom = 1

### TBookmarkFlag (Data.DB)

bfCurrent = 0
bfBOF = 1
bfEOF = 2
bfInserted = 3

### TBorderIcon (System.UITypes)

biSystemMenu = 0
biMinimize = 1
biMaximize = 2
biHelp = 3

### TBreakpointMode (Rt_NexusDevices)

eBreakpointMode_SOFT = 0
eBreakpointMode_HARD = 1
eBreakpointMode_ANY = 2

### TBrowseForFolderOption (Vcl.StdActns)

bifBrowseForComputer = 0
bifBrowseForPrinter = 1
bifBrowseIncludeFiles = 2
bifBrowseIncludeURLS = 3
bifDontGoBelowDomain = 4
bifEditBox = 5
bifNewDialogStyle = 6
bifNoNewFolderButton = 7
bifNoTranslateTargets = 8
bifReturnFSAncestors = 9
bifReturnOnlyFSDirs = 10
bifShareable = 11
bifStatusText = 12
bifUAHint = 13
bifUseNewUI = 14
bifValidate = 15

### TBrowseForFolderOptionEx (Vcl.StdActns)

bifeHidePinnedPlaces = 0
bifeNoDereferenceLinks = 1
bifeForceShowHidden = 2
bifeAllowMultiselect = 3

### TBrushStyle (Vcl.Graphics)

bsSolid = 0
bsClear = 1
bsHorizontal = 2
bsVertical = 3
bsFDiagonal = 4
bsBDiagonal = 5
bsCross = 6
bsDiagCross = 7

### TBucketListSizes (System.Contnrs)

bl2 = 0
bl4 = 1
bl8 = 2
bl16 = 3
bl32 = 4
bl64 = 5
bl128 = 6
bl256 = 7

### TBusKind (Rt_Util)

eBusKindUndefined = 0
eBusKindLowValueFirst = 1
eBusKindHighValueFirst = 2
eBusKindGeneric = 3

### TBusTextStyle (Rt_Schematic)

eBusTextStyle_Full = 0
eBusTextStyle_Prefix = 1

### TButtonKind (dcedit)

bkCustom = 0
bkDropDown = 1  // 脚本里不可用
bkDots = 2  // 脚本里不可用

### TButtonKind (XPThemeForm)

bkNone = 0
bkHelp = 1  // 脚本里是 3
bkMin = 2  // 脚本里不可用
bkMax = 3  // 脚本里不可用
bkClose = 4  // 脚本里是 6

### TButtonLayout (Vcl.Buttons)

blGlyphLeft = 0
blGlyphRight = 1
blGlyphTop = 2
blGlyphBottom = 3

### TButtonState (Vcl.Buttons)

bsUp = 0
bsDisabled = 1
bsDown = 2
bsExclusive = 3

### TButtonState (XPThemeForm)

bsNormal = 0
bsHot = 1  // 脚本里是 4
bsPressed = 2  // 脚本里不可用
bsDisabled = 3  // 脚本里是 1

### TButtonStyle (Vcl.Buttons)

bsAutoDetect = 0
bsWin31 = 1
bsNew = 2

### TCacheState (RT_PCB)

eCacheInvalid = 0
eCacheValid = 1
eCacheManual = 2

### TCalDayOfWeek (System.UITypes)

dowMonday = 0
dowTuesday = 1
dowWednesday = 2
dowThursday = 3
dowFriday = 4
dowSaturday = 5
dowSunday = 6
dowLocaleDefault = 7

### TCANOperator (Data.DBCommon)

coNOTDEFINED = 0
coISBLANK = 1
coNOTBLANK = 2
coEQ = 3
coNE = 4
coGT = 5
coLT = 6
coGE = 7
coLE = 8
coNOT = 9
coAND = 10
coOR = 11
coTUPLE2 = 12
coFIELD2 = 13
coCONST2 = 14
coMINUS = 15
coADD = 16
coSUB = 17
coMUL = 18
coDIV = 19
coMOD = 20
coREM = 21
coSUM = 22
coCOUNT = 23
coMIN = 24
coMAX = 25
coAVG = 26
coCONT = 27
coUDF2 = 28
coCONTINUE2 = 29
coLIKE = 30
coIN = 31
coLIST2 = 32
coUPPER = 33
coLOWER = 34
coFUNC2 = 35
coLISTELEM2 = 36
coASSIGN = 37

### TCanvasOrientation (Vcl.Graphics)

coLeftToRight = 0
coRightToLeft = 1

### TCanvasStates (Vcl.Graphics)

csHandleValid = 0
csFontValid = 1
csPenValid = 2
csBrushValid = 3

### TCaptionPos (XPButton)

cpTop = 0
cpLeft = 1
cpRight = 2
cpBottom = 3

### TCaretStyle (InstrumentComms)

csDOS = 0
csWindows = 1
csBlock = 2

### TCCTCost (RT_PCB)

eForbidden = 0
eHigh = 1
eMedium = 2
eLow = 3
eFree = 4
eDefaultCost = 5

### TCCTSort (RT_PCB)

eSmart = 0
eRandom = 1
eLength = 2
eArea = 3

### TCCTSortDir (RT_PCB)

eUp = 0
eDown = 1

### TCellFunction (Rt_NexusDevices)

eCellFunction_Undefined = 0
eCellFunction_Input = 1
eCellFunction_Clock = 2
eCellFunction_Output2 = 3
eCellFunction_Output3 = 4
eCellFunction_Control = 5
eCellFunction_ControlR = 6
eCellFunction_Internal = 7
eCellFunction_BiDir = 8
eCellFunction_ObserveOnly = 9

### TCellKind (Rt_NexusDevices)

eCellKind_Undefined = 0
eCellKind_BC_0 = 1
eCellKind_BC_1 = 2
eCellKind_BC_2 = 3
eCellKind_BC_3 = 4
eCellKind_BC_4 = 5
eCellKind_BC_5 = 6
eCellKind_BC_6 = 7
eCellKind_BC_7 = 8
eCellKind_BC_8 = 9
eCellKind_BC_9 = 10
eCellKind_BC_10 = 11

### TChannel (Rt_NexusWorkspace)

eChannel_Board = 0
eChannel_Hard = 1
eChannel_Soft = 2
eChannel_Release = 3

### TChannelRoomNamingStyle (RT_Workspace)

eChannelRoomNamingStyle_FlatNumericWithNames = 0
eChannelRoomNamingStyle_FlatAlphaWithNames = 1
eChannelRoomNamingStyle_NumericNamePath = 2
eChannelRoomNamingStyle_AlphaNamePath = 3
eChannelRoomNamingStyle_MixedNamePath = 4

### TCheckBoxState (Vcl.StdCtrls)

cbUnchecked = 0
cbChecked = 1
cbGrayed = 2

### TClassificationField (RT_PCB)

cfToolSize = 0
cfLength = 1
cfHoleType = 2
cfPlated = 3
cfLayerPairIndex = 4
cfObjectId = 5
cfPadShape = 6
cfTemplateName = 7
cfTemplateDescription = 8
cfHoleCombinedTolerance = 9
cfHolePositiveTolerance = 10
cfHoleNegativeTolerance = 11
cfDrillType = 12
cfViaStructureType = 13
cfCounterHoleDepth = 14
cfCounterHoleAngle = 15

### TClassMemberKind (Pcbtypes)

eClassMemberKind_Net = 0
eClassMemberKind_Component = 1
eClassMemberKind_FromTo = 2
eClassMemberKind_Pad = 3
eClassMemberKind_Layer = 4
eClassMemberKind_DesignChannel = 5
eClassMemberKind_DifferentialPair = 6
eClassMemberKind_Polygon = 7
eClassMemberKind_SplitPlane = 8

### TClassMemberKind (RT_PCB)

eClassMemberKind_Net = 0
eClassMemberKind_Component = 1
eClassMemberKind_FromTo = 2
eClassMemberKind_Pad = 3
eClassMemberKind_Layer = 4
eClassMemberKind_DesignChannel = 5
eClassMemberKind_DifferentialPair = 6
eClassMemberKind_Polygon = 7
eClassMemberKind_SplitPlane = 8
eClassMemberKind_ObjectClass = 9
eClassMemberKind_Signal = 10

### TClearanceConstraintMode (RT_PCB)

eClearanceConstraintMode_SingleClearance = 0
eClearanceConstraintMode_ObjectsClearance = 1

### TClockOperationKind (Rt_NexusDevices)

eClockOperation_PhaseShift = 0
eClockOperation_DivideBy = 1
eClockOperation_MultiplyBy = 2

### TCloseAction (System.UITypes)

caNone = 0
caHide = 1
caFree = 2
caMinimize = 3

### TCollectionNotification (System.Generics.Collections)

cnAdded = 0
cnRemoved = 1  // 脚本里不可用
cnExtracted = 2  // 脚本里不可用

### TColorBoxStyles (Vcl.ExtCtrls)

cbStandardColors = 0
cbExtendedColors = 1
cbSystemColors = 2
cbIncludeNone = 3
cbIncludeDefault = 4
cbCustomColor = 5
cbPrettyNames = 6
cbCustomColors = 7

### TColorDepth (Vcl.ImgList)

cdDefault = 0
cdDeviceDependent = 1
cd4Bit = 2
cd8Bit = 3
cd16Bit = 4
cd24Bit = 5
cd32Bit = 6

### TColorDialogOption (Vcl.Dialogs)

cdFullOpen = 0
cdPreventFullOpen = 1
cdShowHelp = 2
cdSolidColor = 3
cdAnyColor = 4

### TComboBoxExStyle (Vcl.ComCtrls)

csExDropDown = 0
csExSimple = 1
csExDropDownList = 2

### TComboBoxExStyleEx (Vcl.ComCtrls)

csExCaseSensitive = 0
csExNoEditImage = 1
csExNoEditImageIndent = 2
csExNoSizeLimit = 3
csExPathWordBreak = 4

### TComboBoxStyle (Vcl.StdCtrls)

csDropDown = 0
csSimple = 1
csDropDownList = 2
csOwnerDrawFixed = 3
csOwnerDrawVariable = 4

### TCommandType (Data.Win.ADODB)

cmdUnknown = 0
cmdText = 1
cmdTable = 2
cmdStoredProc = 3
cmdFile = 4
cmdTableDirect = 5

### TCommonAVI (Vcl.ComCtrls)

aviNone = 0
aviFindFolder = 1
aviFindFile = 2
aviFindComputer = 3
aviCopyFiles = 4
aviCopyFile = 5
aviRecycleFile = 6
aviEmptyRecycle = 7
aviDeleteFile = 8

### TCompilationStage (RT_Workspace)

eCompilationStage_Compiling = 0
eCompilationStage_Flattening = 1

### TComponentCollisionCheckMode (RT_PCB)

eQuickCheck = 0
eMultiLayerCheck = 1
eFullCheck = 2
eComponentBodyCheck = 3

### TComponentKind (RT_Workspace)

eComponentKind_Standard = 0
eComponentKind_Mechanical = 1
eComponentKind_Graphical = 2
eComponentKind_NetTie_BOM = 3
eComponentKind_NetTie_NoBOM = 4
eComponentKind_Standard_NoBOM = 5
eComponentKind_Jumper = 6

### TComponentMoveKind (RT_PCB)

eNoComponentMoveNoAction = 0
eJumpToComponent = 1
eMoveComponentToCursor = 2

### TComponentPlacementType (RT_PCB)

eComponentPlacement_None = 0
eComponentPlacement_BodyUp = 1
eComponentPlacement_BodyDown = 2

### TConfigFileFormat (Rt_ActelFPGA)

eConfigFileFormat_STAPL = 0
eConfigFileFormat_DC = 1
eConfigFileFormat_FDB = 2

### TConfinementStyle (RT_PCB)

eConfineIn = 0
eConfineOut = 1

### TConfirmationOption (RT_ClientServerInterface)

coNever = 0
coAskFirst = 1
coAskIfModified = 2
coAlways = 3

### TConnectionCode (RT_Workspace)

eCC_PinInput = 0
eCC_PinIO = 1
eCC_PinOutput = 2
eCC_PinOpenCollector = 3
eCC_PinPassive = 4
eCC_PinHiZ = 5
eCC_PinOpenEmitter = 6
eCC_PinPower = 7
eCC_PortInput = 8
eCC_PortOutput = 9
eCC_PortBidirectional = 10
eCC_PortUnspecified = 11
eCC_SheetEntryInput = 12
eCC_SheetEntryOutput = 13
eCC_SheetEntryBidirectional = 14
eCC_SheetEntryUnspecified = 15
eCC_UnConnected = 16

### TConnectionMode (RT_PCB)

eRatsNestConnection = 0
eBrokenNetMarker = 1

### TConnectMode (Data.Win.ADODB)

cmUnknown = 0
cmRead = 1
cmWrite = 2
cmReadWrite = 3
cmShareDenyRead = 4
cmShareDenyWrite = 5
cmShareExclusive = 6
cmShareDenyNone = 7

### TConnectOption (Data.Win.ADODB)

coConnectUnspecified = 0
coAsyncConnect = 1

### TConsistentAttribute (Vcl.ComCtrls)

caBold = 0
caColor = 1
caFace = 2
caItalic = 3
caSize = 4
caStrikeOut = 5
caUnderline = 6
caProtected = 7

### TCoolBandMaximize (Vcl.ComCtrls)

bmNone = 0
bmClick = 1
bmDblClick = 2

### TCopperOrientation (RT_PCB)

Above = 0
Below = 1

### TCopyMode (RT_PCB)

eFullCopy = 0
eFieldCopy = 1

### TCornerEdge (Vcl.ExtCtrls)

ceNone = 0
ceSmall = 1
ceMedium = 2
ceLarge = 3

### TCornerStyle (RT_PCB)

eCornerStyle_90 = 0
eCornerStyle_45 = 1
eCornerStyle_Round = 2

### TCounterHoleDirection (RT_PCB)

eFromTopToBottom = 0
eFromBottomToTop = 1

### TCounterHoleMaterial (RT_PCB)

eNoMaterial = 0
eCopperPlated = 1
eSurfaceFinish = 2

### TCounterHoleType (RT_PCB)

eCounterBore = 0
eCounterSink = 1

### TCreateType (Vcl.OleCtnrs)

ctNewObject = 0
ctFromFile = 1
ctLinkToFile = 2
ctFromData = 3
ctLinkFromData = 4

### TCrossRefLocationStyle (RT_Workspace)

eCrossRefLocationNone = 0
eCrossRefLocationZone = 1
eCrossRefLocationXY = 2

### TCrossRefPorts (RT_Workspace)

eCrossRefPortsDisabled = 0
eCrossRefPortsSheetEntry = 1
eCrossRefPortsPorts = 2
eCrossRefPortsSheetEntryAndPorts = 3

### TCrossRefSheetStyle (RT_Workspace)

eCrossRefSheetNone = 0
eCrossRefSheetName = 1
eCrossRefSheetNumber = 2

### TCrossSelectZoomOption (RT_Workspace)

eZoom_None = 0
eZoom_Last = 1
eZoom_All = 2

### TCrossSheetConnectorStyle (Rt_Schematic)

eCrossSheetLeft = 0
eCrossSheetRight = 1

### TCursorLocation (Data.Win.ADODB)

clUseServer = 0
clUseClient = 1

### TCursorOption (Data.Win.ADODB)

coHoldRecords = 0
coMovePrevious = 1
coAddNew = 2
coDelete = 3
coUpdate = 4
coBookmark = 5
coApproxPosition = 6
coUpdateBatch = 7
coResync = 8
coNotify = 9
coFind = 10
coSeek = 11
coIndex = 12

### TCursorShape (Rt_Schematic)

eLargeCursor90 = 0
eSmallCursor90 = 1
eSmallCursor45 = 2
eTinyCursor45 = 3

### TCursorType (Data.Win.ADODB)

ctUnspecified = 0
ctOpenForwardOnly = 1
ctKeyset = 2
ctDynamic = 3
ctStatic = 4

### TCustomDrawStage (Vcl.ComCtrls)

cdPrePaint = 0
cdPostPaint = 1
cdPreErase = 2
cdPostErase = 3

### TCustomDrawTarget (Vcl.ComCtrls)

dtControl = 0
dtItem = 1
dtSubItem = 2

### TcxBlobKind (cxEdit)

bkNone = 0
bkBlob = 1  // 脚本里不可用
bkGraphic = 2  // 脚本里不可用
bkMemo = 3  // 脚本里不可用
bkOle = 4  // 脚本里不可用

### TcxDataSortOrder (cxCustomData)

soNone = 0
soAscending = 1  // 脚本里不可用
soDescending = 2  // 脚本里不可用

### TcxDirection (cxClasses)

dirNone = 0  // 脚本里不可用
dirLeft = 1  // 脚本里是 0
dirRight = 2
dirUp = 3  // 脚本里是 1
dirDown = 4  // 脚本里是 3

### TcxImageAlign (cxImageComboBox)

iaLeft = 0  // 脚本里是 1
iaRight = 1

### TcxPCStandardStyle (cxPC)

tsTabs = 0
tsButtons = 1
tsFlatButtons = 2

### TcxTabPosition (cxPC)

tpTop = 0
tpBottom = 1
tpLeft = 2
tpRight = 3

### TDaisyChainStyle (Pcbtypes)

eDaisyChainLoad = 0
eDaisyChainTerminator = 1
eDaisyChainSource = 2

### TDaisyChainStyle (RT_PCB)

eDaisyChainLoad = 0
eDaisyChainTerminator = 1
eDaisyChainSource = 2

### TDataAction (Data.DB)

daFail = 0
daAbort = 1
daRetry = 2

### TDatabaseType (RT_Workspace)

eDatabaseType_SQLServer = 0
eDatabaseType_Access = 1
eDatabaseType_MySQL = 2
eDatabaseType_Oracle = 3
eDatabaseType_Other = 4

### TDataBits (RT_PCB)

eDataBits5 = 0
eDataBits6 = 1
eDataBits7 = 2
eDataBits8 = 3

### TDataEvent (Data.DB)

deFieldChange = 0
deRecordChange = 1
deDataSetChange = 2
deDataSetScroll = 3
deLayoutChange = 4
deUpdateRecord = 5
deUpdateState = 6
deCheckBrowseMode = 7
dePropertyChange = 8
deFieldListChange = 9
deFocusControl = 10
deParentScroll = 11
deConnectChange = 12
deReconcileError = 13
deDisabledStateChange = 14

### TDataSetState (Data.DB)

dsInactive = 0
dsBrowse = 1
dsEdit = 2
dsInsert = 3
dsSetKey = 4
dsCalcFields = 5
dsFilter = 6
dsNewValue = 7
dsOldValue = 8
dsCurValue = 9
dsBlockRead = 10
dsInternalCalc = 11
dsOpening = 12

### TDateTimeKind (Vcl.ComCtrls)

dtkDate = 0
dtkTime = 1

### TDBNavigatorKind (Vcl.DBCtrls)

dbnHorizontal = 0
dbnVertical = 1

### TDBScreenCursor (Data.DB)

dcrDefault = 0
dcrHourGlass = 1
dcrSQLWait = 2
dcrOther = 3

### TDDBEditMode (ClientProcs)

eDDBCanceled = 0
eDDBCopy = 1
eDDBMove = 2
eDDBLink = 3

### TDebuggerMode (Rt_NexusDevices)

eDebuggerMode_MANUAL = 0
eDebuggerMode_AUTO = 1

### TDebuggerState (RT_Debugger)

eDSDisabled = 0
eDSReady = 1
eDSExecuting = 2
eDSFinished = 3
eDSBusy = 4

### TDefaultMonitor (Vcl.Forms)

dmDesktop = 0
dmPrimary = 1
dmMainForm = 2
dmActiveForm = 3

### TDegreeOfFreedom (RT_PCB)

eDOF_None = 0
eDOF_X = 1
eDOF_Y = 2
eDOF_Z = 3
eDOF_Translate0 = 4
eDOF_Translate1 = 5
eDOF_Translate2 = 6
eDOF_Translate3 = 7
eDOF_Translate4 = 8
eDOF_Translate5 = 9
eDOF_Translate6 = 10
eDOF_Translate7 = 11
eDOF_RotX = 12
eDOF_RotY = 13
eDOF_RotZ = 14
eDOF_Rotate0 = 15
eDOF_Rotate1 = 16
eDOF_Rotate2 = 17
eDOF_Rotate3 = 18
eDOF_Rotate4 = 19
eDOF_Rotate5 = 20
eDOF_Rotate6 = 21
eDOF_Rotate7 = 22
eDOF_Fade = 23

### TDesignatorDisplayMode (RT_PCB)

eDesignatorDisplayMode_Physical = 0
eDesignatorDisplayMode_Logical = 1

### TDeviceIOStandardType (Rt_NexusDevices)

eLVTTL15 = 0
eLVTTL18 = 1
eLVTTL25 = 2
eLVTTL33 = 3
eLVCMOS15 = 4
eLVCMOS18 = 5
eLVCMOS25 = 6
eLVCMOS33 = 7
eLVCMOS5 = 8
ePCI33_3 = 9
ePCI33_5 = 10
ePCI66 = 11
ePCIX_3 = 12
eCOMPACTPCI_3 = 13
eSSTL3I = 14
eSSTL3II = 15
eSSTL2I = 16
eSSTL2II = 17
eSSTL18I = 18
eSSTL18II = 19
eGTL = 20
eGTLP = 21
eHSTLI = 22
eHSTLII = 23
eHSTLIII = 24
eHSTLIV = 25
eHSTL_12 = 26
eHSTLI_18 = 27
eHSTLII_18 = 28
eHSTLIII_18 = 29
eHSTLIV_18 = 30
eCTT = 31
eAGP1x = 32
eAGP2x = 33
eTTL = 34
eLVCMOS12 = 35
eGTL_DCI = 36
eGTLP_DCI = 37
eHSTLI_DCI = 38
eHSTLII_DCI = 39
eHSTLIII_DCI = 40
eHSTLIV_DCI = 41
eHSTLI_18_DCI = 42
eHSTLII_18_DCI = 43
eHSTLIII_18_DCI = 44
eHSTLIV_18_DCI = 45
eDHSTLI = 46
eDHSTLII = 47
eDHSTLIII = 48
eDHSTL18I = 49
eDHSTL18II = 50
eDHSTL18III = 51
eHTT = 52
ePCML = 53
ePCML15 = 54
eSSTL18I_DCI = 55
eSSTL18II_DCI = 56
eSSTL2I_DCI = 57
eSSTL2II_DCI = 58
eSSTL3I_DCI = 59
eSSTL3II_DCI = 60
eLVCMOS15_DCI = 61
eLVCMOS18_DCI = 62
eLVCMOS25_DCI = 63
eLVCMOS33_DCI = 64
eLVCMOS15_DCI_DV2 = 65
eLVCMOS18_DCI_DV2 = 66
eLVCMOS25_DCI_DV2 = 67
eLVCMOS33_DCI_DV2 = 68
eLVDS = 69
eLVPECL = 70
eDSSTL18I = 71
eDSSTL18II = 72
eDSSTL2I = 73
eDSSTL2II = 74
eDSSTL3I = 75
eDSSTL3II = 76
eBLVDS25 = 77
eLVPECL25 = 78
eRSDS25 = 79
eLVDS33 = 80
eLVDS25_DCI = 81
eLVDS33_DCI = 82
eLVDSEXT25 = 83
eLVDSEXT33 = 84
eLVDSEXT25_DCI = 85
eLVDSEXT33_DCI = 86
eLDT = 87
eULVDS25 = 88
eLDT_DT = 89
eLVDS_DT = 90
eLVDSEXT25_DT = 91
eULVDS25_DT = 92
eMiniLVDS25 = 93
eLVCMOS33_1 = 94
eLVCMOS33_2 = 95
eDHSTLII_DCI = 96
eDHSTL18II_DCI = 97
eDSSTL2II_DCI = 98
eDSSTL18II_DCI = 99
eLVTTL12 = 100
ePCML12 = 101
eBLVDS33 = 102
eRSDS33 = 103
eHSLV15_DCI = 104
eHSLV18_DCI = 105
eHSLV25_DCI = 106
eHSLV33_DCI = 107
eMLVDS25 = 108
eMiniLVDS33 = 109
eTMDS33 = 110
ePPDS25 = 111
ePPDS33 = 112
eDHSTL18I_DCI = 113
eDHSTLI_DCI = 114
eDSSTL18I_DCI = 115
eDSSTL2I_DCI = 116
eHSTLII_18T_DCI = 117
eHSTLIIT_DCI = 118
eSSTL18IIT_DCI = 119
eSSTL2IIT_DCI = 120
ePCIX_15 = 121
eCTT25 = 122
eLVCMOS30 = 123
eLVTTL30 = 124
eHSTLII_12 = 125
ePCI33_30 = 126
ePCIX_30 = 127
eDHSTL12I = 128
eDHSTL12II = 129
eSSTL15I = 130
eSSTL15II = 131
eHSTLI_12 = 132
eDSSTL15I = 133
eDSSTL15II = 134
eMiniLVDS25_E_1R = 135
eMiniLVDS25_E_3R = 136
eRSDS25_E_1R = 137
eRSDS25_E_3R = 138
eLVDS_E_1R = 139
eLVDS_E_3R = 140
eGTL33 = 141
eGTL25 = 142
eGTLP33 = 143
eGTLP25 = 144
eI2C = 145
eSMBus = 146
eSDIO = 147
eMOBILE_DDR = 148
eDMOBILE_DDR = 149
eDISPLAY_PORT = 150
eDHSTLIIT_DCI = 151
eDHSTLII_18T_DCI = 152
eSSTL15 = 153
eSSTL15_DCI = 154
eDSSTL15 = 155
eDSSTL15_DCI = 156
eSSTL15T_DCI = 157
eDSSTL2IIT_DCI = 158
eDSSTL18IIT_DCI = 159
eDSSTL15T_DCI = 160
ePPDS25_E_3R = 161
eDSSTL12II = 162
eHCSL = 163
ePCML25 = 164
eDSSTL25I = 165
eDSSTL25II = 166
eDSSTL20II = 167
eDSSTL12I = 168
ePCML14 = 169
eLVTTL33_STI = 170
eLVTTL25_STI = 171
eSSTL25I = 172
eSSTL25II = 173
eLVPECL33 = 174
eMLVDS33 = 175
eLVTTL33D = 176
eLVCMOS33D = 177
eLVCMOS25D = 178
eLVCMOS18D = 179
eLVCMOS15D = 180
eLVCMOS12D = 181
eBLVDS25E = 182
eMLVDS25E = 183
eLVPECL33E = 184
eRSDS25E = 185

### TDeviceState (Rt_NexusDevices)

eDeviceState_Unknown = 0
eDeviceState_Reset = 1
eDeviceState_Programmed = 2
eDeviceState_Programmed_ReadProtected = 3
eDeviceState_Programmed_WriteProtected = 4
eDeviceState_Programmed_ReadWriteProtected = 5

### TDeviceVendor (Rt_AbstractFPGA)

eDeviceVendor_Actel = 0
eDeviceVendor_Altera = 1
eDeviceVendor_Lattice = 2
eDeviceVendor_Sharp = 3
eDeviceVendor_Amcc = 4
eDeviceVendor_Xilinx = 5
eDeviceVendor_TexasInstruments = 6
eDeviceVendor_STMicroelectronics = 7

### TDielectricType (Pcbtypes)

eNoDielectric = 0
eCore = 1
ePrePreg = 2
eSurfaceMaterial = 3

### TDielectricType (RT_PCB)

eNoDielectric = 0
eCore = 1
ePrePreg = 2
eSurfaceMaterial = 3
eFilm = 4

### TDifferenceCheckLevel (RT_Workspace)

eDifferenceCheck_Off = 0
eDifferenceCheck_On = 1
eDifferenceCheck_On_CaseSensitive = 2

### TDifferenceKind (RT_Workspace)

eDifference_Undefined = 0
eDifference_ExtraComponent = 1
eDifference_ExtraNet = 2
eDifference_ExtraNode = 3
eDifference_ExtraComponentClass = 4
eDifference_ExtraNetClass = 5
eDifference_ExtraChannelClass = 6
eDifference_ExtraComponentClassMember = 7
eDifference_ExtraNetClassMember = 8
eDifference_ExtraChannelClassMember = 9
eDifference_ExtraRule = 10
eDifference_ExtraRoomDefinition = 11
eDifference_ExtraParameter = 12
eDifference_ComponentDesignator = 13
eDifference_ComponentFootprint = 14
eDifference_ComponentComment = 15
eDifference_ComponentKind = 16
eDifference_NetName = 17
eDifference_ComponentClassName = 18
eDifference_NetClassName = 19
eDifference_ChannelClassName = 20
eDifference_RoomDefinition = 21
eDifference_ParameterValue = 22
eDifference_ParameterType = 23
eDifference_Rule = 24
eDifference_ComponentDesignItemID = 25
eDifference_ExtraSchematicObject = 26
eDifference_ExtraPcbObject = 27
eDifference_ChangedSchematicObject = 28
eDifference_ChangedPcbObject = 29
eDifference_ChangedPin = 30
eDifference_ExtraDifferentialPair = 31
eDifference_DifferentialPairPositiveNet = 32
eDifference_DifferentialPairNegativeNet = 33
eDifference_ComponentDescription = 34
eDifference_ComponentLibrary = 35
eDifference_ExtraClassCluster = 36
eDifference_ExtraClassClusterMember = 37
eDifference_ClassClusterClassName = 38
eDifference_ConfigurableParameters = 39
eDifference_ComponentVaultGUID = 40
eDifference_ComponentItemGUID = 41
eDifference_ComponentRevisionGUID = 42
eDifference_NetColor = 43
eDifference_ChangedPinPackageLength = 44
eDifference_ExtraSystemDesignPin = 45
eDifference_ComponentParameters = 46
eDifference_ExtraSystemDesignModule = 47
eDifference_ExtraSystemDesignFunctionalBlock = 48
eDifference_ExtraSystemDesignModuleConnector = 49
eDifference_ExtraSystemDesignConnection = 50
eDifference_ChangedSystemDesignModuleProperties = 51
eDifference_ChangedSystemDesignModuleFileName = 52
eDifference_ChangedSystemDesignFunctionalBlock = 53
eDifference_ChangedSystemDesignModuleConnector = 54
eDifference_ChangedSystemDesignConnection = 55
eDifference_ExtraSystemDesignPinInNet = 56
eDifference_ChangedSystemDesignPinNetName = 57
eDifference_SystemDesignPinSwap = 58
eDifference_ChangedSystemDesignPhysicalConnection = 59
eDifference_ExtraSystemDesignPhysicalConnection = 60
eDifference_ChangedSystemDesignPin = 61
eDifference_ExtraDifferentialPairClass = 62
eDifference_DifferentialPairClassName = 63
eDifference_ExtraDifferentialPairClassMember = 64
eDifference_ComponentLocation = 65
eDifference_ManagedComponentLibraryLink = 66
eDifference_ChangedPinPropagationDelay = 67

### TDimensionArrowPosition (Pcbtypes)

eInside = 0
eOutside = 1

### TDimensionArrowPosition (RT_PCB)

eInside = 0
eOutside = 1

### TDimensionKind (Pcbtypes)

eNoDimension = 0
eLinearDimension = 1
eAngularDimension = 2
eRadialDimension = 3
eLeaderDimension = 4
eDatumDimension = 5
eBaselineDimension = 6
eCenterDimension = 7
eOriginalDimension = 8
eLinearDiameterDimension = 9
eRadialDiameterDimension = 10

### TDimensionKind (RT_PCB)

eNoDimension = 0
eLinearDimension = 1
eAngularDimension = 2
eRadialDimension = 3
eLeaderDimension = 4
eDatumDimension = 5
eBaselineDimension = 6
eCenterDimension = 7
eOriginalDimension = 8
eLinearDiameterDimension = 9
eRadialDiameterDimension = 10

### TDimensionTextPosition (Pcbtypes)

eTextAuto = 0
eTextCenter = 1
eTextTop = 2
eTextBottom = 3
eTextRight = 4
eTextLeft = 5
eTextInsideRight = 6
eTextInsideLeft = 7
eTextUniDirectional = 8
eTextManual = 9

### TDimensionTextPosition (RT_PCB)

eTextAuto = 0
eTextCenter = 1
eTextTop = 2
eTextBottom = 3
eTextRight = 4
eTextLeft = 5
eTextInsideRight = 6
eTextInsideLeft = 7
eTextUniDirectional = 8
eTextManual = 9

### TDimensionUnit (Pcbtypes)

eMils = 0
eInches = 1
eMillimeters = 2
eCentimeters = 3
eDegrees = 4
eRadians = 5
eAutomaticUnit = 6

### TDimensionUnit (RT_PCB)

eMils = 0
eInches = 1
eMillimeters = 2
eCentimeters = 3
eDegrees = 4
eRadians = 5
eAutomaticUnit = 6

### TDirection (System.Types)

FromBeginning = 0
FromEnd = 1

### TDisableResult (Rt_NexusDevices)

eDisableResult_Undefined = 0
eDisableResult_HiZ = 1
eDisableResult_Weak0 = 2
eDisableResult_Weak1 = 3
eDisableResult_Pull0 = 4
eDisableResult_Pull1 = 5
eDisableResult_Keeper = 6

### TDisplayCode (Vcl.ComCtrls)

drBounds = 0
drIcon = 1
drLabel = 2
drSelectBounds = 3

### TDisplayStyle (InstrumentTypes)

dsWhite = 0
dsGray = 1
dsCream = 2
dsRed = 3
dsOrange = 4
dsLilac = 5
dsBlue = 6
dsGreen = 7
dsPaleGreen = 8
dsBronze = 9
dsRedLed = 10

### TDocAnnotationScope (RT_Workspace)

eDocAnnotationScope_All = 0
eDocAnnotationScope_IgnoreSelected = 1
eDocAnnotationScope_OnlySelected = 2

### TDocAutoNetClassScope (RT_Workspace)

eDocAutoNetClassScope_None = 0
eDocAutoNetClassScope_LocalOnly = 1
eDocAutoNetClassScope_All = 2

### TDockOrientation (Vcl.Controls)

doNoOrient = 0
doHorizontal = 1
doVertical = 2

### TDocumentOpenMode (RT_Workspace)

eDOM_OpenAll = 0
eDOM_FocusOpen = 1
eDOM_DoNotFocusOpen = 2

### TDocumentsBarGrouping (RT_ClientServerInterface)

dbgNone = 0
dbgByDocKind = 1
dbgByProject = 2

### TDragKind (System.UITypes)

dkDrag = 0
dkDock = 1

### TDragMessage (Vcl.Controls)

dmDragEnter = 0
dmDragLeave = 1
dmDragMove = 2
dmDragDrop = 3
dmDragCancel = 4
dmFindTarget = 5

### TDragMode (System.UITypes)

dmManual = 0
dmAutomatic = 1

### TDragSelectUnselectMode (RT_PCB)

dmDrag = 0
dmMove = 1

### TDragState (System.UITypes)

dsDragEnter = 0
dsDragLeave = 1
dsDragMove = 2

### TDrawGridMode (RT_PCB)

dgLines = 0
dgDots = 1
dgDoNotDraw = 2

### TDrawingStyle (Vcl.ImgList)

dsFocus = 0
dsSelected = 1
dsNormal = 2  // 脚本里是 0
dsTransparent = 3

### TDrawInstrumentButtonCaptionStyle (InstrumentTypes)

dibcNone = 0
dibcNormal = 1
dibcLightedOff = 2
dibcLightedOn = 3

### TDrawMode (Pcbtypes)

eDrawFull = 0
eDrawDraft = 1
eDrawHidden = 2
eDrawThin = 3  // 脚本里不可用

### TDrawMode (RT_PCB)

eDrawFull = 0
eDrawDraft = 1
eDrawHidden = 2

### TDRCReportFileFormat (RT_PCB)

eDRC_HTML = 0
eDRC_Text = 1

### TDRCState (RT_PCB)

drcNone = 0
drcViolation = 1
drcWaived = 2

### TDrillLayerPairType (RT_PCB)

Regular = 0
MicroViaDrill = 1
Backdrill = 2
CounterHole = 3

### TDrillSymbol (Pcbtypes)

eSymbols = 0
eNumbers = 1
eLetters = 2

### TDrillSymbol (RT_PCB)

eSymbols = 0
eNumbers = 1
eLetters = 2

### TDropDownAlign (Vcl.DBCtrls)

daLeft = 0
daRight = 1
daCenter = 2

### TDTCalAlignment (Vcl.ComCtrls)

dtaLeft = 0
dtaRight = 1

### TDTDateFormat (Vcl.ComCtrls)

dfShort = 0
dfLong = 1

### TDTDateMode (Vcl.ComCtrls)

dmComboBox = 0
dmUpDown = 1

### TDuplicates (System.Types)

dupIgnore = 0
dupAccept = 1
dupError = 2

### TdxEditBorderStyle (dxCntner)

xbsNone = 0
xbsSingle = 1  // 脚本里不可用
xbsThick = 2  // 脚本里不可用
xbsFlat = 3  // 脚本里不可用
xbs3D = 4  // 脚本里不可用

### TdxGridBandFixed (dxTL)

bfNone = 0
bfLeft = 1  // 脚本里不可用
bfRight = 2  // 脚本里不可用

### TEasyConsistentAttr (EasyClasses)

caColor = 0  // 脚本里是 1
caBkColor = 1  // 脚本里不可用
caFace = 2
caCharSet = 3  // 脚本里不可用
caPitch = 4  // 脚本里不可用
caSize = 5  // 脚本里是 4
caBold = 6  // 脚本里是 0
caItalic = 7  // 脚本里是 3
caStrikeOut = 8  // 脚本里是 5
caUnderline = 9  // 脚本里是 6
caSubScript = 10  // 脚本里不可用
caSuperScript = 11  // 脚本里不可用
caStyle = 12  // 脚本里不可用
caScriptStyle = 13  // 脚本里不可用
caUserData = 14  // 脚本里不可用
caUrl = 15  // 脚本里不可用

### TECO_Mode (RT_Workspace)

eECO_PerformAction = 0
eECO_ValidateAction = 1
eECO_CheckSupportForAction = 2

### TEdgeBorder (Vcl.ToolWin)

ebLeft = 0
ebTop = 1
ebRight = 2
ebBottom = 3

### TEdgePolarity (Rt_NexusDevices)

eEdgeRising = 0
eEdgeFalling = 1

### TEdgeStyle (Vcl.ToolWin)

esNone = 0
esRaised = 1
esLowered = 2

### TEditCharCase (System.UITypes)

ecNormal = 0
ecUpperCase = 1
ecLowerCase = 2

### TEditingAction (RT_PCB)

eEditAction_Focus = 0
eEditAction_Move = 1
eEditAction_Change = 2
eEditAction_Delete = 3
eEditAction_Select = 4
eEditAction_NonGraphicalSelect = 5
eEditAction_Measure = 6
eEditAction_Dimension = 7

### TEditStyle (Vcl.Grids)

esSimple = 0
esEllipsis = 1
esPickList = 2

### TEllipsisPosition (Vcl.StdCtrls)

epNone = 0
epPathEllipsis = 1
epEndEllipsis = 2
epWordEllipsis = 3

### TEmbeddedBoardOriginMode (Pcbtypes)

eOriginMode_BoardOrigin = 0
eOriginMode_BottomLeft = 1

### TEmbeddedBoardOriginMode (RT_PCB)

eOriginMode_BoardOrigin = 0
eOriginMode_BottomLeft = 1

### TEndianness (Rt_NexusDevices)

eEndianness_None = 0
eEndianness_Big = 1
eEndianness_Little = 2

### TErrorGroup (RT_Workspace)

eErrorGroupDocument = 0
eErrorGroupComponent = 1
eErrorGroupParameters = 2
eErrorGroupBus = 3
eErrorGroupNet = 4
eErrorGroupMisc = 5
eErrorGroupConstraint = 6
eErrorGroupHarnesses = 7
eErrorGroupHighLevelCodeSymbols = 8
eErrorGroupFSM = 9
eErrorGroupSdConnections = 10
eErrorGroupSdMatedParts = 11

### TErrorKind (RT_Workspace)

eError_OffGridObject = 0
eError_OffDocumentObject = 1
eError_MissingChildDocument = 2
eError_MissingChildProject = 3
eError_PortNotLinkedToSheetSymbol = 4
eError_SheetEntryNotLinkedToPort = 5
eError_DuplicateDocumentNumbers = 6
eError_UnconnectedWire = 7
eError_UnconnectedNetItem = 8
eError_NetWithNoDrivingSource = 9
eError_FloatingInputPinsOnNet = 10
eError_DifferentConnectionCodesOnNet = 11
eError_MultipleSameConnectionCodeOnNet = 12
eError_MultipleNamesForNet = 13
eError_AddingItemsFromHiddenNetToNet = 14
eError_AddingHiddenNet = 15
eError_PowerObjectScopeChange = 16
eError_NetParameterInvalidName = 17
eError_NetParameterInvalidValue = 18
eError_MismatchedBusSectionOrdering = 19
eError_MismatchedFirstGenericIndex = 20
eError_MismatchedSecondGenericIndex = 21
eError_MismatchedIOTypeOnBus = 22
eError_BusIndexOutOfRange = 23
eError_RangeSyntaxError = 24
eError_IllegalBusDefinition = 25
eError_IllegalBusRangeValue = 26
eError_MismatchedBusWidths = 27
eError_MismatchedBusLabelOrdering = 28
eError_MixedGenericAndNumericBusLabels = 29
eError_UnDesignatedPart = 30
eError_DuplicateComponentDesignator = 31
eError_DuplicateSheetSymbolDesignator = 32
eError_DuplicateNets = 33
eError_DuplicatePinsInComponent = 34
eError_DuplicateSheetEntrysInSheetSymbol = 35
eError_DuplicatePortsInDocument = 36
eError_DuplicateSubParts = 37
eError_MismatchedHiddenPinConnections = 38
eError_MismatchedPinVisibility = 39
eError_SameParameterWithDifferentValues = 40
eError_SameParameterWithDifferentTypes = 41
eError_MissingModel = 42
eError_ModelInDifferentLocation = 43
eError_MissingModelInFile = 44
eError_DuplicateModelsFound = 45
eError_MissingModelParameter = 46
eError_ErrorInModelParameter = 47
eError_DuplicatePinsInPortMap = 48
eError_MissingPinInPortMap = 49
eError_MissingPinsPortMapSequence = 50
eError_DuplicateImplementation = 51
eError_UnusedPartInComponent = 52
eError_ExtraPinInComponentDisplayMode = 53
eError_MissingPinInComponentDisplayMode = 54
eError_MismatchedBusAndWire = 55
eError_FloatingNetLabel = 56
eError_FloatingPowerObject = 57
eError_SinglePinNet = 58
eError_SignalWithNoLoad = 59
eError_SignalWithNoDriver = 60
eError_SignalWithMultipleDrivers = 61
eError_AutoAssignedPin = 62
eError_NoError = 63
eError_MultipleTopLevelDocuments = 64
eError_MultipleConfigurationTargets = 65
eError_ConflictingConstraints = 66
eError_MissingConfigurationTarget = 67
eError_DuplicateUniqueIDs = 68
eError_DifferentialPairMissingPositiveNet = 69
eError_DifferentialPairMissingNegativeNet = 70
eError_DifferentialPairSameNetInMultiplePairs = 71
eError_DifferentialPairMisConnected = 72
eError_DifferentialPairInversedPolarity = 73
eError_DifferentialPairUnconnectedNet = 74
eError_ConstraintPortWithoutPin = 75
eError_ConstraintBoardNotFound = 76
eError_ConstraintConnectorCreationFailed = 77
eError_ConstraintDuplicateBoardInstance = 78
eError_MissingChildEntity = 79
eError_OpenBusLinkForbidden = 80
eError_OpenBusLinkMismatchingPorts = 81
eError_HarnessDefinitionConflict = 82
eError_HarnessNetMissingHarnessType = 83
eError_UnknownHarnessDefinitionName = 84
eError_BusNetItemOnHarnessNet = 85
eError_HarnessItemOnWireNet = 86
eError_HarnessItemOnBusNet = 87
eError_HarnessConnectorNameSyntax = 88
eError_MultipleHarnessTypesOnHarnessNet = 89
eError_OpenBusCascadedInterconnects = 90
eError_OpenBusArbiterLoop = 91
eError_CodeSymbolMissingExportedRoutine = 92
eError_CodeSymbolNoExportedRoutines = 93
eError_CodeSymbolDuplicateCodeEntryNames = 94
eError_CodeSymbolReservedNamesUsed = 95
eError_CodeSymbolIdentifierCaseMismatch = 96
eError_HDLIdentifierRenamed = 97
eError_AmbiguousDeviceSheet = 98
eError_SheetNamesClash = 99
eError_MissingModelEditor = 100
eError_DuplicateFSMStatesInDocument = 101
eError_NoInputToFSMState = 102
eError_NoOutputFromFSMState = 103
eError_MultipleFSMTransitionsBetweenStates = 104
eError_FSMTransitionEmptyCondition = 105
eError_NoDefaultFSMState = 106
eError_UnreachableFSMStates = 107
eError_UnusedFSMPort = 108
eError_UnApplicableRevisionState = 109
eError_VariantIntegrity = 110
eError_OutOfDateRevision = 111
eError_ObsoleteRevision = 112
eError_SdDifferentNetNames = 113
eError_SdEmptyEntry = 114
eError_SdNoMatedPart = 115
eError_SdNoExternalNet = 116
eError_SdUnresolvedConflict = 117
eError_CircularDocumentDependency = 118
eError_MultiChannelAlternate = 119
eError_AlternateItemFail = 120
eError_UnsynchronizedSchAndExternalNetNames = 121
eError_DeletedComponent = 122
eError_GenericComponent = 123
eError_FloatingDirectiveObject = 124
eError_SheetSymbolsWithDuplicatedIndexes = 125
eError_DuplicatedProjectFiles = 126

### TErrorLevel (RT_ClientServerInterface)

eErrorLevelNoReport = 0
eErrorLevelWarning = 1
eErrorLevelError = 2
eErrorLevelFatal = 3

### TEventReason (Data.Win.ADODB)

erAddNew = 0
erDelete = 1
erUpdate = 2
erUndoUpdate = 3
erUndoAddNew = 4
erUndoDelete = 5
erRequery = 6
erResynch = 7
erClose = 8
erMove = 9
erFirstChange = 10
erMoveFirst = 11
erMoveNext = 12
erMovePrevious = 13
erMoveLast = 14

### TEventStatus (Data.Win.ADODB)

esOK = 0
esErrorsOccured = 1
esCantDeny = 2
esCancel = 3
esUnwantedEvent = 4

### TExecuteOption (Data.Win.ADODB)

eoAsyncExecute = 0
eoAsyncFetch = 1
eoAsyncFetchNonBlocking = 2
eoExecuteNoRecords = 3

### TExpandStyle (Vcl.ExtCtrls)

emAddRows = 0
emAddColumns = 1
emFixedSize = 2

### TExprNodeKind (Data.DBCommon)

enField = 0
enConst = 1
enOperator = 2
enFunc = 3

### TExprScopeKind (Data.DBCommon)

skField = 0
skAgg = 1
skConst = 2

### TExprToken (Data.DBCommon)

etEnd = 0
etSymbol = 1
etName = 2
etLiteral = 3
etLParen = 4
etRParen = 5
etEQ = 6
etNE = 7
etGE = 8
etLE = 9
etGT = 10
etLT = 11
etADD = 12
etSUB = 13
etMUL = 14
etDIV = 15
etComma = 16
etLIKE = 17
etISNULL = 18
etISNOTNULL = 19
etIN = 20

### TExtendedDrillType (Pcbtypes)

eDrilledHole = 0
ePunchedHole = 1
eLaserDrilledHole = 2
ePlasmaDrilledHole = 3

### TExtendedDrillType (RT_PCB)

eDrilledHole = 0
ePunchedHole = 1
eLaserDrilledHole = 2
ePlasmaDrilledHole = 3

### TExtendedHoleType (RT_PCB)

eRoundHole = 0
eSquareHole = 1
eSlotHole = 2

### TExtensionState (Rt_Util)

xsNotInstalled = 0
xsValid = 1
xsInactive = 2
xsOutOfDate = 3

### TFanoutDirection (RT_PCB)

eFanoutDirection_None = 0
eFanoutDirection_InOnly = 1
eFanoutDirection_OutOnly = 2
eFanoutDirection_InThenOut = 3
eFanoutDirection_OutThenIn = 4
eFanoutDirection_Alternating = 5

### TFanoutStyle (RT_PCB)

eFanoutStyle_Auto = 0
eFanoutStyle_Rows = 1
eFanoutStyle_Staggered = 2
eFanoutStyle_BGA = 3
eFanoutStyle_UnderPads = 4

### TFieldAttribute (Data.DB)

faHiddenCol = 0
faReadonly = 1
faRequired = 2
faLink = 3
faUnNamed = 4
faFixed = 5

### TFieldKeyType (RT_Workspace)

eFieldType_Key = 0
eFieldType_Normal = 1

### TFieldKind (Data.DB)

fkData = 0
fkCalculated = 1
fkLookup = 2
fkInternalCalc = 3
fkAggregate = 4

### TFieldLifeCycle (Data.DB)

lcAutomatic = 0
lcPersistent = 1

### TFieldsAutoCreationMode (Data.DB)

acExclusive = 0
acCombineComputed = 1
acCombineAlways = 2

### TFieldsPositionMode (Data.DB)

poLast = 0
poFirst = 1
poFieldNo = 2

### TFieldType (Data.DB)

ftUnknown = 0
ftString = 1
ftSmallint = 2
ftInteger = 3
ftWord = 4
ftBoolean = 5
ftFloat = 6
ftCurrency = 7
ftBCD = 8
ftDate = 9
ftTime = 10
ftDateTime = 11
ftBytes = 12
ftVarBytes = 13
ftAutoInc = 14
ftBlob = 15
ftMemo = 16
ftGraphic = 17
ftFmtMemo = 18
ftParadoxOle = 19
ftDBaseOle = 20
ftTypedBinary = 21
ftCursor = 22
ftFixedChar = 23
ftWideString = 24
ftLargeint = 25
ftADT = 26
ftArray = 27
ftReference = 28
ftDataSet = 29
ftOraBlob = 30
ftOraClob = 31
ftVariant = 32
ftInterface = 33
ftIDispatch = 34
ftGuid = 35
ftTimeStamp = 36
ftFMTBcd = 37
ftFixedWideChar = 38
ftWideMemo = 39
ftOraTimeStamp = 40
ftOraInterval = 41
ftLongWord = 42
ftShortint = 43
ftByte = 44
ftExtended = 45
ftConnection = 46
ftParams = 47
ftStream = 48
ftTimeStampOffset = 49
ftObject = 50
ftSingle = 51

### TFileDialogOption (Vcl.Dialogs)

fdoOverWritePrompt = 0
fdoStrictFileTypes = 1
fdoNoChangeDir = 2
fdoPickFolders = 3
fdoForceFileSystem = 4
fdoAllNonStorageItems = 5
fdoNoValidate = 6
fdoAllowMultiSelect = 7
fdoPathMustExist = 8
fdoFileMustExist = 9
fdoCreatePrompt = 10
fdoShareAware = 11
fdoNoReadOnlyReturn = 12
fdoNoTestFileCreate = 13
fdoHideMRUPlaces = 14
fdoHidePinnedPlaces = 15
fdoNoDereferenceLinks = 16
fdoDontAddToRecent = 17
fdoForceShowHidden = 18
fdoDefaultNoMiniMode = 19
fdoForcePreviewPaneOn = 20

### TFileDialogOverwriteResponse (Vcl.Dialogs)

forDefault = 0
forAccept = 1
forRefuse = 2

### TFileDialogShareViolationResponse (Vcl.Dialogs)

fsrDefault = 0
fsrAccept = 1
fsrRefuse = 2

### TFileEditStyle (Vcl.Dialogs)

fsEdit = 0
fsComboBox = 1

### TFilenameCaseMatch (System.SysUtils)

mkNone = 0
mkExactMatch = 1
mkSingleMatch = 2
mkAmbiguous = 3

### TFileOwnershipWarningLevel (RT_ClientServerInterface)

eFileOwnershipWarningLevel_None = 0
eFileOwnershipWarningLevel_Message = 1
eFileOwnershipWarningLevel_Dialog = 2

### TFilerFlag (System.Classes)

ffInherited = 0
ffChildPos = 1
ffInline = 2

### TFileSystemAttribute (System.SysUtils)

fsCaseSensitive = 0
fsCasePreserving = 1
fsLocal = 2
fsNetwork = 3
fsRemovable = 4
fsSymLink = 5

### TFileTimeType (Rt_Util)

eFTT_Created = 0
eFTT_Modified = 1
eFTT_Accessed = 2

### TFillStyle (Vcl.Graphics)

fsSurface = 0
fsBorder = 1

### TFilter (Vcl.Imaging.pngimage)

pfNone = 0
pfSub = 1
pfUp = 2
pfAverage = 3
pfPaeth = 4

### TFilterGroup (Data.Win.ADODB)

fgUnassigned = 0
fgNone = 1
fgPendingRecords = 2
fgAffectedRecords = 3
fgFetchedRecords = 4
fgPredicate = 5
fgConflictingRecords = 6

### TFilterKind (RT_Workspace)

eFilter_All = 0
eFilter_Documents = 1
eFilter_Projects = 2
eFilter_Workspaces = 3
eFilter_ProjectSource_PCB = 4
eFilter_ProjectSource_FPGA = 5
eFilter_ProjectSource_Core = 6
eFilter_ProjectSource_EMB = 7
eFilter_ProjectSource_ILB = 8
eFilter_ECOFiles = 9
eFilter_ProjectSource_SCR = 10
eFilter_ProjectSource_SystemDesign = 11
eFilter_ProjectSource_Harness = 12
eFilter_ProjectSource_HarnessDesign = 13

### TFilterOption (Data.DB)

foCaseInsensitive = 0
foNoPartialCompare = 1

### TFindItemKind (Vcl.Menus)

fkCommand = 0
fkHandle = 1
fkShortCut = 2

### TFindOption (Vcl.Dialogs)

frDown = 0
frFindNext = 1
frHideMatchCase = 2
frHideWholeWord = 3
frHideUpDown = 4
frMatchCase = 5
frDisableMatchCase = 6
frDisableUpDown = 7
frDisableWholeWord = 8
frReplace = 9
frReplaceAll = 10
frWholeWord = 11
frShowHelp = 12

### TFlattenMode (RT_Workspace)

eFlatten_Smart = 0
eFlatten_Flat = 1
eFlatten_Hierarchical_GlobalPorts = 2
eFlatten_Global = 3
eFlatten_Hierarchical_Strict = 4

### TFloatFormat (System.SysUtils)

ffGeneral = 0
ffExponent = 1
ffFixed = 2
ffNumber = 3
ffCurrency = 4

### TFloatSpecial (System)

fsZero = 0
fsNZero = 1
fsDenormal = 2
fsNDenormal = 3
fsPositive = 4
fsNegative = 5
fsInf = 6
fsNInf = 7
fsNaN = 8

### TFloatValue (System.SysUtils)

fvExtended = 0
fvCurrency = 1

### TFlowRunResult (Rt_NexusDevices)

eFlowRun_DidNotRun = 0
eFlowRun_Cancelled = 1
eFlowRun_Failure = 2
eFlowRun_Success = 3

### TFlowState (RT_Workspace)

eState_UpToDate = 0
eState_OutOfDate = 1
eState_Failed = 2
eState_Missing = 3
eState_Running = 4
eState_None = 5

### TFlowStyle (Vcl.ExtCtrls)

fsLeftRightTopBottom = 0
fsRightLeftTopBottom = 1
fsLeftRightBottomTop = 2
fsRightLeftBottomTop = 3
fsTopBottomLeftRight = 4
fsBottomTopLeftRight = 5
fsTopBottomRightLeft = 6
fsBottomTopRightLeft = 7

### TFontDialogDevice (Vcl.Dialogs)

fdScreen = 0
fdPrinter = 1
fdBoth = 2

### TFontDialogOption (Vcl.Dialogs)

fdAnsiOnly = 0
fdTrueTypeOnly = 1
fdEffects = 2
fdFixedPitchOnly = 3
fdForceFontExist = 4
fdNoFaceSel = 5
fdNoOEMFonts = 6
fdNoSimulations = 7
fdNoSizeSel = 8
fdNoStyleSel = 9
fdNoVectorFonts = 10
fdShowHelp = 11
fdWysiwyg = 12
fdLimitSize = 13
fdScalableOnly = 14
fdApplyButton = 15

### TFontPitch (System.UITypes)

fpDefault = 0
fpVariable = 1
fpFixed = 2

### TFontQuality (System.UITypes)

fqDefault = 0
fqDraft = 1
fqProof = 2
fqNonAntialiased = 3
fqAntialiased = 4
fqClearType = 5
fqClearTypeNatural = 6

### TFontQueryMode (RT_ClientServerInterface)

eGetFont = 0
eSetFont = 1

### TFontStyle (System.UITypes)

fsBold = 0
fsItalic = 1
fsUnderline = 2
fsStrikeOut = 3

### TFormBorderStyle (Vcl.Forms)

bsNone = 0
bsSingle = 1
bsSizeable = 2
bsDialog = 3
bsToolWindow = 4
bsSizeToolWin = 5

### TFormStyle (Vcl.Forms)

fsNormal = 0
fsMDIChild = 1
fsMDIForm = 2
fsStayOnTop = 3

### TFPGADisplayMode (RT_PCB)

peNone = 0
peIOBank = 1
peClkPin = 2
peIODiff = 3
peIOPin = 4

### TFPUPrecisionMode (System.Math)

pmSingle = 0
pmReserved = 1
pmDouble = 2
pmExtended = 3

### TFromToDisplayMode (RT_PCB)

eFromToDisplayMode_Automatic = 0
eFromToDisplayMode_Hide = 1
eFromToDisplayMode_Show = 2

### TFSMCodingStyle_DropDownList (RT_Workspace)

eFMSDropDownList_OneProcess = 0
eFMSDropDownList_TwoProcesses = 1
eFMSDropDownList_ThreeProcesses = 2

### TFSMEncodingStyle_DropDownList (RT_Workspace)

eFMSDropDownList_OneHot = 0
eFMSDropDownList_Binary = 1
eFMSDropDownList_Gray = 2

### TFSMStateShape (Rt_Schematic)

fsmEllipse = 0
fsmRectangle = 1
fsmRoundRect = 2
fsmParallelogram = 3
fsmDiamond = 4

### TFSMTransitionShape (Rt_Schematic)

tsBezier = 0
tsLine = 1
tsPolyline = 2

### TGaugeDrawMode (InstrumentGauges)

gdmPartial = 0
gdmHighlighted = 1
gdmFull = 2

### TGaugeNeedleKind (InstrumentGauges)

gnkPin = 0
gnkTearDrop = 1
gnkTrapezoid = 2

### TGeometryLayerType (RT_PCB)

rltStandart = 0
rltComponentTopSide = 1
rltComponentBottomSide = 2
rltBarrelsLayer = 3
rltArbitraryMeshLayer = 4
rltBoardPlaningLayer = 5
rltTopSolder = 6
rltBottomSolder = 7
rltTopOverlay = 8
rltBottomOverlay = 9
rltTopPaste = 10
rltBottomPaste = 11

### TGestureOption (Vcl.Controls)

goUniDirectional = 0
goSkew = 1
goEndpoint = 2
goRotate = 3

### TGestureType (Vcl.Controls)

gtStandard = 0
gtRecorded = 1
gtRegistered = 2
gtNone = 3

### TGetMode (Data.DB)

gmCurrent = 0
gmNext = 1
gmPrior = 2

### TGetResult (Data.DB)

grOK = 0
grBOF = 1
grEOF = 2
grError = 3

### TGlossEffort (RT_PCB)

eGlossEffort_None = 0
eGlossEffort_Weak = 1
eGlossEffort_Strong = 2

### TGradientPanelStyle (XPPanels)

gsLeftToRight = 0
gsTopToBottom = 1
gsTopShadow = 2

### TGraphicsCursor (RT_PCB)

eCurShapeCross90 = 0
eCurShapeBigCross = 1
eCurShapeCross45 = 2

### TGridDrawingStyle (Vcl.Grids)

gdsClassic = 0
gdsThemed = 1
gdsGradient = 2

### TGridOption (Vcl.Grids)

goFixedVertLine = 0
goFixedHorzLine = 1
goVertLine = 2
goHorzLine = 3
goRangeSelect = 4
goDrawFocusSelected = 5
goRowSizing = 6
goColSizing = 7
goRowMoving = 8
goColMoving = 9
goEditing = 10
goTabs = 11
goRowSelect = 12
goAlwaysShowEditor = 13
goThumbTracking = 14
goFixedColClick = 15
goFixedRowClick = 16
goFixedHotTrack = 17

### TGridState (Vcl.Grids)

gsNormal = 0
gsSelecting = 1
gsRowSizing = 2
gsColSizing = 3
gsRowMoving = 4
gsColMoving = 5

### TGroupPosInd (Data.DB)

gbFirst = 0
gbMiddle = 1
gbLast = 2

### THandshaking (RT_PCB)

eHandshakingNone = 0
eHandshakingXonXOff = 1
eHandshakingHardwire = 2

### THarnessLayoutConnectionPointStyle (Rt_Schematic)

eHLCCircle = 0
eHLCSquare = 1
eHLInsulator = 2

### THarnessShieldStyle (Rt_Schematic)

eShield = 0
eShieldWithConnection = 1

### THarnessSpliceStyle (Rt_Schematic)

eCircle = 0
eInline = 1

### THDLLibCategory (Rt_VHDL)

eHDLLibCategory_Simulation = 0
eHDLLibCategory_Synthesis = 1
eHDLLibCategory_SimulationAndSynthesis = 2

### THDLLibCommand (Rt_VHDL)

eHDLLibCommand_AddFile = 0
eHDLLibCommand_RemoveFile = 1
eHDLLibCommand_MoveFileUp = 2
eHDLLibCommand_MoveFileDown = 3
eHDLLibCommand_EditFile = 4
eHDLLibCommand_CompileFile = 5
eHDLLibCommand_CompileLibrary = 6
eHDLLibCommand_UseAbsolutePath = 7

### THeaderSectionStyle (Vcl.ComCtrls)

hsText = 0
hsOwnerDraw = 1

### THeaderStyle (Vcl.ComCtrls)

hsButtons = 0
hsFlat = 1

### THealthCheckId (RT_PCB)

eHealthCheckBrokenRule = 0
eHealthCheckBrokenXSignals = 1
eHealthCheckLayerIndicesDisorder = 2
eHealthCheckMicrosegmentsGraphics = 3
eHealthCheckPadHoleLength = 4
eHealthCheckComponentRotation360 = 5
eHealthCheckSelfIntersections = 6
eHealthCheckReferencePointOutsideArea = 7
eHealthCheckComponentOnNonSignalLayer = 8
eHealthCheckEmbeddedBoardIncompatibleStack = 9
eHealthCheckZeroAreaRegions = 10
eHealthCheckDuplicatedComponentDesignators = 11
eHealthCheckViaNoDrillSpan = 12
eHealthCheckAbsentTTFont = 13
eHealthCheckShelvedPolygon = 14
eHealthCheckMicrosegmentsBoard = 15
eHealthCheckMicrosegmentsCopper = 16
eHealthCheckUnusedxSignals = 17
eHealthCheckUnusedFromTos = 18
eHealthCheckZeroAreaPolygons = 19

### THelpType (System.Classes)

htKeyword = 0
htContext = 1

### THighLevelCodeDataType (Rt_Schematic)

eHighLevelCodeDataType_SignedInteger = 0
eHighLevelCodeDataType_UnsignedInteger = 1
eHighLevelCodeDataType_FloatingPoint = 2
eHighLevelCodeDataType_Boolean = 3
eHighLevelCodeDataType_Void = 4

### THighLevelCodeEntryRole (Rt_Schematic)

eHighLevelCodeEntryRole_Unknown = 0
eHighLevelCodeEntryRole_Input = 1
eHighLevelCodeEntryRole_Output = 2
eHighLevelCodeEntryRole_Address = 3
eHighLevelCodeEntryRole_Select = 4
eHighLevelCodeEntryRole_WriteEnable = 5

### THighLevelCodeEntryType (Rt_Schematic)

eHighLevelCodeEntryType_Parameter = 0
eHighLevelCodeEntryType_Control = 1
eHighLevelCodeEntryType_Variable = 2

### THighLevelCodeInterfaceMode (Rt_Schematic)

eHighLevelCodeInterfaceMode_Combinatorial = 0
eHighLevelCodeInterfaceMode_MultiCycle = 1
eHighLevelCodeInterfaceMode_Wishbone = 2
eHighLevelCodeInterfaceMode_ASP = 3

### THighLevelCodeScope (Rt_Schematic)

eHighLevelCodeScope_Unknown = 0
eHighLevelCodeScope_Import = 1
eHighLevelCodeScope_Export = 2

### THighlightMethod (RT_Workspace)

eHighlight_Filter = 0
eHighlight_Zoom = 1
eHighlight_Select = 2
eHighlight_Graph = 3
eHighlight_Dim = 4
eHighlight_Thicken = 5
eHighlight_ZoomCursor = 6
eHighlight_ForceSmooth = 7

### THitTest (Vcl.ComCtrls)

htAbove = 0
htBelow = 1
htNowhere = 2
htOnItem = 3
htOnButton = 4
htOnIcon = 5
htOnIndent = 6
htOnLabel = 7
htOnRight = 8
htOnStateIcon = 9
htToLeft = 10
htToRight = 11

### THitTestMode (Rt_Schematic)

eHitTest_AllObjects = 0
eHitTest_OnlyAccessible = 1

### THitTestResult (Rt_Schematic)

eHitTest_Fail = 0
eHitTest_NoAction = 1
eHitTest_Move = 2
eHitTest_InPlaceEdit = 3
eHitTest_CopyPaste = 4
eHitTest_Resize_Any = 5
eHitTest_Resize_EndAngle = 6
eHitTest_Resize_StartAngle = 7
eHitTest_Resize_SecondaryRadius = 8
eHitTest_Resize_Radius = 9
eHitTest_Resize_CornerTopLeft = 10
eHitTest_Resize_CornerTopRight = 11
eHitTest_Resize_CornerBottomRight = 12
eHitTest_Resize_CornerBottomLeft = 13
eHitTest_Resize_SideLeft = 14
eHitTest_Resize_SideRight = 15
eHitTest_Resize_SideTop = 16
eHitTest_Resize_SideBottom = 17
eHitTest_Resize_Vertical = 18
eHitTest_Resize_Horizontal = 19
eHitTest_Resize_SE_NW = 20
eHitTest_Resize_SW_NE = 21
eHitTest_Resize_VerticalFromOrigin = 22
eHitTest_Resize_HorizontalFromOrigin = 23
eHitTest_Resize_HarnessConnectorPrimaryLeft = 24
eHitTest_Resize_HarnessConnectorPrimaryRight = 25
eHitTest_Resize_HarnessConnectorPrimaryTop = 26
eHitTest_Resize_HarnessConnectorPrimaryBottom = 27

### THKInvalidKey (Vcl.ComCtrls)

hcNone = 0
hcShift = 1
hcCtrl = 2
hcAlt = 3
hcShiftCtrl = 4
hcShiftAlt = 5
hcCtrlAlt = 6
hcShiftCtrlAlt = 7

### THKModifier (Vcl.ComCtrls)

hkShift = 0
hkCtrl = 1
hkAlt = 2
hkExt = 3

### THorizontalAlign (Rt_Schematic)

eHorizontalCentreAlign = 0
eLeftAlign = 1
eRightAlign = 2

### THuggingStyle (RT_PCB)

eStyleMixed = 0
eStyleRounded = 1
eStyleDegrees = 2

### TIconArrangement (Vcl.ComCtrls)

iaTop = 0
iaLeft = 1

### TIeeeSymbol (Rt_Schematic)

eNoSymbol = 0
eDot = 1
eRightLeftSignalFlow = 2
eClock = 3
eActiveLowInput = 4
eAnalogSignalIn = 5
eNotLogicConnection = 6
eShiftRight = 7
ePostPonedOutput = 8
eOpenCollector = 9
eHiz = 10
eHighCurrent = 11
ePulse = 12
eSchmitt = 13
eDelay = 14
eGroupLine = 15
eGroupBin = 16
eActiveLowOutput = 17
ePiSymbol = 18
eGreaterEqual = 19
eLessEqual = 20
eSigma = 21
eOpenCollectorPullUp = 22
eOpenEmitter = 23
eOpenEmitterPullUp = 24
eDigitalSignalIn = 25
eAnd = 26
eInvertor = 27
eOr = 28
eXor = 29
eShiftLeft = 30
eInputOutput = 31
eOpenCircuitOutput = 32
eLeftRightSignalFlow = 33
eBidirectionalSignalFlow = 34
eInternalPullUp = 35
eInternalPullDown = 36

### TImageAlignment (Vcl.StdCtrls)

iaLeft = 0  // 脚本里是 1
iaRight = 1
iaTop = 2  // 脚本里是 0
iaBottom = 3
iaCenter = 4

### TImageType (Vcl.ImgList)

itImage = 0
itMask = 1

### TImeMode (Vcl.Controls)

imDisable = 0
imClose = 1
imOpen = 2
imDontCare = 3
imSAlpha = 4
imAlpha = 5
imHira = 6
imSKata = 7
imKata = 8
imChinese = 9
imSHanguel = 10
imHanguel = 11

### TIndexOption (Data.DB)

ixPrimary = 0
ixUnique = 1
ixDescending = 2
ixCaseInsensitive = 3
ixExpression = 4
ixNonMaintained = 5

### TInputSignalVisualKind (RT_Digital_IO)

iskLED = 0
iskNumeric = 1
isk7Segment = 2
iskBar = 3
iskGauge = 4
iskNone = 5

### TInstrumentAction (RT_CustomInstrument)

iaShow = 0
iaHide = 1

### TInstrumentCheckStyle (InstrumentTypes)

icsMixed = 0
icsRed = 1
icsGreen = 2
icsButton = 3
icsRectAmber = 4
icsRectBlue = 5
icsRectGreen = 6
icsRectPurple = 7
icsRectRed = 8
icsRectYellow = 9
icsAmber = 10
icsBlue = 11
icsPurple = 12
icsYellow = 13
icsWhite = 14

### TInstrumentKnobColor (InstrumentSliders)

ikcBlack = 0
ikcBlue = 1
ikcGreen = 2
ikcRed = 3
ikcYellow = 4

### TInstrumentKnobStyle (InstrumentSliders)

iksStandard = 0
iksX50B = 1
iksX80A = 2
iksX80B = 3

### TInstrumentLEDStyle (InstrumentButtons)

ilsCustom = 0
ilsWhite = 1
ilsRed = 2
ilsGreen = 3
ilsBlue = 4
ilsYellow = 5
ilsAmber = 6
ilsPurple = 7

### TInstrumentPanelStyle (InstrumentTypes)

ipsMidGray = 0
ipsLightGray = 1
ipsDarkGray = 2
ipsDarkRed = 3
ipsOliveGreen = 4
ipsBlueGreen = 5
ipsBronze = 6
ipsBlueGray = 7
ipsGreen = 8
ipsBlue = 9
ipsGrayLilac = 10
ipsGrayOrange = 11
ipsGrayBlue = 12

### TInstrumentSide (InstrumentTypes)

isdLeftOrTop = 0
isdRightOrBottom = 1

### TInstrumentSize (InstrumentTypes)

isSmall = 0
isMedium = 1
isLarge = 2

### TInteractiveGesture (Vcl.Controls)

igZoom = 0
igPan = 1
igRotate = 2
igTwoFingerTap = 3
igPressAndTap = 4

### TInteractiveGestureFlag (Vcl.Controls)

gfBegin = 0
gfInertia = 1
gfEnd = 2

### TInteractiveGestureOption (Vcl.Controls)

igoPanSingleFingerHorizontal = 0
igoPanSingleFingerVertical = 1
igoPanInertia = 2
igoPanGutter = 3
igoParentPassthrough = 4

### TInteractiveRouteMode (RT_PCB)

eIgnoreObstacle = 0
eAvoidObstacle = 1
ePushObstacle = 2

### TInterlaceMethod (Vcl.Imaging.pngimage)

imNone = 0
imAdam7 = 1

### TIsolationLevel (Data.Win.ADODB)

ilUnspecified = 0
ilChaos = 1
ilReadUncommitted = 2
ilBrowse = 3
ilCursorStability = 4
ilReadCommitted = 5
ilRepeatableRead = 6
ilSerializable = 7
ilIsolated = 8

### TItemChange (Vcl.ComCtrls)

ctText = 0
ctImage = 1
ctState = 2

### TItemFind (Vcl.ComCtrls)

ifData = 0
ifPartialString = 1
ifExactString = 2
ifNearest = 3

### TItemRequests (Vcl.ComCtrls)

irText = 0
irImage = 1
irParam = 2
irState = 3
irIndent = 4

### TItemState (Vcl.ComCtrls)

isNone = 0
isCut = 1
isDropHilited = 2
isFocused = 3
isSelected = 4
isActivating = 5

### TIterationDepth (Rt_Schematic)

eIterateFirstLevel = 0
eIterateFilteredLevels = 1
eIterateAllLevels = 2

### TIterationMethod (Pcbtypes)

eProcessAll = 0
eProcessFree = 1
eProcessComponent = 2

### TIterationMethod (RT_PCB)

eProcessAll = 0
eProcessFree = 1
eProcessComponent = 2

### TJavascriptAction (RT_ClientServerInterface)

jsaNone = 0
jsaExecute = 1

### TJunctionConversionKind (Rt_Schematic)

jckLockAllAutoJunctions = 0
jckLockXJunctionsOnly = 1
jckConvertXJunctions = 2

### TKeepoutObj (RT_PCB)

eKeepout_Via = 0
eKeepout_Track = 1
eKeepout_Copper = 2
eKeepout_SMDPad = 3
eKeepout_THPad = 4

### TLabelPosition (Vcl.ExtCtrls)

lpAbove = 0
lpBelow = 1
lpLeft = 2
lpRight = 3

### TLayerClassID (RT_PCB)

eLayerClass_All = 0
eLayerClass_Mechanical = 1
eLayerClass_Physical = 2
eLayerClass_Electrical = 3
eLayerClass_Dielectric = 4
eLayerClass_Signal = 5
eLayerClass_InternalPlane = 6
eLayerClass_SolderMask = 7
eLayerClass_Overlay = 8
eLayerClass_PasteMask = 9

### TLayerConstant (RT_PCB)

cNoLayer = 0
cIgnoreLayer = 1
cTopLayer = 2
cMidLayer1 = 3
cMidLayer2 = 4
cMidLayer3 = 5
cMidLayer4 = 6
cMidLayer5 = 7
cMidLayer6 = 8
cMidLayer7 = 9
cMidLayer8 = 10
cMidLayer9 = 11
cMidLayer10 = 12
cMidLayer11 = 13
cMidLayer12 = 14
cMidLayer13 = 15
cMidLayer14 = 16
cMidLayer15 = 17
cMidLayer16 = 18
cMidLayer17 = 19
cMidLayer18 = 20
cMidLayer19 = 21
cMidLayer20 = 22
cMidLayer21 = 23
cMidLayer22 = 24
cMidLayer23 = 25
cMidLayer24 = 26
cMidLayer25 = 27
cMidLayer26 = 28
cMidLayer27 = 29
cMidLayer28 = 30
cMidLayer29 = 31
cMidLayer30 = 32
cBottomLayer = 33
cTopOverlay = 34
cBottomOverlay = 35
cTopPaste = 36
cBottomPaste = 37
cTopSolder = 38
cBottomSolder = 39
cInternalPlane1 = 40
cInternalPlane2 = 41
cInternalPlane3 = 42
cInternalPlane4 = 43
cInternalPlane5 = 44
cInternalPlane6 = 45
cInternalPlane7 = 46
cInternalPlane8 = 47
cInternalPlane9 = 48
cInternalPlane10 = 49
cInternalPlane11 = 50
cInternalPlane12 = 51
cInternalPlane13 = 52
cInternalPlane14 = 53
cInternalPlane15 = 54
cInternalPlane16 = 55
cDrillGuide = 56
cKeepOutLayer = 57
cMechanical1 = 58
cMechanical2 = 59
cMechanical3 = 60
cMechanical4 = 61
cMechanical5 = 62
cMechanical6 = 63
cMechanical7 = 64
cMechanical8 = 65
cMechanical9 = 66
cMechanical10 = 67
cMechanical11 = 68
cMechanical12 = 69
cMechanical13 = 70
cMechanical14 = 71
cMechanical15 = 72
cMechanical16 = 73
cDrillDrawing = 74
cMultiLayer = 75
cConnectLayer = 76
cBackGroundLayer = 77
cDRCErrorLayer = 78
cDRCDetailLayer = 79
cHighlightLayer = 80
cGridColor1 = 81
cGridColor10 = 82
cPadHoleLayer = 83
cViaHoleLayer = 84
cTopPadMasterPlot = 85
cBottomPadMasterPlot = 86
cV7_MidLayers = 87
cAllLayers = 88
cSignalLayers = 89
cInternalPlaneLayers = 90
cElectricalLayers = 91
cMechanicalLayers = 92
cDielectricLayers = 93

### TLayerNameDisplayMode (RT_PCB)

eLayerNameDisplay_Short = 0
eLayerNameDisplay_Medium = 1
eLayerNameDisplay_Long = 2

### TLayerPartition (RT_PCB)

eV7_NoLayer = 0
eV7_TopLayer = 1
eMidLayers = 2
eV7_BottomLayer = 3
eInternalPlaneLayers = 4
eMechanicalLayers = 5
eV7_TopOverlay = 6
eV7_BottomOverlay = 7
eV7_TopPaste = 8
eV7_BottomPaste = 9
eV7_TopSolder = 10
eV7_BottomSolder = 11
eV7_DrillGuide = 12
eV7_KeepOutLayer = 13
eV7_DrillDrawing = 14
eV7_MultiLayer = 15
eV7_ConnectLayer = 16
eV7_BackGroundLayer = 17
eV7_DRCErrorLayer = 18
eV7_HighlightLayer = 19
eV7_GridColor1 = 20
eV7_GridColor10 = 21
eV7_PadHoleLayer = 22
eV7_ViaHoleLayer = 23
eV7_TopPadMasterPlot = 24
eV7_BottomPadMasterPlot = 25
eV7_DRCDetailLayer = 26
eMidDielectricLayers = 27
eTopCoverlayOutlineLayers = 28
eBottomCoverlayOutlineLayers = 29

### TLayerStackDocumentFormat (Rt_LayerStackManager.Interfaces)

dfDefault = 0
dfXml = 1
dfXmlExt = 2

### TLayerStackStyle (RT_PCB)

eLayerStack_Pairs = 0
eLayerStacks_InsidePairs = 1
eLayerStackBuildup = 2
eLayerStackCustom = 3

### TLayerStackType (RT_PCB)

eBoardLayerStack = 0
eBoardRegionLayerStack = 1

### TLEDClickAction (InstrumentChecks)

lcaNone = 0
lcaToggle = 1
lcaRadioButton = 2

### TLEDColorScheme (InstrumentTypes)

lcsCustom = 0
lcsRed = 1
lcsGreen = 2
lcsOrange = 3
lcsBlack = 4
lcsBlue = 5
lcsPurple = 6
lcsYellow = 7
lcsWhite = 8

### TLeftRightSide (Rt_Schematic)

eLeftSide = 0
eRightSide = 1
eTopSide = 2
eBottomSide = 3

### TLengthenerStyle (RT_PCB)

eLengthenerStyle_90 = 0
eLengthenerStyle_45 = 1
eLengthenerStyle_Round = 2
eLengthenerStyle_Mitered90 = 3

### TLibIdentifierKind (RT_Library)

eLibIdentifierKind_Any = 0
eLibIdentifierKind_NameNoType = 1
eLibIdentifierKind_NameWithType = 2
eLibIdentifierKind_FullPath = 3
eLibIdentifierKind_VaultName = 4

### TLibraryScope (RT_Workspace)

lsCurrentComponnet = 0
lsAllComponents = 1

### TLibrarySource (RT_Library)

eLibSrc_Undefined = 0
eLibSrc_File = 1
eLibSrc_Vault = 2

### TLibraryType (RT_IntegratedLibrary)

eLibIntegrated = 0
eLibSource = 1
eLibDatafile = 2
eLibDatabase = 3
eLibNone = 4
eLibQuery = 5
eLibAltium = 6
eLibDesignItems = 7
eLibVault = 8
eLibSimLib = 9
eLibSimMdl = 10
eLibSimCkt = 11
eLibSimCir = 12

### TLineShape (Rt_Schematic)

eLineShapeNone = 0
eLineShapeArrow = 1
eLineShapeSolidArrow = 2
eLineShapeTail = 3
eLineShapeSolidTail = 4
eLineShapeCircle = 5
eLineShapeSquare = 6

### TLineStyle (Rt_Schematic)

eLineStyleSolid = 0
eLineStyleDashed = 1
eLineStyleDotted = 2
eLineStyleDashDotted = 3

### TListArrangement (Vcl.ComCtrls)

arAlignBottom = 0
arAlignLeft = 1
arAlignRight = 2
arAlignTop = 3
arDefault = 4  // 脚本里是 2
arSnapToGrid = 5

### TListAssignOp (System.Classes)

laCopy = 0
laAnd = 1
laOr = 2
laXor = 3
laSrcUnique = 4
laDestUnique = 5

### TListBoxStyle (Vcl.StdCtrls)

lbStandard = 0
lbOwnerDrawFixed = 1
lbOwnerDrawVariable = 2
lbVirtual = 3
lbVirtualOwnerDraw = 4

### TListGroupState (Vcl.ComCtrls)

lgsNormal = 0
lgsHidden = 1
lgsCollapsed = 2
lgsNoHeader = 3
lgsCollapsible = 4
lgsFocused = 5
lgsSelected = 6
lgsSubseted = 7
lgsSubSetLinkFocused = 8

### TListHotTrackStyle (Vcl.ComCtrls)

htHandPoint = 0
htUnderlineCold = 1
htUnderlineHot = 2

### TListItemsSortType (Vcl.ListActns)

stNone = 0
stData = 1
stText = 2
stBoth = 3

### TListNotification (System.Classes)

lnAdded = 0
lnExtracted = 1
lnDeleted = 2

### TLiveHighlightMode (RT_ClientServerInterface)

eLiveHighlightMode_None = 0
eLiveHighlightMode_Low = 1
eLiveHighlightMode_High = 2

### TLoadResource (Vcl.ImgList)

lrDefaultColor = 0
lrDefaultSize = 1
lrFromFile = 2
lrMap3DColors = 3
lrTransparent = 4
lrMonoChrome = 5

### TLocalComparisonDocumentType (RT_ClientServerInterface)

lcdtSchematic = 0
lcdtPCB = 1
lcdtBOM = 2

### TLocalComparisonRevisionType (RT_ClientServerInterface)

lcrtCommit = 0
lcrtRelease = 1

### TLocalTimeType (System.DateUtils)

lttStandard = 0
lttDaylight = 1
lttAmbiguous = 2
lttInvalid = 3

### TLocateOption (Data.DB)

loCaseInsensitive = 0
loPartialKey = 1

### TLogicSimDataTypeID (Rt_VHDL)

eIDArrayType = 0
eIDUnconstrainedArrayType = 1
eIDRecordType = 2
eIDEnumType = 3
eIDBitType = 4
eIDRealType = 5
eIDCharacterType = 6
eIDIntegerType = 7
eIDStringType = 8
eIDAccessType = 9
eIDTimeType = 10
eIDUnknownType = 11

### TLogicSimRadix (Rt_VHDL)

eRadixDecimal = 0
eRadixBinary = 1
eRadixHex = 2
eRadixDefault = 3
eRadixNone = 4

### TLsmSdkComponentPlacement (Rt_LayerStackManager.Interfaces)

LsmComponentPlacement_None = 0
LsmComponentPlacement_BodyUp = 1
LsmComponentPlacement_BodyDown = 2

### TLsmSdkCopperOrientation (Rt_LayerStackManager.Interfaces)

LsmCopperOrientation_Above = 0
LsmCopperOrientation_Below = 1

### TLsmSdkDrillSpanType (Rt_LayerStackManager.Interfaces)

LsmDrillSpanType_Unspecified = 0
LsmDrillSpanType_BackDrill = 1

### TLsmSdkImpedanceProfileType (Rt_LayerStackManager.Interfaces)

LsmTLImpedance_Single = 0
LsmTLImpedance_Differential = 1
LsmTLImpedance_SingleCoplanar = 2
LsmTLImpedance_DifferentialCoplanar = 3

### TLsmSdkLengthUnit (Rt_LayerStackManager.Interfaces)

LsmSdkLengthUnit_Unknown = 0
LsmSdkLengthUnit_Mils = 1
LsmSdkLengthUnit_Inches = 2
LsmSdkLengthUnit_Millimeters = 3
LsmSdkLengthUnit_Centimeters = 4
LsmSdkLengthUnit_Meters = 5

### TLsmSdkRoughnessModelType (Rt_LayerStackManager.Interfaces)

LsmTLRoughnessModel_NoRoughness = 0
LsmTLRoughnessModel_MHammerstad = 1
LsmTLRoughnessModel_HuraySnowball = 2
LsmTLRoughnessModel_MGroiss = 3
LsmTLRoughnessModel_Hemispherical = 4
LsmTLRoughnessModel_HurayBracken = 5

### TLsmSdkStackupSymmetricOptions (Rt_LayerStackManager.Interfaces)

LsmStackup_MirrorTopHalfDown = 0
LsmStackup_MirrorBottomHalfUp = 1
LsmStackup_MirrorAllDown = 2
LsmStackup_MirrorAllUp = 3

### TLsmSdkStackupType (Rt_LayerStackManager.Interfaces)

LsmStackup_Standard = 0
LsmStackup_Printed = 1

### TLsmSdkTLCalcMode (Rt_LayerStackManager.Interfaces)

LsmTLCalcMode_Manual = 0
LsmTLCalcMode_TraceWidth = 1
LsmTLCalcMode_TraceClearance = 2
LsmTLCalcMode_Impedance = 3

### TLsmSdkViaSpanType (Rt_LayerStackManager.Interfaces)

LsmViaSpanType_ThruVia = 0
LsmViaSpanType_BlindVia = 1
LsmViaSpanType_BuriedVia = 2
LsmViaSpanType_StackedMicroVia = 3
LsmViaSpanType_SkipMicroVia = 4

### TMacroManagerState (RT_ClientServerInterface)

mmsIdle = 0
mmsPlaying = 1
mmsRecording = 2

### TMarshalOption (Data.Win.ADODB)

moMarshalAll = 0
moMarshalModifiedOnly = 1

### TMaskExpansionMode (RT_PCB)

eMaskExpansionMode_NoMask = 0
eMaskExpansionMode_Rule = 1
eMaskExpansionMode_Manual = 2

### TMatchFileNameKind (Rt_Util)

eMatchByPath = 0
eMatchByFileName = 1

### TMaterialHatchStyle (RT_PCB)

hsNone = 0
hsVertical = 1
hsHorizontal = 2
hsDiagMain = 3
hsDiagSecond = 4
hsCross = 5
hsLocked = 6

### TMBAExport3DFormat (RT_MBA)

eSTEP = 0
ePARASOLID = 1
ePDF = 2

### TMbcsByteType (System.SysUtils)

mbSingleByte = 0
mbLeadByte = 1
mbTrailByte = 2

### TMeasureMode (RT_FrequencyCounter)

eMeasureMode_Frequency = 0
eMeasureMode_Period = 1
eMeasureMode_Count = 2

### TMeasureUnit (Rt_Util)

cUnitMil = 0
cUnitMM = 1
cUnitIN = 2
cUnitCM = 3
cUnitDXP = 4
cUnitM = 5

### TMechanicalLayerKind (RT_PCB)

mlUndefined = 0
mlAssemblyTop = 1
mlAssemblyBottom = 2
mlAssemblyNotes = 3
mlBoard = 4
mlCoatingTop = 5
mlCoatingBottom = 6
mlComponentCenterTop = 7
mlComponentCenterBottom = 8
mlComponentOutlineTop = 9
mlComponentOutlineBottom = 10
mlCourtyardTop = 11
mlCourtyardBottom = 12
mlDesignatorTop = 13
mlDesignatorBottom = 14
mlDimensions = 15
mlDimensionsTop = 16
mlDimensionsBottom = 17
mlFabNotes = 18
mlGluePointsTop = 19
mlGluePointsBottom = 20
mlGoldPlatingTop = 21
mlGoldPlatingBottom = 22
mlValueTop = 23
mlValueBottom = 24
mlVCut = 25
ml3DBodyTop = 26
ml3DBodyBottom = 27
mlRouteToolPath = 28
mlSheet = 29
mlBoardShape = 30
mlOverlayTop = 31
mlOverlayBottom = 32
mlSolderTop = 33
mlSolderBottom = 34
mlPasteTop = 35
mlPasteBottom = 36
mlTentingTop = 37
mlTentingBottom = 38
mlCoveringTop = 39
mlCoveringBottom = 40
mlPluggingTop = 41
mlPluggingBottom = 42
mlFilling = 43
mlCapping = 44

### TMechanicalLayerPairKind (RT_PCB)

mlpUndefined = 0
mlpAssembly = 1
mlpCoating = 2
mlpComponentCenter = 3
mlpComponentOutline = 4
mlpCourtyard = 5
mlpDesignator = 6
mlpDimensions = 7
mlpGluePoints = 8
mlpGoldPlating = 9
mlpValue = 10
mlp3DBody = 11
mlpOverlay = 12
mlpSolder = 13
mlpPaste = 14
mlpTenting = 15
mlpCovering = 16
mlpPlugging = 17

### TMemoryInterfaceType (Rt_Schematic)

eMemoryInterface_None = 0
eMemoryInterface_Wishbone = 1
eMemoryInterface_SinglePort = 2
eMemoryInterface_DualPort = 3
eMemoryInterface_TrueDualPort = 4

### TMemoryKind (Rt_NexusDevices)

eMemoryKind_Program = 0
eMemoryKind_Data = 1

### TMenuAnimations (Vcl.Menus)

maLeftToRight = 0
maRightToLeft = 1
maTopToBottom = 2
maBottomToTop = 3
maNone = 4

### TMenuBreak (Vcl.Menus)

mbNone = 0
mbBreak = 1
mbBarBreak = 2

### TMenuItemAutoFlag (Vcl.Menus)

maAutomatic = 0
maManual = 1
maParent = 2

### TMessageKind (Rt_VHDL)

cGenericMsg = 0
cCompilerMsg = 1
cWarningMsg = 2
cErrorMsg = 3
cFatalMsg = 4
cConstraintMsg = 5
cOutputMsg = 6
cReportMsg = 7
cVitalNoteMsg = 8
cVitalWarningMsg = 9
cVitalErrorMsg = 10
cVitalFailureMsg = 11

### TMinimumBlockAlignment (System)

mba8Byte = 0
mba16Byte = 1

### TMirrorOperation (RT_PCB)

eHMirror = 0
eVMirror = 1

### TModelDisplayMode (RT_PCB)

dmSolid = 0
dmTransparent = 1
dmWireframe = 2
dmHide = 3
dmNotAssigned = 4

### TModelEditContext (RT_IntegratedLibrary)

eModelEditContext_Schematic = 0
eModelEditContext_Library = 1
eModelEditContext_AltiumLibrary = 2
eModelEditContext_DesignItemManager = 3

### TModelSource (RT_PCB)

eModelSource_Undefined = 0
eModelSource_File = 1
eModelsource_Vault = 2

### TModificationKind (RT_Workspace)

eModification_Unknown = 0
eModification_RemoveNode = 1
eModification_RemoveComponentClassMember = 2
eModification_RemoveNetClassMember = 3
eModification_RemoveChannelClassMember = 4
eModification_RemoveRule = 5
eModification_RemoveNet = 6
eModification_RemoveComponent = 7
eModification_ChangeComponentFootPrint = 8
eModification_ChangeComponentComment = 9
eModification_ChangeComponentDesignator = 10
eModification_ChangeComponentKind = 11
eModification_AnnotateComponent = 12
eModification_AddComponent = 13
eModification_ChangeNetName = 14
eModification_AddNet = 15
eModification_AddNode = 16
eModification_RemoveComponentClass = 17
eModification_RemoveNetClass = 18
eModification_RemoveDifferentialPair = 19
eModification_RemoveChannelClass = 20
eModification_ChangeComponentClassName = 21
eModification_ChangeNetClassName = 22
eModification_ChangeDifferentialPairPositiveNetName = 23
eModification_ChangeDifferentialPairNegativeNetName = 24
eModification_ChangeChannelClassName = 25
eModification_AddComponentClass = 26
eModification_AddNetClass = 27
eModification_AddDifferentialPair = 28
eModification_AddChannelClass = 29
eModification_AddComponentClassMember = 30
eModification_AddNetClassMember = 31
eModification_AddChannelClassMember = 32
eModification_RemoveRoom = 33
eModification_ChangeRoom = 34
eModification_AddRoom = 35
eModification_AddParameter = 36
eModification_RemoveParameter = 37
eModification_ChangeParameterName = 38
eModification_ChangeParameterValue = 39
eModification_ChangeParameterType = 40
eModification_AddRule = 41
eModification_ChangeRule = 42
eModification_FullPartUpdate = 43
eModification_UpdatePartSymbol = 44
eModification_UpdateImplementationValues = 45
eModification_AddImplementation = 46
eModification_RemoveImplementation = 47
eModification_UpdateCurrentImplementation = 48
eModification_ChangePinName = 49
eModification_ChangePinElectrical = 50
eModification_ChangePortElectrical = 51
eModification_SwapPin = 52
eModification_ChangePinSwapId_Pin = 53
eModification_AddConstraintGroup = 54
eModification_RemoveConstraintGroup = 55
eModification_AddPort = 56
eModification_RemovePort = 57
eModification_ChangePortName = 58
eModification_ChangeComponentLibRef = 59
eModification_ChangePin = 60
eModification_ChangePhysicalFootPrint = 61
eModification_ChangeSubPartID = 62
eModification_ChangeLibraryReference = 63
eModification_AnnotatePhysicalComponent = 64
eModification_FullDeviceSheetUpdate = 65
eModification_ChangeComponentDescription = 66
eModification_ChangeComponentLibrary = 67
eModification_AddClusterClass = 68
eModification_AddClusterClassMember = 69
eModification_RemoveClusterClass = 70
eModification_RemoveClusterClassMember = 71
eModification_ChangeClassClusterClassName = 72
eModification_ChangeComponentConfigurableParameters = 73
eModification_ChangeNoERC = 74
eModification_ChangeComponentVaultGUID = 75
eModification_ChangeComponentItemGUID = 76
eModification_ChangeComponentRevisionGUID = 77
eModification_ChangeNetColor = 78
eModification_ChangePinPackageLength = 79
eModification_AddFunctionalBlock = 80
eModification_RemoveFunctionalBlock = 81
eModification_ChangeFunctionalBlock = 82
eModification_AddDiagramPin = 83
eModification_RemoveDiagramPin = 84
eModification_ChangeDiagramPin = 85
eModification_AddMBAEmbeddedDocument = 86
eModification_RemoveMBAEmbeddedDocument = 87
eModification_ChangeMBAEmbeddedDocument = 88
eModification_ChangeComponentParameters = 89
eModification_AddSystemDesignModule = 90
eModification_RemoveSystemDesignModule = 91
eModification_ChangeSystemDesignModuleProperties = 92
eModification_AddSystemDesignModuleConnector = 93
eModification_RemoveSystemDesignModuleConnector = 94
eModification_ChangeSystemDesignModuleConnector = 95
eModification_AddSystemDesignConnection = 96
eModification_RemoveSystemDesignConnection = 97
eModification_ChangeSystemDesignConnection = 98
eModification_ChangeSystemDesignModuleFileName = 99
eModification_ChangeSystemDesignFunctionalBlock = 100
eModification_AddPin = 101
eModification_RemovePin = 102
eModification_AddSystemDesignPinToNet = 103
eModification_RemoveSystemDesignPinFromNet = 104
eModification_ChangeSystemDesignPinNetName = 105
eModification_SystemDesignPinSwap = 106
eModification_ChangeSystemDesignPhysicalConnection = 107
eModification_AddSystemDesignPhysicalConnection = 108
eModification_RemoveSystemDesignPhysicalConnection = 109
eModification_ChangeSystemDesignPin = 110
eModification_DifferentialPairClassAdd = 111
eModification_DifferentialPairClassRemove = 112
eModification_DifferentialPairClassChangeName = 113
eModification_DifferentialPairClassMemberAdd = 114
eModification_DifferentialPairClassMemberRemove = 115
eModification_ChangeComponentLocation = 116
eModification_ChangeManagedComponentLibraryLink = 117
eModification_ChangePinPropagationDelay = 118
eModification_ChangeFootprintParameters = 119

### TModificationStatus (RT_Workspace)

eStatusNone = 0
eStatusIsSupported = 1
eStatusIsNotSupported = 2
eStatusPassedVerification = 3
eStatusFailedVerification = 4
eStatusPassedExecution = 5
eStatusFailedExecution = 6

### TModuleType (Rt_NexusDevices)

eModuleType_RAM_SinglePortBlock = 0
eModuleType_RAM_SinglePortDistributed = 1
eModuleType_ROM_SinglePortBlock = 2
eModuleType_RAM_DualPortBlock = 3
eModuleType_RAM_DualPortDistributed = 4
eModuleType_ROM_DualPortBlock = 5
eModuleType_ClockManager = 6
eModuleType_AsynchronousFIFO = 7
eModuleType_ADD = 8
eModuleType_SUB = 9
eModuleType_ALU = 10
eModuleType_MUL = 11
eModuleType_CMP = 12
eModuleType_LVDSIN = 13
eModuleType_LVDSOUT = 14
eModuleType_None = 15

### TMonitorDefaultTo (Vcl.Forms)

mdNearest = 0
mdNull = 1
mdPrimary = 2

### TMouseActivate (System.UITypes)

maDefault = 0
maActivate = 1
maActivateAndEat = 2
maNoActivate = 3
maNoActivateAndEat = 4

### TMouseButton (System.UITypes)

mbLeft = 0
mbRight = 1
mbMiddle = 2

### TMouseState (XPButton)

msEntered = 0
msLeaved = 1

### TMPBtnType (Vcl.MPlayer)

btPlay = 0
btPause = 1
btStop = 2
btNext = 3  // 脚本里是 0
btPrev = 4  // 脚本里是 1
btStep = 5
btBack = 6
btRecord = 7
btEject = 8

### TMPDevCaps (Vcl.MPlayer)

mpCanStep = 0
mpCanEject = 1
mpCanPlay = 2
mpCanRecord = 3
mpUsesWindow = 4

### TMPDeviceTypes (Vcl.MPlayer)

dtAutoSelect = 0
dtAVIVideo = 1
dtCDAudio = 2
dtDAT = 3
dtDigitalVideo = 4
dtMMMovie = 5
dtOther = 6
dtOverlay = 7
dtScanner = 8
dtSequencer = 9
dtVCR = 10
dtVideodisc = 11
dtWaveAudio = 12

### TMPModes (Vcl.MPlayer)

mpNotReady = 0
mpStopped = 1
mpPlaying = 2
mpRecording = 3
mpSeeking = 4
mpPaused = 5
mpOpen = 6

### TMPNotifyValues (Vcl.MPlayer)

nvSuccessful = 0
nvSuperseded = 1
nvAborted = 2
nvFailure = 3

### TMPTimeFormats (Vcl.MPlayer)

tfMilliseconds = 0
tfHMS = 1
tfMSF = 2
tfFrames = 3
tfSMPTE24 = 4
tfSMPTE25 = 5
tfSMPTE30 = 6
tfSMPTE30Drop = 7
tfBytes = 8
tfSamples = 9
tfTMSF = 10

### TMsgDlgBtn (System.UITypes)

mbYes = 0
mbNo = 1
mbOK = 2
mbCancel = 3
mbAbort = 4
mbRetry = 5
mbIgnore = 6
mbAll = 7
mbNoToAll = 8
mbYesToAll = 9
mbHelp = 10
mbClose = 11

### TMsgDlgType (System.UITypes)

mtWarning = 0
mtError = 1
mtInformation = 2
mtConfirmation = 3
mtCustom = 4

### TMultiSelectStyles (Vcl.ComCtrls)

msControlSelect = 0
msShiftSelect = 1
msVisibleOnly = 2
msSiblingOnly = 3

### TNanoBoardKind (Rt_NexusNanoBoard)

eNanoboardA = 0
eNanoBoardB = 1
eNanoBoard2A = 2
eNanoBoard3000XN = 3
eNanoBoard3000XN_Update = 4
eNanoBoard3000XN_Manufacture = 5
eNanoBoard3000AL = 6
eNanoBoard3000AL_Update = 7
eNanoBoard3000AL_Manufacture = 8
eNanoBoard3000LC = 9
eNanoBoard3000LC_Update = 10
eNanoBoard3000LC_Manufacture = 11
eNanoBoardCustom1 = 12
eFTDI_DeveloperTool5 = 13
eFTDI_SystemOnModule5 = 14
eNanoBoard3000XN_S6 = 15
eNanoBoard3000XN_S6_Update = 16
eNanoBoard3000XN_S6_Manufacture = 17
eNanoBoard3000AL_C4 = 18
eNanoBoard3000AL_C4_Update = 19
eNanoBoard3000AL_C4_Manufacture = 20

### TNavigateBtn (Vcl.DBCtrls)

nbFirst = 0
nbPrior = 1
nbNext = 2
nbLast = 3
nbInsert = 4
nbDelete = 5
nbEdit = 6
nbPost = 7
nbCancel = 8
nbRefresh = 9
nbApplyUpdates = 10
nbCancelUpdates = 11

### TNavigationAction (RT_Workspace)

eNA_None = 0
eNA_Highlight = 1
eNA_Navigate = 2
eNA_Browse = 3

### TNetClassification (RT_PCB)

eDiffPairNet = 0
eSameLengthRule = 1
eSameMatchedLengthRule = 2
eSameNetClass = 3
eOtherBoardNets = 4

### TNetLineMode (RT_PCB)

NetLineMode_Off = 0
NetLineMode_PadToPad = 1
NetLineMode_Reconnection = 2

### TNetScope (Pcbtypes)

eNetScope_DifferentNetsOnly = 0
eNetScope_SameNetOnly = 1
eNetScope_AnyNet = 2

### TNetScope (RT_PCB)

eNetScope_DifferentNetsOnly = 0
eNetScope_SameNetOnly = 1
eNetScope_AnyNet = 2
eNetScope_DifferentDiffPairsOnly = 3
eNetScope_SameDiffPairOnly = 4

### TNetScope (RT_Workspace)

eScopeLocal = 0
eScopeInterface = 1
eScopeGlobal = 2

### TNetTopology (RT_PCB)

eNetTopology_Shortest = 0
eNetTopology_Horizontal = 1
eNetTopology_Vertical = 2
eNetTopology_DaisyChain_Simple = 3
eNetTopology_DaisyChain_MidDriven = 4
eNetTopology_DaisyChain_Balanced = 5
eNetTopology_Starburst = 6

### TNexusAction (Rt_NexusDevices)

eNexusAction_None = 0
eNexusAction_ProcessorPause = 1
eNexusAction_ProcessorContinue = 2
eNexusAction_ProcessorReset = 3
eNexusAction_ProcessorSingleStep = 4
eNexusAction_ProgramCompile = 5
eNexusAction_ProgramDownload = 6
eNexusAction_StartDebug = 7
eNexusAction_StartAttach = 8
eNexusAction_EndDebug = 9
eNexusAction_ShowAboutDialog = 10
eNexusAction_DeviceReset = 11
eNexusAction_DeviceDownload = 12
eNexusAction_ShowViewer = 13
eNexusAction_ChooseFileAndDownload = 14
eNexusAction_ProcessorMenu = 15
eNexusAction_ConfigureJTAGIdMapping = 16
eNexusAction_Flash_DeviceReset = 17
eNexusAction_Flash_DeviceConfigure = 18
eNexusAction_Flash_DeviceDownload = 19
eNexusAction_Flash_ChooseFileAndDownload = 20
eNexusAction_WriteToFlash = 21
eNexusAction_ConfigureFpgaProject = 22
eNexusAction_ShowConfiguration = 23
eNexusAction_ShowCurrentSense = 24
eNexusAction_ShowBoardRegistration = 25
eNexusAction_CustomAction = 26
eNexusAction_OnDblClick = 27
eNexusAction_HideViewer = 28
eNexusAction_UpdateFirmware = 29
eNexusAction_ToggleFirmwareAutoUpdate = 30
eNexusAction_ProgramVerify = 31

### TNexusActionTarget (Rt_NexusDevices)

eNexusActionTarget_None = 0
eNexusActionTarget_SoftDevice = 1
eNexusActionTarget_HardDevice = 2
eNexusActionTarget_SoftChain = 3
eNexusActionTarget_HardChain = 4
eNexusActionTarget_BoardDevice = 5
eNexusActionTarget_BoardChain = 6

### TNexusBreakpointKind (Rt_NexusDevices)

eBreakpointKind_Program_FetchAnyOpcode = 0
eBreakpointKind_Program_FetchSpecificOpcode = 1
eBreakpointKind_DataAtAddress_AnyValue = 2
eBreakpointKind_DataAtAddress_SpecificValue = 3

### TNexusCoreKind (Rt_NexusWorkspace)

eNexusCoreKind_None = 0
eNexusCoreKind_Processor_OCDS = 1
eNexusCoreKind_Processor_Standard = 2
eNexusCoreKind_Processor_Hard = 3
eNexusCoreKind_Memory_Program = 4
eNexusCoreKind_Memory_Data = 5
eNexusCoreKind_Instrument = 6
eNexusCoreKind_ClockManager = 7

### TNexusDriverStatus (Rt_NexusDevices)

eDriverStatus_Unknown = 0
eDriverStatus_Unavailable = 1
eDriverStatus_Available = 2
eDriverStatus_PendingInstallation = 3
eDriverStatus_Installed = 4
eDriverStatus_AllAvailableInstalled = 5

### TNodeAttachMode (Vcl.ComCtrls)

naAdd = 0
naAddFirst = 1
naAddChild = 2
naAddChildFirst = 3
naInsert = 4

### TNoERCSymbol (Rt_Schematic)

eNoERCSymbolCrossThin = 0
eNoERCSymbolCrossThick = 1
eNoERCSymbolCrossSmall = 2
eNoERCSymbolCheckBox = 3
eNoERCSymbolTriangle = 4

### TNumberingStyle (Vcl.ComCtrls)

nsNone = 0
nsBullet = 1

### TNumberTypeEx (XPTypes)

ntNone = 0
ntUnsignedInt = 1
ntSignedInt = 2
ntFloat = 3

### TObjectClearanceId (RT_PCB)

eObjectClearanceID_Arc = 0
eObjectClearanceID_Track = 1
eObjectClearanceID_SMDPad = 2
eObjectClearanceID_THPad = 3
eObjectClearanceID_Via = 4
eObjectClearanceID_Fill = 5
eObjectClearanceID_Poly = 6
eObjectClearanceID_Region = 7
eObjectClearanceID_Text = 8
eObjectClearanceID_Hole = 9
eObjectClearanceID_OutlineEdge = 10
eObjectClearanceID_CavityEdge = 11
eObjectClearanceID_CutoutEdge = 12
eObjectClearanceID_SplitBarrier = 13
eObjectClearanceID_SplitContinuation = 14

### TObjectCreationMode (RT_PCB)

eCreate_Default = 0
eCreate_GlobalCopy = 1

### TObjectCreationMode (Rt_Schematic)

eCreate_Default = 0
eCreate_GlobalCopy = 1

### TObjectId (Pcbtypes)

eIgnoreObject = 0  // 脚本里不可用
eArcObject = 1
ePadObject = 2
eViaObject = 3
eTrackObject = 4
eTextObject = 5
eFillObject = 6
eFromToObject = 7  // 脚本里是 17
eNetObject = 8
eComponentObject = 9
ePolygonObject = 10  // 脚本里不可用
eRegionObject = 11
eComponentBodyObject = 12
eDimensionObject = 13
eCoordinateObject = 14
eClassObject = 15
eRuleObject = 16
eManualFromToObject = 17  // 脚本里不可用
eDifferentialPairObject = 18
eViolationObject = 19
eEmbeddedObject = 20
eEmbeddedBoardObject = 21
eSplitPlaneObject = 22
eTraceObject = 23
eSpareViaObject = 24
eBoardObject = 25
eBoardOutlineObject = 26

### TObjectId (RT_PCB)

eNoObject = 0
eArcObject = 1
ePadObject = 2
eViaObject = 3
eTrackObject = 4
eTextObject = 5
eFillObject = 6
eConnectionObject = 7
eNetObject = 8
eComponentObject = 9
ePolyObject = 10
eRegionObject = 11
eComponentBodyObject = 12
eDimensionObject = 13
eCoordinateObject = 14
eClassObject = 15
eRuleObject = 16
eFromToObject = 17
eDifferentialPairObject = 18
eViolationObject = 19
eEmbeddedObject = 20
eEmbeddedBoardObject = 21
eSplitPlaneObject = 22
eTraceObject = 23
eSpareViaObject = 24
eBoardObject = 25
eBoardOutlineObject = 26

### TObjectId (Rt_Schematic)

eFirstObjectID = 0
eClipBoardContainer = 1
eNote = 2
eProbe = 3
eRectangle = 4
eLine = 5
eConnectionLine = 6
eBusEntry = 7
eArc = 8
eEllipticalArc = 9
eRoundRectangle = 10
eImage = 11
ePie = 12
eTextFrame = 13
eRichTextDocument = 14
eEllipse = 15
eJunction = 16
ePolygon = 17
ePolyline = 18
eWire = 19
eBus = 20
eBezier = 21
eLabel = 22
eHyperlink = 23
eNetLabel = 24
eDesignator = 25
eSchComponent = 26
eParameter = 27
eParameterSet = 28
eParameterList = 29
eSheetName = 30
eSheetFileName = 31
eSheet = 32
eSchLib = 33
eSymbol = 34
eNoERC = 35
eErrorMarker = 36
ePin = 37
ePort = 38
ePowerObject = 39
eSheetEntry = 40
eSheetSymbol = 41
eTemplate = 42
eTaskHolder = 43
eMapDefiner = 44
eImplementationMap = 45
eImplementation = 46
eImplementationsList = 47
eCrossSheetConnector = 48
eCompileMask = 49
eOpenBusComponent = 50
eOpenBusLink = 51
eOpenBusDesignator = 52
eHarnessConnector = 53
eHarnessEntry = 54
eHarnessConnectorType = 55
eSignalHarness = 56
eOpenBusPort = 57
eHighLevelCodeSymbol = 58
eHighLevelCodeEntry = 59
eOpenBusPinGroup = 60
eBlanket = 61
eRTFLink = 62
eFSMState = 63
eFSMTransition = 64
eCommentThread = 65
eCommentThreadNote = 66
eFSMNote = 67
eDiagramModule = 68
eDiagramModuleName = 69
eDiagramModuleSource = 70
eDiagramConnector = 71
eDiagramBlock = 72
eDiagramHarness = 73
eDiagramHarnessName = 74
eDiagramHarnessSource = 75
eDiagramConnectorLink = 76
eDiagramPin = 77
eVirtualParameter = 78
eHarnessWiringDiagram = 79
eHarnessLayoutDrawing = 80
eHarnessComponent = 81
eHarnessWire = 82
eHarnessSplice = 83
eHarnessLayoutLabel = 84
eHarnessLayoutConnectionPoint = 85
eHarnessBundle = 86
eHarnessLogicalSignal = 87
eHarnessPin = 88
eHarnessWireLabel = 89
eHarnessWireData = 90
eHarnessSpliceData = 91
eHarnessShield = 92
eHarnessTwist = 93
eHarnessNoConnect = 94
eHarnessNoConnectData = 95
eHarnessShieldData = 96
eHarnessTwistData = 97
eHarnessCable = 98
eHarnessCableData = 99
eImageParameter = 100
eHarnessAssociatedParts = 101
eLastObjectId = 102

### TObjectState (Data.Win.ADODB)

stClosed = 0
stOpen = 1
stConnecting = 2
stExecuting = 3
stFetching = 4

### TObjectState (Vcl.OleCtnrs)

osEmpty = 0
osLoaded = 1
osRunning = 2
osOpen = 3
osInPlaceActive = 4
osUIActive = 5

### TOpenBusComponentInterfaceType (Rt_Schematic)

obcitPin = 0
obcitHarness = 1

### TOpenBusComponentKind (Rt_Schematic)

obckProcessor = 0
obckArbiter = 1
obckInterconnect = 2
obckPeripheral = 3
obckMemory = 4
obckConnector = 5
obckTerminator = 6

### TOpenBusInternalPinType (Rt_Schematic)

iptInterrupt = 0
iptReset = 1
iptClock = 2

### TOpenBusInterruptExportType (Rt_Schematic)

ietNotExported = 0
ietInternal = 1
ietExportedAsOutput = 2
ietExportedAsInput = 3

### TOpenBusInterruptKind (Rt_Schematic)

ikLevel = 0
ikEdge = 1

### TOpenBusInterruptPolarity (Rt_Schematic)

ipNegative = 0
ipPositive = 1

### TOpenBusPortKind (Rt_Schematic)

obpkPeripheralMaster = 0
obpkPeripheralSlave = 1
obpkArbiterMaster = 2
obpkArbiterSlave = 3
obpkInterconMaster = 4
obpkInterconSlave = 5
obpkConnectorMaster = 6
obpkConnectorSlave = 7

### TOpenBusPortType (Rt_Schematic)

obptUnspecified = 0
obptMaster = 1
obptSlave = 2

### TOpenOption (System.UITypes)

ofReadOnly = 0
ofOverwritePrompt = 1
ofHideReadOnly = 2
ofNoChangeDir = 3
ofShowHelp = 4
ofNoValidate = 5
ofAllowMultiSelect = 6
ofExtensionDifferent = 7
ofPathMustExist = 8
ofFileMustExist = 9
ofCreatePrompt = 10
ofShareAware = 11
ofNoReadOnlyReturn = 12
ofNoTestFileCreate = 13
ofNoNetworkButton = 14
ofNoLongNames = 15
ofOldStyleDialog = 16
ofNoDereferenceLinks = 17
ofEnableIncludeNotify = 18
ofEnableSizing = 19
ofDontAddToRecent = 20
ofForceShowHidden = 21

### TOpenOptionEx (System.UITypes)

ofExNoPlacesBar = 0

### TOperation (System.Classes)

opInsert = 0
opRemove = 1

### TOptionsObjectId (RT_PCB)

eAbstractOptions = 0
eOutputOptions = 1
ePrinterOptions = 2
eGerberOptions = 3
eAdvancedPlacerOptions = 4
eDesignRuleCheckerOptions = 5
eSpecctraRouterOptions = 6
eAdvancedRouterOptions = 7
eEngineeringChangeOrderOptions = 8
eInteractiveRoutingOptions = 9
eSystemOptions = 10
ePinSwapOptions = 11
eEdgeLayoutOptions = 12
eSplitpPlaneDRCOptions = 13
eTestpointOptions = 14

### TOrcadFootPrint (Rt_Schematic)

ePartfield1 = 0
ePartfield2 = 1
ePartfield3 = 2
ePartfield4 = 3
ePartfield5 = 4
ePartfield6 = 5
ePartfield7 = 6
ePartfield8 = 7
eIgnore = 8

### TOutputCategory (RT_Workspace)

eOutput_Netlist = 0
eOutput_Simulator = 1
eOutput_Documentation = 2
eOutput_Assembly = 3
eOutput_Fabrication = 4
eOutput_Report = 5
eOutput_Other = 6
eOutput_Validation = 7
eOutput_Export = 8
eOutput_PostProcess = 9

### TOutputDriverType (RT_PCB)

eUnknownDriver = 0
eProtelGerber = 1
eProtelPlot_Composite = 2
eProtelPlot_Final = 3
eStandardDriver_Composite = 4
eStandardDriver_Final = 5

### TOutputJobVariantScope (RT_Workspace)

eVariantScope_DefinedForEachOutput = 0
eVariantScope_DefinedForWholeOutputJob = 1
eVariantScope_DefinedFromConfiguration = 2

### TOutputPort (Pcbtypes)

eOutputPortCom1 = 0
eOutputPortCom2 = 1
eOutputPortCom3 = 2
eOutputPortCom4 = 3
eOutputPortFile = 4

### TOutputPort (RT_PCB)

eOutputPortCom1 = 0
eOutputPortCom2 = 1
eOutputPortCom3 = 2
eOutputPortCom4 = 3
eOutputPortFile = 4

### TOutputResult (RT_Workspace)

eOutputResult_DidNotRun = 0
eOutputResult_Cancelled = 1
eOutputResult_Failure = 2
eOutputResult_Success = 3

### TOutputSignalVisualKind (RT_Digital_IO)

oskLED = 0
oskNumeric = 1
osk7Segment = 2
oskSlider = 3
oskKnob = 4
oskNone = 5

### TOverlayLayerScope (RT_PCB)

olsBoth = 0
olsTop = 1
olsBottom = 2

### TPackageCompareOption (RT_PCB)

ePrimitiveHashOption_CheckOverlayLayers = 0
ePrimitiveHashOption_CheckAssemblyLayers = 1

### TPadMode (Pcbtypes)

ePadMode_Simple = 0
ePadMode_LocalStack = 1
ePadMode_ExternalStack = 2

### TPadMode (RT_PCB)

ePadMode_Simple = 0
ePadMode_LocalStack = 1
ePadMode_ExternalStack = 2

### TPadViaThermalReliefDataType (RT_PCB)

trtFromRule = 0
trtManual = 1

### TPageMeasureUnits (System.UITypes)

pmDefault = 0
pmMillimeters = 1
pmInches = 2

### TPageScrollerButton (Vcl.ComCtrls)

sbFirst = 0
sbLast = 1

### TPageScrollerButtonState (Vcl.ComCtrls)

bsNormal = 0
bsInvisible = 1
bsGrayed = 2
bsDepressed = 3
bsHot = 4

### TPageScrollerOrientation (Vcl.ComCtrls)

soHorizontal = 0
soVertical = 1

### TPageSetupDialogOption (System.UITypes)

psoDefaultMinMargins = 0
psoDisableMargins = 1
psoDisableOrientation = 2
psoDisablePagePainting = 3
psoDisablePaper = 4
psoDisablePrinter = 5
psoMargins = 6
psoMinMargins = 7
psoShowHelp = 8
psoWarning = 9
psoNoNetworkButton = 10

### TPageType (System.UITypes)

ptEnvelope = 0
ptPaper = 1

### TPaintColorMode (Rt_Util)

ePaintColorMode_FullColor = 0
ePaintColorMode_GrayScale = 1
ePaintColorMode_Monochrome = 2
ePaintColorMode_MonochromeBackground = 3

### TPaintScaleMode (Rt_Util)

psmScreen = 0
psmDefault = 1
psmPrint = 2

### TParameter_ReadOnlyState (Rt_Schematic)

eReadOnly_None = 0
eReadOnly_Name = 1
eReadOnly_Value = 2
eReadOnly_NameAndValue = 3

### TParameterAddMode (RT_Workspace)

eParameterAdd_Default = 0
eParameterAdd_Never = 1
eParameterAdd_Always = 2
eParameterAdd_IfNotBlankInLibrary = 3

### TParameterAppurtenance (RT_PCB)

paUser = 0
paSystem = 1
paFootprint = 2

### TParameterAttribute (Data.Win.ADODB)

paSigned = 0
paNullable = 1
paLong = 2

### TParameterDirection (Data.Win.ADODB)

pdUnknown = 0
pdInput = 1
pdOutput = 2
pdInputOutput = 3
pdReturnValue = 4

### TParameterKind (RT_Workspace)

eParameterKind_String = 0
eParameterKind_Boolean = 1
eParameterKind_Integer = 2
eParameterKind_Float = 3

### TParameterRemoveMode (RT_Workspace)

eParameterRemove_Default = 0
eParameterRemove_Never = 1
eParameterRemove_IfBlankInLibrary = 2

### TParameterSetStyle (Rt_Schematic)

eParameterSetLarge = 0
eParameterSetTiny = 1

### TParameterType (Rt_Schematic)

eParameterType_String = 0
eParameterType_Boolean = 1
eParameterType_Integer = 2
eParameterType_Float = 3

### TParameterUpdateMode (RT_Workspace)

eParameterUpdate_Default = 0
eParameterUpdate_Never = 1
eParameterUpdate_Always = 2

### TParamType (Data.DB)

ptUnknown = 0
ptInput = 1
ptOutput = 2
ptInputOutput = 3
ptResult = 4

### TParity (RT_PCB)

eParityNone = 0
eParityEven = 1
eParityOdd = 2
eParityMark = 3
eParitySpace = 4

### TParserOption (Data.DBCommon)

poExtSyntax = 0
poAggregate = 1
poDefaultExpr = 2
poUseOrigNames = 3
poFieldNameGiven = 4
poFieldDepend = 5

### TPaymentTime (System.Math)

ptEndOfPeriod = 0
ptStartOfPeriod = 1

### TPCB_DocumentPainterMode (RT_PCB)

eDocumentPainterMode_Selectable = 0
eDocumentPainterMode_2D = 1
eDocumentPainterMode_3D = 2

### TPCB_ShapeEdgeType (RT_PCB)

etLine = 0
etCircle = 1
etEllipse = 2
etParabola = 3
etBSpline = 4

### TPCBClassMemberKind (RT_Workspace)

eClassMemberKind_Net = 0
eClassMemberKind_Component = 1
eClassMemberKind_FromTo = 2
eClassMemberKind_Pad = 3
eClassMemberKind_Layer = 4
eClassMemberKind_DesignChannel = 5
eClassMemberKind_DifferentialPair = 6
eClassMemberKind_Polygon = 7
eClassMemberKind_SplitPlane = 8
eClassMemberKind_ObjectClass = 9

### TPcbDragMode (RT_PCB)

eDragNone = 0
eDragAllTracks = 1
eDragConnectedTracks = 2

### TPCBMeshViewMode (RT_PCB)

eShowIn2D = 0
eShowIn3D = 1
eShowBoth = 2
eHideBoth = 3

### TPCBViewMode (RT_PCB)

vmGeneralPCB = 0
vmEditBoardOutline = 1

### TPenMode (Vcl.Graphics)

pmBlack = 0
pmWhite = 1
pmNop = 2
pmNot = 3
pmCopy = 4
pmNotCopy = 5
pmMergePenNot = 6
pmMaskPenNot = 7
pmMergeNotPen = 8
pmMaskNotPen = 9
pmMerge = 10
pmNotMerge = 11
pmMask = 12
pmNotMask = 13
pmXor = 14
pmNotXor = 15

### TPenStyle (Vcl.Graphics)

psSolid = 0
psDash = 1
psDot = 2
psDashDot = 3
psDashDotDot = 4
psClear = 5
psInsideFrame = 6
psUserStyle = 7
psAlternate = 8

### TPersistFormat (Data.Win.ADODB)

pfADTG = 0
pfXML = 1

### TPinElectrical (RT_Workspace)

eElectricInput = 0
eElectricIO = 1
eElectricOutput = 2
eElectricOpenCollector = 3
eElectricPassive = 4
eElectricHiZ = 5
eElectricOpenEmitter = 6
eElectricPower = 7

### TPinItemMode (Rt_Schematic)

ePinItemMode_Default = 0
ePinItemMode_Custom = 1

### TPinTextRotationAnchor (Rt_Schematic)

raPin = 0
raComponent = 1

### TPixelFormat (Vcl.Graphics)

pfDevice = 0
pf1bit = 1
pf4bit = 2
pf8bit = 3
pf15bit = 4
pf16bit = 5
pf24bit = 6
pf32bit = 7
pfCustom = 8

### TPlaceRectangleCornerMode (RT_PCB)

prcmRectangle = 0
prcmFillet = 1
prcmChamfer = 2

### TPlaceTrackMode (RT_PCB)

ePlaceTrackNone = 0
ePlaceTrackAny = 1
ePlaceTrack9090 = 2
ePlaceTrack4590 = 3
ePlaceTrack90Arc = 4

### TPlaneConnectionStyle (RT_PCB)

ePlaneNoConnect = 0
ePlaneReliefConnect = 1
ePlaneDirectConnect = 2

### TPlaneConnectPrimitiveType (RT_PCB)

ePlanePadAndVia = 0
ePlanePad = 1
ePlaneVia = 2

### TPlaneConnectStyle (RT_PCB)

eReliefConnectToPlane = 0
eDirectConnectToPlane = 1
eNoConnect = 2

### TPlaneDrawMode (RT_PCB)

ePlaneDrawoOutlineLayerColoured = 0
ePlaneDrawOutlineNetColoured = 1
ePlaneDrawInvertedNetColoured = 2

### TPlaneKind (RT_PCB)

eXY = 0
eXZ = 1
eYZ = 2

### TPlotterLanguage (Pcbtypes)

ePlotterLanguageHPGL = 0
ePlotterLanguageDMPL = 1

### TPlotterLanguage (RT_PCB)

ePlotterLanguageHPGL = 0
ePlotterLanguageDMPL = 1

### TPluginAutoRunAction (RT_ClientServerInterface)

paraInstall = 0
paraUninstall = 1
paraUpdate = 2
paraAfterInstall = 3
paraBeforeUninstall = 4
paraBeforeUpdate = 5
paraAfterUpdate = 6

### TPluginsStatus (RT_ClientServerInterface)

psActive = 0
psInactive = 1
psNeedsUpgrade = 2
psNeedsRemoval = 3
psInvalid = 4

### TPNGTransparencyMode (Vcl.Imaging.pngimage)

ptmNone = 0
ptmBit = 1
ptmPartial = 2

### TPolygonConnectPrimitiveType (RT_PCB)

ePolyPadAndVia = 0
ePolyTHPad = 1
ePolySMDPad = 2
ePolyVia = 3

### TPolygonNameTemplates (RT_PCB)

eTemplate_NetNameLXXPXXX = 0
eTemplate_LXXNetNamePXXX = 1
eTemplate_NetNameLayerNamePXXX = 2
eTemplate_LayerNameNetNamePXXX = 3

### TPolygonPourOver (RT_PCB)

ePolygonPourOver_None = 0
ePolygonPourOver_SameNet = 1
ePolygonPourOver_SameNetPolygons = 2

### TPolygonReliefAngle (RT_PCB)

ePolygonReliefAngle_45 = 0
ePolygonReliefAngle_90 = 1
ePolygonReliefAngle_0 = 2
ePolygonReliefAngle_135 = 3

### TPolygonRepourMode (RT_PCB)

eNeverRepour = 0
eAskRepour = 1
eAlwaysRepour = 2

### TPolygonType (RT_PCB)

eSignalLayerPolygon = 0
eSplitPlanePolygon = 1
eCoverlayOutlinePolygon = 2

### TPolyHatchStyle (Pcbtypes)

ePolyHatch90 = 0
ePolyHatch45 = 1
ePolyVHatch = 2
ePolyHHatch = 3
ePolyNoHatch = 4
ePolySolid = 5

### TPolyHatchStyle (RT_PCB)

ePolyHatch90 = 0
ePolyHatch45 = 1
ePolyVHatch = 2
ePolyHHatch = 3
ePolyNoHatch = 4
ePolySolid = 5

### TPolylineCutterMode (Rt_Schematic)

eCutterSnapToSegment = 0
eCutterGridSize = 1
eCutterFixedLength = 2

### TPolySegmentType (Pcbtypes)

ePolySegmentLine = 0
ePolySegmentArc = 1

### TPolySegmentType (RT_PCB)

ePolySegmentLine = 0
ePolySegmentArc = 1

### TPopupAlignment (Vcl.Menus)

paLeft = 0
paRight = 1
paCenter = 2

### TPopupMode (Vcl.Forms)

pmNone = 0
pmAuto = 1
pmExplicit = 2

### TPortArrowStyle (Rt_Schematic)

ePortNone = 0
ePortLeft = 1
ePortRight = 2
ePortLeftRight = 3
ePortNoneVertical = 4
ePortTop = 5
ePortBottom = 6
ePortTopBottom = 7

### TPortConnectedEnd (Rt_Schematic)

ePortConnectedEnd_None = 0
ePortConnectedEnd_Origin = 1
ePortConnectedEnd_Extremity = 2
ePortConnectedEnd_Both = 3

### TPortIO (Rt_Schematic)

ePortUnspecified = 0
ePortOutput = 1
ePortInput = 2
ePortBidirectional = 3

### TPosition (Vcl.Forms)

poDesigned = 0
poDefault = 1
poDefaultPosOnly = 2
poDefaultSizeOnly = 3
poScreenCenter = 4
poDesktopCenter = 5
poMainFormCenter = 6
poOwnerFormCenter = 7

### TPositionToolTip (Vcl.ComCtrls)

ptNone = 0
ptTop = 1
ptLeft = 2
ptBottom = 3
ptRight = 4

### TPowerObjectStyle (Rt_Schematic)

ePowerCircle = 0
ePowerArrow = 1
ePowerBar = 2
ePowerWave = 3
ePowerGndPower = 4
ePowerGndSignal = 5
ePowerGndEarth = 6
eGOSTPowerArrow = 7
eGOSTPowerGndPower = 8
eGOSTPowerGndEarth = 9
eGOSTPowerBar = 10

### TPrintDialogOption (System.UITypes)

poPrintToFile = 0
poPageNums = 1
poSelection = 2
poWarning = 3
poHelp = 4
poDisablePrintToFile = 5

### TPrinterBatch (Pcbtypes)

ePlotPerSheet = 0
ePanelize = 1

### TPrinterBatch (RT_PCB)

ePlotPerSheet = 0
ePanelize = 1

### TPrinterCapability (System.UITypes)

pcCopies = 0
pcOrientation = 1
pcCollation = 2

### TPrinterComposite (Pcbtypes)

eColorComposite = 0
eMonoComposite = 1

### TPrinterComposite (RT_PCB)

eColorComposite = 0
eMonoComposite = 1

### TPrinterOrientation (System.UITypes)

poPortrait = 0
poLandscape = 1

### TPrintKind (RT_Outputs)

ePrintKind_FullColor = 0
ePrintKind_GrayScale = 1
ePrintKind_Monochrome = 2

### TPrintRange (System.UITypes)

prAllPages = 0
prSelection = 1
prPageNums = 2

### TPrintScale (Vcl.Forms)

poNone = 0
poProportional = 1
poPrintToFit = 2

### TProcessAction (RT_PCB)

paNone = 0
paClip = 1
paMove = 2

### TProcessFlowState (Rt_NexusDevices)

eFlowState_UpToDate = 0
eFlowState_OutOfDate = 1
eFlowState_Missing = 2
eFlowState_None = 3

### TProgressBarOrientation (Vcl.ComCtrls)

pbHorizontal = 0
pbVertical = 1

### TProgressBarState (Vcl.ComCtrls)

pbsNormal = 0
pbsError = 1
pbsPaused = 2

### TProgressBarStyle (Vcl.ComCtrls)

pbstNormal = 0
pbstMarquee = 1

### TProgressStage (Vcl.Graphics)

psStarting = 0
psRunning = 1
psEnding = 2

### TProviderFlag (Data.DB)

pfInUpdate = 0
pfInWhere = 1
pfInKey = 2
pfHidden = 3

### TPSCommandType (Data.DB)

ctUnknown = 0
ctQuery = 1
ctTable = 2
ctStoredProc = 3
ctServerMethod = 4
ctSelect = 5
ctInsert = 6
ctUpdate = 7
ctDelete = 8
ctDDL = 9

### TPublisherPageFlag (RT_Workspace)

ePublisherPageFlag_SceneChange = 0

### TPushMode (RT_PCB)

eIgnoreOthers = 0
eStopFirst = 1
ePushStopLocked = 2
ePushIgnoreLocked = 3

### TRadix (XPTypes)

rdxBinary = 0
rdxOctal = 1
rdxDecimal = 2
rdxHexadecimal = 3

### TRecordStatus (Data.Win.ADODB)

rsOK = 0
rsNew = 1
rsModified = 2
rsDeleted = 3
rsUnmodified = 4
rsInvalid = 5
rsMultipleChanges = 6
rsPendingChanges = 7
rsCanceled = 8
rsCantRelease = 9
rsConcurrencyViolation = 10
rsIntegrityViolation = 11
rsMaxChangesExceeded = 12
rsObjectOpen = 13
rsOutOfMemory = 14
rsPermissionDenied = 15
rsSchemaViolation = 16
rsDBDeleted = 17

### TRectCorner (RT_PCB)

eCornerBottomLeft = 0
eCornerBottomRight = 1
eCornerTopRight = 2
eCornerTopLeft = 3

### TRegDataType (System.Win.Registry)

rdUnknown = 0
rdString = 1
rdExpandString = 2
rdInteger = 3
rdBinary = 4

### TRegionKind (Pcbtypes)

eRegionKind_Copper = 0
eRegionKind_Cutout = 1
eRegionKind_NamedRegion = 2
eRegionKind_BoardCutout = 3

### TRegionKind (RT_PCB)

eRegionKind_Copper = 0
eRegionKind_Cutout = 1
eRegionKind_NamedRegion = 2
eRegionKind_BoardCutout = 3
eRegionKind_Cavity = 4

### TReleaseDistributionPart (RT_Workspace)

eReleaseDistributionPart_SourceDocuments = 0
eReleaseDistributionPart_BillOfMaterials = 1
eReleaseDistributionPart_AssemblyOutputs = 2
eReleaseDistributionPart_FabricationOutputs = 3

### TReportLevel (Rt_AbstractFPGA)

eReportLevelNoReport = 0
eReportLevelInfo = 1
eReportLevelWarning = 2
eReportLevelError = 3

### TResizeStyle (Vcl.ExtCtrls)

rsNone = 0
rsLine = 1
rsUpdate = 2
rsPattern = 3

### TResType (Vcl.ImgList)

rtBitmap = 0
rtCursor = 1
rtIcon = 2

### TRotationBy90 (Rt_Schematic)

eRotate0 = 0
eRotate90 = 1
eRotate180 = 2
eRotate270 = 3

### TRoundingMode (System.Math)

rmNearest = 0
rmDown = 1
rmUp = 2
rmTruncate = 3

### TRouteVia (RT_PCB)

eViaThruHole = 0
eViaBlindBuriedPair = 1
eViaBlindBuriedAny = 2
eViaNone = 3

### TRoutingCornerStyle (RT_PCB)

eRoutingCornerStyle_90 = 0
eRoutingCornerStyle_45 = 1
eRoutingCornerStyle_Any = 2

### TRoutingDiffPairGapMode (RT_PCB)

eRoutingDiffPairGap_Min = 0
eRoutingDiffPairGap_Preferred = 1
eRoutingDiffPairGap_Max = 2

### TRoutingWidthMode (RT_PCB)

eRoutingWidth_Default = 0
eRoutingWidth_Min = 1
eRoutingWidth_Preferred = 2
eRoutingWidth_Max = 3

### TRSGPBrushKind (RSGdiPlusGraphicsTypes)

bkNone = 0
bkSolid = 1  // 脚本里不可用
bkGradient = 2  // 脚本里不可用
bkBitmap = 3  // 脚本里不可用
bkHatchFill = 4  // 脚本里不可用

### TRSGPHatchStyle (RSGdiPlusGraphicsTypes)

hsHorizontal = 0  // 脚本里是 2
hsVertical = 1
hsForwardDiagonal = 2  // 脚本里不可用
hsBackwardDiagonal = 3  // 脚本里不可用
hsCross = 4  // 脚本里是 5
hsDiagonalCross = 5  // 脚本里不可用
hs05Percent = 6  // 脚本里不可用
hs10Percent = 7  // 脚本里不可用
hs20Percent = 8  // 脚本里不可用
hs25Percent = 9  // 脚本里不可用
hs30Percent = 10  // 脚本里不可用
hs40Percent = 11  // 脚本里不可用
hs50Percent = 12  // 脚本里不可用
hs60Percent = 13  // 脚本里不可用
hs70Percent = 14  // 脚本里不可用
hs75Percent = 15  // 脚本里不可用
hs80Percent = 16  // 脚本里不可用
hs90Percent = 17  // 脚本里不可用
hsLightDownwardDiagonal = 18  // 脚本里不可用
hsLightUpwardDiagonal = 19  // 脚本里不可用
hsDarkDownwardDiagonal = 20  // 脚本里不可用
hsDarkUpwardDiagonal = 21  // 脚本里不可用
hsWideDownwardDiagonal = 22  // 脚本里不可用
hsWideUpwardDiagonal = 23  // 脚本里不可用
hsLightVertical = 24  // 脚本里不可用
hsLightHorizontal = 25  // 脚本里不可用
hsNarrowVertical = 26  // 脚本里不可用
hsNarrowHorizontal = 27  // 脚本里不可用
hsDarkVertical = 28  // 脚本里不可用
hsDarkHorizontal = 29  // 脚本里不可用
hsDashedDownwardDiagonal = 30  // 脚本里不可用
hsDashedUpwardDiagonal = 31  // 脚本里不可用
hsDashedHorizontal = 32  // 脚本里不可用
hsDashedVertical = 33  // 脚本里不可用
hsSmallConfetti = 34  // 脚本里不可用
hsLargeConfetti = 35  // 脚本里不可用
hsZigZag = 36  // 脚本里不可用
hsWave = 37  // 脚本里不可用
hsDiagonalBrick = 38  // 脚本里不可用
hsHorizontalBrick = 39  // 脚本里不可用
hsWeave = 40  // 脚本里不可用
hsPlaid = 41  // 脚本里不可用
hsDivot = 42  // 脚本里不可用
hsDottedGrid = 43  // 脚本里不可用
hsDottedDiamond = 44  // 脚本里不可用
hsShingle = 45  // 脚本里不可用
hsTrellis = 46  // 脚本里不可用
hsSphere = 47  // 脚本里不可用
hsSmallGrid = 48  // 脚本里不可用
hsSmallCheckerBoard = 49  // 脚本里不可用
hsLargeCheckerBoard = 50  // 脚本里不可用
hsOutlinedDiamond = 51  // 脚本里不可用
hsSolidDiamond = 52  // 脚本里不可用

### TRSGPLinearGradientShape (RSGdiPlusGraphicsTypes)

lgsNormal = 0
lgsBell = 1  // 脚本里不可用
lgsTriangular = 2  // 脚本里不可用

### TRSGPStringTrimming (RSGdiPlusGraphicsTypes)

stNone = 0
stCharacter = 1  // 脚本里不可用
stWord = 2  // 脚本里不可用
stEllipsisCharacter = 3  // 脚本里不可用
stEllipsisWord = 4  // 脚本里不可用
stEllipsisPath = 5  // 脚本里不可用

### TRuleKind (Pcbtypes)

eRule_Clearance = 0
eRule_ParallelSegment = 1
eRule_MaxMinWidth = 2
eRule_MaxMinLength = 3
eRule_MatchedLengths = 4
eRule_DaisyChainStubLength = 5
eRule_PowerPlaneConnectStyle = 6
eRule_RoutingTopology = 7
eRule_RoutingPriority = 8
eRule_RoutingLayers = 9
eRule_RoutingCornerStyle = 10
eRule_RoutingViaStyle = 11
eRule_PowerPlaneExpansion = 12  // 脚本里不可用
eRule_SolderMaskExpansion = 13
eRule_PasteMaskExpansion = 14
eRule_ShortCircuit = 15
eRule_BrokenNets = 16
eRule_ViasUnderSMD = 17
eRule_MaximumViaCount = 18
eRule_MinimumAnnularRing = 19
eRule_PolygonConnectStyle = 20
eRule_AcuteAngle = 21
eRule_ConfinementConstraint = 22
eRule_SMDToCorner = 23
eRule_ComponentClearance = 24
eRule_ComponentRotations = 25
eRule_PermittedLayers = 26
eRule_NetsToIgnore = 27
eRule_SignalStimulus = 28
eRule_MaxOvershoot_FallingEdge = 29  // 脚本里不可用
eRule_MaxOvershoot_RisingEdge = 30  // 脚本里不可用
eRule_MaxUndershoot_FallingEdge = 31  // 脚本里不可用
eRule_MaxUndershoot_RisingEdge = 32  // 脚本里不可用
eRule_MaxMinImpedance = 33
eRule_MinSignalTopValue = 34  // 脚本里不可用
eRule_MaxSignalBaseValue = 35  // 脚本里不可用
eRule_FlightTime_RisingEdge = 36
eRule_FlightTime_FallingEdge = 37
eRule_LayerStack = 38
eRule_MaxSlope_RisingEdge = 39
eRule_MaxSlope_FallingEdge = 40
eRule_SupplyNets = 41
eRule_MaxMinHoleSize = 42
eRule_TestPointStyle = 43
eRule_TestPointUsage = 44
eRule_UnconnectedPin = 45
eRule_SMDToPlane = 46
eRule_SMDNeckDown = 47
eRule_LayerPair = 48
eRule_FanoutControl = 49
eRule_MaxMinHeight = 50
eRule_DifferentialPairsRouting = 51
eRule_HoleToHoleClearance = 52
eRule_MinimumSolderMaskSliver = 53
eRule_SilkToSolderMaskClearance = 54
eRule_SilkToSilkClearance = 55
eRule_NetAntennae = 56
eRule_AssyTestPointStyle = 57
eRule_AssyTestPointUsage = 58
eRule_SilkToBoardRegion = 59
eRule_Pcad = 60  // 脚本里不可用
eRule_SMDPADEntry = 61  // 脚本里是 60
eRule_ModifiedPolygon = 62
eRule_BoardOutlineClearance = 63
eRule_BackDrilling = 64
eRule_Creepage = 65
eRule_ReturnPath = 66

### TRuleKind (RT_PCB)

eRule_Clearance = 0
eRule_ParallelSegment = 1
eRule_MaxMinWidth = 2
eRule_MaxMinLength = 3
eRule_MatchedLengths = 4
eRule_DaisyChainStubLength = 5
eRule_PowerPlaneConnectStyle = 6
eRule_RoutingTopology = 7
eRule_RoutingPriority = 8
eRule_RoutingLayers = 9
eRule_RoutingCornerStyle = 10
eRule_RoutingViaStyle = 11
eRule_PowerPlaneClearance = 12
eRule_SolderMaskExpansion = 13
eRule_PasteMaskExpansion = 14
eRule_ShortCircuit = 15
eRule_BrokenNets = 16
eRule_ViasUnderSMD = 17
eRule_MaximumViaCount = 18
eRule_MinimumAnnularRing = 19
eRule_PolygonConnectStyle = 20
eRule_AcuteAngle = 21
eRule_ConfinementConstraint = 22
eRule_SMDToCorner = 23
eRule_ComponentClearance = 24
eRule_ComponentRotations = 25
eRule_PermittedLayers = 26
eRule_NetsToIgnore = 27
eRule_SignalStimulus = 28
eRule_Overshoot_FallingEdge = 29
eRule_Overshoot_RisingEdge = 30
eRule_Undershoot_FallingEdge = 31
eRule_Undershoot_RisingEdge = 32
eRule_MaxMinImpedance = 33
eRule_SignalTopValue = 34
eRule_SignalBaseValue = 35
eRule_FlightTime_RisingEdge = 36
eRule_FlightTime_FallingEdge = 37
eRule_LayerStack = 38
eRule_MaxSlope_RisingEdge = 39
eRule_MaxSlope_FallingEdge = 40
eRule_SupplyNets = 41
eRule_MaxMinHoleSize = 42
eRule_TestPointStyle = 43
eRule_TestPointUsage = 44
eRule_UnconnectedPin = 45
eRule_SMDToPlane = 46
eRule_SMDNeckDown = 47
eRule_LayerPair = 48
eRule_FanoutControl = 49
eRule_MaxMinHeight = 50
eRule_DifferentialPairsRouting = 51
eRule_HoleToHoleClearance = 52
eRule_MinimumSolderMaskSliver = 53
eRule_SilkToSolderMaskClearance = 54
eRule_SilkToSilkClearance = 55
eRule_NetAntennae = 56
eRule_AssyTestPointStyle = 57
eRule_AssyTestPointUsage = 58
eRule_SilkToBoardRegion = 59
eRule_SMDPADEntry = 60
eRule_None = 61
eRule_ModifiedPolygon = 62
eRule_BoardOutlineClearance = 63
eRule_BackDrilling = 64
eRule_Creepage = 65
eRule_ReturnPath = 66

### TRuleLayerKind (Pcbtypes)

eRuleLayerKind_SameLayer = 0
eRuleLayerKind_AdjacentLayer = 1

### TRuleLayerKind (RT_PCB)

eRuleLayerKind_SameLayer = 0
eRuleLayerKind_AdjacentLayer = 1

### TRuleObjectId (Pcbtypes)

eRuleObject_None = 0
eRuleObject_Wire = 1
eRuleObject_Pin = 2
eRuleObject_Smd = 3
eRuleObject_Via = 4
eRuleObject_Fill = 5
eRuleObject_Polygon = 6

### TRuleScope (Pcbtypes)

eScopeKindBoard = 0
eScopeKindLayerClass = 1
eScopeKindLayer = 2
eScopeKindObjectKind = 3
eScopeKindFootprint = 4
eScopeKindComponentClass = 5
eScopeKindComponent = 6
eScopeKindNetClass = 7
eScopeKindNet = 8
eScopeKindFromToClass = 9
eScopeKindFromTo = 10
eScopeKindPadClass = 11
eScopeKindPadSpec = 12
eScopeKindViaSpec = 13
eScopeKindFootprintPad = 14
eScopeKindPad = 15
eScopeKindRegion = 16

### TRuntimeError (System)

reNone = 0
reOutOfMemory = 1
reInvalidPtr = 2
reDivByZero = 3
reRangeError = 4
reIntOverflow = 5
reInvalidOp = 6
reZeroDivide = 7
reOverflow = 8
reUnderflow = 9
reInvalidCast = 10
reAccessViolation = 11
rePrivInstruction = 12
reControlBreak = 13
reStackOverflow = 14
reVarTypeCast = 15
reVarInvalidOp = 16
reVarDispatch = 17
reVarArrayCreate = 18
reVarNotArray = 19
reVarArrayBounds = 20
reAssertionFailed = 21
reExternalException = 22
reIntfCastError = 23
reSafeCallError = 24
reMonitorNotLocked = 25
reNoMonitorSupport = 26
rePlatformNotImplemented = 27
reObjectDisposed = 28

### TRWBehavior (Rt_NexusDevices)

eRWBehavior_None = 0
eRWBehavior_Write_First = 1
eRWBehavior_Read_First = 2

### TSameNamePadstackReplacementMode (RT_PCB)

eAskUser = 0
eReplaceOne = 1
eReplaceAll = 2
eRenameOne = 3
eRenameAll = 4
eKeepOneExisting = 5
eKeepAllExisting = 6

### TScanClockHaltMode (Rt_NexusDevices)

eScanClockHaltMode_None = 0
eScanClockHaltMode_Low = 1
eScanClockHaltMode_Both = 2

### TScanPinKind (Rt_NexusDevices)

eScanPinKind_Normal = 0
eScanPinKind_TRST = 1
eScanPinKind_TCK = 2
eScanPinKind_TDO = 3
eScanPinKind_TDI = 4
eScanPinKind_TMS = 5
eScanPinKind_Power = 6
eScanPinKind_Ground = 7

### TSchCommandType (Rt_Schematic)

eRotateSelectedObjects = 0
eClipboardPasteMoveObjects = 1
eMoveObjectsByDrag = 2
eAlignObjects = 3
eAlignObjectsToGrid = 4
eCreateWire = 5
eResizeEntryContainer = 6
eEditBasicEntryLocation = 7
eEditLocationCmd = 8
eComponentUpdate = 9
eFlipSheetSymbol = 10

### TSchemaInfo (Data.Win.ADODB)

siAsserts = 0
siCatalogs = 1
siCharacterSets = 2
siCollations = 3
siColumns = 4
siCheckConstraints = 5
siConstraintColumnUsage = 6
siConstraintTableUsage = 7
siKeyColumnUsage = 8
siReferentialConstraints = 9
siTableConstraints = 10
siColumnsDomainUsage = 11
siIndexes = 12
siColumnPrivileges = 13
siTablePrivileges = 14
siUsagePrivileges = 15
siProcedures = 16
siSchemata = 17
siSQLLanguages = 18
siStatistics = 19
siTables = 20
siTranslations = 21
siProviderTypes = 22
siViews = 23
siViewColumnUsage = 24
siViewTableUsage = 25
siProcedureParameters = 26
siForeignKeys = 27
siPrimaryKeys = 28
siProcedureColumns = 29
siDBInfoKeywords = 30
siDBInfoLiterals = 31
siCubes = 32
siDimensions = 33
siHierarchies = 34
siLevels = 35
siMeasures = 36
siProperties = 37
siMembers = 38
siProviderSpecific = 39

### TSchematicNetlister (RT_Workspace)

eSchematicNetlister_VHDL = 0
eSchematicNetlister_Verilog = 1

### TScopeKind (RT_PCB)

eScopeKindBoard = 0
eScopeKindLayerClass = 1
eScopeKindLayer = 2
eScopeKindObjectKind = 3
eScopeKindFootprint = 4
eScopeKindComponentClass = 5
eScopeKindComponent = 6
eScopeKindNetClass = 7
eScopeKindNet = 8
eScopeKindFromToClass = 9
eScopeKindFromTo = 10
eScopeKindPadClass = 11
eScopeKindPadSpec = 12
eScopeKindViaSpec = 13
eScopeKindFootprintPad = 14
eScopeKindPad = 15
eScopeKindRegion = 16
eScopeKindSignalClass = 17
eScopeKindLayerStackRegion = 18
eScopeKindDiffPair = 19
eScopeKindDiffPairClass = 20
eScopeKindPackage = 21
eScopeKindDrillPair = 22
eScopeKindInPolygon = 23
eScopeKindPadType = 24
eScopeKindWithinRoom = 25
eScopeKindNetAndLayer = 26
eScopeKindNetAndFootPrint = 27
eScopeKindLayerAndDiffPairClass = 28
eScopeKindPackageAndComponentClass = 29
eScopeKindFootPrintAndLayer = 30
eScopeKindNetAndPadType = 31
eScopeKindPolygonAndLayer = 32
eScopeKindPadClassAndLayer = 33
eScopeKindObjectKindAndLayer = 34
eScopeKindNetAndDrillPair = 35
eScopeKindNetClassAndDrillPair = 36
eScopeKindSignalClassAndLayer = 37
eScopeKindComponentAndLayer = 38
eScopeKindPackageAndLayer = 39
eScopeKindAdvanced = 40

### TScrollBarKind (Vcl.Forms)

sbHorizontal = 0
sbVertical = 1

### TScrollBarStyle (Vcl.Forms)

ssRegular = 0
ssFlat = 1
ssHotTrack = 2

### TScrollBtn (Vcl.Tabs)

sbLeft = 0
sbRight = 1

### TScrollCode (System.UITypes)

scLineUp = 0
scLineDown = 1
scPageUp = 2
scPageDown = 3
scPosition = 4
scTrack = 5
scTop = 6
scBottom = 7
scEndScroll = 8

### TScrollOrientation (Vcl.Tabs)

soLeftRight = 0
soUpDown = 1

### TScrollStyle (System.UITypes)

ssNone = 0
ssHorizontal = 1  // 脚本里是 10
ssVertical = 2
ssBoth = 3

### TSdConflictKind (Rt_SystemDesign.Interfaces)

sdckConflict_PinNetName = 0

### TSdEntryType (Rt_SystemDesign.Interfaces)

Male = 0
Female = 1

### TSearchDirection (Vcl.ComCtrls)

sdLeft = 0
sdRight = 1
sdAbove = 2
sdBelow = 3
sdAll = 4

### TSearchType (Vcl.ComCtrls)

stWholeWord = 0
stMatchCase = 1

### TSectionTrackState (Vcl.ComCtrls)

tsTrackBegin = 0
tsTrackMove = 1
tsTrackEnd = 2

### TSeekOption (Data.Win.ADODB)

soFirstEQ = 0
soLastEQ = 1
soAfterEQ = 2
soAfter = 3
soBeforeEQ = 4
soBefore = 5

### TSeekOrigin (System.Classes)

soBeginning = 0
soCurrent = 1
soEnd = 2

### TSelectMode (Rt_NexusDevices)

eSelectMode_NanoboardChain = 0
eSelectMode_CurrentChain = 1
eSelectMode_HardChain = 2
eSelectMode_SoftChain = 3
eSelectMode_DontCare = 4

### TSetOperation (RT_PCB)

eSetOperation_Difference = 0
eSetOperation_Intersection = 1
eSetOperation_ExculsiveOr = 2
eSetOperation_Union = 3

### TShape (RT_PCB)

eNoShape = 0
eRounded = 1
eRectangular = 2
eOctagonal = 3
eCircleShape = 4
eArcShape = 5
eTerminator = 6
eRoundRectShape = 7
eRotatedRectShape = 8
eRoundedRectangular = 9
eCustomShape = 10

### TShapeSubKind (RT_PCB)

eNoKind = 0
eOctagonalFinger = 1
eRoundedFinger = 2
eRoundedRectangle = 3
eChamferedRectangle = 4

### TShapeType (Vcl.ExtCtrls)

stRectangle = 0
stSquare = 1
stRoundRect = 2
stRoundSquare = 3
stEllipse = 4
stCircle = 5

### TSheetDocumentBorderStyle (Rt_Schematic)

eSheetStandard = 0
eSheetAnsi = 1

### TSheetOrientation (Rt_Schematic)

eLandscape = 0
ePortrait = 1

### TSheetReferenceZoneStyle (Rt_Schematic)

eSheetReferenceZone_Default = 0
eSheetReferenceZone_ASME = 1

### TSheetStyle (Rt_Schematic)

eSheetA4 = 0
eSheetA3 = 1
eSheetA2 = 2
eSheetA1 = 3
eSheetA0 = 4
eSheetA = 5
eSheetB = 6
eSheetC = 7
eSheetD = 8
eSheetE = 9
eSheetLetter = 10
eSheetLegal = 11
eSheetTabloid = 12
eSheetOrcadA = 13
eSheetOrcadB = 14
eSheetOrcadC = 15
eSheetOrcadD = 16
eSheetOrcadE = 17

### TSheetSymbolType (Rt_Schematic)

eSheetSymbolType_Normal = 0
eSheetSymbolType_DeviceSheet = 1
eSheetSymbolType_DesignItem = 2

### TShowAction (Vcl.Forms)

saIgnore = 0
saRestore = 1
saMinimize = 2
saMaximize = 3

### TShowCutterBoxMode (Rt_Schematic)

eBoxNever = 0
eBoxAlways = 1
eBoxOnPolyline = 2

### TShowCutterMarkersMode (Rt_Schematic)

eMarkersNever = 0
eMarkersAlways = 1
eMarkersOnPolyline = 2

### TSignalDirection (RT_Workspace)

eSignalUndefined = 0
eSignalInput = 1
eSignalOutput = 2
eSignalInOut = 3

### TSignalLevel (RT_PCB)

eLowLevel = 0
eHighLevel = 1

### TSize (Rt_Schematic)

eZeroSize = 0
eSmall = 1
eMedium = 2
eLarge = 3

### TSizeMode (Vcl.OleCtnrs)

smClip = 0
smCenter = 1
smScale = 2
smStretch = 3
smAutoSize = 4

### TSizeStyle (Vcl.ExtCtrls)

ssAbsolute = 0
ssPercent = 1
ssAuto = 2

### TSizingOrientation (Vcl.ToolWin)

soNone = 0
soHorizontal = 1  // 脚本里是 0
soVertical = 2  // 脚本里是 1

### TSkipOption (RT_Supplier)

eSkipProducts = 0
eSkipPricing = 1
eSkipInventory = 2
eSkipDatasheets = 3
eSkipAttributes = 4

### TSmartUnionAlignmentType (RT_PCB)

eBottom = 0  // 脚本里是 1
eTop = 1  // 脚本里是 3

### TSmartUnionObjectType (RT_PCB)

eUnknown = 0
eDrillTable = 1
eViaStitching = 2
eLayerStackTable = 3
eAccordion = 4
eMetaDataSmartUnion = 5
eViaShielding = 6
eMultilineText = 7
eAccordionDiffPair = 8
eRectangleSmartUnion = 9

### TSnippetCreationMode (RT_ClientServerInterface)

eSnippetCreationBySelection = 0
eSnippetCreationByUnionIndex = 1

### TSnippetKind (RT_ClientServerInterface)

skUnknown = 0
skSchematic = 1
skPCB = 2

### TSortType (Vcl.ComCtrls)

stNone = 0
stData = 1
stText = 2
stBoth = 3

### TSourceChangeAction (Rt_Schematic)

eUnknownAction = 0
eClear = 1
eSkip = 2
eSelectNew = 3
eCancelChangeSource = 4

### TSourceRelationshipAttribute (RT_SupplierManager)

eSourceRelationship_SupplierName = 0
eSourceRelationship_SupplierPartNumber = 1
eSourceRelationship_ManufacturerName = 2
eSourceRelationship_ManufacturerPartNumber = 3
eSourceRelationship_RoHS = 4
eSourceRelationship_Description = 5
eSourceRelationship_Category = 6
eSourceRelationship_Pricing = 7
eSourceRelationship_Stock = 8

### TSplitRectType (System.Types)

srLeft = 0
srRight = 1
srTop = 2
srBottom = 3

### TSQLToken (Data.DBCommon)

stUnknown = 0
stTableName = 1
stFieldName = 2
stAscending = 3
stDescending = 4
stSelect = 5
stFrom = 6
stWhere = 7
stGroupBy = 8
stHaving = 9
stUnion = 10
stPlan = 11
stOrderBy = 12
stForUpdate = 13
stEnd = 14
stPredicate = 15
stValue = 16
stIsNull = 17
stIsNotNull = 18
stLike = 19
stAnd = 20
stOr = 21
stNumber = 22
stAllFields = 23
stComment = 24
stDistinct = 25

### TStateOfFeature (RT_ClientServerInterface)

fsPublic = 0
fsOpenBeta = 1
fsClosedBeta = 2
fsInDev = 3
fsReleased = 4

### TStaticBorderStyle (Vcl.StdCtrls)

sbsNone = 0
sbsSingle = 1
sbsSunken = 2

### TStatusPanelBevel (Vcl.ComCtrls)

pbNone = 0
pbLowered = 1
pbRaised = 2

### TStatusPanelStyle (Vcl.ComCtrls)

psText = 0
psOwnerDraw = 1

### TStdLogicState (Rt_Schematic)

eStdLogic_Unitialized = 0
eStdLogic_ForcingUnknown = 1
eStdLogic_Forcing0 = 2
eStdLogic_Forcing1 = 3
eStdLogic_HiZ = 4
eStdLogic_WeakUnknown = 5
eStdLogic_Weak0 = 6
eStdLogic_Weak1 = 7
eStdLogic_DontCare = 8

### TStimulusType (RT_PCB)

eConstantLevel = 0
eSinglePulse = 1
ePeriodicPulse = 2

### TStopBits (RT_PCB)

eStopBits1 = 0
eStopBits1_5 = 1
eDataBits2 = 2

### TStreamOriginalFormat (System.Classes)

sofUnknown = 0
sofBinary = 1
sofText = 2
sofUTF8Text = 3

### TStreamOwnership (System.Classes)

soReference = 0
soOwned = 1

### TStringSeachOption (System.StrUtils)

soDown = 0
soMatchCase = 1
soWholeWord = 2

### TSuperscriptMode (Rt_Schematic)

eSuperScript_Never = 0
eSuperScript_Always = 1
eSuperScript_Smart = 2

### TSupplierIncludeOption (RT_Supplier)

eInclude_Pricing = 0
eInclude_Attributes = 1
eInclude_Datasheets = 2
eInclude_Aliases = 3
eInclude_PartsWithoutSuppliers = 4

### TSupplierSearchFilter (RT_Supplier)

eFilter_InStock = 0
eFilter_RoHSCompliant = 1
eFilter_LeadFree = 2
eFilter_PrototypeQuantities = 3
eFilter_CutTape = 4
eFilter_TopSellers = 5
eFilter_NoSpecialOrderItems = 6

### TSVGElementType (RSSVGTypes)

etNone = 0
etDoc = 1  // 脚本里不可用
etGroup = 2  // 脚本里不可用
etImage = 3  // 脚本里不可用
etDefs = 4  // 脚本里不可用
etUse = 5  // 脚本里不可用
etCircle = 6  // 脚本里是 1
etEllipse = 7  // 脚本里是 2
etRectangle = 8  // 脚本里不可用
etLine = 9  // 脚本里是 0
etPolyline = 10  // 脚本里不可用
etPolygon = 11  // 脚本里不可用
etPath = 12  // 脚本里不可用
etText = 13  // 脚本里不可用
etSwitch = 14  // 脚本里不可用
etDesc = 15  // 脚本里不可用
etTitle = 16  // 脚本里不可用
etStyle = 17  // 脚本里不可用
etTSpan = 18  // 脚本里不可用
etTextPath = 19  // 脚本里不可用
etTRef = 20  // 脚本里不可用
etClipPath = 21  // 脚本里不可用
etLinearGradient = 22  // 脚本里不可用
etRadialGradient = 23  // 脚本里不可用
etGradientStop = 24  // 脚本里不可用
etMarker = 25  // 脚本里不可用
etMetadata = 26  // 脚本里不可用
etScript = 27  // 脚本里不可用
etComment = 28  // 脚本里不可用
etSymbol = 29  // 脚本里是 1
etPattern = 30  // 脚本里不可用

### TSysLinkType (Vcl.ExtCtrls)

sltURL = 0
sltID = 1

### TTabletOption (Vcl.Controls)

toPressAndHold = 0
toPenTapFeedback = 1
toPenBarrelFeedback = 2
toTouchUIForceOn = 3
toTouchUIForceOff = 4
toTouchSwitch = 5
toFlicks = 6
toSmoothScrolling = 7
toFlickFallbackKeys = 8

### TTabPosition (Vcl.ComCtrls)

tpTop = 0
tpBottom = 1
tpLeft = 2
tpRight = 3

### TTabSetTabStyle (Vcl.Tabs)

tsStandard = 0
tsOwnerDraw = 1
tsSoftTabs = 2
tsModernTabs = 3
tsModernPopout = 4

### TTabStyle (Vcl.ComCtrls)

tsTabs = 0
tsButtons = 1
tsFlatButtons = 2

### TTapState (Rt_NexusDevices)

TapState_Undefined = 0
TEST_LOGIC_RESET = 1
RUN_TEST_IDLE = 2
SELECT_DR = 3
CAPTURE_DR = 4
SHIFT_DR = 5
EXIT1_DR = 6
PAUSE_DR = 7
EXIT2_DR = 8
UPDATE_DR = 9
SELECT_IR = 10
CAPTURE_IR = 11
SHIFT_IR = 12
EXIT1_IR = 13
PAUSE_IR = 14
EXIT2_IR = 15
UPDATE_IR = 16

### TTargetLengthMode (RT_PCB)

eTargetLength_Manual = 0
eTargetLength_FromNet = 1
eTargetLength_FromRules = 2
eTargetLength_FromDiffPairs = 3

### TTaskDialogCommonButton (Vcl.Dialogs)

tcbOk = 0
tcbYes = 1
tcbNo = 2
tcbCancel = 3
tcbRetry = 4
tcbClose = 5

### TTaskDialogFlag (Vcl.Dialogs)

tfEnableHyperlinks = 0
tfUseHiconMain = 1
tfUseHiconFooter = 2
tfAllowDialogCancellation = 3
tfUseCommandLinks = 4
tfUseCommandLinksNoIcon = 5
tfExpandFooterArea = 6
tfExpandedByDefault = 7
tfVerificationFlagChecked = 8
tfShowProgressBar = 9
tfShowMarqueeProgressBar = 10
tfCallbackTimer = 11
tfPositionRelativeToWindow = 12
tfRtlLayout = 13
tfNoDefaultRadioButton = 14
tfCanBeMinimized = 15

### TTBDrawingStyle (Vcl.ComCtrls)

dsNormal = 0
dsGradient = 1

### TTeardropActionEx (RT_PCB)

eTeardropAction_Add = 0
eTeardropAction_Remove = 1

### TTeardropObject (RT_PCB)

eTeardropObject_Via = 0
eTeardropObject_Pad = 1
eTeardropObject_Track = 2
eTeardropObject_TJunction = 3

### TTeardropStyleEx (RT_PCB)

eTeardropStyle_Curve = 0
eTeardropStyle_Line = 1

### TTemplateKind (RT_Workspace)

tkBOM = 0
tkSchematic = 1
tkDraftsmanSheet = 2
tkDraftsmanDocument = 3
tkProject = 4
tkFootprint = 5
tkSymbol = 6
tkPCB = 7
tkActiveBOM = 8
tkOutputJob = 9
tkMultiBoardSchematic = 10
tkMultiBoardAssembly = 11
tkLayerStack = 12
tkCAMTastic = 13
tkDatabaseLib = 14
tkDatabaseLink = 15
tkPcb3DLib = 16
tkScriptDSUnit = 17
tkScriptDSForm = 18
tkScriptVBSUnit = 19
tkScriptVBSForm = 20
tkScriptJSUnit = 21
tkScriptJSForm = 22
tkScriptTclUnit = 23
tkScriptBasUnit = 24

### TTemplateSource (RT_Workspace)

tsAny = 0
tsLocal = 1
tsServer = 2

### TTemplateUpdateAction (Rt_Schematic)

eTemplateUpdate_DoNothing = 0
eTemplateUpdate_OnlyAddNewParameters = 1
eTemplateUpdate_OverrideAllParameters = 2
eTemplateUpdate_Auto = 3

### TTestpointAllowedSide (RT_PCB)

eAllowTopSide = 0
eAllowBottomSide = 1

### TTestpointValid (RT_PCB)

eRequire = 0
eInvalid = 1
eIgnore = 2  // 脚本里是 8
eRequireAtLeafs = 3

### TTextAutoposition (Pcbtypes)

eAutoPos_Manual = 0
eAutoPos_TopLeft = 1
eAutoPos_CenterLeft = 2
eAutoPos_BottomLeft = 3
eAutoPos_TopCenter = 4
eAutoPos_CenterCenter = 5
eAutoPos_BottomCenter = 6
eAutoPos_TopRight = 7
eAutoPos_CenterRight = 8
eAutoPos_BottomRight = 9

### TTextAutoposition (RT_PCB)

eAutoPos_Manual = 0
eAutoPos_TopLeft = 1
eAutoPos_CenterLeft = 2
eAutoPos_BottomLeft = 3
eAutoPos_TopCenter = 4
eAutoPos_CenterCenter = 5
eAutoPos_BottomCenter = 6
eAutoPos_TopRight = 7
eAutoPos_CenterRight = 8
eAutoPos_BottomRight = 9

### TTextBorderSpaceType (RT_PCB)

bstMargin = 0
bstOffset = 1

### TTextFormats (Vcl.Graphics)

tfBottom = 0
tfCalcRect = 1
tfCenter = 2
tfEditControl = 3
tfEndEllipsis = 4
tfPathEllipsis = 5
tfExpandTabs = 6
tfExternalLeading = 7
tfLeft = 8
tfModifyString = 9
tfNoClip = 10
tfNoPrefix = 11
tfRight = 12
tfRtlReading = 13
tfSingleLine = 14
tfTop = 15
tfVerticalCenter = 16
tfWordBreak = 17
tfHidePrefix = 18
tfNoFullWidthCharBreak = 19
tfPrefixOnly = 20
tfTabStop = 21
tfWordEllipsis = 22
tfComposited = 23

### TTextHorzAnchor (Rt_Schematic)

eTextHorzAnchor_None = 0
eTextHorzAnchor_Both = 1
eTextHorzAnchor_Left = 2
eTextHorzAnchor_Right = 3

### TTextJustification (Rt_Schematic)

eJustify_BottomLeft = 0
eJustify_BottomCenter = 1
eJustify_BottomRight = 2
eJustify_CenterLeft = 3
eJustify_Center = 4
eJustify_CenterRight = 5
eJustify_TopLeft = 6
eJustify_TopCenter = 7
eJustify_TopRight = 8

### TTextKind (Pcbtypes)

eText_StrokeFont = 0
eText_TrueTypeFont = 1
eText_BarCode = 2

### TTextKind (RT_PCB)

eText_StrokeFont = 0
eText_TrueTypeFont = 1
eText_BarCode = 2

### TTextLayout (Vcl.StdCtrls)

tlTop = 0
tlCenter = 1
tlBottom = 2

### TTextLineBreakStyle (System)

tlbsLF = 0
tlbsCRLF = 1

### TTextVertAnchor (Rt_Schematic)

eTextVertAnchor_None = 0
eTextVertAnchor_Both = 1
eTextVertAnchor_Top = 2
eTextVertAnchor_Bottom = 3

### TThermalReliefDefinedType (RT_PCB)

trdRule = 0
trdUser = 1
trdDefault = 2

### TThreadPriority (System.Classes)

tpIdle = 0
tpLowest = 1
tpLower = 2
tpNormal = 3
tpHigher = 4
tpHighest = 5
tpTimeCritical = 6

### TTickMark (Vcl.ComCtrls)

tmBottomRight = 0
tmTopLeft = 1
tmBoth = 2

### TTickStyle (Vcl.ComCtrls)

tsNone = 0
tsAuto = 1
tsManual = 2

### TTileMode (Vcl.Forms)

tbHorizontal = 0
tbVertical = 1

### TTimerMode (Vcl.Forms)

tmShow = 0
tmHide = 1

### TTimeUnits (Rt_Util)

eFs = 0
ePs = 1
eNs = 2
eUs = 3
eMs = 4
eS = 5

### TTimeZoneConversion (Rt_Util)

eTZC_UTC = 0
eTZC_LOCAL = 1

### TTipMode (Vcl.Controls)

tipClose = 0
tipOpen = 1
tipDontCare = 2

### TToolButtonStyle (Vcl.ComCtrls)

tbsButton = 0
tbsCheck = 1
tbsDropDown = 2
tbsSeparator = 3
tbsDivider = 4
tbsTextButton = 5

### TTouchProperty (Vcl.Controls)

tpInteractiveGestures = 0
tpInteractiveGestureOptions = 1
tpParentTabletOptions = 2
tpTabletOptions = 3

### TTrackBarOrientation (Vcl.ComCtrls)

trHorizontal = 0
trVertical = 1

### TTrackButton (Vcl.Menus)

tbRightButton = 0
tbLeftButton = 1

### TTransparentMode (Vcl.Graphics)

tmAuto = 0
tmFixed = 1

### TTypeKind (System)

tkUnknown = 0
tkInteger = 1
tkChar = 2
tkEnumeration = 3
tkFloat = 4
tkString = 5
tkSet = 6
tkClass = 7
tkMethod = 8
tkWChar = 9
tkLString = 10
tkWString = 11
tkVariant = 12
tkArray = 13
tkRecord = 14
tkInterface = 15
tkInt64 = 16
tkDynArray = 17
tkUString = 18
tkClassRef = 19
tkPointer = 20
tkProcedure = 21

### TU3DFlag (RT_Workspace)

U3D_Activate = 0
U3D_Toolbar = 1
U3D_Navigation = 2

### TUDAlignButton (Vcl.ComCtrls)

udLeft = 0
udRight = 1

### TUDBtnType (Vcl.ComCtrls)

btNext = 0
btPrev = 1

### TUdmClient (RT_Workspace)

eUdmDisabled = 0
eUdmNetColors = 1
eUdmNavigator = 2
eUdmProjectView = 3

### TUDOrientation (Vcl.ComCtrls)

udHorizontal = 0
udVertical = 1

### TUnionTypeID (RT_PCB)

eUnionTypeID_SimpleUnion = 0
eUnionTypeID_DrillTable = 1
eUnionTypeID_LayerStackTable = 2
eUnionTypeID_NetLengthTuning = 3
eUnionTypeID_ViaStitching = 4
eUnionTypeID_ViaShielding = 5
eUnionTypeID_SmartPaste = 6
eUnionTypeID_StackedMicroVia = 7
eUnionTypeID_StaggeredMicroVia = 8
eUnionTypeID_DiffPairLengthTuning = 9
eUnionTypeID_Rectangle = 10

### TUnit (RT_PCB)

eMetric = 0  // 脚本里是 1
eImperial = 1  // 脚本里是 0

### TUnit (Rt_Schematic)

eMil = 0
eMM = 1
eIN = 2
eCM = 3
eDXP = 4
eM = 5
eAutoImperial = 6
eAutoMetric = 7

### TUnitStyle (Pcbtypes)

eNoUnits = 0
eYesUnits = 1
eParenthUnits = 2

### TUnitStyle (RT_PCB)

eNoUnits = 0
eYesUnits = 1
eParenthUnits = 2

### TUnitSystem (Rt_Schematic)

eImperial = 0
eMetric = 1

### TUnitType (Vcl.Imaging.pngimage)

utUnknown = 0
utMeter = 1

### TUpdateAction (Data.DB)

uaFail = 0
uaAbort = 1
uaSkip = 2
uaRetry = 3
uaApplied = 4

### TUpdateCheckFrequency (RT_ClientServerInterface)

Never = 0
EveryDay = 1
Every3days = 2
EveryWeek = 3
Every2Weeks = 4
EveryMonth = 5
OnStartUp = 6

### TUpdateKind (Data.DB)

ukModify = 0
ukInsert = 1
ukDelete = 2

### TUpdatePartTarget (Rt_Schematic)

eContext = 0
eSelected = 1
eAll = 2

### TUpdateStatus (Data.DB)

usUnmodified = 0
usModified = 1
usInserted = 2
usDeleted = 3

### TUpDownDirection (Vcl.ComCtrls)

updNone = 0
updUp = 1
updDown = 2

### TUpDownKind (XPExtCtrls)

udkHorizontal = 0
udkVertical = 1

### TV6_Layer (RT_PCB)

eV6_NoLayer = 0
eV6_TopLayer = 1
eV6_MidLayer1 = 2
eV6_MidLayer2 = 3
eV6_MidLayer3 = 4
eV6_MidLayer4 = 5
eV6_MidLayer5 = 6
eV6_MidLayer6 = 7
eV6_MidLayer7 = 8
eV6_MidLayer8 = 9
eV6_MidLayer9 = 10
eV6_MidLayer10 = 11
eV6_MidLayer11 = 12
eV6_MidLayer12 = 13
eV6_MidLayer13 = 14
eV6_MidLayer14 = 15
eV6_MidLayer15 = 16
eV6_MidLayer16 = 17
eV6_MidLayer17 = 18
eV6_MidLayer18 = 19
eV6_MidLayer19 = 20
eV6_MidLayer20 = 21
eV6_MidLayer21 = 22
eV6_MidLayer22 = 23
eV6_MidLayer23 = 24
eV6_MidLayer24 = 25
eV6_MidLayer25 = 26
eV6_MidLayer26 = 27
eV6_MidLayer27 = 28
eV6_MidLayer28 = 29
eV6_MidLayer29 = 30
eV6_MidLayer30 = 31
eV6_BottomLayer = 32
eV6_TopOverlay = 33
eV6_BottomOverlay = 34
eV6_TopPaste = 35
eV6_BottomPaste = 36
eV6_TopSolder = 37
eV6_BottomSolder = 38
eV6_InternalPlane1 = 39
eV6_InternalPlane2 = 40
eV6_InternalPlane3 = 41
eV6_InternalPlane4 = 42
eV6_InternalPlane5 = 43
eV6_InternalPlane6 = 44
eV6_InternalPlane7 = 45
eV6_InternalPlane8 = 46
eV6_InternalPlane9 = 47
eV6_InternalPlane10 = 48
eV6_InternalPlane11 = 49
eV6_InternalPlane12 = 50
eV6_InternalPlane13 = 51
eV6_InternalPlane14 = 52
eV6_InternalPlane15 = 53
eV6_InternalPlane16 = 54
eV6_DrillGuide = 55
eV6_KeepOutLayer = 56
eV6_Mechanical1 = 57
eV6_Mechanical2 = 58
eV6_Mechanical3 = 59
eV6_Mechanical4 = 60
eV6_Mechanical5 = 61
eV6_Mechanical6 = 62
eV6_Mechanical7 = 63
eV6_Mechanical8 = 64
eV6_Mechanical9 = 65
eV6_Mechanical10 = 66
eV6_Mechanical11 = 67
eV6_Mechanical12 = 68
eV6_Mechanical13 = 69
eV6_Mechanical14 = 70
eV6_Mechanical15 = 71
eV6_Mechanical16 = 72
eV6_DrillDrawing = 73
eV6_MultiLayer = 74
eV6_ConnectLayer = 75
eV6_BackGroundLayer = 76
eV6_DRCErrorLayer = 77
eV6_HighlightLayer = 78
eV6_GridColor1 = 79
eV6_GridColor10 = 80
eV6_PadHoleLayer = 81
eV6_ViaHoleLayer = 82

### TV6_PlotLayer (RT_PCB)

eV6_NullPlot = 0
eV6_TopLayerPlot = 1
eV6_MidLayer1Plot = 2
eV6_MidLayer2Plot = 3
eV6_MidLayer3Plot = 4
eV6_MidLayer4Plot = 5
eV6_MidLayer5Plot = 6
eV6_MidLayer6Plot = 7
eV6_MidLayer7Plot = 8
eV6_MidLayer8Plot = 9
eV6_MidLayer9Plot = 10
eV6_MidLayer10Plot = 11
eV6_MidLayer11Plot = 12
eV6_MidLayer12Plot = 13
eV6_MidLayer13Plot = 14
eV6_MidLayer14Plot = 15
eV6_MidLayer15Plot = 16
eV6_MidLayer16Plot = 17
eV6_MidLayer17Plot = 18
eV6_MidLayer18Plot = 19
eV6_MidLayer19Plot = 20
eV6_MidLayer20Plot = 21
eV6_MidLayer21Plot = 22
eV6_MidLayer22Plot = 23
eV6_MidLayer23Plot = 24
eV6_MidLayer24Plot = 25
eV6_MidLayer25Plot = 26
eV6_MidLayer26Plot = 27
eV6_MidLayer27Plot = 28
eV6_MidLayer28Plot = 29
eV6_MidLayer29Plot = 30
eV6_MidLayer30Plot = 31
eV6_BottomLayerPlot = 32
eV6_TopOverlayPlot = 33
eV6_BottomOverlayPlot = 34
eV6_TopPastePlot = 35
eV6_BottomPastePlot = 36
eV6_TopSolderPlot = 37
eV6_BottomSolderPlot = 38
eV6_InternalPlane1Plot = 39
eV6_InternalPlane2Plot = 40
eV6_InternalPlane3Plot = 41
eV6_InternalPlane4Plot = 42
eV6_InternalPlane5Plot = 43
eV6_InternalPlane6Plot = 44
eV6_InternalPlane7Plot = 45
eV6_InternalPlane8Plot = 46
eV6_InternalPlane9Plot = 47
eV6_InternalPlane10Plot = 48
eV6_InternalPlane11Plot = 49
eV6_InternalPlane12Plot = 50
eV6_InternalPlane13Plot = 51
eV6_InternalPlane14Plot = 52
eV6_InternalPlane15Plot = 53
eV6_InternalPlane16Plot = 54
eV6_DrillGuide_Top_BottomPlot = 55
eV6_DrillGuide_Top_Mid1Plot = 56
eV6_DrillGuide_Mid2_Mid3Plot = 57
eV6_DrillGuide_Mid4_Mid5Plot = 58
eV6_DrillGuide_Mid6_Mid7Plot = 59
eV6_DrillGuide_Mid8_Mid9Plot = 60
eV6_DrillGuide_Mid10_Mid11Plot = 61
eV6_DrillGuide_Mid12_Mid13Plot = 62
eV6_DrillGuide_Mid14_Mid15Plot = 63
eV6_DrillGuide_Mid16_Mid17Plot = 64
eV6_DrillGuide_Mid18_Mid19Plot = 65
eV6_DrillGuide_Mid20_Mid21Plot = 66
eV6_DrillGuide_Mid22_Mid23Plot = 67
eV6_DrillGuide_Mid24_Mid25Plot = 68
eV6_DrillGuide_Mid26_Mid27Plot = 69
eV6_DrillGuide_Mid28_Mid29Plot = 70
eV6_DrillGuide_Mid30_BottomPlot = 71
eV6_DrillGuide_SpecialPlot = 72
eV6_KeepOutLayerPlot = 73
eV6_Mechanical1Plot = 74
eV6_Mechanical2Plot = 75
eV6_Mechanical3Plot = 76
eV6_Mechanical4Plot = 77
eV6_Mechanical5Plot = 78
eV6_Mechanical6Plot = 79
eV6_Mechanical7Plot = 80
eV6_Mechanical8Plot = 81
eV6_Mechanical9Plot = 82
eV6_Mechanical10Plot = 83
eV6_Mechanical11Plot = 84
eV6_Mechanical12Plot = 85
eV6_Mechanical13Plot = 86
eV6_Mechanical14Plot = 87
eV6_Mechanical15Plot = 88
eV6_Mechanical16Plot = 89
eV6_DrillDrawing_Top_BottomPlot = 90
eV6_DrillDrawing_Top_Mid1Plot = 91
eV6_DrillDrawing_Mid2_Mid3Plot = 92
eV6_DrillDrawing_Mid4_Mid5Plot = 93
eV6_DrillDrawing_Mid6_Mid7Plot = 94
eV6_DrillDrawing_Mid8_Mid9Plot = 95
eV6_DrillDrawing_Mid10_Mid11Plot = 96
eV6_DrillDrawing_Mid12_Mid13Plot = 97
eV6_DrillDrawing_Mid14_Mid15Plot = 98
eV6_DrillDrawing_Mid16_Mid17Plot = 99
eV6_DrillDrawing_Mid18_Mid19Plot = 100
eV6_DrillDrawing_Mid20_Mid21Plot = 101
eV6_DrillDrawing_Mid22_Mid23Plot = 102
eV6_DrillDrawing_Mid24_Mid25Plot = 103
eV6_DrillDrawing_Mid26_Mid27Plot = 104
eV6_DrillDrawing_Mid28_Mid29Plot = 105
eV6_DrillDrawing_Mid30_BottomPlot = 106
eV6_DrillDrawing_SpecialPlot = 107
eV6_TopPadMasterPlot = 108
eV6_BottomPadMasterPlot = 109

### TValueDisplay (XPTrack)

dvNone = 0
dvLeft = 1
dvTop = 2
dvRight = 3
dvBottom = 4

### TValueType (System.Classes)

vaNull = 0
vaList = 1
vaInt8 = 2
vaInt16 = 3
vaInt32 = 4
vaExtended = 5
vaString = 6
vaIdent = 7
vaFalse = 8
vaTrue = 9
vaBinary = 10
vaSet = 11
vaLString = 12
vaNil = 13
vaCollection = 14
vaSingle = 15
vaCurrency = 16
vaDate = 17
vaWString = 18
vaInt64 = 19
vaUTF8String = 20
vaDouble = 21

### TVaraintGroupSource (RT_Workspace)

vgsDocument = 0
vgsSheetSymbol = 1
vgsComponentClass = 2

### TVarCompareResult (System.Variants)

crLessThan = 0
crEqual = 1
crGreaterThan = 2

### TVariantGraphics (RT_Workspace)

eVariantGraphics_Cross = 0
eVariantGraphics_MeshBox = 1

### TVariantRelationship (System.Variants)

vrEqual = 0
vrLessThan = 1
vrGreaterThan = 2
vrNotEqual = 3

### TVariationKind (RT_Workspace)

eVariation_None = 0
eVariation_NotFitted = 1
eVariation_Alternate = 2

### TVertexAction (RT_PCB)

eDeform = 0
eScale = 1
eSmooth = 2

### TVerticalAlignment (System.Classes)

taAlignTop = 0
taAlignBottom = 1
taVerticalCenter = 2

### TVHDLStatus (Rt_VHDL)

V_READY = 0
V_HALTED = 1
V_STOPPED = 2
V_RUNNING = 3
V_DONE = 4
V_INPUT_PENDING = 5
V_ASSERTION_PENDING = 6

### TViaStructureFeatureSide (RT_PCB)

eViaStructureFeatureSide_Top = 0
eViaStructureFeatureSide_Bottom = 1
eViaStructureFeatureSide_Both = 2

### TViaStructureFeatureType (RT_PCB)

eViaStructureFeatureType_Tenting = 0
eViaStructureFeatureType_Covering = 1
eViaStructureFeatureType_Plugging = 2
eViaStructureFeatureType_Filling = 3
eViaStructureFeatureType_Capping = 4

### TViaStructureType (RT_PCB)

eViaStructureType_None = 0
eViaStructureType_1A_Tenting = 1
eViaStructureType_1B_Tenting = 2
eViaStructureType_2A_TentingAndCovering = 3
eViaStructureType_2B_TentingAndCovering = 4
eViaStructureType_3A_Plugging = 5
eViaStructureType_3B_Plugging = 6
eViaStructureType_4A_PluggingAndCovering = 7
eViaStructureType_4B_PluggingAndCovering = 8
eViaStructureType_5_Filling = 9
eViaStructureType_6A_FillingAndCovering = 10
eViaStructureType_6B_FillingAndCovering = 11
eViaStructureType_7_FillingAndCapping = 12

### TViaType (RT_PCB)

InvalidVia = 0
Thru = 1
Blind = 2
Buried = 3
BackdrillHole = 4
MicroVia = 5
SkipVia = 6

### TViewableObjectID (RT_PCB)

eViewableObject_None = 0
eViewableObject_Arc = 1
eViewableObject_Pad = 2
eViewableObject_Via = 3
eViewableObject_Track = 4
eViewableObject_Text = 5
eViewableObject_Fill = 6
eViewableObject_Connection = 7
eViewableObject_Net = 8
eViewableObject_Component = 9
eViewableObject_Poly = 10
eViewableObject_LinearDimension = 11
eViewableObject_AngularDimension = 12
eViewableObject_RadialDimension = 13
eViewableObject_LeaderDimension = 14
eViewableObject_DatumDimension = 15
eViewableObject_BaselineDimension = 16
eViewableObject_CenterDimension = 17
eViewableObject_OriginalDimension = 18
eViewableObject_LinearDiameterDimension = 19
eViewableObject_RadialDiameterDimension = 20
eViewableObject_Coordinate = 21
eViewableObject_Class = 22
eViewableObject_Rule_Clearance = 23
eViewableObject_Rule_ParallelSegment = 24
eViewableObject_Rule_MaxMinWidth = 25
eViewableObject_Rule_MaxMinLength = 26
eViewableObject_Rule_MatchedLengths = 27
eViewableObject_Rule_DaisyChainStubLength = 28
eViewableObject_Rule_PowerPlaneConnectStyle = 29
eViewableObject_Rule_RoutingTopology = 30
eViewableObject_Rule_RoutingPriority = 31
eViewableObject_Rule_RoutingLayers = 32
eViewableObject_Rule_RoutingCornerStyle = 33
eViewableObject_Rule_RoutingViaStyle = 34
eViewableObject_Rule_PowerPlaneClearance = 35
eViewableObject_Rule_SolderMaskExpansion = 36
eViewableObject_Rule_PasteMaskExpansion = 37
eViewableObject_Rule_ShortCircuit = 38
eViewableObject_Rule_BrokenNets = 39
eViewableObject_Rule_ViasUnderSMD = 40
eViewableObject_Rule_MaximumViaCount = 41
eViewableObject_Rule_MinimumAnnularRing = 42
eViewableObject_Rule_PolygonConnectStyle = 43
eViewableObject_Rule_AcuteAngle = 44
eViewableObject_Rule_ConfinementConstraint = 45
eViewableObject_Rule_SMDToCorner = 46
eViewableObject_Rule_ComponentClearance = 47
eViewableObject_Rule_ComponentRotations = 48
eViewableObject_Rule_PermittedLayers = 49
eViewableObject_Rule_NetsToIgnore = 50
eViewableObject_Rule_SignalStimulus = 51
eViewableObject_Rule_Overshoot_FallingEdge = 52
eViewableObject_Rule_Overshoot_RisingEdge = 53
eViewableObject_Rule_Undershoot_FallingEdge = 54
eViewableObject_Rule_Undershoot_RisingEdge = 55
eViewableObject_Rule_MaxMinImpedance = 56
eViewableObject_Rule_SignalTopValue = 57
eViewableObject_Rule_SignalBaseValue = 58
eViewableObject_Rule_FlightTime_RisingEdge = 59
eViewableObject_Rule_FlightTime_FallingEdge = 60
eViewableObject_Rule_LayerStack = 61
eViewableObject_Rule_MaxSlope_RisingEdge = 62
eViewableObject_Rule_MaxSlope_FallingEdge = 63
eViewableObject_Rule_SupplyNets = 64
eViewableObject_Rule_MaxMinHoleSize = 65
eViewableObject_Rule_TestPointStyle = 66
eViewableObject_Rule_TestPointUsage = 67
eViewableObject_Rule_UnconnectedPin = 68
eViewableObject_Rule_SMDToPlane = 69
eViewableObject_Rule_SMDNeckDown = 70
eViewableObject_Rule_LayerPair = 71
eViewableObject_Rule_FanoutControl = 72
eViewableObject_Rule_MaxMinHeight = 73
eViewableObject_Rule_DifferentialPairs = 74
eViewableObject_Rule_HoleToHoleClearance = 75
eViewableObject_Rule_MinimumSolderMaskSliver = 76
eViewableObject_Rule_SilkToSolderMaskClearance = 77
eViewableObject_Rule_SilkToSilkClearance = 78
eViewableObject_Rule_NetAntennae = 79
eViewableObject_FromTo = 80
eViewableObject_DifferentialPair = 81
eViewableObject_Violation = 82
eViewableObject_Board = 83
eViewableObject_BoardOutline = 84
eViewableObject_Group = 85
eViewableObject_Clipboard = 86
eViewableObject_SplitPlane = 87
eViewableObject_EmbeddedBoard = 88
eViewableObject_Region = 89
eViewableObject_ComponentBody = 90
eViewableObject_Rule_AssyTestPointStyle = 91
eViewableObject_Rule_AssyTestPointUsage = 92
eViewableObject_OwnerDraw = 93
eViewableObject_DrillTable = 94
eViewableObject_ViaStitching = 95
eViewableObject_LayerStackTable = 96
eViewableObject_Viewport = 97
eViewableObject_BoardRegion = 98
eViewableObject_Rule_SilkToBoardRegion = 99
eViewableObject_AccordionObject = 100
eViewableObject_OLEObject = 101
eViewableObject_Rule_SMDPADEntry = 102
eViewableObject_ViaShielding = 103
eViewableObject_Rule_UnpouredPolygon = 104
eViewableObject_MultilineText = 105
eViewableObject_Rule_BoardOutlineClearance = 106
eViewableObject_CoverlayPoly = 107
eViewableObject_PinPair = 108
eViewableObject_Rule_BackDrilling = 109
eViewableObject_StackedVia = 110
eViewableObject_StaggeredVia = 111
eViewableObject_Rule_Creepage = 112
eViewableObject_Rule_ReturnPath = 113
eViewableObject_Rectangle = 114

### TViewStyle (Vcl.ComCtrls)

vsIcon = 0
vsSmallIcon = 1
vsList = 2
vsReport = 3

### TVisibleGrid (Rt_Schematic)

eDotGrid = 0
eLineGrid = 1

### TWaitResult (System.Types)

wrSignaled = 0
wrTimeout = 1
wrAbandoned = 2
wrError = 3
wrIOCompletion = 4

### TWICImageFormat (Vcl.Graphics)

wifBmp = 0
wifPng = 1
wifJpeg = 2
wifGif = 3
wifTiff = 4
wifWMPhoto = 5
wifOther = 6

### TWindowState (System.UITypes)

wsNormal = 0
wsMinimized = 1
wsMaximized = 2

### TWinXPTabPosition (XPPageControl)

tpTop = 0
tpBottom = 1

### TWorkspaceObjectId (RT_Workspace)

eIdAbstractObject = 0
eIdConnective = 1
eIdConnectiveList = 2
eIdWorkspace = 3
eIdProjectBoardLevel = 4
eIdProjectFPGA = 5
eIdProjectCore = 6
eIdProjectEmbedded = 7
eIdProjectLibrary = 8
eIdProjectScript = 9
eIdProjectFreeDocuments = 10
eIdSourceDocument = 11
eIdDocumentGeneric = 12
eIdDocumentSCH = 13
eIdDocumentSCHLIB = 14
eIdDocumentPCBLIB = 15
eIdDocumentFlattened = 16
eIdDocumentEDIF = 17
eIdDocumentVHDL = 18
eIdDocumentVERILOG = 19
eIdDocumentProtelNetlist = 20
eIdDocumentPCADNetlist = 21
eIdDocumentPCB = 22
eIdDocumentCUPL = 23
eIdDocumentAdvSimModel = 24
eIdDocumentAdvSimSubCircuit = 25
eIdDocumentIntegratedLib = 26
eIdDocumentConstraints = 27
eIdDocumentVendorConstraints = 28
eIdDocumentPCadPcb = 29
eIdDocumentPCadLib = 30
eIdDocumentWave = 31
eIdDocumentLogicAnalyser = 32
eIdDocumentHWPartEditor = 33
eIdDocumentBOM = 34
eIdDocumentDraftsman = 35
eIdNet = 36
eIdBus = 37
eIdConstraint = 38
eIdConstraintGroup = 39
eIdPart = 40
eIdFullComponent = 41
eIdFullComponentInstance = 42
eIdImplementation = 43
eIdParameter = 44
eIdSheetSymbol = 45
eIdTextFrame = 46
eIdComponentClass = 47
eIdNetClass = 48
eIdDifferentialPair = 49
eIdChannelClass = 50
eIdRule = 51
eIdRoom = 52
eIdPin = 53
eIdSheetEntry = 54
eIdNetLabel = 55
eIdPowerObject = 56
eIdCrossSheet = 57
eIdPort = 58
eIdDifference = 59
eIdDifferenceManager = 60
eIdModification = 61
eIdChangeManager = 62
eIdViolation = 63
eIdViolationManager = 64
eIdComponentMapManager = 65
eIdVariantManager = 66
eIdVHDLEntity = 67
eIdConfiguration = 68
eIdDirective = 69
eIdSpatialLine = 70
eIdSpatialAnalyser = 71
eIdSpatialCompileMask = 72
eIdReaderSCH = 73
eIdReaderSCHLIB = 74
eIdReaderPCBLIB = 75
eIdReaderEDIF = 76
eIdReaderCUPL = 77
eIdReaderScript = 78
eIdReaderVHDL = 79
eIdReaderVerific = 80
eIdReaderProtelNetlist = 81
eIdReaderPCADNetlist = 82
eIdReaderPCB = 83
eIdReaderAdvSimLib = 84
eIdReaderBOM = 85
eIdCamOutputDoc = 86
eIdCamView = 87
eIdCamJob = 88
eIdGeneratedPage = 89
eIdPrintView = 90
eIdPrinterJob = 91
eIdPrinter = 92
eIdSignalManager = 93
eIdSignal = 94
eIdSignalNode = 95
eIdSignalLink = 96
eIdSubNet = 97
eIdEntityPort = 98
eIdInstancePort = 99
eIdInstance = 100
eIdExternalObject = 101
eIdHashedSCHObject = 102
eIdHashedPCBObject = 103
eIdPCBInstance = 104
eIdConnector = 105
eIdConnection = 106
eIdConnectorMap = 107
eIdMemoryConfiguration = 108
eIdToolChainOptions = 109
eIdDocumentOpenBus = 110
eIdDocumentHarnessDefinitions = 111
eIdHarnessDefinition = 112
eIdPlugIn = 113
eIdDocumentSimData = 114
eIdDocumentC = 115
eIdDocumentH = 116
eIdHighLevelCodeSymbol = 117
eIdSpatialBlanket = 118
eIdClassCluster = 119
eIdDocumentAltiumLibrary = 120
eIdPCBConfiguration = 121
eIdFPGAConfiguration = 122
eIdEmbeddedConfiguration = 123
eIdPortTimingSource = 124
eIdDocumentFSM = 125
eIdFSMState = 126
eIdFSMTransition = 127
eIdHighLevelCodeRoutine = 128
eIdHighLevelCodeMemory = 129
eIdDocumentPVLIB = 130
eIdProjectSystemDesign = 131
eIdProjectHarness = 132
eIdDocumentMBA = 133
eIdDocumentSystemDesign = 134
eIdSLDiagramModule = 135
eIdSLDiagramBlock = 136
eIdSLDiagramConnector = 137
eIdSLDiagramHarness = 138
eIdMBAEmbeddedDocument = 139
eIdSLDiagramConnection = 140
eIdSLDiagramPhysicalConnection = 141
eIdDifferentialPairClass = 142
eIdDocumentPcbLayerStack = 143
eIdDocumentConstraintManager = 144
eIdHarnessConnector = 145
eIdHarnessEntry = 146
eIdDocumentVirtualBOM = 147
eIdReuseBlocks = 148
eIdReuseBlock = 149
eIdReuseComponent = 150
eIdNote = 151
eIdProjectHarnessDesign = 152
eIdDocumentHarnessWiringDiagram = 153
eIdDocumentHarnessLayoutDrawing = 154
eIdDocumentVariantManager = 155

### TWriteAccessState (RT_ClientServerInterface)

wasNotConnected = 0
wasHasAccess = 1
wasNoAccess = 2

### TXactAttribute (Data.Win.ADODB)

xaCommitRetaining = 0
xaAbortRetaining = 1

### TXDoubleRectConnection (XPExtCtrls)

drcLeft2Left = 0
drcLeft2Right = 1
drcRight2Left = 2
drcRight2Right = 3

### TXPAnimationKind (XPPanels)

xakNone = 0
xakFocusRects = 1
xakFading = 2
xakSliding = 3

### TXPButtonState (XPButton)

xbsNone = 0
xbsHot = 1
xbsPressed = 2
xbsMenuDropped = 3

### TXPButtonStyle (WinXPButtons)

xpbsOffice = 0
xpbsWindows = 1

### TXPDrawingMode (XPPanels)

xdmFull = 0
xdmBackground = 1

### TXPExtPanelKind (XPPanels)

epkBackground = 0
epkBitmap = 1
epkGradient = 2
epkSimple = 3
epkWavy = 4
epkGradientWithBitmap = 5
epkVerticalWavy = 6

### TXPGlyphLayout (XPLabels)

xglLeft = 0
xglRight = 1

### TXPGraphicStretching (XPPanels)

xgsNone = 0
xgsStandard = 1
xgsProportional = 2
xgsHorizontal = 3
xgsVertical = 4

### TXPLinkStyle (XPLabels)

xlsCustom = 0
xlsNavigate = 1
xlsNavigateInNewWindow = 2
xlsOpenExternally = 3

### TXPLookAndFeel (XPTypes)

xlfNative = 0
xlfCustom = 1

### TXPScrollElem (XPScrolls)

pseNone = 0
pseStartButton = 1
pseBeforeThumb = 2
pseThumb = 3
pseAfterThumb = 4
pseEndButton = 5

### TXPScrollStyle (XPLists)

pssNone = 0
pssHorizontal = 1
pssVertical = 2
pssBoth = 3
pssAuto = 4
pssAutoHorizontal = 5
pssAutoVertical = 6

### TXPSpeedKind (XPExtCtrls)

xskStandard = 0
xskFading = 1

### TXPSpeedStyle (XPExtCtrls)

xssButton = 0
xssDropDown = 1

### TXPTextOrientation (XPLabels)

xtoDefault = 0
xtoVertical = 1
xtoVerticalClockwise = 2

## 其他常量（4887）

不属于任何枚举类型的常量，按首字母分组。


### A

AdditionalObjectsSet = [53..56, 61]
AllLayers = [1..75]
AllObjects = [1..22]
AllPrimitives = [1..14, 17..18, 20..22]
atbCenter = 1
atbInside = 2
atbOutside = 0
axrComponentOnly = 0
axrIncludeDescendants = 1

### B

bhError = 2
bhInfo = 0
bhsLarge = 1
bhsNormal = 0
bhsSmall = 2
bhWarning = 1
Big = 0
BikiniCoverlayLayerTypeId = '{8DE65238-89ED-47C5-BBF8-0F6F02D1899C}'
BIN_FILE_VERSION = 2
Bit0 = 1
Bit1 = 2
Bit10 = 1024
Bit11 = 2048
Bit12 = 4096
Bit13 = 8192
Bit14 = 16384
Bit15 = 32768
Bit16 = 65536
Bit17 = 131072
Bit18 = 262144
Bit19 = 524288
Bit2 = 4
Bit20 = 1048576
Bit21 = 2097152
Bit22 = 4194304
Bit23 = 8388608
Bit24 = 16777216
Bit25 = 33554432
Bit26 = 67108864
Bit27 = 134217728
Bit28 = 268435456
Bit29 = 536870912
Bit3 = 8
Bit30 = 1073741824
Bit31 = 2147483648
Bit4 = 16
Bit5 = 32
Bit6 = 64
Bit7 = 128
Bit8 = 256
Bit9 = 512
BM_CLICK = 245
BM_GETCHECK = 240
BM_GETIMAGE = 246
BM_GETSTATE = 242
BM_SETCHECK = 241
BM_SETDONTCLICK = 248
BM_SETIMAGE = 247
BM_SETSTATE = 243
BM_SETSTYLE = 244
BN_CLICKED = 0
BN_DBLCLK = 5
BN_DISABLE = 4
BN_DOUBLECLICKED = 5
BN_HILITE = 2
BN_KILLFOCUS = 7
BN_PAINT = 1
BN_PUSHED = 2
BN_SETFOCUS = 6
BN_UNHILITE = 3
BN_UNPUSHED = 3
BOM_LSB_FIRST = '﻿'
BOM_MSB_FIRST = '￾'
BottomLayerPermitted_BitMask = 2
bsrAsIs = 0
bsrLower = 1
bsrUpper = 2

### C

c0_25MM = 98425
c0_40MM = 157480
c0_50MM = 196850
c0_75MM = 295275
c1000_0MM = 393700787
c100_0MM = 39370078
c10_0MM = 3937008
c15_0MM = 5905512
c180 = 180.0
c180divPI = 57.295780181884766
c1_00MM = 393701
c1_5MM = 590551
c1AngleMin = 0.016666666666666666
c1AngleSec = 0.0002777777777777778
c20_0MM = 7874016
c25_0MM = 9842520
c2_0MM = 787402
c2_5MM = 984252
c2PI = 6.2831854820251465
c30_0MM = 11811024
c35_0MM = 13779528
c360 = 360.0
c3_0MM = 1181102
c3_5MM = 1377953
c3PIdiv4 = 2.356194496154785
c40_0MM = 15748031
c45_0MM = 17716535
c4_0MM = 1574803
c4_5MM = 1771654
c50_0MM = 19685039
c55_0MM = 21653543
c5_0MM = 1968504
c5_5MM = 2165354
c60_0MM = 23622047
c65_0MM = 25590551
c6_0MM = 2362205
c6_5MM = 2559055
c70_0MM = 27559055
c75_0MM = 29527559
c7_0MM = 2755906
c7_5MM = 2952756
c80_0MM = 31496063
c85_0MM = 33464567
c8_0MM = 3149606
c8_5MM = 3346457
c90_0MM = 35433071
c95_0MM = 37401575
c9_0MM = 3543307
c9_5MM = 3740157
c_BroadCast = 0
c_BroadCastHandle = ''
c_FromSystem = 0
c_NoEventData = 0
C_SCH_BROKEN_BAR = '¦'
C_SCH_BROKEN_BAR_ORD = 166
C_SCH_CARRIAGE_RETURN_ORD = 13
C_SCH_EQUAL_ORD = 61
C_SCH_GREATER_ORD = 62
C_SCH_NEW_LINE_ORD = 10
C_SCH_NULL_ORD = 0
C_SCH_SPECIAL_DELIMITER_CHAR = ''
C_SCH_SPECIAL_DELIMITER_CHAR_ORD = 142
C_SCH_UTF8_PREFIX = '%UTF8%'
C_SCH_VERTICAL_BAR = '|'
C_SCH_VERTICAL_BAR_ORD = 124
C_SHADOW_FILENAME_PREFIX = '$H-ADO-W-$.'
c_UnshelvePolygons = 1
cACTELDesignerDATBkExt = '.~DAT'
cACTELDesignerDATExt = '.DAT'
cACTELDesignerDBExt = '.ADB'
cACTELDesignerDCExt = '.DC'
cACTELDesignerFDBExt = '.FDB'
cACTELDesignerSTPExt = '.stp'
cACTELDesignerTCLExt = '.TCL'
cACTELFlahProPROExt = '.PRO'
cACTELProgram_DatGen = 'datgen'
cACTELProgram_Designer = 'designer'
cACTELProgram_FlashPro = 'flashpro'
cACTELProgram_Libero = 'libero'
cACTELProgram_SmartDesign = 'smartdesign'
cACTELSmartDesignEFCExt = '.EFC'
cActiveBomRequired = 'ActiveBOM required'
cADTempFileNamePrefix = 'Qjz'
cAdvPCB = 'AdvPCB'
cAllPinPairsClassName = 'All xSignals'
cAllSupplierSearchFilters = [0..5]
cAlteraProgram_GenerateProgrammingFile = 'Quartus_cmd'
cAlteraProgram_GenerateSVF = 'Quartus_Cpf'
cAlteraProgram_QuartusAsm = 'Quartus_Asm'
cAlteraProgram_QuartusFit = 'Quartus_Fit'
cAlteraProgram_QuartusMap = 'Quartus_Map'
cAlteraProgram_QuartusSta = 'Quartus_Sta'
cAlteraProgram_QuartusTan = 'Quartus_Tan'
cAlteraProgram_RunScript = 'Quartus_sh'
cAlteraSoftwareVersion_3x = '3'
cAlteraSoftwareVersion_4x = '4.'
cAlteraSoftwareVersion_5x = '5.'
cAlteraSoftwareVersion_6x = '6.'
cAltium = 'Altium'
cAltiumBuildsKey = '\Software\Altium\Builds'
cAltiumDocumentationScene = 'DXP://Documentation'
cAltiumDocumentationURL = 'http://techdocs.altium.com'
cAltiumPortalNotification = 'altium.dxp.portal'
cAltiumProductFile = 'AltiumInstallation.Ini'
cAltiumSystemFolder = 'System\Installation'
cAlwaysVisibleLayers = [1, 3]
CANEXPRSIZE = 10
CANEXPRVERSION = 2
CANHDRSIZE = 8
cAnsiTitleBlock1 = 17500000
cAnsiTitleBlock10 = 3600000
cAnsiTitleBlock11 = 42000000
cAnsiTitleBlock12 = 17000000
cAnsiTitleBlock13 = 42000000
cAnsiTitleBlock14 = 38200000
cAnsiTitleBlock15 = 27100000
cAnsiTitleBlock16 = 3100000
cAnsiTitleBlock2 = 62500000
cAnsiTitleBlock3 = 42500000
cAnsiTitleBlock4 = 12500000
cAnsiTitleBlock5 = 6300000
cAnsiTitleBlock6 = 2500000
cAnsiTitleBlock7 = 38700000
cAnsiTitleBlock8 = 32500000
cAnsiTitleBlock9 = 27600000
cAnyCompilationStage = [0..1]
cAnyErrorKind = [0..126]
cAnyErrorLevel = [0..3]
cApplicationDeactivated = 12
cApplicationShutdownStarted = 7
cApplicationStartupComplete = 6
cApproxCharacterWidth = 800000
cArcHitTestExtraTolearance = 300000
cArcTolerance = 200000
CarriageReturn = #13
CaseInSensitive = False
cAttributeName_IsImported = 'IsImported'
cAutoRoamEvaluationFinished = 16
cAutoUnits = [0..1]
cAutoUnitThresholdImperial = 5000000
cAutoUnitThresholdMetric1 = 39370078
cAutoUnitThresholdMetric2 = 393700787
cAvailableUpdatesListRetrieved = 11
CB_ADDSTRING = 323
CB_DELETESTRING = 324
CB_DIR = 325
CB_FINDSTRING = 332
CB_FINDSTRINGEXACT = 344
CB_GETCOUNT = 326
CB_GETCURSEL = 327
CB_GETDROPPEDCONTROLRECT = 338
CB_GETDROPPEDSTATE = 343
CB_GETDROPPEDWIDTH = 351
CB_GETEDITSEL = 320
CB_GETEXTENDEDUI = 342
CB_GETHORIZONTALEXTENT = 349
CB_GETITEMDATA = 336
CB_GETITEMHEIGHT = 340
CB_GETLBTEXT = 328
CB_GETLBTEXTLEN = 329
CB_GETLOCALE = 346
CB_GETTOPINDEX = 347
CB_INITSTORAGE = 353
CB_INSERTSTRING = 330
CB_LIMITTEXT = 321
CB_MSGMAX = 357
CB_RESETCONTENT = 331
CB_SELECTSTRING = 333
CB_SETCURSEL = 334
CB_SETDROPPEDWIDTH = 352
CB_SETEDITSEL = 322
CB_SETEXTENDEDUI = 341
CB_SETHORIZONTALEXTENT = 350
CB_SETITEMDATA = 337
CB_SETITEMHEIGHT = 339
CB_SETLOCALE = 345
CB_SETTOPINDEX = 348
CB_SHOWDROPDOWN = 335
cBalloonStemHeight = 10
cBaseUnit = 100000
cBeginRefreshNavigationPanels = 190
CBkgndPanelBorderSize = 3
CBN_CLOSEUP = 8
CBN_DBLCLK = 2
CBN_DROPDOWN = 7
CBN_EDITCHANGE = 5
CBN_EDITUPDATE = 6
CBN_ERRSPACE = -1
CBN_KILLFOCUS = 4
CBN_SELCHANGE = 1
CBN_SELENDCANCEL = 10
CBN_SELENDOK = 9
CBN_SETFOCUS = 3
cBOM_Compare = 'BOM_ReportCompare'
cBOM_PartType = 'BOM_PartType'
cBooleanEditorAttributes = [3, 7, 18, 30..31, 35..39, 43..44, 50..52, 58, 89, 101..103, 113..115, 118, 126..127, 133, 150..151]
cBreakPointNotification = 'altium.dxp.breakpoint'
cBreakpoints_Data = [2..3]
cBreakpoints_Program = [0..1]
cBreakpoints_SpecificData = [1, 3]
cBtnStateChecked = 4
cBtnStateCheckedHot = 5
cBtnStateDisabled = 3
cBtnStateHot = 1
cBtnStateNormal = 0
cBtnStatePressed = 2
cBusEntryTolerance = 500000
cCachedLibraryEDIFFolder = 'CachedEDIF\'
cCachedUserEDIFFolder = 'CachedUserEDIF\'
cCacheLoaded = 5
cCamtasticPreferencesChanged = 6
cCanFastCrossSelect_Emit = 'CanFastCrossSelect_Emit'
cCaseSensitiveModificationKinds = [8..10, 66..67]
cCharacterApproximativeHeight = 1000000
cCharacterApproximativeWidth = 800000
cCharacterWidthTolerance = 400000
cClassicHeaderBorderColor = 15197410
cClassicHeaderColor = 16118512
cClassicHeaderTextColor = 4210752
cClassicSchDocumentIds = [5, 102, 117]
cClassNameParam = 'ClassName'
cClipboardClear = 29
cClipboardPaste = 25
cCollapseCompileMaskButtonOffset = 100000
cCollapseCompileMaskButtonSize = 800000
cCollapsedCompileMaskSize = 1000000
cCollapsedNoteSize = 1000000
cCollapsedRTFLinkSize = 1000000
cCollapseNoteButtonOffset = 100000
cCollapseNoteButtonSize = 400000
cCollapseRTFLinkButtonOffset = 100000
cCollapseRTFLinkButtonSize = 400000
cColorEditorAttributes = [2..4, 83, 91]
cComboBoxEditorAttributes = [1..2, 14..17, 21..23, 26..29, 48..49, 54, 59, 61..68, 70..72, 76, 78..80, 86..88, 90, 96..97, 100, 106, 108, 134..135, 142..143, 152, 154..156]
cCommand_CustomCommand = 'CustomCommand'
cCommandQueueNameAfterDXPServerConnected = 'AfterDXPServerConnected'
cCommandQueueNameAfterLoggedIn = 'AfterLoggedIn'
cCommentsNotification = 'altium.dxp.comments'
cCommonAngularTolerance = 0.001
cCompClassNameParam = 'CompClassName'
cCompDisplayDeMorgan = 1
cCompDisplayIeee = 2
cCompDisplayNormal = 0
cCompilationMaskedPopupString = 'Removed by Compilation Mask'
cCompileMaskRectOffset1 = 1000000
cCompileMaskRectOffset2 = 100000
cCompileMaskShowFullCollapse = 1.5e-05
cCompileMaskShowHalfCollapse = 1e-05
cComplexTextObjectSet = [1, 3, 6..7, 18, 31]
cComponentLinkDescriptionParameterName = 'ComponentLink%dDescription'
cComponentLinkURLParameterName = 'ComponentLink%dURL'
cComponentTypesPreferencesChanged = 35
cConfigurableComponentInstancePrefix = 'Configurable_'
cConfigurationName_Debug = 'Debug'
cConfigurationName_Release = 'Release'
cConfigurationPreferncesLoaded = 22
cConfiguratorName_AB_SYSTEM = 'AB_SYSTEM'
cConfiguratorName_Adder = 'GENERIC_ADDER'
cConfiguratorName_AndSimple = 'AND000S'
cConfiguratorName_ATMEL_TOUCH = 'ATMEL_TOUCH'
cConfiguratorName_Barrier = 'GENERIC_BARRIER'
cConfiguratorName_Buffer = 'GENERIC_BUFFER'
cConfiguratorName_Bus_JS = 'GENERIC_BUS_JS'
cConfiguratorName_BusJoiner = 'J000S_000B'
cConfiguratorName_BusSplitter = 'J000B_000S'
cConfiguratorName_ClockManager = 'GENERIC_CLOCKMANAGER'
cConfiguratorName_Comparator = 'GENERIC_COMPARATOR'
cConfiguratorName_Counter = 'GENERIC_COUNTER'
cConfiguratorName_CrossPointSwitch = 'CrossPointSwitch'
cConfiguratorName_CustomInstrument = 'CUSTOM_INSTRUMENT'
cConfiguratorName_CYPRESS_TOUCH = 'CYPRESS_TOUCH'
cConfiguratorName_DigitalIO = 'DIGITAL_IO'
cConfiguratorName_DigitalIO_Application = 'DIGITAL_IO_APPLICATION'
cConfiguratorName_Divider = 'GENERIC_DIVIDER'
cConfiguratorName_Encoder = 'GENERIC_ENCODER'
cConfiguratorName_Fifo = 'GENERIC_FIFO'
cConfiguratorName_FIRFilter = 'FIR_FILTER'
cConfiguratorName_FPGA_MCU32 = 'FPGA_MCU32'
cConfiguratorName_Gate = 'GENERIC_GATE'
cConfiguratorName_LED_CTRL = 'LED_CTRL'
cConfiguratorName_LogicAnalyser = 'LogicAnalyser'
cConfiguratorName_LogicPrims = 'LogicPrims'
cConfiguratorName_Memory = 'GENERIC_MEMORY'
cConfiguratorName_MemoryInstrument = 'MEMORY_INSTRUMENT'
cConfiguratorName_MICROCHIP2_TOUCH = 'MICROCHIP2_TOUCH'
cConfiguratorName_MICROCHIP_TOUCH = 'MICROCHIP_TOUCH'
cConfiguratorName_Multiplexer = 'GENERIC_MULTIPLEXER'
cConfiguratorName_Multiplier = 'GENERIC_MULTIPLIER'
cConfiguratorName_OpenBusConnector = 'OpenBusConnector'
cConfiguratorName_OpenBusDualConnector = 'OpenBusDualConnector'
cConfiguratorName_PC_INTERFACE = 'PC_INTERFACE'
cConfiguratorName_PWM = 'GENERIC_PWM'
cConfiguratorName_Register = 'GENERIC_REGISTER'
cConfiguratorName_SineWaveTable = 'SINE000W_000H'
cConfiguratorName_STMICROELECTRONICS_TOUCH = 'STMICROELECTRONICS_TOUCH'
cConfiguratorName_WB_ASP = 'WB_ASP'
cConfiguratorName_WB_BOOTLOADER = 'WB_BOOTLOADER'
cConfiguratorName_WB_CELLULAR = 'WB_CELLULAR'
cConfiguratorName_WB_DualMaster = 'WB_DUALMASTER'
cConfiguratorName_WB_Intercon = 'WB_INTERCON'
cConfiguratorName_WB_Interface = 'WB_INTERFACE'
cConfiguratorName_WB_LED_CTRL = 'WB_LED_CTRL'
cConfiguratorName_WB_MEM_CTRL = 'WB_MEM_CTRL'
cConfiguratorName_WB_MP3DEC = 'WB_MP3DEC'
cConfiguratorName_WB_MultiMaster = 'WB_MULTIMASTER'
cConfiguratorName_WB_MultiMasterOpenBus = 'WB_MULTIMASTER_OPENBUS'
cConfiguratorName_WB_OWM_MultiBus = 'WB_OWM_MultiBus'
cConfiguratorName_WB_PRTIO = 'WB_PRTIO'
cConfiguratorName_WB_SPI = 'WB_SPI'
cConfiguratorName_WB_SPI_LED_DRIVER = 'WB_SPI_LED_DRIVER'
cConfiguratorName_WB_USB = 'WB_USB'
cConfiguratorName_WB_VGA = 'WB_VGA'
cConnectionDrawingThreshold = 3
cConnectWithAltiumChanged = 10
cContextHelpDelimiter = '.'
cCoordFractionalPartSaveExtensionName = '_Frac'
cCoordFractionalPartSaveExtensionNameExt = '_Frac1'
cCoreGenParm_BusFormat = 'BusFormat'
cCoreGenParm_ByteIndex = 'ByteIndex'
cCoreGenParm_ByteWrites = 'ByteWrites'
cCoreGenParm_Clock_Count = 'Clock_Count'
cCoreGenParm_Clock_InputFrequency = 'Clock_InputFrequency'
cCoreGenParm_ClockA_Operation = 'ClockA_Operation'
cCoreGenParm_ClockB_Operation = 'ClockB_Operation'
cCoreGenParm_ClockC_Operation = 'ClockC_Operation'
cCoreGenParm_ClockD_Operation = 'ClockD_Operation'
cCoreGenParm_ClockEdgeIsRising = 'ClockEdgeIsRising'
cCoreGenParm_ComponentName = 'ComponentName'
cCoreGenParm_Depth = 'Depth'
cCoreGenParm_DepthA = 'DepthA'
cCoreGenParm_DepthB = 'DepthB'
cCoreGenParm_EnablePin = 'EnablePin'
cCoreGenParm_Family = 'DeviceFamily'
cCoreGenParm_FileName = 'Filename'
cCoreGenParm_HalfIndex = 'HalfIndex'
cCoreGenParm_HexFileEndianness = 'HexFileEndianness'
cCoreGenParm_HexFileName = 'HexFileName'
cCoreGenParm_HexWidth = 'HexWidth'
cCoreGenParm_InferRam = 'InferRam'
cCoreGenParm_ModuleType = 'ModuleType'
cCoreGenParm_PreloadDonePin = 'PreloadDonePin'
cCoreGenParm_ResetPin = 'ResetPin'
cCoreGenParm_Vendor = 'Vendor'
cCoreGenParm_Width = 'Width'
cCoreGenParm_WidthA = 'WidthA'
cCoreGenParm_WidthB = 'WidthB'
cCreateBitStageName = 'create_bit'
cCreateDesignStageName = 'create_design'
cCreateSTAPLStageName = 'create_stapl'
cCreateTimmingRPTStageName = 'create_timing'
cCrossJunctionTolerance = 500000
cCrossOverTolerance = 300000
cCrosspointSwitchDeviceName = 'CROSSPOINT_SWITCH'
cCurrentSchMinorVersion = 7
cCurrentVariantName = ''
cCustomDynamicHelpUpdated = 11
cCustomShapeApproximation = 1000
cDatabase_KeyFieldDelimiter = '[[/\]]'
cDataHighLevelCodeEntryTypes = [0, 2]
cDefaultBarOptions = [0, 4]
cDefaultBoardRegionColor = 6343822
cDefaultConfigurationName = 'Default - All Constraints'
cDefaultConfigurationNameEmbedded = 'Default'
cDefaultDelay = 10
cDefaultDiffPair = 'DefaultDiffPair'
cDefaultDiffPairName = 'DIFFPAIR'
cDefaultDigitsPanelOptions = [1..2]
cDefaultDimBlendLevel = 80
cDefaultElectricalGridSizeMils_1 = 40000
cDefaultElectricalGridSizeMils_2 = 200000
cDefaultElectricalGridSizeMils_3 = 400000
cDefaultElectricalGridSizeMMs_1 = 157480
cDefaultElectricalGridSizeMMs_2 = 393701
cDefaultElectricalGridSizeMMs_3 = 787402
cDefaultEndAngle = 330
cDefaultFileOwnership_Enabled = False
cDefaultFileOwnership_EnabledOutputDirectory = False
cDefaultFileOwnership_WarningLevelOpen = 2
cDefaultFileOwnership_WarningLevelSave = 2
cDefaultGaugeNeedleOptions = []
cDefaultGaugeOptions = [0]
cDefaultGraphGridSize = 12
cDefaultGraphInterval = 500
cDefaultGraphShift = 2
cDefaultGridSizeMils_Coarse1 = 500000
cDefaultGridSizeMils_Coarse2 = 1000000
cDefaultGridSizeMils_Coarse3 = 2000000
cDefaultGridSizeMils_Fine1 = 100000
cDefaultGridSizeMils_Fine2 = 200000
cDefaultGridSizeMils_Fine3 = 500000
cDefaultGridSizeMMs_Coarse1 = 984252
cDefaultGridSizeMMs_Coarse2 = 1968504
cDefaultGridSizeMMs_Coarse3 = 3937008
cDefaultGridSizeMMs_Fine1 = 196850
cDefaultGridSizeMMs_Fine2 = 393701
cDefaultGridSizeMMs_Fine3 = 787402
cDefaultHarnessXSize = 1600000
cDefaultHarnessYSize = 2000000
cDefaultInstrBkgndOptions = [0..2]
cDefaultMBADocument = '[MBA Document]'
cDefaultPenWidth = 100000
cDefaultPollingInterval = 250
cDefaultReleasesTemporaryFolder = ''
cDefaultRetryCount = 10
cDefaultSheetNumberSpaceSize = 12
cDefaultSnapGridSize = 1000000
cDefaultSnapGridSizeMils_1 = 100000
cDefaultSnapGridSizeMils_2 = 500000
cDefaultSnapGridSizeMils_3 = 1000000
cDefaultSnapGridSizeMMs_1 = 393701
cDefaultSnapGridSizeMMs_2 = 984252
cDefaultSnapGridSizeMMs_3 = 1968504
cDefaultStartAngle = 30
cDefaultTerminalOptions = [0]
cDefaultTerminalRxColor = 0
cDefaultTerminalTxColor = 32768
cDefaultThickenDelay = 60
CDefaultTwoDigitYearCenturyWindow = 50
cDefaultVariantName = '[No Variations]'
cDefaultVariantUniqueID = ''
cDefaultVisibleGridSizeMils = 1000000
cDefaultVisibleGridSizeMMs = 393701
CDefMargin = 8
CDefOpenOptions = [2, 8..9, 19]
cDefThumbnailSizeX = 96
cDefThumbnailSizeY = 72
cDeleteBegin = 22
cDeleteStop = 23
cDelimiter_Variant = '@'
cDesignInsight_DefaultConnectivityInsightHoverDelay = 1000
cDesignInsight_DefaultConnectivityInsightHoverTree = False
cDesignInsight_DefaultEnableDocumentInsight = False
cDesignInsight_DefaultEnableProjectInsight = False
cDeveloperToolBoardKinds = [13]
cDeviceFamily_AMCC_PPC405 = 'PPC405'
cDeviceFamily_Arria2GX = 'Arria2GX'
cDeviceFamily_Arria2GZ = 'Arria2GZ'
cDeviceFamily_ArriaGX = 'ArriaGX'
cDeviceFamily_Artix7 = 'Artix7'
cDeviceFamily_BlueStreak = 'BLUESTREAK'
cDeviceFamily_CoolRunner2 = 'CoolRunner2'
cDeviceFamily_CoolRunnerXPLA3 = 'CoolRunnerXPLA3'
cDeviceFamily_Cyclone = 'Cyclone'
cDeviceFamily_Cyclone2 = 'Cyclone2'
cDeviceFamily_Cyclone3 = 'Cyclone3'
cDeviceFamily_Cyclone4E = 'Cyclone4E'
cDeviceFamily_Cyclone4GX = 'Cyclone4GX'
cDeviceFamily_EC = 'EC'
cDeviceFamily_ECP = 'ECP'
cDeviceFamily_ECP2 = 'ECP2'
cDeviceFamily_ECP2M = 'ECP2M'
cDeviceFamily_Fusion = 'Fusion'
cDeviceFamily_IGLOO = 'IGLOO'
cDeviceFamily_IGLOOE = 'IGLOOE'
cDeviceFamily_IGLOOnano = 'IGLOOnano'
cDeviceFamily_IGLOOPLUS = 'IGLOOPLUS'
cDeviceFamily_ispMACH4000B = 'ispMACH4000B'
cDeviceFamily_ispMACH4000C = 'ispMACH4000C'
cDeviceFamily_ispMACH4000V = 'ispMACH4000V'
cDeviceFamily_ispMACH4000Z = 'ispMACH4000Z'
cDeviceFamily_ispXPLD5000MX = 'ispXPLD5000MX'
cDeviceFamily_MachXO = 'MachXO'
cDeviceFamily_MachXO2 = 'MachXO2'
cDeviceFamily_Max2 = 'MAX2'
cDeviceFamily_Max3000A = 'MAX3000A'
cDeviceFamily_Max5 = 'MAX5'
cDeviceFamily_Max7000AE = 'MAX7000AE'
cDeviceFamily_Max7000B = 'MAX7000B'
cDeviceFamily_Max7000S = 'MAX7000S'
cDeviceFamily_ProAsic3 = 'ProASIC3'
cDeviceFamily_ProAsic3E = 'ProASIC3E'
cDeviceFamily_ProAsicPlus = 'ProASICPlus'
cDeviceFamily_SC = 'SC'
cDeviceFamily_SCM = 'SCM'
cDeviceFamily_SmartFusion = 'SmartFusion'
cDeviceFamily_Spartan2 = 'Spartan2'
cDeviceFamily_Spartan2E = 'Spartan2E'
cDeviceFamily_Spartan3 = 'Spartan3'
cDeviceFamily_Spartan3A = 'Spartan3A'
cDeviceFamily_Spartan3ADSP = 'Spartan3ADSP'
cDeviceFamily_Spartan3AN = 'Spartan3AN'
cDeviceFamily_Spartan3E = 'Spartan3E'
cDeviceFamily_Spartan3L = 'Spartan3L'
cDeviceFamily_Spartan6 = 'Spartan6'
cDeviceFamily_Stellaris = 'Stellaris'
cDeviceFamily_STM32 = 'STM32'
cDeviceFamily_Stratix = 'Stratix'
cDeviceFamily_Stratix2 = 'Stratix2'
cDeviceFamily_Stratix2GX = 'Stratix2GX'
cDeviceFamily_Stratix3 = 'Stratix3'
cDeviceFamily_Stratix4 = 'Stratix4'
cDeviceFamily_StratixGX = 'StratixGX'
cDeviceFamily_Virtex = 'Virtex'
cDeviceFamily_Virtex2 = 'Virtex2'
cDeviceFamily_Virtex2P = 'Virtex2P'
cDeviceFamily_Virtex4 = 'Virtex4'
cDeviceFamily_Virtex5 = 'Virtex5'
cDeviceFamily_Virtex6 = 'Virtex6'
cDeviceFamily_VirtexE = 'VirtexE'
cDeviceFamily_XA9500XL = 'XA9500XL'
cDeviceFamily_XACoolRunner2 = 'XACoolRunner2'
cDeviceFamily_XASpartan3A = 'XASpartan3A'
cDeviceFamily_XASpartan3ADSP = 'XASpartan3ADSP'
cDeviceFamily_XASpartan3E = 'XASpartan3E'
cDeviceFamily_XC17V00 = 'XC17V00'
cDeviceFamily_XC18V00 = 'XC18V00'
cDeviceFamily_XC9500 = 'XC9500'
cDeviceFamily_XC9500XL = 'XC9500XL'
cDeviceFamily_XC9500XV = 'XC9500XV'
cDeviceFamily_XCF = 'XCF'
cDeviceFamily_XP = 'XP'
cDeviceFamily_XP2 = 'XP2'
cDiagramSystem_Block = 'Block'
cDiagramSystem_Connector = 'Connector'
cDialogSuffix = '...'
cDifferentialIOStandardTypes = [6..11, 29..46, 48, 50..53, 56..59, 62..63, 68..76, 88..89, 93..100, 121..122, 124..128, 134..145]
cDifferentialPairHeight = 1000000
cDifferentialPairShadowSize = 100000
cDifferentialPairWidth = 2150000
cDiffPairNegNetNaming = '_N'
cDiffPairParam = 'DifferentialPair'
cDiffPairPosNetNaming = '_P'
cDigiKeyPartNumberParameterName = 'DigiKeyPartNumber'
cDir_ANY = [0..7]
cDir_Diagonal = [1, 3, 5, 7]
cDir_HorVert = [0, 2, 4, 6]
cDir_NONE = []
cDisplayErrorOffset = 100000
cDocExtension_Pcb = 'PcbDoc'
cDocExtension_Sch = 'SchDoc'
cDocKind_3DModelDoc = 'Altium3DModelDocument'
cDocKind_AGUIDesign = 'AGUIDesign'
cDocKind_Allegro_DRA = 'Allegro_DRA'
cDocKind_Allegro_LIB = 'Allegro_PcbLib'
cDocKind_Allegro_PCB = 'Allegro_PCB'
cDocKind_AltiumLib = 'AltiumLib'
cDocKind_Annotation = 'Annotation'
cDocKind_Asm = 'ASM'
cDocKind_BOM = 'BOM'
cDocKind_C = 'C'
cDocKind_CADSTAR_File = 'CADSTAR_File'
cDocKind_Camtastic = 'CAMTASTIC'
cDocKind_CIRCUITMAKER2000_CKT = 'CM2000_CKT'
cDocKind_CIRCUITMAKER2000_DEVLIB = 'CM2000_DEVLIB'
cDocKind_CIRCUITMAKER2000_LIB = 'CM2000_LIB'
cDocKind_Ckt = 'CKT'
cDocKind_CMPCB = 'CMPCB'
cDocKind_CmpLib = 'CmpLib'
cDocKind_CmpTemplate = 'CMPT'
cDocKind_ComponentSync = 'CmpSync'
cDocKind_Constraint = 'CONSTRAINT'
cDocKind_ConstraintManager = 'CmPcbDoc'
cDocKind_Constraints = 'CONSTRAINTS'
cDocKind_ControlPanel = 'ControlPanel'
cDocKind_CoreProject = 'COREPROJECT'
cDocKind_Cpp = 'CPP'
cDocKind_CSPCB = 'CSPCB'
cDocKind_CSPcbProject = 'CSPCBPROJECT'
cDocKind_CSSch = 'CSSch'
cDocKind_CSV = 'CSV'
cDocKind_Cupl = 'CUPL'
cDocKind_DatabaseLib = 'DATABASELIB'
cDocKind_DatabaseLink = 'DATABASELINK'
cDocKind_DataClass = 'DataClass'
cDocKind_Datasheet = 'DATASHEET'
cDocKind_DDB = 'DDB'
cDocKind_DefaultPcb = 'DefaultPcb'
cDocKind_DefaultPcbLib = 'DefaultPcbLib'
cDocKind_DeviceClass = 'DeviceClass'
cDocKind_Disassembly = 'DISASSEMBLY'
cDocKind_DraftsmanDocumentTemplate = 'DraftsmanDocumentTemplate'
cDocKind_DraftsmanSheetTemplate = 'DraftsmanSheetTemplate'
cDocKind_DraftsmanTemplate = 'PcbDrawing'
cDocKind_DxDesigner_SCH = 'DxDesigner_SCH'
cDocKind_DxDesigner_SCHLib = 'DxDesigner_SCHLIB'
cDocKind_EAGLE_File = 'EAGLE_File'
cDocKind_Edif = 'EDIF'
cDocKind_EditableControlPanel = 'EditableControlPanel'
cDocKind_EditScript = 'EDITSCRIPT'
cDocKind_EditScriptBasUnit = 'EDITSCRIPTBAS'
cDocKind_EditScriptDS = 'EDITSCRIPTDS'
cDocKind_EditScriptDSDataModule = 'EDITSCRIPTDSDATAMODULE'
cDocKind_EditScriptDSForm = 'EDITSCRIPTDSFORM'
cDocKind_EditScriptDSUnit = 'EDITSCRIPTDSUNIT'
cDocKind_EditScriptInclude = 'EDITSCRIPTINCLUDE'
cDocKind_EditScriptInstrument = 'EDITSCRIPTINSTRUMENT'
cDocKind_EditScriptJS = 'EDITSCRIPTJS'
cDocKind_EditScriptJSDataModule = 'EDITSCRIPTJSDATAMODULE'
cDocKind_EditScriptJSForm = 'EDITSCRIPTJSFORM'
cDocKind_EditScriptJSUnit = 'EDITSCRIPTJSUNIT'
cDocKind_EditScriptTclUnit = 'EDITSCRIPTTCL'
cDocKind_EditScriptVBS = 'EDITSCRIPTVBS'
cDocKind_EditScriptVBSDataModule = 'EDITSCRIPTVBSDATAMODULE'
cDocKind_EditScriptVBSForm = 'EDITSCRIPTVBSFORM'
cDocKind_EditScriptVBSUnit = 'EDITSCRIPTVBSUNIT'
cDocKind_EmbeddedProject = 'EMBEDDEDPROJECT'
cDocKind_EmbeddedStack = 'EmbeddedStack'
cDocKind_Engagement = 'Engagement'
cDocKind_EPM_Test = 'EPM_Test'
cDocKind_Expedition_File = 'Expedition_File'
cDocKind_FavLink = 'FAVLINK'
cDocKind_Fpgaflow = 'FPGAFLOW'
cDocKind_FpgaProject = 'FPGAPROJECT'
cDocKind_FpgaWorkspace = 'FPGAWORKSPACE'
cDocKind_FreeBinaryDoc = 'AltiumBinaryFileDocument'
cDocKind_FreeDocsProject = 'FREEDOCSPROJECT'
cDocKind_FSM = 'FSM'
cDocKind_H = 'H'
cDocKind_HarnessDefinition = 'HARNESS'
cDocKind_HarnessDesign = 'HarnessDesign'
cDocKind_HarnessDrawing = 'HarnessDrawing'
cDocKind_HarnessLayoutDrawing = 'HarnessLayoutDrawing'
cDocKind_HarnessProject = 'HarnessProject'
cDocKind_HarnessWiringDiagram = 'HarnessWiringDiagram'
cDocKind_Html = 'HTML'
cDocKind_HtmlHelp = 'HTMLHELP'
cDocKind_HWPart = 'HWPart'
cDocKind_ImpoterFile = 'ImporterFile'
cDocKind_IntegratedLibrary = 'INTEGRATEDLIBRARY'
cDocKind_IntLibrary = 'INTLIBRARY'
cDocKind_KICAD_File = 'KICAD_File'
cDocKind_LayerStack = 'LsmDoc'
cDocKind_LayerStackup = 'LsmDoc'
cDocKind_LayerStackupDoc = 'AltiumLayerStackup'
cDocKind_LayerStackX = 'LsmDocX'
cDocKind_LibraryMigrator = 'LibraryMigrator'
cDocKind_LogicAnalyser = 'LogicAnalyser'
cDocKind_LogicAnalyserAnalog = 'LogicAnalyserAnalog'
cDocKind_ManagedProject = 'MANAGEDPROJECT'
cDocKind_MBA = 'MultiBoardAssembly'
cDocKind_MBS = 'MultiBoardSchematic'
cDocKind_MDB = 'MDB'
cDocKind_Mdl = 'MDL'
cDocKind_Mentor_DX_File = 'Mentor_DX_File'
cDocKind_MorfikApplication = 'MorfikApplication'
cDocKind_MorfikAppSet = 'MorfikAppSet'
cDocKind_MorfikDebugScripts = 'MorfikDebugScripts'
cDocKind_MorfikDebugSource = 'MorfikDebugSource'
cDocKind_MorfikForm = 'MorfikForm'
cDocKind_MorfikModule = 'MorfikModule'
cDocKind_MorfikPackage = 'MorfikPackage'
cDocKind_MorfikPage = 'MorfikPage'
cDocKind_MorfikProject = 'MorfikProject'
cDocKind_MorfikProjectSource = 'MorfikProjectSource'
cDocKind_MorfikQuery = 'MorfikQuery'
cDocKind_MorfikRelationships = 'MorfikRelationships'
cDocKind_MorfikReport = 'MorfikReport'
cDocKind_MorfikTable = 'MorfikTable'
cDocKind_MorfikWebMethod = 'MorfikWebMethod'
cDocKind_MorfikWidget = 'MorfikWidget'
cDocKind_Multiboard_AssemblyDoc = 'Multiboard_AssemblyDoc'
cDocKind_Multiboard_SchematicDoc = 'Multiboard_SchematicDoc'
cDocKind_NGC = 'NGC'
cDocKind_Nsx = 'NSX'
cDocKind_OLD_PCAD_LIB = 'OLD_PCAD_LIB'
cDocKind_OpenBus = 'OPENBUS'
cDocKind_OpenBusComp = 'OPENBUSCOMP'
cDocKind_ORCAD7_CIS = 'ORCAD7_CIS'
cDocKind_ORCAD7_DSN = 'ORCAD7_DSN'
cDocKind_ORCAD7_LLB = 'ORCAD7_LLB'
cDocKind_ORCAD7_MAX = 'ORCAD7_MAX'
cDocKind_ORCAD7_OLB = 'ORCAD7_OLB'
cDocKind_OutputJob = 'OUTPUTJOB'
cDocKind_PADS_CAELib = 'PADS_CAELib'
cDocKind_PADS_Logic = 'PADS_Logic'
cDocKind_PADS_PartLib = 'PADS_PartLib'
cDocKind_PADS_PCB = 'PADS_PCB'
cDocKind_PADS_PCBLib = 'PADS_PCBLib'
cDocKind_PartChoiceList = 'PartChoiceList'
cDocKind_PartSync = 'PrtSync'
cDocKind_PCAD16_BIN_PCB = 'PCAD16_BIN_PCB'
cDocKind_PCAD16_BIN_SCH = 'PCAD16_BIN_SCH'
cDocKind_PCAD16_LIA = 'PCAD16_LIA'
cDocKind_PCAD16_NETLIST = 'PCAD16_NETLIST'
cDocKind_PCAD16_PCB = 'PCAD16_PCB'
cDocKind_PCAD16_SCH = 'PCAD16_SCH'
cDocKind_PCADLIB = 'PCADLIB'
cDocKind_PCADPCB = 'PCADPCB'
cDocKind_Pcb = 'PCB'
cDocKind_Pcb3DLib = 'PCB3DLIB'
cDocKind_Pcb3DR = 'Pcb3DR'
cDocKind_PcbDrawing = 'PcbDrawing'
cDocKind_PcbLayerStack = 'LsmPcbDoc'
cDocKind_PcbLib = 'PCBLIB'
cDocKind_PcbProject = 'PCBPROJECT'
cDocKind_PcbProjectStructure = 'PCBPROJECTSTRUCTURE'
cDocKind_PcbProjectVariants = 'PCBPROJECTVARIANTS'
cDocKind_PCBReleaseView = 'PCBReleaseView'
cDocKind_PcbSnippet = 'PCBSnippet'
cDocKind_PDF = 'PDF'
cDocKind_PDNA = 'PDNA3'
cDocKind_PickATask = 'PICKATASK'
cDocKind_PinInfo = 'PinInfo'
cDocKind_Preferences = 'Preferences'
cDocKind_Profiler = 'PROFILER'
cDocKind_Project = 'Project'
cDocKind_ProjectGroup = 'PROJECTGROUP'
cDocKind_ProjectHistory = 'ProjectHistory'
cDocKind_ProjectRelease = 'ProjectReleaseDocument'
cDocKind_ProjectReleaseView = 'ProjectReleaseView'
cDocKind_ProtelNetlist = 'PROTELNETLIST'
cDocKind_PvLib = 'PVLIB'
cDocKind_ReleasedItem = 'RELEASEDITEM'
cDocKind_Releases = 'Releases'
cDocKind_ReuseBlock = 'ReuseBlock'
cDocKind_RevisionScheme = 'RevisionScheme'
cDocKind_RTF = 'RTF'
cDocKind_Sch = 'SCH'
cDocKind_Schlib = 'SCHLIB'
cDocKind_SchSnippet = 'SCHSnippet'
cDocKind_SchTemplate = 'SCHDOT'
cDocKind_ScriptProject = 'SCRIPTPROJECT'
cDocKind_SD = 'SdDoc'
cDocKind_SeaOfDocuments = 'SeaOfDocuments'
cDocKind_SimCfg = 'SimCfg'
cDocKind_Simdata = 'SIMDATA'
cDocKind_SimModel = 'SimModel'
cDocKind_SiModel = 'SiModel'
cDocKind_SIPinModelLibrary = 'SIPINMODELLIBRARY'
cDocKind_Situs = 'SITUS'
cDocKind_SpecctraDSN = 'Specctra_DSN'
cDocKind_SVNDatabaseLib = 'SVNDATABASELIB'
cDocKind_SystemDesign = 'SystemDesign'
cDocKind_Unknown = 'UNKNOWN'
cDocKind_VariantManager = 'VariantManager'
cDocKind_VendorConstraint = 'VENDORCONSTRAINT'
cDocKind_Verilog = 'VERILOG'
cDocKind_VerLib = 'VERLIB'
cDocKind_VerTst = 'VERTST'
cDocKind_Vhdl = 'VHDL'
cDocKind_VhdLib = 'VHDLIB'
cDocKind_VhdlSim = 'VHDLSIM'
cDocKind_VhdTst = 'VHDTST'
cDocKind_VirtualBOM = 'VirtualBOM'
cDocKind_VQM = 'VQM'
cDocKind_Wave = 'WAVE'
cDocKind_WaveSim = 'WAVESIM'
cDocKind_WEBAPP = 'WebApp'
cDocKind_Workspace = 'ProjectGroup'
cDocKind_Xml = 'XML'
cDocSubKind_CAM = 'CAM_CAMTASTIC'
cDocSubKind_CAMTEXT = 'CAM_TEXT'
cDocSubKind_ODBTEXT = 'ODB_TEXT'
cDocSubKind_Undefined = 'UNDEF_DOCSUBKIND'
cDocumentActivating = 3
cDocumentAddedToProject = 40
cDocumentBeforeClose = 8
cDocumentBeforeRelease = 41
cDocumentBeforeRemovedFromProject = 42
cDocumentBeforeSave = 29
cDocumentCanClose = 1
cDocumentCanCompile = 0
cDocumentChangedOutsideEditor = 301
cDocumentClosed = 19
cDocumentClosing = 2
cDocumentCompiled = 6
cDocumentCompiling = 7
cDocumentCreated = 36
cDocumentDataDeleted = 1
cDocumentDataInserted = 0
cDocumentDataModified = 2
cDocumentDataRefresh = 3
cDocumentDisplayNameChanging = 37
cDocumentECO_Begin = 700
cDocumentECO_End = 701
cDocumentExistingAddedToProject = 44
cDocumentFormActivated = 0
cDocumentFormCreated = 2
cDocumentFormDeActivated = 1
cDocumentFormDestroyed = 3
cDocumentFormNotification = 'altium.dxp.documentform'
cDocumentFormShown = 4
cDocumentGenerated = 23
cDocumentHDLWaveSignalDeleting = 500
cDocumentHidden = 12
cDocumentImport = 30
cDocumentLoading = 0
cDocumentModifiedChanged = 11
cDocumentNameChanging = 4
cDocumentNameChangingBeforeLoad = 52
cDocumentNotification = 'altium.dxp.document'
cDocumentOpening = 1
cDocumentOwnershipChanged = 300
cDocumentPreviewUpdated = 25
cDocumentProjectActivating = 15
cDocumentProjectChanged = 9
cDocumentProjectPreviewGenerationFinished = 27
cDocumentProjectPreviewGenerationStarted = 26
cDocumentPropertiesChanged = 600
cDocumentReleased = 43
cDocumentRemoved = 24
cDocumentRequest = 'altium.dxp.documentrequest'
cDocumentRouterStarted = 200
cDocumentRouterStopped = 201
cDocumentSaved = 10
cDocumentsBatchOpen_Begin = 900
cDocumentsBatchOpen_End = 901
cDocumentsCommited = 1
cDocumentScrapCompiled = 17
cDocumentScrapCompiling = 16
cDocumentShowMessage = 35
cDocumentSilentReloaded = 800
cDocumentSwPlatformChanged = 401
cDocumentSwPlatformCompiled = 403
cDocumentSwPlatformOpened = 400
cDocumentSwPlatformOptionChanged = 402
cDocumentSystemParameters = [0..25, 30..31]
cDocumentType_PCB = 'PCB'
cDocumentType_Schematic = 'Schematic'
cDocumentValidationFinished = 46
cDocumentValidationStarted = 45
cDocumentWorkspaceLoad_Begin = 101
cDocumentWorkspaceLoad_End = 102
cDocumentWorkspaceSave_Begin = 103
cDocumentWorkspaceSave_End = 104
cDotChar = '.'
cDotEDFExt = '.EDF'
cDotEDFLIBExt = '.EDFLIB'
cDotEDNExt = '.EDN'
cDotNGCExt = '.NGC'
cDotQIPExt = '.QIP'
cDotVERTSTExt = '.VERTST'
cDotVExt = '.V'
cDotVHDExt = '.VHD'
cDotVHDLExt = '.VHDL'
cDotVHDTSTExt = '.VHDTST'
cDotVQMExt = '.VQM'
cDotWidth = 600000
cDragDropFinished = 1
cDragDropNotification = 'altium.dxp.dragdrop'
cDraggingMacroChooseLocation = 'ChooseLocation'
cDraggingMacroDragKey = 'DRAG'
cDraggingMacroMultipleObjects = 'MultipleObjects'
cDraggingMacroParamAction = 'ActionName'
cDraggingMacroParamX = 'X'
cDraggingMacroParamY = 'Y'
cDraggingMacroSelectedObjects = 'SelectedObjects'
cDraggingMacroSingleObjects = 'SingleObjects'
cdsChecked = 3
cdsDefault = 5
cdsDisabled = 2
cdsDropHilited = 12
cDSFFolder = 'dsf'
cdsFocused = 4
cdsGrayed = 1
cdsHot = 6
cdsIndeterminate = 8
cdsMarked = 7
cdsNearHot = 10
cdsOtherSideHot = 11
cdsSelected = 0
cdsShowKeyboardCues = 9
cDualPortModules = [3..5]
cDXPDocument = 'DXPDoc'
cDXPHomePage = 'DXP://Home'
cDXPHomeTarget = 'Home'
cDXPProcess = 'DXPProcess'
cDXPProjectDocumentsScene = 'DXP://Workspace'
cDXPProtocol = 'DXP'
cDXPProtocolPrefix = 'DXP://'
cDXPServerAfterPreferencesChanged = 32
cDXPServerAfterVCSRepoListChanged = 33
cDXPServerConnected = 24
cDXPServerDisconnected = 25
cDXPServerPreferencesChanged = 31
cDXPServerUserLoggedIn = 30
cDXPServerUserOnlineStateChanged = 27
cEDFExt = 'EDF'
cEDFLIBExt = 'EDFLIB'
cEdgeRadius = 4
cEDIExt = 'EDI'
cEDIFUpdaterDllName = 'EDIFUpdater.DLL'
cEditableChildren = [1, 3, 6..7, 13, 16, 30..31, 64]
cEditLocationAborted = 16
cEditLocationBegin = 14
cEditLocationStop = 17
cEditLocationSuccess = 15
cEditObjectList = 27
cEditParam = '_Edit_'
cEditPropertyAborted = 12
cEditPropertyBegin = 10
cEditPropertyStop = 13
cEditPropertySuccess = 11
cEditTextInPlaceAborted = 20
cEditTextInPlaceBegin = 18
cEditTextInPlaceStop = 21
cEditTextInPlaceSuccess = 19
cEDM_Notification = 'altium.dxp.edm'
cEDM_Notification_ActivateWorkspaceWaitError = 13
cEDM_Notification_DocumentUsersChanged = 11
cEDM_Notification_FolderParametersUpdated = 8
cEDM_Notification_ItemsDeleted = 10
cEDM_Notification_PCBReleaseBeforeCommitRelease = 1
cEDM_Notification_PCBReleaseBeforeGeneratorsRun = 0
cEDM_Notification_PCBReleaseInitiatePublish = 4
cEDM_Notification_PCBReleaseReviewPackage = 2
cEDM_Notification_PCBReleaseReviewValidate = 3
cEDM_Notification_RefreshVaultExplorerView = 3
cEDM_Notification_ReleaseCommitted = 2
cEDM_Notification_ReleaseCommittedBatch = 5
cEDM_Notification_ReleasedCloneItem = 4
cEDM_Notification_RevisionsStateChanged = 12
cEDM_Notification_TakeOverManagedProjectCreation = 6
cEDM_Notification_TakeOverProjectReleaser = 7
cEDM_Notification_VaultsChanged = 1
cEDM_Notification_WorkspacesLoaded = 9
cEDMS_CommentsNotification_AddComment = 3
cEDMS_CommentsNotification_SelectComment = 1
cEDMS_CommentsNotification_SelectObject = 2
cEDMS_CommentsNotification_ThreadsChanged = 5
cEDMS_CommentsNotification_ThreadUpdated = 7
cEDMS_CommentsNotification_Update = 6
cEDMS_CommentsNotification_UpdateCommentData = 4
cEDMS_DXPServer_DataSavedToStorage = 1
cEDMS_DXPServer_NotificationServiceConnected = 2
cEDMS_DXPServer_NotificationServiceDisconnected = 3
cEDMSChannelReconnected = 34
cEDMSPreferencesChanged = 26
cEDNExt = 'EDN'
cElectricalLayerNumber_Min = 1
cElectricalLayerNumber_Undefined = -1
cEllipticalArcTolerance = 200000
cEmbeddedPreferencesChanged = 12
cEmptyProbeName = 'Empty Probe'
cEmtpyContainerBoundingRectangleSize = 500000
cErrorKindSetCanSuppress = [4, 7, 9..10, 13, 19, 23..24, 26..29, 33, 35..36, 56..60, 89]
cErrorKindSetRemoved = [6, 19..22, 25, 32, 43..48, 50..51, 59..62, 68, 100]
cErrorKindSetUseConnectionMatrix = [0, 3..4]
cEvsLmNotification = 'altium.dxp.evslm'
cExpression_CurrentFootprint = 'CurrentFootprint'
cExpression_PCBConfigurationName = 'PCBConfigurationName'
cExpression_SheetSymbolDesignator = 'SheetSymbolDesignator'
cExpression_VariantName = 'VariantName'
cExpressionCalculationError = '#NAME?'
cExpressionRecursiveError = '#Circular Reference?'
cExtendedPrefix = '\\?\'
cExtendedUNCPrefix = '\\?\UNC\'
cExtensionHRID_Embedded = 'Embedded'
cFailedLogin = 2
cfaLinkedOLEDoc = 1048576
cfaShortcut = 65536
cFastCrossProbeObjectType_Net = 'Net'
cFastCrossProbeObjectType_Part = 'Part'
cFastCrossProbeObjectType_Pin = 'Pin'
cFavoriteFoldersChanged = 200
cFileExt_Temp = '.$$$'
cFilename_CurrentDir = '.'
cFilename_ParentDir = '..'
cFindReplaceRectInflate = 5000000
cFirstRule = 0
cFirstSystemParameter = 1
cFitDesignStageName = 'fit_design'
cFlashFileNameExtension = 'FlashFileNameExtension'
cFolderPrefix = #1
cFormula_IndirectionIndicator = '='
cFPGAPreferencesChanged = 15
cFPGAVendor_Actel = 'Actel'
cFPGAVendor_Altera = 'Altera'
cFPGAVendor_Amcc = 'AMCC'
cFPGAVendor_Lattice = 'Lattice'
cFPGAVendor_Sharp = 'Sharp'
cFPGAVendor_STMicroelectronics = 'STMicroelectronics'
cFPGAVendor_Xilinx = 'Xilinx'
cFrequency = 'INTEGER freq = 1;   '' RCK frequency 1-4 MHz'
cFrequencyCounterDeviceName = 'FRQCNT2'
cFrequencyGeneratorDeviceName = 'CLKGEN'
cFROMSTAPLTemplateName = 'ActelFROM.txt'
cFSMObjectInspectorViewName = 'FSMObjectInspector'
cFtdiBoardKinds = [13..14]
cFTP = 'ftp'
cGenericARM7DeviceName = 'GenericARM7Device'
cGenericARM920TDeviceName = 'GenericARM920TDevice'
cGenericARM926EJSDeviceName = 'GenericARM926EJSDevice'
cGenericCapability_Exporter = 'EXPORTER'
cGenericCapability_Importer = 'IMPORTER'
cGenericCapability_Netlister = 'NETLISTER'
cGenericCapability_Outputer = 'OUTPUT'
cGenericCapability_Printer = 'PRINTER'
cGenericCapability_Publisher = 'PUBLISHER'
cGenericCapability_Reporter = 'REPORT'
cGenericComponentsLoaded = 220
cGenericDeviceName = 'GenericDevice'
cGenericFamilyName = 'Generic'
cGetCountParam = '_GetCount_'
cGetItemParam = '_GetItem_'
cGetListParam = '_GetList_'
cGetStateCaption = 'Caption'
cGetStateChecked = 'Checked'
cGetStateEnabled = 'Enabled'
cGetStateParameter = 'GetActionState'
cgiFirst = -512
cgiLast = -1
cGlyphComboBoxEditorAttributes = [6..9, 19..20]
cGOSTPowerGndPowerXOffset1 = 0
cGOSTPowerGndPowerXOffset2 = 400000
cGOSTPowerGndPowerXOffset3 = 800000
cGOSTPowerGndPowerXOffset4 = 800000
cGOSTPowerGndPowerYOffset1 = 1000000
cGOSTPowerGndPowerYOffset2 = 600000
cGOSTPowerGndPowerYOffset3 = 200000
cGOSTPowerGndPowerYOffset4 = 200000
cGOSTPowerLength = 1600000
cGOSTPowerNameXOffset1 = 200000
cGOSTPowerObjectLineWidth = 100000
cGroundTypeSet = [4..6, 8..9]
cGroupCrossprobed = 185
cGroupNavigated = 155
cGUIManagerNotification = 'altium.dxp.guimanager'
cGUIShowed = 17
cHalfDotWidth = 300000
cHalfPowerLength = 500000
ChannelsAll = [0..3]
cHarnessArcRadius_Max = 1000000
cHarnessArcRadius_Min = 100000
cHarnessCableEndsLength = 1000000
cHarnessCPInsulationLineLength = 700000
cHarnessCPRadius = 400000
cHarnessDocumentIds = [1..2]
cHarnessEntryHeight = 200000
cHarnessEntryInstanceSeparator = ':'
cHarnessEntryWidth = 200000
cHarnessShieldPinLength = 1000000
cHarnessSpliceRadius = 400000
CharSet = [32..126]
cHDLSimulator_ActiveHDL = 'Active-HDL'
cHDLSimulator_DXP = 'DXP Simulator'
cHDLSimulator_IntegratedActiveHDL = 'Aldec OEM Simulator'
cHDLSimulator_ModelSim = 'ModelSim'
cHoleToleranceEmptyStr = 'N/A'
cHoleToleranceEmptyValue = 2147483647
CHorzGap = 8
cHotKey_NoKey = -1
cHotkeyPrefix = '&'
cHTTP = 'http'
cHTTPS = 'https'
cIeeeSymbols_Inner = [0, 8..13, 22..24, 30, 32]
cIeeeSymbols_InnerEdge = [0, 3]
cIeeeSymbols_Outer = [0, 2, 5..6, 25, 33..34]
cIeeeSymbols_OuterEdge = [0..1, 4, 17]
cIeeeSymbolScaleForPin = 10
cIEESymbolScale_Max = 20000000
cIEESymbolScale_Min = 100000
cIEESymbolScale_Step = 100000
cImageIndexMarker_Error = 73
cImageIndexMarker_Fatal = 74
cImageIndexMarker_NoError = 71
cImageIndexMarker_Warning = 72
cImageMargin = 4
cImplementation_Designspace = 'Designspace'
cImportedPreferences = 15
cIndexPathSeparator = '-'
cInstallationManagerPreferencesChanged = 19
cInstrumentProbeName = 'Instrument Probe'
cIntegratedLibraryCompiled = 53
cInteractiveMacroKey = 'INTERACTIVE'
cInteractiveMacroKeyEdit = 'INTERACTIVE_EDIT'
cInteractiveMacroKeyStart = 'INTERACTIVE_START'
cInteractiveMacroParamAnchor = 'Anchor'
cInteractiveMacroParamClass = 'Class'
cInteractiveMacroParamEnhance = 'Enhance'
cInteractiveMacroParamHwnd = 'Hwnd'
cInteractiveMacroParamId = 'Id'
cInteractiveMacroParamIdName = 'Id_name'
cInteractiveMacroParamKey = 'Key'
cInteractiveMacroParamKeyName = 'Key_name'
cInteractiveMacroParamLocationX = 'LocationX'
cInteractiveMacroParamLocationY = 'LocationY'
cInteractiveMacroParamLparam = 'LParam'
cInteractiveMacroParamMaxClipX = 'MaxClipX'
cInteractiveMacroParamMaxClipY = 'MaxClipY'
cInteractiveMacroParamMinClipX = 'MinClipX'
cInteractiveMacroParamMinClipY = 'MinClipY'
cInteractiveMacroParamMoved = 'Moved'
cInteractiveMacroParamOnlyOne = 'OnlyOne'
cInteractiveMacroParamPID = 'PID'
cInteractiveMacroParamPointOnHandle = 'PointOnHandle'
cInteractiveMacroParamShift = 'Shift'
cInteractiveMacroParamWparam = 'WParam'
cInteractiveMacroParamX = 'X'
cInteractiveMacroParamY = 'Y'
cInteractivePlacementAborted = 8
cInteractivePlacementBegin = 5
cInteractivePlacementPartial = 6
cInteractivePlacementStop = 9
cInteractivePlacementSuccess = 7
cInteractiveProcessBegin = 1
cInteractiveProcessCanceled = 4
cInteractiveProcessGoalAchieved = 3
cInteractiveProcessStop = 2
cInteractiveProcessUpdate = 28
cInternalOptionsChanged = 41
cInternalPrecision = 10000
cInv2PI = 0.15915493667125702
cInv360 = 0.0027777778450399637
cInvalidCacheFileNameChars = [34, 37, 42, 47, 58, 60, 62..63, 92, 124]
cInvalidWindowsFileNameChars = [34, 42, 47, 58, 60, 62..63, 92, 124]
cJTagDelay_OCDS = 5
cJTagTicksDefault = 4
cJTagTicksMax = 255
cJumpLocationZoomRectHeight = 20000000
cJumpLocationZoomRectWidth = 20000000
cKeepoutONRestrictionsDefault = [0..4]
cKeepoutRestrictionsNotDef = []
cl3DDkShadow = -16777195
cl3DLight = -16777194
cLabelTextSuperscriptGap = 200000
cLabFeaturesChanged = 17
clActiveBorder = -16777206
clActiveCaption = -16777214
clAppWorkSpace = -16777204
clAqua = 16776960
cLastRule = 66
cLastSystemParameter = 36
clBackground = -16777215
clBlack = 0
clBlue = 16711680
clBtnFace = -16777201
clBtnHighlight = -16777196
clBtnShadow = -16777200
clBtnText = -16777198
clCaptionText = -16777207
clCream = 15793151
clDefault = 536870912
clDkGray = 8421504
cLengthInfinite = 0
clFuchsia = 16711935
clGradientActiveCaption = -16777189
clGradientInactiveCaption = -16777188
clGray = 8421504
clGrayText = -16777199
clGreen = 32768
clHighlight = -16777203
clHighlightText = -16777202
clHotLight = -16777190
cLibObjectInspectorViewName = 'SchLibObjectInspector'
cLibrariesMigrated = 37
cLibrariesUpdated = 0
cLibraryComponentMacroLocation = 'Location'
cLibraryComponentMacroParams = 'Params'
cLibraryComponentMacroPlaceKey = 'PLACE_LIBRARY_COMPONENT'
cLibraryDialod = 'LibraryDialog'
cLibraryOpenbusCapability = 'Library:Openbus'
cLibraryVHDL_LibCapability = 'Library:VHDL_LIB'
cLibraryVHDLCapability = 'Library:VHDL'
cLicenseChanged_ForceLease = 29
cLicenseDetailsChanged = 8
cLicenseDetailsChanged_Final = 18
cLicenseDetailsChanged_RefreshDisplay = 10
cLicensesUsed = 38
clInactiveBorder = -16777205
clInactiveCaption = -16777213
clInactiveCaptionText = -16777197
cLineCaption = '-'
CLineShapeArrowRatio = 2
cLineTolerance = 300000
clInfoBk = -16777192
clInfoText = -16777193
cListIndexesParam = '_ListIndexes_'
cListParam = '_ListItems_'
clLime = 65280
clLtGray = 12632256
clMaroon = 128
clMedGray = 10789024
clMenu = -16777212
clMenuBar = -16777186
clMenuHighlight = -16777187
clMenuText = -16777209
clMoneyGreen = 12639424
clNavy = 8388608
clNone = 536870911
cLoggedIn = 0
cLoggedIn_InvalidSession = 4
cLoggedOut = 1
cLoggingOut = 22
clOlive = 32896
clPurple = 8388736
clRed = 255
clScrollBar = -16777216
clSilver = 12632256
clSkyBlue = 15780518
cLsmServerName = 'LayerStackManager'
clstValueAppended = 1
clstValueNextParam = 0
clSystemColor = 4278190080
clTeal = 8421376
clWebAliceBlue = 16775408
clWebAntiqueWhite = 14150650
clWebAqua = 16776960
clWebAquamarine = 13959039
clWebAzure = 16777200
clWebBeige = 14480885
clWebBisque = 12903679
clWebBlack = 0
clWebBlanchedAlmond = 13495295
clWebBlue = 16711680
clWebBlueViolet = 14822282
clWebBrown = 2763429
clWebBurlywood = 8894686
clWebCadetBlue = 10526303
clWebChartreuse = 65407
clWebChocolate = 1993170
clWebCoral = 5275647
clWebCornFlowerBlue = 15570276
clWebCornSilk = 14481663
clWebCrimson = 3937500
clWebCyan = 16776960
clWebDarkBlue = 9109504
clWebDarkCyan = 9145088
clWebDarkGoldenRod = 755384
clWebDarkGray = 11119017
clWebDarkgreen = 25600
clWebDarkKhaki = 7059389
clWebDarkMagenta = 9109643
clWebDarkOliveGreen = 3107669
clWebDarkOrange = 36095
clWebDarkOrchid = 13382297
clWebDarkRed = 139
clWebDarkSalmon = 8034025
clWebDarkSeaGreen = 9419919
clWebDarkSlateBlue = 9125192
clWebDarkSlategray = 5197615
clWebDarkTurquoise = 13749760
clWebDarkViolet = 13828244
clWebDeepPink = 9639167
clWebDeepskyBlue = 16760576
clWebDimGray = 6908265
clWebDodgerBlue = 16748574
clWebFirebrick = 2237106
clWebFloralWhite = 15792895
clWebForestGreen = 2263842
clWebFuchsia = 16711935
clWebGainsboro = 14474460
clWebGhostWhite = 16775416
clWebGold = 55295
clWebGoldenRod = 2139610
clWebGray = 8421504
clWebGreen = 32768
clWebGreenYellow = 3145645
clWebHoneydew = 15794160
clWebHotPink = 11823615
clWebIndianRed = 6053069
clWebIndigo = 8519755
clWebIvory = 15794175
clWebKhaki = 9234160
clWebLavender = 16443110
clWebLavenderBlush = 16118015
clWebLawnGreen = 64636
clWebLemonChiffon = 13499135
clWebLightBlue = 15128749
clWebLightCoral = 8421616
clWebLightCyan = 16777184
clWebLightGoldenrodYellow = 13826810
clWebLightGreen = 9498256
clWebLightgrey = 13882323
clWebLightPink = 12695295
clWebLightSalmon = 8036607
clWebLightSeaGreen = 11186720
clWebLightSkyBlue = 16436871
clWebLightSlateGray = 10061943
clWebLightSteelBlue = 14599344
clWebLightYellow = 14745599
clWebLime = 65280
clWebLimeGreen = 3329330
clWebLinen = 15134970
clWebMagenta = 16711935
clWebMaroon = 128
clWebMediumAquamarine = 11193702
clWebMediumBlue = 13434880
clWebMediumOrchid = 13850042
clWebMediumPurple = 14381203
clWebMediumSeaGreen = 7451452
clWebMediumSlateBlue = 15624315
clWebMediumSpringGreen = 10156544
clWebMediumTurquoise = 13422920
clWebMediumVioletRed = 8721863
clWebMidnightBlue = 7346457
clWebMintcream = 16449525
clWebMistyRose = 14804223
clWebMoccasin = 11920639
clWebNavajoWhite = 11394815
clWebNavy = 8388608
clWebOldLace = 15136253
clWebOlive = 32896
clWebOliveDrab = 2330219
clWebOrange = 42495
clWebOrangeRed = 17919
clWebOrchid = 14053594
clWebPaleGoldenrod = 11200750
clWebPaleGreen = 10025880
clWebPaleTurquoise = 15658671
clWebPaleVioletRed = 9662683
clWebPapayaWhip = 14020607
clWebPeachPuff = 12180223
clWebPeru = 4163021
clWebPink = 13353215
clWebPlum = 14524637
clWebPowderBlue = 15130800
clWebPurple = 8388736
clWebRed = 255
clWebRosyBrown = 9408444
clWebRoyalBlue = 14772545
clWebSaddleBrown = 1262987
clWebSalmon = 7504122
clWebSandyBrown = 6333684
clWebSeaGreen = 5737262
clWebSeashell = 15660543
clWebSienna = 2970272
clWebSilver = 12632256
clWebSkyBlue = 15453831
clWebSlateBlue = 13458026
clWebSlateGray = 9470064
clWebSnow = 16448255
clWebSpringGreen = 8388352
clWebSteelBlue = 11829830
clWebTan = 9221330
clWebTeal = 8421376
clWebThistle = 14204888
clWebTomato = 4678655
clWebTurquoise = 13688896
clWebViolet = 15631086
clWebWheat = 11788021
clWebWhite = 16777215
clWebWhiteSmoke = 16119285
clWebYellow = 65535
clWebYellowGreen = 3329434
clWhite = 16777215
clWindow = -16777211
clWindowFrame = -16777210
clWindowText = -16777208
clYellow = 65535
cm_Access_ReadOnly = 0
cm_Access_ReadWrite = 2
cm_Access_WriteOnly = 1
CM_ACTIONEXECUTE = 45120
CM_ACTIONUPDATE = 45119
CM_ACTIVATE = 45056
CM_ALLCHILDRENFLIPPED = 45118
CM_APPKEYDOWN = 45078
CM_APPSYSCOMMAND = 45079
CM_BASE = 45056
CM_BIDIMODECHANGED = 45116
CM_BORDERCHANGED = 45115
CM_BUFFEREDPRINTCLIENT = 45133
CM_BUTTONPRESSED = 45080
CM_CANCELMODE = 45060
CM_CHANGED = 45111
CM_CHILDKEY = 45102
CM_CLROFFSET = 0
CM_COLORCHANGED = 45069
CM_CONTROLCHANGE = 45110
CM_CONTROLLISTCHANGE = 45100
CM_CONTROLLISTCHANGING = 45132
CM_CREATEPOPUP = 45129
CM_CTL3DCHANGED = 45072
CM_CURSORCHANGED = 45071
CM_CUSTOMGESTURESCHANGED = 45139
CM_CUSTOMSTYLECHANGED = 45145
CM_DEACTIVATE = 45057
CM_DESIGNHITTEST = 45084
CM_DESTROYHANDLE = 45130
CM_DIALOGCHAR = 45062
CM_DIALOGHANDLE = 45105
CM_DIALOGKEY = 45061
CM_DOCKCLIENT = 45112
CM_DOCKNOTIFICATION = 45122
CM_DOCWINDOWACTIVATE = 45099
CM_DOUBLEBUFFEREDCHANGED = 45135
CM_DRAG = 45103
CM_ENABLEDCHANGED = 45068
CM_ENTER = 45082
CM_EXIT = 45083
CM_FLOAT = 45114
CM_FOCUSCHANGED = 45063
CM_FONTCHANGE = 45094
CM_FONTCHANGED = 45070
CM_GESTURE = 45138
CM_GESTUREMANAGERCHANGED = 45140
CM_GETDATALINK = 45101
CM_GOTFOCUS = 45058
CM_HINTSHOW = 45104
CM_HINTSHOWPAUSE = 45121
CM_HITTEST = 45066
CM_ICONCHANGED = 45085
CM_INPUTLANGCHANGE = 45142
CM_INVALIDATE = 45108
CM_INVALIDATEDOCKHOST = 45126
CM_INVOKEHELP = 45087
CM_ISSHORTCUT = 45124
CM_ISTOOLCONTROL = 45106
CM_LOSTFOCUS = 45059
CM_MENUCHANGED = 45077
CM_MOUSEACTIVATE = 45131
CM_MOUSEENTER = 45075
CM_MOUSELEAVE = 45076
CM_MOUSEWHEEL = 45123
cm_NoInheritance = 128
CM_PARENTBIDIMODECHANGED = 45117
CM_PARENTCOLORCHANGED = 45065
CM_PARENTCTL3DCHANGED = 45073
CM_PARENTDOUBLEBUFFEREDCHANGED = 45136
CM_PARENTFONTCHANGED = 45064
CM_PARENTSHOWHINTCHANGED = 45091
CM_PARENTTABLETOPTIONSCHANGED = 45144
CM_POPUPHWNDDESTROY = 45128
CM_RECREATEWND = 45107
CM_RELEASE = 45089
CM_SETACTIVECONTROL = 45127
cm_Share_Compat = 0
cm_Share_DenyN = 64
cm_Share_DenyR = 48
cm_Share_DenyRW = 16
cm_Share_DenyW = 32
CM_SHOWHINTCHANGED = 45090
CM_SHOWINGCHANGED = 45081
CM_STANDARDGESTURESCHANGED = 45141
CM_STYLECHANGED = 45137
CM_SUPPLIER_CATEGORYPARAMETERS = 33171
CM_SUPPLIER_ENDSEARCHBYKEYWORD = 33179
CM_SUPPLIER_GETCATEGORYPARAMETERS = 33180
CM_SUPPLIER_OPTIONS_PAGE_MAKE_READ_ONLY = 33182
CM_SUPPLIER_QUERY_SEARCH_STATUS = 33183
CM_SUPPLIER_SEARCHBYKEYWORD = 33176
CM_SUPPLIER_SEARCHBYMANUFACTURERPARTNUMBER = 33178
CM_SUPPLIER_SEARCHBYSUPPLIERPARTNUMBER = 33177
CM_SUPPLIER_SEARCHCOMPLETED = 33181
CM_SUPPLIER_SEARCHERROR = 33170
CM_SUPPLIER_SEARCHRESULT = 33168
CM_SUPPLIER_SEARCHSTATISTICS = 33169
CM_SYSCOLORCHANGE = 45092
CM_SYSFONTCHANGED = 45109
CM_TABFONTCHANGED = 45156
CM_TABLETOPTIONSCHANGED = 45143
CM_TABSTOPCHANGED = 45096
CM_TEXTCHANGED = 45074
CM_THEMECHANGED = 45137
CM_TIMECHANGE = 45095
CM_UIACTIVATE = 45097
CM_UIDEACTIVATE = 45098
CM_UNDOCKCLIENT = 45113
CM_UNTHEMECONTROL = 45134
CM_UPDATEACTIONS = 45125
CM_VISIBLECHANGED = 45067
CM_WANTSPECIALKEY = 45086
CM_WINDOWHOOK = 45088
CM_WININICHANGE = 45093
cMacroClickAndHold = 'ClickAndHold'
cMapDesignStageName = 'map_design'
cMask_AllFiles = '*.*'
cMaxCutterGridSizeMultiple = 10
CMaxDropWidth = 400
cMaxEditableLayer = 74
cMaxLayer_WidthRule = 32
cMaxNavigationZoomPrecision = 100
cMaxOutputParameters = 131072
cMaxShortStringLength = 254
CMaxTextParamLength = 32000
cMaxWarehouseLayer = 75
cMaxWorkspace = 6500
cMaxWorkspaceSize = 650000000
cMaxZoomFactor = 0.00064
cmBlackness = 66
cmDstInvert = 5570569
cMemoryAddressZero = 0
cMemoryElementZero = 0
cMemoryInstrumentDeviceName = 'MEMORY_INSTRUMENT'
cMemoryInstrumentFamilyDescription = 'Memory Instrument Modules'
cMemoryInstrumentFamilyName = 'MEMORY_INSTRUMENT'
cMemoryLength = 65535
cMessagesAdd = 0
cMessagesClearAll = 3
cMessagesFullUpdate = 2
cMessagesNotification = 'altium.dxp.message'
cMessagesReplaceLast = 1
cMessagesReplaceLastOfSameClass = 4
cMessagesUpdateWindow = 5
cMidLayers = [2..31]
cMinBusUnderlineWidth = 700000
cMinCutterGridSizeMultiple = 2
cMinimumSnapGridSize = 100000
cMiniviewerTolerance = 500000
cMinLayer_WidthRule = 1
cMinPortWidth = 3000000
cMinWireUnderlineWidth = 500000
cMinWorkspace = 10
cMinWorkspaceSize = 1000000
cMinZoomFactor = 5e-07
cMiscellaneous = 'Miscellaneous'
cmMergeCopy = 12583114
cmMergePaint = 12255782
cMMsInMil = 0.0254
cmNotSrcCopy = 3342344
cmNotSrcErase = 1114278
cModelCaption_PCB = 'Footprint'
cModelCaption_PCB3D = '3D PCB Model'
cModelCaption_Sch = 'Symbol'
cModelCaption_SI = 'Signal Integrity'
cModelCaption_Sim = 'Simulation Model'
cModelType_DSH = 'Datasheet'
cModelType_PCAD = 'PCADLib'
cModelType_PCB = 'PCBLIB'
cModelType_PCB3D = 'PCB3DLib'
cModelType_SCH = 'SCHLIB'
cModelType_SI = 'SI'
cModelType_Sim = 'SIM'
cModelType_VHDL = 'VHD'
cModeParam = 'Mode'
cModuleLoaded = 0
cModuleNotification = 'altium.dxp.module'
cMorfikPreferencesChanged = 20
CMouseMsgSignature = 224
cmPatCopy = 15728673
cmPatInvert = 5898313
cmPatPaint = 16452105
cMsgOption_CallBackProcess = 'CallBackProcess'
cMsgOption_CallBackProcess2 = 'CallBackProcess2'
cMsgOption_Class = 'Class'
cMsgOption_Document = 'Document'
cMsgOption_HelpFileName = 'HelpFileName'
cMsgOption_HelpTopic = 'HelpTopic'
cMsgOption_ImageIndex = 'ImageIndex'
cMsgOption_ReplaceLastMsgIfSameClass = 'ReplaceLastMessageIfSameClass'
cMsgOption_ReplaceLastMsgOfSameClass = 'ReplaceLastMessageOfSameClass'
cMsgOption_Source = 'Source'
cMsgOption_UserId = 'UserId'
cmSrcAnd = 8913094
cmSrcCopy = 13369376
cmSrcErase = 4457256
cmSrcInvert = 6684742
cmSrcPaint = 15597702
cMSSConfiguratorOutputDir = 'Actel_MSS_Configurator'
CMT_INPUT = 0
CMT_INTERNAL = 2
CMT_OUTPUT = 1
cmtDisk = 0
cmtHalo = 2
cmtSpeechBubbleOutline = 4
cmtSpeechBubbleSolid = 3
cmtTranslucentDisk = 1
cMultichannelDrawingInstances = 2
cMultichannelDrawingOffset = 200000
cMultiPartNameByAlpha = 0
cMultiPartNameByNumber = 1
cMultiPartNameByNumSeperatorInit = ':'
cmWhiteness = 16711778
CN_BANDCHANGE = 5120
CN_BASE = 48128
CN_CHAR = 48386
CN_CHARTOITEM = 48175
CN_COMMAND = 48401
CN_COMPAREITEM = 48185
CN_CTLCOLORBTN = 48437
CN_CTLCOLORDLG = 48438
CN_CTLCOLOREDIT = 48435
CN_CTLCOLORLISTBOX = 48436
CN_CTLCOLORMSGBOX = 48434
CN_CTLCOLORSCROLLBAR = 48439
CN_CTLCOLORSTATIC = 48440
CN_DELETEITEM = 48173
CN_DRAWITEM = 48171
CN_DROPDOWNCLOSED = 5120
CN_HSCROLL = 48404
CN_KEYDOWN = 48384
CN_KEYUP = 48385
CN_MEASUREITEM = 48172
CN_NOTIFY = 48206
CN_PARENTNOTIFY = 48656
CN_SYSCHAR = 48390
CN_SYSKEYDOWN = 48388
CN_VKEYTOITEM = 48174
CN_VSCROLL = 48405
cNanoBoard2And3000Kinds = [2..11, 15..20]
cNanoBoard3000ALC4Kinds = [18..20]
cNanoBoard3000ALKinds = [6..8]
cNanoBoard3000Kinds = [3..11, 15..20]
cNanoBoard3000Kinds_Manufacture = [5, 8, 11, 17, 20]
cNanoBoard3000Kinds_Normal = [3, 6, 9, 15, 18]
cNanoBoard3000Kinds_Update = [4, 7, 10, 16, 19]
cNanoBoard3000LCKinds = [9..11]
cNanoBoard3000XNKinds = [3..5]
cNanoBoard3000XNS6Kinds = [15..17]
cNanoBoardCustomKinds = [12]
cNavigationHistory = 160
cnDeleting = 2
cNewTypeTentingDefault = False
cnExtracting = 1
cNexusBeginUpdate = 1
cNexusClockManagers = [7]
cNexusConfigFileName = 'NexusConfig.ini'
cNexusConnectionStatusChanged = 4
cNexusDeviceIdParameterName = 'NexusDeviceId'
cNexusEndUpdate = 2
cNexusFPGAProgrammed = 10
cNexusHardDeviceUserChange = 12
cNexusInstrumentAction = 9
cNexusInstruments = [1, 6]
cNexusInstrumentsChanged = 11
cNexusMemories = [4..5]
cNexusNotification = 'altium.dxp.nexus'
cNexusNotificationWithInterface = 'altium.dxp.nexus.interface'
cNexusOnIdle = 3
cNexusParameterName_ClockAOperation = 'ClkA_Operation'
cNexusParameterName_ClockBOperation = 'ClkB_Operation'
cNexusParameterName_ClockCOperation = 'ClkC_Operation'
cNexusParameterName_ClockCount = 'Clk_Count'
cNexusParameterName_ClockDOperation = 'ClkD_Operation'
cNexusParameterName_ClockInputFrequency = 'Clk_InputFreq_MHz'
cNexusParameterName_Connector = 'NEXUS_JTAG_CONNECTOR'
cNexusParameterName_Core = 'NEXUS_CORE'
cNexusParameterName_Device = 'NEXUS_JTAG_DEVICE'
cNexusParameterName_FPGA = 'NEXUS_FPGA_DEVICE'
cNexusParameterName_Index = 'NEXUS_JTAG_INDEX'
cNexusParameterName_MemoryByteIndex = 'Memory_ByteIndex'
cNexusParameterName_MemoryByteWrites = 'Memory_ByteWrites'
cNexusParameterName_MemoryClockEdge = 'Memory_ClockEdge'
cNexusParameterName_MemoryContentEndianness = 'Memory_ContentEndianness'
cNexusParameterName_MemoryContentFile = 'Memory_ContentFile'
cNexusParameterName_MemoryDepth = 'Memory_Depth'
cNexusParameterName_MemoryDepthA = 'Memory_DepthA'
cNexusParameterName_MemoryDepthB = 'Memory_DepthB'
cNexusParameterName_MemoryEnablePin = 'Memory_EnablePin'
cNexusParameterName_MemoryHalfIndex = 'Memory_HalfIndex'
cNexusParameterName_MemoryPreloadDone = 'Memory_PreloadDone'
cNexusParameterName_MemoryProgramFile = 'Memory_ProgramFile'
cNexusParameterName_MemoryResetPin = 'Memory_ResetPin'
cNexusParameterName_MemoryType = 'Memory_Type'
cNexusParameterName_MemoryUse = 'Memory_Use'
cNexusParameterName_MemoryWidth = 'Memory_Width'
cNexusParameterName_MemoryWidthA = 'Memory_WidthA'
cNexusParameterName_MemoryWidthB = 'Memory_WidthB'
cNexusParameterName_Order = 'NEXUS_JTAG_ORDER'
cNexusParameterName_PCInterface = 'NEXUS_PC_INTERFACE'
cNexusPortChainsChanged = 6
cNexusPortsChanged = 5
cNexusProcessFlowStatusChanged = 8
cNexusProcessors = [1..2]
cNexusProcessorsAndHardProcessor = [1..3]
cNexusProjectCoreTreeChanged = 7
cNexusReleaseChanged = 13
cNexusWorkbenchPrefParameter_DisabledDongles = 'NexusWBP.DisabledDongles'
cNGCExt = 'NGC'
cNGOExt = 'NGO'
cNoERCLength = 400000
cNoErrorString = 'NoError'
cNonSelectableObjects = [1, 6, 29, 32..33, 42, 44..47, 65..66, 79..80]
cNoParameterPresent = '<no parameter>'
cNoteRectOffset1 = 1000000
cNoteRectOffset2 = 100000
cNoteShowFullCollapse = 1.5e-05
cNoteShowHalfCollapse = 1e-05
cNoteTextMargin = 500000
cNotification = 'altium.dxp.unknown'
cNotificationShutDown = 'altium.dxp.shutdown'
cNoUnionIndex = 0
cNoVariantCaption = '[No Variations]'
cObjectCrossprobed = 180
cObjectInspectorViewName = 'SchObjectInspector'
cObjectKindString_BoardProject = 'PCB Project'
cObjectKindString_FreeDocumentsProject = 'Free Documents'
cObjectNavigated = 150
cObjectPlace = 26
coDigitAsNumbers = 8
cOffSheetLeftLength = 200000
cOffSheetLength = 700000
cOffSheetNameXOffset1 = 700000
cOffSheetNameYOffset1 = 500000
cOffSheetOffset1 = 500000
coIgnoreCase = 2
coIgnoreKanatype = 3
coIgnoreNonSpace = 4
coIgnoreSymbols = 5
coIgnoreWidth = 6
cOldMaxPolygonVertices = 50
cOldSheetEntryGrid = 10
coLingCasing = 7
coLingIgnoreCase = 0
coLingIgnoreDiacritic = 1
COLOR_GRAYSCALE = 0
COLOR_GRAYSCALEALPHA = 4
COLOR_PALETTE = 3
COLOR_RGB = 2
COLOR_RGBALPHA = 6
ColumnHeaderWidth = -2
ColumnTextWidth = -1
ComCtlVersionIE3 = 262214
ComCtlVersionIE4 = 262215
ComCtlVersionIE401 = 262216
ComCtlVersionIE5 = 327760
ComCtlVersionIE501 = 327761
ComCtlVersionIE6 = 393216
cOneHalf = 0.5
ConnectiveObjectsSet = [3, 7, 16, 19..20, 24, 26, 28, 32, 35..41, 48, 53..54, 56, 81..83, 85..86, 88..89, 94]
constDefaultAutoCompleteDelay = 500
constTextMargin = 2
cOpenBusObjectInspectorViewName = 'OpenBusObjectInspector'
cOpenBusPin_HarnessEntry_ParameterName = 'OPENBUS~HarnessEntry'
CopperPlatingLayerTypeId = '{B0827674-798C-4CF8-807C-8E6C2A11C145}'
cOptionName_ConfigurationDevice = 'Configuration Device'
cOptionName_ConfigurationScheme = 'Configuration Scheme'
cOptionName_SkipTimingAnalysis = 'Skip Timing Analysis'
CoreLayerTypeId = '{136C62EF-1FA6-4897-AE71-7E797B632B92}'
cOS_PowerRestored = 100
coStringSort = 9
cPanelsChanged = 9
cParamDelim2 = #2
cParamDelimiter = '|'
cParameter_Clock = 'FPGA_CLOCK'
cParameter_ClockAllowOnNonClockPin = 'FPGA_CLOCK_ALLOW_ON_NON_CLOCK_PIN'
cParameter_ClockDutyCycle = 'FPGA_CLOCK_DUTY_CYCLE'
cParameter_ClockFirstPulse = 'FPGA_CLOCK_FIRST_PULSE'
cParameter_ClockFrequency = 'FPGA_CLOCK_FREQUENCY'
cParameter_ClockPin = 'FPGA_CLOCK_PIN'
cParameter_CoreComponent = 'CORE_COMPONENT'
cParameter_DefaultIOStandard = 'FPGA_DEFAULT_IOSTANDARD'
cParameter_Device = 'FPGA_DEVICE'
cParameter_DriveStrength = 'FPGA_DRIVE'
cParameter_EnumEncoding = 'FPGA_ENUM_ENCODING'
cParameter_FastPin = 'FPGA_FAST_PIN'
cParameter_Flatten = 'FPGA_FLATTEN'
cParameter_Global = 'FPGA_GLOBAL'
cParameter_HoldValue = 'FPGA_HOLD_VALUE'
cParameter_InhibitBuffer = 'FPGA_INHIBIT_BUFFER'
cParameter_IOStandard = 'FPGA_IOSTANDARD'
cParameter_Keep = 'FPGA_KEEP'
cParameter_MaxDelay = 'FPGA_DELAY_MAX'
cParameter_MaxDelayFrom = 'FPGA_DELAY_MAX_FROM'
cParameter_MaxDelayTo = 'FPGA_DELAY_MAX_TO'
cParameter_Memory_Content = 'FPGA_MEMORY_CONTENT'
cParameter_Memory_Type = 'FPGA_MEMORY_TYPE'
cParameter_NoClock = 'FPGA_NOCLOCK'
cParameter_PCIClamp = 'FPGA_PCI_CLAMP'
cParameter_Pinnum = 'FPGA_PINNUM'
cParameter_Pulldown = 'FPGA_PULLDOWN'
cParameter_Pullup = 'FPGA_PULLUP'
cParameter_ReservePin = 'FPGA_RESERVE_PIN'
cParameter_SlewRate = 'FPGA_SLEW'
cParameter_SwapId = 'SWAPID'
cParameterName_Comment = 'Comment'
cParameterName_ComponentAlias = 'Alias'
cParameterName_ComponentController = 'Controller'
cParameterName_Description = 'Description'
cParameterName_Designator = 'Designator'
cParameterName_ExcludeFromSimulation = 'ExcludeFromSimulation'
cParameterName_ExternalNetName = 'ExternalNetName'
cParameterName_HelpURL = 'HelpURL'
cParameterName_InstrumentProbe = 'InstrumentProbe'
cParameterName_LibraryReference = 'LibraryReference'
cParameterName_PageSetup = 'PageSetup'
cParameterName_PartField = 'Part Field'
cParameterName_PartType = 'PartType'
cParameterName_PinDefaultNetName = 'DefaultNet'
cParameterName_PinHiddenNetName = 'HiddenNetName'
cParameterName_PinSelectionMemory = 'PinSelectionMemory'
cParameterName_PinUniqueId = 'PinUniqueId'
cParameterName_ProbeCustomName = 'ProbeCustomName'
cParameterName_ProbeDisplayName = 'ProbeValueDisplay'
cParameterName_ProbeName = 'ProbeName'
cParameterName_SimulationDescription = 'Simulation Description'
cParameterName_SimulationExcludedParts = 'Simulation ExcludedParts'
cParameterName_SimulationFile = 'Simulation File'
cParameterName_SimulationGenericComponent = 'SimulationGenericComponent'
cParameterName_SimulationKind = 'Simulation Kind'
cParameterName_SimulationModelName = 'Simulation ModelName'
cParameterName_SimulationNetList = 'Simulation Netlist'
cParameterName_SimulationParameters = 'Simulation Parameters'
cParameterName_SimulationPortMap = 'Simulation PortMap'
cParameterName_SimulationProbe = 'SimulationProbe'
cParameterName_SimulationSpicePrefix = 'Simulation SpicePrefix'
cParameterName_SimulationSubKind = 'Simulation SubKind'
cParameterName_SourceVerilogModule = 'VERILOGMODULE'
cParameterName_SourceVHDLEntity = 'VHDLENTITY'
cParameterName_StyleID = 'StyleID'
cParameterName_System = 'System'
cParameterSetCircleCenterOffset = 1200000
cParameterSetCircleRadius = 600000
cParameterSetIOffsetX = 1200000
cParameterSetIOffsetY = 500000
cParameterSetLineLength = 600000
cParameterSetLineWidth = 100000
cParameterSetParam000XOffset = 3200000
cParameterSetParam090XOffset = 400000
cParameterSetParam090YOffset = 2400000
cParameterSetParam180XOffset = 1200000
cParameterSetParam270XOffset = 1000000
cParameterSetParam270YOffset = 2200000
cParameterSetParamDefaultLength = 500000
cParameterSetParamDeltaYOffset1 = 1200000
cParameterSetParamYOffset = 200000
cParameterSetTextOffetX = 2000000
cParameterSetTinyCircleCenterOffset = 400000
cParameterSetTinyCircleRadius = 200000
cParameterSetTinyIOffsetX = 400000
cParameterSetTinyIOffsetY = 166666
cParameterSetTinyLineLength = 200000
cParameterSetTinyLineWidth = 33333
cParameterSetTinyParam000XOffset = 1066666
cParameterSetTinyParam090XOffset = 133333
cParameterSetTinyParam090YOffset = 800000
cParameterSetTinyParam180XOffset = 400000
cParameterSetTinyParam270XOffset = 333333
cParameterSetTinyParam270YOffset = 733333
cParameterSetTinyParamDefaultLength = 166666
cParameterSetTinyParamDeltaYOffset1 = 400000
cParameterSetTinyParamYOffset = 66666
cParameterSetTinyTextOffetX = 666666
cParamName_Checksum = 'Checksum'
cParamName_CheckUntracked = 'CheckUntracked'
cParamName_Comment = 'Comment'
cParamName_ComponentComment = 'Component.Comment'
cParamName_ComponentDescription = 'Component.Description'
cParamName_ComponentItemGUID = 'Component.ItemGUID'
cParamName_ComponentKind = 'Component.Kind'
cParamName_ComponentLibrary = 'Component.Library'
cParamName_ComponentLibraryItemID = 'Component.LibraryItemID'
cParamName_ComponentPlacement = 'Component.Placement'
cParamName_ComponentRevisionGUID = 'Component.RevisionGUID'
cParamName_ComponentVaultGUID = 'Component.VaultGUID'
cParamName_CurrentFootprint = 'CurFootPrint'
cParamName_Description = 'Description'
cParamName_DocKind = 'Kind'
cParamName_DocumentFilename = 'DocumentFilename'
cParamName_FileName = 'Filename'
cParamName_FocusedCategory = 'FocusedCategory'
cParamName_Footprint = 'Footprint'
cParamName_IsCustomCommand = 'IsCustomCommand'
cParamName_IsEmbedded = 'Embed'
cParamName_LibrarySource = 'LibrarySource'
cParamName_MessageIndex = 'MessageIndex'
cParamName_ModelID = 'ModelID'
cParamName_ModelSource = 'ModelSource'
cParamName_ModelType = 'ModelType'
cParamName_Name = 'Name'
cParamName_PartID = 'PartID'
cParamName_ProjectFullPath = 'ProjectFullPath'
cParamName_PushAvailable = 'PushAvailable'
cParamName_Result = 'Result'
cParamName_Revision = 'Revision'
cParamName_RevisionType = 'RevisionType'
cParamName_RuleName = 'RuleName'
cParamName_SaveToServer = 'SaveToServer'
cParamName_ShowDialog = 'ShowDialog'
cParamName_VaultFootprint = 'VaultFootprint'
cParamNameDocumentKind = 'DocumentKind'
cParamValue_None = 'None'
cPartProvidersPreferencesChanged = 36
cPathParam = '_Path_'
cPathSeparator = '\'
cPauseInteractiveProcess = 38
cPCB3DPreferencesChanged = 7
cPCBPreferencesChanged = 3
cPCBReleaseDataNotification = 'altium.dxp.edm.pcbreleasedata'
cPI = 3.1415927410125732
cPicoSecond_Factor = 1e-12
cPIdiv180 = 0.01745329238474369
cPIdiv2 = 1.5707963705062866
cPIdiv4 = 0.7853981852531433
cPinBoundingRectInflate = 200000
cPinFullBoundingRectInflate = 500000
cPinHeight = 1000000
cPinIEEESymbolRectInflateBy = 600000
cPinLineWidth = 100000
cPinNameXOffset1 = 200000
cPinNameYOffset1 = 200000
cPinNumberXHalfOffset1 = 200000
cPinNumberXOffset1 = 400000
cPinNumberYHalfOffset1 = 200000
cPinNumberYOffset1 = 400000
cPinSymbolXOffset1 = 600000
cPinSymbolYOffset1 = 600000
cPlacementMethod_DragNDrop = 16384
cPlacementMethod_Single = 32768
cPlacementMethod_SingleRepeatable = 8192
cPolygonObjectsSet = [17..21, 56, 61, 82, 86, 92..93, 98]
cPolylineBoundingRectInflate = 1000000
cPolylineCutterBoxHeight = 300000
cPortHeight = 1000000
cPortTextGap = 1000000
cPortWidthInflate = 1000000
cPowerGndPowerXOffset1 = 0
cPowerGndPowerXOffset2 = 300000
cPowerGndPowerXOffset3 = 600000
cPowerGndPowerXOffset4 = 900000
cPowerGndPowerYOffset1 = 1000000
cPowerGndPowerYOffset2 = 700000
cPowerGndPowerYOffset3 = 400000
cPowerGndPowerYOffset4 = 100000
cPowerLength = 1000000
cPowerNameXOffset1 = 200000
cPowerObjectLineWidth = 100000
CPP_ABI_ADJUST = 24
cPreferencesChangedAndSaved = 101
cPrefIdentHeader_DocumentsInstallPath = 'DocumentsInstallPath'
cPrefIdentHeader_InstallationInProgress = 'InstallationInProgress'
cPrefIdentHeader_NewInstaller = 'NewInstaller'
cPrefIdentHeader_PrevAppLoc = 'Application'
cPrefIdentHeader_PrevBeta = 'Beta'
cPrefIdentHeader_PrevBuild = 'Build'
cPrefIdentHeader_PrevDisplayName = 'Display Name'
cPrefIdentHeader_PrevFullBuild = 'FullBuild'
cPrefIdentHeader_PrevInstalled = 'Installed'
cPrefIdentHeader_PrevName = 'Name'
cPrefIdentHeader_PrevReleaseDate = 'ReleaseDate'
cPrefIdentHeader_PrevSecLoc = 'Security'
cPrefIdentHeader_ProgramsInstallPath = 'ProgramsInstallPath'
cPrefIdentHeader_RegistrySection = 'RegistrySection'
cPrefIdentHeader_UniqueID = 'UniqueID'
cPrefIdentHeader_Version = 'Version'
cPrefix_Model = 'Model.'
cPrefLocationSection = 'Preference Location'
cPreviousDefaultElectricalGridSize_1 = 1000000
cPreviousDefaultElectricalGridSize_2 = 800000
cPricingNameValueSeparator = '='
cPrintZoomFactor = 0.0001
cProbeLength = 1000000
cProbeParameterName = 'Probe'
cProcessorDeviceName = 'ProcessorDeviceName'
cProductLineGUID_CircuitMaker = '7673202F-D04D-4367-8D6A-CB17B3438302'
cProgramDeviceStageName = 'program_device'
cProjectAddExistingFile = 32
cProjectAddNewFile = 33
cProjectClosing = 18
cProjectCreated = 49
cProjectDDMCompiled = 51
cProjectDeviceSheetsChanged = 22
cProjectDocumentsOrderChanged = 50
cProjectImportFinished = 48
cProjectImportStarted = 47
cProjectMakeAvailableOnlineFinished = 54
cProjectManagedParametersChanged = 55
cProjectOptionsChange = 31
cProjectRemoveFile = 34
cProjectVariantChanged = 21
cProjectVariantChangedSilently = 28
cPropagationDelayDefault = 0
cQIPExt = 'QIP'
cQuickReplicateKey = 'QUICK_REPLICATE'
crAppStart = -19
crArrow = -2
crCross = -3
crDefault = 0
crDrag = -12
crDragOkCursor = 6
cRectangularHoleString = 'Rectangle'
cRefreshNavigationPanels = 170
cReleaseManagementChanged = 16
cReplaceFrequency = '.ReplaceFrequency'
cReplacePOSTDR = '.ReplacePOSTDR'
cReplacePOSTIR = '.ReplacePOSTIR'
cReplacePREDR = '.ReplacePREDR'
cReplacePREIR = '.ReplacePREIR'
cReplaceUseRCK = '.ReplaceUseRCK'
cRequiresWorkspace = 'Requires workspace'
cResettingPassword = 3
cResourceCounter_Documents = 'Documents'
cResumeInteractiveProcess = 39
cRetrievedOperator = 15
cRetrievedOperatorAccount = 20
cRevision_Latest = 'Latest'
cRevisionType_Commit = 'Commit'
cRevisionType_Release = 'Release'
crHandCursor = 4
crHandPoint = -21
crHelp = -20
crHourGlass = -11
crHSplit = -14
crIBeam = -4
CRLF = #13#10
crMultiDrag = -16
crnLeftBottom = 2
crnLeftTop = 0
crNo = -18
crNoDrop = -13
crNone = -1
crnRightBottom = 3
crnRightTop = 1
cRoutingDiffPairGapToUseCurrent = -4
cRoutingDiffPairGapToUseMax = -3
cRoutingDiffPairGapToUseMin = -1
cRoutingDiffPairGapToUsePreferred = -2
cRoutingWidthToUseCurrent = -4
cRoutingWidthToUseMax = -3
cRoutingWidthToUseMin = -1
cRoutingWidthToUsePreferred = -2
crPenCursor = 7
crSize = -22
crSizeAll = -22
crSizeNESW = -6
crSizeNS = -7
crSizeNWSE = -8
crSizeWE = -9
crSQLWait = -17
cRTFLinkRectOffset1 = 1000000
cRTFLinkRectOffset2 = 100000
cRTFLinkShadowOffset = 100000
cRTFLinkShowFullCollapse = 1.5e-05
cRTFLinkShowHalfCollapse = 1e-05
crUpArrow = -10
crVSplit = -15
crWarningCursor = 5
csAcceptsControls = 0
csActionClient = 15
csAligning = 14
csAlignmentNeeded = 4
csAlignWithMargins = 20
csAllocated = 1
csAncestor = 5
csCaptureMouse = 1
cSchDocumentIds = [5, 102, 117]
csCheckPropAvail = 1
cSchInternalTolerance_Metric = 20000
cSchPreferencesChanged = 4
cSchPreferencesChanged_UpdateStringsFont = 10
cSchPreferencesChangedWithUpdate = 5
csClicked = 1
csClickEvents = 3
cScopeChanged = 210
cScrapCompileOption_ForceAddParams = 'ForceAddParameters'
csCreating = 6
cScriptingPreferencesChanged = 14
csCustomPaint = 8
csDesignerHide = 11
csDesigning = 4
csDesignInstance = 10
csDesignInteractive = 2
csDestroying = 3
csDestroyingHandle = 9
csDisplayDragImage = 13
cSDKNotification = 'altium.dxp.SDK'
csDocking = 10
csDoubleClicks = 7
cSdParameterName_ConnectionDesignator = 'ConnectionDesignator'
cSdParameterName_DatabaseTableName = 'DatabaseTableName'
cSdParameterName_DesignItemId = 'DesignItemId'
cSdParameterName_ExternalNetName = 'ExternalNetName'
cSdParameterName_HarnessDesignator = 'HarnessDesignator'
cSdParameterName_Id = 'Id'
cSdParameterName_ItemGUID = 'ItemGUID'
cSdParameterName_MatedEntry = 'MatedMatedEntry'
cSdParameterName_MatedPin = 'MatedPin'
cSdParameterName_NetName = 'NetName'
cSdParameterName_ParentId = 'ParentId'
cSdParameterName_ParentSourceId = 'ParentSourceId'
cSdParameterName_PhysicalPath = 'PhysicalPath'
cSdParameterName_SourceId = 'SourceId'
cSdParameterName_SourceLibraryName = 'SourceLibraryName'
cSdParameterName_SystemDesignUniqueId = 'SystemDesignUniqueId'
cSdParameterName_VaultGUID = 'VaultGUID'
cSdServerName = 'SystemDesigner'
cSdUnidentifiedPart = '$$$'
cSection_General = 'General'
cSelectionMacroDeselectedKey = 'DESELECTED'
cSelectionMacroParamHash = 'Hash'
cSelectionMacroParamHiX = 'HighX'
cSelectionMacroParamHiY = 'HighY'
cSelectionMacroParamLayer = 'Layer'
cSelectionMacroParamLoX = 'LowX'
cSelectionMacroParamLoY = 'LowY'
cSelectionMacroParamOrigin = 'Origin'
cSelectionMacroParamUniqueId = 'UniqueId'
cSelectionMacroSelectedKey = 'SELECTED'
cServerName_MBA = 'MultiBoardAssembly'
cServerName_PCB = 'PCB'
cServerName_SCH = 'SCH'
csFixedHeight = 9
csFixedWidth = 8
csFixups = 7
csFocusing = 5
csFramed = 4
csFreeNotification = 8
csGestures = 21
csGlassPaint = 15
cSheetEntryArrowThickness = 200000
cSheetEntryHeight = 800000
cSheetEntryTextGap = 500000
cSheetEntryWidth = 1500000
cSheetNumberSpaceSizeMax = 16
cSheetNumberSpaceSizeMin = 1
cSheetSymbolBoundingRectInflate = 2000000
cSheetSymbolDeviceSheetRadius = 500000
cShowModelModeBoth = 0
cShowModelModeExtrudedOnly = 2
cShowModelModeGenericOnly = 1
cShowModelModePreferGeneric = 3
cSimpleLineTolerance = 300000
cSimulationProbeName = 'Simulation Probe'
cSinglePortModules = [0..2]
csInheritable = 0
csInline = 9
csLButtonDown = 0
csLoading = 0
csMenuEvents = 16
csNeedsBorderPaint = 17
csNoDesignVisible = 10
csNoStdEvents = 12
cSoftDesignNanoboardsChanged = 1
cSoftDesignNotification = 'altium.dxp.softdesign'
csOpaque = 6
csOverrideStylePaint = 23
csPaintBlackOpaqueOnGlass = 22
csPaintCopy = 7
csPalette = 2
csPannable = 19
csPanning = 12
csParentBackground = 18
cSpecctraIF_ServerName = 'SpecctraIF'
cSpecialStringApplicationBuildNumber = 'Application_BuildNumber'
cSpecialStringComputerName = 'ComputerName'
cSpecialStringsFileName = '.SpecialStrings'
cSpecialStringsParameterNameParameters = 'Parameters'
csPrintClient = 16
csReading = 1
csReadingState = 3
csRecreating = 13
csReflector = 14
csReplicatable = 11
csReserved = 2
csSetCaption = 5
csSubComponent = 2
csSysAllocated = 3
csSysReserved = 4
cSTAPLTemplateName = 'STAPLTemplate.txt'
cStimulusParameterName = 'Stimulus'
csTransient = 3
cStringArrayDelimiter = ';'
cStringEditorAttributes = [5..8, 12, 14, 17..20, 40..42, 54..55, 61, 63..65, 68, 99..103, 106..107, 113, 115, 117, 119, 128..131, 140]
cStructureFileExtension = 'Structure'
cStyleID_None = 0
csUnallocated = 0
csUpdating = 6
cSupplierDefaultCountry = 'Unknown'
cSupplierDefaultCurrency = 'USD'
cSupplierDefaultLanguage = 'en-US'
cSupplierName_Allied = 'Allied'
cSupplierName_Altium = 'Altium'
cSupplierName_Arrow = 'Arrow'
cSupplierName_Avnet = 'Avnet'
cSupplierName_Ciiva = 'Ciiva'
cSupplierName_DigiKey = 'Digi-Key'
cSupplierName_Farnell = 'Farnell'
cSupplierName_Mouser = 'Mouser'
cSupplierName_Newark = 'Newark'
cSupplierName_ODBC = 'ODBC'
cSupplierName_RS = 'RS-Components'
cSupplierTimeoutMS = 60000
cSupportsCPLDDevice = 'CPLD'
cSupportsFPGADevice = 'FPGA'
cSupportsGenericProcessor = 'GPROC'
cSupportsHardProcessor = 'PROC'
cSupportsPROMDevice = 'PROM'
cSupportsSoftProcessor = 'SPROC'
cSWPLatest = 'AD13'
cSWPRelease10 = 'R10'
cSWPRelease10_1 = 'AD13'
cSWPSummer09 = 'S09'
cSWPUnknown = 'Unknown'
csWriting = 2
cSysParamName_ConfiguratorName = 'ConfiguratorName'
cSysParamName_Designator = 'Designator'
cSysParamName_DeviceFamily = 'DeviceFamily'
cSysParamName_DeviceName = 'DeviceName'
cSysParamName_DocumentPath = 'DocumentPath'
cSysParamName_FPGAVendor = 'FPGAVendor'
cSysParamName_HDLType = 'HDLType'
cSysParamName_ProjectPath = 'ProjectPath'
cSysParamName_SubProjectPath = 'SubProjectPath'
cSysParamName_Vendor = 'Vendor'
cSysParamName_Version = 'Version'
cSysParamName_VHDLConfiguration = 'Configuration'
cSystemNotification = 'altium.dxp.system'
cSystemOnModuleBoardKinds = [14]
cSystemPreferencesCanceled = 39
cSystemPreferencesChanged = 1
cSystemPreferencesPageChange = 40
ctCounterHoleAngle = 19
ctCounterHoleDepth = 18
ctCustom = 7
cTemplateSourceLocal = 'Local'
cTemplateSourceServer = 'Server'
cTemplateTypeDocDefault = 'DocDefault'
cTemplateTypeNone = 'None'
cTemporarilyLoggedIn = 6
cTextEditPreferencesChanged = 2
cTextFrameTextMargin = 5
cTextHorizontalMargin = 4
cTextVerticalMargin = 4
ctHitCount = 1
ctHoleNegativeTolerance = 15
ctHolePositiveTolerance = 14
ctHoleTolerance = 13
ctHoleType = 6
cTitleBlockHeight = 8000000
cTitleBlockHeight1 = 5000000
cTitleBlockHeight2 = 2000000
cTitleBlockHeight3 = 1000000
cTitleBlockTextXPos_Date1 = 34500000
cTitleBlockTextXPos_Date2 = 30000000
cTitleBlockTextXPos_DrawnBy = 14500000
cTitleBlockTextXPos_File1 = 34500000
cTitleBlockTextXPos_File2 = 30000000
cTitleBlockTextXPos_Number = 29500000
cTitleBlockTextXPos_Revision = 9500000
cTitleBlockTextXPos_SheetNbr = 14500000
cTitleBlockTextXPos_SheetStyle = 34000000
cTitleBlockTextXPos_Size = 34500000
cTitleBlockTextXPos_Title = 34500000
cTitleBlockTextYPos_SheetStyle = 3500000
cTitleBlockTextYPos_TextLine1 = 2000000
cTitleBlockTextYPos_TextLine2 = 1000000
cTitleBlockWidth = 35000000
cTitleBlockWidth1 = 10000000
cTitleBlockWidth2 = 15000000
cTitleBlockWidth3 = 30000000
CTL3D_ALL = 65535
ctLayerPairIndex = 8
ctLength = 3
ctObjectId = 9
ctPadShape = 10
ctPlated = 5
ctRoutPathLength = 4
ctSymbol = 0
ctTemplateDescription = 12
ctTemplateName = 11
ctToolSize = 2
ctViaStructureFeature = 17
ctViaStructureType = 16
cUndoRedo = 24
cUnixPathDelimiter = '/'
cUnknownInstruction = 4294967295
cUnknownNexusDeviceName = 'Unknown Device'
cURLEncodeDelimiter = '%'
CurveKappa = 0.5522847498
CurveKappaInv = 0.4477152502
cUseRCK = 'BOOLEAN USE_RCK=1;'
cV6_MaxLayer_WidthRule = 32
cV6_MaxWarehouseLayer = 75
cV6_MinLayer_WidthRule = 1
cV6_WidthRuleLayers = [1..32]
cValidateStateTransitionNotification = 'altium.dxp.validatestatetransition'
cValidateStateTransitionNotificationEx = 'altium.dxp.validatestatetransitionex'
cValue_DeviceFamily = 'DeviceFamily'
cValue_DeviceVendor = 'DeviceVendor'
cValueParam = '_Value_'
CValuesDelimiter = '~'
cValueSeparator = #2
cVariantSchLibrarySuffix = 'Variants'
cVCSDocumentsBeforeCommit = 12
cVCSDocumentsReverted = 11
cVCSDocumentsRevertedRenamed = 18
cVCSFilesDeleted = 6
cVCSFileStatusChanged = 9
cVCSFileUploaded = 10
cVCSLocationInRepositoryChanged = 5
cVCSNotification = 'altium.dxp.vcs'
cVCSProjectChanged = 8
cVCSProjectCheckouted = 7
cVCSProjectCommited = 14
cVCSProjectPushed = 16
cVCSProjectRemotelyChanged = 13
cVCSProjectRevertedToRevision = 19
cVCSProjectUpdated = 17
cVCSRevisionsChanged = 3
cVCSStatusChanged = 2
cVCSUploadComplete = 15
cVendorACTEL = 'Actel'
cVersionControlAddedRepositoryNotFromUI = 23
cVersionControlPreferencesChanged = 8
cVersionControlPreferencesChangedButNotYetApplied = 18
cVERTSTExt = 'VERTST'
cVExt = 'V'
cVHDExt = 'VHD'
cVHDLExt = 'VHDL'
cVHDLPrefName_AddTopLevel = 'Add Top Level Signals'
cVHDLPrefName_CleanOutput = 'Clean Output'
cVHDLPrefName_ClearWMMessages = 'Clear WMessages'
cVHDLPrefName_CompileOnlyIfModified = 'Compile Only If Modified'
cVHDLPrefName_CrossProbeSchematic = 'Crossprobe Schematic'
cVHDLPrefName_DefaultTimeUnit = 'Default Time Unit'
cVHDLPrefName_DeltaIterationsLimit = 'Delta Iterations Limit'
cVHDLPrefName_EnableModelCopy = 'EnableModelCopy'
cVHDLPrefName_JumpToFirstError = 'Jump To First Error'
cVHDLPrefName_LibraryClean = 'Library Clean'
cVHDLPrefName_LibraryModified = 'Compile If Library Modified'
cVHDLPrefName_LinkOnCompile = 'Link On Compile'
cVHDLPrefName_SaveOnSimulate = 'Save On Simulate'
cVHDLPrefName_SaveOnSynthesize = 'Save On Synthesize'
cVHDLPrefName_SearchHDLModels = 'Search HDL Models'
cVHDLPrefName_SeverityLevel = 'Severity Level'
cVHDLPrefName_ShowExecutionPoint = 'Show Execution Point'
cVHDLPrefName_ShowSignals = 'Show Signals'
cVHDLPrefName_ShowSignalsDialog = 'Show Signals Dialog'
cVHDLPrefName_ShowVariables = 'Show Variables'
cVHDLPrefName_ShowWaveform = 'Show Waveform'
cVHDLPrefName_SmartCompile = 'Smart Compile'
cVHDLPrefName_SynthesizeOnFailedCompile = 'SynthesizeOnFailedCompile'
cVHDLPrefName_UseBuiltInLibraries = 'Use Built-In Libraries'
cVHDLPrefName_UserEDIFDirectory = 'User EDIF Directory'
cVHDLPrefName_UserSchHDLModelDirectory = 'User Schematic HDL Model Directory'
cVHDLPrefName_UserSimulationLibraries = 'User Simulation Libraries'
cVHDLPrefName_UseVHDLForCompilation = 'UseVHDLForCompilation'
cVHDLPrefName_ZoomToSchematic = 'Zoom To Schematic'
cVHDLSynthesizer_Altium = 'Altium Synthesizer'
cVHDLSynthesizer_nVisage = 'nVisage Synthesizer'
cVHDLSynthesizer_Quartus = 'Altera Quartus II'
cVHDLSynthesizer_Synplicity = 'Synplicity'
cVHDLSynthesizer_SynplicityForActel = 'Synplicity For Actel'
cVHDLSynthesizer_SynplicityForLattice = 'Synplicity For Lattice'
cVHDLSynthesizer_XST = 'XST Synthesizer'
cVHDTSTExt = 'VHDTST'
cViewNameParam = 'ViewName'
cViewNotification = 'altium.dxp.view'
cVQMExt = 'VQM'
cWatchNotification = 'altium.dxp.watch'
cWaveRadius = 400000
cWaveSimNotification = 'altium.dxp.wavesim'
cWebAppHostRefreshSceneCategory = 28
cWebAppsPreferencesChanged = 21
cWebBrowserLocationChange = 0
cWebBrowserNotification = 'altium.dxp.webbrowser'
cWidthRuleLayers = [1..32]
cWindowKindHarnessLayoutDrawing = 4
cWindowKindHarnessWiringDiagram = 3
cWindowKindSch_First = 1
cWindowKindSch_Last = 4
cWindowKindSchematic = 1
cWindowKindSchematicLibrary = 2
cWireObjectsSet = [19..20, 56, 82, 86]
cWishboneProbeInstrumentDeviceName = 'WB_PROBE'
cWishboneProbeInstrumentFamilyDescription = 'Wishbone Probe Instrument Modules'
cWishboneProbeInstrumentFamilyName = 'WB_PROBE'
cXilinxProgram_Build = 'NGDBuild'
cXilinxProgram_CoreGen = 'wincoregen'
cXilinxProgram_Fit = 'CpldFit'
cXilinxProgram_Flow = 'xflow'
cXilinxProgram_GenerateJedec = 'hprep6'
cXilinxProgram_GenerateProgrammingFile = 'Bitgen'
cXilinxProgram_GeneratePromFile = 'PromGen'
cXilinxProgram_GenerateSerialVectorFile = 'Impact'
cXilinxProgram_Map = 'MAP'
cXilinxProgram_PlaceAndRoute = 'PAR'
cXilinxProgram_Trace = 'trce'
cXPPanelCloseBtn = 'XPCOLLAPSECLOSE'
cXPPanelExpandBtn = 'XPCOLLAPSEEXPAND'
cXPPanelExpandBtnHorz = 'XPCOLLAPSEEXPANDHORZ'
cXPPanelPlusMinusBtn = 'XPBUTTONPLUSMINUS'
cXPPanelXPCloseBtn = 'XPBUTTONCLOSE'
cZeroSizeLineSmallTolerance = 100000
cZIPExt = 'ZIP'

### D

DateDelta = 693594
DayFriday = 5
DayMonday = 1
DaySaturday = 6
DaysPerWeek = 7
DaySunday = 7
DayThursday = 4
DayTuesday = 2
DayWednesday = 3
dcEnabled = 1
dcSupported = 0
DEFAULT_COPPER_COMPARISION_TOLERANCE = 100000000.0
DEFAULT_LIBRARY_EXTENSION = 'LIB'
DefaultCategoryPanelHeight = 200
DefaultExceptionFlags = [0, 2..3]
DefaultFalseBoolStr = 'False'
DefaultFieldRttiVisibility = [0..3]
DefaultFileName = '*.*'
DefaultMethodRttiVisibility = [2..3]
DefaultPartId = 1
DefaultPropertyRttiVisibility = [2..3]
DefaultRouteGuideLayerName = 'Route Guide'
DefaultRouteGuideMechanicalLayer = 32767
Delimiter = [0, 9..10, 13, 32, 39..41, 44]
dibfAddNoise = 3
dibfBacklighted = 1
dibfDisabled = 2
dibfHorzGradient = 4
dibfPressed = 0
DIELECTRIC_LAYER_FAMILY = 2
DIELECTRIC_LAYER_FLAGS = 513
DielectricLayerTypeId = '{56EB1CA5-014A-4387-A43E-1485F44F081E}'
DigitSet = [45..46, 48..57]
dirDown = 3
DirectiveObjectsSet = [3, 28, 35]
dirLeft = 0
dirUp = 1
DM_GETDEFID = 1024
DM_REPOSITION = 1026
DM_SETDEFID = 1025
DOCHOSTUIDBLCLK_DEFAULT = 0
DOCHOSTUIDBLCLK_SHOWCODE = 2
DOCHOSTUIDBLCLK_SHOWPROPERTIES = 1
DOCHOSTUIFLAG_ACTIVATE_CLIENTHIT_ONLY = 512
DOCHOSTUIFLAG_DIALOG = 1
DOCHOSTUIFLAG_DISABLE_HELP_MENU = 2
DOCHOSTUIFLAG_DISABLE_OFFSCREEN = 64
DOCHOSTUIFLAG_DISABLE_SCRIPT_INACTIVE = 16
DOCHOSTUIFLAG_DIV_BLOCKDEFAULT = 256
DOCHOSTUIFLAG_FLAT_SCROLLBAR = 128
DOCHOSTUIFLAG_NO3DBORDER = 4
DOCHOSTUIFLAG_OPENNEWWIN = 32
DOCHOSTUIFLAG_SCROLL_NO = 8
doDrawFocusRect = 0
doShiftContentIfPressed = 2
doShowAccelChar = 1
doSunkenDisabled = 3
dpoDrawSeparator = 0
dpoGroupDigits = 1
dpoLeadingZeros = 2
drAbort = 3
drAll = 12
drCancel = 2
drClose = 8
drContinue = 11
drHelp = 9
drIgnore = 5
DriveDelim = ':'
drNo = 7
drNone = 0
drNoToAll = 13
drOk = 1
drRetry = 4
drTryAgain = 10
drYes = 6
drYesToAll = 14
dsEditModes = [2..4]
dsMaxStringSize = 8192
dsWriteModes = [2..7, 11]
dtsAllLayerPairsInOneTable = 1
dtsAllLayerPairsInSeparateTables = 2
dtsSelectedLayerPairOnly = 0

### E

e10m = 6
e12m = 7
e14m = 8
e15m = 16
e16m = 9
e17m = 10
e18m = 11
e20m = 12
e21m = 17
e24m = 13
e25m = 18
e2m = 0
e33m = 19
e35m = 20
e3_5m = 14
e3m = 1
e4m = 2
e5m = 15
e6m = 3
e7m = 4
e8m = 5
E_NOINTERFACE = -2147467262
E_NOTIMPL = -2147467263
E_UNEXPECTED = -2147418113
eAddString = 1
eAllComponents = 0
eAltiumJsonSchematicFile_v50 = 9
eAltiumJsonSchematicLibraryFile_v50 = 10
eAnyCase = 2
eAutoGeneratedClass_ComponentBottomSide = 1
eAutoGeneratedClass_ComponentInsideBoard = 2
eAutoGeneratedClass_ComponentOutsideBoard = 3
eAutoGeneratedClass_ComponentTopSide = 0
eAutoWire = 7
eBackGroundLayer = 76
eBareBoardFabrication = 0
eBJT = 0
eBottom = 1
eBottomAlign = 2
eBottomLayer = 32
eBottomLayerPlot = 32
eBottomOnly = 2
eBottomOverlay = 34
eBottomOverlayPlot = 34
eBottomPadMasterPlot = 109
eBottomPaste = 36
eBottomPastePlot = 36
eBottomSignalLayer = 16
eBottomSolder = 38
eBottomSolderPlot = 38
eBreakSegment = 2
eBrowserAll = 0
eBrowserBus = 2
eBrowserBusEntry = 1
eBrowserComponentParameters = 11
eBrowserComponents = 10
eBrowserErrorMarker = 3
eBrowserHierarchyNets = 18
eBrowserImage = 4
eBrowserJunction = 5
eBrowserLabel = 6
eBrowserLibRef = 9
eBrowserNetIdentifiers = 7
eBrowserNetLabel = 8
eBrowserNoERC = 24
eBrowserParameters = 14
eBrowserParameterSets = 15
eBrowserPins = 17
eBrowserPinsAndParts = 16
eBrowserPort = 19
eBrowserPortParameters = 13
eBrowserPowerObject = 20
eBrowserSheetEntry = 21
eBrowserSheetFileName = 23
eBrowserSheetSymbol = 22
eBrowserSheetSymbolParameters = 12
eBrowserTextFrame = 25
eBrowserWire = 26
eCapactitor = 1
eCentreAlign = 1
eChangeAllFreePrimitives = 3
eChangeAllPrimitives = 2
eChangeCancelled = 7
eChangeComponentComments = 5
eChangeComponentDesignators = 4
eChangeLibraryAllComponents = 6
eChangeNone = 0
eChangeThisItem = 1
eChooseDocument_AllOpen = 0
eChooseDocument_ProjectAndDeviceDocuments = 2
eChooseDocument_ProjectDocuments = 1
eCircuitStudioBinarySchematicFile_v50 = 8
eClientEvent_GarbageCollect = 0
eClkDiffN_Pin = 14
eClkDiffP_Pin = 13
eCLKPin = 2
eCoarse2 = 1
eCoarse3 = 2
eCommercial = 0
eCompBlock = 0
eCompDevice = 1
eCompile_All = 2
eCompile_Document = 1
eCompile_None = 0
eCompile_Smart = 3
eComponentSearchScopeAllDrives = 2
eComponentSearchScopeListedLibraries = 1
eComponentSearchScopeSpecifiedPath = 0
eComponentStyle_BGA = 9
eComponentStyle_DIP = 4
eComponentStyle_Edge = 3
eComponentStyle_LCC = 8
eComponentStyle_PGA = 10
eComponentStyle_SIP = 5
eComponentStyle_Small = 1
eComponentStyle_SmallSMT = 2
eComponentStyle_SMDIP = 7
eComponentStyle_SMSIP = 6
eComponentStyle_Unknown = 0
eCompPower = 2
eCompSymbol = 3
eConnectionNode_Hidden = 2
eConnectionNode_InterSheetLink = 1
eConnectionNode_IntraSheetLink = 0
eConnectivity_ConnectionOnly = 0
eConnectivity_WholeNet = 1
eConnectLayer = 75
eConnector = 2
eConnectorKind_Arrow = 1
eConnectorKind_Poly = 0
eConnectorKind_Round = 2
eConnectorState_Female = 2
eConnectorState_Male = 1
eConnectorState_Unknown = 0
eCornerChamfered = 1
eCornerRounded = 0
eCreateForm = 0
eCurrentMDIChild = 1
eCursorBottom = 3
eCursorLeft = 0
eCursorRight = 1
eCursorTop = 2
eDCIN_Pin = 6
eDCIP_Pin = 5
eDeviceProcessor_BYTE_ORDER_BIG_ENDIAN = 1
eDeviceProcessor_BYTE_ORDER_LITTLE_ENDIAN = 0
eDeviceProcessor_TYPE_GENERIC = 3
eDeviceProcessor_TYPE_HARD = 1
eDeviceProcessor_TYPE_SOFT = 2
eDeviceProcessor_TYPE_UNKNOWN = 0
eDifferenceGroup_ClassCluster = 4
eDifferenceGroup_Component = 0
eDifferenceGroup_Net = 1
eDifferenceGroup_Parameter = 2
eDifferenceGroup_Physical = 3
eDifferenceGroup_SystemLevel = 5
eDiffN_Pin = 8
eDiffP_Pin = 7
eDiode = 3
eDir_E = 2
eDir_N = 0
eDir_NE = 1
eDir_NW = 7
eDir_S = 4
eDir_SE = 3
eDir_SW = 5
eDir_W = 6
eDisplayDRC = 3
eDisplayFocused = 4
eDisplayHollow = 1
eDisplayHollowDashed = 6
eDisplayHollowHatched = 7
eDisplayMultiFocused = 5
eDisplaySelected = 2
eDisplaySolid = 0
eDLL_Pin = 15
eDraftQuality = 1
eDrawUse = 2
eDRCErrorLayer = 77
eDrillDrawing = 73
eDrillDrawing_Mid10_Mid11Plot = 96
eDrillDrawing_Mid12_Mid13Plot = 97
eDrillDrawing_Mid14_Mid15Plot = 98
eDrillDrawing_Mid16_Mid17Plot = 99
eDrillDrawing_Mid18_Mid19Plot = 100
eDrillDrawing_Mid20_Mid21Plot = 101
eDrillDrawing_Mid22_Mid23Plot = 102
eDrillDrawing_Mid24_Mid25Plot = 103
eDrillDrawing_Mid26_Mid27Plot = 104
eDrillDrawing_Mid28_Mid29Plot = 105
eDrillDrawing_Mid2_Mid3Plot = 92
eDrillDrawing_Mid30_BottomPlot = 106
eDrillDrawing_Mid4_Mid5Plot = 93
eDrillDrawing_Mid6_Mid7Plot = 94
eDrillDrawing_Mid8_Mid9Plot = 95
eDrillDrawing_SpecialPlot = 107
eDrillDrawing_Top_BottomPlot = 90
eDrillDrawing_Top_Mid1Plot = 91
eDrillGuide = 55
eDrillGuide_Mid10_Mid11Plot = 61
eDrillGuide_Mid12_Mid13Plot = 62
eDrillGuide_Mid14_Mid15Plot = 63
eDrillGuide_Mid16_Mid17Plot = 64
eDrillGuide_Mid18_Mid19Plot = 65
eDrillGuide_Mid20_Mid21Plot = 66
eDrillGuide_Mid22_Mid23Plot = 67
eDrillGuide_Mid24_Mid25Plot = 68
eDrillGuide_Mid26_Mid27Plot = 69
eDrillGuide_Mid28_Mid29Plot = 70
eDrillGuide_Mid2_Mid3Plot = 57
eDrillGuide_Mid30_BottomPlot = 71
eDrillGuide_Mid4_Mid5Plot = 58
eDrillGuide_Mid6_Mid7Plot = 59
eDrillGuide_Mid8_Mid9Plot = 60
eDrillGuide_SpecialPlot = 72
eDrillGuide_Top_BottomPlot = 55
eDrillGuide_Top_Mid1Plot = 56
eDropAction_AskOpenOrInsertText = 1
eDropAction_Insert = 5
eDropAction_None = 0
eDropAction_OpenAsText = 4
eDropAction_OpenInEditor = 3
eDropAction_WarnBinaryAsText = 2
eDXPPreset = 0
eDXPrimitive_DisplayDimm = 1
eDXPrimitive_DisplayDimmTransparent = 8
eDXPrimitive_DisplayGrayScale = 4
eDXPrimitive_DisplayGrayScaleTransparent = 6
eDXPrimitive_DisplayHighlight = 2
eDXPrimitive_DisplayHighlightTransparent = 9
eDXPrimitive_DisplayMonochrome = 5
eDXPrimitive_DisplayMonochromeTRansparent = 7
eDXPrimitive_DisplayNormal = 0
eDXPrimitive_DisplayTransparent = 3
eEdifOptimizationArea = 1
eEdifOptimizationSpeed = 0
eEditAction_DontCare = 0
eElectrical = 5
eExitState_CtrlRolledOut = 2
eExitState_RolledOut = 1
eExitState_Started = 4
eExitState_Success = 3
eExitState_UserAbort = 0
eFast = 1
eFindReplace_AllIdentifiers = 0
eFindReplace_AllObjects = 2
eFindReplace_CurrentDocument = 0
eFindReplace_DeSelectedObjects = 1
eFindReplace_DesignatorsOnly = 2
eFindReplace_NetIdentifiersOnly = 1
eFindReplace_OpenDocuments = 2
eFindReplace_ProjectDocuments = 1
eFindReplace_ProjectPhysicalDocuments = 3
eFindReplace_SelectedObjects = 0
eFine2 = 3
eFine3 = 4
eFlashUse = 3
eFloatingPointType_Double = 1
eFloatingPointType_Single = 0
eFR_OpenPrimDefaultFile = 1
eFR_SavePrimDefaultFile = 0
eFreePads = 4
eFullQuality = 0
eGridColor1 = 79
eGridColor10 = 80
eHDiffN_Pin = 10
eHDiffP_Pin = 9
eHealthCheckScopeAll = 0
eHealthCheckScopeFabricationOutput = 2
eHealthCheckScopePCBLoading = 1
eHide = 1
eHighLevelCodeBusMode_ByteAddressing = 0
eHighLevelCodeBusMode_WordAddressing = 1
eHighLight = 4
eHighlightLayer = 78
eHorizontal = 0
eIC = 4
eIgnoreLayer = 0
eImportModeAdd = 0
eImportModeUpdate = 1
eImportModeUpdateAdd = 2
eInCircuitAssembly = 1
eInductor = 5
eIndustrial = 1
eInner = 0
eInnerEdge = 1
eInputOnlyPin = 4
eInsertVertex = 1
eInternalPlane1 = 39
eInternalPlane10 = 48
eInternalPlane10Plot = 48
eInternalPlane11 = 49
eInternalPlane11Plot = 49
eInternalPlane12 = 50
eInternalPlane12Plot = 50
eInternalPlane13 = 51
eInternalPlane13Plot = 51
eInternalPlane14 = 52
eInternalPlane14Plot = 52
eInternalPlane15 = 53
eInternalPlane15Plot = 53
eInternalPlane16 = 54
eInternalPlane16Plot = 54
eInternalPlane1Plot = 39
eInternalPlane2 = 40
eInternalPlane2Plot = 40
eInternalPlane3 = 41
eInternalPlane3Plot = 41
eInternalPlane4 = 42
eInternalPlane4Plot = 42
eInternalPlane5 = 43
eInternalPlane5Plot = 43
eInternalPlane6 = 44
eInternalPlane6Plot = 44
eInternalPlane7 = 45
eInternalPlane7Plot = 45
eInternalPlane8 = 46
eInternalPlane8Plot = 46
eInternalPlane9 = 47
eInternalPlane9Plot = 47
eInvert = 3
eIOPin = 0
eKeepOutLayer = 56
eKeepOutLayerPlot = 73
eKillVertex = 5
ELECTRICAL_LAYER_FAMILY = 1
eLeft = 0
eLibEditGlobalEditScopeAllLibraries = 2
eLibEditGlobalEditScopeCurrentComponent = 0
eLibEditGlobalEditScopeCurrentLibrary = 1
eLifecycleStatus_EOL = 4
eLifecycleStatus_New = 1
eLifecycleStatus_NRND = 3
eLifecycleStatus_Obsolete = 5
eLifecycleStatus_Production = 2
eLifecycleStatus_Unknown = 0
eLine45End = 4
eLine45Start = 3
eLine90End = 2
eLine90Start = 1
eLineAnyAngle = 0
eLineArcEnd = 6
eLineArcStart = 5
eLoginOption_ErrorsInTitleBar = 2
eLoginOption_HideSigninDialog = 3
eLoginOption_NoDialogs = 0
eLoginOption_PrivateServer = 5
eLoginOption_ShowSignInDialog = 4
eLoginOption_UseCachedUserNameAndPassword = 1
eLowerCase = 1
EM_CANUNDO = 198
EM_CHARFROMPOS = 215
EM_EMPTYUNDOBUFFER = 205
EM_EXLINEFROMCHAR = 1078
EM_FMTLINES = 200
EM_GETFIRSTVISIBLELINE = 206
EM_GETHANDLE = 189
EM_GETIMESTATUS = 217
EM_GETLIMITTEXT = 213
EM_GETLINE = 196
EM_GETLINECOUNT = 186
EM_GETMARGINS = 212
EM_GETMODIFY = 184
EM_GETPASSWORDCHAR = 210
EM_GETRECT = 178
EM_GETSEL = 176
EM_GETTHUMB = 190
EM_GETWORDBREAKPROC = 209
EM_LIMITTEXT = 197
EM_LINEFROMCHAR = 201
EM_LINEINDEX = 187
EM_LINELENGTH = 193
EM_LINESCROLL = 182
EM_POSFROMCHAR = 214
EM_REPLACESEL = 194
EM_SCROLL = 181
EM_SCROLLCARET = 183
EM_SETHANDLE = 188
EM_SETIMESTATUS = 216
EM_SETLIMITTEXT = 197
EM_SETMARGINS = 211
EM_SETMODIFY = 185
EM_SETPASSWORDCHAR = 204
EM_SETREADONLY = 207
EM_SETRECT = 179
EM_SETRECTNP = 180
EM_SETSEL = 177
EM_SETTABSTOPS = 203
EM_SETWORDBREAKPROC = 208
EM_UNDO = 199
eMainWindow = 0
eManufactureMode = 2
emAssembly = 0
eMatchAnySelection = 2
eMatchedNotSelected = 1
eMatchSelected = 0
eMechanical1 = 57
eMechanical10 = 66
eMechanical10Plot = 83
eMechanical11 = 67
eMechanical11Plot = 84
eMechanical12 = 68
eMechanical12Plot = 85
eMechanical13 = 69
eMechanical13Plot = 86
eMechanical14 = 70
eMechanical14Plot = 87
eMechanical15 = 71
eMechanical15Plot = 88
eMechanical16 = 72
eMechanical16Plot = 89
eMechanical1Plot = 74
eMechanical2 = 58
eMechanical2Plot = 75
eMechanical3 = 59
eMechanical3Plot = 76
eMechanical4 = 60
eMechanical4Plot = 77
eMechanical5 = 61
eMechanical5Plot = 78
eMechanical6 = 62
eMechanical6Plot = 79
eMechanical7 = 63
eMechanical7Plot = 80
eMechanical8 = 64
eMechanical8Plot = 81
eMechanical9 = 65
eMechanical9Plot = 82
eMidLayer1 = 2
eMidLayer10 = 11
eMidLayer10Plot = 11
eMidLayer11 = 12
eMidLayer11Plot = 12
eMidLayer12 = 13
eMidLayer12Plot = 13
eMidLayer13 = 14
eMidLayer13Plot = 14
eMidLayer14 = 15
eMidLayer14Plot = 15
eMidLayer15 = 16
eMidLayer15Plot = 16
eMidLayer16 = 17
eMidLayer16Plot = 17
eMidLayer17 = 18
eMidLayer17Plot = 18
eMidLayer18 = 19
eMidLayer18Plot = 19
eMidLayer19 = 20
eMidLayer19Plot = 20
eMidLayer1Plot = 2
eMidLayer2 = 3
eMidLayer20 = 21
eMidLayer20Plot = 21
eMidLayer21 = 22
eMidLayer21Plot = 22
eMidLayer22 = 23
eMidLayer22Plot = 23
eMidLayer23 = 24
eMidLayer23Plot = 24
eMidLayer24 = 25
eMidLayer24Plot = 25
eMidLayer25 = 26
eMidLayer25Plot = 26
eMidLayer26 = 27
eMidLayer26Plot = 27
eMidLayer27 = 28
eMidLayer27Plot = 28
eMidLayer28 = 29
eMidLayer28Plot = 29
eMidLayer29 = 30
eMidLayer29Plot = 30
eMidLayer2Plot = 3
eMidLayer3 = 4
eMidLayer30 = 31
eMidLayer30Plot = 31
eMidLayer3Plot = 4
eMidLayer4 = 5
eMidLayer4Plot = 5
eMidLayer5 = 6
eMidLayer5Plot = 6
eMidLayer6 = 7
eMidLayer6Plot = 7
eMidLayer7 = 8
eMidLayer7Plot = 8
eMidLayer8 = 9
eMidLayer8Plot = 9
eMidLayer9 = 10
eMidLayer9Plot = 10
eMidSignalLayer1 = 2
eMidSignalLayer10 = 11
eMidSignalLayer11 = 12
eMidSignalLayer12 = 13
eMidSignalLayer13 = 14
eMidSignalLayer14 = 15
eMidSignalLayer2 = 3
eMidSignalLayer3 = 4
eMidSignalLayer4 = 5
eMidSignalLayer5 = 6
eMidSignalLayer6 = 7
eMidSignalLayer7 = 8
eMidSignalLayer8 = 9
eMidSignalLayer9 = 10
eMouseMode_ClickAndHold = 2
eMouseMode_ClickDown = 1
eMouseMode_ClickUp = 3
eMouseMode_None = 0
eMoveSegment = 4
eMoveVertex = 0
emPart = 1
EmptyString = ''
eMultiLayer = 74
eMultiSignalLayer = 17
eMultiUse = 1
EN_CHANGE = 768
EN_ERRSPACE = 1280
EN_HSCROLL = 1537
EN_KILLFOCUS = 512
EN_MAXTEXT = 1281
EN_SETFOCUS = 256
EN_UPDATE = 1024
EN_VSCROLL = 1538
eNetlistRunActionAnalogSimulator = 1
eNetlistRunActionDigitalSimulator = 2
eNetlistRunActionMixedSignalSimulator = 3
eNetlistRunActionNone = 0
eNoApertureUse = 0
eNoLayer = 0
eNoneAlign = 0
eNormalMode = 0
eNoSignalLayer = 0
EntryContainerObjectSet = [41, 53]
EntryObjectsSet = [40, 54]
eNullPlot = 0
eObjectAttribute_Accessible = 39
eObjectAttribute_Alignment = 34
eObjectAttribute_AreaColor = 4
eObjectAttribute_ArrowKind = 143
eObjectAttribute_Author = 125
eObjectAttribute_AutoSize = 11
eObjectAttribute_BorderColor = 175
eObjectAttribute_BorderWidth = 35
eObjectAttribute_BundleToGoThroughAssignments = 176
eObjectAttribute_BusTextStyle = 142
eObjectAttribute_CodeEntryName = 149
eObjectAttribute_CodeSymbolExportedRoutineName = 148
eObjectAttribute_Collapsed = 126
eObjectAttribute_Color = 2
eObjectAttribute_ConnectionPointConnectorsAssignment = 177
eObjectAttribute_CornerLocationX = 7
eObjectAttribute_CornerLocationY = 8
eObjectAttribute_CrossSheetConnectorStyle = 98
eObjectAttribute_DatabaseTableName = 133
eObjectAttribute_Description = 42
eObjectAttribute_DesignatorLocked = 45
eObjectAttribute_DesignItemID = 136
eObjectAttribute_DocumentName = 1
eObjectAttribute_EndAngle = 18
eObjectAttribute_EndLineShape = 24
eObjectAttribute_ErrorKind = 127
eObjectAttribute_FileName = 48
eObjectAttribute_FileNameRTF = 49
eObjectAttribute_Font = 28
eObjectAttribute_FontId = 27
eObjectAttribute_FSMStateAction = 167
eObjectAttribute_FSMStateDefault = 168
eObjectAttribute_FSMStateShape = 163
eObjectAttribute_FSMTransitionCondition = 169
eObjectAttribute_FSMTransitionFromState = 165
eObjectAttribute_FSMTransitionShape = 164
eObjectAttribute_FSMTransitionToState = 166
eObjectAttribute_HarnessConnectionPointStyle = 173
eObjectAttribute_HarnessConnectorSide = 139
eObjectAttribute_HarnessShieldStyle = 172
eObjectAttribute_HarnessSpliceStyle = 174
eObjectAttribute_HarnessType = 140
eObjectAttribute_Height = 13
eObjectAttribute_HideHarnessConnectorType = 141
eObjectAttribute_HorizontalJustification = 30
eObjectAttribute_IeeeSymbol = 116
eObjectAttribute_ImageEmbed = 52
eObjectAttribute_ImageKeepAspect = 51
eObjectAttribute_IsHidden = 26
eObjectAttribute_IsMirrored = 44
eObjectAttribute_Item = 153
eObjectAttribute_JunctionSize = 37
eObjectAttribute_Length = 178
eObjectAttribute_LineShapeSize = 25
eObjectAttribute_LineStyle = 22
eObjectAttribute_LineWidth = 36
eObjectAttribute_LocationX = 5
eObjectAttribute_LocationY = 6
eObjectAttribute_Locked = 38
eObjectAttribute_LongStringText = 21
eObjectAttribute_Name = 40
eObjectAttribute_NoERCActive = 159
eObjectAttribute_NoERCSymbol = 160
eObjectAttribute_ObjectId = 0
eObjectAttribute_OpenBusComponentInterfaceType = 150
eObjectAttribute_OpenBusComponentKind = 137
eObjectAttribute_OpenBusLinkMasterPort = 146
eObjectAttribute_OpenBusLinkSlavePort = 147
eObjectAttribute_OpenBusPortLink = 145
eObjectAttribute_OpenBusPortType = 144
eObjectAttribute_Orientation = 29
eObjectAttribute_OwnerName = 41
eObjectAttribute_OwnerPartDisplayMode = 10
eObjectAttribute_OwnerPartId = 9
eObjectAttribute_ParameterAllowDatabaseSynchronize = 59
eObjectAttribute_ParameterAllowLibrarySynchronize = 58
eObjectAttribute_ParameterName = 55
eObjectAttribute_ParameterReadOnlyState = 57
eObjectAttribute_ParameterSetStyle = 151
eObjectAttribute_ParametersList = 53
eObjectAttribute_ParameterType = 56
eObjectAttribute_ParameterValue = 54
eObjectAttribute_PartIdLocked = 46
eObjectAttribute_PinDefaultValue = 63
eObjectAttribute_PinDesignator = 64
eObjectAttribute_PinDesignator_CustomColor = 91
eObjectAttribute_PinDesignator_CustomFont = 90
eObjectAttribute_PinDesignator_CustomFontID = 89
eObjectAttribute_PinDesignator_CustomPosition_Margin = 85
eObjectAttribute_PinDesignator_CustomPosition_RotationAnchor = 87
eObjectAttribute_PinDesignator_CustomPosition_RotationRelative = 86
eObjectAttribute_PinDesignator_FontMode = 88
eObjectAttribute_PinDesignator_PositionMode = 84
eObjectAttribute_PinElectrical = 67
eObjectAttribute_PinFormalType = 62
eObjectAttribute_PinFunctions_Defined = 93
eObjectAttribute_PinFunctions_Selected = 92
eObjectAttribute_PinHiddenNetName = 65
eObjectAttribute_PinIeeeSymbolInner = 69
eObjectAttribute_PinIeeeSymbolInnerEdge = 71
eObjectAttribute_PinIeeeSymbolLineWidth = 162
eObjectAttribute_PinIeeeSymbolOuter = 70
eObjectAttribute_PinIeeeSymbolOuterEdge = 72
eObjectAttribute_PinLength = 68
eObjectAttribute_PinName_CustomColor = 83
eObjectAttribute_PinName_CustomFont = 82
eObjectAttribute_PinName_CustomFontID = 81
eObjectAttribute_PinName_CustomPosition_Margin = 77
eObjectAttribute_PinName_CustomPosition_RotationAnchor = 79
eObjectAttribute_PinName_CustomPosition_RotationRelative = 78
eObjectAttribute_PinName_FontMode = 80
eObjectAttribute_PinName_PositionMode = 76
eObjectAttribute_PinPackageLength = 170
eObjectAttribute_PinPropagationDelay = 171
eObjectAttribute_PinShowDesignator = 66
eObjectAttribute_PinsMoveable = 47
eObjectAttribute_PinSwapId_Part = 74
eObjectAttribute_PinSwapId_PartPin = 75
eObjectAttribute_PinSwapId_Pin = 73
eObjectAttribute_PinWidth = 61
eObjectAttribute_PortArrowStyle = 94
eObjectAttribute_PortIOType = 95
eObjectAttribute_PowerObjectShowNetName = 97
eObjectAttribute_PowerObjectStyle = 96
eobjectAttribute_PrimaryConnectionPosition = 138
eObjectAttribute_Radius = 14
eObjectAttribute_Revision = 154
eObjectAttribute_RichTextStream = 124
eObjectAttribute_RoundRectangleCornerRadiusX = 99
eObjectAttribute_RoundRectangleCornerRadiusY = 100
eObjectAttribute_SchComponentComment = 106
eObjectAttribute_SchComponentDesignator = 103
eObjectAttribute_SchComponentDisplayMode = 104
eObjectAttribute_SchComponentFootprint = 107
eObjectAttribute_SchComponentKind = 108
eObjectAttribute_SchComponentLibraryName = 101
eObjectAttribute_SchComponentLibReference = 102
eObjectAttribute_SchComponentPartId = 105
eObjectAttribute_SchComponentUseDBTableName = 135
eObjectAttribute_SchComponentUseLibraryName = 134
eObjectAttribute_SecondaryRadius = 19
eObjectAttribute_SelectedVertex2_X = 130
eObjectAttribute_SelectedVertex2_Y = 131
eObjectAttribute_SelectedVertex_X = 128
eObjectAttribute_SelectedVertex_Y = 129
eObjectAttribute_SheetEntryDistanceFromTop = 115
eObjectAttribute_SheetEntrySide = 114
eObjectAttribute_SheetFileName = 112
eObjectAttribute_SheetName = 113
eObjectAttribute_ShowDesignator = 111
eObjectAttribute_ShowHiddenFields = 109
eObjectAttribute_ShowHiddenPins = 110
eObjectAttribute_ShowName = 43
eObjectAttribute_Solid = 15
eObjectAttribute_StartAngle = 17
eObjectAttribute_StartLineShape = 23
eObjectAttribute_StringText = 20
eObjectAttribute_SuppressSpecific = 158
eObjectAttribute_SymbolItem = 156
eObjectAttribute_SymbolRevision = 157
eObjectAttribute_SymbolScaleFactor = 117
eObjectAttribute_SymbolVault = 155
eObjectAttribute_TargetFileName = 50
eObjectAttribute_TaskHolderConfiguration = 120
eObjectAttribute_TaskHolderInstanceName = 119
eObjectAttribute_TaskHolderProcess = 118
eObjectAttribute_TextAutoposition = 60
eObjectAttribute_TextColor = 3
eObjectAttribute_TextFrameClipToRect = 123
eObjectAttribute_TextFrameShowBorder = 122
eObjectAttribute_TextFrameWordWrap = 121
eObjectAttribute_TextHorizontalAnchor = 32
eObjectAttribute_TextVerticalAnchor = 33
eObjectAttribute_Transparent = 16
eObjectAttribute_UnionIndex = 132
eObjectAttribute_Url = 161
eObjectAttribute_Vault = 152
eObjectAttribute_VerticalJustification = 31
eObjectAttribute_Width = 12
eObjectPlacementSuccessfull = 2
eOptimize_Balanced = 0
eOptimize_Density = 2
eOptimize_Speed = 1
eOuter = 3
eOuterEdge = 2
eOverWrite = 0
ePadHoleLayer = 81
ePathAbsolute = 0
ePathRelative = 1
ePlaceEdge4590 = 1
ePlaceEdge45Arc90 = 3
ePlaceEdge9045 = 2
ePlaceEdge90Arc45 = 4
ePlaceEdge90Horz90Vert = 6
ePlaceEdge90HorzArc90Vert = 8
ePlaceEdge90Vert90Horz = 5
ePlaceEdge90VertArc90Horz = 7
ePlaceEdgeAny = 0
ePlacementMode_Multiple = 1
ePlacementMode_Single = 0
ePlacementProcessStarted = 3
EpochAsJulianDate = 2415018.5
EpochAsUnixDate = -2209161600
ePowerLayer1 = 18
ePowerLayer2 = 19
ePowerLayer3 = 20
ePowerLayer4 = 21
ePrintAllDocuments = 1
ePrinterColorModeColor = 0
ePrinterColorModeMonochrome = 1
ePrintRangeAll = 0
ePrintRangePages = 2
ePrintRangeSelected = 1
ePrintSingleDocument = 0
eProbeMethodAllNets = 0
eProbeMethodProbedNetsOnly = 1
eProtelAsciiSchematicFile_v40 = 1
eProtelAsciiSchematicFile_v50 = 2
eProtelAsciiSchematicLibraryFile = 5
eProtelBinarySchematicFile_v40 = 3
eProtelBinarySchematicFile_v50 = 4
eProtelBinarySchematicLibraryFile_v40 = 6
eProtelBinarySchematicLibraryFile_v50 = 7
eProtelDOSBinarySchematic = 0
epSelectedLeft = 0
epSelectedRight = 2
Epsilon = 9.99994610111476e-41
Epsilon2 = 1.0000000031710769e-30
epUnselectedLeft = 1
epUnselectedRight = 3
EqualsValue = 0
ERANGE = 1
eRecDiffPin = 12
eRectangleHollow = 0
eRectangleSolid = 1
eRefactorDeviceSymbol_Project = 1
eRefactorDeviceSymbol_Single = 0
eRefactorNormalSymbol_Project = 1
eRefactorNormalSymbol_Single = 0
eRefactorNormalSymbol_Workspace = 2
eReleaseLocation_GlobalRepository = 1
eReleaseLocation_ProjectFolder = 0
eReleaseLocation_VersionControlRepository = 2
eResistor = 6
eRight = 2
eRLLayerNotUsed = 0
eRLRoute_1_OClock = 4
eRLRoute_2_OClock = 5
eRLRoute_45_Down = 9
eRLRoute_45_Up = 8
eRLRoute_4_OClock = 6
eRLRoute_5_OClock = 7
eRLRouteAuto = 11
eRLRouteFanout = 10
eRLRouteHorizontal = 1
eRLRouteSingleLayer = 3
eRLRouteVertical = 2
ERROR_PART_NOT_FOUND = 1
eRuleObject_KeepOut = 7
eRunDialog = 2
eScope1 = 0
eScope2 = 1
eSearchModeCurrentDatabase = 0
eSearchModeMultipleDatabases = 2
eSearchModeSpecifiedDatabase = 1
eSearchModeWindowsFileSystem = 3
eSegmentToArc = 3
eSelectedComponents = 3
eSelectionState_FirstSelected = 1
eSelectionState_MultiSelected = 2
eSelectionState_None = 0
eSelectionState_VerticesSelected = 3
eSheetNumberMethod_Decrease = 1
eSheetNumberMethod_Increase = 0
eSheetNumberOrder_BreadthFirst = 2
eSheetNumberOrder_DepthFirst = 1
eSheetNumberOrder_Display = 0
eShow = 2
eShowLockedTexture_Always = 1
eShowLockedTexture_Never = 0
eShowLockedTexture_WhenHighlighting = 2
eSingleComponent = 0
eSingleObjectPlacementProcessAborted = 0
eSIS_HorizontalFirst = 1
eSIS_None = 0
eSIS_VerticalFirst = 2
eSlow = 0
eSnappingEntity_3DBodySnapPoints = 13
eSnappingEntity_ArcCenters = 15
eSnappingEntity_Axises = 0
eSnappingEntity_BoardShape = 11
eSnappingEntity_FootprintOrigins = 12
eSnappingEntity_Grids = 1
eSnappingEntity_Guides = 2
eSnappingEntity_Intersections = 5
eSnappingEntity_PadCenters = 6
eSnappingEntity_PadEdges = 8
eSnappingEntity_PadVertexes = 7
eSnappingEntity_RegionsPolygonsFills = 10
eSnappingEntity_Texts = 14
eSnappingEntity_TrackArcsLines = 4
eSnappingEntity_TrackArcsVertexes = 3
eSnappingEntity_ViaCenters = 9
eSortByAXThenAY = 0
eSortByAXThenDY = 1
eSortByAYThenAX = 2
eSortByDYThenAX = 3
eSortByName = 4
eSortOrder_Count_Size = 1
eSortOrder_Size_Count = 0
eSourceRelationship_AnalogIcOtherType = 31
eSourceRelationship_Capacitance = 4
eSourceRelationship_ClockFrequencyMax = 18
eSourceRelationship_ForwardCurrentMax = 29
eSourceRelationship_ForwardVoltageMax = 12
eSourceRelationship_ForwardVoltageMax1 = 28
eSourceRelationship_Inductance = 5
eSourceRelationship_LogicIcType = 17
eSourceRelationship_MaxFrequency = 25
eSourceRelationship_MaxInputVoltage = 22
eSourceRelationship_MaxOutputCurrent = 24
eSourceRelationship_MaxSupplyCurrent = 19
eSourceRelationship_MemoryType = 20
eSourceRelationship_Mount = 3
eSourceRelationship_NegativeTolerance = 7
eSourceRelationship_NominalInputVoltage = 27
eSourceRelationship_NumberOfFunctions = 13
eSourceRelationship_NumberOfWords = 21
eSourceRelationship_PackageCode = 10
eSourceRelationship_PinsNumber = 0
eSourceRelationship_PositiveTolerance = 8
eSourceRelationship_RatedCurrentMax = 9
eSourceRelationship_RatedPowerDissipation = 2
eSourceRelationship_Resistance = 1
eSourceRelationship_SensorsTransducersType = 30
eSourceRelationship_SeriesResistance = 11
eSourceRelationship_SizeCode = 6
eSourceRelationship_SupplyVoltageMax = 16
eSourceRelationship_SupplyVoltageMin = 15
eSourceRelationship_SupplyVoltageNom = 14
eSourceRelationship_SupplyVoltageNom1 = 26
eSourceRelationship_SwitchingFrequencyMax = 23
eSourceRelationship_TransitionFrequencyNom = 32
eSpecialPin = 3
eSRAvoidObstacle = 1
eSRIgnoreObstacle = 0
eSRPushObstacle = 3
eSRWalkAroundObstacle = 2
eSystemParameter_Address1 = 15
eSystemParameter_Address2 = 16
eSystemParameter_Address3 = 17
eSystemParameter_Address4 = 18
eSystemParameter_Application_BuildNumber = 31
eSystemParameter_ApprovedBy = 8
eSystemParameter_Author = 10
eSystemParameter_CheckedBy = 9
eSystemParameter_CompanyName = 11
eSystemParameter_ConfigurableComponent = 26
eSystemParameter_Configuratorname = 27
eSystemParameter_CurrentDate = 2
eSystemParameter_CurrentTime = 1
eSystemParameter_Date = 4
eSystemParameter_DocFullPath = 5
eSystemParameter_DocName = 6
eSystemParameter_DocNum = 20
eSystemParameter_DrawnBy = 12
eSystemParameter_Engineer = 13
eSystemParameter_ImagePath = 25
eSystemParameter_IsUserConfigurable = 29
eSystemParameter_ModifiedDate = 7
eSystemParameter_Organization = 14
eSystemParameter_PrjFolderVcsRevision = 32
eSystemParameter_ProjectName = 30
eSystemParameter_ProjFolderVcsRevisionShort = 36
eSystemParameter_Revision = 21
eSystemParameter_Rule = 24
eSystemParameter_SheetCount = 23
eSystemParameter_SheetNum = 22
eSystemParameter_SheetSymbolDesignator = 34
eSystemParameter_SimulationModelCache = 33
eSystemParameter_Time = 3
eSystemParameter_Title = 19
eSystemParameter_UserDefined = 0
eSystemParameter_VcsRevision = 28
eSystemParameter_VcsRevisionShort = 35
eTargetBoardKind_Altera = 2
eTargetBoardKind_BurchBoard = 5
eTargetBoardKind_NanoBoard_NB1_Rev1 = 3
eTargetBoardKind_NanoBoard_NB1_Rev2 = 4
eTargetBoardKind_Unknown = 0
eTargetBoardKind_Xilinx = 1
etFirstIsSel = 1
etFirstNotSel = 2
etLastIsSel = 3
etLastNotSel = 4
etNotSelToNotSel = 7
etNotSelToSel = 5
eTop = 3
eTopAlign = 1
eTopLayer = 1
eTopLayerPlot = 1
eTopOnly = 1
eTopOverlay = 33
eTopOverlayPlot = 33
eTopPadMasterPlot = 108
eTopPaste = 35
eTopPastePlot = 35
eTopSignalLayer = 1
eTopSolder = 37
eTopSolderPlot = 37
eTransDiffPin = 11
etSelToNotSel = 6
eTurn_ClockWise = 2
eTurn_CounterClockWise = 0
eTurn_None = 1
eUnknownFile = 11
eUpdateMode = 1
eUpperCase = 0
eV3_DirectToPwr1 = 2
eV3_DirectToPwr2 = 5
eV3_DirectToPwr3 = 8
eV3_DirectToPwr4 = 11
eV3_NoConnection = 0
eV3_ReliefToPwr1 = 1
eV3_ReliefToPwr2 = 4
eV3_ReliefToPwr3 = 7
eV3_ReliefToPwr4 = 10
eV3_TaggedToPwr1 = 3
eV3_TaggedToPwr2 = 6
eV3_TaggedToPwr3 = 9
eV3_TaggedToPwr4 = 12
eV6_IgnoreLayer = 0
eV7_BottomLayerPlot = 33
eV7_BottomOverlayPlot = 35
eV7_BottomPastePlot = 37
eV7_BottomSolderPlot = 39
eV7_DrillDrawing_SpecialPlot = 74
eV7_DrillGuide_SpecialPlot = 56
eV7_InternalPlane1 = 40
eV7_InternalPlane10 = 49
eV7_InternalPlane10Plot = 49
eV7_InternalPlane11 = 50
eV7_InternalPlane11Plot = 50
eV7_InternalPlane12 = 51
eV7_InternalPlane12Plot = 51
eV7_InternalPlane13 = 52
eV7_InternalPlane13Plot = 52
eV7_InternalPlane14 = 53
eV7_InternalPlane14Plot = 53
eV7_InternalPlane15 = 54
eV7_InternalPlane15Plot = 54
eV7_InternalPlane16 = 55
eV7_InternalPlane16Plot = 55
eV7_InternalPlane1Plot = 40
eV7_InternalPlane2 = 41
eV7_InternalPlane2Plot = 41
eV7_InternalPlane3 = 42
eV7_InternalPlane3Plot = 42
eV7_InternalPlane4 = 43
eV7_InternalPlane4Plot = 43
eV7_InternalPlane5 = 44
eV7_InternalPlane5Plot = 44
eV7_InternalPlane6 = 45
eV7_InternalPlane6Plot = 45
eV7_InternalPlane7 = 46
eV7_InternalPlane7Plot = 46
eV7_InternalPlane8 = 47
eV7_InternalPlane8Plot = 47
eV7_InternalPlane9 = 48
eV7_InternalPlane9Plot = 48
eV7_KeepOutLayerPlot = 57
eV7_Mechanical1 = 58
eV7_Mechanical10 = 67
eV7_Mechanical10Plot = 67
eV7_Mechanical11 = 68
eV7_Mechanical11Plot = 68
eV7_Mechanical12 = 69
eV7_Mechanical12Plot = 69
eV7_Mechanical13 = 70
eV7_Mechanical13Plot = 70
eV7_Mechanical14 = 71
eV7_Mechanical14Plot = 71
eV7_Mechanical15 = 72
eV7_Mechanical15Plot = 72
eV7_Mechanical16 = 73
eV7_Mechanical16Plot = 73
eV7_Mechanical1Plot = 58
eV7_Mechanical2 = 59
eV7_Mechanical2Plot = 59
eV7_Mechanical3 = 60
eV7_Mechanical3Plot = 60
eV7_Mechanical4 = 61
eV7_Mechanical4Plot = 61
eV7_Mechanical5 = 62
eV7_Mechanical5Plot = 62
eV7_Mechanical6 = 63
eV7_Mechanical6Plot = 63
eV7_Mechanical7 = 64
eV7_Mechanical7Plot = 64
eV7_Mechanical8 = 65
eV7_Mechanical8Plot = 65
eV7_Mechanical9 = 66
eV7_Mechanical9Plot = 66
eV7_MidLayer1 = 3
eV7_MidLayer10 = 12
eV7_MidLayer10Plot = 12
eV7_MidLayer11 = 13
eV7_MidLayer11Plot = 13
eV7_MidLayer12 = 14
eV7_MidLayer12Plot = 14
eV7_MidLayer13 = 15
eV7_MidLayer13Plot = 15
eV7_MidLayer14 = 16
eV7_MidLayer14Plot = 16
eV7_MidLayer15 = 17
eV7_MidLayer15Plot = 17
eV7_MidLayer16 = 18
eV7_MidLayer16Plot = 18
eV7_MidLayer17 = 19
eV7_MidLayer17Plot = 19
eV7_MidLayer18 = 20
eV7_MidLayer18Plot = 20
eV7_MidLayer19 = 21
eV7_MidLayer19Plot = 21
eV7_MidLayer1Plot = 3
eV7_MidLayer2 = 4
eV7_MidLayer20 = 22
eV7_MidLayer20Plot = 22
eV7_MidLayer21 = 23
eV7_MidLayer21Plot = 23
eV7_MidLayer22 = 24
eV7_MidLayer22Plot = 24
eV7_MidLayer23 = 25
eV7_MidLayer23Plot = 25
eV7_MidLayer24 = 26
eV7_MidLayer24Plot = 26
eV7_MidLayer25 = 27
eV7_MidLayer25Plot = 27
eV7_MidLayer26 = 28
eV7_MidLayer26Plot = 28
eV7_MidLayer27 = 29
eV7_MidLayer27Plot = 29
eV7_MidLayer28 = 30
eV7_MidLayer28Plot = 30
eV7_MidLayer29 = 31
eV7_MidLayer29Plot = 31
eV7_MidLayer2Plot = 4
eV7_MidLayer3 = 5
eV7_MidLayer30 = 32
eV7_MidLayer30Plot = 32
eV7_MidLayer3Plot = 5
eV7_MidLayer4 = 6
eV7_MidLayer4Plot = 6
eV7_MidLayer5 = 7
eV7_MidLayer5Plot = 7
eV7_MidLayer6 = 8
eV7_MidLayer6Plot = 8
eV7_MidLayer7 = 9
eV7_MidLayer7Plot = 9
eV7_MidLayer8 = 10
eV7_MidLayer8Plot = 10
eV7_MidLayer9 = 11
eV7_MidLayer9Plot = 11
eV7_NullPlot = 0
eV7_TopLayerPlot = 2
eV7_TopOverlayPlot = 34
eV7_TopPastePlot = 36
eV7_TopSolderPlot = 38
eVerilogModuleHeader = 0
eVerilogModuleItem = 2
eVerilogModuleParameter = 1
eVertexMove = 2
eVertexSlideToArc = 1
eVertexSlideToEdge = 0
eVertical = 1
eVerticalCentreAlign = 0
eVerySlow = 2
eVHDLArchDeclaration = 5
eVHDLArchHeader = 4
eVHDLArchStatement = 6
eVHDLEntityDeclaration = 2
eVHDLEntityGeneric = 1
eVHDLEntityHeader = 0
eVHDLEntityStatement = 3
eVHDLModelSimOnly = 1
eVHDLModelSimSynth = 0
eVHDLModelSynthOnly = 2
eViaHoleLayer = 82
eViewDrawDraft = 1
eViewDrawFull = 0
eViewDrawHidden = 2
eViewDrawMultiple = 3
eVREFPin = 1
eWholeLibrary = 1
eWholeObjectPlacementAborted = 1
eWholeProjectPanelize = 2
eWholeProjectSheetPerPage = 1
exAllArithmeticExceptions = [0..5]
ExcludeEmpty = 1
eXilinx_ISF_BaseBlockAddr = 5
eXilinx_ISF_BasePageAddr = 8
eXilinx_ISF_Blocks = 1
eXilinx_ISF_MaskMemSize = 9
eXilinx_ISF_PageSize = 6
eXilinx_ISF_PageSizeP2Mode = 7
eXilinx_ISF_PagesPerBlocks = 4
eXilinx_ISF_PagesPerSectors = 3
eXilinx_ISF_Sectors = 0
eXilinx_ISF_SectorsPerBitstream = 2
eXilinxConfigurationCommand_BeginStartupSequence = 6
eXilinxConfigurationCommand_ChangeCclkRequency = 1
eXilinxConfigurationCommand_LastFrameWrite = 5
eXilinxConfigurationCommand_ReadConfigurationData = 4
eXilinxConfigurationCommand_ResetCrcRegister = 0
eXilinxConfigurationCommand_SetAgHigh = 2
eXilinxConfigurationCommand_WriteConfigurationData = 3
eXilinxRegister_Command = 0
eXilinxRegister_ConfigurationOption = 2
eXilinxRegister_Control = 4
eXilinxRegister_ControlMask = 3
eXilinxRegister_CyclicRedundencyCheck = 7
eXilinxRegister_DaisyChainDataOut = 9
eXilinxRegister_FrameAddress = 5
eXilinxRegister_FrameDataInput = 6
eXilinxRegister_FrameDataOutput = 8
eXilinxRegister_FrameLength = 1
eXilinxRegister_Status = 10
EXTENDED_LAYER_FLAGS = 1
ExtendedColorsCount = 4

### F

faAnyFile = 511
faArchive = 32
faCompressed = 2048
faDirectory = 16
faEncrypted = 16384
faHidden = 2
faInvalid = -1
False = False
faNormal = 128
faReadOnly = 1
faSymLink = 1024
faSysFile = 4
faTemporary = 256
faVirtual = 65536
faVolumeID = 8
fe_AccessIsDenied = 5
fe_FileAccessCodeInvalid = 12
fe_FileNotFound = 2
fe_FunctionInvalid = 1
fe_NoAccessError = 0
fe_NoHandleIsAvalible = 4
fe_PathNotFoundOrFileDoesntExist = 3
feeALLEXCEPT = 63
feeDENORMALOPERAND = 2
feeDIVBYZERO = 4
feeINEXACT = 32
feeINVALID = 1
feeOVERFLOW = 8
feeUNDERFLOW = 16
femALLEXCEPT = 8064
femDENORMALOPERAND = 256
femDIVBYZERO = 512
femINEXACT = 4096
femINVALID = 128
femOVERFLOW = 1024
femUNDERFLOW = 2048
ferALLROUND = 24576
ferDOWNWARD = 8192
ferTONEAREST = 0
ferTOWARDZERO = 24576
ferUPWARD = 16384
FileExtension_Temp = '$$$'
FILTER_AVERAGE = 3
FILTER_NONE = 0
FILTER_PAETH = 4
FILTER_SUB = 1
FILTER_UP = 2
FirstObjectId = 1
fmAlternate = 0
fmClosed = 55216
fmCreate = 65280
fmExclusive = 4
fmInOut = 55219
fmInput = 55217
fmOpenRead = 0
fmOpenReadWrite = 2
fmOpenWrite = 1
fmOutput = 55218
fmShareCompat = 0
fmShareDenyNone = 64
fmShareDenyRead = 48
fmShareDenyWrite = 32
fmShareExclusive = 16
fmWinding = 1
FoilLayerTypeId = '{31E48829-E750-4C28-95E0-1A8313F0158E}'
FormFeed = #12
fsActivated = 5
fsCreatedMDIChild = 4
fsCreating = 0
FSMInsertSet = [2, 4..5, 8..15, 17..18, 21]
fsModal = 3
fsShowing = 2
fsVisible = 1
ftCalcFieldTypes = [1..13, 23..25, 35..38, 40..45, 49, 51]
ftFixedSizeTypes = [2..7, 9..11, 14, 25, 36, 42..45, 49, 51]
ftNonTextTypes = [4..5, 7..14, 18..21]

### G

gcnAdded = 1
gcnModified = 3
gcnRefreshAll = 0
gcnRemoved = 2
gdFixed = 2
gdFocused = 1
gdHotTrack = 4
gdoGradient = 1
gdoHotTrack = 0
gdPressed = 5
gdRowSelected = 3
gdSelected = 0
gnoCenterInView = 1
gnoMarkCenter = 0
goClockwise = 0
goInnerScale = 1
GreaterThanValue = 1
GripperSize = 20

### H

HandleObjectSet = [19, 24..25, 27, 35, 37..41, 46, 48, 54, 61]
HASHSIZE = 1024
HELP_CONTENTS = 3
HELP_HELPONHELP = 4
HELP_PARTIALKEY = 261
HexSet = [48..57, 65..70]
hfFieldSize = 8
hfMonitorOffset = 0
HoursPerDay = 24

### I

iboDrawBackground = 0
iboDrawBorder = 1
iboNoise = 2
igiBegin = 257
igiEnd = 258
igiFirst = 256
igiLast = 511
igiPan = 260
igiPressAndTap = 263
igiRotate = 261
igiTwoFingerTap = 262
igiZoom = 259
ImplementationsSet = [25, 27, 29, 44..47]
INFINITE = 4294967295
Infinity = inf
InitRepeatPause = 400
INTERNAL_PLANE_LAYER_FLAGS = 260
InternalPlanes = [7..22]
InternalUnits = 10000
INVALID_HANDLE_VALUE = ?
ipFirst = 0
ipLast = 1
IsolationLayerTypeId = '{92B02D5E-8D69-48A8-880E-AC4B77DB099D}'

### J

JTAG_Bypass = 15
JTAG_ExTest = 0
JTAG_IdCode = 1
JTAG_Memac = 10
JTAG_NexusEnable = 11
JTAG_Reset = 2

### K

k1Inch = 10000000
k1Mil = 10000
k1MilSq = 100000000.0
kACTELDesignerPathKey = 'Designer Path'
kActelInstallFile = 'install.def'
kACTELPathKey = 'Path'
kADMDirectory = 'adm\'
kBINDirectory = 'bin'
kDefaultArcResolution = 5000
kDegreeSymbol = ?
kDESIGNERProduct = 'Designer'
kDiameterSymbolANSI = ?
kDiameterSymbolUnicode = 'Φ'
kMaxCoord = 999990000
kMaxInternalPlane = 54
kMaxLongChar = 8192
kMaxPadName = 20
kMaxPlotterPens = 8
kMaxPolySize = 5000
kMaxStrokes = 2000
kMinCoord = 0
kMinInternalPlane = 39
kRegistryPath = '\Software\Actel\Libero'
kUnidentifiedPart = '$$$'

### L

LastObjectId = 22
lazCenter = 2
lazNoZoomChange = 0
lazRememberLast = 1
LB_ADDFILE = 406
LB_ADDSTRING = 384
LB_DELETESTRING = 386
LB_DIR = 397
LB_FINDSTRING = 399
LB_FINDSTRINGEXACT = 418
LB_GETANCHORINDEX = 413
LB_GETCARETINDEX = 415
LB_GETCOUNT = 395
LB_GETCURSEL = 392
LB_GETHORIZONTALEXTENT = 403
LB_GETITEMDATA = 409
LB_GETITEMHEIGHT = 417
LB_GETITEMRECT = 408
LB_GETLOCALE = 422
LB_GETSEL = 391
LB_GETSELCOUNT = 400
LB_GETSELITEMS = 401
LB_GETTEXT = 393
LB_GETTEXTLEN = 394
LB_GETTOPINDEX = 398
LB_INITSTORAGE = 424
LB_INSERTSTRING = 385
LB_ITEMFROMPOINT = 425
LB_MSGMAX = 435
LB_RESETCONTENT = 388
LB_SELECTSTRING = 396
LB_SELITEMRANGE = 411
LB_SELITEMRANGEEX = 387
LB_SETANCHORINDEX = 412
LB_SETCARETINDEX = 414
LB_SETCOLUMNWIDTH = 405
LB_SETCOUNT = 423
LB_SETCURSEL = 390
LB_SETHORIZONTALEXTENT = 404
LB_SETITEMDATA = 410
LB_SETITEMHEIGHT = 416
LB_SETLOCALE = 421
LB_SETSEL = 389
LB_SETTABSTOPS = 402
LB_SETTOPINDEX = 407
LBN_DBLCLK = 2
LBN_ERRSPACE = -2
LBN_KILLFOCUS = 5
LBN_SELCANCEL = 3
LBN_SELCHANGE = 1
LBN_SETFOCUS = 4
LdrPrimitiveSet = [2, 4..5, 8..11, 13..15, 17..18, 21..23, 25, 27, 81, 84..86, 88, 90..91, 95..97, 99]
LessThanValue = -1
LibEditorInsertSet = [4..5, 8..15, 17..18, 21..22, 28, 34, 37]
LibPrimitiveSet = [4..5, 8..15, 17..18, 21..23, 28, 34, 37]
LIBRARY_EXTENSION = 'AL'
LibraryVersion = '1.564'
LineFeed = #10
LineSeparator = ' '
Little = 1
loInvariantLocale = 0
loUserLocale = 1
lsmByName = 0
lsmByNumber = 1

### M

MASK_TF_COMPOSITED = 8388608
MAX_DIELECTRIC_LAYER = 65535
MAX_DONGLE_PRODUCT = 32
MAX_INTERNAL_PLANE_LAYER = 65535
MAX_INTERNAL_PLANE_LAYER_S09 = 16
MAX_MECHANICAL_LAYER = 65535
MAX_MECHANICAL_LAYER_LEGACY = 32
MAX_MECHANICAL_LAYER_UNLIM = 1024
MAX_MID_LAYER_S09 = 30
MAX_SIGNAL_LAYER = 65535
MAX_SIGNAL_LAYER_S09 = 32
MaxBoardLayer = 74
MaxComp = 9223372036854775807
MaxCurrency = 922337203685477.6
MaxCustomColors = 16
MaxCustomExtents = 134217727
MaxDateTime = 2958465.99999
MaxDispArgs = 64
MaxDouble = 1.7976931348623157e+308
MaxExtended = 1.7976931348623157e+308
MaxFreeStringLength = 254
MaxGridSize = 134217727
MaxLayer = 82
MaxListSize = 134217727
MaxLocationMarks = 10
MaxLogicalTextSize = 100000000
MaxMechanicalLayer = 72
MaxReferenceCount = 200
MaxRouteLayer = 32
MaxShortInt = 127
MaxSingle = 3.4028234663852886e+38
Maybe = 0
mbAbortIgnore = [4, 6]
mbAbortRetryIgnore = [4..6]
mbOKCancel = [2..3]
mbYesAllNoAllCancel = [0..1, 3, 8..9]
mbYesNo = [0..1]
mbYesNoCancel = [0..1, 3]
MECHANICAL_LAYER_FAMILY = 4
MECHANICAL_LAYER_FLAGS = 1024
MechanicalLayers = [1..16]
MechanicalTypeId = '{7A47E6B3-B591-41F7-A27B-8C6B0477E458}'
mgColored = 2
mgDisabled = 1
mgEnabled = 0
MID_LAYER_FLAGS = 258
MinComp = -9223372036854775807
MinCurrency = -922337203685477.6
MinDateTime = -657434.0
MinDouble = 5e-324
MinExtended = 5e-324
MinLayer = 1
MinMechanicalLayer = 57
MinSingle = 1.401298464324817e-45
MinsPerDay = 1440
MinsPerHour = 60
MISC_LAYER_FAMILY = 0
MonthApril = 4
MonthAugust = 8
MonthDecember = 12
MonthFebruary = 2
MonthJanuary = 1
MonthJuly = 7
MonthJune = 6
MonthMarch = 3
MonthMay = 5
MonthNovember = 11
MonthOctober = 10
MonthSeptember = 9
MonthsPerYear = 12
mrAbort = 3
mrAll = 12
mrCancel = 2
mrClose = 8
mrIgnore = 5
mrNo = 7
mrNone = 0
mrNoToAll = 13
mrOk = 1
mrRetry = 4
mrYes = 6
mrYesToAll = 14
msDBSetText = 2
MSecsPerDay = 86400000
MSecsPerSec = 1000
msMasked = 0
msReEnter = 1
MultiLayers = [0, 18]

### N

NaN = nan
ncrError = 0
ncrLoose = 2
ncrStrict = 1
ndt232bit = 4
ndt264bit = 5
ndt32bit = 2
ndt64bit = 3
ndtDefault = 0
ndtDefault2 = 1
NegativeValue = -1
NegInfinity = -inf
NetIdentifierObjectsSet = [24, 38..40, 48]
Nexus_Control_DebugAcknowledge = 8
Nexus_Control_DebugEnable = 16
Nexus_Control_DebuggerProgramSelect = 1
Nexus_Control_DebugRequest = 4
Nexus_Control_DebugStep = 2
Nexus_Control_ExternalAccess = 64
Nexus_Control_PeripheralClockEnable = 64
Nexus_Control_Reset = 32
Nexus_Control_StepCounterBreakpointEnable = 128
Nexus_MemAccess_Data = 0
Nexus_MemAccess_InActive = 0
Nexus_MemAccess_MemoryRead = 4
Nexus_MemAccess_MemoryWrite = 2
Nexus_MemAccess_Program = 1
Nexus_MemAccess_ReadData = 4
Nexus_MemAccess_ReadProgram = 5
Nexus_MemAccess_WriteData = 2
Nexus_MemAccess_WriteProgram = 3
ngDisabled = 1
ngEnabled = 0
No = 2
NoColorSelected = -16777216
nodeBINARY = 2
nodeCOMPARE = 3
nodeCONST = 5
nodeCONTINUE = 7
nodeFIELD = 4
nodeFUNC = 10
nodeLIST = 9
nodeLISTELEM = 11
nodeNULL = 0
nodeTUPLE = 6
nodeUDF = 8
nodeUNARY = 1
None = 0
nsAllowTimer = 0
nsCut = 0
nsDropHilited = 1
nsExpanded = 4
nsFocused = 2
nsFocusRect = 1
nsSelected = 3
ntContainsUnit = 0
ntDcpBpiName = 2
ntRequiresPackage = 1
NullChar = #0
Numbers = [48..57]
NumSmallBlockTypes = 46

### O

obfpIgnorePeripherals = 1
obfpStopAtArbiter = 0
OBJ_FILE_VERSION = #6
ObjectFieldTypes = [2..5]
OneHour = 0.041666666666666664
OneMillisecond = 1.1574074074074074e-08
OneMinute = 0.0006944444444444445
OneSecond = 1.1574074074074073e-05
opAdd = 0
opAnd = 8
opCmpEQ = 14
opCmpGE = 19
opCmpGT = 18
opCmpLE = 17
opCmpLT = 16
opCmpNE = 15
opCompare = 11
opDivide = 3
OpenBusInsertSet = [2, 4..5, 8..15, 17..18, 21, 28, 36, 62]
opIntDivide = 4
opModulus = 5
opMultiply = 2
opNegate = 12
opNot = 13
opOr = 9
opShiftLeft = 6
opShiftRight = 7
opSubtract = 1
OptimizationMode = 0
opXor = 10
OrdNumOfZero = 48
oriHorizontal = 0
oriVertical = 1
otDRC = 1
otMergeAdd = 2
otMergeHeadAdd = 4
otMergeHeadRemove = 5
otMergeRemove = 3
otMergeWorkingAdd = 6
otMergeWorkingRemove = 7
otNone = 0
ovDiscardUndoState = -6
OverlayLayers = [1..2]
OverlayLayerTypeId = '{C7EF040E-8D00-490B-B00C-A7E7823FF174}'
ovHide = -3
ovInPlaceActivate = -5
ovOpen = -2
ovPrimary = -65536
ovShow = -1
ovUIActivate = -4

### P

ParagraphSeparator = ' '
PasteMaskTypeId = '{E6A36257-B90F-45E5-9F8D-A213ECDB687C}'
PathDelim = '\'
PathSep = ';'
pboBlur = 4
pboDarkenedInactive = 3
pboDrawInactiveArea = 0
pboGradient = 1
pboSmooth = 2
PCBM_BeginModify = 1
PCBM_BoardRegisteration = 2
PCBM_CancelModify = 4
PCBM_Create = 5
PCBM_CycleEnd = 11
PCBM_CycleStart = 12
PCBM_Destroy = 6
PCBM_EndModify = 3
PCBM_NullMessage = 0
PCBM_ProcessCancel = 9
PCBM_ProcessEnd = 8
PCBM_ProcessStart = 7
PCBM_RecallRobotState = 18
PCBM_StoreRobotState = 17
PCBM_SystemInvalid = 13
PCBM_SystemValid = 14
PCBM_UnDoRegister = 16
PCBM_ViewUpdate = 15
PCBM_YieldToRobots = 10
PEConductiveLayerTypeId = '{C558FE3F-D914-4761-9D82-A12591CEB133}'
PECoreLayerTypeId = '{E9A93AD8-17EE-438C-A1B6-92A3995DFDA8}'
PEIsolationLayerTypeId = '{8590CC63-42D8-48CB-8307-72991910BCC9}'
PELayerTypeId = '{8053A284-8886-43E8-BAA0-5AA1D8DE97D1}'
PENonConductiveLayerTypeId = '{18BE3C27-BFEB-4BBA-8E9A-DF4CAEEE1731}'
PEPrepregLayerTypeId = '{743DE2F9-2902-4E35-B39C-BACD385F87DD}'
pfBCB4Produced = 134217728
pfConsumerBCB = 2097152
pfConsumerCompat = 0
pfConsumerDelphi = 1048576
pfConsumerMask = 15728640
pfDelphi4Produced = 201326592
pfDesignOnly = 2
pfExeModule = 0
pfIgnoreDupUnits = 8
pfLibraryModule = 2147483648
pfModuleTypeMask = 3221225472
pfNeverBuild = 1
pfPackageModule = 1073741824
pfProducerMask = 201326592
pfProducerUndefined = 67108864
pfRunOnly = 4
pfV3Produced = 0
PhysicalLayerTypeId = '{DAA9ECCC-0064-462D-854E-0B9E829EF563}'
pidAndroid = 16
pidiOSDevice = 64
pidiOSDevice32 = 64
pidiOSDevice64 = 1024
pidiOSSimulator = 8
pidLinux32 = 32
pidLinux64 = 128
pidOSX32 = 4
pidWin32 = 1
pidWin64 = 2
pidWinARM = 2048
pidWinIoT32 = 512
pidWinNX32 = 256
pkDotMatrix = 0
pkHPPCL = 1
PlaneLayerTypeId = '{F59FAB94-C5ED-467D-94CD-F60A323C5D5B}'
PlatformEndian = 1
PositiveValue = 1
PrepregLayerTypeId = '{1A79611A-039D-4D40-A204-53C26C50F8B5}'
psBottom = 1
psExe = 'EXE'
psExeMacro = '$(EXE)'
psLeft = 2
psLIBPATH = 'LIBRARY_PATH'
psLIBPATHmacro = '$(LIBRARY_PATH)'
PSM_PAGEINFO = 1124
PSM_SHEETINFO = 1125
psMAKEFILE = 'MAKEFILE'
psMAKEFILEmacro = '$(MAKEFILE)'
psOUTDIR = 'OUTDIR'
psOUTDIRmacro = '$(OUTDIR)'
psPRODDIR = 'PRODDIR'
psPRODDIRmacro = '$(PRODDIR)'
psPROJ = 'PROJ'
psPROJDIR = 'PROJDIR'
psPROJDIRmacro = '$(PROJDIR)'
psPROJmacro = '$(PROJ)'
psRight = 3
psSWPLATFORM = 'SWPLATFORM'
psSWPLATFORMmacro = '$(SWPLATFORM)'
psTop = 0

### R

rc3_Cursor = 2
rc3_Icon = 1
rc3_StockIcon = 0
RecodeLeaveFieldAsIs = 65535
RepeatPause = 100
rfIgnoreCase = 1
rfReplaceAll = 0
rgiFirst = -1024
rgiLast = -513
rmCenter = 1
rmExact = 0
rmFPGA = 1
rmPCB = 0
Rotation0AllowedBitMask = 1
Rotation180AllowedBitMask = 8
Rotation270AllowedBitMask = 16
Rotation90AllowedBitMask = 2
RotationsAllAllowedBitMask = 32
RouteGuideMediumName = 'Guide'
RouteGuideShortName = 'RG'
RT_RCDATA = 10
rtDeleted = 2
rtInserted = 1
RTLVersion = 30.0
rtModified = 0
rtUnmodified = 3

### S

S_FALSE = 1
S_OK = 0
sApplyUpdatesDataSetCommand = 'ApplyUpdates'
SBButtonRepeatInterval = 30
SBButtonStartInterval = 200
SBM_ENABLE_ARROWS = 228
SBM_GETPOS = 225
SBM_GETRANGE = 227
SBM_GETSCROLLBARINFO = 235
SBM_GETSCROLLINFO = 234
SBM_SETPOS = 224
SBM_SETRANGE = 226
SBM_SETRANGEREDRAW = 230
SBM_SETSCROLLINFO = 233
scAlt = 32768
sCancelUpdatesDataSetCommand = 'CancelUpdates'
scCommand = 4096
scCtrl = 16384
SCHM_BeginModify = 2
SCHM_CancelModify = 5
SCHM_Create = 6
SCHM_CycleEnd = 11
SCHM_CycleStart = 12
SCHM_Destroy = 7
SCHM_DocumentUnregistration = 15
SCHM_EndModify = 3
SCHM_NullMessage = 0
SCHM_PrimitiveRegistration = 1
SCHM_ProcessCancel = 10
SCHM_ProcessEnd = 9
SCHM_ProcessStart = 8
SCHM_SystemInvalid = 13
SCHM_SystemValid = 14
SCHM_YieldToRobots = 4
SchPrimitiveSet = [2..5, 7..28, 30..31, 35..41, 43, 48..49, 53..56, 61..62]
SchSheetInsertSet = [2..5, 7..24, 26, 28, 35..36, 38..39, 41, 48..49, 53, 56, 61..62]
scNone = 0
scShift = 8192
sdDelimiter = 0
sdDown = 3
sdLineBreak = 3
sdNameValueSeparator = 2
sdQuoteChar = 1
sdStrictDelimiter = 4
sdUp = 2
seAESNI = 128
seBorder = 2
seClient = 1
SecsPerDay = 86400
SecsPerHour = 3600
SecsPerMin = 60
seFont = 0
sePCLMULQDQ = 256
sePOPCNT = 64
seSSE = 1
seSSE2 = 2
seSSE3 = 4
seSSE41 = 16
seSSE42 = 32
seSSSE3 = 8
sfDesignSize = 5
sfFont = 4
sfHeight = 3
sfLeft = 0
sfTop = 1
sfWidth = 2
sgCheck = 24
sgChevronDown = 32
sgChevronLeft = 33
sgChevronRight = 34
sgChevronUp = 31
sgCircle = 27
sgCurlicue = 25
sgDoubleCircle = 28
sgDoubleCurlicue = 26
sgDown = 4
sgDownLeft = 7
sgDownLeftLong = 19
sgDownRight = 8
sgDownRightLong = 20
sgDownUp = 14
sgiCheck = 24
sgiChevronDown = 32
sgiChevronLeft = 33
sgiChevronRight = 34
sgiChevronUp = 31
sgiCircle = 27
sgiCurlicue = 25
sgiDoubleCircle = 28
sgiDoubleCurlicue = 26
sgiDown = 4
sgiDownLeft = 7
sgiDownLeftLong = 19
sgiDownRight = 8
sgiDownRightLong = 20
sgiDownUp = 14
sgiFirst = 1
sgiLast = 34
sgiLeft = 1
sgiLeftDown = 10
sgiLeftRight = 15
sgiLeftUp = 9
sgiNoGesture = 0
sgiRight = 2
sgiRightDown = 12
sgiRightLeft = 16
sgiRightUp = 11
sgiScratchout = 21
sgiSemiCircleLeft = 29
sgiSemiCircleRight = 30
sgiSquare = 23
sgiTriangle = 22
sgiUp = 3
sgiUpDown = 13
sgiUpLeft = 5
sgiUpLeftLong = 17
sgiUpRight = 6
sgiUpRightLong = 18
sgLeft = 1
sgLeftDown = 10
sgLeftRight = 15
sgLeftUp = 9
sgRight = 2
sgRightDown = 12
sgRightLeft = 16
sgRightUp = 11
sgScratchout = 21
sgSemiCircleLeft = 29
sgSemiCircleRight = 30
sgSquare = 23
sgTriangle = 22
sgUp = 3
sgUpDown = 13
sgUpLeft = 5
sgUpLeftLong = 17
sgUpRight = 6
sgUpRightLong = 18
SheetEntryObjectsSet = [40]
SheetLinkerObjectsSet = [38, 40]
SheetSymbolObjectsSet = [41]
SIGNAL_LAYER_FLAGS = 257
SignalLayers = [1..32]
SignalLayerTypeId = '{F4ECCD87-2CFB-4F37-BE50-4F3A272B4D01}'
slePoll = 0
sleSetOnUserChange = 1
sLineBreak = ?
smBlindViaShape = 8
smBoardRegionOutline = 14
smComment = 18
smCompare_DiffAdd = 29
smCompare_DiffDel = 30
smCompare_DiffHeadAdd = 31
smCompare_DiffHeadDel = 32
smCompare_DiffMineAdd = 33
smCompare_DiffMineDel = 34
smComponentBodyReferencePoint = 4
smComponentBodySnapPoint = 5
smComponentJumper = 13
smComponentReferencePoint = 3
smCounterHoleRing2D = 21
smDesignViewTitle = 16
smPadNetName = 10
smPadPowerPlaneConnection = 2
smPasteMaskHiddenAt3D_Arc = 23
smPasteMaskHiddenAt3D_Fill = 25
smPasteMaskHiddenAt3D_Pad = 22
smPasteMaskHiddenAt3D_Region = 26
smPasteMaskHiddenAt3D_Text = 27
smPasteMaskHiddenAt3D_Track = 24
smPolygonCutoutOutline = 0
smPullbackArc = 20
smPullbackTrack = 19
smRGBAShowOnlyWithLayer = 28
smRoomName = 12
smSplitPlane2DHighlight = 15
smTextSpecialString = 17
smTHPadShape = 7
smTrackNetName = 11
smViaHoleShape2D = 6
smViaNetName = 9
smViaPowerPlaneConnection = 1
soFromBeginning = 0
soFromCurrent = 1
soFromEnd = 2
SolderMaskLayers = [5..6]
SolderMaskLayerTypeId = '{7B384237-13D8-4318-8BCB-ACCD8D9A51E7}'
Space = ' '
SpaceSize = 5
SpatialObjectsSet = [2..5, 7..28, 30..32, 34..41, 43, 48..49, 53..56, 61..62, 79..89, 92..94, 98]
SQLSections = [5..13]
ssAlt = 1
ssCommand = 9
ssCtrl = 2
ssDouble = 6
ssHorizontal = 10
ssLeft = 3
ssMiddle = 5
ssPen = 8
ssRight = 4
ssShift = 0
ssTouch = 7
STANDARD_LAYER_FLAGS = 0
StandardColorsCount = 16
staoExcludeEmpty = 1
staoTrimValues = 0
StringDelimiter = ''''
SwitchChars = [5, 7]

### T

taAdd = 1
taAddFirst = 0
TAB = #9
Tabulator = #9
taInsert = 2
TBaseNavigator.TOrientation.orHorizontal = 0
TBaseNavigator.TOrientation.orVertical = 1
tbHiliteHotTrack = 1
tbNoEdges = 0
tbNoEtchedEffect = 4
tbNoMark = 3
tbNoOffset = 2
tbsChecked = 0
tbsEllipses = 6
tbsEnabled = 2
tbsHidden = 3
tbsIndeterminate = 4
tbsMarked = 7
tbsPressed = 1
tbsWrap = 5
TCustomButton.TButtonStyle.bsCommandLink = 1
TCustomButton.TButtonStyle.bsPushButton = 0
TCustomButton.TButtonStyle.bsSplitButton = 2
TCustomCategoryPanelGroup.THeaderStyle.hsGradient = 0
TCustomCategoryPanelGroup.THeaderStyle.hsImage = 1
TCustomCategoryPanelGroup.THeaderStyle.hsThemed = 2
TCustomGestureEngine.TGestureEngineFlag.efMouseEvents = 0
TCustomGestureEngine.TGestureEngineFlag.efTouchEvents = 1
tdiConfirmation = 5
tdiError = 2
tdiInformation = 3
tdiNone = 0
tdiShield = 4
tdiWarning = 1
tfCRLF = 1
tkAnsiChar = 2
tkAnsiString = 10
tkShortString = 5
tkUnicodeString = 18
tkWideChar = 9
tkWideString = 11
toEchoTransmit = 0
toEOF = #0
toFloat = #4
toInteger = #3
Tolerance = 100.0
TopLayerPermitted_BitMask = 1
toString = #2
toSymbol = #1
toWString = #5
True = True
tviDisabled = 0
tviFlat = 1

### U

ufImplicitUnit = 16
ufMainUnit = 1
ufOrgWeakUnit = 8
ufPackageUnit = 2
ufWeakPackageUnit = 6
ufWeakUnit = 4
UM_DELAYDESTROY = 3032
UM_SETTRANSPARENCY = 1025
UnixDateDelta = 25569
UpperAlpha = [65..90]
upWhereAll = 0
upWhereChanged = 1
upWhereKeyOnly = 2

### V

V6_AllLayers = [1..75]
V6_cMaxEditableLayer = 74
V6_cMidLayers = [2..31]
V6_InternalPlanes = [7..22]
V6_kMaxInternalPlane = 54
V6_kMinInternalPlane = 39
V6_MaxBoardLayer = 74
V6_MaxLayer = 82
V6_MaxMechanicalLayer = 72
V6_MaxRouteLayer = 32
V6_MechanicalLayers = [1..16]
V6_MinLayer = 1
V6_MinMechanicalLayer = 57
V6_MultiLayers = [0, 18]
V6_OverlayLayers = [1..2]
V6_SignalLayers = [1..32]
V6_SolderMaskLayers = [5..6]
V6_xAllLayers = [1..74]
V7_ActiveIn3D = [1..7, 10..11, 16]
V7_AllLayers = [1..16]
V7_cWidthRuleLayers = [1..3]
V7_DielectricLayers = [10..11, 27]
V7_EditableLayers = [1..15]
V7_ElectricalLayers = [1..4]
V7_FullLayerSet = [0..29]
V7_InternalPlaneLayers = [4]
V7_InternalPlanes = [4]
V7_InvertedLayers = [4, 8..11]
V7_MechanicalLayers = [5, 28..29]
V7_MidLayers = [2]
V7_MiscLayers = [0, 6..26]
V7_MultiLayer = [7]
V7_MultiLayers = [5, 7]
V7_NonEditableLayers = [0..7, 10]
V7_NotActiveIn3D = [0..1, 4..7]
V7_NotActiveIn3DLayerColor = [5, 8..9, 12..15, 28..29]
V7_NotActiveIn3DLayerColorWithPaste = [5, 12..15, 28..29]
V7_NotActiveIn3DWithPaste = [4..7]
V7_OverlayLayers = [6..7]
V7_PadstackLayers = [1..3]
V7_PasteMaskLayers = [0..1]
V7_PolygonLayers = [1..3, 5..15, 28..29]
V7_SignalLayers = [1..3]
V7_SilkscreenLayers = [6..7]
V7_SolderMaskLayers = [2..3]
V7_SystemLayers = [0, 16..26]
varAny = 257
varArray = 8192
varBoolean = 11
varByRef = 16384
varByte = 17
varCurrency = 6
varDate = 7
varDispatch = 9
varDouble = 5
varEmpty = 0
varError = 10
varInt64 = 20
varInteger = 3
varLongWord = 19
varNull = 1
varObject = 73
varOleStr = 8
varRecord = 36
varShortInt = 16
varSingle = 4
varSmallint = 2
varStrArg = 72
varString = 256
varTypeMask = 4095
varUInt64 = 21
varUnknown = 13
varUStrArg = 74
varUString = 258
varVariant = 12
varWord = 18
vcPrivate = 0
vcProtected = 1
vcPublic = 2
vcPublished = 3
VERROR = 2
VERSION_TEXT = '2.0'
VerticalTab = #11
VFAILURE = 3
VirtualObjectsSet = [1..2]
vmtAddRef = 8
vmtAfterConstruction = -80
vmtArcOffset = 0
vmtAutoTable = -184
vmtBeforeDestruction = -72
vmtClassName = -136
vmtCreateObject = 24
vmtDefaultHandler = -56
vmtDestroy = -32
vmtDispatch = -64
vmtDynamicTable = -144
vmtEquals = -112
vmtFieldTable = -160
vmtFreeInstance = -40
vmtGetHashCode = -104
vmtInitTable = -176
vmtInstanceSize = -128
vmtIntfTable = -192
vmtMethodTable = -152
vmtNewInstance = -48
vmtParent = -120
vmtQueryInterface = 0
vmtRelease = 16
vmtSafeCallException = -88
vmtSelfPtr = -200
vmtToString = -96
vmtTypeInfo = -168
VNOTE = 0
voDrive = 0
voLongName = 2
voPath = 1
vtAnsiString = 11
vtBoolean = 1
vtChar = 2
vtClass = 8
vtCurrency = 12
vtExtended = 3
vtInt64 = 16
vtInteger = 0
vtInterface = 14
vtObject = 7
vtPChar = 6
vtPointer = 5
vtPWideChar = 10
vtString = 4
vtUnicodeString = 17
vtVariant = 13
vtWideChar = 9
vtWideString = 15
VWARNING = 1

### W

WebColorsCount = 140
WeeksPerFortnight = 2
WhiteSpace = [9, 32, 44..46, 92]
WideStringObjects = [5, 9, 13..14]
WirPrimitiveSet = [2, 4..5, 8..11, 13..15, 17..18, 21..23, 25, 27, 81..83, 87..89, 92..94, 98]
WM_ACTIVATE = 6
WM_ACTIVATEAPP = 28
WM_ActivatedByMouse = 3031
WM_APP = 32768
WM_APPCOMMAND = 793
WM_ASKCBFORMATNAME = 780
WM_CANCELJOURNAL = 75
WM_CANCELMODE = 31
WM_CAPTURECHANGED = 533
WM_CHANGECBCHAIN = 781
WM_CHANGEUISTATE = 295
WM_CHAR = 258
WM_CHARTOITEM = 47
WM_CHILDACTIVATE = 34
WM_CLEAR = 771
WM_CLIPBOARDUPDATE = 797
WM_CLOSE = 16
WM_COALESCE_FIRST = 912
WM_COALESCE_LAST = 927
WM_COMMAND = 273
WM_COMMNOTIFY = 68
WM_COMPACTING = 65
WM_COMPAREITEM = 57
WM_CONTEXTMENU = 123
WM_COPY = 769
WM_COPYDATA = 74
WM_COPYGLOBALDATA = 73
WM_CREATE = 1
WM_CTLCOLOR = 25
WM_CTLCOLORBTN = 309
WM_CTLCOLORDLG = 310
WM_CTLCOLOREDIT = 307
WM_CTLCOLORLISTBOX = 308
WM_CTLCOLORMSGBOX = 306
WM_CTLCOLORSCROLLBAR = 311
WM_CTLCOLORSTATIC = 312
WM_CUT = 768
WM_DDE_ACK = 996
WM_DDE_ADVISE = 994
WM_DDE_DATA = 997
WM_DDE_EXECUTE = 1000
WM_DDE_FIRST = 992
WM_DDE_INITIATE = 992
WM_DDE_LAST = 1000
WM_DDE_POKE = 999
WM_DDE_REQUEST = 998
WM_DDE_TERMINATE = 993
WM_DDE_UNADVISE = 995
WM_DEADCHAR = 259
WM_DELETEITEM = 45
WM_DESTROY = 2
WM_DESTROYCLIPBOARD = 775
WM_DEVICECHANGE = 537
WM_DEVMODECHANGE = 27
WM_DISPLAYCHANGE = 126
WM_DPICHANGED = 736
WM_DRAWCLIPBOARD = 776
WM_DRAWITEM = 43
WM_DROPFILES = 563
WM_DWMCOLORIZATIONCOLORCHANGED = 800
WM_DWMCOMPOSITIONCHANGED = 798
WM_DWMNCRENDERINGCHANGED = 799
WM_DWMSENDICONICLIVEPREVIEWBITMAP = 806
WM_DWMSENDICONICTHUMBNAIL = 803
WM_DWMWINDOWMAXIMIZEDCHANGE = 801
WM_ENABLE = 10
WM_ENDSESSION = 22
WM_ENTERIDLE = 289
WM_ENTERMENULOOP = 529
WM_ENTERSIZEMOVE = 561
WM_ERASEBKGND = 20
WM_EXITMENULOOP = 530
WM_EXITSIZEMOVE = 562
WM_FONTCHANGE = 29
WM_GESTURE = 281
WM_GESTURENOTIFY = 282
WM_GETDLGCODE = 135
WM_GETFONT = 49
WM_GETHOTKEY = 51
WM_GETICON = 127
WM_GETMINMAXINFO = 36
WM_GETOBJECT = 61
WM_GETTEXT = 13
WM_GETTEXTLENGTH = 14
WM_GETTITLEBARINFOEX = 831
WM_HANDHELDFIRST = 856
WM_HANDHELDLAST = 863
WM_HELP = 83
WM_HOTKEY = 786
WM_HSCROLL = 276
WM_HSCROLLCLIPBOARD = 782
WM_ICONERASEBKGND = 39
WM_IME_CHAR = 646
WM_IME_COMPOSITION = 271
WM_IME_COMPOSITIONFULL = 644
WM_IME_CONTROL = 643
WM_IME_ENDCOMPOSITION = 270
WM_IME_KEYDOWN = 656
WM_IME_KEYLAST = 271
WM_IME_KEYUP = 657
WM_IME_NOTIFY = 642
WM_IME_REQUEST = 648
WM_IME_SELECT = 645
WM_IME_SETCONTEXT = 641
WM_IME_STARTCOMPOSITION = 269
WM_INITDIALOG = 272
WM_INITMENU = 278
WM_INITMENUPOPUP = 279
WM_INPUT = 255
WM_INPUT_DEVICE_CHANGE = 254
WM_INPUTLANGCHANGE = 81
WM_INPUTLANGCHANGEREQUEST = 80
WM_KEYDOWN = 256
WM_KEYFIRST = 256
WM_KEYLAST = 265
WM_KEYUP = 257
WM_KILLFOCUS = 8
WM_LBUTTONDBLCLK = 515
WM_LBUTTONDOWN = 513
WM_LBUTTONUP = 514
WM_MBUTTONDBLCLK = 521
WM_MBUTTONDOWN = 519
WM_MBUTTONUP = 520
WM_MDIACTIVATE = 546
WM_MDICASCADE = 551
WM_MDICREATE = 544
WM_MDIDESTROY = 545
WM_MDIGETACTIVE = 553
WM_MDIICONARRANGE = 552
WM_MDIMAXIMIZE = 549
WM_MDINEXT = 548
WM_MDIREFRESHMENU = 564
WM_MDIRESTORE = 547
WM_MDISETMENU = 560
WM_MDITILE = 550
WM_MEASUREITEM = 44
WM_MENUCHAR = 288
WM_MENUCOMMAND = 294
WM_MENUDRAG = 291
WM_MENUGETOBJECT = 292
WM_MENURBUTTONUP = 290
WM_MENUSELECT = 287
WM_MOUSEACTIVATE = 33
WM_MOUSEFIRST = 512
WM_MOUSEHOVER = 673
WM_MOUSEHWHEEL = 526
WM_MOUSELAST = 526
WM_MOUSELEAVE = 675
WM_MOUSEMOVE = 512
WM_MOUSEWHEEL = 522
WM_MOVE = 3
WM_MOVING = 534
WM_NCACTIVATE = 134
WM_NCCALCSIZE = 131
WM_NCCREATE = 129
WM_NCDESTROY = 130
WM_NCHITTEST = 132
WM_NCLBUTTONDBLCLK = 163
WM_NCLBUTTONDOWN = 161
WM_NCLBUTTONUP = 162
WM_NCMBUTTONDBLCLK = 169
WM_NCMBUTTONDOWN = 167
WM_NCMBUTTONUP = 168
WM_NCMOUSEHOVER = 672
WM_NCMOUSELEAVE = 674
WM_NCMOUSEMOVE = 160
WM_NCPAINT = 133
WM_NCRBUTTONDBLCLK = 166
WM_NCRBUTTONDOWN = 164
WM_NCRBUTTONUP = 165
WM_NCXBUTTONDBLCLK = 173
WM_NCXBUTTONDOWN = 171
WM_NCXBUTTONUP = 172
WM_NEXTDLGCTL = 40
WM_NEXTMENU = 531
WM_NOTIFY = 78
WM_NOTIFYFORMAT = 85
WM_NULL = 0
WM_PAINT = 15
WM_PAINTCLIPBOARD = 777
WM_PAINTICON = 38
WM_PALETTECHANGED = 785
WM_PALETTEISCHANGING = 784
WM_PARENTNOTIFY = 528
WM_PASTE = 770
WM_PENWINFIRST = 896
WM_PENWINLAST = 911
WM_POWER = 72
WM_POWERBROADCAST = 536
WM_PRINT = 791
WM_PRINTCLIENT = 792
WM_QUERYDRAGICON = 55
WM_QUERYENDSESSION = 17
WM_QUERYNEWPALETTE = 783
WM_QUERYOPEN = 19
WM_QUERYUISTATE = 297
WM_QUEUESYNC = 35
WM_QUIT = 18
WM_RBUTTONDBLCLK = 518
WM_RBUTTONDOWN = 516
WM_RBUTTONUP = 517
WM_RENDERALLFORMATS = 774
WM_RENDERFORMAT = 773
WM_SETCURSOR = 32
WM_SETFOCUS = 7
WM_SETFONT = 48
WM_SETHOTKEY = 50
WM_SETICON = 128
WM_SETREDRAW = 11
WM_SETTEXT = 12
WM_SETTINGCHANGE = 26
WM_SHOWWINDOW = 24
WM_SIZE = 5
WM_SIZECLIPBOARD = 779
WM_SIZING = 532
WM_SPOOLERSTATUS = 42
WM_STYLECHANGED = 125
WM_STYLECHANGING = 124
WM_SYSCHAR = 262
WM_SYSCOLORCHANGE = 21
WM_SYSCOMMAND = 274
WM_SYSDEADCHAR = 263
WM_SYSKEYDOWN = 260
WM_SYSKEYUP = 261
WM_SYSTEM_TRAY_MESSAGE = 1025
WM_SYSTEMERROR = 23
WM_TABLET_ADDED = 712
WM_TABLET_DEFBASE = 704
WM_TABLET_DELETED = 713
WM_TABLET_FIRST = 704
WM_TABLET_FLICK = 715
WM_TABLET_LAST = 735
WM_TABLET_MAXOFFSET = 32
WM_TABLET_QUERYSYSTEMGESTURESTATUS = 716
WM_TCARD = 82
WM_THEMECHANGED = 794
WM_TIMECHANGE = 30
WM_TIMER = 275
WM_TOUCH = 576
WM_UNDO = 772
WM_UNICHAR = 265
WM_UNINITMENUPOPUP = 293
WM_UPDATEUISTATE = 296
WM_USER = 1024
WM_USERCHANGED = 84
WM_VKEYTOITEM = 46
WM_VSCROLL = 277
WM_VSCROLLCLIPBOARD = 778
WM_WINDOWPOSCHANGED = 71
WM_WINDOWPOSCHANGING = 70
WM_WININICHANGE = 26
WM_WTSSESSION_CHANGE = 689
WM_XBUTTONDBLCLK = 525
WM_XBUTTONDOWN = 523
WM_XBUTTONUP = 524
WordDelimiters = [0..47, 58..64, 91..96, 123..255]

### X

xAllLayers = [1..74]
xgbHeaderCaption = 1
xgbIgnoreThemeFont = 0
xIntelligentWire = 1
xNoObjectId = 0
xReviewGraphicalObject = 2

### Y

YearsPerCentury = 100
YearsPerDecade = 10
YearsPerMillennium = 1000
Yes = 1

### Z

Z_FINISH = 4
Z_NO_FLUSH = 0
Z_STREAM_END = 1
ZeroValue = 0
