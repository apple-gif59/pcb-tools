# 原理图接口（ISch_*，单元 Rt_Schematic）

来源：Altium Designer 23.1.1.15 的 `System\ScriptingSystem.dll`（脚本引擎的注册表，2026-10-25 提取）。由 `scripts/gen_docs.py` 生成，不要手改。

每节列出该接口**自己注册的**成员；继承来的成员在父接口那一节（`继承` 一行给出链）。查某个接口的全部成员（含继承）用 `scripts/lookup.py <接口名>`。
属性写成 `read <getter> write <setter>`，没有 `write` 的是只读属性（行尾 `// read-only`），不要赋值（`IPCB_Board.LayerColor` 赋值实测会卡死执行器）。getter/setter 本身也是注册过的方法，可以直接调用。

## IComponentFullInfo
继承：IComponentFullInfo → IComponentInfo → IInterface ｜ 单元：Rt_Schematic ｜ 自有 2 个方法、2 个属性

property Parameters: WideString read GetState_Parameters;  // read-only
property ParametersVisibility: WideString read GetState_ParametersVisibility;  // read-only
function GetState_Parameters: WideString;
function GetState_ParametersVisibility: WideString;

## IComponentInfo
继承：IComponentInfo → IInterface ｜ 单元：Rt_Schematic ｜ 自有 6 个方法、6 个属性

property AliasName: WideString read GetState_AliasName;  // read-only
property CompName: WideString read GetState_CompName;  // read-only
property Description: WideString read GetState_Description;  // read-only
property Offset: Integer read GetState_Offset;  // read-only
property PartCount: Integer read GetState_PartCount;  // read-only
property PartName[APartNumber: Integer]: WideString read GetPartName;  // read-only
function GetPartName(APartNumber: Integer): WideString;
function GetState_AliasName: WideString;
function GetState_CompName: WideString;
function GetState_Description: WideString;
function GetState_Offset: Integer;
function GetState_PartCount: Integer;

## IComponentMetafilePainter
继承：IComponentMetafilePainter → IInterface ｜ 单元：Rt_Schematic ｜ 自有 2 个方法、0 个属性

procedure DrawToMetafile(APartIndex: Integer; APaintColorMode: TPaintColorMode; AScaleMode: TPaintScaleMode; const AFileName: WideString);
procedure SetComponent(const ALibReference: WideString; const ALibraryPath: WideString);

## IComponentPainterView
继承：IComponentPainterView → IInterface ｜ 单元：Rt_Schematic ｜ 自有 9 个方法、0 个属性

procedure HideComponentTextualDescriptions;
procedure HighLightComponentPins(APinNameList: WideString; AHighlightColor: TColor; ANonHighlightColor: TColor);
procedure RegisterListener(APinSelectionListener: IComponentPinSelectionListener);
procedure RenameSpecifiedPins(APinNamesParam: WideString);
procedure SetComponent(LibReference: WideString; LibraryPath: WideString; APartIndex: Integer; AHideTextualDescription: Boolean);
procedure SetComponentByHandle(AHandle: ISch_Component; APartIndex: Integer);
procedure ShowAllPins;
procedure ShowPinsAsSelected(APinNameList: WideString);
procedure ShowSpecifiedPinsOnly(APinNameList: WideString);

## IComponentPainterView2
继承：IComponentPainterView2 → IComponentPainterView → IInterface ｜ 单元：Rt_Schematic ｜ 自有 1 个方法、0 个属性

procedure ConfigView(Parameters: WideString);

## IComponentPinSelectionListener
继承：IComponentPinSelectionListener → IInterface ｜ 单元：Rt_Schematic ｜ 自有 1 个方法、0 个属性

procedure ComponentPinSelectionChanged(NewPinSelectionList: WideString);

## IComponentSubPartsInfo
继承：IComponentSubPartsInfo → IInterface ｜ 单元：Rt_Schematic ｜ 自有 5 个方法、3 个属性

property Designator: WideString read GetState_Designator;  // read-only
property ProjectFilePath: WideString read GetState_ProjectFilePath;  // read-only
property SubPartsHandlesCount: Integer read GetState_SubPartsHandlesCount;  // read-only
function GetState_Designator: WideString;
function GetState_ProjectFilePath: WideString;
function GetState_SubPartsHandlesCount: Integer;
function GetSubPartHandle(AIndex: Integer): WideString;
procedure RemoveSubPartHandle(ASubPartHandle: WideString);

## IConnection
继承：IConnection → IInterface ｜ 单元：Rt_Schematic ｜ 自有 10 个方法、5 个属性

property IsManualJunction: Boolean read GetState_IsManualJunction write SetState_IsManualJunction;
property IsPinConnection: Boolean read GetState_IsPinConnection write SetState_IsPinConnection;
property Location: TLocation read GetState_Location write SetState_Location;
property ObjectsCount: Integer read GetState_ObjectsCount write SetState_ObjectsCount;
property Size: TSize read GetState_Size write SetState_Size;
function GetState_IsManualJunction: Boolean;
function GetState_IsPinConnection: Boolean;
function GetState_Location: IDispatch;
function GetState_ObjectsCount: Integer;
function GetState_Size: TSize;
procedure SetState_IsManualJunction(AValue: Boolean);
procedure SetState_IsPinConnection(AValue: Boolean);
procedure SetState_Location(const AValue: IDispatch);
procedure SetState_ObjectsCount(AValue: Integer);
procedure SetState_Size(AValue: TSize);

## IConnectionsArray
继承：IConnectionsArray → IInterface ｜ 单元：Rt_Schematic ｜ 自有 13 个方法、2 个属性

property Connection[Index: Integer]: IConnection read GetState_Connection;  // read-only
property ConnectionsCount: Integer read GetState_ConnectionsCount;  // read-only
procedure AddConnection(const ALocation: IDispatch);
procedure AddConnectionWithPin(const ALocation: IDispatch; AIsPin: Boolean);
procedure AddConnectionXY(X: Integer; Y: Integer);
procedure AddConnectionXY_WithSize(X: Integer; Y: Integer; ASize: TSize);
procedure AddJunctionsFromComponent(const AConnectionsArraySrc: IConnectionsArray; const AComponent: ISch_Component);
procedure AddJunctionsFromWire(const AConnectionsArraySrc: IConnectionsArray; const AWire: ISch_Wire);
function GetConnectionAt(const ALocation: IDispatch): IConnection;
function GetState_Connection(Index: Integer): IConnection;
function GetState_ConnectionsCount: Integer;
procedure GraphicallyInvalidate;
function RemoveAllConnectionsAt(const ALocation: IDispatch): Boolean;
function RemoveAllConnectionsForLine(const L1: IDispatch; const L2: IDispatch): Boolean;
procedure ResetAllConnections;

## IDirectiveData
继承：IDirectiveData → IInterface ｜ 单元：Rt_Schematic ｜ 自有 19 个方法、10 个属性

property Color: TColor read DM_GetColor write DM_SetColor;
property Directive: INetItem read DM_GetDirective;  // read-only
property IsActive: Boolean read DM_GetIsActive write DM_SetIsActive;
property Location: TLocation read DM_GetLocation write DM_SetLocation;
property Orientation: TRotationBy90 read DM_GetOrientation write DM_SetOrientation;
property StrConnectionPairsToSuppress: WideString read DM_GetStrConnectionPairsToSuppress write DM_SetStrConnectionPairsToSuppress;
property StrErrorKindSetToSuppress: WideString read DM_GetStrErrorKindSetToSuppress write DM_SetStrErrorKindSetToSuppress;
property StrSuppressableErrors: WideString read DM_GetStrSuppressableErrors write DM_SetStrSuppressableErrors;
property SuppressAll: Boolean read DM_GetSuppressAll write DM_SetSuppressAll;
property Symbol: TNoERCSymbol read DM_GetSymbol write DM_SetSymbol;
function DM_GetColor: TColor;
function DM_GetDirective: INetItem;
function DM_GetIsActive: Boolean;
function DM_GetLocation: IDispatch;
function DM_GetOrientation: TRotationBy90;
function DM_GetStrConnectionPairsToSuppress: WideString;
function DM_GetStrErrorKindSetToSuppress: WideString;
function DM_GetStrSuppressableErrors: WideString;
function DM_GetSuppressAll: Boolean;
function DM_GetSymbol: TNoERCSymbol;
procedure DM_SetColor(const Value: TColor);
procedure DM_SetIsActive(const Value: Boolean);
procedure DM_SetLocation(const Value: IDispatch);
procedure DM_SetOrientation(const Value: TRotationBy90);
procedure DM_SetStrConnectionPairsToSuppress(const Value: WideString);
procedure DM_SetStrErrorKindSetToSuppress(const Value: WideString);
procedure DM_SetStrSuppressableErrors(const Value: WideString);
procedure DM_SetSuppressAll(const Value: Boolean);
procedure DM_SetSymbol(const Value: TNoERCSymbol);

## IDocumentPainterView
继承：IDocumentPainterView → IInterface ｜ 单元：Rt_Schematic ｜ 自有 8 个方法、0 个属性

procedure DrawCurrentZoomRectangle_Invert;
procedure GetStringMaxMin(const ALocation: IDispatch; const AText: WideString; AFontId: Integer; const ABoundingRect: IDispatch);
procedure Invalidate;
procedure PaintSingleObject(const AGraphicalObject: ISch_GraphicalObject);
procedure Redraw(const AGraphicalObject: ISch_GraphicalObject);
procedure Refresh;
procedure RefreshCurrentZoomWindow;
procedure SetState_DocumentToPaint(const ADocument: ISch_Document);

## IFSM_Document
继承：IFSM_Document → ISch_Document → ISch_ParametrizedGroup → ISch_GraphicalObject → ISch_BasicContainer → IInterface ｜ 单元：Rt_Schematic ｜ 自有 3 个方法、3 个属性

property DefaultStateID: WideString read GetState_DefaultStateID;  // read-only
property PortID_Clock: WideString read GetState_PortID_Clock;  // read-only
property PortID_Reset: WideString read GetState_PortID_Reset;  // read-only
function GetState_DefaultStateID: WideString;
function GetState_PortID_Clock: WideString;
function GetState_PortID_Reset: WideString;

## IFSM_State
继承：IFSM_State → ISch_ParametrizedGroup → ISch_GraphicalObject → ISch_BasicContainer → IInterface ｜ 单元：Rt_Schematic ｜ 自有 3 个方法、4 个属性

property Actions_Text: WideString read GetState_Actions_Text;  // read-only
property DelayedClock: Integer read GetState_DelayedClock;  // read-only
property DelayedEnable: Boolean read GetState_DelayedEnable;  // read-only
property Text: WideString read GetState_Text;  // read-only
function GetState_Actions_Text: WideString;
function GetState_DelayedClock: Integer;
function GetState_DelayedEnable: Boolean;

## IFSM_Transition
继承：IFSM_Transition → ISch_BasicPolyline → ISch_Polygon → ISch_GraphicalObject → ISch_BasicContainer → IInterface ｜ 单元：Rt_Schematic ｜ 自有 5 个方法、5 个属性

property Actions_Text: WideString read GetState_Actions_Text;  // read-only
property Comment: ISch_Parameter read GetState_SchComment;  // read-only
property FromStateId: WideString read GetState_FromStateId;  // read-only
property Priority: Integer read GetState_Priority;  // read-only
property ToStateId: WideString read GetState_ToStateId;  // read-only
function GetState_Actions_Text: WideString;
function GetState_FromStateId: WideString;
function GetState_Priority: Integer;
function GetState_SchComment: ISch_Parameter;
function GetState_ToStateId: WideString;

## IGridSetting
继承：IGridSetting → IInterface ｜ 单元：Rt_Schematic ｜ 自有 14 个方法、6 个属性

property HotspotGridOn: Boolean read GetState_HotspotGridOn write SetState_HotspotGridOn;
property HotspotGridSize: TCoord read GetState_HotspotGridSize write SetState_HotspotGridSize;
property SnapGridOn: Boolean read GetState_SnapGridOn write SetState_SnapGridOn;
property SnapGridSize: TCoord read GetState_SnapGridSize write SetState_SnapGridSize;
property VisibleGridOn: Boolean read GetState_VisibleGridOn write SetState_VisibleGridOn;
property VisibleGridSize: TCoord read GetState_VisibleGridSize write SetState_VisibleGridSize;
procedure CopyTo(AGridSetting: IGridSetting);
function GetState_HotspotGridOn: Boolean;
function GetState_HotspotGridSize: Integer;
function GetState_SnapGridOn: Boolean;
function GetState_SnapGridSize: Integer;
function GetState_VisibleGridOn: Boolean;
function GetState_VisibleGridSize: Integer;
function SameAs(AGridSetting: IGridSetting): Boolean;
procedure SetState_HotspotGridOn(B: Boolean);
procedure SetState_HotspotGridSize(C: Integer);
procedure SetState_SnapGridOn(B: Boolean);
procedure SetState_SnapGridSize(C: Integer);
procedure SetState_VisibleGridOn(B: Boolean);
procedure SetState_VisibleGridSize(C: Integer);

## IHarnessTypeHolder
继承：IHarnessTypeHolder → IInterface ｜ 单元：Rt_Schematic ｜ 自有 6 个方法、3 个属性

property HarnessType: WideString read GetState_HarnessType write SetState_HarnessType;
property HarnessTypeInferred: Boolean read GetState_HarnessTypeInferred write SetState_HarnessTypeInferred;
property IsHarnessObject: Boolean read GetState_IsHarnessObject write SetState_IsHarnessObject;
function GetState_HarnessType: WideString;
function GetState_HarnessTypeInferred: Boolean;
function GetState_IsHarnessObject: Boolean;
procedure SetState_HarnessType(AValue: WideString);
procedure SetState_HarnessTypeInferred(AValue: Boolean);
procedure SetState_IsHarnessObject(AValue: Boolean);

## ILibCompFullInfoReader
继承：ILibCompFullInfoReader → ILibCompInfoReader → IInterface ｜ 单元：Rt_Schematic ｜ 自有 3 个方法、1 个属性

property ComponentFullInfos[I: Integer]: IComponentFullInfo read GetState_ComponentFullInfo;  // read-only
function GetState_ComponentFullInfo(I: Integer): IComponentFullInfo;
function IsSupportFullLoad: Boolean;
procedure ReadAllComponentFullInfo;

## ILibCompInfoReader
继承：ILibCompInfoReader → IInterface ｜ 单元：Rt_Schematic ｜ 自有 5 个方法、2 个属性

property ComponentInfos[I: Integer]: IComponentInfo read GetState_ComponentInfo;  // read-only
property FileName: WideString read GetState_FileName;  // read-only
function GetState_ComponentInfo(I: Integer): IComponentInfo;
function GetState_FileName: WideString;
function I_ObjectAddress: Pointer;
function NumComponentInfos: Integer;
procedure ReadAllComponentInfo;

## IManagedSheetParentSymbolsInfo
继承：IManagedSheetParentSymbolsInfo → IInterface ｜ 单元：Rt_Schematic ｜ 自有 6 个方法、4 个属性

property Name: WideString read GetState_Name;  // read-only
property ParentSymbolsHandlesCount: Integer read GetState_ParentSymbolsHandlesCount;  // read-only
property ProjectFilePath: WideString read GetState_ProjectFilePath;  // read-only
property RevisionGUID: WideString read GetState_RevisionGUID;  // read-only
function GetParentSymbolHandle(AIndex: Integer): WideString;
function GetState_Name: WideString;
function GetState_ParentSymbolsHandlesCount: Integer;
function GetState_ProjectFilePath: WideString;
function GetState_RevisionGUID: WideString;
procedure RemoveParentSymbolHandle(AParentSymbolHandle: WideString);

## IOpenBus_Component
继承：IOpenBus_Component → ISch_RectangularGroup → ISch_ParametrizedGroup → ISch_GraphicalObject → ISch_BasicContainer → IInterface ｜ 单元：Rt_Schematic ｜ 自有 22 个方法、8 个属性

property ArbiterRoundRobin: Boolean read GetState_ArbiterRoundRobin write SetState_ArbiterRoundRobin;
property ConfiguratorName: WideString read GetState_ConfiguratorName write SetState_ConfiguratorName;
property Designator: ISch_Designator read GetState_Designator;  // read-only
property InterfaceType: TOpenBusComponentInterfaceType read GetState_InterfaceType write SetState_InterfaceType;
property IsUserConfigurable: Boolean read GetState_IsUserConfigurable write SetState_IsUserConfigurable;
property Kind: TOpenBusComponentKind read GetState_Kind write SetState_Kind;
property Name: WideString read GetState_Name write SetState_Name;
property SubProject: WideString read GetState_SubProject write SetState_SubProject;
procedure Connect(const APort1: IOpenBus_Port; const APort2: IOpenBus_Port);
function CreatePort(const ASide: WideString): IOpenBus_Port;
procedure DestroyPort(var APort: IOpenBus_Port);
procedure Disconnect(const APort: IOpenBus_Port);
function GetContainer_InternalPins(APinType: TOpenBusInternalPinType): ISch_BasicContainer;
function GetState_ArbiterRoundRobin: Boolean;
function GetState_ConfiguratorName: WideString;
function GetState_Designator: ISch_Designator;
function GetState_InterfaceType: TOpenBusComponentInterfaceType;
function GetState_IsUserConfigurable: Boolean;
function GetState_Kind: TOpenBusComponentKind;
function GetState_Name: WideString;
function GetState_SchPorts: IOpenBus_PortCollection;
function GetState_SubProject: WideString;
procedure LayoutPorts;
procedure SetState_ArbiterRoundRobin(const AValue: Boolean);
procedure SetState_ConfiguratorName(const Value: WideString);
procedure SetState_InterfaceType(const Value: TOpenBusComponentInterfaceType);
procedure SetState_IsUserConfigurable(AValue: Boolean);
procedure SetState_Kind(const Value: TOpenBusComponentKind);
procedure SetState_Name(const Value: WideString);
procedure SetState_SubProject(const Value: WideString);

## IOpenBus_Document
继承：IOpenBus_Document → IInterface ｜ 单元：Rt_Schematic ｜ 自有 12 个方法、2 个属性

property DefaultClock: WideString read GetDefaultClock write SetDefaultClock;
property DefaultReset: WideString read GetDefaultReset write SetDefaultReset;
procedure AutoConfigure;
procedure DisableAutoConfigure;
procedure EnableAutoConfigure;
function GetAllConnectedMemories(const AComp: IOpenBus_Component): IInterfaceList;
function GetAllConnectedPeripherals(const AComp: IOpenBus_Component): IInterfaceList;
function GetAllProcessors: IInterfaceList;
function GetDefaultClock: WideString;
function GetDefaultReset: WideString;
function RunSignalManager: LongBool;
procedure SetDefaultClock(const AValue: WideString);
procedure SetDefaultReset(const AValue: WideString);
procedure UpdateConnectors;

## IOpenBus_Link
继承：IOpenBus_Link → ISch_Bezier → ISch_BasicPolyline → ISch_Polygon → ISch_GraphicalObject → ISch_BasicContainer → IInterface ｜ 单元：Rt_Schematic ｜ 自有 7 个方法、4 个属性

property PortIn: IOpenBus_Port read GetState_PortIn;  // read-only
property PortInId: WideString read GetState_PortInId write SetState_PortInId;
property PortOut: IOpenBus_Port read GetState_PortOut;  // read-only
property PortOutId: WideString read GetState_PortOutId write SetState_PortOutId;
procedure ConnectPorts(const APortOutId: WideString; const APortInId: WideString);
function GetState_PortIn: IOpenBus_Port;
function GetState_PortInId: WideString;
function GetState_PortOut: IOpenBus_Port;
function GetState_PortOutId: WideString;
procedure SetState_PortInId(const S: WideString);
procedure SetState_PortOutId(const S: WideString);

## IOpenBus_PinGroup
继承：IOpenBus_PinGroup → ISch_BasicContainer → IInterface ｜ 单元：Rt_Schematic ｜ 自有 4 个方法、2 个属性

property Designator: WideString read GetState_Designator write SetState_Designator;
property HarnessType: WideString read GetState_HarnessType write SetState_HarnessType;
function GetState_Designator: WideString;
function GetState_HarnessType: WideString;
procedure SetState_Designator(const AValue: WideString);
procedure SetState_HarnessType(const AValue: WideString);

## IOpenBus_Port
继承：IOpenBus_Port → ISch_GraphicalObject → ISch_BasicContainer → IInterface ｜ 单元：Rt_Schematic ｜ 自有 40 个方法、20 个属性

property AddrBase: Integer read GetState_AddrBase write SetState_AddrBase;
property AddrDecodeWidth: Integer read GetState_AddrDecodeWidth write SetState_AddrDecodeWidth;
property AddrMode: Integer read GetState_AddrMode write SetState_AddrMode;
property AddrWidth: Integer read GetState_AddrWidth write SetState_AddrWidth;
property Caption: WideString read GetState_Caption write SetState_Caption;
property DataWidth: Integer read GetState_DataWidth write SetState_DataWidth;
property HasInputData: Boolean read GetState_HasInputData write SetState_HasInputData;
property HasOutputData: Boolean read GetState_HasOutputData write SetState_HasOutputData;
property HasSelectLines: Boolean read GetState_HasSelectLines write SetState_HasSelectLines;
property HasText: Boolean read GetState_HasText write SetState_HasText;
property Link: IOpenBus_Link read GetState_SchLink write SetState_SchLink;
property LinkId: WideString read GetState_LinkId write SetState_LinkId;
property Name: WideString read GetState_Name;  // read-only
property Number: Integer read GetState_Number write SetState_Number;
property Owner: ISch_GraphicalObject read GetState_SchOwner;  // read-only
property PortType: TOpenBusPortType read GetState_PortType write SetState_PortType;
property Prefix: WideString read GetState_Prefix write SetState_Prefix;
property X: TCoord read GetState_X write SetState_X;
property Y: TCoord read GetState_Y write SetState_Y;
property ZeroDelay: Boolean read GetState_ZeroDelay write SetState_ZeroDelay;
function Duplicate: IOpenBus_Port;
function GetState_AddrBase: Integer;
function GetState_AddrDecodeWidth: Integer;
function GetState_AddrMode: Integer;
function GetState_AddrWidth: Integer;
function GetState_Caption: WideString;
function GetState_DataWidth: Integer;
function GetState_HasInputData: Boolean;
function GetState_HasOutputData: Boolean;
function GetState_HasSelectLines: Boolean;
function GetState_HasText: Boolean;
function GetState_LinkId: WideString;
function GetState_Name: WideString;
function GetState_Number: Integer;
function GetState_PortType: TOpenBusPortType;
function GetState_Prefix: WideString;
function GetState_SchLink: IOpenBus_Link;
function GetState_SchOwner: ISch_GraphicalObject;
function GetState_X: Integer;
function GetState_Y: Integer;
function GetState_ZeroDelay: Boolean;
procedure SetState_AddrBase(const AValue: Integer);
procedure SetState_AddrDecodeWidth(const AValue: Integer);
procedure SetState_AddrMode(const AValue: Integer);
procedure SetState_AddrWidth(const AValue: Integer);
procedure SetState_Caption(const Value: WideString);
procedure SetState_DataWidth(const AValue: Integer);
procedure SetState_HasInputData(const AValue: Boolean);
procedure SetState_HasOutputData(const AValue: Boolean);
procedure SetState_HasSelectLines(const AValue: Boolean);
procedure SetState_HasText(Value: Boolean);
procedure SetState_LinkId(const AValue: WideString);
procedure SetState_Number(const AValue: Integer);
procedure SetState_PortType(const AValue: TOpenBusPortType);
procedure SetState_Prefix(const AValue: WideString);
procedure SetState_Rotation(const AValue: TRotationBy90);
procedure SetState_SchLink(const AValue: IOpenBus_Link);
procedure SetState_X(const AValue: Integer);
procedure SetState_Y(const AValue: Integer);
procedure SetState_ZeroDelay(const AValue: Boolean);

