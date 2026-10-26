# PCB 接口（IPCB_*，单元 RT_PCB）

来源：Altium Designer 23.1.1.15 的 `System\ScriptingSystem.dll`（脚本引擎的注册表，2026-10-25 提取）。由 `scripts/gen_docs.py` 生成，不要手改。

每节列出该接口**自己注册的**成员；继承来的成员在父接口那一节（`继承` 一行给出链）。查某个接口的全部成员（含继承）用 `scripts/lookup.py <接口名>`。
属性写成 `read <getter> write <setter>`，没有 `write` 的是只读属性（行尾 `// read-only`），不要赋值（`IPCB_Board.LayerColor` 赋值实测会卡死执行器）。getter/setter 本身也是注册过的方法，可以直接调用。

## IBoardStackReportSettings
继承：IBoardStackReportSettings → IInterface ｜ 单元：RT_PCB ｜ 自有 10 个方法、0 个属性

function GetState_ColumnName(const AIndex: Integer): WideString;
function GetState_ColumnsCount: Integer;
function GetState_ColumnTitle(const AIndex: Integer): WideString;
function GetState_ColumnVisible(const AIndex: Integer): Boolean;
function GetState_Units: TUnit;
procedure SetState_ColumnVisible(const AIndex: Integer; const AVisible: Boolean);
procedure SetState_MoveDown(const AIndex: Integer);
procedure SetState_MoveUp(const AIndex: Integer);
procedure SetState_NewColumn(const ATitle: WideString; const Name: WideString; const AVisible: Boolean);
procedure SetState_Units(const AValue: TUnit);

## ICoordPointPairList
继承：ICoordPointPairList → IInterface ｜ 单元：RT_PCB ｜ 自有 2 个方法、0 个属性

function GetCoordPointPair(I: Integer): IDispatch;
function GetCount: Integer;

## IDialogManagerProvider
继承：IDialogManagerProvider → IInterface ｜ 单元：RT_PCB ｜ 自有 1 个方法、0 个属性

function GetDialogsManager: IPCB_DialogsManager;

## IHealthCheckIssueCategory
继承：IHealthCheckIssueCategory → IInterface ｜ 单元：RT_PCB ｜ 自有 2 个方法、0 个属性

function GetState_Identity: THealthCheckId;
function GetState_IssuesCount: Integer;

## IHealthCheckIssuesSettings
继承：IHealthCheckIssuesSettings → IInterface ｜ 单元：RT_PCB ｜ 自有 9 个方法、0 个属性

function GetState_AdditionalCommandName: WideString;
function GetState_GetIssueCategory(const AIndex: Integer): IHealthCheckIssueCategory;
function GetState_GetIssuesCategoriesCount: Integer;
function GetState_IsAdditionalCommandAvailable: Boolean;
function GetState_IssuesDescription: WideString;
function GetState_IssuesNote: WideString;
function GetState_MainCommandName: WideString;
procedure RunAdditionalCommand;
procedure RunMainCommand;

## ILayerValueIterator
继承：ILayerValueIterator → IPCB_LayerIterator → IInterface ｜ 单元：RT_PCB ｜ 自有 2 个方法、1 个属性

property Value: Pointer read GetValue write SetValue;
function GetValue: Pointer;
procedure SetValue(const Value: Pointer);

## IPCB_3DBody
继承：IPCB_3DBody → IInterface ｜ 单元：RT_PCB ｜ 自有 17 个方法、0 个属性

procedure Assign(ASource: IPCB_3DBody);
function Clone: IPCB_3DBody;
function FaceCount: Integer;
function FaceCountForPart(const APartIndex: Integer): Integer;
function FindPart(const APartName: string): Integer;
procedure GetAABB(out LowX: Single; out LowY: Single; out LowZ: Single; out HighX: Single; out HighY: Single; out HighZ: Single);
function GetFace(AIndex: Integer): IPCB_3DBodyFace;
function GetFaceForPart(const APartIndex: Integer; AFaceIndex: Integer): Integer;
function GetNameOfPart(const APartIndex: Integer): string;
function GetPartIndex(AIndex: Integer): Integer;
procedure GetPartTriangleRange(const APartIndex: Integer; out AStartTriangleIndex: Integer; out ATrinaglesCount: Integer);
procedure GetTriangleIndices(ATriangleIndex: Integer; out AVertex1Index: Integer; out AVertex2Index: Integer; out AVertex3Index: Integer);
procedure GetVertex(AIndex: Integer; out AX: Single; out AY: Single; out AZ: Single; out ANormalX: Byte; out ANormalY: Byte; out ANormalZ: Byte; out AColorR: Byte; out AColorG: Byte; out AColorB: Byte; out AColorA: Byte);
function PartsCount: Integer;
function RayCast(const ARayOriginX: Single; const ARayOriginY: Single; const ARayOriginZ: Single; const ARayDirX: Single; const ARayDirY: Single; const ARayDirZ: Single): IPCB_3DBodyHitInfo;
function TriangleCount: Integer;
function VertexCount: Integer;

## IPCB_3DBodyFace
继承：IPCB_3DBodyFace → IInterface ｜ 单元：RT_PCB ｜ 自有 6 个方法、0 个属性

function FaceIndex: Integer;
function GetTriangleIndex(const AIndex: Integer): Integer;
procedure GetTriangleIndices(const AIndex: Integer; out AVertex1Index: Integer; out AVertex2Index: Integer; out AVertex3Index: Integer);
function PartIndex: Integer;
function StartTriangleIndex: Integer;
function TriangleCount: Integer;

## IPCB_3DBodyHitInfo
继承：IPCB_3DBodyHitInfo → IInterface ｜ 单元：RT_PCB ｜ 自有 2 个方法、0 个属性

function Count: Integer;
procedure GetHitInfo(AIndex: Integer; out ATriangleIndex: Integer; out AIntPtX: Single; out AIntPtY: Single; out AIntPtZ: Single);

## IPCB_AbstractIterator
继承：IPCB_AbstractIterator → IInterface ｜ 单元：RT_PCB ｜ 自有 10 个方法、0 个属性

procedure AddFilter_AllLayers;
procedure AddFilter_Area(x1: Integer; y1: Integer; x2: Integer; y2: Integer);
procedure AddFilter_IPCB_LayerSet(ALayerSet: IPCB_LayerSet);
procedure AddFilter_LayerSet(ALayerSet: TV6_LayerSet);
procedure AddFilter_LayerSetA(ALayerSet: array of Integer);
procedure AddFilter_ObjectSet(AObjectSet: TObjectSet);
function FirstPCBObject: IPCB_Primitive;
function I_ObjectAddress: Pointer;
function NextPCBObject: IPCB_Primitive;
procedure SetState_FilterAll;

## IPCB_AbstractOptions
继承：IPCB_AbstractOptions → IInterface ｜ 单元：RT_PCB ｜ 自有 9 个方法、1 个属性

property OptionsObjectID: TOptionsObjectId read GetState_ObjectID write SetState_ObjectID;
procedure Export_ToParameters(Parameters: PWideChar);
procedure Export_ToParameters_Version3(Parameters: PWideChar);
procedure Export_ToParameters_Version4(Parameters: PWideChar);
function GetState_ObjectID: TOptionsObjectId;
function I_ObjectAddress: Pointer;
procedure Import_FromParameters(DisplayUnit: TUnit; Parameters: PWideChar);
procedure Import_FromParameters_Version3(DisplayUnit: TUnit; Parameters: PWideChar);
procedure Import_FromParameters_Version4(DisplayUnit: TUnit; Parameters: PWideChar);
procedure SetState_ObjectID(OId: TOptionsObjectId);

## IPCB_AccordinGraphicIterator
继承：IPCB_AccordinGraphicIterator → IInterface ｜ 单元：RT_PCB ｜ 自有 2 个方法、0 个属性

function First: IPCB_Primitive;
function Next: IPCB_Primitive;

## IPCB_Accordion
继承：IPCB_Accordion → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 15 个方法、7 个属性

property AmplitudeIncrement: TCoord read GetState_AmplitudeIncrement write SetState_AmplitudeIncrement;
property ConnecitonLength: TCoord read GetState_ConnecitonLength;  // read-only
property EstimateLength: TCoord read GetState_EstimateLength;  // read-only
property Gap: TCoord read GetState_Gap write SetState_Gap;
property GapIncrement: TCoord read GetState_GapIncrement write SetState_GapIncrement;
property MaxAmplitude: TCoord read GetState_MaxAmplitude write SetState_MaxAmplitude;
property Style: TAccordionStyle read GetState_Style write SetState_Style;
function GetState_AmplitudeIncrement: Integer;
function GetState_ConnecitonLength: Integer;
function GetState_EstimateLength: Integer;
function GetState_Gap: Integer;
function GetState_GapIncrement: Integer;
function GetState_MaxAmplitude: Integer;
function GetState_Settings: IPCB_AccordionMakerSettings;
function GetState_Style: TAccordionStyle;
function Rebuild: Boolean;
procedure SetState_AmplitudeIncrement(Value: Integer);
procedure SetState_Gap(Value: Integer);
procedure SetState_GapIncrement(Value: Integer);
procedure SetState_MaxAmplitude(Value: Integer);
procedure SetState_Style(Value: TAccordionStyle);
procedure UpdateNetByPrimitive(APrimitive: IPCB_Primitive);

## IPCB_AccordionDiffPairMakerSettings
继承：IPCB_AccordionDiffPairMakerSettings → IInterface ｜ 单元：RT_PCB ｜ 自有 8 个方法、2 个属性

property DiffPairTunedTrack: IPCB_Primitive read GetState_DiffPairTunedTrack;  // read-only
property LastOtherPinPair: IPCB_PinPair read GetState_LastOtherPinPair;  // read-only
function GetPinPairActualValue: Integer;
function GetState_DiffPair: IPCB_DifferentialPair;
function GetState_DiffPairOldLength: Integer;
function GetState_DiffPairTunedTrack: IPCB_Primitive;
function GetState_LastOtherPinPair: IPCB_PinPair;
function LastState: IPCB_AccordionMakerSettings;
procedure SetState_DiffPairOldLength(ANewValue: Integer);
procedure UpdateDiffPairPinPairsNet(const ANet: IPCB_Net);

## IPCB_AccordionMakerSettings
继承：IPCB_AccordionMakerSettings → IInterface ｜ 单元：RT_PCB ｜ 自有 124 个方法、31 个属性

property ActualMatchedLengthRule: IPCB_MatchedNetLengthsConstraint read GetState_ActualMatchedLengthRule write SetState_ActualMatchedLengthRule;
property Amplitude: TCoord read GetState_Amplitude write SetState_Amplitude;
property AmplitudeDirection: Integer read GetState_AmplitudeDirection;  // read-only
property AmplitudeIncrement: TCoord read GetState_AmplitudeIncrement write SetState_AmplitudeIncrement;
property ClipToTargetLength: Boolean read GetState_ClipToTargetLength write SetState_ClipToTargetLength;
property Gap: TCoord read GetState_Gap write SetState_Gap;
property GapIncrement: TCoord read GetState_GapIncrement write SetState_GapIncrement;
property LastPinPair: IPCB_PinPair read GetState_LastPinPair;  // read-only
property LastSourceDiffPair: IPCB_DifferentialPair read GetState_LastSourceDiffPair write SetState_LastSourceDiffPair;
property LastSourceNet: IPCB_Net read GetState_LastSourceNet write SetState_LastSourceNet;
property LengthRule: IPCB_MaxMinLengthConstraint read GetState_LengthRule write SetState_LengthRule;
property MatchedLengthRule: IPCB_MatchedNetLengthsConstraint read GetState_MatchedLengthRule;  // read-only
property MatchinglngthRuleRanges[I: Integer]: IPCB_MatchedLengthRange read GetState_MatchinglngthRuleRanges;  // read-only
property MaxLength: TCoord read GetState_MaxLength write SetState_MaxLength;
property MaxValidLength: TCoord read GetState_MaxValidLength write SetState_MaxValidLength;
property MinLength: TCoord read GetState_MinLength write SetState_MinLength;
property MinValidLength: TCoord read GetState_MinValidLength write SetState_MinValidLength;
property MitterRadiusRatio: Double read GetState_MitterRadiusRatio write SetState_MitterRadiusRatio;
property Net: IPCB_Net read GetState_Net;  // read-only
property OldLength: TCoord read GetState_OldLength write SetState_OldLength;
property OriginalNetLength: TCoord read GetState_OriginalNetLength write SetState_OriginalNetLength;
property RangeIsValid: Boolean read GetState_RangeIsValid write SetState_RangeIsValid;
property RuleExist: Boolean read GetState_RuleExist write SetState_RuleExist;
property Style: TAccordionStyle read GetState_Style write SetState_Style;
property TargetDelay: Double read GetState_TargetDelay write SetState_TargetDelay;
property TargetLength: TCoord read GetState_TargetLength write SetState_TargetLength;
property TargetLengthMode: TTargetLengthMode read GetState_TargetLengthMode write SetState_TargetLengthMode;
property Tolerance: TCoord read GetState_Tolerance write SetState_Tolerance;
property TunedObject: IPCB_Primitive read GetState_TunedObject write SetState_TunedObject;
property UseDelayUnits: Boolean read GetState_UseDelayUnits write SetState_UseDelayUnits;
property UseTargetSource: Boolean read GetState_UseTargetSource write SetState_UseTargetSource;
function CalculateNetLength(ANet: IPCB_Net): Int64;
function CalculatePinPairLength(APinPair: IPCB_PinPair): Int64;
function ClampedMaxOf4(const A: Integer; const b: Integer; const C: Integer; const D: Integer): Integer;
function ClampedMinOf4(const A: Integer; const b: Integer; const C: Integer; const D: Integer): Integer;
procedure ClearLastState;
function Clone: IPCB_AccordionMakerSettings;
function ConvertDelayToLength(const ADelay: Double): Integer;
function ConvertDelayToLength_PicoSeconds(const ADelay: Double): Integer;
function ConvertLengthToDelay(const LengthVal: Integer): Double;
function ConvertLengthToDelay_PicoSeconds(const LengthVal: Integer): Double;
function CoordToString(const ACoord: Integer): string;
function DiffPairClassifier_CategoriesCount: Integer;
function DiffPairClassifier_CategoryName(I: Integer): WideString;
function DiffPairClassifier_CategoryObjects(I: Integer): ISafeInterfaceList;
function DiffPairClassifier_Run(ADiffPair: IPCB_Primitive; ABoard: IPCB_Board): Boolean;
procedure Export_ToParameters(const Parameters: IParameterList);
procedure ExportTo_SystemOptions;
function GetState_AccordionMode: TAccordionMode;
function GetState_AccordionMode2: TAccordionMode;
function GetState_ActualMatchedLengthRule: IPCB_MatchedNetLengthsConstraint;
function GetState_Amplitude: Integer;
function GetState_AmplitudeDirection: Integer;
function GetState_AmplitudeIncrement: Integer;
function GetState_ClipToTargetLength: Boolean;
function GetState_Gap: Integer;
function GetState_GapIncrement: Integer;
function GetState_Gauge: Pointer;
function GetState_LastPinPair: IPCB_PinPair;
function GetState_LastSourceDiffPair: IPCB_DifferentialPair;
function GetState_LastSourceNet: IPCB_Net;
function GetState_LengthRule: IPCB_MaxMinLengthConstraint;
function GetState_MatchedLengthRule: IPCB_MatchedNetLengthsConstraint;
function GetState_MatchinglngthRuleRanges(I: Integer): IPCB_MatchedLengthRange;
function GetState_MaxLength: Integer;
function GetState_MaxValidLength: Integer;
function GetState_MinAmplitude: Integer;
function GetState_MinLength: Integer;
function GetState_MinValidLength: Integer;
function GetState_MitterRadiusRatio: Double;
function GetState_Net: IPCB_Net;
function GetState_OldLength: Integer;
function GetState_OriginalNetLength: Integer;
function GetState_RangeIsValid: Boolean;
function GetState_RecentlyUsedDelays(const Index: Integer): Double;
function GetState_RecentlyUsedDelaysCount: Integer;
function GetState_RecentlyUsedLengths(const Index: Integer): Integer;
function GetState_RecentlyUsedLengthsCount: Integer;
function GetState_RotationSnapping: Boolean;
function GetState_RuleExist: Boolean;
function GetState_SawtoothAngle: Double;
function GetState_SawtoothFixedSize: Boolean;
function GetState_SawtoothMinHeight: Integer;
function GetState_SawtoothMinJoint: Integer;
function GetState_SawtoothWidth: Integer;
function GetState_ShowLengthGauge: LongBool;
function GetState_SingleSide: Boolean;
function GetState_Style: TAccordionStyle;
function GetState_TargetDelay: Double;
function GetState_TargetLength: Integer;
function GetState_TargetLengthMode: TTargetLengthMode;
function GetState_Tolerance: Integer;
function GetState_TunedObject: IPCB_Primitive;
function GetState_UseDelayUnits: Boolean;
function GetState_UseTargetSource: Boolean;
procedure Import_FromParameters(const Parameters: IParameterList);
procedure ImportFrom_SystemOptions;
procedure InitilizeTargetRange;
function LastSourceRuleByUniqueID: IPCB_MatchedNetLengthsConstraint;
function LastState: IPCB_AccordionMakerSettings;
function MatchinglngthRuleRanges_Count: Integer;
procedure ModeParameters_ExportTo_SystemOptions;
procedure ModeParameters_ImportFrom_SystemOptions;
function NetsClassifier_CategoriesCount: Integer;
function NetsClassifier_CategoryName(I: Integer): WideString;
function NetsClassifier_CategoryObjects(I: Integer): ISafeInterfaceList;
function NetsClassifier_Run(ANet: IPCB_Net; ABoard: IPCB_Board; const ANetClassificationSet: TNetClassificationSet): Boolean;
procedure NextStyle;
procedure PopState;
procedure PreviousStyle;
procedure PushState;
procedure RecalculateTargetRange;
procedure SetState_AccordionMode(const ANewValue: TAccordionMode);
procedure SetState_ActualMatchedLengthRule(ARule: IPCB_MatchedNetLengthsConstraint);
procedure SetState_Amplitude(ANewValue: Integer);
procedure SetState_AmplitudeIncrement(ANewValue: Integer);
procedure SetState_ClipToTargetLength(ANewValue: Boolean);
procedure SetState_Default;
procedure SetState_Gap(ANewValue: Integer);
procedure SetState_GapIncrement(ANewValue: Integer);
procedure SetState_Gauge(const AValue: Pointer);
procedure SetState_LastSourceDiffPair(ANewValue: IPCB_DifferentialPair);
procedure SetState_LastSourceNet(ANewValue: IPCB_Net);
procedure SetState_LengthRule(ANewValue: IPCB_MaxMinLengthConstraint);
procedure SetState_MaxLength(const Value: Integer);
procedure SetState_MaxValidLength(ANewValue: Integer);
procedure SetState_MinAmplitude(ANewValue: Integer);
procedure SetState_MinLength(const Value: Integer);
procedure SetState_MinValidLength(ANewValue: Integer);
procedure SetState_MitterRadiusRatio(const ANewValue: Double);
procedure SetState_OldLength(ANewValue: Integer);
procedure SetState_OriginalNetLength(ANewValue: Integer);
procedure SetState_RangeIsValid(ANewValue: Boolean);
procedure SetState_RotationSnapping(ANewValue: Boolean);
procedure SetState_RuleExist(const AValue: Boolean);
procedure SetState_SawtoothAngle(ANewValue: Double);
procedure SetState_SawtoothFixedSize(ANewValue: Boolean);
procedure SetState_SawtoothMinHeight(ANewValue: Integer);
procedure SetState_SawtoothMinJoint(ANewValue: Integer);
procedure SetState_SawtoothWidth(ANewValue: Integer);
procedure SetState_ShowLengthGauge(const ANewValue: LongBool);
procedure SetState_SingleSide(ANewValue: Boolean);
procedure SetState_Style(ANewValue: TAccordionStyle);
procedure SetState_TargetDelay(const AValue: Double);
procedure SetState_TargetLength(ANewValue: Integer);
procedure SetState_TargetLengthMode(ANewValue: TTargetLengthMode);
procedure SetState_Tolerance(const ANewValue: Integer);
procedure SetState_TunedObject(ANewValue: IPCB_Primitive);
procedure SetState_UseDelayUnits(const AValue: Boolean);
procedure SetState_UseTargetSource(AValue: Boolean);
procedure ToggleAmplitudeDirection;
procedure UpdatePinPairs(const APrimitive: IPCB_Primitive);
procedure UpdatePinPairsNet(const ANet: IPCB_Net);
procedure UpdatePrimitive(const APrimitive: IPCB_Primitive);
function UseBeforePlacing: Boolean;

## IPCB_AcuteAngle
继承：IPCB_AcuteAngle → IPCB_Rule → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 4 个方法、2 个属性

property CheckTracksOnly: Boolean read GetState_CheckTracksOnly write SetState_CheckTracksOnly;
property Minimum: TAngle read GetState_Minimum write SetState_Minimum;
function GetState_CheckTracksOnly: Boolean;
function GetState_Minimum: Double;
procedure SetState_CheckTracksOnly(Value: Boolean);
procedure SetState_Minimum(Value: Double);

## IPCB_AdvancedPlacerOptions
继承：IPCB_AdvancedPlacerOptions → IPCB_AbstractOptions → IInterface ｜ 单元：RT_PCB ｜ 自有 16 个方法、8 个属性

property PlaceByPassNet1: TPCBString read GetState_PlaceByPassNet1 write SetState_PlaceByPassNet1;
property PlaceByPassNet2: TPCBString read GetState_PlaceByPassNet2 write SetState_PlaceByPassNet2;
property PlaceLargeClear: TCoord read GetState_PlaceLargeClear write SetState_PlaceLargeClear;
property PlaceSmallClear: TCoord read GetState_PlaceSmallClear write SetState_PlaceSmallClear;
property PlaceUseAdvancedPlace: Boolean read GetState_PlaceUseAdvancedPlace write SetState_PlaceUseAdvancedPlace;
property PlaceUseGrouping: Boolean read GetState_PlaceUseGrouping write SetState_PlaceUseGrouping;
property PlaceUseLayerSwap: Boolean read GetState_PlaceUseLayerSwap write SetState_PlaceUseLayerSwap;
property PlaceUseRotation: Boolean read GetState_PlaceUseRotation write SetState_PlaceUseRotation;
function GetState_PlaceByPassNet1: WideString;
function GetState_PlaceByPassNet2: WideString;
function GetState_PlaceLargeClear: Integer;
function GetState_PlaceSmallClear: Integer;
function GetState_PlaceUseAdvancedPlace: Boolean;
function GetState_PlaceUseGrouping: Boolean;
function GetState_PlaceUseLayerSwap: Boolean;
function GetState_PlaceUseRotation: Boolean;
procedure SetState_PlaceByPassNet1(Value: WideString);
procedure SetState_PlaceByPassNet2(Value: WideString);
procedure SetState_PlaceLargeClear(Value: Integer);
procedure SetState_PlaceSmallClear(Value: Integer);
procedure SetState_PlaceUseAdvancedPlace(Value: Boolean);
procedure SetState_PlaceUseGrouping(Value: Boolean);
procedure SetState_PlaceUseLayerSwap(Value: Boolean);
procedure SetState_PlaceUseRotation(Value: Boolean);

## IPCB_AngularDimension
继承：IPCB_AngularDimension → IPCB_Dimension → IPCB_Group → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 13 个方法、2 个属性

property Radius: TCoord read GetState_Radius write SetState_Radius;
property Sector: Integer read GetState_Sector write SetState_Sector;
function Arc1: IPCB_Arc;
function Arc2: IPCB_Arc;
function Arrow1_Track1: IPCB_Track;
function Arrow1_Track2: IPCB_Track;
function Arrow2_Track1: IPCB_Track;
function Arrow2_Track2: IPCB_Track;
function Extension1_Track: IPCB_Track;
function Extension2_Track: IPCB_Track;
function GetState_Radius: Integer;
function GetState_Sector: Integer;
procedure SetState_Radius(Value: Integer);
procedure SetState_Sector(Value: Integer);
function Text: IPCB_Text;

## IPCB_Arc
继承：IPCB_Arc → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 18 个方法、10 个属性

property EndAngle: TAngle read GetState_EndAngle write SetState_EndAngle;
property EndX: TCoord read GetState_EndX;  // read-only
property EndY: TCoord read GetState_EndY;  // read-only
property LineWidth: TCoord read GetState_LineWidth write SetState_LineWidth;
property Radius: TCoord read GetState_Radius write SetState_Radius;
property StartAngle: TAngle read GetState_StartAngle write SetState_StartAngle;
property StartX: TCoord read GetState_StartX;  // read-only
property StartY: TCoord read GetState_StartY;  // read-only
property XCenter: TCoord read GetState_CenterX write SetState_CenterX;
property YCenter: TCoord read GetState_CenterY write SetState_CenterY;
function GetState_CenterX: Integer;
function GetState_CenterY: Integer;
function GetState_EndAngle: Double;
function GetState_EndX: Integer;
function GetState_EndY: Integer;
function GetState_LineWidth: Integer;
function GetState_Radius: Integer;
function GetState_StartAngle: Double;
function GetState_StartX: Integer;
function GetState_StartY: Integer;
function GetState_StrictHitTest(HitX: Integer; HitY: Integer): Boolean;
procedure RotateAroundXY(AX: Integer; AY: Integer; Angle: Double);
procedure SetState_CenterX(AX: Integer);
procedure SetState_CenterY(AY: Integer);
procedure SetState_EndAngle(Angle: Double);
procedure SetState_LineWidth(Width: Integer);
procedure SetState_Radius(Radius: Integer);
procedure SetState_StartAngle(Angle: Double);

## IPCB_AreaCalculation
继承：IPCB_AreaCalculation → IInterface ｜ 单元：RT_PCB ｜ 自有 2 个方法、1 个属性

property Area: Double read GetState_Area write SetState_Area;
function GetState_Area: Double;
procedure SetState_Area(Value: Double);

## IPCB_AreaCalculationBoard
继承：IPCB_AreaCalculationBoard → IPCB_AreaCalculation → IInterface ｜ 单元：RT_PCB ｜ 自有 5 个方法、2 个属性

property ComponentsArea: Double read GetState_ComponentsArea write SetState_ComponentsArea;
property Density: Double read GetState_Density;  // read-only
function GetState_ComponentsArea: Double;
function GetState_CopperBodyList: IPCB_CopperBodyList;
function GetState_Density: Double;
function GetState_LayerArea(CopperBodyList: IPCB_CopperBodyList; Layer: Integer): Double;
procedure SetState_ComponentsArea(Value: Double);

## IPCB_AreaCalculationManual
继承：IPCB_AreaCalculationManual → IPCB_AreaCalculation → IInterface ｜ 单元：RT_PCB ｜ 自有 2 个方法、1 个属性

property AreaManualMode: Boolean read GetState_AreaManualMode write SetState_AreaManualMode;
function GetState_AreaManualMode: Boolean;
procedure SetState_AreaManualMode(Value: Boolean);

## IPCB_AuthorInfo
继承：IPCB_AuthorInfo → IInterface ｜ 单元：RT_PCB ｜ 自有 3 个方法、3 个属性

property Id: TPCBString read GetID;  // read-only
property Source: TPCBString read GetSource;  // read-only
property Title: TPCBString read GetTitle;  // read-only
function GetID: WideString;
function GetSource: WideString;
function GetTitle: WideString;

## IPCB_AutoTestSupport
继承：IPCB_AutoTestSupport → IInterface ｜ 单元：RT_PCB ｜ 自有 1 个方法、0 个属性

function InTestMode: Boolean;

## IPCB_Axis
继承：IPCB_Axis → IInterface ｜ 单元：RT_PCB ｜ 自有 10 个方法、5 个属性

property DirectionX: Single read GetState_DirectionX write SetState_DirectionX;
property DirectionY: Single read GetState_DirectionY write SetState_DirectionY;
property DirectionZ: Single read GetState_DirectionZ write SetState_DirectionZ;
property Name: TPCBString read GetState_Name write SetState_Name;
property Origin: TCoordPoint3D read GetState_Origin write SetState_Origin;
function GetState_DirectionX: Single;
function GetState_DirectionY: Single;
function GetState_DirectionZ: Single;
function GetState_Name: WideString;
function GetState_Origin: IDispatch;
procedure SetState_DirectionX(AValue: Single);
procedure SetState_DirectionY(AValue: Single);
procedure SetState_DirectionZ(AValue: Single);
procedure SetState_Name(AValue: WideString);
procedure SetState_Origin(const AValue: IDispatch);

## IPCB_BackDrilling
继承：IPCB_BackDrilling → IInterface ｜ 单元：RT_PCB ｜ 自有 8 个方法、7 个属性

property BottomBackDrillStopLayer: TV7_Layer read GetState_BottomBackDrillStopLayer;  // read-only
property BottomUnusedStub: TCoord read GetState_BottomUnusedStub;  // read-only
property HoleOversize: TCoord read GetState_HoleOversize;  // read-only
property IsBackdrill: Boolean read GetState_IsBackdrill;  // read-only
property SourceObject: IPCB_Primitive read GetState_SourceObject;  // read-only
property TopBackDrillStopLayer: TV7_Layer read GetState_TopBackDrillStopLayer;  // read-only
property TopUnusedStub: TCoord read GetState_TopUnusedStub;  // read-only
function GetState_BottomBackDrillStopLayer: IDispatch;
function GetState_BottomUnusedStub: Integer;
function GetState_HoleOversize: Integer;
function GetState_IsBackdrill: Boolean;
function GetState_IsBackDrillLayer(Layer: TV6_Layer): Boolean;
function GetState_SourceObject: IPCB_Primitive;
function GetState_TopBackDrillStopLayer: IDispatch;
function GetState_TopUnusedStub: Integer;

## IPCB_BackDrillingRule
继承：IPCB_BackDrillingRule → IPCB_Rule → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 12 个方法、0 个属性

function GetState_BackDrillOverSize: Integer;
function GetState_BackDrillOverSizeNegativeTolerance: Integer;
function GetState_BackDrillOverSizePositiveTolerance: Integer;
function GetState_MaxStubLength: Integer;
function GetState_UseBottomLayer: Boolean;
function GetState_UseTopLayer: Boolean;
procedure SetState_BackDrillOverSize(Value: Integer);
procedure SetState_BackDrillOverSizeNegativeTolerance(Value: Integer);
procedure SetState_BackDrillOverSizePositiveTolerance(Value: Integer);
procedure SetState_MaxStubLength(Value: Integer);
procedure SetState_UseBottomLayer(Value: Boolean);
procedure SetState_UseTopLayer(Value: Boolean);

## IPCB_BaselineDimension
继承：IPCB_BaselineDimension → IPCB_Dimension → IPCB_Group → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 20 个方法、3 个属性

property Angle: TAngle read GetState_Angle write SetState_Angle;
property TextLocations[I: Integer]: TCoordPoint read GetState_TextLocations write SetState_TextLocations;
property TextLocationsCount: Integer read GetState_TextLocationsCount write SetState_TextLocationsCount;
function Arrow1_Track1(I: Integer): IPCB_Track;
function Arrow1_Track2(I: Integer): IPCB_Track;
function Arrow2_Track1(I: Integer): IPCB_Track;
function Arrow2_Track2(I: Integer): IPCB_Track;
function Extension1_Track(I: Integer): IPCB_Track;
function Extension2_Track(I: Integer): IPCB_Track;
function GetState_Angle: Double;
function GetState_TextLocations(I: Integer): IDispatch;
function GetState_TextLocationsCount: Integer;
function Line_Track1(I: Integer): IPCB_Track;
function Line_Track2(I: Integer): IPCB_Track;
procedure SetState_Angle(Value: Double);
procedure SetState_TextLocations(I: Integer; const Value: IDispatch);
procedure SetState_TextLocationsCount(Value: Integer);
function Text: IPCB_Text;
procedure TextLocations_Add(const Point: IDispatch);
procedure TextLocations_Clear;
procedure TextLocations_Delete(Index: Integer);
procedure TextLocations_DeleteLast;
function Texts(I: Integer): IPCB_Text;

## IPCB_BendingLine
继承：IPCB_BendingLine → IInterface ｜ 单元：RT_PCB ｜ 自有 27 个方法、10 个属性

property Angle: TAngle read GetState_Angle write SetState_Angle;
property BoardRegion: IPCB_BoardRegion read GetState_BoardRegion;  // read-only
property FoldIndex: Integer read GetState_FoldIndex write SetState_FoldIndex;
property FromPoint: TCoordPoint read GetState_FromPoint;  // read-only
property Locked: Boolean read GetState_Locked write SetState_Locked;
property Name: WideString read GetProperty_Name write SetProperty_Name;
property Radius: TCoord read GetState_Radius write SetState_Radius;
property Rotation: TAngle read GetProperty_Rotation write SetProperty_Rotation;
property Selected: Boolean read GetProperty_Selected write SetProperty_Selected;
property ToPoint: TCoordPoint read GetState_ToPoint;  // read-only
procedure AddRegion(const ARegionName: WideString);
function GetProperty_FromPoint: IDispatch;
function GetProperty_Name: WideString;
function GetProperty_Rotation: Double;
function GetProperty_Selected: Boolean;
function GetProperty_ToPoint: IDispatch;
function GetState_Angle: Double;
function GetState_BoardRegion: IPCB_BoardRegion;
function GetState_FoldIndex: Integer;
function GetState_FromPoint: IDispatch;
function GetState_Locked: Boolean;
function GetState_Radius: Integer;
function GetState_ToPoint: IDispatch;
function I_ObjectAddress: Pointer;
function IsAffectRegion(const ARegionName: WideString): Boolean;
procedure MoveByXY(dX: Integer; dY: Integer);
procedure RemoveRegion(const ARegionName: WideString);
procedure SetProperty_FromPoint(const AValue: IDispatch);
procedure SetProperty_Name(const AValue: WideString);
procedure SetProperty_Rotation(const AValue: Double);
procedure SetProperty_Selected(const AValue: Boolean);
procedure SetProperty_ToPoint(const AValue: IDispatch);
procedure SetState_Angle(Value: Double);
procedure SetState_FoldIndex(Value: Integer);
procedure SetState_FromToPoints(const AFromPoint: IDispatch; const AToPoint: IDispatch);
procedure SetState_Locked(AValue: Boolean);
procedure SetState_Radius(Value: Integer);

## IPCB_Board
继承：IPCB_Board → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 220 个方法、68 个属性

property AutomaticSplitPlanes: Boolean read GetState_AutomaticSplitPlanes write SetState_AutomaticSplitPlanes;
property BigVisibleGridMultFactor: TReal read GetState_BigVisibleGridMultFactor write SetState_BigVisibleGridMultFactor;
property BigVisibleGridSize: TReal read GetState_BigVisibleGridSize write SetState_BigVisibleGridSize;
property BigVisibleGridUnit: TUnit read GetState_BigVisibleGridUnit write SetState_BigVisibleGridUnit;
property BoardID: Integer read GetState_BoardID;  // read-only
property BoardLayerSetManager: IPCB_BoardLayerSetManager read GetState_BoardLayerSetManager;  // read-only
property BoardOutline: IPCB_BoardOutline read GetState_BoardOutline;  // read-only
property BoardVersion: Double read GetState_BoardVersion;  // read-only
property ChangeProcessor_SystemValid[AProcessorName: string]: Boolean read GetState_SystemValid write SetState_SystemValid;
property ComponentGridSize: TDouble read GetState_ComponentGridSize write SetState_ComponentGridSize;
property ComponentGridSizeX: TDouble read GetState_ComponentGridSizeX write SetState_ComponentGridSizeX;
property ComponentGridSizeY: TDouble read GetState_ComponentGridSizeY write SetState_ComponentGridSizeY;
property CurrentLayer: TLayer read GetState_CurrentLayerV7 write SetState_CurrentLayerV7;
property CurrentLayerV6: TV6_Layer read GetState_CurrentLayer;  // read-only
property DisplayUnit: TUnit read GetState_DisplayUnit write SetState_DisplayUnit;
property DrawDotGrid: Boolean read GetState_DrawDotGrid write SetState_DrawDotGrid;
property DrawMode[OId: TObjectId]: TDrawMode read GetState_DrawMode write SetState_DrawMode;
property DrillLayerPairsCount: Integer read GetState_DrillLayerPairsCount;  // read-only
property ECOOptions: IPCB_ECOOptions read GetState_ECOOptions;  // read-only
property FileName: TPCBString read GetState_FileName;  // read-only
property GerberOptions: IPCB_GerberOptions read GetState_GerberOptions;  // read-only
property InternalPlane1NetName: TPCBString read GetState_InternalPlane1NetName write SetState_InternalPlane1NetName;
property InternalPlane2NetName: TPCBString read GetState_InternalPlane2NetName write SetState_InternalPlane2NetName;
property InternalPlane3NetName: TPCBString read GetState_InternalPlane3NetName write SetState_InternalPlane3NetName;
property InternalPlane4NetName: TPCBString read GetState_InternalPlane4NetName write SetState_InternalPlane4NetName;
property InternalPlaneNetName[L: Integer]: TPCBString read GetState_InternalPlaneNetName write SetState_InternalPlaneNetName;
property LayerColor[L: TV6_Layer]: TColorRef read GetState_LayerColor;  // read-only
property LayerIsDisplayed[L: Integer]: Boolean read GetState_LayerIsDisplayed write SetState_LayerIsDisplayed;
property LayerIsUsed[L: Integer]: Boolean read GetState_LayerIsUsed write SetState_LayerIsUsed;
property LayerPair[I: Integer]: IPCB_DrillLayerPair read GetState_LayerPair;  // read-only
property LayerStack: IPCB_LayerStack read GetState_LayerStack;  // read-only
property LayerStack_V7: IPCB_LayerStack_V7 read GetState_LayerStack_V7;  // read-only
property MasterLayerStack: IPCB_MasterLayerStack read GetState_MasterStack;  // read-only
property MechanicalPairs: IPCB_MechanicalLayerPairs read GetState_MechanicalPairs;  // read-only
property OutputOptions: IPCB_OutputOptions read GetState_OutputOptions;  // read-only
property PadViaCache: IPCB_PadViaLibrary read GetState_PadViaCache;  // read-only
property PadViaLibrary: IPCB_PadViaLibrary read GetState_PadViaLibrary;  // read-only
property PCB3DMovieManager: IPCB_3DMovieManager read GetState_PCB3DMovieManager;  // read-only
property PCBSheet: IPCB_Sheet read GetState_PCBSheet;  // read-only
property PCBWindow: HWND read GetState_Window;  // read-only
property PinPairsManager: IPCB_PinPairsManager read GetState_PinPairsManager;  // read-only
property PlacerOptions: IPCB_AdvancedPlacerOptions read GetState_PlacerOptions;  // read-only
property PolygonNameTemplate: TPolygonNameTemplates read GetState_PolygonNameTemplate write SetState_PolygonNameTemplate;
property PrimitiveCounter: IPCB_PrimitiveCounter read GetPrimitiveCounter;  // read-only
property PrinterOptions: IPCB_PrinterOptions read GetState_PrinterOptions;  // read-only
property RouteToolPathLayer: TLayer read GetState_RouteToolPathLayer write SetState_RouteToolPathLayer;
property RoutingOptions: IPCB_BoardRoutingOptions read GetState_RoutingOptions;  // read-only
property SelectecObject[I: Integer]: IPCB_Primitive read GetState_SelectecObject;  // read-only
property SelectecObjectCount: Integer read GetState_SelectecObjectCount;  // read-only
property SnapGridSize: TDouble read GetState_SnapGridSize write SetState_SnapGridSize;
property SnapGridSizeX: TDouble read GetState_SnapGridSizeX write SetState_SnapGridSizeX;
property SnapGridSizeY: TDouble read GetState_SnapGridSizeY write SetState_SnapGridSizeY;
property SnapGridUnit: TUnit read GetState_SnapGridUnit write SetState_SnapGridUnit;
property TrackGridSize: TDouble read GetState_TrackGridSize write SetState_TrackGridSize;
property ViaGridSize: TDouble read GetState_ViaGridSize write SetState_ViaGridSize;
property ViewConfigDisplaySpecialStrings: Boolean read GetState_ViewConfigDisplaySpecialStrings write SetState_ViewConfigDisplaySpecialStrings;
property ViewConfigIs3D: Boolean read GetState_ViewConfigIs3D;  // read-only
property ViewConfigTopSolderMaskColor3D: TColor read GetState_ViewConfigTopSolderMaskColor3D;  // read-only
property Viewport: IPCB_Viewport read GetState_Viewport write SetState_Viewport;
property VisibleGridMultFactor: TReal read GetState_VisibleGridMultFactor write SetState_VisibleGridMultFactor;
property VisibleGridSize: TReal read GetState_VisibleGridSize write SetState_VisibleGridSize;
property VisibleGridUnit: TUnit read GetState_VisibleGridUnit write SetState_VisibleGridUnit;
property WorldXOrigin: TCoord read GetState_WorldXOrigin write SetState_WorldXOrigin;
property WorldYOrigin: TCoord read GetState_WorldYOrigin write SetState_WorldYOrigin;
property XCursor: TCoord read GetState_XCursor write SetState_XCursor;
property XOrigin: TCoord read GetState_XOrigin write SetState_XOrigin;
property YCursor: TCoord read GetState_YCursor write SetState_YCursor;
property YOrigin: TCoord read GetState_YOrigin write SetState_YOrigin;
procedure AddLayerPair(LowLayer: Integer; HighLayer: Integer);
function AddMesh(MeshString: WideString): Integer;
procedure AddObjectToHighlightObjectList(iPrimitive: IPCB_Primitive);
procedure AddPCBObject(PCBObject: IPCB_Primitive);
function AddPolygonMesh(Shape: IPCB_Contour; z: Integer; Color: Cardinal): Integer;
procedure AnalyzeNet(const ANet: IPCB_Net);
procedure BeginIgnoreChanges;
function BoardIterator_Create: IPCB_BoardIterator;
procedure BoardIterator_Destroy(var AIterator: IPCB_BoardIterator);
function ChooseLocation(var x1: Integer; var y1: Integer; Prompt: WideString): Boolean;
function ChooseRectangleByCorners(Prompt1: WideString; Prompt2: WideString; var x1: Integer; var y1: Integer; var x2: Integer; var y2: Integer): Boolean;
function ClassNameIsUnique(AObjectClass: IPCB_ObjectClass; AName: WideString): Boolean;
procedure CleanNet(const ANet: IPCB_Net);
procedure ClearMeshes;
procedure ClearUndoRedo;
procedure ConnectivelyValidateNets;
function ContextMenuObjectCount(ObjectId: TObjectId): Integer;
function CreateBoardOutline: IPCB_BoardOutline;
function DeleteMesh(Id: Integer): Boolean;
function DifferentialPairNameIsUnique(ADifferentialPair: IPCB_DifferentialPair; AName: WideString): Boolean;
procedure DispatchMessage(Source: IPCB_Primitive; Destination: IPCB_Primitive; MessageID: Word; MessageData: IPCB_Primitive);
procedure DoRedo;
procedure DoUndo;
function ElectricalLayerIterator: IPCB_LayerObjectIterator;
function ElectricalLayers: IPCB_LayerSet;
procedure EnableAllPrimitives(Enable: Boolean);
procedure EndIgnoreChanges;
procedure EndUndo;
function FindDominantRuleForObject(APrimitive: IPCB_Primitive; ARuleKind: TRuleKind): IPCB_Rule;
function FindDominantRuleForObjectPair(APrimitive1: IPCB_Primitive; APrimitive2: IPCB_Primitive; ARuleKind: TRuleKind): IPCB_Rule;
function FindLinkedBoardLibrary(APrimitive: IPCB_Primitive): IPCB_PadViaLibrary;
function FindLinkedBoardTemplate(APrimitive: IPCB_Primitive): IPCB_PadViaTemplate;
function GenerateUniqueID: WideString;
procedure GetFlexTransform(x: Integer; y: Integer; P: Pointer);
function GetLastClickedObject(ObjectSet: TObjectSet; Action: TEditingAction): IPCB_Primitive;
function GetMeshPatchFromPoint(x: Integer; y: Integer; var MeshID: Integer; var PatchIndex0: Integer; var PatchIndex1: Integer; var PatchIndex2: Integer; var IntersectionX: Integer; var IntersectionY: Integer; var IntersectionZ: Integer): Boolean;
function GetObjectAtCursor(ObjectSet: TObjectSet; LayerSet: TV6_LayerSet; StatusBarText: WideString): IPCB_Primitive;
function GetObjectAtXYAskUserIfAmbiguous(HitX: Integer; HitY: Integer; ObjectSet: TObjectSet; LayerSet: TV6_LayerSet; Action: TEditingAction): IPCB_Primitive;
function GetPadViaTemplateForPrimitive(const APrimitive: IPCB_Primitive): IPCB_PadViaTemplate;
function GetPcbComponentByRefDes(Value: WideString): IPCB_Component;
function GetPrimitiveCount(AObjSet: TObjectSet; LayerSet: TV6_LayerSet; AMethod: TIterationMethod): Integer;
function GetPrimitiveCounter: IPCB_PrimitiveCounter;
function GetState_AutomaticSplitPlanes: Boolean;
function GetState_BigVisibleGridMultFactor: Double;
function GetState_BigVisibleGridSize: Double;
function GetState_BigVisibleGridUnit: TUnit;
function GetState_BoardID: Integer;
function GetState_BoardLayerSetManager: IPCB_BoardLayerSetManager;
function GetState_BoardOutline: IPCB_BoardOutline;
function GetState_BoardVersion: Double;
function GetState_ComponentGridSize: Double;
function GetState_ComponentGridSizeX: Double;
function GetState_ComponentGridSizeY: Double;
function GetState_CurrentLayer: TV6_Layer;
function GetState_CurrentLayerV7: Integer;
function GetState_DesignatorDisplayMode: TDesignatorDisplayMode;
function GetState_DisplayUnit: TUnit;
function GetState_DrawDotGrid: Boolean;
function GetState_DrawMode(OId: TObjectId): TDrawMode;
function GetState_DrillLayerPairsCount: Integer;
function GetState_ECOOptions: IPCB_ECOOptions;
function GetState_FileName: WideString;
function GetState_GerberOptions: IPCB_GerberOptions;
function GetState_InternalPlane1NetName: WideString;
function GetState_InternalPlane2NetName: WideString;
function GetState_InternalPlane3NetName: WideString;
function GetState_InternalPlane4NetName: WideString;
function GetState_InternalPlaneNetName(L: Integer): WideString;
function GetState_LayerColor(L: TV6_Layer): Cardinal;
function GetState_LayerIsDisplayed(L: Integer): Boolean;
function GetState_LayerIsUsed(L: Integer): Boolean;
function GetState_LayerPair(I: Integer): IPCB_DrillLayerPair;
function GetState_LayerPairByPair(LowLay: TV6_Layer; HighLay: TV6_Layer): IPCB_DrillLayerPair;
function GetState_LayerStack: IPCB_LayerStack;
function GetState_LayerStack_V7: IPCB_LayerStack_V7;
function GetState_MainGraphicalView: IPCB_GraphicalView;
function GetState_MasterStack: IPCB_MasterLayerStack;
function GetState_MechanicalPairs: IPCB_MechanicalLayerPairs;
function GetState_MeshViewMode(Id: Integer): TPCBMeshViewMode;
function GetState_OutputOptions: IPCB_OutputOptions;
function GetState_PadViaCache: IPCB_PadViaLibrary;
function GetState_PadViaLibrary: IPCB_PadViaLibrary;
function GetState_PCB3DMovieManager: IPCB_3DMovieManager;
function GetState_PCBSheet: IPCB_Sheet;
function GetState_PinPairsManager: IPCB_PinPairsManager;
function GetState_PlacerOptions: IPCB_AdvancedPlacerOptions;
function GetState_PolygonNameTemplate: TPolygonNameTemplates;
function GetState_PrinterOptions: IPCB_PrinterOptions;
function GetState_RouteToolPathLayer: Integer;
function GetState_RoutingOptions: IPCB_BoardRoutingOptions;
function GetState_SelectecObject(I: Integer): IPCB_Primitive;
function GetState_SelectecObjectCount: Integer;
function GetState_SnapGridSize: Double;
function GetState_SnapGridSizeX: Double;
function GetState_SnapGridSizeY: Double;
function GetState_SnapGridUnit: TUnit;
procedure GetState_SplitPlaneNets(NetsList: TStringList);
function GetState_SwitchOutputCapabilityMode: Boolean;
function GetState_SystemValid(AProcessorName: string): Boolean;
function GetState_TrackGridSize: Double;
function GetState_ViaGridSize: Double;
function GetState_ViewConfigAsString(out ConfigType: WideString; out Config: WideString): Boolean;
function GetState_ViewConfigColor2D(Layer: Integer): Cardinal;
function GetState_ViewConfigColor3D(Layer: Integer): Cardinal;
function GetState_ViewConfigDisplaySpecialStrings: Boolean;
function GetState_ViewConfigIs3D: Boolean;
function GetState_ViewConfigOpacity2D(Layer: Integer; ObjectId: TObjectId): Single;
function GetState_ViewConfigOpacity3D(Layer: Integer): Single;
function GetState_ViewConfigTopSolderMaskColor3D: Cardinal;
function GetState_Viewport: IPCB_Viewport;
function GetState_VisibleGridMultFactor: Double;
function GetState_VisibleGridSize: Double;
function GetState_VisibleGridUnit: TUnit;
function GetState_Window: HWND;
function GetState_WorldXOrigin: Integer;
function GetState_WorldYOrigin: Integer;
function GetState_XCursor: Integer;
function GetState_XOrigin: Integer;
function GetState_YCursor: Integer;
function GetState_YOrigin: Integer;
procedure GetState_ZTopBottom(out ZTop: Single; out ZBottom: Single);
function GraphicalView_ViewportRect: IDispatch;
procedure GraphicalView_ZoomOnRect(x1: Integer; y1: Integer; x2: Integer; y2: Integer);
procedure GraphicalView_ZoomRedraw;
function HasServerDocument: Boolean;
procedure HideHoleSymbols;
procedure HidePCBObject(const PCBObject: IPCB_Primitive);
function InternalPlaneLayerIterator: IPCB_LayerObjectIterator;
procedure InvalidatePlane(L: TV6_Layer);
procedure InvalidateScopeTester;
procedure InvertPCBObject(const PCBObject: IPCB_Primitive);
function IsEmptyHoleToleranceValue(Value: Integer): Boolean;
function LayerIterator: IPCB_LayerObjectIterator;
function LayerIterator_IncludeNonEditable: IPCB_LayerObjectIterator;
function LayerName(L: Integer): WideString;
function LayerPositionInSet(ALayerSet: TV6_LayerSet; ALayerObj: IPCB_LayerObject): Integer;
procedure LinkToTemplate(const APrimitive: IPCB_Primitive; const ATemplate: IPCB_PadViaTemplate);
function LoadMeshFile(MeshFile: WideString): Integer;
function MechanicalLayerIterator: IPCB_LayerObjectIterator;
function MechanicalLayers: IPCB_LayerSet;
procedure Navigate_RedrawChangedObjectsInBoard;
function NetNameIsUnique(ANet: IPCB_Net; AName: WideString): Boolean;
procedure NewUndo;
function PrimPrimDistance(APrimitive1: IPCB_Primitive; APrimitive2: IPCB_Primitive): Integer;
procedure RebuildBoardOutline(ADefiningLayer: Integer);
procedure RebuildPadCaches;
procedure RebuildSplitBoardRegions(FullRebuild: Boolean);
procedure RecreateHandles;
procedure ReDrawToDC(DC: NativeUInt; PrintKind: Integer; PrintWhat: Integer; const Layers: TV6_LayerSet);
procedure RemovePCBObject(PCBObject: IPCB_Primitive);
function RuleNameUnique(ARule: IPCB_Rule; AName: WideString): Boolean;
function RunBatchDesignRuleCheck(ReportFilename: WideString; DRCReportFormat: TDRCReportFileFormat; DisplayReportFile: LongBool; PublishToWeb: LongBool): LongBool;
procedure SelectedObjects_Add(P: IPCB_Primitive);
procedure SelectedObjects_BeginUpdate;
procedure SelectedObjects_Clear;
procedure SelectedObjects_EndUpdate;
function SelectedObjectsCount: Integer;
function SelectNewViewConfiguration(const CurConfigType: WideString; const CurConfig: WideString; out ConfigType: WideString; out Config: WideString): Boolean;
procedure SetState_AutomaticSplitPlanes(Value: Boolean);
procedure SetState_BigVisibleGridMultFactor(MultFact: Double);
procedure SetState_BigVisibleGridSize(Value: Double);
procedure SetState_BigVisibleGridUnit(Value: TUnit);
procedure SetState_ComponentGridSize(Value: Double);
procedure SetState_ComponentGridSizeX(Value: Double);
procedure SetState_ComponentGridSizeY(Value: Double);
procedure SetState_CurrentLayerV7(Value: Integer);
procedure SetState_DesignatorDisplayMode(AMode: TDesignatorDisplayMode);
procedure SetState_DisplayUnit(Value: TUnit);
procedure SetState_DocumentHasChanged;
procedure SetState_DrawDotGrid(Value: Boolean);
procedure SetState_DrawMode(OId: TObjectId; Value: TDrawMode);
procedure SetState_InternalPlane1NetName(NetName: WideString);
procedure SetState_InternalPlane2NetName(NetName: WideString);
procedure SetState_InternalPlane3NetName(NetName: WideString);
procedure SetState_InternalPlane4NetName(NetName: WideString);
procedure SetState_InternalPlaneNetName(L: Integer; NetName: WideString);
procedure SetState_LayerIsDisplayed(L: Integer; b: Boolean);
procedure SetState_LayerIsUsed(L: Integer; b: Boolean);
procedure SetState_MeshViewMode(Id: Integer; ViewMode: TPCBMeshViewMode);
procedure SetState_Navigate_HighlightObjectList(HighlightMethods: THighlightMethodSet; ClearExisting: Boolean);
procedure SetState_PolygonNameTemplate(ATemplate: TPolygonNameTemplates);
procedure SetState_RouteToolPathLayer(ALayer: Integer);
procedure SetState_SaveCurrentStatusOfObjectsInBoard;
procedure SetState_SnapGridSize(Value: Double);
procedure SetState_SnapGridSizeX(Value: Double);
procedure SetState_SnapGridSizeY(Value: Double);
procedure SetState_SnapGridUnit(Value: TUnit);
procedure SetState_SwitchOutputCapabilityMode(AOutputCapability: Boolean);
procedure SetState_SystemValid(AProcessorName: string; const AValid: Boolean);
procedure SetState_TrackGridSize(Value: Double);
procedure SetState_ViaGridSize(Value: Double);
procedure SetState_ViewConfigDisplaySpecialStrings(AValue: Boolean);
function SetState_ViewConfigFromString(const ConfigType: WideString; const Config: WideString): Boolean;
function SetState_ViewConfigFromString_ForceRebuild(const ConfigType: WideString; const Config: WideString): Boolean;
procedure SetState_ViewManager_FilterChanging;
procedure SetState_Viewport(Value: IPCB_Viewport);
procedure SetState_VisibleGridMultFactor(MultFact: Double);
procedure SetState_VisibleGridSize(Value: Double);
procedure SetState_VisibleGridUnit(Value: TUnit);
procedure SetState_WorldXOrigin(Value: Integer);
procedure SetState_WorldYOrigin(Value: Integer);
procedure SetState_XCursor(Value: Integer);
procedure SetState_XOrigin(Value: Integer);
procedure SetState_YCursor(Value: Integer);
procedure SetState_YOrigin(Value: Integer);
procedure ShowHoleSymbols(SymbolType: Integer; SymbolSize: Integer; LayerPairIndex: Integer);
procedure ShowPCBObject(const PCBObject: IPCB_Primitive);
function SignalLayerIterator: IPCB_LayerObjectIterator;
function SpatialIterator_Create: IPCB_SpatialIterator;
procedure SpatialIterator_Destroy(var AIterator: IPCB_SpatialIterator);
procedure UnlinkFromTemplate(const APrimitive: IPCB_Primitive);
procedure UpdateBoardOutline;
procedure UpdateCachedVCSRevisionNumberSpecialStrings;
procedure ValidateInvalidPlanes;
procedure ValidateScopeTester;
procedure ViewManager_FullUpdate;
procedure ViewManager_GraphicallyInvalidatePrimitive(PCBObject: IPCB_Primitive);
procedure ViewManager_UpdateLayerTabs;
function VisibleLayers: IPCB_LayerSet;
function WindowBoundingRectangle: IDispatch;

## IPCB_Board3D
继承：IPCB_Board3D → IPCB_Board → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 3 个方法、0 个属性

function GetState_SketchesGridManager: IPCB_SketchesGridManager;
function Is3DRouted: Boolean;
function RouteBodyPlacementBox: IDispatch;

## IPCB_Board3DModelExporter
继承：IPCB_Board3DModelExporter → IInterface ｜ 单元：RT_PCB ｜ 自有 34 个方法、0 个属性

procedure ExportBoard3DModel(const FileName: string; Format: TBoard3DModelExportFormat; Board: IPCB_Board; Project: IProject);
procedure ExportBoard3DModelToOCCDoc(OccDoc: IOCCDocument; Board: IPCB_Board; Project: IProject);
function GetCopperBodyList(Board: IPCB_Board; Options: Integer; MaxVertexPerBody: Integer): IPCB_CopperBodyList;
function GetCopperBodyList2(Board: IPCB_Board; Options: Integer): IPCB_CopperBodyList;
function GetState_CanSelectPrimitives: Boolean;
function GetState_ComponentSuffix: string;
function GetState_ComponentSuffixType: TBoard3DModelExportComponentSuffix;
function GetState_ExportComponentOptions: TBoard3DModelExportComponentOptions;
function GetState_ExportCopperLayer: Integer;
function GetState_ExportCopperOption: TBoard3DModelExportCopperOptions;
function GetState_ExportFoldedBoard: Boolean;
function GetState_ExportFoldedBoardRate: Integer;
function GetState_ExportHolesOption: TBoard3DModelExportHolesOptions;
function GetState_ExportModelsOption: TBoard3DModelExportModelsOptions;
function GetState_ExportPadAndViaBarrelsOnly: Boolean;
function GetState_IncludeCoverLayer: Boolean;
function GetState_IncludeElectricalPadHoles: Boolean;
function GetState_IncludeFreePadHoles: Boolean;
function GetState_IncludeMechanicalPadHoles: Boolean;
procedure SetState_CanSelectPrimitives(Value: Boolean);
procedure SetState_ComponentSuffix(Value: string);
procedure SetState_ComponentSuffixType(Value: TBoard3DModelExportComponentSuffix);
procedure SetState_ExportComponentOptions(Value: TBoard3DModelExportComponentOptions);
procedure SetState_ExportCopperLayer(Value: Integer);
procedure SetState_ExportCopperOption(Value: TBoard3DModelExportCopperOptions);
procedure SetState_ExportFoldedBoard(Value: Boolean);
procedure SetState_ExportFoldedBoardRate(Value: Integer);
procedure SetState_ExportHolesOption(Value: TBoard3DModelExportHolesOptions);
procedure SetState_ExportModelsOption(Value: TBoard3DModelExportModelsOptions);
procedure SetState_ExportPadAndViaBarrelsOnly(Value: Boolean);
procedure SetState_IncludeCoverLayer(Value: Boolean);
procedure SetState_IncludeElectricalPadHoles(Value: Boolean);
procedure SetState_IncludeFreePadHoles(Value: Boolean);
procedure SetState_IncludeMechanicalPadHoles(Value: Boolean);

## IPCB_BoardCollection
继承：IPCB_BoardCollection → IInterface ｜ 单元：RT_PCB ｜ 自有 5 个方法、2 个属性

property Boards[AIndex: Integer]: IPCB_Board read GetBoard;  // read-only
property Count: Integer read GetCount;  // read-only
procedure AddBoard(Board: IPCB_Board);
procedure Clear;
function GetBoard(AIndex: Integer): IPCB_Board;
function GetCount: Integer;
procedure RemoveBoard(Board: IPCB_Board);

## IPCB_BoardEx
继承：IPCB_BoardEx → IInterface ｜ 单元：RT_PCB ｜ 自有 61 个方法、7 个属性

property DesignVariants: IPCB_DesignVariants read GetState_DesignVariants;  // read-only
property FullComponents: IPCB_FullComponents read GetState_FullComponents;  // read-only
property IsLocked: Boolean read GetState_IsLocked write SetState_IsLocked;
property SelectedObjects_FilterDisabled: Boolean read SelectedObjects_GetFilterDisabled write SelectedObjects_SetFilterDisabled;
property ViaManager: IPCB_ViaManager read GetState_ViaManager;  // read-only
property ViaStructureManager: IPCB_ViaStructureManager read GetState_ViaStructureManager;  // read-only
property ZoomOnViolations: Boolean read GetState_ZoomOnViolations write SetState_ZoomOnViolations;
function AddLayerPairEx2(ALowLayer: Integer; AHighLayer: Integer; ADrillLayerPairType: TDrillLayerPairType; const ACounterHoleParams: IPCB_CounterHoleParams): Integer;
function AddMeshToLayer(MeshString: WideString; Layer: Integer): Integer;
function AddPolygonMeshToLayer(Shape: IPCB_Contour; z: Integer; Color: Cardinal; Layer: Integer): Integer;
function BeginReadOnlyMode: Boolean;
function Drillmanager_GetDrillSymbolIndex(APrimitive: IPCB_Primitive): Integer;
function Drillmanager_GetUseFields: TClassificationFieldSet;
function EndReadOnlyMode: Boolean;
procedure ExportToFile(const AFilename: WideString; const AFormat: WideString);
function GetDialogsManager: IPCB_DialogsManager;
function GetExpressionManager: IPCB_ExpressionManager;
function GetSignalDelayForPrim(APrimitive: IPCB_Primitive): Double;
function GetSignalDelayPerMeter(APrimitive: IPCB_Primitive): Double;
function GetState_AutoTraceTuningOptions: IPCB_AccordionMakerSettings;
function GetState_BoardRegionManager: IPCB_BoardRegionsManager;
function GetState_ConstraintManagerData: WideString;
function GetState_CounterHoleParamsPresetList: IPCB_CounterHoleParamsPresetList;
function GetState_DesignVariants: IPCB_DesignVariants;
function GetState_FullComponents: IPCB_FullComponents;
function GetState_GridManager: IPCB_GridManager;
function GetState_IsLocked: Boolean;
function GetState_StateId: Cardinal;
function GetState_TeardropOptions: ITeardropOptions;
function GetState_UseConstraintManager: Boolean;
function GetState_ViaManager: IPCB_ViaManager;
function GetState_ViaStructureManager: IPCB_ViaStructureManager;
function GetState_ZoomOnViolations: Boolean;
function GetViewConfigurationByTypeAsString(AType: WideString; out Config: WideString): Boolean;
function GetVoidsOnPlaneLayer(ALayer: Integer): IPCB_Polygon;
procedure InvalidatePadCaches;
function IsPlaneLayerIsPoured(ALayer: Integer): Boolean;
function IsReadOnly: Boolean;
procedure LoadFromASCIIFile(AFilename: WideString);
procedure LoadFromCMPCBFile(AFilename: WideString);
procedure LoadFromCSPCBFile(AFilename: WideString);
procedure LoadFromJSONFile(AFilename: WideString);
procedure LoadFromPCBFile(AFilename: WideString);
procedure LoadFromPCBLibraryFile(AFilename: WideString; ArrangeComponents: Boolean);
function LoadRulesFromFile(AFilename: WideString): TRuleSet;
function PlaceAssemblyDesignators(UpdateExisting: Boolean): Integer;
procedure PlaceViaStructureFeaturesGeometry;
procedure RemoveAllLayerPairs;
procedure RemoveNonExistedCoverlayOutlines;
procedure RemoveViaStructureFeaturesGeometry;
function RenderToPNG(const OutputFileName: WideString; DPI: Integer; top: Boolean; const ConfigType: WideString; const Config: WideString): HRESULT;
procedure ResetDelaysCalculator;
function SaveRulesToFile(AFilename: WideString): Boolean;
procedure SaveToASCIIFile(AFilename: WideString);
procedure SaveToCMPCBFile(AFilename: WideString);
procedure SaveToCSPCBFile(AFilename: WideString);
procedure SaveToJSONFile(AFilename: WideString);
procedure SaveToPCBFile(AFilename: WideString);
procedure SaveToPCBLibraryFile(AFilename: WideString);
function SelectedObjects_GetFilterDisabled: Boolean;
procedure SelectedObjects_SetFilterDisabled(AValue: Boolean);
procedure SetState_ConstraintManagerData(Value: WideString);
procedure SetState_IsLocked(Value: Boolean);
procedure SetState_MechanicalLayerKindMapping(const Value: TArray<RT_PCB.TMechanicalLayerToKindItem>);
procedure SetState_Navigate_HighlightObjectListEx(HighlightMethods: THighlightMethodSet; ClearExisting: Boolean; HighBoardOutline: Boolean; ClearExistingHighlights: Boolean; FullUpdate: Boolean);
procedure SetState_UseConstraintManager(AValue: Boolean);
procedure SetState_ZoomOnViolations(AValue: Boolean);
procedure SortRulesByPriority;

## IPCB_BoardEx2
继承：IPCB_BoardEx2 → IInterface ｜ 单元：RT_PCB ｜ 自有 14 个方法、2 个属性

property RigidFlexAdvanced: Boolean read GetState_RigidFlexAdvanced write SetState_RigidFlexAdvanced;
property SeparateComponentLayers: Boolean read GetState_SeparateComponentLayers write SetState_SeparateComponentLayers;
function GetBoardRegionAtPoint(AX: Integer; AY: Integer): IPCB_BoardRegion;
function GetBoardRegionForPrimitive(APrimitive: IPCB_Primitive): IPCB_BoardRegion;
function GetHealthCheckManager: IPCB_HealthCheckManager;
function GetLayerStackAtPoint(AX: Integer; AY: Integer): IPCB_LayerStack;
function GetLayerStackForPrimitive(APrimitive: IPCB_Primitive): IPCB_LayerStack;
function GetMeshPatchFromPointWithLayer(x: Integer; y: Integer; var MeshID: Integer; var PatchIndex0: Integer; var PatchIndex1: Integer; var PatchIndex2: Integer; var IntersectionX: Integer; var IntersectionY: Integer; var IntersectionZ: Integer; ALayer: Integer): Boolean;
function GetState_RigidFlexAdvanced: Boolean;
function GetState_SeparateComponentLayers: Boolean;
function HasShelvedOrModifiedPolygons: Boolean;
function IsSimpleRigidFlexCompatible: Boolean;
procedure SetState_ExportFullGeometry(AValue: Boolean);
procedure SetState_RigidFlexAdvanced(Value: Boolean);
procedure SetState_SeparateComponentLayers(Value: Boolean);
function TempUseSubstackRules(AValue: Boolean): IInterface;

## IPCB_BoardEx3
继承：IPCB_BoardEx3 → IInterface ｜ 单元：RT_PCB ｜ 自有 2 个方法、0 个属性

function AddMeshObject(const MeshObject: IPCB_MeshObject): Integer;
function AddMeshObjectToLayer(const MeshObject: IPCB_MeshObject; Layer: Integer): Integer;

## IPCB_BoardIterator
继承：IPCB_BoardIterator → IPCB_AbstractIterator → IInterface ｜ 单元：RT_PCB ｜ 自有 2 个方法、0 个属性

procedure AddFilter_Method(AMethod: TIterationMethod);
procedure AddFilter_ProcessSpecialLayers;

## IPCB_BoardLayerSet
继承：IPCB_BoardLayerSet → IInterface ｜ 单元：RT_PCB ｜ 自有 2 个方法、2 个属性

property Layers: IPCB_LayerSet read GetLayers;  // read-only
property Name: WideString read GetName;  // read-only
function GetLayers: IPCB_LayerSet;
function GetName: WideString;

## IPCB_BoardLayerSetManager
继承：IPCB_BoardLayerSetManager → IInterface ｜ 单元：RT_PCB ｜ 自有 4 个方法、3 个属性

property AllSetsCount: Integer read GetState_Count;  // read-only
property BoardLayerSetByIndex[const AIndex: Integer]: IPCB_BoardLayerSet read GetState_LayerSetByIndex;  // read-only
property BoardLayerSetByName[const ASetName: WideString]: IPCB_BoardLayerSet read GetState_LayerSetByName;  // read-only
function GetState_Count: Integer;
function GetState_LayerSetByIndex(const AIndex: Integer): IPCB_BoardLayerSet;
function GetState_LayerSetByName(const ASetName: WideString): IPCB_BoardLayerSet;
function MakeCurrent(const APos: Integer): Integer;

## IPCB_BoardOutline
继承：IPCB_BoardOutline → IPCB_Polygon → IPCB_Group → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 24 个方法、0 个属性

function BoardOutline_GeometricPolygon: IPCB_GeometricPolygon;
function BuildFromObjects_ReturnGeometricPolygon(ALayer: Integer): IPCB_GeometricPolygon;
function ClipWithPolyRegShapes(AUseHolesFromViaPad: Boolean; AUseEmbedded: Boolean): IPCB_PolyRegShapesClipResult;
function CreateBendingLine(const AFromPoint: IDispatch; const AToPoint: IDispatch; AFoldIndex: Integer; ARadius: Integer; AAngle: Double): IPCB_BendingLine;
function CreateSplitLine(const AFromPoint: IDispatch; const AToPoint: IDispatch): IPCB_SplitBoardRegionLine;
procedure DeleteBendingLine(ABendingLine: IPCB_BendingLine);
procedure DeleteSplitLine(ASplitLine: IPCB_SplitBoardRegionLine);
procedure FindIntersectedRegions(ABendingLine: IPCB_BendingLine);
function GetState_BendingLine(AIndex: Integer): IPCB_BendingLine;
function GetState_BendingLinesCount: Integer;
function GetState_HitPrimitive(APrimitive: IPCB_Primitive): Boolean;
function GetState_IntersectedRegionName(AIndex: Integer): WideString;
function GetState_SelectedBendingLine: IPCB_BendingLine;
function GetState_SplitLine(AIndex: Integer): IPCB_SplitBoardRegionLine;
function GetState_SplitLineCount: Integer;
function IntersectedRegionsCount: Integer;
procedure Invalidate;
procedure InvalidateBoardRegions;
procedure InvalidatePlane(Layer: TV6_Layer);
procedure Rebuild;
procedure RebuildRegion(UseCutouts: Boolean; UseEmbeddedBoardCutouts: Boolean; UseRouteToolLayer: Boolean);
procedure Set3DLock(AValue: Boolean; const APrefferedRegion: IPCB_BoardRegion);
procedure SetState_SelectedBendingLine(const AValue: IPCB_BendingLine);
procedure Validate;

## IPCB_BoardOutlineClearanceConstraint
继承：IPCB_BoardOutlineClearanceConstraint → IPCB_Rule → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 5 个方法、1 个属性

property Gap: TCoord read GetState_Gap write SetState_Gap;
function GetClearance(const Obj1: TObjectClearanceId; const Obj2: TObjectClearanceId): Integer;
function GetObstacleTracks(const APrimitive: IPCB_Primitive): IPCB_Group;
function GetState_Gap: Integer;
procedure SetClearance(const Obj1: TObjectClearanceId; const Obj2: TObjectClearanceId; Value: Integer);
procedure SetState_Gap(const Value: Integer);

## IPCB_BoardRegion
继承：IPCB_BoardRegion → IPCB_Region → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 16 个方法、6 个属性

property BendingLines[AIndex: Integer]: IPCB_BendingLine read GetBendingLines;  // read-only
property BendingLinesCount: Integer read GetState_BendingLinesCount;  // read-only
property CustomCoverlays: Boolean read GetState_CustomCoverlays write SetState_CustomCoverlays;
property LayerStack: IPCB_LayerStack read GetState_LayerStack write SetState_LayerStack;
property Locked3D: Boolean read GetState_Locked3D write SetState_Locked3D;
property Priority: Integer read GetState_Priority write SetState_Priority;
procedure AddCoverlayRegions;
function CreateBendingLine(const AFromPoint: IDispatch; const AToPoint: IDispatch; AFoldIndex: Integer; ARadius: Integer; AAngle: Double): IPCB_BendingLine;
procedure DeleteBendingLine(ABendingLine: IPCB_BendingLine);
function GetBendingLines(AIndex: Integer): IPCB_BendingLine;
function GetState_BendingLinesCount: Integer;
function GetState_CustomCoverlays: Boolean;
function GetState_LayerStack: IPCB_LayerStack;
function GetState_Locked3D: Boolean;
function GetState_Priority: Integer;
function IsAddCoverlayRegionsAvailable: Boolean;
function IsRemoveCoverlayRegionsAvailable: Boolean;
procedure RemoveCoverlayRegions;
procedure SetState_CustomCoverlays(AValue: Boolean);
procedure SetState_LayerStack(Value: IPCB_LayerStack);
procedure SetState_Locked3D(Value: Boolean);
procedure SetState_Priority(const AValue: Integer);

## IPCB_BoardRegionsManager
继承：IPCB_BoardRegionsManager → IInterface ｜ 单元：RT_PCB ｜ 自有 4 个方法、2 个属性

property BoardRegion[AIndex: Integer]: IPCB_BoardRegion read GetProperty_BoardRegion;  // read-only
property BoardRegionCount: Integer read GetProperty_BoardRegionCount;  // read-only
function CreateBoardRegion: IPCB_BoardRegion;
function GenerateNameOfBoardRegion: WideString;
function GetProperty_BoardRegion(AIndex: Integer): IPCB_BoardRegion;
function GetProperty_BoardRegionCount: Integer;

## IPCB_BoardRoutingOptions
继承：IPCB_BoardRoutingOptions → IInterface ｜ 单元：RT_PCB ｜ 自有 7 个方法、3 个属性

property ShowSignalLayersOnly: Boolean read GetState_ShowSignalLayersOnly write SetState_ShowSignalLayersOnly;
property UseLayer[Id: Cardinal]: Boolean read GetState_UseLayer write SetState_UseLayer;
property Values[Key: WideString]: TPCBString read GetState_Value write SetState_Value;
procedure Clear;
function GetState_ShowSignalLayersOnly: Boolean;
function GetState_UseLayer(Id: Cardinal): Boolean;
function GetState_Value(Key: WideString): WideString;
procedure SetState_ShowSignalLayersOnly(Value: Boolean);
procedure SetState_UseLayer(Id: Cardinal; Value: Boolean);
procedure SetState_Value(Key: WideString; Value: WideString);

## IPCB_BoardUnionManager
继承：IPCB_BoardUnionManager → IInterface ｜ 单元：RT_PCB ｜ 自有 8 个方法、0 个属性

procedure AddPrimitiveToUnion(AUnionIndex: Integer; APrimitive: IPCB_Primitive);
procedure DirectAddPrimitiveToUnion(AUnionIndex: Integer; APrimitive: IPCB_Primitive);
function FindUnusedUnionIndex: Integer;
function GetSmartUnionByIndex(const UnionIndex: Integer): IPCB_SmartUnionObject;
function GetState_UnionCount: Integer;
function GetState_Unions(AIndex: Integer): IPCB_Union;
function GetState_UnionsByUnionIndex(AIndex: Integer): IPCB_Union;
function GetUnusedUnionIndexForSmartUnion(const AUnionID: TSmartUnionObjectType): Integer;

## IPCB_BrokenNetRule
继承：IPCB_BrokenNetRule → IPCB_Rule → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 4 个方法、2 个属性

property CheckBadConnections: Boolean read GetState_CheckBadConnections write SetState_CheckBadConnections;
property HighlightPolygons: Boolean read GetState_HighlightPolygons write SetState_HighlightPolygons;
function GetState_CheckBadConnections: Boolean;
function GetState_HighlightPolygons: Boolean;
procedure SetState_CheckBadConnections(Value: Boolean);
procedure SetState_HighlightPolygons(Value: Boolean);

## IPCB_Canceler
继承：IPCB_Canceler → IInterface ｜ 单元：RT_PCB ｜ 自有 1 个方法、0 个属性

function IsCancelled: Boolean;

## IPCB_CapabilitiesFactory
继承：IPCB_CapabilitiesFactory → IInterface ｜ 单元：RT_PCB ｜ 自有 1 个方法、0 个属性

function GetSupportedTextureFileFormats: IStrings;

## IPCB_CartesianGrid
继承：IPCB_CartesianGrid → IPCB_PlacementGrid → IPCB_PlacementGuide → IInterface ｜ 单元：RT_PCB ｜ 自有 12 个方法、6 个属性

property GridStepX: TDouble read GetProperty_GridStepX write SetProperty_GridStepX;
property GridStepY: TDouble read GetProperty_GridStepY write SetProperty_GridStepY;
property QuadrantSizeX: TCoord read GetProperty_QuadrantSizeX write SetProperty_QuadrantSizeX;
property QuadrantSizeY: TCoord read GetProperty_QuadrantSizeY write SetProperty_QuadrantSizeY;
property Rotation: TAngle read GetProperty_Rotation write SetProperty_Rotation;
property ValidQuadrant[const QuadrantIdx_1Based: Cardinal]: Boolean read GetProperty_ValidQuadrant write SetProperty_ValidQuadrant;
function GetProperty_GridStepX: Double;
function GetProperty_GridStepY: Double;
function GetProperty_QuadrantSizeX: Integer;
function GetProperty_QuadrantSizeY: Integer;
function GetProperty_Rotation: Double;
function GetProperty_ValidQuadrant(const QuadrantIdx_1Based: Cardinal): Boolean;
procedure SetProperty_GridStepX(const Value: Double);
procedure SetProperty_GridStepY(const Value: Double);
procedure SetProperty_QuadrantSizeX(const Value: Integer);
procedure SetProperty_QuadrantSizeY(const Value: Integer);
procedure SetProperty_Rotation(const Value: Double);
procedure SetProperty_ValidQuadrant(const QuadrantIdx_1Based: Cardinal; const Value: Boolean);

## IPCB_CenterDimension
继承：IPCB_CenterDimension → IPCB_Dimension → IPCB_Group → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 4 个方法、1 个属性

property Angle: TAngle read GetState_Angle write SetState_Angle;
function Cross_Horizontal_Track: IPCB_Track;
function Cross_Vertical_Track: IPCB_Track;
function GetState_Angle: Double;
procedure SetState_Angle(Value: Double);

## IPCB_CheckNetAntennaeRule
继承：IPCB_CheckNetAntennaeRule → IPCB_Rule → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 2 个方法、1 个属性

property NetAntennaeTolerance: TCoord read GetState_NetAntennaeTolerance write SetState_NetAntennaeTolerance;
function GetState_NetAntennaeTolerance: Integer;
procedure SetState_NetAntennaeTolerance(Value: Integer);

## IPCB_ClearanceConstraint
继承：IPCB_ClearanceConstraint → IPCB_Rule → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 8 个方法、2 个属性

property Gap: TCoord read GetState_Gap write SetState_Gap;
property Mode: TClearanceConstraintMode read GetState_Mode;  // read-only
function GetClearance(P1: IPCB_Primitive; P2: IPCB_Primitive): Integer;
function GetState_Gap: Integer;
function GetState_IgnorePadToPad: Boolean;
function GetState_Mode: TClearanceConstraintMode;
function PrimitivesViolate(P1: IPCB_Primitive; P2: IPCB_Primitive): Boolean;
procedure SetClearance(P1: IPCB_Primitive; P2: IPCB_Primitive; Value: Integer);
procedure SetState_Gap(Value: Integer);
procedure SetState_IgnorePadToPad(Value: Boolean);

## IPCB_ClipBoard
继承：IPCB_ClipBoard → IInterface ｜ 单元：RT_PCB ｜ 自有 1 个方法、0 个属性

function GetPrimitiveCount(AObjSet: TObjectSet): Integer;

## IPCB_ColorID
继承：IPCB_ColorID → IInterface ｜ 单元：RT_PCB ｜ 自有 0 个方法、0 个属性


## IPCB_Component
继承：IPCB_Component → IPCB_Group → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 97 个方法、38 个属性

property Axis[I: Integer]: IPCB_Axis read GetState_Axis;  // read-only
property AxisCount: Integer read GetState_AxisCount;  // read-only
property ChannelOffset: TChannelOffset read GetState_ChannelOffset write SetState_ChannelOffset;
property Comment: IPCB_Text read GetState_Comment;  // read-only
property CommentAutoPosition: TTextAutoposition read GetState_CommentAutoPos write SetState_CommentAutoPos;
property CommentOn: Boolean read GetState_CommentOn write SetState_CommentOn;
property ComponentKind: TComponentKind read GetState_ComponentKind write SetState_ComponentKind;
property DefaultPCB3DModel: TPCBString read GetState_DefaultPCB3DModel write SetState_DefaultPCB3DModel;
property EnablePartSwapping: Boolean read GetState_EnablePartSwapping write SetState_EnablePartSwapping;
property EnablePinSwapping: Boolean read GetState_EnablePinSwapping write SetState_EnablePinSwapping;
property FlippedOnLayer: Boolean read GetState_FlippedOnLayer write SetState_FlippedOnLayer;
property FootprintConfigurableParameters_Encoded: TPCBString read GetState_FootprintConfigurableParameters_Encoded write SetState_FootprintConfigurableParameters_Encoded;
property FootprintConfiguratorName: TPCBString read GetState_FootprintConfiguratorName write SetState_FootprintConfiguratorName;
property FootprintDescription: TPCBString read GetState_FootprintDescription write SetState_FootprintDescription;
property FPGADisplayMode: TFPGADisplayMode read GetState_FPGADisplayMode write SetState_FPGADisplayMode;
property GroupNum: Integer read GetState_GroupNum write SetState_GroupNum;
property Height: TCoord read GetState_Height write SetState_Height;
property IsBGA: Boolean read GetState_IsBGA;  // read-only
property ItemGUID: TPCBString read GetState_ItemGUID write SetState_ItemGUID;
property ItemRevisionGUID: TPCBString read GetState_ItemRevisionGUID write SetState_ItemRevisionGUID;
property JumpersVisible: Boolean read GetState_JumpersVisible write SetState_JumpersVisible;
property LockStrings: Boolean read GetState_LockStrings write SetState_LockStrings;
property ModelHash: TPCBString read GetState_ModelHash;  // read-only
property Name: IPCB_Text read GetState_Name;  // read-only
property NameAutoPosition: TTextAutoposition read GetState_NameAutoPos write SetState_NameAutoPos;
property NameOn: Boolean read GetState_NameOn write SetState_NameOn;
property PackageSpecificHash: TPCBString read GetState_PackageSpecificHash;  // read-only
property Pattern: TPCBString read GetState_Pattern write SetState_Pattern;
property Rotation: TAngle read GetState_Rotation write SetState_Rotation;
property SourceCompDesignItemID: TPCBString read GetState_SourceCompDesignItemID write SetState_SourceCompDesignItemID;
property SourceComponentLibrary: TPCBString read GetState_SourceComponentLibrary write SetState_SourceComponentLibrary;
property SourceDescription: TPCBString read GetState_SourceDescription write SetState_SourceDescription;
property SourceDesignator: TPCBString read GetState_SourceDesignator write SetState_SourceDesignator;
property SourceFootprintLibrary: TPCBString read GetState_SourceFootprintLibrary write SetState_SourceFootprintLibrary;
property SourceHierarchicalPath: TPCBString read GetState_SourceHierarchicalPath write SetState_SourceHierarchicalPath;
property SourceLibReference: TPCBString read GetState_SourceLibReference write SetState_SourceLibReference;
property SourceUniqueId: TPCBString read GetState_SourceUniqueId write SetState_SourceUniqueId;
property VaultGUID: TPCBString read GetState_VaultGUID write SetState_VaultGUID;
function AddAxis: IPCB_Axis;
procedure AutoPosition_NameComment;
procedure AutoPosition_NameComment_APILike;
function BoundingRectangleNoNameComment: IDispatch;
function BoundingRectangleNoNameCommentForSignals: IDispatch;
procedure ChangeAutopositionNameComment;
function ChangeCommentAutoposition(Value: TTextAutoposition): Boolean;
function ChangeNameAutoposition(Value: TTextAutoposition): Boolean;
procedure ClearAxes;
procedure Displace(const Displacement: Pointer);
procedure FlipComponent;
function GetState_Axis(I: Integer): IPCB_Axis;
function GetState_AxisCount: Integer;
function GetState_ChannelOffset: Integer;
function GetState_Comment: IPCB_Text;
function GetState_CommentAutoPos: TTextAutoposition;
function GetState_CommentOn: Boolean;
function GetState_ComponentKind: TComponentKind;
function GetState_DefaultPCB3DModel: WideString;
function GetState_EnablePartSwapping: Boolean;
function GetState_EnablePinSwapping: Boolean;
function GetState_FlippedOnLayer: Boolean;
function GetState_FootprintConfigurableParameters_Encoded: WideString;
function GetState_FootprintConfiguratorName: WideString;
function GetState_FootprintDescription: WideString;
function GetState_FPGADisplayMode: TFPGADisplayMode;
function GetState_GroupNum: Integer;
function GetState_Height: Integer;
function GetState_IsBGA: Boolean;
function GetState_ItemGUID: WideString;
function GetState_ItemRevisionGUID: WideString;
function GetState_JumpersVisible: Boolean;
function GetState_LockStrings: Boolean;
function GetState_ModelHash: WideString;
function GetState_Name: IPCB_Text;
function GetState_NameAutoPos: TTextAutoposition;
function GetState_NameOn: Boolean;
function GetState_PackageSpecificHash: WideString;
function Getstate_PadByName(S: WideString): IPCB_Primitive;
function GetState_Pattern: WideString;
function GetState_Rotation: Double;
function GetState_SourceCompDesignItemID: WideString;
function GetState_SourceComponentLibrary: WideString;
function GetState_SourceDescription: WideString;
function GetState_SourceDesignator: WideString;
function GetState_SourceFootprintLibrary: WideString;
function GetState_SourceHierarchicalPath: WideString;
function GetState_SourceLibReference: WideString;
function GetState_SourceUniqueId: WideString;
function GetState_VaultGUID: WideString;
function IsConfigurableFootprint: Boolean;
function IsFitted: Boolean;
function IsPackageEqual(const AComp: IPCB_Component): Boolean;
function IsPackageEqualEx(const AComp: IPCB_Component; AOptions: TPackageCompareOptionSet): Boolean;
function LoadCompFromLibrary: Boolean;
function LoadFromLibrary(AParams: PWideChar): Boolean;
procedure Rebuild;
function ReferencePointOutsideArea: Boolean;
procedure ResetDisplacement;
procedure RotateAroundXY(AX: Integer; AY: Integer; Angle: Double);
function SaveModelToFile(FullPath: WideString): Boolean;
function SaveModelToFileAsPart(FullPath: WideString): Boolean;
function SaveModelToOccDoc(OccDoc: IOCCDocument): Boolean;
procedure SetComponentPositionFrom(ASource: IPCB_Component);
procedure SetState_ChannelOffset(Value: Integer);
procedure SetState_CommentAutoPos(Value: TTextAutoposition);
procedure SetState_CommentOn(Value: Boolean);
procedure SetState_ComponentKind(Value: TComponentKind);
procedure SetState_DefaultPCB3DModel(Value: WideString);
procedure SetState_EnablePartSwapping(Value: Boolean);
procedure SetState_EnablePinSwapping(Value: Boolean);
procedure SetState_FlippedOnLayer(Value: Boolean);
procedure SetState_FootprintConfigurableParameters_Encoded(Value: WideString);
procedure SetState_FootprintConfiguratorName(Value: WideString);
procedure SetState_FootprintDescription(Value: WideString);
procedure SetState_FPGADisplayMode(Value: TFPGADisplayMode);
procedure SetState_GroupNum(Value: Integer);
procedure SetState_Height(Value: Integer);
procedure SetState_ItemGUID(Value: WideString);
procedure SetState_ItemRevisionGUID(Value: WideString);
procedure SetState_JumpersVisible(Value: Boolean);
procedure SetState_LockStrings(Value: Boolean);
procedure SetState_NameAutoPos(Value: TTextAutoposition);
procedure SetState_NameOn(Value: Boolean);
procedure SetState_Pattern(Value: WideString);
procedure SetState_Rotation(Value: Double);
procedure SetState_SourceCompDesignItemID(Value: WideString);
procedure SetState_SourceComponentLibrary(Value: WideString);
procedure SetState_SourceDescription(Value: WideString);
procedure SetState_SourceDesignator(Value: WideString);
procedure SetState_SourceFootprintLibrary(Value: WideString);
procedure SetState_SourceHierarchicalPath(Value: WideString);
procedure SetState_SourceLibReference(Value: WideString);
procedure SetState_SourceUniqueId(Value: WideString);
procedure SetState_VaultGUID(Value: WideString);
function SetState_XSizeYSize: Boolean;
procedure ShowLibraryInExplorer;

## IPCB_Component3D
继承：IPCB_Component3D → IPCB_Component → IPCB_Group → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 1 个方法、0 个属性

procedure SetState_FacePosition(AFaceIdx: Integer; AU: Integer; AV: Integer; ARot: Double);

## IPCB_ComponentBody
继承：IPCB_ComponentBody → IPCB_Region → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 62 个方法、15 个属性

property Axis[Index: Integer]: IPCB_Axis read GetAxis;  // read-only
property BodyColor3D: TColor read GetBodyColor3D write SetBodyColor3D;
property BodyOpacity3D: Single read GetBodyOpacity3D write SetBodyOpacity3D;
property BodyProjection: TBoardSide read GetBodyProjection write SetBodyProjection;
property Model: IPCB_Model read GetModel write SetModel;
property ModelHasChanged: Boolean read GetState_ModelHasChanged;  // read-only
property OverallHeight: TCoord read GetOverallHeight write SetOverallHeight;
property OverrideColor: Boolean read GetOverrideColor write SetOverrideColor;
property SnapPointX: TCoord read GetState_SnapPointX write SetState_SnapPointX;
property SnapPointY: TCoord read GetState_SnapPointY write SetState_SnapPointY;
property StandoffHeight: TCoord read GetStandoffHeight write SetStandoffHeight;
property Texture: TPCBString read GetTexture write SetTexture;
property TextureCenter: TCoordPoint read GetTextureCenter write SetTextureCenter;
property TextureRotation: TAngle read GetTextureRotation write SetTextureRotation;
property TextureSize: TCoordPoint read GetTextureSize write SetTextureSize;
function AddAxis: IPCB_Axis;
function AxisCount: Integer;
function ChooseFile(var AFilename: WideString): LongBool;
function ChooseModel(var AFilename: WideString): LongBool;
procedure ClearAxes;
procedure Displace(const Displacement: Pointer);
procedure Fade(Value: Single);
function GetAxis(Index: Integer): IPCB_Axis;
function GetBodyColor3D: Cardinal;
function GetBodyOpacity3D: Single;
function GetBodyProjection: TBoardSide;
function GetModel: IPCB_Model;
function GetOverallHeight: Integer;
function GetOverrideColor: Boolean;
function GetStandoffHeight: Integer;
function GetState_ModelHasChanged: Boolean;
function GetState_ModelType: T3DModelType;
function GetState_SnapCount: Integer;
function GetState_SnapPoint(Index: Integer): IDispatch;
function GetState_SnapPointX: Integer;
function GetState_SnapPointY: Integer;
function GetTexture: WideString;
function GetTextureCenter: IDispatch;
function GetTextureRotation: Double;
function GetTextureSize: IDispatch;
procedure GetTransform_ModelToComponent(P: Pointer);
procedure LoadGenericModelFromFile(const AFilename: WideString; const AMakeEmbeded: LongBool);
function ModelFactory_Create(const ModelType: T3DModelType): IPCB_Model;
function ModelFactory_CreateCylinder(const Radius: Integer; const Height: Integer; const Color: Cardinal): IPCB_Model;
function ModelFactory_CreateExtruded(const MinZ: Integer; const MaxZ: Integer; const Color: Cardinal): IPCB_Model;
function ModelFactory_CreateSphere(const Radius: Integer; const Color: Cardinal): IPCB_Model;
procedure ModelFactory_Destroy(var Value: IPCB_Model);
function ModelFactory_FromFilename(FileName: WideString; WatchDirectory: Boolean): IPCB_Model;
function ModelFactory_FromVault(const ATitle: WideString; const AVaultGUID: WideString; const AItemGUID: WideString; const AItemRevisionGUID: WideString): IPCB_Model;
procedure ModelFactory_Replace(const ModelType: T3DModelType; var Value: IPCB_Model);
function ModelFactory_UpdateModel(const Radius: Integer; const Height: Integer; const ModelType: T3DModelType): Boolean;
procedure RecreateModel;
procedure ResetDisplacement;
procedure ResetFade;
function SaveModelToFile(FullPath: WideString): Boolean;
procedure SetBodyColor3D(Value: Cardinal);
procedure SetBodyOpacity3D(Value: Single);
procedure SetBodyProjection(Value: TBoardSide);
procedure SetModel(Value: IPCB_Model);
procedure SetOverallHeight(Value: Integer);
procedure SetOverrideColor(Value: Boolean);
procedure SetStandoffHeight(Value: Integer);
procedure SetState_FromModel;
procedure SetState_Identifier(const Value: WideString);
procedure SetState_ModelType(const Value: T3DModelType);
procedure SetState_SnapCount(Count: Integer);
procedure SetState_SnapPoint(Index: Integer; const Point: IDispatch);
procedure SetState_SnapPointX(Value: Integer);
procedure SetState_SnapPointY(Value: Integer);
procedure SetTexture(Value: WideString);
procedure SetTextureCenter(const Value: IDispatch);
procedure SetTextureRotation(Value: Double);
procedure SetTextureSize(const Value: IDispatch);
function UniqueName: WideString;
procedure UpdateModelFromDisk;
procedure UpdateModelToLatestRevision;
procedure ValidateMesh;

## IPCB_ComponentClearanceConstraint
继承：IPCB_ComponentClearanceConstraint → IPCB_Rule → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 12 个方法、6 个属性

property CheckComponentBoundary: Boolean read GetState_CheckComponentBoundary write SetState_CheckComponentBoundary;
property CollisionCheckMode: TComponentCollisionCheckMode read GetState_CollisionCheckMode write SetState_CollisionCheckMode;
property DoNotCheckWithout3DBody: Boolean read GetState_DoNotCheckWithout3DBody write SetState_DoNotCheckWithout3DBody;
property Gap: TCoord read GetState_Gap write SetState_Gap;
property ShowDistances: Boolean read GetState_ShowDistances write SetState_ShowDistances;
property VerticalGap: TCoord read GetState_VerticalGap write SetState_VerticalGap;
function GetState_CheckComponentBoundary: Boolean;
function GetState_CollisionCheckMode: TComponentCollisionCheckMode;
function GetState_DoNotCheckWithout3DBody: Boolean;
function GetState_Gap: Integer;
function GetState_ShowDistances: Boolean;
function GetState_VerticalGap: Integer;
procedure SetState_CheckComponentBoundary(Value: Boolean);
procedure SetState_CollisionCheckMode(Value: TComponentCollisionCheckMode);
procedure SetState_DoNotCheckWithout3DBody(Value: Boolean);
procedure SetState_Gap(Value: Integer);
procedure SetState_ShowDistances(Value: Boolean);
procedure SetState_VerticalGap(Value: Integer);

## IPCB_ComponentPainter3DChangedHandler
继承：IPCB_ComponentPainter3DChangedHandler → IInterface ｜ 单元：RT_PCB ｜ 自有 1 个方法、0 个属性

procedure Handle3DChangedEvent(Value: Boolean);

## IPCB_ComponentPainterView
继承：IPCB_ComponentPainterView → IInterface ｜ 单元：RT_PCB ｜ 自有 18 个方法、0 个属性

procedure ClearGraphicalObjects;
procedure ConfigView(Parameters: WideString);
function GetDummyBoard: IPCB_Board;
function GetIs3D: Boolean;
function GetIsItemNotFound: Boolean;
procedure KeyDown(var Key: Word; Shift: TShiftState);
procedure MouseWheel(Sender: TObject; Shift: TShiftState; WheelDelta: Integer; const MousePos: IDispatch; var Handled: Boolean);
procedure RefreshView;
procedure Register3DChangedHandler(Is3DChangedHandler: IPCB_ComponentPainter3DChangedHandler);
procedure RegisterGOMouseHoverHandler(GraphicalObjectMouseHoverHandler: IPCB_GOMouseHoverHandler);
procedure SetAllLayersVisibilityState(Visible: Boolean);
procedure SetCamera(LowX: Integer; LowY: Integer; HighX: Integer; HighY: Integer);
procedure SetCameraAngle(LookAtX: Double; LookAtY: Double; LookAtZ: Double; RotationX: Double; RotationY: Double; RotationZ: Double; RotationW: Double; ZoomMultiplier: Double);
procedure SetComponentByHandle(const AComponent: IPCB_Component);
procedure SetComponentByPath(APattern: WideString; ALibraryPath: WideString);
procedure SetDirectXMode;
procedure SetVariantOption(const AVariantOption: IVariantOption);
procedure SetViewRect(LowX: Integer; LowY: Integer; HighX: Integer; HighY: Integer);

## IPCB_ComponentRotationsRule
继承：IPCB_ComponentRotationsRule → IPCB_Rule → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 2 个方法、1 个属性

property AllowedRotations: Integer read GetState_AllowedRotations write SetState_AllowedRotations;
function GetState_AllowedRotations: Integer;
procedure SetState_AllowedRotations(Value: Integer);

## IPCB_ComponentUpdateOptions
继承：IPCB_ComponentUpdateOptions → IInterface ｜ 单元：RT_PCB ｜ 自有 1 个方法、0 个属性

function Import_FromUser_Execute(const AMousePos: IDispatch): Boolean;

## IPCB_ConfinementConstraint
继承：IPCB_ConfinementConstraint → IPCB_Rule → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 19 个方法、8 个属性

property BoundingRect: TCoordRect read GetState_BoundingRectangle write SetState_BoundingRectangle;
property ConstraintLayer: TV6_Layer read GetState_ConstraintLayer write SetState_ConstraintLayer;
property Kind: TConfinementStyle read GetState_Kind write SetState_Kind;
property LockComponents: Boolean read GetState_LockComponents write SetState_LockComponents;
property PointCount: Integer read GetState_PointCount write SetState_PointCount;
property Segments[I: Integer]: TPolySegment read GetState_Segments write SetState_Segments;
property x: TCoord read GetState_XLocation write SetState_XLocation;
property y: TCoord read GetState_YLocation write SetState_YLocation;
function ArrangeComponents: Boolean;
function GetConfinedComponents(AComponents: IInterfaceList): Boolean;
function GetState_BoundingRectangle: IDispatch;
function GetState_ConstraintLayer: TV6_Layer;
function GetState_Kind: TConfinementStyle;
function GetState_LockComponents: Boolean;
function GetState_PointCount: Integer;
function GetState_Segments(I: Integer): IDispatch;
function GetState_XLocation: Integer;
function GetState_YLocation: Integer;
procedure RotateAroundXY(AX: Integer; AY: Integer; Angle: Double);
procedure SetState_BoundingRectangle(const BR: IDispatch);
procedure SetState_ConstraintLayer(Value: TV6_Layer);
procedure SetState_Kind(Value: TConfinementStyle);
procedure SetState_LockComponents(Value: Boolean);
procedure SetState_PointCount(Value: Integer);
procedure SetState_Segments(I: Integer; const Value: IDispatch);
procedure SetState_XLocation(AX: Integer);
procedure SetState_YLocation(AY: Integer);

## IPCB_Connection
继承：IPCB_Connection → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 16 个方法、7 个属性

property Layer1: TV6_Layer read GetState_Layer1 write SetState_Layer1;
property Layer2: TV6_Layer read GetState_Layer2 write SetState_Layer2;
property Mode: TConnectionMode read GetState_Mode write SetState_Mode;
property x1: TCoord read GetState_X1 write SetState_X1;
property x2: TCoord read GetState_X2 write SetState_X2;
property y1: TCoord read GetState_Y1 write SetState_Y1;
property y2: TCoord read GetState_Y2 write SetState_Y2;
function GetState_Layer1: TV6_Layer;
function GetState_Layer2: TV6_Layer;
function GetState_Mode: TConnectionMode;
function GetState_X1: Integer;
function GetState_X2: Integer;
function GetState_Y1: Integer;
function GetState_Y2: Integer;
function IsRedundant: Boolean;
procedure RotateAroundXY(AX: Integer; AY: Integer; Angle: Double);
procedure SetState_Layer1(Value: TV6_Layer);
procedure SetState_Layer2(Value: TV6_Layer);
procedure SetState_Mode(Value: TConnectionMode);
procedure SetState_X1(Value: Integer);
procedure SetState_X2(Value: Integer);
procedure SetState_Y1(Value: Integer);
procedure SetState_Y2(Value: Integer);

## IPCB_Connection3D
继承：IPCB_Connection3D → IPCB_Connection → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 12 个方法、6 个属性

property FaceIdx1: Integer read GetState_FaceIdx1 write SetState_FaceIdx1;
property FaceIdx2: Integer read GetState_FaceIdx2 write SetState_FaceIdx2;
property FaceU1: Integer read GetState_FaceU1 write SetState_FaceU1;
property FaceU2: Integer read GetState_FaceU2 write SetState_FaceU2;
property FaceV1: Integer read GetState_FaceV1 write SetState_FaceV1;
property FaceV2: Integer read GetState_FaceV2 write SetState_FaceV2;
function GetState_FaceIdx1: Integer;
function GetState_FaceIdx2: Integer;
function GetState_FaceU1: Integer;
function GetState_FaceU2: Integer;
function GetState_FaceV1: Integer;
function GetState_FaceV2: Integer;
procedure SetState_FaceIdx1(Value: Integer);
procedure SetState_FaceIdx2(Value: Integer);
procedure SetState_FaceU1(Value: Integer);
procedure SetState_FaceU2(Value: Integer);
procedure SetState_FaceV1(Value: Integer);
procedure SetState_FaceV2(Value: Integer);

## IPCB_Contour
继承：IPCB_Contour → IInterface ｜ 单元：RT_PCB ｜ 自有 18 个方法、5 个属性

property Area: Double read GetState_Area;  // read-only
property Count: Integer read GetState_Count write SetState_Count;
property VertexList: Pointer read GetState_VertexList;  // read-only
property x[I: Integer]: TCoord read GetState_PointX write SetState_PointX;
property y[I: Integer]: TCoord read GetState_PointY write SetState_PointY;
procedure AddContour(const C: IPCB_Contour; const StartIndex: Integer; const EndIndex: Integer);
procedure AddPoint(x: Integer; y: Integer);
procedure Clear;
procedure DeletePoint(Index: Integer);
procedure EnsureCapacity(Value: Integer);
function GetState_Area: Double;
function GetState_Count: Integer;
function GetState_PointX(I: Integer): Integer;
function GetState_PointY(I: Integer): Integer;
function GetState_VertexList: Pointer;
procedure InsertPoint(Index: Integer; x: Integer; y: Integer);
function Replicate: IPCB_Contour;
procedure Rotate(AngleInDegrees: Double);
procedure RotateAboutPoint(AngleInDegrees: Double; x: Integer; y: Integer);
procedure SetState_Count(Value: Integer);
procedure SetState_PointX(I: Integer; const Value: Integer);
procedure SetState_PointY(I: Integer; const Value: Integer);
procedure Translate(x: Integer; y: Integer);

## IPCB_ContourMaker
继承：IPCB_ContourMaker → IInterface ｜ 单元：RT_PCB ｜ 自有 4 个方法、1 个属性

property ArcResolution: TCoord read GetState_ArcResolution write SetState_ArcResolution;
procedure AddArcToContour(AContour: IPCB_Contour; StartAngle: Double; EndAngle: Double; cx: Integer; cy: Integer; Radius: Integer; AClockwise: Boolean);
function GetState_ArcResolution: Integer;
function MakeContour(APrim: IPCB_Primitive; AExpansion: Integer; ALayer: TV6_Layer): IPCB_GeometricPolygon;
procedure SetState_ArcResolution(Value: Integer);

## IPCB_ContourMaker2
继承：IPCB_ContourMaker2 → IPCB_ContourMaker → IInterface ｜ 单元：RT_PCB ｜ 自有 1 个方法、0 个属性

function MakeContour(APrim: IPCB_Primitive; AExpansion: Integer; ALayer: TV6_Layer): IPCB_GeometricPolygon;

## IPCB_ContourUtilities
继承：IPCB_ContourUtilities → IInterface ｜ 单元：RT_PCB ｜ 自有 11 个方法、0 个属性

procedure ClipContourContour(SetOperation: TSetOperation; AContour: IPCB_Contour; BContour: IPCB_Contour; ResultPolygon: IPCB_GeometricPolygon);
procedure ClipSetContour(SetOperation: TSetOperation; AGeometricPolygon: IPCB_GeometricPolygon; AContour: IPCB_Contour; ResultPolygon: IPCB_GeometricPolygon);
procedure ClipSetSet(SetOperation: TSetOperation; AGeometricPolygon: IPCB_GeometricPolygon; BGeometricPolygon: IPCB_GeometricPolygon; ResultPolygon: IPCB_GeometricPolygon);
function ContourArea(AContour: IPCB_Contour): Double;
function ContourIsCW(AContour: IPCB_Contour): Boolean;
function CreateInterfaceList: IInterfaceList;
function GeometricPolygonsTouch(AGeometricPolygon: IPCB_GeometricPolygon; BGeometricPolygon: IPCB_GeometricPolygon): Boolean;
function PointInContour(AContour: IPCB_Contour; x: Integer; y: Integer): Boolean;
procedure SplitIntoConnectedPolygons(AGeometricPolygon: IPCB_GeometricPolygon; ConnectedPolygons: IInterfaceList);
procedure UnionBatchContour(Contours: IInterfaceList; ResultPolygon: IPCB_GeometricPolygon);
procedure UnionBatchSet(Polygons: IInterfaceList; ResultPolygon: IPCB_GeometricPolygon);

## IPCB_Coordinate
继承：IPCB_Coordinate → IPCB_Group → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 28 个方法、11 个属性

property Bold: Boolean read GetState_Bold write SetState_Bold;
property FontName: TPCBString read GetState_FontName write SetState_FontName;
property Italic: Boolean read GetState_Italic write SetState_Italic;
property LineWidth: TCoord read GetState_LineWidth write SetState_LineWidth;
property Rotation: TAngle read GetState_Rotation write SetState_Rotation;
property Size: TCoord read GetState_Size write SetState_Size;
property Style: TUnitStyle read GetState_Style write SetState_Style;
property TextFont: TFontID read GetState_TextFont write SetState_TextFont;
property TextHeight: TCoord read GetState_TextHeight write SetState_TextHeight;
property TextWidth: TCoord read GetState_TextWidth write SetState_TextWidth;
property UseTTFonts: Boolean read GetState_UseTTFonts write SetState_UseTTFonts;
function GetState_Bold: Boolean;
function GetState_FontName: WideString;
function GetState_Italic: Boolean;
function GetState_LineWidth: Integer;
function GetState_Rotation: Double;
function GetState_Size: Integer;
function GetState_StrictHitTest(HitX: Integer; HitY: Integer): Boolean;
function GetState_Style: TUnitStyle;
function GetState_TextFont: SmallInt;
function GetState_TextHeight: Integer;
function GetState_TextWidth: Integer;
function GetState_UseTTFonts: Boolean;
procedure RotateAroundXY(AX: Integer; AY: Integer; Angle: Double);
procedure SetState_Bold(Bold: Boolean);
procedure SetState_FontName(FontName: WideString);
procedure SetState_Italic(Italic: Boolean);
procedure SetState_LineWidth(Value: Integer);
procedure SetState_Rotation(Value: Double);
procedure SetState_Size(Value: Integer);
procedure SetState_Style(Value: TUnitStyle);
procedure SetState_TextFont(Value: SmallInt);
procedure SetState_TextHeight(Value: Integer);
procedure SetState_TextWidth(Value: Integer);
procedure SetState_UseTTFonts(UseTTFonts: Boolean);
function SetState_XSizeYSize: Boolean;
function Text: IPCB_Primitive;
function Track1: IPCB_Primitive;
function Track2: IPCB_Primitive;

## IPCB_CopperBody
继承：IPCB_CopperBody → IInterface ｜ 单元：RT_PCB ｜ 自有 12 个方法、4 个属性

property Layer: TLayer read GetState_Layer;  // read-only
property Net: IPCB_Net read GetState_Net;  // read-only
property Shape[Index: Integer]: IPCB_CopperBodyShape read GetState_Shape;  // read-only
property ShapeCount: Integer read GetState_ShapeCount;  // read-only
procedure ExportToFile(FileName: WideString);
function ExportToString: WideString;
function GetReferenceBody: IPCB_CopperBody;
function GetState_Hash: WideString;
function GetState_Layer: Integer;
function GetState_Net: IPCB_Net;
function GetState_Shape(Index: Integer): IPCB_CopperBodyShape;
function GetState_ShapeCount: Integer;
function GetState_Suffix: WideString;
function GetXOffset: Integer;
function GetYOffset: Integer;
procedure SaveToSVGFile(FileName: WideString);

## IPCB_CopperBodyList
继承：IPCB_CopperBodyList → IInterface ｜ 单元：RT_PCB ｜ 自有 3 个方法、2 个属性

property CopperBody[I: Integer]: IPCB_CopperBody read GetCopperBody;  // read-only
property Count: Integer read GetCount;  // read-only
function ExportToString: WideString;
function GetCopperBody(I: Integer): IPCB_CopperBody;
function GetCount: Integer;

## IPCB_CopperBodyShape
继承：IPCB_CopperBodyShape → IInterface ｜ 单元：RT_PCB ｜ 自有 5 个方法、4 个属性

property IsHole[Index: Integer]: Boolean read GetState_IsHole;  // read-only
property Region[Index: Integer]: IPCB_RegionShape2 read GetState_Region;  // read-only
property RegionCount: Integer read GetState_RegionCount;  // read-only
property RegionData[Index: Integer]: WideString read GetState_RegionData;  // read-only
function GetState_IsHole(Index: Integer): Boolean;
function GetState_Region(Index: Integer): IPCB_RegionShape2;
function GetState_RegionCount: Integer;
function GetState_RegionData(Index: Integer): WideString;
procedure SaveToSVGFile(FileName: WideString);

## IPCB_CopperPolygon
继承：IPCB_CopperPolygon → IInterface ｜ 单元：RT_PCB ｜ 自有 8 个方法、0 个属性

function BorderVertexCount: Integer;
function CapIndexCount: Integer;
procedure GetBorderVertex(const AIndex: Integer; out ACoordX: Single; out ACoordY: Single; out ANormalX: Byte; out ANormalY: Byte; out ANormalZ: Byte);
function GetCapIndex(const Index: Integer): Integer;
function GetLineIndex(const Index: Integer): Integer;
procedure GetVertex(const Index: Integer; out CoordX: Single; out CoordY: Single);
function LineIndexCount: Integer;
function VertexCount: Integer;

## IPCB_CounterHoleDiameterOnDepthList
继承：IPCB_CounterHoleDiameterOnDepthList → IInterface ｜ 单元：RT_PCB ｜ 自有 4 个方法、0 个属性

procedure Clear;
procedure Delete(Index: Integer);
function Get(Index: Integer): IDispatch;
function GetCount: Integer;

## IPCB_CounterHoleFactory
继承：IPCB_CounterHoleFactory → IInterface ｜ 单元：RT_PCB ｜ 自有 4 个方法、0 个属性

function CreateCounterHoleParams: IPCB_CounterHoleParams;
function CreateCounterHoleParamsList: IPCB_CounterHoleParamsList;
function CreateCounterHoleParamsPreset: IPCB_CounterHoleParamsPreset;
function CreateCounterHoleParamsPresetList: IPCB_CounterHoleParamsPresetList;

## IPCB_CounterHoleParams
继承：IPCB_CounterHoleParams → IInterface ｜ 单元：RT_PCB ｜ 自有 18 个方法、5 个属性

property Angle: TAngle read GetAngle write SetAngle;
property Depth: TCoord read GetDepth write SetDepth;
property Diameter: TCoord read GetDiameter write SetDiameter;
property Direction: TCounterHoleDirection read GetDirection write SetDirection;
property Material: TCounterHoleMaterial read GetMaterial write SetMaterial;
procedure CopyFrom(OtherParams: IPCB_CounterHoleParams);
procedure Deserialize(ParamStr: WideString);
function GetAngle: Double;
function GetCounterHoleType: TCounterHoleType;
function GetDepth: Integer;
function GetDepthForDiameter(ADiameter: Integer): Integer;
function GetDiameter: Integer;
function GetDiameterOnDepth(ADepth: Integer): Integer;
function GetDirection: TCounterHoleDirection;
function GetMaterial: TCounterHoleMaterial;
function IsEqual(OtherParams: IPCB_CounterHoleParams): Boolean;
function IsEqualWithoutMaterial(OtherParams: IPCB_CounterHoleParams): Boolean;
function Serialize: WideString;
procedure SetAngle(Value: Double);
procedure SetDepth(Value: Integer);
procedure SetDiameter(Value: Integer);
procedure SetDirection(Value: TCounterHoleDirection);
procedure SetMaterial(Value: TCounterHoleMaterial);

## IPCB_CounterHoleParamsList
继承：IPCB_CounterHoleParamsList → IInterface ｜ 单元：RT_PCB ｜ 自有 9 个方法、2 个属性

property Count: Integer read GetCount;  // read-only
property Params[Index: Integer]: IPCB_CounterHoleParams read GetParams;  // read-only
function AddNew: IPCB_CounterHoleParams;
procedure Clear;
procedure Delete(Index: Integer);
procedure Deserialize(ParamStr: WideString);
function GetCount: Integer;
function GetParams(Index: Integer): IPCB_CounterHoleParams;
function IsEqual(OtherParamList: IPCB_CounterHoleParamsList): Boolean;
function Replicate: IPCB_CounterHoleParamsList;
function Serialize: WideString;

## IPCB_CounterHoleParamsPreset
继承：IPCB_CounterHoleParamsPreset → IInterface ｜ 单元：RT_PCB ｜ 自有 6 个方法、3 个属性

property Description: TPCBString read GetDescription write SetDescription;
property Name: TPCBString read GetName write SetName;
property ParamList: IPCB_CounterHoleParamsList read GetParamList write SetParamList;
function GetDescription: WideString;
function GetName: WideString;
function GetParamList: IPCB_CounterHoleParamsList;
procedure SetDescription(Value: WideString);
procedure SetName(Value: WideString);
procedure SetParamList(Value: IPCB_CounterHoleParamsList);

## IPCB_CounterHoleParamsPresetList
继承：IPCB_CounterHoleParamsPresetList → IInterface ｜ 单元：RT_PCB ｜ 自有 5 个方法、2 个属性

property Count: Integer read GetCount;  // read-only
property Presets[Index: Integer]: IPCB_CounterHoleParamsPreset read GetPreset;  // read-only
function AddNew: IPCB_CounterHoleParamsPreset;
procedure Clear;
procedure Delete(Index: Integer);
function GetCount: Integer;
function GetPreset(Index: Integer): IPCB_CounterHoleParamsPreset;

## IPCB_CreepageRule
继承：IPCB_CreepageRule → IPCB_Rule → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 6 个方法、1 个属性

property CheckDistance: TCoord read GetState_CheckDistance write SetState_CheckDistance;
function GetState_ApplyToPolygonPour: Boolean;
function GetState_CheckDistance: Integer;
function GetState_IgnoreInternalLayers: Boolean;
procedure SetState_ApplyToPolygonPour(Value: Boolean);
procedure SetState_CheckDistance(Value: Integer);
procedure SetState_IgnoreInternalLayers(Value: Boolean);

## IPCB_CustomInteractiveRoutingProcess
继承：IPCB_CustomInteractiveRoutingProcess → IPCB_InteractiveProcess → IInteractiveProcess ｜ 单元：RT_PCB ｜ 自有 77 个方法、36 个属性

property AllowViaPushing: Boolean read GetState_AllowViaPushing write SetState_AllowViaPushing;
property AutoRemoveAntennas: Boolean read GetState_AutoRemoveAntennas write SetState_AutoRemoveAntennas;
property AutoRemoveLoops: Boolean read GetState_AutoRemoveLoops write SetState_AutoRemoveLoops;
property AutoTerminateRouting: Boolean read GetState_AutoTerminateRouting write SetState_AutoTerminateRouting;
property CornerRounding: Boolean read GetState_CornerRounding write SetState_CornerRounding;
property CurrentLayer: TLayer read GetState_CurrentLayer write SetState_CurrentLayer;
property DisplayClearanceBounds: Boolean read GetState_DisplayClearanceBounds write SetState_DisplayClearanceBounds;
property FollowMouseTrail: Boolean read GetState_FollowMouseTrail write SetState_FollowMouseTrail;
property GlossEffort: TGlossEffort read GetState_GlossEffort write SetState_GlossEffort;
property HoleSize: Integer read GetState_HoleSize write SetState_HoleSize;
property HuggingStyle: THuggingStyle read GetState_HuggingStyle write SetState_HuggingStyle;
property LegacyRouter: Boolean read GetState_LegacyRouter;  // read-only
property MinimumArcSize: Double read GetState_MinimumArcSize write SetState_MinimumArcSize;
property MiterSize: Double read GetState_MiterSize write SetState_MiterSize;
property Net: IPCB_Net read GetState_Net write SetState_Net;
property NetList: IPCB_NetList read GetState_NetList;  // read-only
property NextLayer: TLayer read GetState_NextLayer write SetState_InternalNextLayer;
property PadEntryStability: TCoord read GetState_PadEntryStability write SetState_PadEntryStability;
property PickupWidthFromExistingRoutes: Boolean read GetState_PickupWidthFromExistingRoutes write SetState_PickupWidthFromExistingRoutes;
property PinSwapping: Boolean read GetState_PinSwapping write SetState_PinSwapping;
property ReduceClearanceDisplayArea: Boolean read GetState_ReduceClearanceDisplayArea write SetState_ReduceClearanceDisplayArea;
property RestrictTo9045: Boolean read GetState_RestrictTo9045 write SetState_RestrictTo9045;
property RouteMode: TAdvancedRouteMode read GetState_RouteMode write SetState_RouteMode;
property RouteModeEnabled[AMode: TAdvancedRouteMode]: Boolean read GetState_RouteModeEnabled write SetState_RouteModeEnabled;
property RoutingCornerStyle: TRoutingCornerStyle read GetState_RoutingCornerStyle write SetState_RoutingCornerStyle;
property RoutingPoint: TCoordPoint read GetState_RoutingPoint write SetState_RoutingPoint;
property RoutingViaStyleRule: IPCB_RoutingViaStyleRule read GetState_RoutingViaStyleRule;  // read-only
property RoutingWidthMode: TRoutingWidthMode read GetState_RoutingWidthMode write SetState_RoutingWidthMode;
property SubnetJumperLength: Integer read GetState_SubnetJumperLength write SetState_SubnetJumperLength;
property ViaCombinationManager: IPCB_ViaCombinationManagerInterface read GetState_ViaCombinationManager;  // read-only
property ViaDiameter: Integer read GetState_ViaDiameter write SetState_ViaDiameter;
property ViaLayerPair: Integer read GetState_ViaLayerPair write SetState_ViaLayerPair;
property ViaSizeMode: TRoutingWidthMode read GetState_ViaSizeMode write SetState_ViaSizeMode;
property ViaTemplate: IPCB_PadViaTemplate read GetState_ViaTemplate write SetState_ViaTemplate;
property ViaTemplateChanged: Boolean read GetState_ViaTemplateChanged;  // read-only
property Width: Integer read GetState_Width write SetState_Width;
procedure EditRoutingViaStyleRule;
function GetRoutingOptions: IPCB_RoutingOptionsPage;
function GetState_AllowViaPushing: Boolean;
function GetState_AutoRemoveAntennas: Boolean;
function GetState_AutoRemoveLoops: Boolean;
function GetState_AutoTerminateRouting: Boolean;
function GetState_CornerRounding: Boolean;
function GetState_CurrentLayer: Integer;
function GetState_DisplayClearanceBounds: Boolean;
function GetState_FollowMode: Boolean;
function GetState_FollowMouseTrail: Boolean;
function GetState_GlossEffort: TGlossEffort;
function GetState_HoleSize: Integer;
function GetState_HuggingStyle: THuggingStyle;
function GetState_LegacyRouter: Boolean;
function GetState_MinimumArcSize: Double;
function GetState_MiterSize: Double;
function GetState_NeighborGlossEffort: TGlossEffort;
function GetState_Net: IPCB_Net;
function GetState_NetList: IPCB_NetList;
function GetState_NextLayer: Integer;
function GetState_PadEntryStability: Integer;
function GetState_PickupWidthFromExistingRoutes: Boolean;
function GetState_PinSwapping: Boolean;
function GetState_ReduceClearanceDisplayArea: Boolean;
function GetState_RestrictTo9045: Boolean;
function GetState_RouteMode: TAdvancedRouteMode;
function GetState_RouteModeEnabled(AMode: TAdvancedRouteMode): Boolean;
function GetState_RoutingCornerStyle: TRoutingCornerStyle;
function GetState_RoutingPoint: IDispatch;
function GetState_RoutingViaStyleRule: IPCB_RoutingViaStyleRule;
function GetState_RoutingWidthMode: TRoutingWidthMode;
function GetState_SubnetJumperLength: Integer;
function GetState_ViaCombinationManager: IPCB_ViaCombinationManagerInterface;
function GetState_ViaDiameter: Integer;
function GetState_ViaLayerPair: Integer;
function GetState_ViaSizeMode: TRoutingWidthMode;
function GetState_ViaTemplate: IPCB_PadViaTemplate;
function GetState_ViaTemplateChanged: Boolean;
function GetState_Width: Integer;
function NextRoutingWidthMode: TRoutingWidthMode;
function NextViaLayerPair: Integer;
function NextViaSizeMode: TRoutingWidthMode;
function NextViaTemplate: IPCB_PadViaTemplate;
procedure SetState_AllowViaPushing(AValue: Boolean);
procedure SetState_AutoRemoveAntennas(AValue: Boolean);
procedure SetState_AutoRemoveLoops(AValue: Boolean);
procedure SetState_AutoTerminateRouting(AValue: Boolean);
procedure SetState_CornerRounding(AValue: Boolean);
procedure SetState_CurrentLayer(const AValue: Integer);
procedure SetState_DisplayClearanceBounds(AValue: Boolean);
procedure SetState_FollowMouseTrail(AValue: Boolean);
procedure SetState_GlossEffort(AValue: TGlossEffort);
procedure SetState_HoleSize(AValue: Integer);
procedure SetState_HuggingStyle(ANewValue: THuggingStyle);
procedure SetState_InternalNextLayer(AValue: Integer);
procedure SetState_MinimumArcSize(Value: Double);
procedure SetState_MiterSize(ANewValue: Double);
procedure SetState_NeighborGlossEffort(ANewValue: TGlossEffort);
procedure SetState_Net(const AValue: IPCB_Net);
procedure SetState_NextLayer(AValue: Integer);
procedure SetState_PadEntryStability(ANewValue: Integer);
procedure SetState_PickupWidthFromExistingRoutes(AValue: Boolean);
procedure SetState_PinSwapping(AValue: Boolean);
procedure SetState_ReduceClearanceDisplayArea(AValue: Boolean);
procedure SetState_RestrictTo9045(AValue: Boolean);
procedure SetState_RouteMode(AValue: TAdvancedRouteMode);
procedure SetState_RouteModeEnabled(AMode: TAdvancedRouteMode; AValue: Boolean);
procedure SetState_RoutingCornerStyle(AValue: TRoutingCornerStyle);
procedure SetState_RoutingPoint(const AValue: IDispatch);
procedure SetState_RoutingWidthMode(AValue: TRoutingWidthMode);
procedure SetState_SubnetJumperLength(AValue: Integer);
procedure SetState_ViaDiameter(AValue: Integer);
procedure SetState_ViaLayerPair(AValue: Integer);
procedure SetState_ViaSizeMode(AValue: TRoutingWidthMode);
procedure SetState_ViaTemplate(const AValue: IPCB_PadViaTemplate);
procedure SetState_Width(AValue: Integer);

## IPCB_CustomPadShape
继承：IPCB_CustomPadShape → IInterface ｜ 单元：RT_PCB ｜ 自有 9 个方法、3 个属性

property CustomShape[ALayer: Integer]: IPCB_Region read GetProperty_CustomShape write SetProperty_CustomShape;
property CustomShapeInfo[ALayer: Integer]: IPCB_CustomShapeInfo read GetState_CustomShapeInfo;  // read-only
property CustomShapeKind[ALayer: Integer]: TShapeSubKind read GetProperty_CustomShapeKind write SetProperty_CustomShapeKind;
function ConstructCustomPadShape(const ALayer: IDispatch; const AInvolvedPrimitives: ISafeInterfaceList): IPCB_GeometricPolygon;
procedure CreateDefaultShape(ALayer: Integer);
function GetProperty_CustomShape(ALayer: Integer): IPCB_Region;
function GetProperty_CustomShapeKind(ALayer: Integer): TShapeSubKind;
function GetState_CustomShapeInfo(ALayer: Integer): IPCB_CustomShapeInfo;
function GetState_ExtractedRegionOnLayer(ALayer: Integer): IPCB_Region;
function GetState_RegionShapeOnLayer(ALayer: Integer): IPCB_Region;
procedure SetProperty_CustomShape(ALayer: Integer; const AShape: IPCB_Region);
procedure SetProperty_CustomShapeKind(ALayer: Integer; const AValue: TShapeSubKind);

## IPCB_CustomShapeInfo
继承：IPCB_CustomShapeInfo → IInterface ｜ 单元：RT_PCB ｜ 自有 6 个方法、2 个属性

property CornerEnabled[const ACorner: TRectCorner]: Boolean read GetState_CornerEnabled write SetState_CornerEnabled;
property ShapeKind: TShapeSubKind read GetState_ShapeKind write SetState_ShapeKind;
procedure CopyTo(const ADest: IPCB_CustomShapeInfo);
function GetState_CornerEnabled(const ACorner: TRectCorner): Boolean;
function GetState_ShapeKind: TShapeSubKind;
function I_ObjectAddress: Pointer;
procedure SetState_CornerEnabled(const ACorner: TRectCorner; const AValue: Boolean);
procedure SetState_ShapeKind(const AValue: TShapeSubKind);

## IPCB_DRCBinaryResult
继承：IPCB_DRCBinaryResult → IPCB_DRCResult → IInterface ｜ 单元：RT_PCB ｜ 自有 1 个方法、1 个属性

property Prim2: IPCB_Primitive read GetState_Prim2;  // read-only
function GetState_Prim2: IPCB_Primitive;

## IPCB_DRCResult
继承：IPCB_DRCResult → IInterface ｜ 单元：RT_PCB ｜ 自有 8 个方法、6 个属性

property CheckResult: Integer read GetState_CheckResult;  // read-only
property IsBinary: Boolean read GetState_IsBinary;  // read-only
property Prim1: IPCB_Primitive read GetState_Prim1;  // read-only
property Rule: IPCB_Rule read GetState_Rule;  // read-only
property ScopeObjectID: WideString read GetState_ScopeObjectID;  // read-only
property Violation: IPCB_Violation read GetState_Violation;  // read-only
function GetState_CheckResult: Integer;
function GetState_IsBinary: Boolean;
function GetState_Prim1: IPCB_Primitive;
function GetState_Rule: IPCB_Rule;
function GetState_ScopeObjectID: WideString;
function GetState_ScopeObjectKind: TObjectId;
function GetState_ScopeObjectName: WideString;
function GetState_Violation: IPCB_Violation;

## IPCB_DRCResultAggregator
继承：IPCB_DRCResultAggregator → IInterface ｜ 单元：RT_PCB ｜ 自有 5 个方法、0 个属性

procedure BeginUpdate;
procedure ClearBinaryResults;
procedure EndUpdate;
procedure RegisterCheckNotificationHandler(const Handler: IRuleCheckNotificationHandler);
procedure UnregisterCheckNotificationHandler(const Handler: IRuleCheckNotificationHandler);

## IPCB_DRCResultSingleValue
继承：IPCB_DRCResultSingleValue → IPCB_DRCResult → IInterface ｜ 单元：RT_PCB ｜ 自有 1 个方法、1 个属性

property Value: Integer read GetState_Value;  // read-only
function GetState_Value: Integer;

## IPCB_DaisyChainStubLengthConstraint
继承：IPCB_DaisyChainStubLengthConstraint → IPCB_Rule → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 2 个方法、1 个属性

property Limit: TCoord read GetState_Limit write SetState_Limit;
function GetState_Limit: Integer;
procedure SetState_Limit(Value: Integer);

## IPCB_DatumDimension
继承：IPCB_DatumDimension → IPCB_Dimension → IPCB_Group → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 5 个方法、1 个属性

property Angle: TAngle read GetState_Angle write SetState_Angle;
function Extension_Track(I: Integer): IPCB_Track;
function GetState_Angle: Double;
procedure SetState_Angle(Value: Double);
function Text: IPCB_Text;
function Texts(I: Integer): IPCB_Text;

## IPCB_DesignRuleCheckerOptions
继承：IPCB_DesignRuleCheckerOptions → IPCB_AbstractOptions → IInterface ｜ 单元：RT_PCB ｜ 自有 29 个方法、12 个属性

property CheckExternalNetList: Boolean read GetState_CheckExternalNetList write SetState_CheckExternalNetList;
property DoMakeDRCErrorList: Boolean read GetState_DoMakeDRCErrorList write SetState_DoMakeDRCErrorList;
property DoMakeDRCFile: Boolean read GetState_DoMakeDRCFile write SetState_DoMakeDRCFile;
property DoSubNetDetails: Boolean read GetState_DoSubNetDetails write SetState_DoSubNetDetails;
property ExternalNetListFileName: TPCBString read GetState_ExternalNetListFileName write SetState_ExternalNetListFileName;
property IncludePCBHealth: Boolean read GetState_IncludePCBHealth write SetState_IncludePCBHealth;
property InternalPlaneWarnings: Boolean read GetState_InternalPlaneWarnings write SetState_InternalPlaneWarnings;
property MaxViolationCount: Integer read GetState_MaxViolationCount write SetState_MaxViolationCount;
property OnLineRuleSetToCheck: TRuleSet read GetState_OnLineRuleSetToCheck write SetState_OnLineRuleSetToCheck;
property ReportFilename: TPCBString read GetState_ReportFilename write SetState_ReportFilename;
property RuleSetToCheck: TRuleSet read GetState_RuleSetToCheck write SetState_RuleSetToCheck;
property VerifyShortingCopper: Boolean read GetState_VerifyShortingCopper write SetState_VerifyShortingCopper;
procedure Export_ToParameters_GeneralOptions(Parameters: PWideChar);
procedure Export_ToParameters_RulesToCheck(Parameters: PWideChar);
procedure Export_ToParameters_RulesToCheck_Version3(Parameters: PWideChar);
function GetState_CheckExternalNetList: Boolean;
function GetState_DoMakeDRCErrorList: Boolean;
function GetState_DoMakeDRCFile: Boolean;
function GetState_DoSubNetDetails: Boolean;
function GetState_ExternalNetListFileName: WideString;
function GetState_IncludePCBHealth: Boolean;
function GetState_InternalPlaneWarnings: Boolean;
function GetState_MaxViolationCount: Integer;
function GetState_OnLineRuleSetToCheck: TRuleSet;
function GetState_ReportFilename: WideString;
function GetState_RuleSetToCheck: TRuleSet;
function GetState_VerifyShortingCopper: Boolean;
procedure Import_FromParameters_GeneralOptions(Parameters: PWideChar);
procedure Import_FromParameters_RulesToCheck(Parameters: PWideChar);
procedure SetState_CheckExternalNetList(Value: Boolean);
procedure SetState_DoMakeDRCErrorList(Value: Boolean);
procedure SetState_DoMakeDRCFile(Value: Boolean);
procedure SetState_DoSubNetDetails(Value: Boolean);
procedure SetState_ExternalNetListFileName(Value: WideString);
procedure SetState_IncludePCBHealth(Value: Boolean);
procedure SetState_InternalPlaneWarnings(Value: Boolean);
procedure SetState_MaxViolationCount(Value: Integer);
procedure SetState_OnLineRuleSetToCheck(Value: TRuleSet);
procedure SetState_ReportFilename(Value: WideString);
procedure SetState_RuleSetToCheck(Value: TRuleSet);
procedure SetState_VerifyShortingCopper(Value: Boolean);

## IPCB_DesignVariant
继承：IPCB_DesignVariant → IInterface ｜ 单元：RT_PCB ｜ 自有 2 个方法、2 个属性

property Name: TPCBString read GetName;  // read-only
property VariantID: TPCBString read GetVariantID;  // read-only
function GetName: WideString;
function GetVariantID: WideString;

## IPCB_DesignVariants
继承：IPCB_DesignVariants → IInterface ｜ 单元：RT_PCB ｜ 自有 5 个方法、3 个属性

property Count: Integer read GetCount;  // read-only
property Current: IPCB_DesignVariant read GetCurrent;  // read-only
property DesignVariant[AIndex: Integer]: IPCB_DesignVariant read GetDesignVariant;  // read-only
function GetCount: Integer;
function GetCurrent: IPCB_DesignVariant;
function GetDesignVariant(AIndex: Integer): IPCB_DesignVariant;
function GetDesignVariantByID(const AVariantID: WideString): IPCB_DesignVariant;
function GetDesignVariantByName(const AVariantName: WideString): IPCB_DesignVariant;

## IPCB_DialogsManager
继承：IPCB_DialogsManager → IPCB_DialogsManagerEntry → IInterface ｜ 单元：RT_PCB ｜ 自有 0 个方法、0 个属性


## IPCB_DialogsManagerEntry
继承：IPCB_DialogsManagerEntry → IInterface ｜ 单元：RT_PCB ｜ 自有 6 个方法、0 个属性

function ShowBoardStackReportPropertiesDialog(const Settings: IBoardStackReportSettings): Boolean;
function ShowGerberPropertiesDialog(Settings: IGerberSettingsInfoBase): Boolean;
function ShowHealthCheckIssuesDialog(Board: IPCB_Board; Settings: IHealthCheckIssuesSettings): Boolean;
function ShowPrintOutPropertiesDialog(Settings: IPrintSettings): Boolean;
function ShowPrintPreviewDialog(Settings: IPrintSettings): Boolean;
function ShowSilkScreenDialog(const ABoard: IPCB_Board; const ASettings: IPCB_SilkscreenClipperSettings): Boolean;

## IPCB_DielectricLayer
继承：IPCB_DielectricLayer → IPCB_PhysicalLayer → IPCB_LayerObject → IInterface ｜ 单元：RT_PCB ｜ 自有 12 个方法、6 个属性

property DielectricConstant: TDouble read GetState_DielectricConstant write SetState_DielectricConstant;
property DielectricHeight: TCoord read GetState_DielectricHeight write SetState_DielectricHeight;
property DielectricLossTangent: TDouble read GetState_DielectricLossTangent write SetState_DielectricLossTangent;
property DielectricMaterial: TPCBString read GetState_DielectricMaterial write SetState_DielectricMaterial;
property DielectricType: TDielectricType read GetState_DielectricType write SetState_DielectricType;
property IsStiffener: Boolean read GetState_IsStiffener write SetState_IsStiffener;
function GetState_DielectricConstant: Double;
function GetState_DielectricHeight: Integer;
function GetState_DielectricLossTangent: Double;
function GetState_DielectricMaterial: WideString;
function GetState_DielectricType: TDielectricType;
function GetState_IsStiffener: Boolean;
procedure SetState_DielectricConstant(AValue: Double);
procedure SetState_DielectricHeight(AValue: Integer);
procedure SetState_DielectricLossTangent(AValue: Double);
procedure SetState_DielectricMaterial(AValue: WideString);
procedure SetState_DielectricType(AValue: TDielectricType);
procedure SetState_IsStiffener(AValue: Boolean);

## IPCB_DielectricObject
继承：IPCB_DielectricObject → IPCB_DielectricLayer → IPCB_PhysicalLayer → IPCB_LayerObject → IInterface ｜ 单元：RT_PCB ｜ 自有 0 个方法、0 个属性


## IPCB_DifferentialPair
继承：IPCB_DifferentialPair → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 9 个方法、4 个属性

property GatherControl: Boolean read GetState_GatherControl write SetState_GatherControl;
property Name: TPCBString read GetState_Name write SetState_Name;
property NegativeNet: IPCB_Net read GetState_NegativeNet write SetState_NegativeNet;
property PositiveNet: IPCB_Net read GetState_PositiveNet write SetState_PositiveNet;
function GetState_GatherControl: Boolean;
function GetState_Name: WideString;
function GetState_NegativeNet: IPCB_Net;
function GetState_PositiveNet: IPCB_Net;
procedure Reroute;
procedure SetState_GatherControl(Value: Boolean);
procedure SetState_Name(Value: WideString);
procedure SetState_NegativeNet(Value: IPCB_Net);
procedure SetState_PositiveNet(Value: IPCB_Net);

## IPCB_DifferentialPair2
继承：IPCB_DifferentialPair2 → IPCB_DifferentialPair → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 1 个方法、1 个属性

property PairAverageLength: TCoord read GetState_PairAverageLength;  // read-only
function GetState_PairAverageLength: Integer;

## IPCB_DifferentialPairsRoutingRule
继承：IPCB_DifferentialPairsRoutingRule → IPCB_Rule → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 37 个方法、12 个属性

property FavoredImpedance: TDouble read GetState_FavoredImpedance write SetState_FavoredImpedance;
property ImpedanceDriven: Boolean read GetState_ImpedanceDriven write SetState_ImpedanceDriven;
property ImpedanceProfileId: TPCBString read GetState_ImpedanceProfileId write SetState_ImpedanceProfileId;
property MaxGap[const L: Integer]: TCoord read GetState_MaxGap write SetState_MaxGap;
property MaxImpedance: TDouble read GetState_MaxImpedance write SetState_MaxImpedance;
property MaxUncoupledLength: TCoord read GetState_MaxUncoupledLength write SetState_MaxUncoupledLength;
property MaxWidth[const L: Integer]: TCoord read GetState_MaxWidth write SetState_MaxWidth;
property MinGap[const L: Integer]: TCoord read GetState_MinGap write SetState_MinGap;
property MinImpedance: TDouble read GetState_MinImpedance write SetState_MinImpedance;
property MinWidth[const L: Integer]: TCoord read GetState_MinWidth write SetState_MinWidth;
property PreferedGap[const L: Integer]: TCoord read GetState_PreferedGap write SetState_PreferedGap;
property PreferedWidth[const L: Integer]: TCoord read GetState_PreferedWidth write SetState_PreferedWidth;
function GetState_FavoredImpedance: Double;
function GetState_ImpedanceDriven: Boolean;
function GetState_ImpedanceProfileId: WideString;
function GetState_MaxGap(const L: Integer): Integer;
function GetState_MaxGapAtSubStack(const L: Integer; StackID: WideString): Integer;
function GetState_MaxImpedance: Double;
function GetState_MaxUncoupledLength: Integer;
function GetState_MaxWidth(const L: Integer): Integer;
function GetState_MaxWidthAtSubStack(const L: Integer; StackID: WideString): Integer;
function GetState_MinGap(const L: Integer): Integer;
function GetState_MinGapAtSubStack(const L: Integer; StackID: WideString): Integer;
function GetState_MinImpedance: Double;
function GetState_MinWidth(const L: Integer): Integer;
function GetState_MinWidthAtSubStack(const L: Integer; StackID: WideString): Integer;
function GetState_PreferedGap(const L: Integer): Integer;
function GetState_PreferedGapAtSubStack(const L: Integer; StackID: WideString): Integer;
function GetState_PreferedWidth(const L: Integer): Integer;
function GetState_PreferedWidthAtSubStack(const L: Integer; StackID: WideString): Integer;
procedure Invalidate;
procedure SetState_FavoredImpedance(Value: Double);
procedure SetState_ImpedanceDriven(Value: Boolean);
procedure SetState_ImpedanceProfileId(Value: WideString);
procedure SetState_MaxGap(const L: Integer; Value: Integer);
procedure SetState_MaxGapAtSubStack(const L: Integer; StackID: WideString; Value: Integer);
procedure SetState_MaxImpedance(Value: Double);
procedure SetState_MaxUncoupledLength(Value: Integer);
procedure SetState_MaxWidth(const L: Integer; Value: Integer);
procedure SetState_MaxWidthAtSubStack(const L: Integer; StackID: WideString; Value: Integer);
procedure SetState_MinGap(const L: Integer; Value: Integer);
procedure SetState_MinGapAtSubStack(const L: Integer; StackID: WideString; Value: Integer);
procedure SetState_MinImpedance(Value: Double);
procedure SetState_MinWidth(const L: Integer; Value: Integer);
procedure SetState_MinWidthAtSubStack(const L: Integer; StackID: WideString; Value: Integer);
procedure SetState_PreferedGap(const L: Integer; Value: Integer);
procedure SetState_PreferedGapAtSubStack(const L: Integer; StackID: WideString; Value: Integer);
procedure SetState_PreferedWidth(const L: Integer; Value: Integer);
procedure SetState_PreferedWidthAtSubStack(const L: Integer; StackID: WideString; Value: Integer);

## IPCB_DifferentialPairsRoutingRule2
继承：IPCB_DifferentialPairsRoutingRule2 → IPCB_DifferentialPairsRoutingRule → IPCB_Rule → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 7 个方法、3 个属性

property MaxGap[const L: TV6_Layer]: TCoord read GetState_MaxGap write SetState_MaxGap;
property MinGap[const L: TV6_Layer]: TCoord read GetState_MinGap write SetState_MinGap;
property PreferedGap[const L: TV6_Layer]: TCoord read GetState_PreferedGap write SetState_PreferedGap;
function GetState_MaxGap(const L: TV6_Layer): Integer;
function GetState_MinGap(const L: TV6_Layer): Integer;
function GetState_PreferedGap(const L: TV6_Layer): Integer;
procedure SetState_MaxGap(const L: TV6_Layer; Value: Integer);
procedure SetState_MaxUncoupledLength(Value: Integer);
procedure SetState_MinGap(const L: TV6_Layer; Value: Integer);
procedure SetState_PreferedGap(const L: TV6_Layer; Value: Integer);

## IPCB_Dimension
继承：IPCB_Dimension → IPCB_Group → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 74 个方法、33 个属性

property ArrowLength: TCoord read GetState_ArrowLength write SetState_ArrowLength;
property ArrowLineWidth: TCoord read GetState_ArrowLineWidth write SetState_ArrowLineWidth;
property ArrowPosition: TDimensionArrowPosition read GetState_ArrowPosition write SetState_ArrowPosition;
property ArrowSize: TCoord read GetState_ArrowSize write SetState_ArrowSize;
property Bold: Boolean read GetState_Bold write SetState_Bold;
property DimensionKind: TDimensionKind read GetState_DimensionKind write SetState_DimensionKind;
property ExtensionLineWidth: TCoord read GetState_ExtensionLineWidth write SetState_ExtensionLineWidth;
property ExtensionOffset: TCoord read GetState_ExtensionOffset write SetState_ExtensionOffset;
property ExtensionPickGap: TCoord read GetState_ExtensionPickGap write SetState_ExtensionPickGap;
property FontName: TPCBString read GetState_FontName write SetState_FontName;
property Italic: Boolean read GetState_Italic write SetState_Italic;
property LineWidth: TCoord read GetState_LineWidth write SetState_LineWidth;
property References[I: Integer]: TDimensionReference read GetState_References write SetState_References;
property References_Count: Integer read GetState_References_Count;  // read-only
property Size: TCoord read GetState_Size write SetState_Size;
property Style: TUnitStyle read GetState_Style write SetState_Style;
property TextDimensionUnit: TDimensionUnit read GetState_TextDimensionUnit write SetState_TextDimensionUnit;
property TextFont: TFontID read GetState_TextFont write SetState_TextFont;
property TextFormat: TPCBString read GetState_TextFormat write SetState_TextFormat;
property TextGap: TCoord read GetState_TextGap write SetState_TextGap;
property TextHeight: TCoord read GetState_TextHeight write SetState_TextHeight;
property TextLineWidth: TCoord read GetState_TextLineWidth write SetState_TextLineWidth;
property TextPosition: TDimensionTextPosition read GetState_TextPosition write SetState_TextPosition;
property TextPrecision: Integer read GetState_TextPrecision write SetState_TextPrecision;
property TextPrefix: TPCBString read GetState_TextPrefix write SetState_TextPrefix;
property TextSuffix: TPCBString read GetState_TextSuffix write SetState_TextSuffix;
property TextValue: TReal read GetState_TextValue write SetState_TextValue;
property TextWidth: TCoord read GetState_TextWidth write SetState_TextWidth;
property TextX: TCoord read GetState_TextX write SetState_TextX;
property TextY: TCoord read GetState_TextY write SetState_TextY;
property UseTTFonts: Boolean read GetState_UseTTFonts write SetState_UseTTFonts;
property X1Location: TCoord read GetState_X1Location write SetState_X1Location;
property Y1Location: TCoord read GetState_Y1Location write SetState_Y1Location;
function GetState_ArrowLength: Integer;
function GetState_ArrowLineWidth: Integer;
function GetState_ArrowPosition: TDimensionArrowPosition;
function GetState_ArrowSize: Integer;
function GetState_Bold: Boolean;
function GetState_DimensionKind: TDimensionKind;
function GetState_ExtensionLineWidth: Integer;
function GetState_ExtensionOffset: Integer;
function GetState_ExtensionPickGap: Integer;
function GetState_FontName: WideString;
function GetState_Italic: Boolean;
function GetState_LineWidth: Integer;
function GetState_References(I: Integer): IDispatch;
function GetState_References_Count: Integer;
function GetState_Size: Integer;
function GetState_Style: TUnitStyle;
function GetState_TextDimensionUnit: TDimensionUnit;
function GetState_TextFont: SmallInt;
function GetState_TextFormat: WideString;
function GetState_TextGap: Integer;
function GetState_TextHeight: Integer;
function GetState_TextLineWidth: Integer;
function GetState_TextPosition: TDimensionTextPosition;
function GetState_TextPrecision: Integer;
function GetState_TextPrefix: WideString;
function GetState_TextSuffix: WideString;
function GetState_TextValue: Double;
function GetState_TextWidth: Integer;
function GetState_TextX: Integer;
function GetState_TextY: Integer;
function GetState_UseTTFonts: Boolean;
function GetState_X1Location: Integer;
function GetState_Y1Location: Integer;
procedure MoveTextByXY(AX: Integer; AY: Integer);
procedure MoveTextToXY(AX: Integer; AY: Integer);
procedure References_Add(const r: IDispatch);
procedure References_Delete(Index: Integer);
procedure References_DeleteLast;
function References_IndexOf(P: IPCB_Primitive; Index: Integer): Integer;
function References_Validate: Boolean;
procedure ResetPrefixIfNeeded;
procedure RotateAroundXY(AX: Integer; AY: Integer; Angle: Double);
procedure SetState_ArrowLength(Value: Integer);
procedure SetState_ArrowLineWidth(Value: Integer);
procedure SetState_ArrowPosition(Value: TDimensionArrowPosition);
procedure SetState_ArrowSize(Value: Integer);
procedure SetState_Bold(Bold: Boolean);
procedure SetState_DimensionKind(Value: TDimensionKind);
procedure SetState_ExtensionLineWidth(Value: Integer);
procedure SetState_ExtensionOffset(Value: Integer);
procedure SetState_ExtensionPickGap(Value: Integer);
procedure SetState_FontName(FontName: WideString);
procedure SetState_Italic(Italic: Boolean);
procedure SetState_LineWidth(Value: Integer);
procedure SetState_References(I: Integer; const Value: IDispatch);
procedure SetState_Size(Value: Integer);
procedure SetState_Style(Value: TUnitStyle);
procedure SetState_TextDimensionUnit(Value: TDimensionUnit);
procedure SetState_TextFont(Value: SmallInt);
procedure SetState_TextFormat(Value: WideString);
procedure SetState_TextGap(Value: Integer);
procedure SetState_TextHeight(Value: Integer);
procedure SetState_TextLineWidth(Value: Integer);
procedure SetState_TextPosition(Value: TDimensionTextPosition);
procedure SetState_TextPrecision(Value: Integer);
procedure SetState_TextPrefix(Value: WideString);
procedure SetState_TextSuffix(Value: WideString);
procedure SetState_TextValue(Value: Double);
procedure SetState_TextWidth(Value: Integer);
procedure SetState_TextX(Value: Integer);
procedure SetState_TextY(Value: Integer);
procedure SetState_UseTTFonts(UseTTFonts: Boolean);
procedure SetState_X1Location(Value: Integer);
procedure SetState_Y1Location(Value: Integer);

## IPCB_DocumentPainterListener
继承：IPCB_DocumentPainterListener → IInterface ｜ 单元：RT_PCB ｜ 自有 10 个方法、0 个属性

function OnBeginDrag(const Prim: IPCB_Primitive; DegreeOfFreedom: TDegreeOfFreedom): Double;
procedure OnCalculateDragDisplacement(const Prim: IPCB_Primitive; DegreeOfFreedom: TDegreeOfFreedom; P: Pointer);
procedure OnClick(const Prim: IPCB_Primitive; DegreeOfFreedom: TDegreeOfFreedom);
procedure OnDegreeOfFreedomChanged(DegreeOfFreedom: TDegreeOfFreedom);
procedure OnDragging(const Prim: IPCB_Primitive; DegreeOfFreedom: TDegreeOfFreedom; Dist: Double);
procedure OnEndDrag(const Prim: IPCB_Primitive);
procedure OnPan(LookAtX: Double; LookAtY: Double; LookAtZ: Double);
procedure OnPrimitivesMeshed;
procedure OnRotate(RotationX: Double; RotationY: Double; RotationZ: Double; RotationW: Double);
procedure OnZoom(ZoomMultiplier: Double);

## IPCB_DocumentPainterView
继承：IPCB_DocumentPainterView → IInterface ｜ 单元：RT_PCB ｜ 自有 19 个方法、0 个属性

procedure AddOrUpdatePrim(const Prim: IPCB_Primitive);
procedure ClearSelection;
function ClientRect: IDispatch;
function FocusedPrimitive: IPCB_Primitive;
procedure FocusPrimitive(const Prim: IPCB_Primitive);
function GetState_ViewConfigAsString(out ConfigType: WideString; out Config: WideString): Boolean;
procedure KeyDown(var Key: Word; Shift: TShiftState);
function RunLayerConfigurationDialog: Boolean;
procedure SelectPrimitive(const Prim: IPCB_Primitive);
procedure SetBoard(const ABoard: IPCB_Board);
procedure SetBounds(ALeft: Integer; ATop: Integer; AWidth: Integer; AHeight: Integer);
procedure SetCameraAngle(LookAtX: Double; LookAtY: Double; LookAtZ: Double; RotationX: Double; RotationY: Double; RotationZ: Double; RotationW: Double; ZoomMultiplier: Double);
procedure SetDegreeOfFreedom(DegreeOfFreedom: TDegreeOfFreedom);
procedure SetDocumentPainterListener(const ACameraMoveListener: IPCB_DocumentPainterListener);
procedure SetInteractive(Value: LongBool);
function SetState_ViewConfigFromString(const ConfigType: WideString; const Config: WideString): Boolean;
procedure SetVariant(Variant: IProjectVariant);
procedure ShowFloorShadow(Enabled: LongBool);
procedure Zoom(Delta: Integer);

## IPCB_DrillLayerPair
继承：IPCB_DrillLayerPair → IInterface ｜ 单元：RT_PCB ｜ 自有 30 个方法、13 个属性

property Board: IPCB_Board read GetState_Board;  // read-only
property CounterHoleParams: IPCB_CounterHoleParams read GetProperty_Params;  // read-only
property Description: TPCBString read GetState_Description;  // read-only
property DrillLayerPairType: TDrillLayerPairType read GetState_DrillLayerPairType write SetState_DrillLayerPairType;
property HighLayer: TV6_Layer read GetState_HighLayer write SetState_HighLayer;
property Inverted: Boolean read GetState_Inverted write SetState_Inverted;
property IsBackdrill: Boolean read GetState_IsBackdrill write SetState_IsBackdrill;
property LowLayer: TV6_Layer read GetState_LowLayer write SetState_LowLayer;
property Name: TPCBString read GetState_Name;  // read-only
property PlotDrillDrawing: Boolean read GetState_PlotDrillDrawing write SetState_PlotDrillDrawing;
property PlotDrillGuide: Boolean read GetState_PlotDrillGuide write SetState_PlotDrillGuide;
property StartLayer: IPCB_LayerObject read GetState_StartLayer;  // read-only
property StopLayer: IPCB_LayerObject read GetState_StopLayer;  // read-only
procedure AddToSubstack(const StackID: WideString);
procedure DeleteFromAllSubstacks;
procedure DeleteFromSubstack(const StackID: WideString);
function GetProperty_Params: IPCB_CounterHoleParams;
function GetState_Board: IPCB_Board;
function GetState_Description: WideString;
function GetState_DrillLayerPairType: TDrillLayerPairType;
function GetState_HighLayer: TV6_Layer;
function GetState_Inverted: Boolean;
function GetState_IsBackdrill: Boolean;
function GetState_LowLayer: TV6_Layer;
function GetState_Name: WideString;
function GetState_PlotDrillDrawing: Boolean;
function GetState_PlotDrillGuide: Boolean;
function GetState_StartLayer: IPCB_LayerObject;
function GetState_StopLayer: IPCB_LayerObject;
function I_ObjectAddress: Pointer;
function IsCounterHole: Boolean;
function IsDefinedIn(const StackID: WideString): Boolean;
function IsSimilarTo(ADLP: IPCB_DrillLayerPair): Boolean;
procedure OrderLayers;
procedure SetState_DrillLayerPairType(Value: TDrillLayerPairType);
procedure SetState_HighLayer(L: TV6_Layer);
procedure SetState_Inverted(Value: Boolean);
procedure SetState_IsBackdrill(Value: Boolean);
procedure SetState_LowLayer(L: TV6_Layer);
procedure SetState_PlotDrillDrawing(Value: Boolean);
procedure SetState_PlotDrillGuide(Value: Boolean);
procedure Substacks_FromString(const Src: WideString);
function Substacks_ToString: WideString;

## IPCB_DrillTable
继承：IPCB_DrillTable → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 51 个方法、25 个属性

property DrillTableUnits: TUnit read GetState_DrillTableUnits write SetState_DrillTableUnits;
property Font: TFontID read GetState_Font write SetState_Font;
property IncludeFooter: Boolean read GetState_IncludeFooter write SetState_IncludeFooter;
property IncludeNonplatedPads: Boolean read GetState_IncludeNonplatedPads write SetState_IncludeNonplatedPads;
property IncludeNonslottedPads: Boolean read GetState_IncludeNonSlottedPads write SetState_IncludeNonSlottedPads;
property IncludePlatedPads: Boolean read GetState_IncludePlatedPads write SetState_IncludePlatedPads;
property IncludeSlottedPads: Boolean read GetState_IncludeSlottedPads write SetState_IncludeSlottedPads;
property IncludeTitle: Boolean read GetState_IncludeTitle write SetState_IncludeTitle;
property IncludeTitleDrillLayerPair: Boolean read GetState_IncludeTitleDrillLayerPair write SetState_IncludeTitleDrilllayerPair;
property IncludeTitleIncludedHoles: Boolean read GetState_IncludeTitleIncludedHoles write SetState_IncludeTitleIncludedHoles;
property IncludeTitlePlatingThickness: Boolean read GetState_IncludeTitlePlatingThickness write SetState_IncludeTitlePlatingThickness;
property IncludeVias: Boolean read GetState_IncludeVias write SetState_IncludeVias;
property LayerPair: IPCB_DrillLayerPair read GetState_LayerPair write SetState_LayerPair;
property LineWidth: TCoord read GetState_LineWidth write SetState_LineWidth;
property Mirror: Boolean read GetState_Mirror write SetState_Mirror;
property PlatingThickness: TCoord read GetState_PlatingThickness write SetState_PlatingThickness;
property SeparatePadsVias: Boolean read GetState_SeparatePadsVias write SetState_SeparatePadsVias;
property ShowColumnComment: Boolean read GetState_ShowColumnComment write SetState_ShowColumnComment;
property ShowColumnObjType: Boolean read GetState_ShowColumnObjType write SetState_ShowColumnObjType;
property ShowColumnTolerance: Boolean read GetState_ShowColumnTolerance write SetState_ShowColumnTolerance;
property ShowSecondaryUnits: Boolean read GetState_ShowSecondaryUnits write SetState_ShowSecondaryUnits;
property Size: TCoord read GetState_Size write SetState_Size;
property Width: TCoord read GetState_Width write SetState_Width;
property x: TCoord read GetState_X write SetState_X;
property y: TCoord read GetState_Y write SetState_Y;
function GetDrillTableGraphicIterator: IPCB_DrillTableGraphicIterator;
function GetState_DrillTableUnits: TUnit;
function GetState_Font: SmallInt;
function GetState_IncludeFooter: Boolean;
function GetState_IncludeNonplatedPads: Boolean;
function GetState_IncludeNonSlottedPads: Boolean;
function GetState_IncludePlatedPads: Boolean;
function GetState_IncludeSlottedPads: Boolean;
function GetState_IncludeTitle: Boolean;
function GetState_IncludeTitleDrillLayerPair: Boolean;
function GetState_IncludeTitleIncludedHoles: Boolean;
function GetState_IncludeTitlePlatingThickness: Boolean;
function GetState_IncludeVias: Boolean;
function GetState_LayerPair: IPCB_DrillLayerPair;
function GetState_LineWidth: Integer;
function GetState_Mirror: Boolean;
function GetState_PlatingThickness: Integer;
function GetState_SeparatePadsVias: Boolean;
function GetState_ShowColumnComment: Boolean;
function GetState_ShowColumnObjType: Boolean;
function GetState_ShowColumnTolerance: Boolean;
function GetState_ShowSecondaryUnits: Boolean;
function GetState_Size: Integer;
function GetState_Width: Integer;
function GetState_X: Integer;
function GetState_Y: Integer;
procedure SetState_DrillTableUnits(Value: TUnit);
procedure SetState_Font(Font: SmallInt);
procedure SetState_IncludeFooter(Value: Boolean);
procedure SetState_IncludeNonplatedPads(Value: Boolean);
procedure SetState_IncludeNonSlottedPads(Value: Boolean);
procedure SetState_IncludePlatedPads(Value: Boolean);
procedure SetState_IncludeSlottedPads(Value: Boolean);
procedure SetState_IncludeTitle(Value: Boolean);
procedure SetState_IncludeTitleDrilllayerPair(Value: Boolean);
procedure SetState_IncludeTitleIncludedHoles(Value: Boolean);
procedure SetState_IncludeTitlePlatingThickness(Value: Boolean);
procedure SetState_IncludeVias(Value: Boolean);
procedure SetState_LayerPair(LayerPair: IPCB_DrillLayerPair);
procedure SetState_LineWidth(Value: Integer);
procedure SetState_Mirror(Value: Boolean);
procedure SetState_PlatingThickness(Value: Integer);
procedure SetState_SeparatePadsVias(Value: Boolean);
procedure SetState_ShowColumnComment(Value: Boolean);
procedure SetState_ShowColumnObjType(Value: Boolean);
procedure SetState_ShowColumnTolerance(Value: Boolean);
procedure SetState_ShowSecondaryUnits(Value: Boolean);
procedure SetState_Size(Value: Integer);
procedure SetState_Width(Value: Integer);
procedure SetState_X(Value: Integer);
procedure SetState_Y(Value: Integer);

## IPCB_DrillTableGraphicIterator
继承：IPCB_DrillTableGraphicIterator → IInterface ｜ 单元：RT_PCB ｜ 自有 2 个方法、0 个属性

function First: IPCB_Primitive;
function Next: IPCB_Primitive;

## IPCB_DrillTableIterator
继承：IPCB_DrillTableIterator → IInterface ｜ 单元：RT_PCB ｜ 自有 2 个方法、0 个属性

function First: IPCB_DrillTable;
function Next: IPCB_DrillTable;

## IPCB_ECOOptions
继承：IPCB_ECOOptions → IPCB_AbstractOptions → IInterface ｜ 单元：RT_PCB ｜ 自有 4 个方法、2 个属性

property ECOFileName: TPCBString read GetState_ECOFileName write SetState_ECOFileName;
property ECOIsActive: Boolean read GetState_ECOIsActive write SetState_ECOIsActive;
function GetState_ECOFileName: WideString;
function GetState_ECOIsActive: Boolean;
procedure SetState_ECOFileName(ECOFileName: WideString);
procedure SetState_ECOIsActive(ECOActive: Boolean);

## IPCB_ElectricalLayer
继承：IPCB_ElectricalLayer → IPCB_PhysicalLayer → IPCB_LayerObject → IInterface ｜ 单元：RT_PCB ｜ 自有 2 个方法、1 个属性

property CopperThickness: TCoord read GetState_CopperThickness write SetState_CopperThickness;
function GetState_CopperThickness: Integer;
procedure SetState_CopperThickness(AValue: Integer);

## IPCB_ElectricalLayer2
继承：IPCB_ElectricalLayer2 → IPCB_PhysicalLayer → IPCB_LayerObject → IInterface ｜ 单元：RT_PCB ｜ 自有 2 个方法、1 个属性

property CopperOrientation: TCopperOrientation read GetState_CopperOrientation write SetState_CopperOrientation;
function GetState_CopperOrientation: TCopperOrientation;
procedure SetState_CopperOrientation(AValue: TCopperOrientation);

## IPCB_ElectricalLayerMapping
继承：IPCB_ElectricalLayerMapping → IInterface ｜ 单元：RT_PCB ｜ 自有 5 个方法、0 个属性

procedure FixPrimitiveLayerIfNeeded(const Primitive: IPCB_Primitive);
function GetDestLayerStack: IPCB_LayerStackBase;
function GetSourceLayerStack: IPCB_LayerStackBase;
function IsMappingNeeded: Boolean;
function TryMapLayerByPosition(const SourceLayer: Integer; out DestLayer: Integer): Boolean;

## IPCB_ElectricalParameters
继承：IPCB_ElectricalParameters → IInterface ｜ 单元：RT_PCB ｜ 自有 2 个方法、2 个属性

property Current: Double read GetState_Current;  // read-only
property Resistance: Double read GetState_Resistance;  // read-only
function GetState_Current: Double;
function GetState_Resistance: Double;

## IPCB_Embedded
继承：IPCB_Embedded → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 4 个方法、2 个属性

property Description: TPCBString read GetState_Description write SetState_Description;
property Name: TPCBString read GetState_Name write SetState_Name;
function GetState_Description: WideString;
function GetState_Name: WideString;
procedure SetState_Description(Value: WideString);
procedure SetState_Name(Value: WideString);

## IPCB_EmbeddedBoard
继承：IPCB_EmbeddedBoard → IPCB_RectangularPrimitive → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 42 个方法、16 个属性

property ChildBoard: IPCB_Board read GetState_ChildBoard;  // read-only
property ColCount: Integer read GetState_ColCount write SetState_ColCount;
property ColSpacing: TCoord read GetState_ColSpacing write SetState_ColSpacing;
property DocumentPath: TPCBString read GetState_DocumentPath write SetState_DocumentPath;
property MirrorFlag: Boolean read GetState_Mirror write SetState_Mirror;
property OriginMode: TEmbeddedBoardOriginMode read GetState_OriginMode write SetState_OriginMode;
property RowCount: Integer read GetState_RowCount write SetState_RowCount;
property RowSpacing: TCoord read GetState_RowSpacing write SetState_RowSpacing;
property TransmitBoardShape: Boolean read GetState_TransmitBoardShape write SetState_TransmitBoardShape;
property TransmitDimensions: Boolean read GetState_TransmitDimensions write SetState_TransmitDimensions;
property TransmitDrillTable: Boolean read GetState_TransmitDrillTable write SetState_TransmitDrillTable;
property TransmitLayersEnabled[Layer: Integer]: Boolean read GetState_TransmitLayersEnabled write SetState_TransmitLayersEnabled;
property TransmitLayerStackTable: Boolean read GetState_TransmitLayerStackTable write SetState_TransmitLayerStackTable;
property TransmitParametersCount: Integer read GetState_TransmitParametersCount;  // read-only
property TransmitParametersEnabled[Parameter: WideString]: Boolean read GetState_TransmitParametersEnabled write SetState_TransmitParametersEnabled;
property TransmitParametersName[Value: Integer]: TPCBString read GetState_TransmitParametersName;  // read-only
procedure ApplyFilterToIterator(const AIterator: IPCB_AbstractIterator);
function AreLayerStacksCompatible: LongBool;
function AreTransmitSettingsEqual(const AEmbeddedBoard: IPCB_EmbeddedBoard): Boolean;
function BoardIterator_CreateFiltered: IPCB_BoardIterator;
procedure BoardIterator_Destroy(var AIterator: IPCB_BoardIterator);
procedure CollectTransmitParameters;
function GetForbiddenParameterList: IPCB_ParameterList;
function GetState_ChildBoard: IPCB_Board;
function GetState_ColCount: Integer;
function GetState_ColMargin: Integer;
function GetState_ColSpacing: Integer;
function GetState_DocumentPath: WideString;
function GetState_Mirror: Boolean;
function GetState_OriginMode: TEmbeddedBoardOriginMode;
function GetState_RowCount: Integer;
function GetState_RowMargin: Integer;
function GetState_RowSpacing: Integer;
function GetState_TransmitBoardShape: Boolean;
function GetState_TransmitDimensions: Boolean;
function GetState_TransmitDrillTable: Boolean;
function GetState_TransmitLayersEnabled(Layer: Integer): Boolean;
function GetState_TransmitLayerStackTable: Boolean;
function GetState_TransmitParametersCount: Integer;
function GetState_TransmitParametersEnabled(Parameter: WideString): Boolean;
function GetState_TransmitParametersName(Value: Integer): WideString;
procedure SetState_ColCount(Value: Integer);
procedure SetState_ColMargin(Value: Integer);
procedure SetState_ColSpacing(Value: Integer);
procedure SetState_DocumentPath(Value: WideString);
procedure SetState_Mirror(Value: Boolean);
procedure SetState_OriginMode(Value: TEmbeddedBoardOriginMode);
procedure SetState_RowCount(Value: Integer);
procedure SetState_RowMargin(Value: Integer);
procedure SetState_RowSpacing(Value: Integer);
procedure SetState_TransmitBoardShape(Value: Boolean);
procedure SetState_TransmitDimensions(Value: Boolean);
procedure SetState_TransmitDrillTable(Value: Boolean);
procedure SetState_TransmitLayersEnabled(Layer: Integer; const Value: Boolean);
procedure SetState_TransmitLayerStackTable(Value: Boolean);
procedure SetState_TransmitParametersEnabled(Parameter: WideString; const Value: Boolean);
function SpatialIterator_CreateFiltered: IPCB_SpatialIterator;
procedure SpatialIterator_Destroy(var AIterator: IPCB_SpatialIterator);

## IPCB_ExpressionManager
继承：IPCB_ExpressionManager → IInterface ｜ 单元：RT_PCB ｜ 自有 6 个方法、0 个属性

function ExecRuleExpression(const Expression: WideString; Board: IPCB_Board; const RuleKind: TRuleKind; out AffectedObjects: Integer): Boolean;
function HighlightByExpression(Expression: WideString; Board: IPCB_Board; HighlightMethods: THighlightMethodSet): Boolean;
function IsExpressionValid(const Expression: WideString; const Board: IPCB_Board; out ErrLine: Integer; out ErrChar: Integer; out ErrMessage: WideString): Boolean;
function ShowExpressionBuilder(Board: IPCB_Board; out ResExpression: WideString): Boolean;
function ShowExpressionHelper(Expression: WideString; Board: IPCB_Board; out ResExpression: WideString): Boolean;
procedure ShowSmartEdit(SpecialString: WideString; EditedAtributeId: Integer; BoardCollection: IPCB_BoardCollection);

## IPCB_ExternalQueryExpressionForm
继承：IPCB_ExternalQueryExpressionForm → IInterface ｜ 单元：RT_PCB ｜ 自有 4 个方法、0 个属性

function GetState_QueryExpression: WideString;
function GetState_ReadOnly: Boolean;
procedure SetState_QueryExpression(AExpressin: WideString);
procedure SetState_ReadOnly(AValue: Boolean);

## IPCB_ExternalRuleForm
继承：IPCB_ExternalRuleForm → IInterface ｜ 单元：RT_PCB ｜ 自有 2 个方法、0 个属性

procedure ApplyRuleChanges;
procedure UpdateRuleState;

## IPCB_ExternalRuleHost
继承：IPCB_ExternalRuleHost → IInterface ｜ 单元：RT_PCB ｜ 自有 2 个方法、0 个属性

function GetRuleExternalForm(const ARule: IPCB_Rule): IExternalForm;
function GetRuleQueryExpressionForm(const ABoard: IPCB_Board): IExternalForm;

## IPCB_Factory
继承：IPCB_Factory → IInterface ｜ 单元：RT_PCB ｜ 自有 4 个方法、0 个属性

function AllLayers: IPCB_LayerSet;
function CreateElectricalLayerMapping(const SourceLayerStack: IPCB_LayerStackBase; const DestLayerStack: IPCB_LayerStackBase): IPCB_ElectricalLayerMapping;
function CreateLayerSet: IPCB_LayerSet;
function SignalLayers: IPCB_LayerSet;

## IPCB_FanoutControlRule
继承：IPCB_FanoutControlRule → IPCB_Rule → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 10 个方法、5 个属性

property BGAFanoutDirection: TBGAFanoutDirection read GetState_BGAFanoutDirection write SetState_BGAFanoutDirection;
property BGAFanoutViaMode: TBGAFanoutViaMode read GetState_BGAFanoutViaMode write SetState_BGAFanoutViaMode;
property FanoutDirection: TFanoutDirection read GetState_FanoutDirection write SetState_FanoutDirection;
property FanoutStyle: TFanoutStyle read GetState_FanoutStyle write SetState_FanoutStyle;
property ViaGrid: TCoord read GetState_ViaGrid write SetState_ViaGrid;
function GetState_BGAFanoutDirection: TBGAFanoutDirection;
function GetState_BGAFanoutViaMode: TBGAFanoutViaMode;
function GetState_FanoutDirection: TFanoutDirection;
function GetState_FanoutStyle: TFanoutStyle;
function GetState_ViaGrid: Integer;
procedure SetState_BGAFanoutDirection(Value: TBGAFanoutDirection);
procedure SetState_BGAFanoutViaMode(Value: TBGAFanoutViaMode);
procedure SetState_FanoutDirection(Value: TFanoutDirection);
procedure SetState_FanoutStyle(Value: TFanoutStyle);
procedure SetState_ViaGrid(Value: Integer);

## IPCB_Fill
继承：IPCB_Fill → IPCB_RectangularPrimitive → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 8 个方法、0 个属性

function GetState_Length: Integer;
function GetState_LocationX: Integer;
function GetState_LocationY: Integer;
function GetState_Width: Integer;
procedure SetState_Length(const ANewValue: Integer);
procedure SetState_LocationX(const ANewValue: Integer);
procedure SetState_LocationY(const ANewValue: Integer);
procedure SetState_Width(const ANewValue: Integer);

## IPCB_FromTo
继承：IPCB_FromTo → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 10 个方法、3 个属性

property FromPad: TPCBString read GetState_FromPad write SetState_FromPad;
property NetName: TPCBString read GetState_NetName write SetState_NetName;
property ToPad: TPCBString read GetState_ToPad write SetState_ToPad;
function GetFromPad: IPCB_Pad;
function GetNet: IPCB_Net;
function GetState_FromPad: WideString;
function GetState_NetName: WideString;
function GetState_RoutedLength: Integer;
function GetState_ToPad: WideString;
function GetToPad: IPCB_Pad;
procedure SetState_FromPad(Value: WideString);
procedure SetState_NetName(Value: WideString);
procedure SetState_ToPad(Value: WideString);

## IPCB_FullComponent
继承：IPCB_FullComponent → IInterface ｜ 单元：RT_PCB ｜ 自有 13 个方法、13 个属性

property Comment: TPCBString read GetComment;  // read-only
property ComponentID: TPCBString read GetComponentID;  // read-only
property Description: TPCBString read GetDescription;  // read-only
property Designator: TPCBString read GetDesignator;  // read-only
property DesignVariant: IPCB_DesignVariant read GetDesignVariant;  // read-only
property Footprint: IPCB_Component read GetFootprint;  // read-only
property ItemGUID: TPCBString read GetItemGUID;  // read-only
property Kind: TComponentKind read GetKind;  // read-only
property LibraryItemID: TPCBString read GetLibraryItemID;  // read-only
property LibraryName: TPCBString read GetLibraryName;  // read-only
property Parameters: IPCB_ParameterList read GetParameters;  // read-only
property RevisionGUID: TPCBString read GetRevisionGUID;  // read-only
property VaultGUID: TPCBString read GetVaultGUID;  // read-only
function GetComment: WideString;
function GetComponentID: WideString;
function GetDescription: WideString;
function GetDesignator: WideString;
function GetDesignVariant: IPCB_DesignVariant;
function GetFootprint: IPCB_Component;
function GetItemGUID: WideString;
function GetKind: TComponentKind;
function GetLibraryItemID: WideString;
function GetLibraryName: WideString;
function GetParameters: IPCB_ParameterList;
function GetRevisionGUID: WideString;
function GetVaultGUID: WideString;

## IPCB_FullComponentList
继承：IPCB_FullComponentList → IInterface ｜ 单元：RT_PCB ｜ 自有 2 个方法、2 个属性

property Count: Integer read GetCount;  // read-only
property Items[AIndex: Integer]: IPCB_FullComponent read GetItem;  // read-only
function GetCount: Integer;
function GetItem(AIndex: Integer): IPCB_FullComponent;

## IPCB_FullComponents
继承：IPCB_FullComponents → IInterface ｜ 单元：RT_PCB ｜ 自有 3 个方法、0 个属性

function GetComponents(const ADesignVariant: IPCB_DesignVariant): IPCB_FullComponentList;
function GetComponentsForAllVariants: IPCB_FullComponentList;
function GetComponentsForCurrentVariant: IPCB_FullComponentList;

## IPCB_GOMouseHoverHandler
继承：IPCB_GOMouseHoverHandler → IInterface ｜ 单元：RT_PCB ｜ 自有 1 个方法、0 个属性

procedure HandleMouseHoverEvent(GraphicalObject: Pointer);

## IPCB_GeometricPolygon
继承：IPCB_GeometricPolygon → IInterface ｜ 单元：RT_PCB ｜ 自有 10 个方法、5 个属性

property Area: Double read GetState_Area;  // read-only
property Contour[I: Integer]: IPCB_Contour read GetState_Contour;  // read-only
property Count: Integer read GetState_Count;  // read-only
property IsHole[I: Integer]: Boolean read GetState_IsHole write SetState_IsHole;
property Polygon: Pointer read GetState_Polygon;  // read-only
function AddContour(AContour: IPCB_Contour): IPCB_Contour;
function AddContourIsHole(AContour: IPCB_Contour; IsHole: Boolean): IPCB_Contour;
function AddEmptyContour: IPCB_Contour;
function GetState_Area: Double;
function GetState_Contour(I: Integer): IPCB_Contour;
function GetState_Count: Integer;
function GetState_IsHole(I: Integer): Boolean;
function GetState_Polygon: Pointer;
function Replicate: IPCB_GeometricPolygon;
procedure SetState_IsHole(I: Integer; Value: Boolean);

## IPCB_GeometryItem
继承：IPCB_GeometryItem → IInterface ｜ 单元：RT_PCB ｜ 自有 2 个方法、0 个属性

procedure GetAABB(out LowX: Single; out LowY: Single; out LowZ: Single; out HighX: Single; out HighY: Single; out HighZ: Single);
function GetLayerData(Layer: Integer; GType: TGeometryLayerType): IPCB_GeometryLayerData;

## IPCB_GeometryItems
继承：IPCB_GeometryItems → IInterface ｜ 单元：RT_PCB ｜ 自有 2 个方法、0 个属性

function Count: Integer;
function Item(Index: Integer): IPCB_GeometryItem;

## IPCB_GeometryLayerData
继承：IPCB_GeometryLayerData → IInterface ｜ 单元：RT_PCB ｜ 自有 8 个方法、0 个属性

procedure Arc(IsCutout: Boolean; Index: Integer; out CenterX: Single; out CenterY: Single; out AngleStart: Single; out AngleEnd: Single; out Radius: Single; out Width: Single; out LowZ: Integer; out HighZ: Integer; out ColorID: IPCB_ColorID);
function ArcCount(IsCutout: Boolean): Integer;
procedure Mesh(AIndex: Integer; out SrcBody: IPCB_3DBody; out Texture: IPCB_Texture; out m00: Single; out m01: Single; out m02: Single; out m03: Single; out m10: Single; out m11: Single; out m12: Single; out m13: Single; out m20: Single; out m21: Single; out m22: Single; out m23: Single; out m30: Single; out m31: Single; out m32: Single; out m33: Single);
function MeshCount: Integer;
procedure Poly(IsCutout: Boolean; Index: Integer; out CopperPoly: IPCB_CopperPolygon; out IsCore: Boolean; out Outline: Boolean; out m00: Single; out m01: Single; out m02: Single; out m10: Single; out m11: Single; out m12: Single; out m20: Single; out m21: Single; out m22: Single; out LowZ: Integer; out HighZ: Integer; out ColorID: IPCB_ColorID);
function PolyCount(IsCutout: Boolean): Integer;
procedure Uni(IsCutout: Boolean; Index: Integer; out PosX: Single; out PosY: Single; out DirX: Single; out DirY: Single; out SizeX: Single; out SizeY: Single; out Radius: Single; out LowZ: Integer; out HighZ: Integer; out ColorID: IPCB_ColorID);
function UniCount(IsCutout: Boolean): Integer;

## IPCB_GeometryMaker
继承：IPCB_GeometryMaker → IInterface ｜ 单元：RT_PCB ｜ 自有 5 个方法、2 个属性

property LayerMap: IPCB_GeometryMakerLayerMap read GetState_LayerMap write SetState_LayerMap;
property MaterialMap: IPCB_GeometryMakerMaterialMap read GetState_MaterialMap write SetState_MaterialMap;
function BuildGeometry(const APrim: IPCB_Primitive): IPCB_GeometryItems;
function GetState_LayerMap: IPCB_GeometryMakerLayerMap;
function GetState_MaterialMap: IPCB_GeometryMakerMaterialMap;
procedure SetState_LayerMap(AValue: IPCB_GeometryMakerLayerMap);
procedure SetState_MaterialMap(AValue: IPCB_GeometryMakerMaterialMap);

## IPCB_GeometryMakerLayerFilterLogic
继承：IPCB_GeometryMakerLayerFilterLogic → IInterface ｜ 单元：RT_PCB ｜ 自有 1 个方法、0 个属性

function DoFilter(const Layer: Integer; GType: TGeometryLayerType): Boolean;

## IPCB_GeometryMakerLayerMap
继承：IPCB_GeometryMakerLayerMap → IInterface ｜ 单元：RT_PCB ｜ 自有 5 个方法、1 个属性

property Count: Integer read GetCount;  // read-only
function GetCount: Integer;
function GetLayerInfo(AIndex: Integer; out ALayer: Integer; out AGeometryLayerType: TGeometryLayerType): Boolean;
function GetLayerZBottom(ALayer: Integer): Integer;
function GetLayerZTop(ALayer: Integer): Integer;
function GetZCoord(AZIndex: Integer): Integer;

## IPCB_GeometryMakerMaterialMap
继承：IPCB_GeometryMakerMaterialMap → IInterface ｜ 单元：RT_PCB ｜ 自有 3 个方法、0 个属性

function GetColorID(const Layer: Integer; GType: TGeometryLayerType; ObjectId: TObjectId; Hatching: TMaterialHatchStyle; Bordered: Boolean; ADRCState: TDRCState; ColorOverrideR: Byte; ColorOverrideG: Byte; ColorOverrideB: Byte; ColorOverrideA: Byte; const FilterLogic: IPCB_GeometryMakerLayerFilterLogic): IPCB_ColorID;
function GetState_ViewConfiguration: IInterface;
procedure SetState_ViewConfiguration(const AValue: IInterface);

## IPCB_GerberOptions
继承：IPCB_GerberOptions → IPCB_AbstractOptions → IInterface ｜ 单元：RT_PCB ｜ 自有 36 个方法、18 个属性

property AptTable: TPCBString read GetState_AptTable write SetState_AptTable;
property BorderSize: TCoord read GetState_BorderSize write SetState_BorderSize;
property CenterPhotoPlots: Boolean read GetState_CenterPhotoPlots write SetState_CenterPhotoPlots;
property EmbedApertures: Boolean read GetState_EmbedApertures write SetState_EmbedApertures;
property FilmSizeX: TCoord read GetState_FilmSizeX write SetState_FilmSizeX;
property FilmSizeY: TCoord read GetState_FilmSizeY write SetState_FilmSizeY;
property FlashAllFills: Boolean read GetState_FlashAllFills write SetState_FlashAllFills;
property G54: Boolean read GetState_G54 write SetState_G54;
property GerberDecs: Integer read GetState_GerberDecs write SetState_GerberDecs;
property GerberUnits: Integer read GetState_GerberUnits write SetState_GerberUnits;
property MaxAperSize: TCoord read GetState_MaxAperSize write SetState_MaxAperSize;
property MinusTol: TCoord read GetState_MinusTol write SetState_MinusTol;
property PadsFlashOnly: Boolean read GetState_PadsFlashOnly write SetState_PadsFlashOnly;
property Panelize: Boolean read GetState_Panelize write SetState_Panelize;
property PlusTol: TCoord read GetState_PlusTol write SetState_PlusTol;
property ReliefShapesAllowed: Boolean read GetState_ReliefShapesAllowed write SetState_ReliefShapesAllowed;
property SortOutput: Boolean read GetState_SortOutput write SetState_SortOutput;
property UseSoftwareArcs: Boolean read GetState_UseSoftwareArcs write SetState_UseSoftwareArcs;
function GetState_AptTable: WideString;
function GetState_BorderSize: Integer;
function GetState_CenterPhotoPlots: Boolean;
function GetState_EmbedApertures: Boolean;
function GetState_FilmSizeX: Integer;
function GetState_FilmSizeY: Integer;
function GetState_FlashAllFills: Boolean;
function GetState_G54: Boolean;
function GetState_GerberDecs: Integer;
function GetState_GerberUnits: Integer;
function GetState_MaxAperSize: Integer;
function GetState_MinusTol: Integer;
function GetState_PadsFlashOnly: Boolean;
function GetState_Panelize: Boolean;
function GetState_PlusTol: Integer;
function GetState_ReliefShapesAllowed: Boolean;
function GetState_SortOutput: Boolean;
function GetState_UseSoftwareArcs: Boolean;
procedure SetState_AptTable(Value: WideString);
procedure SetState_BorderSize(Value: Integer);
procedure SetState_CenterPhotoPlots(Value: Boolean);
procedure SetState_EmbedApertures(Value: Boolean);
procedure SetState_FilmSizeX(Value: Integer);
procedure SetState_FilmSizeY(Value: Integer);
procedure SetState_FlashAllFills(Value: Boolean);
procedure SetState_G54(Value: Boolean);
procedure SetState_GerberDecs(Value: Integer);
procedure SetState_GerberUnits(Value: Integer);
procedure SetState_MaxAperSize(Value: Integer);
procedure SetState_MinusTol(Value: Integer);
procedure SetState_PadsFlashOnly(Value: Boolean);
procedure SetState_Panelize(Value: Boolean);
procedure SetState_PlusTol(Value: Integer);
procedure SetState_ReliefShapesAllowed(Value: Boolean);
procedure SetState_SortOutput(Value: Boolean);
procedure SetState_UseSoftwareArcs(Value: Boolean);

## IPCB_GraphicalView
继承：IPCB_GraphicalView → IInterface ｜ 单元：RT_PCB ｜ 自有 30 个方法、0 个属性

procedure ClientToPCBLocation(const x: Integer; const y: Integer; out PX: Integer; out PY: Integer);
procedure CloseState_TemporaryWindow;
function GetExtents_Camera(out LookAtX: Single; out LookAtY: Single; out LookAtZ: Single; out Zoom: Double; out Width: Integer; out Height: Integer; const BoardFlipped: Boolean): Boolean;
function GetExtents_CameraIncludeComponents(out LookAtX: Single; out LookAtY: Single; out LookAtZ: Single; out Zoom: Double; out Width: Integer; out Height: Integer; const BoardFlipped: Boolean): Boolean;
function GetExtents_CameraIncludeComponentsExt(out LookAtX: Single; out LookAtY: Single; out LookAtZ: Single; out Zoom: Double; out Width: Integer; out Height: Integer; const BoardFlipped: Boolean; const AllLayers: Boolean; const SelectedObjects: Boolean): Boolean;
function GetState_AspectRatio: Single;
function GetState_Camera(out LookAtX: Single; out LookAtY: Single; out LookAtZ: Single; out QuatX: Single; out QuatY: Single; out QuatZ: Single; out QuatW: Single; out Zoom: Double): Boolean;
function GetState_CameraFov(out Fov: Single): Boolean;
function GetState_CameraUpVector(out UpX: Single; out UpY: Single; out UpZ: Single): Boolean;
function GetState_FoldingRate: Single;
function GetState_ViewMode: TPCBViewMode;
function GetState_ViewPortMils(out Width: Integer; out Height: Integer): Boolean;
function GetState_WindowSize(out Width: Integer; out Height: Integer): Boolean;
function HasPausedProcess: Boolean;
function HasRunningProcess: Boolean;
function InRoutingProcess: Boolean;
function Is3D: Boolean;
procedure PCBLocationToClient(const x: Integer; const y: Integer; out PX: Integer; out PY: Integer);
procedure RenderToDC(DC: NativeUInt; const ResX: Integer; const ResY: Integer; const DestRect: IDispatch; const SrcRect: IDispatch);
procedure RenderToDCTransparent(DC: NativeUInt; const ResX: Integer; const ResY: Integer; const DestRect: IDispatch; const SrcRect: IDispatch; const Transparent: Boolean);
procedure SetIs3D(AValue: Boolean);
function SetState_Camera(const LookAtX: Single; const LookAtY: Single; const LookAtZ: Single; const QuatX: Single; const QuatY: Single; const QuatZ: Single; const QuatW: Single; const Zoom: Double): Boolean;
function SetState_CameraFov(const Fov: Single): Boolean;
function SetState_CameraUpVector(const UpX: Single; const UpY: Single; const UpZ: Single): Boolean;
procedure SetState_FoldingRate(Value: Single);
procedure SetState_FoldingRateWithAnimation(Value: Single);
function SetState_TemporaryWindow(Width: Integer; Height: Integer): Boolean;
procedure SetState_ViewMode(Value: TPCBViewMode);
function SetState_ViewPortMils(const Width: Integer; const Height: Integer): Boolean;
procedure ZoomBoard;

## IPCB_GraphicalView3D
继承：IPCB_GraphicalView3D → IInterface ｜ 单元：RT_PCB ｜ 自有 1 个方法、0 个属性

procedure ClientToRay(x: Integer; y: Integer; out OrigX: Single; out OrigY: Single; out OrigZ: Single; out DirX: Single; out DirY: Single; out DirZ: Single);

## IPCB_GridManager
继承：IPCB_GridManager → IInterface ｜ 单元：RT_PCB ｜ 自有 22 个方法、0 个属性

function AddCartesianGrid: IPCB_CartesianGrid;
function AddMCADCartesianGrid: IPCB_CartesianGrid;
function AddMCADPolarGrid: IPCB_PolarGrid;
function AddPolarGrid: IPCB_PolarGrid;
procedure BeginUpdate;
function CanDecrementGridPriority(const AGrid: IPCB_PlacementGrid): Boolean;
function CanIncrementGridPriority(const AGrid: IPCB_PlacementGrid): Boolean;
function CreatePlacementGridIterator: IPCB_PlacementGridIterator;
function CreateRealPlacementGuideIterator: IPCB_RealPlacementGuideIterator;
function DecrementGridPriority(const AGrid: IPCB_PlacementGrid): Boolean;
procedure DeleteAllGrids;
procedure DeleteAllGuides;
procedure DeleteAllMCADGrids;
function DeleteGrid(const AGrid: IPCB_PlacementGrid): Boolean;
function DeleteGuide(const AGuide: IPCB_PlacementGuide): Boolean;
procedure EndUpdate;
function FindApplicableGrid(APrimitive: IPCB_Primitive): IPCB_PlacementGrid;
function FindApplicableGridByXY(AX: Integer; AY: Integer): IPCB_PlacementGrid;
function IncrementGridPriority(const AGrid: IPCB_PlacementGrid): Boolean;
procedure NextStateID;
procedure ResolveGridPriorities;
function RunGridEditor(const ABoard: IPCB_Board; const AGrid: IPCB_PlacementGrid): Boolean;

## IPCB_GridManagerPcbLib
继承：IPCB_GridManagerPcbLib → IPCB_GridManager → IInterface ｜ 单元：RT_PCB ｜ 自有 2 个方法、0 个属性

function GetIsLibComponentGridnGuide(const AGrid: IPCB_PlacementGuide): Boolean;
procedure SetIsLibComponentGridnGuide(const AGrid: IPCB_PlacementGuide; AValue: Boolean);

## IPCB_Group
继承：IPCB_Group → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 19 个方法、4 个属性

property LayerUsed[L: TV6_Layer]: Boolean read GetState_LayerUsed write SetState_LayerUsed;
property PrimitiveLock: Boolean read GetState_PrimitiveLock write SetState_PrimitiveLock;
property x: TCoord read GetState_XLocation write SetState_XLocation;
property y: TCoord read GetState_YLocation write SetState_YLocation;
procedure AddPCBObject(PCBObject: IPCB_Primitive);
function FastSetState_XSizeYSize: Boolean;
procedure FreePrimitives;
function GetPrimitiveAt(I: Integer; ObjectId: TObjectId): IPCB_Primitive;
function GetPrimitiveCount(ObjectSet: TObjectSet): Integer;
function GetState_LayerUsed(L: TV6_Layer): Boolean;
function GetState_PrimitiveLock: Boolean;
function GetState_XLocation: Integer;
function GetState_YLocation: Integer;
function GroupIterator_Create: IPCB_GroupIterator;
procedure GroupIterator_Destroy(var AIterator: IPCB_GroupIterator);
procedure RemovePCBObject(PCBObject: IPCB_Primitive);
function ReplicateWithChildren: IPCB_Primitive;
procedure SetState_LayersUsedArray;
procedure SetState_LayerUsed(L: TV6_Layer; Value: Boolean);
procedure SetState_PrimitiveLock(Value: Boolean);
procedure SetState_XLocation(AX: Integer);
function SetState_XSizeYSize: Boolean;
procedure SetState_YLocation(AY: Integer);

## IPCB_Group3D
继承：IPCB_Group3D → IPCB_Group → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 1 个方法、0 个属性

function TryProjectPointToSurface(AX: Integer; AY: Integer; out AU: Integer; out AV: Integer; out AFaceIdx: Integer): Boolean;

## IPCB_GroupComparisionResult
继承：IPCB_GroupComparisionResult → IInterface ｜ 单元：RT_PCB ｜ 自有 19 个方法、3 个属性

property GroupFootprintsMatch: Boolean read GetGroupFootprintsMatch;  // read-only
property HasAttributeDifferencesAllLayers: Boolean read GetHasAttributeDifferencesAllLayers;  // read-only
property NumberOfCells: Integer read GetNumberOfCells;  // read-only
function GetAffectedFootprintParameters: IInterfaceList;
function GetFootprintParameterDifference(Index: Integer): WideString;
function GetFootprintParameterDifferenceCount: Integer;
function GetGroupFootprintsMatch: Boolean;
function GetHasAttributeDifferencesAllLayers: Boolean;
function GetNumberOfCells: Integer;
function GetPrimitiveBoundingRectangleForLayer(Layer: Integer; PrimIndex: Integer; var LowX: Integer; var LowY: Integer; var HighX: Integer; var HighY: Integer): Boolean;
function GetPrimitiveCountForGraphicalObject(GraphicalObject: Pointer): Integer;
function GetPrimitiveCountForLayer(Layer: Integer): Integer;
function GetPrimitiveCountForLayerOnlyVisual(Layer: Integer): Integer;
function GetPrimitiveDescriptorForGraphicalObject(GraphicalObject: Pointer; PrimIndex: Integer): string;
function GetPrimitiveDescriptorForLayer(Layer: Integer; PrimIndex: Integer): string;
function GetPrimitiveForGraphicalObject(GraphicalObject: Pointer; PrimIndex: Integer): IPCB_Primitive;
function GetPrimitiveForLayer(Layer: Integer; PrimIndex: Integer): IPCB_Primitive;
function GetPrimitiveHasDiffsForLayer(Layer: Integer; PrimIndex: Integer): Boolean;
function GetTotalLayerSet: IPCB_LayerSet;
function LayerContainsDifferences(Layer: Integer): Boolean;
procedure SetGroupHighlightLayer(Layer: Integer);
procedure SetInView;

## IPCB_GroupEx
继承：IPCB_GroupEx → IPCB_Group → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 2 个方法、0 个属性

procedure CancelGroupWarehouseRegistration(const APrimitive: IPCB_Primitive);
procedure RegisterWithGroupWarehouse(const APrimitive: IPCB_Primitive);

## IPCB_GroupIterator
继承：IPCB_GroupIterator → IPCB_AbstractIterator → IInterface ｜ 单元：RT_PCB ｜ 自有 0 个方法、0 个属性


## IPCB_HealthCheckAbsentTTFontsRecord
继承：IPCB_HealthCheckAbsentTTFontsRecord → IPCB_HealthCheckRecord → IInterface ｜ 单元：RT_PCB ｜ 自有 2 个方法、0 个属性

function GetCount: Integer;
function GetFontName(APos: Integer): WideString;

## IPCB_HealthCheckFromToRecord
继承：IPCB_HealthCheckFromToRecord → IPCB_HealthCheckPrimitiveRecord → IPCB_HealthCheckRecord → IInterface ｜ 单元：RT_PCB ｜ 自有 1 个方法、0 个属性

function GetIdentifier: WideString;

## IPCB_HealthCheckManager
继承：IPCB_HealthCheckManager → IPCB_HealthCheckManagerObservable → IInterface ｜ 单元：RT_PCB ｜ 自有 3 个方法、0 个属性

function GetHealthChecksStorage: IPCB_HealthChecksStorage;
function GetHealthCheckTypeTrait(AHealthCheckId: THealthCheckId): IPCB_HealthCheckTypeTrait;
procedure ResendLastResults(AHealthCheckId: THealthCheckId);

## IPCB_HealthCheckManagerFactory
继承：IPCB_HealthCheckManagerFactory → IInterface ｜ 单元：RT_PCB ｜ 自有 2 个方法、0 个属性

function GetHealthCheckManager: IPCB_HealthCheckManager;
procedure SetBoard(ABoard: IPCB_Primitive);

## IPCB_HealthCheckManagerObservable
继承：IPCB_HealthCheckManagerObservable → IInterface ｜ 单元：RT_PCB ｜ 自有 2 个方法、0 个属性

procedure AddObserver(const AHealthCheckManagerObserver: IPCB_HealthCheckManagerObserver);
procedure RemoveObserver(const AHealthCheckManagerObserver: IPCB_HealthCheckManagerObserver);

## IPCB_HealthCheckManagerObserver
继承：IPCB_HealthCheckManagerObserver → IInterface ｜ 单元：RT_PCB ｜ 自有 5 个方法、0 个属性

procedure OnAddRecord(const AHealthCheckRecord: IPCB_HealthCheckRecord);
procedure OnCancelled(AHealthCheckId: THealthCheckId);
procedure OnDone(AHealthCheckId: THealthCheckId);
procedure OnReportProgress(AHealthCheckId: THealthCheckId; ACurrentCount: Integer; ATotalCount: Integer);
procedure OnStart(AHealthCheckId: THealthCheckId);

## IPCB_HealthCheckMicrosegmentsRecord
继承：IPCB_HealthCheckMicrosegmentsRecord → IPCB_HealthCheckPrimitiveRecord → IPCB_HealthCheckRecord → IInterface ｜ 单元：RT_PCB ｜ 自有 2 个方法、0 个属性

function GetCount: Integer;
function GetSegment(APos: Integer): IDispatch;

## IPCB_HealthCheckPinPairRecord
继承：IPCB_HealthCheckPinPairRecord → IPCB_HealthCheckPrimitiveRecord → IPCB_HealthCheckRecord → IInterface ｜ 单元：RT_PCB ｜ 自有 1 个方法、0 个属性

function GetDescription: WideString;

## IPCB_HealthCheckPrimitiveRecord
继承：IPCB_HealthCheckPrimitiveRecord → IPCB_HealthCheckRecord → IInterface ｜ 单元：RT_PCB ｜ 自有 1 个方法、0 个属性

function GetPrimitive: IPCB_Primitive;

## IPCB_HealthCheckRecord
继承：IPCB_HealthCheckRecord → IInterface ｜ 单元：RT_PCB ｜ 自有 2 个方法、0 个属性

function GetCheckId: THealthCheckId;
function GetViolationsCount: Integer;

## IPCB_HealthCheckRecordFixer
继承：IPCB_HealthCheckRecordFixer → IInterface ｜ 单元：RT_PCB ｜ 自有 2 个方法、0 个属性

function Fix: Boolean;
function IsUndoRedoHandledByImpl: Boolean;

## IPCB_HealthCheckRecordRepresentation
继承：IPCB_HealthCheckRecordRepresentation → IInterface ｜ 单元：RT_PCB ｜ 自有 3 个方法、0 个属性

function GetHealthCheckRecord: IPCB_HealthCheckRecord;
function GetViolationCoordPoint(Index: Integer; const Coord: IDispatch): Boolean;
function GetViolationDescription(Index: Integer): WideString;

## IPCB_HealthCheckRuleRecord
继承：IPCB_HealthCheckRuleRecord → IPCB_HealthCheckPrimitiveRecord → IPCB_HealthCheckRecord → IInterface ｜ 单元：RT_PCB ｜ 自有 1 个方法、0 个属性

function GetRule: IPCB_Rule;

## IPCB_HealthCheckSelfIntersectionsRecord
继承：IPCB_HealthCheckSelfIntersectionsRecord → IPCB_HealthCheckPrimitiveRecord → IPCB_HealthCheckRecord → IInterface ｜ 单元：RT_PCB ｜ 自有 2 个方法、0 个属性

function GetCount: Integer;
function GetPoint(APos: Integer): IDispatch;

## IPCB_HealthCheckTypeTrait
继承：IPCB_HealthCheckTypeTrait → IInterface ｜ 单元：RT_PCB ｜ 自有 6 个方法、0 个属性

function GetHealthCheckDescription: WideString;
function GetHealthCheckRecordRepresentation(const AHealthCheckRecord: IPCB_HealthCheckRecord): IPCB_HealthCheckRecordRepresentation;
function IsFixable: Boolean;
function IsHealthCheckActive: Boolean;
function IsNavigatable: Boolean;
procedure NavigateTo(const ARecord: IPCB_HealthCheckRecord; APos: Integer);

## IPCB_HealthChecksStorage
继承：IPCB_HealthChecksStorage → IInterface ｜ 单元：RT_PCB ｜ 自有 5 个方法、0 个属性

procedure Deserialize(ASerializedStr: WideString);
function GetHealthCheckEnabled(AID: THealthCheckId): Boolean;
function IsDefault: Boolean;
function Serialize: WideString;
procedure SetHealthCheckEnabled(AID: THealthCheckId; AEnabled: Boolean);

## IPCB_HoleToHoleClearanceRule
继承：IPCB_HoleToHoleClearanceRule → IPCB_Rule → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 4 个方法、2 个属性

property AllowStackedMicroVias: Boolean read GetState_AllowStackedMicroVias write SetState_AllowStackedMicroVias;
property Gap: TCoord read GetState_Gap write SetState_Gap;
function GetState_AllowStackedMicroVias: Boolean;
function GetState_Gap: Integer;
procedure SetState_AllowStackedMicroVias(Value: Boolean);
procedure SetState_Gap(Value: Integer);

## IPCB_ImpedanceProfile
继承：IPCB_ImpedanceProfile → IInterface ｜ 单元：RT_PCB ｜ 自有 20 个方法、8 个属性

property DisplayName: TPCBString read GetState_DisplayName write SetState_DisplayName;
property Id: TPCBString read GetState_ID;  // read-only
property Impedance: TDouble read GetState_Impedance write SetState_Impedance;
property ImpedanceTolerance: TDouble read GetState_ImpedanceTolerance write SetState_ImpedanceTolerance;
property IsCoplanar: Boolean read GetState_IsCoplanar write SetState_IsCoplanar;
property IsDiffPair: Boolean read GetState_IsDiffPair write SetState_IsDiffPair;
property MasterLayerStack: IPCB_MasterLayerStack read GetState_MasterLayerStack;  // read-only
property Name: TPCBString read GetState_Name write SetState_Name;
function CreateTraceImpedance(Substack: IPCB_LayerStack; Layer: Integer): IPCB_TraceImpedance;
function GetState_DisplayName: WideString;
function GetState_ID: WideString;
function GetState_Impedance: Double;
function GetState_ImpedanceTolerance: Double;
function GetState_IsCoplanar: Boolean;
function GetState_IsDiffPair: Boolean;
function GetState_MasterLayerStack: IPCB_MasterLayerStack;
function GetState_Name: WideString;
function GetTraceImpedanceByIndex(Index: Integer): IPCB_TraceImpedance;
function GetTraceImpedanceCount: Integer;
function GetTraceImpedanceForLayer(Substack: IPCB_LayerStack; Layer: Integer): IPCB_TraceImpedance;
function I_ObjectAddress: Pointer;
function RemoveTraceImpedance(TraceImpedance: IPCB_TraceImpedance): Boolean;
procedure SetState_DisplayName(Value: WideString);
procedure SetState_Impedance(Value: Double);
procedure SetState_ImpedanceTolerance(Value: Double);
procedure SetState_IsCoplanar(Value: Boolean);
procedure SetState_IsDiffPair(Value: Boolean);
procedure SetState_Name(Value: WideString);

## IPCB_InteractiveDiffPairRoutingProcess
继承：IPCB_InteractiveDiffPairRoutingProcess → IPCB_CustomInteractiveRoutingProcess → IPCB_InteractiveProcess → IInteractiveProcess ｜ 单元：RT_PCB ｜ 自有 8 个方法、2 个属性

property DifferentialPair: IPCB_DifferentialPair read GetState_DifferentialPair;  // read-only
property GapMode: TRoutingDiffPairGapMode read GetState_GapMode write SetState_GapMode;
function GetState_DifferentialPair: IPCB_DifferentialPair;
function GetState_DiffPairRule: IPCB_DifferentialPairsRoutingRule;
function GetState_GapMode: TRoutingDiffPairGapMode;
function GetState_ShowLengthGauge: Boolean;
function NextGapMode: TRoutingDiffPairGapMode;
function ProjectAvailableForPinSwap(out AErrorMessage: WideString): Boolean;
procedure SetState_GapMode(AValue: TRoutingDiffPairGapMode);
procedure SetState_ShowLengthGauge(AValue: Boolean);

## IPCB_InteractiveLineRoutingProcess
继承：IPCB_InteractiveLineRoutingProcess → IPCB_InteractiveProcess → IInteractiveProcess ｜ 单元：RT_PCB ｜ 自有 5 个方法、3 个属性

property CurrentLayer: TLayer read GetState_CurrentLayer write SetState_CurrentLayer;
property LineWidth: Integer read GetState_LineWidth write SetState_LineWidth;
property PlacingKeepOuts: Boolean read GetState_PlacingKeepOuts;  // read-only
function GetState_CurrentLayer: Integer;
function GetState_LineWidth: Integer;
function GetState_PlacingKeepOuts: Boolean;
procedure SetState_CurrentLayer(const AValue: Integer);
procedure SetState_LineWidth(AValue: Integer);

## IPCB_InteractiveMultiRoutingProcess
继承：IPCB_InteractiveMultiRoutingProcess → IPCB_CustomInteractiveRoutingProcess → IPCB_InteractiveProcess → IInteractiveProcess ｜ 单元：RT_PCB ｜ 自有 5 个方法、0 个属性

procedure EditMaxMinWidthRule;
function GetState_BusSpacing: Integer;
function GetState_GetMinClearanceFromRule: Integer;
function GetState_WidthRule: IPCB_MaxMinWidthConstraint;
procedure SetState_BusSpacing(const ANewValue: Integer);

## IPCB_InteractiveProcess
继承：IPCB_InteractiveProcess → IInteractiveProcess ｜ 单元：RT_PCB ｜ 自有 1 个方法、0 个属性

function GetState_Board: IPCB_Board;

## IPCB_InteractiveRoutingOptions
继承：IPCB_InteractiveRoutingOptions → IPCB_AbstractOptions → IInterface ｜ 单元：RT_PCB ｜ 自有 53 个方法、25 个属性

property Beginx: TCoord read GetState_Beginx write SetState_Beginx;
property Beginy: TCoord read GetState_Beginy write SetState_Beginy;
property EndLineX: TCoord read GetState_EndLineX write SetState_EndLineX;
property EndLineY: TCoord read GetState_EndLineY write SetState_EndLineY;
property Midx: TCoord read GetState_Midx write SetState_Midx;
property MidY: TCoord read GetState_MidY write SetState_MidY;
property OldCx: TCoord read GetState_OldCx write SetState_OldCx;
property OldCy: TCoord read GetState_OldCy write SetState_OldCy;
property OldMidx: TCoord read GetState_OldMidx write SetState_OldMidx;
property OldMidy: TCoord read GetState_OldMidy write SetState_OldMidy;
property OldTrackArcAngle1: TCoord read GetState_OldTrackArcAngle1 write SetState_OldTrackArcAngle1;
property OldTrackArcAngle2: TCoord read GetState_OldTrackArcAngle2 write SetState_OldTrackArcAngle2;
property OldTrackArcRadius: TCoord read GetState_OldTrackArcRadius write SetState_OldTrackArcRadius;
property OldTrackArcX: TCoord read GetState_OldTrackArcX write SetState_OldTrackArcX;
property OldTrackArcY: TCoord read GetState_OldTrackArcY write SetState_OldTrackArcY;
property OldTrackDrawLayer: TV6_Layer read GetState_OldTrackDrawLayer write SetState_OldTrackDrawLayer;
property OldTrackDrawSize: TCoord read GetState_OldTrackDrawSize write SetState_OldTrackDrawSize;
property PlaceTrackMode: TPlaceTrackMode read GetState_PlaceTrackMode write SetState_PlaceTrackMode;
property StartX: TCoord read GetState_StartX write SetState_StartX;
property StartY: TCoord read GetState_StartY write SetState_StartY;
property TrackArcAngle1: TCoord read GetState_TrackArcAngle1 write SetState_TrackArcAngle1;
property TrackArcAngle2: TCoord read GetState_TrackArcAngle2 write SetState_TrackArcAngle2;
property TrackArcRadius: TCoord read GetState_TrackArcRadius write SetState_TrackArcRadius;
property TrackArcX: TCoord read GetState_TrackArcX write SetState_TrackArcX;
property TrackArcY: TCoord read GetState_TrackArcY write SetState_TrackArcY;
procedure Export_ToParameters_GeneralOptions(Parameters: PWideChar);
procedure Export_ToParameters_LayerOptions(Parameters: PWideChar);
procedure Export_ToParameters_LayerOptions_Version3(Parameters: PWideChar);
function GetState_Beginx: Integer;
function GetState_Beginy: Integer;
function GetState_EndLineX: Integer;
function GetState_EndLineY: Integer;
function GetState_Midx: Integer;
function GetState_MidY: Integer;
function GetState_OldCx: Integer;
function GetState_OldCy: Integer;
function GetState_OldMidx: Integer;
function GetState_OldMidy: Integer;
function GetState_OldTrackArcAngle1: Integer;
function GetState_OldTrackArcAngle2: Integer;
function GetState_OldTrackArcRadius: Integer;
function GetState_OldTrackArcX: Integer;
function GetState_OldTrackArcY: Integer;
function GetState_OldTrackDrawLayer: TV6_Layer;
function GetState_OldTrackDrawSize: Integer;
function GetState_PlaceTrackMode: TPlaceTrackMode;
function GetState_StartX: Integer;
function GetState_StartY: Integer;
function GetState_TrackArcAngle1: Integer;
function GetState_TrackArcAngle2: Integer;
function GetState_TrackArcRadius: Integer;
function GetState_TrackArcX: Integer;
function GetState_TrackArcY: Integer;
procedure SetState_Beginx(Value: Integer);
procedure SetState_Beginy(Value: Integer);
procedure SetState_EndLineX(Value: Integer);
procedure SetState_EndLineY(Value: Integer);
procedure SetState_Midx(Value: Integer);
procedure SetState_MidY(Value: Integer);
procedure SetState_OldCx(Value: Integer);
procedure SetState_OldCy(Value: Integer);
procedure SetState_OldMidx(Value: Integer);
procedure SetState_OldMidy(Value: Integer);
procedure SetState_OldTrackArcAngle1(Value: Integer);
procedure SetState_OldTrackArcAngle2(Value: Integer);
procedure SetState_OldTrackArcRadius(Value: Integer);
procedure SetState_OldTrackArcX(Value: Integer);
procedure SetState_OldTrackArcY(Value: Integer);
procedure SetState_OldTrackDrawLayer(Value: TV6_Layer);
procedure SetState_OldTrackDrawSize(Value: Integer);
procedure SetState_PlaceTrackMode(Value: TPlaceTrackMode);
procedure SetState_StartX(Value: Integer);
procedure SetState_StartY(Value: Integer);
procedure SetState_TrackArcAngle1(Value: Integer);
procedure SetState_TrackArcAngle2(Value: Integer);
procedure SetState_TrackArcRadius(Value: Integer);
procedure SetState_TrackArcX(Value: Integer);
procedure SetState_TrackArcY(Value: Integer);

## IPCB_InteractiveRoutingProcess
继承：IPCB_InteractiveRoutingProcess → IPCB_CustomInteractiveRoutingProcess → IPCB_InteractiveProcess → IInteractiveProcess ｜ 单元：RT_PCB ｜ 自有 8 个方法、2 个属性

property Impedance: Double read GetState_Impedance;  // read-only
property ShowLengthGauge: Boolean read GetState_ShowLengthGauge write SetState_ShowLengthGauge;
procedure EditMaxMinWidthRule;
function GetState_DifferentialPair: IPCB_DifferentialPair;
function GetState_DiffPairRule: IPCB_DifferentialPairsRoutingRule;
function GetState_Impedance: Double;
function GetState_ShowLengthGauge: Boolean;
function GetState_WidthRule: IPCB_MaxMinWidthConstraint;
function ProjectAvailableForPinSwap(out AErrorMessage: WideString): Boolean;
procedure SetState_ShowLengthGauge(AValue: Boolean);

## IPCB_InternalPlane
继承：IPCB_InternalPlane → IPCB_ElectricalLayer → IPCB_PhysicalLayer → IPCB_LayerObject → IInterface ｜ 单元：RT_PCB ｜ 自有 4 个方法、2 个属性

property NetName: TPCBString read GetState_NetName write SetState_NetName;
property PullBackDistance: TCoord read GetState_PullBackDistance write SetState_PullBackDistance;
function GetState_NetName: WideString;
function GetState_PullBackDistance: Integer;
procedure SetState_NetName(AName: WideString);
procedure SetState_PullBackDistance(ADist: Integer);

## IPCB_InternalPlane_V7
继承：IPCB_InternalPlane_V7 → IPCB_InternalPlane → IPCB_ElectricalLayer → IPCB_PhysicalLayer → IPCB_LayerObject → IInterface ｜ 单元：RT_PCB ｜ 自有 0 个方法、0 个属性


## IPCB_KeepoutRestrictions
继承：IPCB_KeepoutRestrictions → IInterface ｜ 单元：RT_PCB ｜ 自有 13 个方法、6 个属性

property IsKeepoutForCopper: Boolean read GetState_IsKeepoutForCopper write SetState_IsKeepoutForCopper;
property IsKeepoutForSMDPad: Boolean read GetState_IsKeepoutForSMDPad write SetState_IsKeepoutForSMDPad;
property IsKeepoutForTHPad: Boolean read GetState_IsKeepoutForTHPad write SetState_IsKeepoutForTHPad;
property IsKeepoutForTrack: Boolean read GetState_IsKeepoutForTrack write SetState_IsKeepoutForTrack;
property IsKeepoutForVia: Boolean read GetState_IsKeepoutForVia write SetState_IsKeepoutForVia;
property KeepoutRestrictions: TKeepoutRestrictionsSet read GetState_KeepoutRestrictions write SetState_KeepoutRestrictions;
function GetState_IsKeepoutForCopper: Boolean;
function GetState_IsKeepoutForSMDPad: Boolean;
function GetState_IsKeepoutForTHPad: Boolean;
function GetState_IsKeepoutForTrack: Boolean;
function GetState_IsKeepoutForVia: Boolean;
function GetState_KeepoutRestrictions: TKeepoutRestrictionsSet;
function IsPrimitiveInKeepoutRestriction(APrimitive: IPCB_Primitive): Boolean;
procedure SetState_IsKeepoutForCopper(const Value: Boolean);
procedure SetState_IsKeepoutForSMDPad(const Value: Boolean);
procedure SetState_IsKeepoutForTHPad(const Value: Boolean);
procedure SetState_IsKeepoutForTrack(const Value: Boolean);
procedure SetState_IsKeepoutForVia(const Value: Boolean);
procedure SetState_KeepoutRestrictions(const Value: TKeepoutRestrictionsSet);

## IPCB_LayerIterator
继承：IPCB_LayerIterator → IInterface ｜ 单元：RT_PCB ｜ 自有 10 个方法、0 个属性

function AddFilter_ElectricalLayers: IPCB_LayerIterator;
function AddFilter_InternalPlaneLayers: IPCB_LayerIterator;
function AddFilter_LayerSet(ALayerSet: IPCB_LayerSet): IPCB_LayerIterator;
function AddFilter_MechanicalLayers: IPCB_LayerIterator;
function AddFilter_MiscLayers: IPCB_LayerIterator;
function AddFilter_SignalLayers: IPCB_LayerIterator;
function First: Boolean;
function Layer: Integer;
function Next: Boolean;
procedure SetBeforeFirst;

## IPCB_LayerListIterator
继承：IPCB_LayerListIterator → IPCB_LayerIterator → IInterface ｜ 单元：RT_PCB ｜ 自有 3 个方法、2 个属性

property Forward: Boolean read GetForward write SetForward;
property Index: Integer read GetIndex;  // read-only
function GetForward: Boolean;
function GetIndex: Integer;
procedure SetForward(const Value: Boolean);

## IPCB_LayerObject
继承：IPCB_LayerObject → IInterface ｜ 单元：RT_PCB ｜ 自有 10 个方法、2 个属性

property Name: TPCBString read GetState_LayerName write SetState_LayerName;
property UsedByPrims: Boolean read GetState_UsedByPrims write SetState_UsedByPrims;
function GetState_LayerDisplayName(Value: TLayerNameDisplayMode): WideString;
function GetState_LayerName: WideString;
function GetState_UsedByPrims: Boolean;
function I_ObjectAddress: Pointer;
function IsInLayerStack: Boolean;
function LayerStack: IPCB_LayerStackBase;
procedure SetState_LayerName(AName: WideString);
procedure SetState_UsedByPrims(Value: Boolean);
function V6_LayerID: TV6_Layer;
function V7_LayerID: IDispatch;

## IPCB_LayerObject2
继承：IPCB_LayerObject2 → IPCB_LayerObject → IInterface ｜ 单元：RT_PCB ｜ 自有 3 个方法、0 个属性

function GetState_DisplayInSingleLayerMode: Boolean;
function Id: WideString;
procedure SetState_DisplayInSingleLayerMode(Value: Boolean);

## IPCB_LayerObjectIterator
继承：IPCB_LayerObjectIterator → IPCB_LayerIterator → IInterface ｜ 单元：RT_PCB ｜ 自有 1 个方法、0 个属性

function LayerObject: IPCB_LayerObject;

## IPCB_LayerObject_V7
继承：IPCB_LayerObject_V7 → IPCB_ElectricalLayer → IPCB_PhysicalLayer → IPCB_LayerObject → IInterface ｜ 单元：RT_PCB ｜ 自有 5 个方法、1 个属性

property IsDisplayed[Board: IPCB_Board]: Boolean read GetState_IsDisplayed write SetState_IsDisplayed;
function Dielectric: IPCB_DielectricObject;
function GetState_IsDisplayed(Board: IPCB_Board): Boolean;
function GetState_LayerOriginalDispalayName: WideString;
function LayerID: TV6_Layer;
procedure SetState_IsDisplayed(Board: IPCB_Board; Value: Boolean);

## IPCB_LayerPairsRule
继承：IPCB_LayerPairsRule → IPCB_Rule → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 2 个方法、1 个属性

property EnforceLayerPairs: Boolean read GetState_EnforceLayerPairs write SetState_EnforceLayerPairs;
function GetState_EnforceLayerPairs: Boolean;
procedure SetState_EnforceLayerPairs(Value: Boolean);

## IPCB_LayerSet
继承：IPCB_LayerSet → IInterface ｜ 单元：RT_PCB ｜ 自有 28 个方法、0 个属性

function Complement: IPCB_LayerSet;
function Contains(L: Integer): Boolean;
function ContainsInternalPlaneLayers: Boolean;
function EqualTo(ALayerSet: IPCB_LayerSet): Boolean;
function Exclude(L: Integer): IPCB_LayerSet;
function ExcludeA(L: array of Integer): IPCB_LayerSet;
function ExcludeAllLayers: IPCB_LayerSet;
function ExcludeInternalPlaneLayers: IPCB_LayerSet;
function ExcludeMechanicalLayers: IPCB_LayerSet;
function ExcludeSignalLayers: IPCB_LayerSet;
function GetFirstLayer: Integer;
function Include(L: Integer): IPCB_LayerSet;
function IncludeA(L: array of Integer): IPCB_LayerSet;
function IncludeAllLayers: IPCB_LayerSet;
function IncludeInternalPlaneLayers: IPCB_LayerSet;
function IncludeMechanicalLayers: IPCB_LayerSet;
function IncludeMiscLayers: IPCB_LayerSet;
function IncludeSignalLayers: IPCB_LayerSet;
function IncludeStandardLayers: IPCB_LayerSet;
function Intersection(LayerSet: IPCB_LayerSet): IPCB_LayerSet;
function IsAllLayers: Boolean;
function IsEmpty: Boolean;
function IsFinite: Boolean;
function LayerIterator: IPCB_LayerIterator;
function Replicate: IPCB_LayerSet;
function SerializeToString: string;
function ToString: string;
function Union(LayerSet: IPCB_LayerSet): IPCB_LayerSet;

## IPCB_LayerSetUtils
继承：IPCB_LayerSetUtils → IInterface ｜ 单元：RT_PCB ｜ 自有 17 个方法、0 个属性

function AllLayers: IPCB_LayerSet;
function AreDisjoint(SetA: IPCB_LayerSet; SetB: IPCB_LayerSet): Boolean;
function Complement(SetA: IPCB_LayerSet): IPCB_LayerSet;
function CreateLayerSet: IPCB_LayerSet;
function EmptySet: IPCB_LayerSet;
function Equal(SetA: IPCB_LayerSet; SetB: IPCB_LayerSet): Boolean;
function Factory(L: Integer): IPCB_LayerSet;
function FactoryA(Ls: array of Integer): IPCB_LayerSet;
function InternalPlaneLayers: IPCB_LayerSet;
function Intersection(SetA: IPCB_LayerSet; SetB: IPCB_LayerSet): IPCB_LayerSet;
function MechanicalLayers: IPCB_LayerSet;
function NonEditableLayers: IPCB_LayerSet;
function SerializeFromString(Str: string): IPCB_LayerSet;
function SerializeToString(ALayerSet: IPCB_LayerSet): string;
function SignalLayers: IPCB_LayerSet;
function StandardLayers: IPCB_LayerSet;
function Union(SetA: IPCB_LayerSet; SetB: IPCB_LayerSet): IPCB_LayerSet;

## IPCB_LayerStack
继承：IPCB_LayerStack → IPCB_LayerStackBase → IInterface ｜ 单元：RT_PCB ｜ 自有 16 个方法、7 个属性

property BottomSignalLayer: TLayer read GetState_BottomSignalLayer;  // read-only
property Color: Cardinal read GetState_Color write SetState_Color;
property IsService: Boolean read GetState_IsService write SetState_IsService;
property LayerStackType: TLayerStackType read GetState_LayerStackType write SetState_LayerStackType;
property ShowDielectricBottom: Boolean read GetState_ShowBotDielectric write SetState_ShowBotDielectric;
property ShowDielectricTop: Boolean read GetState_ShowTopDielectric write SetState_ShowTopDielectric;
property TopSignalLayer: TLayer read GetState_TopSignalLayer;  // read-only
function Board: IPCB_Board;
function DielectricBottom: IPCB_SolderMaskLayer;
function DielectricTop: IPCB_SolderMaskLayer;
function GetState_BottomSignalLayer: Integer;
function GetState_Color: Cardinal;
function GetState_IsService: Boolean;
function GetState_LayerStackType: TLayerStackType;
function GetState_ShowBotDielectric: Boolean;
function GetState_ShowTopDielectric: Boolean;
function GetState_TopSignalLayer: Integer;
function LayerObject(ALayer: TV6_Layer): IPCB_LayerObject;
procedure SetState_Color(AColor: Cardinal);
procedure SetState_IsService(Value: Boolean);
procedure SetState_LayerStackType(Value: TLayerStackType);
procedure SetState_ShowBotDielectric(Value: Boolean);
procedure SetState_ShowTopDielectric(Value: Boolean);

## IPCB_LayerStackBase
继承：IPCB_LayerStackBase → IInterface ｜ 单元：RT_PCB ｜ 自有 17 个方法、3 个属性

property DisplayName[DisplayMode: TLayerNameDisplayMode]: TPCBString read GetDisplayName;  // read-only
property IsFlex: Boolean read GetState_IsFlex write SetState_IsFlex;
property Name: TPCBString read GetState_Name write SetState_Name;
function Count: Integer;
function First(T: TLayerClassID): IPCB_LayerObject;
function Get_ZBottom(Layer: IPCB_LayerObject): Integer;
function Get_ZTop(Layer: IPCB_LayerObject): Integer;
function GetDisplayName(DisplayMode: TLayerNameDisplayMode): WideString;
function GetState_IsFlex: Boolean;
function GetState_Name: WideString;
function I_ObjectAddress: Pointer;
function Id: WideString;
function Iterator: IPCB_LayerObjectIterator;
function Last(T: TLayerClassID): IPCB_LayerObject;
function LayerNumberInStack(const ALayer: Integer): Integer;
function Next(T: TLayerClassID; ARefLayer: IPCB_LayerObject): IPCB_LayerObject;
function Previous(T: TLayerClassID; ARefLayer: IPCB_LayerObject): IPCB_LayerObject;
procedure SetState_IsFlex(Value: Boolean);
procedure SetState_Name(AName: WideString);
function StateID: Integer;

## IPCB_LayerStackEx
继承：IPCB_LayerStackEx → IInterface ｜ 单元：RT_PCB ｜ 自有 2 个方法、0 个属性

function GetElectricalLayer(PositionInStack: Integer; LayerPartition: TLayerPartition): IPCB_LayerObject;
function GetElectricalLayerPosInStack(const Layer: Integer): Integer;

## IPCB_LayerStack_V7
继承：IPCB_LayerStack_V7 → IInterface ｜ 单元：RT_PCB ｜ 自有 24 个方法、7 个属性

property Board: IPCB_Board read GetState_Board;  // read-only
property DielectricBottom: IPCB_DielectricObject read GetState_DielectricBottom;  // read-only
property DielectricTop: IPCB_DielectricObject read GetState_DielectricTop;  // read-only
property LayerObject[L: TV6_Layer]: IPCB_LayerObject_V7 read GetState_LayerObject;  // read-only
property LayerObject_V7[L: Integer]: IPCB_LayerObject_V7 read GetState_LayerObject_V7;  // read-only
property ShowDielectricBottom: Boolean read GetState_ShowBotDielectric write SetState_ShowBotDielectric;
property ShowDielectricTop: Boolean read GetState_ShowTopDielectric write SetState_ShowTopDielectric;
function FirstAvailableInternalPlane: IPCB_InternalPlane_V7;
function FirstAvailableSignalLayer: IPCB_LayerObject_V7;
function FirstLayer: IPCB_LayerObject_V7;
function GetState_Board: IPCB_Board;
function GetState_DielectricBottom: IPCB_DielectricObject;
function GetState_DielectricTop: IPCB_DielectricObject;
function GetState_LayerObject(L: TV6_Layer): IPCB_LayerObject_V7;
function GetState_LayerObject_V7(L: Integer): IPCB_LayerObject_V7;
function GetState_LayerStackStyle: TLayerStackStyle;
function GetState_ShowBotDielectric: Boolean;
function GetState_ShowTopDielectric: Boolean;
procedure InsertInStackAbove(RefL: IPCB_LayerObject_V7; L: IPCB_LayerObject_V7);
procedure InsertInStackBelow(RefL: IPCB_LayerObject_V7; L: IPCB_LayerObject_V7);
procedure InsertLayer(L: TV6_Layer);
function LastInternalPlane: IPCB_InternalPlane_V7;
function LastLayer: IPCB_LayerObject_V7;
function LayersInStackCount: Integer;
function NextLayer(L: IPCB_LayerObject_V7): IPCB_LayerObject_V7;
function PreviousLayer(L: IPCB_LayerObject_V7): IPCB_LayerObject_V7;
procedure RemoveFromStack(L: IPCB_LayerObject_V7);
procedure SetState_LayerStackStyle(SS: TLayerStackStyle);
procedure SetState_ShowBotDielectric(Value: Boolean);
procedure SetState_ShowTopDielectric(Value: Boolean);
function SignalLayerCount: Integer;

## IPCB_LayerStackupDocumentPainterView
继承：IPCB_LayerStackupDocumentPainterView → IInterface ｜ 单元：RT_PCB ｜ 自有 2 个方法、0 个属性

procedure Refresh;
procedure SetState_DocumentToPaint(const ADocument: IServerDocument);

## IPCB_LayerToColor
继承：IPCB_LayerToColor → IInterface ｜ 单元：RT_PCB ｜ 自有 10 个方法、1 个属性

property Data[const AKey: IDispatch]: TColor read GetData write SetData;
procedure Clear;
procedure CopyTo(const ARight: IPCB_LayerToColor);
function Count: Integer;
function EqualTo(const Other: IPCB_LayerToColor): Boolean;
function Exists(const ALayer: IDispatch): Boolean;
function GetData(const AKey: IDispatch): Cardinal;
function I_ObjectAddress: Pointer;
function LayerIterator: ILayerValueIterator;
procedure ReplicateTo(const ARight: IPCB_LayerToColor);
procedure SetData(const AKey: IDispatch; const AData: Cardinal);

## IPCB_LayerUtils
继承：IPCB_LayerUtils → IInterface ｜ 单元：RT_PCB ｜ 自有 13 个方法、0 个属性

function AsShortDisplayString(L: Integer): WideString;
function AsString(L: Integer): WideString;
function FirstLayerInRange(LayerType: TLayerPartition; UnAvaiableLayers: IPCB_LayerSet): Integer;
function FromShortDisplayString(S: WideString): Integer;
function FromString(S: WideString): Integer;
function IsElectricalLayer(L: Integer): Boolean;
function IsInternalPlaneLayer(L: Integer): Boolean;
function IsMechanicalLayer(L: Integer): Boolean;
function IsMidLayer(L: Integer): Boolean;
function IsSignalLayer(L: Integer): Boolean;
function LayerIterator_PossibleLayers: IPCB_LayerListIterator;
function LayerIterator_PossibleSummer09Layers: IPCB_LayerListIterator;
function MechanicalLayer(I: Cardinal): Integer;

## IPCB_LeaderDimension
继承：IPCB_LeaderDimension → IPCB_Dimension → IPCB_Group → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 16 个方法、3 个属性

property Dot: Boolean read GetState_Dot write SetState_Dot;
property DotSize: TCoord read GetState_DotSize write SetState_DotSize;
property Shape: TShape read GetState_Shape write SetState_Shape;
function Arrow_Track1: IPCB_Track;
function Arrow_Track2: IPCB_Track;
function Circle_Arc: IPCB_Arc;
function Dot_Arc: IPCB_Arc;
function GetState_Dot: Boolean;
function GetState_DotSize: Integer;
function GetState_Shape: TShape;
function Line_Track(I: Integer): IPCB_Track;
procedure SetState_Dot(Value: Boolean);
procedure SetState_DotSize(Value: Integer);
procedure SetState_Shape(Value: TShape);
function Square_Track1: IPCB_Track;
function Square_Track2: IPCB_Track;
function Square_Track3: IPCB_Track;
function Square_Track4: IPCB_Track;
function Text: IPCB_Text;

## IPCB_LettersCache
继承：IPCB_LettersCache → IInterface ｜ 单元：RT_PCB ｜ 自有 1 个方法、0 个属性

function I_ObjectAddress: Pointer;

## IPCB_LibComponent
继承：IPCB_LibComponent → IPCB_Group → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 22 个方法、5 个属性

property Description: TPCBString read GetState_Description write SetState_Description;
property Height: TCoord read GetState_Height write SetState_Height;
property ItemGUID: TPCBString read GetState_ItemGUID write SetState_ItemGUID;
property ItemRevisionGUID: TPCBString read GetState_ItemRevisionGUID write SetState_ItemRevisionGUID;
property Name: TPCBString read GetState_Pattern write SetState_Pattern;
procedure CopyTo(const P: IPCB_LibComponent; CopyMode: TCopyMode);
function GetState_Area: Double;
function GetState_ComponentKind: TComponentKind;
function GetState_Description: WideString;
function GetState_Height: Integer;
function GetState_ItemGUID: WideString;
function GetState_ItemRevisionGUID: WideString;
function GetState_Pattern: WideString;
function GetState_VaultGUID: WideString;
function ReleasableInterface: IInterface;
function SaveModelToFile(const AFilename: WideString; ASaveAsPart: Boolean): Boolean;
procedure SaveToFile(VFSAddress: WideString);
procedure SetState_Area(const Value: Double);
procedure SetState_ComponentKind(const Value: TComponentKind);
procedure SetState_Description(Value: WideString);
procedure SetState_Height(Value: Integer);
procedure SetState_ItemGUID(Value: WideString);
procedure SetState_ItemRevisionGUID(Value: WideString);
procedure SetState_Pattern(Value: WideString);
procedure SetState_VaultGUID(const Value: WideString);
procedure TransferAllPrimitivesBackFromBoard;
procedure TransferAllPrimitivesOntoBoard;

## IPCB_LibComponent_BatchRelease
继承：IPCB_LibComponent_BatchRelease → IInterface ｜ 单元：RT_PCB ｜ 自有 2 个方法、2 个属性

property Component: IPCB_LibComponent read GetState_Component;  // read-only
property ComponentLibrary: IPCB_Library read GetState_ComponentLibrary;  // read-only
function GetState_Component: IPCB_LibComponent;
function GetState_ComponentLibrary: IPCB_Library;

## IPCB_Library
继承：IPCB_Library → IInterface ｜ 单元：RT_PCB ｜ 自有 39 个方法、9 个属性

property Board: IPCB_Board read GetState_Board;  // read-only
property CurrentComponent: IPCB_LibComponent read GetState_CurrentComponent write SetState_CurrentComponent;
property FolderGUID: TPCBString read GetState_FolderGUID write SetState_FolderGUID;
property IsSimpleDesignMode: Boolean read GetState_IsSimpleDesignMode;  // read-only
property IsSingleComponentMode: Boolean read GetState_IsSingleComponentMode;  // read-only
property LibraryID: Integer read GetState_LibraryID;  // read-only
property LifeCycleDefinitionGUID: TPCBString read GetState_LifeCycleDefinitionGUID write SetState_LifeCycleDefinitionGUID;
property RevisionNamingSchemeGUID: TPCBString read GetState_RevisionNamingSchemeGUID write SetState_RevisionNamingSchemeGUID;
property VaultGUID: TPCBString read GetState_VaultGUID write SetState_VaultGUID;
function AddComponent(const Name: WideString): IPCB_LibComponent;
function ComponentCount: Integer;
function CreateNewComponent: IPCB_LibComponent;
function DeRegisterComponent(Component: IPCB_LibComponent): Boolean;
function GetComponent(I: Integer): IPCB_LibComponent;
function GetComponentByName(const CompName: WideString): IPCB_LibComponent;
function GetState_Board: IPCB_Board;
function GetState_CurrentComponent: IPCB_LibComponent;
function GetState_FolderGUID: WideString;
function GetState_IsSimpleDesignMode: Boolean;
function GetState_IsSingleComponentMode: Boolean;
function GetState_LibraryID: Integer;
function GetState_LifeCycleDefinitionGUID: WideString;
function GetState_RevisionNamingSchemeGUID: WideString;
function GetState_VaultGUID: WideString;
function GetUniqueCompName(const ATestCompName: WideString): WideString;
function GlobalComponentUpdateOptions: IPCB_ComponentUpdateOptions;
function HasServerDocument: Boolean;
function I_ObjectAddress: Pointer;
function LibraryIterator_Create: IPCB_LibraryIterator;
procedure LibraryIterator_Destroy(var AIterator: IPCB_LibraryIterator);
function LibraryLoaderSaver_Create: IPCB_LibraryLoaderSaver;
procedure LibraryLoaderSaver_Destroy(var ALoaderSaver: IPCB_LibraryLoaderSaver);
function LinkDocumentToReleaseVault(Parameters: WideString; var ErrorMsg: WideString): Boolean;
procedure Navigate_Component(ComponentName: WideString);
procedure Navigate_FirstComponent;
procedure RefreshView;
function RegisterComponent(Component: IPCB_LibComponent): Boolean;
function ReleaseDocument(Parameters: WideString; var ErrorMsg: WideString): Boolean;
procedure RemoveComponent(var AComponent: IPCB_LibComponent);
function SaveComponentWithLibrary(ComponentName: WideString; FileName: WideString): Boolean;
function SaveEmptyLibrary(FileName: WideString): Boolean;
function SetBoardToComponentByName(const ACompName: WideString): Boolean;
procedure SetCurrentComponentReference(AX: Integer; AY: Integer);
procedure SetState_CurrentComponent(const Component: IPCB_LibComponent);
procedure SetState_FolderGUID(Value: WideString);
procedure SetState_LifeCycleDefinitionGUID(Value: WideString);
procedure SetState_RevisionNamingSchemeGUID(Value: WideString);
procedure SetState_VaultGUID(Value: WideString);

## IPCB_LibraryIterator
继承：IPCB_LibraryIterator → IPCB_AbstractIterator → IInterface ｜ 单元：RT_PCB ｜ 自有 0 个方法、0 个属性


## IPCB_LibraryLoaderSaver
继承：IPCB_LibraryLoaderSaver → IInterface ｜ 单元：RT_PCB ｜ 自有 2 个方法、0 个属性

function LoadFromFile(APCBLibrary: IPCB_Library; const AFilename: WideString): Boolean;
function SaveToFile(APCBLibrary: IPCB_Library; const AFilename: WideString): Boolean;

## IPCB_LinearDiameterDimension
继承：IPCB_LinearDiameterDimension → IPCB_LinearDimension → IPCB_Dimension → IPCB_Group → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 0 个方法、0 个属性


## IPCB_LinearDimension
继承：IPCB_LinearDimension → IPCB_Dimension → IPCB_Group → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 11 个方法、1 个属性

property Angle: TAngle read GetState_Angle write SetState_Angle;
function Arrow1_Track1: IPCB_Track;
function Arrow1_Track2: IPCB_Track;
function Arrow2_Track1: IPCB_Track;
function Arrow2_Track2: IPCB_Track;
function Extension1_Track: IPCB_Track;
function Extension2_Track: IPCB_Track;
function GetState_Angle: Double;
function Line_Track1: IPCB_Track;
function Line_Track2: IPCB_Track;
procedure SetState_Angle(Value: Double);
function Text: IPCB_Text;

## IPCB_LiveHandleContainer
继承：IPCB_LiveHandleContainer → IInterface ｜ 单元：RT_PCB ｜ 自有 1 个方法、0 个属性

function GetHandle: NativeUInt;

## IPCB_MasterLayerStack
继承：IPCB_MasterLayerStack → IPCB_LayerStackBase → IInterface ｜ 单元：RT_PCB ｜ 自有 18 个方法、2 个属性

property LayerStackStyle: TLayerStackStyle read GetState_LayerStackStyle write SetState_LayerStackStyle;
property Substacks[Index: Integer]: IPCB_LayerStack read GetState_Substacks;  // read-only
function Board: IPCB_Board;
function CreateLayer(const ALayer: IDispatch): IPCB_LayerObject;
function CreateSubstack: IPCB_LayerStack;
procedure DisableLayer(ASubstack: IPCB_LayerStack; ALayer: IPCB_LayerObject);
procedure EnableLayer(ASubstack: IPCB_LayerStack; ALayer: IPCB_LayerObject);
procedure Export_ToParameters(Params: PWideChar);
function GetState_LayerStackStyle: TLayerStackStyle;
function GetState_Substacks(Index: Integer): IPCB_LayerStack;
function GetSubstack(ASubstackID: WideString): IPCB_LayerStack;
procedure Import_FromParameters(Params: PWideChar);
function InsertAbove(ARefLayer: IPCB_LayerObject; ALayer: IPCB_LayerObject): IPCB_LayerObject;
function InsertBelow(ARefLayer: IPCB_LayerObject; ALayer: IPCB_LayerObject): IPCB_LayerObject;
function InsertOnBottom(ALayer: IPCB_LayerObject): IPCB_LayerObject;
function InsertOnTop(ALayer: IPCB_LayerObject): IPCB_LayerObject;
function RemoveLayer(Layer: IPCB_LayerObject): Boolean;
function RemoveSubstack(Substack: IPCB_LayerStack): Boolean;
procedure SetState_LayerStackStyle(AStackStyle: TLayerStackStyle);
function SubstackCount: Integer;

## IPCB_MasterLayerStack2
继承：IPCB_MasterLayerStack2 → IPCB_MasterLayerStack → IPCB_LayerStackBase → IInterface ｜ 单元：RT_PCB ｜ 自有 20 个方法、0 个属性

function AddMechanicalLayer: IPCB_MechanicalLayer;
procedure ChangeSubStackId(ASubstack: IPCB_LayerStack; NewID: WideString);
procedure ClearAllPhysicalLayers;
function CreateImpedanceProfile: IPCB_ImpedanceProfile;
function CreateImpedanceProfileWithId(Id: WideString): IPCB_ImpedanceProfile;
function CreateLayerPairByKind(AKind: TMechanicalLayerPairKind): Boolean;
function CreateLayerWithId(const ALayer: IDispatch; const LayerID: WideString): IPCB_LayerObject;
function CreateSubstackWithId(Id: WideString): IPCB_LayerStack;
procedure Export_ToLayerStackManagerParameters(Params: PWideChar);
function FindLayerByKind(ALayerKind: TMechanicalLayerKind): IPCB_MechanicalLayer;
function GetImpedanceProfileById(Id: WideString): IPCB_ImpedanceProfile;
function GetImpedanceProfileByIndex(Index: Integer): IPCB_ImpedanceProfile;
function GetImpedanceProfileCount: Integer;
function GetMechanicalLayer(AIndexInMechanicalFamily: Integer): IPCB_MechanicalLayer;
function GetState_CustomData: WideString;
procedure Import_FromLayerStackManagerParameters(Params: PWideChar);
function MeasureLayerDistance(const StartLayer: IPCB_LayerObject; const EndLayer: IPCB_LayerObject): Integer;
procedure Merge_FromLayerStackManagerParameters(Params: PWideChar; Actions: PWideChar);
function RemoveImpedanceProfile(ImpedanceProfile: IPCB_ImpedanceProfile): Boolean;
procedure SetState_CustomData(Value: WideString);

## IPCB_MatchedLengthRange
继承：IPCB_MatchedLengthRange → IInterface ｜ 单元：RT_PCB ｜ 自有 6 个方法、5 个属性

property ClippedTargetRangeStart: TCoord read GetState_ClippedTargetRangeStart;  // read-only
property ClippedTargetRangeStop: TCoord read GetState_ClippedTargetRangeStop;  // read-only
property DriverRule: IPCB_MatchedNetLengthsConstraint read GetState_DriverRule;  // read-only
property RangeValid: Boolean read GetState_RangeValid;  // read-only
property UseTargetSource: Boolean read GetState_UseTargetSource;  // read-only
function DriverRule_Name: WideString;
function GetState_ClippedTargetRangeStart: Integer;
function GetState_ClippedTargetRangeStop: Integer;
function GetState_DriverRule: IPCB_MatchedNetLengthsConstraint;
function GetState_RangeValid: Boolean;
function GetState_UseTargetSource: Boolean;

## IPCB_MatchedNetLengthsConstraint
继承：IPCB_MatchedNetLengthsConstraint → IPCB_Rule → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 24 个方法、11 个属性

property Amplitude: TCoord read GetState_Amplitude write SetState_Amplitude;
property CheckBetweenXSignals: Boolean read Get_CheckBetweenXSignals write Set_CheckBetweenXSignals;
property CheckDiffPairVsDiffPair: Boolean read Get_CheckDiffPairVsDiffPair write Set_CheckDiffPairVsDiffPair;
property CheckNetsInDiffPair: Boolean read Get_CheckNetsInDiffPair write Set_CheckNetsInDiffPair;
property CheckOtherElectricalObjects: Boolean read Get_CheckOtherElectricalObjects write Set_CheckOtherElectricalObjects;
property DelayTolerance: Double read GetState_DelayTolerance write SetState_DelayTolerance;
property Gap: TCoord read GetState_Gap write SetState_Gap;
property Style: TLengthenerStyle read GetState_Style write SetState_Style;
property TargetSourceName: TPCBString read GetState_TargetSourceName write SetState_TargetSourceName;
property Tolerance: TCoord read GetState_Tolerance write SetState_Tolerance;
property UseDelayUnits: Boolean read GetState_UseDelayUnits write SetState_UseDelayUnits;
function Get_CheckBetweenXSignals: Boolean;
function Get_CheckDiffPairVsDiffPair: Boolean;
function Get_CheckNetsInDiffPair: Boolean;
function Get_CheckOtherElectricalObjects: Boolean;
function GetState_Amplitude: Integer;
function GetState_DelayTolerance: Double;
function GetState_Gap: Integer;
function GetState_Style: TLengthenerStyle;
function GetState_TargetSourceName: WideString;
function GetState_Tolerance: Integer;
function GetState_UseDelayUnits: Boolean;
function MatchLengthForFromTo(P1: IPCB_Primitive; P2: IPCB_Primitive): IPCB_Violation;
function MatchLengthForNet(P1: IPCB_Primitive; P2: IPCB_Primitive): IPCB_Violation;
procedure Set_CheckBetweenXSignals(Value: Boolean);
procedure Set_CheckDiffPairVsDiffPair(Value: Boolean);
procedure Set_CheckNetsInDiffPair(Value: Boolean);
procedure Set_CheckOtherElectricalObjects(Value: Boolean);
procedure SetState_Amplitude(Value: Integer);
procedure SetState_DelayTolerance(Value: Double);
procedure SetState_Gap(Value: Integer);
procedure SetState_Style(Value: TLengthenerStyle);
procedure SetState_TargetSourceName(AValue: WideString);
procedure SetState_Tolerance(Value: Integer);
procedure SetState_UseDelayUnits(Value: Boolean);

## IPCB_MaxMinHeightConstraint
继承：IPCB_MaxMinHeightConstraint → IPCB_Rule → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 6 个方法、3 个属性

property MaxHeight: TCoord read GetState_MaxHeight write SetState_MaxHeight;
property MinHeight: TCoord read GetState_MinHeight write SetState_MinHeight;
property PreferedHeight: TCoord read GetState_PreferedHeight write SetState_PreferedHeight;
function GetState_MaxHeight: Integer;
function GetState_MinHeight: Integer;
function GetState_PreferedHeight: Integer;
procedure SetState_MaxHeight(Value: Integer);
procedure SetState_MinHeight(Value: Integer);
procedure SetState_PreferedHeight(Value: Integer);

## IPCB_MaxMinHoleSizeConstraint
继承：IPCB_MaxMinHoleSizeConstraint → IPCB_Rule → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 10 个方法、5 个属性

property AbsoluteValues: Boolean read GetState_AbsoluteValues write SetState_AbsoluteValues;
property MaxLimit: TCoord read GetState_MaxLimit write SetState_MaxLimit;
property MaxPercent: TReal read GetState_MaxPercent write SetState_MaxPercent;
property MinLimit: TCoord read GetState_MinLimit write SetState_MinLimit;
property MinPercent: TReal read GetState_MinPercent write SetState_MinPercent;
function GetState_AbsoluteValues: Boolean;
function GetState_MaxLimit: Integer;
function GetState_MaxPercent: Double;
function GetState_MinLimit: Integer;
function GetState_MinPercent: Double;
procedure SetState_AbsoluteValues(Value: Boolean);
procedure SetState_MaxLimit(Value: Integer);
procedure SetState_MaxPercent(Value: Double);
procedure SetState_MinLimit(Value: Integer);
procedure SetState_MinPercent(Value: Double);

## IPCB_MaxMinLengthConstraint
继承：IPCB_MaxMinLengthConstraint → IPCB_Rule → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 10 个方法、5 个属性

property MaxDelay: Double read GetState_MaxDelay write SetState_MaxDelay;
property MaxLimit: TCoord read GetState_MaxLimit write SetState_MaxLimit;
property MinDelay: Double read GetState_MinDelay write SetState_MinDelay;
property MinLimit: TCoord read GetState_MinLimit write SetState_MinLimit;
property UseDelayUnits: Boolean read GetState_UseDelayUnits write SetState_UseDelayUnits;
function GetState_MaxDelay: Double;
function GetState_MaxLimit: Integer;
function GetState_MinDelay: Double;
function GetState_MinLimit: Integer;
function GetState_UseDelayUnits: Boolean;
procedure SetState_MaxDelay(Value: Double);
procedure SetState_MaxLimit(Value: Integer);
procedure SetState_MinDelay(Value: Double);
procedure SetState_MinLimit(Value: Integer);
procedure SetState_UseDelayUnits(Value: Boolean);

## IPCB_MaxMinWidthConstraint
继承：IPCB_MaxMinWidthConstraint → IPCB_Rule → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 26 个方法、9 个属性

property CheckConnectedCopper: Boolean read GetState_CheckConnectedCopper write SetState_CheckConnectedCopper;
property FavoredImpedance: TDouble read GetState_FavoredImpedance write SetState_FavoredImpedance;
property FavoredWidth[const L: Integer]: TCoord read GetState_FavoredWidth write SetState_FavoredWidth;
property ImpedanceDriven: Boolean read GetState_ImpedanceDriven write SetState_ImpedanceDriven;
property ImpedanceProfileId: TPCBString read GetState_ImpedanceProfileId write SetState_ImpedanceProfileId;
property MaxImpedance: TDouble read GetState_MaxImpedance write SetState_MaxImpedance;
property MaxWidth[const L: Integer]: TCoord read GetState_MaxWidth write SetState_MaxWidth;
property MinImpedance: TDouble read GetState_MinImpedance write SetState_MinImpedance;
property MinWidth[const L: Integer]: TCoord read GetState_MinWidth write SetState_MinWidth;
function GetState_CheckConnectedCopper: Boolean;
function GetState_FavoredImpedance: Double;
function GetState_FavoredWidth(const L: Integer): Integer;
function GetState_FavoredWidthAtSubStack(const L: Integer; StackID: WideString): Integer;
function GetState_ImpedanceDriven: Boolean;
function GetState_ImpedanceProfileId: WideString;
function GetState_IsLayerDefined(const L: Integer; StackID: WideString): Boolean;
function GetState_MaxImpedance: Double;
function GetState_MaxWidth(const L: Integer): Integer;
function GetState_MaxWidthAtSubStack(const L: Integer; StackID: WideString): Integer;
function GetState_MinImpedance: Double;
function GetState_MinWidth(const L: Integer): Integer;
function GetState_MinWidthAtSubStack(const L: Integer; StackID: WideString): Integer;
procedure Invalidate;
procedure SetState_CheckConnectedCopper(Value: Boolean);
procedure SetState_FavoredImpedance(Value: Double);
procedure SetState_FavoredWidth(const L: Integer; Value: Integer);
procedure SetState_FavoredWidthAtSubStack(const L: Integer; StackID: WideString; Value: Integer);
procedure SetState_ImpedanceDriven(Value: Boolean);
procedure SetState_ImpedanceProfileId(Value: WideString);
procedure SetState_MaxImpedance(Value: Double);
procedure SetState_MaxWidth(const L: Integer; Value: Integer);
procedure SetState_MaxWidthAtSubStack(const L: Integer; StackID: WideString; Value: Integer);
procedure SetState_MinImpedance(Value: Double);
procedure SetState_MinWidth(const L: Integer; Value: Integer);
procedure SetState_MinWidthAtSubStack(const L: Integer; StackID: WideString; Value: Integer);

## IPCB_MaxOvershootFall
继承：IPCB_MaxOvershootFall → IPCB_Rule → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 2 个方法、1 个属性

property Maximum: Double read GetState_Maximum write SetState_Maximum;
function GetState_Maximum: Double;
procedure SetState_Maximum(Value: Double);

## IPCB_MaxOvershootRise
继承：IPCB_MaxOvershootRise → IPCB_Rule → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 2 个方法、1 个属性

property Maximum: Double read GetState_Maximum write SetState_Maximum;
function GetState_Maximum: Double;
procedure SetState_Maximum(Value: Double);

## IPCB_MaxUndershootFall
继承：IPCB_MaxUndershootFall → IPCB_Rule → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 2 个方法、1 个属性

property Maximum: Double read GetState_Maximum write SetState_Maximum;
function GetState_Maximum: Double;
procedure SetState_Maximum(Value: Double);

## IPCB_MaxUndershootRise
继承：IPCB_MaxUndershootRise → IPCB_Rule → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 2 个方法、1 个属性

property Maximum: Double read GetState_Maximum write SetState_Maximum;
function GetState_Maximum: Double;
procedure SetState_Maximum(Value: Double);

## IPCB_MaximumViaCountRule
继承：IPCB_MaximumViaCountRule → IPCB_Rule → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 2 个方法、1 个属性

property Limit: Integer read GetState_Limit write SetState_Limit;
function GetState_Limit: Integer;
procedure SetState_Limit(Value: Integer);

## IPCB_MechanicalLayer
继承：IPCB_MechanicalLayer → IPCB_LayerObject → IInterface ｜ 单元：RT_PCB ｜ 自有 8 个方法、4 个属性

property DisplayInSingleLayerMode: Boolean read GetState_DisplayInSingleLayerMode write SetState_DisplayInSingleLayerMode;
property Kind: TMechanicalLayerKind read GetState_Kind write SetState_Kind;
property LinkToSheet: Boolean read GetState_LinkToSheet write SetState_LinkToSheet;
property MechanicalLayerEnabled: Boolean read GetState_MechLayerEnabled write SetState_MechLayerEnabled;
function GetState_DisplayInSingleLayerMode: Boolean;
function GetState_Kind: TMechanicalLayerKind;
function GetState_LinkToSheet: Boolean;
function GetState_MechLayerEnabled: Boolean;
procedure SetState_DisplayInSingleLayerMode(AValue: Boolean);
procedure SetState_Kind(AValue: TMechanicalLayerKind);
procedure SetState_LinkToSheet(AValue: Boolean);
procedure SetState_MechLayerEnabled(AValue: Boolean);

## IPCB_MechanicalLayerPairs
继承：IPCB_MechanicalLayerPairs → IInterface ｜ 单元：RT_PCB ｜ 自有 16 个方法、3 个属性

property LayerPair[I: Integer]: TMechanicalLayerPair read GetState_LayerPair;  // read-only
property LayerPairKind[I: Integer]: TMechanicalLayerPairKind read GetState_LayerPairKind write SetState_LayerPairKind;
property LayerPairLayerStackID[I: Integer]: WideString read GetState_LayerPairLayerStackID;  // read-only
function AddPair(Layer1: Integer; Layer2: Integer): Integer;
function AddPairToStack(LayerStack: IPCB_LayerStack; Layer1: Integer; Layer2: Integer): Integer;
procedure Clear;
function Count: Integer;
function CreatePairByKind(AKind: TMechanicalLayerPairKind): Integer;
procedure Export_ToParameters(Params: PWideChar);
function FlipLayer(var L: TV6_Layer): Boolean;
function FlipLayerV7(var L: Integer): Boolean;
function GetState_LayerPair(I: Integer): IDispatch;
function GetState_LayerPairKind(I: Integer): TMechanicalLayerPairKind;
function GetState_LayerPairLayerStackID(I: Integer): WideString;
procedure Import_FromParameters(Params: PWideChar);
function LayerUsed(Layer: Integer): Boolean;
function PairDefined(Layer1: Integer; Layer2: Integer): Boolean;
function RemovePair(Layer1: Integer; Layer2: Integer): Boolean;
procedure SetState_LayerPairKind(I: Integer; AKind: TMechanicalLayerPairKind);

## IPCB_MeshColorList
继承：IPCB_MeshColorList → IInterface ｜ 单元：RT_PCB ｜ 自有 5 个方法、0 个属性

procedure Clear;
procedure Delete(AIndex: Integer);
function Get(AIndex: Integer): Cardinal;
function GetAsString: WideString;
function GetCount: Integer;

## IPCB_MeshItem
继承：IPCB_MeshItem → IInterface ｜ 单元：RT_PCB ｜ 自有 7 个方法、0 个属性

function GetColorList: IPCB_MeshColorList;
function GetLayerName: WideString;
function GetName: WideString;
function GetTriangleList: IPCB_MeshTriangleList;
function GetVertexList: IPCB_MeshVertexList;
procedure SetLayerName(const AValue: WideString);
procedure SetName(const AValue: WideString);

## IPCB_MeshItemList
继承：IPCB_MeshItemList → IInterface ｜ 单元：RT_PCB ｜ 自有 4 个方法、0 个属性

procedure Clear;
procedure Delete(AIndex: Integer);
function Get(AIndex: Integer): IPCB_MeshItem;
function GetCount: Integer;

## IPCB_MeshObject
继承：IPCB_MeshObject → IInterface ｜ 单元：RT_PCB ｜ 自有 1 个方法、0 个属性

function GetMeshItems: IPCB_MeshItemList;

## IPCB_MeshTriangleList
继承：IPCB_MeshTriangleList → IInterface ｜ 单元：RT_PCB ｜ 自有 5 个方法、0 个属性

procedure Clear;
procedure Delete(AIndex: Integer);
function Get(AIndex: Integer): IDispatch;
function GetAsString: WideString;
function GetCount: Integer;

## IPCB_MeshVertexList
继承：IPCB_MeshVertexList → IInterface ｜ 单元：RT_PCB ｜ 自有 5 个方法、0 个属性

procedure Clear;
procedure Delete(AIndex: Integer);
function Get(AIndex: Integer): IDispatch;
function GetAsString: WideString;
function GetCount: Integer;

## IPCB_MinimumAnnularRing
继承：IPCB_MinimumAnnularRing → IPCB_Rule → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 2 个方法、1 个属性

property Minimum: TCoord read GetState_Minimum write SetState_Minimum;
function GetState_Minimum: Integer;
procedure SetState_Minimum(Value: Integer);

## IPCB_MinimumSolderMaskSliverRule
继承：IPCB_MinimumSolderMaskSliverRule → IPCB_Rule → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 2 个方法、1 个属性

property MinSolderMaskSliver: TCoord read GetState_MinSolderMaskSliver write SetState_MinSolderMaskSliver;
function GetState_MinSolderMaskSliver: Integer;
procedure SetState_MinSolderMaskSliver(Value: Integer);

## IPCB_Model
继承：IPCB_Model → IPCB_ModelProperties_Base → IInterface ｜ 单元：RT_PCB ｜ 自有 34 个方法、12 个属性

property Checksum: Cardinal read GetChecksum;  // read-only
property DataSize: Int64 read GetDataSize;  // read-only
property Embed: Boolean read GetEmbed write SetEmbed;
property FileName: TPCBString read GetFileName;  // read-only
property ItemGUID: TPCBString read GetItemGUID write SetItemGUID;
property ItemRevisionGUID: TPCBString read GetItemRevisionGUID write SetItemRevisionGUID;
property ModelSource: TModelSource read GetModelSource write SetModelSource;
property ModelType: T3DModelType read GetState_ModelType write SetState_ModelType;
property Name: TPCBString read GetName write SetName;
property Origin: TCoordPoint read GetOrigin write SetOrigin;
property Rotation: TAngle read GetRotation write SetRotation;
property VaultGUID: TPCBString read GetVaultGUID write SetVaultGUID;
procedure AddTo(const ViewWrapper: IOccWrapper; const ITransformation: IPCB3D_Transformation; const Name: WideString);
procedure AddToAssembly(const ViewWrapper: IOccWrapper; const AssemblyIndex: Integer; const ITransformation: IPCB3D_Transformation; const Name: WideString);
procedure AddToAssembly2(const ViewWrapper: IOccWrapper; const AssemblyIndex: Integer; const ITransformation: IPCB3D_Transformation; const Name: WideString; const Color: Cardinal);
procedure ExportToStep(const FileName: WideString);
function ForceCheck_IsStale: Boolean;
function GetChecksum: Cardinal;
function GetDataHash(const AHashType: WideString): WideString;
function GetDataSize: Int64;
function GetEmbed: Boolean;
function GetFileName: WideString;
function GetItemGUID: WideString;
function GetItemRevisionGUID: WideString;
function GetModelSource: TModelSource;
function GetName: WideString;
function GetOrigin: IDispatch;
function GetRotation: Double;
procedure GetState(out RotX: Double; out RotY: Double; out RotZ: Double; out Dz: Integer);
function GetState_ModelType: T3DModelType;
function GetVaultGUID: WideString;
function I_ObjectAddress: Pointer;
function I_Replicate: IPCB_Model;
function I_ReplicateToGeneric: IPCB_Model;
function IsEmpty: Boolean;
function IsStale: Boolean;
procedure SetEmbed(const Value: Boolean);
procedure SetItemGUID(const Value: WideString);
procedure SetItemRevisionGUID(const Value: WideString);
procedure SetModelSource(Value: TModelSource);
procedure SetName(const Value: WideString);
procedure SetOrigin(const Value: IDispatch);
procedure SetRotation(const NewValue: Double);
procedure SetState(RotX: Double; RotY: Double; RotZ: Double; Dz: Integer);
procedure SetState_ModelType(const Value: T3DModelType);
procedure SetVaultGUID(const Value: WideString);

## IPCB_ModelOptions
继承：IPCB_ModelOptions → IInterface ｜ 单元：RT_PCB ｜ 自有 3 个方法、0 个属性

procedure GetSearchPaths(Project: IProject; AbsoluteSearchPaths: IPCB_WideStrings; UnusedPaths: IPCB_WideStrings);
function GetState_MeshDirectory: WideString;
procedure SetState_MeshDirectory(const AValue: WideString);

## IPCB_ModelProperties_Base
继承：IPCB_ModelProperties_Base → IInterface ｜ 单元：RT_PCB ｜ 自有 0 个方法、0 个属性


## IPCB_ModelProperties_Cylinder
继承：IPCB_ModelProperties_Cylinder → IPCB_ModelProperties_Base → IInterface ｜ 单元：RT_PCB ｜ 自有 4 个方法、2 个属性

property Height: TCoord read GetState_Height write SetState_Height;
property Radius: TCoord read GetState_Radius write SetState_Radius;
function GetState_Height: Integer;
function GetState_Radius: Integer;
procedure SetState_Height(const Value: Integer);
procedure SetState_Radius(const Value: Integer);

## IPCB_ModelProperties_Extruded
继承：IPCB_ModelProperties_Extruded → IPCB_ModelProperties_Base → IInterface ｜ 单元：RT_PCB ｜ 自有 4 个方法、2 个属性

property MaxZ: TCoord read GetState_MaxZ write SetState_MaxZ;
property MinZ: TCoord read GetState_MinZ write SetState_MinZ;
function GetState_MaxZ: Integer;
function GetState_MinZ: Integer;
procedure SetState_MaxZ(const Value: Integer);
procedure SetState_MinZ(const Value: Integer);

## IPCB_ModelProperties_Sphere
继承：IPCB_ModelProperties_Sphere → IPCB_ModelProperties_Base → IInterface ｜ 单元：RT_PCB ｜ 自有 2 个方法、1 个属性

property Radius: TCoord read GetState_Radius write SetState_Radius;
function GetState_Radius: Integer;
procedure SetState_Radius(const Value: Integer);

## IPCB_ModifiedPolygonRule
继承：IPCB_ModifiedPolygonRule → IPCB_Rule → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 4 个方法、2 个属性

property AllowModified: Boolean read GetState_AllowModified write SetState_AllowModified;
property AllowShelved: Boolean read GetState_AllowShelved write SetState_AllowShelved;
function GetState_AllowModified: Boolean;
function GetState_AllowShelved: Boolean;
procedure SetState_AllowModified(Value: Boolean);
procedure SetState_AllowShelved(Value: Boolean);

## IPCB_MultilineText
继承：IPCB_MultilineText → IPCB_RectangularPrimitive → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 0 个方法、0 个属性


## IPCB_Net
继承：IPCB_Net → IPCB_Group → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 35 个方法、16 个属性

property Color: TColor read GetState_Color write SetState_Color;
property ConnectivelyInvalid: Boolean read GetState_ConnectivelyInvalid;  // read-only
property ConnectsVisible: Boolean read GetState_ConnectsVisible write SetState_ConnectsVisible;
property DifferentialPair: Pointer read GetState_DifferentialPair write SetState_DifferentialPair;
property InDifferentialPair: Boolean read GetState_InDifferentialPair;  // read-only
property IsHighlighted: Boolean read GetState_IsHighlighted write SetState_IsHighlighted;
property JumpersVisible: Boolean read GetState_JumpersVisible write SetState_JumpersVisible;
property LiveHighlightMode: TLiveHighlightMode read GetState_LiveHighlightMode write SetState_LiveHighlightMode;
property LoopRemoval: Boolean read GetState_LoopRemoval write SetState_LoopRemoval;
property Name: TPCBString read GetState_Name write SetState_Name;
property OverrideColorForDraw: Boolean read GetState_OverrideColorForDraw write SetState_OverrideColorForDraw;
property PadByName[PadName: WideString]: IPCB_Primitive read Getstate_PadByName;  // read-only
property PadByPinDescription[PinDes: WideString]: IPCB_Primitive read Getstate_PadByPinDescription;  // read-only
property PinCount: Integer read GetState_PinCount;  // read-only
property RoutedLength: TCoord read GetState_RoutedLength;  // read-only
property ViaCount: Integer read GetState_ViaCount;  // read-only
procedure CancelGroupWarehouseRegistration(iPad: IPCB_Pad);
procedure ConnectivelyInValidate;
function GetLogicalNet: IPCB_Group;
function GetState_Color: Cardinal;
function GetState_ConnectivelyInvalid: Boolean;
function GetState_ConnectsVisible: Boolean;
function GetState_DifferentialPair: Pointer;
function GetState_InDifferentialPair: Boolean;
function GetState_IsHighlighted: Boolean;
function GetState_JumpersVisible: Boolean;
function GetState_LiveHighlightMode: TLiveHighlightMode;
function GetState_LoopRemoval: Boolean;
function GetState_Name: WideString;
function GetState_OverrideColorForDraw: Boolean;
function Getstate_PadByName(PadName: WideString): IPCB_Primitive;
function Getstate_PadByPinDescription(PinDes: WideString): IPCB_Primitive;
function GetState_PinCount: Integer;
function GetState_RoutedLength: Integer;
function GetState_ViaCount: Integer;
function GetSubnets: IPCB_Group;
procedure HideNetConnects;
procedure Rebuild;
procedure RegisterWithGroupWarehouse(iPad: IPCB_Pad);
procedure SetState_Color(Color: Cardinal);
procedure SetState_ConnectsVisible(Value: Boolean);
procedure SetState_DifferentialPair(Value: Pointer);
procedure SetState_IsHighlighted(Dummy: Boolean);
procedure SetState_JumpersVisible(Value: Boolean);
procedure SetState_LiveHighlightMode(Value: TLiveHighlightMode);
procedure SetState_LoopRemoval(Value: Boolean);
procedure SetState_Name(Name: WideString);
procedure SetState_OverrideColorForDraw(Value: Boolean);
procedure ShowNetConnects;
procedure SubnetIndices_Reset;
procedure SubnetIndices_Set;

## IPCB_Net2
继承：IPCB_Net2 → IPCB_Net → IPCB_Group → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 9 个方法、0 个属性

function GetPCBDifferentialPair: IPCB_DifferentialPair2;
function GetState_Calculated_Topology: TNetTopology;
function GetState_DelayTotal: Double;
function GetState_EstimatedLength: Int64;
function GetState_ManhattanLength: Int64;
function GetState_RoutedLength64: Int64;
function GetState_SignalDelay: Double;
function GetState_SignalLength: Int64;
procedure SetSelection_PrimitivesInNet(ASelected: Boolean);

## IPCB_NetList
继承：IPCB_NetList → IInterface ｜ 单元：RT_PCB ｜ 自有 2 个方法、2 个属性

property Count: Integer read GetCount;  // read-only
property NetByIndex[AIndex: Integer]: IPCB_Net read GetNetByIndex;  // read-only
function GetCount: Integer;
function GetNetByIndex(AIndex: Integer): IPCB_Net;

## IPCB_NetsToIgnoreRule
继承：IPCB_NetsToIgnoreRule → IPCB_Rule → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 0 个方法、0 个属性


## IPCB_OLEMetadata
继承：IPCB_OLEMetadata → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 10 个方法、0 个属性

procedure CloseOLEEditor(const SaveChanges: LongBool);
function GetState_LocationX: Integer;
function GetState_LocationY: Integer;
function GetState_Rotation: Double;
procedure Invalidate;
procedure RebuildAfterUpdate;
procedure SetState_LocationX(const ANewValue: Integer);
procedure SetState_LocationY(const ANewValue: Integer);
procedure SetState_Rotation(const ANewValue: Double);
procedure ShowOLEEditor;

## IPCB_ObjectClass
继承：IPCB_ObjectClass → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 16 个方法、4 个属性

property MemberKind: TClassMemberKind read GetState_MemberKind write SetState_MemberKind;
property MemberName[I: Integer]: TPCBString read GetState_MemberName;  // read-only
property Name: TPCBString read GetState_Name write SetState_Name;
property SuperClass: Boolean read GetState_SuperClass write SetState_SuperClass;
procedure AddLayerMember(L: TV6_Layer);
procedure AddMember(P: IPCB_Primitive);
procedure AddMemberByName(AName: WideString);
function GetState_MemberKind: TClassMemberKind;
function GetState_MemberName(I: Integer): WideString;
function GetState_Name: WideString;
function GetState_SuperClass: Boolean;
function IsLayerMember(L: TV6_Layer): Boolean;
function IsMember(S: WideString): Boolean;
function IsValidObjectKind(P: IPCB_Primitive): Boolean;
procedure RemoveAllMembers;
procedure RemoveLayerMember(L: TV6_Layer);
procedure RemoveMember(P: IPCB_Primitive);
procedure SetState_MemberKind(Value: TClassMemberKind);
procedure SetState_Name(Value: WideString);
procedure SetState_SuperClass(Value: Boolean);

## IPCB_ObjectClass1
继承：IPCB_ObjectClass1 → IPCB_ObjectClassBase → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 5 个方法、0 个属性

procedure AddLayerMember(L: TV6_Layer);
procedure AddMemberByName(AName: WideString);
function IsLayerMember(L: TV6_Layer): Boolean;
function IsMember(S: WideString): Boolean;
procedure RemoveLayerMember(L: TV6_Layer);

## IPCB_ObjectClass2
继承：IPCB_ObjectClass2 → IPCB_ObjectClass → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 5 个方法、4 个属性

property DisplayName: TPCBString read GetState_DisplayName;  // read-only
property MemberNameEx[Kind: TClassMemberKind; I: Integer]: TPCBString read GetState_MemberName;  // read-only
property MembersCount: Integer read GetState_MembersCount;  // read-only
property MembersCountByKind[Kind: TClassMemberKind]: Integer read GetState_MembersCountByKind;  // read-only
function GetState_DisplayName: WideString;
function GetState_MemberName(Kind: TClassMemberKind; I: Integer): WideString;
function GetState_MembersCount: Integer;
function GetState_MembersCountByKind(Kind: TClassMemberKind): Integer;
function IsMember(P: IPCB_Primitive): Boolean;

## IPCB_ObjectClassBase
继承：IPCB_ObjectClassBase → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 14 个方法、5 个属性

property DisplayName: TPCBString read GetState_DisplayName write SetState_DisplayName;
property MemberKind: TClassMemberKind read GetState_MemberKind write SetState_MemberKind;
property MembersCount: Integer read GetState_MembersCount;  // read-only
property Name: TPCBString read GetState_Name write SetState_Name;
property SuperClass: Boolean read GetState_SuperClass write SetState_SuperClass;
procedure AddMember(P: IPCB_Primitive);
function GetState_DisplayName: WideString;
function GetState_MemberKind: TClassMemberKind;
function GetState_MembersCount: Integer;
function GetState_Name: WideString;
function GetState_SuperClass: Boolean;
function IsMember(P: IPCB_Primitive): Boolean;
function IsValidObjectKind(P: IPCB_Primitive): Boolean;
procedure RemoveAllMembers;
procedure RemoveMember(P: IPCB_Primitive);
procedure SetState_DisplayName(Value: WideString);
procedure SetState_MemberKind(Value: TClassMemberKind);
procedure SetState_Name(Value: WideString);
procedure SetState_SuperClass(Value: Boolean);

## IPCB_OnIdleNotification
继承：IPCB_OnIdleNotification → IInterface ｜ 单元：RT_PCB ｜ 自有 2 个方法、0 个属性

procedure RegisterHandlerNotification(const AHandler: INotificationHandler);
procedure UnRegisterHandlerNotification(const AHandler: INotificationHandler);

## IPCB_OptionsList
继承：IPCB_OptionsList → IInterface ｜ 单元：RT_PCB ｜ 自有 4 个方法、0 个属性

procedure Delete(Options: IPCB_AbstractOptions);
function GetState_OptionSet(ObjectId: TOptionsObjectId): IPCB_AbstractOptions;
procedure Insert(Options: IPCB_AbstractOptions);
function MemoryUsed: Integer;

## IPCB_OriginalDimension
继承：IPCB_OriginalDimension → IPCB_Dimension → IPCB_Group → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 9 个方法、0 个属性

function Text: IPCB_Text;
function Track1: IPCB_Primitive;
function Track2: IPCB_Primitive;
function Track3: IPCB_Primitive;
function Track4: IPCB_Primitive;
function Track5: IPCB_Primitive;
function Track6: IPCB_Primitive;
function Track7: IPCB_Primitive;
function Track8: IPCB_Primitive;

## IPCB_OutputConverter
继承：IPCB_OutputConverter → IInterface ｜ 单元：RT_PCB ｜ 自有 3 个方法、1 个属性

property SubstituteFonts: Boolean read GetState_SubstituteFonts;  // read-only
function Convert(const AText: IPCB_Text; out AConvertedString: WideString): Boolean;
function GetState_SubstituteFonts: Boolean;
function StringDimensions(const aString: WideString; Size: Integer; Font: SmallInt; Mirror: Boolean; out Width: Integer; out Height: Integer): Boolean;

## IPCB_OutputOptions
继承：IPCB_OutputOptions → IPCB_AbstractOptions → IInterface ｜ 单元：RT_PCB ｜ 自有 26 个方法、10 个属性

property BottomLayerOnPadMaster: Boolean read GetState_BottomLayerOnPadMaster write SetState_BottomLayerOnPadMaster;
property DrillDrawSymbolSize: TCoord read GetState_DrillDrawSymbolSize write SetState_DrillDrawSymbolSize;
property DrillGuideHoleSize: TCoord read GetState_DrillGuideHoleSize write SetState_DrillGuideHoleSize;
property DrillSymbolKind: TDrillSymbol read GetState_DrillSymbolKind write SetState_DrillSymbolKind;
property FlipLayer[PL: TV6_PlotLayer]: Boolean read GetState_FlipLayer write SetState_FlipLayer;
property IncludeUnconnectedPads: Boolean read GetState_IncludeUnconnectedPads write SetState_IncludeUnconnectedPads;
property IncludeViasInSolderMask: Boolean read GetState_IncludeViasInSolderMask write SetState_IncludeViasInSolderMask;
property MultiLayerOnPadMaster: Boolean read GetState_MultiLayerOnPadMaster write SetState_MultiLayerOnPadMaster;
property PlotLayer[PL: TV6_PlotLayer]: Boolean read GetState_PlotLayer write SetState_PlotLayer;
property TopLayerOnPadMaster: Boolean read GetState_TopLayerOnPadMaster write SetState_TopLayerOnPadMaster;
procedure Export_ToParameters_GeneralOptions(Parameters: PWideChar);
procedure Export_ToParameters_LayerOptions(Parameters: PWideChar);
procedure Export_ToParameters_LayerOptions_Version3(Parameters: PWideChar);
function GetState_BottomLayerOnPadMaster: Boolean;
function GetState_DrillDrawSymbolSize: Integer;
function GetState_DrillGuideHoleSize: Integer;
function GetState_DrillSymbolKind: TDrillSymbol;
function GetState_FlipLayer(PL: TV6_PlotLayer): Boolean;
function GetState_IncludeUnconnectedPads: Boolean;
function GetState_IncludeViasInSolderMask: Boolean;
function GetState_MultiLayerOnPadMaster: Boolean;
function GetState_PlotLayer(PL: TV6_PlotLayer): Boolean;
function GetState_TopLayerOnPadMaster: Boolean;
procedure Import_FromParameters_GeneralOptions(DisplayUnit: TUnit; Parameters: PWideChar);
procedure Import_FromParameters_LayerOptions(Parameters: PWideChar);
procedure Import_FromParameters_LayerOptions_Version3(Parameters: PWideChar);
procedure SetState_BottomLayerOnPadMaster(Value: Boolean);
procedure SetState_DrillDrawSymbolSize(Value: Integer);
procedure SetState_DrillGuideHoleSize(Value: Integer);
procedure SetState_DrillSymbolKind(Value: TDrillSymbol);
procedure SetState_FlipLayer(PL: TV6_PlotLayer; Value: Boolean);
procedure SetState_IncludeUnconnectedPads(Value: Boolean);
procedure SetState_IncludeViasInSolderMask(Value: Boolean);
procedure SetState_MultiLayerOnPadMaster(Value: Boolean);
procedure SetState_PlotLayer(PL: TV6_PlotLayer; Value: Boolean);
procedure SetState_TopLayerOnPadMaster(Value: Boolean);

## IPCB_OverlayLayer
继承：IPCB_OverlayLayer → IPCB_PhysicalLayer → IPCB_LayerObject → IInterface ｜ 单元：RT_PCB ｜ 自有 0 个方法、0 个属性


## IPCB_Pad
继承：IPCB_Pad → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 90 个方法、42 个属性

property BotShape: TShape read GetState_BotShape write SetState_BotShape;
property BotXSize: TCoord read GetState_BotXSize write SetState_BotXSize;
property BotYSize: TCoord read GetState_BotYSize write SetState_BotYSize;
property Cache: TPadCache read GetState_Cache write SetState_Cache;
property DrillType: TExtendedDrillType read GetState_DrillType write SetState_DrillType;
property HoleNegativeTolerance: TCoord read GetState_HoleNegativeTolerance write SetState_HoleNegativeTolerance;
property HolePositiveTolerance: TCoord read GetState_HolePositiveTolerance write SetState_HolePositiveTolerance;
property HoleRotation: TAngle read GetState_HoleRotation write SetState_HoleRotation;
property HoleSize: TCoord read GetState_HoleSize write SetState_HoleSize;
property HoleType: TExtendedHoleType read GetState_HoleType write SetState_HoleType;
property HoleWidth: TCoord read GetState_HoleWidth write SetState_HoleWidth;
property IsConnectedToPlane[Layer: TV6_Layer]: Boolean read GetState_IsConnectedToPlane write SetState_IsConnectedToPlane;
property JumperID: Integer read GetState_JumperID write SetState_JumperID;
property MidShape: TShape read GetState_MidShape write SetState_MidShape;
property MidXSize: TCoord read GetState_MidXSize write SetState_MidXSize;
property MidYSize: TCoord read GetState_MidYSize write SetState_MidYSize;
property Mode: TPadMode read GetState_Mode write SetState_Mode;
property Name: TPCBString read GetState_Name write SetState_Name;
property OwnerPart_ID: Integer read GetState_OwnerPart_ID write SetState_OwnerPart_ID;
property PinDescriptor: TPCBString read GetState_PinDescriptorString;  // read-only
property Plated: Boolean read GetState_Plated write SetState_Plated;
property Rotation: TAngle read GetState_Rotation write SetState_Rotation;
property ShapeOnLayer[L: Integer]: TShape read GetState_ShapeOnLayer;  // read-only
property SolderMaskExpansionFromHoleEdge: Boolean read GetState_SolderMaskExpansionFromHoleEdge write SetState_SolderMaskExpansionFromHoleEdge;
property StackShapeOnLayer[L: Integer]: TShape read GetState_StackShapeOnLayer write SetState_StackShapeOnLayer;
property SwapID_Pad: TPCBString read GetState_SwapID_Pad write SetState_SwapID_Pad;
property SwapID_Part: TPCBString read GetState_SwapID_Part write SetState_SwapID_Part;
property SwappedPadName: TPCBString read GetState_SwappedPadName write SetState_SwappedPadName;
property TemplateLink: IPCB_PadViaTemplateLink read GetState_TemplateLink;  // read-only
property TopShape: TShape read GetState_TopShape write SetState_TopShape;
property TopXSize: TCoord read GetState_TopXSize write SetState_TopXSize;
property TopYSize: TCoord read GetState_TopYSize write SetState_TopYSize;
property Width[L: TV6_Layer]: TCoord read GetState_WidthOnLayer;  // read-only
property WidthOnLayer[L: TV6_Layer]: TCoord read GetState_WidthOnLayer;  // read-only
property x: TCoord read GetState_XLocation write SetState_XLocation;
property XPadOffset[L: TV6_Layer]: TCoord read GetState_XPadOffsetOnLayer write SetState_XPadOffsetOnLayer;
property XSizeOnLayer[L: Integer]: TCoord read GetState_XSizeOnLayer;  // read-only
property XStackSizeOnLayer[L: Integer]: TCoord read GetState_XStackSizeOnLayer write SetState_XStackSizeOnLayer;
property y: TCoord read GetState_YLocation write SetState_YLocation;
property YPadOffset[L: TV6_Layer]: TCoord read GetState_YPadOffsetOnLayer write SetState_YPadOffsetOnLayer;
property YSizeOnLayer[L: Integer]: TCoord read GetState_YSizeOnLayer;  // read-only
property YStackSizeOnLayer[L: Integer]: TCoord read GetState_YStackSizeOnLayer write SetState_YStackSizeOnLayer;
function BoundingRectangleOnLayer(ALayer: TV6_Layer): IDispatch;
procedure ClearStackSizeAndShapes;
function DefinitionLayerIterator: IPCB_LayerIterator;
function GetState_BotShape: TShape;
function GetState_BotXSize: Integer;
function GetState_BotYSize: Integer;
function GetState_Cache: IDispatch;
function GetState_DrillType: TExtendedDrillType;
function GetState_HoleNegativeTolerance: Integer;
function GetState_HolePositiveTolerance: Integer;
function GetState_HoleRotation: Double;
function GetState_HoleSize: Integer;
function GetState_HoleType: TExtendedHoleType;
function GetState_HoleWidth: Integer;
function GetState_IsConnectedToPlane(Layer: TV6_Layer): Boolean;
function GetState_JumperID: Integer;
function GetState_MidShape: TShape;
function GetState_MidXSize: Integer;
function GetState_MidYSize: Integer;
function GetState_Mode: TPadMode;
function GetState_Name: WideString;
function GetState_OwnerPart_ID: Integer;
function GetState_PinDescriptorString: WideString;
function GetState_Plated: Boolean;
function GetState_Rotation: Double;
function GetState_ShapeOnLayer(L: Integer): TShape;
function GetState_SolderMaskExpansionFromHoleEdge: Boolean;
function GetState_StackShapeOnLayer(L: Integer): TShape;
function GetState_SwapID_Pad: WideString;
function GetState_SwapID_Part: WideString;
function GetState_SwappedPadName: WideString;
function GetState_TemplateLink: IPCB_PadViaTemplateLink;
function GetState_TopShape: TShape;
function GetState_TopXSize: Integer;
function GetState_TopYSize: Integer;
function GetState_WidthOnLayer(L: TV6_Layer): Integer;
function GetState_XLocation: Integer;
function GetState_XPadOffsetOnLayer(L: TV6_Layer): Integer;
function GetState_XSizeOnLayer(L: Integer): Integer;
function GetState_XStackSizeOnLayer(L: Integer): Integer;
function GetState_YLocation: Integer;
function GetState_YPadOffsetOnLayer(L: TV6_Layer): Integer;
function GetState_YSizeOnLayer(L: Integer): Integer;
function GetState_YStackSizeOnLayer(L: Integer): Integer;
procedure InvalidateCache;
procedure InvalidateSizeShape;
function IsPadStack: Boolean;
function IsSurfaceMount: Boolean;
function IsVirtualPin: Boolean;
function PlaneConnectionStyleForLayer(ALayer: TV6_Layer): TPlaneConnectionStyle;
procedure ReValidateSizeShape;
procedure RotateAroundXY(AX: Integer; AY: Integer; Angle: Double);
procedure SetState_BotShape(Value: TShape);
procedure SetState_BotXSize(Value: Integer);
procedure SetState_BotYSize(Value: Integer);
procedure SetState_Cache(const Value: IDispatch);
procedure SetState_DrillType(DrillType: TExtendedDrillType);
procedure SetState_HoleNegativeTolerance(Value: Integer);
procedure SetState_HolePositiveTolerance(Value: Integer);
procedure SetState_HoleRotation(HRotation: Double);
procedure SetState_HoleSize(Value: Integer);
procedure SetState_HoleType(HoleType: TExtendedHoleType);
procedure SetState_HoleWidth(HoleWidth: Integer);
procedure SetState_IsConnectedToPlane(Layer: TV6_Layer; Value: Boolean);
procedure SetState_JumperID(Value: Integer);
procedure SetState_MidShape(Value: TShape);
procedure SetState_MidXSize(Value: Integer);
procedure SetState_MidYSize(Value: Integer);
procedure SetState_Mode(Mode: TPadMode);
procedure SetState_Name(Value: WideString);
procedure SetState_OwnerPart_ID(Value: Integer);
procedure SetState_Plated(Value: Boolean);
procedure SetState_Rotation(Value: Double);
procedure SetState_SolderMaskExpansionFromHoleEdge(AValue: Boolean);
procedure SetState_StackShapeOnLayer(L: Integer; Value: TShape);
procedure SetState_SwapID_Pad(Value: WideString);
procedure SetState_SwapID_Part(Value: WideString);
procedure SetState_SwappedPadName(Value: WideString);
procedure SetState_TopShape(Value: TShape);
procedure SetState_TopXSize(Value: Integer);
procedure SetState_TopYSize(Value: Integer);
procedure SetState_XLocation(AX: Integer);
procedure SetState_XPadOffsetOnLayer(L: TV6_Layer; XOffset: Integer);
procedure SetState_XStackSizeOnLayer(L: Integer; Value: Integer);
procedure SetState_YLocation(AY: Integer);
procedure SetState_YPadOffsetOnLayer(L: TV6_Layer; YOffset: Integer);
procedure SetState_YStackSizeOnLayer(L: Integer; Value: Integer);
function SolderMaskExpansionFromHoleEdgeWithRule: Boolean;
procedure UpdateCache;
procedure ValidateSizeShape;

## IPCB_Pad2
继承：IPCB_Pad2 → IPCB_Pad → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 6 个方法、4 个属性

property CornerRadius[L: Integer]: TCoord read GetState_CornerRadiusOnLayer;  // read-only
property CRPercentage[L: Integer]: Byte read GetState_CRPercentageOnLayer;  // read-only
property PinPackageLength: TCoord read GetState_PinPackageLength write SetState_PinPackageLength;
property StackCRPctOnLayer[L: Integer]: Byte read GetState_StackCRPctOnLayer write SetState_StackCRPctOnLayer;
function GetState_CornerRadiusOnLayer(L: Integer): Integer;
function GetState_CRPercentageOnLayer(L: Integer): Byte;
function GetState_PinPackageLength: Integer;
function GetState_StackCRPctOnLayer(L: Integer): Byte;
procedure SetState_PinPackageLength(Value: Integer);
procedure SetState_StackCRPctOnLayer(L: Integer; Value: Byte);

## IPCB_Pad3
继承：IPCB_Pad3 → IPCB_Pad2 → IPCB_Pad → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 32 个方法、11 个属性

property BoardRegion: IPCB_BoardRegion read GetState_BoardRegion;  // read-only
property CounterHoles: IPCB_CounterHoleParamsList read GetProperty_CounterHoles write SetProperty_CounterHoles;
property DaisyChainStyle: TDaisyChainStyle read GetState_DaisyChainStyle write SetState_DaisyChainStyle;
property IsHoleStraddling[const ALayer: IDispatch]: Boolean read GetState_IsHoleStraddling write SetState_IsHoleStraddling;
property IsPadRemoved[ALayer: Integer]: Boolean read GetState_IsPadRemoved write SetState_IsPadRemoved;
property MaxXSignalLayers: TCoord read GetState_MaxXSignalLayers;  // read-only
property MaxYSignalLayers: TCoord read GetState_MaxYSignalLayers;  // read-only
property MultiLayerHighBits: Word read GetState_MultiLayerHighBits write SetState_MultiLayerHighBits;
property SplitPlanes[const IntPlaneLayer: IDispatch]: IPCB_SplitPlane read GetProperty_SplitPlanes write SetProperty_SplitPlanes;
property XPadOffsetAll: TCoord read GetState_XPadOffsetAllLayers write SetState_XPadOffsetAllLayers;
property YPadOffsetAll: TCoord read GetState_YPadOffsetAllLayers write SetState_YPadOffsetAllLayers;
procedure EditShapeOnLayer(ALayer: Integer);
function GetCounterHoleDiameters: IPCB_CounterHoleDiameterOnDepthList;
function GetFirstBottomCounterHole: IPCB_CounterHoleParams;
function GetFirstTopCounterHole: IPCB_CounterHoleParams;
function GetHoleXSize: Integer;
function GetHoleYSize: Integer;
function GetProperty_CounterHoles: IPCB_CounterHoleParamsList;
function GetProperty_SplitPlanes(const IntPlaneLayer: IDispatch): IPCB_SplitPlane;
function GetState_BoardRegion: IPCB_BoardRegion;
function GetState_DaisyChainStyle: TDaisyChainStyle;
function GetState_HoleString: WideString;
function GetState_IsHoleStraddling(const ALayer: IDispatch): Boolean;
function GetState_IsPadRemoved(ALayer: Integer): Boolean;
function GetState_MaxXSignalLayers: Integer;
function GetState_MaxYSignalLayers: Integer;
function GetState_MultiLayerHighBits: Word;
function GetState_XPadOffsetAllLayers: Integer;
function GetState_YPadOffsetAllLayers: Integer;
function IsCounterHole: Boolean;
function IsHoleSizeValid: Boolean;
procedure RemoveUnusedPads(PreserveStartEnd: Boolean);
procedure RestoreUnusedPads;
procedure SetProperty_CounterHoles(const AValue: IPCB_CounterHoleParamsList);
procedure SetProperty_SplitPlanes(const IntPlaneLayer: IDispatch; ASplitPlane: IPCB_SplitPlane);
procedure SetState_DaisyChainStyle(ANewValue: TDaisyChainStyle);
procedure SetState_IsHoleStraddling(const ALayer: IDispatch; AValue: Boolean);
procedure SetState_IsPadRemoved(ALayer: Integer; AValue: Boolean);
procedure SetState_MultiLayerHighBits(AValue: Word);
procedure SetState_XPadOffsetAllLayers(ANewValue: Integer);
procedure SetState_YPadOffsetAllLayers(ANewValue: Integer);
procedure UntieCounterHoles;
procedure UpdateCounterHoles;

## IPCB_Pad4
继承：IPCB_Pad4 → IPCB_Pad3 → IPCB_Pad2 → IPCB_Pad → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 1 个方法、1 个属性

property HoleSizeOnLayer[ALayer: Integer]: TCoord read GetProperty_HoleSizeOnLayer;  // read-only
function GetProperty_HoleSizeOnLayer(ALayer: Integer): Integer;

## IPCB_PadTemplate
继承：IPCB_PadTemplate → IPCB_PadViaTemplate → IInterface ｜ 单元：RT_PCB ｜ 自有 0 个方法、0 个属性


## IPCB_PadViaLibrary
继承：IPCB_PadViaLibrary → IInterface ｜ 单元：RT_PCB ｜ 自有 18 个方法、7 个属性

property Activated: Boolean read GetState_Activated write SetState_Activated;
property Count: Integer read GetState_Count;  // read-only
property DisplayUnits: TUnit read GetState_DisplayUnits write SetState_DisplayUnits;
property LibraryID: WideString read GetState_LibraryID;  // read-only
property LibraryName: WideString read GetState_LibraryName;  // read-only
property LibraryPath: WideString read GetState_LibraryPath;  // read-only
property Templates[AIndex: Integer]: IPCB_PadViaTemplate read GetState_Template;  // read-only
function AddExternalTemplate(const ATemplate: IPCB_PadViaTemplate): IPCB_PadViaTemplate;
procedure AddTemplate(const APrimitive: IPCB_Primitive);
function CheckDublicate(const ATemplate: IPCB_PadViaTemplate): Boolean;
procedure Clear;
procedure CopyTo(const ADest: IPCB_PadViaLibrary);
procedure DeleteTemplate(AIndex: Integer);
function FindTemplate(const ATemplate: WideString): IPCB_PadViaTemplate;
function GetState_Activated: Boolean;
function GetState_Count: Integer;
function GetState_DisplayUnits: TUnit;
function GetState_LibraryID: WideString;
function GetState_LibraryName: WideString;
function GetState_LibraryPath: WideString;
function GetState_Template(AIndex: Integer): IPCB_PadViaTemplate;
function I_ObjectAddress: Pointer;
function RemoveTemplate(const ATemplate: IPCB_PadViaTemplate): Boolean;
procedure SetState_Activated(AValue: Boolean);
procedure SetState_DisplayUnits(AValue: TUnit);

## IPCB_PadViaLibraryDocument
继承：IPCB_PadViaLibraryDocument → IServerDocument → IInterface ｜ 单元：RT_PCB ｜ 自有 6 个方法、3 个属性

property CurrentTemplate: IPCB_PadViaTemplate read GetState_CurrentTemplate write SetState_CurrentTemplate;
property DisplayUnits: TUnit read GetState_DisplayUnits write SetState_DisplayUnits;
property PadViaLibrary: IPCB_PadViaLibrary read GetState_PadViaLibrary;  // read-only
function GetState_CurrentTemplate: IPCB_PadViaTemplate;
function GetState_DisplayUnits: TUnit;
function GetState_PadViaLibrary: IPCB_PadViaLibrary;
procedure NavigateFirst;
procedure SetState_CurrentTemplate(AValue: IPCB_PadViaTemplate);
procedure SetState_DisplayUnits(AValue: TUnit);

## IPCB_PadViaLibraryManager
继承：IPCB_PadViaLibraryManager → IInterface ｜ 单元：RT_PCB ｜ 自有 19 个方法、1 个属性

property NeedUpdate: Boolean read GetNeedUpdate write SetNeedUpdate;
function AddRemoveLibraries(const ABoard: IPCB_Board): WideString;
function CreateTemplate(AObjectId: TObjectId): IPCB_PadViaTemplate;
procedure ExchangeTemplatesOnPrimitives(ABoard: IPCB_Primitive; AOldTemplate: IPCB_PadViaTemplate; ANewTemplate: IPCB_PadViaTemplate; ANeedUpdate: Boolean);
function FindLibrary(const ABoard: IPCB_Board; const ALibraryID: WideString): IPCB_PadViaLibrary;
function GetInstalledLibrary(I: Integer): IPCB_PadViaLibrary;
function GetInstalledLibraryCount: Integer;
function GetLibraryName(const APrimitive: IPCB_Primitive): WideString;
function GetLinkedToLibrary(const APrimitive: IPCB_Primitive): WordBool;
function GetNeedUpdate: Boolean;
function GetTemplateNameWithDynamicName(ATemplate: IPCB_PadViaTemplate): WideString;
procedure InstallLibrary(const APath: WideString);
procedure LibrariesModified;
procedure LockUpdates;
procedure PlaceTemplate(const ABoard: IPCB_Primitive; const ATemplate: IPCB_PadViaTemplate);
procedure PlaceTemplateFromParameters(const ABoard: IPCB_Primitive; const Parameters: IParameterList);
procedure SetNeedUpdate(AValue: Boolean);
procedure UninstallLibrary(APvLib: IPCB_PadViaLibrary);
procedure UnlockUpdates;
procedure UpdateViews;

## IPCB_PadViaPainterView
继承：IPCB_PadViaPainterView → IInterface ｜ 单元：RT_PCB ｜ 自有 17 个方法、0 个属性

procedure ClearGraphicalObjects;
procedure ConfigView(Parameters: WideString);
function GetDummyBoard: IPCB_Board;
function GetIs3D: Boolean;
procedure GetState_BkColor(out r: Byte; out g: Byte; out b: Byte);
function GetState_SelectedLayer: Integer;
procedure KeyDown(var Key: Word; Shift: TShiftState);
procedure MouseWheel(Sender: TObject; Shift: TShiftState; WheelDelta: Integer; const MousePos: IDispatch; var Handled: Boolean);
procedure RefreshView;
procedure RegisterGOMouseHoverHandler(GraphicalObjectMouseHoverHandler: IPCB_GOMouseHoverHandler);
procedure SetAllLayersVisibilityState(Visible: Boolean);
procedure SetCamera(LowX: Integer; LowY: Integer; HighX: Integer; HighY: Integer);
procedure SetDirectXMode;
procedure SetPadViaByHandle(const APad: IPCB_Primitive);
procedure SetState_BkColor(r: Byte; g: Byte; b: Byte);
procedure SetViewRect(LowX: Integer; LowY: Integer; HighX: Integer; HighY: Integer);
procedure UpdatePrimitive;

## IPCB_PadViaTemplate
继承：IPCB_PadViaTemplate → IInterface ｜ 单元：RT_PCB ｜ 自有 25 个方法、12 个属性

property ExternalLink: IPCB_PadViaTemplateLink read GetState_ExternalLink;  // read-only
property Internal: Boolean read GetState_Internal write SetState_Internal;
property IsBackdrill: Boolean read GetState_IsBackdrill;  // read-only
property LibraryID: WideString read GetState_LibraryID write SetState_LibraryID;
property ObjectId: TObjectId read GetState_ObjectID;  // read-only
property ObjectIDString: WideString read GetState_ObjectIDString;  // read-only
property PrimLinkCount: Integer read GetState_PrimLinkCount;  // read-only
property RemoveUnused: Boolean read GetState_RemoveUnused write SetState_RemoveUnused;
property RevisionID: WideString read GetState_RevisionID write SetState_RevisionID;
property TemplateDescription: WideString read GetState_TemplateDescription write SetState_TemplateDescription;
property TemplateID: WideString read GetState_TemplateID write SetState_TemplateID;
property TemplateName: WideString read GetState_TemplateName write SetState_TemplateName;
procedure CopyTo(ADest: IPCB_PadViaTemplate; ACopyMode: TCopyMode);
function CreatePrimitive: IPCB_Primitive;
function CreateTemplateLink: IPCB_PadViaTemplateLink;
function GetFullTemplateID: WideString;
function GetState_ExternalLink: IPCB_PadViaTemplateLink;
function GetState_Internal: Boolean;
function GetState_IsBackdrill: Boolean;
function GetState_LibraryID: WideString;
function GetState_ObjectID: TObjectId;
function GetState_ObjectIDString: WideString;
function GetState_PrimLinkCount: Integer;
function GetState_RemoveUnused: Boolean;
function GetState_RevisionID: WideString;
function GetState_TemplateDescription: WideString;
function GetState_TemplateID: WideString;
function GetState_TemplateName: WideString;
function HasLocalChanges(APrimitive: IPCB_Primitive): Boolean;
function I_ObjectAddress: Pointer;
procedure SetState_Internal(AValue: Boolean);
procedure SetState_LibraryID(const AValue: WideString);
procedure SetState_RemoveUnused(AValue: Boolean);
procedure SetState_RevisionID(const AValue: WideString);
procedure SetState_TemplateDescription(const AValue: WideString);
procedure SetState_TemplateID(const AValue: WideString);
procedure SetState_TemplateName(const AValue: WideString);

## IPCB_PadViaTemplateLink
继承：IPCB_PadViaTemplateLink → IInterface ｜ 单元：RT_PCB ｜ 自有 9 个方法、3 个属性

property LibraryID: WideString read GetState_LibraryID write SetState_LibraryID;
property RevisionID: WideString read GetState_RevisionID write SetState_RevisionID;
property TemplateID: WideString read GetState_TemplateID write SetState_TemplateID;
procedure Clear;
procedure CopyTo(ADest: IPCB_PadViaTemplateLink);
function GetFullTemplateID: WideString;
function GetState_LibraryID: WideString;
function GetState_RevisionID: WideString;
function GetState_TemplateID: WideString;
procedure SetState_LibraryID(const AValue: WideString);
procedure SetState_RevisionID(const AValue: WideString);
procedure SetState_TemplateID(const AValue: WideString);

## IPCB_ParallelSegmentConstraint
继承：IPCB_ParallelSegmentConstraint → IPCB_Rule → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 4 个方法、2 个属性

property Gap: TCoord read GetState_Gap write SetState_Gap;
property Limit: TCoord read GetState_Limit write SetState_Limit;
function GetState_Gap: Integer;
function GetState_Limit: Integer;
procedure SetState_Gap(Value: Integer);
procedure SetState_Limit(Value: Integer);

## IPCB_Parameter
继承：IPCB_Parameter → IInterface ｜ 单元：RT_PCB ｜ 自有 7 个方法、4 个属性

property Attributes: IPCB_ParameterAttributes read GetAttributes;  // read-only
property IsInherited: Boolean read GetIsInherited write SetIsInherited;
property Name: TPCBString read GetName write SetName;
property Value: TPCBString read GetValue write SetValue;
function GetAttributes: IPCB_ParameterAttributes;
function GetIsInherited: Boolean;
function GetName: WideString;
function GetValue: WideString;
procedure SetIsInherited(AValue: Boolean);
procedure SetName(const AValue: WideString);
procedure SetValue(const AValue: WideString);

## IPCB_ParameterAttributes
继承：IPCB_ParameterAttributes → IInterface ｜ 单元：RT_PCB ｜ 自有 5 个方法、1 个属性

property Attribute[const AName: WideString]: TPCBString read GetAttribute write SetAttribute;
function GetAttribute(const AName: WideString): WideString;
function HasAttribute(const AName: WideString): Boolean;
procedure ResetAllAttributes;
procedure ResetAttribute(const AName: WideString);
procedure SetAttribute(const AName: WideString; const AValue: WideString);

## IPCB_ParameterList
继承：IPCB_ParameterList → IInterface ｜ 单元：RT_PCB ｜ 自有 9 个方法、3 个属性

property ByIndex[AIndex: Integer]: IPCB_Parameter read GetByIndex write SetByIndex;
property ByName[const AName: WideString]: IPCB_Parameter read GetByName;  // read-only
property Count: Integer read GetCount;  // read-only
procedure Clear;
function FindByName(const AName: WideString): IPCB_Parameter;
function GetByIndex(AIndex: Integer): IPCB_Parameter;
function GetByName(const AName: WideString): IPCB_Parameter;
function GetCount: Integer;
procedure RemoveByIndex(AIndex: Integer);
procedure RemoveByName(const AName: WideString);
procedure SetByIndex(AIndex: Integer; const AParameter: IPCB_Parameter);
function TryRemoveByName(const AName: WideString): Boolean;

## IPCB_ParametersFactory
继承：IPCB_ParametersFactory → IInterface ｜ 单元：RT_PCB ｜ 自有 3 个方法、0 个属性

function CreateParameterList: IPCB_ParameterList;
function CreateParameterNameValue(const AName: WideString; const AValue: WideString): IPCB_Parameter;
function CreatePrimitiveParametersOfVariant(const APrimitive: IPCB_Primitive; const AVariantName: WideString): IPCB_PrimitiveParameters;

## IPCB_PasteMaskExpansionRule
继承：IPCB_PasteMaskExpansionRule → IPCB_Rule → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 8 个方法、4 个属性

property Expansion: TCoord read GetState_Expansion write SetState_Expansion;
property Percent: Double read GetState_Percent write SetState_Percent;
property UsePaste: Boolean read GetState_UsePaste write SetState_UsePaste;
property UsePercent: Boolean read GetState_UsePercent write SetState_UsePercent;
function GetState_Expansion: Integer;
function GetState_Percent: Double;
function GetState_UsePaste: Boolean;
function GetState_UsePercent: Boolean;
procedure SetState_Expansion(Value: Integer);
procedure SetState_Percent(const Value: Double);
procedure SetState_UsePaste(Value: Boolean);
procedure SetState_UsePercent(const Value: Boolean);

## IPCB_PasteMaskLayer
继承：IPCB_PasteMaskLayer → IPCB_PhysicalLayer → IPCB_LayerObject → IInterface ｜ 单元：RT_PCB ｜ 自有 0 个方法、0 个属性


## IPCB_PermittedLayersRule
继承：IPCB_PermittedLayersRule → IPCB_Rule → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 2 个方法、1 个属性

property PermittedLayers: TV6_LayerSet read GetState_PermittedLayers write SetState_PermittedLayers;
function GetState_PermittedLayers: TV6_LayerSet;
procedure SetState_PermittedLayers(Value: TV6_LayerSet);

## IPCB_PhysicalLayer
继承：IPCB_PhysicalLayer → IPCB_LayerObject → IInterface ｜ 单元：RT_PCB ｜ 自有 0 个方法、0 个属性


## IPCB_PhysicalLayer2
继承：IPCB_PhysicalLayer2 → IPCB_LayerObject → IInterface ｜ 单元：RT_PCB ｜ 自有 4 个方法、2 个属性

property ElectricalResistivity: Double read GetElectricalResistivity write SetElectricalResistivity;
property IsAdditiveLayer: Boolean read GetIsAdditiveLayer write SetIsAdditiveLayer;
function GetElectricalResistivity: Double;
function GetIsAdditiveLayer: Boolean;
procedure SetElectricalResistivity(const AValue: Double);
procedure SetIsAdditiveLayer(const AValue: Boolean);

## IPCB_PinPair
继承：IPCB_PinPair → IInterface ｜ 单元：RT_PCB ｜ 自有 19 个方法、11 个属性

property Color: TColor read GetState_Color write SetState_Color;
property DelayTotal: Double read GetState_DelayTotal;  // read-only
property Length: Int64 read GetState_Length;  // read-only
property Name: WideString read GetState_Name write SetState_Name;
property NodeCount: Integer read GetState_NodeCount;  // read-only
property OverrideColorForDraw: Boolean read GetState_OverrideColorForDraw write SetState_OverrideColorForDraw;
property PinPackageLength: Int64 read GetState_PinPackageLength;  // read-only
property Primitives[Index: Integer]: IPCB_Primitive read GetPrimitives;  // read-only
property PrimitivesCount: Integer read GetState_PrimitivesCount;  // read-only
property RoutedLength: Int64 read GetState_RoutedLength;  // read-only
property UnroutedLength: Int64 read GetState_UnroutedLength;  // read-only
function CastToPrimitive: IPCB_Primitive;
function GetPinPairItemDisplayName(Prim: IPCB_Primitive): WideString;
function GetPrimitives(Index: Integer): IPCB_Primitive;
function GetState_Color: Cardinal;
function GetState_DelayTotal: Double;
function GetState_IsBroken: Boolean;
function GetState_Length: Int64;
function GetState_Name: WideString;
function GetState_NodeCount: Integer;
function GetState_OverrideColorForDraw: Boolean;
function GetState_PinPackageLength: Int64;
function GetState_PrimitivesCount: Integer;
function GetState_RoutedLength: Int64;
function GetState_UnroutedLength: Int64;
function I_ObjectAddress: Pointer;
procedure Rebuild;
procedure SetState_Color(Value: Cardinal);
procedure SetState_Name(const NewName: WideString);
procedure SetState_OverrideColorForDraw(Value: Boolean);

## IPCB_PinPairTiePoint
继承：IPCB_PinPairTiePoint → IInterface ｜ 单元：RT_PCB ｜ 自有 2 个方法、2 个属性

property PinPairs: IInterfaceListEx read GetState_PinPairs;  // read-only
property TiePointPad: IPCB_Pad2 read GetState_TiePointPad;  // read-only
function GetState_PinPairs: IInterfaceListEx;
function GetState_TiePointPad: IPCB_Pad2;

## IPCB_PinPairsManager
继承：IPCB_PinPairsManager → IInterface ｜ 单元：RT_PCB ｜ 自有 12 个方法、2 个属性

property PinPairs[Index: Integer]: IPCB_PinPair read GetState_PinPairs;  // read-only
property PinPairsCount: Integer read GetState_PinPairsCount;  // read-only
procedure AssignPinPairClass(APinPairs: IInterfaceList; AClassName: WideString);
function CanCreateTiePoints(APinPairs: IInterfaceList): Boolean;
function CreateFromPins(const APins: IInterfaceList): IPCB_PinPair;
function CreateFromPinsDescriptors(const APins: WideString): IPCB_PinPair;
function CreateTiePoints(APinPairs: IInterfaceList): IInterfaceList;
procedure Delete(const APinPair: IPCB_PinPair);
function GetPinPairOf(const APrimitive: IPCB_Primitive): IPCB_PinPair;
function GetState_PinPairs(Index: Integer): IPCB_PinPair;
function GetState_PinPairsCount: Integer;
procedure InvalidateAll;
function StateID: Int64;
function SwapPins(const PinA: IPCB_Primitive; const PinB: IPCB_Primitive; const OldNetA: IPCB_Net; const OldNetB: IPCB_Net): IInterfaceList;

## IPCB_PlacementGrid
继承：IPCB_PlacementGrid → IPCB_PlacementGuide → IInterface ｜ 单元：RT_PCB ｜ 自有 25 个方法、13 个属性

property ColorLarge: TColor read GetProperty_ColorLarge write SetProperty_ColorLarge;
property ComponentGrid: Boolean read GetProperty_ComponentGrid write SetProperty_ComponentGrid;
property DisplayUnit: TUnit read GetProperty_DisplayUnit write SetProperty_DisplayUnit;
property DrawMode: TDrawGridMode read GetProperty_DrawMode write SetProperty_DrawMode;
property DrawModeLarge: TDrawGridMode read GetProperty_DrawModeLarge write SetProperty_DrawModeLarge;
property DrawMultiplier: Integer read GetProperty_DrawMultiplier write SetProperty_DrawMultiplier;
property DrawMultiplierLarge: Integer read GetProperty_DrawMultiplierLarge write SetProperty_DrawMultiplierLarge;
property Enabled: Boolean read GetProperty_Enabled write SetProperty_Enabled;
property IsDefault: Boolean read GetProperty_IsDefault;  // read-only
property Name: WideString read GetProperty_NameW write SetProperty_NameW;
property Origin: TCoordPoint read GetProperty_Origin write SetProperty_Origin;
property Priority: Cardinal read GetProperty_Priority write SetProperty_Priority;
property ShowOrigin: Boolean read GetProperty_ShowOrigin write SetProperty_ShowOrigin;
function GetProperty_ColorLarge: Cardinal;
function GetProperty_ComponentGrid: Boolean;
function GetProperty_DisplayUnit: TUnit;
function GetProperty_DrawMode: TDrawGridMode;
function GetProperty_DrawModeLarge: TDrawGridMode;
function GetProperty_DrawMultiplier: Integer;
function GetProperty_DrawMultiplierLarge: Integer;
function GetProperty_Enabled: Boolean;
function GetProperty_IsDefault: Boolean;
function GetProperty_NameW: WideString;
function GetProperty_Origin: IDispatch;
function GetProperty_Priority: Cardinal;
function GetProperty_ShowOrigin: Boolean;
procedure SetProperty_ColorLarge(const Value: Cardinal);
procedure SetProperty_ComponentGrid(Value: Boolean);
procedure SetProperty_DisplayUnit(const Value: TUnit);
procedure SetProperty_DrawMode(const Value: TDrawGridMode);
procedure SetProperty_DrawModeLarge(const Value: TDrawGridMode);
procedure SetProperty_DrawMultiplier(const Value: Integer);
procedure SetProperty_DrawMultiplierLarge(const Value: Integer);
procedure SetProperty_Enabled(Value: Boolean);
procedure SetProperty_NameW(const Value: WideString);
procedure SetProperty_Origin(const Value: IDispatch);
procedure SetProperty_Priority(const Value: Cardinal);
procedure SetProperty_ShowOrigin(const Value: Boolean);

## IPCB_PlacementGridIterator
继承：IPCB_PlacementGridIterator → IPCB_PlacementIterator → IInterface ｜ 单元：RT_PCB ｜ 自有 2 个方法、0 个属性

function First: IPCB_PlacementGrid;
function Next: IPCB_PlacementGrid;

## IPCB_PlacementGuide
继承：IPCB_PlacementGuide → IInterface ｜ 单元：RT_PCB ｜ 自有 5 个方法、2 个属性

property Color: TColor read GetProperty_Color write SetProperty_Color;
property IsMCADSource: Boolean read GetProperty_IsMCADSource;  // read-only
function GetOwnerBoard: IPCB_Board;
function GetProperty_Color: Cardinal;
function GetProperty_IsMCADSource: Boolean;
function I_ObjectAddress: Pointer;
procedure SetProperty_Color(const Value: Cardinal);

## IPCB_PlacementGuideLine
继承：IPCB_PlacementGuideLine → IPCB_RealPlacementGuide → IPCB_PlacementGuide → IInterface ｜ 单元：RT_PCB ｜ 自有 10 个方法、2 个属性

property x: Integer read GetProperty_X write SetProperty_X;
property y: Integer read GetProperty_Y write SetProperty_Y;
function GetProperty_X: Integer;
function GetProperty_Y: Integer;
function IsHorizontal: Boolean;
function IsMinus45Degrees: Boolean;
function IsPlus45Degrees: Boolean;
function IsVertical: Boolean;
procedure MoveOriginTo(const AX: Integer; const AY: Integer);
procedure SetOrigin(const x: Integer; const y: Integer);
procedure SetProperty_X(const AValue: Integer);
procedure SetProperty_Y(const AValue: Integer);

## IPCB_PlacementGuideSnapPoint
继承：IPCB_PlacementGuideSnapPoint → IPCB_RealPlacementGuide → IPCB_PlacementGuide → IInterface ｜ 单元：RT_PCB ｜ 自有 4 个方法、2 个属性

property x: Integer read GetProperty_X write SetProperty_X;
property y: Integer read GetProperty_Y write SetProperty_Y;
function GetProperty_X: Integer;
function GetProperty_Y: Integer;
procedure SetProperty_X(const AValue: Integer);
procedure SetProperty_Y(const AValue: Integer);

## IPCB_PlacementIterator
继承：IPCB_PlacementIterator → IInterface ｜ 单元：RT_PCB ｜ 自有 3 个方法、0 个属性

procedure SetFilter_IncludeDynamicGuides(AValue: Boolean);
procedure SetFilter_IncludeGrids(AValue: Boolean);
procedure SetFilter_IncludeStaticGuides(AValue: Boolean);

## IPCB_PolarGrid
继承：IPCB_PolarGrid → IPCB_PlacementGrid → IPCB_PlacementGuide → IInterface ｜ 单元：RT_PCB ｜ 自有 15 个方法、6 个属性

property AngularStep: TAngle read GetProperty_AngularStep write SetProperty_AngularStep;
property EndAngle: TAngle read GetProperty_EndAngle write SetProperty_EndAngle;
property MaxRadius: TDouble read GetProperty_MaxRadius write SetProperty_MaxRadius;
property MinRadius: TDouble read GetProperty_MinRadius write SetProperty_MinRadius;
property RadialStep: TDouble read GetProperty_RadialStep write SetProperty_RadialStep;
property StartAngle: TAngle read GetProperty_StartAngle write SetProperty_StartAngle;
procedure AngleRadiusToCoord(const Angle: Double; const Radius: Integer; out OutX: Integer; out OutY: Integer);
function CoordToAngle(const x: Integer; const y: Integer): Double;
function CoordToRadius(const x: Integer; const y: Integer): Integer;
function GetProperty_AngularStep: Double;
function GetProperty_EndAngle: Double;
function GetProperty_MaxRadius: Double;
function GetProperty_MinRadius: Double;
function GetProperty_RadialStep: Double;
function GetProperty_StartAngle: Double;
procedure SetProperty_AngularStep(const Value: Double);
procedure SetProperty_EndAngle(const Value: Double);
procedure SetProperty_MaxRadius(const Value: Double);
procedure SetProperty_MinRadius(const Value: Double);
procedure SetProperty_RadialStep(const Value: Double);
procedure SetProperty_StartAngle(const Value: Double);

## IPCB_PolarGridCoordinates
继承：IPCB_PolarGridCoordinates → IInterface ｜ 单元：RT_PCB ｜ 自有 8 个方法、0 个属性

function GetState_PolarCoordAngle: Double;
function GetState_PolarCoordAvailable: Boolean;
function GetState_PolarCoordRadius: Integer;
function GetState_PolarCoordRotation: Double;
function GetState_PolarGridName: WideString;
procedure SetState_PolarCoordAngle(const AValue: Double);
procedure SetState_PolarCoordRadius(const AValue: Integer);
procedure SetState_PolarCoordRotation(const AValue: Double);

## IPCB_PolyRegShapesClipResult
继承：IPCB_PolyRegShapesClipResult → IInterface ｜ 单元：RT_PCB ｜ 自有 3 个方法、3 个属性

property Cutouts: IPCB_Shapes read GetCutouts;  // read-only
property InoperablePrims: IPCB_Shapes read GetInoperablePrims;  // read-only
property NewPrims: IPCB_Shapes read GetNewPrims;  // read-only
function GetCutouts: IPCB_Shapes;
function GetInoperablePrims: IPCB_Shapes;
function GetNewPrims: IPCB_Shapes;

## IPCB_Polygon
继承：IPCB_Polygon → IPCB_Group → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 81 个方法、32 个属性

property ArcApproximation: TCoord read GetState_ArcApproximation write SetState_ArcApproximation;
property ArcPourMode: Boolean read GetState_ArcPourMode write SetState_ArcPourMode;
property AreaSize: Double read GetState_AreaSize write SetState_AreaSize;
property AutoGenerateName: Boolean read GetState_AutoGenerateName write SetState_AutoGenerateName;
property AvoidObsticles: Boolean read GetState_AvoidObsticles write SetState_AvoidObsticles;
property BorderWidth: TCoord read GetState_BorderWidth write SetState_BorderWidth;
property ClipAcuteCorners: Boolean read GetState_ClipAcuteCorners write SetState_ClipAcuteCorners;
property DrawDeadCopper: Boolean read GetState_DrawDeadCopper write SetState_DrawDeadCopper;
property DrawRemovedIslands: Boolean read GetState_DrawRemovedIslands write SetState_DrawRemovedIslands;
property DrawRemovedNecks: Boolean read GetState_DrawRemovedNecks write SetState_DrawRemovedNecks;
property ExpandOutline: Boolean read GetState_ExpandOutline write SetState_ExpandOutline;
property Grid: TCoord read GetState_Grid write SetState_Grid;
property IgnoreViolations: Boolean read GetState_IgnoreViolations write SetState_IgnoreViolations;
property IslandAreaThreshold: Double read GetState_IslandAreaThreshold write SetState_IslandAreaThreshold;
property MinTrack: TCoord read GetState_MinTrack write SetState_MinTrack;
property MitreCorners: Boolean read GetState_MitreCorners write SetState_MitreCorners;
property Name: TPCBString read GetState_Name write SetState_Name;
property NeckWidthThreshold: TCoord read GetState_NeckWidthThreshold write SetState_NeckWidthThreshold;
property ObeyPolygonCutout: Boolean read GetState_ObeyPolygonCutout write SetState_ObeyPolygonCutout;
property OptimalVoidRotation: Boolean read GetState_OptimalVoidRotation write SetState_OptimalVoidRotation;
property PointCount: Integer read GetState_PointCount write SetState_PointCount;
property PolygonType: TPolygonType read GetState_PolygonType write SetState_PolygonType;
property PolyHatchStyle: TPolyHatchStyle read GetState_PolyHatchStyle write SetState_PolyHatchStyle;
property Poured: Boolean read GetState_Poured write SetState_Poured;
property PourIndex: Integer read GetState_PourIndex write SetState_PourIndex;
property PourOver: TPolygonPourOver read GetState_PourOver write SetState_PourOver;
property RemoveDead: Boolean read GetState_RemoveDead write SetState_RemoveDead;
property RemoveIslandsByArea: Boolean read GetState_RemoveIslandsByArea write SetState_RemoveIslandsByArea;
property RemoveNarrowNecks: Boolean read GetState_RemoveNarrowNecks write SetState_RemoveNarrowNecks;
property Segments[I: Integer]: TPolySegment read GetState_Segments write SetState_Segments;
property TrackSize: TCoord read GetState_TrackSize write SetState_TrackSize;
property UseOctagons: Boolean read GetState_UseOctagons write SetState_UseOctagons;
function AcceptsLayer(Layer: TV6_Layer): Boolean;
procedure CopperPourValidate;
function GetDefaultName: WideString;
function GetState_ArcApproximation: Integer;
function GetState_ArcPourMode: Boolean;
function GetState_AreaSize: Double;
function GetState_AutoGenerateName: Boolean;
function GetState_AvoidObsticles: Boolean;
function GetState_BorderWidth: Integer;
function GetState_ClipAcuteCorners: Boolean;
function GetState_CopperPourInvalid: Boolean;
function GetState_DrawDeadCopper: Boolean;
function GetState_DrawRemovedIslands: Boolean;
function GetState_DrawRemovedNecks: Boolean;
function GetState_ExpandOutline: Boolean;
function GetState_Grid: Integer;
function GetState_HitPrimitive(APrimitive: IPCB_Primitive): Boolean;
function GetState_IgnoreViolations: Boolean;
function GetState_InRepour: Boolean;
function GetState_IslandAreaThreshold: Double;
function GetState_MinTrack: Integer;
function GetState_MitreCorners: Boolean;
function GetState_Name: WideString;
function GetState_NeckWidthThreshold: Integer;
function GetState_ObeyPolygonCutout: Boolean;
function GetState_OptimalVoidRotation: Boolean;
function GetState_PointCount: Integer;
function GetState_PolygonType: TPolygonType;
function GetState_PolyHatchStyle: TPolyHatchStyle;
function GetState_Poured: Boolean;
function GetState_PourIndex: Integer;
function GetState_PourOver: TPolygonPourOver;
function GetState_RemoveDead: Boolean;
function GetState_RemoveIslandsByArea: Boolean;
function GetState_RemoveNarrowNecks: Boolean;
function GetState_Segments(I: Integer): IDispatch;
function GetState_StrictHitTest(HitX: Integer; HitY: Integer): Boolean;
function GetState_TrackSize: Integer;
function GetState_UseOctagons: Boolean;
procedure GrowPolyshape(ADist: Integer);
function PointInPolygon(HitX: Integer; HitY: Integer): Boolean;
function PrimitiveInsidePoly(APrimitive: IPCB_Primitive): Boolean;
procedure Rebuild;
procedure RotateAroundXY(AX: Integer; AY: Integer; Angle: Double);
procedure SetState_ArcApproximation(Value: Integer);
procedure SetState_ArcPourMode(Value: Boolean);
procedure SetState_AreaSize(Value: Double);
procedure SetState_AutoGenerateName(Value: Boolean);
procedure SetState_AutoNameInvalidate;
procedure SetState_AvoidObsticles(Value: Boolean);
procedure SetState_BorderWidth(Value: Integer);
procedure SetState_ClipAcuteCorners(Value: Boolean);
procedure SetState_CopperPourInvalid;
procedure SetState_CopperPourValid;
procedure SetState_DrawDeadCopper(Value: Boolean);
procedure SetState_DrawRemovedIslands(Value: Boolean);
procedure SetState_DrawRemovedNecks(Value: Boolean);
procedure SetState_ExpandOutline(Value: Boolean);
procedure SetState_Grid(Value: Integer);
procedure SetState_IgnoreViolations(Value: Boolean);
procedure SetState_IslandAreaThreshold(Value: Double);
procedure SetState_MinTrack(Value: Integer);
procedure SetState_MitreCorners(Value: Boolean);
procedure SetState_Name(Name: WideString);
procedure SetState_NeckWidthThreshold(Value: Integer);
procedure SetState_ObeyPolygonCutout(AValue: Boolean);
procedure SetState_OptimalVoidRotation(AValue: Boolean);
procedure SetState_PointCount(Value: Integer);
procedure SetState_PolygonType(Value: TPolygonType);
procedure SetState_PolyHatchStyle(Value: TPolyHatchStyle);
procedure SetState_Poured(Value: Boolean);
procedure SetState_PourIndex(Value: Integer);
procedure SetState_PourOver(Value: TPolygonPourOver);
procedure SetState_RemoveDead(Value: Boolean);
procedure SetState_RemoveIslandsByArea(Value: Boolean);
procedure SetState_RemoveNarrowNecks(Value: Boolean);
procedure SetState_Segments(I: Integer; const Value: IDispatch);
procedure SetState_TrackSize(Value: Integer);
procedure SetState_UseOctagons(Value: Boolean);
function SetState_XSizeYSize: Boolean;
function xBoundingRectangle: IDispatch;

## IPCB_PolygonConnectStyleRule
继承：IPCB_PolygonConnectStyleRule → IPCB_Rule → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 21 个方法、5 个属性

property ConnectStyle: TPlaneConnectStyle read GetState_ConnectStyle write SetState_ConnectStyle;
property PolygonReliefAngle: TPolygonReliefAngle read GetState_PolygonReliefAngle write SetState_PolygonReliefAngle;
property ReliefAirGap: TCoord read GetState_ReliefAirGap write SetState_ReliefAirGap;
property ReliefConductorWidth: TCoord read GetState_ReliefConductorWidth write SetState_ReliefConductorWidth;
property ReliefEntries: Integer read GetState_ReliefEntries write SetState_ReliefEntries;
function GetState_ConnectStyle: TPlaneConnectStyle;
function GetState_ConnectStyleByType(PrimitiveType: TPolygonConnectPrimitiveType): TPlaneConnectStyle;
function GetState_PolygonReliefAngle: TPolygonReliefAngle;
function GetState_PolygonReliefAngleByType(PrimitiveType: TPolygonConnectPrimitiveType): TPolygonReliefAngle;
function GetState_ReliefAirGap: Integer;
function GetState_ReliefAirGapByType(PrimitiveType: TPolygonConnectPrimitiveType): Integer;
function GetState_ReliefConductorWidth: Integer;
function GetState_ReliefConductorWidthByType(PrimitiveType: TPolygonConnectPrimitiveType): Integer;
function GetState_ReliefEntries: Integer;
function GetState_ReliefEntriesByType(PrimitiveType: TPolygonConnectPrimitiveType): Integer;
function GetState_SamePadAndViaParams: Boolean;
procedure SetState_ConnectStyle(Value: TPlaneConnectStyle);
procedure SetState_ConnectStyleByType(PrimitiveType: TPolygonConnectPrimitiveType; Value: TPlaneConnectStyle);
procedure SetState_PolygonReliefAngle(Value: TPolygonReliefAngle);
procedure SetState_PolygonReliefAngleByType(PrimitiveType: TPolygonConnectPrimitiveType; Value: TPolygonReliefAngle);
procedure SetState_ReliefAirGap(Value: Integer);
procedure SetState_ReliefAirGapByType(PrimitiveType: TPolygonConnectPrimitiveType; Value: Integer);
procedure SetState_ReliefConductorWidth(Value: Integer);
procedure SetState_ReliefConductorWidthByType(PrimitiveType: TPolygonConnectPrimitiveType; Value: Integer);
procedure SetState_ReliefEntries(Value: Integer);
procedure SetState_ReliefEntriesByType(PrimitiveType: TPolygonConnectPrimitiveType; Value: Integer);

## IPCB_PolygonThermalRelief
继承：IPCB_PolygonThermalRelief → IInterface ｜ 单元：RT_PCB ｜ 自有 8 个方法、3 个属性

property ManualThermalReliefsCount: Integer read GetProperty_ManualThermalReliefsCount;  // read-only
property ThermalReliefData[const ADataForLayer: IDispatch]: TPadViaThermalReliefData read GetProperty_ThermalReliefData write SetProperty_ThermalReliefData;
property ThermalReliefDataType[const ADataForLayer: IDispatch]: TPadViaThermalReliefDataType read GetProperty_ThermalReliefDataType write SetProperty_ThermalReliefDataType;
function EditThermalReliefData(const ADataForLayer: IDispatch; const AData: IDispatch): Boolean;
function GetProperty_ManualThermalReliefsCount: Integer;
function GetProperty_ThermalReliefData(const ADataForLayer: IDispatch): IDispatch;
function GetProperty_ThermalReliefDataType(const ADataForLayer: IDispatch): TPadViaThermalReliefDataType;
procedure RemoveThermalRelief(const ADataForLayer: IDispatch);
procedure SetAllThermalReliefsToRule;
procedure SetProperty_ThermalReliefData(const ADataForLayer: IDispatch; const AReliefData: IDispatch);
procedure SetProperty_ThermalReliefDataType(const ADataForLayer: IDispatch; const AValue: TPadViaThermalReliefDataType);

## IPCB_PowerPlaneClearanceRule
继承：IPCB_PowerPlaneClearanceRule → IPCB_Rule → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 2 个方法、1 个属性

property Clearance: TCoord read GetState_Clearance write SetState_Clearance;
function GetState_Clearance: Integer;
procedure SetState_Clearance(Value: Integer);

## IPCB_PowerPlaneConnectStyleRule
继承：IPCB_PowerPlaneConnectStyleRule → IPCB_Rule → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 21 个方法、5 个属性

property PlaneConnectStyle: TPlaneConnectStyle read GetState_PlaneConnectStyle write SetState_PlaneConnectStyle;
property ReliefAirGap: TCoord read GetState_ReliefAirGap write SetState_ReliefAirGap;
property ReliefConductorWidth: TCoord read GetState_ReliefConductorWidth write SetState_ReliefConductorWidth;
property ReliefEntries: Integer read GetState_ReliefEntries write SetState_ReliefEntries;
property ReliefExpansion: TCoord read GetState_ReliefExpansion write SetState_ReliefExpansion;
function GetState_PlaneConnectStyle: TPlaneConnectStyle;
function GetState_PlaneConnectStyleByType(Value: TPlaneConnectPrimitiveType): TPlaneConnectStyle;
function GetState_ReliefAirGap: Integer;
function GetState_ReliefAirGapByType(Value: TPlaneConnectPrimitiveType): Integer;
function GetState_ReliefConductorWidth: Integer;
function GetState_ReliefConductorWidthByType(Value: TPlaneConnectPrimitiveType): Integer;
function GetState_ReliefEntries: Integer;
function GetState_ReliefEntriesByType(Value: TPlaneConnectPrimitiveType): Integer;
function GetState_ReliefExpansion: Integer;
function GetState_ReliefExpansionByType(Value: TPlaneConnectPrimitiveType): Integer;
function GetState_SamePadAndViaParams: Boolean;
procedure SetState_PlaneConnectStyle(Value: TPlaneConnectStyle);
procedure SetState_PlaneConnectStyleByType(PrimitiveType: TPlaneConnectPrimitiveType; Value: TPlaneConnectStyle);
procedure SetState_ReliefAirGap(Value: Integer);
procedure SetState_ReliefAirGapByType(PrimitiveType: TPlaneConnectPrimitiveType; Value: Integer);
procedure SetState_ReliefConductorWidth(Value: Integer);
procedure SetState_ReliefConductorWidthByType(PrimitiveType: TPlaneConnectPrimitiveType; Value: Integer);
procedure SetState_ReliefEntries(Value: Integer);
procedure SetState_ReliefEntriesByType(PrimitiveType: TPlaneConnectPrimitiveType; Value: Integer);
procedure SetState_ReliefExpansion(Value: Integer);
procedure SetState_ReliefExpansionByType(PrimitiveType: TPlaneConnectPrimitiveType; Value: Integer);

## IPCB_PrimDelay
继承：IPCB_PrimDelay → IInterface ｜ 单元：RT_PCB ｜ 自有 3 个方法、1 个属性

property PropagationDelay: Double read GetState_PropagationDelay write SetState_PropagationDelay;
function CanEdit: Boolean;
function GetState_PropagationDelay: Double;
procedure SetState_PropagationDelay(const Value: Double);

## IPCB_PrimPrim
继承：IPCB_PrimPrim → IInterface ｜ 单元：RT_PCB ｜ 自有 2 个方法、0 个属性

function ArePrimsConnectedByCopper(const APrimitive1: IPCB_Primitive; const APrimitive2: IPCB_Primitive): Boolean;
function PrimPrimDistance_IgnoreLayer(const APrimitive1: IPCB_Primitive; const APrimitive2: IPCB_Primitive): Integer;

## IPCB_Primitive
继承：IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 134 个方法、64 个属性

property AllowGlobalEdit: Boolean read GetState_AllowGlobalEdit write SetState_AllowGlobalEdit;
property Board: IPCB_Board read GetState_Board write SetState_Board;
property Component: IPCB_Component read GetState_Component write SetState_Component;
property Coordinate: IPCB_Coordinate read GetState_Coordinate write SetState_Coordinate;
property Descriptor: TPCBString read GetState_DescriptorString;  // read-only
property Detail: TPCBString read GetState_DetailString;  // read-only
property Dimension: IPCB_Dimension read GetState_Dimension write SetState_Dimension;
property DrawAsPreview: Boolean read GetState_DrawAsPreview write SetState_DrawAsPreview;
property DRCError: Boolean read GetState_DRCError write SetState_DRCError;
property Enabled: Boolean read GetState_Enabled write SetState_Enabled;
property Enabled_Direct: Boolean read GetState_Enabled_Direct write SetState_Enabled_Direct;
property Enabled_vComponent: Boolean read GetState_Enabled_vComponent write SetState_Enabled_vComponent;
property Enabled_vCoordinate: Boolean read GetState_Enabled_vCoordinate write SetState_Enabled_vCoordinate;
property Enabled_vDimension: Boolean read GetState_Enabled_vDimension write SetState_Enabled_vDimension;
property Enabled_vNet: Boolean read GetState_Enabled_vNet write SetState_Enabled_vNet;
property Enabled_vPolygon: Boolean read GetState_Enabled_vPolygon write SetState_Enabled_vPolygon;
property EnableDraw: Boolean read GetState_EnableDraw write SetState_EnableDraw;
property Handle: TPCBString read GetState_Handle;  // read-only
property Identifier: TPCBString read GetState_Identifier;  // read-only
property InBoard: Boolean read GetState_InBoard write SetState_InBoard;
property InComponent: Boolean read GetState_InComponent write SetState_InComponent;
property InCoordinate: Boolean read GetState_InCoordinate write SetState_InCoordinate;
property Index: Word read GetState_Index write SetState_Index;
property InDimension: Boolean read GetState_InDimension write SetState_InDimension;
property InNet: Boolean read GetState_InNet write SetState_InNet;
property InPolygon: Boolean read GetState_InPolygon write SetState_InPolygon;
property InSelectionMemory[Index: Integer]: Boolean read GetState_InSelectionMemory write SetState_InSelectionMemory;
property IsAssyTestpoint_Bottom: Boolean read GetState_IsAssyTestPoint_Bottom write SetState_IsAssyTestPoint_Bottom;
property IsAssyTestpoint_Top: Boolean read GetState_IsAssyTestPoint_Top write SetState_IsAssyTestPoint_Top;
property IsElectricalPrim: Boolean read GetState_IsElectricalPrim;  // read-only
property IsKeepout: Boolean read GetState_IsKeepout write SetState_IsKeepout;
property IsPreRoute: Boolean read GetState_IsPreRoute write SetState_IsPreRoute;
property IsTenting: Boolean read GetState_IsTenting write SetState_IsTenting;
property IsTenting_Bottom: Boolean read GetState_IsTenting_Bottom write SetState_IsTenting_Bottom;
property IsTenting_Top: Boolean read GetState_IsTenting_Top write SetState_IsTenting_Top;
property IsTestpoint_Bottom: Boolean read GetState_IsTestPoint_Bottom write SetState_IsTestPoint_Bottom;
property IsTestpoint_Top: Boolean read GetState_IsTestPoint_Top write SetState_IsTestPoint_Top;
property Layer: TLayer read GetState_V7Layer write SetState_V7Layer;
property Layer_V6: TV6_Layer read GetState_Layer write SetState_Layer;
property MiscFlag1: Boolean read GetState_MiscFlag1 write SetState_MiscFlag1;
property MiscFlag2: Boolean read GetState_MiscFlag2 write SetState_MiscFlag2;
property MiscFlag3: Boolean read GetState_MiscFlag3 write SetState_MiscFlag3;
property Moveable: Boolean read GetState_Moveable write SetState_Moveable;
property Net: IPCB_Net read GetState_Net write SetState_Net;
property ObjectId: TObjectId read GetState_ObjectID;  // read-only
property ObjectIDString: TPCBString read GetState_ObjectIDString;  // read-only
property PadCacheRobotFlag: Boolean read GetState_PadCacheRobotFlag write SetState_PadCacheRobotFlag;
property PasteMaskExpansion: TCoord read GetState_PasteMaskExpansion;  // read-only
property Polygon: IPCB_Polygon read GetState_Polygon write SetState_Polygon;
property PolygonOutline: Boolean read GetState_PolygonOutline write SetState_PolygonOutline;
property PowerPlaneClearance: TCoord read GetState_PowerPlaneClearance;  // read-only
property PowerPlaneConnectStyle: TPlaneConnectStyle read GetState_PowerPlaneConnectStyle;  // read-only
property PowerPlaneReliefExpansion: TCoord read GetState_PowerPlaneReliefExpansion;  // read-only
property ReliefAirGap: TCoord read GetState_ReliefAirGap;  // read-only
property ReliefConductorWidth: TCoord read GetState_ReliefConductorWidth;  // read-only
property ReliefEntries: Integer read GetState_ReliefEntries;  // read-only
property Selected: Boolean read GetState_Selected write SetState_Selected;
property SolderMaskExpansion: TCoord read GetState_SolderMaskExpansion;  // read-only
property TearDrop: Boolean read GetState_TearDrop write SetState_TearDrop;
property UnionIndex: Integer read GetState_UnionIndex write SetState_UnionIndex;
property UniqueId: TPCBString read GetState_UniqueId write SetState_UniqueID;
property Used: Boolean read GetState_Used write SetState_Used;
property UserRouted: Boolean read GetState_UserRouted write SetState_UserRouted;
property ViewableObjectID: TViewableObjectID read GetState_ViewableObjectID;  // read-only
procedure BeginModify;
function BoundingRectangle: IDispatch;
function BoundingRectangleChildren: IDispatch;
function BoundingRectangleForPainting: IDispatch;
function BoundingRectangleForSelection: IDispatch;
procedure CancelModify;
procedure EndModify;
procedure Export_ToParameters(AParams: PWideChar);
procedure FlipXY(Axis: Integer; MirrOp: TMirrorOperation);
function GetState_AllowGlobalEdit: Boolean;
function GetState_Board: IPCB_Board;
function GetState_Component: IPCB_Component;
function GetState_Coordinate: IPCB_Coordinate;
function GetState_DescriptorString: WideString;
function GetState_DetailString: WideString;
function GetState_Dimension: IPCB_Dimension;
function GetState_DrawAsPreview: Boolean;
function GetState_DRCError: Boolean;
function GetState_Enabled: Boolean;
function GetState_Enabled_Direct: Boolean;
function GetState_Enabled_vComponent: Boolean;
function GetState_Enabled_vCoordinate: Boolean;
function GetState_Enabled_vDimension: Boolean;
function GetState_Enabled_vNet: Boolean;
function GetState_Enabled_vPolygon: Boolean;
function GetState_EnableDraw: Boolean;
function GetState_Handle: WideString;
function GetState_Identifier: WideString;
function GetState_InBoard: Boolean;
function GetState_InComponent: Boolean;
function GetState_InCoordinate: Boolean;
function GetState_Index: Word;
function GetState_InDimension: Boolean;
function GetState_InNet: Boolean;
function GetState_InPolygon: Boolean;
function GetState_InSelectionMemory(Index: Integer): Boolean;
function GetState_IsAssyTestPoint_Bottom: Boolean;
function GetState_IsAssyTestPoint_Top: Boolean;
function GetState_IsElectricalPrim: Boolean;
function GetState_IsKeepout: Boolean;
function GetState_IsPreRoute: Boolean;
function GetState_IsTenting: Boolean;
function GetState_IsTenting_Bottom: Boolean;
function GetState_IsTenting_Top: Boolean;
function GetState_IsTestPoint_Bottom: Boolean;
function GetState_IsTestPoint_Top: Boolean;
function GetState_Layer: TV6_Layer;
function GetState_MiscFlag1: Boolean;
function GetState_MiscFlag2: Boolean;
function GetState_MiscFlag3: Boolean;
function GetState_Moveable: Boolean;
function GetState_Net: IPCB_Net;
function GetState_ObjectID: TObjectId;
function GetState_ObjectIDString: WideString;
function GetState_PadCacheRobotFlag: Boolean;
function GetState_PasteMaskExpansion: Integer;
function GetState_Polygon: IPCB_Polygon;
function GetState_PolygonOutline: Boolean;
function GetState_PowerPlaneClearance: Integer;
function GetState_PowerPlaneConnectStyle: TPlaneConnectStyle;
function GetState_PowerPlaneReliefExpansion: Integer;
function GetState_ReliefAirGap: Integer;
function GetState_ReliefConductorWidth: Integer;
function GetState_ReliefEntries: Integer;
function GetState_Selected: Boolean;
function GetState_SolderMaskExpansion: Integer;
function GetState_TearDrop: Boolean;
function GetState_UnionIndex: Integer;
function GetState_UniqueId: WideString;
function GetState_Used: Boolean;
function GetState_UserRouted: Boolean;
function GetState_V7Layer: Integer;
function GetState_ViewableObjectID: TViewableObjectID;
procedure GraphicallyInvalidate;
function I_ObjectAddress: Pointer;
function IsFreePrimitive: Boolean;
function IsHidden: Boolean;
function IsSaveable(AVer: TAdvPCBFileFormatVersion): Boolean;
procedure Mirror(Axis: Integer; MirrOp: TMirrorOperation);
procedure MoveByXY(AX: Integer; AY: Integer);
procedure MoveToXY(AX: Integer; AY: Integer);
function Replicate: IPCB_Primitive;
function RequiredParamterSpace: Integer;
procedure RotateBy(Angle: Double);
procedure SetState_AllowGlobalEdit(Value: Boolean);
procedure SetState_Board(ABoard: IPCB_Board);
procedure SetState_Component(Value: IPCB_Component);
procedure SetState_Coordinate(Value: IPCB_Coordinate);
procedure SetState_Dimension(Value: IPCB_Dimension);
procedure SetState_DrawAsPreview(Value: Boolean);
procedure SetState_DRCError(Value: Boolean);
procedure SetState_Enabled(Value: Boolean);
procedure SetState_Enabled_Direct(Value: Boolean);
procedure SetState_Enabled_vComponent(Value: Boolean);
procedure SetState_Enabled_vCoordinate(Value: Boolean);
procedure SetState_Enabled_vDimension(Value: Boolean);
procedure SetState_Enabled_vNet(Value: Boolean);
procedure SetState_Enabled_vPolygon(Value: Boolean);
procedure SetState_EnableDraw(Value: Boolean);
procedure SetState_InBoard(Value: Boolean);
procedure SetState_InComponent(Value: Boolean);
procedure SetState_InCoordinate(Value: Boolean);
procedure SetState_Index(AIndex: Word);
procedure SetState_InDimension(Value: Boolean);
procedure SetState_InNet(Value: Boolean);
procedure SetState_InPolygon(Value: Boolean);
procedure SetState_InSelectionMemory(Index: Integer; Value: Boolean);
procedure SetState_IsAssyTestPoint_Bottom(Value: Boolean);
procedure SetState_IsAssyTestPoint_Top(Value: Boolean);
procedure SetState_IsKeepout(Value: Boolean);
procedure SetState_IsPreRoute(b: Boolean);
procedure SetState_IsTenting(Value: Boolean);
procedure SetState_IsTenting_Bottom(Value: Boolean);
procedure SetState_IsTenting_Top(Value: Boolean);
procedure SetState_IsTestPoint_Bottom(Value: Boolean);
procedure SetState_IsTestPoint_Top(Value: Boolean);
procedure SetState_Layer(ALayer: TV6_Layer);
procedure SetState_MiscFlag1(Value: Boolean);
procedure SetState_MiscFlag2(Value: Boolean);
procedure SetState_MiscFlag3(Value: Boolean);
procedure SetState_Moveable(Value: Boolean);
procedure SetState_Net(Value: IPCB_Net);
procedure SetState_PadCacheRobotFlag(Value: Boolean);
procedure SetState_Polygon(Value: IPCB_Polygon);
procedure SetState_PolygonOutline(Value: Boolean);
procedure SetState_Preview(Enable: Boolean; Color: Cardinal; Opacity: Single; z: Integer; Height: Integer; sx: Single; sy: Single; SZ: Single);
procedure SetState_Selected(b: Boolean);
procedure SetState_TearDrop(Value: Boolean);
procedure SetState_UnionIndex(Value: Integer);
procedure SetState_UniqueID(const Value: WideString);
procedure SetState_Used(Value: Boolean);
procedure SetState_UserRouted(Value: Boolean);
procedure SetState_V7Layer(L: Integer);
procedure SwapLayerPairs;

## IPCB_Primitive2
继承：IPCB_Primitive2 → IInterface ｜ 单元：RT_PCB ｜ 自有 21 个方法、10 个属性

property IsEmbeddedComponentCavity: Boolean read GetState_IsEmbeddedComponentCavity;  // read-only
property PasteMaskEnabled: Boolean read GetState_PasteMaskEnabled write SetState_PasteMaskEnabled;
property PasteMaskExpansion: TCoord read GetState_PasteMaskExpansion write SetState_PasteMaskExpansion;
property PasteMaskExpansionMode: TMaskExpansionMode read GetState_PasteMaskExpansionMode write SetState_PasteMaskExpansionMode;
property PasteMaskPercent: Double read GetState_PasteMaskPercent write SetState_PasteMaskPercent;
property PasteMaskUsePercent: Boolean read GetState_PasteMaskUsePercent write SetState_PasteMaskUsePercent;
property RoutingMinWidth: TCoord read GetState_RoutingMinWidth;  // read-only
property RoutingViaWidth: TCoord read GetState_RoutingViaWidth;  // read-only
property SolderMaskExpansion: TCoord read GetState_SolderMaskExpansion write SetState_SolderMaskExpansion;
property SolderMaskExpansionMode: TMaskExpansionMode read GetState_SolderMaskExpansionMode write SetState_SolderMaskExpansionMode;
function GetState_IsEmbeddedComponentCavity: Boolean;
function GetState_PasteMaskEnabled: Boolean;
function GetState_PasteMaskExpansion: Integer;
function GetState_PasteMaskExpansionMode: TMaskExpansionMode;
function GetState_PasteMaskPercent: Double;
function GetState_PasteMaskUsePercent: Boolean;
function GetState_RoutingMinWidth: Integer;
function GetState_RoutingViaWidth: Integer;
function GetState_SolderMaskExpansion: Integer;
function GetState_SolderMaskExpansionMode: TMaskExpansionMode;
function HasMaskExpansion(MaskLayer: Integer): Boolean;
procedure Import_FromUser_PostProcess;
procedure Import_FromUser_PreProcess;
function MaskExpansion(MaskLayer: Integer): Integer;
procedure SetState_PasteMaskEnabled(Value: Boolean);
procedure SetState_PasteMaskExpansion(Value: Integer);
procedure SetState_PasteMaskExpansionMode(Value: TMaskExpansionMode);
procedure SetState_PasteMaskPercent(Value: Double);
procedure SetState_PasteMaskUsePercent(Value: Boolean);
procedure SetState_SolderMaskExpansion(Value: Integer);
procedure SetState_SolderMaskExpansionMode(Value: TMaskExpansionMode);

## IPCB_Primitive3D
继承：IPCB_Primitive3D → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 8 个方法、4 个属性

property FaceIdx: Integer read GetState_FaceIdx write SetState_FaceIdx;
property FaceRotation: Double read GetState_FaceRotation write SetState_FaceRotation;
property FaceU: Integer read GetState_FaceU write SetState_FaceU;
property FaceV: Integer read GetState_FaceV write SetState_FaceV;
function GetState_FaceIdx: Integer;
function GetState_FaceRotation: Double;
function GetState_FaceU: Integer;
function GetState_FaceV: Integer;
procedure SetState_FaceIdx(Value: Integer);
procedure SetState_FaceRotation(Value: Double);
procedure SetState_FaceU(Value: Integer);
procedure SetState_FaceV(Value: Integer);

## IPCB_PrimitiveComparator
继承：IPCB_PrimitiveComparator → IInterface ｜ 单元：RT_PCB ｜ 自有 0 个方法、0 个属性


## IPCB_PrimitiveCounter
继承：IPCB_PrimitiveCounter → IInterface ｜ 单元：RT_PCB ｜ 自有 4 个方法、2 个属性

property HoleCount[HoleType: TExtendedHoleType]: Cardinal read GetHoleCount;  // read-only
property StringCount: Cardinal read GetStringCount;  // read-only
function GetCount(ObjectSet: TObjectSet): Cardinal;
function GetHoleCount(HoleType: TExtendedHoleType): Cardinal;
function GetObjectCount(ObjectId: TObjectId): Cardinal;
function GetStringCount: Cardinal;

## IPCB_PrimitiveParameters
继承：IPCB_PrimitiveParameters → IInterface ｜ 单元：RT_PCB ｜ 自有 39 个方法、13 个属性

property Appurtenance: TParameterAppurtenance read GetAppurtenance;  // read-only
property IsCurrentVariant: Boolean read GetIsCurrentVariant;  // read-only
property IsDefaultVariant: Boolean read GetIsDefaultVariant;  // read-only
property IsFullyInherited: Boolean read GetIsFullyInherited write SetIsFullyInherited;
property IsFullyInheritedAllVariants: Boolean read GetIsFullyInheritedAllVariants write SetIsFullyInheritedAllVariants;
property ParameterByIndex[AIndex: Integer]: IPCB_Parameter read GetParameterByIndex;  // read-only
property ParameterByName[const AName: WideString]: IPCB_Parameter read GetParameterByName;  // read-only
property ValueByName[const AName: WideString]: TPCBString read GetValueByName write SetValueByName;
property ValueByNameDef[?, ?]: TPCBString read GetValueByNameDef;  // read-only
property VariantCount: Integer read GetVariantCount;  // read-only
property VariantIndex: Integer read GetVariantIndex;  // read-only
property VariantName: TPCBString read GetVariantName;  // read-only
property VariantUniqueID: TPCBString read GetVariantUniqueID;  // read-only
procedure AddOrSetParameter(const AParameter: IPCB_Parameter);
procedure AddParameter(const AParameter: IPCB_Parameter);
function Count: Integer;
function ExportToList: IPCB_ParameterList;
function FindParameterByName(const AName: WideString): IPCB_Parameter;
function GetAppurtenance: TParameterAppurtenance;
function GetIsCurrentVariant: Boolean;
function GetIsDefaultVariant: Boolean;
function GetIsFullyInherited: Boolean;
function GetIsFullyInheritedAllVariants: Boolean;
function GetParameterByIndex(AIndex: Integer): IPCB_Parameter;
function GetParameterByName(const AName: WideString): IPCB_Parameter;
function GetValueByName(const AName: WideString): WideString;
function GetVariantCount: Integer;
function GetVariantIndex: Integer;
function GetVariantName: WideString;
function GetVariantUniqueID: WideString;
procedure ImportFromList(const AParameters: IPCB_ParameterList);
procedure NewValueByName(const AName: WideString; const AValue: WideString);
procedure RemoveAllParameters;
procedure RemoveAllParametersAndVariants;
procedure RemoveByIndex(AIndex: Integer);
procedure RemoveByName(const AName: WideString);
procedure SetIsFullyInherited(AValue: Boolean);
procedure SetIsFullyInheritedAllVariants(AValue: Boolean);
procedure SetOrNewValueByName(const AName: WideString; const AValue: WideString);
procedure SetParameter(const AParameter: IPCB_Parameter);
procedure SetValueByName(const AName: WideString; const AValue: WideString);
procedure SwitchAppurtenance(AValue: TParameterAppurtenance);
procedure SwitchToCurrentVariant;
procedure SwitchToDefaultVariant;
procedure SwitchToVariantByIndex(AIndex: Integer);
procedure SwitchToVariantByName(const AVariantName: WideString);
procedure SwitchToVariantByUniqueID(const AUniqueID: WideString);
function TryGetValueByName(const AName: WideString; out AValue: WideString): Boolean;
function TryNewValueByName(const AName: WideString; const AValue: WideString): Boolean;
function TryRemoveByName(const AName: WideString): Boolean;
function TrySetValueByName(const AName: WideString; const AValue: WideString): Boolean;
function TrySwitchToNextVariant: Boolean;

## IPCB_PrimitiveSerialize
继承：IPCB_PrimitiveSerialize → IInterface ｜ 单元：RT_PCB ｜ 自有 2 个方法、0 个属性

procedure ExportToParameters(AParameters: IWideParameterList);
procedure ImportFromParameters(AParameters: IWideParameterList);

## IPCB_PrintedElectronics
继承：IPCB_PrintedElectronics → IInterface ｜ 单元：RT_PCB ｜ 自有 2 个方法、0 个属性

function GetPrintedElectronics: IPrintedElectronics;
function IsPrintedElectronics: Boolean;

## IPCB_PrinterOptions
继承：IPCB_PrinterOptions → IPCB_AbstractOptions → IInterface ｜ 单元：RT_PCB ｜ 自有 70 个方法、32 个属性

property BatchType: TPrinterBatch read GetState_BatchType write SetState_BatchType;
property cBorderSize: TCoord read GetState_cBorderSize write SetState_cBorderSize;
property CompositePlotColorLayers[L: TV6_Layer]: TColor read GetState_CompositePlotColorLayers write SetState_CompositePlotColorLayers;
property CompositePlotLayers[L: TV6_Layer]: Boolean read GetState_CompositePlotLayers write SetState_CompositePlotLayers;
property CompositePlotMonoLayers[L: TV6_Layer]: TColor read GetState_CompositePlotMonoLayers write SetState_CompositePlotMonoLayers;
property CompositePlotPens[L: TV6_Layer]: Integer read GetState_CompositePlotPens write SetState_CompositePlotPens;
property CompositeType: TPrinterComposite read GetState_CompositeType write SetState_CompositeType;
property Device: TPCBString read GetState_Device write SetState_Device;
property Driver: TPCBString read GetState_Driver write SetState_Driver;
property OutPut: TPCBString read GetState_OutPut write SetState_OutPut;
property OutputDriverType: TOutputDriverType read GetState_OutputDriverType write SetState_OutputDriverType;
property PlotMode[OId: TObjectId]: TDrawMode read GetState_PlotMode write SetState_PlotMode;
property PlotPadNets: Boolean read GetState_PlotPadNets write SetState_PlotPadNets;
property PlotPadNumbers: Boolean read GetState_PlotPadNumbers write SetState_PlotPadNumbers;
property PlotterLanguage: TPlotterLanguage read GetState_PlotterLanguage write SetState_PlotterLanguage;
property PlotterOutputPort: TOutputPort read GetState_PlotterOutputPort write SetState_PlotterOutputPort;
property PlotterPens[Pen: Integer]: TPlotterPen read GetState_PlotterPens write SetState_PlotterPens;
property PlotterScale: TGeometry read GetState_PlotterScale write SetState_PlotterScale;
property PlotterShowHoles: Boolean read GetState_PlotterShowHoles write SetState_PlotterShowHoles;
property PlotterUseSoftwareArcs: Boolean read GetState_PlotterUseSoftwareArcs write SetState_PlotterUseSoftwareArcs;
property PlotterWaitBetweenSheets: Boolean read GetState_PlotterWaitBetweenSheets write SetState_PlotterWaitBetweenSheets;
property PlotterXCorrect: TGeometry read GetState_PlotterXCorrect write SetState_PlotterXCorrect;
property PlotterXOffset: TCoord read GetState_PlotterXOffset write SetState_PlotterXOffset;
property PlotterYCorrect: TGeometry read GetState_PlotterYCorrect write SetState_PlotterYCorrect;
property PlotterYOffset: TCoord read GetState_PlotterYOffset write SetState_PlotterYOffset;
property Scale: TGeometry read GetState_Scale write SetState_Scale;
property ScaleToFitPage: Boolean read GetState_ScaleToFitPage write SetState_ScaleToFitPage;
property ShowHoles: Boolean read GetState_ShowHoles write SetState_ShowHoles;
property UsePrinterFonts: Boolean read GetState_UsePrinterFonts write SetState_UsePrinterFonts;
property UseSoftwareArcs: Boolean read GetState_UseSoftwareArcs write SetState_UseSoftwareArcs;
property XCorrect: TGeometry read GetState_XCorrect write SetState_XCorrect;
property YCorrect: TGeometry read GetState_YCorrect write SetState_YCorrect;
procedure Export_ToParameters_GeneralOptions(Parameters: PWideChar);
procedure Export_ToParameters_LayerOptions(Parameters: PWideChar);
procedure Export_ToParameters_LayerOptions_Version3(Parameters: PWideChar);
function GetState_BatchType: TPrinterBatch;
function GetState_cBorderSize: Integer;
function GetState_CompositePlotColorLayers(L: TV6_Layer): Cardinal;
function GetState_CompositePlotLayers(L: TV6_Layer): Boolean;
function GetState_CompositePlotMonoLayers(L: TV6_Layer): Cardinal;
function GetState_CompositePlotPens(L: TV6_Layer): Integer;
function GetState_CompositeType: TPrinterComposite;
function GetState_Device: WideString;
function GetState_Driver: WideString;
function GetState_OutPut: WideString;
function GetState_OutputDriverType: TOutputDriverType;
function GetState_PlotMode(OId: TObjectId): TDrawMode;
function GetState_PlotPadNets: Boolean;
function GetState_PlotPadNumbers: Boolean;
function GetState_PlotterLanguage: TPlotterLanguage;
function GetState_PlotterOutputPort: TOutputPort;
function GetState_PlotterPens(Pen: Integer): IDispatch;
function GetState_PlotterScale: Double;
function GetState_PlotterShowHoles: Boolean;
function GetState_PlotterUseSoftwareArcs: Boolean;
function GetState_PlotterWaitBetweenSheets: Boolean;
function GetState_PlotterXCorrect: Double;
function GetState_PlotterXOffset: Integer;
function GetState_PlotterYCorrect: Double;
function GetState_PlotterYOffset: Integer;
function GetState_Scale: Double;
function GetState_ScaleToFitPage: Boolean;
function GetState_ShowHoles: Boolean;
function GetState_UsePrinterFonts: Boolean;
function GetState_UseSoftwareArcs: Boolean;
function GetState_XCorrect: Double;
function GetState_YCorrect: Double;
procedure Import_FromParameters_GeneralOptions(DisplayUnit: TUnit; Parameters: PWideChar);
procedure Import_FromParameters_LayerOptions(Parameters: PWideChar);
procedure Import_FromParameters_LayerOptions_Version3(Parameters: PWideChar);
procedure SetState_BatchType(Value: TPrinterBatch);
procedure SetState_cBorderSize(Value: Integer);
procedure SetState_CompositePlotColorLayers(L: TV6_Layer; Value: Cardinal);
procedure SetState_CompositePlotLayers(L: TV6_Layer; Value: Boolean);
procedure SetState_CompositePlotMonoLayers(L: TV6_Layer; Value: Cardinal);
procedure SetState_CompositePlotPens(L: TV6_Layer; Value: Integer);
procedure SetState_CompositeType(Value: TPrinterComposite);
procedure SetState_Device(Value: WideString);
procedure SetState_Driver(Value: WideString);
procedure SetState_OutPut(Value: WideString);
procedure SetState_OutputDriverType(Value: TOutputDriverType);
procedure SetState_PlotMode(OId: TObjectId; Value: TDrawMode);
procedure SetState_PlotPadNets(Value: Boolean);
procedure SetState_PlotPadNumbers(Value: Boolean);
procedure SetState_PlotterLanguage(Value: TPlotterLanguage);
procedure SetState_PlotterOutputPort(Value: TOutputPort);
procedure SetState_PlotterPens(Pen: Integer; const Value: IDispatch);
procedure SetState_PlotterScale(Value: Double);
procedure SetState_PlotterShowHoles(Value: Boolean);
procedure SetState_PlotterUseSoftwareArcs(Value: Boolean);
procedure SetState_PlotterWaitBetweenSheets(Value: Boolean);
procedure SetState_PlotterXCorrect(Value: Double);
procedure SetState_PlotterXOffset(Value: Integer);
procedure SetState_PlotterYCorrect(Value: Double);
procedure SetState_PlotterYOffset(Value: Integer);
procedure SetState_Scale(Value: Double);
procedure SetState_ScaleToFitPage(Value: Boolean);
procedure SetState_ShowHoles(Value: Boolean);
procedure SetState_UsePrinterFonts(Value: Boolean);
procedure SetState_UseSoftwareArcs(Value: Boolean);
procedure SetState_XCorrect(Value: Double);
procedure SetState_YCorrect(Value: Double);

## IPCB_ProcessControl
继承：IPCB_ProcessControl → IInterface ｜ 单元：RT_PCB ｜ 自有 4 个方法、0 个属性

procedure PostBatchProcess(const AContext: IInterface; AParameters: PWideChar);
procedure PostProcess_Clustered(const AContext: IInterface; AParameters: PWideChar);
procedure PreBatchProcess(const AContext: IInterface; AParameters: PWideChar);
procedure PreProcess_Clustered(const AContext: IInterface; AParameters: PWideChar);

## IPCB_RadialDiameterDimension
继承：IPCB_RadialDiameterDimension → IPCB_RadialDimension → IPCB_Dimension → IPCB_Group → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 3 个方法、0 个属性

function Arrow2_Track1: IPCB_Track;
function Arrow2_Track2: IPCB_Track;
function Line3_Track: IPCB_Track;

## IPCB_RadialDimension
继承：IPCB_RadialDimension → IPCB_Dimension → IPCB_Group → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 7 个方法、1 个属性

property AngleStep: TAngle read GetState_AngleStep write SetState_AngleStep;
function Arrow_Track1: IPCB_Track;
function Arrow_Track2: IPCB_Track;
function GetState_AngleStep: Double;
function Line1_Track: IPCB_Track;
function Line2_Track: IPCB_Track;
procedure SetState_AngleStep(Value: Double);
function Text: IPCB_Text;

## IPCB_RealPlacementGuide
继承：IPCB_RealPlacementGuide → IPCB_PlacementGuide → IInterface ｜ 单元：RT_PCB ｜ 自有 3 个方法、2 个属性

property Enabled: Boolean read GetProperty_Enabled write SetProperty_Enabled;
property SourceObject: IPCB_Primitive read GetState_SourceObject;  // read-only
function GetProperty_Enabled: Boolean;
function GetState_SourceObject: IPCB_Primitive;
procedure SetProperty_Enabled(const AValue: Boolean);

## IPCB_RealPlacementGuideIterator
继承：IPCB_RealPlacementGuideIterator → IPCB_PlacementIterator → IInterface ｜ 单元：RT_PCB ｜ 自有 2 个方法、0 个属性

function First: IPCB_RealPlacementGuide;
function Next: IPCB_RealPlacementGuide;

## IPCB_RectangleTool
继承：IPCB_RectangleTool → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 19 个方法、9 个属性

property ChamferFilletSize: TCoord read GetState_ChamferFilletSize write SetState_ChamferFilletSize;
property CornerMode: TPlaceRectangleCornerMode read GetState_CornerMode write SetState_CornerMode;
property Height: TCoord read GetState_Height write SetState_Height;
property HoldAspectRatio: Boolean read GetState_HoldAspectRatio write SetState_HoldAspectRatio;
property LineWidth: TCoord read GetState_LineWidth write SetState_LineWidth;
property Rotation: TAngle read GetState_Rotation write SetState_Rotation;
property Width: TCoord read GetState_Width write SetState_Width;
property XCenter: TCoord read GetState_XCenter write SetState_XCenter;
property YCenter: TCoord read GetState_YCenter write SetState_YCenter;
function GetState_ChamferFilletSize: Integer;
function GetState_CornerMode: TPlaceRectangleCornerMode;
function GetState_Height: Integer;
function GetState_HoldAspectRatio: Boolean;
function GetState_LineWidth: Integer;
function GetState_Rotation: Double;
function GetState_Width: Integer;
function GetState_XCenter: Integer;
function GetState_YCenter: Integer;
procedure Invalidate;
procedure SetState_ChamferFilletSize(AValue: Integer);
procedure SetState_CornerMode(AValue: TPlaceRectangleCornerMode);
procedure SetState_Height(AValue: Integer);
procedure SetState_HoldAspectRatio(AValue: Boolean);
procedure SetState_LineWidth(AValue: Integer);
procedure SetState_Rotation(AValue: Double);
procedure SetState_Width(AValue: Integer);
procedure SetState_XCenter(AValue: Integer);
procedure SetState_YCenter(AValue: Integer);

## IPCB_RectangularPrimitive
继承：IPCB_RectangularPrimitive → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 17 个方法、7 个属性

property Rotation: TAngle read GetState_Rotation write SetState_Rotation;
property X1Location: TCoord read GetState_X1Location write SetState_X1Location;
property X2Location: TCoord read GetState_X2Location write SetState_X2Location;
property XLocation: TCoord read GetState_XLocation write SetState_XLocation;
property Y1Location: TCoord read GetState_Y1Location write SetState_Y1Location;
property Y2Location: TCoord read GetState_Y2Location write SetState_Y2Location;
property YLocation: TCoord read GetState_YLocation write SetState_YLocation;
function GetState_Rotation: Double;
function GetState_X1Location: Integer;
function GetState_X2Location: Integer;
function GetState_XLocation: Integer;
function GetState_Y1Location: Integer;
function GetState_Y2Location: Integer;
function GetState_YLocation: Integer;
function IsRedundant: Boolean;
procedure RotateAroundXY(AX: Integer; AY: Integer; Angle: Double);
procedure SetState_Rotation(Rotation: Double);
procedure SetState_X1Location(AX1: Integer);
procedure SetState_X2Location(AX2: Integer);
procedure SetState_XLocation(AX: Integer);
function SetState_XSizeYSize: Boolean;
procedure SetState_Y1Location(AY1: Integer);
procedure SetState_Y2Location(AY2: Integer);
procedure SetState_YLocation(AY: Integer);

## IPCB_Region
继承：IPCB_Region → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 15 个方法、8 个属性

property Area: Int64 read GetState_Area;  // read-only
property CavityHeight: TCoord read GetState_CavityHeight write SetState_CavityHeight;
property GeometricPolygon: IPCB_GeometricPolygon read GetGeometricPolygon write SetGeometricPolygon;
property HoleCount: Integer read GetHoleCount;  // read-only
property Holes[I: Integer]: IPCB_Contour read GetHole;  // read-only
property Kind: TRegionKind read GetState_Kind write SetState_Kind;
property MainContour: IPCB_Contour read GetMainContour;  // read-only
property Name: TPCBString read GetState_Name write SetState_Name;
function GetGeometricPolygon: IPCB_GeometricPolygon;
function GetHole(I: Integer): IPCB_Contour;
function GetHoleCount: Integer;
function GetMainContour: IPCB_Contour;
function GetState_Area: Int64;
function GetState_CavityHeight: Integer;
function GetState_Kind: TRegionKind;
function GetState_Name: WideString;
function IsSimpleRegion: Boolean;
procedure RotateAroundXY(AX: Integer; AY: Integer; Angle: Double);
procedure SetGeometricPolygon(AGeometricPolygon: IPCB_GeometricPolygon);
procedure SetOutlineContour(Contour: IPCB_Contour);
procedure SetState_CavityHeight(Value: Integer);
procedure SetState_Kind(Value: TRegionKind);
procedure SetState_Name(Value: WideString);

## IPCB_Region2
继承：IPCB_Region2 → IPCB_Region → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 13 个方法、3 个属性

property ArcApproximation: TCoord read GetState_ArcApproximation write SetState_ArcApproximation;
property x: TCoord read GetState_X;  // read-only
property y: TCoord read GetState_Y;  // read-only
procedure AddSnapPoint(const APoint: IDispatch);
procedure CheckNonCopper;
procedure DeleteSnapPoint(AIndex: Integer);
function GetState_ArcApproximation: Integer;
function GetState_SelfIntersectionPoint(APos: Integer): IDispatch;
function GetState_SelfIntersectionsCount: Integer;
function GetState_SnapCount: Integer;
function GetState_SnapPoint(AIndex: Integer): IDispatch;
function GetState_X: Integer;
function GetState_Y: Integer;
function GetTrisArea: Int64;
procedure SetState_ArcApproximation(Value: Integer);
procedure SetState_SnapPoint(AIndex: Integer; const APoint: IDispatch);

## IPCB_Region3D
继承：IPCB_Region3D → IPCB_Region → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 4 个方法、0 个属性

procedure Boundary_AddPoint(const APoint: IDispatch; AFaceIdx: Integer);
procedure Boundary_Clear;
procedure Boundary_GetPoint(AIdx: Integer; const Point: IDispatch; out FaceIdx: Integer);
function Boundary_PointsCount: Integer;

## IPCB_RegionShape
继承：IPCB_RegionShape → IInterface ｜ 单元：RT_PCB ｜ 自有 8 个方法、2 个属性

property ShapeSegmentCount: Integer read GetState_ShapeSegmentCount write SetState_ShapeSegmentCount;
property ShapeSegments[I: Integer]: TPolySegment read GetState_ShapeSegment write SetState_ShapeSegment;
procedure DeleteSegmentAt(const Index: Integer);
function GetState_ShapeSegment(I: Integer): IDispatch;
function GetState_ShapeSegmentCount: Integer;
function InsertSegmentAt(const Index: Integer): IDispatch;
procedure SetState_ShapeSegment(I: Integer; const Value: IDispatch);
procedure SetState_ShapeSegmentCount(Value: Integer);
procedure UpdateContourFromShape(ConserveExistingHoles: Boolean);
procedure UpdateShapeFromContour;

## IPCB_RegionShape2
继承：IPCB_RegionShape2 → IInterface ｜ 单元：RT_PCB ｜ 自有 6 个方法、2 个属性

property Edge[I: Integer]: IPCB_ShapeEdge read GetState_Edge;  // read-only
property EdgeCount: Integer read GetState_EdgeCount;  // read-only
procedure ClearEdges;
procedure Delete(Index: Integer);
function GetState_Edge(I: Integer): IPCB_ShapeEdge;
function GetState_EdgeCount: Integer;
function Insert(Index: Integer; const AType: TPCB_ShapeEdgeType): IPCB_ShapeEdge;
procedure UpdateContourFromShape(ConserveExistingHoles: Boolean);

## IPCB_RegionShape_Utils
继承：IPCB_RegionShape_Utils → IInterface ｜ 单元：RT_PCB ｜ 自有 3 个方法、0 个属性

procedure CleanUp(ATolerance: Integer);
function GetSmallSegments(ATolerance: Integer): ICoordPointPairList;
procedure RemoveRedundantVertices;

## IPCB_ReturnPathRule
继承：IPCB_ReturnPathRule → IPCB_Rule → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 6 个方法、3 个属性

property GapLimit: TCoord read GetState_GapLimit write SetState_GapLimit;
property ImpedanceProfileId: TPCBString read GetState_ImpedanceProfileId write SetState_ImpedanceProfileId;
property UseAntiPads: Boolean read GetState_UseAntiPads write SetState_UseAntiPads;
function GetState_GapLimit: Integer;
function GetState_ImpedanceProfileId: WideString;
function GetState_UseAntiPads: Boolean;
procedure SetState_GapLimit(Value: Integer);
procedure SetState_ImpedanceProfileId(Value: WideString);
procedure SetState_UseAntiPads(Value: Boolean);

## IPCB_RoutingCornerStyleRule
继承：IPCB_RoutingCornerStyleRule → IPCB_Rule → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 6 个方法、3 个属性

property MaxSetBack: TCoord read GetState_MaxSetBack write SetState_MaxSetBack;
property MinSetBack: TCoord read GetState_MinSetBack write SetState_MinSetBack;
property Style: TCornerStyle read GetState_Style write SetState_Style;
function GetState_MaxSetBack: Integer;
function GetState_MinSetBack: Integer;
function GetState_Style: TCornerStyle;
procedure SetState_MaxSetBack(Value: Integer);
procedure SetState_MinSetBack(Value: Integer);
procedure SetState_Style(Value: TCornerStyle);

## IPCB_RoutingLayersRule
继承：IPCB_RoutingLayersRule → IPCB_Rule → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 3 个方法、1 个属性

property RoutingLayers[SignalLayer: Integer]: Boolean read GetState_RoutingLayers write SetState_RoutingLayers;
function GetState_RoutingLayers(SignalLayer: Integer): Boolean;
procedure ResetRoutingLayers;
procedure SetState_RoutingLayers(SignalLayer: Integer; Value: Boolean);

## IPCB_RoutingOptionsPage
继承：IPCB_RoutingOptionsPage → IInterface ｜ 单元：RT_PCB ｜ 自有 76 个方法、0 个属性

function GetState_AllowViaPushing: Boolean;
function GetState_AutoRemoveAntennas: Boolean;
function GetState_AutoRemoveLoops: Boolean;
function GetState_AutoRemoveViaLoops: Boolean;
function GetState_AutoTerminateRouting: Boolean;
function GetState_AvoidPolygons: Boolean;
function GetState_AvoidRooms: Boolean;
function GetState_ComponentMoveRelevantRouting: Boolean;
function GetState_ComponentMoveRelevantRoutingPinsLimit: Integer;
function GetState_ComponentNetLineMode: TNetLineMode;
function GetState_ComponentPushing: TPushMode;
function GetState_ComponentReroute: Boolean;
function GetState_ConflictMode: TAdvancedRouteMode;
function GetState_ConflictModeEnabled(AMode: TAdvancedRouteMode): Boolean;
function GetState_DifferentialPairMode: Boolean;
function GetState_DifferentialPairModeForVias: Boolean;
function GetState_DiffPairGapToUse: Integer;
function GetState_DisplayClearanceBounds: Boolean;
function GetState_DragAvoidObstacleMode: TAvoidObstacleMode;
function GetState_DragMergeParallel: Boolean;
function GetState_Dragselected: TDragSelectUnselectMode;
function GetState_DragUnselected: TDragSelectUnselectMode;
function GetState_DragWithMiters: Boolean;
function GetState_GlossEffort: TGlossEffort;
function GetState_HuggingStyle: THuggingStyle;
function GetState_MinimumArcSize: Double;
function GetState_MiterSize: Double;
function GetState_NeighborGlossEffort: TGlossEffort;
function GetState_PadEntryStability: Integer;
function GetState_PickupWidthFromExistingRoutes: Boolean;
function GetState_PreferredClearanceRatio: Double;
function GetState_ReduceClearanceDisplayArea: Boolean;
function GetState_RoutingWidthMode: TRoutingWidthMode;
function GetState_ShowGaugeDuringDragging: Boolean;
function GetState_SmartDrag: Boolean;
function GetState_VertexAction: TVertexAction;
function GetState_ViaSizeMode: TRoutingWidthMode;
function GetState_WidthToUse: Integer;
procedure SetState_AllowViaPushing(AValue: Boolean);
procedure SetState_AutoRemoveAntennas(AValue: Boolean);
procedure SetState_AutoRemoveLoops(AValue: Boolean);
procedure SetState_AutoRemoveViaLoops(AValue: Boolean);
procedure SetState_AutoTerminateRouting(AValue: Boolean);
procedure SetState_AvoidPolygons(AValue: Boolean);
procedure SetState_AvoidRooms(AValue: Boolean);
procedure SetState_ComponentMoveRelevantRouting(AValue: Boolean);
procedure SetState_ComponentMoveRelevantRoutingPinsLimit(AValue: Integer);
procedure SetState_ComponentNetLineMode(AValue: TNetLineMode);
procedure SetState_ComponentPushing(AValue: TPushMode);
procedure SetState_ComponentReroute(AValue: Boolean);
procedure SetState_ConflictMode(AValue: TAdvancedRouteMode);
procedure SetState_ConflictModeEnabled(AMode: TAdvancedRouteMode; AValue: Boolean);
procedure SetState_DifferentialPairMode(AValue: Boolean);
procedure SetState_DifferentialPairModeForVias(AValue: Boolean);
procedure SetState_DiffPairGapToUse(AValue: Integer);
procedure SetState_DisplayClearanceBounds(AValue: Boolean);
procedure SetState_DragAvoidObstacleMode(AValue: TAvoidObstacleMode);
procedure SetState_DragMergeParallel(AValue: Boolean);
procedure SetState_DragSelected(AValue: TDragSelectUnselectMode);
procedure SetState_DragUnSelected(AValue: TDragSelectUnselectMode);
procedure SetState_DragWithMiters(AValue: Boolean);
procedure SetState_GlossEffort(ANewValue: TGlossEffort);
procedure SetState_HuggingStyle(AValue: THuggingStyle);
procedure SetState_MinimumArcSize(AValue: Double);
procedure SetState_MiterSize(AValue: Double);
procedure SetState_NeighborGlossEffort(ANewValue: TGlossEffort);
procedure SetState_PadEntryStability(AValue: Integer);
procedure SetState_PickupWidthFromExistingRoutes(AValue: Boolean);
procedure SetState_PreferredClearanceRatio(AValue: Double);
procedure SetState_ReduceClearanceDisplayArea(AValue: Boolean);
procedure SetState_RoutingWidthMode(AValue: TRoutingWidthMode);
procedure SetState_ShowGaugeDuringDragging(AValue: Boolean);
procedure SetState_SmartDrag(AValue: Boolean);
procedure SetState_VertexAction(ANewValue: TVertexAction);
procedure SetState_ViaSizeMode(AValue: TRoutingWidthMode);
procedure SetState_WidthToUse(AValue: Integer);

## IPCB_RoutingPriorityRule
继承：IPCB_RoutingPriorityRule → IPCB_Rule → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 2 个方法、1 个属性

property RoutingPriority: Integer read GetState_RoutingPriority write SetState_RoutingPriority;
function GetState_RoutingPriority: Integer;
procedure SetState_RoutingPriority(Value: Integer);

## IPCB_RoutingTopologyRule
继承：IPCB_RoutingTopologyRule → IPCB_Rule → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 2 个方法、1 个属性

property Topology: TNetTopology read GetState_Topology write SetState_Topology;
function GetState_Topology: TNetTopology;
procedure SetState_Topology(Value: TNetTopology);

## IPCB_RoutingViaStackInfo
继承：IPCB_RoutingViaStackInfo → IInterface ｜ 单元：RT_PCB ｜ 自有 4 个方法、3 个属性

property Title: WideString read GetState_Title;  // read-only
property ViaDataCount: Integer read GetState_ViaDataCount;  // read-only
property ViaDataInfo[AIndex: Integer]: IPCB_ViaRoutingDataInfo read GetState_ViaDataInfo;  // read-only
function FirstViaDataInfo: IPCB_ViaRoutingDataInfo;
function GetState_Title: WideString;
function GetState_ViaDataCount: Integer;
function GetState_ViaDataInfo(AIndex: Integer): IPCB_ViaRoutingDataInfo;

## IPCB_RoutingViaStyleRule
继承：IPCB_RoutingViaStyleRule → IPCB_Rule → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 22 个方法、8 个属性

property MaxHoleWidth: TCoord read GetState_MaxHoleWidth write SetState_MaxHoleWidth;
property MaxWidth: TCoord read GetState_MaxWidth write SetState_MaxWidth;
property MinHoleWidth: TCoord read GetState_MinHoleWidth write SetState_MinHoleWidth;
property MinWidth: TCoord read GetState_MinWidth write SetState_MinWidth;
property PreferedHoleWidth: TCoord read GetState_PreferedHoleWidth write SetState_PreferedHoleWidth;
property PreferedWidth: TCoord read GetState_PreferedWidth write SetState_PreferedWidth;
property UseViaTemplates: Boolean read GetState_UseViaTemplates write SetState_UseViaTemplates;
property ViaStyle: TRouteVia read GetState_ViaStyle write SetState_ViaStyle;
procedure AddViaTemplate(TemplateGUID: WideString; TemplateName: WideString);
procedure DeleteAllViaTemplates;
procedure DeleteMissingViaTemplates;
function GetState_MaxHoleWidth: Integer;
function GetState_MaxWidth: Integer;
function GetState_MinHoleWidth: Integer;
function GetState_MinWidth: Integer;
function GetState_PreferedHoleWidth: Integer;
function GetState_PreferedWidth: Integer;
function GetState_UseViaTemplates: Boolean;
function GetState_ViaStyle: TRouteVia;
function GetViaTemplate(const Index: Integer): IPCB_PadViaTemplate;
function GetViaTemplateCount: Integer;
function IsViaTemplateUsed(ATemplateGUID: WideString): Boolean;
procedure SetState_MaxHoleWidth(Value: Integer);
procedure SetState_MaxWidth(Value: Integer);
procedure SetState_MinHoleWidth(Value: Integer);
procedure SetState_MinWidth(Value: Integer);
procedure SetState_PreferedHoleWidth(Value: Integer);
procedure SetState_PreferedWidth(Value: Integer);
procedure SetState_UseViaTemplates(Value: Boolean);
procedure SetState_ViaStyle(Value: TRouteVia);

## IPCB_Rule
继承：IPCB_Rule → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 35 个方法、9 个属性

property Comment: TPCBString read GetState_Comment write SetState_Comment;
property DefinedByLogicalDocument: Boolean read GetState_DefinedByLogicalDocument write SetState_DefinedByLogicalDocument;
property DRCEnabled: Boolean read GetState_DRCEnabled write SetState_DRCEnabled;
property LayerKind: TRuleLayerKind read GetState_LayerKind write SetState_LayerKind;
property Name: TPCBString read GetState_Name write SetState_Name;
property NetScope: TNetScope read GetState_NetScope write SetState_NetScope;
property RuleKind: TRuleKind read GetState_RuleKind write SetState_RuleKind;
property Scope1Expression: TPCBString read GetState_Scope1Expression write SetState_Scope1Expression;
property Scope2Expression: TPCBString read GetState_Scope2Expression write SetState_Scope2Expression;
function ActualCheck(P1: IPCB_Primitive; P2: IPCB_Primitive): IPCB_Violation;
function CheckBinaryScope(P1: IPCB_Primitive; P2: IPCB_Primitive): Boolean;
function CheckUnaryScope(P: IPCB_Primitive): Boolean;
procedure Export_ToParameters(AParams: PWideChar);
function GetState_CollisionExpansion: Integer;
function GetState_Comment: WideString;
function GetState_DataSummaryString: WideString;
function GetState_DefinedByLogicalDocument: Boolean;
function GetState_DRCEnabled: Boolean;
function GetState_LayerKind: TRuleLayerKind;
function GetState_Name: WideString;
function GetState_NetScope: TNetScope;
function GetState_RuleKind: TRuleKind;
function GetState_Scope1Expression: WideString;
function GetState_Scope2Expression: WideString;
function GetState_ScopeDescriptorString: WideString;
function GetState_ShortDescriptorString: WideString;
function GetState_ViolationDescriptorString(V: IPCB_Violation): WideString;
function GetWhatsThisHelpString: WideString;
function IsUnary: Boolean;
function IsValid: Boolean;
function NetScopeMatches(P1: IPCB_Primitive; P2: IPCB_Primitive): Boolean;
function Priority: Word;
function Scope1Includes(P: IPCB_Primitive): Boolean;
function Scope2Includes(P: IPCB_Primitive): Boolean;
function ScopeKindIsValid(AScopeKind: TScopeKind): Boolean;
procedure SetState_Comment(Value: WideString);
procedure SetState_DefinedByLogicalDocument(Value: Boolean);
procedure SetState_DRCEnabled(Value: Boolean);
procedure SetState_LayerKind(Value: TRuleLayerKind);
procedure SetState_Name(Value: WideString);
procedure SetState_NetScope(Value: TNetScope);
procedure SetState_RuleKind(Value: TRuleKind);
procedure SetState_Scope1Expression(const Value: WideString);
procedure SetState_Scope2Expression(const Value: WideString);

## IPCB_Rule1
继承：IPCB_Rule1 → IPCB_Rule → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 3 个方法、0 个属性

function GetState_Priority: Word;
procedure Import_FromParameters(AParameters: PWideChar);
procedure SetState_Priority(const Priority: Word);

## IPCB_RuleFlightTime_FallingEdge
继承：IPCB_RuleFlightTime_FallingEdge → IPCB_Rule → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 2 个方法、1 个属性

property MaximumFlightTime: Double read GetState_MaximumFlightTime write SetState_MaximumFlightTime;
function GetState_MaximumFlightTime: Double;
procedure SetState_MaximumFlightTime(Value: Double);

## IPCB_RuleFlightTime_RisingEdge
继承：IPCB_RuleFlightTime_RisingEdge → IPCB_Rule → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 2 个方法、1 个属性

property MaximumFlightTime: Double read GetState_MaximumFlightTime write SetState_MaximumFlightTime;
function GetState_MaximumFlightTime: Double;
procedure SetState_MaximumFlightTime(Value: Double);

## IPCB_RuleManager
继承：IPCB_RuleManager → IInterface ｜ 单元：RT_PCB ｜ 自有 3 个方法、0 个属性

procedure SetRulePriority(const ARule: IPCB_Rule; const APriority: Word);
procedure UpdateRulePriorities;
procedure UpdateRulePrioritiesByRuleKind(const ARuleKind: TRuleKind);

## IPCB_RuleMaxMinImpedance
继承：IPCB_RuleMaxMinImpedance → IPCB_Rule → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 4 个方法、2 个属性

property Maximum: Double read GetState_Maximum write SetState_Maximum;
property Minimum: Double read GetState_Minimum write SetState_Minimum;
function GetState_Maximum: Double;
function GetState_Minimum: Double;
procedure SetState_Maximum(Value: Double);
procedure SetState_Minimum(Value: Double);

## IPCB_RuleMaxSignalBaseValue
继承：IPCB_RuleMaxSignalBaseValue → IPCB_Rule → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 2 个方法、1 个属性

property Maximum: Double read GetState_Maximum write SetState_Maximum;
function GetState_Maximum: Double;
procedure SetState_Maximum(Value: Double);

## IPCB_RuleMaxSlopeFallingEdge
继承：IPCB_RuleMaxSlopeFallingEdge → IPCB_Rule → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 2 个方法、1 个属性

property MaxSlope: Double read GetState_MaxSlope write SetState_MaxSlope;
function GetState_MaxSlope: Double;
procedure SetState_MaxSlope(Value: Double);

## IPCB_RuleMaxSlopeRisingEdge
继承：IPCB_RuleMaxSlopeRisingEdge → IPCB_Rule → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 2 个方法、1 个属性

property MaxSlope: Double read GetState_MaxSlope write SetState_MaxSlope;
function GetState_MaxSlope: Double;
procedure SetState_MaxSlope(Value: Double);

## IPCB_RuleMinSignalTopValue
继承：IPCB_RuleMinSignalTopValue → IPCB_Rule → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 2 个方法、1 个属性

property Minimum: Double read GetState_Minimum write SetState_Minimum;
function GetState_Minimum: Double;
procedure SetState_Minimum(Value: Double);

## IPCB_RuleSupplyNets
继承：IPCB_RuleSupplyNets → IPCB_Rule → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 2 个方法、1 个属性

property Voltage: Double read GetState_Voltage write SetState_Voltage;
function GetState_Voltage: Double;
procedure SetState_Voltage(Value: Double);

## IPCB_SMDNeckDownConstraint
继承：IPCB_SMDNeckDownConstraint → IPCB_Rule → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 2 个方法、1 个属性

property Percent: Double read GetState_Percent write SetState_Percent;
function GetState_Percent: Double;
procedure SetState_Percent(Value: Double);

## IPCB_SMDPADEntryConstraint
继承：IPCB_SMDPADEntryConstraint → IPCB_Rule → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 0 个方法、0 个属性


## IPCB_SMDToCornerConstraint
继承：IPCB_SMDToCornerConstraint → IPCB_Rule → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 10 个方法、5 个属性

property Can_AnyAngle: Boolean read GetState_Can_AnyAngle write SetState_Can_AnyAngle;
property Can_Corner: Boolean read GetState_Can_Corner write SetState_Can_Corner;
property Can_IgnoreFirstCorner: Boolean read GetState_Can_IgnoreFirstCorner write SetState_Can_IgnoreFirstCorner;
property Can_Side: Boolean read GetState_Can_Side write SetState_Can_Side;
property Distance: TCoord read GetState_Distance write SetState_Distance;
function GetState_Can_AnyAngle: Boolean;
function GetState_Can_Corner: Boolean;
function GetState_Can_IgnoreFirstCorner: Boolean;
function GetState_Can_Side: Boolean;
function GetState_Distance: Integer;
procedure SetState_Can_AnyAngle(Value: Boolean);
procedure SetState_Can_Corner(Value: Boolean);
procedure SetState_Can_IgnoreFirstCorner(Value: Boolean);
procedure SetState_Can_Side(Value: Boolean);
procedure SetState_Distance(Value: Integer);

## IPCB_SMDToPlaneConstraint
继承：IPCB_SMDToPlaneConstraint → IPCB_Rule → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 3 个方法、1 个属性

property Distance: TCoord read GetState_Distance write SetState_Distance;
function GetState_Distance: Integer;
function IsInternalPlaneNet(Net: IPCB_Net; Board: IPCB_Board): Boolean;
procedure SetState_Distance(Value: Integer);

## IPCB_ServerInterface
继承：IPCB_ServerInterface → IInterface ｜ 单元：RT_PCB ｜ 自有 68 个方法、11 个属性

property CanFastCrossSelect_Emit: Boolean read GetState_CanFastCrossSelect_Emit;  // read-only
property CanFastCrossSelect_Receive: Boolean read GetState_CanFastCrossSelect_Receive write SetState_CanFastCrossSelect_Receive;
property Capabilities: IPCB_CapabilitiesFactory read GetCapabilitiesFactory;  // read-only
property InteractiveRoutingOptions: IPCB_InteractiveRoutingOptions read GetState_InteractiveRoutingOptions;  // read-only
property ParametersFactory: IPCB_ParametersFactory read GetParametersFactory;  // read-only
property ShowStatus: Boolean read GetState_ShowStatus write SetState_ShowStatus;
property SpecialStringConverter: IPCB_SpecialStringConverter read GetState_SpecialStringConverter;  // read-only
property SystemOptions: IPCB_SystemOptions read GetState_SystemOptions;  // read-only
property TTFLettersCache: IPCB_LettersCache read GetState_TTFLettersCache;  // read-only
property TTFontsCache: IPCB_TTFontsCache read GetState_TTFontsCache;  // read-only
property ViolationsFactory: IPCB_ViolationsFactory read GetViolationsFactory;  // read-only
function Board3DModelExporter: IPCB_Board3DModelExporter;
function CreateAndLoadPCBLibraryFromFile(const APath: WideString): IPCB_Library;
function CreateComponentPainter: IPCB_ComponentPainterView;
function CreateDocumentPainter(Mode: TPCB_DocumentPainterMode): IPCB_DocumentPainterView;
function CreateLayerStackupPainter: IPCB_LayerStackupDocumentPainterView;
function CreatePadViaPainter: IPCB_PadViaPainterView;
function CreatePCBGroup: IPCB_GroupEx;
function CreatePCBLibComp: IPCB_LibComponent;
function CreatePCBLibrary: IPCB_Library;
function CreatePCBWideStringList: IPCB_WideStrings;
function CreatePhysicalLayerMap(ABoard: IPCB_Board): IPCB_GeometryMakerLayerMap;
procedure DestroyPCBContour(var APCBContour: IPCB_Contour);
procedure DestroyPCBLibComp(var APCBLibComp: IPCB_LibComponent);
procedure DestroyPCBLibrary(var APCBLibrary: IPCB_Library);
procedure DestroyPCBObject(var APCBObject: IPCB_Primitive);
procedure DisableFastParams;
procedure DocumentLiveHighlight_Start(ADocumentPath: WideString);
procedure DocumentLiveHighlight_Stop(ADocumentPath: WideString);
procedure EnableFastParams;
function GetCapabilitiesFactory: IPCB_CapabilitiesFactory;
function GetCurrentPCBBoard: IPCB_Board;
function GetCurrentPCBLibrary: IPCB_Library;
function GetOccWrapper: IOccWrapper;
function GetParametersFactory: IPCB_ParametersFactory;
function GetPCBBoardByBoardID(BoardID: Integer): IPCB_Board;
function GetPCBBoardByPath(const APath: WideString): IPCB_Board;
function GetPCBLibraryByLibraryID(LibraryID: Integer): IPCB_Library;
function GetPCBLibraryByPath(const APath: WideString): IPCB_Library;
function GetState_CanFastCrossSelect_Emit: Boolean;
function GetState_CanFastCrossSelect_Receive: Boolean;
function GetState_InteractiveRoutingOptions: IPCB_InteractiveRoutingOptions;
function GetState_PadViaLibraryManager: IPCB_PadViaLibraryManager;
function GetState_ShowStatus: Boolean;
function GetState_SpecialStringConverter: IPCB_SpecialStringConverter;
function GetState_SystemOptions: IPCB_SystemOptions;
function GetState_TTFLettersCache: IPCB_LettersCache;
function GetState_TTFontsCache: IPCB_TTFontsCache;
function GetViolationsFactory: IPCB_ViolationsFactory;
function IsObsoleteRuleKind(ARuleKind: TRuleKind): Boolean;
function LayerSet: IPCB_LayerSetUtils;
function LayerUtils: IPCB_LayerUtils;
function LoadCompFromLibrary(const APattern: WideString; const ALibPath: WideString): IPCB_LibComponent;
function LoadPCBBoardByPath(const APath: WideString): IPCB_Board;
function LoadPCBLibraryByPath(const APath: WideString): IPCB_Library;
function LoadPCBLibraryFromFile(const APath: WideString): IPCB_Library;
function PaintFootprintThumbnail(ViewName: WideString; ViewFileAddress: WideString; Width: Integer; Height: Integer): HBITMAP;
procedure PcbApi_Export_ToPainter(var APainter: IInterface; LibReference: string; LibraryPath: string);
function PCBClassFactory(const AClassKind: TObjectId): IPCB_ObjectClass;
function PCBClassFactoryByClassMember(const AClassKind: TClassMemberKind): IPCB_ObjectClass;
function PCBContourFactory: IPCB_Contour;
function PCBContourMaker: IPCB_ContourMaker;
function PCBContourUtilities: IPCB_ContourUtilities;
function PCBGeometricPolygonFactory: IPCB_GeometricPolygon;
function PCBGeometryMaker: IPCB_GeometryMaker;
function PCBObjectFactory(const AObjectId: TObjectId; const ADimensionKind: TDimensionKind; const ACreationMode: TObjectCreationMode): IPCB_Primitive;
function PCBRuleFactory(const ARuleKind: TRuleKind): IPCB_Rule;
procedure PostBatchProcess;
procedure PostProcess;
procedure PostProcess_Clustered;
procedure PreBatchProcess;
procedure PreProcess;
procedure PreProcess_Clustered;
function PrimitiveComparator: IPCB_PrimitiveComparator;
procedure RefreshDocumentView(ADocumentPath: WideString);
function RunFontEditorDialog(var ATextHeight: Integer; var AUseTTFont: Boolean; var AStrokeFontName: WideString; var AStrokeWidth: Integer; var ATTFontName: WideString; var ATTBold: Boolean; var ATTItalic: Boolean; var ATTInverted: Boolean; var ATTInvertedBorder: Integer): Boolean;
procedure SendMessageToRobots(Source: Pointer; Destination: Pointer; MessageID: Word; MessageData: Pointer);
procedure SetState_CanFastCrossSelect_Receive(b: Boolean);
procedure SetState_ShowStatus(AValue: Boolean);

## IPCB_ShapeEdge
继承：IPCB_ShapeEdge → IInterface ｜ 单元：RT_PCB ｜ 自有 10 个方法、6 个属性

property EdgeType: TPCB_ShapeEdgeType read GetState_EdgeType;  // read-only
property EndPt: TCoordPoint read GetState_EndPt write SetState_EndPt;
property StartPt: TCoordPoint read GetState_StartPt write SetState_StartPt;
property SubPt[Index: Integer]: TCoordPoint read GetState_SubPt;  // read-only
property SubPtCount: Integer read GetState_SubPtCount;  // read-only
property UserData: TPCBString read GetState_UserData write SetState_UserData;
procedure ClearShape;
function GetState_EdgeType: TPCB_ShapeEdgeType;
function GetState_EndPt: IDispatch;
function GetState_StartPt: IDispatch;
function GetState_SubPt(Index: Integer): IDispatch;
function GetState_SubPtCount: Integer;
function GetState_UserData: WideString;
procedure SetState_EndPt(const Value: IDispatch);
procedure SetState_StartPt(const Value: IDispatch);
procedure SetState_UserData(const Value: WideString);

## IPCB_ShapeEdge_BSpline
继承：IPCB_ShapeEdge_BSpline → IPCB_ShapeEdge → IInterface ｜ 单元：RT_PCB ｜ 自有 12 个方法、6 个属性

property CPoint[I: Integer]: TCoordPoint read GetState_CPoint write SetState_CPoint;
property CPointsCount: Integer read GetState_CPointsCount write SetState_CPointsCount;
property Degree: Integer read GetState_Degree write SetState_Degree;
property IsClosed: Boolean read GetState_IsClosed write SetState_IsClosed;
property Knot[I: Integer]: TDouble read GetState_Knot write SetState_Knot;
property KnotCount: Integer read GetState_KnotCount;  // read-only
function GetState_CPoint(I: Integer): IDispatch;
function GetState_CPointsCount: Integer;
function GetState_Degree: Integer;
function GetState_IsClosed: Boolean;
function GetState_Knot(I: Integer): Double;
function GetState_KnotCount: Integer;
procedure SetDefaultKnots;
procedure SetState_CPoint(I: Integer; const Value: IDispatch);
procedure SetState_CPointsCount(const Value: Integer);
procedure SetState_Degree(const Value: Integer);
procedure SetState_IsClosed(const Value: Boolean);
procedure SetState_Knot(I: Integer; const Value: Double);

## IPCB_ShapeEdge_Circle
继承：IPCB_ShapeEdge_Circle → IPCB_ShapeEdge → IInterface ｜ 单元：RT_PCB ｜ 自有 11 个方法、6 个属性

property AngleEnd: TDouble read GetState_AngleEnd;  // read-only
property AngleStart: TDouble read GetState_AngleStart;  // read-only
property Center: TCoordPoint read GetState_Center write SetState_Center;
property ClockWise: Boolean read GetState_ClockWise write SetState_ClockWise;
property IsClosed: Boolean read GetState_IsClosed write SetState_IsClosed;
property Radius: TCoord read GetState_Radius write SetState_Radius;
procedure FillClosed(const Center: IDispatch; Radius: Integer);
function GetState_AngleEnd: Double;
function GetState_AngleStart: Double;
function GetState_Center: IDispatch;
function GetState_ClockWise: Boolean;
function GetState_IsClosed: Boolean;
function GetState_Radius: Integer;
procedure SetState_Center(const Value: IDispatch);
procedure SetState_ClockWise(const Value: Boolean);
procedure SetState_IsClosed(const Value: Boolean);
procedure SetState_Radius(const Value: Integer);

## IPCB_ShapeEdge_CircleUtils
继承：IPCB_ShapeEdge_CircleUtils → IInterface ｜ 单元：RT_PCB ｜ 自有 2 个方法、1 个属性

property CentralAngle: TDouble read Get_CentralAngle write Set_CentralAngle;
function Get_CentralAngle: Double;
procedure Set_CentralAngle(const Value: Double);

## IPCB_ShapeEdge_Ellipse
继承：IPCB_ShapeEdge_Ellipse → IPCB_ShapeEdge → IInterface ｜ 单元：RT_PCB ｜ 自有 12 个方法、5 个属性

property Center: TCoordPoint read GetState_Center write SetState_Center;
property ClockWise: Boolean read GetState_ClockWise write SetState_ClockWise;
property IsClosed: Boolean read GetState_IsClosed write SetState_IsClosed;
property MajorPt: TCoordPoint read GetState_MajorPt write SetState_MajorPt;
property MinorPt: TCoordPoint read GetState_MinorPt write SetState_MinorPt;
procedure Fill(const Center: IDispatch; const MinorPt: IDispatch; const MajorPt: IDispatch; const StartPt: IDispatch; const EndPt: IDispatch; ClockWise: Boolean);
procedure FillClosed(const Center: IDispatch; const MinorPt: IDispatch; const MajorPt: IDispatch);
function GetState_Center: IDispatch;
function GetState_ClockWise: Boolean;
function GetState_IsClosed: Boolean;
function GetState_MajorPt: IDispatch;
function GetState_MinorPt: IDispatch;
procedure SetState_Center(const Value: IDispatch);
procedure SetState_ClockWise(const Value: Boolean);
procedure SetState_IsClosed(const Value: Boolean);
procedure SetState_MajorPt(const Value: IDispatch);
procedure SetState_MinorPt(const Value: IDispatch);

## IPCB_ShapeEdge_Line
继承：IPCB_ShapeEdge_Line → IPCB_ShapeEdge → IInterface ｜ 单元：RT_PCB ｜ 自有 0 个方法、0 个属性


## IPCB_ShapeEdge_Parabola
继承：IPCB_ShapeEdge_Parabola → IPCB_ShapeEdge → IInterface ｜ 单元：RT_PCB ｜ 自有 5 个方法、2 个属性

property Focus: TCoordPoint read GetState_Focus write SetState_Focus;
property Vertex: TCoordPoint read GetState_Vertex write SetState_Vertex;
procedure Fill(const AVertex: IDispatch; const AFocus: IDispatch; const AStartPt: IDispatch; const AEndPt: IDispatch);
function GetState_Focus: IDispatch;
function GetState_Vertex: IDispatch;
procedure SetState_Focus(const Value: IDispatch);
procedure SetState_Vertex(const Value: IDispatch);

## IPCB_Shapes
继承：IPCB_Shapes → IInterface ｜ 单元：RT_PCB ｜ 自有 2 个方法、0 个属性

function Count: Integer;
function Items(Index: Integer): IPCB_RegionShape;

## IPCB_Sheet
继承：IPCB_Sheet → IInterface ｜ 单元：RT_PCB ｜ 自有 14 个方法、6 个属性

property LockSheet: Boolean read GetState_LockSheet write SetState_LockSheet;
property SheetHeight: TCoord read GetState_SheetHeight write SetState_SheetHeight;
property SheetWidth: TCoord read GetState_SheetWidth write SetState_SheetWidth;
property SheetX: TCoord read GetState_SheetX write SetState_SheetX;
property SheetY: TCoord read GetState_SheetY write SetState_SheetY;
property ShowSheet: Boolean read GetState_ShowSheet write SetState_ShowSheet;
function GetState_LockSheet: Boolean;
function GetState_SheetHeight: Integer;
function GetState_SheetWidth: Integer;
function GetState_SheetX: Integer;
function GetState_SheetY: Integer;
function GetState_ShowSheet: Boolean;
function I_ObjectAddress: Pointer;
procedure SetState_LockSheet(Value: Boolean);
procedure SetState_SheetHeight(Value: Integer);
procedure SetState_SheetWidth(Value: Integer);
procedure SetState_SheetX(Value: Integer);
procedure SetState_SheetY(Value: Integer);
procedure SetState_ShowSheet(Value: Boolean);
procedure UpdateSheetPosition;

## IPCB_ShortCircuitConstraint
继承：IPCB_ShortCircuitConstraint → IPCB_Rule → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 2 个方法、1 个属性

property Allowed: Boolean read GetState_Allowed write SetState_Allowed;
function GetState_Allowed: Boolean;
procedure SetState_Allowed(Value: Boolean);

## IPCB_SignalLayer
继承：IPCB_SignalLayer → IPCB_ElectricalLayer → IPCB_PhysicalLayer → IPCB_LayerObject → IInterface ｜ 单元：RT_PCB ｜ 自有 2 个方法、1 个属性

property ComponentPlacement: TComponentPlacementType read GetState_ComponentPlacement write SetState_ComponentPlacement;
function GetState_ComponentPlacement: TComponentPlacementType;
procedure SetState_ComponentPlacement(AValue: TComponentPlacementType);

## IPCB_SignalStimulus
继承：IPCB_SignalStimulus → IPCB_Rule → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 11 个方法、5 个属性

property Kind: TStimulusType read GetState_Kind write SetState_Kind;
property Level: TSignalLevel read GetState_Level write SetState_Level;
property PeriodTime: Double read GetState_PeriodTime write SetState_PeriodTime;
property StartTime: Double read GetState_StartTime write SetState_StartTime;
property StopTime: Double read GetState_StopTime write SetState_StopTime;
procedure Export_ToStmFile(AFilename: WideString);
function GetState_Kind: TStimulusType;
function GetState_Level: TSignalLevel;
function GetState_PeriodTime: Double;
function GetState_StartTime: Double;
function GetState_StopTime: Double;
procedure SetState_Kind(Value: TStimulusType);
procedure SetState_Level(Value: TSignalLevel);
procedure SetState_PeriodTime(Value: Double);
procedure SetState_StartTime(Value: Double);
procedure SetState_StopTime(Value: Double);

## IPCB_SilkToSilkClearanceRule
继承：IPCB_SilkToSilkClearanceRule → IPCB_Rule → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 2 个方法、1 个属性

property SilkToSilkClearance: TCoord read GetState_SilkToSilkClearance write SetState_SilkToSilkClearance;
function GetState_SilkToSilkClearance: Integer;
procedure SetState_SilkToSilkClearance(Value: Integer);

## IPCB_SilkToSolderMaskClearanceRule
继承：IPCB_SilkToSolderMaskClearanceRule → IPCB_Rule → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 4 个方法、2 个属性

property IsClearanceToExposedCopper: Boolean read GetState_IsClearanceToExposedCopper write SetState_IsClearanceToExposedCopper;
property SilkToMaskGap: TCoord read GetState_SilkToMaskGap write SetState_SilkToMaskGap;
function GetState_IsClearanceToExposedCopper: Boolean;
function GetState_SilkToMaskGap: Integer;
procedure SetState_IsClearanceToExposedCopper(Value: Boolean);
procedure SetState_SilkToMaskGap(Value: Integer);

## IPCB_SilkscreenClipperSettings
继承：IPCB_SilkscreenClipperSettings → IInterface ｜ 单元：RT_PCB ｜ 自有 24 个方法、12 个属性

property DeleteOutside: Boolean read GetDeleteOutside write SetDeleteOutside;
property DistanceToBoardShape: TCoord read GetDistanceToBoardShape write SetDistanceToBoardShape;
property DistanceToSolderMask: Integer read GetDistanceToSolderMask write SetDistanceToSolderMask;
property FillRegionAction: TProcessAction read GetFillRegionAction write SetFillRegionAction;
property IncludeLockedPrims: Boolean read GetIncludeLockedPrims write SetIncludeLockedPrims;
property LayerScope: TOverlayLayerScope read GetLayerScope write SetLayerScope;
property MaxMoveDistance: TCoord read GetMaxMoveDistance write SetMaxMoveDistance;
property MinimumLength: TCoord read GetMinimumLength write SetMinimumLength;
property MoveText: Boolean read GetMoveText write SetMoveText;
property SelectedOnly: Boolean read GetSelectedOnly write SetSelectedOnly;
property UseBoardClearanceRule: Boolean read GetUseBoardClearanceRule write SetUseBoardClearanceRule;
property UseToSolderHoleRule: Boolean read GetUseToSolderHoleRule write SetUseToSolderHoleRule;
function GetDeleteOutside: Boolean;
function GetDistanceToBoardShape: Integer;
function GetDistanceToSolderMask: Integer;
function GetFillRegionAction: TProcessAction;
function GetIncludeLockedPrims: Boolean;
function GetLayerScope: TOverlayLayerScope;
function GetMaxMoveDistance: Integer;
function GetMinimumLength: Integer;
function GetMoveText: Boolean;
function GetSelectedOnly: Boolean;
function GetUseBoardClearanceRule: Boolean;
function GetUseToSolderHoleRule: Boolean;
procedure SetDeleteOutside(const AValue: Boolean);
procedure SetDistanceToBoardShape(const AValue: Integer);
procedure SetDistanceToSolderMask(const AValue: Integer);
procedure SetFillRegionAction(const AValue: TProcessAction);
procedure SetIncludeLockedPrims(const AValue: Boolean);
procedure SetLayerScope(const AValue: TOverlayLayerScope);
procedure SetMaxMoveDistance(const AValue: Integer);
procedure SetMinimumLength(const AValue: Integer);
procedure SetMoveText(const AValue: Boolean);
procedure SetSelectedOnly(const AValue: Boolean);
procedure SetUseBoardClearanceRule(const AValue: Boolean);
procedure SetUseToSolderHoleRule(const AValue: Boolean);

## IPCB_SketchesGridManager
继承：IPCB_SketchesGridManager → IInterface ｜ 单元：RT_PCB ｜ 自有 14 个方法、0 个属性

function GetState_EnableGrid: Boolean;
function GetState_HorizontalOffset: Integer;
function GetState_HorizontalSize: Integer;
function GetState_PlaneKind: TPlaneKind;
function GetState_Rotation: Double;
function GetState_VerticalOffset: Integer;
function GetState_VerticalSize: Integer;
procedure SetState_EnableGrid(AValue: Boolean);
procedure SetState_HorizontalOffset(AValue: Integer);
procedure SetState_HorizontalSize(AValue: Integer);
procedure SetState_PlaneKind(AValue: TPlaneKind);
procedure SetState_Rotation(AValue: Double);
procedure SetState_VerticalOffset(AValue: Integer);
procedure SetState_VerticalSize(AValue: Integer);

## IPCB_SlidingRoutingProcess
继承：IPCB_SlidingRoutingProcess → IPCB_InteractiveProcess → IInteractiveProcess ｜ 单元：RT_PCB ｜ 自有 37 个方法、0 个属性

procedure EditMatchedNetLengthsRule;
procedure EditMaxMinWidthRule;
procedure EditRoutingViaStyleRule;
function GetRoutingOptions: IPCB_RoutingOptionsPage;
function GetState_AllowViaPusing: Boolean;
function GetState_DisplayClearanceBoundaries: Boolean;
function GetState_GlossEffort: TGlossEffort;
function GetState_HuggingStyle: THuggingStyle;
function GetState_IsSingleNet: Boolean;
function GetState_Layer: Integer;
function GetState_MatchedNetLengthsRule: IPCB_MatchedNetLengthsConstraint;
function GetState_MinimumArcSize: Double;
function GetState_MiterSize: Double;
function GetState_NeighborGlossEffort: TGlossEffort;
function GetState_Net: IPCB_Net;
function GetState_NetDelay: Double;
function GetState_NetLength: Int64;
function GetState_PadEntryStability: Integer;
function GetState_ReduceClearanceDisplayArea: Boolean;
function GetState_RoutingViaStyleRule: IPCB_RoutingViaStyleRule;
function GetState_ShowLengthGauge: Boolean;
function GetState_Sliding: TAdvancedRouteMode;
function GetState_VertexAction: TVertexAction;
function GetState_WidthRule: IPCB_MaxMinWidthConstraint;
procedure SetState_AllowViaPusing(ANewValue: Boolean);
procedure SetState_DisplayClearanceBoundaries(ANewValue: Boolean);
procedure SetState_GlossEffort(ANewValue: TGlossEffort);
procedure SetState_HuggingStyle(ANewValue: THuggingStyle);
procedure SetState_IsSingleNet(ANewValue: Boolean);
procedure SetState_MinimumArcSize(ANewValue: Double);
procedure SetState_MiterSize(ANewValue: Double);
procedure SetState_NeighborGlossEffort(ANewValue: TGlossEffort);
procedure SetState_PadEntryStability(ANewValue: Integer);
procedure SetState_ReduceClearanceDisplayArea(ANewValue: Boolean);
procedure SetState_ShowLengthGauge(ANewValue: Boolean);
procedure SetState_Sliding(ANewValue: TAdvancedRouteMode);
procedure SetState_VertexAction(ANewValue: TVertexAction);

## IPCB_SmartUnionObject
继承：IPCB_SmartUnionObject → IPCB_SmartUnionPlaceHolder → IPCB_RectangularPrimitive → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 44 个方法、17 个属性

property Alignment: TSmartUnionAlignmentType read GetState_Alignment write SetState_Alignment;
property BasePoint: TCoordPoint read GetState_BasePoint;  // read-only
property ExpansionEnabled: Boolean read GetState_ExpansionEnabled write SetState_ExpansionEnabled;
property IsValid: Boolean read GetState_Valid;  // read-only
property MaxHeight: TCoord read GetState_MaxHeight;  // read-only
property Placeholder: IPCB_Primitive read GetState_Placeholder;  // read-only
property Primitives: IInterfaceListEx read GetState_Primitives;  // read-only
property PrimitivesLocked: Boolean read GetState_PrimitivesLocked write SetState_PrimitivesLocked;
property RotationCenter: TCoordPoint read GetState_RotationCenter;  // read-only
property RotationHandle: TCoordPoint read GetState_RotationHandle;  // read-only
property RotationHandleEnabled: Boolean read GetState_RotationHandleEnabled write SetState_RotationHandleEnabled;
property RotationHandleOffset: TCoord read GetState_RotationHandleOffset write SetState_RotationHandleOffset;
property ShowUnionShape: Boolean read GetState_ShowUnionShape write SetState_ShowUnionShape;
property SilentRotate: Boolean read GetState_SilentRotate write SetState_SilentRotate;
property Size: TCoordPoint read GetState_Size;  // read-only
property UnionType: TSmartUnionObjectType read GetState_UnionType;  // read-only
property UseMiddleHandles: Boolean read GetState_UseMiddleHandles write SetState_UseMiddleHandles;
function AddArc(ACX: Integer; ACY: Integer; ARadius: Integer; ALineWidth: Integer; AAngle1: Double; AAngle2: Double): IPCB_Arc;
function AllowSelectPrimsInUnion: Boolean;
procedure CancelGroupWarehouseRegistration(APrimitive: IPCB_Primitive);
procedure DeleteObjectFromUnion;
procedure DoDraw(ABoard: IPCB_Board);
function EditingHandlesEnabled: Boolean;
procedure ExplodeToPrimitives;
procedure FreePrimitives;
procedure FromString(aString: string);
function GetState_Alignment: TSmartUnionAlignmentType;
function GetState_BasePoint: IDispatch;
function GetState_ExpansionEnabled: Boolean;
function GetState_MaxHeight: Integer;
function GetState_Placeholder: IPCB_Primitive;
function GetState_Primitives: IInterfaceListEx;
function GetState_PrimitivesLocked: Boolean;
function GetState_RotationCenter: IDispatch;
function GetState_RotationHandle: IDispatch;
function GetState_RotationHandleEnabled: Boolean;
function GetState_RotationHandleOffset: Integer;
function GetState_ShowUnionShape: Boolean;
function GetState_SilentRotate: Boolean;
function GetState_Size: IDispatch;
function GetState_UnionType: TSmartUnionObjectType;
function GetState_UseMiddleHandles: Boolean;
function GetState_Valid: Boolean;
procedure HandleBeforeClear;
procedure Invalidate;
function IsAccessible(AAction: TEditingAction): Boolean;
function IsPrimitiveValidForUnion(APrimitive: IPCB_Primitive): Boolean;
procedure MoveByPlaceHolder;
procedure NotifyPrimitiveMove(AX: Integer; AY: Integer; APrimitive: IPCB_Primitive);
procedure RebuildAfterLoad;
procedure RegisterOnBoard(ABoard: IPCB_Board);
procedure RegisterWithGroupWarehouse(APrimitive: IPCB_Primitive);
procedure SetState_Alignment(AValue: TSmartUnionAlignmentType);
procedure SetState_ExpansionEnabled(AValue: Boolean);
procedure SetState_PrimitivesLocked(ALocked: Boolean);
procedure SetState_RotationHandleEnabled(AValue: Boolean);
procedure SetState_RotationHandleOffset(AValue: Integer);
procedure SetState_ShowUnionShape(AValue: Boolean);
procedure SetState_SilentRotate(AValue: Boolean);
procedure SetState_UseMiddleHandles(AValue: Boolean);
procedure UnRegisterFromBoard(ABoard: IPCB_Board);

## IPCB_SmartUnionPlaceHolder
继承：IPCB_SmartUnionPlaceHolder → IPCB_RectangularPrimitive → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 0 个方法、0 个属性


## IPCB_SolderMaskExpansionRule
继承：IPCB_SolderMaskExpansionRule → IPCB_Rule → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 10 个方法、1 个属性

property Expansion: TCoord read GetState_Expansion write SetState_Expansion;
function GetState_Expansion: Integer;
function GetState_ExpansionBottom: Integer;
function GetState_FromHoleEdge: Boolean;
function GetState_UseSeparateExpansions: Boolean;
procedure SetState_Expansion(Value: Integer);
procedure SetState_ExpansionBottom(Value: Integer);
procedure SetState_FromHoleEdge(Value: Boolean);
procedure SetState_IsTenting_Bottom(Value: Boolean);
procedure SetState_IsTenting_Top(Value: Boolean);
procedure SetState_UseSeparateExpansions(Value: Boolean);

## IPCB_SolderMaskLayer
继承：IPCB_SolderMaskLayer → IPCB_DielectricLayer → IPCB_PhysicalLayer → IPCB_LayerObject → IInterface ｜ 单元：RT_PCB ｜ 自有 2 个方法、1 个属性

property Expansion: TCoord read GetState_GetExpansion write SetState_SetExpansion;
function GetState_GetExpansion: Integer;
procedure SetState_SetExpansion(AValue: Integer);

## IPCB_SpatialIterator
继承：IPCB_SpatialIterator → IPCB_AbstractIterator → IInterface ｜ 单元：RT_PCB ｜ 自有 1 个方法、0 个属性

procedure AddFilter_ProcessSpecialLayers;

## IPCB_SpecctraDSNFile
继承：IPCB_SpecctraDSNFile → IInterface ｜ 单元：RT_PCB ｜ 自有 2 个方法、0 个属性

procedure ImportFile(const AFilePath: WideString);
function IsValidSpecctraDSNFile(const AFilename: WideString): Boolean;

## IPCB_SpecctraRouterOptions
继承：IPCB_SpecctraRouterOptions → IPCB_AbstractOptions → IInterface ｜ 单元：RT_PCB ｜ 自有 108 个方法、54 个属性

property Adv10: Boolean read GetState_Adv10 write SetState_Adv10;
property AdvancedDo: Boolean read GetState_AdvancedDo write SetState_AdvancedDo;
property BusDiagonal: Boolean read GetState_BusDiagonal write SetState_BusDiagonal;
property CleanPasses: Integer read GetState_CleanPasses write SetState_CleanPasses;
property CrossCost: TCCTCost read GetState_CrossCost write SetState_CrossCost;
property CrossTax: TCCTTax read GetState_CrossTax write SetState_CrossTax;
property Dfm10: Boolean read GetState_Dfm10 write SetState_Dfm10;
property DoBus: Boolean read GetState_DoBus write SetState_DoBus;
property DoCritic: Boolean read GetState_DoCritic write SetState_DoCritic;
property DoFanout: Boolean read GetState_DoFanout write SetState_DoFanout;
property DoMiter: Boolean read GetState_DoMiter write SetState_DoMiter;
property DoQuit: Boolean read GetState_DoQuit write SetState_DoQuit;
property DoRecorner: Boolean read GetState_DoRecorner write SetState_DoRecorner;
property DoSeedVias: Boolean read GetState_DoSeedVias write SetState_DoSeedVias;
property DoSetback[I: Integer]: Boolean read GetState_DoSetback write SetState_DoSetback;
property DoSpread: Boolean read GetState_DoSpread write SetState_DoSpread;
property FilterPasses: Integer read GetState_FilterPasses write SetState_FilterPasses;
property FoIn: Boolean read GetState_FoIn write SetState_FoIn;
property FoOut: Boolean read GetState_FoOut write SetState_FoOut;
property FoPads: Boolean read GetState_FoPads write SetState_FoPads;
property FoPasses: Integer read GetState_FoPasses write SetState_FoPasses;
property FoPower: Boolean read GetState_FoPower write SetState_FoPower;
property ForceVias: Boolean read GetState_ForceVias write SetState_ForceVias;
property FoSignal: Boolean read GetState_FoSignal write SetState_FoSignal;
property FoVias: Boolean read GetState_FoVias write SetState_FoVias;
property Hyb10: Boolean read GetState_Hyb10 write SetState_Hyb10;
property LayerCost[L: TV6_Layer]: TCCTCost read GetState_LayerCost write SetState_LayerCost;
property LayerTax[L: TV6_Layer]: TCCTTax read GetState_LayerTax write SetState_LayerTax;
property LayerWWCost[L: TV6_Layer]: TCCTCost read GetState_LayerWWCost write SetState_LayerWWCost;
property LayerWWTax[L: TV6_Layer]: TCCTTax read GetState_LayerWWTax write SetState_LayerWWTax;
property MinimizePads: Boolean read GetState_MinimizePads write SetState_MinimizePads;
property NoConflicts: Boolean read GetState_NoConflicts write SetState_NoConflicts;
property OffCenterCost: TCCTCost read GetState_OffCenterCost write SetState_OffCenterCost;
property OffCenterTax: TCCTTax read GetState_OffCenterTax write SetState_OffCenterTax;
property OffGridCost: TCCTCost read GetState_OffGridCost write SetState_OffGridCost;
property OffGridTax: TCCTTax read GetState_OffGridTax write SetState_OffGridTax;
property ProtectPreRoutes: Boolean read GetState_ProtectPreRoutes write SetState_ProtectPreRoutes;
property ReorderNets: Boolean read GetState_ReorderNets write SetState_ReorderNets;
property RoutePasses: Integer read GetState_RoutePasses write SetState_RoutePasses;
property SeedViaLimit: TCoord read GetState_SeedViaLimit write SetState_SeedViaLimit;
property Setback[I: Integer]: TCoord read GetState_Setback write SetState_Setback;
property SideExitCost: TCCTCost read GetState_SideExitCost write SetState_SideExitCost;
property SideExitTax: TCCTTax read GetState_SideExitTax write SetState_SideExitTax;
property SortDir: TCCTSortDir read GetState_SortDir write SetState_SortDir;
property SortKind: TCCTSort read GetState_SortKind write SetState_SortKind;
property SpVersion: Integer read GetState_SpVersion write SetState_SpVersion;
property SqueezeCost: TCCTCost read GetState_SqueezeCost write SetState_SqueezeCost;
property SqueezeTax: TCCTTax read GetState_SqueezeTax write SetState_SqueezeTax;
property ViaCost: TCCTCost read GetState_ViaCost write SetState_ViaCost;
property ViaGrid: TReal read GetState_ViaGrid write SetState_ViaGrid;
property ViaTax: TCCTTax read GetState_ViaTax write SetState_ViaTax;
property WireGrid: TReal read GetState_WireGrid write SetState_WireGrid;
property WwCost: TCCTCost read GetState_WwCost write SetState_WwCost;
property WwTax: TCCTTax read GetState_WwTax write SetState_WwTax;
function GetState_Adv10: Boolean;
function GetState_AdvancedDo: Boolean;
function GetState_BusDiagonal: Boolean;
function GetState_CleanPasses: Integer;
function GetState_CrossCost: TCCTCost;
function GetState_CrossTax: Double;
function GetState_Dfm10: Boolean;
function GetState_DoBus: Boolean;
function GetState_DoCritic: Boolean;
function GetState_DoFanout: Boolean;
function GetState_DoMiter: Boolean;
function GetState_DoQuit: Boolean;
function GetState_DoRecorner: Boolean;
function GetState_DoSeedVias: Boolean;
function GetState_DoSetback(I: Integer): Boolean;
function GetState_DoSpread: Boolean;
function GetState_FilterPasses: Integer;
function GetState_FoIn: Boolean;
function GetState_FoOut: Boolean;
function GetState_FoPads: Boolean;
function GetState_FoPasses: Integer;
function GetState_FoPower: Boolean;
function GetState_ForceVias: Boolean;
function GetState_FoSignal: Boolean;
function GetState_FoVias: Boolean;
function GetState_Hyb10: Boolean;
function GetState_LayerCost(L: TV6_Layer): TCCTCost;
function GetState_LayerTax(L: TV6_Layer): Double;
function GetState_LayerWWCost(L: TV6_Layer): TCCTCost;
function GetState_LayerWWTax(L: TV6_Layer): Double;
function GetState_MinimizePads: Boolean;
function GetState_NoConflicts: Boolean;
function GetState_OffCenterCost: TCCTCost;
function GetState_OffCenterTax: Double;
function GetState_OffGridCost: TCCTCost;
function GetState_OffGridTax: Double;
function GetState_ProtectPreRoutes: Boolean;
function GetState_ReorderNets: Boolean;
function GetState_RoutePasses: Integer;
function GetState_SeedViaLimit: Integer;
function GetState_Setback(I: Integer): Integer;
function GetState_SideExitCost: TCCTCost;
function GetState_SideExitTax: Double;
function GetState_SortDir: TCCTSortDir;
function GetState_SortKind: TCCTSort;
function GetState_SpVersion: Integer;
function GetState_SqueezeCost: TCCTCost;
function GetState_SqueezeTax: Double;
function GetState_ViaCost: TCCTCost;
function GetState_ViaGrid: Double;
function GetState_ViaTax: Double;
function GetState_WireGrid: Double;
function GetState_WwCost: TCCTCost;
function GetState_WwTax: Double;
procedure SetState_Adv10(Value: Boolean);
procedure SetState_AdvancedDo(Value: Boolean);
procedure SetState_BusDiagonal(Value: Boolean);
procedure SetState_CleanPasses(Value: Integer);
procedure SetState_CrossCost(Value: TCCTCost);
procedure SetState_CrossTax(Value: Double);
procedure SetState_Dfm10(Value: Boolean);
procedure SetState_DoBus(Value: Boolean);
procedure SetState_DoCritic(Value: Boolean);
procedure SetState_DoFanout(Value: Boolean);
procedure SetState_DoMiter(Value: Boolean);
procedure SetState_DoQuit(Value: Boolean);
procedure SetState_DoRecorner(Value: Boolean);
procedure SetState_DoSeedVias(Value: Boolean);
procedure SetState_DoSetback(I: Integer; Value: Boolean);
procedure SetState_DoSpread(Value: Boolean);
procedure SetState_FilterPasses(Value: Integer);
procedure SetState_FoIn(Value: Boolean);
procedure SetState_FoOut(Value: Boolean);
procedure SetState_FoPads(Value: Boolean);
procedure SetState_FoPasses(Value: Integer);
procedure SetState_FoPower(Value: Boolean);
procedure SetState_ForceVias(Value: Boolean);
procedure SetState_FoSignal(Value: Boolean);
procedure SetState_FoVias(Value: Boolean);
procedure SetState_Hyb10(Value: Boolean);
procedure SetState_LayerCost(L: TV6_Layer; Value: TCCTCost);
procedure SetState_LayerTax(L: TV6_Layer; Value: Double);
procedure SetState_LayerWWCost(L: TV6_Layer; Value: TCCTCost);
procedure SetState_LayerWWTax(L: TV6_Layer; Value: Double);
procedure SetState_MinimizePads(Value: Boolean);
procedure SetState_NoConflicts(Value: Boolean);
procedure SetState_OffCenterCost(Value: TCCTCost);
procedure SetState_OffCenterTax(Value: Double);
procedure SetState_OffGridCost(Value: TCCTCost);
procedure SetState_OffGridTax(Value: Double);
procedure SetState_ProtectPreRoutes(Value: Boolean);
procedure SetState_ReorderNets(Value: Boolean);
procedure SetState_RoutePasses(Value: Integer);
procedure SetState_SeedViaLimit(Value: Integer);
procedure SetState_Setback(I: Integer; Value: Integer);
procedure SetState_SideExitCost(Value: TCCTCost);
procedure SetState_SideExitTax(Value: Double);
procedure SetState_SortDir(Value: TCCTSortDir);
procedure SetState_SortKind(Value: TCCTSort);
procedure SetState_SpVersion(Value: Integer);
procedure SetState_SqueezeCost(Value: TCCTCost);
procedure SetState_SqueezeTax(Value: Double);
procedure SetState_ViaCost(Value: TCCTCost);
procedure SetState_ViaGrid(Value: Double);
procedure SetState_ViaTax(Value: Double);
procedure SetState_WireGrid(Value: Double);
procedure SetState_WwCost(Value: TCCTCost);
procedure SetState_WwTax(Value: Double);

## IPCB_SpecialStringConverter
继承：IPCB_SpecialStringConverter → IInterface ｜ 单元：RT_PCB ｜ 自有 12 个方法、0 个属性

procedure AddForbiddenParamList(const AData: IPCB_ParameterList);
procedure AddSpecialStringConverterCache(const AData: IParameterList);
function Convert(const Primitive: IPCB_Primitive; const aString: WideString; out ConvertedString: WideString): Boolean;
function FirstSpecialStringName: WideString;
function GetBoardSpecificSpecialStrings(const ABoard: IPCB_Board): IPCB_WideStrings;
function I_ObjectAddress: Pointer;
function IsVCSRevisionSpecialString(const aString: WideString): Boolean;
function NextSpecialStringName: WideString;
function PopStaticStringValue(const ASpecialString: WideString): Boolean;
function PushStaticStringValue(const ASpecialString: WideString; const ANewValue: WideString): Boolean;
procedure RemoveForbiddenParamList;
procedure RemoveSpecialStringConverterCache;

## IPCB_SplitBoardRegionLine
继承：IPCB_SplitBoardRegionLine → IInterface ｜ 单元：RT_PCB ｜ 自有 4 个方法、0 个属性

function GetState_FromPoint: IDispatch;
function GetState_ToPoint: IDispatch;
function I_ObjectAddress: Pointer;
procedure SetState_FromToPoints(const AFromPoint: IDispatch; const AToPoint: IDispatch);

## IPCB_SplitBoardRegionWithArcs
继承：IPCB_SplitBoardRegionWithArcs → IInterface ｜ 单元：RT_PCB ｜ 自有 4 个方法、4 个属性

property Edge[AIndex: Integer]: IPCB_ShapeEdge read GetProperty_Edge;  // read-only
property EdgeCount: Integer read GetProperty_EdgeCount;  // read-only
property LeftBoardRegion: IPCB_BoardRegion read GetProperty_LeftBoardRegion;  // read-only
property RightBoardRegion: IPCB_BoardRegion read GetProperty_RightBoardRegion;  // read-only
function GetProperty_Edge(AIndex: Integer): IPCB_ShapeEdge;
function GetProperty_EdgeCount: Integer;
function GetProperty_LeftBoardRegion: IPCB_BoardRegion;
function GetProperty_RightBoardRegion: IPCB_BoardRegion;

## IPCB_SplitPlane
继承：IPCB_SplitPlane → IPCB_Group → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 32 个方法、10 个属性

property ArcApproximation: TCoord read GetState_ArcApproximation write SetState_ArcApproximation;
property AreaSize: Extended read GetState_AreaSize write SetState_AreaSize;
property IslandAreaThreshold: Double read GetState_IslandAreaThreshold write SetState_IslandAreaThreshold;
property NeckWidthThreshold: TCoord read GetState_NeckWidthThreshold write SetState_NeckWidthThreshold;
property OptimalVoidRotation: Boolean read GetState_OptimalVoidRotation write SetState_OptimalVoidRotation;
property PointCount: Integer read GetState_PointCount write SetState_PointCount;
property RemoveDead: Boolean read GetState_RemoveDead write SetState_RemoveDead;
property RemoveIslandsByArea: Boolean read GetState_RemoveIslandsByArea write SetState_RemoveIslandsByArea;
property RemoveNarrowNecks: Boolean read GetState_RemoveNarrowNecks write SetState_RemoveNarrowNecks;
property Segments[I: Integer]: TPolySegment read GetState_Segments write SetState_Segments;
function AcceptsLayer(Layer: TV6_Layer): Boolean;
function GetNegativeRegion: IPCB_Region;
function GetState_ArcApproximation: Integer;
function GetState_AreaSize: Extended;
function GetState_HitPrimitive(APrimitive: IPCB_Primitive): Boolean;
function GetState_IslandAreaThreshold: Double;
function GetState_NeckWidthThreshold: Integer;
function GetState_OptimalVoidRotation: Boolean;
function GetState_PointCount: Integer;
function GetState_RemoveDead: Boolean;
function GetState_RemoveIslandsByArea: Boolean;
function GetState_RemoveNarrowNecks: Boolean;
function GetState_Segments(I: Integer): IDispatch;
function GetState_StrictHitTest(HitX: Integer; HitY: Integer): Boolean;
procedure GrowPolyshape(ADist: Integer);
function PointInPolygon(HitX: Integer; HitY: Integer): Boolean;
procedure Pour;
function PrimitiveInsidePoly(APrimitive: IPCB_Primitive): Boolean;
procedure RemovePour;
procedure RotateAroundXY(AX: Integer; AY: Integer; Angle: Double);
procedure SetState_ArcApproximation(AValue: Integer);
procedure SetState_AreaSize(Value: Extended);
procedure SetState_IslandAreaThreshold(AValue: Double);
procedure SetState_NeckWidthThreshold(AValue: Integer);
procedure SetState_OptimalVoidRotation(AValue: Boolean);
procedure SetState_PointCount(Value: Integer);
procedure SetState_RemoveDead(AValue: Boolean);
procedure SetState_RemoveIslandsByArea(AValue: Boolean);
procedure SetState_RemoveNarrowNecks(AValue: Boolean);
procedure SetState_Segments(I: Integer; const Value: IDispatch);
function SetState_XSizeYSize: Boolean;
function xBoundingRectangle: IDispatch;

## IPCB_SplitPlaneRegion
继承：IPCB_SplitPlaneRegion → IPCB_Region → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 2 个方法、1 个属性

property SplitPlane: IPCB_SplitPlane read GetState_SplitPlane write SetState_SplitPlane;
function GetState_SplitPlane: IPCB_SplitPlane;
procedure SetState_SplitPlane(Value: IPCB_SplitPlane);

## IPCB_StackObject
继承：IPCB_StackObject → IInterface ｜ 单元：RT_PCB ｜ 自有 19 个方法、0 个属性

function GetLayerStack: IPCB_LayerStack;
function GetState_Cache: IDispatch;
function GetState_HoleNegativeTolerance: Integer;
function GetState_HolePositiveTolerance: Integer;
function GetState_HoleSize: Integer;
function GetState_Mode: TPadMode;
function GetState_SolderMaskExpansionFromHoleEdge: Boolean;
function GetState_TemplateLink: IPCB_PadViaTemplateLink;
function GetState_XLocation: Integer;
function GetState_YLocation: Integer;
procedure InvalidateCache;
procedure SetState_Cache(const Value: IDispatch);
procedure SetState_HoleNegativeTolerance(Value: Integer);
procedure SetState_HolePositiveTolerance(Value: Integer);
procedure SetState_HoleSize(Value: Integer);
procedure SetState_Mode(Mode: TPadMode);
procedure SetState_SolderMaskExpansionFromHoleEdge(AValue: Boolean);
procedure SetState_XLocation(AX: Integer);
procedure SetState_YLocation(AY: Integer);

## IPCB_SystemOptions
继承：IPCB_SystemOptions → IPCB_AbstractOptions → IInterface ｜ 单元：RT_PCB ｜ 自有 267 个方法、130 个属性

property AreaRectangleSelectionColor: TColor read GetState_AreaRectangleSelectionColor write SetState_AreaRectangleSelectionColor;
property AutoPan: Boolean read GetState_AutoPan write SetState_AutoPan;
property AutoPanLargeStep: Integer read GetState_AutoPanLargeStep write SetState_AutoPanLargeStep;
property AutoPanMode: TAutoPanMode read GetState_AutoPanMode write SetState_AutoPanMode;
property AutoPanSmallStep: Integer read GetState_AutoPanSmallStep write SetState_AutoPanSmallStep;
property AutoPanSpeed: Integer read GetState_AutoPanSpeed write SetState_AutoPanSpeed;
property AutoPanUnit: TAutoPanUnit read GetState_AutoPanUnit write SetState_AutoPanUnit;
property AutoVia: Boolean read GetState_AutoVia write SetState_AutoVia;
property BackgroundMaskLevel: Integer read GetState_BackgroundMaskLevel write SetState_BackgroundMaskLevel;
property BoardAreaColor: TColor read GetState_BoardAreaColor write SetState_BoardAreaColor;
property BoardCursorType: TGraphicsCursor read GetState_BoardCursorType write SetState_BoardCursorType;
property BoardLineColor: TColor read GetState_BoardLineColor write SetState_BoardLineColor;
property CheckComments: Boolean read GetState_CheckComments write SetState_CheckComments;
property CheckPatterns: Boolean read GetState_CheckPatterns write SetState_CheckPatterns;
property CleanRedraw: Boolean read GetState_CleanRedraw write SetState_CleanRedraw;
property ClickClearsSelection: Boolean read GetState_ClickClearsSelection write SetState_ClickClearsSelection;
property Com1Parameters: TSerialParameters read GetState_Com1Parameters write SetState_Com1Parameters;
property Com2Parameters: TSerialParameters read GetState_Com2Parameters write SetState_Com2Parameters;
property Com3Parameters: TSerialParameters read GetState_Com3Parameters write SetState_Com3Parameters;
property Com4Parameters: TSerialParameters read GetState_Com4Parameters write SetState_Com4Parameters;
property ComponentLockPrimitives: Boolean read GetState_ComponentLockPrimitives write SetState_ComponentLockPrimitives;
property ComponentMoveKind: TComponentMoveKind read GetState_ComponentMoveKind write SetState_ComponentMoveKind;
property ComponentRefPointColor: TColor read GetState_ComponentRefPointColor write SetState_ComponentRefPointColor;
property ConfirmSelectionMemoryClear: Boolean read GetState_ConfirmSelectionMemoryClear write SetState_ConfirmSelectionMemoryClear;
property DefaultPrimsPermanent: Boolean read GetState_DefaultPrimsPermanent write SetState_DefaultPrimsPermanent;
property DefaultTTFont: TPCBString read GetState_DefaultTTFont write SetState_DefaultTTFont;
property DeleteDeadEnds: Boolean read GetState_DeleteDeadEnds write SetState_DeleteDeadEnds;
property DeleteUnconnectedComps: Boolean read GetState_DeleteUnconnectedComps write SetState_DeleteUnconnectedComps;
property DeleteUnconnectedPrims: Boolean read GetState_DeleteUnconnectedPrims write SetState_DeleteUnconnectedPrims;
property DisplaySpecialStrings: Boolean read GetState_DisplaySpecialStrings write SetState_DisplaySpecialStrings;
property DoOnlineDRC: Boolean read GetState_DoOnlineDRC write SetState_DoOnlineDRC;
property DoubleClickRunsInspector: Boolean read GetState_DoubleClickRunsInspector write SetState_DoubleClickRunsInspector;
property DraftTrackThreshold: TCoord read GetState_DraftTrackThreshold write SetState_DraftTrackThreshold;
property DragMode: TPcbDragMode read GetState_DragMode write SetState_DragMode;
property DragVertexAction: TVertexAction read GetState_DragVertexAction write SetState_DragVertexAction;
property DrawMode[OId: TObjectId]: TDrawMode read GetState_DrawMode write SetState_DrawMode;
property DuplicateDesignatorsAllowed: Boolean read GetState_DuplicateDesignatorsAllowed write SetState_DuplicateDesignatorsAllowed;
property FilteredObjectsBlend: Integer read GetState_FilteredObjectsBlend write SetState_FilteredObjectsBlend;
property FirstDimensionLine: TColor read GetState_FirstDimensionLine write SetState_FirstDimensionLine;
property FractionalDigits[aUnit: TUnit]: Integer read GetState_FractionalDigits write SetState_FractionalDigits;
property FromTosDisplayMode: TFromToDisplayMode read GetState_FromTosDisplayMode write SetState_FromTosDisplayMode;
property GlobalEditIncludeArcsWithTracks: Boolean read GetState_GlobalEditIncludeArcsWithTracks write SetState_GlobalEditIncludeArcsWithTracks;
property HighlightFull: Boolean read GetState_HighlightFull write SetState_HighlightFull;
property HighlightObjectsBlend: Integer read GetState_HighlightObjectsBlend write SetState_HighlightObjectsBlend;
property HoldShiftToSelectObjectId[OId: TObjectId]: Boolean read GetState_HoldShiftToSelectObjectId write SetState_HoldShiftToSelectObjectId;
property HuggingStyle: THuggingStyle read GetState_HuggingStyle write SetState_HuggingStyle;
property InteractiveRouteMode: TInteractiveRouteMode read GetState_InteractiveRouteMode write SetState_InteractiveRouteMode;
property LayerColors[L: Integer]: TColor read GetState_LayerColors_V7 write SetState_LayerColors_V7;
property LayerColors_V6[L: TV6_Layer]: TColor read GetState_LayerColors write SetState_LayerColors;
property LayerDrawingOrder[I: Integer]: TLayer read GetState_LayerDrawingOrder write SetState_LayerDrawingOrder;
property LayerDrawingOrderCount: Integer read GetState_LayerDrawingOrderCount write SetState_LayerDrawingOrderCount;
property LayerNameDisplayMode: TLayerNameDisplayMode read GetState_LayerNameDisplayMode write SetState_LayerNameDisplayMode;
property LockPreRoutes: Boolean read GetState_LockPreRoutes write SetState_LockPreRoutes;
property LoopRemoval: Boolean read GetState_LoopRemoval write SetState_LoopRemoval;
property MinimumArcSize: Double read GetState_MinimumArcSize write SetState_MinimumArcSize;
property MinPadViaObjectSizeInPixels: Integer read GetState_MinPadViaObjectSizeInPixels write SetState_MinPadViaObjectSizeInPixels;
property MiterSize: Double read GetState_MiterSize write SetState_MiterSize;
property ModelOptions: IPCB_ModelOptions read GetState_ModelOptions;  // read-only
property MustHoldShiftToSelect: Boolean read GetState_MustHoldShiftToSelect write SetState_MustHoldShiftToSelect;
property NearestComponent: Boolean read GetState_NearestComponent write SetState_NearestComponent;
property NetlistReportDialog: Boolean read GetState_NetlistReportDialog write SetState_NetlistReportDialog;
property NetlistReportFile: Boolean read GetState_NetlistReportFile write SetState_NetlistReportFile;
property OnlySelectVisible: Boolean read GetState_OnlySelectVisible write SetState_OnlySelectVisible;
property OriginMarkerColor: TColor read GetState_OriginMarkerColor write SetState_OriginMarkerColor;
property PadEntryStability: Integer read GetState_PadEntryStability write SetState_PadEntryStability;
property PadstackUpdateFromGlobalsOnLoad: TSameNamePadstackReplacementMode read GetState_PadstackUpdateFromGlobalsOnLoad write SetState_PadstackUpdateFromGlobalsOnLoad;
property PadTypesDisplayMode: TFromToDisplayMode read GetState_PadTypesDisplayMode write SetState_PadTypesDisplayMode;
property PadViaFontBkColor: TColor read GetState_PadViaFontBkColor write SetState_PadViaFontBkColor;
property PadViaFontColor: TColor read GetState_PadViaFontColor write SetState_PadViaFontColor;
property PadViaFontName: TPCBString read GetState_PadViaFontName write SetState_PadViaFontName;
property PadViaFontStyle: TFontStyles read GetState_PadViaFontStyle write SetState_PadViaFontStyle;
property PadViaMinFontSize: Integer read GetState_PadViaMinFontSize write SetState_PadViaMinFontSize;
property Paste_HasSameDesignator: Boolean read GetState_Paste_HasSameDesignator write SetState_Paste_HasSameDesignator;
property Paste_InSameClass: Boolean read GetState_Paste_InSameClass write SetState_Paste_InSameClass;
property Paste_InSameNet: Boolean read GetState_Paste_InSameNet write SetState_Paste_InSameNet;
property Paste_OnSameLayer: Boolean read GetState_Paste_OnSameLayer write SetState_Paste_OnSameLayer;
property PlaceShoveDepth: Integer read GetState_PlaceShoveDepth write SetState_PlaceShoveDepth;
property PlaneDrawMode: TPlaneDrawMode read GetState_PlaneDrawMode write SetState_PlaneDrawMode;
property PlowThroughPolygons: Boolean read GetState_PlowThroughPolygons write SetState_PlowThroughPolygons;
property PolygonRepour: TPolygonRepourMode read GetState_PolygonRepour write SetState_PolygonRepour;
property PolygonThreshold: Integer read GetState_PolygonThreshold write SetState_PolygonThreshold;
property ProtectLockedPrimitives: Boolean read GetState_ProtectLockedPrimitives write SetState_ProtectLockedPrimitives;
property QuestionDelete: Boolean read GetState_QuestionDelete write SetState_QuestionDelete;
property QuestionDrag: Boolean read GetState_QuestionDrag write SetState_QuestionDrag;
property QuestionGlobalChange: Boolean read GetState_QuestionGlobalChange write SetState_QuestionGlobalChange;
property RedrawLayerOnToggle: Boolean read GetState_RedrawLayerOnToggle write SetState_RedrawLayerOnToggle;
property RemoveDuplicatesOnOutput: Boolean read GetState_RemoveDuplicatesOnOutput write SetState_RemoveDuplicatesOnOutput;
property RepeatCircular: Boolean read GetState_RepeatCircular write SetState_RepeatCircular;
property RepeatCountDefault: Integer read GetState_RepeatCountDefault write SetState_RepeatCountDefault;
property RepeatDegrees: TGeometry read GetState_RepeatDegrees write SetState_RepeatDegrees;
property RepeatInc: TPCBString read GetState_RepeatInc write SetState_RepeatInc;
property RepeatRotateItem: Boolean read GetState_RepeatRotateItem write SetState_RepeatRotateItem;
property RepeatX: TGeometry read GetState_RepeatX write SetState_RepeatX;
property RepeatXUnit: TUnit read GetState_RepeatXUnit write SetState_RepeatXUnit;
property RepeatY: TGeometry read GetState_RepeatY write SetState_RepeatY;
property RepeatYUnit: TUnit read GetState_RepeatYUnit write SetState_RepeatYUnit;
property ReportsCSV: Boolean read GetState_ReportsCSV write SetState_ReportsCSV;
property RotationStep: TAngle read GetState_RotationStep write SetState_RotationStep;
property RouteGuideColor: TColor read GetState_RouteGuideColor write SetState_RouteGuideColor;
property SameNamePadstackReplacementMode: TSameNamePadstackReplacementMode read GetState_SameNamePadstackReplacementMode write SetState_SameNamePadstackReplacementMode;
property SaveDefs: Boolean read GetState_SaveDefs write SetState_SaveDefs;
property SecondDimensionLine: TColor read GetState_SecondDimensionLine write SetState_SecondDimensionLine;
property ShadowsInPCB: Boolean read GetState_ShadowsInPCB write SetState_ShadowsInPCB;
property SheetAreaColor: TColor read GetState_SheetAreaColor write SetState_SheetAreaColor;
property SheetLineColor: TColor read GetState_SheetLineColor write SetState_SheetLineColor;
property ShowAllPrimitivesInHighlightedNets: Boolean read GetState_ShowAllPrimitivesInHighlightedNets write SetState_ShowAllPrimitivesInHighlightedNets;
property ShowComponentRefPoint: Boolean read GetState_ShowComponentRefPoint write SetState_ShowComponentRefPoint;
property ShowInvisibleObjects: Boolean read GetState_ShowInvisibleObjects write SetState_ShowInvisibleObjects;
property ShowPadNets: Boolean read GetState_ShowPadNets write SetState_ShowPadNets;
property ShowPadNumbers: Boolean read GetState_ShowPadNumbers write SetState_ShowPadNumbers;
property ShowStatusInfo: Boolean read GetState_ShowStatusInfo write SetState_ShowStatusInfo;
property ShowStatusInterval: Integer read GetState_ShowStatusInterval write SetState_ShowStatusInterval;
property ShowTestPoints: Boolean read GetState_ShowTestPoints write SetState_ShowTestPoints;
property ShowViaNets: Boolean read GetState_ShowViaNets write SetState_ShowViaNets;
property ShowViaSpan: Boolean read GetState_ShowViaSpan write SetState_ShowViaSpan;
property SingleLayerMode: Boolean read GetState_SingleLayerMode write SetState_SingleLayerMode;
property SnapToCentre: Boolean read GetState_SnapToCentre write SetState_SnapToCentre;
property TextToRectSize: Integer read GetState_TextToRectSize write SetState_TextToRectSize;
property TouchRectangleSelectionColor: TColor read GetState_TouchRectangleSelectionColor write SetState_TouchRectangleSelectionColor;
property UndoRedoStackSize: Integer read GetState_UndoRedoStackSize write SetState_UndoRedoStackSize;
property UseAmbiguityMenu: Boolean read GetState_AmbiguityMenu write SetState_AmbiguityMenu;
property UseDithered: Boolean read GetState_UseDithered write SetState_UseDithered;
property UseNetColorForHighlight: Boolean read GetState_UseNetColorForHighlight write SetState_UseNetColorForHighlight;
property UseSmartTrackEnds: Boolean read GetState_UseSmartTrackEnds write SetState_UseSmartTrackEnds;
property UseTransparent: Boolean read GetState_UseTransparent write SetState_UseTransparent;
property ValidateOnLoad: Boolean read GetState_ValidateOnLoad write SetState_ValidateOnLoad;
property WaivedDRCErrorColor: TColor read GetState_WaivedDRCErrorColor write SetState_WaivedDRCErrorColor;
property WaivedViolationColor: TColor read GetState_WaivedViolationColor write SetState_WaivedViolationColor;
property WorkspaceColor1: TColor read GetState_WorkspaceColor1 write SetState_WorkspaceColor1;
property WorkspaceColor2: TColor read GetState_WorkspaceColor2 write SetState_WorkspaceColor2;
procedure Export_ToIniFile;
function GetOptionsForGlossRetrace: IPCB_RoutingOptionsPage;
function GetState_AmbiguityMenu: Boolean;
function GetState_AmbiguityThreshold: Integer;
function GetState_AreaRectangleSelectionColor: Cardinal;
function GetState_AutoPan: Boolean;
function GetState_AutoPanLargeStep: Integer;
function GetState_AutoPanMode: TAutoPanMode;
function GetState_AutoPanSmallStep: Integer;
function GetState_AutoPanSpeed: Integer;
function GetState_AutoPanUnit: TAutoPanUnit;
function GetState_AutoVia: Boolean;
function GetState_BackgroundMaskLevel: Integer;
function GetState_BoardAreaColor: Cardinal;
function GetState_BoardCursorType: TGraphicsCursor;
function GetState_BoardLineColor: Cardinal;
function GetState_CheckComments: Boolean;
function GetState_CheckPatterns: Boolean;
function GetState_CleanRedraw: Boolean;
function GetState_ClickClearsSelection: Boolean;
function GetState_Com1Parameters: IDispatch;
function GetState_Com2Parameters: IDispatch;
function GetState_Com3Parameters: IDispatch;
function GetState_Com4Parameters: IDispatch;
function GetState_ComponentLockPrimitives: Boolean;
function GetState_ComponentMoveKind: TComponentMoveKind;
function GetState_ComponentRefPointColor: Cardinal;
function GetState_ConfirmSelectionMemoryClear: Boolean;
function GetState_DefaultPrimsPermanent: Boolean;
function GetState_DefaultTTFont: WideString;
function GetState_DeleteDeadEnds: Boolean;
function GetState_DeleteUnconnectedComps: Boolean;
function GetState_DeleteUnconnectedPrims: Boolean;
function GetState_DisplaySpecialStrings: Boolean;
function GetState_DoOnlineDRC: Boolean;
function GetState_DoubleClickRunsInspector: Boolean;
function GetState_DraftTrackThreshold: Integer;
function GetState_DragMode: TPcbDragMode;
function GetState_DragVertexAction: TVertexAction;
function GetState_DrawMode(OId: TObjectId): TDrawMode;
function GetState_DuplicateDesignatorsAllowed: Boolean;
function GetState_FilteredObjectsBlend: Integer;
function GetState_FirstDimensionLine: Cardinal;
function GetState_FractionalDigits(aUnit: TUnit): Integer;
function GetState_FromTosDisplayMode: TFromToDisplayMode;
function GetState_GlobalEditIncludeArcsWithTracks: Boolean;
function GetState_HighlightColor: Cardinal;
function GetState_HighlightFull: Boolean;
function GetState_HighlightObjectsBlend: Integer;
function GetState_HoldShiftToSelectObjectId(OId: TObjectId): Boolean;
function GetState_HuggingStyle: THuggingStyle;
function GetState_InteractiveRouteMode: TInteractiveRouteMode;
function GetState_LayerColors(L: TV6_Layer): Cardinal;
function GetState_LayerColors_V7(L: Integer): Cardinal;
function GetState_LayerDrawingOrder(I: Integer): Integer;
function GetState_LayerDrawingOrderCount: Integer;
function GetState_LayerNameDisplayMode: TLayerNameDisplayMode;
function GetState_LockPreRoutes: Boolean;
function GetState_LoopRemoval: Boolean;
function GetState_MinimumArcSize: Double;
function GetState_MinPadViaObjectSizeInPixels: Integer;
function GetState_MiterSize: Double;
function GetState_ModelOptions: IPCB_ModelOptions;
function GetState_MustHoldShiftToSelect: Boolean;
function GetState_NearestComponent: Boolean;
function GetState_NetlistReportDialog: Boolean;
function GetState_NetlistReportFile: Boolean;
function GetState_OnlySelectVisible: Boolean;
function GetState_OriginMarkerColor: Cardinal;
function GetState_PadEntryStability: Integer;
function GetState_PadstackUpdateFromGlobalsOnLoad: TSameNamePadstackReplacementMode;
function GetState_PadTypesDisplayMode: TFromToDisplayMode;
function GetState_PadViaFontBkColor: Cardinal;
function GetState_PadViaFontColor: Cardinal;
function GetState_PadViaFontName: WideString;
function GetState_PadViaFontStyle: TFontStyles;
function GetState_PadViaMinFontSize: Integer;
function GetState_Paste_HasSameDesignator: Boolean;
function GetState_Paste_InSameClass: Boolean;
function GetState_Paste_InSameNet: Boolean;
function GetState_Paste_OnSameLayer: Boolean;
function GetState_PlaceShoveDepth: Integer;
function GetState_PlaneDrawMode: TPlaneDrawMode;
function GetState_PlowThroughPolygons: Boolean;
function GetState_PolygonRepour: TPolygonRepourMode;
function GetState_PolygonThreshold: Integer;
function GetState_ProtectLockedPrimitives: Boolean;
function GetState_QuestionDelete: Boolean;
function GetState_QuestionDrag: Boolean;
function GetState_QuestionGlobalChange: Boolean;
function GetState_RedrawLayerOnToggle: Boolean;
function GetState_RemoveDuplicatesOnOutput: Boolean;
function GetState_RepeatCircular: Boolean;
function GetState_RepeatCountDefault: Integer;
function GetState_RepeatDegrees: Double;
function GetState_RepeatInc: WideString;
function GetState_RepeatRotateItem: Boolean;
function GetState_RepeatX: Double;
function GetState_RepeatXUnit: TUnit;
function GetState_RepeatY: Double;
function GetState_RepeatYUnit: TUnit;
function GetState_ReportsCSV: Boolean;
function GetState_RotationStep: Double;
function GetState_RouteGuideColor: Cardinal;
function GetState_SameNamePadstackReplacementMode: TSameNamePadstackReplacementMode;
function GetState_SaveDefs: Boolean;
function GetState_SecondDimensionLine: Cardinal;
function GetState_ShadowsInPCB: Boolean;
function GetState_SheetAreaColor: Cardinal;
function GetState_SheetLineColor: Cardinal;
function GetState_ShowAllPrimitivesInHighlightedNets: Boolean;
function GetState_ShowComponentRefPoint: Boolean;
function GetState_ShowInvisibleObjects: Boolean;
function GetState_ShowPadNets: Boolean;
function GetState_ShowPadNumbers: Boolean;
function GetState_ShowStatusInfo: Boolean;
function GetState_ShowStatusInterval: Integer;
function GetState_ShowTestPoints: Boolean;
function GetState_ShowViaNets: Boolean;
function GetState_ShowViaSpan: Boolean;
function GetState_SingleLayerMode: Boolean;
function GetState_SnapToCentre: Boolean;
function GetState_TextToRectSize: Integer;
function GetState_TouchRectangleSelectionColor: Cardinal;
function GetState_UndoRedoStackSize: Integer;
function GetState_UseDithered: Boolean;
function GetState_UseNetColorForHighlight: Boolean;
function GetState_UseSmartTrackEnds: Boolean;
function GetState_UseTransparent: Boolean;
function GetState_ValidateOnLoad: Boolean;
function GetState_WaivedDRCErrorColor: Cardinal;
function GetState_WaivedViolationColor: Cardinal;
function GetState_WorkspaceColor1: Cardinal;
function GetState_WorkspaceColor2: Cardinal;
procedure Import_FromIniFile;
function LayerColorIterator: IPCB_LayerIterator;
procedure SetState_AmbiguityMenu(Value: Boolean);
procedure SetState_AmbiguityThreshold(Value: Integer);
procedure SetState_AreaRectangleSelectionColor(Value: Cardinal);
procedure SetState_AutoPan(Value: Boolean);
procedure SetState_AutoPanLargeStep(Value: Integer);
procedure SetState_AutoPanMode(Value: TAutoPanMode);
procedure SetState_AutoPanSmallStep(Value: Integer);
procedure SetState_AutoPanSpeed(Value: Integer);
procedure SetState_AutoPanUnit(Value: TAutoPanUnit);
procedure SetState_AutoVia(Value: Boolean);
procedure SetState_BackgroundMaskLevel(Value: Integer);
procedure SetState_BoardAreaColor(Value: Cardinal);
procedure SetState_BoardCursorType(Value: TGraphicsCursor);
procedure SetState_BoardLineColor(Value: Cardinal);
procedure SetState_CheckComments(Value: Boolean);
procedure SetState_CheckPatterns(Value: Boolean);
procedure SetState_CleanRedraw(Value: Boolean);
procedure SetState_ClickClearsSelection(Value: Boolean);
procedure SetState_Com1Parameters(const Value: IDispatch);
procedure SetState_Com2Parameters(const Value: IDispatch);
procedure SetState_Com3Parameters(const Value: IDispatch);
procedure SetState_Com4Parameters(const Value: IDispatch);
procedure SetState_ComponentLockPrimitives(Value: Boolean);
procedure SetState_ComponentMoveKind(Value: TComponentMoveKind);
procedure SetState_ComponentRefPointColor(Value: Cardinal);
procedure SetState_ConfirmSelectionMemoryClear(Value: Boolean);
procedure SetState_DefaultPrimsPermanent(Value: Boolean);
procedure SetState_DefaultTTFont(Value: WideString);
procedure SetState_DeleteDeadEnds(Value: Boolean);
procedure SetState_DeleteUnconnectedComps(Value: Boolean);
procedure SetState_DeleteUnconnectedPrims(Value: Boolean);
procedure SetState_DisplaySpecialStrings(Value: Boolean);
procedure SetState_DoOnlineDRC(Value: Boolean);
procedure SetState_DoubleClickRunsInspector(Value: Boolean);
procedure SetState_DraftTrackThreshold(Value: Integer);
procedure SetState_DragMode(Value: TPcbDragMode);
procedure SetState_DragVertexAction(Value: TVertexAction);
procedure SetState_DrawMode(OId: TObjectId; Value: TDrawMode);
procedure SetState_DuplicateDesignatorsAllowed(Value: Boolean);
procedure SetState_FilteredObjectsBlend(Value: Integer);
procedure SetState_FirstDimensionLine(Value: Cardinal);
procedure SetState_FractionalDigits(aUnit: TUnit; const aDigits: Integer);
procedure SetState_FromTosDisplayMode(Value: TFromToDisplayMode);
procedure SetState_GlobalEditIncludeArcsWithTracks(Value: Boolean);
procedure SetState_HighlightColor(Value: Cardinal);
procedure SetState_HighlightFull(Value: Boolean);
procedure SetState_HighlightObjectsBlend(Value: Integer);
procedure SetState_HoldShiftToSelectObjectId(OId: TObjectId; Value: Boolean);
procedure SetState_HuggingStyle(Value: THuggingStyle);
procedure SetState_InteractiveRouteMode(Value: TInteractiveRouteMode);
procedure SetState_LayerColors(L: TV6_Layer; Value: Cardinal);
procedure SetState_LayerColors_V7(L: Integer; Value: Cardinal);
procedure SetState_LayerDrawingOrder(I: Integer; Value: Integer);
procedure SetState_LayerDrawingOrderCount(I: Integer);
procedure SetState_LayerNameDisplayMode(Value: TLayerNameDisplayMode);
procedure SetState_LockPreRoutes(Value: Boolean);
procedure SetState_LoopRemoval(Value: Boolean);
procedure SetState_MinimumArcSize(Value: Double);
procedure SetState_MinPadViaObjectSizeInPixels(Value: Integer);
procedure SetState_MiterSize(Value: Double);
procedure SetState_MustHoldShiftToSelect(Value: Boolean);
procedure SetState_NearestComponent(Value: Boolean);
procedure SetState_NetlistReportDialog(Value: Boolean);
procedure SetState_NetlistReportFile(Value: Boolean);
procedure SetState_OnlySelectVisible(Value: Boolean);
procedure SetState_OriginMarkerColor(Value: Cardinal);
procedure SetState_PadEntryStability(Value: Integer);
procedure SetState_PadstackUpdateFromGlobalsOnLoad(Value: TSameNamePadstackReplacementMode);
procedure SetState_PadTypesDisplayMode(Value: TFromToDisplayMode);
procedure SetState_PadViaFontBkColor(Value: Cardinal);
procedure SetState_PadViaFontColor(Value: Cardinal);
procedure SetState_PadViaFontName(Value: WideString);
procedure SetState_PadViaFontStyle(Value: TFontStyles);
procedure SetState_PadViaMinFontSize(Value: Integer);
procedure SetState_Paste_HasSameDesignator(Value: Boolean);
procedure SetState_Paste_InSameClass(Value: Boolean);
procedure SetState_Paste_InSameNet(Value: Boolean);
procedure SetState_Paste_OnSameLayer(Value: Boolean);
procedure SetState_PlaceShoveDepth(Value: Integer);
procedure SetState_PlaneDrawMode(Value: TPlaneDrawMode);
procedure SetState_PlowThroughPolygons(Value: Boolean);
procedure SetState_PolygonRepour(Value: TPolygonRepourMode);
procedure SetState_PolygonThreshold(Value: Integer);
procedure SetState_ProtectLockedPrimitives(Value: Boolean);
procedure SetState_QuestionDelete(Value: Boolean);
procedure SetState_QuestionDrag(Value: Boolean);
procedure SetState_QuestionGlobalChange(Value: Boolean);
procedure SetState_RedrawLayerOnToggle(Value: Boolean);
procedure SetState_RemoveDuplicatesOnOutput(Value: Boolean);
procedure SetState_RepeatCircular(Value: Boolean);
procedure SetState_RepeatCountDefault(Value: Integer);
procedure SetState_RepeatDegrees(Value: Double);
procedure SetState_RepeatInc(Value: WideString);
procedure SetState_RepeatRotateItem(Value: Boolean);
procedure SetState_RepeatX(Value: Double);
procedure SetState_RepeatXUnit(Value: TUnit);
procedure SetState_RepeatY(Value: Double);
procedure SetState_RepeatYUnit(Value: TUnit);
procedure SetState_ReportsCSV(Value: Boolean);
procedure SetState_RotationStep(Value: Double);
procedure SetState_RouteGuideColor(Value: Cardinal);
procedure SetState_SameNamePadstackReplacementMode(Value: TSameNamePadstackReplacementMode);
procedure SetState_SaveDefs(Value: Boolean);
procedure SetState_SecondDimensionLine(Value: Cardinal);
procedure SetState_ShadowsInPCB(Value: Boolean);
procedure SetState_SheetAreaColor(Value: Cardinal);
procedure SetState_SheetLineColor(Value: Cardinal);
procedure SetState_ShowAllPrimitivesInHighlightedNets(Value: Boolean);
procedure SetState_ShowComponentRefPoint(Value: Boolean);
procedure SetState_ShowInvisibleObjects(Value: Boolean);
procedure SetState_ShowPadNets(Value: Boolean);
procedure SetState_ShowPadNumbers(Value: Boolean);
procedure SetState_ShowStatusInfo(Value: Boolean);
procedure SetState_ShowStatusInterval(Value: Integer);
procedure SetState_ShowTestPoints(Value: Boolean);
procedure SetState_ShowViaNets(Value: Boolean);
procedure SetState_ShowViaSpan(Value: Boolean);
procedure SetState_SingleLayerMode(Value: Boolean);
procedure SetState_SnapToCentre(Value: Boolean);
procedure SetState_TextToRectSize(Value: Integer);
procedure SetState_TouchRectangleSelectionColor(Value: Cardinal);
procedure SetState_UndoRedoStackSize(Value: Integer);
procedure SetState_UseDithered(Value: Boolean);
procedure SetState_UseNetColorForHighlight(Value: Boolean);
procedure SetState_UseSmartTrackEnds(Value: Boolean);
procedure SetState_UseTransparent(Value: Boolean);
procedure SetState_ValidateOnLoad(Value: Boolean);
procedure SetState_WaivedDRCErrorColor(Value: Cardinal);
procedure SetState_WaivedViolationColor(Value: Cardinal);
procedure SetState_WorkspaceColor1(Value: Cardinal);
procedure SetState_WorkspaceColor2(Value: Cardinal);

## IPCB_TTFontData
继承：IPCB_TTFontData → IInterface ｜ 单元：RT_PCB ｜ 自有 17 个方法、9 个属性

property Bold: Boolean read GetState_Bold;  // read-only
property CanEmbed: Boolean read GetState_CanEmbed;  // read-only
property CharSet: Byte read GetState_CharSet;  // read-only
property EmbeddedFontHandle: THandle read GetState_EmbeddedFontHandle;  // read-only
property FontFaceName: TPCBString read GetState_FontFaceName;  // read-only
property FontFullName: TPCBString read GetState_FontFullName;  // read-only
property FontStyleName: TPCBString read GetState_FontStyleName;  // read-only
property Italic: Boolean read GetState_Italic;  // read-only
property RefCount: Integer read GetState_RefCount;  // read-only
function AddRef: Integer;
function FontExists: Boolean;
function GetEmbeddedFontData(var DataSize: Integer): PByte;
function GetState_Bold: Boolean;
function GetState_CanEmbed: Boolean;
function GetState_CharSet: Byte;
function GetState_EmbeddedFontHandle: NativeUInt;
function GetState_FontFaceName: WideString;
function GetState_FontFullName: WideString;
function GetState_FontStyleName: WideString;
function GetState_Italic: Boolean;
function GetState_RefCount: Integer;
function I_ObjectAddress: Pointer;
function IsEmbedded: Boolean;
function IsEmbeddedInDocument(const ABoard: Pointer): Boolean;
function IsSame(const FaceName: WideString; const Bold: Boolean; const Italic: Boolean; const CharSet: Byte): Boolean;
function Release: Integer;

## IPCB_TTFontsCache
继承：IPCB_TTFontsCache → IInterface ｜ 单元：RT_PCB ｜ 自有 9 个方法、3 个属性

property EmbeddedFontsCount[ABoard: Pointer]: Integer read GetState_EmbeddedFontsCount;  // read-only
property Font[I: Integer]: IPCB_TTFontData read GetState_Font;  // read-only
property FontsCount: Integer read GetState_FontsCount;  // read-only
procedure AddEmbeddedFont(const FullFontName: WideString; const FaceName: WideString; const StyleName: WideString; const Bold: Boolean; const Italic: Boolean; const CharSet: Byte; FontData: Pointer; DataLen: Integer; const ABoard: Pointer);
procedure AddFont(const FaceName: WideString; const Bold: Boolean; const Italic: Boolean; const CharSet: Byte; const ABoard: Pointer);
function ExportFontsToList(const ABoard: Pointer; const AFontsList: IPCB_WideStrings): Integer;
function GetFont(const FaceName: WideString; const Bold: Boolean; const Italic: Boolean; const CharSet: Byte; const ABoard: Pointer): IPCB_TTFontData;
function GetNextEmbeddedFont(var APos: Integer; const ABoard: Pointer): IPCB_TTFontData;
function GetState_EmbeddedFontsCount(ABoard: Pointer): Integer;
function GetState_Font(I: Integer): IPCB_TTFontData;
function GetState_FontsCount: Integer;
function I_ObjectAddress: Pointer;

## IPCB_TestPointStyleRule
继承：IPCB_TestPointStyleRule → IPCB_Rule → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 34 个方法、15 个属性

property AllowedSide: TTestpointAllowedSideSet read GetState_AllowedSide write SetState_AllowedSide;
property BoardEdgeClearance: TCoord read GetState_BoardEdgeClearance write SetState_BoardEdgeClearance;
property CompBodyClearance: TCoord read GetState_CompBodyClearance write SetState_CompBodyClearance;
property GridOrigin: TCoordPoint read GetState_GridOrigin write SetState_GridOrigin;
property GridTolerance: TCoord read GetState_GridTolerance write SetState_GridTolerance;
property MaxHoleSize: TCoord read GetState_MaxHoleSize write SetState_MaxHoleSize;
property MaxSize: TCoord read GetState_MaxSize write SetState_MaxSize;
property MinHoleSize: TCoord read GetState_MinHoleSize write SetState_MinHoleSize;
property MinSize: TCoord read GetState_MinSize write SetState_MinSize;
property MinSpacing: TCoord read GetState_MinSpacing write SetState_MinSpacing;
property PreferedHoleSize: TCoord read GetState_PreferedHoleSize write SetState_PreferedHoleSize;
property PreferedSize: TCoord read GetState_PreferedSize write SetState_PreferedSize;
property TestpointGrid: TCoord read GetState_TestpointGrid write SetState_TestpointGrid;
property TestpointUnderComponent: Boolean read GetState_TestpointUnderComponent write SetState_TestpointUnderComponent;
property UseGrid: Boolean read GetState_UseGrid write SetState_UseGrid;
function GetState_AllowedSide: TTestpointAllowedSideSet;
function GetState_BoardEdgeClearance: Integer;
function GetState_CompBodyClearance: Integer;
function GetState_DistanceToPadHoleCenter: Integer;
function GetState_DistanceToViaHoleCenter: Integer;
function GetState_GridOrigin: IDispatch;
function GetState_GridTolerance: Integer;
function GetState_MaxHoleSize: Integer;
function GetState_MaxSize: Integer;
function GetState_MinHoleSize: Integer;
function GetState_MinSize: Integer;
function GetState_MinSpacing: Integer;
function GetState_PreferedHoleSize: Integer;
function GetState_PreferedSize: Integer;
function GetState_TestpointGrid: Integer;
function GetState_TestpointUnderComponent: Boolean;
function GetState_UseGrid: Boolean;
procedure SetState_AllowedSide(Value: TTestpointAllowedSideSet);
procedure SetState_BoardEdgeClearance(Value: Integer);
procedure SetState_CompBodyClearance(Value: Integer);
procedure SetState_DistanceToPadHoleCenter(Value: Integer);
procedure SetState_DistanceToViaHoleCenter(Value: Integer);
procedure SetState_GridOrigin(const Value: IDispatch);
procedure SetState_GridTolerance(Value: Integer);
procedure SetState_MaxHoleSize(Value: Integer);
procedure SetState_MaxSize(Value: Integer);
procedure SetState_MinHoleSize(Value: Integer);
procedure SetState_MinSize(Value: Integer);
procedure SetState_MinSpacing(Value: Integer);
procedure SetState_PreferedHoleSize(Value: Integer);
procedure SetState_PreferedSize(Value: Integer);
procedure SetState_TestpointGrid(Value: Integer);
procedure SetState_TestpointUnderComponent(Value: Boolean);
procedure SetState_UseGrid(Value: Boolean);

## IPCB_TestPointUsage
继承：IPCB_TestPointUsage → IPCB_Rule → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 4 个方法、2 个属性

property AllowMultipleOnNet: Boolean read GetState_AllowMultipleOnNet write SetState_AllowMultipleOnNet;
property Valid: TTestpointValid read GetState_Valid write SetState_Valid;
function GetState_AllowMultipleOnNet: Boolean;
function GetState_Valid: TTestpointValid;
procedure SetState_AllowMultipleOnNet(Value: Boolean);
procedure SetState_Valid(Value: TTestpointValid);

## IPCB_Text
继承：IPCB_Text → IPCB_RectangularPrimitive → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 89 个方法、43 个属性

property BarCodeBitPattern: TPCBString read GetState_BarCodeBitPattern;  // read-only
property BarCodeFontName: TPCBString read GetState_BarCodeFontName write SetState_BarCodeFontName;
property BarCodeFullHeight: TCoord read GetState_BarCodeFullHeight write SetState_BarCodeFullHeight;
property BarCodeFullWidth: TCoord read GetState_BarCodeFullWidth write SetState_BarCodeFullWidth;
property BarCodeInverted: Boolean read GetState_BarCodeInverted write SetState_BarCodeInverted;
property BarCodeKind: TBarcodeKind read GetState_BarCodeKind write SetState_BarCodeKind;
property BarCodeMinWidth: TCoord read GetState_BarCodeMinWidth write SetState_BarCodeMinWidth;
property BarCodeRenderMode: TBarcodeRenderMode read GetState_BarCodeRenderMode write SetState_BarCodeRenderMode;
property BarCodeShowText: Boolean read GetState_BarCodeShowText write SetState_BarCodeShowText;
property BarCodeXMargin: TCoord read GetState_BarCodeXMargin write SetState_BarCodeXMargin;
property BarCodeYMargin: TCoord read GetState_BarCodeYMargin write SetState_BarCodeYMargin;
property Bold: Boolean read GetState_Bold write SetState_Bold;
property BorderSpaceType: TTextBorderSpaceType read GetState_BorderSpaceType write SetState_BorderSpaceType;
property CharSet: Byte read GetState_CharSet write SetState_CharSet;
property ConvertedString: TPCBString read GetState_ConvertedString;  // read-only
property DisableSpecialStringConversion: Boolean read GetState_DisableSpecialStringConversion write SetState_DisableSpecialStringConversion;
property FontID: TFontID read GetState_FontID write SetState_FontID;
property FontName: TPCBString read GetState_FontName write SetState_FontName;
property Inverted: Boolean read GetState_Inverted write SetState_Inverted;
property InvertedTTTextBorder: TCoord read GetState_InvertedTTTextBorder write SetState_InvertedTTTextBorder;
property InvRectHeight: Integer read GetState_InvRectHeight write SetState_InvRectHeight;
property InvRectWidth: Integer read GetState_InvRectWidth write SetState_InvRectWidth;
property Italic: Boolean read GetState_Italic write SetState_Italic;
property MirrorFlag: Boolean read GetState_Mirror write SetState_Mirror;
property Multiline: Boolean read GetState_Multiline write SetState_Multiline;
property MultilineTextAutoPosition: TTextAutoposition read GetState_MultilineTextAutoPosition write SetState_MultilineTextAutoPosition;
property MultilineTextHeight: TCoord read GetState_MultilineTextHeight write SetState_MultilineTextHeight;
property MultilineTextResizeEnabled: Boolean read GetState_MultilineTextResizeEnabled;  // read-only
property MultilineTextWidth: TCoord read GetState_MultilineTextWidth write SetState_MultilineTextWidth;
property Size: TCoord read GetState_Size write SetState_Size;
property Text: TPCBString read GetState_Text write SetState_Text;
property TextKind: TTextKind read GetState_TextKind write SetState_TextKind;
property TTFInvertedTextJustify: TTextAutoposition read GetState_TTFInvertedTextJustify write SetState_TTFInvertedTextJustify;
property TTFOffsetFromInvertedRect: TCoord read GetState_TTFOffsetFromInvertedRect write SetState_TTFOffsetFromInvertedRect;
property TTFTextHeight: Integer read GetState_TTFTextHeight write SetState_TTFTextHeight;
property TTFTextWidth: Integer read GetState_TTFTextWidth write SetState_TTFTextWidth;
property TTTextOutline: Pointer read GetTrueTypeTextOutline;  // read-only
property TTTextOutlineGeometricPolygon: IPCB_GeometricPolygon read GetTrueTypeTextOutlineGeometricPolygon;  // read-only
property UnderlyingString: TPCBString read GetState_UnderlyingString write SetState_UnderlyingString;
property UseInvertedRectangle: Boolean read GetState_UseInvertedRectangle write SetState_UseInvertedRectangle;
property UseTTFonts: Boolean read GetState_UseTTFonts write SetState_UseTTFonts;
property Width: TCoord read GetState_Width write SetState_Width;
property WordWrap: Boolean read GetState_WordWrap;  // read-only
procedure BeginOutputGeneration(AConverter: IPCB_OutputConverter; AList: IInterfaceList);
function CanEditMultilineRectSize: Boolean;
procedure EndOutputGeneration;
function GetDesignatorDisplayString: WideString;
function GetState_BarCodeBitPattern: WideString;
function GetState_BarCodeFontName: WideString;
function GetState_BarCodeFullHeight: Integer;
function GetState_BarCodeFullWidth: Integer;
function GetState_BarCodeInverted: Boolean;
function GetState_BarCodeKind: TBarcodeKind;
function GetState_BarCodeMinWidth: Integer;
function GetState_BarCodeRenderMode: TBarcodeRenderMode;
function GetState_BarCodeShowText: Boolean;
function GetState_BarCodeXMargin: Integer;
function GetState_BarCodeYMargin: Integer;
function GetState_Bold: Boolean;
function GetState_BorderSpaceType: TTextBorderSpaceType;
function GetState_CharSet: Byte;
function GetState_ConvertedString: WideString;
function GetState_DisableSpecialStringConversion: Boolean;
function GetState_FontID: SmallInt;
function GetState_FontName: WideString;
function GetState_Inverted: Boolean;
function GetState_InvertedTTTextBorder: Integer;
function GetState_InvRectHeight: Integer;
function GetState_InvRectWidth: Integer;
function GetState_Italic: Boolean;
function GetState_Mirror: Boolean;
function GetState_Multiline: Boolean;
function GetState_MultilineTextAutoPosition: TTextAutoposition;
function GetState_MultilineTextHeight: Integer;
function GetState_MultilineTextResizeEnabled: Boolean;
function GetState_MultilineTextWidth: Integer;
function GetState_Size: Integer;
function GetState_Text: WideString;
function GetState_TextKind: TTextKind;
function GetState_TTFInvertedTextJustify: TTextAutoposition;
function GetState_TTFOffsetFromInvertedRect: Integer;
function GetState_TTFTextHeight: Integer;
function GetState_TTFTextWidth: Integer;
function GetState_UnderlyingString: WideString;
function GetState_UseInvertedRectangle: Boolean;
function GetState_UseTTFonts: Boolean;
function GetState_Width: Integer;
function GetState_WordWrap: Boolean;
function GetTrueTypeTextOutline: Pointer;
function GetTrueTypeTextOutlineGeometricPolygon: IPCB_GeometricPolygon;
function InAutoDimension: Boolean;
function IsComment: Boolean;
function IsDesignator: Boolean;
function IsHidden: Boolean;
function RotationHandle: IDispatch;
procedure SetState_BarCodeFontName(const Value: WideString);
procedure SetState_BarCodeFullHeight(const Value: Integer);
procedure SetState_BarCodeFullWidth(const Value: Integer);
procedure SetState_BarCodeInverted(const Value: Boolean);
procedure SetState_BarCodeKind(const Value: TBarcodeKind);
procedure SetState_BarCodeMinWidth(const Value: Integer);
procedure SetState_BarCodeRenderMode(const Value: TBarcodeRenderMode);
procedure SetState_BarCodeShowText(const Value: Boolean);
procedure SetState_BarCodeXMargin(const Value: Integer);
procedure SetState_BarCodeYMargin(const Value: Integer);
procedure SetState_Bold(Bold: Boolean);
procedure SetState_BorderSpaceType(Value: TTextBorderSpaceType);
procedure SetState_CharSet(CharSet: Byte);
procedure SetState_DisableSpecialStringConversion(AValue: Boolean);
procedure SetState_FontID(FontID: SmallInt);
procedure SetState_FontName(FontName: WideString);
procedure SetState_Inverted(Inverted: Boolean);
procedure SetState_InvertedTTTextBorder(Border: Integer);
procedure SetState_InvRectHeight(Value: Integer);
procedure SetState_InvRectWidth(Value: Integer);
procedure SetState_Italic(Italic: Boolean);
procedure SetState_Mirror(Mirror: Boolean);
procedure SetState_Multiline(Value: Boolean);
procedure SetState_MultilineTextAutoPosition(AutoPosition: TTextAutoposition);
procedure SetState_MultilineTextHeight(Height: Integer);
procedure SetState_MultilineTextWidth(Width: Integer);
procedure SetState_Size(Size: Integer);
procedure SetState_Text(Text: WideString);
procedure SetState_TextKind(const Value: TTextKind);
procedure SetState_TTFInvertedTextJustify(Value: TTextAutoposition);
procedure SetState_TTFOffsetFromInvertedRect(Value: Integer);
procedure SetState_TTFTextHeight(Value: Integer);
procedure SetState_TTFTextWidth(Value: Integer);
procedure SetState_UnderlyingString(Value: WideString);
procedure SetState_UseInvertedRectangle(Value: Boolean);
procedure SetState_UseTTFonts(UseTTFonts: Boolean);
procedure SetState_Width(Width: Integer);

## IPCB_Text3
继承：IPCB_Text3 → IPCB_Text → IPCB_RectangularPrimitive → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 13 个方法、3 个属性

property AdvanceSnapping: Boolean read GetState_AdvanceSnapping write SetState_AdvanceSnapping;
property SnapPointX: TCoord read GetState_SnapPointX write SetState_SnapPointX;
property SnapPointY: TCoord read GetState_SnapPointY write SetState_SnapPointY;
procedure CopyTo(const P: IPCB_Text; CopyMode: TCopyMode);
function GetActualTextBr: IDispatch;
function GetState_AdvanceSnapping: Boolean;
function GetState_SnapPointX: Integer;
function GetState_SnapPointY: Integer;
procedure PushJustificationCenter(APushState: Boolean);
procedure RepositionAfterPush;
procedure SetState_AdvanceSnapping(const Value: Boolean);
procedure SetState_SnapPointX(const Value: Integer);
procedure SetState_SnapPointY(const Value: Integer);
function StringXPosition: Integer;
function StringYPosition: Integer;
procedure UpdateTextPosition;

## IPCB_Texture
继承：IPCB_Texture → IInterface ｜ 单元：RT_PCB ｜ 自有 0 个方法、0 个属性


## IPCB_TraceImpedance
继承：IPCB_TraceImpedance → IInterface ｜ 单元：RT_PCB ｜ 自有 42 个方法、19 个属性

property CalculatedImpedance: TDouble read GetState_CalculatedImpedance write SetState_CalculatedImpedance;
property ClearanceToPlane: TCoord read GetState_ClearanceToPlane write SetState_ClearanceToPlane;
property DiffPairGap: TCoord read GetState_DiffPairGap write SetState_DiffPairGap;
property EtchFactor: TDouble read GetState_EtchFactor write SetState_EtchFactor;
property ImpedanceError: TDouble read GetState_ImpedanceError write SetState_ImpedanceError;
property ImpedanceProfile: IPCB_ImpedanceProfile read GetState_ImpedanceProfile;  // read-only
property IsEnabled: Boolean read GetState_IsEnabled write SetState_IsEnabled;
property IsTraceGapLocked: Boolean read GetState_IsTraceGapLocked write SetState_IsTraceGapLocked;
property IsTraceWidthLocked: Boolean read GetState_IsTraceWidthLocked write SetState_IsTraceWidthLocked;
property Layer: TLayer read GetState_Layer;  // read-only
property PropagationSpeed: TDouble read GetState_PropagationSpeed write SetState_PropagationSpeed;
property RefBottomLayer: TLayer read GetState_RefBottomLayer write SetState_RefBottomLayer;
property RefTopLayer: TLayer read GetState_RefTopLayer write SetState_RefTopLayer;
property SolderMaskThicknessBetweenTraces: TCoord read GetState_SolderMaskThicknessBetweenTraces write SetState_SolderMaskThicknessBetweenTraces;
property SolderMaskThicknessOnTopOfTraces: TCoord read GetState_SolderMaskThicknessOnTopOfTraces write SetState_SolderMaskThicknessOnTopOfTraces;
property Substack: IPCB_LayerStack read GetState_SubStack;  // read-only
property TraceMinWidth: TCoord read GetState_TraceMinWidth write SetState_TraceMaxWidth;
property TraceWidth: TCoord read GetState_TraceWidth write SetState_TraceWidth;
property UseSolderMask: Boolean read GetState_UseSolderMask write SetState_UseSolderMask;
function GetState_CalculatedImpedance: Double;
function GetState_ClearanceToPlane: Integer;
function GetState_DiffPairGap: Integer;
function GetState_DiffPairMaxGap: Integer;
function GetState_DiffPairMinGap: Integer;
function GetState_EtchFactor: Double;
function GetState_ImpedanceError: Double;
function GetState_ImpedanceProfile: IPCB_ImpedanceProfile;
function GetState_IsEnabled: Boolean;
function GetState_IsTraceGapLocked: Boolean;
function GetState_IsTraceWidthLocked: Boolean;
function GetState_Layer: Integer;
function GetState_PropagationSpeed: Double;
function GetState_RefBottomLayer: Integer;
function GetState_RefTopLayer: Integer;
function GetState_SolderMaskThicknessBetweenTraces: Integer;
function GetState_SolderMaskThicknessOnTopOfTraces: Integer;
function GetState_SubStack: IPCB_LayerStack;
function GetState_TraceMaxWidth: Integer;
function GetState_TraceMinWidth: Integer;
function GetState_TraceWidth: Integer;
function GetState_UseSolderMask: Boolean;
function I_ObjectAddress: Pointer;
procedure SetState_CalculatedImpedance(Value: Double);
procedure SetState_ClearanceToPlane(Value: Integer);
procedure SetState_DiffPairGap(Value: Integer);
procedure SetState_DiffPairMaxGap(Value: Integer);
procedure SetState_DiffPairMinGap(Value: Integer);
procedure SetState_EtchFactor(Value: Double);
procedure SetState_ImpedanceError(Value: Double);
procedure SetState_IsEnabled(Value: Boolean);
procedure SetState_IsTraceGapLocked(Value: Boolean);
procedure SetState_IsTraceWidthLocked(Value: Boolean);
procedure SetState_PropagationSpeed(Value: Double);
procedure SetState_RefBottomLayer(Value: Integer);
procedure SetState_RefTopLayer(Value: Integer);
procedure SetState_SolderMaskThicknessBetweenTraces(AValue: Integer);
procedure SetState_SolderMaskThicknessOnTopOfTraces(AValue: Integer);
procedure SetState_TraceMaxWidth(Value: Integer);
procedure SetState_TraceMinWidth(Value: Integer);
procedure SetState_TraceWidth(Value: Integer);
procedure SetState_UseSolderMask(AValue: Boolean);

## IPCB_Track
继承：IPCB_Track → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 12 个方法、5 个属性

property Width: TCoord read GetState_Width write SetState_Width;
property x1: TCoord read GetState_X1 write SetState_X1;
property x2: TCoord read GetState_X2 write SetState_X2;
property y1: TCoord read GetState_Y1 write SetState_Y1;
property y2: TCoord read GetState_Y2 write SetState_Y2;
function GetState_Length: Integer;
function GetState_Width: Integer;
function GetState_X1: Integer;
function GetState_X2: Integer;
function GetState_Y1: Integer;
function GetState_Y2: Integer;
procedure SetState_Length(Value: Integer);
procedure SetState_Width(Value: Integer);
procedure SetState_X1(Value: Integer);
procedure SetState_X2(Value: Integer);
procedure SetState_Y1(Value: Integer);
procedure SetState_Y2(Value: Integer);

## IPCB_Track3D
继承：IPCB_Track3D → IPCB_Track → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 22 个方法、7 个属性

property FaceIdx1: Integer read GetState_FaceIdx1 write SetState_FaceIdx1;
property FaceIdx2: Integer read GetState_FaceIdx2 write SetState_FaceIdx2;
property FaceU1: Integer read GetState_FaceU1 write SetState_FaceU1;
property FaceU2: Integer read GetState_FaceU2 write SetState_FaceU2;
property FaceV1: Integer read GetState_FaceV1 write SetState_FaceV1;
property FaceV2: Integer read GetState_FaceV2 write SetState_FaceV2;
property Path_Point[AIdx: Integer]: TCoordPoint read Path_GetPoint write Path_SetPoint;
function GetState_FaceIdx1: Integer;
function GetState_FaceIdx2: Integer;
function GetState_FaceU1: Integer;
function GetState_FaceU2: Integer;
function GetState_FaceV1: Integer;
function GetState_FaceV2: Integer;
procedure Path_AddPoint(const APt: IDispatch);
procedure Path_DeleteLast;
procedure Path_DeletePoint(AIdx: Integer);
function Path_First: IDispatch;
function Path_GetPoint(AIdx: Integer): IDispatch;
procedure Path_InsertPoint(AIdx: Integer; const APt: IDispatch);
function Path_Last: IDispatch;
function Path_PointsCount: Integer;
procedure Path_SetPoint(AIdx: Integer; const APt: IDispatch);
function Path_StateID: Integer;
procedure SetState_FaceIdx1(Value: Integer);
procedure SetState_FaceIdx2(Value: Integer);
procedure SetState_FaceU1(Value: Integer);
procedure SetState_FaceU2(Value: Integer);
procedure SetState_FaceV1(Value: Integer);
procedure SetState_FaceV2(Value: Integer);

## IPCB_UnConnectedPinRule
继承：IPCB_UnConnectedPinRule → IPCB_Rule → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 0 个方法、0 个属性


## IPCB_Union
继承：IPCB_Union → IInterface ｜ 单元：RT_PCB ｜ 自有 3 个方法、0 个属性

function GetState_Name: WideString;
function GetState_Type: TUnionTypeID;
function GetState_UnionIndex: Integer;

## IPCB_Via
继承：IPCB_Via → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 44 个方法、22 个属性

property Cache: TPadCache read GetState_Cache write SetState_Cache;
property CounterHoleParams: IPCB_CounterHoleParams read GetCounterHole_Params;  // read-only
property DrillLayerPairType: TDrillLayerPairType read GetState_DrillLayerPairType write SetState_DrillLayerPairType;
property Height: TCoord read GetState_Height;  // read-only
property HighLayer: TLayer read GetState_HighLayer write SetState_HighLayer;
property HoleNegativeTolerance: TCoord read GetState_HoleNegativeTolerance write SetState_HoleNegativeTolerance;
property HolePositiveTolerance: TCoord read GetState_HolePositiveTolerance write SetState_HolePositiveTolerance;
property HoleSize: TCoord read GetState_HoleSize write SetState_HoleSize;
property IsConnectedToPlane[Layer: TV6_Layer]: Boolean read GetState_IsConnectedToPlane write SetState_IsConnectedToPlane;
property LowLayer: TLayer read GetState_LowLayer write SetState_LowLayer;
property Mode: TPadMode read GetState_Mode write SetState_Mode;
property Plated: Boolean read GetProperty_Plated;  // read-only
property ShapeOnLayer[Layer: Integer]: TShape read GetState_ShapeOnLayer;  // read-only
property Size: TCoord read GetState_Size write SetState_Size;
property SizeOnLayer[Layer: Integer]: TCoord read GetState_SizeOnLayer write SetState_SizeOnLayer;
property SolderMaskExpansionFromHoleEdge: Boolean read GetState_SolderMaskExpansionFromHoleEdge write SetState_SolderMaskExpansionFromHoleEdge;
property StackSizeOnLayer[Layer: Integer]: TCoord read GetState_StackSizeOnLayer write SetState_StackSizeOnLayer;
property StartLayer: IPCB_LayerObject read GetState_StartLayer;  // read-only
property StopLayer: IPCB_LayerObject read GetState_StopLayer;  // read-only
property TemplateLink: IPCB_PadViaTemplateLink read GetState_TemplateLink;  // read-only
property x: TCoord read GetState_XLocation write SetState_XLocation;
property y: TCoord read GetState_YLocation write SetState_YLocation;
procedure ClearStackSizes;
function DefinitionLayerIterator: IPCB_LayerIterator;
function GetCounterHole_Params: IPCB_CounterHoleParams;
function GetProperty_Plated: Boolean;
function GetState_Cache: IDispatch;
function GetState_DrillLayerPairType: TDrillLayerPairType;
function GetState_Height: Integer;
function GetState_HighLayer: Integer;
function GetState_HoleNegativeTolerance: Integer;
function GetState_HolePositiveTolerance: Integer;
function GetState_HoleSize: Integer;
function GetState_IsBackdrill: Boolean;
function GetState_IsConnectedToPlane(Layer: TV6_Layer): Boolean;
function GetState_LowLayer: Integer;
function GetState_Mode: TPadMode;
function GetState_ShapeOnLayer(Layer: Integer): TShape;
function GetState_Size: Integer;
function GetState_SizeOnLayer(Layer: Integer): Integer;
function GetState_SolderMaskExpansionFromHoleEdge: Boolean;
function GetState_StackSizeOnLayer(Layer: Integer): Integer;
function GetState_StartLayer: IPCB_LayerObject;
function GetState_StopLayer: IPCB_LayerObject;
function GetState_TemplateLink: IPCB_PadViaTemplateLink;
function GetState_XLocation: Integer;
function GetState_YLocation: Integer;
function IntersectLayer(ALayer: Integer): Boolean;
function IsCounterHole: Boolean;
function PlaneConnectionStyleForLayer(ALayer: TV6_Layer): TPlaneConnectionStyle;
procedure RotateAroundXY(AX: Integer; AY: Integer; Angle: Double);
procedure SetState_Cache(const Value: IDispatch);
procedure SetState_DrillLayerPairType(AValue: TDrillLayerPairType);
procedure SetState_HighLayer(L: Integer);
procedure SetState_HoleNegativeTolerance(Value: Integer);
procedure SetState_HolePositiveTolerance(Value: Integer);
procedure SetState_HoleSize(Value: Integer);
procedure SetState_IsConnectedToPlane(Layer: TV6_Layer; Value: Boolean);
procedure SetState_LowLayer(L: Integer);
procedure SetState_Mode(Mode: TPadMode);
procedure SetState_Size(Size: Integer);
procedure SetState_SizeOnLayer(Layer: Integer; Size: Integer);
procedure SetState_SolderMaskExpansionFromHoleEdge(AValue: Boolean);
procedure SetState_StackSizeOnLayer(Layer: Integer; Size: Integer);
procedure SetState_XLocation(AX: Integer);
procedure SetState_YLocation(AY: Integer);

## IPCB_ViaCombinationManagerInterface
继承：IPCB_ViaCombinationManagerInterface → IInterface ｜ 单元：RT_PCB ｜ 自有 6 个方法、3 个属性

property CurrentStack: IPCB_RoutingViaStackInfo read GetState_CurrentStack write SetState_CurrentStack;
property ViaStackCount: Integer read GetState_ViaStackCount;  // read-only
property ViaStacks[AIndex: Integer]: IPCB_RoutingViaStackInfo read GetState_ViaStack;  // read-only
function GetState_CurrentStack: IPCB_RoutingViaStackInfo;
function GetState_ViaStack(AIndex: Integer): IPCB_RoutingViaStackInfo;
function GetState_ViaStackCount: Integer;
procedure NextStack;
procedure PrevStack;
procedure SetState_CurrentStack(const AStack: IPCB_RoutingViaStackInfo);

## IPCB_ViaDraggingProcess
继承：IPCB_ViaDraggingProcess → IPCB_InteractiveProcess → IInteractiveProcess ｜ 单元：RT_PCB ｜ 自有 1 个方法、0 个属性

function GetRoutingOptions: IPCB_RoutingOptionsPage;

## IPCB_ViaManager
继承：IPCB_ViaManager → IInterface ｜ 单元：RT_PCB ｜ 自有 3 个方法、0 个属性

function GetViaType(const AViaPrim: IPCB_Primitive): TViaType;
function IsMicroVia(const AViaPrim: IPCB_Primitive): Boolean;
function IsPartOfStackedVia(const AViaPrim: IPCB_Primitive): Boolean;

## IPCB_ViaRoutingDataInfo
继承：IPCB_ViaRoutingDataInfo → IInterface ｜ 单元：RT_PCB ｜ 自有 15 个方法、11 个属性

property DrillLayerPair: IPCB_DrillLayerPair read GetState_DrillLayerPair;  // read-only
property HighLayer: TLayer read GetState_HighLayer;  // read-only
property HoleSize: TCoord read GetState_HoleSize write SetState_HoleSize;
property LayerStack: IPCB_LayerStack read GetState_LayerStack;  // read-only
property LowLayer: TLayer read GetState_LowLayer;  // read-only
property PairType: TDrillLayerPairType read GetState_PairType;  // read-only
property Rule: IPCB_RoutingViaStyleRule read GetState_Rule;  // read-only
property Template: IPCB_PadViaTemplate read GetState_Template write SetState_Template;
property Title: WideString read GetState_Title;  // read-only
property ViaSize: TCoord read GetState_ViaSize write SetState_ViaSize;
property ViaType: TViaType read GetState_ViaType;  // read-only
function GetState_DrillLayerPair: IPCB_DrillLayerPair;
function GetState_HighLayer: Integer;
function GetState_HoleSize: Integer;
function GetState_LayerStack: IPCB_LayerStack;
function GetState_LowLayer: Integer;
function GetState_PairType: TDrillLayerPairType;
function GetState_Rule: IPCB_RoutingViaStyleRule;
function GetState_Template: IPCB_PadViaTemplate;
function GetState_Title: WideString;
function GetState_ViaSize: Integer;
function GetState_ViaSizeOnLayer(ALayer: Integer): Integer;
function GetState_ViaType: TViaType;
procedure SetState_HoleSize(AValue: Integer);
procedure SetState_Template(AValue: IPCB_PadViaTemplate);
procedure SetState_ViaSize(AValue: Integer);

## IPCB_ViaShieldingOptions
继承：IPCB_ViaShieldingOptions → IInterface ｜ 单元：RT_PCB ｜ 自有 43 个方法、18 个属性

property AddCopper: Boolean read GetState_AddCopper write SetState_AddCopper;
property AddPolyCutout: Boolean read GetState_AddPolyCutout write SetState_AddPolyCutout;
property Board: IPCB_Board read GetState_Board write SetState_Board;
property Distance: TCoord read GetState_Distance write SetState_Distance;
property MultipleObjects: Boolean read GetState_MultipleObjects write SetState_MultipleObjects;
property Net: IPCB_Net read GetState_Net write SetState_Net;
property NetName: TDynamicString read GetState_NetName write SetState_NetName;
property ObjectCount: Integer read GetState_ObjectCount;  // read-only
property Objects[AIndex: Integer]: IPCB_Primitive read GetState_Objects;  // read-only
property Pullback: TCoord read GetState_Pullback write SetState_Pullback;
property RowCount: Integer read GetState_RowCount write SetState_RowCount;
property RowStep: TCoord read GetState_RowStep write SetState_RowStep;
property Stagger: Boolean read GetState_Stagger write SetState_Stagger;
property Step: TCoord read GetState_Step write SetState_Step;
property TemplateVia: IPCB_Via read GetState_TemplateVia write SetState_TemplateVia;
property ViaNet: IPCB_Net read GetState_ViaNet write SetState_ViaNet;
property ViaNetName: TDynamicString read GetState_ViaNetName write SetState_ViaNetName;
property ViaPadClearance: TCoord read GetState_ViaPadClearance write SetState_ViaPadClearance;
procedure AddObject(APrimitive: IPCB_Primitive);
procedure Export_ToOptionsWriter;
procedure Export_ToParameters(const AParameters: IParameterList);
procedure Export_ToParameters_SelectedObjects(const AParameters: IParameterList);
function GetState_AddCopper: Boolean;
function GetState_AddPolyCutout: Boolean;
function GetState_Board: IPCB_Board;
function GetState_Distance: Integer;
function GetState_MultipleObjects: Boolean;
function GetState_Net: IPCB_Net;
function GetState_NetName: string;
function GetState_ObjectCount: Integer;
function GetState_Objects(AIndex: Integer): IPCB_Primitive;
function GetState_Pullback: Integer;
function GetState_RowCount: Integer;
function GetState_RowStep: Integer;
function GetState_Stagger: Boolean;
function GetState_Step: Integer;
function GetState_TemplateVia: IPCB_Via;
function GetState_ViaNet: IPCB_Net;
function GetState_ViaNetName: string;
function GetState_ViaPadClearance: Integer;
function I_ObjectAddress: Pointer;
procedure Import_FromOptionsReader;
procedure Import_FromParameters(const AParameters: IParameterList);
function Replicate: IPCB_ViaShieldingOptions;
procedure SetState_AddCopper(AValue: Boolean);
procedure SetState_AddPolyCutout(AValue: Boolean);
procedure SetState_Board(AValue: IPCB_Board);
procedure SetState_Default;
procedure SetState_Distance(AValue: Integer);
procedure SetState_MultipleObjects(AValue: Boolean);
procedure SetState_Net(AValue: IPCB_Net);
procedure SetState_NetName(AValue: string);
procedure SetState_Pullback(AValue: Integer);
procedure SetState_RowCount(AValue: Integer);
procedure SetState_RowStep(AValue: Integer);
procedure SetState_Stagger(AValue: Boolean);
procedure SetState_Step(AValue: Integer);
procedure SetState_TemplateVia(AValue: IPCB_Via);
procedure SetState_ViaNet(AValue: IPCB_Net);
procedure SetState_ViaNetName(AValue: string);
procedure SetState_ViaPadClearance(AValue: Integer);

## IPCB_ViaShieldingSU
继承：IPCB_ViaShieldingSU → IPCB_SmartUnionObject → IPCB_SmartUnionPlaceHolder → IPCB_RectangularPrimitive → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 5 个方法、3 个属性

property IsFilled: Boolean read GetState_IsFilled;  // read-only
property MultipleObjects: Boolean read GetState_MultipleObjects write SetState_MultipleObjects;
property Options: IPCB_ViaShieldingOptions read GetState_Options;  // read-only
function GetState_IsFilled: Boolean;
function GetState_MultipleObjects: Boolean;
function GetState_Options: IPCB_ViaShieldingOptions;
procedure Rebuild;
procedure SetState_MultipleObjects(AValue: Boolean);

## IPCB_ViaStitchFloodOptions
继承：IPCB_ViaStitchFloodOptions → IInterface ｜ 单元：RT_PCB ｜ 自有 26 个方法、10 个属性

property Board: IPCB_Board read GetState_Board write SetState_Board;
property Net: IPCB_Net read GetState_Net write SetState_Net;
property NetName: TDynamicString read GetState_NetName write SetState_NetName;
property OffsetX: TCoord read GetState_OffsetX write SetState_OffsetX;
property OffsetY: TCoord read GetState_OffsetY write SetState_OffsetY;
property Pullback: TCoord read GetState_Pullback write SetState_Pullback;
property Stagger: Boolean read GetState_Stagger write SetState_Stagger;
property Step: TCoord read GetState_Step write SetState_Step;
property TemplateVia: IPCB_Via read GetState_TemplateVia;  // read-only
property ViaPadClearance: TCoord read GetState_ViaPadClearance write SetState_ViaPadClearance;
procedure Export_ToOptionsWriter;
procedure Export_ToParameters(const AParameters: IParameterList);
function GetState_Board: IPCB_Board;
function GetState_Net: IPCB_Net;
function GetState_NetName: string;
function GetState_OffsetX: Integer;
function GetState_OffsetY: Integer;
function GetState_Pullback: Integer;
function GetState_Stagger: Boolean;
function GetState_Step: Integer;
function GetState_TemplateVia: IPCB_Via;
function GetState_ViaPadClearance: Integer;
function I_ObjectAddress: Pointer;
procedure Import_FromOptionsReader;
procedure Import_FromParameters(const AParameters: IParameterList);
function Replicate: IPCB_ViaStitchFloodOptions;
procedure SetState_Board(AValue: IPCB_Board);
procedure SetState_Default;
procedure SetState_Net(AValue: IPCB_Net);
procedure SetState_NetName(AValue: string);
procedure SetState_OffsetX(AValue: Integer);
procedure SetState_OffsetY(AValue: Integer);
procedure SetState_Pullback(AValue: Integer);
procedure SetState_Stagger(AValue: Boolean);
procedure SetState_Step(AValue: Integer);
procedure SetState_ViaPadClearance(AValue: Integer);

## IPCB_ViaStitchingSU
继承：IPCB_ViaStitchingSU → IPCB_SmartUnionObject → IPCB_SmartUnionPlaceHolder → IPCB_RectangularPrimitive → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 8 个方法、3 个属性

property IsConstrainArea: Boolean read GetState_IsConstrainArea write SetState_IsConstrainArea;
property IsDefiningArea: Boolean read GetState_IsDefiningArea write SetState_IsDefiningArea;
property Options: IPCB_ViaStitchFloodOptions read GetState_Options;  // read-only
function DefineArea: LongBool;
function GetState_GeometricPolygon: IPCB_GeometricPolygon;
function GetState_IsConstrainArea: Boolean;
function GetState_IsDefiningArea: Boolean;
function GetState_Options: IPCB_ViaStitchFloodOptions;
procedure RebuildAfterUpdate(const ShowPrompt: LongBool);
procedure SetState_IsConstrainArea(AValue: Boolean);
procedure SetState_IsDefiningArea(AValue: Boolean);

## IPCB_ViaStructure
继承：IPCB_ViaStructure → IInterface ｜ 单元：RT_PCB ｜ 自有 16 个方法、9 个属性

property CanEditFeature[AType: TViaStructureFeatureType]: Boolean read GetState_CanEditFeature;  // read-only
property CanEditMaterial[AType: TViaStructureFeatureType]: Boolean read GetState_CanEditMaterial;  // read-only
property CanEditSide[AType: TViaStructureFeatureType]: Boolean read GetState_CanEditSide;  // read-only
property Feature[AIndex: Integer]: IPCB_ViaStructureFeature read GetState_Feature;  // read-only
property FeatureByType[AType: TViaStructureFeatureType]: IPCB_ViaStructureFeature read GetState_FeatureByType;  // read-only
property FeaturesCount: Integer read GetState_FeaturesCount;  // read-only
property FeaturesSide: TViaStructureFeatureSide read GetState_FeaturesSide write SetState_FeaturesSide;
property StructureType: TViaStructureType read GetState_StructureType write SetState_StructureType;
property vIndexForSave: Integer read GetState_vIndexForSave write SetState_vIndexForSave;
procedure CopyTo(const AViaStructure: IPCB_ViaStructure);
function GetFeatureTypes: TViaStructureFeatureTypeSet;
function GetState_CanEditFeature(AType: TViaStructureFeatureType): Boolean;
function GetState_CanEditMaterial(AType: TViaStructureFeatureType): Boolean;
function GetState_CanEditSide(AType: TViaStructureFeatureType): Boolean;
function GetState_Feature(AIndex: Integer): IPCB_ViaStructureFeature;
function GetState_FeatureByType(AType: TViaStructureFeatureType): IPCB_ViaStructureFeature;
function GetState_FeaturesCount: Integer;
function GetState_FeaturesSide: TViaStructureFeatureSide;
function GetState_StructureType: TViaStructureType;
function GetState_vIndexForSave: Integer;
function IsEqual(AViaStructure: IPCB_ViaStructure): Boolean;
function Replicate: IPCB_ViaStructure;
procedure SetState_FeaturesSide(AValue: TViaStructureFeatureSide);
procedure SetState_StructureType(AValue: TViaStructureType);
procedure SetState_vIndexForSave(AIndex: Integer);

## IPCB_ViaStructureFeature
继承：IPCB_ViaStructureFeature → IInterface ｜ 单元：RT_PCB ｜ 自有 9 个方法、4 个属性

property CanSelectSide[ASide: TViaStructureFeatureSide]: Boolean read GetState_CanSelectSide;  // read-only
property FeatureType: TViaStructureFeatureType read GetState_FeatureType write SetState_FeatureType;
property Material: TPCBString read GetState_Material write SetState_Material;
property Side: TViaStructureFeatureSide read GetState_Side write SetState_Side;
procedure CopyTo(const AFeature: IPCB_ViaStructureFeature);
function GetState_CanSelectSide(ASide: TViaStructureFeatureSide): Boolean;
function GetState_FeatureType: TViaStructureFeatureType;
function GetState_Material: WideString;
function GetState_Side: TViaStructureFeatureSide;
function Replicate: IPCB_ViaStructureFeature;
procedure SetState_FeatureType(AType: TViaStructureFeatureType);
procedure SetState_Material(AMaterial: WideString);
procedure SetState_Side(ASide: TViaStructureFeatureSide);

## IPCB_ViaStructureManager
继承：IPCB_ViaStructureManager → IInterface ｜ 单元：RT_PCB ｜ 自有 8 个方法、2 个属性

property Count: Integer read GetState_Count;  // read-only
property Items[AIndex: Integer]: IPCB_ViaStructure read GetState_Item;  // read-only
procedure ChangeFeatureTypeCounter(AFeatureType: TViaStructureFeatureType; AIncrement: Boolean);
procedure Clear;
procedure ClearFeatureTypeCounter;
function CreateViaStructure(AFullFeatureList: Boolean; AViaStructureType: TViaStructureType): IPCB_ViaStructure;
function GetState_Count: Integer;
function GetState_Item(AIndex: Integer): IPCB_ViaStructure;
function IsFeatureTypeExists(AFeatureType: TViaStructureFeatureType): Boolean;
function RegisterViaStructure(const AViaStructure: IPCB_ViaStructure): IPCB_ViaStructure;

## IPCB_ViaStructureSupport
继承：IPCB_ViaStructureSupport → IInterface ｜ 单元：RT_PCB ｜ 自有 5 个方法、2 个属性

property ViaStructure: IPCB_ViaStructure read GetState_ViaStructure write SetState_ViaStructure;
property ViaStructureType: TViaStructureType read GetState_ViaStructureType write SetState_ViaStructureType;
function GetState_ViaStructure: IPCB_ViaStructure;
function GetState_ViaStructureType: TViaStructureType;
function GetViaStructureReplica: IPCB_ViaStructure;
procedure SetState_ViaStructure(const AValue: IPCB_ViaStructure);
procedure SetState_ViaStructureType(const AValue: TViaStructureType);

## IPCB_ViaTemplate
继承：IPCB_ViaTemplate → IPCB_PadViaTemplate → IInterface ｜ 单元：RT_PCB ｜ 自有 0 个方法、0 个属性


## IPCB_ViasUnderSMDConstraint
继承：IPCB_ViasUnderSMDConstraint → IPCB_Rule → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 2 个方法、1 个属性

property Allowed: Boolean read GetState_Allowed write SetState_Allowed;
function GetState_Allowed: Boolean;
procedure SetState_Allowed(Value: Boolean);

## IPCB_Viewport
继承：IPCB_Viewport → IPCB_RectangularPrimitive → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 28 个方法、12 个属性

property IsViewport: Boolean read GetState_IsViewport write SetState_IsViewport;
property Scale: Double read GetState_Scale write SetState_Scale;
property TitleFontColor: TColor read GetState_TitleFontColor write SetState_TitleFontColor;
property TitleFontName: TPCBString read GetState_TitleFontName write SetState_TitleFontName;
property TitleFontSize: Integer read GetState_TitleFontSize write SetState_TitleFontSize;
property TitleObject: Int64 read GetState_TitleObject;  // read-only
property ViewConfig: TPCBString read GetState_ViewConfig write SetState_ViewConfig;
property ViewConfigType: TPCBString read GetState_ViewConfigType write SetState_ViewConfigType;
property ViewportRect: TCoordRect read GetState_ViewportRect write SetState_ViewportRect;
property ViewportTitle: TPCBString read GetState_ViewportTitle write SetState_ViewportTitle;
property ViewportVisible: Boolean read GetState_ViewportVisible write SetState_ViewportVisible;
property VisibleLayers: IPCB_LayerSet read GetState_VisibleLayers;  // read-only
procedure DefineViewportRectGraphically;
function GetState_ChildBoard: IPCB_Board;
function GetState_DocumentPath: WideString;
function GetState_IsViewport: Boolean;
function GetState_Mirror: Boolean;
function GetState_Scale: Double;
function GetState_TitleFontColor: Cardinal;
function GetState_TitleFontName: WideString;
function GetState_TitleFontSize: Integer;
function GetState_TitleObject: Int64;
function GetState_ViewConfig: WideString;
function GetState_ViewConfigType: WideString;
function GetState_ViewportRect: IDispatch;
function GetState_ViewportTitle: WideString;
function GetState_ViewportVisible: Boolean;
function GetState_VisibleLayers: IPCB_LayerSet;
procedure SetState_DocumentPath(Value: WideString);
procedure SetState_IsViewport(Value: Boolean);
procedure SetState_Mirror(Value: Boolean);
procedure SetState_Scale(Value: Double);
procedure SetState_TitleFontColor(Value: Cardinal);
procedure SetState_TitleFontName(Value: WideString);
procedure SetState_TitleFontSize(Value: Integer);
procedure SetState_ViewConfig(Value: WideString);
procedure SetState_ViewConfigType(Value: WideString);
procedure SetState_ViewportRect(const Value: IDispatch);
procedure SetState_ViewportTitle(Value: WideString);
procedure SetState_ViewportVisible(Value: Boolean);

## IPCB_Violation
继承：IPCB_Violation → IPCB_Primitive → IInterface ｜ 单元：RT_PCB ｜ 自有 10 个方法、7 个属性

property Description: TPCBString read GetState_Description;  // read-only
property IsWaived: Boolean read GetState_IsWaived;  // read-only
property Name: TPCBString read GetState_Name;  // read-only
property Primitive1: IPCB_Primitive read GetState_Primitive1;  // read-only
property Primitive2: IPCB_Primitive read GetState_Primitive2;  // read-only
property Rule: IPCB_Primitive read GetState_Rule;  // read-only
property WaivedInfo: IPCB_WaivedViolationInfo read GetState_WaivedInfo write SetState_WaivedInfo;
function GetState_Description: WideString;
function GetState_IsWaived: Boolean;
function GetState_Name: WideString;
function GetState_Primitive1: IPCB_Primitive;
function GetState_Primitive2: IPCB_Primitive;
function GetState_Rule: IPCB_Primitive;
function GetState_ShortDescriptorString: WideString;
function GetState_WaivedInfo: IPCB_WaivedViolationInfo;
function IsRedundant: Boolean;
procedure SetState_WaivedInfo(const AValue: IPCB_WaivedViolationInfo);

## IPCB_ViolationsFactory
继承：IPCB_ViolationsFactory → IInterface ｜ 单元：RT_PCB ｜ 自有 4 个方法、0 个属性

function CreateAuthorInfo(const AID: string; const ATitle: string; const ASource: string): IPCB_AuthorInfo;
function CreateCurrentAuthorInfo: IPCB_AuthorInfo;
function CreateDefaultWaivedViolationInfo: IPCB_WaivedViolationInfo;
function CreateWaivedViolationInfo: IPCB_WaivedViolationInfo;

## IPCB_WaivedViolationInfo
继承：IPCB_WaivedViolationInfo → IInterface ｜ 单元：RT_PCB ｜ 自有 9 个方法、3 个属性

property Author: IPCB_AuthorInfo read GetAuthor write SetAuthor;
property Comment: TPCBString read GetComment write SetComment;
property CreatedAt: TDateTime read GetCreatedAt write SetCreatedAt;
function CanChangeAuthor: Boolean;
function Clone: IPCB_WaivedViolationInfo;
procedure CopyTo(const ADest: IPCB_WaivedViolationInfo);
function GetAuthor: IPCB_AuthorInfo;
function GetComment: WideString;
function GetCreatedAt: TDateTime;
procedure SetAuthor(const AValue: IPCB_AuthorInfo);
procedure SetComment(const AValue: WideString);
procedure SetCreatedAt(AValue: TDateTime);

## IPCB_WideStrings
继承：IPCB_WideStrings → IInterface ｜ 单元：RT_PCB ｜ 自有 10 个方法、4 个属性

property Count: Integer read GetCount;  // read-only
property Duplicates: TDuplicates read GetDuplicates write SetDuplicates;
property Sorted: Boolean read GetSorted write SetSorted;
property Strings[Index: Integer]: WideString read Get write Put;
procedure BeginUpdate;
procedure Clear;
procedure EndUpdate;
function Get(Index: Integer): WideString;
function GetCount: Integer;
function GetDuplicates: TDuplicates;
function GetSorted: Boolean;
procedure Put(Index: Integer; const Value: WideString);
procedure SetDuplicates(Value: TDuplicates);
procedure SetSorted(Value: Boolean);

## IPrintedElectronics
继承：IPrintedElectronics → IInterface ｜ 单元：RT_PCB ｜ 自有 11 个方法、0 个属性

procedure Clear;
function GetDielectricalLayers: IPCB_LayerSet;
function GetDielectricBetweenTwoLayers(AUpperLayer: Integer; ALowerLayer: Integer): IPCB_LayerSet;
function GetElectricalLayers: IPCB_LayerSet;
function GetLowerDielectricBetweenTwoLayers(AUpperLayer: Integer; ALowerLayer: Integer): IPCB_LayerObject;
function GetMaxClearance: Integer;
function GetMaxViaSizeOnElectricalLayers(const APrimitive: IPCB_Primitive): Integer;
function GetState_ArcApproximation: Integer;
function ProducePrimitiveToCheck(APrimitive1: IPCB_Primitive; APrimitive2: IPCB_Primitive; var AUpperPrimitive: IPCB_Primitive; var ALowerPrimitive: IPCB_Primitive): Boolean;
function ProducePrimitiveToCheckOnTopLayerInGroup(APrimitive1: IPCB_Primitive; APrimitive2: IPCB_Primitive; var AUpperPrimitive: IPCB_Primitive; var ALowerPrimitive: IPCB_Primitive): Boolean;
procedure RemovePrimitive(APrimitive: IPCB_Primitive);

## IRuleCheckNotificationHandler
继承：IRuleCheckNotificationHandler → IInterface ｜ 单元：RT_PCB ｜ 自有 5 个方法、0 个属性

procedure BatchHandleNotifications(const ADRCResultList: IInterfaceList);
procedure BeginUpdate;
procedure ClearBinaryResults;
procedure EndUpdate;
procedure HandleNotification(const DRCResult: IPCB_DRCResult);

## IStackObjectThermalReliefIterator
继承：IStackObjectThermalReliefIterator → IInterface ｜ 单元：RT_PCB ｜ 自有 3 个方法、0 个属性

function Current: IDispatch;
function First: Boolean;
function Next: Boolean;

## ITeardropOptions
继承：ITeardropOptions → IInterface ｜ 单元：RT_PCB ｜ 自有 18 个方法、8 个属性

property Action: TTeardropActionEx read GetState_Action write SetState_Action;
property Adjust: Boolean read GetState_Adjust write SetState_Adjust;
property CreateReport: Boolean read GetState_CreateReport write SetState_CreateReport;
property ForceTeardrops: Boolean read GetState_ForceTeardrops write SetState_ForceTeardrops;
property ObjectEnabled[AObject: TTeardropObject]: Boolean read GetState_ObjectEnabled write SetState_ObjectEnabled;
property SelectedObjectsOnly: Boolean read GetState_SelectedObjectsOnly write SetState_SelectedObjectsOnly;
property SizePercentArray[AObject: TTeardropObject]: TTeardropObjectSize read GetState_SizePercentArray write SetState_SizePercentArray;
property Style: TTeardropStyleEx read GetState_Style write SetState_Style;
procedure Export_ToParameters(AParameters: IParameterList);
function GetState_Action: TTeardropActionEx;
function GetState_Adjust: Boolean;
function GetState_CreateReport: Boolean;
function GetState_ForceTeardrops: Boolean;
function GetState_ObjectEnabled(AObject: TTeardropObject): Boolean;
function GetState_SelectedObjectsOnly: Boolean;
function GetState_SizePercentArray(AObject: TTeardropObject): IDispatch;
function GetState_Style: TTeardropStyleEx;
function Import_FromParameters(AParameters: IParameterList): Boolean;
procedure SetState_Action(AValue: TTeardropActionEx);
procedure SetState_Adjust(AValue: Boolean);
procedure SetState_CreateReport(AValue: Boolean);
procedure SetState_ForceTeardrops(AValue: Boolean);
procedure SetState_ObjectEnabled(AObject: TTeardropObject; AValue: Boolean);
procedure SetState_SelectedObjectsOnly(AValue: Boolean);
procedure SetState_SizePercentArray(AObject: TTeardropObject; const AValue: IDispatch);
procedure SetState_Style(AValue: TTeardropStyleEx);