## IOpenBus_PortCollection
继承：IOpenBus_PortCollection → IInterface ｜ 单元：Rt_Schematic ｜ 自有 3 个方法、2 个属性

property Count: Integer read GetCount;  // read-only
property Ports[AIndex: Integer]: IOpenBus_Port read GetPortsSch;  // read-only
function GetCount: Integer;
function GetPortsSch(AIndex: Integer): IOpenBus_Port;
procedure SetPortIndexInSection(const APort: IOpenBus_Port; AIndex: Integer);

## ISCH_GraphicalViewZoomableInterface
继承：ISCH_GraphicalViewZoomableInterface → IInterface ｜ 单元：Rt_Schematic ｜ 自有 3 个方法、0 个属性

procedure ClientToSCHLocation(const X: Integer; const Y: Integer; out PX: Integer; out PY: Integer);
function GetState_ZoomFactor: Double;
procedure SCHLocationToClient(const X: Integer; const Y: Integer; out PX: Integer; out PY: Integer);

## ISCH_HarnessDocumentInterface
继承：ISCH_HarnessDocumentInterface → IInterface ｜ 单元：Rt_Schematic ｜ 自有 2 个方法、0 个属性

function GetLocalComponentPCBLibraryPath(const ASourceLibraryName: WideString; const ADatabaseTableName: WideString; const ADesignItemID: WideString): WideString;
function GetManagedComponentPCBLibraryPath(const AVaultGUID: WideString; const ARevisionGUID: WideString): WideString;

## ISchCommandManager
继承：ISchCommandManager → IInterface ｜ 单元：Rt_Schematic ｜ 自有 10 个方法、0 个属性

procedure AlignToGrid;
function BeginTransaction(ACommandType: TSchCommandType): Boolean;
procedure EnableRobots(AEnable: Boolean);
procedure Mirror(const AAxis: IDispatch);
procedure Move(Dx: Integer; Dy: Integer);
procedure RevertChanges;
procedure Rotate(const ACenter: IDispatch; ARotation: TRotationBy90);
procedure SetObjects(const AObjects: IWideStrings);
procedure StoreChanges;
procedure UpdateSchData;

## ISchCommandManagerFactory
继承：ISchCommandManagerFactory → IInterface ｜ 单元：Rt_Schematic ｜ 自有 3 个方法、0 个属性

function GetCommandManager(const AProjectPath: WideString; const ADocumentPath: WideString): ISchCommandManager;
function GetDragDropTarget(const ADocument: IInterface; const APainter: IInterface): IInterface;
function GetDragGroup: IInterface;

## ISchTemplates
继承：ISchTemplates → IInterface ｜ 单元：Rt_Schematic ｜ 自有 15 个方法、0 个属性

procedure DoSetTemplateFileName(const DocumentInterface: IServerDocument; const AConfigurationTemplateHRID: WideString);
function LoadedLocalTemplates: Boolean;
function LoadedServerTemplates: Boolean;
function LocalTemplate(Index: Integer): ITemplateInfo;
function LocalTemplatesCount: Integer;
procedure RefreshLocalTemplates(const ADocument: IServerDocument);
procedure RefreshServerTemplates;
procedure RefreshServerTemplatesAsync;
function ServerTemplate(Index: Integer): ITemplateInfo;
function ServerTemplateFile(Index: Integer): WideString;
function ServerTemplateFilesCount: Integer;
function ServerTemplatesCount: Integer;
procedure ServerTemplatesLock;
procedure ServerTemplatesUnLock;
procedure SortTemplateInfoList(const AList: IInterfaceList);

## ISch_Arc
继承：ISch_Arc → ISch_GraphicalObject → ISch_BasicContainer → IInterface ｜ 单元：Rt_Schematic ｜ 自有 8 个方法、4 个属性

property EndAngle: TAngle read GetState_EndAngle write SetState_EndAngle;
property LineWidth: TSize read GetState_LineWidth write SetState_LineWidth;
property Radius: TDistance read GetState_Radius write SetState_Radius;
property StartAngle: TAngle read GetState_StartAngle write SetState_StartAngle;
function GetState_EndAngle: Double;
function GetState_LineWidth: TSize;
function GetState_Radius: Integer;
function GetState_StartAngle: Double;
procedure SetState_EndAngle(AAngle: Double);
procedure SetState_LineWidth(ASize: TSize);
procedure SetState_Radius(ARadius: Integer);
procedure SetState_StartAngle(AAngle: Double);

## ISch_BasicContainer
继承：ISch_BasicContainer → IInterface ｜ 单元：Rt_Schematic ｜ 自有 26 个方法、5 个属性

property Container: ISch_BasicContainer read GetState_SchBasicContainer;  // read-only
property Handle: WideString read GetState_Handle;  // read-only
property ObjectId: TObjectId read GetState_ObjectId;  // read-only
property OwnerDocument: ISch_Document read GetState_OwnerSchDocument;  // read-only
property UniqueId: WideString read GetState_UniqueId write SetState_UniqueId;
procedure AddAndPositionSchObject(AObject: ISch_BasicContainer);
procedure AddSchObject(AObject: ISch_BasicContainer);
procedure DeleteAll;
function ExportToParameters: WideString;
procedure FreeAllContainedObjects;
function GetState_DescriptionString: WideString;
function GetState_Handle: WideString;
function GetState_IdentifierString: WideString;
function GetState_ObjectId: TObjectId;
function GetState_OwnerSchDocument: ISch_Document;
function GetState_SchBasicContainer: ISch_BasicContainer;
function GetState_SchParameterByName(const AName: WideString): ISch_Parameter;
function GetState_Text: WideString;
function GetState_UniqueId: WideString;
function GetState_WiringDiagramOriginUniqueId: WideString;
function I_ObjectAddress: IInterface;
function Import_FromUser: Boolean;
procedure PostProcess_Import_FromUser;
procedure PreProcess_Import_FromUser;
procedure RemoveSchObject(AObject: ISch_BasicContainer);
function Replicate: ISch_BasicContainer;
function SchIterator_Create: ISch_Iterator;
procedure SchIterator_Destroy(var AIterator: ISch_Iterator);
procedure SetState_Default(AUnit: TUnitSystem);
procedure SetState_Text(const AValue: WideString);
procedure SetState_UniqueId(const AValue: WideString);

## ISch_BasicPolyline
继承：ISch_BasicPolyline → ISch_Polygon → ISch_GraphicalObject → ISch_BasicContainer → IInterface ｜ 单元：Rt_Schematic ｜ 自有 2 个方法、1 个属性

property LineStyle: TLineStyle read GetState_LineStyle write SetState_LineStyle;
function GetState_LineStyle: TLineStyle;
procedure SetState_LineStyle(AValue: TLineStyle);

## ISch_Bezier
继承：ISch_Bezier → ISch_BasicPolyline → ISch_Polygon → ISch_GraphicalObject → ISch_BasicContainer → IInterface ｜ 单元：Rt_Schematic ｜ 自有 0 个方法、0 个属性


## ISch_Blanket
继承：ISch_Blanket → ISch_CollapsiblePolygon → ISch_Polygon → ISch_GraphicalObject → ISch_BasicContainer → IInterface ｜ 单元：Rt_Schematic ｜ 自有 2 个方法、1 个属性

property LineStyle: TLineStyle read GetState_LineStyle write SetState_LineStyle;
function GetState_LineStyle: TLineStyle;
procedure SetState_LineStyle(AValue: TLineStyle);

## ISch_Bus
继承：ISch_Bus → ISch_Wire → ISch_BasicPolyline → ISch_Polygon → ISch_GraphicalObject → ISch_BasicContainer → IInterface ｜ 单元：Rt_Schematic ｜ 自有 0 个方法、0 个属性


## ISch_BusEntry
继承：ISch_BusEntry → ISch_Line → ISch_GraphicalObject → ISch_BasicContainer → IInterface ｜ 单元：Rt_Schematic ｜ 自有 0 个方法、0 个属性


## ISch_Circle
继承：ISch_Circle → ISch_GraphicalObject → ISch_BasicContainer → IInterface ｜ 单元：Rt_Schematic ｜ 自有 8 个方法、4 个属性

property IsSolid: Boolean read GetState_IsSolid write SetState_IsSolid;
property LineWidth: TSize read GetState_LineWidth write SetState_LineWidth;
property Radius: TDistance read GetState_Radius write SetState_Radius;
property Transparent: Boolean read GetState_Transparent write SetState_Transparent;
function GetState_IsSolid: Boolean;
function GetState_LineWidth: TSize;
function GetState_Radius: Integer;
function GetState_Transparent: Boolean;
procedure SetState_IsSolid(ASolid: Boolean);
procedure SetState_LineWidth(AWidth: TSize);
procedure SetState_Radius(ARadius: Integer);
procedure SetState_Transparent(B: Boolean);

## ISch_CollapsiblePolygon
继承：ISch_CollapsiblePolygon → ISch_Polygon → ISch_GraphicalObject → ISch_BasicContainer → IInterface ｜ 单元：Rt_Schematic ｜ 自有 2 个方法、1 个属性

property Collapsed: Boolean read GetState_Collapsed write SetState_Collapsed;
function GetState_Collapsed: Boolean;
procedure SetState_Collapsed(B: Boolean);

## ISch_CollapsibleRectangle
继承：ISch_CollapsibleRectangle → ISch_Rectangle → ISch_GraphicalObject → ISch_BasicContainer → IInterface ｜ 单元：Rt_Schematic ｜ 自有 2 个方法、1 个属性

property Collapsed: Boolean read GetState_Collapsed write SetState_Collapsed;
function GetState_Collapsed: Boolean;
procedure SetState_Collapsed(B: Boolean);

## ISch_CompileMask
继承：ISch_CompileMask → ISch_CollapsibleRectangle → ISch_Rectangle → ISch_GraphicalObject → ISch_BasicContainer → IInterface ｜ 单元：Rt_Schematic ｜ 自有 0 个方法、0 个属性


## ISch_ComplexText
继承：ISch_ComplexText → ISch_Label → ISch_GraphicalObject → ISch_BasicContainer → IInterface ｜ 单元：Rt_Schematic ｜ 自有 8 个方法、4 个属性

property Autoposition: Boolean read GetState_Autoposition write SetState_Autoposition;
property IsHidden: Boolean read GetState_IsHidden write SetState_IsHidden;
property TextHorzAnchor: TTextHorzAnchor read GetState_TextHorzAnchor write SetState_TextHorzAnchor;
property TextVertAnchor: TTextVertAnchor read GetState_TextVertAnchor write SetState_TextVertAnchor;
function GetState_Autoposition: Boolean;
function GetState_IsHidden: Boolean;
function GetState_TextHorzAnchor: TTextHorzAnchor;
function GetState_TextVertAnchor: TTextVertAnchor;
procedure SetState_Autoposition(B: Boolean);
procedure SetState_IsHidden(B: Boolean);
procedure SetState_TextHorzAnchor(A: TTextHorzAnchor);
procedure SetState_TextVertAnchor(A: TTextVertAnchor);

## ISch_Component
继承：ISch_Component → ISch_ParametrizedGroup → ISch_GraphicalObject → ISch_BasicContainer → IInterface ｜ 单元：Rt_Schematic ｜ 自有 138 个方法、52 个属性

property Alias[I: Integer]: WideString read GetState_AliasAt write SetState_AliasAt;
property AliasAsText: WideString read GetState_AliasAsText write SetState_AliasAsText;
property AliasCount: Integer read GetState_AliasCount;  // read-only
property Comment: ISch_Parameter read GetState_SchComment;  // read-only
property ComponentDescription: WideString read GetState_ComponentDescription write SetState_ComponentDescription;
property ComponentKind: TComponentKind read GetState_ComponentKind write SetState_ComponentKind;
property ConfigurationParameters: WideString read GetState_ConfigurationParameters;  // read-only
property ConfiguratorName: WideString read GetState_ConfiguratorName;  // read-only
property CurrentPartID: Integer read GetState_CurrentPartID write SetState_CurrentPartID;
property DatabaseLibraryName: WideString read GetState_DatabaseLibraryName;  // read-only
property DatabaseTableName: WideString read GetState_DatabaseTableName write SetState_DatabaseTableName;
property Designator: ISch_Designator read GetState_SchDesignator;  // read-only
property DesignatorLocked: Boolean read GetState_DesignatorLocked write SetState_DesignatorLocked;
property DesignItemId: WideString read GetState_DesignItemId write SetState_DesignItemId;
property DisplayFieldNames: Boolean read GetState_DisplayFieldNames write SetState_DisplayFieldNames;
property DisplayMode: TDisplayMode read GetState_DisplayMode write SetState_DisplayMode;
property DisplayModeCount: Integer read GetState_DisplayModeCount write SetState_DisplayModeCount_Check;
property GenericComponentTemplateGUID: WideString read GetState_GenericComponentTemplateGuid write SetState_GenericComponentTemplateGuid;
property IsMirrored: Boolean read GetState_IsMirrored write SetState_IsMirrored;
property IsUnmanaged: Boolean read GetState_IsUnmanaged;  // read-only
property IsUserConfigurable: Boolean read GetState_IsUserConfigurable write SetState_IsUserConfigurable;
property ItemGUID: WideString read GetState_ItemGUID write SetState_ItemGUID;
property LibIdentifierKind: TLibIdentifierKind read GetState_LibIdentifierKind;  // read-only
property LibraryIdentifier: WideString read GetState_LibraryIdentifier;  // read-only
property LibraryPath: WideString read GetState_LibraryPath write SetState_LibraryPath;
property LibReference: WideString read GetState_LibReference write SetState_LibReference;
property Orientation: TRotationBy90 read GetState_Orientation write SetState_Orientation;
property OverideColors: Boolean read GetState_OverideColors write SetState_OverideColors;
property PartCount: Integer read GetState_PartCountNoPart0 write SetState_PartCountNoPart0;
property PartIdLocked: Boolean read GetState_PartIdLocked write SetState_PartIdLocked;
property PinColor: TColor read GetState_PinColor write SetState_PinColor;
property PinsMoveable: Boolean read GetState_PinsMoveable write SetState_PinsMoveable;
property RevisionDetails: WideString read GetState_RevisionDetails;  // read-only
property RevisionGUID: WideString read GetState_RevisionGUID write SetState_RevisionGUID;
property RevisionHRID: WideString read GetState_RevisionHRID;  // read-only
property RevisionState: WideString read GetState_RevisionState;  // read-only
property RevisionStatus: WideString read GetState_RevisionStatus;  // read-only
property SelectedInLibrary: Boolean read GetState_SelectedInLibrary write SetState_SelectedInLibrary;
property SheetPartFileName: WideString read GetState_SheetPartFileName write SetState_SheetPartFileName;
property ShowHiddenFields: Boolean read GetState_ShowHiddenFields write SetState_ShowHiddenFields;
property ShowHiddenPins: Boolean read GetState_ShowHiddenPins write SetState_ShowHiddenPins;
property SourceLibraryName: WideString read GetState_SourceLibraryName write SetState_SourceLibraryName;
property SymbolItemGUID: WideString read GetState_SymbolItemGUID write SetState_SymbolItemGUID;
property SymbolReference: WideString read GetState_SymbolReference write SetState_SymbolReference;
property SymbolRevisionGUID: WideString read GetState_SymbolRevisionGUID write SetState_SymbolRevisionGUID;
property SymbolVaultGUID: WideString read GetState_SymbolVaultGUID write SetState_SymbolVaultGUID;
property TargetFileName: WideString read GetState_TargetFileName write SetState_TargetFileName;
property UseDBTableName: Boolean read GetState_UseDBTableName write SetState_UseDBTableName;
property UseLibraryName: Boolean read GetState_UseLibraryName write SetState_UseLibraryName;
property VariantOption: IVariantOption read GetState_VariantOption write SetState_VariantOption;
property VaultGUID: WideString read GetState_VaultGUID write SetState_VaultGUID;
property VaultHRID: WideString read GetState_VaultHRID;  // read-only
procedure AddDisplayMode;
procedure AddImplementationToComponent(AnImplementation: ISch_Implementation);
procedure AddPart;
function AddPin: ISch_Pin;
function AddSchImplementation: ISch_Implementation;
function AddSchParameter: ISch_Parameter;
procedure Alias_Add(S: WideString);
procedure Alias_Clear;
procedure Alias_Delete(I: Integer);
procedure Alias_Remove(S: WideString);
procedure ApplyChosenComponent(const DestComponent: IDispatch);
function ChangeComponentLibraryToLibrary(LibraryName: WideString; TableName: WideString; AllowSelectNew: Boolean; Action: TSourceChangeAction): TSourceChangeAction;
function ChangeComponentLibraryToVault(AVaultGUID: WideString; AllowSelectNew: Boolean; Action: TSourceChangeAction): TSourceChangeAction;
function ChooseFromLibrary: IDispatch;
function ChooseFromVault: IDispatch;
procedure DeleteDisplayMode(AMode: Byte);
procedure DeletePart(APartId: Integer);
function EditPins: Boolean;
function EditPinsWithSelection(ASelectedPins: ISafeInterfaceList): Boolean;
function FullPartDesignator(APartId: Integer): WideString;
function GetAllPinCount: Integer;
function GetEmptyImplementation: ISch_Implementation;
function GetGraphicalHash: WideString;
function GetState_AliasAsText: WideString;
function GetState_AliasAt(I: Integer): WideString;
function GetState_AliasCount: Integer;
function GetState_ComponentDescription: WideString;
function GetState_ComponentKind: TComponentKind;
function GetState_ConfigurationParameters: WideString;
function GetState_ConfiguratorName: WideString;
function GetState_CurrentPartID: Integer;
function GetState_CustomDisplayModeName(ADisplayMode: Byte): WideString;
function GetState_DatabaseLibraryKeys(ADelimiter: WideString): WideString;
function GetState_DatabaseLibraryName: WideString;
function GetState_DatabaseTableName: WideString;
function GetState_DesignatorLocked: Boolean;
function GetState_DesignItemId: WideString;
function GetState_DisplayFieldNames: Boolean;
function GetState_DisplayMode: Byte;
function GetState_DisplayModeCount: Integer;
function GetState_GenericComponentTemplateGuid: WideString;
function GetState_IsMirrored: Boolean;
function GetState_IsUnmanaged: Boolean;
function GetState_IsUserConfigurable: Boolean;
function GetState_ItemGUID: WideString;
function GetState_LibIdentifierKind: TLibIdentifierKind;
function GetState_LibraryIdentifier: WideString;
function GetState_LibraryPath: WideString;
function GetState_LibReference: WideString;
function GetState_Orientation: TRotationBy90;
function GetState_OverideColors: Boolean;
function GetState_PartCountNoPart0: Integer;
function GetState_PartIdLocked: Boolean;
function GetState_PinColor: TColor;
function GetState_PinsMoveable: Boolean;
function GetState_RevisionDetails: WideString;
function GetState_RevisionGUID: WideString;
function GetState_RevisionHRID: WideString;
function GetState_RevisionState: WideString;
function GetState_RevisionStatus: WideString;
function GetState_SchComment: ISch_Parameter;
function GetState_SchDesignator: ISch_Designator;
function GetState_SelectedInLibrary: Boolean;
function GetState_SheetPartFileName: WideString;
function GetState_ShowHiddenFields: Boolean;
function GetState_ShowHiddenPins: Boolean;
function GetState_SourceLibraryName: WideString;
function GetState_SymbolItemGUID: WideString;
function GetState_SymbolReference: WideString;
function GetState_SymbolRevisionGUID: WideString;
function GetState_SymbolVaultGUID: WideString;
function GetState_TargetFileName: WideString;
function GetState_UseDBTableName: Boolean;
function GetState_UseLibraryName: Boolean;
function GetState_VariantOption: IVariantOption;
function GetState_VaultGUID: WideString;
function GetState_VaultHRID: WideString;
function HasConfiguredPinMapping: Boolean;
function InLibrary: Boolean;
function InSheet: Boolean;
function IsGenericComponent: Boolean;
function IsIntegratedComponent: Boolean;
function IsMultiPartComponent: Boolean;
procedure JumpTo(APin: ISch_Pin);
procedure OffsetParameters_Default;
function PartIdString(APartId: Integer): WideString;
procedure RemovePins(APins: ISafeInterfaceList);
procedure RemoveSchImplementation(AnImplementation: ISch_Implementation);
procedure SaveToFile(VFSAddress: WideString);
procedure SetState_AliasAsText(AValue: WideString);
procedure SetState_AliasAt(I: Integer; AValue: WideString);
procedure SetState_ComponentDescription(AValue: WideString);
procedure SetState_ComponentKind(AValue: TComponentKind);
procedure SetState_CurrentPartID(AValue: Integer);
procedure SetState_CustomDisplayModeName(ADisplayMode: Byte; AValue: WideString);
procedure SetState_DatabaseTableName(AValue: WideString);
procedure SetState_DesignatorLocked(AValue: Boolean);
procedure SetState_DesignItemId(AValue: WideString);
procedure SetState_DisplayFieldNames(AValue: Boolean);
procedure SetState_DisplayMode(AValue: Byte);
procedure SetState_DisplayModeCount_Check(AValue: Integer);
procedure SetState_FilePosition(AValue: Integer);
procedure SetState_GenericComponentTemplateGuid(AValue: WideString);
procedure SetState_IsMirrored(AValue: Boolean);
procedure SetState_IsUserConfigurable(AValue: Boolean);
procedure SetState_ItemGUID(AValue: WideString);
procedure SetState_LibraryPath(AValue: WideString);
procedure SetState_LibReference(AValue: WideString);
procedure SetState_Orientation(AValue: TRotationBy90);
procedure SetState_OrientationWithoutRotating(AValue: TRotationBy90);
procedure SetState_OverideColors(AValue: Boolean);
procedure SetState_PartCountNoPart0(AValue: Integer);
procedure SetState_PartIdLocked(AValue: Boolean);
procedure SetState_PinColor(AValue: TColor);
procedure SetState_PinsMoveable(AValue: Boolean);
procedure SetState_RevisionGUID(AValue: WideString);
procedure SetState_SelectedInLibrary(AValue: Boolean);
procedure SetState_SheetPartFileName(AValue: WideString);
procedure SetState_ShowHiddenFields(AValue: Boolean);
procedure SetState_ShowHiddenPins(AValue: Boolean);
procedure SetState_SourceLibraryName(AValue: WideString);
procedure SetState_SymbolItemGUID(AValue: WideString);
procedure SetState_SymbolReference(AValue: WideString);
procedure SetState_SymbolRevisionGUID(AValue: WideString);
procedure SetState_SymbolVaultGUID(AValue: WideString);
procedure SetState_TargetFileName(AValue: WideString);
procedure SetState_UseDBTableName(AValue: Boolean);
procedure SetState_UseLibraryName(AValue: Boolean);
procedure SetState_VariantOption(AValue: IVariantOption);
procedure SetState_VaultGUID(AValue: WideString);
procedure ShowInVaultExplorer;
procedure ShowLibraryInExplorer;
function SuggestedSearchKeywords: WideString;
procedure UpdatePart_PostProcess;
procedure UpdatePart_PreProcess;
procedure UpdatePrimitivesAccessibility;
procedure ValidateImplementationsCurrentState;
procedure ValidateLink;

## ISch_ConnectionLine
继承：ISch_ConnectionLine → ISch_BusEntry → ISch_Line → ISch_GraphicalObject → ISch_BasicContainer → IInterface ｜ 单元：Rt_Schematic ｜ 自有 2 个方法、1 个属性

property IsInferred: Boolean read GetState_IsInferred write SetState_IsInferred;
function GetState_IsInferred: Boolean;
procedure SetState_IsInferred(B: Boolean);

## ISch_ConnectivityStorage
继承：ISch_ConnectivityStorage → ISch_BasicContainer → IInterface ｜ 单元：Rt_Schematic ｜ 自有 0 个方法、0 个属性


## ISch_CrossReferenceObject
继承：ISch_CrossReferenceObject → IInterface ｜ 单元：Rt_Schematic ｜ 自有 1 个方法、1 个属性

property CrossRefObjectsInfo: WideString read GetState_CrossRefObjectsInfo;  // read-only
function GetState_CrossRefObjectsInfo: WideString;

## ISch_CrossSheetConnector
继承：ISch_CrossSheetConnector → ISch_PowerObject → ISch_Label → ISch_GraphicalObject → ISch_BasicContainer → IInterface ｜ 单元：Rt_Schematic ｜ 自有 5 个方法、1 个属性

property CrossSheetStyle: TCrossSheetConnectorStyle read GetCrossSheetConnectorStyle write SetCrossSheetConnectorStyle;
procedure DeleteCrossRef;
function GetCrossSheetConnectorStyle: TCrossSheetConnectorStyle;
function GetState_CrossRef: WideString;
procedure SetCrossSheetConnectorStyle(const Value: TCrossSheetConnectorStyle);
procedure SetState_CrossRef(AValue: WideString);

## ISch_DataModelUtils
继承：ISch_DataModelUtils → IInterface ｜ 单元：Rt_Schematic ｜ 自有 7 个方法、0 个属性

function ChangeComponentsLibraryToLibrary(SchComponents: ISafeInterfaceList; LibraryName: WideString; TableName: WideString; AllowSelectNew: Boolean): Boolean;
function ChangeComponentsLibraryToVault(SchComponents: ISafeInterfaceList; VaultGUID: WideString; AllowSelectNew: Boolean): Boolean;
function DecomposePinNameToPinFunctions(const PinName: WideString): ISafeInterfaceList;
function GetComponentSubPartsInfo(AComponent: ISch_Component): IComponentSubPartsInfo;
function GetManagedSheetParentSymbolsInfo(ASheetSymbol: ISch_SheetSymbol): IManagedSheetParentSymbolsInfo;
procedure UpdateComponentSubPartsToGivenRevision(AComponentSubPartsInfo: IComponentSubPartsInfo; AVaultGUID: WideString; AItemGUID: WideString; ARevisionGUID: WideString; ADesignItemID: WideString; ASourceLibraryName: WideString);
procedure UpdateManagedSheetParentSymbolsToGivenRevision(AManagedSheetParentSymbolsInfo: IManagedSheetParentSymbolsInfo; AVaultGUID: WideString; AItemGUID: WideString; ARevisionGUID: WideString);

## ISch_Designator
继承：ISch_Designator → ISch_Parameter → ISch_ComplexText → ISch_Label → ISch_GraphicalObject → ISch_BasicContainer → IInterface ｜ 单元：Rt_Schematic ｜ 自有 2 个方法、1 个属性

property PhysicalDesignator: WideString read GetState_PhysicalDesignator write SetState_PhysicalDesignator;
function GetState_PhysicalDesignator: WideString;
procedure SetState_PhysicalDesignator(AValue: WideString);

## ISch_DialogManager
继承：ISch_DialogManager → ISch_DialogManagerEntry → IInterface ｜ 单元：Rt_Schematic ｜ 自有 0 个方法、0 个属性


## ISch_DialogManagerEntry
继承：ISch_DialogManagerEntry → IInterface ｜ 单元：Rt_Schematic ｜ 自有 2 个方法、0 个属性

function ShowPrintOutPropertiesDialog(Settings: IPrintSettings): Boolean;
function ShowPrintPreviewDialog(Settings: IPrintSettings): Boolean;

## ISch_Directive
继承：ISch_Directive → ISch_GraphicalObject → ISch_BasicContainer → IInterface ｜ 单元：Rt_Schematic ｜ 自有 0 个方法、1 个属性

property Text: WideString read GetState_Text write SetState_Text;

## ISch_Document
继承：ISch_Document → ISch_ParametrizedGroup → ISch_GraphicalObject → ISch_BasicContainer → IInterface ｜ 单元：Rt_Schematic ｜ 自有 114 个方法、46 个属性

property BorderOn: Boolean read GetState_BorderOn write SetState_BorderOn;
property CustomMarginWidth: TCoord read GetState_CustomMarginWidth write SetState_CustomMarginWidth;
property CustomSheetStyle: WideString read GetState_CustomSheetStyle write SetState_CustomSheetStyle;
property CustomX: TCoord read GetState_CustomX write SetState_CustomX;
property CustomXZones: TCoord read GetState_CustomXZones write SetState_CustomXZones;
property CustomY: TCoord read GetState_CustomY write SetState_CustomY;
property CustomYZones: TCoord read GetState_CustomYZones write SetState_CustomYZones;
property DisplayUnit: TUnit read GetState_Unit write SetState_Unit;
property DocumentBorderStyle: TSheetDocumentBorderStyle read GetState_DocumentBorderStyle write SetState_DocumentBorderStyle;
property DocumentName: WideString read GetState_DocumentName;  // read-only
property HotspotGridOn: Boolean read GetState_HotspotGridOn write SetState_HotspotGridOn;
property HotspotGridSize: TCoord read GetState_HotspotGridSize write SetState_HotspotGridSize;
property InternalTolerance: TCoord read GetState_InternalTolerance;  // read-only
property ItemRevisionGUID: WideString read GetState_ItemRevisionGUID write SetState_ItemRevisionGUID;
property LoadFormat: WideString read GetState_LoadFormat write SetState_LoadFormat;
property MinorVersion: Integer read GetState_MinorVersion;  // read-only
property PropsRevisionGUID: WideString read GetPropsRevisionGUID;  // read-only
property PropsVaultGUID: WideString read GetPropsVaultGUID;  // read-only
property ReferenceZonesOn: Boolean read GetState_ReferenceZonesOn write SetState_ReferenceZonesOn;
property ReferenceZoneStyle: TSheetReferenceZoneStyle read GetState_ReferenceZoneStyle write SetState_ReferenceZoneStyle;
property ReleaseItemGUID: WideString read GetState_ReleaseItemGUID write SetState_ReleaseItemGUID;
property ReleaseVaultGUID: WideString read GetState_ReleaseVaultGUID write SetState_ReleaseVaultGUID;
property SchDocID: Integer read GetState_SchDocID;  // read-only
property SheetMarginWidth: TCoord read GetState_SheetMarginWidth write SetState_SheetMarginWidth;
property SheetNumberSpaceSize: Integer read GetState_SheetNumberSpaceSize write SetState_SheetNumberSpaceSize;
property SheetSizeX: TCoord read GetState_SheetSizeX write SetState_SheetSizeX;
property SheetSizeY: TCoord read GetState_SheetSizeY write SetState_SheetSizeY;
property SheetStyle: TSheetStyle read GetState_SheetStyle write SetState_SheetStyle;
property SheetZonesX: Integer read GetState_SheetZonesX write SetState_SheetZonesX;
property SheetZonesY: Integer read GetState_SheetZonesY write SetState_SheetZonesY;
property ShowTemplateGraphics: Boolean read GetState_ShowTemplateGraphics write SetState_ShowTemplateGraphics;
property SnapGridOn: Boolean read GetState_SnapGridOn write SetState_SnapGridOn;
property SnapGridSize: TCoord read GetState_SnapGridSize write SetState_SnapGridSize;
property SystemFont: TFontID read GetState_SystemFont write SetState_SystemFont;
property TemplateFileName: WideString read GetState_TemplateFileName write SetState_TemplateFileName;
property TemplateItemGUID: WideString read GetTemplateItemGUID;  // read-only
property TemplateRevisionGUID: WideString read GetTemplateRevisionGUID;  // read-only
property TemplateRevisionHRID: WideString read GetTemplateRevisionHRID;  // read-only
property TemplateVaultGUID: WideString read GetTemplateVaultGUID;  // read-only
property TemplateVaultHRID: WideString read GetTemplateVaultHRID;  // read-only
property TitleBlockOn: Boolean read GetState_TitleBlockOn write SetState_TitleBlockOn;
property UnitSystem: TUnitSystem read GetState_UnitSystem;  // read-only
property UseCustomSheet: Boolean read GetState_UseCustomSheet write SetState_UseCustomSheet;
property VisibleGridOn: Boolean read GetState_VisibleGridOn write SetState_VisibleGridOn;
property VisibleGridSize: TCoord read GetState_VisibleGridSize write SetState_VisibleGridSize;
property WorkspaceOrientation: TSheetOrientation read GetState_WorkspaceOrientation write SetState_WorkspaceOrientation;
function BoundingRectangle_Selected: IDispatch;
function ChooseLocationInteractively(const ALocation: IDispatch; Prompt: WideString): Boolean;
function ChooseRectangleInteractively(const ARect: IDispatch; Prompt1: WideString; Prompt2: WideString): Boolean;
function CountContextMenuObjects(AObjectSet: TObjectSet): Integer;
function CreateFilteredHitTest(const ATestMode: THitTestMode; const ALocation: IDispatch; const AObjectSet: TObjectSet; const AParentObjectSet: TObjectSet; const AIncludePins: Boolean; const ACrossSelect: Boolean): ISch_HitTest;
function CreateHitTest(ATestMode: THitTestMode; const ALocation: IDispatch): ISch_HitTest;
procedure CreateLibraryFromProject(AddLibToProject: Boolean; FileName: WideString; RunQuiet: Boolean);
function CreateUseHandle(const AGraphicalObject: ISch_GraphicalObject; const AView: IInterface; const ALocation: IDispatch): ISch_HitTest;
procedure DocumentModifiedChanged(AChanged: Boolean);
function GenerateUniqueID: WideString;
function GetDialogManager: ISch_DialogManager;
function GetPropsRevisionGUID: WideString;
function GetPropsVaultGUID: WideString;
function GetState_BorderOn: Boolean;
function GetState_CustomMarginWidth: Integer;
function GetState_CustomSheetStyle: WideString;
function GetState_CustomX: Integer;
function GetState_CustomXZones: Integer;
function GetState_CustomY: Integer;
function GetState_CustomYZones: Integer;
function GetState_DocumentBorderStyle: TSheetDocumentBorderStyle;
function GetState_DocumentName: WideString;
function GetState_HotspotGridOn: Boolean;
function GetState_HotspotGridSize: Integer;
function GetState_InternalTolerance: Integer;
function GetState_ItemRevisionGUID: WideString;
function GetState_LoadFormat: WideString;
function GetState_MinorVersion: Integer;
function GetState_ReferenceZonesOn: Boolean;
function GetState_ReferenceZoneStyle: TSheetReferenceZoneStyle;
function GetState_ReleaseItemGUID: WideString;
function GetState_ReleaseVaultGUID: WideString;
function GetState_SchDocID: Integer;
function GetState_SheetMarginWidth: Integer;
function GetState_SheetNumberSpaceSize: Integer;
function GetState_SheetSizeX: Integer;
function GetState_SheetSizeY: Integer;
function GetState_SheetStyle: TSheetStyle;
function GetState_SheetZonesX: Integer;
function GetState_SheetZonesY: Integer;
function GetState_ShowTemplateGraphics: Boolean;
function GetState_SnapGridOn: Boolean;
function GetState_SnapGridSize: Integer;
function GetState_SystemFont: Integer;
function GetState_TemplateFileName: WideString;
function GetState_TitleBlockOn: Boolean;
function GetState_Unit: TUnit;
function GetState_UnitSystem: TUnitSystem;
function GetState_UseCustomSheet: Boolean;
function GetState_VisibleGridOn: Boolean;
function GetState_VisibleGridSize: Integer;
function GetState_WorkspaceOrientation: TSheetOrientation;
function GetTemplateItemGUID: WideString;
function GetTemplateRevisionGUID: WideString;
function GetTemplateRevisionHRID: WideString;
function GetTemplateVaultGUID: WideString;
function GetTemplateVaultHRID: WideString;
function Graphical_VirtualRectangle: IDispatch;
function GridCoordinateClosest(ACoord: Integer): Integer;
function GridCoordinateUp(ACoord: Integer): Integer;
function HasPausedProcess: Boolean;
function HasServerDocument: Boolean;
function IsInEditorView: Boolean;
procedure LockViewUpdate;
procedure Notify_FullUpdate;
function ObjectReferenceZone(AObject: ISch_BasicContainer): WideString;
procedure OptimizeUseOfPolylines;
procedure PlaceSchComponent(ALibraryPath: WideString; ALibRef: WideString; var SchObject: ISch_Component);
function PopupMenuHitTest: ISch_HitTest;
procedure RecreateHandles;
procedure RedrawToDC(DC: HDC; PrintKind: Integer; PrintWhat: Integer);
procedure RegisterSchObjectInContainer(AObject: ISch_BasicContainer);
procedure SetPreferencesInfo(const AVaultGUID: WideString; const ARevisionGUID: WideString);
procedure SetState_BorderOn(AValue: Boolean);
procedure SetState_CustomMarginWidth(AValue: Integer);
procedure SetState_CustomSheetStyle(AValue: WideString);
procedure SetState_CustomX(AValue: Integer);
procedure SetState_CustomXZones(AValue: Integer);
procedure SetState_CustomY(AValue: Integer);
procedure SetState_CustomYZones(AValue: Integer);
procedure SetState_DocumentBorderStyle(AValue: TSheetDocumentBorderStyle);
procedure SetState_HotspotGridOn(AValue: Boolean);
procedure SetState_HotspotGridSize(AValue: Integer);
procedure SetState_ItemRevisionGUID(const AValue: WideString);
procedure SetState_LoadFormat(AValue: WideString);
procedure SetState_ReferenceZonesOn(AValue: Boolean);
procedure SetState_ReferenceZoneStyle(AValue: TSheetReferenceZoneStyle);
procedure SetState_ReleaseItemGUID(const AValue: WideString);
procedure SetState_ReleaseVaultGUID(const AValue: WideString);
procedure SetState_SheetMarginWidth(AValue: Integer);
procedure SetState_SheetNumberSpaceSize(AValue: Integer);
procedure SetState_SheetSizeX(AValue: Integer);
procedure SetState_SheetSizeY(AValue: Integer);
procedure SetState_SheetStyle(AValue: TSheetStyle);
procedure SetState_SheetZonesX(AValue: Integer);
procedure SetState_SheetZonesY(AValue: Integer);
procedure SetState_ShowTemplateGraphics(AValue: Boolean);
procedure SetState_SnapGridOn(AValue: Boolean);
procedure SetState_SnapGridSize(AValue: Integer);
procedure SetState_SystemFont(AValue: Integer);
procedure SetState_TemplateFileName(AValue: WideString);
procedure SetState_TitleBlockOn(AValue: Boolean);
procedure SetState_Unit(AValue: TUnit);
procedure SetState_UseCustomSheet(AValue: Boolean);
procedure SetState_VisibleGridOn(AValue: Boolean);
procedure SetState_VisibleGridSize(AValue: Integer);
procedure SetState_WorkspaceOrientation(AValue: TSheetOrientation);
procedure SetTemplateInfo(const AVaultGUID: WideString; const AItemGUID: WideString; const ARevisionGUID: WideString; const AVaultHRID: WideString; const ARevisionHRID: WideString);
procedure UnLockViewUpdate;
procedure UnregisterAndFreeAllConnectionLines;
procedure UnRegisterSchObjectFromContainer(AObject: ISch_BasicContainer);
procedure UpdateDisplayForCurrentSheet;
procedure UpdateDocumentProperties;
function UpdatePartsToLatestRevision(ATarget: TUpdatePartTarget; const AContextObject: IInterface; ANeedConfirm: Boolean; AClearMessages: Boolean; out AUpdatedCount: Integer; out AUpToDateCount: Integer; out AErrorCount: Integer): Boolean;

## ISch_DrawableDocument
继承：ISch_DrawableDocument → IInterface ｜ 单元：Rt_Schematic ｜ 自有 1 个方法、0 个属性

procedure RedrawTo(GraphicCanvas: IInterface; PrintKind: Integer; PrintWhat: Integer);

## ISch_Ellipse
继承：ISch_Ellipse → ISch_Circle → ISch_GraphicalObject → ISch_BasicContainer → IInterface ｜ 单元：Rt_Schematic ｜ 自有 2 个方法、1 个属性

property SecondaryRadius: TDistance read GetState_SecondaryRadius write SetState_SecondaryRadius;
function GetState_SecondaryRadius: Integer;
procedure SetState_SecondaryRadius(ARadius: Integer);

## ISch_EllipticalArc
继承：ISch_EllipticalArc → ISch_Arc → ISch_GraphicalObject → ISch_BasicContainer → IInterface ｜ 单元：Rt_Schematic ｜ 自有 2 个方法、1 个属性

property SecondaryRadius: TDistance read GetState_SecondaryRadius write SetState_SecondaryRadius;
function GetState_SecondaryRadius: Integer;
procedure SetState_SecondaryRadius(ARadius: Integer);

## ISch_ErrorMarker
继承：ISch_ErrorMarker → ISch_Directive → ISch_GraphicalObject → ISch_BasicContainer → IInterface ｜ 单元：Rt_Schematic ｜ 自有 0 个方法、0 个属性


## ISch_FontManager
继承：ISch_FontManager → IInterface ｜ 单元：Rt_Schematic ｜ 自有 17 个方法、11 个属性

property Bold[AnId: Integer]: Boolean read GetState_Bold;  // read-only
property DefaultHorizontalSysFontId: Integer read GetState_DefaultHorizontalSysFontId;  // read-only
property DefaultVerticalSysFontId: Integer read GetState_DefaultVerticalSysFontId;  // read-only
property FontCount: Integer read GetState_FontCount;  // read-only
property FontName[AnId: Integer]: TFontName read GetState_FontName;  // read-only
property Italic[AnId: Integer]: Boolean read GetState_Italic;  // read-only
property Rotation[AnId: Integer]: Integer read GetState_Rotation;  // read-only
property SaveFlag[AnId: Integer]: Boolean read GetState_SaveFlag;  // read-only
property Size[AnId: Integer]: Integer read GetState_Size;  // read-only
property StrikeOut[AnId: Integer]: Boolean read GetState_StrikeOut;  // read-only
property Underline[AnId: Integer]: Boolean read GetState_UnderLine;  // read-only
function GetFontHandle(AnId: Integer; const CurrentLogFont: IDispatch; ScreenSize: Integer): NativeUInt;
function GetFontID(Size: Integer; Rotation: Integer; Underline: Boolean; Italic: Boolean; Bold: Boolean; StrikeOut: Boolean; const FontName: WideString): Integer;
function GetFontSize(FontID: Integer): Integer;
procedure GetFontSpec(FontID: Integer; var Size: Integer; var Rotation: Integer; var Underline: Boolean; var Italic: Boolean; var Bold: Boolean; var StrikeOut: Boolean; var FontName: WideString);
function GetState_Bold(AnId: Integer): Boolean;
function GetState_DefaultHorizontalSysFontId: Integer;
function GetState_DefaultVerticalSysFontId: Integer;
function GetState_FontCount: Integer;
function GetState_FontName(AnId: Integer): WideString;
function GetState_Italic(AnId: Integer): Boolean;
function GetState_Rotation(AnId: Integer): Integer;
function GetState_SaveFlag(AnId: Integer): Boolean;
function GetState_Size(AnId: Integer): Integer;
function GetState_StrikeOut(AnId: Integer): Boolean;
function GetState_UnderLine(AnId: Integer): Boolean;
function Import_FromUser(var FontID: Integer): Boolean;
function IsFontVertical(FontID: Integer): Boolean;

## ISch_FontManager2
继承：ISch_FontManager2 → IInterface ｜ 单元：Rt_Schematic ｜ 自有 17 个方法、0 个属性

function GetFontHandle(AnId: Integer; const CurrentLogFont: IDispatch; ScreenSize: Integer): NativeUInt;
function GetFontID(Size: Integer; Rotation: Integer; Underline: Boolean; Italic: Boolean; Bold: Boolean; StrikeOut: Boolean; const FontName: WideString): Integer;
function GetFontSize(FontID: Integer): Integer;
procedure GetFontSpec(FontID: Integer; var Size: Integer; var Rotation: Integer; var Underline: Boolean; var Italic: Boolean; var Bold: Boolean; var StrikeOut: Boolean; var FontName: WideString);
function GetState_Bold(AnId: Integer): Boolean;
function GetState_DefaultHorizontalSysFontId: Integer;
function GetState_DefaultVerticalSysFontId: Integer;
function GetState_FontCount: Integer;
function GetState_FontName(AnId: Integer): WideString;
function GetState_Italic(AnId: Integer): Boolean;
function GetState_Rotation(AnId: Integer): Integer;
function GetState_SaveFlag(AnId: Integer): Boolean;
function GetState_Size(AnId: Integer): Integer;
function GetState_StrikeOut(AnId: Integer): Boolean;
function GetState_UnderLine(AnId: Integer): Boolean;
function Import_FromUser(var FontID: Integer): Boolean;
function IsFontVertical(FontID: Integer): Boolean;

## ISch_GraphicalObject
继承：ISch_GraphicalObject → ISch_BasicContainer → IInterface ｜ 单元：Rt_Schematic ｜ 自有 43 个方法、16 个属性

property AreaColor: TColor read GetState_AreaColor write SetState_AreaColor;
property Color: TColor read GetState_Color write SetState_Color;
property CompilationMasked: Boolean read GetState_CompilationMasked write SetState_CompilationMasked;
property Dimmed: Boolean read GetState_Dimmed write SetState_Dimmed;
property Disabled: Boolean read GetState_Disabled write SetState_Disabled;
property DisplayError: Boolean read GetState_DisplayError write SetState_DisplayError;
property EnableDraw: Boolean read GetState_EnableDraw write SetState_EnableDraw;
property ErrorColor: TColor read GetState_ErrorColor write SetState_ErrorColor;
property ErrorKind: TErrorKind read GetState_ErrorKind write SetState_ErrorKind;
property ErrorString: WideString read GetState_ErrorString write SetState_ErrorString;
property GraphicallyLocked: Boolean read GetState_GraphicallyLocked write SetState_GraphicallyLocked;
property LiveHighlightValue: WideString read GetState_LiveHighlightValue write SetState_LiveHighlightValue;
property Location: TLocation read GetState_Location write SetState_Location;
property OwnerPartDisplayMode: TDisplayMode read GetState_OwnerPartDisplayMode write SetState_OwnerPartDisplayMode;
property OwnerPartId: Integer read GetState_OwnerPartId write SetState_OwnerPartId;
property Selection: Boolean read GetState_Selection write SetState_Selection;
procedure AddErrorString(const AErrorString: WideString; AtEnd: LongBool);
function BoundingRectangle: IDispatch;
function BoundingRectangle_Full: IDispatch;
function GetHash: WideString;
function GetState_AreaColor: TColor;
function GetState_Color: TColor;
function GetState_CompilationMasked: Boolean;
function GetState_Dimmed: Boolean;
function GetState_Disabled: Boolean;
function GetState_DisplayError: Boolean;
function GetState_EnableDraw: Boolean;
function GetState_ErrorColor: TColor;
function GetState_ErrorKind: TErrorKind;
function GetState_ErrorString: WideString;
function GetState_GraphicallyLocked: Boolean;
function GetState_LiveHighlightValue: WideString;
function GetState_Location: IDispatch;
function GetState_OwnerPartDisplayMode: Byte;
function GetState_OwnerPartId: Integer;
function GetState_Selection: Boolean;
procedure GraphicallyInvalidate;
procedure Mirror(const Axis: IDispatch);
procedure MoveByXY(X: Integer; Y: Integer);
procedure MoveToXY(X: Integer; Y: Integer);
procedure ResetErrorFields;
procedure RotateBy90(const Center: IDispatch; A: TRotationBy90);
procedure SetState_AreaColor(AColor: TColor);
procedure SetState_Color(AColor: TColor);
procedure SetState_CompilationMasked(AValue: Boolean);
procedure SetState_Dimmed(B: Boolean);
procedure SetState_Disabled(B: Boolean);
procedure SetState_DisplayError(AValue: Boolean);
procedure SetState_EnableDraw(B: Boolean);
procedure SetState_ErrorColor(AValue: TColor);
procedure SetState_ErrorKind(AValue: TErrorKind);
procedure SetState_ErrorString(const AValue: WideString);
procedure SetState_GraphicallyLocked(AValue: Boolean);
procedure SetState_LiveHighlightValue(AValue: WideString);
procedure SetState_Location(const ALocation: IDispatch);
procedure SetState_OwnerPartDisplayMode(AValue: Byte);
procedure SetState_OwnerPartId(AValue: Integer);
procedure SetState_Selection(B: Boolean);
procedure SetState_xSizeySize;

## ISch_HarnessAssociatedPartsOwner
继承：ISch_HarnessAssociatedPartsOwner → IInterface ｜ 单元：Rt_Schematic ｜ 自有 8 个方法、0 个属性

function AddAssociatedPart: Boolean;
function GetAssociatedPart(Index: Integer): ISch_HarnessComponent;
function GetAssociatedPartsCount: Integer;
function GetFirstAssociatedPart: ISch_HarnessComponent;
procedure RemoveAllAssociatedParts;
procedure RemoveAssociatedPart(Index: Integer);
function SetAssociatedPart(Index: Integer): Boolean;
function SetFirstAssociatedPart: Boolean;

## ISch_HarnessBundle
继承：ISch_HarnessBundle → ISch_Wire → ISch_BasicPolyline → ISch_Polygon → ISch_GraphicalObject → ISch_BasicContainer → IInterface ｜ 单元：Rt_Schematic ｜ 自有 2 个方法、1 个属性

property Length: TDistance read GetState_Length write SetState_Length;
function GetState_Length: Integer;
procedure SetState_Length(ALength: Integer);

## ISch_HarnessBundleSubLineData
继承：ISch_HarnessBundleSubLineData → ISch_ConnectivityStorage → ISch_BasicContainer → IInterface ｜ 单元：Rt_Schematic ｜ 自有 0 个方法、0 个属性


## ISch_HarnessCable
继承：ISch_HarnessCable → ISch_Rectangle → ISch_GraphicalObject → ISch_BasicContainer → IInterface ｜ 单元：Rt_Schematic ｜ 自有 6 个方法、4 个属性

property Comment: ISch_Parameter read GetState_SchComment;  // read-only
property Designator: ISch_Designator read GetState_SchDesignator;  // read-only
property DesignatorLocked: Boolean read GetState_DesignatorLocked write SetState_DesignatorLocked;
property Orientation: TRotationBy90 read GetState_Orientation write SetState_Orientation;
function GetState_DesignatorLocked: Boolean;
function GetState_Orientation: TRotationBy90;
function GetState_SchComment: ISch_Parameter;
function GetState_SchDesignator: ISch_Designator;
procedure SetState_DesignatorLocked(AValue: Boolean);
procedure SetState_Orientation(ARotationBy90: TRotationBy90);

## ISch_HarnessCableData
继承：ISch_HarnessCableData → ISch_HarnessBundleSubLineData → ISch_ConnectivityStorage → ISch_BasicContainer → IInterface ｜ 单元：Rt_Schematic ｜ 自有 0 个方法、0 个属性


## ISch_HarnessComponent
继承：ISch_HarnessComponent → ISch_Component → ISch_ParametrizedGroup → ISch_GraphicalObject → ISch_BasicContainer → IInterface ｜ 单元：Rt_Schematic ｜ 自有 0 个方法、0 个属性


## ISch_HarnessConnector
继承：ISch_HarnessConnector → ISch_RectangularGroup → ISch_ParametrizedGroup → ISch_GraphicalObject → ISch_BasicContainer → IInterface ｜ 单元：Rt_Schematic ｜ 自有 14 个方法、6 个属性

property HarnessConnectorType: ISch_HarnessConnectorType read GetState_SchHarnessConnectorType;  // read-only
property HarnessType: WideString read GetState_HarnessType write SetState_HarnessType;
property HideHarnessConnectorType: Boolean read GetState_HideHarnessConnectorType write SetState_HideHarnessConnectorType;
property LineWidth: TSize read GetState_LineWidth write SetState_LineWidth;
property MasterEntryLocation: TLocation read GetState_MasterEntryLocation;  // read-only
property PrimaryConnectionPosition: TCoord read GetState_PrimaryConnectionPosition write SetState_PrimaryConnectionPosition;
function CreateEntry: ISch_HarnessEntry;
procedure DeleteEntry(const AEntry: ISch_HarnessEntry);
function GetState_HarnessType: WideString;
function GetState_HideHarnessConnectorType: Boolean;
function GetState_LineWidth: TSize;
function GetState_MasterEntryLocation: IDispatch;
function GetState_PrimaryConnectionPosition: Integer;
function GetState_SchHarnessConnectorType: ISch_HarnessConnectorType;
function GetState_Side: TLeftRightSide;
procedure SetState_HarnessType(AValue: WideString);
procedure SetState_HideHarnessConnectorType(AValue: Boolean);
procedure SetState_LineWidth(Value: TSize);
procedure SetState_PrimaryConnectionPosition(AValue: Integer);
procedure SetState_Side(AValue: TLeftRightSide);

## ISch_HarnessConnectorType
继承：ISch_HarnessConnectorType → ISch_ComplexText → ISch_Label → ISch_GraphicalObject → ISch_BasicContainer → IInterface ｜ 单元：Rt_Schematic ｜ 自有 0 个方法、0 个属性


## ISch_HarnessDocument
继承：ISch_HarnessDocument → ISch_Document → ISch_ParametrizedGroup → ISch_GraphicalObject → ISch_BasicContainer → IInterface ｜ 单元：Rt_Schematic ｜ 自有 0 个方法、0 个属性


## ISch_HarnessEntry
继承：ISch_HarnessEntry → ISch_GraphicalObject → ISch_BasicContainer → IInterface ｜ 单元：Rt_Schematic ｜ 自有 18 个方法、9 个属性

property DistanceFromTop: TCoord read GetState_DistanceFromTop write SetState_DistanceFromTop;
property HarnessType: WideString read GetState_HarnessType write SetState_HarnessType;
property Name: WideString read GetState_Name write SetState_Name;
property OverrideDisplayString: WideString read GetState_OverrideDisplayString write SetState_OverrideDisplayString;
property OwnerHarnessConnector: ISch_HarnessConnector read GetState_SchOwnerHarnessConnector;  // read-only
property Side: TLeftRightSide read GetState_Side write SetState_Side;
property TextColor: TColor read GetState_TextColor write SetState_TextColor;
property TextFontID: TFontID read GetState_TextFontID write SetState_TextFontID;
property TextStyle: TBusTextStyle read GetState_TextStyle write SetState_TextStyle;
function GetState_DistanceFromTop: Integer;
function GetState_HarnessType: WideString;
function GetState_Name: WideString;
function GetState_OverrideDisplayString: WideString;
function GetState_SchOwnerHarnessConnector: ISch_HarnessConnector;
function GetState_Side: TLeftRightSide;
function GetState_TextColor: TColor;
function GetState_TextFontID: Integer;
function GetState_TextStyle: TBusTextStyle;
function IsVertical: Boolean;
procedure SetState_DistanceFromTop(Value: Integer);
procedure SetState_HarnessType(Value: WideString);
procedure SetState_Name(Value: WideString);
procedure SetState_OverrideDisplayString(Value: WideString);
procedure SetState_Side(Value: TLeftRightSide);
procedure SetState_TextColor(Value: TColor);
procedure SetState_TextFontID(Value: Integer);
procedure SetState_TextStyle(Value: TBusTextStyle);

## ISch_HarnessLayoutConnectionPoint
继承：ISch_HarnessLayoutConnectionPoint → ISch_Label → ISch_GraphicalObject → ISch_BasicContainer → IInterface ｜ 单元：Rt_Schematic ｜ 自有 10 个方法、3 个属性

property BorderColor: TColor read GetState_BorderColor write SetState_BorderColor;
property ShowName: Boolean read GetState_ShowName write SetState_ShowName;
property Style: THarnessLayoutConnectionPointStyle read GetState_Style write SetState_Style;
function AddConnector(const ConnectorUniqueId: WideString): ISch_HarnessLayoutConnectionPointConnector;
function GetState_BorderColor: TColor;
function GetState_Connector(Index: Integer): ISch_HarnessLayoutConnectionPointConnector;
function GetState_ConnectorsCount: Integer;
function GetState_ShowName: Boolean;
function GetState_Style: THarnessLayoutConnectionPointStyle;
procedure RemoveConnector(const ConnectorUniqueId: WideString);
procedure SetState_BorderColor(AColor: TColor);
procedure SetState_ShowName(AValue: Boolean);
procedure SetState_Style(AStyle: THarnessLayoutConnectionPointStyle);

## ISch_HarnessLayoutConnectionPointConnector
继承：ISch_HarnessLayoutConnectionPointConnector → IInterface ｜ 单元：Rt_Schematic ｜ 自有 6 个方法、3 个属性

property PinId[const AIndex: Integer]: WideString read GetState_PinId;  // read-only
property PinsCount: Integer read GetState_PinsCount;  // read-only
property UniqueId: WideString read GetState_UniqueId write SetState_UniqueId;
procedure AddPin(const APinId: WideString);
function GetState_PinId(const AIndex: Integer): WideString;
function GetState_PinsCount: Integer;
function GetState_UniqueId: WideString;
procedure RemovePin(const APinId: WideString);
procedure SetState_UniqueId(const AValue: WideString);

## ISch_HarnessLayoutDrawing
继承：ISch_HarnessLayoutDrawing → ISch_HarnessDocument → ISch_Document → ISch_ParametrizedGroup → ISch_GraphicalObject → ISch_BasicContainer → IInterface ｜ 单元：Rt_Schematic ｜ 自有 0 个方法、0 个属性


## ISch_HarnessLayoutLabel
继承：ISch_HarnessLayoutLabel → ISch_Label → ISch_GraphicalObject → ISch_BasicContainer → IInterface ｜ 单元：Rt_Schematic ｜ 自有 3 个方法、2 个属性

property Designator: ISch_Designator read GetState_SchDesignator;  // read-only
property DesignatorLocked: Boolean read GetState_DesignatorLocked write SetState_DesignatorLocked;
function GetState_DesignatorLocked: Boolean;
function GetState_SchDesignator: ISch_Designator;
procedure SetState_DesignatorLocked(AValue: Boolean);

## ISch_HarnessLogicalSignal
继承：ISch_HarnessLogicalSignal → ISch_Line → ISch_GraphicalObject → ISch_BasicContainer → IInterface ｜ 单元：Rt_Schematic ｜ 自有 0 个方法、0 个属性


## ISch_HarnessNoConnect
继承：ISch_HarnessNoConnect → ISch_Label → ISch_GraphicalObject → ISch_BasicContainer → IInterface ｜ 单元：Rt_Schematic ｜ 自有 4 个方法、2 个属性

property ShowName: Boolean read GetState_ShowName write SetState_ShowName;
property Style: TNoERCSymbol read GetState_Style write SetState_Style;
function GetState_ShowName: Boolean;
function GetState_Style: TNoERCSymbol;
procedure SetState_ShowName(AShowName: Boolean);
procedure SetState_Style(AStyle: TNoERCSymbol);

## ISch_HarnessNoConnectData
继承：ISch_HarnessNoConnectData → ISch_ConnectivityStorage → ISch_BasicContainer → IInterface ｜ 单元：Rt_Schematic ｜ 自有 2 个方法、1 个属性

property Designator: WideString read GetState_Designator write SetState_Designator;
function GetState_Designator: WideString;
procedure SetState_Designator(const ADesignator: WideString);

## ISch_HarnessPin
继承：ISch_HarnessPin → ISch_Pin → ISch_ParametrizedGroup → ISch_GraphicalObject → ISch_BasicContainer → IInterface ｜ 单元：Rt_Schematic ｜ 自有 0 个方法、0 个属性


## ISch_HarnessShield
继承：ISch_HarnessShield → ISch_Rectangle → ISch_GraphicalObject → ISch_BasicContainer → IInterface ｜ 单元：Rt_Schematic ｜ 自有 4 个方法、2 个属性

property Orientation: TRotationBy90 read GetState_Orientation write SetState_Orientation;
property Style: THarnessShieldStyle read GetState_Style write SetState_Style;
function GetState_Orientation: TRotationBy90;
function GetState_Style: THarnessShieldStyle;
procedure SetState_Orientation(ARotationBy90: TRotationBy90);
procedure SetState_Style(AStyle: THarnessShieldStyle);

## ISch_HarnessShieldData
继承：ISch_HarnessShieldData → ISch_ConnectivityStorage → ISch_BasicContainer → IInterface ｜ 单元：Rt_Schematic ｜ 自有 0 个方法、0 个属性


## ISch_HarnessSplice
继承：ISch_HarnessSplice → ISch_Label → ISch_GraphicalObject → ISch_BasicContainer → IInterface ｜ 单元：Rt_Schematic ｜ 自有 8 个方法、4 个属性

property BorderColor: TColor read GetState_BorderColor write SetState_BorderColor;
property Designator: WideString read GetState_Designator write SetState_Designator;
property ShowName: Boolean read GetState_ShowName write SetState_ShowName;
property Style: THarnessSpliceStyle read GetState_Style write SetState_Style;
function GetState_BorderColor: TColor;
function GetState_Designator: WideString;
function GetState_ShowName: Boolean;
function GetState_Style: THarnessSpliceStyle;
procedure SetState_BorderColor(AColor: TColor);
procedure SetState_Designator(const ADesignator: WideString);
procedure SetState_ShowName(AShowName: Boolean);
procedure SetState_Style(AStyle: THarnessSpliceStyle);

## ISch_HarnessSpliceData
继承：ISch_HarnessSpliceData → ISch_ConnectivityStorage → ISch_BasicContainer → IInterface ｜ 单元：Rt_Schematic ｜ 自有 4 个方法、2 个属性

property Designator: WideString read GetState_Designator write SetState_Designator;
property Style: THarnessSpliceStyle read GetState_Style write SetState_Style;
function GetState_Designator: WideString;
function GetState_Style: THarnessSpliceStyle;
procedure SetState_Designator(const ADesignator: WideString);
procedure SetState_Style(AStyle: THarnessSpliceStyle);

## ISch_HarnessTwist
继承：ISch_HarnessTwist → ISch_Rectangle → ISch_GraphicalObject → ISch_BasicContainer → IInterface ｜ 单元：Rt_Schematic ｜ 自有 2 个方法、1 个属性

property Orientation: TRotationBy90 read GetState_Orientation write SetState_Orientation;
function GetState_Orientation: TRotationBy90;
procedure SetState_Orientation(ARotationBy90: TRotationBy90);

## ISch_HarnessTwistData
继承：ISch_HarnessTwistData → ISch_ConnectivityStorage → ISch_BasicContainer → IInterface ｜ 单元：Rt_Schematic ｜ 自有 0 个方法、0 个属性


## ISch_HarnessUtils
继承：ISch_HarnessUtils → IInterface ｜ 单元：Rt_Schematic ｜ 自有 0 个方法、0 个属性


## ISch_HarnessWire
继承：ISch_HarnessWire → ISch_Wire → ISch_BasicPolyline → ISch_Polygon → ISch_GraphicalObject → ISch_BasicContainer → IInterface ｜ 单元：Rt_Schematic ｜ 自有 4 个方法、3 个属性

property Comment: ISch_Parameter read GetState_SchComment;  // read-only
property Designator: ISch_Designator read GetState_SchDesignator;  // read-only
property DesignatorLocked: Boolean read GetState_DesignatorLocked write SetState_DesignatorLocked;
function GetState_DesignatorLocked: Boolean;
function GetState_SchComment: ISch_Parameter;
function GetState_SchDesignator: ISch_Designator;
procedure SetState_DesignatorLocked(AValue: Boolean);

## ISch_HarnessWireData
继承：ISch_HarnessWireData → ISch_HarnessBundleSubLineData → ISch_ConnectivityStorage → ISch_BasicContainer → IInterface ｜ 单元：Rt_Schematic ｜ 自有 4 个方法、0 个属性

function GetState_Comment: WideString;
function GetState_EndVertex1ConnectedSchObject: ISch_BasicContainer;
function GetState_EndVertex2ConnectedSchObject: ISch_BasicContainer;
function GetState_Name: WideString;

## ISch_HarnessWireLabel
继承：ISch_HarnessWireLabel → ISch_NetLabel → ISch_Label → ISch_GraphicalObject → ISch_BasicContainer → IInterface ｜ 单元：Rt_Schematic ｜ 自有 0 个方法、0 个属性


## ISch_HarnessWiringDiagram
继承：ISch_HarnessWiringDiagram → ISch_HarnessDocument → ISch_Document → ISch_ParametrizedGroup → ISch_GraphicalObject → ISch_BasicContainer → IInterface ｜ 单元：Rt_Schematic ｜ 自有 0 个方法、0 个属性


## ISch_HighLevelCodeEntry
继承：ISch_HighLevelCodeEntry → ISch_SheetEntry → ISch_GraphicalObject → ISch_BasicContainer → IInterface ｜ 单元：Rt_Schematic ｜ 自有 14 个方法、7 个属性

property DataIdentifier: WideString read GetState_DataIdentifier write SetState_DataIdentifier;
property DataType: THighLevelCodeDataType read GetState_DataType write SetState_DataType;
property DataTypeString: WideString read GetState_DataTypeString;  // read-only
property DataWidth: Integer read GetState_DataWidth write SetState_DataWidth;
property EntryType: THighLevelCodeEntryType read GetState_EntryType write SetState_EntryType;
property ParentRoutine: WideString read GetState_ParentRoutine write SetState_ParentRoutine;
property Role: THighLevelCodeEntryRole read GetState_Role write SetState_Role;
function GetState_DataIdentifier: WideString;
function GetState_DataType: THighLevelCodeDataType;
function GetState_DataTypeString: WideString;
function GetState_DataWidth: Integer;
function GetState_EntryType: THighLevelCodeEntryType;
function GetState_ParentRoutine: WideString;
function GetState_Role: THighLevelCodeEntryRole;
procedure SetState_DataIdentifier(AValue: WideString);
procedure SetState_DataType(AValue: THighLevelCodeDataType);
procedure SetState_DataWidth(AValue: Integer);
procedure SetState_EntryType(AValue: THighLevelCodeEntryType);
procedure SetState_ParentRoutine(AValue: WideString);
procedure SetState_Role(AValue: THighLevelCodeEntryRole);
function SymbolInfo: IInterface;

## ISch_HighLevelCodeMemory
继承：ISch_HighLevelCodeMemory → IInterface ｜ 单元：Rt_Schematic ｜ 自有 22 个方法、11 个属性

property AddressWidth: Integer read GetState_AddressWidth write SetState_AddressWidth;
property BusMode: WideString read GetState_BusMode write SetState_BusMode;
property DataWidth: Integer read GetState_DataWidth write SetState_DataWidth;
property IFace: TMemoryInterfaceType read GetState_Interface write SetState_Interface;
property IsReserved: Boolean read GetState_IsReserved write SetState_IsReserved;
property Mau: Integer read GetState_Mau write SetState_Mau;
property MemType: TMemoryInterfaceType read GetState_Type write SetState_Type;
property Name: WideString read GetState_Name write SetState_Name;
property Offset: WideString read GetState_Offset write SetState_Offset;
property Scope: THighLevelCodeScope read GetState_Scope write SetState_Scope;
property Size: WideString read GetState_Size write SetState_Size;
function GetState_AddressWidth: Integer;
function GetState_BusMode: WideString;
function GetState_DataWidth: Integer;
function GetState_Interface: TMemoryInterfaceType;
function GetState_IsReserved: Boolean;
function GetState_Mau: Integer;
function GetState_Name: WideString;
function GetState_Offset: WideString;
function GetState_Scope: THighLevelCodeScope;
function GetState_Size: WideString;
function GetState_Type: TMemoryInterfaceType;
procedure SetState_AddressWidth(AValue: Integer);
procedure SetState_BusMode(AValue: WideString);
procedure SetState_DataWidth(AValue: Integer);
procedure SetState_Interface(AValue: TMemoryInterfaceType);
procedure SetState_IsReserved(AValue: Boolean);
procedure SetState_Mau(AValue: Integer);
procedure SetState_Name(AValue: WideString);
procedure SetState_Offset(AValue: WideString);
procedure SetState_Scope(AValue: THighLevelCodeScope);
procedure SetState_Size(AValue: WideString);
procedure SetState_Type(AValue: TMemoryInterfaceType);

## ISch_HighLevelCodeRoutine
继承：ISch_HighLevelCodeRoutine → IInterface ｜ 单元：Rt_Schematic ｜ 自有 22 个方法、10 个属性

property AllowStalls: Boolean read GetState_AllowStalls write SetState_AllowStalls;
property InterfaceMode: THighLevelCodeInterfaceMode read GetState_InterfaceMode write SetState_InterfaceMode;
property IsLinked: Boolean read GetState_IsLinked write SetState_IsLinked;
property LinkTarget: WideString read GetState_LinkTarget write SetState_LinkTarget;
property NoWait: Boolean read GetState_NoWait write SetState_NoWait;
property Pipelined: Boolean read GetState_Pipelined write SetState_Pipelined;
property PipelineII: WideString read GetState_PipelineII write SetState_PipelineII;
property PipelineLatency: WideString read GetState_PipelineLatency write SetState_PipelineLatency;
property RoutineName: WideString read GetState_RoutineName write SetState_RoutineName;
property Scope: THighLevelCodeScope read GetState_Scope write SetState_Scope;
function DeclarationString(WithQualifiers: Boolean): WideString;
function GetEntries: IInterfaceList;
function GetState_AllowStalls: Boolean;
function GetState_InterfaceMode: THighLevelCodeInterfaceMode;
function GetState_IsLinked: Boolean;
function GetState_LinkTarget: WideString;
function GetState_NoWait: Boolean;
function GetState_Pipelined: Boolean;
function GetState_PipelineII: WideString;
function GetState_PipelineLatency: WideString;
function GetState_RoutineName: WideString;
function GetState_Scope: THighLevelCodeScope;
procedure SetState_AllowStalls(AValue: Boolean);
procedure SetState_InterfaceMode(AValue: THighLevelCodeInterfaceMode);
procedure SetState_IsLinked(AValue: Boolean);
procedure SetState_LinkTarget(AValue: WideString);
procedure SetState_NoWait(AValue: Boolean);
procedure SetState_Pipelined(AValue: Boolean);
procedure SetState_PipelineII(AValue: WideString);
procedure SetState_PipelineLatency(AValue: WideString);
procedure SetState_RoutineName(AValue: WideString);
procedure SetState_Scope(AValue: THighLevelCodeScope);

## ISch_HighLevelCodeSymbol
继承：ISch_HighLevelCodeSymbol → ISch_SheetSymbol → ISch_RectangularGroup → ISch_ParametrizedGroup → ISch_GraphicalObject → ISch_BasicContainer → IInterface ｜ 单元：Rt_Schematic ｜ 自有 23 个方法、20 个属性

property AdditionalFile[I: Integer]: WideString read GetState_AdditionalFile;  // read-only
property AdditionalFileCount: Integer read GetState_AdditionalFileCount;  // read-only
property EnableResetLogic: Boolean read GetState_EnableResetLogic;  // read-only
property InternalMemoryCount: Integer read GetState_InternalMemoryCount;  // read-only
property InternalMemorySize: WideString read GetState_InternalMemorySize;  // read-only
property JtagBufferDepth: Integer read GetState_JtagBufferDepth;  // read-only
property JtagBufferWidth: Integer read GetState_JtagBufferWidth;  // read-only
property JtagDebugInterface: Boolean read GetState_JtagDebugInterface;  // read-only
property JtagLossless: Boolean read GetState_JtagLossless;  // read-only
property Memory[I: Integer]: ISch_HighLevelCodeMemory read GetState_SchMemory;  // read-only
property MemoryCount: Integer read GetState_MemoryCount;  // read-only
property RegisterOutputs: Boolean read GetState_RegisterOutputs;  // read-only
property ReserveAddressZero: Boolean read GetState_ReserveAddressZero;  // read-only
property ResetUninitializedVariables: Boolean read GetState_ResetUninitializedVariables;  // read-only
property Routine[I: Integer]: ISch_HighLevelCodeRoutine read GetState_SchRoutine;  // read-only
property RoutineCount: Integer read GetState_RoutineCount;  // read-only
property StartOnRisingEdge: Boolean read GetState_StartOnRisingEdge;  // read-only
property ToolchainC_Int16: Boolean read GetState_ToolchainC_Int16;  // read-only
property ToolchainC_Misc: WideString read GetState_ToolchainC_Misc;  // read-only
property ToolchainHdl_Misc: WideString read GetState_ToolchainHdl_Misc;  // read-only
function GetState_AdditionalFile(I: Integer): WideString;
function GetState_AdditionalFileCount: Integer;
function GetState_EnableResetLogic: Boolean;
function GetState_InternalMemoryCount: Integer;
function GetState_InternalMemorySize: WideString;
function GetState_JtagBufferDepth: Integer;
function GetState_JtagBufferWidth: Integer;
function GetState_JtagDebugInterface: Boolean;
function GetState_JtagLossless: Boolean;
function GetState_MemoryCount: Integer;
function GetState_RegisterOutputs: Boolean;
function GetState_ReserveAddressZero: Boolean;
function GetState_ResetUninitializedVariables: Boolean;
function GetState_RoutineCount: Integer;
function GetState_SchMemory(I: Integer): ISch_HighLevelCodeMemory;
function GetState_SchRoutine(I: Integer): ISch_HighLevelCodeRoutine;
function GetState_StartOnRisingEdge: Boolean;
function GetState_ToolchainC_Int16: Boolean;
function GetState_ToolchainC_Misc: WideString;
function GetState_ToolchainHdl_Misc: WideString;
function TopLevel_InterfaceMode: THighLevelCodeInterfaceMode;
function TopLevel_Name: WideString;
function TopLevel_WishboneWidth: Integer;

## ISch_HitTest
继承：ISch_HitTest → IInterface ｜ 单元：Rt_Schematic ｜ 自有 4 个方法、2 个属性

property HitObject[I: Integer]: ISch_GraphicalObject read GetState_HitObject;  // read-only
property HitTestCount: Integer read GetState_HitTestCount;  // read-only
function GetState_HighestPriorityObject: ISch_GraphicalObject;
function GetState_HitObject(I: Integer): ISch_GraphicalObject;
function GetState_HitTestCount: Integer;
function GetState_SecondHighestPriorityObject: ISch_GraphicalObject;

## ISch_Hyperlink
继承：ISch_Hyperlink → ISch_Label → ISch_GraphicalObject → ISch_BasicContainer → IInterface ｜ 单元：Rt_Schematic ｜ 自有 2 个方法、1 个属性

property Url: WideString read GetState_Url write SetState_Url;
function GetState_Url: WideString;
procedure SetState_Url(AUrl: WideString);

## ISch_Image
继承：ISch_Image → ISch_Rectangle → ISch_GraphicalObject → ISch_BasicContainer → IInterface ｜ 单元：Rt_Schematic ｜ 自有 9 个方法、3 个属性

property EmbedImage: Boolean read GetState_EmbedImage write SetState_EmbedImage;
property FileName: WideString read GetState_FileName write SetState_FileName;
property KeepAspect: Boolean read GetState_KeepAspect write SetState_KeepAspect;
procedure DrawToHDC(Handle: HDC; X: Integer; Y: Integer; Width: Integer; Height: Integer; ColorMode: TPaintColorMode);
function FullPath: WideString;
function GetState_EmbedImage: Boolean;
function GetState_FileName: WideString;
function GetState_KeepAspect: Boolean;
procedure SaveImageToFile(FileName: WideString);
procedure SetState_EmbedImage(const Value: Boolean);
procedure SetState_FileName(const Value: WideString);
procedure SetState_KeepAspect(const Value: Boolean);

## ISch_ImageParameter
继承：ISch_ImageParameter → ISch_Parameter → ISch_ComplexText → ISch_Label → ISch_GraphicalObject → ISch_BasicContainer → IInterface ｜ 单元：Rt_Schematic ｜ 自有 0 个方法、0 个属性


## ISch_Implementation
继承：ISch_Implementation → ISch_BasicContainer → IInterface ｜ 单元：Rt_Schematic ｜ 自有 33 个方法、16 个属性

property DatabaseDatalinksLocked: Boolean read GetState_DatabaseDatalinksLocked write SetState_DatabaseDatalinksLocked;
property DatabaseModel: Boolean read GetState_DatabaseModel write SetState_DatabaseModel;
property DatafileLink[I: Integer]: ISch_ModelDatafileLink read GetState_SchDatafileLink;  // read-only
property DatafileLinkCount: Integer read GetState_DatafileLinkCount;  // read-only
property DatalinksLocked: Boolean read GetState_DatalinksLocked write SetState_DatalinksLocked;
property DefinerByInterfaceDesignator[S: WideString]: ISch_MapDefiner read GetState_SchDefinerByInterfaceDesignator;  // read-only
property Description: WideString read GetState_Description write SetState_Description;
property IntegratedModel: Boolean read GetState_IntegratedModel write SetState_IntegratedModel;
property IsCurrent: Boolean read GetState_IsCurrent write SetState_IsCurrent;
property MapAsString: WideString read GetState_MapAsString write SetState_MapAsString;
property ModelItemGUID: WideString read GetState_ModelItemGUID write SetState_ModelItemGUID;
property ModelName: WideString read GetState_ModelName write SetState_ModelName;
property ModelRevisionGUID: WideString read GetState_ModelRevisionGUID write SetState_ModelRevisionGUID;
property ModelType: WideString read GetState_ModelType write SetState_ModelType;
property ModelVaultGUID: WideString read GetState_ModelVaultGUID write SetState_ModelVaultGUID;
property UseComponentLibrary: Boolean read GetState_UseComponentLibrary write SetState_UseComponentLibrary;
procedure AddDataFileLink(anEntityName: WideString; ALocation: WideString; aFileKind: WideString);
procedure ClearAllDatafileLinks;
function GetState_DatabaseDatalinksLocked: Boolean;
function GetState_DatabaseModel: Boolean;
function GetState_DatafileLinkCount: Integer;
function GetState_DatalinksLocked: Boolean;
function GetState_Description: WideString;
function GetState_IntegratedModel: Boolean;
function GetState_IsCurrent: Boolean;
function GetState_MapAsString: WideString;
function GetState_ModelItemGUID: WideString;
function GetState_ModelName: WideString;
function GetState_ModelRevisionGUID: WideString;
function GetState_ModelType: WideString;
function GetState_ModelVaultGUID: WideString;
function GetState_SchDatafileLink(I: Integer): ISch_ModelDatafileLink;
function GetState_SchDefinerByInterfaceDesignator(S: WideString): ISch_MapDefiner;
function GetState_UseComponentLibrary: Boolean;
procedure LockImplementation;
function Map_Import_FromUser(AlowOneToMany: Boolean): Boolean;
procedure SetState_DatabaseDatalinksLocked(AValue: Boolean);
procedure SetState_DatabaseModel(AValue: Boolean);
procedure SetState_DatalinksLocked(AValue: Boolean);
procedure SetState_Description(AValue: WideString);
procedure SetState_IntegratedModel(AValue: Boolean);
procedure SetState_IsCurrent(AValue: Boolean);
procedure SetState_MapAsString(AValue: WideString);
procedure SetState_ModelItemGUID(AValue: WideString);
procedure SetState_ModelName(AValue: WideString);
procedure SetState_ModelRevisionGUID(AValue: WideString);
procedure SetState_ModelType(AValue: WideString);
procedure SetState_ModelVaultGUID(AValue: WideString);
procedure SetState_UseComponentLibrary(AValue: Boolean);

## ISch_Iterator
继承：ISch_Iterator → IInterface ｜ 单元：Rt_Schematic ｜ 自有 10 个方法、0 个属性

procedure AddFilter_Area(x1: Integer; y1: Integer; x2: Integer; y2: Integer);
procedure AddFilter_CurrentDisplayModePrimitives;
procedure AddFilter_CurrentPartPrimitives;
procedure AddFilter_ObjectSet(const AObjectSet: TObjectSet);
procedure AddFilter_PartPrimitives(APartId: Integer; ADisplayMode: Byte);
function FirstSchObject: ISch_BasicContainer;
function NextSchObject: ISch_BasicContainer;
procedure SetContainer(const AContainer: ISch_BasicContainer);
procedure SetState_FilterAll;
procedure SetState_IterationDepth(AIterationDepth: TIterationDepth);

## ISch_Junction
继承：ISch_Junction → ISch_GraphicalObject → ISch_BasicContainer → IInterface ｜ 单元：Rt_Schematic ｜ 自有 4 个方法、2 个属性

property Locked: Boolean read GetState_Locked write SetState_Locked;
property Size: TSize read GetState_Size write SetState_Size;
function GetState_Locked: Boolean;
function GetState_Size: TSize;
procedure SetState_Locked(ALocked: Boolean);
procedure SetState_Size(ASize: TSize);

## ISch_JunctionConvertSettings
继承：ISch_JunctionConvertSettings → IInterface ｜ 单元：Rt_Schematic ｜ 自有 10 个方法、4 个属性

property BatchMode: Boolean read GetBatchMode write SetBatchMode;
property JunctionConversion: TJunctionConversionKind read GetJunctionConversion write SetJunctionConversion;
property MiterSize: TDistance read GetMiterSize write SetMiterSize;
property ShowDialog: Boolean read GetShowDialog write SetShowDialog;
procedure Export_ToIniFile(const OptionsWriter: IOptionsWriter);
function GetBatchMode: Boolean;
function GetJunctionConversion: TJunctionConversionKind;
function GetMiterSize: Integer;
function GetShowDialog: Boolean;
procedure Import_FromIniFile(const OptionsReader: IOptionsReader);
procedure SetBatchMode(Value: Boolean);
procedure SetJunctionConversion(Value: TJunctionConversionKind);
procedure SetMiterSize(Value: Integer);
procedure SetShowDialog(Value: Boolean);

## ISch_Label
继承：ISch_Label → ISch_GraphicalObject → ISch_BasicContainer → IInterface ｜ 单元：Rt_Schematic ｜ 自有 14 个方法、9 个属性

property CalculatedValueString: WideString read GetState_CalculatedValueString;  // read-only
property DisplayString: WideString read GetState_DisplayString;  // read-only
property FontID: TFontID read GetState_FontId write SetState_FontId;
property Formula: WideString read GetState_Formula;  // read-only
property IsMirrored: Boolean read GetState_IsMirrored write SetState_IsMirrored;
property Justification: TTextJustification read GetState_Justification write SetState_Justification;
property Orientation: TRotationBy90 read GetState_Orientation write SetState_Orientation;
property OverrideDisplayString: WideString read GetState_OverrideDisplayString write SetState_OverrideDisplayString;
property Text: WideString read GetState_Text write SetState_Text;
function GetState_CalculatedValueString: WideString;
function GetState_DisplayString: WideString;
function GetState_FontId: Integer;
function GetState_Formula: WideString;
function GetState_IsMirrored: Boolean;
function GetState_Justification: TTextJustification;
function GetState_Orientation: TRotationBy90;
function GetState_OverrideDisplayString: WideString;
function GetState_SimpleCalculatedString: WideString;
procedure SetState_FontId(AFontId: Integer);
procedure SetState_IsMirrored(AValue: Boolean);
procedure SetState_Justification(AValue: TTextJustification);
procedure SetState_Orientation(ARotation: TRotationBy90);
procedure SetState_OverrideDisplayString(S: WideString);

## ISch_Lib
继承：ISch_Lib → ISch_Document → ISch_ParametrizedGroup → ISch_GraphicalObject → ISch_BasicContainer → IInterface ｜ 单元：Rt_Schematic ｜ 自有 41 个方法、9 个属性

property AlwaysShowCD: Boolean read GetState_AlwaysShowCD write SetState_AlwaysShowCD;
property CurrentSchComponent: ISch_Component read GetState_Current_SchComponent write SetState_Current_SchComponent;
property Description: WideString read GetState_Description write SetState_Description;
property FolderGUID: WideString read GetState_FolderGUID write SetState_FolderGUID;
property IsSimpleDesignMode: Boolean read GetState_IsSimpleDesignMode;  // read-only
property IsSingleComponentMode: Boolean read GetState_IsSingleComponentMode;  // read-only
property LifeCycleDefinitionGUID: WideString read GetState_LifeCycleDefinitionGUID write SetState_LifeCycleDefinitionGUID;
property RevisionNamingSchemeGUID: WideString read GetState_RevisionNamingSchemeGUID write SetState_RevisionNamingSchemeGUID;
property ShowHiddenPins: Boolean read GetState_ShowHiddenPins write SetState_ShowHiddenPins;
procedure AddSchComponent(const AComponent: ISch_Component);
procedure AddSchComponentWithoutNotification(const AComponent: ISch_Component);
function CreateLibraryValidator: ISch_LibraryValidator;
function GetState_AlwaysShowCD: Boolean;
function GetState_Current_SchComponent: ISch_Component;
function GetState_CurrentSchComponentDisplayMode: Byte;
function GetState_CurrentSchComponentLibReference: WideString;
function GetState_CurrentSchComponentPartId: Integer;
function GetState_Description: WideString;
function GetState_FolderGUID: WideString;
function GetState_IsSimpleDesignMode: Boolean;
function GetState_IsSingleComponentMode: Boolean;
function GetState_LifeCycleDefinitionGUID: WideString;
function GetState_RevisionNamingSchemeGUID: WideString;
function GetState_SchComponentByLibRef(ALibRef: WideString): ISch_Component;
function GetState_ShowHiddenPins: Boolean;
function LibIsEmpty: Boolean;
function LinkDocumentToReleaseVault(Parameters: WideString; var ErrorMsg: WideString): Boolean;
procedure LoadFromFile(const VFSAddress: WideString);
function ReleaseDocument(Parameters: WideString; var ErrorMsg: WideString): Boolean;
procedure RemoveSchComponent(const AComponent: ISch_Component);
procedure SaveToFile(const VFSAddress: WideString);
function Sch_LibraryRuleChecker_Create: ISch_LibraryRuleChecker;
procedure Sch_LibraryRuleChecker_Destroy(var ARuleChecker: ISch_LibraryRuleChecker);
function SchLibIterator_Create: ISch_Iterator;
procedure SetState_AlwaysShowCD(AValue: Boolean);
procedure SetState_Current_SchComponent(AValue: ISch_Component);
procedure SetState_CurrentSchComponentAddDisplayMode;
procedure SetState_CurrentSchComponentAddPart;
procedure SetState_CurrentSchComponentDisplayMode(ADisplayMode: Byte);
procedure SetState_CurrentSchComponentLibReference(const AValue: WideString);
procedure SetState_CurrentSchComponentPartId(APartId: Integer);
procedure SetState_CurrentSchComponentRemoveDisplayMode;
procedure SetState_CurrentSchComponentRemovePart;
procedure SetState_Description(AValue: WideString);
procedure SetState_FolderGUID(AValue: WideString);
procedure SetState_LifeCycleDefinitionGUID(AValue: WideString);
procedure SetState_RevisionNamingSchemeGUID(AValue: WideString);
procedure SetState_ShowHiddenPins(AValue: Boolean);
procedure TransferComponentsPrimitivesBackFromEditor;
procedure TransferComponentsPrimitivesToEditor;

## ISch_LibraryRuleChecker
继承：ISch_LibraryRuleChecker → IInterface ｜ 单元：Rt_Schematic ｜ 自有 21 个方法、9 个属性

property Duplicate_Component: Boolean read GetState_Duplicate_Component write SetState_Duplicate_Component;
property Duplicate_Pins: Boolean read GetState_Duplicate_Pins write SetState_Duplicate_Pins;
property Missing_Default_Designator: Boolean read GetState_Missing_Default_Designator write SetState_Missing_Default_Designator;
property Missing_Description: Boolean read GetState_Missing_Description write SetState_Missing_Description;
property Missing_Footprint: Boolean read GetState_Missing_Footprint write SetState_Missing_Footprint;
property Missing_Pin_Name: Boolean read GetState_Missing_Pin_Name write SetState_Missing_Pin_Name;
property Missing_Pin_Number: Boolean read GetState_Missing_Pin_Number write SetState_Missing_Pin_Number;
property Missing_Pins_In_Sequence: Boolean read GetState_Missing_Pins_In_Sequence write SetState_Missing_Pins_In_Sequence;
property ShowReport: Boolean read GetState_ShowReport write SetState_ShowReport;
function GetState_Duplicate_Component: Boolean;
function GetState_Duplicate_Pins: Boolean;
function GetState_Missing_Default_Designator: Boolean;
function GetState_Missing_Description: Boolean;
function GetState_Missing_Footprint: Boolean;
function GetState_Missing_Pin_Name: Boolean;
function GetState_Missing_Pin_Number: Boolean;
function GetState_Missing_Pins_In_Sequence: Boolean;
function GetState_ShowReport: Boolean;
function Import_FromUser: Boolean;
function Run: Boolean;
procedure SetState_Duplicate_Component(AValue: Boolean);
procedure SetState_Duplicate_Pins(AValue: Boolean);
function SetState_FromParameters(Parameters: PWideChar): Boolean;
procedure SetState_Missing_Default_Designator(AValue: Boolean);
procedure SetState_Missing_Description(AValue: Boolean);
procedure SetState_Missing_Footprint(AValue: Boolean);
procedure SetState_Missing_Pin_Name(AValue: Boolean);
procedure SetState_Missing_Pin_Number(AValue: Boolean);
procedure SetState_Missing_Pins_In_Sequence(AValue: Boolean);
procedure SetState_ShowReport(AValue: Boolean);

## ISch_LibraryValidator
继承：ISch_LibraryValidator → IInterface ｜ 单元：Rt_Schematic ｜ 自有 1 个方法、0 个属性

procedure Validate(AChecksResult: IInterfaceList; AErrorKinds: TFileLessViolationKinds);

## ISch_Line
继承：ISch_Line → ISch_GraphicalObject → ISch_BasicContainer → IInterface ｜ 单元：Rt_Schematic ｜ 自有 6 个方法、3 个属性

property Corner: TLocation read GetState_Corner write SetState_Corner;
property LineStyle: TLineStyle read GetState_LineStyle write SetState_LineStyle;
property LineWidth: TSize read GetState_LineWidth write SetState_LineWidth;
function GetState_Corner: IDispatch;
function GetState_LineStyle: TLineStyle;
function GetState_LineWidth: TSize;
procedure SetState_Corner(const ALocation: IDispatch);
procedure SetState_LineStyle(AStyle: TLineStyle);
procedure SetState_LineWidth(ASize: TSize);

## ISch_MapDefiner
继承：ISch_MapDefiner → ISch_BasicContainer → IInterface ｜ 单元：Rt_Schematic ｜ 自有 9 个方法、5 个属性

property Designator_Implementation[Index: Integer]: WideString read GetState_Designator_Implementation;  // read-only
property Designator_ImplementationCount: Integer read GetState_Designator_ImplementationCount;  // read-only
property Designator_Implementations_AsString: WideString read GetState_Designators_Implementation_AsString;  // read-only
property Designator_Interface: WideString read GetState_Designator_Interface write SetState_Designator_Interface;
property IsTrivial: Boolean read GetState_IsTrivial;  // read-only
function GetState_Designator_Implementation(Index: Integer): WideString;
function GetState_Designator_ImplementationCount: Integer;
function GetState_Designator_Interface: WideString;
function GetState_Designators_Implementation_AsString: WideString;
function GetState_IsTrivial: Boolean;
procedure SetState_AllFromString(AValue: WideString);
procedure SetState_Designator_ImplementationAdd(AValue: WideString);
procedure SetState_Designator_ImplementationClear;
procedure SetState_Designator_Interface(AValue: WideString);

## ISch_ModelDatafileLink
继承：ISch_ModelDatafileLink → IInterface ｜ 单元：Rt_Schematic ｜ 自有 8 个方法、5 个属性

property EntityName: WideString read GetState_EntityName write SetState_EntityName;
property FileKind: WideString read GetState_FileKind write SetState_FileKind;
property LibIdentifierKind: TLibIdentifierKind read GetState_LibIdentifierKind;  // read-only
property LibraryIdentifier: WideString read GetState_LibraryIdentifier;  // read-only
property Location: WideString read GetState_Location write SetState_Location;
function GetState_EntityName: WideString;
function GetState_FileKind: WideString;
function GetState_LibIdentifierKind: TLibIdentifierKind;
function GetState_LibraryIdentifier: WideString;
function GetState_Location: WideString;
procedure SetState_EntityName(AValue: WideString);
procedure SetState_FileKind(AValue: WideString);
procedure SetState_Location(AValue: WideString);

## ISch_NetLabel
继承：ISch_NetLabel → ISch_Label → ISch_GraphicalObject → ISch_BasicContainer → IInterface ｜ 单元：Rt_Schematic ｜ 自有 0 个方法、0 个属性


## ISch_NoERC
继承：ISch_NoERC → ISch_GraphicalObject → ISch_BasicContainer → IInterface ｜ 单元：Rt_Schematic ｜ 自有 14 个方法、7 个属性

property IsActive: Boolean read GetIsActive write SetIsActive;
property Orientation: TRotationBy90 read GetOrientation write SetOrientation;
property StrConnectionPairsToSuppress: WideString read GetStrConnectionPairsToSuppress write SetStrConnectionPairsToSuppress;
property StrErrorKindSetToSuppress: WideString read GetStrErrorKindSetToSuppress write SetStrErrorKindSetToSuppress;
property StrSuppressableErrors: WideString read GetStrSuppressableErrors;  // read-only
property SuppressAll: Boolean read GetSuppressAll write SetSuppressAll;
property Symbol: TNoERCSymbol read GetSymbol write SetSymbol;
function GetIsActive: Boolean;
function GetOrientation: TRotationBy90;
function GetStrConnectionPairsToSuppress: WideString;
function GetStrErrorKindSetToSuppress: WideString;
function GetStrSuppressableErrors: WideString;
function GetSuppressAll: Boolean;
function GetSymbol: TNoERCSymbol;
function Import_FromUser_MultipleNoErc(AObjects: ISafeInterfaceList): Boolean;
procedure SetIsActive(AIsActive: Boolean);
procedure SetOrientation(ARotationBy90: TRotationBy90);
procedure SetStrConnectionPairsToSuppress(AStrConnectionPairsToSuppress: WideString);
procedure SetStrErrorKindSetToSuppress(AStrErrorKindSet: WideString);
procedure SetSuppressAll(ASuppressAll: Boolean);
procedure SetSymbol(ASymbol: TNoERCSymbol);

## ISch_Note
继承：ISch_Note → ISch_TextFrame → ISch_Rectangle → ISch_GraphicalObject → ISch_BasicContainer → IInterface ｜ 单元：Rt_Schematic ｜ 自有 4 个方法、2 个属性

property Author: WideString read GetState_Author write SetState_Author;
property Collapsed: Boolean read GetState_Collapsed write SetState_Collapsed;
function GetState_Author: WideString;
function GetState_Collapsed: Boolean;
procedure SetState_Author(AValue: WideString);
procedure SetState_Collapsed(AValue: Boolean);

## ISch_OpenBusGroup
继承：ISch_OpenBusGroup → ISch_ParametrizedGroup → ISch_GraphicalObject → ISch_BasicContainer → IInterface ｜ 单元：Rt_Schematic ｜ 自有 10 个方法、5 个属性

property Circular: Boolean read GetState_Circular write SetState_Circular;
property IsMirrored: Boolean read GetState_IsMirrored write SetState_IsMirrored;
property Orientation: TRotationBy90 read GetState_Orientation write SetState_Orientation;
property XSize: TCoord read GetState_XSize write SetState_XSize;
property YSize: TCoord read GetState_YSize write SetState_YSize;
function GetState_Circular: Boolean;
function GetState_IsMirrored: Boolean;
function GetState_Orientation: TRotationBy90;
function GetState_XSize: Integer;
function GetState_YSize: Integer;
procedure SetState_Circular(Value: Boolean);
procedure SetState_IsMirrored(AValue: Boolean);
procedure SetState_Orientation(AValue: TRotationBy90);
procedure SetState_XSize(Value: Integer);
procedure SetState_YSize(Value: Integer);

## ISch_Parameter
继承：ISch_Parameter → ISch_ComplexText → ISch_Label → ISch_GraphicalObject → ISch_BasicContainer → IInterface ｜ 单元：Rt_Schematic ｜ 自有 21 个方法、13 个属性

property AllowDatabaseSynchronize: Boolean read GetState_AllowDatabaseSynchronize write SetState_AllowDatabaseSynchronize;
property AllowLibrarySynchronize: Boolean read GetState_AllowLibrarySynchronize write SetState_AllowLibrarySynchronize;
property Description: WideString read GetState_Description write SetState_Description;
property IsConfigurable: Boolean read GetState_IsConfigurable;  // read-only
property IsRule: Boolean read GetState_IsRule;  // read-only
property IsSystemParameter: Boolean read GetState_IsSystemParameter;  // read-only
property Name: WideString read GetState_Name write SetState_Name;
property NameIsReadOnly: Boolean read GetState_NameIsReadOnly;  // read-only
property ParamType: TParameterType read GetState_ParamType write SetState_ParamType;
property ReadOnlyState: TParameter_ReadOnlyState read GetState_ReadOnlyState write SetState_ReadOnlyState;
property ShowName: Boolean read GetState_ShowName write SetState_ShowName;
property ValueIsReadOnly: Boolean read GetState_ValueIsReadOnly;  // read-only
property VariantOption: IVariantOption read GetState_VariantOption write SetState_VariantOption;
function GetState_AllowDatabaseSynchronize: Boolean;
function GetState_AllowLibrarySynchronize: Boolean;
function GetState_Description: WideString;
function GetState_IsConfigurable: Boolean;
function GetState_IsRule: Boolean;
function GetState_IsSystemParameter: Boolean;
function GetState_Name: WideString;
function GetState_NameIsReadOnly: Boolean;
function GetState_ParamType: TParameterType;
function GetState_ReadOnlyState: TParameter_ReadOnlyState;
function GetState_ShowName: Boolean;
function GetState_ValueIsReadOnly: Boolean;
function GetState_VariantOption: IVariantOption;
procedure SetState_AllowDatabaseSynchronize(B: Boolean);
procedure SetState_AllowLibrarySynchronize(B: Boolean);
procedure SetState_Description(S: WideString);
procedure SetState_Name(S: WideString);
procedure SetState_ParamType(N: TParameterType);
procedure SetState_ReadOnlyState(R: TParameter_ReadOnlyState);
procedure SetState_ShowName(N: Boolean);
procedure SetState_VariantOption(V: IVariantOption);

## ISch_ParameterSet
继承：ISch_ParameterSet → ISch_ParametrizedGroup → ISch_GraphicalObject → ISch_BasicContainer → IInterface ｜ 单元：Rt_Schematic ｜ 自有 6 个方法、3 个属性

property Name: WideString read GetState_Name write SetState_Name;
property Orientation: TRotationBy90 read GetState_Orientation write SetState_Orientation;
property Style: TParameterSetStyle read GetState_Style write SetState_Style;
function GetState_Name: WideString;
function GetState_Orientation: TRotationBy90;
function GetState_Style: TParameterSetStyle;
procedure SetState_Name(AValue: WideString);
procedure SetState_Orientation(AValue: TRotationBy90);
procedure SetState_Style(AStyle: TParameterSetStyle);

## ISch_ParametrizedGroup
继承：ISch_ParametrizedGroup → ISch_GraphicalObject → ISch_BasicContainer → IInterface ｜ 单元：Rt_Schematic ｜ 自有 4 个方法、0 个属性

function Add_Parameter(const AName: WideString; const AValue: WideString; out AParameter: ISch_Parameter): LongBool;
function Import_FromUser_Parameters: Boolean;
function Remove_Parameter(const Parameter: ISch_Parameter): LongBool;
procedure ResetAllSchParametersPosition;

## ISch_Pie
继承：ISch_Pie → ISch_Arc → ISch_GraphicalObject → ISch_BasicContainer → IInterface ｜ 单元：Rt_Schematic ｜ 自有 2 个方法、1 个属性

property IsSolid: Boolean read GetState_IsSolid write SetState_IsSolid;
function GetState_IsSolid: Boolean;
procedure SetState_IsSolid(B: Boolean);

## ISch_Pin
继承：ISch_Pin → ISch_ParametrizedGroup → ISch_GraphicalObject → ISch_BasicContainer → IInterface ｜ 单元：Rt_Schematic ｜ 自有 79 个方法、38 个属性

property DefaultValue: WideString read GetState_DefaultValue write SetState_DefaultValue;
property Description: WideString read GetState_Description write SetState_Description;
property Designator: WideString read GetState_Designator write SetState_Designator;
property Designator_CustomColor: TColor read GetState_Designator_CustomColor write SetState_Designator_CustomColor;
property Designator_CustomFontID: TFontID read GetState_Designator_CustomFontID write SetState_Designator_CustomFontID;
property Designator_CustomPosition_Margin: TCoord read GetState_Designator_CustomPosition_Margin write SetState_Designator_CustomPosition_Margin;
property Designator_CustomPosition_RotationAnchor: TPinTextRotationAnchor read GetState_Designator_CustomPosition_RotationAnchor write SetState_Designator_CustomPosition_RotationAnchor;
property Designator_CustomPosition_RotationRelative: TRotationBy90 read GetState_Designator_CustomPosition_RotationRelative write SetState_Designator_CustomPosition_RotationRelative;
property Designator_FontMode: TPinItemMode read GetState_Designator_FontMode write SetState_Designator_FontMode;
property Designator_PositionMode: TPinItemMode read GetState_Designator_PositionMode write SetState_Designator_PositionMode;
property Electrical: TPinElectrical read GetState_Electrical write SetState_Electrical;
property FormalType: TStdLogicState read GetState_FormalType write SetState_FormalType;
property HiddenNetName: WideString read GetState_HiddenNetName write SetState_HiddenNetName;
property IsHidden: Boolean read GetState_IsHidden write SetState_IsHidden;
property Name: WideString read GetState_Name write SetState_Name;
property Name_CustomColor: TColor read GetState_Name_CustomColor write SetState_Name_CustomColor;
property Name_CustomFontID: TFontID read GetState_Name_CustomFontID write SetState_Name_CustomFontID;
property Name_CustomPosition_Margin: TCoord read GetState_Name_CustomPosition_Margin write SetState_Name_CustomPosition_Margin;
property Name_CustomPosition_RotationAnchor: TPinTextRotationAnchor read GetState_Name_CustomPosition_RotationAnchor write SetState_Name_CustomPosition_RotationAnchor;
property Name_CustomPosition_RotationRelative: TRotationBy90 read GetState_Name_CustomPosition_RotationRelative write SetState_Name_CustomPosition_RotationRelative;
property Name_FontMode: TPinItemMode read GetState_Name_FontMode write SetState_Name_FontMode;
property Name_PositionMode: TPinItemMode read GetState_Name_PositionMode write SetState_Name_PositionMode;
property Orientation: TRotationBy90 read GetState_Orientation write SetState_Orientation;
property PinLength: TCoord read GetState_PinLength write SetState_PinLength;
property PinPackageLength: TCoord read GetState_PinPackageLength write SetState_PinPackageLength;
property PropagationDelay: Double read GetState_PropagationDelay write SetState_PropagationDelay;
property ShowDesignator: Boolean read GetState_ShowDesignator write SetState_ShowDesignator;
property ShowName: Boolean read GetState_ShowName write SetState_ShowName;
property SwapId_Pair: WideString read GetState_SwapIdPair write SetState_SwapIdPair;
property SwapId_Part: WideString read GetState_SwapIdPart write SetState_SwapIdPart;
property SwapId_PartPin: WideString read GetState_SwapIdPartPin write SetState_SwapIdPartPin;
property SwapId_Pin: WideString read GetState_SwapIdPin write SetState_SwapIdPin;
property Symbol_Inner: TIeeeSymbol read GetState_Symbol_Inner write SetState_Symbol_Inner;
property Symbol_InnerEdge: TIeeeSymbol read GetState_Symbol_InnerEdge write SetState_Symbol_InnerEdge;
property Symbol_LineWidth: TSize read GetState_Symbol_LineWidth write SetState_Symbol_LineWidth;
property Symbol_Outer: TIeeeSymbol read GetState_Symbol_Outer write SetState_Symbol_Outer;
property Symbol_OuterEdge: TIeeeSymbol read GetState_Symbol_OuterEdge write SetState_Symbol_OuterEdge;
property Width: Integer read GetState_Width write SetState_Width;
function FullDesignator: WideString;
function GetState_DefaultValue: WideString;
function GetState_Description: WideString;
function GetState_Designator: WideString;
function GetState_Designator_CustomColor: TColor;
function GetState_Designator_CustomFontID: Integer;
function GetState_Designator_CustomPosition_Margin: Integer;
function GetState_Designator_CustomPosition_RotationAnchor: TPinTextRotationAnchor;
function GetState_Designator_CustomPosition_RotationRelative: TRotationBy90;
function GetState_Designator_FontMode: TPinItemMode;
function GetState_Designator_PositionMode: TPinItemMode;
function GetState_Electrical: TPinElectrical;
function GetState_FormalType: TStdLogicState;
function GetState_HiddenNetName: WideString;
function GetState_IsHidden: Boolean;
function GetState_Name: WideString;
function GetState_Name_CustomColor: TColor;
function GetState_Name_CustomFontID: Integer;
function GetState_Name_CustomPosition_Margin: Integer;
function GetState_Name_CustomPosition_RotationAnchor: TPinTextRotationAnchor;
function GetState_Name_CustomPosition_RotationRelative: TRotationBy90;
function GetState_Name_FontMode: TPinItemMode;
function GetState_Name_PositionMode: TPinItemMode;
function GetState_Orientation: TRotationBy90;
function GetState_PinLength: Integer;
function GetState_PinPackageLength: Integer;
function GetState_PropagationDelay: Double;
function GetState_ShowDesignator: Boolean;
function GetState_ShowName: Boolean;
function GetState_SwapIdPair: WideString;
function GetState_SwapIdPart: WideString;
function GetState_SwapIdPartPin: WideString;
function GetState_SwapIdPin: WideString;
function GetState_Symbol_Inner: TIeeeSymbol;
function GetState_Symbol_InnerEdge: TIeeeSymbol;
function GetState_Symbol_LineWidth: TSize;
function GetState_Symbol_Outer: TIeeeSymbol;
function GetState_Symbol_OuterEdge: TIeeeSymbol;
function GetState_Width: Integer;
function OwnerSchComponent: ISch_Component;
procedure SetState_DefaultValue(AValue: WideString);
procedure SetState_Description(AValue: WideString);
procedure SetState_Designator(AValue: WideString);
procedure SetState_Designator_CustomColor(AValue: TColor);
procedure SetState_Designator_CustomFontID(AValue: Integer);
procedure SetState_Designator_CustomPosition_Margin(AValue: Integer);
procedure SetState_Designator_CustomPosition_RotationAnchor(AValue: TPinTextRotationAnchor);
procedure SetState_Designator_CustomPosition_RotationRelative(AValue: TRotationBy90);
procedure SetState_Designator_FontMode(AValue: TPinItemMode);
procedure SetState_Designator_PositionMode(AValue: TPinItemMode);
procedure SetState_Electrical(AValue: TPinElectrical);
procedure SetState_FormalType(AValue: TStdLogicState);
procedure SetState_FunctionsFromName;
procedure SetState_HiddenNetName(AValue: WideString);
procedure SetState_IsHidden(AValue: Boolean);
procedure SetState_Name(AValue: WideString);
procedure SetState_Name_CustomColor(AValue: TColor);
procedure SetState_Name_CustomFontID(AValue: Integer);
procedure SetState_Name_CustomPosition_Margin(AValue: Integer);
procedure SetState_Name_CustomPosition_RotationAnchor(AValue: TPinTextRotationAnchor);
procedure SetState_Name_CustomPosition_RotationRelative(AValue: TRotationBy90);
procedure SetState_Name_FontMode(AValue: TPinItemMode);
procedure SetState_Name_PositionMode(AValue: TPinItemMode);
procedure SetState_Orientation(AValue: TRotationBy90);
procedure SetState_PinLength(AValue: Integer);
procedure SetState_PinPackageLength(AValue: Integer);
procedure SetState_PropagationDelay(AValue: Double);
procedure SetState_ShowDesignator(AValue: Boolean);
procedure SetState_ShowName(AValue: Boolean);
procedure SetState_SwapIdPair(AValue: WideString);
procedure SetState_SwapIdPart(AValue: WideString);
procedure SetState_SwapIdPartPin(AValue: WideString);
procedure SetState_SwapIdPin(AValue: WideString);
procedure SetState_Symbol_Inner(AValue: TIeeeSymbol);
procedure SetState_Symbol_InnerEdge(AValue: TIeeeSymbol);
procedure SetState_Symbol_LineWidth(AValue: TSize);
procedure SetState_Symbol_Outer(AValue: TIeeeSymbol);
procedure SetState_Symbol_OuterEdge(AValue: TIeeeSymbol);
procedure SetState_Width(AValue: Integer);

## ISch_Polygon
继承：ISch_Polygon → ISch_GraphicalObject → ISch_BasicContainer → IInterface ｜ 单元：Rt_Schematic ｜ 自有 13 个方法、5 个属性

property IsSolid: Boolean read GetState_IsSolid write SetState_IsSolid;
property LineWidth: TSize read GetState_LineWidth write SetState_LineWidth;
property Transparent: Boolean read GetState_Transparent write SetState_Transparent;
property Vertex[I: Integer]: TLocation read GetState_Vertex write SetState_Vertex;
property VerticesCount: Integer read GetState_VerticesCount write SetState_VerticesCount;
procedure ClearAllVertices;
function GetState_IsSolid: Boolean;
function GetState_LineWidth: TSize;
function GetState_Transparent: Boolean;
function GetState_Vertex(I: Integer): IDispatch;
function GetState_VerticesCount: Integer;
function InsertVertex(Index: Integer): Boolean;
function RemoveVertex(var Index: Integer): Boolean;
procedure SetState_IsSolid(AValue: Boolean);
procedure SetState_LineWidth(AValue: TSize);
procedure SetState_Transparent(B: Boolean);
procedure SetState_Vertex(I: Integer; const ALocation: IDispatch);
procedure SetState_VerticesCount(AValue: Integer);

## ISch_Polyline
继承：ISch_Polyline → ISch_BasicPolyline → ISch_Polygon → ISch_GraphicalObject → ISch_BasicContainer → IInterface ｜ 单元：Rt_Schematic ｜ 自有 6 个方法、3 个属性

property EndLineShape: TLineShape read GetState_EndLineShape write SetState_EndLineShape;
property LineShapeSize: TSize read GetState_LineShapeSize write SetState_LineShapeSize;
property StartLineShape: TLineShape read GetState_StartLineShape write SetState_StartLineShape;
function GetState_EndLineShape: TLineShape;
function GetState_LineShapeSize: TSize;
function GetState_StartLineShape: TLineShape;
procedure SetState_EndLineShape(AValue: TLineShape);
procedure SetState_LineShapeSize(AValue: TSize);
procedure SetState_StartLineShape(AValue: TLineShape);

## ISch_Port
继承：ISch_Port → ISch_ParametrizedGroup → ISch_GraphicalObject → ISch_BasicContainer → IInterface ｜ 单元：Rt_Schematic ｜ 自有 32 个方法、15 个属性

property Alignment: THorizontalAlign read GetState_Alignment write SetState_Alignment;
property AutoSize: Boolean read GetState_AutoSize write SetState_AutoSize;
property BorderWidth: TSize read GetState_BorderWidth write SetState_BorderWidth;
property ConnectedEnd: TPortConnectedEnd read GetState_ConnectedEnd write SetState_ConnectedEnd;
property CrossReference: WideString read GetState_CrossRef write SetState_CrossRef;
property FontID: TFontID read GetState_FontId write SetState_FontId;
property HarnessColor: TColor read GetState_HarnessColor write SetState_HarnessColor;
property HarnessType: WideString read GetState_HarnessType write SetState_HarnessType;
property Height: TCoord read GetState_Height write SetState_Height;
property IOType: TPortIO read GetState_IOType write SetState_IOType;
property Name: WideString read GetState_Name write SetState_Name;
property OverrideDisplayString: WideString read GetState_OverrideDisplayString write SetState_OverrideDisplayString;
property Style: TPortArrowStyle read GetState_Style write SetState_Style;
property TextColor: TColor read GetState_TextColor write SetState_TextColor;
property Width: TCoord read GetState_Width write SetState_Width;
function GetState_Alignment: THorizontalAlign;
function GetState_AutoSize: Boolean;
function GetState_BorderWidth: TSize;
function GetState_ConnectedEnd: TPortConnectedEnd;
function GetState_CrossRef: WideString;
function GetState_FontId: Integer;
function GetState_HarnessColor: TColor;
function GetState_HarnessType: WideString;
function GetState_Height: Integer;
function GetState_IOType: TPortIO;
function GetState_Name: WideString;
function GetState_NetNamesForPort: WideString;
function GetState_OverrideDisplayString: WideString;
function GetState_Style: TPortArrowStyle;
function GetState_TextColor: TColor;
function GetState_Width: Integer;
function IsVertical: Boolean;
procedure SetState_Alignment(AValue: THorizontalAlign);
procedure SetState_AutoSize(AValue: Boolean);
procedure SetState_BorderWidth(AValue: TSize);
procedure SetState_ConnectedEnd(AValue: TPortConnectedEnd);
procedure SetState_CrossRef(AValue: WideString);
procedure SetState_FontId(AFontId: Integer);
procedure SetState_HarnessColor(AValue: TColor);
procedure SetState_HarnessType(AValue: WideString);
procedure SetState_Height(AValue: Integer);
procedure SetState_IOType(AValue: TPortIO);
procedure SetState_Name(AValue: WideString);
procedure SetState_OverrideDisplayString(AValue: WideString);
procedure SetState_Style(AValue: TPortArrowStyle);
procedure SetState_TextColor(AValue: TColor);
procedure SetState_Width(AValue: Integer);

## ISch_PowerObject
继承：ISch_PowerObject → ISch_Label → ISch_GraphicalObject → ISch_BasicContainer → IInterface ｜ 单元：Rt_Schematic ｜ 自有 4 个方法、2 个属性

property ShowNetName: Boolean read GetState_ShowNetName write SetState_ShowNetName;
property Style: TPowerObjectStyle read GetState_Style write SetState_Style;
function GetState_ShowNetName: Boolean;
function GetState_Style: TPowerObjectStyle;
procedure SetState_ShowNetName(AValue: Boolean);
procedure SetState_Style(AStyle: TPowerObjectStyle);

## ISch_Preferences
继承：ISch_Preferences → IInterface ｜ 单元：Rt_Schematic ｜ 自有 211 个方法、105 个属性

property AddTemplateToClipBoard: Boolean read Get_AddTemplateToClipBoard write Set_AddTemplateToClipBoard;
property AllowDeviceSheetEditing: Boolean read Get_AllowDeviceSheetEditing write Set_AllowDeviceSheetEditing;
property AlwaysDrag: Boolean read Get_AlwaysDrag write Set_AlwaysDrag;
property AutoBackupFileCount: Integer read Get_AutoBackupFileCount write Set_AutoBackupFileCount;
property AutoBackupTime: Integer read Get_AutoBackupTime write Set_AutoBackupTime;
property AutoPanJumpDistance: TCoord read Get_AutoPanJumpDistance write Set_AutoPanJumpDistance;
property AutoPanShiftJumpDistance: TCoord read Get_AutoPanShiftJumpDistance write Set_AutoPanShiftJumpDistance;
property AutoPanStyle: TAutoPanStyle read Get_AutoPanStyle write Set_AutoPanStyle;
property AutoZoom: Boolean read Get_AutoZoom write Set_AutoZoom;
property BufferedPainting: Boolean read Get_BufferedPainting write Set_BufferedPainting;
property BusAutoJunctionsColor: TColor read Get_BusAutoJunctionsColor write Set_BusAutoJunctionsColor;
property BusAutoJunctionsSize: TSize read Get_BusAutoJunctionsSize write Set_BusAutoJunctionsSize;
property BusDragJunctionsColor: TColor read Get_BusDragJunctionsColor write Set_BusDragJunctionsColor;
property ClickClearsSelection: Boolean read Get_ClickClearsSelection write Set_ClickClearsSelection;
property ComponentsCutWires: Boolean read Get_ComponentsCutWires write Set_ComponentsCutWires;
property ConfirmSelectionMemoryClear: Boolean read Get_ConfirmSelectionMemoryClear write Set_ConfirmSelectionMemoryClear;
property ConvertSpecialStrings: Boolean read Get_ConvertSpecialStrings write Set_ConvertSpecialStrings;
property CrossRefLocationStyle: TCrossRefLocationStyle read Get_CrossRefLocationStyle write Set_CrossRefLocationStyle;
property CrossRefSheetStyle: TCrossRefSheetStyle read Get_CrossRefSheetStyle write Set_CrossRefSheetStyle;
property CtrlDbleClickGoesDown: Boolean read Get_CtrlDbleClickGoesDown write Set_CtrlDbleClickGoesDown;
property CutterFixedLength: TCoord read Get_CutterFixedLength write Set_CutterFixedLength;
property CutterGridSizeMultiple: Integer read Get_CutterGridSizeMultiple write Set_CutterGridSizeMultiple;
property DefaultDisplayUnit: TUnit read Get_DefaultUnit write Set_DefaultUnit;
property DefaultEarthName: WideString read Get_DefaultEarthName write Set_DefaultEarthName;
property DefaultPowerGndName: WideString read Get_DefaultPowerGndName write Set_DefaultPowerGndName;
property DefaultPrimsPermanent: Boolean read Get_DefaultPrimsPermanent write Set_DefaultPrimsPermanent;
property DefaultSheetStyle: TSheetStyle read Get_DefaultSheetStyle write Set_DefaultSheetStyle;
property DefaultSignalGndName: WideString read Get_DefaultSignalGndName write Set_DefaultSignalGndName;
property DefaultTemplateFileName: WideString read Get_DefaultTemplateFileName write Set_DefaultTemplateFileName;
property DefaultUnitSystem: TUnitSystem read Get_DefaultUnitSystem;  // read-only
property DisplayPrinterFonts: Boolean read Get_DisplayPrinterFonts write Set_DisplayPrinterFonts;
property DocMenuID: WideString read Get_DocMenuID write Set_DocMenuID;
property DocumentScope: TChosenDocumentScope read Get_DocumentScope write Set_DocumentScope;
property DoubleClickRunsInspector: Boolean read Get_DoubleClickRunsInspector write Set_DoubleClickRunsInspector;
property DragStepSize: TSize read Get_DragStepSize write Set_DragStepSize;
property ExpandComponentDesignators: Boolean read Get_ExpandComponentDesignators write Set_ExpandComponentDesignators;
property ExpandDocumentNumber: Boolean read Get_ExpandDocumentNumber write Set_ExpandDocumentNumber;
property ExpandNetLabelsText: Boolean read Get_ExpandNetLabelsText write Set_ExpandNetLabelsText;
property ExpandPortsName: Boolean read Get_ExpandPortsName write Set_ExpandPortsName;
property ExpandSheetNumber: Boolean read Get_ExpandSheetNumber write Set_ExpandSheetNumber;
property FSMMenuID: WideString read Get_FSMMenuID write Set_FSMMenuID;
property GraphicsCursorStyle: TCursorShape read Get_GraphicsCursorStyle write Set_GraphicsCursorStyle;
property HotSpotGridDistance: Integer read Get_HotSpotGridDistance write Set_HotSpotGridDistance;
property IgnoreSelection: Boolean read Get_IgnoreSelection write Set_IgnoreSelection;
property LastModelType: WideString read Get_LastModelType write Set_LastModelType;
property LibMenuID: WideString read Get_LibMenuID write Set_LibMenuID;
property LibraryScope: TLibraryScope read Get_LibraryScope write Set_LibraryScope;
property MaintainOrthogonal: Boolean read Get_MaintainOrthogonal write Set_MaintainOrthogonal;
property ManualJunctionsColor: TColor read Get_ManualJunctionsColor write Set_ManualJunctionsColor;
property MarkManualParameters: Boolean read Get_MarkManualParameters write Set_MarkManualParameters;
property Metafile_Blankets: Boolean read Get_Metafile_Blankets write Set_Metafile_Blankets;
property Metafile_NoERCMarkers: Boolean read Get_Metafile_NoERCMarkers write Set_Metafile_NoERCMarkers;
property Metafile_Notes: Boolean read Get_Metafile_Notes write Set_Metafile_Notes;
property Metafile_NotesCollapsed: Boolean read Get_Metafile_NotesCollapsed write Set_Metafile_NotesCollapsed;
property Metafile_OpenEnds: Boolean read Get_Metafile_OpenEnds write Set_Metafile_OpenEnds;
property Metafile_ParameterSets: Boolean read Get_Metafile_ParameterSets write Set_Metafile_ParameterSets;
property Metafile_Probes: Boolean read Get_Metafile_Probes write Set_Metafile_Probes;
property Metafile_StrNoERCSymbolsToShow: WideString read Get_Metafile_StrNoERCSymbolsToShow write Set_Metafile_StrNoERCSymbolsToShow;
property MultiPartNamingMethod: Integer read Get_MultiPartNamingMethod write Set_MultiPartNamingMethod;
property MultipartSeparator: WideString read Get_MultiPartSeparator write Set_MultiPartSeparator;
property MultiSelectionColor: TColor read Get_MultiSelectionColor write Set_MultiSelectionColor;
property OpenBusMenuID: WideString read Get_OpenBusMenuID write Set_OpenBusMenuID;
property OptimizePolylines: Boolean read Get_OptimizePolylines write Set_OptimizePolylines;
property OrcadFootPrint: TOrcadFootPrint read Get_OrcadFootPrint write Set_OrcadFootPrint;
property PhysicalViewDimLevel: Integer read Get_PhysicalViewDimLevel write Set_PhysicalViewDimLevel;
property PinNameMargin: Integer read Get_PinNameMargin write Set_PinNameMargin;
property PinNumberMargin: Integer read Get_PinNumberMargin write Set_PinNumberMargin;
property PolylineCutterMode: TPolylineCutterMode read Get_PolylineCutterMode write Set_PolylineCutterMode;
property ResizeColor: TColor read Get_ResizeColor write Set_ResizeColor;
property RunInPlaceEditing: Boolean read Get_RunInPlaceEditing write Set_RunInPlaceEditing;
property SelectionColor: TColor read Get_SelectionColor write Set_SelectionColor;
property SelectionReference: Boolean read Get_SelectionReference write Set_SelectionReference;
property Sensitivity: Integer read Get_Sensitivity write Set_Sensitivity;
property SheetStyle_MarginWidth[S: TSheetStyle]: TCoord read Get_SheetStyle_MarginWidth;  // read-only
property SheetStyle_XSize[S: TSheetStyle]: TCoord read Get_SheetStyle_XSize;  // read-only
property SheetStyle_XZones[S: TSheetStyle]: TCoord read Get_SheetStyle_XZones;  // read-only
property SheetStyle_YSize[S: TSheetStyle]: TCoord read Get_SheetStyle_YSize;  // read-only
property SheetStyle_YZones[S: TSheetStyle]: TCoord read Get_SheetStyle_YZones;  // read-only
property ShowCutterBoxMode: TShowCutterBoxMode read Get_ShowCutterBoxMode write Set_ShowCutterBoxMode;
property ShowCutterMarkersMode: TShowCutterMarkersMode read Get_ShowCutterMarkersMode write Set_ShowCutterMarkersMode;
property ShowPinDirection: Boolean read Get_ShowPinDirection write Set_ShowPinDirection;
property SingleSlashNegation: Boolean read Get_SingleSlashNegation write Set_SingleSlashNegation;
property SnapToCenter: Boolean read Get_SnapToCenter write Set_SnapToCenter;
property SnapToHotSpot: Boolean read Get_SnapToHotSpot write Set_SnapToHotSpot;
property SpatialAnalysisDuringDragging: Boolean read Get_SpatialAnalysisDuringDragging write Set_SpatialAnalysisDuringDragging;
property StringIncA: WideString read Get_StringIncA write Set_StringIncA;
property StringIncB: WideString read Get_StringIncB write Set_StringIncB;
property StringIncRemoveLeadingZero: Boolean read Get_StringIncRemoveLeadingZero write Set_StringIncRemoveLeadingZero;
property SuperscriptDesignator: TSuperscriptMode read Get_SuperscriptDesignator write Set_SuperscriptDesignator;
property SuperscriptDocumentNumber: TSuperscriptMode read Get_SuperscriptDocumentNumber write Set_SuperscriptDocumentNumber;
property SuperscriptNetLabel: TSuperscriptMode read Get_SuperscriptNetLabel write Set_SuperscriptNetLabel;
property SuperscriptPort: TSuperscriptMode read Get_SuperscriptPort write Set_SuperscriptPort;
property SuperscriptSheetNumber: TSuperscriptMode read Get_SuperscriptSheetNumber write Set_SuperscriptSheetNumber;
property TranslateRotateColor: TColor read Get_TranslateRotateColor write Set_TranslateRotateColor;
property UndoRedoStackSize: Integer read Get_UndoRedoStackSize write Set_UndoRedoStackSize;
property UseOrcadPortWidth: Boolean read Get_UseOrcadPortWidth write Set_UseOrcadPortWidth;
property ViolationColor[ALevel: TErrorLevel]: TColor read Get_ViolationColorByLevel write Set_ViolationColorByLevel;
property ViolationDisplay[ALevel: TErrorLevel]: Boolean read Get_ViolationDisplayByLevel write Set_ViolationDisplayByLevel;
property VisibleGridColor: TColor read Get_VisibleGridColor write Set_VisibleGridColor;
property VisibleGridStyle: TVisibleGrid read Get_VisibleGridStyle write Set_VisibleGridStyle;
property WatermarkDeviceSheet: Boolean read Get_WatermarkDeviceSheet write Set_WatermarkDeviceSheet;
property WatermarkReadOnlySheet: Boolean read Get_WatermarkReadOnlySheet write Set_WatermarkReadOnlySheet;
property WireAutoJunctionsColor: TColor read Get_WireAutoJunctionsColor write Set_WireAutoJunctionsColor;
property WireAutoJunctionsSize: TSize read Get_WireAutoJunctionsSize write Set_WireAutoJunctionsSize;
property WireDragJunctionsColor: TColor read Get_WireDragJunctionsColor write Set_WireDragJunctionsColor;
function Get_AddTemplateToClipBoard: Boolean;
function Get_AllowDeviceSheetEditing: Boolean;
function Get_AlwaysDrag: Boolean;
function Get_AutoBackupFileCount: Integer;
function Get_AutoBackupTime: Integer;
function Get_AutoPanJumpDistance: Integer;
function Get_AutoPanShiftJumpDistance: Integer;
function Get_AutoPanStyle: TAutoPanStyle;
function Get_AutoZoom: Boolean;
function Get_BufferedPainting: Boolean;
function Get_BusAutoJunctionsColor: TColor;
function Get_BusAutoJunctionsSize: TSize;
function Get_BusDragJunctionsColor: TColor;
function Get_ClickClearsSelection: Boolean;
function Get_ComponentsCutWires: Boolean;
function Get_ConfirmSelectionMemoryClear: Boolean;
function Get_ConvertSpecialStrings: Boolean;
function Get_CrossRefLocationStyle: TCrossRefLocationStyle;
function Get_CrossRefSheetStyle: TCrossRefSheetStyle;
function Get_CtrlDbleClickGoesDown: Boolean;
function Get_CutterFixedLength: Integer;
function Get_CutterGridSizeMultiple: Integer;
function Get_DefaultEarthName: WideString;
function Get_DefaultPowerGndName: WideString;
function Get_DefaultPrimOverridesLibraryComment: Boolean;
function Get_DefaultPrimOverridesLibraryDesignator: Boolean;
function Get_DefaultPrimsPermanent: Boolean;
function Get_DefaultSheetStyle: TSheetStyle;
function Get_DefaultSignalGndName: WideString;
function Get_DefaultTemplateFileName: WideString;
function Get_DefaultUnit: TUnit;
function Get_DefaultUnitSystem: TUnitSystem;
function Get_DisplayPrinterFonts: Boolean;
function Get_DocMenuID: WideString;
function Get_DocumentScope: TChosenDocumentScope;
function Get_DoubleClickRunsInspector: Boolean;
function Get_DragStepSize: TSize;
function Get_ExpandComponentDesignators: Boolean;
function Get_ExpandDocumentNumber: Boolean;
function Get_ExpandNetLabelsText: Boolean;
function Get_ExpandPortsName: Boolean;
function Get_ExpandSheetNumber: Boolean;
function Get_FSMMenuID: WideString;
function Get_GraphicsCursorStyle: TCursorShape;
function Get_HotSpotGridDistance: Integer;
function Get_IgnoreSelection: Boolean;
function Get_LastModelType: WideString;
function Get_LibMenuID: WideString;
function Get_LibraryScope: TLibraryScope;
function Get_MaintainOrthogonal: Boolean;
function Get_ManualJunctionsColor: TColor;
function Get_MarkManualParameters: Boolean;
function Get_Metafile_Blankets: Boolean;
function Get_Metafile_NoERCMarkers: Boolean;
function Get_Metafile_Notes: Boolean;
function Get_Metafile_NotesCollapsed: Boolean;
function Get_Metafile_OpenEnds: Boolean;
function Get_Metafile_ParameterSets: Boolean;
function Get_Metafile_Probes: Boolean;
function Get_Metafile_StrNoERCSymbolsToShow: WideString;
function Get_MultiPartNamingMethod: Integer;
function Get_MultiPartSeparator: WideString;
function Get_MultiSelectionColor: TColor;
function Get_OpenBusMenuID: WideString;
function Get_OptimizePolylines: Boolean;
function Get_OrcadFootPrint: TOrcadFootPrint;
function Get_PhysicalViewDimLevel: Integer;
function Get_PinNameMargin: Integer;
function Get_PinNumberMargin: Integer;
function Get_PolylineCutterMode: TPolylineCutterMode;
function Get_ResizeColor: TColor;
function Get_RunInPlaceEditing: Boolean;
function Get_SelectionColor: TColor;
function Get_SelectionReference: Boolean;
function Get_Sensitivity: Integer;
function Get_SheetStyle_MarginWidth(S: TSheetStyle): Integer;
function Get_SheetStyle_XSize(S: TSheetStyle): Integer;
function Get_SheetStyle_XZones(S: TSheetStyle): Integer;
function Get_SheetStyle_YSize(S: TSheetStyle): Integer;
function Get_SheetStyle_YZones(S: TSheetStyle): Integer;
function Get_ShowCutterBoxMode: TShowCutterBoxMode;
function Get_ShowCutterMarkersMode: TShowCutterMarkersMode;
function Get_ShowPinDirection: Boolean;
function Get_SingleSlashNegation: Boolean;
function Get_SnapToCenter: Boolean;
function Get_SnapToHotSpot: Boolean;
function Get_SpatialAnalysisDuringDragging: Boolean;
function Get_StringIncA: WideString;
function Get_StringIncB: WideString;
function Get_StringIncRemoveLeadingZero: Boolean;
function Get_SuperscriptDesignator: TSuperscriptMode;
function Get_SuperscriptDocumentNumber: TSuperscriptMode;
function Get_SuperscriptNetLabel: TSuperscriptMode;
function Get_SuperscriptPort: TSuperscriptMode;
function Get_SuperscriptSheetNumber: TSuperscriptMode;
function Get_TranslateRotateColor: TColor;
function Get_UndoRedoStackSize: Integer;
function Get_UseOrcadPortWidth: Boolean;
function Get_ViolationColorByLevel(ALevel: TErrorLevel): TColor;
function Get_ViolationDisplayByLevel(ALevel: TErrorLevel): Boolean;
function Get_VisibleGridColor: TColor;
function Get_VisibleGridStyle: TVisibleGrid;
function Get_WatermarkDeviceSheet: Boolean;
function Get_WatermarkReadOnlySheet: Boolean;
function Get_WireAutoJunctionsColor: TColor;
function Get_WireAutoJunctionsSize: TSize;
function Get_WireDragJunctionsColor: TColor;
function GridPresetAt(AUnit: TUnitSystem; AnIndex: Integer): IGridSetting;
function GridPresetsCount(AUnit: TUnitSystem): Integer;
function Import_FromUser: Boolean;
procedure Set_AddTemplateToClipBoard(AValue: Boolean);
procedure Set_AllowDeviceSheetEditing(AValue: Boolean);
procedure Set_AlwaysDrag(AValue: Boolean);
procedure Set_AutoBackupFileCount(AValue: Integer);
procedure Set_AutoBackupTime(AValue: Integer);
procedure Set_AutoPanJumpDistance(AValue: Integer);
procedure Set_AutoPanShiftJumpDistance(AValue: Integer);
procedure Set_AutoPanStyle(AValue: TAutoPanStyle);
procedure Set_AutoZoom(AValue: Boolean);
procedure Set_BufferedPainting(AValue: Boolean);
procedure Set_BusAutoJunctionsColor(AValue: TColor);
procedure Set_BusAutoJunctionsSize(AValue: TSize);
procedure Set_BusDragJunctionsColor(Value: TColor);
procedure Set_ClickClearsSelection(AValue: Boolean);
procedure Set_ComponentsCutWires(AValue: Boolean);
procedure Set_ConfirmSelectionMemoryClear(AValue: Boolean);
procedure Set_ConvertSpecialStrings(AValue: Boolean);
procedure Set_CrossRefLocationStyle(AValue: TCrossRefLocationStyle);
procedure Set_CrossRefSheetStyle(AValue: TCrossRefSheetStyle);
procedure Set_CtrlDbleClickGoesDown(AValue: Boolean);
procedure Set_CutterFixedLength(AValue: Integer);
procedure Set_CutterGridSizeMultiple(AValue: Integer);
procedure Set_DefaultEarthName(AValue: WideString);
procedure Set_DefaultPowerGndName(AValue: WideString);
procedure Set_DefaultPrimOverridesLibraryComment(AValue: Boolean);
procedure Set_DefaultPrimOverridesLibraryDesignator(AValue: Boolean);
procedure Set_DefaultPrimsPermanent(AValue: Boolean);
procedure Set_DefaultSheetStyle(AValue: TSheetStyle);
procedure Set_DefaultSignalGndName(AValue: WideString);
procedure Set_DefaultTemplateFileName(AValue: WideString);
procedure Set_DefaultUnit(AValue: TUnit);
procedure Set_DisplayPrinterFonts(AValue: Boolean);
procedure Set_DocMenuID(const AValue: WideString);
procedure Set_DocumentScope(AValue: TChosenDocumentScope);
procedure Set_DoubleClickRunsInspector(AValue: Boolean);
procedure Set_DragStepSize(AValue: TSize);
procedure Set_ExpandComponentDesignators(AValue: Boolean);
procedure Set_ExpandDocumentNumber(AValue: Boolean);
procedure Set_ExpandNetLabelsText(AValue: Boolean);
procedure Set_ExpandPortsName(AValue: Boolean);
procedure Set_ExpandSheetNumber(AValue: Boolean);
procedure Set_FSMMenuID(const AValue: WideString);
procedure Set_GraphicsCursorStyle(AValue: TCursorShape);
procedure Set_HotSpotGridDistance(AValue: Integer);
procedure Set_IgnoreSelection(AValue: Boolean);
procedure Set_LastModelType(AValue: WideString);
procedure Set_LibMenuID(const AValue: WideString);
procedure Set_LibraryScope(AValue: TLibraryScope);
procedure Set_MaintainOrthogonal(AValue: Boolean);
procedure Set_ManualJunctionsColor(AValue: TColor);
procedure Set_MarkManualParameters(AValue: Boolean);
procedure Set_Metafile_Blankets(AValue: Boolean);
procedure Set_Metafile_NoERCMarkers(AValue: Boolean);
procedure Set_Metafile_Notes(AValue: Boolean);
procedure Set_Metafile_NotesCollapsed(AValue: Boolean);
procedure Set_Metafile_OpenEnds(AValue: Boolean);
procedure Set_Metafile_ParameterSets(AValue: Boolean);
procedure Set_Metafile_Probes(AValue: Boolean);
procedure Set_Metafile_StrNoERCSymbolsToShow(AValue: WideString);
procedure Set_MultiPartNamingMethod(AValue: Integer);
procedure Set_MultiPartSeparator(AValue: WideString);
procedure Set_MultiSelectionColor(AValue: TColor);
procedure Set_OpenBusMenuID(const AValue: WideString);
procedure Set_OptimizePolylines(AValue: Boolean);
procedure Set_OrcadFootPrint(AValue: TOrcadFootPrint);
procedure Set_PhysicalViewDimLevel(AValue: Integer);
procedure Set_PinNameMargin(AValue: Integer);
procedure Set_PinNumberMargin(AValue: Integer);
procedure Set_PolylineCutterMode(AValue: TPolylineCutterMode);
procedure Set_ResizeColor(AValue: TColor);
procedure Set_RunInPlaceEditing(AValue: Boolean);
procedure Set_SelectionColor(AValue: TColor);
procedure Set_SelectionReference(AValue: Boolean);
procedure Set_Sensitivity(AValue: Integer);
procedure Set_ShowCutterBoxMode(AValue: TShowCutterBoxMode);
procedure Set_ShowCutterMarkersMode(AValue: TShowCutterMarkersMode);
procedure Set_ShowPinDirection(AValue: Boolean);
procedure Set_SingleSlashNegation(AValue: Boolean);
procedure Set_SnapToCenter(AValue: Boolean);
procedure Set_SnapToHotSpot(AValue: Boolean);
procedure Set_SpatialAnalysisDuringDragging(Value: Boolean);
procedure Set_StringIncA(AValue: WideString);
procedure Set_StringIncB(AValue: WideString);
procedure Set_StringIncRemoveLeadingZero(AValue: Boolean);
procedure Set_SuperscriptDesignator(AValue: TSuperscriptMode);
procedure Set_SuperscriptDocumentNumber(AValue: TSuperscriptMode);
procedure Set_SuperscriptNetLabel(AValue: TSuperscriptMode);
procedure Set_SuperscriptPort(AValue: TSuperscriptMode);
procedure Set_SuperscriptSheetNumber(AValue: TSuperscriptMode);
procedure Set_TranslateRotateColor(AValue: TColor);
procedure Set_UndoRedoStackSize(AValue: Integer);
procedure Set_UseOrcadPortWidth(AValue: Boolean);
procedure Set_ViolationColorByLevel(ALevel: TErrorLevel; AValue: TColor);
procedure Set_ViolationDisplayByLevel(ALevel: TErrorLevel; AValue: Boolean);
procedure Set_VisibleGridColor(AValue: TColor);
procedure Set_VisibleGridStyle(AValue: TVisibleGrid);
procedure Set_WatermarkDeviceSheet(AValue: Boolean);
procedure Set_WatermarkReadOnlySheet(AValue: Boolean);
procedure Set_WireAutoJunctionsColor(AValue: TColor);
procedure Set_WireAutoJunctionsSize(AValue: TSize);
procedure Set_WireDragJunctionsColor(Value: TColor);

## ISch_Probe
继承：ISch_Probe → ISch_ParameterSet → ISch_ParametrizedGroup → ISch_GraphicalObject → ISch_BasicContainer → IInterface ｜ 单元：Rt_Schematic ｜ 自有 0 个方法、0 个属性


## ISch_RTFLink
继承：ISch_RTFLink → ISch_RectangularGroup → ISch_ParametrizedGroup → ISch_GraphicalObject → ISch_BasicContainer → IInterface ｜ 单元：Rt_Schematic ｜ 自有 3 个方法、2 个属性

property FileNameRTF: WideString read GetState_FileNameRTF write SetState_FileNameRTF;
property FullPathRTF: WideString read GetState_FullPathRTF;  // read-only
function GetState_FileNameRTF: WideString;
function GetState_FullPathRTF: WideString;
procedure SetState_FileNameRTF(AFileName: WideString);

## ISch_Rectangle
继承：ISch_Rectangle → ISch_GraphicalObject → ISch_BasicContainer → IInterface ｜ 单元：Rt_Schematic ｜ 自有 8 个方法、4 个属性

property Corner: TLocation read GetState_Corner write SetState_Corner;
property IsSolid: Boolean read GetState_IsSolid write SetState_IsSolid;
property LineWidth: TSize read GetState_LineWidth write SetState_LineWidth;
property Transparent: Boolean read GetState_Transparent write SetState_Transparent;
function GetState_Corner: IDispatch;
function GetState_IsSolid: Boolean;
function GetState_LineWidth: TSize;
function GetState_Transparent: Boolean;
procedure SetState_Corner(const ALocation: IDispatch);
procedure SetState_IsSolid(B: Boolean);
procedure SetState_LineWidth(ASize: TSize);
procedure SetState_Transparent(B: Boolean);

## ISch_RectangularGroup
继承：ISch_RectangularGroup → ISch_ParametrizedGroup → ISch_GraphicalObject → ISch_BasicContainer → IInterface ｜ 单元：Rt_Schematic ｜ 自有 4 个方法、2 个属性

property XSize: TCoord read GetState_XSize write SetState_XSize;
property YSize: TCoord read GetState_YSize write SetState_YSize;
function GetState_XSize: Integer;
function GetState_YSize: Integer;
procedure SetState_XSize(Value: Integer);
procedure SetState_YSize(Value: Integer);

## ISch_RichTextDocument
继承：ISch_RichTextDocument → ISch_Rectangle → ISch_GraphicalObject → ISch_BasicContainer → IInterface ｜ 单元：Rt_Schematic ｜ 自有 2 个方法、1 个属性

property ShowBorder: Boolean read GetState_ShowBorder write SetState_ShowBorder;
function GetState_ShowBorder: Boolean;
procedure SetState_ShowBorder(AValue: Boolean);

## ISch_RobotManager
继承：ISch_RobotManager → IInterface ｜ 单元：Rt_Schematic ｜ 自有 2 个方法、0 个属性

procedure SendMessage(Source: ISch_BasicContainer; Destination: ISch_BasicContainer; MessageID: Word; MessageData: ISch_BasicContainer);
procedure SendMessageByHandle(Source: WideString; Destination: WideString; MessageID: Word; MessageData: WideString);

## ISch_RoundRectangle
继承：ISch_RoundRectangle → ISch_Rectangle → ISch_GraphicalObject → ISch_BasicContainer → IInterface ｜ 单元：Rt_Schematic ｜ 自有 4 个方法、2 个属性

property CornerXRadius: TDistance read GetState_CornerXRadius write SetState_CornerXRadius;
property CornerYRadius: TDistance read GetState_CornerYRadius write SetState_CornerYRadius;
function GetState_CornerXRadius: Integer;
function GetState_CornerYRadius: Integer;
procedure SetState_CornerXRadius(ADistance: Integer);
procedure SetState_CornerYRadius(ADistance: Integer);

## ISch_ServerInterface
继承：ISch_ServerInterface → IInterface ｜ 单元：Rt_Schematic ｜ 自有 45 个方法、5 个属性

property FontManager: ISch_FontManager read GetState_FontManager;  // read-only
property JunctionConvertSettings: ISch_JunctionConvertSettings read GetState_JunctionConvertSettings;  // read-only
property Preferences: ISch_Preferences read GetState_SchPreferences;  // read-only
property ProbesTimerEnabled: Boolean read GetState_ProbesTimerEnabled write SetState_ProbesTimerEnabled;
property RobotManager: ISch_RobotManager read GetState_RobotManager;  // read-only
function CreateComponentMetafilePainter: IComponentMetafilePainter;
function CreateComponentPainter: IComponentPainterView;
function CreateDocumentPainter: IDocumentPainterView;
function CreateLibCompFullInfoReader(ALibFileName: WideString): ILibCompFullInfoReader;
function CreateLibCompInfoReader(ALibFileName: WideString): ILibCompInfoReader;
function CreateSchLibrary: ISch_Lib;
function CreateSchLibraryWrapped: ISch_Lib;
procedure DestroyCompFullInfoReader(var ALibCompReader: ILibCompFullInfoReader);
procedure DestroyCompInfoReader(var ALibCompReader: ILibCompInfoReader);
procedure DestroySchLibrary(var SchLib: ISch_Lib);
procedure DestroySchObject(var ASchObject: ISch_BasicContainer);
function GetCurrentSchDocument: ISch_Document;
function GetDDMHarnessProject(const AProjectFilePath: WideString): IDDMHarnessProject;
function GetDialogManager: ISch_DialogManager;
function GetDMHarnessObjectHelper: IInterface;
function GetHarnessUtils: ISch_HarnessUtils;
function GetSchDocumentByPath(APath: WideString): ISch_Document;
function GetSchDocumentByPathWrapped(const APath: WideString): ISch_Document;
function GetSchDocumentBySchDocID(DocID: Integer): ISch_Document;
function GetState_FontManager: ISch_FontManager;
function GetState_JunctionConvertSettings: ISch_JunctionConvertSettings;
function GetState_ProbesTimerEnabled: Boolean;
function GetState_RobotManager: ISch_RobotManager;
function GetState_SchPreferences: ISch_Preferences;
function LoadComponent(ALibIdentifierKind: TLibIdentifierKind; const ALibraryIdentifier: WideString; const ADesignItemID: WideString): ISch_Component;
function LoadComponentFromDatabaseLibrary(ALibraryName: WideString; ADatabaseTableName: WideString; ADatabaseKeys: WideString): ISch_Component;
function LoadComponentFromLibrary(ALibReference: WideString; ALibraryName: WideString): ISch_Component;
function LoadComponentFromLibraryWrapped(ALibReference: WideString; ALibraryName: WideString): ISch_Component;
function LoadComponentWrapped(ALibIdentifierKind: TLibIdentifierKind; const ALibraryIdentifier: WideString; const ADesignItemID: WideString): ISch_Component;
function LoadDesignItemDeviceSheet(ALibIdentifierKind: TLibIdentifierKind; const ALibraryIdentifier: WideString; const ADesignItemID: WideString; LocationX: Integer; LocationY: Integer): ISch_SheetSymbol;
function LoadSchDocumentByPath(const AFullPath: WideString): ISch_Document;
function LoadSchDocumentByPathWrapped(const AFullPath: WideString): ISch_Document;
function PaintComponentThumbnail(SymbolName: WideString; SymbolLibraryFullPath: WideString; PartIndex: Integer; Width: Integer; Height: Integer): HBITMAP;
function PaintDeviceSheetThumbnail(DeviceSheetName: WideString; Width: Integer; Height: Integer): HBITMAP;
function PaintLoadedComponentThumbnail(ASchPart: ISch_Component; PartIndex: Integer; Width: Integer; Height: Integer): HBITMAP;
function ReportSchObjectsDifferences(const AObject1: ISch_BasicContainer; const AObject2: ISch_BasicContainer; AIgnoreSpatialAttributes: Boolean; ADiffDescription: PWideChar): Integer;
procedure SaveSchDocument(ADoc: ISch_Document; AFullPath: WideString; AFileFormat: WideString);
function SchObjectFactory(AObjectId: TObjectId; ACreationMode: TObjectCreationMode): ISch_BasicContainer;
function SchObjectFactoryBySettings(AObjectId: TObjectId; AUnit: TUnitSystem): ISch_BasicContainer;
function SelectWireHarness(const AHarnessList: WideString): WideString;
procedure SetDocumentManagedTemplate(const ADocument: IServerDocument; const AVaultGUID: WideString; const ARevisionGUID: WideString; AAction: TTemplateUpdateAction; ASilent: Boolean);
procedure SetOriginalHarnessProject(const AProjectFilePath: WideString; const AOriginalProject: IProject);
procedure SetState_ProbesTimerEnabled(AValue: Boolean);
procedure UpdateDocumentTemplate(ADocument: IServerDocument; VaultGUID: WideString; ItemRevisionGUID: WideString);
function UpdateSignalValueDisplay(DMObject: IDMObject; Value: Integer; BitIndex: Integer): LongBool;

## ISch_Sheet
继承：ISch_Sheet → ISch_Document → ISch_ParametrizedGroup → ISch_GraphicalObject → ISch_BasicContainer → IInterface ｜ 单元：Rt_Schematic ｜ 自有 4 个方法、3 个属性

property BusConnections: IConnectionsArray read GetState_BusConnections;  // read-only
property HasUnsavedUniqueIdsChanges: Boolean read GetState_HasUnsavedUniqueIdsChanges;  // read-only
property WireConnections: IConnectionsArray read GetState_WireConnections;  // read-only
procedure AddReuseBlockPartInfo(const ABlockId: WideString; const ABlockGUID: IFullItemGUID; const ASchSnippetGUID: IFullItemGUID; const APcbSnippetGUID: IFullItemGUID; const AUniqueId: WideString; const AUniqueIdInReuseBlock: WideString);
function GetState_BusConnections: IConnectionsArray;
function GetState_HasUnsavedUniqueIdsChanges: Boolean;
function GetState_WireConnections: IConnectionsArray;

## ISch_SheetEntry
继承：ISch_SheetEntry → ISch_GraphicalObject → ISch_BasicContainer → IInterface ｜ 单元：Rt_Schematic ｜ 自有 29 个方法、13 个属性

property ArrowKind: TArrowKind read GetState_ArrowKind write SetState_ArrowKind;
property DistanceFromTop: TCoord read GetState_DistanceFromTop write SetState_DistanceFromTop;
property HarnessColor: TColor read GetState_HarnessColor write SetState_HarnessColor;
property HarnessType: WideString read GetState_HarnessType write SetState_HarnessType;
property IOType: TPortIO read GetState_IOType write SetState_IOType;
property Name: WideString read GetState_Name write SetState_Name;
property OverrideDisplayString: WideString read GetState_OverrideDisplayString write SetState_OverrideDisplayString;
property OwnerSheetSymbol: ISch_SheetSymbol read GetState_OwnerSchSheetSymbol;  // read-only
property Side: TLeftRightSide read GetState_Side write SetState_Side;
property Style: TPortArrowStyle read GetState_Style write SetState_Style;
property TextColor: TColor read GetState_TextColor write SetState_TextColor;
property TextFontID: TFontID read GetState_TextFontID write SetState_TextFontID;
property TextStyle: TBusTextStyle read GetState_TextStyle write SetState_TextStyle;
procedure DeleteCrossRef;
function GetState_ArrowKind: TArrowKind;
function GetState_CrossRef: WideString;
function GetState_DistanceFromTop: Integer;
function GetState_HarnessColor: TColor;
function GetState_HarnessType: WideString;
function GetState_IOType: TPortIO;
function GetState_Name: WideString;
function GetState_OverrideDisplayString: WideString;
function GetState_OwnerSchSheetSymbol: ISch_SheetSymbol;
function GetState_Side: TLeftRightSide;
function GetState_Style: TPortArrowStyle;
function GetState_TextColor: TColor;
function GetState_TextFontID: Integer;
function GetState_TextStyle: TBusTextStyle;
function IsVertical: Boolean;
procedure SetState_ArrowKind(Value: TArrowKind);
procedure SetState_CrossRef(AValue: WideString);
procedure SetState_DistanceFromTop(Value: Integer);
procedure SetState_HarnessColor(AValue: TColor);
procedure SetState_HarnessType(Value: WideString);
procedure SetState_IOType(Value: TPortIO);
procedure SetState_Name(Value: WideString);
procedure SetState_OverrideDisplayString(Value: WideString);
procedure SetState_Side(Value: TLeftRightSide);
procedure SetState_Style(Value: TPortArrowStyle);
procedure SetState_TextColor(Value: TColor);
procedure SetState_TextFontID(Value: Integer);
procedure SetState_TextStyle(Value: TBusTextStyle);

## ISch_SheetFileName
继承：ISch_SheetFileName → ISch_ComplexText → ISch_Label → ISch_GraphicalObject → ISch_BasicContainer → IInterface ｜ 单元：Rt_Schematic ｜ 自有 0 个方法、0 个属性


## ISch_SheetName
继承：ISch_SheetName → ISch_ComplexText → ISch_Label → ISch_GraphicalObject → ISch_BasicContainer → IInterface ｜ 单元：Rt_Schematic ｜ 自有 0 个方法、0 个属性


## ISch_SheetSymbol
继承：ISch_SheetSymbol → ISch_RectangularGroup → ISch_ParametrizedGroup → ISch_GraphicalObject → ISch_BasicContainer → IInterface ｜ 单元：Rt_Schematic ｜ 自有 28 个方法、13 个属性

property DesignItemId: WideString read GetState_DesignItemId write SetState_DesignItemId;
property IsSolid: Boolean read GetState_IsSolid write SetState_IsSolid;
property ItemGUID: WideString read GetState_ItemGUID write SetState_ItemGUID;
property LibIdentifierKind: TLibIdentifierKind read GetState_LibIdentifierKind;  // read-only
property LibraryIdentifier: WideString read GetState_LibraryIdentifier;  // read-only
property LineWidth: TSize read GetState_LineWidth write SetState_LineWidth;
property RevisionGUID: WideString read GetState_RevisionGUID write SetState_RevisionGUID;
property SheetFileName: ISch_SheetFileName read GetState_SchSheetFileName;  // read-only
property SheetName: ISch_SheetName read GetState_SchSheetName;  // read-only
property ShowHiddenFields: Boolean read GetState_ShowHiddenFields write SetState_ShowHiddenFields;
property SourceLibraryName: WideString read GetState_SourceLibraryName write SetState_SourceLibraryName;
property SymbolType: TSheetSymbolType read GetState_SymbolType write SetState_SymbolType;
property VaultGUID: WideString read GetState_VaultGUID write SetState_VaultGUID;
procedure ChangeSymbolType(AType: TSheetSymbolType);
function CreateEntry: ISch_SheetEntry;
procedure DeleteEntry(const AEntry: ISch_SheetEntry);
function GetState_DesignItemId: WideString;
function GetState_IsSolid: Boolean;
function GetState_ItemGUID: WideString;
function GetState_LibIdentifierKind: TLibIdentifierKind;
function GetState_LibraryIdentifier: WideString;
function GetState_LineWidth: TSize;
function GetState_RevisionGUID: WideString;
function GetState_SchSheetFileName: ISch_SheetFileName;
function GetState_SchSheetFullPath: WideString;
function GetState_SchSheetName: ISch_SheetName;
function GetState_ShowHiddenFields: Boolean;
function GetState_SourceLibraryName: WideString;
function GetState_SymbolType: TSheetSymbolType;
function GetState_VaultGUID: WideString;
function SelectSchSheetFileName(out AFileName: WideString): LongBool;
procedure SetState_DesignItemId(Value: WideString);
procedure SetState_IsSolid(Value: Boolean);
procedure SetState_ItemGUID(Value: WideString);
procedure SetState_LineWidth(Value: TSize);
procedure SetState_RevisionGUID(Value: WideString);
procedure SetState_ShowHiddenFields(Value: Boolean);
procedure SetState_SourceLibraryName(Value: WideString);
procedure SetState_SymbolType(Value: TSheetSymbolType);
procedure SetState_VaultGUID(Value: WideString);
procedure UpdateToLatestRevision;

## ISch_Symbol
继承：ISch_Symbol → ISch_GraphicalObject → ISch_BasicContainer → IInterface ｜ 单元：Rt_Schematic ｜ 自有 10 个方法、5 个属性

property IsMirrored: Boolean read GetState_IsMirrored write SetState_IsMirrored;
property LineWidth: TSize read GetState_LineWidth write SetState_LineWidth;
property Orientation: TRotationBy90 read GetState_Orientation write SetState_Orientation;
property ScaleFactor: TCoord read GetState_ScaleFactor write SetState_ScaleFactor;
property Symbol: TIeeeSymbol read GetState_Symbol write SetState_Symbol;
function GetState_IsMirrored: Boolean;
function GetState_LineWidth: TSize;
function GetState_Orientation: TRotationBy90;
function GetState_ScaleFactor: Integer;
function GetState_Symbol: TIeeeSymbol;
procedure SetState_IsMirrored(AValue: Boolean);
procedure SetState_LineWidth(AValue: TSize);
procedure SetState_Orientation(AValue: TRotationBy90);
procedure SetState_ScaleFactor(AValue: Integer);
procedure SetState_Symbol(AValue: TIeeeSymbol);

## ISch_Template
继承：ISch_Template → ISch_GraphicalObject → ISch_BasicContainer → IInterface ｜ 单元：Rt_Schematic ｜ 自有 2 个方法、1 个属性

property FileName: WideString read GetState_FileName write SetState_FileName;
function GetState_FileName: WideString;
procedure SetState_FileName(AValue: WideString);

## ISch_TextFrame
继承：ISch_TextFrame → ISch_Rectangle → ISch_GraphicalObject → ISch_BasicContainer → IInterface ｜ 单元：Rt_Schematic ｜ 自有 14 个方法、8 个属性

property Alignment: THorizontalAlign read GetState_Alignment write SetState_Alignment;
property ClipToRect: Boolean read GetState_ClipToRect write SetState_ClipToRect;
property FontID: Integer read GetState_FontId write SetState_FontId;
property ShowBorder: Boolean read GetState_ShowBorder write SetState_ShowBorder;
property Text: WideString read GetState_Text write SetState_Text;
property TextColor: TColor read GetState_TextColor write SetState_TextColor;
property TextMargin: TCoord read GetState_TextMargin write SetState_TextMargin;
property WordWrap: Boolean read GetState_WordWrap write SetState_WordWrap;
function GetState_Alignment: THorizontalAlign;
function GetState_ClipToRect: Boolean;
function GetState_FontId: Integer;
function GetState_ShowBorder: Boolean;
function GetState_TextColor: TColor;
function GetState_TextMargin: Integer;
function GetState_WordWrap: Boolean;
procedure SetState_Alignment(AValue: THorizontalAlign);
procedure SetState_ClipToRect(AValue: Boolean);
procedure SetState_FontId(AValue: Integer);
procedure SetState_ShowBorder(AValue: Boolean);
procedure SetState_TextColor(AValue: TColor);
procedure SetState_TextMargin(AValue: Integer);
procedure SetState_WordWrap(AValue: Boolean);

## ISch_Voltage
继承：ISch_Voltage → ISch_ParametrizedGroup → ISch_GraphicalObject → ISch_BasicContainer → IInterface ｜ 单元：Rt_Schematic ｜ 自有 3 个方法、0 个属性

function GetState_IsVoltageComponent: Boolean;
function GetState_SignalType: WideString;
procedure SetState_SignalType(AValue: WideString);

## ISch_Wire
继承：ISch_Wire → ISch_BasicPolyline → ISch_Polygon → ISch_GraphicalObject → ISch_BasicContainer → IInterface ｜ 单元：Rt_Schematic ｜ 自有 10 个方法、4 个属性

property AutoWire: Boolean read GetState_AutoWire write SetState_AutoWire;
property CompilationMaskedSegment[AIndex: Integer]: Boolean read GetState_CompilationMaskedSegment write SetState_CompilationMaskedSegment;
property EditingEndPoint: Boolean read GetState_EditingEndPoint write SetState_EditingEndPoint;
property UnderlineColor: TColor read GetState_UnderlineColor write SetState_UnderlineColor;
function GetState_AutoWire: Boolean;
function GetState_CompilationMaskedSegment(AIndex: Integer): Boolean;
function GetState_EditingEndPoint: Boolean;
function GetState_UnderlineColor: TColor;
procedure OrderCrossOverArray;
procedure ResetCompilationMaskedSegments;
procedure SetState_AutoWire(AValue: Boolean);
procedure SetState_CompilationMaskedSegment(AIndex: Integer; AValue: Boolean);
procedure SetState_EditingEndPoint(AValue: Boolean);
procedure SetState_UnderlineColor(AValue: TColor);

## ISch_WrappedObject
继承：ISch_WrappedObject → IInterface ｜ 单元：Rt_Schematic ｜ 自有 1 个方法、0 个属性

function GetOrCreateWrapper: ISch_Wrapper;

## ISch_Wrapper
继承：ISch_Wrapper → IInterface ｜ 单元：Rt_Schematic ｜ 自有 1 个方法、0 个属性

procedure ReleaseObject;

