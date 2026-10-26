# 类

来源：Altium Designer 23.1.1.15 的 `System\ScriptingSystem.dll`（脚本引擎的注册表，2026-10-25 提取）。由 `scripts/gen_docs.py` 生成，不要手改。

每节列出该类自己的成员：显式注册的方法/属性，加上 RTTI 里的 published 属性（窗体控件的属性、事件都在这里）。继承成员在父类那一节；不在本文件里的父类（如 TObject）没有向脚本单独注册成员。带下标的类属性只知道下标个数，不知道类型（写成 `Index: ?`）。

## AlignAttribute
继承：AlignAttribute → TCustomAttribute → TObject ｜ 单元：System

property Align: Integer;  // read-only
procedure Create(Align: Integer);

## ComponentPlatformsAttribute
继承：ComponentPlatformsAttribute → TCustomAttribute → TObject ｜ 单元：System.Classes

property Platforms: TPlatformIds;
procedure Create(const Platforms: Cardinal);

## DefaultAttribute
继承：DefaultAttribute → TDefaultAttributeBase → TCustomAttribute → TObject ｜ 单元：System.Classes

procedure Create(const DefaultValue: Boolean);

## EADOError
继承：EADOError → EDatabaseError → Exception → TObject ｜ 单元：Data.Win.ADODB


## EBitsError
继承：EBitsError → Exception → TObject ｜ 单元：System.Classes


## EClassNotFound
继承：EClassNotFound → EFilerError → EStreamError → Exception → TObject ｜ 单元：System.Classes


## EClipboardException
继承：EClipboardException → Exception → TObject ｜ 单元：Vcl.Clipbrd


## ECommonCalendarError
继承：ECommonCalendarError → Exception → TObject ｜ 单元：Vcl.ComCtrls


## EComponentError
继承：EComponentError → Exception → TObject ｜ 单元：System.Classes


## EDatabaseError
继承：EDatabaseError → Exception → TObject ｜ 单元：Data.DB


## EDateTimeError
继承：EDateTimeError → ECommonCalendarError → Exception → TObject ｜ 单元：Vcl.ComCtrls


## EDateTimeException
继承：EDateTimeException → Exception → TObject ｜ 单元：System.DateUtils


## EDBEditError
继承：EDBEditError → Exception → TObject ｜ 单元：Vcl.Mask


## EFCreateError
继承：EFCreateError → EFileStreamError → EStreamError → Exception → TObject ｜ 单元：System.Classes


## EFileCorruptedException
继承：EFileCorruptedException → Exception → TObject ｜ 单元：Rt_Util


## EFilerError
继承：EFilerError → EStreamError → Exception → TObject ｜ 单元：System.Classes


## EFileStreamError
继承：EFileStreamError → EStreamError → Exception → TObject ｜ 单元：System.Classes


## EFOpenError
继承：EFOpenError → EFileStreamError → EStreamError → Exception → TObject ｜ 单元：System.Classes


## EGestureException
继承：EGestureException → Exception → TObject ｜ 单元：Vcl.Controls


## EGridPanelException
继承：EGridPanelException → Exception → TObject ｜ 单元：Vcl.ExtCtrls


## EIniFileException
继承：EIniFileException → Exception → TObject ｜ 单元：System.IniFiles


## EInOutError
继承：EInOutError → Exception → TObject ｜ 单元：System.SysUtils ｜ 未在类列表里注册，只能通过实例访问

field ErrorCode;

## EInvalidArgument
继承：EInvalidArgument → EMathError → EMathError ｜ 单元：System.Math


## EInvalidGraphic
继承：EInvalidGraphic → Exception → TObject ｜ 单元：Vcl.Graphics


## EInvalidGraphicOperation
继承：EInvalidGraphicOperation → Exception → TObject ｜ 单元：Vcl.Graphics


## EInvalidGridOperation
继承：EInvalidGridOperation → Exception → TObject ｜ 单元：Vcl.Grids


## EInvalidImage
继承：EInvalidImage → EFilerError → EStreamError → Exception → TObject ｜ 单元：System.Classes


## EInvalidOperation
继承：EInvalidOperation → Exception → TObject ｜ 单元：System.Classes


## EListError
继承：EListError → Exception → TObject ｜ 单元：System.SysUtils


## ELocalTimeInvalid
继承：ELocalTimeInvalid → Exception → TObject ｜ 单元：System.DateUtils


## ELoginCredentialError
继承：ELoginCredentialError → Exception → TObject ｜ 单元：System.Classes


## EMCIDeviceError
继承：EMCIDeviceError → Exception → TObject ｜ 单元：Vcl.MPlayer


## EMenuError
继承：EMenuError → Exception → TObject ｜ 单元：Vcl.Menus


## EMethodNotFound
继承：EMethodNotFound → EFilerError → EStreamError → Exception → TObject ｜ 单元：System.Classes


## EMonthCalError
继承：EMonthCalError → ECommonCalendarError → Exception → TObject ｜ 单元：Vcl.ComCtrls


## EObserverException
继承：EObserverException → Exception → TObject ｜ 单元：System.Classes


## EOleCtrlError
继承：EOleCtrlError → Exception → TObject ｜ 单元：Vcl.OleCtrls


## EOSError
继承：EOSError → Exception → TObject ｜ 单元：System.SysUtils ｜ 未在类列表里注册，只能通过实例访问

field ErrorCode;

## EOutOfResources
继承：EOutOfResources → EOutOfMemory → EOutOfMemory ｜ 单元：System.Classes


## EOutputError
继承：EOutputError → Exception → TObject ｜ 单元：Rt_AbstractOutput


## EParserError
继承：EParserError → Exception → TObject ｜ 单元：System.Classes


## EPlatformVersionException
继承：EPlatformVersionException → Exception → TObject ｜ 单元：Vcl.Dialogs


## EPNGCannotChangeTransparent
继承：EPNGCannotChangeTransparent → Exception → TObject ｜ 单元：Vcl.Imaging.pngimage


## EPNGCouldNotLoadResource
继承：EPNGCouldNotLoadResource → Exception → TObject ｜ 单元：Vcl.Imaging.pngimage


## EPngError
继承：EPngError → Exception → TObject ｜ 单元：Vcl.Imaging.pngimage


## EPNGHeaderNotPresent
继承：EPNGHeaderNotPresent → Exception → TObject ｜ 单元：Vcl.Imaging.pngimage


## EPNGIHDRNotFirst
继承：EPNGIHDRNotFirst → Exception → TObject ｜ 单元：Vcl.Imaging.pngimage


## EPngInvalidCRC
继承：EPngInvalidCRC → Exception → TObject ｜ 单元：Vcl.Imaging.pngimage


## EPNGInvalidFileHeader
继承：EPNGInvalidFileHeader → Exception → TObject ｜ 单元：Vcl.Imaging.pngimage


## EPngInvalidIHDR
继承：EPngInvalidIHDR → Exception → TObject ｜ 单元：Vcl.Imaging.pngimage


## EPNGInvalidNewSize
继承：EPNGInvalidNewSize → Exception → TObject ｜ 单元：Vcl.Imaging.pngimage


## EPNGInvalidPalette
继承：EPNGInvalidPalette → Exception → TObject ｜ 单元：Vcl.Imaging.pngimage


## EPNGInvalidSpec
继承：EPNGInvalidSpec → Exception → TObject ｜ 单元：Vcl.Imaging.pngimage


## EPNGMissingMultipleIDAT
继承：EPNGMissingMultipleIDAT → Exception → TObject ｜ 单元：Vcl.Imaging.pngimage


## EPNGMissingPalette
继承：EPNGMissingPalette → Exception → TObject ｜ 单元：Vcl.Imaging.pngimage


## EPNGNoImageData
继承：EPNGNoImageData → Exception → TObject ｜ 单元：Vcl.Imaging.pngimage


## EPNGNotExists
继承：EPNGNotExists → Exception → TObject ｜ 单元：Vcl.Imaging.pngimage


## EPNGOutMemory
继承：EPNGOutMemory → Exception → TObject ｜ 单元：Vcl.Imaging.pngimage


## EPNGSizeExceeds
继承：EPNGSizeExceeds → Exception → TObject ｜ 单元：Vcl.Imaging.pngimage


## EPngUnexpectedEnd
继承：EPngUnexpectedEnd → Exception → TObject ｜ 单元：Vcl.Imaging.pngimage


## EPNGUnknownCompression
继承：EPNGUnknownCompression → Exception → TObject ｜ 单元：Vcl.Imaging.pngimage


## EPNGUnknownCriticalChunk
继承：EPNGUnknownCriticalChunk → Exception → TObject ｜ 单元：Vcl.Imaging.pngimage


## EPNGUnknownInterlace
继承：EPNGUnknownInterlace → Exception → TObject ｜ 单元：Vcl.Imaging.pngimage


## EPNGZLIBError
继承：EPNGZLIBError → Exception → TObject ｜ 单元：Vcl.Imaging.pngimage


## EPrinter
继承：EPrinter → Exception → TObject ｜ 单元：Vcl.Printers


## EReadError
继承：EReadError → EFilerError → EStreamError → Exception → TObject ｜ 单元：System.Classes


## ERegistryException
继承：ERegistryException → Exception → TObject ｜ 单元：System.Win.Registry


## EResNotFound
继承：EResNotFound → Exception → TObject ｜ 单元：System.Classes


## EStreamError
继承：EStreamError → Exception → TObject ｜ 单元：System.Classes


## EStringListError
继承：EStringListError → Exception → TObject ｜ 单元：System.Classes


## EThread
继承：EThread → Exception → TObject ｜ 单元：System.Classes


## EThreadExternalException
继承：EThreadExternalException → EThread → Exception → TObject ｜ 单元：System.Classes


## ETreeViewError
继承：ETreeViewError → Exception → TObject ｜ 单元：Vcl.ComCtrls


## EUpdateError
继承：EUpdateError → EDatabaseError → Exception → TObject ｜ 单元：Data.DB

property Context: String;  // read-only
property ErrorCode: Integer;  // read-only
property OriginalException: Exception;  // read-only
property PreviousError: Integer;  // read-only
procedure Create(NativeError: string; Context: string; ErrCode: Integer; PrevError: Integer; E: Exception);

## EUserException
继承：EUserException → Exception → TObject ｜ 单元：Rt_Util


## EVariantArrayCreateError
继承：EVariantArrayCreateError → EVariantError → EVariantError ｜ 单元：System.Variants


## EVariantArrayLockedError
继承：EVariantArrayLockedError → EVariantError → EVariantError ｜ 单元：System.Variants


## EVariantBadIndexError
继承：EVariantBadIndexError → EVariantError → EVariantError ｜ 单元：System.Variants


## EVariantBadVarTypeError
继承：EVariantBadVarTypeError → EVariantError → EVariantError ｜ 单元：System.Variants


## EVariantDispatchError
继承：EVariantDispatchError → EVariantError → EVariantError ｜ 单元：System.Variants


## EVariantInvalidArgError
继承：EVariantInvalidArgError → EVariantError → EVariantError ｜ 单元：System.Variants


## EVariantInvalidNullOpError
继承：EVariantInvalidNullOpError → EVariantInvalidOpError → EVariantError ｜ 单元：System.Variants


## EVariantInvalidOpError
继承：EVariantInvalidOpError → EVariantError → EVariantError ｜ 单元：System.Variants


## EVariantNotAnArrayError
继承：EVariantNotAnArrayError → EVariantError → EVariantError ｜ 单元：System.Variants


## EVariantNotImplError
继承：EVariantNotImplError → EVariantError → EVariantError ｜ 单元：System.Variants


## EVariantOutOfMemoryError
继承：EVariantOutOfMemoryError → EVariantError → EVariantError ｜ 单元：System.Variants


## EVariantOverflowError
继承：EVariantOverflowError → EVariantError → EVariantError ｜ 单元：System.Variants


## EVariantRangeCheckError
继承：EVariantRangeCheckError → EVariantOverflowError → EVariantError ｜ 单元：System.Variants


## EVariantTypeCastError
继承：EVariantTypeCastError → EVariantError → EVariantError ｜ 单元：System.Variants


## EVariantUnexpectedError
继承：EVariantUnexpectedError → EVariantError → EVariantError ｜ 单元：System.Variants


## EWriteError
继承：EWriteError → EFilerError → EStreamError → Exception → TObject ｜ 单元：System.Classes


## Exception
继承：Exception → TObject ｜ 单元：System.SysUtils ｜ 未在类列表里注册，只能通过实例访问

property BaseException: Exception;  // read-only
property HelpContext: Integer;
property InnerException: Exception;  // read-only
property Message: String;
property StackInfo: Pointer;  // read-only
property StackTrace: String;  // read-only
procedure Create(const Msg: string);
procedure CreateFmt(const Msg: string; const Args: array of TVarRec);
procedure CreateFmtHelp(const Msg: string; const Args: array of TVarRec; AHelpContext: Integer);
procedure CreateHelp(const Msg: string; AHelpContext: Integer);
procedure CreateRes(Ident: NativeUInt);
procedure CreateResFmt(Ident: NativeUInt; const Args: array of TVarRec);
procedure CreateResHelp(Ident: NativeUInt; AHelpContext: Integer);
function GetBaseException: Exception;
procedure RaiseOuterException(E: Exception);
procedure ThrowOuterException(E: Exception);

## HFAAttribute
继承：HFAAttribute → TCustomAttribute → TObject ｜ 单元：System

property ElementCount: Integer;  // read-only
property ElementType: Pointer;  // read-only
procedure Create(const ElementType: Pointer; const ElementCount: Integer);

## HPPGENAttribute
继承：HPPGENAttribute → TCustomAttribute → TObject ｜ 单元：System

procedure Create(const AData: string);

## NoDefaultAttribute
继承：NoDefaultAttribute → TDefaultAttributeBase → TCustomAttribute → TObject ｜ 单元：System.Classes

procedure Create;

## ObservableMemberAttribute
继承：ObservableMemberAttribute → TCustomAttribute → TObject ｜ 单元：System.Classes

property MemberName: String;  // read-only
procedure Create(const AMemberName: string);

## RefAttribute
继承：RefAttribute → TCustomAttribute → TObject ｜ 单元：System


## StoredAttribute
继承：StoredAttribute → TCustomAttribute → TObject ｜ 单元：System

property Flag: Boolean;  // read-only
property Name: String;  // read-only
procedure Create;

## TAbstractDeviceIOStandard
继承：TAbstractDeviceIOStandard → TDispatchObjectNoRef → TDispatchObjectNoRef ｜ 单元：Rt_AbstractFPGA

function GetDisplayName: WideString;
function GetDriveCount: Integer;
function GetDriveStrength(Index: Integer): WideString;
function GetParamName: WideString;
function GetSlewCount: Integer;
function GetSlewValue(Index: Integer): WideString;
function GetStandard: TDeviceIOStandardType;

## TAbstractDevicePin
继承：TAbstractDevicePin → TDispatchObjectNoRef → TDispatchObjectNoRef ｜ 单元：Rt_AbstractFPGA

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

## TAbstractSupplier
继承：TAbstractSupplier → TInterfacedObject → TObject ｜ 单元：RT_Supplier

procedure BackgroundGetCategoryParameters(Category: ISupplierCategory; Handle: HWND);
procedure BackgroundSearchByKeyword(Keywords: WideString; RecordCount: Integer; StartRecord: Integer; SearchFilters: TSupplierSearchFilters; Category: ISupplierCategory; ParametricFilters: ISupplierParametricFilters; Handle: HWND);
procedure BackgroundSearchByManufacturerPartNumber(ManufacturerPartNumber: WideString; Handle: HWND);
procedure BackgroundSearchBySupplierPartNumber(SupplierPartNumber: WideString; SkipOptions: TSkipOptionSet; Handle: HWND);
procedure Create(BrandIndex: Integer);
function CreateSupplierCart: ISupplierCart;
function CreateSupplierThread: TSupplierThread;
function GetCategoryParameters(Category: ISupplierCategory): ISupplierCategoryParameters;
function GetOptionsPage: IOptionsPage;
function GetSearchUrl(const APartNumber: WideString): WideString;
procedure OptionsChanged(const Options: WideString);
function SearchByKeyword(Keywords: WideString; RecordCount: Integer; StartRecord: Integer; SearchFilters: TSupplierSearchFilters; Category: ISupplierCategory; ParametricFilters: ISupplierParametricFilters): ISupplierSearchResults;
function SearchByManufacturerPartNumber(ManufacturerPartNumber: WideString): ISupplierSearchResults;
function SearchBySupplierPartNumber(SupplierPartNumber: WideString; SkipOptions: TSkipOptionSet): ISupplierSourceRelationship;
function SupportedSearchFilters: TSupplierSearchFilters;

## TAbstractSupplierCart
继承：TAbstractSupplierCart → TInterfacedObject → TObject ｜ 单元：RT_Supplier

procedure Add(SupplierName: WideString; SupplierPartNumber: WideString; Quantity: Integer);
function URL: WideString;

## TAbstractSupplierSourceRelationship
继承：TAbstractSupplierSourceRelationship → TInterfacedObject → TObject ｜ 单元：RT_Supplier

procedure Create;
function GetState_AvailabilityCount: Integer;
function GetState_AvailabilityLeadTime(I: Integer): WideString;
function GetState_AvailabilityQuantity(I: Integer): Integer;
function GetState_BreakQuantity(I: Integer): Integer;
function GetState_Category: WideString;
function GetState_Currency: WideString;
function GetState_Description: WideString;
function GetState_ManufacturerName: WideString;
function GetState_ManufacturerPartNumber: WideString;
function GetState_Name: WideString;
function GetState_ParameterAt(I: Integer): IItemParameter;
function GetState_ParameterByName(Name: WideString): IItemParameter;
function GetState_ParametersCount: Integer;
function GetState_PartId: WideString;
function GetState_ProductPhotoURL: WideString;
function GetState_ProviderGUID: WideString;
function GetState_ProviderName: WideString;
function GetState_QuantityInStock: Integer;
function GetState_RoHS: WideString;
function GetState_SupplierName: WideString;
function GetState_SupplierPartNumber: WideString;
function GetState_SupplierPartNumberAlias: WideString;
function GetState_SupplierSource: WideString;
function GetState_SupportingDocumentIdAt(I: Integer): WideString;
function GetState_SupportingDocumentsIdsCount: Integer;
function GetState_UnitPrice(I: Integer): WideString;
function GetState_UnitPriceCount: Integer;
function GetState_UnitPriceForQuantity(Quantity: Integer): WideString;
function I_ObjectAddress: Pointer;

## TActelMSSConfigFile
继承：TActelMSSConfigFile → TObject ｜ 单元：Rt_ActelFPGA

procedure Create(AFileName: string);
function GetPortDirection(AIndex: Integer): TPinElectrical;
function GetPortName(AIndex: Integer): string;
function GetPortsCount: Integer;
function GetUseAnalogInterface: Boolean;

## TActelMSSConfigurator
继承：TActelMSSConfigurator → TObject ｜ 单元：Rt_ActelFPGA

function CopyConfigurationFile(ATargetFolder: string): Boolean;
function CopyDesignFile(ATargetFolder: string): string;
procedure Create(ANexusDriver: INexusDriver);
function GetTopLevelPorts(AProjectPath: string; var APinNames: TDynamicStringArray; var APinElectrical: TPinElectricalArray): Boolean;
function GetUseAnalogInterface: Boolean;
procedure Launch;

## TAction
继承：TAction → TCustomAction → TContainedAction ｜ 单元：Vcl.ActnList

property AutoCheck: Boolean;
property Caption: string;
property Checked: Boolean;
property Enabled: Boolean;
property GroupIndex: Integer;
property HelpContext: THelpContext;
property HelpKeyword: string;
property HelpType: THelpType;
property Hint: string;
property ImageIndex: TImageIndex;
property OnExecute: TNotifyEvent;
property OnHint: THintEvent;
property OnUpdate: TNotifyEvent;
property SecondaryShortCuts: TCustomShortCutList;
property ShortCut: TShortCut;
property Visible: Boolean;

## TActionLink
继承：TActionLink → TContainedActionLink → TContainedActionLink ｜ 单元：Vcl.ActnList


## TActionList
继承：TActionList → TCustomActionList → TContainedActionList ｜ 单元：Vcl.ActnList

property Images: TCustomImageList;
property OnChange: TNotifyEvent;
property OnExecute: TActionEvent;
property OnStateChange: TNotifyEvent;
property OnUpdate: TActionEvent;
property State: TActionListState;

## TADOBlobStream
继承：TADOBlobStream → TMemoryStream → TCustomMemoryStream → TStream → TObject ｜ 单元：Data.Win.ADODB

procedure Create(Field: TBlobField; Mode: TBlobStreamMode);
procedure Truncate;

## TADOCommand
继承：TADOCommand → TComponent → TPersistent → TObject ｜ 单元：Data.Win.ADODB

property CommandObject: _Command;  // read-only
property CommandText: WideString;
property CommandTimeout: Integer;
property CommandType: TCommandType;
property Connection: TADOConnection;
property ConnectionString: WideString;
property ExecuteOptions: TExecuteOptions;
property ParamCheck: Boolean;
property Parameters: TParameters;
property Prepared: WordBool;
property Properties: Properties;  // read-only
property States: TObjectStates;  // read-only
procedure Cancel;
function Execute: _Recordset;
procedure Initialize(DoAppend: Boolean);
procedure OpenConnection;
procedure SetCommandText(const Value: WideString);
function SetConnectionFlag(Flag: Integer; Value: Boolean): Boolean;

## TADOConnection
继承：TADOConnection → TCustomConnection → TComponent → TPersistent → TObject ｜ 单元：Data.Win.ADODB

property AfterConnect: TNotifyEvent;
property AfterDisconnect: TNotifyEvent;
property Attributes: TXactAttributes;
property BeforeConnect: TNotifyEvent;
property BeforeDisconnect: TNotifyEvent;
property CommandCount: Integer;  // read-only
property Commands[Index: ?]: TADOCommand;  // read-only
property CommandTimeout: Integer;
property Connected: Boolean;
property ConnectionObject: _Connection;
property ConnectionString: WideString;
property ConnectionTimeout: Integer;
property ConnectOptions: TConnectOption;
property CursorLocation: TCursorLocation;
property DataSets[Index: ?]: TCustomADODataSet;  // read-only
property DefaultDatabase: WideString;
property Errors: Errors;  // read-only
property InTransaction: Boolean;  // read-only
property IsolationLevel: TIsolationLevel;
property KeepConnection: Boolean;
property LoginPrompt: Boolean;
property Mode: TConnectMode;
property OnBeginTransComplete: TBeginTransCompleteEvent;
property OnCommitTransComplete: TConnectErrorEvent;
property OnConnectComplete: TConnectErrorEvent;
property OnDisconnect: TDisconnectEvent;
property OnExecuteComplete: TExecuteCompleteEvent;
property OnInfoMessage: TInfoMessageEvent;
property OnLogin: TLoginEvent;
property OnRollbackTransComplete: TConnectErrorEvent;
property OnWillConnect: TWillConnectEvent;
property OnWillExecute: TWillExecuteEvent;
property Properties: Properties;  // read-only
property Provider: WideString;
property State: TObjectStates;  // read-only
property Version: WideString;  // read-only
function BeginTrans: Integer;
procedure Cancel;
procedure CheckDisconnect;
procedure CommitTrans;
procedure GetFieldNames(const TableName: string; List: TStrings);
procedure GetProcedureNames(List: TStrings);
procedure GetTableNames(List: TStrings; SystemTables: Boolean);
procedure Open(const UserID: WideString; const Password: WideString);
procedure OpenSchema(const Schema: TSchemaInfo; const Restrictions: OleVariant; const SchemaID: OleVariant; DataSet: TADODataSet);
procedure RollbackTrans;
procedure WaitForConnectComplete;

## TADODataSet
继承：TADODataSet → TCustomADODataSet → TDataSet → TComponent → TPersistent → TObject ｜ 单元：Data.Win.ADODB

property AfterCancel: TDataSetNotifyEvent;
property AfterClose: TDataSetNotifyEvent;
property AfterDelete: TDataSetNotifyEvent;
property AfterEdit: TDataSetNotifyEvent;
property AfterInsert: TDataSetNotifyEvent;
property AfterOpen: TDataSetNotifyEvent;
property AfterPost: TDataSetNotifyEvent;
property AfterScroll: TDataSetNotifyEvent;
property BeforeCancel: TDataSetNotifyEvent;
property BeforeClose: TDataSetNotifyEvent;
property BeforeDelete: TDataSetNotifyEvent;
property BeforeEdit: TDataSetNotifyEvent;
property BeforeInsert: TDataSetNotifyEvent;
property BeforeOpen: TDataSetNotifyEvent;
property BeforePost: TDataSetNotifyEvent;
property BeforeScroll: TDataSetNotifyEvent;
property CommandText: WideString;
property CommandTimeout: Integer;
property CommandType: TCommandType;
property DataSetField: TDataSetField;
property DataSource: TDataSource;
property EnableBCD: Boolean;
property FieldDefs: TFieldDefs;
property IndexDefs: TIndexDefs;
property IndexFieldNames: string;
property IndexName: WideString;
property MasterFields: WideString;
property OnCalcFields: TDataSetNotifyEvent;
property OnDeleteError: TDataSetErrorEvent;
property OnEditError: TDataSetErrorEvent;
property OnNewRecord: TDataSetNotifyEvent;
property OnPostError: TDataSetErrorEvent;
property ParamCheck: Boolean;
property Parameters: TParameters;
property Prepared: Boolean;
property RDSConnection: TRDSConnection;
property StoreDefs: Boolean;
procedure CreateDataSet;
procedure GetIndexNames(List: TStrings);

## TADOQuery
继承：TADOQuery → TCustomADODataSet → TDataSet → TComponent → TPersistent → TObject ｜ 单元：Data.Win.ADODB

property CommandTimeout: Integer;
property DataSource: TDataSource;
property EnableBCD: Boolean;
property ParamCheck: Boolean;
property Parameters: TParameters;
property Prepared: Boolean;
property RowsAffected: Integer;  // read-only
property SQL: TStrings;
function ExecSQL: Integer;

## TADOStoredProc
继承：TADOStoredProc → TCustomADODataSet → TDataSet → TComponent → TPersistent → TObject ｜ 单元：Data.Win.ADODB

property CommandTimeout: Integer;
property DataSource: TDataSource;
property EnableBCD: Boolean;
property Parameters: TParameters;
property Prepared: Boolean;
property ProcedureName: WideString;
procedure ExecProc;

## TADOTable
继承：TADOTable → TCustomADODataSet → TDataSet → TComponent → TPersistent → TObject ｜ 单元：Data.Win.ADODB

property CommandTimeout: Integer;
property EnableBCD: Boolean;
property IndexDefs: TIndexDefs;
property IndexFieldNames: string;
property IndexName: WideString;
property MasterFields: WideString;
property MasterSource: TDataSource;
property ReadOnly: Boolean;
property TableDirect: Boolean;
property TableName: WideString;
procedure GetIndexNames(List: TStrings);

## TADTField
继承：TADTField → TObjectField → TField → TComponent → TPersistent → TObject ｜ 单元：Data.DB


## TAggregatedObject
继承：TAggregatedObject → TObject ｜ 单元：System

property Controller: IInterface;  // read-only
procedure Create(const Controller: IInterface);

## TAggregateField
继承：TAggregateField → TField → TComponent → TPersistent → TObject ｜ 单元：Data.DB

property Active: Boolean;
property currency: Boolean;
property DisplayFormat: string;
property DisplayName: string;
property Expression: string;
property FieldKind: TFieldKind;
property GroupingLevel: Integer;
property Handle: TAggHandle;
property IndexName: string;
property Precision: Integer;
property ResultType: TFieldType;
property Visible: Boolean;

## TAltiumPortalNotification
继承：TAltiumPortalNotification → TNotificationWithCode → TInterfacedObject → TObject ｜ 单元：RT_ClientServerInterface

procedure Create(ACode: Integer; const AApplicationName: string; const AParameterList: IInterfaceList);

## TAnimate
继承：TAnimate → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.ComCtrls

property Active: Boolean;
property Align: TAlign;
property Anchors: TAnchors;
property AutoSize: Boolean;
property BorderWidth: TBorderWidth;
property Center: Boolean;
property Color: TColor;
property CommonAVI: TCommonAVI;
property Constraints: TSizeConstraints;
property DoubleBuffered: Boolean;
property FileName: string;
property FrameCount: Integer;  // read-only
property FrameHeight: Integer;  // read-only
property FrameWidth: Integer;  // read-only
property OnClose: TNotifyEvent;
property OnGesture: TGestureEvent;
property OnOpen: TNotifyEvent;
property OnStart: TNotifyEvent;
property OnStop: TNotifyEvent;
property Open: Boolean;
property ParentColor: Boolean;
property ParentDoubleBuffered: Boolean;
property ParentShowHint: Boolean;
property Repetitions: Integer;
property ResHandle: THandle;
property ResId: Integer;
property ResName: String;
property ShowHint: Boolean;
property StartFrame: SmallInt;
property StopFrame: SmallInt;
property Timers: Boolean;
property Touch: TTouchManager;
property Transparent: Boolean;
property Visible: Boolean;
procedure DoClose;
procedure DoOpen;
procedure DoStart;
procedure DoStop;
procedure Play(FromFrame: Word; ToFrame: Word; Count: Integer);
procedure Reset;
procedure Seek(Frame: SmallInt);
procedure Stop;

## TApplication
继承：TApplication → TComponent → TPersistent → TObject ｜ 单元：Vcl.Forms

property ActionUpdateDelay: Integer;
property Active: Boolean;  // read-only
property ActiveFormHandle: HWND;  // read-only
property AllowTesting: Boolean;
property AutoDragDocking: Boolean;
property BiDiKeyboard: String;
property BiDiMode: TBiDiMode;
property CurrentHelpFile: String;  // read-only
property DefaultFont: TFont;
property DialogHandle: HWND;
property EnumAllWindowsOnActivateHint: Boolean;
property ExeName: String;  // read-only
property Handle: HWND;
property HelpFile: String;
property HelpSystem: IHelpSystem;  // read-only
property Hint: String;
property HintColor: TColor;
property HintHidePause: Integer;
property HintPause: Integer;
property HintShortCuts: Boolean;
property HintShortPause: Integer;
property Icon: TIcon;
property IsMetropolisUI: Boolean;  // read-only
property MainForm: TForm;  // read-only
property MainFormHandle: HWND;  // read-only
property MainFormOnTaskBar: Boolean;
property ModalLevel: Integer;  // read-only
property ModalPopupMode: TPopupMode;
property NonBiDiKeyboard: String;
property PopupControlWnd: HWND;  // read-only
property ShowHint: Boolean;
property ShowMainForm: Boolean;
property Terminated: Boolean;  // read-only
property Title: String;
property UpdateFormatSettings: Boolean;
property UpdateMetricSettings: Boolean;
procedure ActivateHint(const CursorPos: IDispatch);
function AddPopupForm(APopupForm: TCustomForm): Integer;
procedure ApplyBiDiKeyboardLayout;
procedure ApplyNonBiDiKeyboardLayout;
procedure BringToFront;
procedure CancelHint;
procedure ControlDestroyed(Control: TControl);
procedure CreateHandle;
procedure DoApplicationIdle;
function ExecuteAction(Action: TBasicAction): Boolean;
procedure HandleException(Sender: TObject);
procedure HandleMessage;
function HelpCommand(Command: Integer; Data: NativeInt): Boolean;
function HelpContext(Context: THelpContext): Boolean;
function HelpJump(const JumpID: string): Boolean;
function HelpKeyword(const Keyword: string): Boolean;
function HelpShowTableOfContents: Boolean;
procedure HideHint;
procedure HintMouseMessage(Control: TControl; const Message: IDispatch);
procedure HookSynchronizeWakeup;
procedure Initialize;
function IsRightToLeft: Boolean;
function MessageBox(const Text: PWideChar; const Caption: PWideChar; Flags: Integer): Integer;
procedure Minimize;
procedure ModalFinished;
procedure ModalStarted;
procedure NormalizeAllTopMosts;
procedure NormalizeTopMosts;
procedure ProcessMessages;
procedure RemovePopupForm(APopupForm: TCustomForm);
procedure Restore;
procedure RestoreTopMosts;
procedure Run;
procedure ShowException(E: Exception);
procedure Terminate;
procedure UnhookSynchronizeWakeup;
function UpdateAction(Action: TBasicAction): Boolean;
procedure UseMetropolisUI;
function UseRightToLeftAlignment: Boolean;
function UseRightToLeftReading: Boolean;
function UseRightToLeftScrollBar: Boolean;

## TArrayField
继承：TArrayField → TObjectField → TField → TComponent → TPersistent → TObject ｜ 单元：Data.DB

property Size: Integer;

## TAutoDisconnectExternalFormRefCount
继承：TAutoDisconnectExternalFormRefCount → TExternalFormComponentRefCount → TExternalFormComponent → TPanel → TCustomPanel → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：ExternalForm


## TAutoIncField
继承：TAutoIncField → TIntegerField → TNumericField → TField → TComponent → TPersistent → TObject ｜ 单元：Data.DB


## TBalloonHint
继承：TBalloonHint → TCustomHint → TComponent → TPersistent → TObject ｜ 单元：Vcl.Controls


## TBaseAsyncResult
继承：TBaseAsyncResult → TInterfacedObject → TObject ｜ 单元：System.Classes

procedure AsyncDispatch;
procedure Complete;
procedure Create;
procedure Dispatch(const AsyncResult: TBaseAsyncResult);
function Invoke: IAsyncResult;
procedure Schedule;
procedure WaitForCompletion;

## TBaseDIOSignal
继承：TBaseDIOSignal → TInterfacedObject → TObject ｜ 单元：RT_BaseDIO

property InternalValue: TSignalValueType;
property IsInput: Boolean;  // read-only
property Name: WideString;  // read-only
property Value: TSignalValueType;
property Width: Integer;  // read-only
function Clone: TBaseDIOSignal;
procedure Create(const AName: string; AWidth: Integer; AInitValue: Cardinal; AIsInput: Boolean);
procedure ExportTo_ParamString(AIndex: Integer; var AParamString: string);
function GetValue: Cardinal;
procedure ImportFrom_ParamString(AIndex: Integer; const AParamString: string);
function IsEqualTo(AnotherSignal: TBaseDIOSignal): Boolean;
procedure SetValue(AValue: Cardinal);

## TBaseDragControlObject
继承：TBaseDragControlObject → TDragObject → TObject ｜ 单元：Vcl.Controls

property Control: TControl;
procedure Create(AControl: TControl);
procedure EndDrag(Target: TObject; X: Integer; Y: Integer);

## TBaseNavigator
继承：TBaseNavigator → TCustomPanel → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.Buttons

property Align: TAlign;
property Anchors: TAnchors;
property ConfirmDelete: Boolean;
property Constraints: TSizeConstraints;
property Ctl3D: Boolean;
property DragCursor: TCursor;
property DragKind: TDragKind;
property DragMode: TDragMode;
property Enabled: Boolean;
property Flat: Boolean;
property Orientation: TOrientation;
property ParentCtl3D: Boolean;
property ParentShowHint: Boolean;
property PopupMenu: TPopupMenu;
property ShowHint: Boolean;
property TabOrder: TTabOrder;
property TabStop: Boolean;
property Visible: Boolean;
procedure BtnIDClick(Index: Integer);
procedure EnabledChanged;
procedure SetButtonGlyph(Index: Integer);

## TBaseXPSpinEdit
继承：TBaseXPSpinEdit → TCustomXPEdit → TXPCustomControl → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：XPEdits2

property Button: TXPUpDown;  // read-only
procedure InternalCheckAndSetValue;
procedure InternalDecrementValue;
procedure InternalIncrementValue;
function IsValidChar(Key: Char): Boolean;
procedure SetButtonVisibility;

## TBasicAction
继承：TBasicAction → TComponent → TPersistent → TObject ｜ 单元：System.Classes

property ActionComponent: TComponent;
procedure Change;
function Execute: Boolean;
procedure ExecuteTarget(Target: TObject);
function HandlesTarget(Target: TObject): Boolean;
procedure RegisterChanges(const Value: TBasicActionLink);
function Suspended: Boolean;
procedure UnRegisterChanges(const Value: TBasicActionLink);
function Update: Boolean;
procedure UpdateTarget(Target: TObject);

## TBasicActionLink
继承：TBasicActionLink → TObject ｜ 单元：System.Classes

property Action: TBasicAction;
procedure AssignClient(AClient: TObject);
procedure Change;
procedure Create(AClient: TObject);
function Execute(AComponent: TComponent): Boolean;
function IsOnExecuteLinked: Boolean;
procedure SetAction(Value: TBasicAction);
function Update: Boolean;

## TBCDField
继承：TBCDField → TNumericField → TField → TComponent → TPersistent → TObject ｜ 单元：Data.DB

property currency: Boolean;
property MaxValue: Currency;
property MinValue: Currency;
property Precision: Integer;
property Size: Integer;
property Value: Currency;

## TBevel
继承：TBevel → TGraphicControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.ExtCtrls

property Align: TAlign;
property Anchors: TAnchors;
property Constraints: TSizeConstraints;
property OnGesture: TGestureEvent;
property ParentShowHint: Boolean;
property Shape: TBevelShape;
property ShowHint: Boolean;
property Style: TBevelStyle;
property Touch: TTouchManager;
property Visible: Boolean;

## TBinaryField
继承：TBinaryField → TField → TComponent → TPersistent → TObject ｜ 单元：Data.DB

property Size: Integer;

## TBinaryReader
继承：TBinaryReader → TObject ｜ 单元：System.Classes

property BaseStream: TStream;  // read-only
procedure Close;
procedure Create(Stream: TStream; AEncoding: TEncoding; AOwnsStream: Boolean);
function GetBaseStream: TStream;
function PeekChar: Integer;
function Read: Integer;
function Read7BitEncodedInt: Integer;
function ReadBoolean: Boolean;
function ReadByte: Byte;
function ReadCardinal: Cardinal;
function ReadChar: Char;
function ReadDouble: Double;
function ReadInt16: SmallInt;
function ReadInt32: Integer;
function ReadInt64: Int64;
function ReadInteger: Integer;
function ReadSByte: ShortInt;
function ReadShortInt: ShortInt;
function ReadSingle: Single;
function ReadSmallInt: SmallInt;
function ReadString: string;
function ReadUInt16: Word;
function ReadUInt32: Cardinal;
function ReadUInt64: UInt64;
function ReadWord: Word;

## TBinaryWriter
继承：TBinaryWriter → TObject ｜ 单元：System.Classes

property BaseStream: TStream;  // read-only
property Null: TBinaryWriter;  // read-only
procedure Close;
procedure Create(Stream: TStream);
function GetBaseStream: TStream;
function Seek(const Offset: Int64; Origin: TSeekOrigin): Int64;
procedure Write(Value: Byte);
procedure Write7BitEncodedInt(Value: Integer);

## TBitBtn
继承：TBitBtn → TCustomButton → TButtonControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.Buttons

property Action: TBasicAction;
property Align: TAlign;
property Anchors: TAnchors;
property BiDiMode: TBiDiMode;
property Cancel: Boolean;
property Caption: TCaption;
property Constraints: TSizeConstraints;
property Default: Boolean;
property DoubleBuffered: Boolean;
property DragCursor: TCursor;
property DragKind: TDragKind;
property DragMode: TDragMode;
property Enabled: Boolean;
property Font: TFont;
property Glyph: TBitmap;
property Kind: TBitBtnKind;
property Layout: TButtonLayout;
property Margin: Integer;
property ModalResult: TModalResult;
property NumGlyphs: TNumGlyphs;
property OnClick: TNotifyEvent;
property OnContextPopup: TContextPopupEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnEndDock: TEndDragEvent;
property OnEndDrag: TEndDragEvent;
property OnEnter: TNotifyEvent;
property OnExit: TNotifyEvent;
property OnKeyDown: TKeyEvent;
property OnKeyPress: TKeyPressEvent;
property OnKeyUp: TKeyEvent;
property OnMouseActivate: TMouseActivateEvent;
property OnMouseDown: TMouseEvent;
property OnMouseEnter: TNotifyEvent;
property OnMouseLeave: TNotifyEvent;
property OnMouseMove: TMouseMoveEvent;
property OnMouseUp: TMouseEvent;
property OnStartDock: TStartDockEvent;
property OnStartDrag: TStartDragEvent;
property ParentBiDiMode: Boolean;
property ParentDoubleBuffered: Boolean;
property ParentFont: Boolean;
property ParentShowHint: Boolean;
property PopupMenu: TPopupMenu;
property ShowHint: Boolean;
property Spacing: Integer;
property Style: TButtonStyle;
property StyleElements: TStyleElements;
property TabOrder: TTabOrder;
property TabStop: Boolean;
property Visible: Boolean;
property WordWrap: Boolean;

## TBitBtnActionLink
继承：TBitBtnActionLink → TControlActionLink → TActionLink → TContainedActionLink ｜ 单元：Vcl.Buttons


## TBitBtnStyleHook
继承：TBitBtnStyleHook → TButtonStyleHook → TMouseTrackControlStyleHook ｜ 单元：Vcl.Buttons


## TBitConverter
继承：TBitConverter → TObject ｜ 单元：System.Types


## TBitmap
继承：TBitmap → TGraphic → TInterfacedPersistent → TPersistent → TObject ｜ 单元：Vcl.Graphics

property AlphaFormat: TAlphaFormat;
property Canvas: TCanvas;  // read-only
property Handle: HBITMAP;
property HandleType: TBitmapHandleType;
property IgnorePalette: Boolean;
property MaskHandle: HBITMAP;
property Monochrome: Boolean;
property PixelFormat: TPixelFormat;
property ScanLine[Index: ?]: Pointer;  // read-only
property TransparentColor: TColor;
property TransparentMode: TTransparentMode;
procedure Dormant;
procedure FreeImage;
function GetHandle: HBITMAP;
function GetMaskHandle: HBITMAP;
function HandleAllocated: Boolean;
procedure LoadFromResourceID(Instance: NativeUInt; ResID: Integer);
procedure LoadFromResourceName(Instance: NativeUInt; const ResName: string);
procedure Mask(TransparentColor: TColor);
function ReleaseHandle: HBITMAP;
function ReleaseMaskHandle: HBITMAP;
function ReleasePalette: HPALETTE;
procedure SetHandleType(Value: TBitmapHandleType);

## TBitmapImage
继承：TBitmapImage → TSharedImage → TObject ｜ 单元：Vcl.Graphics


## TBits
继承：TBits → TObject ｜ 单元：System.Classes

property Bits[Index: ?]: Boolean;
property Size: Integer;
function OpenBit: Integer;

## TBlobField
继承：TBlobField → TField → TComponent → TPersistent → TObject ｜ 单元：Data.DB

property BlobSize: Integer;  // read-only
property BlobType: TBlobType;
property GraphicHeader: Boolean;
property Modified: Boolean;
property Size: Integer;
property Transliterate: Boolean;
function GetBlobSize: Integer;
procedure LoadFromFile(const FileName: string);
procedure LoadFromStream(Stream: TStream);
procedure SaveToFile(const FileName: string);
procedure SaveToStream(Stream: TStream);

## TBooleanField
继承：TBooleanField → TField → TComponent → TPersistent → TObject ｜ 单元：Data.DB

property DisplayValues: string;
property Value: Boolean;

## TBoundLabel
继承：TBoundLabel → TCustomLabel → TGraphicControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.ExtCtrls

property BiDiMode: TBiDiMode;
property Caption: TCaption;
property Color: TColor;
property DragCursor: TCursor;
property DragKind: TDragKind;
property DragMode: TDragMode;
property Font: TFont;
property Height: Integer;
property Layout: TTextLayout;
property Left: Integer;  // read-only
property OnClick: TNotifyEvent;
property OnContextPopup: TContextPopupEvent;
property OnDblClick: TNotifyEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnEndDock: TEndDragEvent;
property OnEndDrag: TEndDragEvent;
property OnGesture: TGestureEvent;
property OnMouseActivate: TMouseActivateEvent;
property OnMouseDown: TMouseEvent;
property OnMouseMove: TMouseMoveEvent;
property OnMouseUp: TMouseEvent;
property OnStartDock: TStartDockEvent;
property OnStartDrag: TStartDragEvent;
property ParentBiDiMode: Boolean;
property ParentColor: Boolean;
property ParentFont: Boolean;
property ParentShowHint: Boolean;
property PopupMenu: TPopupMenu;
property ShowAccelChar: Boolean;
property ShowHint: Boolean;
property Top: Integer;  // read-only
property Touch: TTouchManager;
property Transparent: Boolean;
property Width: Integer;
property WordWrap: Boolean;

## TBreakpoint
继承：TBreakpoint → TInterfacedObject → TObject ｜ 单元：RT_Debugger

procedure Create(aFileName: WideString; aLine: Integer; aManager: IDebugger);
function GetEnabled: Boolean;
function GetFileName: WideString;
function GetLine: Integer;
function GetValid: Boolean;
procedure SetEnabled(anEnabled: Boolean);
procedure SetFileName(aFileName: WideString);
procedure SetFocus;
procedure SetLine(aLine: Integer);
procedure SetValid(aValid: Boolean);

## TBrowseForFolder
继承：TBrowseForFolder → TCommonDialogAction → TCustomAction → TContainedAction ｜ 单元：Vcl.StdActns

property BeforeExecute: TNotifyEvent;
property BrowseOptions: TBrowseOptions;
property BrowseOptionsEx: TBrowseOptionsEx;
property Caption: string;
property DialogCaption: string;
property Enabled: Boolean;
property Folder: String;
property FolderNameLabel: string;
property Folders[Index: ?]: String;  // read-only
property HelpContext: THelpContext;
property HelpKeyword: string;
property HelpType: THelpType;
property Hint: string;
property ImageIndex: TImageIndex;
property OkButtonLabel: string;
property OnAccept: TNotifyEvent;
property OnCallback: TBrowseForFolderCallbackEvent;
property OnCancel: TNotifyEvent;
property OnHint: THintEvent;
property OnValidate: TBrowseForFolderCallbackEvent;
property RootDir: string;
property SecondaryShortCuts: TCustomShortCutList;
property SelectionCount: Integer;  // read-only
property ShortCut: TShortCut;
property UseFileDialog: Boolean;
property Visible: Boolean;

## TBrush
继承：TBrush → TGraphicsObject → TPersistent → TObject ｜ 单元：Vcl.Graphics

property Bitmap: TBitmap;
property Color: TColor;
property Handle: HBrush;
property Style: TBrushStyle;
procedure Create;

## TBrushRecall
继承：TBrushRecall → TRecall → TObject ｜ 单元：Vcl.Graphics

procedure Create(ABrush: TBrush);

## TBucketList
继承：TBucketList → TCustomBucketList → TObject ｜ 单元：System.Contnrs

procedure Create(ABuckets: TBucketListSizes);

## TButton
继承：TButton → TCustomButton → TButtonControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.StdCtrls

property Action: TBasicAction;
property Align: TAlign;
property Anchors: TAnchors;
property BiDiMode: TBiDiMode;
property Cancel: Boolean;
property Caption: TCaption;
property CommandLinkHint: string;
property Constraints: TSizeConstraints;
property Default: Boolean;
property DisabledImageIndex: TImageIndex;
property DoubleBuffered: Boolean;
property DragCursor: TCursor;
property DragKind: TDragKind;
property DragMode: TDragMode;
property DropDownMenu: TPopupMenu;
property ElevationRequired: Boolean;
property Enabled: Boolean;
property Font: TFont;
property HotImageIndex: TImageIndex;
property ImageAlignment: TImageAlignment;
property ImageIndex: TImageIndex;
property ImageMargins: TImageMargins;
property Images: TCustomImageList;
property ModalResult: TModalResult;
property OnClick: TNotifyEvent;
property OnContextPopup: TContextPopupEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnDropDownClick: TNotifyEvent;
property OnEndDock: TEndDragEvent;
property OnEndDrag: TEndDragEvent;
property OnEnter: TNotifyEvent;
property OnExit: TNotifyEvent;
property OnKeyDown: TKeyEvent;
property OnKeyPress: TKeyPressEvent;
property OnKeyUp: TKeyEvent;
property OnMouseActivate: TMouseActivateEvent;
property OnMouseDown: TMouseEvent;
property OnMouseEnter: TNotifyEvent;
property OnMouseLeave: TNotifyEvent;
property OnMouseMove: TMouseMoveEvent;
property OnMouseUp: TMouseEvent;
property OnStartDock: TStartDockEvent;
property OnStartDrag: TStartDragEvent;
property ParentBiDiMode: Boolean;
property ParentDoubleBuffered: Boolean;
property ParentFont: Boolean;
property ParentShowHint: Boolean;
property PopupMenu: TPopupMenu;
property PressedImageIndex: TImageIndex;
property SelectedImageIndex: TImageIndex;
property ShowHint: Boolean;
property Style: TCustomButton.TButtonStyle;
property StyleElements: TStyleElements;
property StylusHotImageIndex: TImageIndex;
property TabOrder: TTabOrder;
property TabStop: Boolean;
property Visible: Boolean;
property WordWrap: Boolean;

## TButtonActionLink
继承：TButtonActionLink → TWinControlActionLink → TControlActionLink → TActionLink → TContainedActionLink ｜ 单元：Vcl.StdCtrls


## TButtonControl
继承：TButtonControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.StdCtrls

function GetChecked: Boolean;
procedure SetChecked(Value: Boolean);

## TButtonedEdit
继承：TButtonedEdit → TCustomButtonedEdit → TCustomEdit → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.ExtCtrls

property Align: TAlign;
property Alignment: TAlignment;
property Anchors: TAnchors;
property AutoSelect: Boolean;
property AutoSize: Boolean;
property BevelEdges: TBevelEdges;
property BevelInner: TBevelCut;
property BevelKind: TBevelKind;
property BevelOuter: TBevelCut;
property BevelWidth: TBevelWidth;
property BiDiMode: TBiDiMode;
property BorderStyle: TBorderStyle;
property CharCase: TEditCharCase;
property Color: TColor;
property Constraints: TSizeConstraints;
property Ctl3D: Boolean;
property DoubleBuffered: Boolean;
property DragCursor: TCursor;
property DragKind: TDragKind;
property DragMode: TDragMode;
property Enabled: Boolean;
property Font: TFont;
property HideSelection: Boolean;
property Images: TCustomImageList;
property ImeMode: TImeMode;
property ImeName: TImeName;
property LeftButton: TEditButton;
property MaxLength: Integer;
property NumbersOnly: Boolean;
property OEMConvert: Boolean;
property OnChange: TNotifyEvent;
property OnClick: TNotifyEvent;
property OnContextPopup: TContextPopupEvent;
property OnDblClick: TNotifyEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnEndDock: TEndDragEvent;
property OnEndDrag: TEndDragEvent;
property OnEnter: TNotifyEvent;
property OnExit: TNotifyEvent;
property OnGesture: TGestureEvent;
property OnKeyDown: TKeyEvent;
property OnKeyPress: TKeyPressEvent;
property OnKeyUp: TKeyEvent;
property OnLeftButtonClick: TNotifyEvent;
property OnMouseActivate: TMouseActivateEvent;
property OnMouseDown: TMouseEvent;
property OnMouseEnter: TNotifyEvent;
property OnMouseLeave: TNotifyEvent;
property OnMouseMove: TMouseMoveEvent;
property OnMouseUp: TMouseEvent;
property OnRightButtonClick: TNotifyEvent;
property OnStartDock: TStartDockEvent;
property OnStartDrag: TStartDragEvent;
property ParentBiDiMode: Boolean;
property ParentColor: Boolean;
property ParentCtl3D: Boolean;
property ParentDoubleBuffered: Boolean;
property ParentFont: Boolean;
property ParentShowHint: Boolean;
property PasswordChar: Char;
property PopupMenu: TPopupMenu;
property ReadOnly: Boolean;
property RightButton: TEditButton;
property ShowHint: Boolean;
property StyleElements: TStyleElements;
property TabOrder: TTabOrder;
property TabStop: Boolean;
property Text: TCaption;
property TextHint: string;
property Touch: TTouchManager;
property Visible: Boolean;

## TButtonStyleHook
继承：TButtonStyleHook → TMouseTrackControlStyleHook → TMouseTrackControlStyleHook ｜ 单元：Vcl.StdCtrls


## TByteField
继承：TByteField → TIntegerField → TNumericField → TField → TComponent → TPersistent → TObject ｜ 单元：Data.DB


## TBytesField
继承：TBytesField → TBinaryField → TField → TComponent → TPersistent → TObject ｜ 单元：Data.DB


## TBytesStream
继承：TBytesStream → TMemoryStream → TCustomMemoryStream → TStream → TObject ｜ 单元：System.Classes

procedure Create(const ABytes: TArray<System.Byte>);

## TCanvas
继承：TCanvas → TCustomCanvas → TPersistent → TObject ｜ 单元：Vcl.Graphics

property Brush: TBrush;
property CopyMode: Integer;
property Font: TFont;
property Handle: HDC;
property Pen: TPen;
procedure CopyRect(const Dest: IDispatch; Canvas: TCanvas; const Source: IDispatch);
procedure Create;
procedure CreateHandle;
function HandleAllocated: Boolean;

## TCategoryPanel
继承：TCategoryPanel → TCustomCategoryPanel → TCustomPanel → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.ExtCtrls

property BiDiMode: TBiDiMode;
property Caption: TCaption;
property Collapsed: Boolean;
property CollapsedHotImageIndex: TImageIndex;
property CollapsedImageIndex: TImageIndex;
property CollapsedPressedImageIndex: TImageIndex;
property Color: TColor;
property Ctl3D: Boolean;
property DockSite: Boolean;
property DoubleBuffered: Boolean;
property DragCursor: TCursor;
property DragKind: TDragKind;
property DragMode: TDragMode;
property Enabled: Boolean;
property ExpandedHotImageIndex: TImageIndex;
property ExpandedImageIndex: TImageIndex;
property ExpandedPressedImageIndex: TImageIndex;
property Font: TFont;
property FullRepaint: Boolean;
property Height: Integer;
property Left: Integer;
property Locked: Boolean;
property OnClick: TNotifyEvent;
property OnCollapse: TNotifyEvent;
property OnContextPopup: TContextPopupEvent;
property OnDblClick: TNotifyEvent;
property OnDockDrop: TDockDropEvent;
property OnDockOver: TDockOverEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnEndDock: TEndDragEvent;
property OnEndDrag: TEndDragEvent;
property OnEnter: TNotifyEvent;
property OnExit: TNotifyEvent;
property OnExpand: TNotifyEvent;
property OnGesture: TGestureEvent;
property OnGetSiteInfo: TGetSiteInfoEvent;
property OnMouseActivate: TMouseActivateEvent;
property OnMouseDown: TMouseEvent;
property OnMouseEnter: TNotifyEvent;
property OnMouseLeave: TNotifyEvent;
property OnMouseMove: TMouseMoveEvent;
property OnMouseUp: TMouseEvent;
property OnStartDock: TStartDockEvent;
property OnStartDrag: TStartDragEvent;
property OnUnDock: TUnDockEvent;
property Padding: TPadding;
property ParentBackground: Boolean;
property ParentBiDiMode: Boolean;
property ParentColor: Boolean;
property ParentCtl3D: Boolean;
property ParentDoubleBuffered: Boolean;
property ParentFont: Boolean;
property ParentShowHint: Boolean;
property PopupMenu: TPopupMenu;
property ShowHint: Boolean;
property StyleElements: TStyleElements;
property TabOrder: TTabOrder;
property TabStop: Boolean;
property Touch: TTouchManager;
property UseDockManager: Boolean;
property Visible: Boolean;
property Width: Integer;

## TCategoryPanelGroup
继承：TCategoryPanelGroup → TCustomCategoryPanelGroup → TScrollingWinControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.ExtCtrls

property Align: TAlign;
property Anchors: TAnchors;
property BevelEdges: TBevelEdges;
property BevelInner: TBevelCut;
property BevelKind: TBevelKind;
property BevelOuter: TBevelCut;
property BevelWidth: TBevelWidth;
property BiDiMode: TBiDiMode;
property ChevronAlignment: TAlignment;
property ChevronColor: TColor;
property ChevronHotColor: TColor;
property Color: TColor;
property Constraints: TSizeConstraints;
property Ctl3D: Boolean;
property DockSite: Boolean;
property DoubleBuffered: Boolean;
property DragCursor: TCursor;
property DragKind: TDragKind;
property DragMode: TDragMode;
property Enabled: Boolean;
property Font: TFont;
property GradientBaseColor: TColor;
property GradientColor: TColor;
property GradientDirection: TGradientDirection;
property HeaderAlignment: TAlignment;
property HeaderFont: TFont;
property HeaderHeight: Integer;
property HeaderImage: TPicture;
property HeaderStyle: TCustomCategoryPanelGroup.THeaderStyle;
property Height: Integer;
property Images: TCustomImageList;
property OnCanResize: TCanResizeEvent;
property OnClick: TNotifyEvent;
property OnConstrainedResize: TConstrainedResizeEvent;
property OnContextPopup: TContextPopupEvent;
property OnDblClick: TNotifyEvent;
property OnDockDrop: TDockDropEvent;
property OnDockOver: TDockOverEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnEndDock: TEndDragEvent;
property OnEndDrag: TEndDragEvent;
property OnEnter: TNotifyEvent;
property OnExit: TNotifyEvent;
property OnGesture: TGestureEvent;
property OnGetSiteInfo: TGetSiteInfoEvent;
property OnMouseActivate: TMouseActivateEvent;
property OnMouseDown: TMouseEvent;
property OnMouseEnter: TNotifyEvent;
property OnMouseLeave: TNotifyEvent;
property OnMouseMove: TMouseMoveEvent;
property OnMouseUp: TMouseEvent;
property OnMouseWheel: TMouseWheelEvent;
property OnMouseWheelDown: TMouseWheelUpDownEvent;
property OnMouseWheelUp: TMouseWheelUpDownEvent;
property OnResize: TNotifyEvent;
property OnStartDock: TStartDockEvent;
property OnStartDrag: TStartDragEvent;
property OnUnDock: TUnDockEvent;
property Padding: TPadding;
property ParentBackground: Boolean;
property ParentBiDiMode: Boolean;
property ParentColor: Boolean;
property ParentCtl3D: Boolean;
property ParentDoubleBuffered: Boolean;
property ParentFont: Boolean;
property ParentShowHint: Boolean;
property PopupMenu: TPopupMenu;
property ShowHint: Boolean;
property StyleElements: TStyleElements;
property TabOrder: TTabOrder;
property TabStop: Boolean;
property Touch: TTouchManager;
property Visible: Boolean;
property Width: Integer;

## TCategoryPanelSurface
继承：TCategoryPanelSurface → TCustomTransparentControl → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.ExtCtrls


## TCellCollection
继承：TCellCollection → TOwnedCollection → TCollection → TPersistent → TObject ｜ 单元：Vcl.ExtCtrls

property Items[Index: ?]: TCellItem;
function Owner: TCustomGridPanel;

## TCellItem
继承：TCellItem → TCollectionItem → TPersistent → TObject ｜ 单元：Vcl.ExtCtrls

property SizeStyle: TSizeStyle;
property Value: Double;

## TChangeLink
继承：TChangeLink → TImageLink → TImageLink ｜ 单元：Vcl.ImgList

property Sender: TCustomImageList;

## TCheckBox
继承：TCheckBox → TCustomCheckBox → TButtonControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.StdCtrls

property Action: TBasicAction;
property Align: TAlign;
property Alignment: TLeftRight;
property AllowGrayed: Boolean;
property Anchors: TAnchors;
property BiDiMode: TBiDiMode;
property Caption: TCaption;
property Checked: Boolean;
property Color: TColor;
property Constraints: TSizeConstraints;
property Ctl3D: Boolean;
property DoubleBuffered: Boolean;
property DragCursor: TCursor;
property DragKind: TDragKind;
property DragMode: TDragMode;
property Enabled: Boolean;
property Font: TFont;
property OnClick: TNotifyEvent;
property OnContextPopup: TContextPopupEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnEndDock: TEndDragEvent;
property OnEndDrag: TEndDragEvent;
property OnEnter: TNotifyEvent;
property OnExit: TNotifyEvent;
property OnKeyDown: TKeyEvent;
property OnKeyPress: TKeyPressEvent;
property OnKeyUp: TKeyEvent;
property OnMouseActivate: TMouseActivateEvent;
property OnMouseDown: TMouseEvent;
property OnMouseEnter: TNotifyEvent;
property OnMouseLeave: TNotifyEvent;
property OnMouseMove: TMouseMoveEvent;
property OnMouseUp: TMouseEvent;
property OnStartDock: TStartDockEvent;
property OnStartDrag: TStartDragEvent;
property ParentBiDiMode: Boolean;
property ParentColor: Boolean;
property ParentCtl3D: Boolean;
property ParentDoubleBuffered: Boolean;
property ParentFont: Boolean;
property ParentShowHint: Boolean;
property PopupMenu: TPopupMenu;
property ShowHint: Boolean;
property State: TCheckBoxState;
property StyleElements: TStyleElements;
property TabOrder: TTabOrder;
property TabStop: Boolean;
property Visible: Boolean;
property WordWrap: Boolean;

## TCheckBoxStyleHook
继承：TCheckBoxStyleHook → TMouseTrackControlStyleHook → TMouseTrackControlStyleHook ｜ 单元：Vcl.StdCtrls


## TCheckConstraint
继承：TCheckConstraint → TCollectionItem → TPersistent → TObject ｜ 单元：Data.DB

property CustomConstraint: string;
property ErrorMessage: string;
property FromDictionary: Boolean;
property ImportedConstraint: string;

## TCheckConstraints
继承：TCheckConstraints → TCollection → TPersistent → TObject ｜ 单元：Data.DB

property Items[Index: ?]: TCheckConstraint;
function Add: TCheckConstraint;
procedure Create(Owner: TPersistent);

## TCheckListBox
继承：TCheckListBox → TCustomListBox → TCustomMultiSelectListControl → TCustomListControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.CheckLst

property Align: TAlign;
property AllowGrayed: Boolean;
property Anchors: TAnchors;
property AutoComplete: Boolean;
property BevelEdges: TBevelEdges;
property BevelInner: TBevelCut;
property BevelKind: TBevelKind;
property BevelOuter: TBevelCut;
property BevelWidth: TBevelWidth;
property BiDiMode: TBiDiMode;
property BorderStyle: TBorderStyle;
property Checked[Index: ?]: Boolean;
property Color: TColor;
property Columns: Integer;
property Constraints: TSizeConstraints;
property Ctl3D: Boolean;
property DoubleBuffered: Boolean;
property DragCursor: TCursor;
property DragKind: TDragKind;
property DragMode: TDragMode;
property Enabled: Boolean;
property Flat: Boolean;
property Font: TFont;
property Header[Index: ?]: Boolean;
property HeaderBackgroundColor: TColor;
property HeaderColor: TColor;
property ImeMode: TImeMode;
property ImeName: TImeName;
property IntegralHeight: Boolean;
property ItemEnabled[Index: ?]: Boolean;
property ItemHeight: Integer;
property Items: TStrings;
property OnClick: TNotifyEvent;
property OnClickCheck: TNotifyEvent;
property OnContextPopup: TContextPopupEvent;
property OnData: TLBGetDataEvent;
property OnDataFind: TLBFindDataEvent;
property OnDataObject: TLBGetDataObjectEvent;
property OnDblClick: TNotifyEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnDrawItem: TDrawItemEvent;
property OnEndDock: TEndDragEvent;
property OnEndDrag: TEndDragEvent;
property OnEnter: TNotifyEvent;
property OnExit: TNotifyEvent;
property OnGesture: TGestureEvent;
property OnKeyDown: TKeyEvent;
property OnKeyPress: TKeyPressEvent;
property OnKeyUp: TKeyEvent;
property OnMeasureItem: TMeasureItemEvent;
property OnMouseActivate: TMouseActivateEvent;
property OnMouseDown: TMouseEvent;
property OnMouseEnter: TNotifyEvent;
property OnMouseLeave: TNotifyEvent;
property OnMouseMove: TMouseMoveEvent;
property OnMouseUp: TMouseEvent;
property OnStartDock: TStartDockEvent;
property OnStartDrag: TStartDragEvent;
property ParentBiDiMode: Boolean;
property ParentColor: Boolean;
property ParentCtl3D: Boolean;
property ParentDoubleBuffered: Boolean;
property ParentFont: Boolean;
property ParentShowHint: Boolean;
property PopupMenu: TPopupMenu;
property ScrollWidth: Integer;
property ShowHint: Boolean;
property Sorted: Boolean;
property State[Index: ?]: TCheckBoxState;
property Style: TListBoxStyle;
property StyleElements: TStyleElements;
property TabOrder: TTabOrder;
property TabStop: Boolean;
property TabWidth: Integer;
property Touch: TTouchManager;
property Visible: Boolean;
procedure CheckAll(AState: TCheckBoxState; AllowGrayed: Boolean; AllowDisabled: Boolean);
procedure ClickCheck;

## TChunk
继承：TChunk → TObject ｜ 单元：Vcl.Imaging.pngimage

property Data: Pointer;  // read-only
property DataSize: Cardinal;  // read-only
property Header: TChunkIHDR;  // read-only
property Index: Integer;  // read-only
property Name: AnsiString;  // read-only
property Owner: TPngImage;  // read-only
procedure Assign(Source: TChunk);
procedure Create(Owner: TPngImage);
function GetName: string;
procedure ResizeData(const NewSize: Cardinal);
function SaveData(Stream: TStream): Boolean;
function SaveToStream(Stream: TStream): Boolean;

## TChunkgAMA
继承：TChunkgAMA → TChunk → TObject ｜ 单元：Vcl.Imaging.pngimage

property Gamma: Cardinal;

## TChunkIDAT
继承：TChunkIDAT → TChunk → TObject ｜ 单元：Vcl.Imaging.pngimage


## TChunkIEND
继承：TChunkIEND → TChunk → TObject ｜ 单元：Vcl.Imaging.pngimage


## TChunkIHDR
继承：TChunkIHDR → TChunk → TObject ｜ 单元：Vcl.Imaging.pngimage

property Bitdepth: Byte;
property ColorType: Byte;
property CompressionMethod: Byte;
property FilterMethod: Byte;
property Height: Cardinal;
property ImageHandleValue: HBitmap;  // read-only
property InterlaceMethod: Byte;
property Width: Cardinal;

## TChunkpHYs
继承：TChunkpHYs → TChunk → TObject ｜ 单元：Vcl.Imaging.pngimage

property PPUnitX: Cardinal;
property PPUnitY: Cardinal;
property UnitType: TUnitType;

## TChunkPLTE
继承：TChunkPLTE → TChunk → TObject ｜ 单元：Vcl.Imaging.pngimage

property Count: Integer;  // read-only
property Item[Index: ?]: TRGBQuad;  // read-only

## TChunktEXt
继承：TChunktEXt → TChunk → TObject ｜ 单元：Vcl.Imaging.pngimage

property Keyword: AnsiString;
property Text: AnsiString;

## TChunktIME
继承：TChunktIME → TChunk → TObject ｜ 单元：Vcl.Imaging.pngimage

property Day: Byte;
property Hour: Byte;
property Minute: Byte;
property Month: Byte;
property Second: Byte;
property Year: Word;

## TChunktRNS
继承：TChunktRNS → TChunk → TObject ｜ 单元：Vcl.Imaging.pngimage

property BitTransparency: Boolean;  // read-only
property TransparentColor: ColorRef;

## TChunkzTXt
继承：TChunkzTXt → TChunktEXt → TChunk → TObject ｜ 单元：Vcl.Imaging.pngimage


## TClassFinder
继承：TClassFinder → TObject ｜ 单元：System.Classes


## TClassHelperBase
继承：TClassHelperBase → TInterfacedObject → TObject ｜ 单元：System


## TClassList
继承：TClassList → TList → TObject ｜ 单元：System.Contnrs


## TClipboard
继承：TClipboard → TPersistent → TObject ｜ 单元：Vcl.Clipbrd

property AsText: String;
property FormatCount: Integer;  // read-only
property Formats[Index: ?]: Word;  // read-only
procedure Clear;
procedure Close;
function GetAsHandle(Format: Word): NativeUInt;
function GetComponent(Owner: TComponent; Parent: TComponent): TComponent;
function GetTextBuf(Buffer: PWideChar; BufSize: Integer): Integer;
function HasFormat(Format: Word): Boolean;
procedure Open;
procedure SetAsHandle(Format: Word; Value: NativeUInt);
procedure SetComponent(Component: TComponent);
procedure SetTextBuf(Buffer: PWideChar);
procedure WndProc(const Message: IDispatch);

## TCollection
继承：TCollection → TPersistent → TObject ｜ 单元：System.Classes

property Capacity: Integer;
property Count: Integer;  // read-only
property Items[Index: ?]: TCollectionItem;
function Add: TCollectionItem;
procedure Added(var Item: TCollectionItem);
procedure BeginUpdate;
procedure Clear;
procedure Delete(Index: Integer);
procedure Deleting(Item: TCollectionItem);
procedure EndUpdate;
function FindItemID(ID: Integer): TCollectionItem;
function GetAttr(Index: Integer): string;
function GetAttrCount: Integer;
function GetEnumerator: TCollectionEnumerator;
function GetItemAttr(Index: Integer; ItemIndex: Integer): string;
function Insert(Index: Integer): TCollectionItem;
procedure Notify(Item: TCollectionItem; Action: TCollectionNotification);
function Owner: TPersistent;
procedure SetItemName(Item: TCollectionItem);
procedure Update(Item: TCollectionItem);

## TCollectionEnumerator
继承：TCollectionEnumerator → TObject ｜ 单元：System.Classes

property Current: TCollectionItem;  // read-only
procedure Create(ACollection: TCollection);
function GetCurrent: TCollectionItem;
function MoveNext: Boolean;

## TCollectionItem
继承：TCollectionItem → TPersistent → TObject ｜ 单元：System.Classes

property Collection: TCollection;
property DisplayName: String;
property ID: Integer;  // read-only
property Index: Integer;
procedure Create(Collection: TCollection);
function GetDisplayName: string;
procedure Release;
procedure SetCollection(Value: TCollection);
procedure SetDisplayName(const Value: string);
procedure SetIndex(Value: Integer);

## TColorBox
继承：TColorBox → TCustomColorBox → TCustomComboBox → TCustomCombo → TCustomListControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.ExtCtrls

property Align: TAlign;
property Anchors: TAnchors;
property AutoComplete: Boolean;
property AutoDropDown: Boolean;
property BevelEdges: TBevelEdges;
property BevelInner: TBevelCut;
property BevelKind: TBevelKind;
property BevelOuter: TBevelCut;
property BiDiMode: TBiDiMode;
property Color: TColor;
property Constraints: TSizeConstraints;
property Ctl3D: Boolean;
property DefaultColorColor: TColor;
property DoubleBuffered: Boolean;
property DropDownCount: Integer;
property Enabled: Boolean;
property Font: TFont;
property ItemHeight: Integer;
property NoneColorColor: TColor;
property OnChange: TNotifyEvent;
property OnClick: TNotifyEvent;
property OnCloseUp: TNotifyEvent;
property OnContextPopup: TContextPopupEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnDropDown: TNotifyEvent;
property OnEndDock: TEndDragEvent;
property OnEndDrag: TEndDragEvent;
property OnEnter: TNotifyEvent;
property OnExit: TNotifyEvent;
property OnGesture: TGestureEvent;
property OnGetColors: TGetColorsEvent;
property OnKeyDown: TKeyEvent;
property OnKeyPress: TKeyPressEvent;
property OnKeyUp: TKeyEvent;
property OnMouseEnter: TNotifyEvent;
property OnMouseLeave: TNotifyEvent;
property OnSelect: TNotifyEvent;
property OnStartDock: TStartDockEvent;
property OnStartDrag: TStartDragEvent;
property ParentBiDiMode: Boolean;
property ParentColor: Boolean;
property ParentCtl3D: Boolean;
property ParentDoubleBuffered: Boolean;
property ParentFont: Boolean;
property ParentShowHint: Boolean;
property PopupMenu: TPopupMenu;
property Selected: TColor;
property ShowHint: Boolean;
property Style: TColorBoxStyle;
property StyleElements: TStyleElements;
property TabOrder: TTabOrder;
property TabStop: Boolean;
property Touch: TTouchManager;
property Visible: Boolean;

## TColorDialog
继承：TColorDialog → TCommonDialog → TComponent → TPersistent → TObject ｜ 单元：Vcl.Dialogs

property Color: TColor;
property Ctl3D: Boolean;
property CustomColors: TStrings;
property Options: TColorDialogOptions;

## TColorListBox
继承：TColorListBox → TCustomColorListBox → TCustomListBox → TCustomMultiSelectListControl → TCustomListControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.ExtCtrls

property Align: TAlign;
property Anchors: TAnchors;
property AutoComplete: Boolean;
property BevelEdges: TBevelEdges;
property BevelInner: TBevelCut;
property BevelKind: TBevelKind;
property BevelOuter: TBevelCut;
property BiDiMode: TBiDiMode;
property Color: TColor;
property Constraints: TSizeConstraints;
property Ctl3D: Boolean;
property DefaultColorColor: TColor;
property DoubleBuffered: Boolean;
property Enabled: Boolean;
property Font: TFont;
property ItemHeight: Integer;
property NoneColorColor: TColor;
property OnClick: TNotifyEvent;
property OnContextPopup: TContextPopupEvent;
property OnDblClick: TNotifyEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnEndDock: TEndDragEvent;
property OnEndDrag: TEndDragEvent;
property OnEnter: TNotifyEvent;
property OnExit: TNotifyEvent;
property OnGesture: TGestureEvent;
property OnGetColors: TLBGetColorsEvent;
property OnKeyDown: TKeyEvent;
property OnKeyPress: TKeyPressEvent;
property OnKeyUp: TKeyEvent;
property OnMouseActivate: TMouseActivateEvent;
property OnMouseDown: TMouseEvent;
property OnMouseEnter: TNotifyEvent;
property OnMouseLeave: TNotifyEvent;
property OnMouseMove: TMouseMoveEvent;
property OnMouseUp: TMouseEvent;
property OnStartDock: TStartDockEvent;
property OnStartDrag: TStartDragEvent;
property ParentBiDiMode: Boolean;
property ParentColor: Boolean;
property ParentCtl3D: Boolean;
property ParentDoubleBuffered: Boolean;
property ParentFont: Boolean;
property ParentShowHint: Boolean;
property PopupMenu: TPopupMenu;
property Selected: TColor;
property ShowHint: Boolean;
property Style: TColorBoxStyle;
property StyleElements: TStyleElements;
property TabOrder: TTabOrder;
property TabStop: Boolean;
property Touch: TTouchManager;
property Visible: Boolean;

## TColorSelect
继承：TColorSelect → TCommonDialogAction → TCustomAction → TContainedAction ｜ 单元：Vcl.StdActns

property BeforeExecute: TNotifyEvent;
property Caption: string;
property Dialog: TColorDialog;  // read-only
property Enabled: Boolean;
property HelpContext: THelpContext;
property HelpKeyword: string;
property HelpType: THelpType;
property Hint: string;
property ImageIndex: TImageIndex;
property OnAccept: TNotifyEvent;
property OnCancel: TNotifyEvent;
property OnHint: THintEvent;
property OnUpdate: TNotifyEvent;
property SecondaryShortCuts: TCustomShortCutList;
property ShortCut: TShortCut;
property Visible: Boolean;

## TColumnCollection
继承：TColumnCollection → TCellCollection → TOwnedCollection → TCollection → TPersistent → TObject ｜ 单元：Vcl.ExtCtrls

function Add: TColumnItem;
procedure Create(AOwner: TPersistent);

## TColumnItem
继承：TColumnItem → TCellItem → TCollectionItem → TPersistent → TObject ｜ 单元：Vcl.ExtCtrls


## TComboBox
继承：TComboBox → TCustomComboBox → TCustomCombo → TCustomListControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.StdCtrls

property Align: TAlign;
property Anchors: TAnchors;
property AutoCloseUp: Boolean;
property AutoComplete: Boolean;
property AutoCompleteDelay: Cardinal;
property AutoDropDown: Boolean;
property BevelEdges: TBevelEdges;
property BevelInner: TBevelCut;
property BevelKind: TBevelKind;
property BevelOuter: TBevelCut;
property BiDiMode: TBiDiMode;
property CharCase: TEditCharCase;
property Color: TColor;
property Constraints: TSizeConstraints;
property Ctl3D: Boolean;
property DoubleBuffered: Boolean;
property DragCursor: TCursor;
property DragKind: TDragKind;
property DragMode: TDragMode;
property DropDownCount: Integer;
property Enabled: Boolean;
property Font: TFont;
property ImeMode: TImeMode;
property ImeName: TImeName;
property ItemHeight: Integer;
property ItemIndex: Integer;
property Items: TStrings;
property MaxLength: Integer;
property OnChange: TNotifyEvent;
property OnClick: TNotifyEvent;
property OnCloseUp: TNotifyEvent;
property OnContextPopup: TContextPopupEvent;
property OnDblClick: TNotifyEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnDrawItem: TDrawItemEvent;
property OnDropDown: TNotifyEvent;
property OnEndDock: TEndDragEvent;
property OnEndDrag: TEndDragEvent;
property OnEnter: TNotifyEvent;
property OnExit: TNotifyEvent;
property OnGesture: TGestureEvent;
property OnKeyDown: TKeyEvent;
property OnKeyPress: TKeyPressEvent;
property OnKeyUp: TKeyEvent;
property OnMeasureItem: TMeasureItemEvent;
property OnMouseEnter: TNotifyEvent;
property OnMouseLeave: TNotifyEvent;
property OnSelect: TNotifyEvent;
property OnStartDock: TStartDockEvent;
property OnStartDrag: TStartDragEvent;
property ParentBiDiMode: Boolean;
property ParentColor: Boolean;
property ParentCtl3D: Boolean;
property ParentDoubleBuffered: Boolean;
property ParentFont: Boolean;
property ParentShowHint: Boolean;
property PopupMenu: TPopupMenu;
property ShowHint: Boolean;
property Sorted: Boolean;
property Style: TComboBoxStyle;
property StyleElements: TStyleElements;
property TabOrder: TTabOrder;
property TabStop: Boolean;
property Text: TCaption;
property TextHint: string;
property Touch: TTouchManager;
property Visible: Boolean;

## TComboBoxEx
继承：TComboBoxEx → TCustomComboBoxEx → TCustomCombo → TCustomListControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.ComCtrls

property Action: TBasicAction;
property Align: TAlign;
property Anchors: TAnchors;
property AutoCompleteOptions: TAutoCompleteOptions;
property BiDiMode: TBiDiMode;
property Color: TColor;
property Constraints: TSizeConstraints;
property Ctl3D: Boolean;
property DoubleBuffered: Boolean;
property DragCursor: TCursor;
property DragKind: TDragKind;
property DragMode: TDragMode;
property DropDownCount: Integer;
property Enabled: Boolean;
property Font: TFont;
property Images: TCustomImageList;
property ImeMode: TImeMode;
property ImeName: TImeName;
property ItemHeight: Integer;
property ItemsEx: TComboExItems;
property MaxLength: Integer;
property OnBeginEdit: TNotifyEvent;
property OnChange: TNotifyEvent;
property OnClick: TNotifyEvent;
property OnContextPopup: TContextPopupEvent;
property OnDblClick: TNotifyEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnDropDown: TNotifyEvent;
property OnEndDock: TEndDragEvent;
property OnEndDrag: TEndDragEvent;
property OnEndEdit: TNotifyEvent;
property OnEnter: TNotifyEvent;
property OnExit: TNotifyEvent;
property OnGesture: TGestureEvent;
property OnKeyDown: TKeyEvent;
property OnKeyPress: TKeyPressEvent;
property OnKeyUp: TKeyEvent;
property OnMouseMove: TMouseMoveEvent;
property OnSelect: TNotifyEvent;
property OnStartDock: TStartDockEvent;
property OnStartDrag: TStartDragEvent;
property ParentBiDiMode: Boolean;
property ParentColor: Boolean;
property ParentCtl3D: Boolean;
property ParentDoubleBuffered: Boolean;
property ParentFont: Boolean;
property ParentShowHint: Boolean;
property PopupMenu: TPopupMenu;
property ShowHint: Boolean;
property Style: TComboBoxExStyle;
property StyleElements: TStyleElements;
property StyleEx: TComboBoxExStyles;
property TabOrder: TTabOrder;
property TabStop: Boolean;
property Text: TCaption;
property Touch: TTouchManager;
property Visible: Boolean;

## TComboBoxExActionLink
继承：TComboBoxExActionLink → TListActionLink → TListActionLink ｜ 单元：Vcl.ComCtrls


## TComboBoxExStrings
继承：TComboBoxExStrings → TCustomComboBoxStrings → TStrings → TPersistent → TObject ｜ 单元：Vcl.ComCtrls

property ItemsEx: TComboExItems;
property SortType: TListItemsSortType;
function AddItem(const Caption: string; const ImageIndex: Integer; const SelectedImageIndex: Integer; const OverlayImageIndex: Integer; const Indent: Integer; Data: Pointer): TComboExItem;
procedure Create(Owner: TCustomComboBoxEx);

## TComboBoxExStyleHook
继承：TComboBoxExStyleHook → TComboBoxStyleHook → TMouseTrackControlStyleHook ｜ 单元：Vcl.ComCtrls


## TComboBoxStyleHook
继承：TComboBoxStyleHook → TMouseTrackControlStyleHook → TMouseTrackControlStyleHook ｜ 单元：Vcl.StdCtrls


## TComboExItem
继承：TComboExItem → TListControlItem → TListControlItem ｜ 单元：Vcl.ComCtrls

property Indent: Integer;
property OverlayImageIndex: TImageIndex;
property SelectedImageIndex: TImageIndex;
procedure SetOverlayImageIndex(const Value: TImageIndex);
procedure SetSelectedImageIndex(const Value: TImageIndex);

## TComboExItems
继承：TComboExItems → TListControlItems → TListControlItems ｜ 单元：Vcl.ComCtrls

property ComboItems[Index: ?]: TComboExItem;  // read-only
function Add: TComboExItem;
function AddItem(const Caption: string; const ImageIndex: Integer; const SelectedImageIndex: Integer; const OverlayImageIndex: Integer; const Indent: Integer; Data: Pointer): TComboExItem;
function Insert(Index: Integer): TComboExItem;
procedure SetItem(const Index: Integer);

## TCommonCalendar
继承：TCommonCalendar → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.ComCtrls

procedure BoldDays(Days: array of Cardinal; var MonthBoldInfo: Cardinal);
procedure CheckEmptyDate;
procedure CheckValidDate(Value: TDate);
function GetCalendarHandle: HWND;
function GetCalStyles: Cardinal;
function MsgSetCalColors(ColorIndex: Integer; ColorValue: TColor): Boolean;
function MsgSetDateTime(const Value: IDispatch): Boolean;

## TCommonDialog
继承：TCommonDialog → TComponent → TPersistent → TObject ｜ 单元：Vcl.Dialogs

property Ctl3D: Boolean;
property Handle: HWND;  // read-only
property HelpContext: THelpContext;
property OnClose: TNotifyEvent;
property OnShow: TNotifyEvent;
procedure DoClose;
procedure DoShow;
function Execute: Boolean;
function GetHandle: HWND;
function MessageHook(const Msg: IDispatch): Boolean;
function TaskModalDialog(DialogFunc: Pointer; var DialogData): LongBool;
procedure WndProc(const Message: IDispatch);

## TCommonDialogAction
继承：TCommonDialogAction → TCustomAction → TContainedAction ｜ 单元：Vcl.StdActns

property ExecuteResult: Boolean;  // read-only
procedure DoAccept;
procedure DoCancel;
procedure SetupDialog;

## TComponent
继承：TComponent → TPersistent → TObject ｜ 单元：System.Classes

property ComObject: IUnknown;  // read-only
property ComponentCount: Integer;  // read-only
property ComponentIndex: Integer;
property Components[Index: ?]: TComponent;  // read-only
property ComponentState: TComponentState;  // read-only
property ComponentStyle: TComponentStyle;  // read-only
property DesignInfo: TDesignInfo;
property Name: TComponentName;
property Observers: TObservers;  // read-only
property Owner: TComponent;  // read-only
property Tag: NativeInt;
property VCLComObject: Pointer;
procedure AsyncSchedule(const AsyncResult: TBaseAsyncResult);
function CanObserve(const ID: Integer): Boolean;
procedure Create(AOwner: TComponent);
procedure DestroyComponents;
procedure Destroying;
function EndFunctionInvoke(const AsyncResult: IAsyncResult): TObject;
procedure EndInvoke(const AsyncResult: IAsyncResult);
function ExecuteAction(Action: TBasicAction): Boolean;
function FindComponent(const AName: string): TComponent;
procedure FreeNotification(AComponent: TComponent);
procedure FreeOnRelease;
function GetChildOwner: TComponent;
function GetChildParent: TComponent;
function GetEnumerator: TComponentEnumerator;
function GetObservers: TObservers;
function GetParentComponent: TComponent;
function HasParent: Boolean;
procedure InsertComponent(const AComponent: TComponent);
function IsImplementorOf(const I: IInterface): Boolean;
procedure Loaded;
procedure Notification(AComponent: TComponent; Operation: TOperation);
procedure ObserverAdded(const ID: Integer; const Observer: IObserver);
procedure PaletteCreated;
procedure ReadState(Reader: TReader);
function ReferenceInterface(const I: IInterface; Operation: TOperation): Boolean;
procedure RemoveComponent(const AComponent: TComponent);
procedure RemoveFreeNotification(AComponent: TComponent);
procedure SetChildOrder(Child: TComponent; Order: Integer);
procedure SetName(const NewName: TComponentName);
procedure SetParentComponent(Value: TComponent);
procedure SetSubComponent(IsSubComponent: Boolean);
function UpdateAction(Action: TBasicAction): Boolean;
procedure Updated;
procedure UpdateRegistry(Register: Boolean; const ClassID: string; const ProgID: string);
procedure Updating;
procedure ValidateContainer(AComponent: TComponent);
procedure ValidateInsert(AComponent: TComponent);
procedure ValidateRename(AComponent: TComponent; const CurName: string; const NewName: string);
procedure WriteState(Writer: TWriter);

## TComponentEnumerator
继承：TComponentEnumerator → TObject ｜ 单元：System.Classes

property Current: TComponent;  // read-only
procedure Create(AComponent: TComponent);
function GetCurrent: TComponent;
function MoveNext: Boolean;

## TComponentList
继承：TComponentList → TObjectList → TList → TObject ｜ 单元：System.Contnrs

property Items[Index: ?]: TComponent;
function Add(AComponent: TComponent): Integer;
procedure Create;
function Extract(Item: TComponent): TComponent;
function ExtractItem(Item: TComponent; Direction: TDirection): TComponent;
function First: TComponent;
function IndexOf(AComponent: TComponent): Integer;
function IndexOfItem(AComponent: TComponent; ADirection: TDirection): Integer;
procedure Insert(Index: Integer; AComponent: TComponent);
function Last: TComponent;
function Remove(AComponent: TComponent): Integer;
function RemoveItem(AComponent: TComponent; ADirection: TDirection): Integer;

## TCompressedBitmap
继承：TCompressedBitmap → TBitmap → TGraphic → TInterfacedPersistent → TPersistent → TObject ｜ 单元：XPImages


## TContainedObject
继承：TContainedObject → TAggregatedObject → TObject ｜ 单元：System


## TControl
继承：TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.Controls

property Action: TBasicAction;
property Align: TAlign;
property AlignWithMargins: Boolean;
property Anchors: TAnchors;
property BiDiMode: TBiDiMode;
property BoundsRect: TRect;
property ClientHeight: Integer;
property ClientOrigin: TPoint;  // read-only
property ClientRect: TRect;  // read-only
property ClientWidth: Integer;
property Constraints: TSizeConstraints;
property ControlState: TControlState;
property ControlStyle: TControlStyle;
property Cursor: TCursor;
property CustomHint: TCustomHint;
property DockOrientation: TDockOrientation;
property Enabled: Boolean;
property ExplicitHeight: Integer;  // read-only
property ExplicitLeft: Integer;  // read-only
property ExplicitTop: Integer;  // read-only
property ExplicitWidth: Integer;  // read-only
property Floating: Boolean;  // read-only
property Height: Integer;
property HelpContext: THelpContext;
property HelpKeyword: string;
property HelpType: THelpType;
property Hint: string;
property HostDockSite: TWinControl;
property Left: Integer;
property LRDockWidth: Integer;
property Margins: TMargins;
property Parent: TWinControl;
property ParentCustomHint: Boolean;
property ShowHint: Boolean;
property StyleElements: TStyleElements;
property TBDockHeight: Integer;
property Top: Integer;
property Touch: TTouchManager;
property UndockHeight: Integer;
property UndockWidth: Integer;
property Visible: Boolean;
property Width: Integer;
procedure ActionChange(Sender: TObject; CheckDefaults: Boolean);
procedure AdjustSize;
procedure BeginAutoDrag;
procedure BeginDrag(Immediate: Boolean; Threshold: Integer);
procedure BringToFront;
function CanAutoSize(var NewWidth: Integer; var NewHeight: Integer): Boolean;
function CanResize(var NewWidth: Integer; var NewHeight: Integer): Boolean;
procedure ChangeScale(M: Integer; D: Integer);
procedure Click;
function ClientToParent(const Point: IDispatch; AParent: TWinControl): IDispatch;
function ClientToScreen(const Point: IDispatch): IDispatch;
procedure ConstrainedResize(var MinWidth: Integer; var MinHeight: Integer; var MaxWidth: Integer; var MaxHeight: Integer);
procedure CreateTouchManager;
procedure DblClick;
procedure DefaultDockImage(DragDockObject: TDragDockObject; Erase: Boolean);
function DefaultScalingFlags: TScalingFlags;
function DesignWndProc(const Message: IDispatch): Boolean;
procedure Dock(NewDockSite: TWinControl; const ARect: IDispatch);
procedure DockTrackNoTarget(Source: TDragDockObject; X: Integer; Y: Integer);
procedure DoContextPopup(const MousePos: IDispatch; var Handled: Boolean);
procedure DoDock(NewDockSite: TWinControl; const ARect: IDispatch);
procedure DoEndDock(Target: TObject; X: Integer; Y: Integer);
procedure DoEndDrag(Target: TObject; X: Integer; Y: Integer);
procedure DoGesture(const EventInfo: IDispatch; var Handled: Boolean);
procedure DoGetGestureOptions(var Gestures: TInteractiveGestures; var Options: TInteractiveGestureOptions);
function DoMouseWheel(Shift: TShiftState; WheelDelta: Integer; const MousePos: IDispatch): Boolean;
function DoMouseWheelDown(Shift: TShiftState; const MousePos: IDispatch): Boolean;
function DoMouseWheelUp(Shift: TShiftState; const MousePos: IDispatch): Boolean;
procedure DoStartDock(var DragObject: TDragObject);
procedure DoStartDrag(var DragObject: TDragObject);
procedure DragCanceled;
procedure DragDrop(Source: TObject; X: Integer; Y: Integer);
function Dragging: Boolean;
procedure DragOver(Source: TObject; X: Integer; Y: Integer; State: TDragState; var Accept: Boolean);
procedure DrawDragDockImage(DragDockObject: TDragDockObject);
function DrawTextBiDiModeFlags(Flags: Integer): Integer;
function DrawTextBiDiModeFlagsReadingOnly: Integer;
procedure EndDrag(Drop: Boolean);
procedure EraseDragDockImage(DragDockObject: TDragDockObject);
function GetAction: TBasicAction;
function GetClientOrigin: IDispatch;
function GetClientRect: IDispatch;
function GetControlsAlignment: TAlignment;
function GetDeviceContext(var WindowHandle: HWND): HDC;
function GetDockEdge(const MousePos: IDispatch): TAlign;
function GetDragImages: TDragImageList;
function GetEnabled: Boolean;
function GetFloating: Boolean;
function GetPalette: HPALETTE;
function GetPopupMenu: TPopupMenu;
function GetTextBuf(Buffer: PWideChar; BufSize: Integer): Integer;
function GetTextLen: Integer;
procedure Hide;
procedure InitiateAction;
procedure Invalidate;
function IsRightToLeft: Boolean;
function IsTouchPropertyStored(AProperty: TTouchProperty): Boolean;
function ManualDock(NewDockSite: TWinControl; DropControl: TControl; ControlSide: TAlign): Boolean;
function ManualFloat(const ScreenPos: IDispatch): Boolean;
function MouseActivate(Button: TMouseButton; Shift: TShiftState; X: Integer; Y: Integer; HitTest: Integer): TMouseActivate;
procedure MouseDown(Button: TMouseButton; Shift: TShiftState; X: Integer; Y: Integer);
procedure MouseMove(Shift: TShiftState; X: Integer; Y: Integer);
procedure MouseUp(Button: TMouseButton; Shift: TShiftState; X: Integer; Y: Integer);
procedure MouseWheelHandler(const Message: IDispatch);
function PaletteChanged(Foreground: Boolean): Boolean;
function ParentToClient(const Point: IDispatch; AParent: TWinControl): IDispatch;
function Perform(Msg: Cardinal; WPARAM: NativeUInt; LParam: NativeInt): NativeInt;
procedure PositionDockRect(DragDockObject: TDragDockObject);
procedure Refresh;
procedure Repaint;
function ReplaceDockedControl(Control: TControl; NewDockSite: TWinControl; DropControl: TControl; ControlSide: TAlign): Boolean;
procedure RequestAlign;
procedure Resize;
function ScreenToClient(const Point: IDispatch): IDispatch;
procedure SendToBack;
procedure SetAutoSize(Value: Boolean);
procedure SetBiDiMode(Value: TBiDiMode);
procedure SetBounds(ALeft: Integer; ATop: Integer; AWidth: Integer; AHeight: Integer);
procedure SetDesignVisible(Value: Boolean);
procedure SetDragMode(Value: TDragMode);
procedure SetEnabled(Value: Boolean);
procedure SetParent(AParent: TWinControl);
procedure SetParentBiDiMode(Value: Boolean);
procedure SetTextBuf(Buffer: PWideChar);
procedure SetZOrder(TopMost: Boolean);
procedure Show;
procedure Update;
procedure UpdateStyleElements;
function UseRightToLeftAlignment: Boolean;
function UseRightToLeftReading: Boolean;
function UseRightToLeftScrollBar: Boolean;
procedure VisibleChanging;
procedure WndProc(const Message: IDispatch);

## TControlAction
继承：TControlAction → TCustomControlAction → TCustomAction → TContainedAction ｜ 单元：Vcl.Controls

property AutoCheck: Boolean;
property Caption: string;
property Checked: Boolean;
property DropdownMenu: TPopupMenu;
property Enabled: Boolean;
property EnableDropdown: Boolean;
property GroupIndex: Integer;
property HelpContext: THelpContext;
property HelpKeyword: string;
property HelpType: THelpType;
property Hint: string;
property ImageIndex: TImageIndex;
property OnExecute: TNotifyEvent;
property OnHint: THintEvent;
property OnUpdate: TNotifyEvent;
property PopupMenu: TPopupMenu;
property SecondaryShortCuts: TCustomShortCutList;
property ShortCut: TShortCut;
property Visible: Boolean;

## TControlActionLink
继承：TControlActionLink → TActionLink → TContainedActionLink ｜ 单元：Vcl.Controls

function DoShowHint(var HintStr: string): Boolean;
function IsDropdownMenuLinked: Boolean;
function IsEnableDropdownLinked: Boolean;
function IsPopupMenuLinked: Boolean;
procedure SetDropdownMenu(Value: TPopupMenu);
procedure SetEnableDropdown(Value: Boolean);
procedure SetPopupMenu(Value: TPopupMenu);

## TControlBar
继承：TControlBar → TCustomControlBar → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.ExtCtrls

property Align: TAlign;
property Anchors: TAnchors;
property AutoDock: Boolean;
property AutoDrag: Boolean;
property AutoSize: Boolean;
property BevelEdges: TBevelEdges;
property BevelInner: TBevelCut;
property BevelKind: TBevelKind;
property BevelOuter: TBevelCut;
property BevelWidth: TBevelWidth;
property BorderWidth: TBorderWidth;
property Canvas: TCanvas;  // read-only
property Color: TColor;
property Constraints: TSizeConstraints;
property CornerEdge: TCornerEdge;
property DockSite: Boolean;
property DragCursor: TCursor;
property DragKind: TDragKind;
property DragMode: TDragMode;
property DrawingStyle: TBandDrawingStyle;
property Enabled: Boolean;
property GradientDirection: TGradientDirection;
property GradientEndColor: TColor;
property GradientStartColor: TColor;
property OnAlignInsertBefore: TAlignInsertBeforeEvent;
property OnAlignPosition: TAlignPositionEvent;
property OnBandDrag: TBandDragEvent;
property OnBandInfo: TBandInfoEvent;
property OnBandMove: TBandMoveEvent;
property OnBandPaint: TBandPaintEvent;
property OnBeginBandMove: TBeginBandMoveEvent;
property OnCanResize: TCanResizeEvent;
property OnClick: TNotifyEvent;
property OnConstrainedResize: TConstrainedResizeEvent;
property OnContextPopup: TContextPopupEvent;
property OnDblClick: TNotifyEvent;
property OnDockDrop: TDockDropEvent;
property OnDockOver: TDockOverEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnEndBandMove: TEndBandMoveEvent;
property OnEndDock: TEndDragEvent;
property OnEndDrag: TEndDragEvent;
property OnEnter: TNotifyEvent;
property OnExit: TNotifyEvent;
property OnGesture: TGestureEvent;
property OnGetSiteInfo: TGetSiteInfoEvent;
property OnMouseActivate: TMouseActivateEvent;
property OnMouseDown: TMouseEvent;
property OnMouseEnter: TNotifyEvent;
property OnMouseLeave: TNotifyEvent;
property OnMouseMove: TMouseMoveEvent;
property OnMouseUp: TMouseEvent;
property OnPaint: TNotifyEvent;
property OnResize: TNotifyEvent;
property OnStartDock: TStartDockEvent;
property OnStartDrag: TStartDragEvent;
property OnUnDock: TUnDockEvent;
property ParentBackground: Boolean;
property ParentColor: Boolean;
property ParentCtl3D: Boolean;
property ParentFont: Boolean;
property ParentShowHint: Boolean;
property Picture: TPicture;
property PopupMenu: TPopupMenu;
property RowSize: TRowSize;
property RowSnap: Boolean;
property ShowHint: Boolean;
property TabOrder: TTabOrder;
property TabStop: Boolean;
property Touch: TTouchManager;
property Visible: Boolean;

## TControlCanvas
继承：TControlCanvas → TCanvas → TCustomCanvas → TPersistent → TObject ｜ 单元：Vcl.Controls

property Control: TControl;
procedure FreeHandle;
procedure UpdateTextFlags;

## TControlCollection
继承：TControlCollection → TOwnedCollection → TCollection → TPersistent → TObject ｜ 单元：Vcl.ExtCtrls

property ControlItems[Index1: ?, Index2: ?]: TControlItem;  // read-only
property Controls[Index1: ?, Index2: ?]: TControl;
property Items[Index: ?]: TControlItem;
function Add: TControlItem;
procedure AddControl(AControl: TControl; AColumn: Integer; ARow: Integer);
procedure Create(AOwner: TPersistent);
function IndexOf(AControl: TControl): Integer;
function Owner: TCustomGridPanel;
procedure RemoveControl(AControl: TControl);

## TControlItem
继承：TControlItem → TCollectionItem → TPersistent → TObject ｜ 单元：Vcl.ExtCtrls

property Column: Integer;
property ColumnSpan: TCellSpan;
property Control: TControl;
property Row: Integer;
property RowSpan: TCellSpan;
procedure SetLocation(AColumn: Integer; ARow: Integer; APushed: Boolean);

## TControlScrollBar
继承：TControlScrollBar → TPersistent → TObject ｜ 单元：Vcl.Forms

property ButtonSize: Integer;
property Color: TColor;
property Increment: TScrollBarInc;
property Kind: TScrollBarKind;  // read-only
property Margin: Word;
property ParentColor: Boolean;
property Position: Integer;
property Range: Integer;
property ScrollPos: Integer;  // read-only
property Size: Integer;
property Smooth: Boolean;
property Style: TScrollBarStyle;
property ThumbSize: Integer;
property Tracking: Boolean;
property Visible: Boolean;
procedure ChangeBiDiPosition;
function IsScrollBarVisible: Boolean;

## TConversion
继承：TConversion → TObject ｜ 单元：Vcl.ComCtrls

function ConvertReadStream(Stream: TStream; Buffer: TArray<System.Byte>; BufSize: Integer): Integer;
function ConvertWriteStream(Stream: TStream; Buffer: TArray<System.Byte>; BufSize: Integer): Integer;
procedure Create;

## TCoolBand
继承：TCoolBand → TCollectionItem → TPersistent → TObject ｜ 单元：Vcl.ComCtrls

property Bitmap: TBitmap;
property BorderStyle: TBorderStyle;
property Break: Boolean;
property Color: TColor;
property Control: TWinControl;
property FixedBackground: Boolean;
property FixedSize: Boolean;
property Height: Integer;  // read-only
property HorizontalOnly: Boolean;
property ImageIndex: TImageIndex;
property MinHeight: Integer;
property MinWidth: Integer;
property ParentBitmap: Boolean;
property ParentColor: Boolean;
property Text: string;
property Visible: Boolean;
property Width: Integer;
procedure ChangeScale(M: Integer; D: Integer);
procedure ParentBitmapChanged;
procedure ParentColorChanged;

## TCoolBands
继承：TCoolBands → TCollection → TPersistent → TObject ｜ 单元：Vcl.ComCtrls

property CoolBar: TCoolBar;  // read-only
property Items[Index: ?]: TCoolBand;
function Add: TCoolBand;
procedure Create(CoolBar: TCoolBar);
function FindBand(AControl: TControl): TCoolBand;

## TCoolBar
继承：TCoolBar → TToolWindow → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.ComCtrls

property Align: TAlign;
property Anchors: TAnchors;
property AutoSize: Boolean;
property BandBorderStyle: TBorderStyle;
property BandMaximize: TCoolBandMaximize;
property Bands: TCoolBands;
property Bitmap: TBitmap;
property BorderWidth: TBorderWidth;
property Color: TColor;
property Constraints: TSizeConstraints;
property Ctl3D: Boolean;
property DockSite: Boolean;
property DoubleBuffered: Boolean;
property DragCursor: TCursor;
property DragKind: TDragKind;
property DragMode: TDragMode;
property EdgeBorders: TEdgeBorders;
property EdgeInner: TEdgeStyle;
property EdgeOuter: TEdgeStyle;
property Enabled: Boolean;
property FixedOrder: Boolean;
property FixedSize: Boolean;
property Font: TFont;
property Images: TCustomImageList;
property OnChange: TNotifyEvent;
property OnClick: TNotifyEvent;
property OnContextPopup: TContextPopupEvent;
property OnDblClick: TNotifyEvent;
property OnDockDrop: TDockDropEvent;
property OnDockOver: TDockOverEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnEndDock: TEndDragEvent;
property OnEndDrag: TEndDragEvent;
property OnGesture: TGestureEvent;
property OnGetSiteInfo: TGetSiteInfoEvent;
property OnMouseActivate: TMouseActivateEvent;
property OnMouseDown: TMouseEvent;
property OnMouseEnter: TNotifyEvent;
property OnMouseLeave: TNotifyEvent;
property OnMouseMove: TMouseMoveEvent;
property OnMouseUp: TMouseEvent;
property OnResize: TNotifyEvent;
property OnStartDock: TStartDockEvent;
property OnStartDrag: TStartDragEvent;
property OnUnDock: TUnDockEvent;
property ParentColor: Boolean;
property ParentDoubleBuffered: Boolean;
property ParentFont: Boolean;
property ParentShowHint: Boolean;
property PopupMenu: TPopupMenu;
property ShowHint: Boolean;
property ShowText: Boolean;
property StyleElements: TStyleElements;
property Touch: TTouchManager;
property Vertical: Boolean;
property Visible: Boolean;
procedure Change;

## TCoolBarStyleHook
继承：TCoolBarStyleHook → TStyleHook → TStyleHook ｜ 单元：Vcl.ComCtrls


## TCurrencyField
继承：TCurrencyField → TFloatField → TNumericField → TField → TComponent → TPersistent → TObject ｜ 单元：Data.DB

property currency: Boolean;

## TCustomAction
继承：TCustomAction → TContainedAction → TContainedAction ｜ 单元：Vcl.ActnList

property ActionList: TCustomActionList;
property Images: TCustomImageList;  // read-only

## TCustomActionList
继承：TCustomActionList → TContainedActionList → TContainedActionList ｜ 单元：Vcl.ActnList

property Images: TCustomImageList;
function IsShortCut(const Message: IDispatch): Boolean;
procedure SetImages(Value: TCustomImageList);

## TCustomActiveForm
继承：TCustomActiveForm → TCustomForm → TScrollingWinControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.Forms

property ActiveControl: TWinControl;
property Anchors: TAnchors;
property AutoScroll: Boolean;
property AutoSize: Boolean;
property AxBorderStyle: TActiveFormBorderStyle;
property BorderWidth: TBorderWidth;
property Caption: TCaption;
property Color: TColor;
property Constraints: TSizeConstraints;
property Font: TFont;
property Height: Integer;
property HorzScrollBar: TControlScrollBar;
property KeyPreview: Boolean;
property OldCreateOrder: Boolean;
property OnActivate: TNotifyEvent;
property OnAfterMonitorDpiChanged: TMonitorDpiChangedEvent;
property OnBeforeMonitorDpiChanged: TMonitorDpiChangedEvent;
property OnClick: TNotifyEvent;
property OnContextPopup: TContextPopupEvent;
property OnCreate: TNotifyEvent;
property OnDblClick: TNotifyEvent;
property OnDeactivate: TNotifyEvent;
property OnDestroy: TNotifyEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnKeyDown: TKeyEvent;
property OnKeyPress: TKeyPressEvent;
property OnKeyUp: TKeyEvent;
property OnMouseActivate: TMouseActivateEvent;
property OnMouseDown: TMouseEvent;
property OnMouseEnter: TNotifyEvent;
property OnMouseLeave: TNotifyEvent;
property OnMouseMove: TMouseMoveEvent;
property OnMouseUp: TMouseEvent;
property OnPaint: TNotifyEvent;
property Padding: TPadding;
property PixelsPerInch: Integer;
property PopupMenu: TPopupMenu;
property PrintScale: TPrintScale;
property Scaled: Boolean;
property ShowHint: Boolean;
property VertScrollBar: TControlScrollBar;
property Visible: Boolean;
property Width: Integer;

## TCustomADODataSet
继承：TCustomADODataSet → TDataSet → TComponent → TPersistent → TObject ｜ 单元：Data.Win.ADODB

property Active: Boolean;
property AfterCancel: TDataSetNotifyEvent;
property AfterClose: TDataSetNotifyEvent;
property AfterDelete: TDataSetNotifyEvent;
property AfterEdit: TDataSetNotifyEvent;
property AfterInsert: TDataSetNotifyEvent;
property AfterOpen: TDataSetNotifyEvent;
property AfterPost: TDataSetNotifyEvent;
property AfterRefresh: TDataSetNotifyEvent;
property AfterScroll: TDataSetNotifyEvent;
property AutoCalcFields: Boolean;
property BeforeCancel: TDataSetNotifyEvent;
property BeforeClose: TDataSetNotifyEvent;
property BeforeDelete: TDataSetNotifyEvent;
property BeforeEdit: TDataSetNotifyEvent;
property BeforeInsert: TDataSetNotifyEvent;
property BeforeOpen: TDataSetNotifyEvent;
property BeforePost: TDataSetNotifyEvent;
property BeforeRefresh: TDataSetNotifyEvent;
property BeforeScroll: TDataSetNotifyEvent;
property CacheSize: Integer;
property Connection: TADOConnection;
property ConnectionString: WideString;
property CursorLocation: TCursorLocation;
property CursorType: TCursorType;
property DesignerData: String;
property EnableBCD: Boolean;
property ExecuteOptions: TExecuteOptions;
property Filter: string;
property Filtered: Boolean;
property FilterGroup: TFilterGroup;
property IndexFieldCount: Integer;  // read-only
property IndexFields[Index: ?]: TField;
property IndexName: WideString;
property LockType: TADOLockType;
property MarshalOptions: TMarshalOption;
property MaxRecords: Integer;
property OnCalcFields: TDataSetNotifyEvent;
property OnDeleteError: TDataSetErrorEvent;
property OnEditError: TDataSetErrorEvent;
property OnEndOfRecordset: TEndOfRecordsetEvent;
property OnFetchComplete: TRecordsetEvent;
property OnFetchProgress: TFetchProgressEvent;
property OnFieldChangeComplete: TFieldChangeCompleteEvent;
property OnFilterRecord: TFilterRecordEvent;
property OnMoveComplete: TRecordsetErrorEvent;
property OnNewRecord: TDataSetNotifyEvent;
property OnPostError: TDataSetErrorEvent;
property OnRecordChangeComplete: TRecordChangeCompleteEvent;
property OnRecordsetChangeComplete: TRecordsetErrorEvent;
property OnRecordsetCreate: TRecordsetCreate;
property OnWillChangeField: TWillChangeFieldEvent;
property OnWillChangeRecord: TWillChangeRecordEvent;
property OnWillChangeRecordset: TRecordsetReasonEvent;
property OnWillMove: TRecordsetReasonEvent;
property Properties: Properties;  // read-only
property Recordset: _Recordset;
property RecordsetState: TObjectStates;  // read-only
property RecordStatus: TRecordStatusSet;  // read-only
property Sort: WideString;
procedure CancelBatch(AffectRecords: TAffectRecords);
procedure CancelUpdates;
procedure Clone(Source: TCustomADODataSet; LockType: TADOLockType);
procedure DeleteRecords(AffectRecords: TAffectRecords);
procedure DestroyLookupCursor;
procedure FilterOnBookmarks(Bookmarks: array of TVarRec);
procedure LoadFromFile(const FileName: WideString);
procedure MasterChanged(Sender: TObject);
procedure MasterDisabled(Sender: TObject);
function NextRecordset(var RecordsAffected: Integer): _Recordset;
procedure PrepareCursor;
procedure Requery(Options: TExecuteOptions);
procedure SaveToFile(const FileName: WideString; Format: TPersistFormat);
function Seek(const KeyValues: Variant; SeekOption: TSeekOption): Boolean;
procedure SetConnection(const Value: TADOConnection);
function SetConnectionFlag(Flag: Integer; Value: Boolean): Boolean;
procedure SetDataSource(const Value: TDataSource);
function Supports(CursorOptions: TCursorOptions): Boolean;
procedure UpdateBatch(AffectRecords: TAffectRecords);

## TCustomAttribute
继承：TCustomAttribute → TObject ｜ 单元：System


## TCustomBucketList
继承：TCustomBucketList → TObject ｜ 单元：System.Contnrs

property Data[Index: ?]: Pointer;
function Add(AItem: Pointer; AData: Pointer): Pointer;
function AddItem(ABucket: Integer; AItem: Pointer; AData: Pointer): Pointer;
procedure Assign(AList: TCustomBucketList);
function BucketFor(AItem: Pointer): Integer;
procedure Clear;
function DeleteItem(ABucket: Integer; AIndex: Integer): Pointer;
function Exists(AItem: Pointer): Boolean;
function Find(AItem: Pointer; out AData: Pointer): Boolean;
function FindItem(AItem: Pointer; out ABucket: Integer; out AIndex: Integer): Boolean;
function Remove(AItem: Pointer): Pointer;

## TCustomButton
继承：TCustomButton → TButtonControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.StdCtrls

property Cancel: Boolean;
property CommandLinkHint: String;
property Default: Boolean;
property DisabledImageIndex: TImageIndex;
property DropDownMenu: TPopupMenu;
property ElevationRequired: Boolean;
property HotImageIndex: TImageIndex;
property ImageAlignment: TImageAlignment;
property ImageIndex: TImageIndex;
property ImageMargins: TImageMargins;
property Images: TCustomImageList;
property ModalResult: TModalResult;
property PressedImageIndex: TImageIndex;
property SelectedImageIndex: TImageIndex;
property Style: TButtonStyle;
property StylusHotImageIndex: TImageIndex;
property TabStop: Boolean;
procedure SetButtonStyle(ADefault: Boolean);
procedure UpdateImageList;
procedure UpdateImages;

## TCustomButtonedEdit
继承：TCustomButtonedEdit → TCustomEdit → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.ExtCtrls

property Images: TCustomImageList;
property LeftButton: TEditButton;
property RightButton: TEditButton;
procedure UpdateEditMargins;

## TCustomCanvas
继承：TCustomCanvas → TPersistent → TObject ｜ 单元：Vcl.Graphics

property CanvasOrientation: TCanvasOrientation;  // read-only
property ClipRect: TRect;  // read-only
property LockCount: Integer;  // read-only
property PenPos: TPoint;
property Pixels[Index1: ?, Index2: ?]: TColor;
property TextFlags: Longint;
procedure AngleArc(X: Integer; Y: Integer; Radius: Cardinal; StartAngle: Single; SweepAngle: Single);
procedure Arc(X1: Integer; Y1: Integer; X2: Integer; Y2: Integer; X3: Integer; Y3: Integer; X4: Integer; Y4: Integer);
procedure ArcTo(X1: Integer; Y1: Integer; X2: Integer; Y2: Integer; X3: Integer; Y3: Integer; X4: Integer; Y4: Integer);
procedure BrushCopy(const Dest: IDispatch; Bitmap: TBitmap; const Source: IDispatch; Color: TColor);
procedure Changed;
procedure Changing;
procedure Chord(X1: Integer; Y1: Integer; X2: Integer; Y2: Integer; X3: Integer; Y3: Integer; X4: Integer; Y4: Integer);
procedure Draw(X: Integer; Y: Integer; Graphic: TGraphic);
procedure DrawFocusRect(const Rect: IDispatch);
procedure Ellipse(X1: Integer; Y1: Integer; X2: Integer; Y2: Integer);
procedure FillRect(const Rect: IDispatch);
procedure FloodFill(X: Integer; Y: Integer; Color: TColor; FillStyle: TFillStyle);
procedure FrameRect(const Rect: IDispatch);
function GetCanvasOrientation: TCanvasOrientation;
function GetClipRect: IDispatch;
function GetPenPos: IDispatch;
function GetPixel(X: Integer; Y: Integer): TColor;
procedure LineTo(X: Integer; Y: Integer);
procedure Lock;
procedure MoveTo(X: Integer; Y: Integer);
procedure Pie(X1: Integer; Y1: Integer; X2: Integer; Y2: Integer; X3: Integer; Y3: Integer; X4: Integer; Y4: Integer);
procedure PolyBezier(const Points: IDispatch);
procedure PolyBezierTo(const Points: IDispatch);
procedure Polygon(const Points: IDispatch);
procedure Polyline(const Points: IDispatch);
procedure Rectangle(X1: Integer; Y1: Integer; X2: Integer; Y2: Integer);
procedure Refresh;
procedure RequiredState(ReqState: TCanvasState);
procedure RoundRect(X1: Integer; Y1: Integer; X2: Integer; Y2: Integer; X3: Integer; Y3: Integer);
procedure SetPenPos(const Value: IDispatch);
procedure SetPixel(X: Integer; Y: Integer; Value: TColor);
procedure StretchDraw(const Rect: IDispatch; Graphic: TGraphic);
function TextExtent(const Text: string): IDispatch;
function TextHeight(const Text: string): Integer;
procedure TextOut(X: Integer; Y: Integer; const Text: string);
function TextWidth(const Text: string): Integer;
function TryLock: Boolean;
procedure Unlock;

## TCustomCategoryPanel
继承：TCustomCategoryPanel → TCustomPanel → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.ExtCtrls

property Collapsed: Boolean;
property CollapsedHotImageIndex: TImageIndex;
property CollapsedImageIndex: TImageIndex;
property CollapsedPressedImageIndex: TImageIndex;
property ExpandedHotImageIndex: TImageIndex;
property ExpandedImageIndex: TImageIndex;
property ExpandedPressedImageIndex: TImageIndex;
property HeaderState: THeaderState;  // read-only
property PanelGroup: TCustomCategoryPanelGroup;
procedure CalcRectBounds;
procedure Collapse;
procedure DrawCollapsedPanel(ACanvas: TCanvas);
procedure DrawHeader;
procedure DrawHeaderBackground(ACanvas: TCanvas);
procedure DrawHeaderCaption(ACanvas: TCanvas);
procedure DrawHeaderChevron(ACanvas: TCanvas);
procedure Expand;
function GetCollapsedHeight: Integer;

## TCustomCategoryPanelGroup
继承：TCustomCategoryPanelGroup → TScrollingWinControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.ExtCtrls

property ChevronAlignment: TAlignment;
property ChevronColor: TColor;
property ChevronHotColor: TColor;
property Color: TColor;
property GradientBaseColor: TColor;
property GradientColor: TColor;
property GradientDirection: TGradientDirection;
property HeaderAlignment: TAlignment;
property HeaderFont: TFont;
property HeaderHeight: Integer;
property HeaderImage: TPicture;
property HeaderStyle: THeaderStyle;
property Images: TCustomImageList;
property Panels: TList;  // read-only
procedure CollapseAll;
function CreatePanel(AOwner: TComponent): TCustomCategoryPanel;
procedure ExpandAll;
procedure ReorderPanels;

## TCustomCheckBox
继承：TCustomCheckBox → TButtonControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.StdCtrls

property TabStop: Boolean;
procedure Toggle;

## TCustomColorBox
继承：TCustomColorBox → TCustomComboBox → TCustomCombo → TCustomListControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.ExtCtrls

property ColorNames[Index: ?]: String;  // read-only
property Colors[Index: ?]: TColor;  // read-only
property DefaultColorColor: TColor;
property NoneColorColor: TColor;
property Selected: TColor;
property Style: TColorBoxStyle;
function PickCustomColor: Boolean;

## TCustomColorListBox
继承：TCustomColorListBox → TCustomListBox → TCustomMultiSelectListControl → TCustomListControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.ExtCtrls

property ColorNames[Index: ?]: String;  // read-only
property Colors[Index: ?]: TColor;  // read-only
property DefaultColorColor: TColor;
property NoneColorColor: TColor;
property Selected: TColor;
property Style: TColorBoxStyle;
function PickCustomColor: Boolean;

## TCustomCombo
继承：TCustomCombo → TCustomListControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.StdCtrls

property Canvas: TCanvas;  // read-only
property DroppedDown: Boolean;
property Items: TStrings;
property SelLength: Integer;
property SelStart: Integer;
property TabStop: Boolean;
procedure AdjustDropDown;
procedure Change;
procedure CloseUp;
procedure ComboWndProc(const Message: IDispatch; ComboWnd: HWND; ComboProc: Pointer);
procedure DropDown;
procedure EditWndProc(const Message: IDispatch);
function GetItemCount: Integer;
function GetItemHt: Integer;
function IsItemHeightStored: Boolean;
procedure Select;
procedure SetDropDownCount(const Value: Integer);
procedure SetItemHeight(Value: Integer);
procedure SetItems(const Value: TStrings);

## TCustomComboBox
继承：TCustomComboBox → TCustomCombo → TCustomListControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.StdCtrls

property AutoCloseUp: Boolean;
property AutoComplete: Boolean;
property AutoCompleteDelay: Cardinal;
property AutoDropDown: Boolean;
property CharCase: TEditCharCase;
property SelText: String;
property TextHint: String;
procedure DoSetTextHint;
procedure DrawItem(Index: Integer; const Rect: IDispatch; State: TOwnerDrawState);
procedure MeasureItem(Index: Integer; var Height: Integer);
procedure SetStyle(Value: TComboBoxStyle);

## TCustomComboBoxEx
继承：TCustomComboBoxEx → TCustomCombo → TCustomListControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.ComCtrls

property AutoCompleteOptions: TAutoCompleteOptions;
property DropDownCount: Integer;
property Images: TCustomImageList;
property ItemsEx: TComboExItems;
property SelText: String;
property Style: TComboBoxExStyle;
property StyleEx: TComboBoxExStyles;

## TCustomComboBoxStrings
继承：TCustomComboBoxStrings → TStrings → TPersistent → TObject ｜ 单元：Vcl.StdCtrls

procedure Create;

## TCustomConnection
继承：TCustomConnection → TComponent → TPersistent → TObject ｜ 单元：Data.DB

property Connected: Boolean;
property DataSetCount: Integer;  // read-only
property DataSets[Index: ?]: TDataSet;  // read-only
property LoginPrompt: Boolean;
procedure Close;
procedure DoConnect;
procedure DoDisconnect;
function GetConnected: Boolean;
function GetDataSet(Index: Integer): TDataSet;
function GetDataSetCount: Integer;
procedure Open;
procedure SetConnected(Value: Boolean);
procedure UnRegisterClient(Client: TObject);

## TCustomControl
继承：TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.Controls

procedure Paint;

## TCustomControlAction
继承：TCustomControlAction → TCustomAction → TContainedAction ｜ 单元：Vcl.Controls

property DropdownMenu: TPopupMenu;
property EnableDropdown: Boolean;
property PopupMenu: TPopupMenu;

## TCustomControlBar
继承：TCustomControlBar → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.ExtCtrls

property Picture: TPicture;
procedure DoBandMove(Control: TControl; const ARect: IDispatch);
procedure DoBandPaint(Control: TControl; Canvas: TCanvas; const ARect: IDispatch; var Options: TBandPaintOptions);
function DoBeginBandMove(Control: TControl): Boolean;
procedure DoEndBandMove(Control: TControl);
function DragControl(AControl: TControl; X: Integer; Y: Integer; KeepCapture: Boolean): Boolean;
procedure GetControlInfo(AControl: TControl; const Insets: IDispatch; var PreferredSize: Integer; var RowCount: Integer);
procedure PaintControlFrame(Canvas: TCanvas; AControl: TControl; const ARect: IDispatch);
procedure StickControls;

## TCustomDBLookupComboBox
继承：TCustomDBLookupComboBox → TDBLookupControl → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.DBCtrls

property DropDownAlign: TDropDownAlign;
property DropDownRows: Integer;
property DropDownWidth: Integer;
property KeyValue: Variant;
property ListVisible: Boolean;  // read-only
property Text: String;  // read-only
procedure CloseUp(Accept: Boolean);
procedure DropDown;

## TCustomDesignedAreaPanel
继承：TCustomDesignedAreaPanel → TCustomForm → TScrollingWinControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：RT_CustomInstrument

property Cursor: TCursor;
property Font: TFont;
property Height: Integer;
property Hint: string;
property Name: TComponentName;
property OnClick: TNotifyEvent;
property OnCreate: TNotifyEvent;
property OnDblClick: TNotifyEvent;
property OnDestroy: TNotifyEvent;
property OnHide: TNotifyEvent;
property OnKeyDown: TKeyEvent;
property OnKeyPress: TKeyPressEvent;
property OnKeyUp: TKeyEvent;
property OnMouseActivate: TMouseActivateEvent;
property OnMouseDown: TMouseEvent;
property OnMouseEnter: TNotifyEvent;
property OnMouseLeave: TNotifyEvent;
property OnMouseMove: TMouseMoveEvent;
property OnMouseUp: TMouseEvent;
property OnMouseWheel: TMouseWheelEvent;
property OnMouseWheelDown: TMouseWheelUpDownEvent;
property OnMouseWheelUp: TMouseWheelUpDownEvent;
property OnReadWrite: TNotifyEvent;
property OnResize: TNotifyEvent;
property OnShow: TNotifyEvent;
property ParentFont: Boolean;
property ParentShowHint: Boolean;
property PopupMenu: TPopupMenu;
property ShowHint: Boolean;
property Width: Integer;
procedure DoInstrumentAction(AInstrumentID: Byte; AnAction: TInstrumentAction);
procedure DoShowOptionsDialog;
function GetIsStandardRackPanel: Boolean;
procedure InstrumentAction(AInstrumentID: Byte; AnAction: TInstrumentAction);
procedure ShowOptionsDialog;

## TCustomDockForm
继承：TCustomDockForm → TCustomForm → TScrollingWinControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.Forms

property AutoScroll: Boolean;
property BorderStyle: TFormBorderStyle;
property FormStyle: TFormStyle;
property PixelsPerInch: Integer;

## TCustomDrawGrid
继承：TCustomDrawGrid → TCustomGrid → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.Grids

property Canvas: TCanvas;  // read-only
property Col: Longint;
property ColWidths[Index: ?]: Integer;
property DrawingStyle: TGridDrawingStyle;
property EditorMode: Boolean;
property GridHeight: Integer;  // read-only
property GridWidth: Integer;  // read-only
property LeftCol: Longint;
property Row: Longint;
property RowHeights[Index: ?]: Integer;
property Selection: TGridRect;
property TabStops[Index: ?]: Boolean;
property TopRow: Longint;
function CellRect(ACol: Integer; ARow: Integer): IDispatch;
procedure MouseToCell(X: Integer; Y: Integer; var ACol: Integer; var ARow: Integer);

## TCustomEdit
继承：TCustomEdit → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.StdCtrls

property Alignment: TAlignment;
property CanUndo: Boolean;  // read-only
property Modified: Boolean;
property ReadOnly: Boolean;
property SelLength: Integer;
property SelStart: Integer;
property SelText: String;
property TabStop: Boolean;
property Text: TCaption;
property TextHint: String;
procedure Change;
procedure Clear;
procedure ClearSelection;
procedure ClearUndo;
procedure CopyToClipboard;
procedure CutToClipboard;
procedure DoSetMaxLength(Value: Integer);
procedure DoSetTextHint(const Value: string);
function GetSelLength: Integer;
function GetSelStart: Integer;
function GetSelText: string;
function GetSelTextBuf(Buffer: PWideChar; BufSize: Integer): Integer;
procedure PasteFromClipboard;
procedure SelectAll;
procedure SetSelLength(Value: Integer);
procedure SetSelStart(Value: Integer);
procedure SetSelText(const Value: string);
procedure SetSelTextBuf(Buffer: PWideChar);
procedure Undo;

## TCustomFileDialog
继承：TCustomFileDialog → TComponent → TPersistent → TObject ｜ 单元：Vcl.Dialogs

property ClientGuid: String;
property DefaultExtension: String;
property DefaultFolder: String;
property Dialog: IFileDialog;  // read-only
property FavoriteLinks: TFavoriteLinkItems;
property FileName: TFileName;
property FileNameLabel: String;
property Files: TStrings;  // read-only
property FileTypeIndex: Cardinal;
property FileTypes: TFileTypeItems;
property Handle: HWND;  // read-only
property OkButtonLabel: String;
property Options: TFileDialogOptions;
property ShellItem: IShellItem;  // read-only
property ShellItems: IShellItemArray;  // read-only
property Title: String;
function Execute: Boolean;
function FileOkClick: HRESULT;
function FolderChange: HRESULT;
function FolderChanging(psiFolder: IShellItem): HRESULT;
function Overwrite(psiFile: IShellItem; var Response: Cardinal): HRESULT;
function SelectionChange: HRESULT;
function ShareViolation(psiFile: IShellItem; var Response: Cardinal): HRESULT;
function TypeChange: HRESULT;

## TCustomFileOpenDialog
继承：TCustomFileOpenDialog → TCustomFileDialog → TComponent → TPersistent → TObject ｜ 单元：Vcl.Dialogs


## TCustomFileSaveDialog
继承：TCustomFileSaveDialog → TCustomFileDialog → TComponent → TPersistent → TObject ｜ 单元：Vcl.Dialogs


## TCustomFlowPanel
继承：TCustomFlowPanel → TCustomPanel → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.ExtCtrls

property AutoWrap: Boolean;
property FlowStyle: TFlowStyle;
function GetControlIndex(AControl: TControl): Integer;
procedure SetControlIndex(AControl: TControl; Index: Integer);

## TCustomForm
继承：TCustomForm → TScrollingWinControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.Forms

property Action: TBasicAction;
property Active: Boolean;  // read-only
property ActiveControl: TWinControl;
property ActiveOleControl: TWinControl;
property BorderStyle: TFormBorderStyle;
property Canvas: TCanvas;  // read-only
property Caption: TCaption;
property Color: TColor;
property Designer: IDesignerHook;
property DropTarget: Boolean;
property Font: TFont;
property FormState: TFormState;  // read-only
property GlassFrame: TGlassFrame;
property HelpFile: String;
property KeyPreview: Boolean;
property Left: Integer;
property Menu: TMainMenu;
property ModalResult: TModalResult;
property Monitor: TMonitor;  // read-only
property OleFormObject: IOleForm;
property PopupMode: TPopupMode;
property PopupParent: TCustomForm;
property ScreenSnap: Boolean;
property SnapBuffer: Integer;
property TaskbarHandler: TTaskbarHandler;
property Top: Integer;
property WindowState: TWindowState;
procedure Activate;
procedure ActiveChanged;
procedure ClientWndProc(const Message: IDispatch);
procedure Close;
function CloseQuery: Boolean;
procedure CreateNew(AOwner: TComponent; Dummy: Integer);
procedure Deactivate;
procedure DefocusControl(Control: TWinControl; Removing: Boolean);
procedure DoClose(var Action: TCloseAction);
procedure DoCreate;
procedure DoDestroy;
procedure DoHide;
procedure DoShow;
procedure DoThumbButtonNotify(ItemID: Word);
procedure DoThumbPreviewRequest(APreviewHeight: Word; APreviewWidth: Word);
procedure DoWindowPreviewRequest;
procedure FocusControl(Control: TWinControl);
procedure GetBorderIconStyles(var Style: Cardinal; var ExStyle: Cardinal);
procedure GetBorderStyles(var Style: Cardinal; var ExStyle: Cardinal; var ClassStyle: Cardinal);
function GetFormImage: TBitmap;
function GetOwnerWindow: HWND;
function HandleCreateException: Boolean;
procedure Hide;
procedure InitializeNewForm;
function IsShortCut(const Message: IDispatch): Boolean;
procedure MakeFullyVisible(AMonitor: TMonitor);
procedure Paint;
procedure Print;
procedure RecreateAsPopup(AWindowHandle: HWND);
procedure Release;
procedure SendCancelMode(Sender: TControl);
procedure set_PopupParent(Value: TCustomForm);
function SetFocusedControl(Control: TWinControl): Boolean;
procedure Show;
function ShowModal: Integer;
procedure UpdateActions;
function WantChildKey(Child: TControl; const Message: IDispatch): Boolean;

## TCustomFrame
继承：TCustomFrame → TScrollingWinControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.Forms


## TCustomGestureCollection
继承：TCustomGestureCollection → TCollection → TPersistent → TObject ｜ 单元：Vcl.Controls

property GestureManager: TCustomGestureManager;  // read-only
property Items[Index: ?]: TCustomGestureCollectionItem;
function AddGesture: TCustomGestureCollectionItem;
function FindGesture(AGestureID: TGestureID): TCustomGestureCollectionItem;
function GetGestureManager: TCustomGestureManager;
function GetUniqueGestureID: TGestureID;
procedure RemoveGesture(AGestureID: TGestureID);

## TCustomGestureCollectionItem
继承：TCustomGestureCollectionItem → TCollectionItem → TPersistent → TObject ｜ 单元：Vcl.Controls

property Action: TBasicAction;
property Deviation: Integer;
property ErrorMargin: Integer;
property GestureID: TGestureID;
property GestureType: TGestureType;  // read-only
property Name: String;
property Options: TGestureOptions;

## TCustomGestureEngine
继承：TCustomGestureEngine → TObject ｜ 单元：Vcl.Controls

property Active: Boolean;
property Flags: TGestureEngineFlags;  // read-only
procedure Create(AControl: TWinControl);
function GetActive: Boolean;
function GetFlags: TCustomGestureEngine.TGestureEngineFlags;
procedure Notification(const Message: IDispatch);
procedure SetActive(const Value: Boolean);
function Supported: Boolean;

## TCustomGestureManager
继承：TCustomGestureManager → TComponent → TPersistent → TObject ｜ 单元：Vcl.Controls

function AddRecordedGesture(Item: TCustomGestureCollectionItem): TGestureID;
function FindCustomGesture(AGestureID: TGestureID): TCustomGestureCollectionItem;
function FindGesture(AControl: TControl; AGestureID: TGestureID): TCustomGestureCollectionItem;
procedure RegisterControl(AControl: TControl);
procedure RemoveRecordedGesture(AGestureID: TGestureID);
function SelectGesture(AControl: TControl; AGestureID: TGestureID): Boolean;
procedure UnregisterControl(AControl: TControl);
procedure UnselectGesture(AControl: TControl; AGestureID: TGestureID);

## TCustomGraphicInstrumentWithBackground
继承：TCustomGraphicInstrumentWithBackground → TGraphicControl → TControl → TComponent → TPersistent → TObject ｜ 单元：InstrumentBaseControls

procedure BackgroundOptionsChanged(AChanges: TInstrumentBackgroundOptions);
procedure MarginChanged;

## TCustomGraphicInstrumentWithInterior
继承：TCustomGraphicInstrumentWithInterior → TCustomGraphicInstrumentWithBackground → TGraphicControl → TControl → TComponent → TPersistent → TObject ｜ 单元：InstrumentBaseControls

procedure DoPaint(ACanvas: TCanvas; X: Integer; Y: Integer);
procedure PaintInterior(ACanvas: TCanvas; const ARect: IDispatch);
function UseCreamBackground: Boolean;

## TCustomGraphicInstrumentWithNoise
继承：TCustomGraphicInstrumentWithNoise → TCustomGraphicInstrumentWithBackground → TGraphicControl → TControl → TComponent → TPersistent → TObject ｜ 单元：InstrumentBaseControls

procedure PaintControlBackground(ABitmap: TBitmap; X: Integer; Y: Integer);
procedure PaintControlForeground(ABitmap: TBitmap; X: Integer; Y: Integer);
procedure PaintOnPanel(APanel: TCustomInstrumentBackgroundPanel);

## TCustomGrid
继承：TCustomGrid → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.Grids

property TabStop: Boolean;
procedure AdjustSize(Index: Integer; Amount: Integer; Rows: Boolean);
function BeginColumnDrag(var Origin: Integer; var Destination: Integer; const MousePt: IDispatch): Boolean;
function BeginRowDrag(var Origin: Integer; var Destination: Integer; const MousePt: IDispatch): Boolean;
procedure CalcSizingState(X: Integer; Y: Integer; var State: TGridState; var Index: Integer; var SizingPos: Integer; var SizingOfs: Integer; const FixedInfo: IDispatch);
function CanEditAcceptKey(Key: Char): Boolean;
function CanEditModify: Boolean;
function CanEditShow: Boolean;
function CanGridAcceptKey(Key: Word; Shift: TShiftState): Boolean;
function CheckColumnDrag(var Origin: Integer; var Destination: Integer; const MousePt: IDispatch): Boolean;
function CheckRowDrag(var Origin: Integer; var Destination: Integer; const MousePt: IDispatch): Boolean;
procedure ColumnMoved(FromIndex: Integer; ToIndex: Integer);
procedure ColWidthsChanged;
function CreateEditor: TInplaceEdit;
procedure DeleteColumn(ACol: Integer);
procedure DeleteRow(ARow: Integer);
procedure DrawCell(ACol: Integer; ARow: Integer; const ARect: IDispatch; AState: TGridDrawState);
procedure DrawCellBackground(const ARect: IDispatch; AColor: TColor; AState: TGridDrawState; ACol: Integer; ARow: Integer);
procedure DrawCellHighlight(const ARect: IDispatch; AState: TGridDrawState; ACol: Integer; ARow: Integer);
function EndColumnDrag(var Origin: Integer; var Destination: Integer; const MousePt: IDispatch): Boolean;
function EndRowDrag(var Origin: Integer; var Destination: Integer; const MousePt: IDispatch): Boolean;
procedure FixedCellClick(ACol: Integer; ARow: Integer);
function GetEditLimit: Integer;
function GetEditMask(ACol: Integer; ARow: Integer): string;
function GetEditStyle(ACol: Integer; ARow: Integer): TEditStyle;
function GetEditText(ACol: Integer; ARow: Integer): string;
function MouseCoord(X: Integer; Y: Integer): IDispatch;
procedure RowHeightsChanged;
procedure RowMoved(FromIndex: Integer; ToIndex: Integer);
function SelectCell(ACol: Integer; ARow: Integer): Boolean;
procedure SelectionMoved(const OldSel: IDispatch);
procedure SetEditText(ACol: Integer; ARow: Integer; const Value: string);
procedure SizeChanged(OldColCount: Integer; OldRowCount: Integer);
procedure TimedScroll(Direction: TGridScrollDirection);
procedure TopLeftChanged;

## TCustomGridPanel
继承：TCustomGridPanel → TCustomPanel → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.ExtCtrls

property CellCount: Integer;  // read-only
property CellRect[Index1: ?, Index2: ?]: TRect;  // read-only
property CellSize[Index1: ?, Index2: ?]: TPoint;  // read-only
property ColumnCollection: TColumnCollection;
property ColumnSpanIndex[Index1: ?, Index2: ?]: Integer;  // read-only
property ControlCollection: TControlCollection;
property ExpandStyle: TExpandStyle;
property RowCollection: TRowCollection;
property RowSpanIndex[Index1: ?, Index2: ?]: Integer;  // read-only
function IsColumnEmpty(AColumn: Integer): Boolean;
function IsRowEmpty(ARow: Integer): Boolean;
procedure UpdateControlsColumn(AColumn: Integer);
procedure UpdateControlsRow(ARow: Integer);

## TCustomGroupBox
继承：TCustomGroupBox → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.StdCtrls


## TCustomHeaderControl
继承：TCustomHeaderControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.ComCtrls

property Align: TAlign;
property Anchors: TAnchors;
property BiDiMode: TBiDiMode;
property BorderWidth: TBorderWidth;
property Canvas: TCanvas;  // read-only
property CheckBoxes: Boolean;
property Constraints: TSizeConstraints;
property DragCursor: TCursor;
property DragKind: TDragKind;
property DragMode: TDragMode;
property DragReorder: Boolean;
property Enabled: Boolean;
property Font: TFont;
property FullDrag: Boolean;
property HotTrack: Boolean;
property Images: TCustomImageList;
property NoSizing: Boolean;
property OnCreateSectionClass: TCustomHCCreateSectionClassEvent;
property OnDrawSection: TCustomDrawSectionEvent;
property OnSectionCheck: TCustomSectionNotifyEvent;
property OnSectionClick: TCustomSectionNotifyEvent;
property OnSectionDrag: TSectionDragEvent;
property OnSectionEndDrag: TNotifyEvent;
property OnSectionResize: TCustomSectionNotifyEvent;
property OnSectionTrack: TCustomSectionTrackEvent;
property OverFlow: Boolean;
property Sections: THeaderSections;
property Style: THeaderStyle;
function CreateSection: THeaderSection;
function CreateSections: THeaderSections;
procedure DrawSection(Section: THeaderSection; const Rect: IDispatch; Pressed: Boolean);
procedure SectionCheck(Section: THeaderSection);
procedure SectionClick(Section: THeaderSection);
procedure SectionDrag(FromSection: THeaderSection; ToSection: THeaderSection; var AllowDrag: Boolean);
procedure SectionEndDrag;
procedure SectionResize(Section: THeaderSection);
procedure SectionTrack(Section: THeaderSection; Width: Integer; State: TSectionTrackState);
procedure SetImages(Value: TCustomImageList);

## TCustomHint
继承：TCustomHint → TComponent → TPersistent → TObject ｜ 单元：Vcl.Controls

property Delay: Cardinal;
property Description: String;
property HideAfter: Integer;
property ImageIndex: TImageIndex;
property Images: TImageList;
property ShowingHint: Boolean;  // read-only
property Style: TBalloonHintStyle;
property Title: String;
procedure HideHint;
procedure NCPaintHint(HintWindow: TCustomHintWindow; DC: HDC);
procedure PaintHint(HintWindow: TCustomHintWindow);
procedure SetHintSize(HintWindow: TCustomHintWindow);
procedure ShowHint;

## TCustomHintShowHideThread
继承：TCustomHintShowHideThread → TThread → TObject ｜ 单元：Vcl.Controls

procedure Create(Hint: TCustomHintWindow; HintObject: TCustomHint);
procedure HideHint;
procedure ResumeWork;

## TCustomHintWindow
继承：TCustomHintWindow → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.Controls

property Description: String;  // read-only
property HintParent: TCustomHint;
property ImageIndex: TImageIndex;  // read-only
property PopAbove: Boolean;  // read-only
property Title: String;  // read-only
procedure AutoSize;
procedure NCPaint(DC: HDC);
procedure PositionAt(const Point: IDispatch);
procedure PositionAtCursor;

## TCustomHotKey
继承：TCustomHotKey → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.ComCtrls


## TCustomImageList
继承：TCustomImageList → TBaseImageList → TBaseImageList ｜ 单元：Vcl.ImgList

property AllocBy: Integer;
property BkColor: TColor;
property BlendColor: TColor;
property ColorDepth: TColorDepth;
property DrawingStyle: TDrawingStyle;
property GrayscaleFactor: Byte;
property Handle: HImageList;
property Height: Integer;
property ImageType: TImageType;
property Masked: Boolean;
property ShareImages: Boolean;
property Width: Integer;
function Add(Image: TBitmap; Mask: TBitmap): Integer;
function AddIcon(Image: TIcon): Integer;
function AddImage(Value: TCustomImageList; Index: Integer): Integer;
procedure AddImages(Value: TCustomImageList);
function AddMasked(Image: TBitmap; MaskColor: TColor): Integer;
procedure BeginUpdate;
procedure Clear;
procedure CreateSize(AWidth: Integer; AHeight: Integer);
procedure Delete(Index: Integer);
procedure DoDraw(Index: Integer; Canvas: TCanvas; X: Integer; Y: Integer; Style: Cardinal; Enabled: Boolean);
procedure Draw(Canvas: TCanvas; X: Integer; Y: Integer; Index: Integer; Enabled: Boolean);
procedure DrawOverlay(Canvas: TCanvas; X: Integer; Y: Integer; ImageIndex: Integer; Overlay: TOverlay; Enabled: Boolean);
procedure EndUpdate;
function FileLoad(ResType: TResType; const Name: string; MaskColor: TColor): Boolean;
function GetBitmap(Index: Integer; Image: TBitmap): Boolean;
function GetHotSpot: IDispatch;
procedure GetIcon(Index: Integer; Image: TIcon);
function GetImageBitmap: HBITMAP;
function GetInstRes(Instance: NativeUInt; ResType: TResType; const Name: string; Width: Integer; LoadFlags: TLoadResources; MaskColor: TColor): Boolean;
function GetMaskBitmap: HBITMAP;
function GetResource(ResType: TResType; const Name: string; Width: Integer; LoadFlags: TLoadResources; MaskColor: TColor): Boolean;
function HandleAllocated: Boolean;
procedure Initialize;
procedure Insert(Index: Integer; Image: TBitmap; Mask: TBitmap);
procedure InsertIcon(Index: Integer; Image: TIcon);
procedure InsertMasked(Index: Integer; Image: TBitmap; MaskColor: TColor);
procedure Move(CurIndex: Integer; NewIndex: Integer);
function Overlay(ImageIndex: Integer; Overlay: TOverlay): Boolean;
procedure ReadData(Stream: TStream);
procedure RegisterChanges(Value: TChangeLink);
procedure Replace(Index: Integer; Image: TBitmap; Mask: TBitmap);
procedure ReplaceIcon(Index: Integer; Image: TIcon);
procedure ReplaceMasked(Index: Integer; NewImage: TBitmap; MaskColor: TColor);
function ResInstLoad(Instance: NativeUInt; ResType: TResType; const Name: string; MaskColor: TColor): Boolean;
function ResourceLoad(ResType: TResType; const Name: string; MaskColor: TColor): Boolean;
procedure SetSize(AWidth: Integer; AHeight: Integer);
procedure UnRegisterChanges(Value: TChangeLink);
procedure WriteData(Stream: TStream);

## TCustomIniFile
继承：TCustomIniFile → TObject ｜ 单元：System.IniFiles

property FileName: String;  // read-only
procedure Create(const FileName: string);
procedure DeleteKey(const Section: string; const Ident: string);
procedure EraseSection(const Section: string);
procedure InternalReadSections(const Section: string; Strings: TStrings; SubSectionNamesOnly: Boolean; Recurse: Boolean);
function ReadBinaryStream(const Section: string; const Name: string; Value: TStream): Integer;
function ReadBool(const Section: string; const Ident: string; Default: Boolean): Boolean;
function ReadDate(const Section: string; const Name: string; Default: TDateTime): TDateTime;
function ReadDateTime(const Section: string; const Name: string; Default: TDateTime): TDateTime;
function ReadFloat(const Section: string; const Name: string; Default: Double): Double;
function ReadInteger(const Section: string; const Ident: string; Default: Integer): Integer;
procedure ReadSection(const Section: string; Strings: TStrings);
procedure ReadSections(Strings: TStrings);
procedure ReadSectionValues(const Section: string; Strings: TStrings);
function ReadString(const Section: string; const Ident: string; const Default: string): string;
procedure ReadSubSections(const Section: string; Strings: TStrings; Recurse: Boolean);
function ReadTime(const Section: string; const Name: string; Default: TDateTime): TDateTime;
function SectionExists(const Section: string): Boolean;
procedure UpdateFile;
function ValueExists(const Section: string; const Ident: string): Boolean;
procedure WriteBinaryStream(const Section: string; const Name: string; Value: TStream);
procedure WriteBool(const Section: string; const Ident: string; Value: Boolean);
procedure WriteDate(const Section: string; const Name: string; Value: TDateTime);
procedure WriteDateTime(const Section: string; const Name: string; Value: TDateTime);
procedure WriteFloat(const Section: string; const Name: string; Value: Double);
procedure WriteInteger(const Section: string; const Ident: string; Value: Integer);
procedure WriteString(const Section: string; const Ident: string; const Value: string);
procedure WriteTime(const Section: string; const Name: string; Value: TDateTime);

## TCustomInstrumentBackgroundPanel
继承：TCustomInstrumentBackgroundPanel → TXPCustomExtPanel → TXPCustomControl → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：InstrumentPanels

property BackgroundColor: TColor;  // read-only
property CoreName: String;
property JtagID: Integer;
property Label_Title: TLabel;  // read-only
property PortID: Integer;
property Primary: Boolean;
property ShowCoreName: Boolean;
property ShowGrooves: Boolean;
property ShowJTAG: Boolean;
property ShowMountingHoles: Boolean;
property ShowTitle: Boolean;
property Style: TInstrumentPanelStyle;
property Title: String;
procedure UpdateBackgroundImage;
procedure UpdateChildControls;

## TCustomInstrumentButton
继承：TCustomInstrumentButton → TXPCustomSpeedButton → TXPBaseCustomSpeedButton → TXPCustomTransparentControl → TXPCustomControl → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：InstrumentButtons

property Font: TFont;
property ParentFont: Boolean;
procedure BackgroundChanged(Sender: TObject);
function GetCaptionFontColor(ADown: Boolean; AOn: Boolean): TColor;
function GetDrawCaptionStyle(ADown: Boolean; AOn: Boolean): TDrawInstrumentButtonCaptionStyle;
function GetDrawFlags(ADown: Boolean; AOn: Boolean): TDrawInstrumentButtonFlags;
function GetGlowIntensity: TGlowIntensity;
procedure UpdateBitmaps;

## TCustomInstrumentCaption
继承：TCustomInstrumentCaption → TCustomInstrumentLabel → TCustomLabel → TGraphicControl → TControl → TComponent → TPersistent → TObject ｜ 单元：InstrumentLabels


## TCustomInstrumentCheckBox
继承：TCustomInstrumentCheckBox → TGraphicControl → TControl → TComponent → TPersistent → TObject ｜ 单元：InstrumentChecks

procedure Changed;

## TCustomInstrumentDigitsPanel
继承：TCustomInstrumentDigitsPanel → TCustomGraphicInstrumentWithInterior → TCustomGraphicInstrumentWithBackground → TGraphicControl → TControl → TComponent → TPersistent → TObject ｜ 单元：InstrumentDigitPanels

procedure DigitClick(ADigitIndex: Integer; AButton: TMouseButton);
function GetDigitHeight: Integer;
function GetDigitWidth: Integer;
procedure PaintDigit(ACanvas: TCanvas; const ARect: IDispatch; AValue: Byte);
procedure PaintDigits(ACanvas: TCanvas; const ARect: IDispatch);
procedure SetDigits(const AValue: NaturalNumber);
procedure SetDigitsInGroup(const AValue: NaturalNumber);
procedure SetNumberType(const AValue: TNumberType);
procedure SetPrecision(const AValue: TPrecision);
procedure SetRadix(const AValue: TRadix);
procedure ValueChanged;

## TCustomInstrumentDigitsPanelWithBackground
继承：TCustomInstrumentDigitsPanelWithBackground → TCustomInstrumentDigitsPanel → TCustomGraphicInstrumentWithInterior → TCustomGraphicInstrumentWithBackground → TGraphicControl → TControl → TComponent → TPersistent → TObject ｜ 单元：InstrumentDigitPanels


## TCustomInstrumentEdit
继承：TCustomInstrumentEdit → TCustomXPEdit → TXPCustomControl → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：InstrumentExtControls


## TCustomInstrumentGauge
继承：TCustomInstrumentGauge → TCustomGraphicInstrumentWithNoise → TCustomGraphicInstrumentWithBackground → TGraphicControl → TControl → TComponent → TPersistent → TObject ｜ 单元：InstrumentGauges

procedure DoGetScaleLabel(AValue: Double; var ALabelString: string);
procedure SetMax(const Value: Double);
procedure SetMin(const Value: Double);

## TCustomInstrumentGlyphButton
继承：TCustomInstrumentGlyphButton → TCustomInstrumentButton → TXPCustomSpeedButton → TXPBaseCustomSpeedButton → TXPCustomTransparentControl → TXPCustomControl → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：InstrumentButtons

procedure LEDChanged;

## TCustomInstrumentGraph
继承：TCustomInstrumentGraph → TCustomGraphicInstrumentWithInterior → TCustomGraphicInstrumentWithBackground → TGraphicControl → TControl → TComponent → TPersistent → TObject ｜ 单元：InstrumentGraphs

procedure BeginSetValues;
procedure DoGetValue(var AValue: Double; AIndex: Integer);
procedure EndSetValues;
procedure SetMax(AValue: Double);
procedure SetMin(AValue: Double);

## TCustomInstrumentKnob
继承：TCustomInstrumentKnob → TCustomInstrumentSlider → TXPCustomControl → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：InstrumentSliders


## TCustomInstrumentLabel
继承：TCustomInstrumentLabel → TCustomLabel → TGraphicControl → TControl → TComponent → TPersistent → TObject ｜ 单元：InstrumentLabels

procedure DoPaint(ACanvas: TCanvas; const ARect: IDispatch);

## TCustomInstrumentLEDDigits
继承：TCustomInstrumentLEDDigits → TCustomInstrumentDigitsPanel → TCustomGraphicInstrumentWithInterior → TCustomGraphicInstrumentWithBackground → TGraphicControl → TControl → TComponent → TPersistent → TObject ｜ 单元：InstrumentDigitPanels

procedure SetMaxValue(const AValue: Double);
procedure SetMinValue(const AValue: Double);

## TCustomInstrumentLEDsPanel
继承：TCustomInstrumentLEDsPanel → TCustomInstrumentDigitsPanelWithBackground → TCustomInstrumentDigitsPanel → TCustomGraphicInstrumentWithInterior → TCustomGraphicInstrumentWithBackground → TGraphicControl → TControl → TComponent → TPersistent → TObject ｜ 单元：InstrumentDigitPanels

procedure SetMaxValue(const AValue: Cardinal);
procedure SetMinValue(const AValue: Cardinal);

## TCustomInstrumentListBox
继承：TCustomInstrumentListBox → TCustomXPListBox → TXPCustomControl → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：InstrumentLists


## TCustomInstrumentMultiGraph
继承：TCustomInstrumentMultiGraph → TCustomInstrumentGraph → TCustomGraphicInstrumentWithInterior → TCustomGraphicInstrumentWithBackground → TGraphicControl → TControl → TComponent → TPersistent → TObject ｜ 单元：InstrumentGraphs


## TCustomInstrumentNumericPanel
继承：TCustomInstrumentNumericPanel → TCustomInstrumentDigitsPanelWithBackground → TCustomInstrumentDigitsPanel → TCustomGraphicInstrumentWithInterior → TCustomGraphicInstrumentWithBackground → TGraphicControl → TControl → TComponent → TPersistent → TObject ｜ 单元：InstrumentDigitPanels

procedure SetMaxValue(const AValue: Double);
procedure SetMinValue(const AValue: Double);

## TCustomInstrumentPanel
继承：TCustomInstrumentPanel → TXPCustomControl → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：InstrumentPanels

procedure PaintOnPanel(APanel: TCustomInstrumentBackgroundPanel);

## TCustomInstrumentProgressBar
继承：TCustomInstrumentProgressBar → TCustomGraphicInstrumentWithNoise → TCustomGraphicInstrumentWithBackground → TGraphicControl → TControl → TComponent → TPersistent → TObject ｜ 单元：InstrumentProgress

procedure SetMax(const Value: Double);
procedure SetMin(const Value: Double);

## TCustomInstrumentRadioButton
继承：TCustomInstrumentRadioButton → TCustomInstrumentCheckBox → TGraphicControl → TControl → TComponent → TPersistent → TObject ｜ 单元：InstrumentChecks

procedure TurnSiblingsOff;

## TCustomInstrumentRadioGroup
继承：TCustomInstrumentRadioGroup → TCustomInstrumentPanel → TXPCustomControl → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：InstrumentChecks


## TCustomInstrumentScrollBar
继承：TCustomInstrumentScrollBar → TCustomXPScrollBar → TXPCustomControl → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：InstrumentScrolls


## TCustomInstrumentShape
继承：TCustomInstrumentShape → TShape → TGraphicControl → TControl → TComponent → TPersistent → TObject ｜ 单元：InstrumentExtControls


## TCustomInstrumentSignal
继承：TCustomInstrumentSignal → TBaseDIOSignal → TInterfacedObject → TObject ｜ 单元：RT_CustomInstrument

procedure ForceGetSetValue;

## TCustomInstrumentSignalManager
继承：TCustomInstrumentSignalManager → TObject ｜ 单元：RT_CustomInstrument

procedure BeginUpdate;
procedure Create(ADesignedAreaPanel: TWinControl; const AGetSignalsIntf: IInterface);
procedure EndUpdate;
function GetInputSignal(Index: Integer): TCustomInstrumentSignal;
function GetInputSignalCount: Integer;
function GetOutputSignal(Index: Integer): TCustomInstrumentSignal;
function GetOutputSignalCount: Integer;
function GetSignalByName(const ASignalName: string): TCustomInstrumentSignal;
function IsInUpdate: Boolean;

## TCustomInstrumentSilkScreen
继承：TCustomInstrumentSilkScreen → TXPCustomControl → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：InstrumentPanels


## TCustomInstrumentSingleGraph
继承：TCustomInstrumentSingleGraph → TCustomInstrumentGraph → TCustomGraphicInstrumentWithInterior → TCustomGraphicInstrumentWithBackground → TGraphicControl → TControl → TComponent → TPersistent → TObject ｜ 单元：InstrumentGraphs


## TCustomInstrumentSlider
继承：TCustomInstrumentSlider → TXPCustomControl → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：InstrumentSliders

procedure Changed;
procedure DoGetHintText(AValue: Double; var AHintText: string);
procedure DoGetScaleLabel(AValue: Double; ASide: TInstrumentSide; var ALabelString: string);
procedure DrawHandle(ACanvas: TCanvas; xOffset: Integer; yOffset: Integer);
procedure DrawNumber(ACanvas: TCanvas; xOffset: Integer; yOffset: Integer; ANumberValue: Double; const ANumberStr: string);
procedure DrawSlot(ACanvas: TCanvas; xOffset: Integer; yOffset: Integer);
procedure DrawTick(ACanvas: TCanvas; xOffset: Integer; yOffset: Integer; ATicks: TInstrumentTicksFloat; ATickValue: Double; AGraphics: Pointer; APen: Pointer);
function GetPositionFromMouse(X: Integer; Y: Integer): Double;
function GetToolTipReferenceRect: IDispatch;
procedure SetMaxValue(AValue: Double);
procedure SetMinValue(AValue: Double);

## TCustomInstrumentTerminal
继承：TCustomInstrumentTerminal → TCustomInstrumentPanel → TXPCustomControl → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：InstrumentComms

procedure Clear;
procedure DoTransmitChar(AChar: Char);
procedure GetLines(ALines: TStrings);
procedure PutChar(AChar: Char; ATransmit: Boolean);
procedure PutString(const AString: string; ATransmit: Boolean);

## TCustomInstrumentTrackBar
继承：TCustomInstrumentTrackBar → TCustomInstrumentSlider → TXPCustomControl → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：InstrumentSliders


## TCustomLabel
继承：TCustomLabel → TGraphicControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.StdCtrls

property Canvas: TCanvas;  // read-only
property Caption: TCaption;
property GlowSize: Integer;
procedure AdjustBounds;
procedure DoDrawText(const Rect: IDispatch; Flags: Integer);
function GetLabelText: string;

## TCustomLabeledEdit
继承：TCustomLabeledEdit → TCustomEdit → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.ExtCtrls

property EditLabel: TBoundLabel;  // read-only
property LabelPosition: TLabelPosition;
property LabelSpacing: Integer;
procedure SetupInternalLabel;

## TCustomLinkLabel
继承：TCustomLinkLabel → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.ExtCtrls

property Alignment: TLinkAlignment;
property AutoSize: Boolean;
property UseVisualStyle: Boolean;
function UseThemes: Boolean;

## TCustomListBox
继承：TCustomListBox → TCustomMultiSelectListControl → TCustomListControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.StdCtrls

property AutoComplete: Boolean;
property AutoCompleteDelay: Cardinal;
property Canvas: TCanvas;  // read-only
property Count: Integer;
property Items: TStrings;
property ScrollWidth: Integer;
property Selected[Index: ?]: Boolean;
property TabStop: Boolean;
property TopIndex: Integer;
procedure DeleteString(Index: Integer);
procedure DrawItem(Index: Integer; const Rect: IDispatch; State: TOwnerDrawState);
function GetItemData(Index: Integer): NativeInt;
function InternalGetItemData(Index: Integer): NativeInt;
procedure InternalSetItemData(Index: Integer; AData: NativeInt);
function ItemAtPos(const Pos: IDispatch; Existing: Boolean): Integer;
function ItemRect(Index: Integer): IDispatch;
procedure LoadRecreateItems(RecreateItems: TStrings);
procedure MeasureItem(Index: Integer; var Height: Integer);
procedure ResetContent;
procedure SaveRecreateItems(RecreateItems: TStrings);
procedure SetItemData(Index: Integer; AData: NativeInt);

## TCustomListControl
继承：TCustomListControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.Controls

property ItemIndex: Integer;
procedure AddItem(Item: string; AObject: TObject);
procedure Clear;
procedure ClearSelection;
procedure CopySelection(Destination: TCustomListControl);
procedure DeleteSelected;
function GetCount: Integer;
function GetItemIndex: Integer;
procedure MoveSelection(Destination: TCustomListControl);
procedure SelectAll;
procedure SetItemIndex(const Value: Integer);

## TCustomListView
继承：TCustomListView → TCustomMultiSelectListControl → TCustomListControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.ComCtrls

property BoundingRect: TRect;  // read-only
property Canvas: TCanvas;  // read-only
property CheckBoxes: Boolean;
property Column[Index: ?]: TListColumn;  // read-only
property DropTarget: TListItem;
property FlatScrollBars: Boolean;
property FullDrag: Boolean;
property GridLines: Boolean;
property HotTrack: Boolean;
property HotTrackStyles: TListHotTrackStyles;
property ItemFocused: TListItem;
property Items: TListItems;
property RowSelect: Boolean;
property SelCount: Integer;  // read-only
property Selected: TListItem;
property TopItem: TListItem;  // read-only
property ViewOrigin: TPoint;  // read-only
property VisibleRowCount: Integer;  // read-only
property WorkAreas: TWorkAreas;  // read-only
function AlphaSort: Boolean;
procedure Arrange(Code: TListArrangement);
function CanChange(Item: TListItem; Change: Integer): Boolean;
function CanEdit(Item: TListItem): Boolean;
procedure Change(Item: TListItem; Change: Integer);
procedure ColClick(Column: TListColumn);
procedure ColRightClick(Column: TListColumn; const Point: IDispatch);
function CreateListItem: TListItem;
function CreateListItems: TListItems;
function CustomDraw(const ARect: IDispatch; Stage: TCustomDrawStage): Boolean;
function CustomDrawItem(Item: TListItem; State: TCustomDrawState; Stage: TCustomDrawStage): Boolean;
function CustomDrawSubItem(Item: TListItem; SubItem: Integer; State: TCustomDrawState; Stage: TCustomDrawStage): Boolean;
procedure Delete(Item: TListItem);
procedure DoInfoTip(Item: TListItem; var InfoTip: string);
procedure DoSelectItem(Item: TListItem; Selected: Boolean);
procedure DrawItem(Item: TListItem; const Rect: IDispatch; State: TOwnerDrawState);
procedure Edit(const Item: IDispatch);
function FindCaption(StartIndex: Integer; Value: string; Partial: Boolean; Inclusive: Boolean; Wrap: Boolean): TListItem;
function FindData(StartIndex: Integer; Value: Pointer; Inclusive: Boolean; Wrap: Boolean): TListItem;
function GetHitTestInfoAt(X: Integer; Y: Integer): THitTests;
function GetItemAt(X: Integer; Y: Integer): TListItem;
function GetNearestItem(const Point: IDispatch; Direction: TSearchDirection): TListItem;
function GetNextItem(StartItem: TListItem; Direction: TSearchDirection; States: TItemStates): TListItem;
function GetSearchString: string;
procedure InsertItem(Item: TListItem);
function IsCustomDrawn(Target: TCustomDrawTarget; Stage: TCustomDrawStage): Boolean;
function IsEditing: Boolean;
function OwnerDataFetch(Item: TListItem; Request: TItemRequest): Boolean;
function OwnerDataFind(Find: TItemFind; const FindString: string; const FindPosition: IDispatch; FindData: Pointer; StartIndex: Integer; Direction: TSearchDirection; Wrap: Boolean): Integer;
function OwnerDataHint(StartIndex: Integer; EndIndex: Integer): Boolean;
function OwnerDataStateChange(StartIndex: Integer; EndIndex: Integer; OldState: TItemStates; NewState: TItemStates): Boolean;
procedure Scroll(DX: Integer; DY: Integer);
procedure SetViewStyle(Value: TViewStyle);
function StringWidth(S: string): Integer;
procedure UpdateItems(FirstIndex: Integer; LastIndex: Integer);

## TCustomMaskEdit
继承：TCustomMaskEdit → TCustomEdit → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.Mask

property EditText: String;
property IsMasked: Boolean;  // read-only
property Text: TMaskedText;
function EditCanModify: Boolean;
function GetTextLen: Integer;
procedure Reset;
function Validate(const Value: string; var Pos: Integer): Boolean;
procedure ValidateEdit;
procedure ValidateError;

## TCustomMemo
继承：TCustomMemo → TCustomEdit → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.StdCtrls

property CaretPos: TPoint;
property Lines: TStrings;
function GetCaretPos: IDispatch;
procedure SetCaretPos(const Value: IDispatch);

## TCustomMemoryStream
继承：TCustomMemoryStream → TStream → TObject ｜ 单元：System.Classes

property Memory: Pointer;  // read-only
procedure SaveToFile(const FileName: string);
procedure SaveToStream(Stream: TStream);

## TCustomMultiSelectListControl
继承：TCustomMultiSelectListControl → TCustomListControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.Controls

property MultiSelect: Boolean;
property SelCount: Integer;  // read-only
function GetSelCount: Integer;
procedure SetMultiSelect(Value: Boolean);

## TCustomOutputSettings
继承：TCustomOutputSettings → TObject ｜ 单元：Rt_AbstractOutput

property Settings: IOutputSettings;

## TCustomPanel
继承：TCustomPanel → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.ExtCtrls

property ParentBackground: Boolean;

## TCustomPanningWindow
继承：TCustomPanningWindow → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.Controls

function GetIsPanning: Boolean;
function StartPanning(AHandle: NativeUInt; AControl: TControl): Boolean;
procedure StopPanning;

## TCustomRadioGroup
继承：TCustomRadioGroup → TCustomGroupBox → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.ExtCtrls

property Buttons[Index: ?]: TRadioButton;  // read-only
property WordWrap: Boolean;
function CanModify: Boolean;

## TCustomRichEdit
继承：TCustomRichEdit → TCustomMemo → TCustomEdit → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.ComCtrls

property ActiveLineNo: DWORD;  // read-only
property DefAttributes: TTextAttributes;
property PageRect: TRect;
property Paragraph: TParaAttributes;  // read-only
property SelAttributes: TTextAttributes;
property Zoom: Integer;
function FindText(const SearchStr: string; StartPos: Integer; Length: Integer; Options: TSearchTypes): Integer;
procedure Print(const Caption: string);
procedure RequestSize(const Rect: IDispatch);
procedure SelectionChange;

## TCustomStaticText
继承：TCustomStaticText → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.StdCtrls


## TCustomStatusBar
继承：TCustomStatusBar → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.ComCtrls

property AutoHint: Boolean;
property Canvas: TCanvas;  // read-only
property Panels: TStatusPanels;
property SimplePanel: Boolean;
property SimpleText: String;
property SizeGrip: Boolean;
property UseSystemFont: Boolean;
function CreatePanel: TStatusPanel;
function CreatePanels: TStatusPanels;
function DoHint: Boolean;
procedure DrawPanel(Panel: TStatusPanel; const Rect: IDispatch);

## TCustomTabControl
继承：TCustomTabControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.ComCtrls

property Canvas: TCanvas;  // read-only
property TabStop: Boolean;
function CanChange: Boolean;
function CanShowTab(TabIndex: Integer): Boolean;
procedure Change;
procedure DrawTab(TabIndex: Integer; const Rect: IDispatch; Active: Boolean);
function GetHitTestInfoAt(X: Integer; Y: Integer): THitTests;
function GetImageIndex(TabIndex: Integer): Integer;
function IndexOfTabAt(X: Integer; Y: Integer): Integer;
function RowCount: Integer;
procedure ScrollTabs(Delta: Integer);
procedure SetTabIndex(Value: Integer);
function TabRect(Index: Integer): IDispatch;

## TCustomTaskDialog
继承：TCustomTaskDialog → TComponent → TPersistent → TObject ｜ 单元：Vcl.Dialogs

property Button: TTaskDialogButtonItem;
property Buttons: TTaskDialogButtons;
property Caption: String;
property CommonButtons: TTaskDialogCommonButtons;
property CustomFooterIcon: TIcon;
property CustomMainIcon: TIcon;
property DefaultButton: TTaskDialogCommonButton;
property ExpandButtonCaption: String;
property Expanded: Boolean;  // read-only
property ExpandedText: String;
property Flags: TTaskDialogFlags;
property FooterIcon: TTaskDialogIcon;
property FooterText: String;
property Handle: HWND;  // read-only
property HelpContext: Integer;
property MainIcon: TTaskDialogIcon;
property ModalResult: TModalResult;
property ProgressBar: TTaskDialogProgressBar;
property RadioButton: TTaskDialogRadioButtonItem;  // read-only
property RadioButtons: TTaskDialogButtons;
property Text: String;
property Title: String;
property URL: String;  // read-only
property VerificationText: String;
function CallbackProc(HWND: HWND; Msg: Cardinal; wParam: NativeUInt; lParam: NativeInt; lpRefData: NativeInt): HRESULT;
function Execute: Boolean;

## TCustomTouchManager
继承：TCustomTouchManager → TPersistent → TObject ｜ 单元：Vcl.Controls

property GestureEngine: TCustomGestureEngine;
property GestureManager: TCustomGestureManager;
property InteractiveGestureOptions: TInteractiveGestureOptions;
property InteractiveGestures: TInteractiveGestures;
property ParentTabletOptions: Boolean;
property TabletOptions: TTabletOptions;
procedure ChangeNotification(AControl: TControl);
procedure Create(AControl: TControl);
function FindGesture(AGestureID: TGestureID): TCustomGestureCollectionItem;
procedure RemoveChangeNotification(AControl: TControl);
function SelectGesture(AGestureID: TGestureID): Boolean;
procedure UnselectGesture(AGestureID: TGestureID);

## TCustomTransparentControl
继承：TCustomTransparentControl → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.Controls

property InterceptMouse: Boolean;

## TCustomTrayIcon
继承：TCustomTrayIcon → TComponent → TPersistent → TObject ｜ 单元：Vcl.ExtCtrls

property Animate: Boolean;
property AnimateInterval: Cardinal;
property BalloonHint: String;
property BalloonTimeout: Integer;
property BalloonTitle: String;
property Hint: String;
property Icon: TIcon;
property IconIndex: Integer;
property Icons: TCustomImageList;
property PopupMenu: TPopupMenu;
property Visible: Boolean;
procedure DoOnAnimate(Sender: TObject);
procedure Refresh;
procedure SetDefaultIcon;
procedure SetIconIndex(Value: Integer);
procedure SetVisible(Value: Boolean);
procedure ShowBalloonHint;
procedure WindowProc(const Message: IDispatch);

## TCustomTreeView
继承：TCustomTreeView → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.ComCtrls

property Canvas: TCanvas;  // read-only
property DropTarget: TTreeNode;
property Selected: TTreeNode;
property SelectionCount: Cardinal;  // read-only
property Selections[Index: ?]: TTreeNode;  // read-only
property TopItem: TTreeNode;
procedure Added(Node: TTreeNode);
function AlphaSort(ARecurse: Boolean): Boolean;
function CanChange(Node: TTreeNode): Boolean;
function CanCollapse(Node: TTreeNode): Boolean;
function CanEdit(Node: TTreeNode): Boolean;
function CanExpand(Node: TTreeNode): Boolean;
procedure Change(Node: TTreeNode);
procedure ClearSelection(KeepPrimary: Boolean);
procedure Collapse(Node: TTreeNode);
function CreateNode: TTreeNode;
function CreateNodes: TTreeNodes;
function CustomDraw(const ARect: IDispatch; Stage: TCustomDrawStage): Boolean;
function CustomDrawItem(Node: TTreeNode; State: TCustomDrawState; Stage: TCustomDrawStage; var PaintImages: Boolean): Boolean;
procedure Delete(Node: TTreeNode);
procedure Deselect(Node: TTreeNode);
procedure Edit(const Item: IDispatch);
procedure Expand(Node: TTreeNode);
function FindNextToSelect: TTreeNode;
procedure FullCollapse;
procedure FullExpand;
function GetHitTestInfoAt(X: Integer; Y: Integer): THitTests;
procedure GetImageIndex(Node: TTreeNode);
function GetNodeAt(X: Integer; Y: Integer): TTreeNode;
procedure GetSelectedIndex(Node: TTreeNode);
function GetSelections(AList: TList): TTreeNode;
function IsCustomDrawn(Target: TCustomDrawTarget; Stage: TCustomDrawStage): Boolean;
function IsEditing: Boolean;
procedure LoadFromFile(const FileName: string);
procedure LoadFromStream(Stream: TStream);
procedure SaveToFile(const FileName: string);
procedure SaveToStream(Stream: TStream);
procedure Select(Node: TTreeNode; ShiftState: TShiftState);
procedure Subselect(Node: TTreeNode; Validate: Boolean);

## TCustomUpDown
继承：TCustomUpDown → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.ComCtrls

function CanChange: Boolean;
procedure Click(Button: TUDBtnType);

## TCustomVariantType
继承：TCustomVariantType → TObject ｜ 单元：System.Variants

property VarType: TVarType;  // read-only
procedure BinaryOp(const Left: IDispatch; const Right: IDispatch; const Operator: Integer);
procedure Cast(const Dest: IDispatch; const Source: IDispatch);
procedure CastTo(const Dest: IDispatch; const Source: IDispatch; const AVarType: Word);
procedure CastToOle(const Dest: IDispatch; const Source: IDispatch);
procedure Clear(const V: IDispatch);
procedure Compare(const Left: IDispatch; const Right: IDispatch; var Relationship: TVarCompareResult);
function CompareOp(const Left: IDispatch; const Right: IDispatch; const Operator: Integer): Boolean;
procedure Copy(const Dest: IDispatch; const Source: IDispatch; const Indirect: Boolean);
procedure Create;
function IsClear(const V: IDispatch): Boolean;
function LeftPromotion(const V: IDispatch; const Operator: Integer; out RequiredVarType: Word): Boolean;
function OlePromotion(const V: IDispatch; out RequiredVarType: Word): Boolean;
function RightPromotion(const V: IDispatch; const Operator: Integer; out RequiredVarType: Word): Boolean;
procedure UnaryOp(const Right: IDispatch; const Operator: Integer);

## TCustomXPEdit
继承：TCustomXPEdit → TXPCustomControl → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：XPEdits2

property CanUndo: Boolean;  // read-only
property Modified: Boolean;
property SelLength: Integer;
property SelStart: Integer;
property SelText: TXPString;
property Text: TCaption;
property UnicodeText: String;
property UseColor: Boolean;
function CalcInternalHeight: Integer;
procedure Change;
procedure ChangeHotFont(IsHot: Boolean);
procedure Clear;
procedure ClearSelection;
procedure ClearUndo;
procedure CopyToClipboard;
procedure CreateCaret;
procedure CutToClipboard;
procedure DestroyCaret;
procedure DoEndCapture;
procedure DrawInside(const ARect: IDispatch; AColor: TColor; AFrameColor: TColor; AHLTextColor: TColor; AHLColor: TColor; AFontColor: TColor);
function GetAutoWidth: Integer;
function GetBodyImage: TGraphic;
function GetBodyImageSize: Integer;
function GetCursorPos: IDispatch;
function GetEditDetails: IDispatch;
function GetEditorBounds: IDispatch;
function GetEditState: TThemedEdit;
function GetExcludeRect: IDispatch;
procedure InsertString(Str: string);
procedure InternalSetCursor;
procedure NumberFormatChanged;
procedure PasteFromClipboard;
procedure SelectAll;
procedure SetCaretPos(Value: Integer);
procedure SetText(const Value: TCaption);
procedure SetTransparent(const Value: Boolean);
procedure Undo;

## TCustomXPEditControlAutomation
继承：TCustomXPEditControlAutomation → TBaseControlAutomation → TBaseControlAutomation ｜ 单元：XPEdits2


## TCustomXPFloatSpinEdit
继承：TCustomXPFloatSpinEdit → TBaseXPSpinEdit → TCustomXPEdit → TXPCustomControl → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：XPEdits2


## TCustomXPListBox
继承：TCustomXPListBox → TXPCustomControl → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：XPLists

property TextMargin: Integer;  // read-only
procedure Clear;
procedure ClearSelection;
procedure ClickCheck;
procedure CorrectPopupItemHeight(var Value: Integer);
procedure DoDrawCheck(Index: Integer);
procedure DoDrawEmptySpace;
procedure DoDrawItem(Index: Integer);
procedure DoDrawItemText(Index: Integer; const ARect: IDispatch);
procedure DoOwnerDrawItem(Index: Integer);
function GetBackColor: TColor;
function GetFrameColor: TColor;
function GetFrameSize: Integer;
function GetItemsClientRect: IDispatch;
function GetItemTextHeight: Integer;
function GetItemTextWidth(Index: Integer): Integer;
function GetLookAndFeel: TXPLookAndFeel;
function GetNextItemIndex: Integer;
function GetPrevItemIndex: Integer;
function GetSelColor: TColor;
function GetSelTextColor: TColor;
function GetTextShift: Integer;
function GetThemeCheckSize(const ARect: IDispatch; AState: TThemedButton): IDispatch;
function ItemAtPos(const Pos: IDispatch; Existing: Boolean): Integer;
function ItemRect(Index: Integer): IDispatch;
procedure NCCalcSize(const Msg: IDispatch);
function NCPaint: Boolean;
procedure SelectAll;
procedure SelectionChanged;
procedure SetHideSelection(Value: Boolean);
procedure SetLookAndFeel(Value: TXPLookAndFeel);
procedure UpdateItemsAreaWidth;

## TCustomXPScrollBar
继承：TCustomXPScrollBar → TXPCustomControl → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：XPScrolls

procedure Change;
procedure DrawArrowBtn(const ARect: IDispatch; AState: Integer; AOffset: Integer; AIsUp: Boolean);
procedure DrawShaft(const ARect: IDispatch; AState: Integer);
procedure DrawThumb(const ARect: IDispatch; AState: Integer);
function IgnoreThemePainting: Boolean;
procedure Scroll(ScrollCode: TScrollCode; var ScrollPos: Integer);
procedure SetParams(APosition: Integer; AMin: Integer; AMax: Integer);
procedure UpdateView(const MousePt: IDispatch);

## TCustomXPSpinEdit
继承：TCustomXPSpinEdit → TBaseXPSpinEdit → TCustomXPEdit → TXPCustomControl → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：XPEdits2


## TCustomXPWideSpinEdit
继承：TCustomXPWideSpinEdit → TBaseXPSpinEdit → TCustomXPEdit → TXPCustomControl → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：XPEdits2


## TDashboardPanelOptions
继承：TDashboardPanelOptions → TPersistent → TObject ｜ 单元：RT_CustomInstrument

property Contraints: TSizeConstraints;
property Resizeable: Boolean;
procedure Create;

## TDataForEDM_UserLoggedInNotification
继承：TDataForEDM_UserLoggedInNotification → TInterfacedObject → TObject ｜ 单元：RT_ClientServerInterface

procedure Create(const ASessionId: WideString; const AUserName: WideString; const AHost: WideString);
function GetCanLogin: LongBool;
function GetDenyReason: WideString;
function GetHost: WideString;
function GetSessionID: WideString;
function GetUserName: WideString;
procedure SetCanLogin(const AData: LongBool);
procedure SetDenyReason(const AData: WideString);

## TDataLink
继承：TDataLink → TPersistent → TObject ｜ 单元：Data.DB

property Active: Boolean;  // read-only
property ActiveRecord: Integer;
property BOF: Boolean;  // read-only
property BufferCount: Integer;
property DataSet: TDataSet;  // read-only
property DataSource: TDataSource;
property DataSourceFixed: Boolean;
property Editing: Boolean;  // read-only
property Eof: Boolean;  // read-only
property ReadOnly: Boolean;
property RecordCount: Integer;  // read-only
procedure ActiveChanged;
procedure CheckBrowseMode;
procedure Create;
procedure DataEvent(Event: TDataEvent; Info: NativeInt);
procedure DataSetChanged;
procedure DataSetScrolled(Distance: Integer);
function Edit: Boolean;
procedure EditingChanged;
function ExecuteAction(Action: TBasicAction): Boolean;
procedure FocusControl(Field: TFieldRef);
function GetActiveRecord: Integer;
function GetBOF: Boolean;
function GetBufferCount: Integer;
function GetEOF: Boolean;
function GetRecordCount: Integer;
procedure LayoutChanged;
function MoveBy(Distance: Integer): Integer;
procedure RecordChanged(Field: TField);
procedure SetActiveRecord(Value: Integer);
procedure SetBufferCount(Value: Integer);
function UpdateAction(Action: TBasicAction): Boolean;
procedure UpdateData;
procedure UpdateRecord;

## TDataModule
继承：TDataModule → TComponent → TPersistent → TObject ｜ 单元：System.Classes

property DesignOffset: TPoint;
property DesignSize: TPoint;
property OldCreateOrder: Boolean;
property OnCreate: TNotifyEvent;
property OnDestroy: TNotifyEvent;
procedure CreateNew(AOwner: TComponent; Dummy: Integer);
procedure DoCreate;
procedure DoDestroy;
function HandleCreateException: Boolean;

## TDataSet
继承：TDataSet → TComponent → TPersistent → TObject ｜ 单元：Data.DB

property Active: Boolean;
property AggFields: TFields;  // read-only
property AutoCalcFields: Boolean;
property BlockReadSize: Integer;
property BOF: Boolean;  // read-only
property CanModify: Boolean;  // read-only
property CanRefresh: Boolean;  // read-only
property DataSetField: TDataSetField;
property DataSource: TDataSource;  // read-only
property Designer: TDataSetDesigner;  // read-only
property Eof: Boolean;  // read-only
property FieldCount: Integer;  // read-only
property FieldDefList: TFieldDefList;  // read-only
property FieldDefs: TFieldDefs;
property FieldList: TFieldList;  // read-only
property Fields: TFields;  // read-only
property FieldValues[Index: ?]: Variant;
property Filter: String;
property Filtered: Boolean;
property FilterOptions: TFilterOptions;
property Found: Boolean;  // read-only
property IsUniDirectional: Boolean;  // read-only
property Modified: Boolean;  // read-only
property ObjectView: Boolean;
property RecNo: Integer;
property RecordCount: Integer;  // read-only
property RecordSize: Word;  // read-only
property SparseArrays: Boolean;
property State: TDataSetState;  // read-only
procedure ActivateBuffers;
function ActiveBuffer: NativeInt;
function AllocRecordBuffer: PByte;
procedure Append;
procedure AppendRecord(const Values: array of TVarRec);
procedure BindFields(Binding: Boolean);
procedure BlockReadNext;
function BookmarkValid(Bookmark: TArray<System.Byte>): Boolean;
procedure CalculateFields(Buffer: NativeInt);
procedure Cancel;
procedure CheckActive;
procedure CheckBrowseMode;
procedure CheckFieldCompatibility(Field: TField; FieldDef: TFieldDef);
procedure CheckInactive;
procedure ClearBuffers;
procedure ClearCalcFields(Buffer: NativeInt);
procedure ClearFields;
procedure Close;
procedure CloseBlob(Field: TField);
procedure CloseCursor;
function CompareBookmarks(Bookmark1: TArray<System.Byte>; Bookmark2: TArray<System.Byte>): Integer;
function ControlsDisabled: Boolean;
function CopyFields(Source: TDataSet): Integer;
function CreateBlobStream(Field: TField; Mode: TBlobStreamMode): TStream;
procedure CreateFields;
function CreateNestedDataSet(DataSetField: TDataSetField): TDataSet;
procedure CursorPosChanged;
procedure DataConvert(Field: TField; Source: TArray<System.Byte>; var Dest: TArray<System.Byte>; ToNative: Boolean);
procedure DataEvent(Event: TDataEvent; Info: NativeInt);
function DefaultFields: Boolean;
procedure DefChanged(Sender: TObject);
procedure Delete;
procedure DestroyFields;
procedure DisableControls;
procedure DoAfterCancel;
procedure DoAfterClose;
procedure DoAfterDelete;
procedure DoAfterEdit;
procedure DoAfterInsert;
procedure DoAfterOpen;
procedure DoAfterPost;
procedure DoAfterRefresh;
procedure DoAfterScroll;
procedure DoBeforeCancel;
procedure DoBeforeClose;
procedure DoBeforeDelete;
procedure DoBeforeEdit;
procedure DoBeforeInsert;
procedure DoBeforeOpen;
procedure DoBeforePost;
procedure DoBeforeRefresh;
procedure DoBeforeScroll;
procedure DoOnCalcFields;
procedure DoOnNewRecord;
procedure Edit;
procedure EnableControls;
function FieldByName(const FieldName: string): TField;
function FindField(const FieldName: string): TField;
function FindFirst: Boolean;
function FindLast: Boolean;
function FindNext: Boolean;
function FindPrior: Boolean;
function FindRecord(Restart: Boolean; GoForward: Boolean): Boolean;
procedure First;
procedure FreeBookmark(Bookmark: TArray<System.Byte>);
procedure FreeFieldBuffers;
procedure FreeRecordBuffer(var Buffer: PByte);
function GetAggRecordCount(Grp: TGroupPosInd): Integer;
function GetAggregateValue(Field: TField): Variant;
function GetBlobFieldData(FieldNo: Integer; var Buffer: TArray<System.Byte>): Integer;
procedure GetBookmarkData(Buffer: NativeInt; Data: TArray<System.Byte>);
function GetBookmarkFlag(Buffer: NativeInt): TBookmarkFlag;
function GetBookmarkStr: AnsiString;
procedure GetCalcFields(Buffer: NativeInt);
function GetCalcFieldTypes: TFieldTypes;
function GetCanModify: Boolean;
function GetCanRefresh: Boolean;
function GetCurrentRecord(Buffer: NativeInt): Boolean;
function GetDataSource: TDataSource;
procedure GetDetailDataSets(List: TList<Data.DB.TDataSet>);
procedure GetDetailLinkFields(MasterFields: TList<Data.DB.TField>; DetailFields: TList<Data.DB.TField>);
function GetFieldData(Field: TField; var Buffer: TArray<System.Byte>): Boolean;
function GetFieldFullName(Field: TField): string;
procedure GetFieldList(List: TList<Data.DB.TField>; const FieldNames: string);
procedure GetFieldNames(List: TStrings);
function GetIsIndexField(Field: TField): Boolean;
function GetNextRecord: Boolean;
function GetNextRecords: Integer;
function GetPriorRecord: Boolean;
function GetPriorRecords: Integer;
function GetRecNo: Integer;
function GetRecord(Buffer: NativeInt; GetMode: TGetMode; DoCheck: Boolean): TGetResult;
function GetRecordCount: Integer;
function GetRecordSize: Word;
function GetStateFieldValue(State: TDataSetState; Field: TField): Variant;
procedure GotoBookmark(Bookmark: TArray<System.Byte>);
procedure InitFieldDefs;
procedure InitRecord(Buffer: NativeInt);
procedure Insert;
procedure InsertRecord(const Values: array of TVarRec);
procedure InternalAddRecord(Buffer: NativeInt; Append: Boolean);
procedure InternalCancel;
procedure InternalClose;
procedure InternalDelete;
procedure InternalEdit;
procedure InternalFirst;
procedure InternalGotoBookmark(Bookmark: TArray<System.Byte>);
procedure InternalHandleException;
procedure InternalInitFieldDefs;
procedure InternalInitRecord(Buffer: NativeInt);
procedure InternalInsert;
procedure InternalLast;
procedure InternalOpen;
procedure InternalPost;
procedure InternalRefresh;
procedure InternalSetToRecord(Buffer: NativeInt);
function IsCursorOpen: Boolean;
function IsEmpty: Boolean;
function IsLinkedTo(DataSource: TDataSource): Boolean;
function IsSequenced: Boolean;
procedure Last;
function Locate(const KeyFields: string; const KeyValues: Variant; Options: TLocateOptions): Boolean;
function Lookup(const KeyFields: string; const KeyValues: Variant; const ResultFields: string): Variant;
function MoveBy(Distance: Integer): Integer;
procedure Next;
procedure Open;
procedure OpenCursor(InfoQuery: Boolean);
procedure Post;
procedure Prior;
procedure PSEndTransaction(Commit: Boolean);
procedure PSExecute;
function PSExecuteStatement(const ASQL: string; AParams: TParams): Integer;
procedure PSGetAttributes(List: TList);
function PSGetCommandText: string;
function PSGetCommandType: TPSCommandType;
function PSGetDefaultOrder: TIndexDef;
function PSGetIndexDefs(IndexTypes: TIndexOptions): TIndexDefs;
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
procedure Refresh;
procedure RefreshInternalCalcFields(Buffer: NativeInt);
procedure ResetAggField(Field: TField);
procedure Resync(Mode: TResyncMode);
procedure SetActive(Value: Boolean);
procedure SetBlockReadSize(Value: Integer);
procedure SetBookmarkData(Buffer: NativeInt; Data: TArray<System.Byte>);
procedure SetBookmarkFlag(Buffer: NativeInt; Value: TBookmarkFlag);
procedure SetBookmarkStr(const Value: AnsiString);
procedure SetBufListSize(Value: Integer);
procedure SetCurrentRecord(Index: Integer);
procedure SetDataSetField(const Value: TDataSetField);
procedure SetFieldData(Field: TField; Buffer: TArray<System.Byte>);
procedure SetFieldDefProps(Field: TField; FieldDef: TFieldDef);
procedure SetFieldProps(Field: TField; FieldDef: TFieldDef);
procedure SetFields(const Values: array of TVarRec);
procedure SetFiltered(Value: Boolean);
procedure SetFilterOptions(Value: TFilterOptions);
procedure SetFilterText(const Value: string);
procedure SetRecNo(Value: Integer);
procedure SetStateFieldValue(State: TDataSetState; Field: TField; const Value: Variant);
function Translate(Src: PAnsiChar; Dest: PAnsiChar; ToOem: Boolean): Integer;
procedure UpdateCursorPos;
procedure UpdateIndexDefs;
procedure UpdateRecord;
function UpdateStatus: TUpdateStatus;

## TDataSetAction
继承：TDataSetAction → TAction → TCustomAction → TContainedAction ｜ 单元：Vcl.DBActns

property DataSource: TDataSource;
function GetDataSet(Target: TObject): TDataSet;

## TDataSetCancel
继承：TDataSetCancel → TDataSetAction → TAction → TCustomAction → TContainedAction ｜ 单元：Vcl.DBActns

property DataSource: TDataSource;

## TDataSetDelete
继承：TDataSetDelete → TDataSetAction → TAction → TCustomAction → TContainedAction ｜ 单元：Vcl.DBActns

property DataSource: TDataSource;

## TDataSetDesigner
继承：TDataSetDesigner → TObject ｜ 单元：Data.DB

property DataSet: TDataSet;  // read-only
procedure BeginDesign;
procedure Create(DataSet: TDataSet);
procedure DataEvent(Event: TDataEvent; Info: NativeInt);
procedure EndDesign;

## TDataSetEdit
继承：TDataSetEdit → TDataSetAction → TAction → TCustomAction → TContainedAction ｜ 单元：Vcl.DBActns

property DataSource: TDataSource;

## TDataSetField
继承：TDataSetField → TObjectField → TField → TComponent → TPersistent → TObject ｜ 单元：Data.DB

property IncludeObjectField: Boolean;
property NestedDataSet: TDataSet;  // read-only

## TDataSetFirst
继承：TDataSetFirst → TDataSetAction → TAction → TCustomAction → TContainedAction ｜ 单元：Vcl.DBActns

property DataSource: TDataSource;

## TDataSetInsert
继承：TDataSetInsert → TDataSetAction → TAction → TCustomAction → TContainedAction ｜ 单元：Vcl.DBActns

property DataSource: TDataSource;

## TDataSetLast
继承：TDataSetLast → TDataSetAction → TAction → TCustomAction → TContainedAction ｜ 单元：Vcl.DBActns

property DataSource: TDataSource;

## TDataSetNext
继承：TDataSetNext → TDataSetAction → TAction → TCustomAction → TContainedAction ｜ 单元：Vcl.DBActns

property DataSource: TDataSource;

## TDataSetPost
继承：TDataSetPost → TDataSetAction → TAction → TCustomAction → TContainedAction ｜ 单元：Vcl.DBActns

property DataSource: TDataSource;

## TDataSetPrior
继承：TDataSetPrior → TDataSetAction → TAction → TCustomAction → TContainedAction ｜ 单元：Vcl.DBActns

property DataSource: TDataSource;

## TDataSetRefresh
继承：TDataSetRefresh → TDataSetAction → TAction → TCustomAction → TContainedAction ｜ 单元：Vcl.DBActns

property DataSource: TDataSource;

## TDataSource
继承：TDataSource → TComponent → TPersistent → TObject ｜ 单元：Data.DB

property AutoEdit: Boolean;
property DataSet: TDataSet;
property Enabled: Boolean;
property OnDataChange: TDataChangeEvent;
property OnStateChange: TNotifyEvent;
property OnUpdateData: TNotifyEvent;
property State: TDataSetState;  // read-only
procedure Edit;
function IsLinkedTo(DataSet: TDataSet): Boolean;

## TDataSourceLink
继承：TDataSourceLink → TDataLink → TPersistent → TObject ｜ 单元：Vcl.DBCtrls

procedure Create;

## TDateField
继承：TDateField → TDateTimeField → TField → TComponent → TPersistent → TObject ｜ 单元：Data.DB


## TDateTimeField
继承：TDateTimeField → TField → TComponent → TPersistent → TObject ｜ 单元：Data.DB

property DisplayFormat: string;
property EditMask: TEditMask;
property Value: TDateTime;

## TDateTimePicker
继承：TDateTimePicker → TCommonCalendar → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.ComCtrls

property Align: TAlign;
property Anchors: TAnchors;
property BevelEdges: TBevelEdges;
property BevelInner: TBevelCut;
property BevelKind: TBevelKind;
property BevelOuter: TBevelCut;
property BevelWidth: TBevelWidth;
property BiDiMode: TBiDiMode;
property CalAlignment: TDTCalAlignment;
property CalColors: TMonthCalColors;
property Checked: Boolean;
property Color: TColor;
property Constraints: TSizeConstraints;
property Date: TDate;
property DateFormat: TDTDateFormat;
property DateMode: TDTDateMode;
property DateTime: TDateTime;
property DoubleBuffered: Boolean;
property DragCursor: TCursor;
property DragKind: TDragKind;
property DragMode: TDragMode;
property DroppedDown: Boolean;  // read-only
property Enabled: Boolean;
property Font: TFont;
property Format: string;
property ImeMode: TImeMode;
property ImeName: TImeName;
property Kind: TDateTimeKind;
property MaxDate: TDate;
property MinDate: TDate;
property OnChange: TNotifyEvent;
property OnClick: TNotifyEvent;
property OnCloseUp: TNotifyEvent;
property OnContextPopup: TContextPopupEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnDropDown: TNotifyEvent;
property OnEndDock: TEndDragEvent;
property OnEndDrag: TEndDragEvent;
property OnEnter: TNotifyEvent;
property OnExit: TNotifyEvent;
property OnGesture: TGestureEvent;
property OnKeyDown: TKeyEvent;
property OnKeyPress: TKeyPressEvent;
property OnKeyUp: TKeyEvent;
property OnMouseEnter: TNotifyEvent;
property OnMouseLeave: TNotifyEvent;
property OnStartDock: TStartDockEvent;
property OnStartDrag: TStartDragEvent;
property OnUserInput: TDTParseInputEvent;
property ParentBiDiMode: Boolean;
property ParentColor: Boolean;
property ParentDoubleBuffered: Boolean;
property ParentFont: Boolean;
property ParentShowHint: Boolean;
property ParseInput: Boolean;
property PopupMenu: TPopupMenu;
property ShowCheckbox: Boolean;
property ShowHint: Boolean;
property StyleElements: TStyleElements;
property TabOrder: TTabOrder;
property TabStop: Boolean;
property Time: TTime;
property Touch: TTouchManager;
property Visible: Boolean;
procedure Change;

## TDateTimePickerStyleHook
继承：TDateTimePickerStyleHook → TMouseTrackControlStyleHook → TMouseTrackControlStyleHook ｜ 单元：Vcl.ComCtrls


## TDBBitConverter
继承：TDBBitConverter → TBitConverter → TObject ｜ 单元：Data.DB

function UnsafeInToInterface(const B: TArray<System.Byte>; Offset: Integer): IInterface;
function UnsafeInToVariant(const B: TArray<System.Byte>; Offset: Integer): Variant;

## TDBCheckBox
继承：TDBCheckBox → TCustomCheckBox → TButtonControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.DBCtrls

property Action: TBasicAction;
property Align: TAlign;
property Alignment: TLeftRight;
property AllowGrayed: Boolean;
property Anchors: TAnchors;
property BiDiMode: TBiDiMode;
property Caption: TCaption;
property Checked: Boolean;
property Color: TColor;
property Constraints: TSizeConstraints;
property Ctl3D: Boolean;
property DataField: string;
property DataSource: TDataSource;
property DragCursor: TCursor;
property DragKind: TDragKind;
property DragMode: TDragMode;
property Enabled: Boolean;
property Field: TField;  // read-only
property Font: TFont;
property OnClick: TNotifyEvent;
property OnContextPopup: TContextPopupEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnEndDock: TEndDragEvent;
property OnEndDrag: TEndDragEvent;
property OnEnter: TNotifyEvent;
property OnExit: TNotifyEvent;
property OnKeyDown: TKeyEvent;
property OnKeyPress: TKeyPressEvent;
property OnKeyUp: TKeyEvent;
property OnMouseActivate: TMouseActivateEvent;
property OnMouseDown: TMouseEvent;
property OnMouseEnter: TNotifyEvent;
property OnMouseLeave: TNotifyEvent;
property OnMouseMove: TMouseMoveEvent;
property OnMouseUp: TMouseEvent;
property OnStartDock: TStartDockEvent;
property OnStartDrag: TStartDragEvent;
property ParentBiDiMode: Boolean;
property ParentColor: Boolean;
property ParentCtl3D: Boolean;
property ParentFont: Boolean;
property ParentShowHint: Boolean;
property PopupMenu: TPopupMenu;
property ReadOnly: Boolean;
property ShowHint: Boolean;
property State: TCheckBoxState;
property StyleElements: TStyleElements;
property TabOrder: TTabOrder;
property TabStop: Boolean;
property ValueChecked: string;
property ValueUnchecked: string;
property Visible: Boolean;
property WordWrap: Boolean;

## TDBComboBox
继承：TDBComboBox → TCustomComboBox → TCustomCombo → TCustomListControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.DBCtrls

property Align: TAlign;
property Anchors: TAnchors;
property AutoComplete: Boolean;
property AutoDropDown: Boolean;
property BevelEdges: TBevelEdges;
property BevelInner: TBevelCut;
property BevelKind: TBevelKind;
property BevelOuter: TBevelCut;
property BevelWidth: TBevelWidth;
property BiDiMode: TBiDiMode;
property CharCase: TEditCharCase;
property Color: TColor;
property Constraints: TSizeConstraints;
property Ctl3D: Boolean;
property DataField: string;
property DataSource: TDataSource;
property DragCursor: TCursor;
property DragKind: TDragKind;
property DragMode: TDragMode;
property DropDownCount: Integer;
property Enabled: Boolean;
property Field: TField;  // read-only
property Font: TFont;
property ImeMode: TImeMode;
property ImeName: TImeName;
property ItemHeight: Integer;
property Items: TStrings;
property OnChange: TNotifyEvent;
property OnClick: TNotifyEvent;
property OnContextPopup: TContextPopupEvent;
property OnDblClick: TNotifyEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnDrawItem: TDrawItemEvent;
property OnDropDown: TNotifyEvent;
property OnEndDock: TEndDragEvent;
property OnEndDrag: TEndDragEvent;
property OnEnter: TNotifyEvent;
property OnExit: TNotifyEvent;
property OnGesture: TGestureEvent;
property OnKeyDown: TKeyEvent;
property OnKeyPress: TKeyPressEvent;
property OnKeyUp: TKeyEvent;
property OnMeasureItem: TMeasureItemEvent;
property OnMouseEnter: TNotifyEvent;
property OnMouseLeave: TNotifyEvent;
property OnStartDock: TStartDockEvent;
property OnStartDrag: TStartDragEvent;
property ParentBiDiMode: Boolean;
property ParentColor: Boolean;
property ParentCtl3D: Boolean;
property ParentFont: Boolean;
property ParentShowHint: Boolean;
property PopupMenu: TPopupMenu;
property ReadOnly: Boolean;
property ShowHint: Boolean;
property Sorted: Boolean;
property Style: TComboBoxStyle;
property StyleElements: TStyleElements;
property TabOrder: TTabOrder;
property TabStop: Boolean;
property Text: TCaption;
property Touch: TTouchManager;
property Visible: Boolean;

## TDBEdit
继承：TDBEdit → TCustomMaskEdit → TCustomEdit → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.DBCtrls

property Align: TAlign;
property Anchors: TAnchors;
property AutoSelect: Boolean;
property AutoSize: Boolean;
property BevelEdges: TBevelEdges;
property BevelInner: TBevelCut;
property BevelKind: TBevelKind;
property BevelOuter: TBevelCut;
property BevelWidth: TBevelWidth;
property BiDiMode: TBiDiMode;
property BorderStyle: TBorderStyle;
property CharCase: TEditCharCase;
property Color: TColor;
property Constraints: TSizeConstraints;
property Ctl3D: Boolean;
property DataField: string;
property DataSource: TDataSource;
property DragCursor: TCursor;
property DragKind: TDragKind;
property DragMode: TDragMode;
property Enabled: Boolean;
property Field: TField;  // read-only
property Font: TFont;
property ImeMode: TImeMode;
property ImeName: TImeName;
property MaxLength: Integer;
property OnChange: TNotifyEvent;
property OnClick: TNotifyEvent;
property OnContextPopup: TContextPopupEvent;
property OnDblClick: TNotifyEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnEndDock: TEndDragEvent;
property OnEndDrag: TEndDragEvent;
property OnEnter: TNotifyEvent;
property OnExit: TNotifyEvent;
property OnGesture: TGestureEvent;
property OnKeyDown: TKeyEvent;
property OnKeyPress: TKeyPressEvent;
property OnKeyUp: TKeyEvent;
property OnMouseActivate: TMouseActivateEvent;
property OnMouseDown: TMouseEvent;
property OnMouseEnter: TNotifyEvent;
property OnMouseLeave: TNotifyEvent;
property OnMouseMove: TMouseMoveEvent;
property OnMouseUp: TMouseEvent;
property OnStartDock: TStartDockEvent;
property OnStartDrag: TStartDragEvent;
property ParentBiDiMode: Boolean;
property ParentColor: Boolean;
property ParentCtl3D: Boolean;
property ParentFont: Boolean;
property ParentShowHint: Boolean;
property PasswordChar: Char;
property PopupMenu: TPopupMenu;
property ReadOnly: Boolean;
property ShowHint: Boolean;
property StyleElements: TStyleElements;
property TabOrder: TTabOrder;
property TabStop: Boolean;
property Touch: TTouchManager;
property Visible: Boolean;

## TDBImage
继承：TDBImage → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.DBCtrls

property Align: TAlign;
property Anchors: TAnchors;
property AutoDisplay: Boolean;
property BorderStyle: TBorderStyle;
property Center: Boolean;
property Color: TColor;
property Constraints: TSizeConstraints;
property Ctl3D: Boolean;
property DataField: string;
property DataSource: TDataSource;
property DragCursor: TCursor;
property DragKind: TDragKind;
property DragMode: TDragMode;
property Enabled: Boolean;
property Field: TField;  // read-only
property Font: TFont;
property OnClick: TNotifyEvent;
property OnContextPopup: TContextPopupEvent;
property OnDblClick: TNotifyEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnEndDock: TEndDragEvent;
property OnEndDrag: TEndDragEvent;
property OnEnter: TNotifyEvent;
property OnExit: TNotifyEvent;
property OnGesture: TGestureEvent;
property OnKeyDown: TKeyEvent;
property OnKeyPress: TKeyPressEvent;
property OnKeyUp: TKeyEvent;
property OnMouseActivate: TMouseActivateEvent;
property OnMouseDown: TMouseEvent;
property OnMouseEnter: TNotifyEvent;
property OnMouseLeave: TNotifyEvent;
property OnMouseMove: TMouseMoveEvent;
property OnMouseUp: TMouseEvent;
property OnStartDock: TStartDockEvent;
property OnStartDrag: TStartDragEvent;
property ParentColor: Boolean;
property ParentCtl3D: Boolean;
property ParentFont: Boolean;
property ParentShowHint: Boolean;
property Picture: TPicture;
property PopupMenu: TPopupMenu;
property Proportional: Boolean;
property QuickDraw: Boolean;
property ReadOnly: Boolean;
property ShowHint: Boolean;
property Stretch: Boolean;
property TabOrder: TTabOrder;
property TabStop: Boolean;
property Touch: TTouchManager;
property Visible: Boolean;
procedure CopyToClipboard;
procedure CutToClipboard;
procedure LoadPicture;
procedure PasteFromClipboard;

## TDBListBox
继承：TDBListBox → TCustomListBox → TCustomMultiSelectListControl → TCustomListControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.DBCtrls

property Align: TAlign;
property Anchors: TAnchors;
property AutoComplete: Boolean;
property BevelEdges: TBevelEdges;
property BevelInner: TBevelCut;
property BevelKind: TBevelKind;
property BevelOuter: TBevelCut;
property BevelWidth: TBevelWidth;
property BiDiMode: TBiDiMode;
property BorderStyle: TBorderStyle;
property Color: TColor;
property Constraints: TSizeConstraints;
property Ctl3D: Boolean;
property DataField: string;
property DataSource: TDataSource;
property DragCursor: TCursor;
property DragKind: TDragKind;
property DragMode: TDragMode;
property Enabled: Boolean;
property Field: TField;  // read-only
property Font: TFont;
property ImeMode: TImeMode;
property ImeName: TImeName;
property IntegralHeight: Boolean;
property ItemHeight: Integer;
property Items: TStrings;
property OnClick: TNotifyEvent;
property OnContextPopup: TContextPopupEvent;
property OnDblClick: TNotifyEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnDrawItem: TDrawItemEvent;
property OnEndDock: TEndDragEvent;
property OnEndDrag: TEndDragEvent;
property OnEnter: TNotifyEvent;
property OnExit: TNotifyEvent;
property OnGesture: TGestureEvent;
property OnKeyDown: TKeyEvent;
property OnKeyPress: TKeyPressEvent;
property OnKeyUp: TKeyEvent;
property OnMeasureItem: TMeasureItemEvent;
property OnMouseActivate: TMouseActivateEvent;
property OnMouseDown: TMouseEvent;
property OnMouseEnter: TNotifyEvent;
property OnMouseLeave: TNotifyEvent;
property OnMouseMove: TMouseMoveEvent;
property OnMouseUp: TMouseEvent;
property OnStartDock: TStartDockEvent;
property OnStartDrag: TStartDragEvent;
property ParentBiDiMode: Boolean;
property ParentColor: Boolean;
property ParentCtl3D: Boolean;
property ParentFont: Boolean;
property ParentShowHint: Boolean;
property PopupMenu: TPopupMenu;
property ReadOnly: Boolean;
property ShowHint: Boolean;
property Style: TListBoxStyle;
property StyleElements: TStyleElements;
property TabOrder: TTabOrder;
property TabStop: Boolean;
property Touch: TTouchManager;
property Visible: Boolean;

## TDBLookupComboBox
继承：TDBLookupComboBox → TCustomDBLookupComboBox → TDBLookupControl → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.DBCtrls

property Align: TAlign;
property Anchors: TAnchors;
property BevelEdges: TBevelEdges;
property BevelInner: TBevelCut;
property BevelKind: TBevelKind;
property BevelOuter: TBevelCut;
property BevelWidth: TBevelWidth;
property BiDiMode: TBiDiMode;
property Color: TColor;
property Constraints: TSizeConstraints;
property Ctl3D: Boolean;
property DataField: string;
property DataSource: TDataSource;
property DragCursor: TCursor;
property DragKind: TDragKind;
property DragMode: TDragMode;
property DropDownAlign: TDropDownAlign;
property DropDownRows: Integer;
property DropDownWidth: Integer;
property Enabled: Boolean;
property Font: TFont;
property ImeMode: TImeMode;
property ImeName: TImeName;
property KeyField: string;
property ListField: string;
property ListFieldIndex: Integer;
property ListSource: TDataSource;
property NullValueKey: TShortCut;
property OnClick: TNotifyEvent;
property OnCloseUp: TNotifyEvent;
property OnContextPopup: TContextPopupEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnDropDown: TNotifyEvent;
property OnEndDock: TEndDragEvent;
property OnEndDrag: TEndDragEvent;
property OnEnter: TNotifyEvent;
property OnExit: TNotifyEvent;
property OnGesture: TGestureEvent;
property OnKeyDown: TKeyEvent;
property OnKeyPress: TKeyPressEvent;
property OnKeyUp: TKeyEvent;
property OnMouseActivate: TMouseActivateEvent;
property OnMouseDown: TMouseEvent;
property OnMouseEnter: TNotifyEvent;
property OnMouseLeave: TNotifyEvent;
property OnMouseMove: TMouseMoveEvent;
property OnMouseUp: TMouseEvent;
property OnStartDock: TStartDockEvent;
property OnStartDrag: TStartDragEvent;
property ParentBiDiMode: Boolean;
property ParentColor: Boolean;
property ParentCtl3D: Boolean;
property ParentFont: Boolean;
property ParentShowHint: Boolean;
property PopupMenu: TPopupMenu;
property ReadOnly: Boolean;
property ShowHint: Boolean;
property StyleElements: TStyleElements;
property TabOrder: TTabOrder;
property TabStop: Boolean;
property Touch: TTouchManager;
property Visible: Boolean;

## TDBLookupControl
继承：TDBLookupControl → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.DBCtrls

property Field: TField;  // read-only
function CanModify: Boolean;
function GetBorderSize: Integer;
function GetTextHeight: Integer;
procedure KeyValueChanged;
procedure ListLinkDataChanged;
function LocateKey: Boolean;
procedure ProcessSearchKey(Key: Char);
procedure SelectKeyValue(const Value: Variant);
procedure UpdateDataFields;
procedure UpdateListFields;

## TDBLookupListBox
继承：TDBLookupListBox → TDBLookupControl → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.DBCtrls

property Align: TAlign;
property Anchors: TAnchors;
property BevelEdges: TBevelEdges;
property BevelInner: TBevelCut;
property BevelKind: TBevelKind;
property BevelOuter: TBevelCut;
property BevelWidth: TBevelWidth;
property BiDiMode: TBiDiMode;
property BorderStyle: TBorderStyle;
property Color: TColor;
property Constraints: TSizeConstraints;
property Ctl3D: Boolean;
property DataField: string;
property DataSource: TDataSource;
property DragCursor: TCursor;
property DragKind: TDragKind;
property DragMode: TDragMode;
property Enabled: Boolean;
property Font: TFont;
property ImeMode: TImeMode;
property ImeName: TImeName;
property KeyField: string;
property KeyValue: Variant;
property ListField: string;
property ListFieldIndex: Integer;
property ListSource: TDataSource;
property NullValueKey: TShortCut;
property OnClick: TNotifyEvent;
property OnContextPopup: TContextPopupEvent;
property OnDblClick: TNotifyEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnEndDock: TEndDragEvent;
property OnEndDrag: TEndDragEvent;
property OnEnter: TNotifyEvent;
property OnExit: TNotifyEvent;
property OnGesture: TGestureEvent;
property OnKeyDown: TKeyEvent;
property OnKeyPress: TKeyPressEvent;
property OnKeyUp: TKeyEvent;
property OnMouseActivate: TMouseActivateEvent;
property OnMouseDown: TMouseEvent;
property OnMouseEnter: TNotifyEvent;
property OnMouseLeave: TNotifyEvent;
property OnMouseMove: TMouseMoveEvent;
property OnMouseUp: TMouseEvent;
property OnStartDock: TStartDockEvent;
property OnStartDrag: TStartDragEvent;
property ParentBiDiMode: Boolean;
property ParentColor: Boolean;
property ParentCtl3D: Boolean;
property ParentFont: Boolean;
property ParentShowHint: Boolean;
property PopupMenu: TPopupMenu;
property ReadOnly: Boolean;
property RowCount: Integer;
property SelectedItem: String;  // read-only
property ShowHint: Boolean;
property StyleElements: TStyleElements;
property TabOrder: TTabOrder;
property TabStop: Boolean;
property Touch: TTouchManager;
property Visible: Boolean;

## TDBMemo
继承：TDBMemo → TCustomMemo → TCustomEdit → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.DBCtrls

property Align: TAlign;
property Alignment: TAlignment;
property Anchors: TAnchors;
property AutoDisplay: Boolean;
property BevelEdges: TBevelEdges;
property BevelInner: TBevelCut;
property BevelKind: TBevelKind;
property BevelOuter: TBevelCut;
property BevelWidth: TBevelWidth;
property BiDiMode: TBiDiMode;
property BorderStyle: TBorderStyle;
property Color: TColor;
property Constraints: TSizeConstraints;
property Ctl3D: Boolean;
property DataField: string;
property DataSource: TDataSource;
property DragCursor: TCursor;
property DragKind: TDragKind;
property DragMode: TDragMode;
property Enabled: Boolean;
property Field: TField;  // read-only
property Font: TFont;
property HideSelection: Boolean;
property ImeMode: TImeMode;
property ImeName: TImeName;
property MaxLength: Integer;
property OnChange: TNotifyEvent;
property OnClick: TNotifyEvent;
property OnContextPopup: TContextPopupEvent;
property OnDblClick: TNotifyEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnEndDock: TEndDragEvent;
property OnEndDrag: TEndDragEvent;
property OnEnter: TNotifyEvent;
property OnExit: TNotifyEvent;
property OnGesture: TGestureEvent;
property OnKeyDown: TKeyEvent;
property OnKeyPress: TKeyPressEvent;
property OnKeyUp: TKeyEvent;
property OnMouseActivate: TMouseActivateEvent;
property OnMouseDown: TMouseEvent;
property OnMouseEnter: TNotifyEvent;
property OnMouseLeave: TNotifyEvent;
property OnMouseMove: TMouseMoveEvent;
property OnMouseUp: TMouseEvent;
property OnStartDock: TStartDockEvent;
property OnStartDrag: TStartDragEvent;
property ParentBiDiMode: Boolean;
property ParentColor: Boolean;
property ParentCtl3D: Boolean;
property ParentFont: Boolean;
property ParentShowHint: Boolean;
property PopupMenu: TPopupMenu;
property ReadOnly: Boolean;
property ScrollBars: TScrollStyle;
property ShowHint: Boolean;
property StyleElements: TStyleElements;
property TabOrder: TTabOrder;
property TabStop: Boolean;
property Touch: TTouchManager;
property Visible: Boolean;
property WantReturns: Boolean;
property WantTabs: Boolean;
property WordWrap: Boolean;
procedure LoadMemo;

## TDBNavigator
继承：TDBNavigator → TCustomPanel → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.DBCtrls

property Align: TAlign;
property Anchors: TAnchors;
property BeforeAction: ENavClick;
property ConfirmDelete: Boolean;
property Constraints: TSizeConstraints;
property Ctl3D: Boolean;
property DataSource: TDataSource;
property DragCursor: TCursor;
property DragKind: TDragKind;
property DragMode: TDragMode;
property Enabled: Boolean;
property Flat: Boolean;
property Hints: TStrings;
property Kind: TDBNavigatorKind;
property MaxErrors: Integer;
property OnClick: ENavClick;
property OnContextPopup: TContextPopupEvent;
property OnDblClick: TNotifyEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnEndDock: TEndDragEvent;
property OnEndDrag: TEndDragEvent;
property OnEnter: TNotifyEvent;
property OnExit: TNotifyEvent;
property OnResize: TNotifyEvent;
property OnStartDock: TStartDockEvent;
property OnStartDrag: TStartDragEvent;
property ParentCtl3D: Boolean;
property ParentShowHint: Boolean;
property PopupMenu: TPopupMenu;
property ShowHint: Boolean;
property TabOrder: TTabOrder;
property TabStop: Boolean;
property Visible: Boolean;
property VisibleButtons: TNavButtonSet;
procedure BtnClick(Index: TNavigateBtn);
procedure SetButtonGlyph(Index: TNavigateBtn);

## TDBRadioGroup
继承：TDBRadioGroup → TCustomRadioGroup → TCustomGroupBox → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.DBCtrls

property Align: TAlign;
property Anchors: TAnchors;
property BiDiMode: TBiDiMode;
property Caption: TCaption;
property Color: TColor;
property Columns: Integer;
property Constraints: TSizeConstraints;
property Ctl3D: Boolean;
property DataField: string;
property DataSource: TDataSource;
property DragCursor: TCursor;
property DragKind: TDragKind;
property DragMode: TDragMode;
property Enabled: Boolean;
property Field: TField;  // read-only
property Font: TFont;
property ItemIndex: Integer;
property Items: TStrings;
property OnChange: TNotifyEvent;
property OnClick: TNotifyEvent;
property OnContextPopup: TContextPopupEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnEndDock: TEndDragEvent;
property OnEndDrag: TEndDragEvent;
property OnEnter: TNotifyEvent;
property OnExit: TNotifyEvent;
property OnGesture: TGestureEvent;
property OnMouseEnter: TNotifyEvent;
property OnMouseLeave: TNotifyEvent;
property OnStartDock: TStartDockEvent;
property OnStartDrag: TStartDragEvent;
property ParentBackground: Boolean;
property ParentBiDiMode: Boolean;
property ParentColor: Boolean;
property ParentCtl3D: Boolean;
property ParentFont: Boolean;
property ParentShowHint: Boolean;
property PopupMenu: TPopupMenu;
property ReadOnly: Boolean;
property ShowHint: Boolean;
property StyleElements: TStyleElements;
property TabOrder: TTabOrder;
property TabStop: Boolean;
property Touch: TTouchManager;
property Value: String;
property Values: TStrings;
property Visible: Boolean;
procedure Change;

## TDBRichEdit
继承：TDBRichEdit → TCustomRichEdit → TCustomMemo → TCustomEdit → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.DBCtrls

property Align: TAlign;
property Alignment: TAlignment;
property Anchors: TAnchors;
property AutoDisplay: Boolean;
property BevelEdges: TBevelEdges;
property BevelInner: TBevelCut;
property BevelKind: TBevelKind;
property BevelOuter: TBevelCut;
property BevelWidth: TBevelWidth;
property BiDiMode: TBiDiMode;
property BorderStyle: TBorderStyle;
property Color: TColor;
property Constraints: TSizeConstraints;
property Ctl3D: Boolean;
property DataField: string;
property DataSource: TDataSource;
property DragCursor: TCursor;
property DragKind: TDragKind;
property DragMode: TDragMode;
property Enabled: Boolean;
property Field: TField;  // read-only
property Font: TFont;
property HideScrollBars: Boolean;
property HideSelection: Boolean;
property ImeMode: TImeMode;
property ImeName: TImeName;
property MaxLength: Integer;
property OnChange: TNotifyEvent;
property OnClick: TNotifyEvent;
property OnContextPopup: TContextPopupEvent;
property OnDblClick: TNotifyEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnEndDock: TEndDragEvent;
property OnEndDrag: TEndDragEvent;
property OnEnter: TNotifyEvent;
property OnExit: TNotifyEvent;
property OnGesture: TGestureEvent;
property OnKeyDown: TKeyEvent;
property OnKeyPress: TKeyPressEvent;
property OnKeyUp: TKeyEvent;
property OnMouseActivate: TMouseActivateEvent;
property OnMouseDown: TMouseEvent;
property OnMouseEnter: TNotifyEvent;
property OnMouseLeave: TNotifyEvent;
property OnMouseMove: TMouseMoveEvent;
property OnMouseUp: TMouseEvent;
property OnProtectChange: TRichEditProtectChange;
property OnResizeRequest: TRichEditResizeEvent;
property OnSaveClipboard: TRichEditSaveClipboard;
property OnSelectionChange: TNotifyEvent;
property OnStartDock: TStartDockEvent;
property OnStartDrag: TStartDragEvent;
property ParentBiDiMode: Boolean;
property ParentColor: Boolean;
property ParentCtl3D: Boolean;
property ParentFont: Boolean;
property ParentShowHint: Boolean;
property PlainText: Boolean;
property PopupMenu: TPopupMenu;
property ReadOnly: Boolean;
property ScrollBars: TScrollStyle;
property ShowHint: Boolean;
property StyleElements: TStyleElements;
property TabOrder: TTabOrder;
property TabStop: Boolean;
property Touch: TTouchManager;
property Visible: Boolean;
property WantReturns: Boolean;
property WantTabs: Boolean;
property WordWrap: Boolean;
property Zoom: Integer;
procedure LoadMemo;

## TDBText
继承：TDBText → TCustomLabel → TGraphicControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.DBCtrls

property Align: TAlign;
property Alignment: TAlignment;
property Anchors: TAnchors;
property AutoSize: Boolean;
property BiDiMode: TBiDiMode;
property Color: TColor;
property Constraints: TSizeConstraints;
property DataField: string;
property DataSource: TDataSource;
property DragCursor: TCursor;
property DragKind: TDragKind;
property DragMode: TDragMode;
property Enabled: Boolean;
property Field: TField;  // read-only
property Font: TFont;
property OnClick: TNotifyEvent;
property OnContextPopup: TContextPopupEvent;
property OnDblClick: TNotifyEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnEndDock: TEndDragEvent;
property OnEndDrag: TEndDragEvent;
property OnGesture: TGestureEvent;
property OnMouseActivate: TMouseActivateEvent;
property OnMouseDown: TMouseEvent;
property OnMouseEnter: TNotifyEvent;
property OnMouseLeave: TNotifyEvent;
property OnMouseMove: TMouseMoveEvent;
property OnMouseUp: TMouseEvent;
property OnStartDock: TStartDockEvent;
property OnStartDrag: TStartDragEvent;
property ParentBiDiMode: Boolean;
property ParentColor: Boolean;
property ParentFont: Boolean;
property ParentShowHint: Boolean;
property PopupMenu: TPopupMenu;
property ShowHint: Boolean;
property StyleElements: TStyleElements;
property Touch: TTouchManager;
property Transparent: Boolean;
property Visible: Boolean;
property WordWrap: Boolean;

## TDebugger
继承：TDebugger → TInterfacedObject → TObject ｜ 单元：RT_Debugger

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
procedure Create;
function CreateBreakpoint(aFileName: WideString; aLine: Integer): TBreakpoint;
function CreateWatch(aExpression: WideString): TWatch;
function CreateWatchExt(aExpression: WideString; aFullPath: WideString; aLineNumber: Integer): TWatch;
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
procedure View_AttachStatusMonitor(aView: IDebugStatusMonitor);
procedure View_AttachWatchMonitor(aMonitor: IWatchMonitor);
procedure View_DetachBreakpointMonitor(aMonitor: IBreakpointMonitor);
procedure View_DetachStatusMonitor(aView: IDebugStatusMonitor);
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

## TDefaultAttributeBase
继承：TDefaultAttributeBase → TCustomAttribute → TObject ｜ 单元：System.Classes

property Value: Variant;  // read-only

## TDefaultLookupList
继承：TDefaultLookupList → TLookupList → TObject ｜ 单元：Data.DB


## TDefCollection
继承：TDefCollection → TOwnedCollection → TCollection → TPersistent → TObject ｜ 单元：Data.DB

property DataSet: TDataSet;  // read-only
property Updated: Boolean;
function Find(const AName: string): TNamedItem;
procedure GetItemNames(List: TStrings);
function IndexOf(const AName: string): Integer;

## TDetailDataLink
继承：TDetailDataLink → TDataLink → TPersistent → TObject ｜ 单元：Data.DB

property DetailDataSet: TDataSet;  // read-only
function GetDetailDataSet: TDataSet;

## TDigitsPanelMetrics
继承：TDigitsPanelMetrics → TPersistent → TObject ｜ 单元：InstrumentDigitPanels

property EndSpace: Integer;
property GroupSpace: Integer;
property Space: Integer;
property StartSpace: Integer;
procedure Create(AOwner: TCustomInstrumentDigitsPanel);

## TDockTree
继承：TDockTree → TInterfacedObject → TObject ｜ 单元：Vcl.Controls

procedure AdjustDockRect(Control: TControl; const ARect: IDispatch);
procedure AdjustFrameRect(Control: TControl; const ARect: IDispatch);
procedure Create(DockSite: TWinControl);
function HitTest(const MousePos: IDispatch; out HTFlag: Integer): TControl;
procedure InsertControl(Control: TControl; InsertAt: TAlign; DropCtl: TControl);
procedure LoadFromStream(Stream: TStream);
procedure MouseDown(Button: TMouseButton; Shift: TShiftState; X: Integer; Y: Integer; var Handled: Boolean);
procedure MouseMove(Shift: TShiftState; X: Integer; Y: Integer; var Handled: Boolean);
procedure MouseUp(Button: TMouseButton; Shift: TShiftState; X: Integer; Y: Integer; var Handled: Boolean);
procedure PaintDockFrame(Canvas: TCanvas; Control: TControl; const ARect: IDispatch);
procedure PaintSite(DC: HDC);
procedure PositionDockRect(Client: TControl; DropCtl: TControl; DropAlign: TAlign; const DockRect: IDispatch);
function ReferenceFromOrient(const Orient: TDockOrientation): Integer;
procedure RemoveControl(Control: TControl);
procedure ResetBounds(Force: Boolean);
procedure SaveToStream(Stream: TStream);
procedure ShowHint(const CursorPos: IDispatch; const CursorRect: IDispatch; var HintStr: string);
procedure WndProc(const Message: IDispatch);
function ZoneCaptionHitTest(const Zone: TDockZone; const MousePos: IDispatch; var HTFlag: Integer): Boolean;

## TDockZone
继承：TDockZone → TObject ｜ 单元：Vcl.Controls

property ChildControl: TControl;  // read-only
property ChildCount: Integer;  // read-only
property LimitBegin: Integer;  // read-only
property LimitSize: Integer;  // read-only
property Visible: Boolean;  // read-only
property VisibleChildCount: Integer;  // read-only
property ZoneLimit: Integer;
procedure Create(Tree: TDockTree);
procedure ExpandZoneLimit(NewLimit: Integer);
function FirstVisibleChild: TDockZone;
function NextVisible: TDockZone;
function PrevVisible: TDockZone;
procedure ResetChildren;
procedure ResetZoneLimits;
procedure Update;

## TDocumentFormNotification
继承：TDocumentFormNotification → TNotificationWithCode → TInterfacedObject → TObject ｜ 单元：RT_ClientServerInterface

procedure Create(ACode: Integer; Handle: NativeUInt; AFormId: Integer);

## TDocumentNotification
继承：TDocumentNotification → TNotificationWithCode → TInterfacedObject → TObject ｜ 单元：RT_ClientServerInterface

property OldFileName: WideString;  // read-only
property ServerDocument: IServerDocument;  // read-only
procedure Create(ACode: Integer; const AServerDocument: IServerDocument; const AFileName: string; const AData: IInterface);
procedure CreateForRename(ACode: Integer; const AServerDocument: IServerDocument; const AOldFileName: string);
procedure CreateGenerated(ACode: Integer; const AFileName: string);

## TDocumentRenamedNotification
继承：TDocumentRenamedNotification → TDocumentNotification → TNotificationWithCode → TInterfacedObject → TObject ｜ 单元：RT_ClientServerInterface

property NewFileName: WideString;  // read-only
property ProjectFileName: WideString;  // read-only
procedure Create(ACode: Integer; const AOldFileName: WideString; const ANewFileName: WideString; const AProjectFileName: WideString);

## TDocumentRequest
继承：TDocumentRequest → TNotificationWithCode → TInterfacedObject → TObject ｜ 单元：RT_ClientServerInterface

procedure Create(ACode: Integer; AInitialResult: Integer; const AServerDoc: IServerDocument);

## TDocumentToPrint
继承：TDocumentToPrint → TObject ｜ 单元：Rt_AbstractOutput

field BackgroundLoaded;
field Document;
procedure Create(ADocument: IDocument);

## TDragControlObject
继承：TDragControlObject → TBaseDragControlObject → TDragObject → TObject ｜ 单元：Vcl.Controls


## TDragControlObjectEx
继承：TDragControlObjectEx → TDragControlObject → TBaseDragControlObject → TDragObject → TObject ｜ 单元：Vcl.Controls


## TDragDockObject
继承：TDragDockObject → TBaseDragControlObject → TDragObject → TObject ｜ 单元：Vcl.Controls

property Brush: TBrush;
property DockRect: TRect;
property DropAlign: TAlign;  // read-only
property DropOnControl: TControl;  // read-only
property EraseDockRect: TRect;
property EraseWhenMoving: Boolean;  // read-only
property Floating: Boolean;
property FrameWidth: Integer;  // read-only
procedure AdjustDockRect(const ARect: IDispatch);
procedure DrawDragDockImage;
procedure EraseDragDockImage;
function GetEraseWhenMoving: Boolean;
function GetFrameWidth: Integer;

## TDragDockObjectEx
继承：TDragDockObjectEx → TDragDockObject → TBaseDragControlObject → TDragObject → TObject ｜ 单元：Vcl.Controls


## TDragDropNotification
继承：TDragDropNotification → TNotificationWithCode → TInterfacedObject → TObject ｜ 单元：RT_ClientServerInterface

procedure Create(ACode: Integer; const ADragDropObject: IDragDropObject);

## TDragImageList
继承：TDragImageList → TCustomImageList → TBaseImageList ｜ 单元：Vcl.Controls

property DragCursor: TCursor;
property Dragging: Boolean;  // read-only
property DragHotspot: TPoint;
function BeginDrag(Window: HWND; X: Integer; Y: Integer): Boolean;
function DragLock(Window: HWND; XPos: Integer; YPos: Integer): Boolean;
function DragMove(X: Integer; Y: Integer): Boolean;
procedure DragUnlock;
function EndDrag: Boolean;
procedure HideDragImage;
function SetDragImage(Index: Integer; HotSpotX: Integer; HotSpotY: Integer): Boolean;
procedure ShowDragImage;

## TDragObject
继承：TDragObject → TObject ｜ 单元：Vcl.Controls

property AlwaysShowDragImages: Boolean;
property Cancelling: Boolean;
property DragHandle: HWND;
property DragPos: TPoint;
property DragTarget: TDragTarget;
property DragTargetPos: TPoint;
property Dropped: Boolean;  // read-only
property MouseDeltaX: Double;  // read-only
property MouseDeltaY: Double;  // read-only
property RightClickCancels: Boolean;
procedure Assign(Source: TDragObject);
procedure Finished(Target: TObject; X: Integer; Y: Integer; Accepted: Boolean);
function GetDragCursor(Accepted: Boolean; X: Integer; Y: Integer): TCursor;
function GetDragImages: TDragImageList;
function GetName: string;
procedure HideDragImage;
function Instance: NativeUInt;
procedure ShowDragImage;
procedure WndProc(const Msg: IDispatch);

## TDragObjectEx
继承：TDragObjectEx → TDragObject → TObject ｜ 单元：Vcl.Controls


## TDrawGrid
继承：TDrawGrid → TCustomDrawGrid → TCustomGrid → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.Grids

property Align: TAlign;
property Anchors: TAnchors;
property BevelEdges: TBevelEdges;
property BevelInner: TBevelCut;
property BevelKind: TBevelKind;
property BevelOuter: TBevelCut;
property BevelWidth: TBevelWidth;
property BiDiMode: TBiDiMode;
property BorderStyle: TBorderStyle;
property ColCount: Integer;
property Color: TColor;
property Constraints: TSizeConstraints;
property Ctl3D: Boolean;
property DefaultColWidth: Integer;
property DefaultDrawing: Boolean;
property DefaultRowHeight: Integer;
property DoubleBuffered: Boolean;
property DragCursor: TCursor;
property DragKind: TDragKind;
property DragMode: TDragMode;
property DrawingStyle: TGridDrawingStyle;
property Enabled: Boolean;
property FixedColor: TColor;
property FixedCols: Integer;
property FixedRows: Integer;
property Font: TFont;
property GradientEndColor: TColor;
property GradientStartColor: TColor;
property GridLineWidth: Integer;
property OnClick: TNotifyEvent;
property OnColumnMoved: TMovedEvent;
property OnContextPopup: TContextPopupEvent;
property OnDblClick: TNotifyEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnDrawCell: TDrawCellEvent;
property OnEndDock: TEndDragEvent;
property OnEndDrag: TEndDragEvent;
property OnEnter: TNotifyEvent;
property OnExit: TNotifyEvent;
property OnFixedCellClick: TFixedCellClickEvent;
property OnGesture: TGestureEvent;
property OnGetEditMask: TGetEditEvent;
property OnGetEditText: TGetEditEvent;
property OnKeyDown: TKeyEvent;
property OnKeyPress: TKeyPressEvent;
property OnKeyUp: TKeyEvent;
property OnMouseActivate: TMouseActivateEvent;
property OnMouseDown: TMouseEvent;
property OnMouseEnter: TNotifyEvent;
property OnMouseLeave: TNotifyEvent;
property OnMouseMove: TMouseMoveEvent;
property OnMouseUp: TMouseEvent;
property OnMouseWheelDown: TMouseWheelUpDownEvent;
property OnMouseWheelUp: TMouseWheelUpDownEvent;
property OnRowMoved: TMovedEvent;
property OnSelectCell: TSelectCellEvent;
property OnSetEditText: TSetEditEvent;
property OnStartDock: TStartDockEvent;
property OnStartDrag: TStartDragEvent;
property OnTopLeftChanged: TNotifyEvent;
property Options: TGridOptions;
property ParentBiDiMode: Boolean;
property ParentColor: Boolean;
property ParentCtl3D: Boolean;
property ParentDoubleBuffered: Boolean;
property ParentFont: Boolean;
property ParentShowHint: Boolean;
property PopupMenu: TPopupMenu;
property RowCount: Integer;
property ScrollBars: TScrollStyle;
property ShowHint: Boolean;
property StyleElements: TStyleElements;
property TabOrder: TTabOrder;
property Touch: TTouchManager;
property Visible: Boolean;
property VisibleColCount: Integer;  // read-only
property VisibleRowCount: Integer;  // read-only

## TDXPServer_Notification
继承：TDXPServer_Notification → TNotificationWithCode → TInterfacedObject → TObject ｜ 单元：RT_ClientServerInterface


## TEdit
继承：TEdit → TCustomEdit → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.StdCtrls

property Align: TAlign;
property Alignment: TAlignment;
property Anchors: TAnchors;
property AutoSelect: Boolean;
property AutoSize: Boolean;
property BevelEdges: TBevelEdges;
property BevelInner: TBevelCut;
property BevelKind: TBevelKind;
property BevelOuter: TBevelCut;
property BevelWidth: TBevelWidth;
property BiDiMode: TBiDiMode;
property BorderStyle: TBorderStyle;
property CharCase: TEditCharCase;
property Color: TColor;
property Constraints: TSizeConstraints;
property Ctl3D: Boolean;
property DoubleBuffered: Boolean;
property DragCursor: TCursor;
property DragKind: TDragKind;
property DragMode: TDragMode;
property Enabled: Boolean;
property Font: TFont;
property HideSelection: Boolean;
property ImeMode: TImeMode;
property ImeName: TImeName;
property MaxLength: Integer;
property NumbersOnly: Boolean;
property OEMConvert: Boolean;
property OnChange: TNotifyEvent;
property OnClick: TNotifyEvent;
property OnContextPopup: TContextPopupEvent;
property OnDblClick: TNotifyEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnEndDock: TEndDragEvent;
property OnEndDrag: TEndDragEvent;
property OnEnter: TNotifyEvent;
property OnExit: TNotifyEvent;
property OnGesture: TGestureEvent;
property OnKeyDown: TKeyEvent;
property OnKeyPress: TKeyPressEvent;
property OnKeyUp: TKeyEvent;
property OnMouseActivate: TMouseActivateEvent;
property OnMouseDown: TMouseEvent;
property OnMouseEnter: TNotifyEvent;
property OnMouseLeave: TNotifyEvent;
property OnMouseMove: TMouseMoveEvent;
property OnMouseUp: TMouseEvent;
property OnStartDock: TStartDockEvent;
property OnStartDrag: TStartDragEvent;
property ParentBiDiMode: Boolean;
property ParentColor: Boolean;
property ParentCtl3D: Boolean;
property ParentDoubleBuffered: Boolean;
property ParentFont: Boolean;
property ParentShowHint: Boolean;
property PasswordChar: Char;
property PopupMenu: TPopupMenu;
property ReadOnly: Boolean;
property ShowHint: Boolean;
property StyleElements: TStyleElements;
property TabOrder: TTabOrder;
property TabStop: Boolean;
property Text: TCaption;
property TextHint: string;
property Touch: TTouchManager;
property Visible: Boolean;

## TEditAction
继承：TEditAction → TAction → TCustomAction → TContainedAction ｜ 单元：Vcl.StdActns

property Control: TCustomEdit;
function GetControl(Target: TObject): TCustomEdit;

## TEditButton
继承：TEditButton → TPersistent → TObject ｜ 单元：Vcl.ExtCtrls

property CustomHint: TCustomHint;
property DisabledImageIndex: TImageIndex;
property DropDownMenu: TPopupMenu;
property Enabled: Boolean;
property Hint: string;
property HotImageIndex: TImageIndex;
property ImageIndex: TImageIndex;
property PressedImageIndex: TImageIndex;
property Visible: Boolean;
procedure UpdateBounds;

## TEditCopy
继承：TEditCopy → TEditAction → TAction → TCustomAction → TContainedAction ｜ 单元：Vcl.StdActns


## TEditCut
继承：TEditCut → TEditAction → TAction → TCustomAction → TContainedAction ｜ 单元：Vcl.StdActns


## TEditDelete
继承：TEditDelete → TEditAction → TAction → TCustomAction → TContainedAction ｜ 单元：Vcl.StdActns


## TEditPaste
继承：TEditPaste → TEditAction → TAction → TCustomAction → TContainedAction ｜ 单元：Vcl.StdActns


## TEditSelectAll
继承：TEditSelectAll → TEditAction → TAction → TCustomAction → TContainedAction ｜ 单元：Vcl.StdActns


## TEditStyleHook
继承：TEditStyleHook → TMouseTrackControlStyleHook → TMouseTrackControlStyleHook ｜ 单元：Vcl.StdCtrls


## TEditUndo
继承：TEditUndo → TEditAction → TAction → TCustomAction → TContainedAction ｜ 单元：Vcl.StdActns


## TEDM_Notification
继承：TEDM_Notification → TNotificationWithCode → TInterfacedObject → TObject ｜ 单元：RT_ClientServerInterface

procedure Create(ACode: Integer; const ADItemGUID: WideString; const ADItemRevisionGUID: WideString; const AContentTypeGUID: WideString);
function GetContentTypeGUID: WideString;
function GetDItemGUID: WideString;
function GetDItemRevisionGUID: WideString;

## TEDM_PCBReleaseDataNotification
继承：TEDM_PCBReleaseDataNotification → TNotificationWithCode → TInterfacedObject → TObject ｜ 单元：RT_ClientServerInterface

procedure Create(const ACode: Integer; const APCBReleaseData: IInterface);

## TEDM_UserLoggedInNotification
继承：TEDM_UserLoggedInNotification → TNotificationWithCode → TInterfacedObject → TObject ｜ 单元：RT_ClientServerInterface

procedure Create(const ASessionId: WideString; const AUserName: WideString; const AHost: WideString);

## TEDMS_CommentsNotification
继承：TEDMS_CommentsNotification → TNotificationWithCode → TInterfacedObject → TObject ｜ 单元：RT_ClientServerInterface

procedure Create(const ACode: Integer; const ACommentThread: IEDMS_CommentThreadHolder);

## TEDMS_CommentThreadHolder
继承：TEDMS_CommentThreadHolder → TInterfacedObject → TObject ｜ 单元：RT_ClientServerInterface

procedure Create(const AThreadId: WideString; const AProjectUniqID: WideString; const AServerID: WideString; const AData: WideString; AIsSharedWithMeProject: Boolean);

## TEncodedParameter
继承：TEncodedParameter → TParameter → TCollectionItem → TPersistent → TObject ｜ 单元：RT_SupplierManager

field Visible;
procedure Create(const AName: string; const AValue: string; AVisible: Boolean);

## TEncodedParameterList
继承：TEncodedParameterList → TObjectList → TList → TObject ｜ 单元：RT_SupplierManager

property EncodedParameter[Index: ?]: TEncodedParameter;  // read-only
procedure GetState_AsOrdinaryParameterList(ParameterList: TParameterList);
function GetState_ParameterAsString(const Name: string; var Value: string): Boolean;
function GetState_ParameterByName(const AName: string): TEncodedParameter;
procedure SetState_AddEncodedParameter(const AName: string; const AValue: string; Visible: Boolean);

## TEncoding
继承：TEncoding → TObject ｜ 单元：System.SysUtils ｜ 未在类列表里注册，只能通过实例访问

property ANSI: TEncoding;  // read-only
property ASCII: TEncoding;  // read-only
property BigEndianUnicode: TEncoding;  // read-only
property CodePage: Cardinal;  // read-only
property Default: TEncoding;  // read-only
property EncodingName: String;  // read-only
property IsSingleByte: Boolean;  // read-only
property Unicode: TEncoding;  // read-only
property UTF7: TEncoding;  // read-only
property UTF8: TEncoding;  // read-only
function Clone: TEncoding;
procedure FreeEncodings;
function GetBufferEncoding(const Buffer: TArray<System.Byte>; var AEncoding: TEncoding): Integer;
function GetByteCount(const Chars: Char): Integer;
function GetCharCount(const Bytes: array of Byte): Integer;
function GetEncoding(CodePage: Integer): TEncoding;
function GetMaxByteCount(CharCount: Integer): Integer;
function GetMaxCharCount(ByteCount: Integer): Integer;
function GetString(const Bytes: TArray<System.Byte>): string;
function IsStandardEncoding(AEncoding: TEncoding): Boolean;

## TEnumPropDesc
继承：TEnumPropDesc → TObject ｜ 单元：Vcl.OleCtrls

procedure Create(DispID: Integer; ValueCount: Integer; const TypeInfo: ITypeInfo);
function StringToValue(const S: string): Integer;
function ValueToString(V: Integer): string;

## TEventDispatch
继承：TEventDispatch → TObject ｜ 单元：Vcl.OleCtrls

procedure Create(Control: TOleControl);

## TEvsLmtNotification
继承：TEvsLmtNotification → TNotificationWithCode → TInterfacedObject → TObject ｜ 单元：RT_ClientServerInterface

procedure Create(ACode: Integer);

## TExprParser
继承：TExprParser → TObject ｜ 单元：Data.DBCommon

property DataSize: Integer;  // read-only
procedure SetExprParams(const Text: string; Options: TFilterOptions; ParserOptions: TParserOptions; const FieldName: string);

## TExtendedField
继承：TExtendedField → TNumericField → TField → TComponent → TPersistent → TObject ｜ 单元：Data.DB

property currency: Boolean;
property MaxValue: Extended;
property MinValue: Extended;
property Precision: Integer;
property Value: Extended;

## TExternalActionItem
继承：TExternalActionItem → TInterfacedObject → TObject ｜ 单元：RT_ClientServerInterface

property ActionItem[Index: ?]: IExternalActionItem;  // read-only
property ActionItemCount: Integer;  // read-only
procedure Create(const ACaption: WideString; AEnabled: LongBool; AVisible: LongBool; AAction: TBasicAction; AExternalActionItemList: IExternalActionItemList);
function Execute: LongBool;
function GetActionItem(AIndex: Integer): IExternalActionItem;
function GetActionItemCount: Integer;
function GetCaption: WideString;
function GetEnabled: LongBool;
function GetVisible: LongBool;

## TExternalActionItemList
继承：TExternalActionItemList → TInterfaceList → TInterfacedObject → TObject ｜ 单元：RT_ClientServerInterface

property ActionItem[Index: ?]: IExternalActionItem;  // read-only
function GetActionItem(AIndex: Integer): IExternalActionItem;

## TExternalComponentMessageAdapter
继承：TExternalComponentMessageAdapter → TObject ｜ 单元：ExternalForm

procedure Create(AControl: TWinControl);

## TExternalFormComponent
继承：TExternalFormComponent → TPanel → TCustomPanel → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：ExternalForm

property Align: TAlign;
property ExternalForm: IExternalForm;
property ExternHandle: HWND;  // read-only
property OnKeyDown: TKeyEvent;
property OnMouseWheel: TMouseWheelEvent;
function _AddRef: Integer;
function _Release: Integer;
procedure Activate;
procedure Disconnect;
procedure DisconnectAndRelease;
procedure SetExternalForm(const Value: IExternalForm);
procedure SwitchExternalForm(const Value: IExternalForm);
procedure UpdateCaption;

## TExternalFormComponentRefCount
继承：TExternalFormComponentRefCount → TExternalFormComponent → TPanel → TCustomPanel → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：ExternalForm


## TFastStringList
继承：TFastStringList → TStringList → TStrings → TPersistent → TObject ｜ 单元：RT_StrUtils


## TFavoriteLinkItem
继承：TFavoriteLinkItem → TCollectionItem → TPersistent → TObject ｜ 单元：Vcl.Dialogs

property Location: string;

## TFavoriteLinkItems
继承：TFavoriteLinkItems → TCollection → TPersistent → TObject ｜ 单元：Vcl.Dialogs

property Items[Index: ?]: TFavoriteLinkItem;
function Add: TFavoriteLinkItem;
function GetEnumerator: TFavoriteLinkItemsEnumerator;

## TFavoriteLinkItemsEnumerator
继承：TFavoriteLinkItemsEnumerator → TObject ｜ 单元：Vcl.Dialogs

property Current: TFavoriteLinkItem;  // read-only
procedure Create(ACollection: TFavoriteLinkItems);
function GetCurrent: TFavoriteLinkItem;
function MoveNext: Boolean;

## TField
继承：TField → TComponent → TPersistent → TObject ｜ 单元：Data.DB

property Alignment: TAlignment;
property AsAnsiString: AnsiString;
property AsBCD: TBcd;
property AsBoolean: Boolean;
property AsCurrency: Currency;
property AsDateTime: TDateTime;
property AsExtended: Extended;
property AsFloat: Double;
property AsInteger: Longint;
property AsLargeInt: Largeint;
property AsLongWord: LongWord;
property AsSingle: Single;
property AsSQLTimeStamp: TSQLTimeStamp;
property AsSQLTimeStampOffset: TSQLTimeStampOffset;
property AsString: String;
property AsVariant: Variant;
property AsWideString: String;
property AttributeSet: String;
property AutoGenerateValue: TAutoRefreshFlag;
property Calculated: Boolean;
property CanModify: Boolean;  // read-only
property ConstraintErrorMessage: string;
property CurValue: Variant;  // read-only
property CustomConstraint: string;
property DataSet: TDataSet;
property DataSize: Integer;  // read-only
property DataType: TFieldType;  // read-only
property DefaultExpression: string;
property DisplayLabel: string;
property DisplayName: String;  // read-only
property DisplayText: String;  // read-only
property DisplayWidth: Integer;
property EditMask: TEditMask;
property EditMaskPtr: TEditMask;  // read-only
property FieldKind: TFieldKind;
property FieldName: string;
property FieldNo: Integer;  // read-only
property FullName: String;  // read-only
property HasConstraints: Boolean;  // read-only
property ImportedConstraint: string;
property Index: Integer;
property IsIndexField: Boolean;  // read-only
property IsNull: Boolean;  // read-only
property KeyFields: string;
property LifeCycle: TFieldLifeCycle;
property Lookup: Boolean;
property LookupCache: Boolean;
property LookupDataSet: TDataSet;
property LookupKeyFields: string;
property LookupList: TLookupList;  // read-only
property LookupResultField: string;
property NewValue: Variant;
property Offset: Integer;  // read-only
property OldValue: Variant;  // read-only
property OnChange: TFieldNotifyEvent;
property OnGetText: TFieldGetTextEvent;
property OnSetText: TFieldSetTextEvent;
property OnValidate: TFieldNotifyEvent;
property Origin: string;
property ParentField: TObjectField;
property ProviderFlags: TProviderFlags;
property ReadOnly: Boolean;
property Required: Boolean;
property Size: Integer;
property Text: String;
property Validating: Boolean;  // read-only
property ValidChars: TFieldChars;
property Value: Variant;
property Visible: Boolean;
function AccessError(const TypeName: string): EDatabaseError;
procedure AssignValue(const Value: IDispatch);
procedure Bind(Binding: Boolean);
procedure Change;
procedure CheckTypeSize(Value: Integer);
procedure Clear;
procedure CopyData(Source: TArray<System.Byte>; Dest: TArray<System.Byte>);
procedure FocusControl;
procedure FreeBuffers;
function GetAsAnsiString: AnsiString;
function GetAsBCD: IDispatch;
function GetAsBoolean: Boolean;
function GetAsByteArray: Variant;
function GetAsBytes: TArray<System.Byte>;
function GetAsCurrency: Currency;
function GetAsDateTime: TDateTime;
function GetAsExtended: Extended;
function GetAsFloat: Double;
function GetAsInteger: Integer;
function GetAsLargeInt: Int64;
function GetAsLongWord: Cardinal;
function GetAsSingle: Single;
function GetAsSQLTimeStamp: IDispatch;
function GetAsSQLTimeStampOffset: IDispatch;
function GetAsString: string;
function GetAsVariant: Variant;
function GetAsWideString: string;
function GetCanModify: Boolean;
function GetClassDesc: string;
function GetDataSize: Integer;
function GetDefaultWidth: Integer;
function GetFieldNo: Integer;
function GetHasConstraints: Boolean;
function GetIOSize: Integer;
function GetIsNull: Boolean;
function GetSize: Integer;
procedure GetText(var Text: string; DisplayText: Boolean);
procedure GetWideText(var Text: string; DisplayText: Boolean);
function IsBlob: Boolean;
function IsValidChar(InputChar: Char): Boolean;
procedure RefreshLookupList;
procedure SetAsAnsiString(const Value: AnsiString);
procedure SetAsBCD(const Value: IDispatch);
procedure SetAsBoolean(Value: Boolean);
procedure SetAsByteArray(const Value: Variant);
procedure SetAsBytes(const Value: TArray<System.Byte>);
procedure SetAsCurrency(Value: Currency);
procedure SetAsDateTime(Value: TDateTime);
procedure SetAsExtended(Value: Extended);
procedure SetAsFloat(Value: Double);
procedure SetAsInteger(Value: Integer);
procedure SetAsLargeInt(Value: Int64);
procedure SetAsLongWord(Value: Cardinal);
procedure SetAsSingle(Value: Single);
procedure SetAsSQLTimeStamp(const Value: IDispatch);
procedure SetAsSQLTimeStampOffset(const Value: IDispatch);
procedure SetAsString(const Value: string);
procedure SetAsVariant(const Value: Variant);
procedure SetAsWideString(const Value: string);
procedure SetData(Buffer: TArray<System.Byte>; NativeFormat: Boolean);
procedure SetDataSet(ADataSet: TDataSet);
procedure SetFieldDefProps(FieldDef: TFieldDef);
procedure SetFieldKind(Value: TFieldKind);
procedure SetFieldProps(FieldDef: TFieldDef);
procedure SetFieldType(Value: TFieldType);
procedure SetParentField(AField: TObjectField);
procedure SetSize(Value: Integer);
procedure SetText(const Value: string);
procedure SetVarValue(const Value: Variant);
procedure SetWideText(const Value: string);
procedure Validate(Buffer: TArray<System.Byte>);

## TFieldDataLink
继承：TFieldDataLink → TDataLink → TPersistent → TObject ｜ 单元：Vcl.DBCtrls

property CanModify: Boolean;  // read-only
property Control: TComponent;
property Editing: Boolean;  // read-only
property Field: TField;  // read-only
property FieldName: String;
procedure Create;
function Edit: Boolean;
procedure Modified;
procedure Reset;

## TFieldDef
继承：TFieldDef → TNamedItem → TCollectionItem → TPersistent → TObject ｜ 单元：Data.DB

property Attributes: TFieldAttributes;
property ChildDefs: TFieldDefs;
property DataSet: TDataSet;  // read-only
property DataType: TFieldType;
property FieldNo: Integer;
property InternalCalcField: Boolean;
property ParentDef: TFieldDef;  // read-only
property Precision: Integer;
property Required: Boolean;
property Size: Integer;
function AddChild: TFieldDef;
procedure Create(Owner: TFieldDefs; const Name: string; DataType: TFieldType; Size: Integer; Required: Boolean; FieldNo: Integer);
function CreateField(Owner: TComponent; ParentField: TObjectField; const FieldName: string; CreateChildren: Boolean): TField;
function HasChildDefs: Boolean;

## TFieldDefList
继承：TFieldDefList → TFlatList → TStringList → TStrings → TPersistent → TObject ｜ 单元：Data.DB

property FieldDefs[Index: ?]: TFieldDef;  // read-only
function FieldByName(const Name: string): TFieldDef;
function Find(const Name: string): TFieldDef;

## TFieldDefs
继承：TFieldDefs → TDefCollection → TOwnedCollection → TCollection → TPersistent → TObject ｜ 单元：Data.DB

property HiddenFields: Boolean;
property Items[Index: ?]: TFieldDef;
property ParentDef: TFieldDef;  // read-only
procedure Add(const Name: string; DataType: TFieldType; Size: Integer; Required: Boolean);
function AddFieldDef: TFieldDef;
procedure Create(AOwner: TPersistent);
function Find(const Name: string): TFieldDef;
procedure Update;

## TFieldList
继承：TFieldList → TFlatList → TStringList → TStrings → TPersistent → TObject ｜ 单元：Data.DB

property Fields[Index: ?]: TField;  // read-only
function FieldByName(const Name: string): TField;
function Find(const Name: string): TField;

## TFieldOptions
继承：TFieldOptions → TPersistent → TObject ｜ 单元：Data.DB

property AutoCreateMode: TFieldsAutoCreationMode;
property PositionMode: TFieldsPositionMode;
property UpdatePersistent: Boolean;
procedure Create(DataSet: TDataSet);

## TFields
继承：TFields → TObject ｜ 单元：Data.DB

property Count: Integer;  // read-only
property DataSet: TDataSet;  // read-only
property Fields[Index: ?]: TField;
property LifeCycles: TFieldLifeCycles;
procedure Add(Field: TField);
procedure CheckFieldName(const FieldName: string);
procedure CheckFieldNames(const FieldNames: string);
procedure Clear;
procedure ClearAutomatic;
procedure Create(ADataSet: TDataSet);
function FieldByName(const FieldName: string): TField;
function FieldByNumber(FieldNo: Integer): TField;
function FindField(const FieldName: string): TField;
function GetEnumerator: TFieldsEnumerator;
procedure GetFieldNames(List: TStrings);
function IndexOf(Field: TField): Integer;
procedure Remove(Field: TField);

## TFieldsEnumerator
继承：TFieldsEnumerator → TObject ｜ 单元：Data.DB

property Current: TField;  // read-only
procedure Create(AFields: TFields);
function GetCurrent: TField;
function MoveNext: Boolean;

## TFileAction
继承：TFileAction → TCommonDialogAction → TCustomAction → TContainedAction ｜ 单元：Vcl.StdActns


## TFileExit
继承：TFileExit → TCustomAction → TContainedAction ｜ 单元：Vcl.StdActns

property Caption: string;
property Enabled: Boolean;
property HelpContext: THelpContext;
property HelpKeyword: string;
property HelpType: THelpType;
property Hint: string;
property ImageIndex: TImageIndex;
property OnHint: THintEvent;
property OnUpdate: TNotifyEvent;
property SecondaryShortCuts: TCustomShortCutList;
property ShortCut: TShortCut;
property Visible: Boolean;

## TFileLessViolationDescription
继承：TFileLessViolationDescription → TInterfacedObject → TObject ｜ 单元：RT_Workspace

procedure Create(AKind: TFileLessViolationKind; const AGUID: WideString; const ADescription: WideString; ALevel: TErrorLevel; AGroup: TFileLessViolationGroup; AIsExternal: Boolean; const AImplementer: WideString);

## TFileOpen
继承：TFileOpen → TFileAction → TCommonDialogAction → TCustomAction → TContainedAction ｜ 单元：Vcl.StdActns

property BeforeExecute: TNotifyEvent;
property Caption: string;
property Dialog: TOpenDialog;  // read-only
property Enabled: Boolean;
property HelpContext: THelpContext;
property HelpKeyword: string;
property HelpType: THelpType;
property Hint: string;
property ImageIndex: TImageIndex;
property OnAccept: TNotifyEvent;
property OnCancel: TNotifyEvent;
property OnHint: THintEvent;
property OnUpdate: TNotifyEvent;
property SecondaryShortCuts: TCustomShortCutList;
property ShortCut: TShortCut;
property UseDefaultApp: Boolean;
property Visible: Boolean;

## TFileOpenDialog
继承：TFileOpenDialog → TCustomFileOpenDialog → TCustomFileDialog → TComponent → TPersistent → TObject ｜ 单元：Vcl.Dialogs

property ClientGuid: string;
property DefaultExtension: string;
property DefaultFolder: string;
property FavoriteLinks: TFavoriteLinkItems;
property FileName: TFileName;
property FileNameLabel: string;
property FileTypeIndex: Cardinal;
property FileTypes: TFileTypeItems;
property OkButtonLabel: string;
property OnExecute: TNotifyEvent;
property OnFileOkClick: TFileDialogCloseEvent;
property OnFolderChange: TNotifyEvent;
property OnFolderChanging: TFileDialogFolderChangingEvent;
property OnSelectionChange: TNotifyEvent;
property OnShareViolation: TFileDialogShareViolationEvent;
property OnTypeChange: TNotifyEvent;
property Options: TFileDialogOptions;
property Title: string;

## TFileOpenWith
继承：TFileOpenWith → TFileOpen → TFileAction → TCommonDialogAction → TCustomAction → TContainedAction ｜ 单元：Vcl.StdActns

property AfterOpen: TNotifyEvent;
property BeforeExecute: TNotifyEvent;
property FileName: TFileName;
property HelpContext: THelpContext;
property HelpKeyword: string;
property HelpType: THelpType;
property OnUpdate: TNotifyEvent;

## TFilePageSetup
继承：TFilePageSetup → TCommonDialogAction → TCustomAction → TContainedAction ｜ 单元：Vcl.StdActns

property BeforeExecute: TNotifyEvent;
property Caption: string;
property Dialog: TPageSetupDialog;  // read-only
property Enabled: Boolean;
property HelpContext: THelpContext;
property HelpKeyword: string;
property HelpType: THelpType;
property Hint: string;
property ImageIndex: TImageIndex;
property OnAccept: TNotifyEvent;
property OnCancel: TNotifyEvent;
property OnHint: THintEvent;
property OnUpdate: TNotifyEvent;
property SecondaryShortCuts: TCustomShortCutList;
property ShortCut: TShortCut;
property Visible: Boolean;

## TFilePrintSetup
继承：TFilePrintSetup → TCommonDialogAction → TCustomAction → TContainedAction ｜ 单元：Vcl.StdActns

property BeforeExecute: TNotifyEvent;
property Caption: string;
property Dialog: TPrinterSetupDialog;  // read-only
property Enabled: Boolean;
property HelpContext: THelpContext;
property HelpKeyword: string;
property HelpType: THelpType;
property Hint: string;
property ImageIndex: TImageIndex;
property OnAccept: TNotifyEvent;
property OnCancel: TNotifyEvent;
property OnHint: THintEvent;
property OnUpdate: TNotifyEvent;
property SecondaryShortCuts: TCustomShortCutList;
property ShortCut: TShortCut;
property Visible: Boolean;

## TFiler
继承：TFiler → TObject ｜ 单元：System.Classes

property Ancestor: TPersistent;
property IgnoreChildren: Boolean;
property LookupRoot: TComponent;  // read-only
property Root: TComponent;
procedure Create(Stream: TStream; BufSize: Integer);
procedure FlushBuffer;
procedure SetRoot(Value: TComponent);

## TFileSaveAs
继承：TFileSaveAs → TFileAction → TCommonDialogAction → TCustomAction → TContainedAction ｜ 单元：Vcl.StdActns

property BeforeExecute: TNotifyEvent;
property Caption: string;
property Dialog: TSaveDialog;  // read-only
property Enabled: Boolean;
property HelpContext: THelpContext;
property Hint: string;
property ImageIndex: TImageIndex;
property OnAccept: TNotifyEvent;
property OnCancel: TNotifyEvent;
property OnHint: THintEvent;
property OnUpdate: TNotifyEvent;
property SecondaryShortCuts: TCustomShortCutList;
property ShortCut: TShortCut;
property Visible: Boolean;

## TFileSaveDialog
继承：TFileSaveDialog → TCustomFileSaveDialog → TCustomFileDialog → TComponent → TPersistent → TObject ｜ 单元：Vcl.Dialogs

property ClientGuid: string;
property DefaultExtension: string;
property DefaultFolder: string;
property FavoriteLinks: TFavoriteLinkItems;
property FileName: TFileName;
property FileNameLabel: string;
property FileTypeIndex: Cardinal;
property FileTypes: TFileTypeItems;
property OkButtonLabel: string;
property OnExecute: TNotifyEvent;
property OnFileOkClick: TFileDialogCloseEvent;
property OnFolderChange: TNotifyEvent;
property OnFolderChanging: TFileDialogFolderChangingEvent;
property OnOverwrite: TFileDialogOverwriteEvent;
property OnSelectionChange: TNotifyEvent;
property OnShareViolation: TFileDialogShareViolationEvent;
property OnTypeChange: TNotifyEvent;
property Options: TFileDialogOptions;
property Title: string;

## TFileStream
继承：TFileStream → THandleStream → TStream → TObject ｜ 单元：System.Classes

property FileName: String;  // read-only
procedure Create(const AFileName: string; Mode: Word);

## TFileTypeItem
继承：TFileTypeItem → TCollectionItem → TPersistent → TObject ｜ 单元：Vcl.Dialogs

property DisplayName: string;
property DisplayNameWStr: LPCWSTR;  // read-only
property FileMask: string;
property FileMaskWStr: LPCWSTR;  // read-only

## TFileTypeItems
继承：TFileTypeItems → TCollection → TPersistent → TObject ｜ 单元：Vcl.Dialogs

property Items[Index: ?]: TFileTypeItem;
function Add: TFileTypeItem;

## TFilterExpr
继承：TFilterExpr → TObject ｜ 单元：Data.DBCommon

property DataSet: TDataSet;

## TFindDialog
继承：TFindDialog → TCommonDialog → TComponent → TPersistent → TObject ｜ 单元：Vcl.Dialogs

property FindText: string;
property Left: Integer;
property OnFind: TNotifyEvent;
property Options: TFindOptions;
property Position: TPoint;
property Top: Integer;
procedure CloseDialog;
procedure Find;
procedure Replace;

## TFlatList
继承：TFlatList → TStringList → TStrings → TPersistent → TObject ｜ 单元：Data.DB

property DataSet: TDataSet;  // read-only
procedure Create(ADataSet: TDataSet);
function FindItem(const Name: string; MustExist: Boolean): TObject;
function GetUpdated: Boolean;
procedure Update;
procedure UpdateList;

## TFloatField
继承：TFloatField → TNumericField → TField → TComponent → TPersistent → TObject ｜ 单元：Data.DB

property currency: Boolean;
property MaxValue: Double;
property MinValue: Double;
property Precision: Integer;
property Value: Double;

## TFlowPanel
继承：TFlowPanel → TCustomFlowPanel → TCustomPanel → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.ExtCtrls

property Align: TAlign;
property Alignment: TAlignment;
property Anchors: TAnchors;
property AutoSize: Boolean;
property AutoWrap: Boolean;
property BevelEdges: TBevelEdges;
property BevelInner: TBevelCut;
property BevelKind: TBevelKind;
property BevelOuter: TBevelCut;
property BevelWidth: TBevelWidth;
property BiDiMode: TBiDiMode;
property BorderStyle: TBorderStyle;
property BorderWidth: TBorderWidth;
property Caption: TCaption;
property Color: TColor;
property Constraints: TSizeConstraints;
property Ctl3D: Boolean;
property DockSite: Boolean;
property DoubleBuffered: Boolean;
property DragCursor: TCursor;
property DragKind: TDragKind;
property DragMode: TDragMode;
property Enabled: Boolean;
property FlowStyle: TFlowStyle;
property Font: TFont;
property FullRepaint: Boolean;
property Locked: Boolean;
property OnAlignInsertBefore: TAlignInsertBeforeEvent;
property OnAlignPosition: TAlignPositionEvent;
property OnCanResize: TCanResizeEvent;
property OnClick: TNotifyEvent;
property OnConstrainedResize: TConstrainedResizeEvent;
property OnContextPopup: TContextPopupEvent;
property OnDblClick: TNotifyEvent;
property OnDockDrop: TDockDropEvent;
property OnDockOver: TDockOverEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnEndDock: TEndDragEvent;
property OnEndDrag: TEndDragEvent;
property OnEnter: TNotifyEvent;
property OnExit: TNotifyEvent;
property OnGesture: TGestureEvent;
property OnGetSiteInfo: TGetSiteInfoEvent;
property OnMouseActivate: TMouseActivateEvent;
property OnMouseDown: TMouseEvent;
property OnMouseEnter: TNotifyEvent;
property OnMouseLeave: TNotifyEvent;
property OnMouseMove: TMouseMoveEvent;
property OnMouseUp: TMouseEvent;
property OnResize: TNotifyEvent;
property OnStartDock: TStartDockEvent;
property OnStartDrag: TStartDragEvent;
property OnUnDock: TUnDockEvent;
property Padding: TPadding;
property ParentBackground: Boolean;
property ParentBiDiMode: Boolean;
property ParentColor: Boolean;
property ParentCtl3D: Boolean;
property ParentDoubleBuffered: Boolean;
property ParentFont: Boolean;
property ParentShowHint: Boolean;
property PopupMenu: TPopupMenu;
property ShowCaption: Boolean;
property ShowHint: Boolean;
property StyleElements: TStyleElements;
property TabOrder: TTabOrder;
property TabStop: Boolean;
property Touch: TTouchManager;
property UseDockManager: Boolean;
property VerticalAlignment: TVerticalAlignment;
property Visible: Boolean;

## TFlowStage_ACTEL_CreateBitFile
继承：TFlowStage_ACTEL_CreateBitFile → TFlowStage_ACTEL_VendorProcess → TFlowStage_VendorProcess → TFlowStage_WithDriver → TProcessFlowStage ｜ 单元：Rt_ActelFPGA

procedure Create(ANexusDriver: INexusDriver; const APath: string; OutputExt: string);

## TFlowStage_ACTEL_CreateSTAPLFile
继承：TFlowStage_ACTEL_CreateSTAPLFile → TFlowStage_ACTEL_VendorProcess → TFlowStage_VendorProcess → TFlowStage_WithDriver → TProcessFlowStage ｜ 单元：Rt_ActelFPGA

procedure Create(ANexusDriver: INexusDriver; const APath: string; OutputExt: string);

## TFlowStage_ACTEL_FitDesign
继承：TFlowStage_ACTEL_FitDesign → TFlowStage_ACTEL_VendorProcess → TFlowStage_VendorProcess → TFlowStage_WithDriver → TProcessFlowStage ｜ 单元：Rt_ActelFPGA

procedure Create(ANexusDriver: INexusDriver; const APath: string; OutputExt: string);

## TFlowStage_ACTEL_MapDesign
继承：TFlowStage_ACTEL_MapDesign → TFlowStage_ACTEL_VendorProcess → TFlowStage_VendorProcess → TFlowStage_WithDriver → TProcessFlowStage ｜ 单元：Rt_ActelFPGA

procedure Create(ANexusDriver: INexusDriver; const APath: string; OutputExt: string);

## TFlowStage_ACTEL_TimingRpt
继承：TFlowStage_ACTEL_TimingRpt → TFlowStage_ACTEL_VendorProcess → TFlowStage_VendorProcess → TFlowStage_WithDriver → TProcessFlowStage ｜ 单元：Rt_ActelFPGA

procedure Create(ANexusDriver: INexusDriver; const APath: string; OutputExt: string);

## TFlowStage_ACTEL_TranslateDesign
继承：TFlowStage_ACTEL_TranslateDesign → TFlowStage_ACTEL_VendorProcess → TFlowStage_VendorProcess → TFlowStage_WithDriver → TProcessFlowStage ｜ 单元：Rt_ActelFPGA

procedure Create(ANexusDriver: INexusDriver; const APath: string; OutputExt: string);

## TFlowStage_ACTEL_VendorProcess
继承：TFlowStage_ACTEL_VendorProcess → TFlowStage_VendorProcess → TFlowStage_WithDriver → TProcessFlowStage ｜ 单元：Rt_ActelFPGA

field FTCLScriptFileName;
function ACTELInputFile: string;
function ACTELOutputFile: string;
procedure Create(AInputExt: string; AOutputExt: string; AReportExts: string; AName: string; ACaption: string; ADescription: string; AnApplicationName: string; AnApplicationPath: string; ADriver: INexusDriver);
function PostProcess: Boolean;
function StagePostProcess: Boolean;

## TFlowStage_Altera_Abstract
继承：TFlowStage_Altera_Abstract → TFlowStage_VendorProcess → TFlowStage_WithDriver → TProcessFlowStage ｜ 单元：Rt_AlteraFPGA


## TFlowStage_Altera_GeneratePofFile
继承：TFlowStage_Altera_GeneratePofFile → TFlowStage_Altera_Abstract → TFlowStage_VendorProcess → TFlowStage_WithDriver → TProcessFlowStage ｜ 单元：Rt_AlteraFPGA

procedure Create(ANexusDriver: INexusDriver);

## TFlowStage_Altera_MakeScriptFile
继承：TFlowStage_Altera_MakeScriptFile → TFlowStage_Altera_Abstract → TFlowStage_VendorProcess → TFlowStage_WithDriver → TProcessFlowStage ｜ 单元：Rt_AlteraFPGA

procedure Create(ANexusDriver: INexusDriver; APLDFlow: Boolean);

## TFlowStage_Altera_QuartusAsm
继承：TFlowStage_Altera_QuartusAsm → TFlowStage_Altera_Abstract → TFlowStage_VendorProcess → TFlowStage_WithDriver → TProcessFlowStage ｜ 单元：Rt_AlteraFPGA

procedure Create(ANexusDriver: INexusDriver; MakeScriptFile_Stage: TFlowStage_Altera_MakeScriptFile);

## TFlowStage_Altera_QuartusFit
继承：TFlowStage_Altera_QuartusFit → TFlowStage_Altera_Abstract → TFlowStage_VendorProcess → TFlowStage_WithDriver → TProcessFlowStage ｜ 单元：Rt_AlteraFPGA

procedure Create(ANexusDriver: INexusDriver);

## TFlowStage_Altera_QuartusMap
继承：TFlowStage_Altera_QuartusMap → TFlowStage_Altera_Abstract → TFlowStage_VendorProcess → TFlowStage_WithDriver → TProcessFlowStage ｜ 单元：Rt_AlteraFPGA

procedure Create(ANexusDriver: INexusDriver);

## TFlowStage_Altera_QuartusSVF
继承：TFlowStage_Altera_QuartusSVF → TFlowStage_Altera_Abstract → TFlowStage_VendorProcess → TFlowStage_WithDriver → TProcessFlowStage ｜ 单元：Rt_AlteraFPGA

procedure Create(ANexusDriver: INexusDriver);

## TFlowStage_Altera_QuartusTan
继承：TFlowStage_Altera_QuartusTan → TFlowStage_Altera_Abstract → TFlowStage_VendorProcess → TFlowStage_WithDriver → TProcessFlowStage ｜ 单元：Rt_AlteraFPGA

procedure Create(ANexusDriver: INexusDriver; MakeScriptFile_Stage: TFlowStage_Altera_MakeScriptFile);

## TFlowStage_Download
继承：TFlowStage_Download → TFlowStage_WithDriver → TProcessFlowStage ｜ 单元：Rt_AbstractFPGA

procedure Create(AFileExt: string; ACaption: string; ADescription: string; AResetBeforeDownload: Boolean; ADriver: INexusDriver);

## TFlowStage_DownloadCPLD
继承：TFlowStage_DownloadCPLD → TFlowStage_Download → TFlowStage_WithDriver → TProcessFlowStage ｜ 单元：Rt_AbstractFPGA

procedure Create(AResetBeforeDownload: Boolean; ADriver: INexusDriver);

## TFlowStage_DownloadFPGA
继承：TFlowStage_DownloadFPGA → TFlowStage_Download → TFlowStage_WithDriver → TProcessFlowStage ｜ 单元：Rt_AbstractFPGA

procedure Create(AFileExt: string; ADriver: INexusDriver);

## TFlowStage_VendorProcess
继承：TFlowStage_VendorProcess → TFlowStage_WithDriver → TProcessFlowStage ｜ 单元：Rt_AbstractFPGA

function ConstraintsFile_Build: string;
function ConstraintsFile_Merged: string;
procedure Create(AInputExt: string; AOutputExt: string; AReportExts: string; AName: string; ACaption: string; ADescription: string; AnApplicationName: string; AnApplicationPath: string; ADriver: INexusDriver);
function DefaultOptionsFileName: string;
function GetInputExtension: string;
function GetOutputExtension: string;
function GetStartupClock: string;
function GetUserID: string;
function InputFile: string;
procedure LoadDefaultOptions;
procedure LoadProjectOptions;
procedure MergeConstraintFiles;
function OutputFile: string;
function Parameters: string;
function ProcessReportLine(S: string): TReportLevel;
function ReplaceLine(ALine: string): string;
function RunConsoleApp: Cardinal;
procedure SetInputExtension(const Value: string);
procedure SetOutputExtension(const Value: string);
function ShouldIgnoreLine(const ALine: string): Boolean;

## TFlowStage_WithDriver
继承：TFlowStage_WithDriver → TProcessFlowStage → TProcessFlowStage ｜ 单元：Rt_AbstractFPGA

procedure Create(ADriver: INexusDriver; const AName: string; const ACaption: string; const ADescription: string);

## TFlowStage_Xilinx_Abstract
继承：TFlowStage_Xilinx_Abstract → TFlowStage_VendorProcess → TFlowStage_WithDriver → TProcessFlowStage ｜ 单元：Rt_XilinxFPGA

property IsVivado: Boolean;  // read-only
function ConstraintParameters: string;
procedure CreateVivadoScript(Cmd: TStrings; ReplaceMacros: Boolean);
function InputProject: string;

## TFlowStage_Xilinx_Build
继承：TFlowStage_Xilinx_Build → TFlowStage_Xilinx_Abstract → TFlowStage_VendorProcess → TFlowStage_WithDriver → TProcessFlowStage ｜ 单元：Rt_XilinxFPGA

procedure Create(ANexusDriver: INexusDriver);

## TFlowStage_Xilinx_Fit
继承：TFlowStage_Xilinx_Fit → TFlowStage_Xilinx_Abstract → TFlowStage_VendorProcess → TFlowStage_WithDriver → TProcessFlowStage ｜ 单元：Rt_XilinxFPGA

procedure Create(ANexusDriver: INexusDriver);

## TFlowStage_Xilinx_GenerateProgrammingFile
继承：TFlowStage_Xilinx_GenerateProgrammingFile → TFlowStage_Xilinx_Abstract → TFlowStage_VendorProcess → TFlowStage_WithDriver → TProcessFlowStage ｜ 单元：Rt_XilinxFPGA

procedure Create(ANexusDriver: INexusDriver);

## TFlowStage_Xilinx_GeneratePromFile
继承：TFlowStage_Xilinx_GeneratePromFile → TFlowStage_Xilinx_Abstract → TFlowStage_VendorProcess → TFlowStage_WithDriver → TProcessFlowStage ｜ 单元：Rt_XilinxFPGA

procedure Create(ANexusDriver: INexusDriver);

## TFlowStage_Xilinx_GenerateSerialVectorFile
继承：TFlowStage_Xilinx_GenerateSerialVectorFile → TFlowStage_Xilinx_Abstract → TFlowStage_VendorProcess → TFlowStage_WithDriver → TProcessFlowStage ｜ 单元：Rt_XilinxFPGA

procedure Create(ANexusDriver: INexusDriver);

## TFlowStage_Xilinx_MakeEraseSVF
继承：TFlowStage_Xilinx_MakeEraseSVF → TFlowStage_Xilinx_GenerateSerialVectorFile → TFlowStage_Xilinx_Abstract → TFlowStage_VendorProcess → TFlowStage_WithDriver → TProcessFlowStage ｜ 单元：Rt_XilinxFPGA

procedure Create(ANexusDriver: INexusDriver);
procedure CreateWithOptions(ANexusDriver: INexusDriver);

## TFlowStage_Xilinx_MakeJedec
继承：TFlowStage_Xilinx_MakeJedec → TFlowStage_Xilinx_Abstract → TFlowStage_VendorProcess → TFlowStage_WithDriver → TProcessFlowStage ｜ 单元：Rt_XilinxFPGA

procedure Create(ANexusDriver: INexusDriver);

## TFlowStage_Xilinx_Map
继承：TFlowStage_Xilinx_Map → TFlowStage_Xilinx_Abstract → TFlowStage_VendorProcess → TFlowStage_WithDriver → TProcessFlowStage ｜ 单元：Rt_XilinxFPGA

procedure Create(ANexusDriver: INexusDriver);

## TFlowStage_Xilinx_McsToSVF
继承：TFlowStage_Xilinx_McsToSVF → TFlowStage_Xilinx_GenerateSerialVectorFile → TFlowStage_Xilinx_Abstract → TFlowStage_VendorProcess → TFlowStage_WithDriver → TProcessFlowStage ｜ 单元：Rt_XilinxFPGA

procedure Create(ANexusDriver: INexusDriver);
procedure CreateWithOptions(ANexusDriver: INexusDriver);

## TFlowStage_Xilinx_PlaceAndRoute
继承：TFlowStage_Xilinx_PlaceAndRoute → TFlowStage_Xilinx_Abstract → TFlowStage_VendorProcess → TFlowStage_WithDriver → TProcessFlowStage ｜ 单元：Rt_XilinxFPGA

procedure Create(ANexusDriver: INexusDriver);

## TFlowStage_Xilinx_Trace
继承：TFlowStage_Xilinx_Trace → TFlowStage_Xilinx_Abstract → TFlowStage_VendorProcess → TFlowStage_WithDriver → TProcessFlowStage ｜ 单元：Rt_XilinxFPGA

procedure Create(ANexusDriver: INexusDriver);

## TFMTBCDField
继承：TFMTBCDField → TNumericField → TField → TComponent → TPersistent → TObject ｜ 单元：Data.DB

property currency: Boolean;
property MaxValue: string;
property MinValue: string;
property Precision: Integer;
property Size: Integer;
property Value: TBcd;

## TFont
继承：TFont → TGraphicsObject → TPersistent → TObject ｜ 单元：Vcl.Graphics

property Charset: TFontCharset;
property Color: TColor;
property FontAdapter: IChangeNotifier;
property Handle: HFont;
property Height: Integer;
property Name: TFontName;
property Orientation: Integer;
property Pitch: TFontPitch;
property PixelsPerInch: Integer;
property Quality: TFontQuality;
property Size: Integer;
property Style: TFontStyles;
procedure Create;

## TFontDialog
继承：TFontDialog → TCommonDialog → TComponent → TPersistent → TObject ｜ 单元：Vcl.Dialogs

property Device: TFontDialogDevice;
property Font: TFont;
property MaxFontSize: Integer;
property MinFontSize: Integer;
property OnApply: TFDApplyEvent;
property Options: TFontDialogOptions;
procedure Apply(Wnd: HWND);

## TFontEdit
继承：TFontEdit → TCommonDialogAction → TCustomAction → TContainedAction ｜ 单元：Vcl.StdActns

property BeforeExecute: TNotifyEvent;
property Caption: string;
property Dialog: TFontDialog;  // read-only
property Enabled: Boolean;
property HelpContext: THelpContext;
property HelpKeyword: string;
property HelpType: THelpType;
property Hint: string;
property ImageIndex: TImageIndex;
property OnAccept: TNotifyEvent;
property OnCancel: TNotifyEvent;
property OnHint: THintEvent;
property OnUpdate: TNotifyEvent;
property SecondaryShortCuts: TCustomShortCutList;
property ShortCut: TShortCut;
property Visible: Boolean;

## TFontRecall
继承：TFontRecall → TRecall → TObject ｜ 单元：Vcl.Graphics

procedure Create(AFont: TFont);

## TForm
继承：TForm → TCustomForm → TScrollingWinControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.Forms

property Action: TBasicAction;
property ActiveControl: TWinControl;
property ActiveMDIChild: TForm;  // read-only
property Align: TAlign;
property AlphaBlend: Boolean;
property AlphaBlendValue: Byte;
property Anchors: TAnchors;
property AutoScroll: Boolean;
property AutoSize: Boolean;
property BiDiMode: TBiDiMode;
property BorderIcons: TBorderIcons;
property BorderStyle: TFormBorderStyle;
property BorderWidth: TBorderWidth;
property Caption: TCaption;
property ClientHandle: HWND;  // read-only
property ClientHeight: Integer;
property ClientWidth: Integer;
property Color: TColor;
property Constraints: TSizeConstraints;
property Ctl3D: Boolean;
property DefaultMonitor: TDefaultMonitor;
property DockManager: IDockManager;
property DockSite: Boolean;
property DoubleBuffered: Boolean;
property DragKind: TDragKind;
property DragMode: TDragMode;
property Enabled: Boolean;
property Font: TFont;
property FormStyle: TFormStyle;
property GlassFrame: TGlassFrame;
property Height: Integer;
property HelpFile: string;
property HorzScrollBar: TControlScrollBar;
property Icon: TIcon;
property KeyPreview: Boolean;
property MDIChildCount: Integer;  // read-only
property MDIChildren[Index: ?]: TForm;  // read-only
property Menu: TMainMenu;
property ObjectMenuItem: TMenuItem;
property OldCreateOrder: Boolean;
property OnActivate: TNotifyEvent;
property OnAfterMonitorDpiChanged: TMonitorDpiChangedEvent;
property OnAlignInsertBefore: TAlignInsertBeforeEvent;
property OnAlignPosition: TAlignPositionEvent;
property OnBeforeMonitorDpiChanged: TMonitorDpiChangedEvent;
property OnCanResize: TCanResizeEvent;
property OnClick: TNotifyEvent;
property OnClose: TCloseEvent;
property OnCloseQuery: TCloseQueryEvent;
property OnConstrainedResize: TConstrainedResizeEvent;
property OnContextPopup: TContextPopupEvent;
property OnCreate: TNotifyEvent;
property OnDblClick: TNotifyEvent;
property OnDeactivate: TNotifyEvent;
property OnDestroy: TNotifyEvent;
property OnDockDrop: TDockDropEvent;
property OnDockOver: TDockOverEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnEndDock: TEndDragEvent;
property OnGesture: TGestureEvent;
property OnGetSiteInfo: TGetSiteInfoEvent;
property OnHelp: THelpEvent;
property OnHide: TNotifyEvent;
property OnKeyDown: TKeyEvent;
property OnKeyPress: TKeyPressEvent;
property OnKeyUp: TKeyEvent;
property OnMouseActivate: TMouseActivateEvent;
property OnMouseDown: TMouseEvent;
property OnMouseEnter: TNotifyEvent;
property OnMouseLeave: TNotifyEvent;
property OnMouseMove: TMouseMoveEvent;
property OnMouseUp: TMouseEvent;
property OnMouseWheel: TMouseWheelEvent;
property OnMouseWheelDown: TMouseWheelUpDownEvent;
property OnMouseWheelUp: TMouseWheelUpDownEvent;
property OnPaint: TNotifyEvent;
property OnResize: TNotifyEvent;
property OnShortCut: TShortCutEvent;
property OnShow: TNotifyEvent;
property OnStartDock: TStartDockEvent;
property OnUnDock: TUnDockEvent;
property Padding: TPadding;
property ParentBiDiMode: Boolean;
property ParentFont: Boolean;
property PixelsPerInch: Integer;
property PopupMenu: TPopupMenu;
property PopupMode: TPopupMode;
property PopupParent: TCustomForm;
property Position: TPosition;
property PrintScale: TPrintScale;
property Scaled: Boolean;
property ScreenSnap: Boolean;
property ShowHint: Boolean;
property SnapBuffer: Integer;
property StyleElements: TStyleElements;
property TileMode: TTileMode;
property TipMode: TTipMode;
property Touch: TTouchManager;
property TransparentColor: Boolean;
property TransparentColorValue: TColor;
property UseDockManager: Boolean;
property VertScrollBar: TControlScrollBar;
property Visible: Boolean;
property Width: Integer;
property WindowMenu: TMenuItem;
property WindowState: TWindowState;
procedure ArrangeIcons;
procedure Cascade;
procedure Next;
procedure Previous;
procedure Tile;

## TFormStyleHook
继承：TFormStyleHook → TMouseTrackControlStyleHook → TMouseTrackControlStyleHook ｜ 单元：Vcl.Forms


## TFrame
继承：TFrame → TCustomFrame → TScrollingWinControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.Forms

property Align: TAlign;
property Anchors: TAnchors;
property AutoScroll: Boolean;
property AutoSize: Boolean;
property BiDiMode: TBiDiMode;
property Color: TColor;
property Constraints: TSizeConstraints;
property Ctl3D: Boolean;
property DockSite: Boolean;
property DoubleBuffered: Boolean;
property DragCursor: TCursor;
property DragKind: TDragKind;
property DragMode: TDragMode;
property Enabled: Boolean;
property Font: TFont;
property OnAlignInsertBefore: TAlignInsertBeforeEvent;
property OnAlignPosition: TAlignPositionEvent;
property OnCanResize: TCanResizeEvent;
property OnClick: TNotifyEvent;
property OnConstrainedResize: TConstrainedResizeEvent;
property OnContextPopup: TContextPopupEvent;
property OnDblClick: TNotifyEvent;
property OnDockDrop: TDockDropEvent;
property OnDockOver: TDockOverEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnEndDock: TEndDragEvent;
property OnEndDrag: TEndDragEvent;
property OnEnter: TNotifyEvent;
property OnExit: TNotifyEvent;
property OnGesture: TGestureEvent;
property OnGetSiteInfo: TGetSiteInfoEvent;
property OnMouseActivate: TMouseActivateEvent;
property OnMouseDown: TMouseEvent;
property OnMouseEnter: TNotifyEvent;
property OnMouseLeave: TNotifyEvent;
property OnMouseMove: TMouseMoveEvent;
property OnMouseUp: TMouseEvent;
property OnMouseWheel: TMouseWheelEvent;
property OnMouseWheelDown: TMouseWheelUpDownEvent;
property OnMouseWheelUp: TMouseWheelUpDownEvent;
property OnResize: TNotifyEvent;
property OnStartDock: TStartDockEvent;
property OnStartDrag: TStartDragEvent;
property OnUnDock: TUnDockEvent;
property Padding: TPadding;
property ParentBackground: Boolean;
property ParentBiDiMode: Boolean;
property ParentColor: Boolean;
property ParentCtl3D: Boolean;
property ParentDoubleBuffered: Boolean;
property ParentFont: Boolean;
property ParentShowHint: Boolean;
property PopupMenu: TPopupMenu;
property ShowHint: Boolean;
property TabOrder: TTabOrder;
property TabStop: Boolean;
property Touch: TTouchManager;
property Visible: Boolean;

## TGaugeNeedle
继承：TGaugeNeedle → TPersistent → TObject ｜ 单元：InstrumentGauges

property CenterSize: NaturalNumber;
property EdgeSize: NaturalNumber;
property FillColor: TColor;
property Kind: TGaugeNeedleKind;
property LineColor: TColor;
property LineWidth: Integer;
property Options: TGaugeNeedleOptions;
property Visible: Boolean;
procedure Create(AOwner: TControl);

## TGDIHandleRecall
继承：TGDIHandleRecall → TObject ｜ 单元：Vcl.Graphics

property Canvas: TCanvas;  // read-only
procedure Create(DC: HDC; GDIObject: Cardinal);

## TGeneratedPage
继承：TGeneratedPage → TDispatchObject → TDispatchObject ｜ 单元：Rt_AbstractOutput

property Hyperlinks: ILocatedHyperlinkList;
field BoardOffSet;
field Canvas;
field DocumentData;
field Flags;
field Height;
field InputValues;
field Metafile;
field MetafileName;
field PageRenderer;
field Subtitle;
field TileRectangle;
field UniqueKey;
field ViewPort;
field Width;
field WindowHeight;
field WindowWidth;
procedure CloseCanvas;
procedure ClosePage;
procedure CreateMetafile;
function GetCanvasHandle: NativeUInt;
function GetHeight: Integer;
function GetHyperlinkList: ILocatedHyperlinkList;
function GetMetafile: TMetafile;
function GetMetafileHandle: NativeUInt;
function GetMetafileName: WideString;
function GetWidth: Integer;
procedure OpenCanvas;
procedure SetHyperlinkList(const AHyperlinkList: ILocatedHyperlinkList);
procedure StoreMetafile(const AFileName: string);

## TGeneratedPageGdiPlusMetafile
继承：TGeneratedPageGdiPlusMetafile → TGeneratedPage → TDispatchObject ｜ 单元：Rt_AbstractOutput

property GdiPlusMetafile: IGPMetafile;  // read-only
function GPMetafile: IInterface;

## TGetCategoryParametersArgs
继承：TGetCategoryParametersArgs → TObject ｜ 单元：RT_Supplier

field Category;

## TGlassFrame
继承：TGlassFrame → TPersistent → TObject ｜ 单元：Vcl.Forms

property Bottom: Integer;
property Enabled: Boolean;
property Left: Integer;
property Right: Integer;
property SheetOfGlass: Boolean;
property Top: Integer;
procedure Change;
procedure Create(Client: TCustomForm);
function FrameExtended: Boolean;
function IntersectsControl(Control: TControl): Boolean;

## TGraphGrid
继承：TGraphGrid → TPersistent → TObject ｜ 单元：InstrumentGraphs

property Pen: TPen;
property Visible: Boolean;
property XStep: Integer;
property YStep: Integer;
procedure Create(AOwner: TCustomInstrumentGraph);
procedure Shift;

## TGraphic
继承：TGraphic → TInterfacedPersistent → TPersistent → TObject ｜ 单元：Vcl.Graphics

property Empty: Boolean;  // read-only
property Height: Integer;
property Modified: Boolean;
property Palette: HPALETTE;
property PaletteModified: Boolean;
property SupportsPartialTransparency: Boolean;  // read-only
property Transparent: Boolean;
property Width: Integer;
procedure Changed(Sender: TObject);
procedure Create;
procedure Draw(ACanvas: TCanvas; const Rect: IDispatch);
procedure DrawTransparent(ACanvas: TCanvas; const Rect: IDispatch; Opacity: Byte);
function Equals(Graphic: TGraphic): Boolean;
function GetEmpty: Boolean;
function GetHeight: Integer;
function GetPalette: HPALETTE;
function GetSupportsPartialTransparency: Boolean;
function GetTransparent: Boolean;
function GetWidth: Integer;
procedure LoadFromClipboardFormat(AFormat: Word; AData: NativeUInt; APalette: HPALETTE);
procedure LoadFromFile(const Filename: string);
procedure LoadFromStream(Stream: TStream);
procedure Progress(Sender: TObject; Stage: TProgressStage; PercentDone: Byte; RedrawNow: Boolean; const R: IDispatch; const Msg: string);
procedure ReadData(Stream: TStream);
procedure SaveToClipboardFormat(var AFormat: Word; var AData: NativeUInt; var APalette: HPALETTE);
procedure SaveToFile(const Filename: string);
procedure SaveToStream(Stream: TStream);
procedure SetHeight(Value: Integer);
procedure SetPalette(Value: HPALETTE);
procedure SetSize(AWidth: Integer; AHeight: Integer);
procedure SetTransparent(Value: Boolean);
procedure SetWidth(Value: Integer);
procedure WriteData(Stream: TStream);

## TGraphicControl
继承：TGraphicControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.Controls

procedure Paint;

## TGraphicField
继承：TGraphicField → TBlobField → TField → TComponent → TPersistent → TObject ｜ 单元：Data.DB


## TGraphicsObject
继承：TGraphicsObject → TPersistent → TObject ｜ 单元：Vcl.Graphics

procedure Changed;
function HandleAllocated: Boolean;

## TGraphPolling
继承：TGraphPolling → TPersistent → TObject ｜ 单元：InstrumentGraphs

property Enabled: Boolean;
property Interval: Cardinal;
procedure Create(AOwner: TCustomInstrumentGraph);

## TGraphSignal
继承：TGraphSignal → TCollectionItem → TPersistent → TObject ｜ 单元：InstrumentGraphs

property HighFill: TBrush;
property HighSignal: TPen;
property LowFill: TBrush;
property LowSignal: TPen;
property NormalFill: TBrush;
property NormalSignal: TPen;
property RelativeFill: Boolean;
property Value: Double;

## TGraphSignals
继承：TGraphSignals → TOwnedCollection → TCollection → TPersistent → TObject ｜ 单元：InstrumentGraphs

property Items[Index: ?]: TGraphSignal;
function Add: TGraphSignal;
procedure Create(AOwner: TPersistent);

## TGraphThreshold
继承：TGraphThreshold → TPersistent → TObject ｜ 单元：InstrumentGraphs

property Enabled: Boolean;
property Pen: TPen;
property Value: Double;
procedure Create(AOwner: TCustomInstrumentGraph);

## TGridPanel
继承：TGridPanel → TCustomGridPanel → TCustomPanel → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.ExtCtrls

property Align: TAlign;
property Alignment: TAlignment;
property Anchors: TAnchors;
property BevelEdges: TBevelEdges;
property BevelInner: TBevelCut;
property BevelKind: TBevelKind;
property BevelOuter: TBevelCut;
property BevelWidth: TBevelWidth;
property BiDiMode: TBiDiMode;
property BorderStyle: TBorderStyle;
property BorderWidth: TBorderWidth;
property Caption: TCaption;
property Color: TColor;
property ColumnCollection: TColumnCollection;
property Constraints: TSizeConstraints;
property ControlCollection: TControlCollection;
property Ctl3D: Boolean;
property DockManager: IDockManager;
property DockSite: Boolean;
property DoubleBuffered: Boolean;
property DragCursor: TCursor;
property DragKind: TDragKind;
property DragMode: TDragMode;
property Enabled: Boolean;
property ExpandStyle: TExpandStyle;
property Font: TFont;
property FullRepaint: Boolean;
property Locked: Boolean;
property OnAlignInsertBefore: TAlignInsertBeforeEvent;
property OnAlignPosition: TAlignPositionEvent;
property OnCanResize: TCanResizeEvent;
property OnClick: TNotifyEvent;
property OnConstrainedResize: TConstrainedResizeEvent;
property OnContextPopup: TContextPopupEvent;
property OnDblClick: TNotifyEvent;
property OnDockDrop: TDockDropEvent;
property OnDockOver: TDockOverEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnEndDock: TEndDragEvent;
property OnEndDrag: TEndDragEvent;
property OnEnter: TNotifyEvent;
property OnExit: TNotifyEvent;
property OnGesture: TGestureEvent;
property OnGetSiteInfo: TGetSiteInfoEvent;
property OnMouseActivate: TMouseActivateEvent;
property OnMouseDown: TMouseEvent;
property OnMouseEnter: TNotifyEvent;
property OnMouseLeave: TNotifyEvent;
property OnMouseMove: TMouseMoveEvent;
property OnMouseUp: TMouseEvent;
property OnResize: TNotifyEvent;
property OnStartDock: TStartDockEvent;
property OnStartDrag: TStartDragEvent;
property OnUnDock: TUnDockEvent;
property Padding: TPadding;
property ParentBackground: Boolean;
property ParentBiDiMode: Boolean;
property ParentColor: Boolean;
property ParentCtl3D: Boolean;
property ParentDoubleBuffered: Boolean;
property ParentFont: Boolean;
property ParentShowHint: Boolean;
property PopupMenu: TPopupMenu;
property RowCollection: TRowCollection;
property ShowCaption: Boolean;
property ShowHint: Boolean;
property StyleElements: TStyleElements;
property TabOrder: TTabOrder;
property TabStop: Boolean;
property Touch: TTouchManager;
property UseDockManager: Boolean;
property VerticalAlignment: TVerticalAlignment;
property Visible: Boolean;

## TGroupBox
继承：TGroupBox → TCustomGroupBox → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.StdCtrls

property Align: TAlign;
property Anchors: TAnchors;
property BiDiMode: TBiDiMode;
property Caption: TCaption;
property Color: TColor;
property Constraints: TSizeConstraints;
property Ctl3D: Boolean;
property DockSite: Boolean;
property DoubleBuffered: Boolean;
property DragCursor: TCursor;
property DragKind: TDragKind;
property DragMode: TDragMode;
property Enabled: Boolean;
property Font: TFont;
property OnAlignInsertBefore: TAlignInsertBeforeEvent;
property OnAlignPosition: TAlignPositionEvent;
property OnClick: TNotifyEvent;
property OnContextPopup: TContextPopupEvent;
property OnDblClick: TNotifyEvent;
property OnDockDrop: TDockDropEvent;
property OnDockOver: TDockOverEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnEndDock: TEndDragEvent;
property OnEndDrag: TEndDragEvent;
property OnEnter: TNotifyEvent;
property OnExit: TNotifyEvent;
property OnGesture: TGestureEvent;
property OnGetSiteInfo: TGetSiteInfoEvent;
property OnMouseActivate: TMouseActivateEvent;
property OnMouseDown: TMouseEvent;
property OnMouseEnter: TNotifyEvent;
property OnMouseLeave: TNotifyEvent;
property OnMouseMove: TMouseMoveEvent;
property OnMouseUp: TMouseEvent;
property OnStartDock: TStartDockEvent;
property OnStartDrag: TStartDragEvent;
property OnUnDock: TUnDockEvent;
property Padding: TPadding;
property ParentBackground: Boolean;
property ParentBiDiMode: Boolean;
property ParentColor: Boolean;
property ParentCtl3D: Boolean;
property ParentDoubleBuffered: Boolean;
property ParentFont: Boolean;
property ParentShowHint: Boolean;
property PopupMenu: TPopupMenu;
property ShowHint: Boolean;
property StyleElements: TStyleElements;
property TabOrder: TTabOrder;
property TabStop: Boolean;
property Touch: TTouchManager;
property Visible: Boolean;

## TGroupBoxStyleHook
继承：TGroupBoxStyleHook → TStyleHook → TStyleHook ｜ 单元：Vcl.StdCtrls


## TGuidField
继承：TGuidField → TStringField → TField → TComponent → TPersistent → TObject ｜ 单元：Data.DB


## THandleStream
继承：THandleStream → TStream → TObject ｜ 单元：System.Classes

property Handle: THandle;  // read-only
procedure Create(AHandle: NativeUInt);

## THashedStringList
继承：THashedStringList → TStringList → TStrings → TPersistent → TObject ｜ 单元：System.IniFiles


## THashStringList
继承：THashStringList → TObject ｜ 单元：RT_StrUtils

property CaseSensitive: Boolean;
procedure AddValue(const Key: string; Value: Pointer);
procedure Clear;
function Count: Integer;
procedure Create(const AIsCaseSensitive: Boolean);
function CreateHashListItem(AIsCaseSensitive: Boolean): TStrings;
procedure DestroyAllObjects;
function ExtractValue(const Key: string; var Value: Pointer): Boolean;
function GetHashStrings(Index: Integer): TStrings;
function GetHashStringsCount: Integer;
procedure GetKeyIndex(const Key: string; out Bucket: Integer; out Index: Integer);
function GetValue(const Key: string; var Value: Pointer): Boolean;
function GetValueFromIndex(Bucket: Integer; Index: Integer): Pointer;
function KeyExists(const Key: string): Boolean;
procedure RemoveValues(AValue: Pointer);

## THeader
继承：THeader → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.ExtCtrls

property Align: TAlign;
property AllowResize: Boolean;
property Anchors: TAnchors;
property BorderStyle: TBorderStyle;
property Constraints: TSizeConstraints;
property DoubleBuffered: Boolean;
property Enabled: Boolean;
property Font: TFont;
property OnContextPopup: TContextPopupEvent;
property OnGesture: TGestureEvent;
property OnSized: TSectionEvent;
property OnSizing: TSectionEvent;
property ParentDoubleBuffered: Boolean;
property ParentFont: Boolean;
property ParentShowHint: Boolean;
property PopupMenu: TPopupMenu;
property Sections: TStrings;
property SectionWidth[Index: ?]: Integer;
property ShowHint: Boolean;
property TabOrder: TTabOrder;
property TabStop: Boolean;
property Touch: TTouchManager;
property Visible: Boolean;
procedure Sized(ASection: Integer; AWidth: Integer);
procedure Sizing(ASection: Integer; AWidth: Integer);

## THeaderControl
继承：THeaderControl → TCustomHeaderControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.ComCtrls

property Align: TAlign;
property Anchors: TAnchors;
property BiDiMode: TBiDiMode;
property BorderWidth: TBorderWidth;
property Constraints: TSizeConstraints;
property DoubleBuffered: Boolean;
property DragCursor: TCursor;
property DragKind: TDragKind;
property DragMode: TDragMode;
property DragReorder: Boolean;
property Enabled: Boolean;
property Font: TFont;
property FullDrag: Boolean;
property HotTrack: Boolean;
property Images: TCustomImageList;
property OnContextPopup: TContextPopupEvent;
property OnCreateSectionClass: TCustomHCCreateSectionClassEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnDrawSection: TDrawSectionEvent;
property OnEndDock: TEndDragEvent;
property OnEndDrag: TEndDragEvent;
property OnGesture: TGestureEvent;
property OnMouseActivate: TMouseActivateEvent;
property OnMouseDown: TMouseEvent;
property OnMouseEnter: TNotifyEvent;
property OnMouseLeave: TNotifyEvent;
property OnMouseMove: TMouseMoveEvent;
property OnMouseUp: TMouseEvent;
property OnResize: TNotifyEvent;
property OnSectionClick: TSectionNotifyEvent;
property OnSectionDrag: TSectionDragEvent;
property OnSectionEndDrag: TNotifyEvent;
property OnSectionResize: TSectionNotifyEvent;
property OnSectionTrack: TSectionTrackEvent;
property OnStartDock: TStartDockEvent;
property OnStartDrag: TStartDragEvent;
property ParentBiDiMode: Boolean;
property ParentDoubleBuffered: Boolean;
property ParentFont: Boolean;
property ParentShowHint: Boolean;
property PopupMenu: TPopupMenu;
property Sections: THeaderSections;
property ShowHint: Boolean;
property Style: THeaderStyle;
property StyleElements: TStyleElements;
property Touch: TTouchManager;
property Visible: Boolean;

## THeaderSection
继承：THeaderSection → TCollectionItem → TPersistent → TObject ｜ 单元：Vcl.ComCtrls

property Alignment: TAlignment;
property AllowClick: Boolean;
property AutoSize: Boolean;
property BiDiMode: TBiDiMode;
property CheckBox: Boolean;
property Checked: Boolean;
property FixedWidth: Boolean;
property ImageIndex: TImageIndex;
property Left: Integer;  // read-only
property MaxWidth: Integer;
property MinWidth: Integer;
property ParentBiDiMode: Boolean;
property Right: Integer;  // read-only
property Style: THeaderSectionStyle;
property Text: string;
property Width: Integer;
procedure ParentBiDiModeChanged;
function UseRightToLeftAlignment: Boolean;
function UseRightToLeftReading: Boolean;

## THeaderSections
继承：THeaderSections → TCollection → TPersistent → TObject ｜ 单元：Vcl.ComCtrls

property Items[Index: ?]: THeaderSection;
function Add: THeaderSection;
function AddItem(Item: THeaderSection; Index: Integer): THeaderSection;
procedure Create(HeaderControl: TCustomHeaderControl);
function Insert(Index: Integer): THeaderSection;

## THeaderStyleHook
继承：THeaderStyleHook → TMouseTrackControlStyleHook → TMouseTrackControlStyleHook ｜ 单元：Vcl.ComCtrls


## THelpAction
继承：THelpAction → TAction → TCustomAction → TContainedAction ｜ 单元：Vcl.StdActns


## THelpContents
继承：THelpContents → THelpAction → TAction → TCustomAction → TContainedAction ｜ 单元：Vcl.StdActns


## THelpContextAction
继承：THelpContextAction → THelpAction → TAction → TCustomAction → TContainedAction ｜ 单元：Vcl.StdActns


## THelpOnHelp
继承：THelpOnHelp → THelpAction → TAction → TCustomAction → TContainedAction ｜ 单元：Vcl.StdActns


## THelpTopicSearch
继承：THelpTopicSearch → THelpAction → TAction → TCustomAction → TContainedAction ｜ 单元：Vcl.StdActns


## THintAction
继承：THintAction → TCustomAction → TContainedAction ｜ 单元：Vcl.StdActns

property Hint: string;

## THintWindow
继承：THintWindow → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.Controls

property BiDiMode: TBiDiMode;
property Canvas: TCanvas;  // read-only
property Caption: TCaption;
property Color: TColor;
property Font: TFont;
procedure ActivateHint(const Rect: IDispatch; const AHint: string);
procedure ActivateHintData(const Rect: IDispatch; const AHint: string; AData: Pointer);
function CalcHintRect(MaxWidth: Integer; const AHint: string; AData: Pointer): IDispatch;
function IsHintMsg(const Msg: IDispatch): Boolean;
procedure NCPaint(DC: HDC);
procedure ReleaseHandle;
function ShouldHideHint: Boolean;

## THotKey
继承：THotKey → TCustomHotKey → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.ComCtrls

property Anchors: TAnchors;
property AutoSize: Boolean;
property BiDiMode: TBiDiMode;
property Constraints: TSizeConstraints;
property Enabled: Boolean;
property Hint: string;
property HotKey: TShortCut;
property InvalidKeys: THKInvalidKeys;
property Modifiers: THKModifiers;
property OnChange: TNotifyEvent;
property OnContextPopup: TContextPopupEvent;
property OnEnter: TNotifyEvent;
property OnExit: TNotifyEvent;
property OnGesture: TGestureEvent;
property OnMouseActivate: TMouseActivateEvent;
property OnMouseDown: TMouseEvent;
property OnMouseEnter: TNotifyEvent;
property OnMouseLeave: TNotifyEvent;
property OnMouseMove: TMouseMoveEvent;
property OnMouseUp: TMouseEvent;
property ParentBiDiMode: Boolean;
property ParentShowHint: Boolean;
property PopupMenu: TPopupMenu;
property ShowHint: Boolean;
property StyleElements: TStyleElements;
property TabOrder: TTabOrder;
property TabStop: Boolean;
property Touch: TTouchManager;
property Visible: Boolean;

## THyperlink
继承：THyperlink → TInterfacedObject → TObject ｜ 单元：Rt_AbstractOutput

procedure Create(const AURL: string; const ADisplayText: string);

## TIcon
继承：TIcon → TGraphic → TInterfacedPersistent → TPersistent → TObject ｜ 单元：Vcl.Graphics

property Handle: HICON;
function HandleAllocated: Boolean;
procedure LoadFromResourceID(Instance: NativeUInt; ResID: Integer);
procedure LoadFromResourceName(Instance: NativeUInt; const ResName: string);
function ReleaseHandle: HICON;

## TIconImage
继承：TIconImage → TSharedImage → TObject ｜ 单元：Vcl.Graphics


## TIconOptions
继承：TIconOptions → TPersistent → TObject ｜ 单元：Vcl.ComCtrls

property Arrangement: TIconArrangement;
property AutoArrange: Boolean;
property WrapText: Boolean;
procedure Create(AOwner: TCustomListView);

## TIDispatchField
继承：TIDispatchField → TInterfaceField → TField → TComponent → TPersistent → TObject ｜ 单元：Data.DB

property Value: IDispatch;

## TImage
继承：TImage → TGraphicControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.ExtCtrls

property Align: TAlign;
property Anchors: TAnchors;
property AutoSize: Boolean;
property Canvas: TCanvas;  // read-only
property Center: Boolean;
property Constraints: TSizeConstraints;
property DragCursor: TCursor;
property DragKind: TDragKind;
property DragMode: TDragMode;
property Enabled: Boolean;
property IncrementalDisplay: Boolean;
property OnClick: TNotifyEvent;
property OnContextPopup: TContextPopupEvent;
property OnDblClick: TNotifyEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnEndDock: TEndDragEvent;
property OnEndDrag: TEndDragEvent;
property OnGesture: TGestureEvent;
property OnMouseActivate: TMouseActivateEvent;
property OnMouseDown: TMouseEvent;
property OnMouseEnter: TNotifyEvent;
property OnMouseLeave: TNotifyEvent;
property OnMouseMove: TMouseMoveEvent;
property OnMouseUp: TMouseEvent;
property OnProgress: TProgressEvent;
property OnStartDock: TStartDockEvent;
property OnStartDrag: TStartDragEvent;
property ParentShowHint: Boolean;
property Picture: TPicture;
property PopupMenu: TPopupMenu;
property Proportional: Boolean;
property ShowHint: Boolean;
property Stretch: Boolean;
property Touch: TTouchManager;
property Transparent: Boolean;
property Visible: Boolean;
procedure Progress(Sender: TObject; Stage: TProgressStage; PercentDone: Byte; RedrawNow: Boolean; const R: IDispatch; const Msg: string);

## TImageList
继承：TImageList → TDragImageList → TCustomImageList → TBaseImageList ｜ 单元：Vcl.Controls

property AllocBy: Integer;
property BkColor: TColor;
property BlendColor: TColor;
property ColorDepth: TColorDepth;
property DrawingStyle: TDrawingStyle;
property GrayscaleFactor: Byte;
property Height: Integer;
property ImageType: TImageType;
property Masked: Boolean;
property OnChange: TNotifyEvent;
property ShareImages: Boolean;
property Width: Integer;

## TImageMargins
继承：TImageMargins → TPersistent → TObject ｜ 单元：Vcl.StdCtrls

property Bottom: Integer;
property Left: Integer;
property Right: Integer;
property Top: Integer;
procedure Change;

## TIndexDef
继承：TIndexDef → TNamedItem → TCollectionItem → TPersistent → TObject ｜ 单元：Data.DB

property CaseInsFields: string;
property DescFields: string;
property Expression: string;
property FieldExpression: String;  // read-only
property Fields: string;
property GroupingLevel: Integer;
property Options: TIndexOptions;
property Source: string;
procedure Create(Owner: TIndexDefs; const Name: string; const Fields: string; Options: TIndexOptions);

## TIndexDefs
继承：TIndexDefs → TDefCollection → TOwnedCollection → TCollection → TPersistent → TObject ｜ 单元：Data.DB

property Items[Index: ?]: TIndexDef;
procedure Add(const Name: string; const Fields: string; Options: TIndexOptions);
function AddIndexDef: TIndexDef;
procedure Create(ADataSet: TDataSet);
function Find(const Name: string): TIndexDef;
function FindIndexForFields(const Fields: string): TIndexDef;
function GetIndexForFields(const Fields: string; CaseInsensitive: Boolean): TIndexDef;
procedure Update;

## TIniFile
继承：TIniFile → TCustomIniFile → TObject ｜ 单元：System.IniFiles


## TInplaceEdit
继承：TInplaceEdit → TCustomMaskEdit → TCustomEdit → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.Grids

procedure BoundsChanged;
procedure Deselect;
procedure Hide;
procedure Invalidate;
procedure Move(const Loc: IDispatch);
function PosEqual(const Rect: IDispatch): Boolean;
procedure SetFocus;
procedure UpdateContents;
procedure UpdateLoc(const Loc: IDispatch);
function Visible: Boolean;

## TInplaceEditList
继承：TInplaceEditList → TInplaceEdit → TCustomMaskEdit → TCustomEdit → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.Grids

property ActiveList: TWinControl;
property ButtonWidth: Integer;
property DropDownRows: Integer;
property EditStyle: TEditStyle;  // read-only
property ListVisible: Boolean;
property PickList: TCustomListbox;  // read-only
property PickListLoaded: Boolean;
property Pressed: Boolean;  // read-only
procedure CloseUp(Accept: Boolean);
procedure DoDropDownKeys(var Key: Word; Shift: TShiftState);
procedure DoEditButtonClick;
procedure DoGetPickListItems;
procedure DropDown;
procedure RestoreContents;

## TInputIOSignalLink
继承：TInputIOSignalLink → TIOSignalLink → TComponent → TPersistent → TObject ｜ 单元：RT_Digital_IO

property OnChange: TInputSignalChangedEvent;

## TInstrumentBackground
继承：TInstrumentBackground → TCustomGraphicInstrumentWithInterior → TCustomGraphicInstrumentWithBackground → TGraphicControl → TControl → TComponent → TPersistent → TObject ｜ 单元：InstrumentExtControls

property Align: TAlign;
property Anchors: TAnchors;
property BackgroundOptions: TInstrumentBackgroundOptions;
property Color: TColor;
property Constraints: TSizeConstraints;
property CustomHint: TCustomHint;
property DragCursor: TCursor;
property DragKind: TDragKind;
property DragMode: TDragMode;
property Enabled: Boolean;
property OnClick: TNotifyEvent;
property OnContextPopup: TContextPopupEvent;
property OnDblClick: TNotifyEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnEndDock: TEndDragEvent;
property OnEndDrag: TEndDragEvent;
property OnMouseActivate: TMouseActivateEvent;
property OnMouseDown: TMouseEvent;
property OnMouseEnter: TNotifyEvent;
property OnMouseLeave: TNotifyEvent;
property OnMouseMove: TMouseMoveEvent;
property OnMouseUp: TMouseEvent;
property OnStartDock: TStartDockEvent;
property OnStartDrag: TStartDragEvent;
property ParentColor: Boolean;
property ParentShowHint: Boolean;
property PopupMenu: TPopupMenu;
property ShowHint: Boolean;
property Visible: Boolean;

## TInstrumentBackgroundPanel
继承：TInstrumentBackgroundPanel → TCustomInstrumentBackgroundPanel → TXPCustomExtPanel → TXPCustomControl → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：InstrumentPanels

property Align: TAlign;
property Alignment: TAlignment;
property Anchors: TAnchors;
property Bitmap: TBitmap;
property Constraints: TSizeConstraints;
property CoreName: string;
property CustomHint: TCustomHint;
property DockSite: Boolean;
property DoubleBuffered: Boolean;
property DragCursor: TCursor;
property DragKind: TDragKind;
property DragMode: TDragMode;
property Enabled: Boolean;
property Font: TFont;
property JtagID: Integer;
property Kind: TXPExtPanelKind;
property OnCanResize: TCanResizeEvent;
property OnClick: TNotifyEvent;
property OnConstrainedResize: TConstrainedResizeEvent;
property OnContextPopup: TContextPopupEvent;
property OnDblClick: TNotifyEvent;
property OnDockDrop: TDockDropEvent;
property OnDockOver: TDockOverEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnEndDock: TEndDragEvent;
property OnEndDrag: TEndDragEvent;
property OnEnter: TNotifyEvent;
property OnExit: TNotifyEvent;
property OnGetSiteInfo: TGetSiteInfoEvent;
property OnMouseDown: TMouseEvent;
property OnMouseMove: TMouseMoveEvent;
property OnMouseUp: TMouseEvent;
property OnPaint: TNotifyEvent;
property OnResize: TNotifyEvent;
property OnStartDock: TStartDockEvent;
property OnStartDrag: TStartDragEvent;
property OnUnDock: TUnDockEvent;
property ParentFont: Boolean;
property ParentShowHint: Boolean;
property PopupMenu: TPopupMenu;
property PortID: Integer;
property Primary: Boolean;
property ShowCoreName: Boolean;
property ShowGrooves: Boolean;
property ShowHint: Boolean;
property ShowJTAG: Boolean;
property ShowMountingHoles: Boolean;
property ShowTitle: Boolean;
property Style: TInstrumentPanelStyle;
property Title: string;
property UseDockManager: Boolean;
property Visible: Boolean;

## TInstrumentButton
继承：TInstrumentButton → TCustomInstrumentButton → TXPCustomSpeedButton → TXPBaseCustomSpeedButton → TXPCustomTransparentControl → TXPCustomControl → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：InstrumentButtons

property Action: TBasicAction;
property AllowAllUp: Boolean;
property Anchors: TAnchors;
property Backlight: Boolean;
property Caption: TCaption;
property Down: Boolean;
property Enabled: Boolean;
property Font: TFont;
property GroupIndex: Integer;
property OnClick: TNotifyEvent;
property OnContextPopup: TContextPopupEvent;
property OnDblClick: TNotifyEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnEndDrag: TEndDragEvent;
property OnMouseActivate: TMouseActivateEvent;
property OnMouseDown: TMouseEvent;
property OnMouseEnter: TNotifyEvent;
property OnMouseLeave: TNotifyEvent;
property OnMouseMove: TMouseMoveEvent;
property OnMouseUp: TMouseEvent;
property OnStartDrag: TStartDragEvent;
property ParentFont: Boolean;
property ParentShowHint: Boolean;
property PopupMenu: TPopupMenu;
property ShowHint: Boolean;
property Visible: Boolean;

## TInstrumentCaption
继承：TInstrumentCaption → TCustomInstrumentCaption → TCustomInstrumentLabel → TCustomLabel → TGraphicControl → TControl → TComponent → TPersistent → TObject ｜ 单元：InstrumentLabels

property Align: TAlign;
property Alignment: TAlignment;
property Anchors: TAnchors;
property AutoSize: Boolean;
property Caption: TCaption;
property Color: TColor;
property Constraints: TSizeConstraints;
property CustomHint: TCustomHint;
property DragCursor: TCursor;
property DragKind: TDragKind;
property DragMode: TDragMode;
property EllipsisPosition: TEllipsisPosition;
property Enabled: Boolean;
property FocusControl: TWinControl;
property Font: TFont;
property OnClick: TNotifyEvent;
property OnContextPopup: TContextPopupEvent;
property OnDblClick: TNotifyEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnEndDrag: TEndDragEvent;
property OnMouseDown: TMouseEvent;
property OnMouseEnter: TNotifyEvent;
property OnMouseLeave: TNotifyEvent;
property OnMouseMove: TMouseMoveEvent;
property OnMouseUp: TMouseEvent;
property OnStartDrag: TStartDragEvent;
property ParentColor: Boolean;
property ParentFont: Boolean;
property ParentShowHint: Boolean;
property PopupMenu: TPopupMenu;
property ShowAccelChar: Boolean;
property ShowHint: Boolean;
property Transparent: Boolean;
property Visible: Boolean;

## TInstrumentCheckBox
继承：TInstrumentCheckBox → TCustomInstrumentCheckBox → TGraphicControl → TControl → TComponent → TPersistent → TObject ｜ 单元：InstrumentChecks

property Action: TBasicAction;
property Alignment: TLeftRight;
property Anchors: TAnchors;
property Caption: TCaption;
property Checked: Boolean;
property Constraints: TSizeConstraints;
property CustomHint: TCustomHint;
property DragCursor: TCursor;
property DragKind: TDragKind;
property DragMode: TDragMode;
property Enabled: Boolean;
property Font: TFont;
property GlyphStyle: TInstrumentCheckStyle;
property OnClick: TNotifyEvent;
property OnContextPopup: TContextPopupEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnEndDrag: TEndDragEvent;
property OnMouseDown: TMouseEvent;
property OnMouseMove: TMouseMoveEvent;
property OnMouseUp: TMouseEvent;
property OnStartDrag: TStartDragEvent;
property ParentFont: Boolean;
property ParentShowHint: Boolean;
property PopupMenu: TPopupMenu;
property ReadOnly: Boolean;
property ShowHint: Boolean;
property Visible: Boolean;

## TInstrumentEdit
继承：TInstrumentEdit → TCustomInstrumentEdit → TCustomXPEdit → TXPCustomControl → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：InstrumentExtControls

property Align: TAlign;
property Anchors: TAnchors;
property AutoSelect: Boolean;
property AutoSize: Boolean;
property BorderStyle: TBorderStyle;
property CharCase: TEditCharCase;
property Color: TColor;
property Constraints: TSizeConstraints;
property Ctl3D: Boolean;
property Cursor: TCursor;
property CustomHint: TCustomHint;
property DoubleBuffered: Boolean;
property DragCursor: TCursor;
property DragKind: TDragKind;
property DragMode: TDragMode;
property Enabled: Boolean;
property Font: TFont;
property HideSelection: Boolean;
property HotTrack: Boolean;
property ImeMode: TImeMode;
property ImeName: TImeName;
property MaxLength: Integer;
property OEMConvert: Boolean;
property OnChange: TNotifyEvent;
property OnClick: TNotifyEvent;
property OnContextPopup: TContextPopupEvent;
property OnDblClick: TNotifyEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnEndDrag: TEndDragEvent;
property OnEnter: TNotifyEvent;
property OnExit: TNotifyEvent;
property OnKeyDown: TKeyEvent;
property OnKeyPress: TKeyPressEvent;
property OnKeyUp: TKeyEvent;
property OnMouseActivate: TMouseActivateEvent;
property OnMouseDown: TMouseEvent;
property OnMouseEnter: TNotifyEvent;
property OnMouseLeave: TNotifyEvent;
property OnMouseMove: TMouseMoveEvent;
property OnMouseUp: TMouseEvent;
property OnStartDrag: TStartDragEvent;
property ParentColor: Boolean;
property ParentCtl3D: Boolean;
property ParentFont: Boolean;
property ParentShowHint: Boolean;
property PasswordChar: Char;
property PopupMenu: TPopupMenu;
property ReadOnly: Boolean;
property ShowHint: Boolean;
property TabOrder: TTabOrder;
property TabStop: Boolean;
property Text: TCaption;
property Transparent: Boolean;
property Visible: Boolean;

## TInstrumentGauge
继承：TInstrumentGauge → TCustomInstrumentGauge → TCustomGraphicInstrumentWithNoise → TCustomGraphicInstrumentWithBackground → TGraphicControl → TControl → TComponent → TPersistent → TObject ｜ 单元：InstrumentGauges

property Anchors: TAnchors;
property AutoSize: Boolean;
property BackgroundOptions: TInstrumentBackgroundOptions;
property Color: TColor;
property Constraints: TSizeConstraints;
property CustomHint: TCustomHint;
property DragCursor: TCursor;
property DragKind: TDragKind;
property DragMode: TDragMode;
property DrawMode: TGaugeDrawMode;
property Enabled: Boolean;
property EndAngle: TDegAngle;
property Font: TFont;
property InactiveColor: TColor;
property LargeTicks: TInstrumentTicksFloat;
property Margin: NaturalNumber;
property Max: Double;
property MediumTicks: TInstrumentTicksFloat;
property Min: Double;
property Needle: TGaugeNeedle;
property Numbers: TInstrumentNumbers;
property OnClick: TNotifyEvent;
property OnContextPopup: TContextPopupEvent;
property OnDblClick: TNotifyEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnEndDock: TEndDragEvent;
property OnEndDrag: TEndDragEvent;
property OnGetScaleLabel: TGetTextFloatEvent;
property OnMouseActivate: TMouseActivateEvent;
property OnMouseDown: TMouseEvent;
property OnMouseEnter: TNotifyEvent;
property OnMouseLeave: TNotifyEvent;
property OnMouseMove: TMouseMoveEvent;
property OnMouseUp: TMouseEvent;
property OnStartDock: TStartDockEvent;
property OnStartDrag: TStartDragEvent;
property Options: TGaugeOptions;
property ParentColor: Boolean;
property ParentFont: Boolean;
property ParentShowHint: Boolean;
property PopupMenu: TPopupMenu;
property Position: Double;
property Radius: NaturalNumber;
property ShowHint: Boolean;
property SmallTicks: TInstrumentTicksFloat;
property StartAngle: TDegAngle;
property Visible: Boolean;

## TInstrumentGlyphButton
继承：TInstrumentGlyphButton → TCustomInstrumentGlyphButton → TCustomInstrumentButton → TXPCustomSpeedButton → TXPBaseCustomSpeedButton → TXPCustomTransparentControl → TXPCustomControl → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：InstrumentButtons

property Action: TBasicAction;
property AllowAllUp: Boolean;
property Anchors: TAnchors;
property Backlight: Boolean;
property BacklightColor: TColor;
property Caption: TCaption;
property CaptionGlowIntensity: TGlowIntensity;
property CaptionLEDStyle: TInstrumentLEDStyle;
property Down: Boolean;
property Enabled: Boolean;
property Font: TFont;
property Glyph: TGraphic;
property GroupIndex: Integer;
property IsLED: Boolean;
property NumGlyphs: TNumGlyphs;
property OnClick: TNotifyEvent;
property OnContextPopup: TContextPopupEvent;
property OnDblClick: TNotifyEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnEndDrag: TEndDragEvent;
property OnMouseActivate: TMouseActivateEvent;
property OnMouseDown: TMouseEvent;
property OnMouseEnter: TNotifyEvent;
property OnMouseLeave: TNotifyEvent;
property OnMouseMove: TMouseMoveEvent;
property OnMouseUp: TMouseEvent;
property OnStartDrag: TStartDragEvent;
property ParentFont: Boolean;
property ParentShowHint: Boolean;
property PopupMenu: TPopupMenu;
property ShowHint: Boolean;
property Visible: Boolean;

## TInstrumentGraph
继承：TInstrumentGraph → TCustomInstrumentSingleGraph → TCustomInstrumentGraph → TCustomGraphicInstrumentWithInterior → TCustomGraphicInstrumentWithBackground → TGraphicControl → TControl → TComponent → TPersistent → TObject ｜ 单元：InstrumentGraphs

property Align: TAlign;
property Anchors: TAnchors;
property BackgroundOptions: TInstrumentBackgroundOptions;
property Color: TColor;
property Constraints: TSizeConstraints;
property CustomHint: TCustomHint;
property DragCursor: TCursor;
property DragKind: TDragKind;
property DragMode: TDragMode;
property Enabled: Boolean;
property Grid: TGraphGrid;
property HighThreshold: TGraphThreshold;
property LowThreshold: TGraphThreshold;
property Margin: NaturalNumber;
property Max: Double;
property Min: Double;
property OnClick: TNotifyEvent;
property OnContextPopup: TContextPopupEvent;
property OnDblClick: TNotifyEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnEndDock: TEndDragEvent;
property OnEndDrag: TEndDragEvent;
property OnGetValue: TGetValueEvent;
property OnMouseActivate: TMouseActivateEvent;
property OnMouseDown: TMouseEvent;
property OnMouseEnter: TNotifyEvent;
property OnMouseLeave: TNotifyEvent;
property OnMouseMove: TMouseMoveEvent;
property OnMouseUp: TMouseEvent;
property OnStartDock: TStartDockEvent;
property OnStartDrag: TStartDragEvent;
property ParentColor: Boolean;
property ParentShowHint: Boolean;
property Polling: TGraphPolling;
property PopupMenu: TPopupMenu;
property Shift: NaturalNumber;
property ShowHint: Boolean;
property SignalForm: TGraphSignal;
property Value: Double;
property Visible: Boolean;

## TInstrumentKnob
继承：TInstrumentKnob → TCustomInstrumentKnob → TCustomInstrumentSlider → TXPCustomControl → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：InstrumentSliders

property Anchors: TAnchors;
property Constraints: TSizeConstraints;
property CustomHint: TCustomHint;
property Discrete: Boolean;
property DoubleBuffered: Boolean;
property DragCursor: TCursor;
property DragKind: TDragKind;
property DragMode: TDragMode;
property Enabled: Boolean;
property Font: TFont;
property Increment: Double;
property KnobColor: TInstrumentKnobColor;
property KnobSize: TInstrumentSize;
property LargeTicks: TInstrumentTicksFloat;
property MaxValue: Double;
property MediumTicks: TInstrumentTicksFloat;
property MinValue: Double;
property Numbers: TInstrumentNumbers;
property OnChange: TNotifyEvent;
property OnClick: TNotifyEvent;
property OnDblClick: TNotifyEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnEndDrag: TEndDragEvent;
property OnGetHintText: TGetTextFloatEvent;
property OnGetScaleLabel: TGetTextFloatExEvent;
property OnMouseDown: TMouseEvent;
property OnMouseMove: TMouseMoveEvent;
property OnMouseUp: TMouseEvent;
property OnStartDrag: TStartDragEvent;
property ParentFont: Boolean;
property ParentShowHint: Boolean;
property PopupMenu: TPopupMenu;
property ScaleVisible: Boolean;
property Sensitivity: Integer;
property ShowHint: Boolean;
property ShowToolTip: TPositionToolTip;
property SideLength: Integer;
property SmallTicks: TInstrumentTicksFloat;
property Style: TInstrumentKnobStyle;
property TickStartRadius: Integer;
property Value: Double;
property ValueIncrement: Double;
property Visible: Boolean;

## TInstrumentLabel
继承：TInstrumentLabel → TCustomInstrumentLabel → TCustomLabel → TGraphicControl → TControl → TComponent → TPersistent → TObject ｜ 单元：InstrumentLabels

property Align: TAlign;
property Alignment: TAlignment;
property Anchors: TAnchors;
property AutoSize: Boolean;
property Caption: TCaption;
property Color: TColor;
property Constraints: TSizeConstraints;
property CustomHint: TCustomHint;
property DragCursor: TCursor;
property DragKind: TDragKind;
property DragMode: TDragMode;
property EllipsisPosition: TEllipsisPosition;
property Enabled: Boolean;
property FocusControl: TWinControl;
property Font: TFont;
property Layout: TTextLayout;
property OnClick: TNotifyEvent;
property OnContextPopup: TContextPopupEvent;
property OnDblClick: TNotifyEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnEndDrag: TEndDragEvent;
property OnMouseDown: TMouseEvent;
property OnMouseEnter: TNotifyEvent;
property OnMouseLeave: TNotifyEvent;
property OnMouseMove: TMouseMoveEvent;
property OnMouseUp: TMouseEvent;
property OnStartDrag: TStartDragEvent;
property ParentColor: Boolean;
property ParentFont: Boolean;
property ParentShowHint: Boolean;
property PopupMenu: TPopupMenu;
property ShowAccelChar: Boolean;
property ShowHint: Boolean;
property Transparent: Boolean;
property Visible: Boolean;

## TInstrumentLEDButton
继承：TInstrumentLEDButton → TInstrumentGlyphButton → TCustomInstrumentGlyphButton → TCustomInstrumentButton → TXPCustomSpeedButton → TXPBaseCustomSpeedButton → TXPCustomTransparentControl → TXPCustomControl → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：InstrumentExtControls


## TInstrumentLEDDigits
继承：TInstrumentLEDDigits → TCustomInstrumentLEDDigits → TCustomInstrumentDigitsPanel → TCustomGraphicInstrumentWithInterior → TCustomGraphicInstrumentWithBackground → TGraphicControl → TControl → TComponent → TPersistent → TObject ｜ 单元：InstrumentDigitPanels

property ActiveColor: TColor;
property Align: TAlign;
property Alignment: TLeftRight;
property Anchors: TAnchors;
property AutoSize: Boolean;
property BackgroundOptions: TInstrumentBackgroundOptions;
property Color: TColor;
property ColorScheme: TLEDColorScheme;
property Constraints: TSizeConstraints;
property Digits: NaturalNumber;
property DigitsInGroup: NaturalNumber;
property DragCursor: TCursor;
property DragKind: TDragKind;
property DragMode: TDragMode;
property Enabled: Boolean;
property InactiveColor: TColor;
property Margin: NaturalNumber;
property MaxValue: Double;
property Metrics: TLEDDigitsMetrics;
property MinValue: Double;
property NumberType: TNumberType;
property OnClick: TNotifyEvent;
property OnContextPopup: TContextPopupEvent;
property OnDblClick: TNotifyEvent;
property OnDigitClick: TDigitMouseClickEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnEndDock: TEndDragEvent;
property OnEndDrag: TEndDragEvent;
property OnMouseActivate: TMouseActivateEvent;
property OnMouseDown: TMouseEvent;
property OnMouseEnter: TNotifyEvent;
property OnMouseLeave: TNotifyEvent;
property OnMouseMove: TMouseMoveEvent;
property OnMouseUp: TMouseEvent;
property OnStartDock: TStartDockEvent;
property OnStartDrag: TStartDragEvent;
property Options: TDigitsPanelOptions;
property ParentColor: Boolean;
property ParentShowHint: Boolean;
property PopupMenu: TPopupMenu;
property Precision: TPrecision;
property Radix: TRadix;
property ShowHint: Boolean;
property Value: Double;
property Visible: Boolean;

## TInstrumentLEDsPanel
继承：TInstrumentLEDsPanel → TCustomInstrumentLEDsPanel → TCustomInstrumentDigitsPanelWithBackground → TCustomInstrumentDigitsPanel → TCustomGraphicInstrumentWithInterior → TCustomGraphicInstrumentWithBackground → TGraphicControl → TControl → TComponent → TPersistent → TObject ｜ 单元：InstrumentDigitPanels

property Align: TAlign;
property Alignment: TLeftRight;
property Anchors: TAnchors;
property AutoSize: Boolean;
property BackgroundOptions: TInstrumentBackgroundOptions;
property Color: TColor;
property Constraints: TSizeConstraints;
property CreamBackground: Boolean;
property CustomHint: TCustomHint;
property Digits: NaturalNumber;
property DigitsInGroup: NaturalNumber;
property DragCursor: TCursor;
property DragKind: TDragKind;
property DragMode: TDragMode;
property Enabled: Boolean;
property Margin: NaturalNumber;
property MaxValue: Cardinal;
property Metrics: TDigitsPanelMetrics;
property MinValue: Cardinal;
property OnClick: TNotifyEvent;
property OnContextPopup: TContextPopupEvent;
property OnDblClick: TNotifyEvent;
property OnDigitClick: TDigitMouseClickEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnEndDock: TEndDragEvent;
property OnEndDrag: TEndDragEvent;
property OnMouseActivate: TMouseActivateEvent;
property OnMouseDown: TMouseEvent;
property OnMouseEnter: TNotifyEvent;
property OnMouseLeave: TNotifyEvent;
property OnMouseMove: TMouseMoveEvent;
property OnMouseUp: TMouseEvent;
property OnStartDock: TStartDockEvent;
property OnStartDrag: TStartDragEvent;
property Options: TDigitsPanelOptions;
property ParentColor: Boolean;
property ParentShowHint: Boolean;
property PopupMenu: TPopupMenu;
property ShowHint: Boolean;
property Style: TInstrumentCheckStyle;
property Value: Cardinal;
property Visible: Boolean;

## TInstrumentListBox
继承：TInstrumentListBox → TCustomInstrumentListBox → TCustomXPListBox → TXPCustomControl → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：InstrumentLists

property Align: TAlign;
property AllowGrayed: Boolean;
property AlphaNumericSorting: Boolean;
property Anchors: TAnchors;
property AutoComplete: Boolean;
property AutoCompleteDelay: Cardinal;
property Checked[Index: ?]: Boolean;
property CheckStyle: TInstrumentCheckStyle;
property Columns: Cardinal;
property Constraints: TSizeConstraints;
property Count: Integer;  // read-only
property CustomHint: TCustomHint;
property DoubleBuffered: Boolean;
property DragCursor: TCursor;
property DragKind: TDragKind;
property DragMode: TDragMode;
property Enabled: Boolean;
property ExtendedSelect: Boolean;
property Font: TFont;
property ItemHeight: Integer;
property ItemIndex: Integer;
property Items: TStrings;
property MultiSelect: Boolean;
property OnClick: TNotifyEvent;
property OnClickCheck: TNotifyEvent;
property OnContextPopup: TContextPopupEvent;
property OnDblClick: TNotifyEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnEndDock: TEndDragEvent;
property OnEndDrag: TEndDragEvent;
property OnEnter: TNotifyEvent;
property OnExit: TNotifyEvent;
property OnKeyDown: TKeyEvent;
property OnKeyPress: TKeyPressEvent;
property OnKeyUp: TKeyEvent;
property OnMouseActivate: TMouseActivateEvent;
property OnMouseDown: TMouseEvent;
property OnMouseEnter: TNotifyEvent;
property OnMouseLeave: TNotifyEvent;
property OnMouseMove: TMouseMoveEvent;
property OnMouseUp: TMouseEvent;
property OnStartDock: TStartDockEvent;
property OnStartDrag: TStartDragEvent;
property ParentFont: Boolean;
property ParentShowHint: Boolean;
property PopupMenu: TPopupMenu;
property ScrollBars: TXPScrollStyle;
property SelCount: Integer;  // read-only
property Selected[Index: ?]: Boolean;
property ShowHint: Boolean;
property Sorted: Boolean;
property State[Index: ?]: TCheckBoxState;
property TabOrder: TTabOrder;
property TabStop: Boolean;
property TopIndex: Integer;
property UseCheckBoxes: Boolean;
property Visible: Boolean;

## TInstrumentMultiGraph
继承：TInstrumentMultiGraph → TCustomInstrumentMultiGraph → TCustomInstrumentGraph → TCustomGraphicInstrumentWithInterior → TCustomGraphicInstrumentWithBackground → TGraphicControl → TControl → TComponent → TPersistent → TObject ｜ 单元：InstrumentGraphs

property Align: TAlign;
property Anchors: TAnchors;
property BackgroundOptions: TInstrumentBackgroundOptions;
property Color: TColor;
property Constraints: TSizeConstraints;
property CustomHint: TCustomHint;
property DragCursor: TCursor;
property DragKind: TDragKind;
property DragMode: TDragMode;
property Enabled: Boolean;
property Grid: TGraphGrid;
property HighThreshold: TGraphThreshold;
property LowThreshold: TGraphThreshold;
property Margin: NaturalNumber;
property Max: Double;
property Min: Double;
property OnClick: TNotifyEvent;
property OnContextPopup: TContextPopupEvent;
property OnDblClick: TNotifyEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnEndDock: TEndDragEvent;
property OnEndDrag: TEndDragEvent;
property OnGetValue: TGetMultiValueEvent;
property OnMouseActivate: TMouseActivateEvent;
property OnMouseDown: TMouseEvent;
property OnMouseEnter: TNotifyEvent;
property OnMouseLeave: TNotifyEvent;
property OnMouseMove: TMouseMoveEvent;
property OnMouseUp: TMouseEvent;
property OnStartDock: TStartDockEvent;
property OnStartDrag: TStartDragEvent;
property ParentColor: Boolean;
property ParentShowHint: Boolean;
property Polling: TGraphPolling;
property PopupMenu: TPopupMenu;
property Shift: NaturalNumber;
property ShowHint: Boolean;
property Signals: TGraphSignals;
property Visible: Boolean;

## TInstrumentNumbers
继承：TInstrumentNumbers → TPersistent → TObject ｜ 单元：InstrumentClasses

property Gap: Integer;
property Visible: Boolean;
procedure Create(AOwner: TControl);

## TInstrumentNumbersFloat
继承：TInstrumentNumbersFloat → TInstrumentNumbers → TPersistent → TObject ｜ 单元：InstrumentClasses

property Gap: Integer;
property Step: Double;
property Visible: Boolean;

## TInstrumentNumbersInt
继承：TInstrumentNumbersInt → TInstrumentNumbers → TPersistent → TObject ｜ 单元：InstrumentClasses

property Gap: Integer;
property Step: Int64;
property Visible: Boolean;

## TInstrumentNumericPanel
继承：TInstrumentNumericPanel → TCustomInstrumentNumericPanel → TCustomInstrumentDigitsPanelWithBackground → TCustomInstrumentDigitsPanel → TCustomGraphicInstrumentWithInterior → TCustomGraphicInstrumentWithBackground → TGraphicControl → TControl → TComponent → TPersistent → TObject ｜ 单元：InstrumentDigitPanels

property Align: TAlign;
property Alignment: TLeftRight;
property Anchors: TAnchors;
property AutoSize: Boolean;
property BackgroundOptions: TInstrumentBackgroundOptions;
property Color: TColor;
property Constraints: TSizeConstraints;
property CreamBackground: Boolean;
property CustomHint: TCustomHint;
property Digits: NaturalNumber;
property DigitsInGroup: NaturalNumber;
property DragCursor: TCursor;
property DragKind: TDragKind;
property DragMode: TDragMode;
property Enabled: Boolean;
property Font: TFont;
property GroupSeparator: Char;
property Margin: NaturalNumber;
property MaxValue: Double;
property Metrics: TDigitsPanelMetrics;
property MinValue: Double;
property NumberType: TNumberType;
property OnClick: TNotifyEvent;
property OnContextPopup: TContextPopupEvent;
property OnDblClick: TNotifyEvent;
property OnDigitClick: TDigitMouseClickEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnEndDock: TEndDragEvent;
property OnEndDrag: TEndDragEvent;
property OnMouseActivate: TMouseActivateEvent;
property OnMouseDown: TMouseEvent;
property OnMouseEnter: TNotifyEvent;
property OnMouseLeave: TNotifyEvent;
property OnMouseMove: TMouseMoveEvent;
property OnMouseUp: TMouseEvent;
property OnStartDock: TStartDockEvent;
property OnStartDrag: TStartDragEvent;
property Options: TDigitsPanelOptions;
property ParentColor: Boolean;
property ParentFont: Boolean;
property ParentShowHint: Boolean;
property PopupMenu: TPopupMenu;
property Precision: TPrecision;
property Radix: TRadix;
property ShowHint: Boolean;
property Value: Double;
property Visible: Boolean;

## TInstrumentPanel
继承：TInstrumentPanel → TCustomInstrumentPanel → TXPCustomControl → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：InstrumentPanels

property Align: TAlign;
property Anchors: TAnchors;
property AutoSize: Boolean;
property Constraints: TSizeConstraints;
property CustomHint: TCustomHint;
property DisplayStyle: TDisplayStyle;
property DockSite: Boolean;
property DoubleBuffered: Boolean;
property DragCursor: TCursor;
property DragKind: TDragKind;
property DragMode: TDragMode;
property Enabled: Boolean;
property Font: TFont;
property OnCanResize: TCanResizeEvent;
property OnClick: TNotifyEvent;
property OnConstrainedResize: TConstrainedResizeEvent;
property OnContextPopup: TContextPopupEvent;
property OnDblClick: TNotifyEvent;
property OnDockDrop: TDockDropEvent;
property OnDockOver: TDockOverEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnEndDock: TEndDragEvent;
property OnEndDrag: TEndDragEvent;
property OnEnter: TNotifyEvent;
property OnExit: TNotifyEvent;
property OnGetSiteInfo: TGetSiteInfoEvent;
property OnMouseDown: TMouseEvent;
property OnMouseMove: TMouseMoveEvent;
property OnMouseUp: TMouseEvent;
property OnResize: TNotifyEvent;
property OnStartDock: TStartDockEvent;
property OnStartDrag: TStartDragEvent;
property OnUnDock: TUnDockEvent;
property ParentDisplayStyle: Boolean;
property ParentFont: Boolean;
property ParentShowHint: Boolean;
property PopupMenu: TPopupMenu;
property ShowHint: Boolean;
property TabStop: Boolean;
property UseDockManager: Boolean;
property Visible: Boolean;

## TInstrumentProgressBar
继承：TInstrumentProgressBar → TCustomInstrumentProgressBar → TCustomGraphicInstrumentWithNoise → TCustomGraphicInstrumentWithBackground → TGraphicControl → TControl → TComponent → TPersistent → TObject ｜ 单元：InstrumentProgress

property ActiveColors: TXPGradient;
property Align: TAlign;
property Anchors: TAnchors;
property BackgroundOptions: TInstrumentBackgroundOptions;
property BarColor: TColor;
property BarEndColor: TColor;
property BarInactiveColor: TColor;
property BarMiddleColor: TColor;
property Color: TColor;
property ColorScheme: TLEDColorScheme;
property Constraints: TSizeConstraints;
property CustomHint: TCustomHint;
property DragCursor: TCursor;
property DragKind: TDragKind;
property DragMode: TDragMode;
property Enabled: Boolean;
property InactiveColors: TXPGradient;
property Margin: NaturalNumber;
property Max: Double;
property Metrics: TProgressBarMetrics;
property Min: Double;
property OnClick: TNotifyEvent;
property OnContextPopup: TContextPopupEvent;
property OnDblClick: TNotifyEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnEndDock: TEndDragEvent;
property OnEndDrag: TEndDragEvent;
property OnMouseActivate: TMouseActivateEvent;
property OnMouseDown: TMouseEvent;
property OnMouseEnter: TNotifyEvent;
property OnMouseLeave: TNotifyEvent;
property OnMouseMove: TMouseMoveEvent;
property OnMouseUp: TMouseEvent;
property OnStartDock: TStartDockEvent;
property OnStartDrag: TStartDragEvent;
property Options: TProgressBarOptions;
property Orientation: TProgressBarOrientation;
property ParentColor: Boolean;
property ParentShowHint: Boolean;
property PopupMenu: TPopupMenu;
property Position: Double;
property ShowHint: Boolean;
property Visible: Boolean;

## TInstrumentRadioButton
继承：TInstrumentRadioButton → TCustomInstrumentRadioButton → TCustomInstrumentCheckBox → TGraphicControl → TControl → TComponent → TPersistent → TObject ｜ 单元：InstrumentChecks

property Action: TBasicAction;
property Alignment: TLeftRight;
property Anchors: TAnchors;
property Caption: TCaption;
property Checked: Boolean;
property Constraints: TSizeConstraints;
property CustomHint: TCustomHint;
property DragCursor: TCursor;
property DragKind: TDragKind;
property DragMode: TDragMode;
property Enabled: Boolean;
property Font: TFont;
property GlyphStyle: TInstrumentCheckStyle;
property GroupIndex: Integer;
property OnClick: TNotifyEvent;
property OnContextPopup: TContextPopupEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnEndDrag: TEndDragEvent;
property OnMouseDown: TMouseEvent;
property OnMouseMove: TMouseMoveEvent;
property OnMouseUp: TMouseEvent;
property OnStartDrag: TStartDragEvent;
property ParentFont: Boolean;
property ParentShowHint: Boolean;
property PopupMenu: TPopupMenu;
property ReadOnly: Boolean;
property ShowHint: Boolean;
property Visible: Boolean;

## TInstrumentRadioGroup
继承：TInstrumentRadioGroup → TCustomInstrumentRadioGroup → TCustomInstrumentPanel → TXPCustomControl → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：InstrumentChecks

property Align: TAlign;
property Anchors: TAnchors;
property Background: Boolean;
property Constraints: TSizeConstraints;
property CustomHint: TCustomHint;
property DoubleBuffered: Boolean;
property DragCursor: TCursor;
property DragKind: TDragKind;
property DragMode: TDragMode;
property Enabled: Boolean;
property Font: TFont;
property GlyphStyle: TInstrumentCheckStyle;
property ItemIndex: Integer;
property Items: TStrings;
property LEDClickAction: TLEDClickAction;
property OnClick: TNotifyEvent;
property OnContextPopup: TContextPopupEvent;
property OnDblClick: TNotifyEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnEndDrag: TEndDragEvent;
property OnEnter: TNotifyEvent;
property OnExit: TNotifyEvent;
property OnMouseActivate: TMouseActivateEvent;
property OnMouseDown: TMouseEvent;
property OnMouseEnter: TNotifyEvent;
property OnMouseLeave: TNotifyEvent;
property OnMouseMove: TMouseMoveEvent;
property OnMouseUp: TMouseEvent;
property OnStartDrag: TStartDragEvent;
property ParentFont: Boolean;
property ParentShowHint: Boolean;
property PopupMenu: TPopupMenu;
property ShowHint: Boolean;
property TabOrder: TTabOrder;
property TabStop: Boolean;
property Visible: Boolean;

## TInstrumentScrollBar
继承：TInstrumentScrollBar → TCustomInstrumentScrollBar → TCustomXPScrollBar → TXPCustomControl → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：InstrumentScrolls

property Align: TAlign;
property Anchors: TAnchors;
property Color: TColor;
property Constraints: TSizeConstraints;
property CustomHint: TCustomHint;
property DoubleBuffered: Boolean;
property DragCursor: TCursor;
property DragKind: TDragKind;
property DragMode: TDragMode;
property Enabled: Boolean;
property Kind: TScrollBarKind;
property LargeChange: TScrollBarInc;
property Max: Integer;
property Min: Integer;
property OnChange: TNotifyEvent;
property OnContextPopup: TContextPopupEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnEndDock: TEndDragEvent;
property OnEndDrag: TEndDragEvent;
property OnEnter: TNotifyEvent;
property OnExit: TNotifyEvent;
property OnKeyDown: TKeyEvent;
property OnKeyPress: TKeyPressEvent;
property OnKeyUp: TKeyEvent;
property OnMouseEnter: TNotifyEvent;
property OnMouseLeave: TNotifyEvent;
property OnScroll: TScrollEvent;
property OnStartDock: TStartDockEvent;
property OnStartDrag: TStartDragEvent;
property PageSize: Integer;
property ParentShowHint: Boolean;
property PopupMenu: TPopupMenu;
property Position: Integer;
property ShowHint: Boolean;
property SmallChange: TScrollBarInc;
property TabOrder: TTabOrder;
property TabStop: Boolean;
property Visible: Boolean;

## TInstrumentShape
继承：TInstrumentShape → TCustomInstrumentShape → TShape → TGraphicControl → TControl → TComponent → TPersistent → TObject ｜ 单元：InstrumentExtControls

property Radius: Integer;

## TInstrumentSilkScreen
继承：TInstrumentSilkScreen → TCustomInstrumentSilkScreen → TXPCustomControl → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：InstrumentPanels

property Align: TAlign;
property Anchors: TAnchors;
property AutoSize: Boolean;
property Constraints: TSizeConstraints;
property CustomHint: TCustomHint;
property DockSite: Boolean;
property DoubleBuffered: Boolean;
property DragCursor: TCursor;
property DragKind: TDragKind;
property DragMode: TDragMode;
property Enabled: Boolean;
property Font: TFont;
property OnCanResize: TCanResizeEvent;
property OnClick: TNotifyEvent;
property OnConstrainedResize: TConstrainedResizeEvent;
property OnContextPopup: TContextPopupEvent;
property OnDblClick: TNotifyEvent;
property OnDockDrop: TDockDropEvent;
property OnDockOver: TDockOverEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnEndDock: TEndDragEvent;
property OnEndDrag: TEndDragEvent;
property OnEnter: TNotifyEvent;
property OnExit: TNotifyEvent;
property OnGetSiteInfo: TGetSiteInfoEvent;
property OnMouseDown: TMouseEvent;
property OnMouseMove: TMouseMoveEvent;
property OnMouseUp: TMouseEvent;
property OnResize: TNotifyEvent;
property OnStartDock: TStartDockEvent;
property OnStartDrag: TStartDragEvent;
property OnUnDock: TUnDockEvent;
property ParentFont: Boolean;
property ParentShowHint: Boolean;
property PopupMenu: TPopupMenu;
property ShowHint: Boolean;
property TabStop: Boolean;
property UseDockManager: Boolean;
property Visible: Boolean;

## TInstrumentTerminal
继承：TInstrumentTerminal → TCustomInstrumentTerminal → TCustomInstrumentPanel → TXPCustomControl → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：InstrumentComms

property Align: TAlign;
property Anchors: TAnchors;
property AutoSize: Boolean;
property CaretStyle: TCaretStyle;
property Constraints: TSizeConstraints;
property CustomHint: TCustomHint;
property DisplayStyle: TDisplayStyle;
property DockSite: Boolean;
property DoubleBuffered: Boolean;
property DragCursor: TCursor;
property DragKind: TDragKind;
property DragMode: TDragMode;
property Enabled: Boolean;
property Font: TFont;
property OnCanResize: TCanResizeEvent;
property OnClick: TNotifyEvent;
property OnConstrainedResize: TConstrainedResizeEvent;
property OnContextPopup: TContextPopupEvent;
property OnDblClick: TNotifyEvent;
property OnDockDrop: TDockDropEvent;
property OnDockOver: TDockOverEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnEndDock: TEndDragEvent;
property OnEndDrag: TEndDragEvent;
property OnEnter: TNotifyEvent;
property OnExit: TNotifyEvent;
property OnGetSiteInfo: TGetSiteInfoEvent;
property OnMouseDown: TMouseEvent;
property OnMouseMove: TMouseMoveEvent;
property OnMouseUp: TMouseEvent;
property OnResize: TNotifyEvent;
property OnStartDock: TStartDockEvent;
property OnStartDrag: TStartDragEvent;
property OnTransmitChar: TTransmitCharEvent;
property OnUnDock: TUnDockEvent;
property Options: TTerminalOptions;
property Padding: TPadding;
property ParentFont: Boolean;
property ParentShowHint: Boolean;
property PopupMenu: TPopupMenu;
property RxColor: TColor;
property ShowHint: Boolean;
property SmoothDraw: Boolean;
property TabOrder: TTabOrder;
property TabStop: Boolean;
property TxColor: TColor;
property UseDockManager: Boolean;
property Visible: Boolean;

## TInstrumentTicks
继承：TInstrumentTicks → TPersistent → TObject ｜ 单元：InstrumentClasses

property Color: TColor;
property Length: Integer;
property Visible: Boolean;
property Width: Integer;
procedure Create(AOwner: TControl);

## TInstrumentTicksFloat
继承：TInstrumentTicksFloat → TInstrumentTicks → TPersistent → TObject ｜ 单元：InstrumentClasses

property Step: Double;

## TInstrumentTicksInt
继承：TInstrumentTicksInt → TInstrumentTicks → TPersistent → TObject ｜ 单元：InstrumentClasses

property Step: Int64;

## TInstrumentTrackBar
继承：TInstrumentTrackBar → TCustomInstrumentTrackBar → TCustomInstrumentSlider → TXPCustomControl → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：InstrumentSliders

property Align: TAlign;
property Anchors: TAnchors;
property AutoSize: Boolean;
property Color: TColor;
property Constraints: TSizeConstraints;
property CustomHint: TCustomHint;
property Discrete: Boolean;
property DoubleBuffered: Boolean;
property DragCursor: TCursor;
property DragKind: TDragKind;
property DragMode: TDragMode;
property Enabled: Boolean;
property Font: TFont;
property HandleSize: TInstrumentSize;
property Horizontal: Boolean;
property Increment: Double;
property LargeTicks: TInstrumentTicksFloat;
property MaxValue: Double;
property MediumTicks: TInstrumentTicksFloat;
property MinValue: Double;
property Numbers: TInstrumentNumbers;
property OnChange: TNotifyEvent;
property OnClick: TNotifyEvent;
property OnDblClick: TNotifyEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnEndDrag: TEndDragEvent;
property OnGetHintText: TGetTextFloatEvent;
property OnGetScaleLabel: TGetTextFloatExEvent;
property OnMouseDown: TMouseEvent;
property OnMouseMove: TMouseMoveEvent;
property OnMouseUp: TMouseEvent;
property OnStartDrag: TStartDragEvent;
property ParentColor: Boolean;
property ParentFont: Boolean;
property ParentShowHint: Boolean;
property PopupMenu: TPopupMenu;
property ScaleVisible: Boolean;
property ShowHint: Boolean;
property ShowToolTip: TPositionToolTip;
property SmallTicks: TInstrumentTicksFloat;
property Value: Double;
property ValueIncrement: Double;
property Visible: Boolean;

## TIntegerBucketList
继承：TIntegerBucketList → TBucketList → TCustomBucketList → TObject ｜ 单元：System.Contnrs

property Data[Index: ?]: NativeInt;
function Add(AItem: NativeInt; AData: NativeInt): NativeInt;
function Remove(AItem: NativeInt): NativeInt;

## TIntegerField
继承：TIntegerField → TNumericField → TField → TComponent → TPersistent → TObject ｜ 单元：Data.DB

property MaxValue: Integer;
property MinValue: Integer;
property Value: Longint;
function GetValue(var Value: Integer): Boolean;

## TInterfacedObject
继承：TInterfacedObject → TObject ｜ 单元：System

property RefCount: Integer;  // read-only

## TInterfacedObjectNoRef
继承：TInterfacedObjectNoRef → TInterfacedObject → TObject ｜ 单元：RT_ClientServerInterface


## TInterfacedPersistent
继承：TInterfacedPersistent → TPersistent → TObject ｜ 单元：System.Classes


## TInterfaceField
继承：TInterfaceField → TField → TComponent → TPersistent → TObject ｜ 单元：Data.DB

property Value: IUnknown;

## TInterfaceList
继承：TInterfaceList → TInterfacedObject → TObject ｜ 单元：System.Classes

property Capacity: Integer;
property Count: Integer;
property Items[Index: ?]: IInterface;
function Add(const Item: IInterface): Integer;
procedure Clear;
procedure Create;
procedure Delete(Index: Integer);
procedure Exchange(Index1: Integer; Index2: Integer);
function Expand: TInterfaceList;
function First: IInterface;
function GetEnumerator: TInterfaceListEnumerator;
function IndexOf(const Item: IInterface): Integer;
function IndexOfItem(const Item: IInterface; Direction: TDirection): Integer;
procedure Insert(Index: Integer; const Item: IInterface);
function Last: IInterface;
procedure Lock;
function Remove(const Item: IInterface): Integer;
function RemoveItem(const Item: IInterface; Direction: TDirection): Integer;
procedure Unlock;

## TInterfaceListEnumerator
继承：TInterfaceListEnumerator → TObject ｜ 单元：System.Classes

property Current: IInterface;  // read-only
procedure Create(AInterfaceList: TInterfaceList);
function GetCurrent: IInterface;
function MoveNext: Boolean;

## TInvokeableVariantType
继承：TInvokeableVariantType → TCustomVariantType → TObject ｜ 单元：System.Variants

function DoFunction(const Dest: IDispatch; const V: IDispatch; const Name: string; const Arguments: TVarDataArray): Boolean;
function DoProcedure(const V: IDispatch; const Name: string; const Arguments: TVarDataArray): Boolean;
function FixupIdent(const AText: string): string;
function GetProperty(const Dest: IDispatch; const V: IDispatch; const Name: string): Boolean;
function SetProperty(const V: IDispatch; const Name: string; const Value: IDispatch): Boolean;

## TIOSignalLink
继承：TIOSignalLink → TComponent → TPersistent → TObject ｜ 单元：RT_Digital_IO

property CompoundSignalName: string;
property Manager: TSignalLinkManager;
property Value: TSignalValueType;
function Clone(const ACompoundSignalName: string): TIOSignalLink;
procedure DoChange(var AValue: Cardinal);
procedure DoUserChange(AnObject: TObject);
function GetMaxValue: Cardinal;
function GetMinValue: Cardinal;
function IsInput: Boolean;
procedure SetValue(AValue: Cardinal);

## TLabel
继承：TLabel → TCustomLabel → TGraphicControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.StdCtrls

property Align: TAlign;
property Alignment: TAlignment;
property Anchors: TAnchors;
property AutoSize: Boolean;
property BiDiMode: TBiDiMode;
property Caption: TCaption;
property Color: TColor;
property Constraints: TSizeConstraints;
property DragCursor: TCursor;
property DragKind: TDragKind;
property DragMode: TDragMode;
property EllipsisPosition: TEllipsisPosition;
property Enabled: Boolean;
property FocusControl: TWinControl;
property Font: TFont;
property GlowSize: Integer;
property Layout: TTextLayout;
property OnClick: TNotifyEvent;
property OnContextPopup: TContextPopupEvent;
property OnDblClick: TNotifyEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnEndDock: TEndDragEvent;
property OnEndDrag: TEndDragEvent;
property OnGesture: TGestureEvent;
property OnMouseActivate: TMouseActivateEvent;
property OnMouseDown: TMouseEvent;
property OnMouseEnter: TNotifyEvent;
property OnMouseLeave: TNotifyEvent;
property OnMouseMove: TMouseMoveEvent;
property OnMouseUp: TMouseEvent;
property OnStartDock: TStartDockEvent;
property OnStartDrag: TStartDragEvent;
property ParentBiDiMode: Boolean;
property ParentColor: Boolean;
property ParentFont: Boolean;
property ParentShowHint: Boolean;
property PopupMenu: TPopupMenu;
property ShowAccelChar: Boolean;
property ShowHint: Boolean;
property StyleElements: TStyleElements;
property Touch: TTouchManager;
property Transparent: Boolean;
property Visible: Boolean;
property WordWrap: Boolean;

## TLabeledEdit
继承：TLabeledEdit → TCustomLabeledEdit → TCustomEdit → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.ExtCtrls

property Alignment: TAlignment;
property Anchors: TAnchors;
property AutoSelect: Boolean;
property AutoSize: Boolean;
property BevelEdges: TBevelEdges;
property BevelInner: TBevelCut;
property BevelKind: TBevelKind;
property BevelOuter: TBevelCut;
property BiDiMode: TBiDiMode;
property BorderStyle: TBorderStyle;
property CharCase: TEditCharCase;
property Color: TColor;
property Constraints: TSizeConstraints;
property Ctl3D: Boolean;
property DoubleBuffered: Boolean;
property DragCursor: TCursor;
property DragKind: TDragKind;
property DragMode: TDragMode;
property EditLabel: TBoundLabel;  // read-only
property Enabled: Boolean;
property Font: TFont;
property HideSelection: Boolean;
property ImeMode: TImeMode;
property ImeName: TImeName;
property LabelPosition: TLabelPosition;
property LabelSpacing: Integer;
property MaxLength: Integer;
property NumbersOnly: Boolean;
property OEMConvert: Boolean;
property OnChange: TNotifyEvent;
property OnClick: TNotifyEvent;
property OnContextPopup: TContextPopupEvent;
property OnDblClick: TNotifyEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnEndDock: TEndDragEvent;
property OnEndDrag: TEndDragEvent;
property OnEnter: TNotifyEvent;
property OnExit: TNotifyEvent;
property OnGesture: TGestureEvent;
property OnKeyDown: TKeyEvent;
property OnKeyPress: TKeyPressEvent;
property OnKeyUp: TKeyEvent;
property OnMouseActivate: TMouseActivateEvent;
property OnMouseDown: TMouseEvent;
property OnMouseEnter: TNotifyEvent;
property OnMouseLeave: TNotifyEvent;
property OnMouseMove: TMouseMoveEvent;
property OnMouseUp: TMouseEvent;
property OnStartDock: TStartDockEvent;
property OnStartDrag: TStartDragEvent;
property ParentBiDiMode: Boolean;
property ParentColor: Boolean;
property ParentCtl3D: Boolean;
property ParentDoubleBuffered: Boolean;
property ParentFont: Boolean;
property ParentShowHint: Boolean;
property PasswordChar: Char;
property PopupMenu: TPopupMenu;
property ReadOnly: Boolean;
property ShowHint: Boolean;
property StyleElements: TStyleElements;
property TabOrder: TTabOrder;
property TabStop: Boolean;
property Text: TCaption;
property TextHint: string;
property Touch: TTouchManager;
property Visible: Boolean;

## TLanguages
继承：TLanguages → TObject ｜ 单元：System.SysUtils ｜ 未在类列表里注册，只能通过实例访问

property Count: Integer;  // read-only
property Ext[Index: ?]: String;  // read-only
property ID[Index: ?]: String;  // read-only
property LocaleID[Index: ?]: TLocaleID;  // read-only
property LocaleIDFromName[Index: ?]: TLocaleID;  // read-only
property LocaleName[Index: ?]: String;  // read-only
property Name[Index: ?]: String;  // read-only
property NameFromLCID[Index: ?]: String;  // read-only
property NameFromLocaleID[Index: ?]: String;  // read-only
property UserDefaultLocale: TLocaleID;  // read-only
procedure Create;
function GetLocaleIDFromLocaleName(const LocaleName: string): Cardinal;
function IndexOf(ID: Cardinal): Integer;

## TLargeintField
继承：TLargeintField → TNumericField → TField → TComponent → TPersistent → TObject ｜ 单元：Data.DB

property MaxValue: Int64;
property MinValue: Int64;
property Value: Largeint;

## TLEDDigitsMetrics
继承：TLEDDigitsMetrics → TDigitsPanelMetrics → TPersistent → TObject ｜ 单元：InstrumentDigitPanels

property EndSpace: Integer;
property Gap: Integer;
property Height: NaturalNumber;
property Space: Integer;
property StartSpace: Integer;
property Thickness: NaturalNumber;
property Width: NaturalNumber;  // read-only

## TLibraryReportInfo
继承：TLibraryReportInfo → TDispatchObject → TDispatchObject ｜ 单元：RT_IntegratedLibrary

procedure Create(const AFileName: string);
function GetComponentCount: Integer;
function GetComponentList: WideString;
function GetLibraryIterator: ILibObjectIterator;
function GetParameterCount: Integer;
function GetParameterName(AIndex: Integer): WideString;
function GetParameterValue(AIndex: Integer): WideString;
function GetTitle: WideString;

## TLinkLabel
继承：TLinkLabel → TCustomLinkLabel → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.ExtCtrls

property Align: TAlign;
property Alignment: TCustomLinkLabel.TLinkAlignment;
property Anchors: TAnchors;
property AutoSize: Boolean;
property BevelEdges: TBevelEdges;
property BevelInner: TBevelCut;
property BevelKind: TBevelKind;
property BevelOuter: TBevelCut;
property Caption: TCaption;
property Color: TColor;
property Constraints: TSizeConstraints;
property DragCursor: TCursor;
property DragKind: TDragKind;
property DragMode: TDragMode;
property Enabled: Boolean;
property Font: TFont;
property OnClick: TNotifyEvent;
property OnContextPopup: TContextPopupEvent;
property OnDblClick: TNotifyEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnEndDock: TEndDragEvent;
property OnEndDrag: TEndDragEvent;
property OnGesture: TGestureEvent;
property OnLinkClick: TSysLinkEvent;
property OnMouseActivate: TMouseActivateEvent;
property OnMouseDown: TMouseEvent;
property OnMouseEnter: TNotifyEvent;
property OnMouseLeave: TNotifyEvent;
property OnMouseMove: TMouseMoveEvent;
property OnMouseUp: TMouseEvent;
property OnStartDock: TStartDockEvent;
property OnStartDrag: TStartDragEvent;
property ParentColor: Boolean;
property ParentFont: Boolean;
property ParentShowHint: Boolean;
property PopupMenu: TPopupMenu;
property ShowHint: Boolean;
property TabOrder: TTabOrder;
property TabStop: Boolean;
property Touch: TTouchManager;
property UseVisualStyle: Boolean;
property Visible: Boolean;

## TLinkLabelStyleHook
继承：TLinkLabelStyleHook → TStyleHook → TStyleHook ｜ 单元：Vcl.ExtCtrls


## TLinkObservers
继承：TLinkObservers → TObject ｜ 单元：System.Classes

function AllowControlChange(const AControl: TComponent): Boolean;
procedure ControlChanged(const AControl: TComponent);
procedure ControlValueModified(AObservers: TObservers);
function ControlValueTrackUpdate(const AObservers: TObservers): Boolean;
procedure ControlValueUpdate(AObservers: TObservers);
function EditGridLinkEdit(const AObservers: TObservers): Boolean;
function EditGridLinkIsEditing(const AObservers: TObservers): Boolean;
function EditGridLinkIsModified(const AObservers: TObservers): Boolean;
function EditGridLinkIsReadOnly(const AObservers: TObservers): Boolean;
function EditGridLinkIsValidChar(const AObservers: TObservers; AKey: Char): Boolean;
procedure EditGridLinkModified(const AObservers: TObservers);
procedure EditGridLinkReset(const AObservers: TObservers);
procedure EditGridLinkSetIsReadOnly(const AObservers: TObservers; AValue: Boolean);
procedure EditGridLinkUpdate(const AObservers: TObservers);
function EditLinkEdit(const AObservers: TObservers): Boolean;
function EditLinkIsEditing(const AObservers: TObservers): Boolean;
function EditLinkIsModified(const AObservers: TObservers): Boolean;
function EditLinkIsReadOnly(const AObservers: TObservers): Boolean;
function EditLinkIsValidChar(const AObservers: TObservers; AKey: Char): Boolean;
procedure EditLinkModified(AObservers: TObservers);
procedure EditLinkReset(const AObservers: TObservers);
procedure EditLinkSetIsReadOnly(const AObservers: TObservers; AValue: Boolean);
function EditLinkTrackUpdate(const AObservers: TObservers): Boolean;
procedure EditLinkUpdate(const AObservers: TObservers);
function GetEditGridLink(const AObservers: TObservers): IEditGridLinkObserver;
function GetEditLink(const AObservers: TObservers): IEditLinkObserver;
procedure ListSelectionChanged(const AObservers: TObservers);
procedure PositionLinkPosChanged(const AObservers: TObservers);
procedure PositionLinkPosChanging(const AObservers: TObservers);

## TList
继承：TList → TObject ｜ 单元：System.Classes

property Capacity: Integer;
property Count: Integer;
property Items[Index: ?]: Pointer;
function Add(Item: Pointer): Integer;
procedure Assign(ListA: TList; AOperator: TListAssignOp; ListB: TList);
procedure Clear;
procedure Delete(Index: Integer);
procedure Error(const Msg: string; Data: NativeInt);
procedure Exchange(Index1: Integer; Index2: Integer);
function Expand: TList;
function Extract(Item: Pointer): Pointer;
function ExtractItem(Item: Pointer; Direction: TDirection): Pointer;
function First: Pointer;
function GetEnumerator: TListEnumerator;
procedure Grow;
function IndexOf(Item: Pointer): Integer;
function IndexOfItem(Item: Pointer; Direction: TDirection): Integer;
procedure Insert(Index: Integer; Item: Pointer);
function Last: Pointer;
procedure Move(CurIndex: Integer; NewIndex: Integer);
procedure Notify(Ptr: Pointer; Action: TListNotification);
procedure Pack;
function Remove(Item: Pointer): Integer;
function RemoveItem(Item: Pointer; Direction: TDirection): Integer;

## TListBox
继承：TListBox → TCustomListBox → TCustomMultiSelectListControl → TCustomListControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.StdCtrls

property Align: TAlign;
property Anchors: TAnchors;
property AutoComplete: Boolean;
property AutoCompleteDelay: Cardinal;
property BevelEdges: TBevelEdges;
property BevelInner: TBevelCut;
property BevelKind: TBevelKind;
property BevelOuter: TBevelCut;
property BevelWidth: TBevelWidth;
property BiDiMode: TBiDiMode;
property BorderStyle: TBorderStyle;
property Color: TColor;
property Columns: Integer;
property Constraints: TSizeConstraints;
property Ctl3D: Boolean;
property DoubleBuffered: Boolean;
property DragCursor: TCursor;
property DragKind: TDragKind;
property DragMode: TDragMode;
property Enabled: Boolean;
property ExtendedSelect: Boolean;
property Font: TFont;
property ImeMode: TImeMode;
property ImeName: TImeName;
property IntegralHeight: Boolean;
property ItemHeight: Integer;
property Items: TStrings;
property MultiSelect: Boolean;
property OnClick: TNotifyEvent;
property OnContextPopup: TContextPopupEvent;
property OnData: TLBGetDataEvent;
property OnDataFind: TLBFindDataEvent;
property OnDataObject: TLBGetDataObjectEvent;
property OnDblClick: TNotifyEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnDrawItem: TDrawItemEvent;
property OnEndDock: TEndDragEvent;
property OnEndDrag: TEndDragEvent;
property OnEnter: TNotifyEvent;
property OnExit: TNotifyEvent;
property OnGesture: TGestureEvent;
property OnKeyDown: TKeyEvent;
property OnKeyPress: TKeyPressEvent;
property OnKeyUp: TKeyEvent;
property OnMeasureItem: TMeasureItemEvent;
property OnMouseActivate: TMouseActivateEvent;
property OnMouseDown: TMouseEvent;
property OnMouseEnter: TNotifyEvent;
property OnMouseLeave: TNotifyEvent;
property OnMouseMove: TMouseMoveEvent;
property OnMouseUp: TMouseEvent;
property OnStartDock: TStartDockEvent;
property OnStartDrag: TStartDragEvent;
property ParentBiDiMode: Boolean;
property ParentColor: Boolean;
property ParentCtl3D: Boolean;
property ParentDoubleBuffered: Boolean;
property ParentFont: Boolean;
property ParentShowHint: Boolean;
property PopupMenu: TPopupMenu;
property ScrollWidth: Integer;
property ShowHint: Boolean;
property Sorted: Boolean;
property Style: TListBoxStyle;
property StyleElements: TStyleElements;
property TabOrder: TTabOrder;
property TabStop: Boolean;
property TabWidth: Integer;
property Touch: TTouchManager;
property Visible: Boolean;

## TListBoxStyleHook
继承：TListBoxStyleHook → TScrollingStyleHook → TMouseTrackControlStyleHook ｜ 单元：Vcl.StdCtrls


## TListColumn
继承：TListColumn → TCollectionItem → TPersistent → TObject ｜ 单元：Vcl.ComCtrls

property Alignment: TAlignment;
property AutoSize: Boolean;
property Caption: string;
property ImageIndex: TImageIndex;
property MaxWidth: TWidth;
property MinWidth: TWidth;
property Tag: Integer;
property Width: TWidth;
property WidthType: TWidth;  // read-only

## TListColumns
继承：TListColumns → TCollection → TPersistent → TObject ｜ 单元：Vcl.ComCtrls

property Items[Index: ?]: TListColumn;
function Add: TListColumn;
procedure Create(AOwner: TCustomListView);
function Owner: TCustomListView;

## TListEnumerator
继承：TListEnumerator → TObject ｜ 单元：System.Classes

property Current: Pointer;  // read-only
procedure Create(AList: TList);
function GetCurrent: Pointer;
function MoveNext: Boolean;

## TListGroup
继承：TListGroup → TCollectionItem → TPersistent → TObject ｜ 单元：Vcl.ComCtrls

property Footer: string;
property FooterAlign: TAlignment;
property GroupID: Integer;
property Header: string;
property HeaderAlign: TAlignment;
property State: TListGroupStateSet;
property Subtitle: string;
property TitleImage: TImageIndex;

## TListGroups
继承：TListGroups → TCollection → TPersistent → TObject ｜ 单元：Vcl.ComCtrls

property Items[Index: ?]: TListGroup;
property NextGroupID: Integer;  // read-only
function Add: TListGroup;
procedure Create(AOwner: TCustomListView);
function Owner: TCustomListView;

## TListItem
继承：TListItem → TPersistent → TObject ｜ 单元：Vcl.ComCtrls

property Caption: String;
property Checked: Boolean;
property Cut: Boolean;
property Data: TCustomData;
property Deleting: Boolean;  // read-only
property DropTarget: Boolean;
property Focused: Boolean;
property GroupID: Integer;
property Handle: HWND;  // read-only
property ImageIndex: TImageIndex;
property Indent: Integer;
property Index: Integer;  // read-only
property Left: Integer;
property ListView: TCustomListView;  // read-only
property OverlayIndex: TImageIndex;
property Owner: TListItems;  // read-only
property Position: TPoint;
property Selected: Boolean;
property StateIndex: TImageIndex;
property SubItemImages[Index: ?]: Integer;
property SubItems: TStrings;
property Top: Integer;
procedure CancelEdit;
procedure Create(AOwner: TListItems);
procedure Delete;
function DisplayRect(Code: TDisplayCode): IDispatch;
function EditCaption: Boolean;
function GetPosition: IDispatch;
procedure MakeVisible(PartialOK: Boolean);
procedure SetPosition(const Value: IDispatch);
procedure Update;
function WorkArea: Integer;

## TListItems
继承：TListItems → TPersistent → TObject ｜ 单元：Vcl.ComCtrls

property Count: Integer;
property Handle: HWND;  // read-only
property Item[Index: ?]: TListItem;
property Owner: TCustomListView;  // read-only
function Add: TListItem;
function AddItem(Item: TListItem; Index: Integer): TListItem;
procedure BeginUpdate;
procedure Clear;
procedure Create(AOwner: TCustomListView);
procedure Delete(Index: Integer);
procedure EndUpdate;
function GetEnumerator: TListItemsEnumerator;
function IndexOf(Value: TListItem): Integer;
function Insert(Index: Integer): TListItem;

## TListItemsEnumerator
继承：TListItemsEnumerator → TObject ｜ 单元：Vcl.ComCtrls

property Current: TListItem;  // read-only
procedure Create(AListItems: TListItems);
function GetCurrent: TListItem;
function MoveNext: Boolean;

## TListSourceLink
继承：TListSourceLink → TDataLink → TPersistent → TObject ｜ 单元：Vcl.DBCtrls

procedure Create;

## TListView
继承：TListView → TCustomListView → TCustomMultiSelectListControl → TCustomListControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.ComCtrls

property Action: TBasicAction;
property Align: TAlign;
property AllocBy: Integer;
property Anchors: TAnchors;
property BevelEdges: TBevelEdges;
property BevelInner: TBevelCut;
property BevelKind: TBevelKind;
property BevelOuter: TBevelCut;
property BevelWidth: TBevelWidth;
property BiDiMode: TBiDiMode;
property BorderStyle: TBorderStyle;
property BorderWidth: TBorderWidth;
property Checkboxes: Boolean;
property Color: TColor;
property ColumnClick: Boolean;
property Columns: TListColumns;
property Constraints: TSizeConstraints;
property Ctl3D: Boolean;
property DoubleBuffered: Boolean;
property DragCursor: TCursor;
property DragKind: TDragKind;
property DragMode: TDragMode;
property Enabled: Boolean;
property FlatScrollBars: Boolean;
property Font: TFont;
property FullDrag: Boolean;
property GridLines: Boolean;
property GroupHeaderImages: TCustomImageList;
property Groups: TListGroups;
property GroupView: Boolean;
property HideSelection: Boolean;
property HotTrack: Boolean;
property HotTrackStyles: TListHotTrackStyles;
property HoverTime: Integer;
property IconOptions: TIconOptions;
property Items: TListItems;
property LargeImages: TCustomImageList;
property MultiSelect: Boolean;
property OnAdvancedCustomDraw: TLVAdvancedCustomDrawEvent;
property OnAdvancedCustomDrawItem: TLVAdvancedCustomDrawItemEvent;
property OnAdvancedCustomDrawSubItem: TLVAdvancedCustomDrawSubItemEvent;
property OnChange: TLVChangeEvent;
property OnChanging: TLVChangingEvent;
property OnClick: TNotifyEvent;
property OnColumnClick: TLVColumnClickEvent;
property OnColumnDragged: TNotifyEvent;
property OnColumnRightClick: TLVColumnRClickEvent;
property OnCompare: TLVCompareEvent;
property OnContextPopup: TContextPopupEvent;
property OnCreateItemClass: TLVCreateItemClassEvent;
property OnCustomDraw: TLVCustomDrawEvent;
property OnCustomDrawItem: TLVCustomDrawItemEvent;
property OnCustomDrawSubItem: TLVCustomDrawSubItemEvent;
property OnData: TLVOwnerDataEvent;
property OnDataFind: TLVOwnerDataFindEvent;
property OnDataHint: TLVOwnerDataHintEvent;
property OnDataStateChange: TLVOwnerDataStateChangeEvent;
property OnDblClick: TNotifyEvent;
property OnDeletion: TLVDeletedEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnDrawItem: TLVDrawItemEvent;
property OnEdited: TLVEditedEvent;
property OnEditing: TLVEditingEvent;
property OnEndDock: TEndDragEvent;
property OnEndDrag: TEndDragEvent;
property OnEnter: TNotifyEvent;
property OnExit: TNotifyEvent;
property OnGesture: TGestureEvent;
property OnGetImageIndex: TLVNotifyEvent;
property OnGetSubItemImage: TLVSubItemImageEvent;
property OnInfoTip: TLVInfoTipEvent;
property OnInsert: TLVDeletedEvent;
property OnItemChecked: TLVCheckedItemEvent;
property OnKeyDown: TKeyEvent;
property OnKeyPress: TKeyPressEvent;
property OnKeyUp: TKeyEvent;
property OnMouseActivate: TMouseActivateEvent;
property OnMouseDown: TMouseEvent;
property OnMouseEnter: TNotifyEvent;
property OnMouseLeave: TNotifyEvent;
property OnMouseMove: TMouseMoveEvent;
property OnMouseUp: TMouseEvent;
property OnResize: TNotifyEvent;
property OnSelectItem: TLVSelectItemEvent;
property OnStartDock: TStartDockEvent;
property OnStartDrag: TStartDragEvent;
property OwnerData: Boolean;
property OwnerDraw: Boolean;
property ParentBiDiMode: Boolean;
property ParentColor: Boolean;
property ParentDoubleBuffered: Boolean;
property ParentFont: Boolean;
property ParentShowHint: Boolean;
property PopupMenu: TPopupMenu;
property ReadOnly: Boolean;
property RowSelect: Boolean;
property ShowColumnHeaders: Boolean;
property ShowHint: Boolean;
property ShowWorkAreas: Boolean;
property SmallImages: TCustomImageList;
property SortType: TSortType;
property StateImages: TCustomImageList;
property StyleElements: TStyleElements;
property TabOrder: TTabOrder;
property TabStop: Boolean;
property Touch: TTouchManager;
property ViewStyle: TViewStyle;
property Visible: Boolean;

## TListViewActionLink
继承：TListViewActionLink → TListActionLink → TListActionLink ｜ 单元：Vcl.ComCtrls


## TListViewStyleHook
继承：TListViewStyleHook → TScrollingStyleHook → TMouseTrackControlStyleHook ｜ 单元：Vcl.ComCtrls


## TLocatedHyperlink
继承：TLocatedHyperlink → TInterfacedObject → TObject ｜ 单元：Rt_AbstractOutput

procedure Create(const AHyperlink: IHyperlink; const ARegion: IRectangleD);

## TLocatedHyperlinkList
继承：TLocatedHyperlinkList → TInterfacedObject → TObject ｜ 单元：Rt_AbstractOutput

procedure Create(const AHyperlinks: array of ILocatedHyperlink);

## TLoginCredentialService
继承：TLoginCredentialService → TObject ｜ 单元：System.Classes


## TLongWordField
继承：TLongWordField → TNumericField → TField → TComponent → TPersistent → TObject ｜ 单元：Data.DB

property MaxValue: Cardinal;
property MinValue: Cardinal;
property Value: LongWord;
function GetValue(var Value: Cardinal): Boolean;

## TLookupList
继承：TLookupList → TObject ｜ 单元：Data.DB

procedure Add(const AKey: Variant; const AValue: Variant);
procedure Clear;
procedure Create;
function ValueOfKey(const AKey: Variant): Variant;

## TMainMenu
继承：TMainMenu → TMenu → TComponent → TPersistent → TObject ｜ 单元：Vcl.Menus

property AutoHotkeys: TMenuAutoFlag;
property AutoLineReduction: TMenuAutoFlag;
property AutoMerge: Boolean;
property BiDiMode: TBiDiMode;
property Images: TCustomImageList;
property OnChange: TMenuChangeEvent;
property OwnerDraw: Boolean;
property ParentBiDiMode: Boolean;
procedure GetOle2AcceleratorTable(var AccelTable: HACCEL; var AccelCount: Integer; const Groups: array of Integer);
procedure Merge(Menu: TMainMenu);
procedure PopulateOle2Menu(SharedMenu: HMENU; const Groups: array of Integer; var Widths: array of Integer);
procedure SetOle2MenuHandle(Handle: HMENU);
procedure Unmerge(Menu: TMainMenu);

## TMargins
继承：TMargins → TPersistent → TObject ｜ 单元：Vcl.Controls

property Bottom: TMarginSize;
property ControlHeight: Integer;  // read-only
property ControlLeft: Integer;  // read-only
property ControlTop: Integer;  // read-only
property ControlWidth: Integer;  // read-only
property ExplicitHeight: Integer;  // read-only
property ExplicitLeft: Integer;  // read-only
property ExplicitTop: Integer;  // read-only
property ExplicitWidth: Integer;  // read-only
property Left: TMarginSize;
property Right: TMarginSize;
property Top: TMarginSize;
procedure Change;
procedure Create(Control: TControl);
function GetControlBound(Index: Integer): Integer;
procedure InitDefaults(Margins: TMargins);
procedure SetBounds(ALeft: Integer; ATop: Integer; ARight: Integer; ABottom: Integer);
procedure SetControlBounds(ALeft: Integer; ATop: Integer; AWidth: Integer; AHeight: Integer; Aligning: Boolean);

## TMarshal
继承：TMarshal → TObject ｜ 单元：System

function AllocMem(Size: NativeInt): IDispatch;
function AllocStringAsAnsi(const Str: string): IDispatch;
function AllocStringAsUnicode(const Str: string): IDispatch;
function AllocStringAsUtf8(const Str: string): IDispatch;
function AsAnsi(const S: string): AnsiString;
procedure Copy(Src: TArray<System.Byte>; StartIndex: Integer; const Dest: IDispatch; Count: Integer);
procedure Create;
function FixString(var Str: string): IDispatch;
procedure FreeMem(const Ptr: IDispatch);
function InOutString(const S: string): PWideChar;
function InString(const S: string): PWideChar;
procedure Move(const Src: IDispatch; const Dest: IDispatch; Count: NativeInt);
function OutString(const S: string): PWideChar;
function ReadByte(const Ptr: IDispatch; Ofs: NativeInt): Byte;
function ReadInt16(const Ptr: IDispatch; Ofs: NativeInt): SmallInt;
function ReadInt32(const Ptr: IDispatch; Ofs: NativeInt): Integer;
function ReadInt64(const Ptr: IDispatch; Ofs: NativeInt): Int64;
function ReadPtr(const Ptr: IDispatch; Ofs: NativeInt): IDispatch;
function ReadStringAsAnsi(const Ptr: IDispatch; Len: Integer): string;
function ReadStringAsAnsiUpTo(CodePage: Word; const Ptr: IDispatch; MaxLen: Integer): string;
function ReadStringAsUnicode(const Ptr: IDispatch; Len: Integer): string;
function ReadStringAsUnicodeUpTo(const Ptr: IDispatch; MaxLen: Integer): string;
function ReadStringAsUtf8(const Ptr: IDispatch; Len: Integer): string;
function ReadStringAsUtf8UpTo(const Ptr: IDispatch; MaxLen: Integer): string;
function ReallocMem(const OldPtr: IDispatch; NewSize: NativeInt): IDispatch;
procedure UnfixString(const Ptr: IDispatch);
function UnsafeAddrOf(var Value): IDispatch;
function UnsafeFixString(const Str: string): IDispatch;
procedure WriteByte(const Ptr: IDispatch; Ofs: NativeInt; Value: Byte);
procedure WriteInt16(const Ptr: IDispatch; Ofs: NativeInt; Value: SmallInt);
procedure WriteInt32(const Ptr: IDispatch; Ofs: NativeInt; Value: Integer);
procedure WriteInt64(const Ptr: IDispatch; Ofs: NativeInt; Value: Int64);
procedure WritePtr(const Ptr: IDispatch; Ofs: NativeInt; const Value: IDispatch);
procedure WriteStringAsAnsi(const Ptr: IDispatch; const Value: string; MaxCharsIncNull: Integer);
procedure WriteStringAsUnicode(const Ptr: IDispatch; const Value: string; MaxCharsIncNull: Integer);
procedure WriteStringAsUtf8(const Ptr: IDispatch; const Value: string; MaxCharsIncNull: Integer);

## TMaskEdit
继承：TMaskEdit → TCustomMaskEdit → TCustomEdit → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.Mask

property Align: TAlign;
property Alignment: TAlignment;
property Anchors: TAnchors;
property AutoSelect: Boolean;
property AutoSize: Boolean;
property BevelEdges: TBevelEdges;
property BevelInner: TBevelCut;
property BevelKind: TBevelKind;
property BevelOuter: TBevelCut;
property BevelWidth: TBevelWidth;
property BiDiMode: TBiDiMode;
property BorderStyle: TBorderStyle;
property CharCase: TEditCharCase;
property Color: TColor;
property Constraints: TSizeConstraints;
property Ctl3D: Boolean;
property DoubleBuffered: Boolean;
property DragCursor: TCursor;
property DragKind: TDragKind;
property DragMode: TDragMode;
property EditMask: TEditMask;
property Enabled: Boolean;
property Font: TFont;
property ImeMode: TImeMode;
property ImeName: TImeName;
property MaxLength: Integer;
property OnChange: TNotifyEvent;
property OnClick: TNotifyEvent;
property OnDblClick: TNotifyEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnEndDock: TEndDragEvent;
property OnEndDrag: TEndDragEvent;
property OnEnter: TNotifyEvent;
property OnExit: TNotifyEvent;
property OnGesture: TGestureEvent;
property OnKeyDown: TKeyEvent;
property OnKeyPress: TKeyPressEvent;
property OnKeyUp: TKeyEvent;
property OnMouseActivate: TMouseActivateEvent;
property OnMouseDown: TMouseEvent;
property OnMouseEnter: TNotifyEvent;
property OnMouseLeave: TNotifyEvent;
property OnMouseMove: TMouseMoveEvent;
property OnMouseUp: TMouseEvent;
property OnStartDock: TStartDockEvent;
property OnStartDrag: TStartDragEvent;
property ParentBiDiMode: Boolean;
property ParentColor: Boolean;
property ParentCtl3D: Boolean;
property ParentDoubleBuffered: Boolean;
property ParentFont: Boolean;
property ParentShowHint: Boolean;
property PasswordChar: Char;
property PopupMenu: TPopupMenu;
property ReadOnly: Boolean;
property ShowHint: Boolean;
property StyleElements: TStyleElements;
property TabOrder: TTabOrder;
property TabStop: Boolean;
property Text: TMaskedText;
property TextHint: string;
property Touch: TTouchManager;
property Visible: Boolean;

## TMasterDataLink
继承：TMasterDataLink → TDetailDataLink → TDataLink → TPersistent → TObject ｜ 单元：Data.DB

property FieldNames: String;
procedure Create(DataSet: TDataSet);

## TMBCSEncoding
继承：TMBCSEncoding → TEncoding → TObject ｜ 单元：System.SysUtils ｜ 未在类列表里注册，只能通过实例访问

procedure Create;

## TMediaPlayer
继承：TMediaPlayer → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.MPlayer

property Align: TAlign;
property Anchors: TAnchors;
property AutoEnable: Boolean;
property AutoOpen: Boolean;
property AutoRewind: Boolean;
property Capabilities: TMPDevCapsSet;  // read-only
property ColoredButtons: TButtonSet;
property Constraints: TSizeConstraints;
property DeviceID: Word;  // read-only
property DeviceType: TMPDeviceTypes;
property Display: TWinControl;
property DisplayRect: TRect;
property DoubleBuffered: Boolean;
property Enabled: Boolean;
property EnabledButtons: TButtonSet;
property EndPos: Longint;
property Error: Longint;  // read-only
property ErrorMessage: String;  // read-only
property FileName: string;
property Frames: Longint;
property Length: Longint;  // read-only
property Mode: TMPModes;  // read-only
property Notify: Boolean;
property NotifyValue: TMPNotifyValues;  // read-only
property OnClick: EMPNotify;
property OnContextPopup: TContextPopupEvent;
property OnEnter: TNotifyEvent;
property OnExit: TNotifyEvent;
property OnMouseEnter: TNotifyEvent;
property OnMouseLeave: TNotifyEvent;
property OnNotify: TNotifyEvent;
property OnPostClick: EMPPostNotify;
property ParentDoubleBuffered: Boolean;
property ParentShowHint: Boolean;
property PopupMenu: TPopupMenu;
property Position: Longint;
property Shareable: Boolean;
property ShowHint: Boolean;
property Start: Longint;  // read-only
property StartPos: Longint;
property TabOrder: TTabOrder;
property TabStop: Boolean;
property TimeFormat: TMPTimeFormats;
property TrackLength[Index: ?]: Longint;  // read-only
property TrackPosition[Index: ?]: Longint;  // read-only
property Tracks: Longint;  // read-only
property Visible: Boolean;
property VisibleButtons: TButtonSet;
property Wait: Boolean;
procedure AutoButtonSet(Btn: TMPBtnType);
procedure Back;
procedure Click(Button: TMPBtnType; var DoDefault: Boolean);
procedure Close;
procedure DoNotify;
procedure Eject;
procedure Next;
procedure Open;
procedure Pause;
procedure PauseOnly;
procedure Play;
procedure PostClick(Button: TMPBtnType);
procedure Previous;
procedure Resume;
procedure Rewind;
procedure Save;
procedure StartRecording;
procedure Step;
procedure Stop;

## TMemIniFile
继承：TMemIniFile → TCustomIniFile → TObject ｜ 单元：System.IniFiles

property CaseSensitive: Boolean;
property Encoding: TEncoding;
procedure Clear;
procedure Create(const FileName: string);
procedure GetStrings(const List: TStrings);
procedure Rename(const FileName: string; Reload: Boolean);
procedure SetStrings(const List: TStrings);

## TMemo
继承：TMemo → TCustomMemo → TCustomEdit → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.StdCtrls

property Align: TAlign;
property Alignment: TAlignment;
property Anchors: TAnchors;
property BevelEdges: TBevelEdges;
property BevelInner: TBevelCut;
property BevelKind: TBevelKind;
property BevelOuter: TBevelCut;
property BiDiMode: TBiDiMode;
property BorderStyle: TBorderStyle;
property CharCase: TEditCharCase;
property Color: TColor;
property Constraints: TSizeConstraints;
property Ctl3D: Boolean;
property DoubleBuffered: Boolean;
property DragCursor: TCursor;
property DragKind: TDragKind;
property DragMode: TDragMode;
property Enabled: Boolean;
property Font: TFont;
property HideSelection: Boolean;
property ImeMode: TImeMode;
property ImeName: TImeName;
property Lines: TStrings;
property MaxLength: Integer;
property OEMConvert: Boolean;
property OnChange: TNotifyEvent;
property OnClick: TNotifyEvent;
property OnContextPopup: TContextPopupEvent;
property OnDblClick: TNotifyEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnEndDock: TEndDragEvent;
property OnEndDrag: TEndDragEvent;
property OnEnter: TNotifyEvent;
property OnExit: TNotifyEvent;
property OnGesture: TGestureEvent;
property OnKeyDown: TKeyEvent;
property OnKeyPress: TKeyPressEvent;
property OnKeyUp: TKeyEvent;
property OnMouseActivate: TMouseActivateEvent;
property OnMouseDown: TMouseEvent;
property OnMouseEnter: TNotifyEvent;
property OnMouseLeave: TNotifyEvent;
property OnMouseMove: TMouseMoveEvent;
property OnMouseUp: TMouseEvent;
property OnStartDock: TStartDockEvent;
property OnStartDrag: TStartDragEvent;
property ParentBiDiMode: Boolean;
property ParentColor: Boolean;
property ParentCtl3D: Boolean;
property ParentDoubleBuffered: Boolean;
property ParentFont: Boolean;
property ParentShowHint: Boolean;
property PopupMenu: TPopupMenu;
property ReadOnly: Boolean;
property ScrollBars: TScrollStyle;
property ShowHint: Boolean;
property StyleElements: TStyleElements;
property TabOrder: TTabOrder;
property TabStop: Boolean;
property Touch: TTouchManager;
property Visible: Boolean;
property WantReturns: Boolean;
property WantTabs: Boolean;
property WordWrap: Boolean;

## TMemoField
继承：TMemoField → TBlobField → TField → TComponent → TPersistent → TObject ｜ 单元：Data.DB

property Transliterate: Boolean;
property Value: AnsiString;

## TMemoryStream
继承：TMemoryStream → TCustomMemoryStream → TStream → TObject ｜ 单元：System.Classes

procedure Clear;
procedure LoadFromFile(const FileName: string);
procedure LoadFromStream(Stream: TStream);
function Realloc(var NewCapacity: Integer): Pointer;

## TMemoStyleHook
继承：TMemoStyleHook → TScrollingStyleHook → TMouseTrackControlStyleHook ｜ 单元：Vcl.StdCtrls


## TMenu
继承：TMenu → TComponent → TPersistent → TObject ｜ 单元：Vcl.Menus

property AutoHotkeys: TMenuAutoFlag;
property AutoLineReduction: TMenuAutoFlag;
property BiDiMode: TBiDiMode;
property Handle: HMENU;  // read-only
property Images: TCustomImageList;
property Items: TMenuItem;  // read-only
property OwnerDraw: Boolean;
property ParentBiDiMode: Boolean;
property WindowHandle: HWND;
function CreateMenuItem: TMenuItem;
function DispatchCommand(ACommand: Word): Boolean;
function DispatchPopup(AHandle: HMENU): Boolean;
procedure DoChange(Source: TMenuItem; Rebuild: Boolean);
function FindItem(Value: NativeUInt; Kind: TFindItemKind): TMenuItem;
function GetHandle: HMENU;
function GetHelpContext(Value: NativeUInt; ByCommand: Boolean): THelpContext;
function IsRightToLeft: Boolean;
function IsShortCut(const Message: IDispatch): Boolean;
procedure MenuChanged(Sender: TObject; Source: TMenuItem; Rebuild: Boolean);
procedure ParentBiDiModeChanged;
procedure ProcessMenuChar(const Message: IDispatch);

## TMenuActionLink
继承：TMenuActionLink → TActionLink → TContainedActionLink ｜ 单元：Vcl.Menus

function IsAutoCheckLinked: Boolean;

## TMenuItem
继承：TMenuItem → TComponent → TPersistent → TObject ｜ 单元：Vcl.Menus

property Action: TBasicAction;
property AutoCheck: Boolean;
property AutoHotkeys: TMenuItemAutoFlag;
property AutoLineReduction: TMenuItemAutoFlag;
property Bitmap: TBitmap;
property Break: TMenuBreak;
property Caption: string;
property Checked: Boolean;
property Command: Word;  // read-only
property Count: Integer;  // read-only
property Default: Boolean;
property Enabled: Boolean;
property GroupIndex: Byte;
property Handle: HMENU;  // read-only
property HelpContext: THelpContext;
property Hint: string;
property ImageIndex: TImageIndex;
property Items[Index: ?]: TMenuItem;  // read-only
property MenuIndex: Integer;
property OnAdvancedDrawItem: TAdvancedMenuDrawItemEvent;
property OnClick: TNotifyEvent;
property OnDrawItem: TMenuDrawItemEvent;
property OnMeasureItem: TMenuMeasureItemEvent;
property Parent: TMenuItem;  // read-only
property RadioItem: Boolean;
property ShortCut: TShortCut;
property SubMenuImages: TCustomImageList;
property Visible: Boolean;
procedure ActionChange(Sender: TObject; CheckDefaults: Boolean);
procedure Add(Item: TMenuItem);
procedure AdvancedDrawItem(ACanvas: TCanvas; const ARect: IDispatch; State: TOwnerDrawState; TopLevel: Boolean);
procedure Clear;
procedure Click;
procedure Delete(Index: Integer);
procedure DrawItem(ACanvas: TCanvas; const ARect: IDispatch; Selected: Boolean);
function Find(ACaption: string): TMenuItem;
function GetEnumerator: TMenuItemEnumerator;
function GetImageList: TCustomImageList;
function GetParentMenu: TMenu;
function IndexOf(Item: TMenuItem): Integer;
procedure InitiateAction;
procedure Insert(Index: Integer; Item: TMenuItem);
function InsertNewLineAfter(AItem: TMenuItem): Integer;
function InsertNewLineBefore(AItem: TMenuItem): Integer;
function IsLine: Boolean;
procedure MeasureItem(ACanvas: TCanvas; var Width: Integer; var Height: Integer);
procedure MenuChanged(Rebuild: Boolean);
function NewBottomLine: Integer;
function NewTopLine: Integer;
procedure Remove(Item: TMenuItem);
function RethinkHotkeys: Boolean;
function RethinkLines: Boolean;

## TMenuItemEnumerator
继承：TMenuItemEnumerator → TObject ｜ 单元：Vcl.Menus

property Current: TMenuItem;  // read-only
procedure Create(AMenuItem: TMenuItem);
function GetCurrent: TMenuItem;
function MoveNext: Boolean;

## TMenuItemStack
继承：TMenuItemStack → TStack → TOrderedList → TObject ｜ 单元：Vcl.Menus

procedure ClearItem(AItem: TMenuItem);

## TMenuStringBuilder
继承：TMenuStringBuilder → TObject ｜ 单元：RT_StrUtils

property MenuString: String;  // read-only
procedure AddLink(const ACaption: string; const APLID: string; const AParams: string; const AImageName: string);
procedure Create;
procedure FinishFolder;
procedure StartFolder(const ACaption: string; const AImageName: string);

## TMessagesNotification
继承：TMessagesNotification → TNotificationWithCode → TInterfacedObject → TObject ｜ 单元：RT_ClientServerInterface

procedure Create(ACode: Integer);

## TMetafile
继承：TMetafile → TGraphic → TInterfacedPersistent → TPersistent → TObject ｜ 单元：Vcl.Graphics

property CreatedBy: String;  // read-only
property Description: String;  // read-only
property Enhanced: Boolean;
property Handle: HENHMETAFILE;
property Inch: Word;
property MMHeight: Integer;
property MMWidth: Integer;
procedure Clear;
function HandleAllocated: Boolean;
function ReleaseHandle: NativeUInt;

## TMetafileCanvas
继承：TMetafileCanvas → TCanvas → TCustomCanvas → TPersistent → TObject ｜ 单元：Vcl.Graphics

procedure Create(AMetafile: TMetafile; ReferenceDevice: HDC);
procedure CreateWithComment(AMetafile: TMetafile; ReferenceDevice: HDC; const CreatedBy: string; const Description: string);

## TMetafileImage
继承：TMetafileImage → TSharedImage → TObject ｜ 单元：Vcl.Graphics


## TModelDatafile
继承：TModelDatafile → TDispatchObject → TDispatchObject ｜ 单元：RT_IntegratedLibrary

procedure Create(AFullPath: WideString);

## TModuleNotification
继承：TModuleNotification → TNotificationWithCode → TInterfacedObject → TObject ｜ 单元：RT_ClientServerInterface

procedure Create(const AModuleName: string; ACode: Integer);

## TMonitor
继承：TMonitor → TObject ｜ 单元：Vcl.Forms

property BoundsRect: TRect;  // read-only
property Handle: HMONITOR;  // read-only
property Height: Integer;  // read-only
property Left: Integer;  // read-only
property MonitorNum: Integer;  // read-only
property PixelsPerInch: Integer;  // read-only
property Primary: Boolean;  // read-only
property Top: Integer;  // read-only
property Width: Integer;  // read-only
property WorkareaRect: TRect;  // read-only

## TMonthCalColors
继承：TMonthCalColors → TPersistent → TObject ｜ 单元：Vcl.ComCtrls

property BackColor: TColor;
property MonthBackColor: TColor;
property TextColor: TColor;
property TitleBackColor: TColor;
property TitleTextColor: TColor;
property TrailingTextColor: TColor;
procedure Create(AOwner: TCommonCalendar);

## TMonthCalendar
继承：TMonthCalendar → TCommonCalendar → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.ComCtrls

property Align: TAlign;
property Anchors: TAnchors;
property AutoSize: Boolean;
property BiDiMode: TBiDiMode;
property BorderWidth: TBorderWidth;
property CalColors: TMonthCalColors;
property Constraints: TSizeConstraints;
property Date: TDate;
property DoubleBuffered: Boolean;
property DragCursor: TCursor;
property DragKind: TDragKind;
property DragMode: TDragMode;
property Enabled: Boolean;
property EndDate: TDate;
property FirstDayOfWeek: TCalDayOfWeek;
property Font: TFont;
property ImeMode: TImeMode;
property ImeName: TImeName;
property MaxDate: TDate;
property MaxSelectRange: Integer;
property MinDate: TDate;
property MultiSelect: Boolean;
property OnClick: TNotifyEvent;
property OnContextPopup: TContextPopupEvent;
property OnDblClick: TNotifyEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnEndDock: TEndDragEvent;
property OnEndDrag: TEndDragEvent;
property OnEnter: TNotifyEvent;
property OnExit: TNotifyEvent;
property OnGesture: TGestureEvent;
property OnGetMonthBoldInfo: TOnGetMonthBoldInfoEvent;
property OnGetMonthInfo: TOnGetMonthInfoEvent;
property OnKeyDown: TKeyEvent;
property OnKeyPress: TKeyPressEvent;
property OnKeyUp: TKeyEvent;
property OnMouseEnter: TNotifyEvent;
property OnMouseLeave: TNotifyEvent;
property OnStartDock: TStartDockEvent;
property OnStartDrag: TStartDragEvent;
property ParentBiDiMode: Boolean;
property ParentDoubleBuffered: Boolean;
property ParentFont: Boolean;
property ParentShowHint: Boolean;
property PopupMenu: TPopupMenu;
property ShowHint: Boolean;
property ShowToday: Boolean;
property ShowTodayCircle: Boolean;
property TabOrder: TTabOrder;
property TabStop: Boolean;
property Touch: TTouchManager;
property Visible: Boolean;
property WeekNumbers: Boolean;

## TMouse
继承：TMouse → TObject ｜ 单元：Vcl.Controls

property Capture: HWND;
property CursorPos: TPoint;
property DragImmediate: Boolean;
property DragThreshold: Integer;
property IsDragging: Boolean;  // read-only
property IsPanning: Boolean;  // read-only
property MousePresent: Boolean;  // read-only
property PanningWindow: TCustomPanningWindow;
property RegWheelMessage: UINT;  // read-only
property WheelPresent: Boolean;  // read-only
property WheelScrollLines: Integer;  // read-only
procedure Create;
function CreatePanningWindow: TCustomPanningWindow;
procedure SettingChanged(Setting: Integer);

## TMultiReadExclusiveWriteSynchronizer
继承：TMultiReadExclusiveWriteSynchronizer → TInterfacedObject → TObject ｜ 单元：System.SysUtils ｜ 未在类列表里注册，只能通过实例访问

property RevisionLevel: Cardinal;  // read-only
procedure BeginRead;
function BeginWrite: Boolean;
procedure Create;
procedure EndRead;
procedure EndWrite;

## TMultiWaitEvent
继承：TMultiWaitEvent → TObject ｜ 单元：System.Types


## TNamedItem
继承：TNamedItem → TCollectionItem → TPersistent → TObject ｜ 单元：Data.DB

property Name: string;

## TNavButton
继承：TNavButton → TSpeedButton → TGraphicControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.Buttons

property Index: TNavigateBtn;
property NavStyle: TNavButtonStyle;
property ThemeDisabled: TThemedDataNavButtons;
property ThemeHot: TThemedDataNavButtons;
property ThemeNormal: TThemedDataNavButtons;
property ThemePressed: TThemedDataNavButtons;

## TNavDataLink
继承：TNavDataLink → TDataLink → TPersistent → TObject ｜ 单元：Vcl.DBCtrls

procedure Create(ANav: TDBNavigator);

## TNexusNotification
继承：TNexusNotification → TNotificationWithCode → TInterfacedObject → TObject ｜ 单元：Rt_NexusWorkspace


## TNexusNotificationWithInterface
继承：TNexusNotificationWithInterface → TNexusNotification → TNotificationWithCode → TInterfacedObject → TObject ｜ 单元：Rt_NexusWorkspace

procedure Create(ACode: Integer; const AData: IInterface);
function GetData: IInterface;

## TNexusNotificationWithObject
继承：TNexusNotificationWithObject → TNexusNotification → TNotificationWithCode → TInterfacedObject → TObject ｜ 单元：Rt_NexusWorkspace

procedure Create(ACode: Integer; const AData: TObject);
function GetData: TObject;

## TNexusPortChainsData
继承：TNexusPortChainsData → TObject ｜ 单元：Rt_NexusWorkspace

property Channels: TChannelSet;  // read-only
property NexusPort: INexusPort;  // read-only
procedure Create(const ANexusPort: INexusPort; const AChannels: TChannelSet);

## TNonRefCountedInterfacedObject
继承：TNonRefCountedInterfacedObject → TObject ｜ 单元：Rt_Util


## TNotebook
继承：TNotebook → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.ExtCtrls

property ActivePage: string;
property Align: TAlign;
property Anchors: TAnchors;
property Color: TColor;
property Constraints: TSizeConstraints;
property Ctl3D: Boolean;
property DoubleBuffered: Boolean;
property DragCursor: TCursor;
property DragKind: TDragKind;
property DragMode: TDragMode;
property Enabled: Boolean;
property Font: TFont;
property OnClick: TNotifyEvent;
property OnContextPopup: TContextPopupEvent;
property OnDblClick: TNotifyEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnEndDock: TEndDragEvent;
property OnEndDrag: TEndDragEvent;
property OnEnter: TNotifyEvent;
property OnExit: TNotifyEvent;
property OnGesture: TGestureEvent;
property OnMouseActivate: TMouseActivateEvent;
property OnMouseDown: TMouseEvent;
property OnMouseEnter: TNotifyEvent;
property OnMouseLeave: TNotifyEvent;
property OnMouseMove: TMouseMoveEvent;
property OnMouseUp: TMouseEvent;
property OnPageChanged: TNotifyEvent;
property OnStartDock: TStartDockEvent;
property OnStartDrag: TStartDragEvent;
property PageIndex: Integer;
property Pages: TStrings;
property ParentColor: Boolean;
property ParentCtl3D: Boolean;
property ParentDoubleBuffered: Boolean;
property ParentFont: Boolean;
property ParentShowHint: Boolean;
property PopupMenu: TPopupMenu;
property ShowHint: Boolean;
property TabOrder: TTabOrder;
property TabStop: Boolean;
property Touch: TTouchManager;
property Visible: Boolean;

## TNotificationWithCode
继承：TNotificationWithCode → TInterfacedObject → TObject ｜ 单元：RT_ClientServerInterface

property Code: Integer;  // read-only
property Data: IInterface;
property NotificationType: WideString;
procedure AddContextParameters(AParameters: TParameterList);
procedure Create(ACode: Integer);

## TNumericField
继承：TNumericField → TField → TComponent → TPersistent → TObject ｜ 单元：Data.DB

property Alignment: TAlignment;
property DisplayFormat: string;
property EditFormat: string;

## TObject
继承：TObject ｜ 单元：System

procedure AfterConstruction;
procedure BeforeDestruction;
function ClassInfo: Pointer;
function ClassName: string;
function ClassNameIs(const Name: string): Boolean;
procedure CleanupInstance;
procedure Create;
procedure DefaultHandler(var Message);
procedure Destroy;
procedure Dispatch(var Message);
procedure DisposeOf;
function Equals(Obj: TObject): Boolean;
function FieldAddress(const Name: ShortString): Pointer;
procedure Free;
procedure FreeInstance;
function GetHashCode: Integer;
function InitInstance(Instance: Pointer): TObject;
function InstanceSize: Integer;
function MethodAddress(const Name: ShortString): Pointer;
function MethodName(Address: Pointer): string;
function NewInstance: TObject;
function QualifiedClassName: string;
function SafeCallException(ExceptObject: TObject; ExceptAddr: Pointer): HRESULT;
function ToString: string;
function UnitName: string;
function UnitScope: string;

## TObjectBucketList
继承：TObjectBucketList → TBucketList → TCustomBucketList → TObject ｜ 单元：System.Contnrs

property Data[Index: ?]: TObject;
function Add(AItem: TObject; AData: TObject): TObject;
function Remove(AItem: TObject): TObject;

## TObjectField
继承：TObjectField → TField → TComponent → TPersistent → TObject ｜ 单元：Data.DB

property FieldCount: Integer;  // read-only
property Fields: TFields;  // read-only
property FieldValues[Index: ?]: Variant;
property ObjectType: string;
property UnNamed: Boolean;  // read-only
function GetFields: TFields;
function GetFieldValue(Index: Integer): Variant;
procedure SetFieldValue(Index: Integer; const Value: Variant);

## TObjectList
继承：TObjectList → TList → TObject ｜ 单元：System.Contnrs

property Items[Index: ?]: TObject;
property OwnsObjects: Boolean;
function Add(AObject: TObject): Integer;
procedure Create;
function Extract(Item: TObject): TObject;
function ExtractItem(Item: TObject; Direction: TDirection): TObject;
function First: TObject;
function IndexOf(AObject: TObject): Integer;
function IndexOfItem(AObject: TObject; ADirection: TDirection): Integer;
procedure Insert(Index: Integer; AObject: TObject);
function Last: TObject;
function Remove(AObject: TObject): Integer;
function RemoveItem(AObject: TObject; ADirection: TDirection): Integer;

## TObjectQueue
继承：TObjectQueue → TQueue → TOrderedList → TObject ｜ 单元：System.Contnrs

function Peek: TObject;
function Pop: TObject;
function Push(AObject: TObject): TObject;

## TObjectStack
继承：TObjectStack → TStack → TOrderedList → TObject ｜ 单元：System.Contnrs

function Peek: TObject;
function Pop: TObject;
function Push(AObject: TObject): TObject;

## TObserverMapping
继承：TObserverMapping → TObject ｜ 单元：System.Classes

procedure Create;
procedure Destroy;
function GetObserverID(const Key: string): Integer;

## TObservers
继承：TObservers → TObject ｜ 单元：System.Classes

procedure AddObserver(const ID: Integer; const AIntf: IInterface);
function CanObserve(const ID: Integer): Boolean;
procedure Create;
function GetMultiCastObserver(const ID: Integer): IInterfaceList;
function GetSingleCastObserver(const ID: Integer): IInterface;
function IsObserving(const ID: Integer): Boolean;
procedure RemoveObserver(const ID: Integer; const AIntf: IInterface);
function TryIsObserving(const ID: Integer; out AIntf: IInterface): Boolean;

## TOleContainer
继承：TOleContainer → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.OleCtnrs

property Align: TAlign;
property AllowActiveDoc: Boolean;
property AllowInPlace: Boolean;
property Anchors: TAnchors;
property AutoActivate: TAutoActivate;
property AutoVerbMenu: Boolean;
property BorderStyle: TBorderStyle;
property CanPaste: Boolean;  // read-only
property Caption: TCaption;
property Color: TColor;
property Constraints: TSizeConstraints;
property CopyOnSave: Boolean;
property Ctl3D: Boolean;
property DragCursor: TCursor;
property DragMode: TDragMode;
property Enabled: Boolean;
property Iconic: Boolean;
property Linked: Boolean;  // read-only
property Modified: Boolean;
property NewInserted: Boolean;  // read-only
property ObjectVerbs: TStrings;  // read-only
property OldStreamFormat: Boolean;
property OleClassName: String;  // read-only
property OleObject: Variant;  // read-only
property OleObjectInterface: IOleObject;  // read-only
property OnActivate: TNotifyEvent;
property OnDeactivate: TNotifyEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnEndDrag: TEndDragEvent;
property OnEnter: TNotifyEvent;
property OnExit: TNotifyEvent;
property OnKeyDown: TKeyEvent;
property OnKeyPress: TKeyPressEvent;
property OnKeyUp: TKeyEvent;
property OnMouseActivate: TMouseActivateEvent;
property OnMouseDown: TMouseEvent;
property OnMouseMove: TMouseMoveEvent;
property OnMouseUp: TMouseEvent;
property OnObjectMove: TObjectMoveEvent;
property OnResize: TNotifyEvent;
property OnStartDrag: TStartDragEvent;
property ParentColor: Boolean;
property ParentCtl3D: Boolean;
property ParentShowHint: Boolean;
property PopupMenu: TPopupMenu;
property PrimaryVerb: Integer;  // read-only
property ShowHint: Boolean;
property SizeMode: TSizeMode;
property SourceDoc: String;  // read-only
property State: TObjectState;  // read-only
property StorageInterface: IStorage;  // read-only
property TabOrder: TTabOrder;
property TabStop: Boolean;
property Visible: Boolean;
procedure Changed;
function ChangeIconDialog: Boolean;
procedure Close;
procedure Copy;
procedure CreateLinkToFile(const FileName: string; Iconic: Boolean);
procedure CreateObject(const OleClassName: string; Iconic: Boolean);
procedure CreateObjectFromFile(const FileName: string; Iconic: Boolean);
procedure CreateObjectFromInfo(const CreateInfo: IDispatch);
procedure DestroyObject;
procedure DoVerb(Verb: Integer);
function GetIconMetaPict: NativeUInt;
function InsertObjectDialog: Boolean;
procedure LoadFromFile(const FileName: string);
procedure LoadFromStream(Stream: TStream);
function ObjectPropertiesDialog: Boolean;
procedure Paste;
function PasteSpecialDialog: Boolean;
procedure Run;
procedure SaveAsDocument(const FileName: string);
procedure SaveToFile(const FileName: string);
procedure SaveToStream(Stream: TStream);
procedure UpdateObject;
procedure UpdateVerbs;

## TOleControl
继承：TOleControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.OleCtrls

property Anchors: TAnchors;
property DefaultDispatch: IDispatch;  // read-only
property OleObject: Variant;  // read-only
property PerPropBrowsing: IPerPropertyBrowsing;  // read-only
property TabStop: Boolean;
procedure BrowseProperties;
procedure DoObjectVerb(Verb: Integer);
function GetEnumPropDesc(DispID: Integer): TEnumPropDesc;
function GetHelpContext(Member: string; var HelpCtx: Integer; var HelpFile: string): Boolean;
procedure GetObjectVerbs(List: TStrings);
function GetPropDisplayString(DispID: Integer): string;
procedure GetPropDisplayStrings(DispID: Integer; List: TStrings);
procedure InitControlData;
procedure InitControlInterface(const Obj: IInterface);
procedure InvokeEvent(DispID: Integer; const Params: IDispatch);
function IsCustomProperty(DispID: Integer): Boolean;
function IsPropPageProperty(DispID: Integer): Boolean;
function OnChanged(DispID: Integer): HRESULT;
function OnRequestEdit(DispID: Integer): HRESULT;
procedure SetPropDisplayString(DispID: Integer; const Value: string);
procedure ShowAboutBox;
procedure StandardEvent(DispID: Integer; const Params: IDispatch);
function SuppressException(E: Exception): Boolean;

## TOleForm
继承：TOleForm → TInterfacedObject → TObject ｜ 单元：Vcl.OleCtnrs

procedure Create(Form: TCustomForm);

## TOpenBusExportedInterruptsBuilder
继承：TOpenBusExportedInterruptsBuilder → TObject ｜ 单元：Rt_Schematic

property InterruptExportType[Index: ?]: TOpenBusInterruptExportType;
property InterruptKind[Index: ?]: TOpenBusInterruptKind;
property InterruptPolarity[Index: ?]: TOpenBusInterruptPolarity;
procedure Create(const AEncodedString: string);
function GetEncodedString: string;
function GetMask_Control: Cardinal;
function GetMask_EdgeKinds: Cardinal;
function GetMask_Kinds: Cardinal;
function GetMask_LevelKinds: Cardinal;

## TOpenDialog
继承：TOpenDialog → TCommonDialog → TComponent → TPersistent → TObject ｜ 单元：Vcl.Dialogs

property DefaultExt: string;
property FileEditStyle: TFileEditStyle;
property FileName: TFileName;
property Files: TStrings;  // read-only
property Filter: string;
property FilterIndex: Integer;
property HistoryList: TStrings;
property InitialDir: string;
property OnCanClose: TCloseQueryEvent;
property OnFolderChange: TNotifyEvent;
property OnIncludeItem: TIncludeItemEvent;
property OnSelectionChange: TNotifyEvent;
property OnTypeChange: TNotifyEvent;
property Options: TOpenOptions;
property OptionsEx: TOpenOptionsEx;
property Title: string;
function DoCanClose: Boolean;
procedure DoFolderChange;
procedure DoSelectionChange;
procedure DoTypeChange;
function GetStaticRect: IDispatch;

## TOpenPictureDialog
继承：TOpenPictureDialog → TOpenDialog → TCommonDialog → TComponent → TPersistent → TObject ｜ 单元：Vcl.ExtDlgs

property Filter: string;
procedure PreviewClick(Sender: TObject);

## TOpenTextFileDialog
继承：TOpenTextFileDialog → TOpenDialog → TCommonDialog → TComponent → TPersistent → TObject ｜ 单元：Vcl.ExtDlgs

property EncodingIndex: Integer;
property Encodings: TStrings;

## TOrderedList
继承：TOrderedList → TObject ｜ 单元：System.Contnrs

function AtLeast(ACount: Integer): Boolean;
function Count: Integer;
procedure Create;
function Peek: Pointer;
function PeekItem: Pointer;
function Pop: Pointer;
function PopItem: Pointer;
function Push(AItem: Pointer): Pointer;
procedure PushItem(AItem: Pointer);

## TOutputFileMaker
继承：TOutputFileMaker → TObject ｜ 单元：Rt_AbstractOutput

field OutputSettings;
field TargetFilename;
function AddToProject: Boolean;
procedure AllowGenerateCancel;
function Board: TPcbBoard;
function CheckGenerateCancelled: Boolean;
procedure Create(AOutputSettings: TOutputSettings);
function DocumentPath: string;
function ExplicitTargetFileName: string;
procedure Generate;
function GetFolderPath: string;
procedure GetOutputFileNames(Files: IStrings);
function GetOutputStatus: Boolean;
function GetTargetFileName(Ext: string): string;
function MakeAddressForOutputFile(Prefix: string; Extension: string; EditorKind: string): string;
function MakeOutputFilename(FileName: string; Extension: string): string;
function MakeOutputFilenameFromExtension(Extension: string): string;
function MakeOutputFilenameFromName(S: string): string;
procedure Notify_BeginGeneratingOutputFile(GeneratedFileName: string);
procedure Notify_FinishGeneratingOutputFile(GeneratedFileName: string);
function OpenOutputs: Boolean;
function PredefinedOutput: string;
function PrepareOutputFolder(FolderName: string; var OutputFolderAddress: string): Boolean;
function PrepareSubFolder(FolderAddress: string; SubFolderName: string; var PreparedSubFolderAddress: string): Boolean;
function Project: IProject;
procedure SetFolderPath(ADirectory: string);
procedure SetOutputStatus(Status: Boolean);
procedure ShowError(const S: string);
function TargetFolder: string;
function TargetPrefix: string;

## TOutputGenerator
继承：TOutputGenerator → TDispatchObject → TDispatchObject ｜ 单元：Rt_AbstractOutput

field AddToProject;
field Board;
field BoardHandle;
field CallBackHandle;
field DocumentPath;
field ExplicitTargetFileName;
field FCurrentOutputjobFileFullPath;
field fOutputMediumType;
field Name;
field OpenOutputs;
field OutputPreferences;
field OutputPreferencesForm;
field OutputPropertiesForm;
field OutputSettings;
field PageRenderer;
field ParameterSet;
field PredefinedOutput;
field PrintInputValues;
field PrintOutputValues;
field PrintPageOptions;
field Project;
field RenderedPages;
field TargetFolder;
field TargetPrefix;
procedure AddParameter(const Value: WideString);
procedure AllowGenerateCancel;
function CheckGenerateCancelled: Boolean;
procedure ClearParameters;
procedure CreateAndLoadPCB;
procedure Export_ToParameterSet(ParameterSet: TStringList);
procedure Finalize;
function GetAddToProject: WordBool;
function GetBoard: TObject;
function GetBoardHandle: NativeUInt;
function GetCurrentOutputjobFileFullPath: WideString;
function GetDocumentPath: WideString;
function GetExplicitTargetFileName: WideString;
function GetName: WideString;
function GetOpenOutputs: WordBool;
function GetOutputMediumType: WideString;
function GetOutputSettings: TObject;
function GetPageHandle(PageIndex: Integer): NativeUInt;
function GetPageInterface(APageIndex: Integer): IGeneratedPage;
function GetParameterCount: Integer;
function GetParameterValue(Index: Integer): WideString;
function GetProject: IProject;
function GetTargetPrefix: WideString;
procedure Import_FromParameterSet(ParameterSet: TStringList);
procedure Notify(NotificationKind: TOutputNotificationKind; Data: PWideChar);
procedure Notify_BeginGeneratingOutputFile(const GeneratedFileName: WideString);
procedure Notify_BeginPrintingDocument(const GeneratedFileName: WideString);
procedure Notify_FinishGeneratingOutputFile(const GeneratedFileName: WideString);
procedure Notify_FinishPrintingDocument(const GeneratedFileName: WideString);
procedure Notify_WarningInGeneratedFiles(const Warning: WideString);
procedure ParameterTransferBegin;
procedure ParameterTransferEnd;
procedure PredictOutputFileNames(Files: IStrings);
function RunGenerator: WordBool;
function RunPreferencesForm: WordBool;
function RunPropertiesForm: WordBool;
function RunWizard(X: Integer; Y: Integer): TDialogResult;
procedure SetAddToProject(AAddToProject: WordBool);
procedure SetCurrentOutputjobFileFullPath(AFullPath: WideString);
procedure SetDocumentPath(const ADocumentPath: WideString);
procedure SetExplicitTargetFileName(const AExplicitTargetFileName: WideString);
procedure SetOpenOutputs(AOpenOutputs: WordBool);
procedure SetOutputMediumType(const OutputMediumType: WideString);
procedure SetOutputPath(const ATargetFolder: WideString);
procedure SetPageOptionsToDefault(const PageOptions: IDispatch);
procedure SetTargetPrefix(const ATargetPrefix: WideString);
procedure UnloadAndFreePCB;

## TOutputGeneratorWithExtraInfo
继承：TOutputGeneratorWithExtraInfo → TOutputGenerator → TDispatchObject ｜ 单元：Rt_AbstractOutput


## TOutputGeneratorWithNamedParameters
继承：TOutputGeneratorWithNamedParameters → TOutputGenerator → TDispatchObject ｜ 单元：Rt_AbstractOutput

procedure AddNamedParameter(const Name: WideString; const Value: WideString);
function GetParameterName(Index: Integer): WideString;

## TOutputIOSignalLink
继承：TOutputIOSignalLink → TIOSignalLink → TComponent → TPersistent → TObject ｜ 单元：RT_Digital_IO

property OnChange: TOutputSignalChangedEvent;
property Value: Cardinal;

## TOutputPreferences
继承：TOutputPreferences → TNonRefCountedInterfacedObject → TObject ｜ 单元：Rt_AbstractOutput

field OutputGenerator;
function Board: TPcbBoard;
function BoardHandle: NativeInt;
procedure Create(AOutputGenerator: TOutputGenerator);
function DocumentPath: string;
procedure Export_ToIniFile;
procedure Import_FromIniFile;
function PredefinedOutput: string;
function Project: IProject;
procedure SetState_Default;
function TargetFolder: string;

## TOutputPreferencesForm
继承：TOutputPreferencesForm → TServerDialog → TServerDialog ｜ 单元：Rt_AbstractOutput

field OutputPreferences;
function Board: TPcbBoard;
procedure Create(AOutputPreferences: TOutputPreferences);
function DefaultHelpFile: string;
function DocumentPath: string;
procedure GetState_Controls;
function PredefinedOutput: string;
function Project: IProject;
procedure SetState_Controls;
function TargetFolder: string;

## TOutputPropertiesForm
继承：TOutputPropertiesForm → TServerDialog → TServerDialog ｜ 单元：Rt_AbstractOutput

field OutputSettings;
function Board: TPcbBoard;
procedure Create(AOutputSettings: TOutputSettings);
function DefaultHelpFile: string;
function DocumentPath: string;
procedure GetState_Controls;
function PostProcess: Boolean;
function PredefinedOutput: string;
function PreProcess: Boolean;
function Project: IProject;
procedure RunPreferencesForm;
procedure SetState_Controls;
function TargetFolder: string;

## TOutputSettings
继承：TOutputSettings → TCustomOutputSettings → TObject ｜ 单元：Rt_AbstractOutput

field OutputGenerator;
function Board: TPcbBoard;
function BoardHandle: NativeInt;
procedure Create(AOutputGenerator: TOutputGenerator);
function DocumentPath: string;
procedure Export_ToParameters(Parameters: PWideChar);
procedure Export_ToParameterSet(ParameterSet: TStringList);
procedure Import_FromParameters(Parameters: PWideChar);
procedure Import_FromParameterSet(ParameterSet: TStringList);
procedure InitializeFromDefaultOutput;
function PredefinedOutput: string;
function Project: IProject;
procedure SetState_Default;
procedure ShowError(const S: string);
procedure ShowWarning(const S: string);
function TargetFolder: string;

## TOutputWizard
继承：TOutputWizard → TServerDialog → TServerDialog ｜ 单元：Rt_AbstractOutput

field OutputSettings;
field StartX;
field StartY;
function Board: TPcbBoard;
procedure Create(AOutputSettings: TOutputSettings; AStartX: Integer; AStartY: Integer);
function DocumentPath: string;
procedure FormActivate(Sender: TObject);
procedure GetState_Controls;
function PredefinedOutput: string;
function Project: IProject;
procedure SetState_Controls;
function TargetFolder: string;

## TOwnedCollection
继承：TOwnedCollection → TCollection → TPersistent → TObject ｜ 单元：System.Classes


## TPadding
继承：TPadding → TMargins → TPersistent → TObject ｜ 单元：Vcl.Controls

property Bottom: TMarginSize;
property Left: TMarginSize;
property Right: TMarginSize;
property Top: TMarginSize;

## TPage
继承：TPage → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.ExtCtrls

property Caption: TCaption;
property Height: Integer;
property OnAlignInsertBefore: TAlignInsertBeforeEvent;
property OnAlignPosition: TAlignPositionEvent;
property OnGesture: TGestureEvent;
property TabOrder: TTabOrder;
property Touch: TTouchManager;
property Visible: Boolean;
property Width: Integer;

## TPageControl
继承：TPageControl → TCustomTabControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.ComCtrls

property ActivePage: TTabSheet;
property ActivePageIndex: Integer;
property Align: TAlign;
property Anchors: TAnchors;
property BiDiMode: TBiDiMode;
property Constraints: TSizeConstraints;
property DockSite: Boolean;
property DoubleBuffered: Boolean;
property DragCursor: TCursor;
property DragKind: TDragKind;
property DragMode: TDragMode;
property Enabled: Boolean;
property Font: TFont;
property HotTrack: Boolean;
property Images: TCustomImageList;
property MultiLine: Boolean;
property OnChange: TNotifyEvent;
property OnChanging: TTabChangingEvent;
property OnContextPopup: TContextPopupEvent;
property OnDockDrop: TDockDropEvent;
property OnDockOver: TDockOverEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnDrawTab: TDrawTabEvent;
property OnEndDock: TEndDragEvent;
property OnEndDrag: TEndDragEvent;
property OnEnter: TNotifyEvent;
property OnExit: TNotifyEvent;
property OnGesture: TGestureEvent;
property OnGetImageIndex: TTabGetImageEvent;
property OnGetSiteInfo: TGetSiteInfoEvent;
property OnMouseActivate: TMouseActivateEvent;
property OnMouseDown: TMouseEvent;
property OnMouseEnter: TNotifyEvent;
property OnMouseLeave: TNotifyEvent;
property OnMouseMove: TMouseMoveEvent;
property OnMouseUp: TMouseEvent;
property OnResize: TNotifyEvent;
property OnStartDock: TStartDockEvent;
property OnStartDrag: TStartDragEvent;
property OnUnDock: TUnDockEvent;
property OwnerDraw: Boolean;
property PageCount: Integer;  // read-only
property Pages[Index: ?]: TTabSheet;  // read-only
property ParentBiDiMode: Boolean;
property ParentDoubleBuffered: Boolean;
property ParentFont: Boolean;
property ParentShowHint: Boolean;
property PopupMenu: TPopupMenu;
property RaggedRight: Boolean;
property ScrollOpposite: Boolean;
property ShowHint: Boolean;
property Style: TTabStyle;
property StyleElements: TStyleElements;
property TabHeight: SmallInt;
property TabIndex: Integer;
property TabOrder: TTabOrder;
property TabPosition: TTabPosition;
property TabStop: Boolean;
property TabWidth: SmallInt;
property Touch: TTouchManager;
property Visible: Boolean;
function FindNextPage(CurPage: TTabSheet; GoForward: Boolean; CheckTabVisible: Boolean): TTabSheet;
procedure SelectNextPage(GoForward: Boolean; CheckTabVisible: Boolean);
procedure UpdateActivePage;

## TPageRenderer
继承：TPageRenderer → TInterfacedObject → TObject ｜ 单元：Rt_AbstractOutput

function CreateGeneratedPage: TGeneratedPage;
function DocumentPath: string;
function GetDMDocumentByIndex(Index: Integer): IDocument;
function GetDocumentByIndex(Index: Integer): string;
procedure GetPageDefaults(const PageOptions: IDispatch);
function GetTotalPageCount: Integer;
function IsDocumentKindSupported(DocKind: string): Boolean;
function KeepGeneratedPagesInMemory: Boolean;
procedure LoadRequiredDocuments(DocumentKind: string);
function OutputGenerator: IOutputGenerator;
function PostProcessDocument(Index: Integer): Boolean;
function PostProcessJob: Boolean;
function PostProcessPage(X: Integer; Y: Integer): Boolean;
function PostProcessPageSet(Index: Integer): Boolean;
function PreProcessDocument(Index: Integer): Boolean;
function PreProcessJob: Boolean;
function PreProcessPage(X: Integer; Y: Integer): Boolean;
function PreProcessPageSet(Index: Integer): Boolean;
function Project: IProject;
procedure RenderPage(GeneratedPage: TGeneratedPage; TileX: Integer; TileY: Integer; DocumentNumber: Integer; PageSetNumber: Integer; PageNumber: Integer; TotalPages: Integer);
function ReturnDocumentKind: string;
function ReturnDocumentSortKey(Document: IDocument): string;
procedure Run(Publisher: IPublisher);
procedure SetupPageParameters;
procedure ShowError(const S: string);

## TPageScroller
继承：TPageScroller → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.ComCtrls

property Align: TAlign;
property Anchors: TAnchors;
property AutoScroll: Boolean;
property BorderWidth: TBorderWidth;
property ButtonSize: Integer;
property Color: TColor;
property Constraints: TSizeConstraints;
property Control: TWinControl;
property DockSite: Boolean;
property DoubleBuffered: Boolean;
property DragCursor: TCursor;
property DragKind: TDragKind;
property DragMode: TDragMode;
property DragScroll: Boolean;
property Enabled: Boolean;
property Font: TFont;
property Margin: Integer;
property OnClick: TNotifyEvent;
property OnContextPopup: TContextPopupEvent;
property OnDblClick: TNotifyEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnEndDock: TEndDragEvent;
property OnEndDrag: TEndDragEvent;
property OnEnter: TNotifyEvent;
property OnExit: TNotifyEvent;
property OnKeyDown: TKeyEvent;
property OnKeyPress: TKeyPressEvent;
property OnKeyUp: TKeyEvent;
property OnMouseWheel: TMouseWheelEvent;
property OnResize: TNotifyEvent;
property OnScroll: TPageScrollEvent;
property OnStartDock: TStartDockEvent;
property OnStartDrag: TStartDragEvent;
property Orientation: TPageScrollerOrientation;
property ParentBackground: Boolean;
property ParentColor: Boolean;
property ParentDoubleBuffered: Boolean;
property ParentFont: Boolean;
property ParentShowHint: Boolean;
property PopupMenu: TPopupMenu;
property Position: Integer;
property ShowHint: Boolean;
property StyleElements: TStyleElements;
property TabOrder: TTabOrder;
property TabStop: Boolean;
property Visible: Boolean;
function GetButtonState(Button: TPageScrollerButton): TPageScrollerButtonState;
procedure Scroll(Shift: TShiftState; X: Integer; Y: Integer; Orientation: TPageScrollerOrientation; var Delta: Integer);

## TPageScrollerStyleHook
继承：TPageScrollerStyleHook → TStyleHook → TStyleHook ｜ 单元：Vcl.ComCtrls


## TPageSetupDialog
继承：TPageSetupDialog → TCommonDialog → TComponent → TPersistent → TObject ｜ 单元：Vcl.Dialogs

property BeforePaint: TPageSetupBeforePaintEvent;
property MarginBottom: Integer;
property MarginLeft: Integer;
property MarginRight: Integer;
property MarginTop: Integer;
property MinMarginBottom: Integer;
property MinMarginLeft: Integer;
property MinMarginRight: Integer;
property MinMarginTop: Integer;
property OnDrawEnvStamp: TPaintPageEvent;
property OnDrawFullPage: TPaintPageEvent;
property OnDrawGreekText: TPaintPageEvent;
property OnDrawMargin: TPaintPageEvent;
property OnDrawMinMargin: TPaintPageEvent;
property OnDrawRetAddress: TPaintPageEvent;
property Options: TPageSetupDialogOptions;
property PageHeight: Integer;
property PageSetupDlgRec: TPageSetupDlg;  // read-only
property PageWidth: Integer;
property Units: TPageMeasureUnits;
function GetDefaults: Boolean;

## TPaintBox
继承：TPaintBox → TGraphicControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.ExtCtrls

property Align: TAlign;
property Anchors: TAnchors;
property Canvas: TCanvas;  // read-only
property Color: TColor;
property Constraints: TSizeConstraints;
property DragCursor: TCursor;
property DragKind: TDragKind;
property DragMode: TDragMode;
property Enabled: Boolean;
property Font: TFont;
property OnClick: TNotifyEvent;
property OnContextPopup: TContextPopupEvent;
property OnDblClick: TNotifyEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnEndDock: TEndDragEvent;
property OnEndDrag: TEndDragEvent;
property OnGesture: TGestureEvent;
property OnMouseActivate: TMouseActivateEvent;
property OnMouseDown: TMouseEvent;
property OnMouseEnter: TNotifyEvent;
property OnMouseLeave: TNotifyEvent;
property OnMouseMove: TMouseMoveEvent;
property OnMouseUp: TMouseEvent;
property OnPaint: TNotifyEvent;
property OnStartDock: TStartDockEvent;
property OnStartDrag: TStartDragEvent;
property ParentColor: Boolean;
property ParentFont: Boolean;
property ParentShowHint: Boolean;
property PopupMenu: TPopupMenu;
property ShowHint: Boolean;
property Touch: TTouchManager;
property Visible: Boolean;

## TPaintControl
继承：TPaintControl → TObject ｜ 单元：Vcl.DBCtrls

property Ctl3DButton: Boolean;
property Handle: HWnd;  // read-only
procedure Create(AOwner: TWinControl; const ClassName: string);
procedure DestroyHandle;

## TPanel
继承：TPanel → TCustomPanel → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.ExtCtrls

property Align: TAlign;
property Alignment: TAlignment;
property Anchors: TAnchors;
property AutoSize: Boolean;
property BevelEdges: TBevelEdges;
property BevelInner: TBevelCut;
property BevelKind: TBevelKind;
property BevelOuter: TBevelCut;
property BevelWidth: TBevelWidth;
property BiDiMode: TBiDiMode;
property BorderStyle: TBorderStyle;
property BorderWidth: TBorderWidth;
property Caption: TCaption;
property Color: TColor;
property Constraints: TSizeConstraints;
property Ctl3D: Boolean;
property DockManager: IDockManager;
property DockSite: Boolean;
property DoubleBuffered: Boolean;
property DragCursor: TCursor;
property DragKind: TDragKind;
property DragMode: TDragMode;
property Enabled: Boolean;
property Font: TFont;
property FullRepaint: Boolean;
property Locked: Boolean;
property OnAlignInsertBefore: TAlignInsertBeforeEvent;
property OnAlignPosition: TAlignPositionEvent;
property OnCanResize: TCanResizeEvent;
property OnClick: TNotifyEvent;
property OnConstrainedResize: TConstrainedResizeEvent;
property OnContextPopup: TContextPopupEvent;
property OnDblClick: TNotifyEvent;
property OnDockDrop: TDockDropEvent;
property OnDockOver: TDockOverEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnEndDock: TEndDragEvent;
property OnEndDrag: TEndDragEvent;
property OnEnter: TNotifyEvent;
property OnExit: TNotifyEvent;
property OnGesture: TGestureEvent;
property OnGetSiteInfo: TGetSiteInfoEvent;
property OnMouseActivate: TMouseActivateEvent;
property OnMouseDown: TMouseEvent;
property OnMouseEnter: TNotifyEvent;
property OnMouseLeave: TNotifyEvent;
property OnMouseMove: TMouseMoveEvent;
property OnMouseUp: TMouseEvent;
property OnResize: TNotifyEvent;
property OnStartDock: TStartDockEvent;
property OnStartDrag: TStartDragEvent;
property OnUnDock: TUnDockEvent;
property Padding: TPadding;
property ParentBackground: Boolean;
property ParentBiDiMode: Boolean;
property ParentColor: Boolean;
property ParentCtl3D: Boolean;
property ParentDoubleBuffered: Boolean;
property ParentFont: Boolean;
property ParentShowHint: Boolean;
property PopupMenu: TPopupMenu;
property ShowCaption: Boolean;
property ShowHint: Boolean;
property StyleElements: TStyleElements;
property TabOrder: TTabOrder;
property TabStop: Boolean;
property Touch: TTouchManager;
property UseDockManager: Boolean;
property VerticalAlignment: TVerticalAlignment;
property Visible: Boolean;

## TParaAttributes
继承：TParaAttributes → TPersistent → TObject ｜ 单元：Vcl.ComCtrls

property Alignment: TAlignment;
property FirstIndent: Longint;
property LeftIndent: Longint;
property Numbering: TNumberingStyle;
property RightIndent: Longint;
property Tab[Index: ?]: Longint;
property TabCount: Integer;
procedure Create(AOwner: TCustomRichEdit);

## TParam
继承：TParam → TCollectionItem → TPersistent → TObject ｜ 单元：Data.DB

property AsAnsiString: AnsiString;
property AsBCD: Currency;
property AsBoolean: Boolean;
property AsByte: Longint;
property AsCurrency: Currency;
property AsDataSet: TDataSet;
property AsDate: TDateTime;
property AsDateTime: TDateTime;
property AsFloat: Double;
property AsFMTBCD: TBcd;
property AsInteger: Longint;
property AsLargeInt: Largeint;
property AsLongWord: LongWord;
property AsMemo: String;
property AsObject: TObject;
property AsParams: TParams;
property AsShortInt: Longint;
property AsSingle: Single;
property AsSmallInt: Longint;
property AsSQLTimeStamp: TSQLTimeStamp;
property AsSQLTimeStampOffset: TSQLTimeStampOffset;
property AsStream: TStream;
property AsString: String;
property AsTime: TDateTime;
property AsWideString: String;
property AsWord: Longint;
property Bound: Boolean;
property DataType: TFieldType;
property IsNull: Boolean;  // read-only
property Name: string;
property NativeStr: String;
property NumericScale: Integer;
property ParamType: TParamType;
property Precision: Integer;
property Size: Integer;
property Text: String;
property Value: Variant;
procedure AssignField(Field: TField);
procedure AssignFieldValue(Field: TField; const Value: Variant);
procedure Clear;
procedure Create(AParams: TParams; AParamType: TParamType);
procedure GetData(Buffer: TArray<System.Byte>);
function GetDataSize: Integer;
procedure LoadFromFile(const FileName: string; BlobType: TBlobType);
procedure LoadFromStream(Stream: TStream; BlobType: TBlobType);
procedure SetBlobData(Buffer: TArray<System.Byte>; Size: Integer);
procedure SetData(Buffer: TArray<System.Byte>);
procedure SetDataSet(DataSet: TDataSet; AInstanceOwner: Boolean);
function SetObjectValue(const AInstance: TObject; const ADataType: TFieldType; AInstanceOwner: Boolean): IParamObject;
procedure SetParams(Params: TParams; AInstanceOwner: Boolean);
procedure SetStream(Stream: TStream; AInstanceOwner: Boolean; KnownSize: Integer);

## TParameter
继承：TParameter → TCollectionItem → TPersistent → TObject ｜ 单元：Data.Win.ADODB

property Attributes: TParameterAttributes;
property DataType: TFieldType;
property Direction: TParameterDirection;
property Name: TDynamicString;
property NumericScale: Byte;
property ParameterObject: _Parameter;  // read-only
property Parameters: TParameters;  // read-only
property Precision: Byte;
property Properties: Properties;  // read-only
property Size: Integer;
property Value: TDynamicString;
procedure AppendChunk(Val: OleVariant);
procedure Create(const AName: string; const AValue: string);
procedure LoadFromFile(const FileName: string; DataType: TFieldType);
procedure LoadFromStream(Stream: TStream; DataType: TFieldType);

## TParameterList
继承：TParameterList → TList → TObject ｜ 单元：Rt_Param

procedure ClearAllParameters;
procedure GetState(P: PWideChar);
function GetState_ParameterAsBoolean(const Name: string; var Value: Boolean): Boolean;
function GetState_ParameterAsDouble(const Name: string; var Value: Double): Boolean;
function GetState_ParameterAsInt64(const Name: string; var Value: Int64): Boolean;
function GetState_ParameterAsInteger(const Name: string; var Value: Integer): Boolean;
function GetState_ParameterAsLongInt(const Name: string; var Value: Integer): Boolean;
function GetState_ParameterAsPChar(const Name: string; var Value: PWideChar): Boolean;
function GetState_ParameterAsReal(const Name: string; var Value: Single): Boolean;
function GetState_ParameterAsSmallInt(const Name: string; var Value: SmallInt): Boolean;
function GetState_ParameterAsString(const Name: string; var Value: string): Boolean;
function GetState_ParameterAsWord(const Name: string; var Value: Word): Boolean;
function GetState_ParameterAsWordBool(const Name: string; var Value: WordBool): Boolean;
function GetState_ParameterByName(const AName: string): TParameter;
function GetState_ToString: string;
procedure SetState(P: PWideChar; TrimAll: Boolean);
procedure SetState_AddOrReplaceParameter(const AName: string; const AValue: string; CanReplace: Boolean);
procedure SetState_AddParameter(const AName: string; const AValue: string; TrimAll: Boolean);
procedure SetState_AddParameterAsBoolean(const AName: string; Value: Boolean);
procedure SetState_AddParameterAsDouble(const AName: string; const Value: Double);
procedure SetState_AddParameterAsInt64(const AName: string; Value: Int64);
procedure SetState_AddParameterAsInteger(const AName: string; Value: Integer);
procedure SetState_AddParameterAsString(const AName: string; const Value: string; TrimAll: Boolean);
procedure SetState_FromString(const S: string; TrimAll: Boolean);
function SetState_RemoveByName(const AName: string): Boolean;

## TParameters
继承：TParameters → TOwnedCollection → TCollection → TPersistent → TObject ｜ 单元：Data.Win.ADODB

property Command: TADOCommand;  // read-only
property Items[Index: ?]: TParameter;
property ParameterCollection: Parameters;  // read-only
property ParamValues[Index: ?]: Variant;
function AddParameter: TParameter;
procedure AssignValues(Value: TParameters);
function CreateParameter(const Name: WideString; DataType: TFieldType; Direction: TParameterDirection; Size: Integer; Value: OleVariant): TParameter;
function FindParam(const Value: WideString): TParameter;
procedure GetParamList(List: TList; const ParamNames: WideString);
function IsEqual(Value: TParameters): Boolean;
function ParamByName(const Value: WideString): TParameter;
function ParseSQL(const SQL: WideString; DoCreate: Boolean): WideString;
function Refresh: Boolean;

## TParamObject
继承：TParamObject → TInterfacedObject → TObject ｜ 单元：Data.DB

procedure Create(AObject: TObject; ADataType: TFieldType; AInstanceOwner: Boolean);

## TParams
继承：TParams → TCollection → TPersistent → TObject ｜ 单元：Data.DB

property Items[Index: ?]: TParam;
property ParamValues[Index: ?]: Variant;
procedure AddParam(Value: TParam);
function AddParameter: TParam;
procedure AssignValues(Value: TParams);
procedure Create(Owner: TPersistent);
function CreateParam(FldType: TFieldType; const ParamName: string; ParamType: TParamType): TParam;
function FindParam(const Value: string): TParam;
procedure GetParamList(List: TList<Data.DB.TParam>; const ParamNames: string);
function IsEqual(Value: TParams): Boolean;
function ParamByName(const Value: string): TParam;
function ParseSQL(const SQL: string; DoCreate: Boolean): string;
procedure RemoveParam(Value: TParam);

## TParamStreamObject
继承：TParamStreamObject → TParamObject → TInterfacedObject → TObject ｜ 单元：Data.DB


## TParser
继承：TParser → TObject ｜ 单元：System.Classes

property FloatType: Char;  // read-only
property LinePos: Integer;  // read-only
property SourceLine: Integer;  // read-only
property Token: Char;  // read-only
procedure CheckToken(T: Char);
procedure CheckTokenSymbol(const S: string);
procedure Error(const Ident: string);
procedure ErrorFmt(const Ident: string; const Args: array of TVarRec);
procedure ErrorStr(const Message: string);
procedure HexToBinary(Stream: TStream);
function NextToken: Char;
function SourcePos: Integer;
function TokenComponentIdent: string;
function TokenFloat: Extended;
function TokenInt: Int64;
function TokenString: string;
function TokenSymbolIs(const S: string): Boolean;
function TokenWideString: string;

## TPen
继承：TPen → TGraphicsObject → TPersistent → TObject ｜ 单元：Vcl.Graphics

property Color: TColor;
property Handle: HPen;
property Mode: TPenMode;
property Style: TPenStyle;
property Width: Integer;
procedure Create;

## TPenRecall
继承：TPenRecall → TRecall → TObject ｜ 单元：Vcl.Graphics

procedure Create(APen: TPen);

## TPersistent
继承：TPersistent → TObject ｜ 单元：System.Classes

procedure Assign(Source: TPersistent);
procedure AssignTo(Dest: TPersistent);
procedure DefineProperties(Filer: TFiler);
function GetNamePath: string;
function GetOwner: TPersistent;

## TPicture
继承：TPicture → TInterfacedPersistent → TPersistent → TObject ｜ 单元：Vcl.Graphics

property Bitmap: TBitmap;
property Graphic: TGraphic;
property Height: Integer;  // read-only
property Icon: TIcon;
property Metafile: TMetafile;
property PictureAdapter: IChangeNotifier;
property Width: Integer;  // read-only
procedure Changed(Sender: TObject);
procedure Create;
procedure LoadFromClipboardFormat(AFormat: Word; AData: NativeUInt; APalette: HPALETTE);
procedure LoadFromFile(const Filename: string);
procedure Progress(Sender: TObject; Stage: TProgressStage; PercentDone: Byte; RedrawNow: Boolean; const R: IDispatch; const Msg: string);
procedure SaveToClipboardFormat(var AFormat: Word; var AData: NativeUInt; var APalette: HPALETTE);
procedure SaveToFile(const Filename: string);
function SupportsClipboardFormat(AFormat: Word): Boolean;

## TPlatformValueBuffer
继承：TPlatformValueBuffer → TObject ｜ 单元：Data.DB

procedure Copy(Buffer: TArray<System.Byte>; const Dest: TArray<System.Byte>; Offset: Integer; Count: Integer);
procedure Free(Buffer: TArray<System.Byte>);

## TPngImage
继承：TPngImage → TGraphic → TInterfacedPersistent → TPersistent → TObject ｜ 单元：Vcl.Imaging.pngimage

property Canvas: TCanvas;  // read-only
property Chunks: TPNGList;  // read-only
property CompressionLevel: TCompressionLevel;
property Empty: Boolean;  // read-only
property ExtraScanline[Index: ?]: Pointer;  // read-only
property Filters: TFilters;
property Header: TChunkIHDR;  // read-only
property Height: Integer;  // read-only
property InterlaceMethod: TInterlaceMethod;
property MaxIdatSize: Integer;
property PixelInformation: TChunkpHYs;  // read-only
property Pixels[Index1: ?, Index2: ?]: TColor;
property Scanline[Index: ?]: Pointer;  // read-only
property TransparencyMode: TPNGTransparencyMode;  // read-only
property TransparentColor: TColor;
property Version: String;  // read-only
property Width: Integer;  // read-only
procedure AddtEXt(const Keyword: AnsiString; const Text: AnsiString);
procedure AddzTXt(const Keyword: AnsiString; const Text: AnsiString);
procedure AssignHandle(Handle: HBITMAP; Transparent: Boolean; TransparentColor: Cardinal);
procedure CreateAlpha;
procedure CreateBlank(ColorType: Cardinal; Bitdepth: Cardinal; CX: Integer; CY: Integer);
procedure DrawUsingPixelInformation(Canvas: TCanvas; const Point: IDispatch);
function GetPixels(const X: Integer; const Y: Integer): TColor;
function HasPixelInformation: Boolean;
procedure LoadFromResourceID(Instance: NativeUInt; ResID: Integer);
procedure LoadFromResourceName(Instance: NativeUInt; const Name: string);
procedure RemoveTransparency;
procedure Resize(const CX: Integer; const CY: Integer);
procedure SetPixels(const X: Integer; const Y: Integer; const Value: TColor);

## TPNGList
继承：TPNGList → TPNGPointerList → TObject ｜ 单元：Vcl.Imaging.pngimage

property Item[Index: ?]: TChunk;  // read-only
procedure RemoveChunk(Chunk: TChunk);

## TPNGPointerList
继承：TPNGPointerList → TObject ｜ 单元：Vcl.Imaging.pngimage

property Count: Cardinal;
procedure Create(AOwner: TPngImage);
function Remove(Value: Pointer): Pointer;

## TPopupDataList
继承：TPopupDataList → TDBLookupListBox → TDBLookupControl → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.DBCtrls


## TPopupList
继承：TPopupList → TList → TObject ｜ 单元：Vcl.Menus

property Window: HWND;  // read-only
procedure Add(Popup: TPopupMenu);
procedure Remove(Popup: TPopupMenu);
procedure WndProc(const Message: IDispatch);

## TPopupMenu
继承：TPopupMenu → TMenu → TComponent → TPersistent → TObject ｜ 单元：Vcl.Menus

property Alignment: TPopupAlignment;
property AutoHotkeys: TMenuAutoFlag;
property AutoLineReduction: TMenuAutoFlag;
property AutoPopup: Boolean;
property BiDiMode: TBiDiMode;
property HelpContext: THelpContext;
property Images: TCustomImageList;
property MenuAnimation: TMenuAnimation;
property OnChange: TMenuChangeEvent;
property OnPopup: TNotifyEvent;
property OwnerDraw: Boolean;
property ParentBiDiMode: Boolean;
property PopupComponent: TComponent;
property PopupPoint: TPoint;  // read-only
property TrackButton: TTrackButton;
procedure CloseMenu;
procedure DoPopup(Sender: TObject);
procedure Popup(X: Integer; Y: Integer);

## TPreferencesPageNotification
继承：TPreferencesPageNotification → TSystemNotification → TNotificationWithCode → TInterfacedObject → TObject ｜ 单元：RT_ClientServerInterface

procedure Create(ACode: Integer; const AServerName: string; const APageName: string);

## TPrintDialog
继承：TPrintDialog → TCommonDialog → TComponent → TPersistent → TObject ｜ 单元：Vcl.Dialogs

property Collate: Boolean;
property Copies: Integer;
property FromPage: Integer;
property MaxPage: Integer;
property MinPage: Integer;
property Options: TPrintDialogOptions;
property PrintRange: TPrintRange;
property PrintToFile: Boolean;
property ToPage: Integer;

## TPrintDlg
继承：TPrintDlg → TCommonDialogAction → TCustomAction → TContainedAction ｜ 单元：Vcl.StdActns

property BeforeExecute: TNotifyEvent;
property Caption: string;
property Dialog: TPrintDialog;  // read-only
property Enabled: Boolean;
property HelpContext: THelpContext;
property HelpKeyword: string;
property HelpType: THelpType;
property Hint: string;
property ImageIndex: TImageIndex;
property OnAccept: TNotifyEvent;
property OnCancel: TNotifyEvent;
property OnHint: THintEvent;
property OnUpdate: TNotifyEvent;
property SecondaryShortCuts: TCustomShortCutList;
property ShortCut: TShortCut;
property Visible: Boolean;

## TPrinter
继承：TPrinter → TObject ｜ 单元：Vcl.Printers

property Aborted: Boolean;  // read-only
property Canvas: TCanvas;  // read-only
property Capabilities: TPrinterCapabilities;  // read-only
property Copies: Integer;
property Fonts: TStrings;  // read-only
property Handle: HDC;  // read-only
property Orientation: TPrinterOrientation;
property PageHeight: Integer;  // read-only
property PageNumber: Integer;  // read-only
property PageWidth: Integer;  // read-only
property PrinterIndex: Integer;
property Printers: TStrings;  // read-only
property Printing: Boolean;  // read-only
property Title: String;
procedure Abort;
procedure BeginDoc;
procedure Create;
procedure EndDoc;
procedure GetPrinter(ADevice: PWideChar; ADriver: PWideChar; APort: PWideChar; var ADeviceMode: NativeUInt);
procedure NewPage;
procedure Refresh;
procedure SetPrinter(ADevice: PWideChar; ADriver: PWideChar; APort: PWideChar; ADeviceMode: NativeUInt);

## TPrinterSetupDialog
继承：TPrinterSetupDialog → TCommonDialog → TComponent → TPersistent → TObject ｜ 单元：Vcl.Dialogs


## TProcessFlow_ACTEL_ProASICPlus
继承：TProcessFlow_ACTEL_ProASICPlus → TProcessFlowCategory → TProcessFlowCategory ｜ 单元：Rt_ActelFPGA

property DesignerPath: TDynamicString;
field FDesignerPath;
procedure Create(ANexusDriver: INexusDriver);

## TProcessFlow_ACTELCPLD
继承：TProcessFlow_ACTELCPLD → TProcessFlowCategory → TProcessFlowCategory ｜ 单元：Rt_ActelFPGA

procedure Create(ANexusDriver: INexusDriver);

## TProcessFlow_ACTELFPGA
继承：TProcessFlow_ACTELFPGA → TProcessFlowCategory → TProcessFlowCategory ｜ 单元：Rt_ActelFPGA

property DesignerPath: TDynamicString;
field FDesignerPath;
procedure Create(ANexusDriver: INexusDriver);

## TProcessFlow_AlteraCPLD
继承：TProcessFlow_AlteraCPLD → TProcessFlowCategory → TProcessFlowCategory ｜ 单元：Rt_AlteraFPGA

procedure Create(ANexusDriver: INexusDriver);

## TProcessFlow_AlteraFPGA
继承：TProcessFlow_AlteraFPGA → TProcessFlowCategory → TProcessFlowCategory ｜ 单元：Rt_AlteraFPGA

procedure Create(ANexusDriver: INexusDriver);

## TProcessFlow_XilinxCPLD
继承：TProcessFlow_XilinxCPLD → TProcessFlowCategory → TProcessFlowCategory ｜ 单元：Rt_XilinxFPGA

procedure Create(ANexusDriver: INexusDriver);

## TProcessFlow_XilinxFPGA
继承：TProcessFlow_XilinxFPGA → TProcessFlowCategory → TProcessFlowCategory ｜ 单元：Rt_XilinxFPGA

procedure Create(ANexusDriver: INexusDriver);

## TProgressBar
继承：TProgressBar → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.ComCtrls

property Align: TAlign;
property Anchors: TAnchors;
property BackgroundColor: TColor;
property BarColor: TColor;
property BorderWidth: TBorderWidth;
property Constraints: TSizeConstraints;
property DoubleBuffered: Boolean;
property DragCursor: TCursor;
property DragKind: TDragKind;
property DragMode: TDragMode;
property Enabled: Boolean;
property Hint: string;
property MarqueeInterval: Integer;
property Max: Integer;
property Min: Integer;
property OnContextPopup: TContextPopupEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnEndDock: TEndDragEvent;
property OnEndDrag: TEndDragEvent;
property OnEnter: TNotifyEvent;
property OnExit: TNotifyEvent;
property OnGesture: TGestureEvent;
property OnMouseActivate: TMouseActivateEvent;
property OnMouseDown: TMouseEvent;
property OnMouseEnter: TNotifyEvent;
property OnMouseLeave: TNotifyEvent;
property OnMouseMove: TMouseMoveEvent;
property OnMouseUp: TMouseEvent;
property OnStartDock: TStartDockEvent;
property OnStartDrag: TStartDragEvent;
property Orientation: TProgressBarOrientation;
property ParentDoubleBuffered: Boolean;
property ParentShowHint: Boolean;
property PopupMenu: TPopupMenu;
property Position: Integer;
property ShowHint: Boolean;
property Smooth: Boolean;
property SmoothReverse: Boolean;
property State: TProgressBarState;
property Step: Integer;
property Style: TProgressBarStyle;
property StyleElements: TStyleElements;
property TabOrder: TTabOrder;
property TabStop: Boolean;
property Touch: TTouchManager;
property Visible: Boolean;
procedure StepBy(Delta: Integer);
procedure StepIt;

## TProgressBarMetrics
继承：TProgressBarMetrics → TPersistent → TObject ｜ 单元：InstrumentProgress

property BlockGap: Integer;
property BlockSize: NaturalNumber;
procedure Create(AOwner: TCustomInstrumentProgressBar);

## TProgressBarStyleHook
继承：TProgressBarStyleHook → TStyleHook → TStyleHook ｜ 单元：Vcl.ComCtrls


## TPushButtonActionLink
继承：TPushButtonActionLink → TButtonActionLink → TWinControlActionLink → TControlActionLink → TActionLink → TContainedActionLink ｜ 单元：Vcl.StdCtrls


## TQueue
继承：TQueue → TOrderedList → TObject ｜ 单元：System.Contnrs


## TRadioButton
继承：TRadioButton → TButtonControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.StdCtrls

property Action: TBasicAction;
property Align: TAlign;
property Alignment: TLeftRight;
property Anchors: TAnchors;
property BiDiMode: TBiDiMode;
property Caption: TCaption;
property Checked: Boolean;
property Color: TColor;
property Constraints: TSizeConstraints;
property Ctl3D: Boolean;
property DoubleBuffered: Boolean;
property DragCursor: TCursor;
property DragKind: TDragKind;
property DragMode: TDragMode;
property Enabled: Boolean;
property Font: TFont;
property OnClick: TNotifyEvent;
property OnContextPopup: TContextPopupEvent;
property OnDblClick: TNotifyEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnEndDock: TEndDragEvent;
property OnEndDrag: TEndDragEvent;
property OnEnter: TNotifyEvent;
property OnExit: TNotifyEvent;
property OnKeyDown: TKeyEvent;
property OnKeyPress: TKeyPressEvent;
property OnKeyUp: TKeyEvent;
property OnMouseActivate: TMouseActivateEvent;
property OnMouseDown: TMouseEvent;
property OnMouseEnter: TNotifyEvent;
property OnMouseLeave: TNotifyEvent;
property OnMouseMove: TMouseMoveEvent;
property OnMouseUp: TMouseEvent;
property OnStartDock: TStartDockEvent;
property OnStartDrag: TStartDragEvent;
property ParentBiDiMode: Boolean;
property ParentColor: Boolean;
property ParentCtl3D: Boolean;
property ParentDoubleBuffered: Boolean;
property ParentFont: Boolean;
property ParentShowHint: Boolean;
property PopupMenu: TPopupMenu;
property ShowHint: Boolean;
property StyleElements: TStyleElements;
property TabOrder: TTabOrder;
property TabStop: Boolean;
property Visible: Boolean;
property WordWrap: Boolean;

## TRadioButtonStyleHook
继承：TRadioButtonStyleHook → TCheckBoxStyleHook → TMouseTrackControlStyleHook ｜ 单元：Vcl.StdCtrls


## TRadioGroup
继承：TRadioGroup → TCustomRadioGroup → TCustomGroupBox → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.ExtCtrls

property Align: TAlign;
property Anchors: TAnchors;
property BiDiMode: TBiDiMode;
property Caption: TCaption;
property Color: TColor;
property Columns: Integer;
property Constraints: TSizeConstraints;
property Ctl3D: Boolean;
property DoubleBuffered: Boolean;
property DragCursor: TCursor;
property DragKind: TDragKind;
property DragMode: TDragMode;
property Enabled: Boolean;
property Font: TFont;
property ItemIndex: Integer;
property Items: TStrings;
property OnClick: TNotifyEvent;
property OnContextPopup: TContextPopupEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnEndDock: TEndDragEvent;
property OnEndDrag: TEndDragEvent;
property OnEnter: TNotifyEvent;
property OnExit: TNotifyEvent;
property OnGesture: TGestureEvent;
property OnStartDock: TStartDockEvent;
property OnStartDrag: TStartDragEvent;
property ParentBackground: Boolean;
property ParentBiDiMode: Boolean;
property ParentColor: Boolean;
property ParentCtl3D: Boolean;
property ParentDoubleBuffered: Boolean;
property ParentFont: Boolean;
property ParentShowHint: Boolean;
property PopupMenu: TPopupMenu;
property ShowHint: Boolean;
property StyleElements: TStyleElements;
property TabOrder: TTabOrder;
property TabStop: Boolean;
property Touch: TTouchManager;
property Visible: Boolean;
property WordWrap: Boolean;

## TRDSConnection
继承：TRDSConnection → TCustomConnection → TComponent → TPersistent → TObject ｜ 单元：Data.Win.ADODB

property AfterConnect: TNotifyEvent;
property AfterDisconnect: TNotifyEvent;
property AppServer: OleVariant;  // read-only
property BeforeConnect: TNotifyEvent;
property BeforeDisconnect: TNotifyEvent;
property ComputerName: WideString;
property Connected: Boolean;
property DataSpaceObject: DataSpace;  // read-only
property InternetTimeout: Integer;
property ServerName: WideString;
function GetRecordset(const CommandText: WideString; ConnectionString: WideString): _Recordset;

## TReader
继承：TReader → TFiler → TObject ｜ 单元：System.Classes

property Owner: TComponent;
property Parent: TComponent;
property Position: Longint;
procedure BeginReferences;
procedure CheckValue(Value: TValueType);
procedure CopyValue(const Writer: TWriter);
function EndOfList: Boolean;
procedure EndReferences;
function Error(const Message: string): Boolean;
function FindMethod(Root: TComponent; const MethodName: string): Pointer;
function FindMethodInstance(Root: TComponent; const MethodName: string): IDispatch;
procedure FixupReferences;
function NextValue: TValueType;
procedure Read(var Buffer; Count: Integer);
function ReadBoolean: Boolean;
function ReadChar: Char;
procedure ReadCollection(const Collection: TCollection);
function ReadComponent(Component: TComponent): TComponent;
function ReadCurrency: Currency;
function ReadDate: TDateTime;
function ReadDouble: Double;
function ReadFloat: Extended;
function ReadIdent: string;
function ReadInt64: Int64;
function ReadInteger: Integer;
procedure ReadListBegin;
procedure ReadListEnd;
procedure ReadPrefix(var Flags: TFilerFlags; var AChildPos: Integer);
function ReadRootComponent(const Root: TComponent): TComponent;
procedure ReadSignature;
function ReadSingle: Single;
function ReadStr: string;
function ReadString: string;
function ReadValue: TValueType;
procedure ReadVar(var Buffer: AnsiChar; Count: Integer);
function ReadVariant: Variant;
function ReadWideChar: Char;
function ReadWideString: string;
procedure ReferenceName(var Name: string);
procedure SetName(Component: TComponent; var Name: string);
procedure SkipValue;

## TRecall
继承：TRecall → TObject ｜ 单元：System.Classes

property Reference: TPersistent;  // read-only
procedure Create(AStorage: TPersistent; AReference: TPersistent);
procedure Forget;
procedure Store;

## TReferenceField
继承：TReferenceField → TDataSetField → TObjectField → TField → TComponent → TPersistent → TObject ｜ 单元：Data.DB

property ReferenceTableName: string;
property Size: Integer;

## TRegIniFile
继承：TRegIniFile → TRegistry → TObject ｜ 单元：System.Win.Registry

property FileName: String;  // read-only
procedure Create(const FileName: string);
procedure DeleteKey(const Section: string; const Ident: string);
procedure EraseSection(const Section: string);
function ReadBool(const Section: string; const Ident: string; Default: Boolean): Boolean;
function ReadInteger(const Section: string; const Ident: string; Default: Integer): Integer;
procedure ReadSection(const Section: string; Strings: TStrings);
procedure ReadSections(Strings: TStrings);
procedure ReadSectionValues(const Section: string; Strings: TStrings);
function ReadString(const Section: string; const Ident: string; const Default: string): string;
procedure WriteBool(const Section: string; const Ident: string; Value: Boolean);
procedure WriteInteger(const Section: string; const Ident: string; Value: Integer);
procedure WriteString(const Section: string; const Ident: string; const Value: string);

## TRegistry
继承：TRegistry → TObject ｜ 单元：System.Win.Registry

property Access: LongWord;
property CurrentKey: HKEY;  // read-only
property CurrentPath: String;  // read-only
property LastError: Longint;  // read-only
property LastErrorMsg: String;  // read-only
property LazyWrite: Boolean;
property RootKey: HKEY;
property RootKeyName: String;  // read-only
procedure CloseKey;
procedure Create;
function CreateKey(const Key: string): Boolean;
function DeleteKey(const Key: string): Boolean;
function DeleteValue(const Name: string): Boolean;
function GetDataAsString(const ValueName: string; PrefixType: Boolean): string;
function GetDataInfo(const ValueName: string; const Value: IDispatch): Boolean;
function GetDataSize(const ValueName: string): Integer;
function GetDataType(const ValueName: string): TRegDataType;
function GetKeyInfo(const Value: IDispatch): Boolean;
procedure GetKeyNames(Strings: TStrings);
procedure GetValueNames(Strings: TStrings);
function HasSubKeys: Boolean;
function KeyExists(const Key: string): Boolean;
function LoadKey(const Key: string; const FileName: string): Boolean;
procedure MoveKey(const OldName: string; const NewName: string; Delete: Boolean);
function OpenKey(const Key: string; CanCreate: Boolean): Boolean;
function OpenKeyReadOnly(const Key: string): Boolean;
function ReadBinaryData(const Name: string; var Buffer: string; BufSize: Integer): Integer;
function ReadBool(const Name: string): Boolean;
function ReadCurrency(const Name: string): Currency;
function ReadDate(const Name: string): TDateTime;
function ReadDateTime(const Name: string): TDateTime;
function ReadFloat(const Name: string): Double;
function ReadInteger(const Name: string): Integer;
function ReadString(const Name: string): string;
function ReadTime(const Name: string): TDateTime;
function RegistryConnect(const UNCName: string): Boolean;
procedure RenameValue(const OldName: string; const NewName: string);
function ReplaceKey(const Key: string; const FileName: string; const BackUpFileName: string): Boolean;
function RestoreKey(const Key: string; const FileName: string): Boolean;
function SaveKey(const Key: string; const FileName: string): Boolean;
function UnLoadKey(const Key: string): Boolean;
function ValueExists(const Name: string): Boolean;
procedure WriteBinaryData(const Name: string; var Buffer: string; BufSize: Integer);
procedure WriteBool(const Name: string; Value: Boolean);
procedure WriteCurrency(const Name: string; Value: Currency);
procedure WriteDate(const Name: string; Value: TDateTime);
procedure WriteDateTime(const Name: string; Value: TDateTime);
procedure WriteExpandString(const Name: string; const Value: string);
procedure WriteFloat(const Name: string; Value: Double);
procedure WriteInteger(const Name: string; Value: Integer);
procedure WriteString(const Name: string; const Value: string);
procedure WriteTime(const Name: string; Value: TDateTime);

## TRegistryIniFile
继承：TRegistryIniFile → TCustomIniFile → TObject ｜ 单元：System.Win.Registry

property RegIniFile: TRegIniFile;  // read-only
procedure Create(const FileName: string);

## TReplaceDialog
继承：TReplaceDialog → TFindDialog → TCommonDialog → TComponent → TPersistent → TObject ｜ 单元：Vcl.Dialogs

property OnReplace: TNotifyEvent;
property ReplaceText: string;

## TResourceStream
继承：TResourceStream → TCustomMemoryStream → TStream → TObject ｜ 单元：System.Classes

procedure Create(Instance: NativeUInt; const ResName: string; ResType: PWideChar);
procedure CreateFromID(Instance: NativeUInt; ResID: Integer; ResType: PWideChar);

## TRichEdit
继承：TRichEdit → TCustomRichEdit → TCustomMemo → TCustomEdit → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.ComCtrls

property Align: TAlign;
property Alignment: TAlignment;
property Anchors: TAnchors;
property BevelEdges: TBevelEdges;
property BevelInner: TBevelCut;
property BevelKind: TBevelKind;
property BevelOuter: TBevelCut;
property BevelWidth: TBevelWidth;
property BiDiMode: TBiDiMode;
property BorderStyle: TBorderStyle;
property BorderWidth: TBorderWidth;
property Color: TColor;
property Constraints: TSizeConstraints;
property Ctl3D: Boolean;
property DragCursor: TCursor;
property DragKind: TDragKind;
property DragMode: TDragMode;
property Enabled: Boolean;
property Font: TFont;
property HideScrollBars: Boolean;
property HideSelection: Boolean;
property ImeMode: TImeMode;
property ImeName: TImeName;
property Lines: TStrings;
property MaxLength: Integer;
property OnChange: TNotifyEvent;
property OnClick: TNotifyEvent;
property OnContextPopup: TContextPopupEvent;
property OnDblClick: TNotifyEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnEndDock: TEndDragEvent;
property OnEndDrag: TEndDragEvent;
property OnEnter: TNotifyEvent;
property OnExit: TNotifyEvent;
property OnGesture: TGestureEvent;
property OnKeyDown: TKeyEvent;
property OnKeyPress: TKeyPressEvent;
property OnKeyUp: TKeyEvent;
property OnMouseActivate: TMouseActivateEvent;
property OnMouseDown: TMouseEvent;
property OnMouseEnter: TNotifyEvent;
property OnMouseLeave: TNotifyEvent;
property OnMouseMove: TMouseMoveEvent;
property OnMouseUp: TMouseEvent;
property OnMouseWheel: TMouseWheelEvent;
property OnMouseWheelDown: TMouseWheelUpDownEvent;
property OnMouseWheelUp: TMouseWheelUpDownEvent;
property OnProtectChange: TRichEditProtectChange;
property OnResizeRequest: TRichEditResizeEvent;
property OnSaveClipboard: TRichEditSaveClipboard;
property OnSelectionChange: TNotifyEvent;
property OnStartDock: TStartDockEvent;
property OnStartDrag: TStartDragEvent;
property ParentBiDiMode: Boolean;
property ParentColor: Boolean;
property ParentCtl3D: Boolean;
property ParentFont: Boolean;
property ParentShowHint: Boolean;
property PlainText: Boolean;
property PopupMenu: TPopupMenu;
property ReadOnly: Boolean;
property ScrollBars: TScrollStyle;
property ShowHint: Boolean;
property StyleElements: TStyleElements;
property TabOrder: TTabOrder;
property TabStop: Boolean;
property Touch: TTouchManager;
property Visible: Boolean;
property WantReturns: Boolean;
property WantTabs: Boolean;
property WordWrap: Boolean;
property Zoom: Integer;

## TRichEditStyleHook
继承：TRichEditStyleHook → TScrollingStyleHook → TMouseTrackControlStyleHook ｜ 单元：Vcl.ComCtrls


## TRowCollection
继承：TRowCollection → TCellCollection → TOwnedCollection → TCollection → TPersistent → TObject ｜ 单元：Vcl.ExtCtrls

function Add: TRowItem;
procedure Create(AOwner: TPersistent);

## TRowItem
继承：TRowItem → TCellItem → TCollectionItem → TPersistent → TObject ｜ 单元：Vcl.ExtCtrls


## TSaveDialog
继承：TSaveDialog → TOpenDialog → TCommonDialog → TComponent → TPersistent → TObject ｜ 单元：Vcl.Dialogs


## TSavePictureDialog
继承：TSavePictureDialog → TOpenPictureDialog → TOpenDialog → TCommonDialog → TComponent → TPersistent → TObject ｜ 单元：Vcl.ExtDlgs


## TSaveTextFileDialog
继承：TSaveTextFileDialog → TOpenTextFileDialog → TOpenDialog → TCommonDialog → TComponent → TPersistent → TObject ｜ 单元：Vcl.ExtDlgs


## TScreen
继承：TScreen → TComponent → TPersistent → TObject ｜ 单元：Vcl.Forms

property ActiveControl: TWinControl;  // read-only
property ActiveCustomForm: TCustomForm;  // read-only
property ActiveForm: TForm;  // read-only
property CaptionFont: TFont;
property Cursor: TCursor;
property CursorCount: Integer;  // read-only
property Cursors[Index: ?]: HCURSOR;
property CustomFormCount: Integer;  // read-only
property CustomForms[Index: ?]: TCustomForm;  // read-only
property DataModuleCount: Integer;  // read-only
property DataModules[Index: ?]: TDataModule;  // read-only
property DefaultIme: String;  // read-only
property DefaultKbLayout: HKL;  // read-only
property DesktopHeight: Integer;  // read-only
property DesktopLeft: Integer;  // read-only
property DesktopRect: TRect;  // read-only
property DesktopTop: Integer;  // read-only
property DesktopWidth: Integer;  // read-only
property FocusedForm: TCustomForm;
property Fonts: TStrings;  // read-only
property FormCount: Integer;  // read-only
property Forms[Index: ?]: TForm;  // read-only
property Height: Integer;  // read-only
property HintFont: TFont;
property IconFont: TFont;
property Imes: TStrings;  // read-only
property MenuFont: TFont;
property MessageFont: TFont;
property MonitorCount: Integer;  // read-only
property Monitors[Index: ?]: TMonitor;  // read-only
property PixelsPerInch: Integer;  // read-only
property PrimaryMonitor: TMonitor;  // read-only
property SaveFocusedList: TList;  // read-only
property Width: Integer;  // read-only
property WorkAreaHeight: Integer;  // read-only
property WorkAreaLeft: Integer;  // read-only
property WorkareaRect: TRect;  // read-only
property WorkAreaTop: Integer;  // read-only
property WorkAreaWidth: Integer;  // read-only
procedure DisableAlign;
procedure EnableAlign;
function MonitorFromPoint(const Point: IDispatch; MonitorDefault: TMonitorDefaultTo): TMonitor;
function MonitorFromRect(const Rect: IDispatch; MonitorDefault: TMonitorDefaultTo): TMonitor;
function MonitorFromWindow(const Handle: NativeUInt; MonitorDefault: TMonitorDefaultTo): TMonitor;
procedure Realign;
procedure ResetFonts;

## TScrollBar
继承：TScrollBar → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.StdCtrls

property Align: TAlign;
property Anchors: TAnchors;
property BiDiMode: TBiDiMode;
property Constraints: TSizeConstraints;
property Ctl3D: Boolean;
property DoubleBuffered: Boolean;
property DragCursor: TCursor;
property DragKind: TDragKind;
property DragMode: TDragMode;
property Enabled: Boolean;
property Kind: TScrollBarKind;
property LargeChange: TScrollBarInc;
property Max: Integer;
property Min: Integer;
property OnChange: TNotifyEvent;
property OnContextPopup: TContextPopupEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnEndDock: TEndDragEvent;
property OnEndDrag: TEndDragEvent;
property OnEnter: TNotifyEvent;
property OnExit: TNotifyEvent;
property OnKeyDown: TKeyEvent;
property OnKeyPress: TKeyPressEvent;
property OnKeyUp: TKeyEvent;
property OnMouseEnter: TNotifyEvent;
property OnMouseLeave: TNotifyEvent;
property OnScroll: TScrollEvent;
property OnStartDock: TStartDockEvent;
property OnStartDrag: TStartDragEvent;
property PageSize: Integer;
property ParentBiDiMode: Boolean;
property ParentCtl3D: Boolean;
property ParentDoubleBuffered: Boolean;
property ParentShowHint: Boolean;
property PopupMenu: TPopupMenu;
property Position: Integer;
property ShowHint: Boolean;
property SmallChange: TScrollBarInc;
property StyleElements: TStyleElements;
property TabOrder: TTabOrder;
property TabStop: Boolean;
property Visible: Boolean;
procedure Change;
procedure Scroll(ScrollCode: TScrollCode; var ScrollPos: Integer);
procedure SetParams(APosition: Integer; AMin: Integer; AMax: Integer);

## TScrollBarStyleHook
继承：TScrollBarStyleHook → TMouseTrackControlStyleHook → TMouseTrackControlStyleHook ｜ 单元：Vcl.StdCtrls


## TScrollBarStyleHook.TScrollWindow
继承：TScrollBarStyleHook.TScrollWindow → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.StdCtrls

property SizeBox: Boolean;
property StyleHook: TScrollBarStyleHook;
property Vertical: Boolean;

## TScrollBox
继承：TScrollBox → TScrollingWinControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.Forms

property Align: TAlign;
property Anchors: TAnchors;
property AutoScroll: Boolean;
property AutoSize: Boolean;
property BevelEdges: TBevelEdges;
property BevelInner: TBevelCut;
property BevelKind: TBevelKind;
property BevelOuter: TBevelCut;
property BevelWidth: TBevelWidth;
property BiDiMode: TBiDiMode;
property BorderStyle: TBorderStyle;
property Color: TColor;
property Constraints: TSizeConstraints;
property Ctl3D: Boolean;
property DockSite: Boolean;
property DoubleBuffered: Boolean;
property DragCursor: TCursor;
property DragKind: TDragKind;
property DragMode: TDragMode;
property Enabled: Boolean;
property Font: TFont;
property OnCanResize: TCanResizeEvent;
property OnClick: TNotifyEvent;
property OnConstrainedResize: TConstrainedResizeEvent;
property OnContextPopup: TContextPopupEvent;
property OnDblClick: TNotifyEvent;
property OnDockDrop: TDockDropEvent;
property OnDockOver: TDockOverEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnEndDock: TEndDragEvent;
property OnEndDrag: TEndDragEvent;
property OnEnter: TNotifyEvent;
property OnExit: TNotifyEvent;
property OnGesture: TGestureEvent;
property OnGetSiteInfo: TGetSiteInfoEvent;
property OnMouseActivate: TMouseActivateEvent;
property OnMouseDown: TMouseEvent;
property OnMouseEnter: TNotifyEvent;
property OnMouseLeave: TNotifyEvent;
property OnMouseMove: TMouseMoveEvent;
property OnMouseUp: TMouseEvent;
property OnMouseWheel: TMouseWheelEvent;
property OnMouseWheelDown: TMouseWheelUpDownEvent;
property OnMouseWheelUp: TMouseWheelUpDownEvent;
property OnResize: TNotifyEvent;
property OnStartDock: TStartDockEvent;
property OnStartDrag: TStartDragEvent;
property OnUnDock: TUnDockEvent;
property Padding: TPadding;
property ParentBackground: Boolean;
property ParentBiDiMode: Boolean;
property ParentColor: Boolean;
property ParentCtl3D: Boolean;
property ParentDoubleBuffered: Boolean;
property ParentFont: Boolean;
property ParentShowHint: Boolean;
property PopupMenu: TPopupMenu;
property ShowHint: Boolean;
property StyleElements: TStyleElements;
property TabOrder: TTabOrder;
property TabStop: Boolean;
property Touch: TTouchManager;
property Visible: Boolean;

## TScrollBoxStyleHook
继承：TScrollBoxStyleHook → TScrollingStyleHook → TMouseTrackControlStyleHook ｜ 单元：Vcl.Forms


## TScroller
继承：TScroller → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.Tabs

property Change: Integer;
property Max: Integer;
property Min: Integer;
property OnClick: TNotifyEvent;
property Position: Integer;
property ScrollOrientation: TScrollOrientation;

## TScrollingStyleHook
继承：TScrollingStyleHook → TMouseTrackControlStyleHook → TMouseTrackControlStyleHook ｜ 单元：Vcl.Forms


## TScrollingWinControl
继承：TScrollingWinControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.Forms

property HorzScrollBar: TControlScrollBar;
property OnAlignInsertBefore: TAlignInsertBeforeEvent;
property OnAlignPosition: TAlignPositionEvent;
property VertScrollBar: TControlScrollBar;
function AutoScrollEnabled: Boolean;
procedure AutoScrollInView(AControl: TControl);
procedure DisableAutoRange;
procedure EnableAutoRange;
procedure Resizing(State: TWindowState);
procedure ScrollInView(AControl: TControl);

## TSearchAction
继承：TSearchAction → TCommonDialogAction → TCustomAction → TContainedAction ｜ 单元：Vcl.StdActns

procedure Search(Sender: TObject);

## TSearchByKeywordArgs
继承：TSearchByKeywordArgs → TObject ｜ 单元：RT_Supplier

field Category;
field Keywords;
field ParametricFilters;
field RecordCount;
field SearchFilters;
field StartRecord;

## TSearchByManufacturerPartNumberArgs
继承：TSearchByManufacturerPartNumberArgs → TObject ｜ 单元：RT_Supplier

field ManufacturerPartNumber;

## TSearchBySupplierPartNumberArgs
继承：TSearchBySupplierPartNumberArgs → TObject ｜ 单元：RT_Supplier

field PartNumber;
field SkipOptions;

## TSearchFind
继承：TSearchFind → TSearchAction → TCommonDialogAction → TCustomAction → TContainedAction ｜ 单元：Vcl.StdActns

property BeforeExecute: TNotifyEvent;
property Caption: string;
property Dialog: TFindDialog;  // read-only
property Enabled: Boolean;
property HelpContext: THelpContext;
property HelpKeyword: string;
property HelpType: THelpType;
property Hint: string;
property ImageIndex: TImageIndex;
property OnAccept: TNotifyEvent;
property OnCancel: TNotifyEvent;
property OnHint: THintEvent;
property OnUpdate: TNotifyEvent;
property SecondaryShortCuts: TCustomShortCutList;
property ShortCut: TShortCut;
property Visible: Boolean;

## TSearchFindFirst
继承：TSearchFindFirst → TSearchFind → TSearchAction → TCommonDialogAction → TCustomAction → TContainedAction ｜ 单元：Vcl.StdActns


## TSearchFindNext
继承：TSearchFindNext → TCustomAction → TContainedAction ｜ 单元：Vcl.StdActns

property Caption: string;
property Enabled: Boolean;
property HelpContext: THelpContext;
property HelpKeyword: string;
property HelpType: THelpType;
property Hint: string;
property ImageIndex: TImageIndex;
property OnHint: THintEvent;
property OnUpdate: TNotifyEvent;
property SearchFind: TSearchFind;
property SecondaryShortCuts: TCustomShortCutList;
property ShortCut: TShortCut;
property Visible: Boolean;

## TSearchReplace
继承：TSearchReplace → TSearchAction → TCommonDialogAction → TCustomAction → TContainedAction ｜ 单元：Vcl.StdActns

property BeforeExecute: TNotifyEvent;
property Caption: string;
property Dialog: TReplaceDialog;  // read-only
property Enabled: Boolean;
property HelpContext: THelpContext;
property HelpKeyword: string;
property HelpType: THelpType;
property Hint: string;
property ImageIndex: TImageIndex;
property OnAccept: TNotifyEvent;
property OnCancel: TNotifyEvent;
property OnHint: THintEvent;
property OnUpdate: TNotifyEvent;
property SecondaryShortCuts: TCustomShortCutList;
property ShortCut: TShortCut;
property Visible: Boolean;

## TServerExternalFormComponent
继承：TServerExternalFormComponent → TExternalFormComponent → TPanel → TCustomPanel → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：ExternalForm


## TServerExternalFormComponentRefCount
继承：TServerExternalFormComponentRefCount → TExternalFormComponentRefCount → TExternalFormComponent → TPanel → TCustomPanel → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：ExternalForm


## TServerModel
继承：TServerModel → TDispatchObject → TDispatchObject ｜ 单元：RT_IntegratedLibrary

procedure Create(AName: string; ACheckSchPins: Boolean; ACheckModelPins: Boolean);

## TServerModel2
继承：TServerModel2 → TServerModel → TDispatchObject ｜ 单元：RT_IntegratedLibrary


## TShape
继承：TShape → TGraphicControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.ExtCtrls

property Align: TAlign;
property Anchors: TAnchors;
property Brush: TBrush;
property Constraints: TSizeConstraints;
property DragCursor: TCursor;
property DragKind: TDragKind;
property DragMode: TDragMode;
property Enabled: Boolean;
property OnContextPopup: TContextPopupEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnEndDock: TEndDragEvent;
property OnEndDrag: TEndDragEvent;
property OnGesture: TGestureEvent;
property OnMouseActivate: TMouseActivateEvent;
property OnMouseDown: TMouseEvent;
property OnMouseEnter: TNotifyEvent;
property OnMouseLeave: TNotifyEvent;
property OnMouseMove: TMouseMoveEvent;
property OnMouseUp: TMouseEvent;
property OnStartDock: TStartDockEvent;
property OnStartDrag: TStartDragEvent;
property ParentShowHint: Boolean;
property Pen: TPen;
property Shape: TShapeType;
property ShowHint: Boolean;
property Touch: TTouchManager;
property Visible: Boolean;
procedure StyleChanged(Sender: TObject);

## TSharedImage
继承：TSharedImage → TObject ｜ 单元：Vcl.Graphics

procedure FreeHandle;

## TShortCutList
继承：TShortCutList → TCustomShortCutList → TCustomShortCutList ｜ 单元：Vcl.ActnList


## TShortintField
继承：TShortintField → TIntegerField → TNumericField → TField → TComponent → TPersistent → TObject ｜ 单元：Data.DB


## TSignalLinkManager
继承：TSignalLinkManager → TComponent → TPersistent → TObject ｜ 单元：RT_Digital_IO

property AutoPolling: Boolean;
property OnPoll: TNotifyEvent;
property PollingInterval: Cardinal;
property SignalLinkCount: Integer;  // read-only
property SignalLinks[Index: ?]: TIOSignalLink;  // read-only
procedure ClearSignalLinks;
procedure DoPoll;
procedure UpdateSignals(AInput: LongBool; AOutput: LongBool);

## TSimpleRWSync
继承：TSimpleRWSync → TInterfacedObject → TObject ｜ 单元：System.SysUtils ｜ 未在类列表里注册，只能通过实例访问

procedure BeginRead;
function BeginWrite: Boolean;
procedure Create;
procedure EndRead;
procedure EndWrite;

## TSingleField
继承：TSingleField → TNumericField → TField → TComponent → TPersistent → TObject ｜ 单元：Data.DB

property currency: Boolean;
property MaxValue: Single;
property MinValue: Single;
property Precision: Integer;
property Value: Single;

## TSizeConstraints
继承：TSizeConstraints → TPersistent → TObject ｜ 单元：Vcl.Controls

property MaxHeight: TConstraintSize;
property MaxWidth: TConstraintSize;
property MinHeight: TConstraintSize;
property MinWidth: TConstraintSize;
procedure Change;
procedure Create(Control: TControl);

## TSmallintField
继承：TSmallintField → TIntegerField → TNumericField → TField → TComponent → TPersistent → TObject ｜ 单元：Data.DB


## TSoftDesignNotification
继承：TSoftDesignNotification → TNotificationWithCode → TInterfacedObject → TObject ｜ 单元：RT_ClientServerInterface

procedure AddBoardUniqueId(ABoardUniqueId: WideString);
procedure AddFirmwareVersion(AFirmwareVersion: WideString);
procedure Create(ACode: Integer);
function GetBoardUniqueIdCount: Integer;
function GetBoardUniqueIds(AIndex: Integer): WideString;
function GetFirmwareVersions(AIndex: Integer): WideString;

## TSpeedButton
继承：TSpeedButton → TGraphicControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.Buttons

property Action: TBasicAction;
property Align: TAlign;
property AllowAllUp: Boolean;
property Anchors: TAnchors;
property BiDiMode: TBiDiMode;
property Caption: TCaption;
property Constraints: TSizeConstraints;
property Down: Boolean;
property Enabled: Boolean;
property Flat: Boolean;
property Font: TFont;
property Glyph: TBitmap;
property GroupIndex: Integer;
property Layout: TButtonLayout;
property Margin: Integer;
property NumGlyphs: TNumGlyphs;
property OnClick: TNotifyEvent;
property OnDblClick: TNotifyEvent;
property OnMouseActivate: TMouseActivateEvent;
property OnMouseDown: TMouseEvent;
property OnMouseEnter: TNotifyEvent;
property OnMouseLeave: TNotifyEvent;
property OnMouseMove: TMouseMoveEvent;
property OnMouseUp: TMouseEvent;
property ParentBiDiMode: Boolean;
property ParentFont: Boolean;
property ParentShowHint: Boolean;
property PopupMenu: TPopupMenu;
property ShowHint: Boolean;
property Spacing: Integer;
property StyleElements: TStyleElements;
property Transparent: Boolean;
property Visible: Boolean;

## TSpeedButtonActionLink
继承：TSpeedButtonActionLink → TControlActionLink → TActionLink → TContainedActionLink ｜ 单元：Vcl.Buttons

function IsGlyphLinked(Index: TImageIndex): Boolean;

## TSplitter
继承：TSplitter → TGraphicControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.ExtCtrls

property Align: TAlign;
property AutoSnap: Boolean;
property Beveled: Boolean;
property Canvas: TCanvas;  // read-only
property Color: TColor;
property Constraints: TSizeConstraints;
property Cursor: TCursor;
property MinSize: NaturalNumber;
property OnCanResize: TSplitterCanResizeEvent;
property OnMoved: TNotifyEvent;
property OnPaint: TNotifyEvent;
property ParentColor: Boolean;
property ResizeStyle: TResizeStyle;
property StyleElements: TStyleElements;
property Visible: Boolean;
property Width: Integer;
function CanResize(var NewSize: Integer): Boolean;
function DoCanResize(var NewSize: Integer): Boolean;
procedure StopSizing;

## TSQLTimeStampField
继承：TSQLTimeStampField → TField → TComponent → TPersistent → TObject ｜ 单元：Data.DB

property DisplayFormat: string;
property EditMask: TEditMask;
property Value: TSQLTimeStamp;

## TSQLTimeStampOffsetField
继承：TSQLTimeStampOffsetField → TSQLTimeStampField → TField → TComponent → TPersistent → TObject ｜ 单元：Data.DB

property Value: TSQLTimeStampOffset;

## TStack
继承：TStack → TOrderedList → TObject ｜ 单元：System.Contnrs


## TStaticText
继承：TStaticText → TCustomStaticText → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.StdCtrls

property Align: TAlign;
property Alignment: TAlignment;
property Anchors: TAnchors;
property AutoSize: Boolean;
property BevelEdges: TBevelEdges;
property BevelInner: TBevelCut;
property BevelKind: TBevelKind;
property BevelOuter: TBevelCut;
property BiDiMode: TBiDiMode;
property BorderStyle: TStaticBorderStyle;
property Caption: TCaption;
property Color: TColor;
property Constraints: TSizeConstraints;
property DoubleBuffered: Boolean;
property DragCursor: TCursor;
property DragKind: TDragKind;
property DragMode: TDragMode;
property Enabled: Boolean;
property FocusControl: TWinControl;
property Font: TFont;
property OnClick: TNotifyEvent;
property OnContextPopup: TContextPopupEvent;
property OnDblClick: TNotifyEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnEndDock: TEndDragEvent;
property OnEndDrag: TEndDragEvent;
property OnGesture: TGestureEvent;
property OnMouseActivate: TMouseActivateEvent;
property OnMouseDown: TMouseEvent;
property OnMouseEnter: TNotifyEvent;
property OnMouseLeave: TNotifyEvent;
property OnMouseMove: TMouseMoveEvent;
property OnMouseUp: TMouseEvent;
property OnStartDock: TStartDockEvent;
property OnStartDrag: TStartDragEvent;
property ParentBiDiMode: Boolean;
property ParentColor: Boolean;
property ParentDoubleBuffered: Boolean;
property ParentFont: Boolean;
property ParentShowHint: Boolean;
property PopupMenu: TPopupMenu;
property ShowAccelChar: Boolean;
property ShowHint: Boolean;
property StyleElements: TStyleElements;
property TabOrder: TTabOrder;
property TabStop: Boolean;
property Touch: TTouchManager;
property Transparent: Boolean;
property Visible: Boolean;

## TStaticTextStyleHook
继承：TStaticTextStyleHook → TStyleHook → TStyleHook ｜ 单元：Vcl.StdCtrls


## TStatusBar
继承：TStatusBar → TCustomStatusBar → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.ComCtrls

property Action: TBasicAction;
property Align: TAlign;
property Anchors: TAnchors;
property AutoHint: Boolean;
property BiDiMode: TBiDiMode;
property BorderWidth: TBorderWidth;
property Color: TColor;
property Constraints: TSizeConstraints;
property DoubleBuffered: Boolean;
property DragCursor: TCursor;
property DragKind: TDragKind;
property DragMode: TDragMode;
property Enabled: Boolean;
property Font: TFont;
property OnClick: TNotifyEvent;
property OnContextPopup: TContextPopupEvent;
property OnCreatePanelClass: TSBCreatePanelClassEvent;
property OnDblClick: TNotifyEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnDrawPanel: TDrawPanelEvent;
property OnEndDock: TEndDragEvent;
property OnEndDrag: TEndDragEvent;
property OnGesture: TGestureEvent;
property OnHint: TNotifyEvent;
property OnMouseActivate: TMouseActivateEvent;
property OnMouseDown: TMouseEvent;
property OnMouseEnter: TNotifyEvent;
property OnMouseLeave: TNotifyEvent;
property OnMouseMove: TMouseMoveEvent;
property OnMouseUp: TMouseEvent;
property OnResize: TNotifyEvent;
property OnStartDock: TStartDockEvent;
property OnStartDrag: TStartDragEvent;
property Panels: TStatusPanels;
property ParentBiDiMode: Boolean;
property ParentColor: Boolean;
property ParentDoubleBuffered: Boolean;
property ParentFont: Boolean;
property ParentShowHint: Boolean;
property PopupMenu: TPopupMenu;
property ShowHint: Boolean;
property SimplePanel: Boolean;
property SimpleText: string;
property SizeGrip: Boolean;
property StyleElements: TStyleElements;
property Touch: TTouchManager;
property UseSystemFont: Boolean;
property Visible: Boolean;

## TStatusBarStyleHook
继承：TStatusBarStyleHook → TStyleHook → TStyleHook ｜ 单元：Vcl.ComCtrls


## TStatusPanel
继承：TStatusPanel → TCollectionItem → TPersistent → TObject ｜ 单元：Vcl.ComCtrls

property Alignment: TAlignment;
property Bevel: TStatusPanelBevel;
property BiDiMode: TBiDiMode;
property ParentBiDiMode: Boolean;
property Style: TStatusPanelStyle;
property Text: string;
property Width: Integer;
procedure ParentBiDiModeChanged;
function UseRightToLeftAlignment: Boolean;
function UseRightToLeftReading: Boolean;

## TStatusPanels
继承：TStatusPanels → TCollection → TPersistent → TObject ｜ 单元：Vcl.ComCtrls

property Items[Index: ?]: TStatusPanel;
function Add: TStatusPanel;
function AddItem(Item: TStatusPanel; Index: Integer): TStatusPanel;
procedure Create(StatusBar: TCustomStatusBar);
function Insert(Index: Integer): TStatusPanel;

## TStream
继承：TStream → TObject ｜ 单元：System.Classes

property Position: Int64;
property Size: Int64;
function CopyFrom(const Source: TStream; Count: Int64): Int64;
procedure FixupResourceHeader(FixupInfo: Integer);
function GetSize: Int64;
function Read(var Buffer; Count: Integer): Integer;
procedure ReadBuffer(var Buffer; Count: Integer);
procedure ReadBufferData(var Buffer: Boolean);
function ReadComponent(const Instance: TComponent): TComponent;
function ReadComponentRes(const Instance: TComponent): TComponent;
function ReadData(Buffer: Pointer; Count: Integer): Integer;
procedure ReadResHeader;
function Seek(Offset: Integer; Origin: Word): Integer;
procedure SetSize(NewSize: Integer);
function Write(const Buffer; Count: Integer): Integer;
procedure WriteBuffer(const Buffer; Count: Integer);
procedure WriteBufferData(var Buffer: Integer; Count: Integer);
procedure WriteComponent(const Instance: TComponent);
procedure WriteComponentRes(const ResName: string; const Instance: TComponent);
function WriteData(const Buffer: TArray<System.Byte>; Count: Integer): Integer;
procedure WriteDescendent(const Instance: TComponent; const Ancestor: TComponent);
procedure WriteDescendentRes(const ResName: string; const Instance: TComponent; const Ancestor: TComponent);
procedure WriteResourceHeader(const ResName: string; out FixupInfo: Integer);

## TStreamAdapter
继承：TStreamAdapter → TInterfacedObject → TObject ｜ 单元：System.Classes

property Stream: TStream;  // read-only
property StreamOwnership: TStreamOwnership;
function Clone(out stm: IStream): HRESULT;
function Commit(grfCommitFlags: Cardinal): HRESULT;
function CopyTo(stm: IStream; cb: UInt64; out cbRead: UInt64; out cbWritten: UInt64): HRESULT;
procedure Create(Stream: TStream; Ownership: TStreamOwnership);
function LockRegion(libOffset: UInt64; cb: UInt64; dwLockType: Cardinal): HRESULT;
function Read(pv: Pointer; cb: Cardinal; pcbRead: PFixedUInt): HRESULT;
function Revert: HRESULT;
function Seek(dlibMove: Int64; dwOrigin: Cardinal; out libNewPosition: UInt64): HRESULT;
function SetSize(libNewSize: UInt64): HRESULT;
function UnlockRegion(libOffset: UInt64; cb: UInt64; dwLockType: Cardinal): HRESULT;
function Write(pv: Pointer; cb: Cardinal; pcbWritten: PFixedUInt): HRESULT;

## TStreamReader
继承：TStreamReader → TTextReader → TObject ｜ 单元：System.Classes

property BaseStream: TStream;  // read-only
property CurrentEncoding: TEncoding;  // read-only
property EndOfStream: Boolean;  // read-only
procedure Create(Stream: TStream);
procedure DiscardBufferedData;
procedure OwnStream;

## TStreamWriter
继承：TStreamWriter → TTextWriter → TObject ｜ 单元：System.Classes

property AutoFlush: Boolean;
property BaseStream: TStream;  // read-only
property Encoding: TEncoding;  // read-only
property NewLine: String;
procedure Create(Stream: TStream);
procedure OwnStream;

## TStringBuilder
继承：TStringBuilder → TObject ｜ 单元：System.SysUtils ｜ 未在类列表里注册，只能通过实例访问

property Capacity: Integer;
property Chars[Index: ?]: Char;
property Length: Integer;
property MaxCapacity: Integer;  // read-only
function Append(const Value: Boolean): TStringBuilder;
function AppendFormat(const Format: string; const Args: array of TVarRec): TStringBuilder;
function AppendLine: TStringBuilder;
procedure Clear;
procedure CopyTo(SourceIndex: Integer; const Destination: TArray<System.Char>; DestinationIndex: Integer; Count: Integer);
procedure Create;
function EnsureCapacity(aCapacity: Integer): Integer;
function Equals(StringBuilder: TStringBuilder): Boolean;
function Insert(Index: Integer; const Value: Boolean): TStringBuilder;
function Remove(StartIndex: Integer; RemLength: Integer): TStringBuilder;
function Replace(const OldChar: Char; const NewChar: Char): TStringBuilder;
function ToString(StartIndex: Integer; StrLength: Integer): string;

## TStringField
继承：TStringField → TField → TComponent → TPersistent → TObject ｜ 单元：Data.DB

property EditMask: TEditMask;
property FixedChar: Boolean;
property Size: Integer;
property Transliterate: Boolean;
property Value: AnsiString;

## TStringGrid
继承：TStringGrid → TDrawGrid → TCustomDrawGrid → TCustomGrid → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.Grids

property Cells[Index1: ?, Index2: ?]: String;
property Cols[Index: ?]: TStrings;
property Objects[Index1: ?, Index2: ?]: TObject;
property Rows[Index: ?]: TStrings;

## TStringGridStrings
继承：TStringGridStrings → TStrings → TPersistent → TObject ｜ 单元：Vcl.Grids

procedure Create(AGrid: TStringGrid; AIndex: Integer);

## TStringHash
继承：TStringHash → TObject ｜ 单元：System.IniFiles

procedure Add(const Key: string; Value: Integer);
procedure Clear;
procedure Create(Size: Cardinal);
function HashOf(const Key: string): Cardinal;
function Modify(const Key: string; Value: Integer): Boolean;
procedure Remove(const Key: string);
function ValueOf(const Key: string): Integer;

## TStringList
继承：TStringList → TStrings → TPersistent → TObject ｜ 单元：System.Classes

property CaseSensitive: Boolean;
property Duplicates: TDuplicates;
property OwnsObjects: Boolean;
property Sorted: Boolean;
procedure Changed;
procedure Changing;
procedure Create;
function Find(const S: string; var Index: Integer): Boolean;
procedure InsertItem(Index: Integer; const S: string; AObject: TObject);
procedure Sort;

## TStringReader
继承：TStringReader → TTextReader → TObject ｜ 单元：System.Classes

procedure Create(S: string);

## TStrings
继承：TStrings → TPersistent → TObject ｜ 单元：System.Classes

property Capacity: Integer;
property CommaText: String;
property Count: Integer;  // read-only
property DefaultEncoding: TEncoding;
property DelimitedText: String;
property Delimiter: Char;
property Encoding: TEncoding;  // read-only
property LineBreak: String;
property Names[Index: ?]: String;  // read-only
property NameValueSeparator: Char;
property Objects[Index: ?]: TObject;
property QuoteChar: Char;
property StrictDelimiter: Boolean;
property Strings[Index: ?]: String;
property StringsAdapter: IStringsAdapter;
property Text: String;
property ValueFromIndex[Index: ?]: String;
property Values[Index: ?]: String;
property WriteBOM: Boolean;
function Add(const S: string): Integer;
function AddObject(const S: string; AObject: TObject): Integer;
procedure AddStrings(Strings: TStrings);
procedure Append(const S: string);
procedure BeginUpdate;
procedure Clear;
function CompareStrings(const S1: string; const S2: string): Integer;
procedure Create;
procedure Delete(Index: Integer);
procedure EndUpdate;
function Equals(Strings: TStrings): Boolean;
procedure Exchange(Index1: Integer; Index2: Integer);
function Get(Index: Integer): string;
function GetCapacity: Integer;
function GetCount: Integer;
function GetEnumerator: TStringsEnumerator;
function GetObject(Index: Integer): TObject;
function GetText: PWideChar;
function GetTextStr: string;
function IndexOf(const S: string): Integer;
function IndexOfName(const Name: string): Integer;
function IndexOfObject(AObject: TObject): Integer;
procedure Insert(Index: Integer; const S: string);
procedure InsertObject(Index: Integer; const S: string; AObject: TObject);
procedure LoadFromFile(const FileName: string);
procedure LoadFromStream(Stream: TStream);
procedure Move(CurIndex: Integer; NewIndex: Integer);
procedure Put(Index: Integer; const S: string);
procedure PutObject(Index: Integer; AObject: TObject);
procedure SaveToFile(const FileName: string);
procedure SaveToStream(Stream: TStream);
procedure SetCapacity(NewCapacity: Integer);
procedure SetEncoding(const Value: TEncoding);
procedure SetText(Text: PWideChar);
procedure SetTextStr(const Value: string);
procedure SetUpdateState(Updating: Boolean);
function ToObjectArray: TArray<System.TObject>;
function ToStringArray: TArray<System.string>;

## TStringsAdapter
继承：TStringsAdapter → TDispatchObject → TDispatchObject ｜ 单元：RT_Workspace

procedure Create(AStrings: TStrings);

## TStringsEnumerator
继承：TStringsEnumerator → TObject ｜ 单元：System.Classes

property Current: String;  // read-only
procedure Create(AStrings: TStrings);
function GetCurrent: string;
function MoveNext: Boolean;

## TStringStream
继承：TStringStream → TBytesStream → TMemoryStream → TCustomMemoryStream → TStream → TObject ｜ 单元：System.Classes

property DataString: String;  // read-only
property Encoding: TEncoding;  // read-only
procedure Create;
function ReadString(Count: Integer): string;
procedure WriteString(const AString: string);

## TStringWriter
继承：TStringWriter → TTextWriter → TObject ｜ 单元：System.Classes

procedure Create;

## TSupplierCategory
继承：TSupplierCategory → TInterfacedObject → TObject ｜ 单元：RT_Supplier

procedure Create(ACategoryName: string);

## TSupplierCategoryParameters
继承：TSupplierCategoryParameters → TInterfaceList → TInterfacedObject → TObject ｜ 单元：RT_Supplier

function GetParameterKind(I: Integer): ISupplierParameterKind;

## TSupplierEventsHandler
继承：TSupplierEventsHandler → TObject ｜ 单元：RT_Supplier

property Handle: HWND;  // read-only
procedure Create;
procedure WndMethod(const Msg: IDispatch);

## TSupplierParameter
继承：TSupplierParameter → TDispatchObject → TDispatchObject ｜ 单元：Rt_AltiumLibrary

procedure Create(Name: WideString; Value: WideString);

## TSupplierParameterKind
继承：TSupplierParameterKind → TInterfacedObject → TObject ｜ 单元：RT_Supplier

procedure AddValue(Value: ISupplierParameterValue);
procedure Create;
function GetID: Integer;
function GetName: WideString;
function GetValue(I: Integer): ISupplierParameterValue;
procedure SetID(ID: Integer);
procedure SetName(Name: WideString);
function ValueCount: Integer;

## TSupplierParameterValue
继承：TSupplierParameterValue → TInterfacedObject → TObject ｜ 单元：RT_Supplier

function GetID: Integer;
function GetValue: WideString;
procedure SetID(ID: Integer);
procedure SetValue(Value: WideString);

## TSupplierParametricFilter
继承：TSupplierParametricFilter → TInterfacedObject → TObject ｜ 单元：RT_Supplier

function GetParameterKindID: Integer;
function GetParameterValueID: Integer;
procedure SetParameterKindID(ID: Integer);
procedure SetParameterValueID(ID: Integer);

## TSupplierParametricFilters
继承：TSupplierParametricFilters → TInterfaceList → TInterfacedObject → TObject ｜ 单元：RT_Supplier

function GetFilter(I: Integer): ISupplierParametricFilter;

## TSupplierPreferences
继承：TSupplierPreferences → TObject ｜ 单元：RT_Supplier

procedure Create;
function GetEnterpriseOptions: WideString;
procedure Load(Data: WideString);
procedure LoadFromCustomIni(Ini: TMemIniFile);
procedure LoadFromIni;
procedure LoadFromText(Text: WideString);
procedure Save;
procedure SaveToIni;

## TSupplierSearchError
继承：TSupplierSearchError → TInterfacedObject → TObject ｜ 单元：RT_Supplier

procedure Create(AErrorMessage: WideString; ASupplierName: WideString);
function ErrorMessage: WideString;
function SupplierName: WideString;

## TSupplierSearchResults
继承：TSupplierSearchResults → TInterfaceList → TInterfacedObject → TObject ｜ 单元：RT_Supplier

procedure Create;
function GetSearchError: ISupplierSearchError;
function GetSearchStatistics: ISupplierSearchStatistics;
function GetSourceRelationship(I: Integer): ISupplierSourceRelationship;
procedure SetSearchError(Value: ISupplierSearchError);
procedure SetSearchStatistics(Value: ISupplierSearchStatistics);

## TSupplierSearchStatistics
继承：TSupplierSearchStatistics → TInterfacedObject → TObject ｜ 单元：RT_Supplier

procedure Create(ASupplierName: string);

## TSupplierSourceRelationship
继承：TSupplierSourceRelationship → TAbstractSupplierSourceRelationship → TInterfacedObject → TObject ｜ 单元：RT_Supplier

procedure Create;

## TSupplierSourceRelationshipError
继承：TSupplierSourceRelationshipError → TAbstractSupplierSourceRelationship → TInterfacedObject → TObject ｜ 单元：RT_Supplier

procedure Create(ErrorCode: Integer; SupplierName: string; SupplierPartNumber: string);
function GetState_ErrorCode: Integer;

## TSupplierThread
继承：TSupplierThread → TObject ｜ 单元：RT_Supplier

property SupplierName: WideString;  // read-only
procedure BackgroundGetCategoryParameters(Category: ISupplierCategory; Handle: HWND);
procedure BackgroundSearchByKeyword(Keywords: WideString; RecordCount: Integer; StartRecord: Integer; SearchFilters: TSupplierSearchFilters; Category: ISupplierCategory; ParametricFilters: ISupplierParametricFilters; Handle: HWND);
procedure BackgroundSearchByManufacturerPartNumber(ManufacturerPartNumber: WideString; Handle: HWND);
procedure BackgroundSearchBySupplierPartNumber(SupplierPartNumber: WideString; SkipOptions: TSkipOptionSet; Handle: HWND);
procedure Create(CreateSuspended: Boolean; ASupplierName: WideString);
function GetCategoryParameters(Category: ISupplierCategory; Handle: HWND): ISupplierCategoryParameters;
function SearchByKeyword(Keywords: WideString; RecordCount: Integer; StartRecord: Integer; SearchFilters: TSupplierSearchFilters; Category: ISupplierCategory; ParametricFilters: ISupplierParametricFilters; Handle: HWND): ISupplierSearchResults;
function SearchByManufacturerPartNumber(ManufacturerPartNumber: WideString; Handle: HWND): ISupplierSearchResults;
function SearchBySupplierPartNumber(SupplierPartNumber: WideString; SkipOptions: TSkipOptionSet; Handle: HWND): ISupplierSourceRelationship;

## TSystemNotification
继承：TSystemNotification → TNotificationWithCode → TInterfacedObject → TObject ｜ 单元：RT_ClientServerInterface

procedure Create(ACode: Integer);

## TTabbedNotebook
继承：TTabbedNotebook → TCustomTabControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.TabNotBk

property ActivePage: string;
property Align: TAlign;
property Anchors: TAnchors;
property Constraints: TSizeConstraints;
property DoubleBuffered: Boolean;
property Enabled: Boolean;
property Font: TFont;
property OnChange: TPageChangeEvent;
property OnClick: TNotifyEvent;
property OnContextPopup: TContextPopupEvent;
property OnEnter: TNotifyEvent;
property OnExit: TNotifyEvent;
property OnGesture: TGestureEvent;
property PageIndex: Integer;
property Pages: TStrings;
property ParentDoubleBuffered: Boolean;
property ParentShowHint: Boolean;
property PopupMenu: TPopupMenu;
property ShowHint: Boolean;
property StyleElements: TStyleElements;
property TabFont: TFont;
property TabOrder: TTabOrder;
property TabsPerRow: Integer;
property TabStop: Boolean;
property TopFont: TFont;  // read-only
property Touch: TTouchManager;
property Visible: Boolean;
procedure CMTabFontChanged(const Message: IDispatch);
function GetIndexForPage(const PageName: string): Integer;
procedure TabFontChanged(Sender: TObject);

## TTabControl
继承：TTabControl → TCustomTabControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.ComCtrls

property Align: TAlign;
property Anchors: TAnchors;
property BiDiMode: TBiDiMode;
property Constraints: TSizeConstraints;
property DisplayRect: TRect;  // read-only
property DockSite: Boolean;
property DoubleBuffered: Boolean;
property DragCursor: TCursor;
property DragKind: TDragKind;
property DragMode: TDragMode;
property Enabled: Boolean;
property Font: TFont;
property HotTrack: Boolean;
property Images: TCustomImageList;
property MultiLine: Boolean;
property MultiSelect: Boolean;
property OnChange: TNotifyEvent;
property OnChanging: TTabChangingEvent;
property OnContextPopup: TContextPopupEvent;
property OnDockDrop: TDockDropEvent;
property OnDockOver: TDockOverEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnDrawTab: TDrawTabEvent;
property OnEndDock: TEndDragEvent;
property OnEndDrag: TEndDragEvent;
property OnEnter: TNotifyEvent;
property OnExit: TNotifyEvent;
property OnGesture: TGestureEvent;
property OnGetImageIndex: TTabGetImageEvent;
property OnGetSiteInfo: TGetSiteInfoEvent;
property OnMouseActivate: TMouseActivateEvent;
property OnMouseDown: TMouseEvent;
property OnMouseEnter: TNotifyEvent;
property OnMouseLeave: TNotifyEvent;
property OnMouseMove: TMouseMoveEvent;
property OnMouseUp: TMouseEvent;
property OnResize: TNotifyEvent;
property OnStartDock: TStartDockEvent;
property OnStartDrag: TStartDragEvent;
property OnUnDock: TUnDockEvent;
property OwnerDraw: Boolean;
property ParentBiDiMode: Boolean;
property ParentDoubleBuffered: Boolean;
property ParentFont: Boolean;
property ParentShowHint: Boolean;
property PopupMenu: TPopupMenu;
property RaggedRight: Boolean;
property ScrollOpposite: Boolean;
property ShowHint: Boolean;
property Style: TTabStyle;
property StyleElements: TStyleElements;
property TabHeight: SmallInt;
property TabIndex: Integer;
property TabOrder: TTabOrder;
property TabPosition: TTabPosition;
property Tabs: TStrings;
property TabStop: Boolean;
property TabWidth: SmallInt;
property Touch: TTouchManager;
property Visible: Boolean;

## TTabControlStyleHook
继承：TTabControlStyleHook → TMouseTrackControlStyleHook → TMouseTrackControlStyleHook ｜ 单元：Vcl.ComCtrls


## TTabList
继承：TTabList → TStringList → TStrings → TPersistent → TObject ｜ 单元：Vcl.Tabs

procedure Create(const ATabSet: TTabSet);

## TTabPage
继承：TTabPage → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.TabNotBk

property Caption: TCaption;
property Enabled: Boolean;
property Height: Integer;
property OnGesture: TGestureEvent;
property TabOrder: TTabOrder;
property Touch: TTouchManager;
property Visible: Boolean;
property Width: Integer;

## TTabSet
继承：TTabSet → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.Tabs

property Align: TAlign;
property Anchors: TAnchors;
property AutoScroll: Boolean;
property BackgroundColor: TColor;
property Canvas: TCanvas;  // read-only
property Constraints: TSizeConstraints;
property DitherBackground: Boolean;
property DoubleBuffered: Boolean;
property DragCursor: TCursor;
property DragKind: TDragKind;
property DragMode: TDragMode;
property Enabled: Boolean;
property EndMargin: Integer;
property FirstIndex: Integer;
property Font: TFont;
property Images: TCustomImageList;
property OnAlignInsertBefore: TAlignInsertBeforeEvent;
property OnAlignPosition: TAlignPositionEvent;
property OnChange: TTabChangeEvent;
property OnClick: TNotifyEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnDrawTab: TTabSetDrawTabEvent;
property OnEndDock: TEndDragEvent;
property OnEndDrag: TEndDragEvent;
property OnEnter: TNotifyEvent;
property OnExit: TNotifyEvent;
property OnGesture: TGestureEvent;
property OnGetImageIndex: TTabGetImageEvent;
property OnMeasureTab: TMeasureTabEvent;
property OnMouseActivate: TMouseActivateEvent;
property OnMouseDown: TMouseEvent;
property OnMouseEnter: TNotifyEvent;
property OnMouseLeave: TNotifyEvent;
property OnMouseMove: TMouseMoveEvent;
property OnMouseUp: TMouseEvent;
property OnStartDock: TStartDockEvent;
property OnStartDrag: TStartDragEvent;
property ParentBackground: Boolean;
property ParentDoubleBuffered: Boolean;
property ParentShowHint: Boolean;
property PopupMenu: TPopupMenu;
property SelectedColor: TColor;
property ShowHint: Boolean;
property ShrinkToFit: Boolean;
property SoftTop: Boolean;
property StartMargin: Integer;
property Style: TTabSetTabStyle;
property StyleElements: TStyleElements;
property TabHeight: Integer;
property TabIndex: Integer;
property TabPosition: TTabPosition;
property Tabs: TStrings;
property Touch: TTouchManager;
property UnselectedColor: TColor;
property Visible: Boolean;
property VisibleTabs: Integer;  // read-only
procedure DrawTab(TabCanvas: TCanvas; const R: IDispatch; Index: Integer; Selected: Boolean);
function GetImageIndex(TabIndex: Integer): Integer;
function ItemAtPos(const Pos: IDispatch; IgnoreTabHeight: Boolean): Integer;
function ItemRect(Index: Integer): IDispatch;
function ItemWidth(Index: Integer): Integer;
procedure MeasureTab(Index: Integer; var TabWidth: Integer);
function MinClientRect: IDispatch;
procedure SelectNext(Direction: Boolean);
procedure SetTabIndex(Value: Integer);

## TTabSheet
继承：TTabSheet → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.ComCtrls

property BorderWidth: TBorderWidth;
property Caption: TCaption;
property Constraints: TSizeConstraints;
property DoubleBuffered: Boolean;
property DragMode: TDragMode;
property Enabled: Boolean;
property Font: TFont;
property Height: Integer;
property Highlighted: Boolean;
property ImageIndex: TImageIndex;
property Left: Integer;
property OnContextPopup: TContextPopupEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnEndDrag: TEndDragEvent;
property OnEnter: TNotifyEvent;
property OnExit: TNotifyEvent;
property OnGesture: TGestureEvent;
property OnHide: TNotifyEvent;
property OnMouseActivate: TMouseActivateEvent;
property OnMouseDown: TMouseEvent;
property OnMouseEnter: TNotifyEvent;
property OnMouseLeave: TNotifyEvent;
property OnMouseMove: TMouseMoveEvent;
property OnMouseUp: TMouseEvent;
property OnResize: TNotifyEvent;
property OnShow: TNotifyEvent;
property OnStartDrag: TStartDragEvent;
property PageControl: TPageControl;
property PageIndex: Integer;
property ParentDoubleBuffered: Boolean;
property ParentFont: Boolean;
property ParentShowHint: Boolean;
property PopupMenu: TPopupMenu;
property ShowHint: Boolean;
property TabIndex: Integer;  // read-only
property TabVisible: Boolean;
property Top: Integer;
property Touch: TTouchManager;
property Visible: Boolean;
property Width: Integer;
procedure DoHide;
procedure DoShow;

## TTaskDialog
继承：TTaskDialog → TCustomTaskDialog → TComponent → TPersistent → TObject ｜ 单元：Vcl.Dialogs

property Buttons: TTaskDialogButtons;
property Caption: string;
property CommonButtons: TTaskDialogCommonButtons;
property CustomFooterIcon: TIcon;
property CustomMainIcon: TIcon;
property DefaultButton: TTaskDialogCommonButton;
property ExpandButtonCaption: string;
property ExpandedText: string;
property Flags: TTaskDialogFlags;
property FooterIcon: TTaskDialogIcon;
property FooterText: string;
property HelpContext: Integer;
property MainIcon: TTaskDialogIcon;
property OnButtonClicked: TTaskDlgClickEvent;
property OnDialogConstructed: TNotifyEvent;
property OnDialogCreated: TNotifyEvent;
property OnDialogDestroyed: TNotifyEvent;
property OnExpanded: TNotifyEvent;
property OnHyperlinkClicked: TNotifyEvent;
property OnNavigated: TNotifyEvent;
property OnRadioButtonClicked: TNotifyEvent;
property OnTimer: TTaskDlgTimerEvent;
property OnVerificationClicked: TNotifyEvent;
property ProgressBar: TTaskDialogProgressBar;
property RadioButtons: TTaskDialogButtons;
property Text: string;
property Title: string;
property VerificationText: string;

## TTaskDialogBaseButtonItem
继承：TTaskDialogBaseButtonItem → TCollectionItem → TPersistent → TObject ｜ 单元：Vcl.Dialogs

property Caption: string;
property Default: Boolean;
property Enabled: Boolean;
property ModalResult: TModalResult;
property TextWStr: LPCWSTR;  // read-only
procedure Click;
procedure SetInitialState;

## TTaskDialogButtonItem
继承：TTaskDialogButtonItem → TTaskDialogBaseButtonItem → TCollectionItem → TPersistent → TObject ｜ 单元：Vcl.Dialogs

property CommandLinkHint: string;
property ElevationRequired: Boolean;
property ModalResult: TModalResult;

## TTaskDialogButtons
继承：TTaskDialogButtons → TOwnedCollection → TCollection → TPersistent → TObject ｜ 单元：Vcl.Dialogs

property DefaultButton: TTaskDialogBaseButtonItem;
property Items[Index: ?]: TTaskDialogBaseButtonItem;
function Add: TTaskDialogBaseButtonItem;
function FindButton(AModalResult: TModalResult): TTaskDialogBaseButtonItem;
function GetEnumerator: TTaskDialogButtonsEnumerator;
procedure SetInitialState;

## TTaskDialogButtonsEnumerator
继承：TTaskDialogButtonsEnumerator → TObject ｜ 单元：Vcl.Dialogs

property Current: TTaskDialogBaseButtonItem;  // read-only
procedure Create(ACollection: TTaskDialogButtons);
function GetCurrent: TTaskDialogBaseButtonItem;
function MoveNext: Boolean;

## TTaskDialogProgressBar
继承：TTaskDialogProgressBar → TPersistent → TObject ｜ 单元：Vcl.Dialogs

property MarqueeSpeed: Cardinal;
property Max: Integer;
property Min: Integer;
property Position: Integer;
property State: TProgressBarState;
procedure Create(AClient: TCustomTaskDialog);
procedure Initialize;

## TTaskDialogRadioButtonItem
继承：TTaskDialogRadioButtonItem → TTaskDialogBaseButtonItem → TCollectionItem → TPersistent → TObject ｜ 单元：Vcl.Dialogs


## TTextAttributes
继承：TTextAttributes → TPersistent → TObject ｜ 单元：Vcl.ComCtrls

property Charset: TFontCharset;
property Color: TColor;
property ConsistentAttributes: TConsistentAttributes;  // read-only
property Height: Integer;
property Name: TFontName;
property Pitch: TFontPitch;
property Protected: Boolean;
property Size: Integer;
property Style: TFontStyles;
procedure Create(AOwner: TCustomRichEdit; AttributeType: TAttributeType);

## TTextFileAdapter
继承：TTextFileAdapter → TInterfacedObject → TObject ｜ 单元：Rt_NexusDevices

procedure Create(const ATextFile: PTextFile);

## TTextReader
继承：TTextReader → TObject ｜ 单元：System.Classes

procedure Close;
function Peek: Integer;
function Read: Integer;
function ReadBlock(var Buffer: TArray<System.Char>; Index: Integer; Count: Integer): Integer;
function ReadLine: string;
function ReadToEnd: string;

## TTextWriter
继承：TTextWriter → TObject ｜ 单元：System.Classes

procedure Close;
procedure Flush;
procedure Write(Value: Boolean);
procedure WriteLine;

## TThread
继承：TThread → TObject ｜ 单元：System.Classes

property Current: TThread;  // read-only
property CurrentThread: TThread;  // read-only
property ExternalThread: Boolean;  // read-only
property FatalException: TObject;  // read-only
property Finished: Boolean;  // read-only
property FreeOnTerminate: Boolean;
property Handle: THandle;  // read-only
property IsSingleProcessor: Boolean;  // read-only
property Priority: TThreadPriority;
property ProcessorCount: Integer;  // read-only
property Started: Boolean;  // read-only
property Suspended: Boolean;
property ThreadID: TThreadID;  // read-only
function CheckTerminated: Boolean;
procedure Create;
procedure DoTerminate;
procedure Execute;
function GetCPUUsage(const PrevSystemTimes: IDispatch): Integer;
function GetSystemTimes(const SystemTimes: IDispatch): Boolean;
function GetTickCount: Cardinal;
procedure NameThreadForDebugging(AThreadName: AnsiString; AThreadID: Cardinal);
procedure Resume;
procedure SetReturnValue(Value: Integer);
procedure Sleep(Timeout: Integer);
procedure SpinWait(Iterations: Integer);
procedure Start;
procedure Suspend;
procedure Terminate;
procedure TerminatedSet;
function WaitFor: Cardinal;
procedure Yield;

## TThreadList
继承：TThreadList → TObject ｜ 单元：System.Classes

property Duplicates: TDuplicates;
procedure Add(Item: Pointer);
procedure Clear;
procedure Create;
function LockList: TList;
procedure Remove(Item: Pointer);
procedure RemoveItem(Item: Pointer; Direction: TDirection);
procedure UnlockList;

## TTimeField
继承：TTimeField → TDateTimeField → TField → TComponent → TPersistent → TObject ｜ 单元：Data.DB


## TTimer
继承：TTimer → TComponent → TPersistent → TObject ｜ 单元：Vcl.ExtCtrls

property Enabled: Boolean;
property Interval: Cardinal;
property OnTimer: TNotifyEvent;
procedure Timer;

## TTimeZone
继承：TTimeZone → TObject ｜ 单元：System.DateUtils

property Abbreviation: String;  // read-only
property DisplayName: String;  // read-only
property ID: String;  // read-only
property Local: TTimeZone;  // read-only
property UtcOffset: TTimeSpan;  // read-only
function DoGetDisplayName(const ADateTime: TDateTime; const ForceDaylight: Boolean): string;
function DoGetID: string;
procedure DoGetOffsetsAndType(const ADateTime: TDateTime; out AOffset: Int64; out ADstSave: Int64; out AType: TLocalTimeType);
function GetAbbreviation(const ADateTime: TDateTime; const ForceDaylight: Boolean): string;
function GetDisplayName(const ADateTime: TDateTime; const ForceDaylight: Boolean): string;
function GetLocalTimeType(const ADateTime: TDateTime): TLocalTimeType;
function GetUtcOffset(const ADateTime: TDateTime; const ForceDaylight: Boolean): IDispatch;
function IsAmbiguousTime(const ADateTime: TDateTime): Boolean;
function IsDaylightTime(const ADateTime: TDateTime; const ForceDaylight: Boolean): Boolean;
function IsInvalidTime(const ADateTime: TDateTime): Boolean;
function IsStandardTime(const ADateTime: TDateTime; const ForceDaylight: Boolean): Boolean;
function ToLocalTime(const ADateTime: TDateTime): TDateTime;
function ToUniversalTime(const ADateTime: TDateTime; const ForceDaylight: Boolean): TDateTime;

## TToolBar
继承：TToolBar → TToolWindow → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.ComCtrls

property Align: TAlign;
property AllowTextButtons: Boolean;
property Anchors: TAnchors;
property AutoSize: Boolean;
property BorderWidth: TBorderWidth;
property ButtonCount: Integer;  // read-only
property ButtonHeight: Integer;
property Buttons[Index: ?]: TToolButton;  // read-only
property ButtonWidth: Integer;
property Canvas: TCanvas;  // read-only
property Caption: TCaption;
property Color: TColor;
property Constraints: TSizeConstraints;
property Ctl3D: Boolean;
property Customizable: Boolean;
property CustomizeKeyName: String;
property CustomizeValueName: String;
property DisabledImages: TCustomImageList;
property DockSite: Boolean;
property DoubleBuffered: Boolean;
property DragCursor: TCursor;
property DragKind: TDragKind;
property DragMode: TDragMode;
property DrawingStyle: TTBDrawingStyle;
property EdgeBorders: TEdgeBorders;
property EdgeInner: TEdgeStyle;
property EdgeOuter: TEdgeStyle;
property Enabled: Boolean;
property Flat: Boolean;
property Font: TFont;
property GradientDirection: TGradientDirection;
property GradientDrawingOptions: TTBGradientDrawingOptions;
property GradientEndColor: TColor;
property GradientStartColor: TColor;
property Height: Integer;
property HideClippedButtons: Boolean;
property HotImages: TCustomImageList;
property HotTrackColor: TColor;
property Images: TCustomImageList;
property Indent: Integer;
property List: Boolean;
property Menu: TMainMenu;
property OnAdvancedCustomDraw: TTBAdvancedCustomDrawEvent;
property OnAdvancedCustomDrawButton: TTBAdvancedCustomDrawBtnEvent;
property OnClick: TNotifyEvent;
property OnContextPopup: TContextPopupEvent;
property OnCustomDraw: TTBCustomDrawEvent;
property OnCustomDrawButton: TTBCustomDrawBtnEvent;
property OnCustomizeAdded: TTBButtonEvent;
property OnCustomizeCanDelete: TTBCustomizeQueryEvent;
property OnCustomizeCanInsert: TTBCustomizeQueryEvent;
property OnCustomized: TNotifyEvent;
property OnCustomizeDelete: TTBButtonEvent;
property OnCustomizeNewButton: TTBNewButtonEvent;
property OnCustomizeReset: TNotifyEvent;
property OnCustomizing: TNotifyEvent;
property OnDblClick: TNotifyEvent;
property OnDockDrop: TDockDropEvent;
property OnDockOver: TDockOverEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnEndDock: TEndDragEvent;
property OnEndDrag: TEndDragEvent;
property OnEnter: TNotifyEvent;
property OnExit: TNotifyEvent;
property OnGesture: TGestureEvent;
property OnGetSiteInfo: TGetSiteInfoEvent;
property OnMouseActivate: TMouseActivateEvent;
property OnMouseDown: TMouseEvent;
property OnMouseEnter: TNotifyEvent;
property OnMouseLeave: TNotifyEvent;
property OnMouseMove: TMouseMoveEvent;
property OnMouseUp: TMouseEvent;
property OnResize: TNotifyEvent;
property OnStartDock: TStartDockEvent;
property OnStartDrag: TStartDragEvent;
property OnUnDock: TUnDockEvent;
property ParentColor: Boolean;
property ParentDoubleBuffered: Boolean;
property ParentFont: Boolean;
property ParentShowHint: Boolean;
property PopupMenu: TPopupMenu;
property RowCount: Integer;  // read-only
property ShowCaptions: Boolean;
property ShowHint: Boolean;
property StyleElements: TStyleElements;
property TabOrder: TTabOrder;
property TabStop: Boolean;
property Touch: TTouchManager;
property Transparent: Boolean;
property Visible: Boolean;
property Wrapable: Boolean;
procedure CancelMenu;
function CheckMenuDropdown(Button: TToolButton): Boolean;
procedure ClickButton(Button: TToolButton);
function CustomDraw(const ARect: IDispatch; Stage: TCustomDrawStage): Boolean;
function CustomDrawButton(Button: TToolButton; State: TCustomDrawState; Stage: TCustomDrawStage; var Flags: TTBCustomDrawFlags): Boolean;
function DoQueryDelete(Index: Integer): Boolean;
function DoQueryInsert(Index: Integer): Boolean;
function GetEnumerator: TToolBarEnumerator;
function GradientDrawButton(Button: TToolButton; State: TCustomDrawState; var Flags: TTBCustomDrawFlags): Boolean;
function GradientDrawToolBar(const ARect: IDispatch): Boolean;
procedure InitMenu(Button: TToolButton);
function IsCustomDrawn(Target: TCustomDrawTarget; Stage: TCustomDrawStage): Boolean;
function TrackMenu(Button: TToolButton): Boolean;

## TToolBarDockObject
继承：TToolBarDockObject → TDragDockObject → TBaseDragControlObject → TDragObject → TObject ｜ 单元：Vcl.ComCtrls

function ToolDockImage(Erase: Boolean): Boolean;

## TToolBarEnumerator
继承：TToolBarEnumerator → TObject ｜ 单元：Vcl.ComCtrls

property Current: TToolButton;  // read-only
procedure Create(AToolBar: TToolBar);
function GetCurrent: TToolButton;
function MoveNext: Boolean;

## TToolBarStyleHook
继承：TToolBarStyleHook → TMouseTrackControlStyleHook → TMouseTrackControlStyleHook ｜ 单元：Vcl.ComCtrls


## TToolButton
继承：TToolButton → TGraphicControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.ComCtrls

property Action: TBasicAction;
property AllowAllUp: Boolean;
property AutoSize: Boolean;
property Caption: TCaption;
property Down: Boolean;
property DragCursor: TCursor;
property DragKind: TDragKind;
property DragMode: TDragMode;
property DropdownMenu: TPopupMenu;
property Enabled: Boolean;
property EnableDropdown: Boolean;
property Grouped: Boolean;
property Height: Integer;
property ImageIndex: TImageIndex;
property Indeterminate: Boolean;
property Index: Integer;  // read-only
property Marked: Boolean;
property MenuItem: TMenuItem;
property OnClick: TNotifyEvent;
property OnContextPopup: TContextPopupEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnEndDock: TEndDragEvent;
property OnEndDrag: TEndDragEvent;
property OnMouseActivate: TMouseActivateEvent;
property OnMouseDown: TMouseEvent;
property OnMouseEnter: TNotifyEvent;
property OnMouseLeave: TNotifyEvent;
property OnMouseMove: TMouseMoveEvent;
property OnMouseUp: TMouseEvent;
property OnStartDock: TStartDockEvent;
property OnStartDrag: TStartDragEvent;
property ParentShowHint: Boolean;
property PopupMenu: TPopupMenu;
property ShowHint: Boolean;
property Style: TToolButtonStyle;
property Visible: Boolean;
property Width: Integer;
property Wrap: Boolean;
procedure BeginUpdate;
function CheckMenuDropdown: Boolean;
procedure EndUpdate;
procedure RefreshControl;
procedure UpdateControl;

## TToolButtonActionLink
继承：TToolButtonActionLink → TControlActionLink → TActionLink → TContainedActionLink ｜ 单元：Vcl.ComCtrls


## TToolDockForm
继承：TToolDockForm → TCustomDockForm → TCustomForm → TScrollingWinControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.ToolWin


## TToolDockObject
继承：TToolDockObject → TDragDockObject → TBaseDragControlObject → TDragObject → TObject ｜ 单元：Vcl.ToolWin


## TToolWindow
继承：TToolWindow → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.ToolWin

property EdgeBorders: TEdgeBorders;
property EdgeInner: TEdgeStyle;
property EdgeOuter: TEdgeStyle;
procedure NCPaint(DC: HDC);

## TTouchManager
继承：TTouchManager → TCustomTouchManager → TPersistent → TObject ｜ 单元：Vcl.Controls

property GestureManager: TCustomGestureManager;
property InteractiveGestureOptions: TInteractiveGestureOptions;
property InteractiveGestures: TInteractiveGestures;
property ParentTabletOptions: Boolean;
property TabletOptions: TTabletOptions;

## TTrackBar
继承：TTrackBar → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.ComCtrls

property Align: TAlign;
property Anchors: TAnchors;
property BorderWidth: TBorderWidth;
property Constraints: TSizeConstraints;
property Ctl3D: Boolean;
property DoubleBuffered: Boolean;
property DragCursor: TCursor;
property DragKind: TDragKind;
property DragMode: TDragMode;
property Enabled: Boolean;
property Frequency: Integer;
property LineSize: Integer;
property Max: Integer;
property Min: Integer;
property OnChange: TNotifyEvent;
property OnContextPopup: TContextPopupEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnEndDock: TEndDragEvent;
property OnEndDrag: TEndDragEvent;
property OnEnter: TNotifyEvent;
property OnExit: TNotifyEvent;
property OnGesture: TGestureEvent;
property OnKeyDown: TKeyEvent;
property OnKeyPress: TKeyPressEvent;
property OnKeyUp: TKeyEvent;
property OnStartDock: TStartDockEvent;
property OnStartDrag: TStartDragEvent;
property Orientation: TTrackBarOrientation;
property PageSize: Integer;
property ParentCtl3D: Boolean;
property ParentDoubleBuffered: Boolean;
property ParentShowHint: Boolean;
property PopupMenu: TPopupMenu;
property Position: Integer;
property PositionToolTip: TPositionToolTip;
property SelEnd: Integer;
property SelStart: Integer;
property ShowHint: Boolean;
property ShowSelRange: Boolean;
property SliderVisible: Boolean;
property StyleElements: TStyleElements;
property TabOrder: TTabOrder;
property TabStop: Boolean;
property ThumbLength: Integer;
property TickMarks: TTickMark;
property TickStyle: TTickStyle;
property Touch: TTouchManager;
property Visible: Boolean;
procedure Changed;
procedure SetTick(Value: Integer);

## TTrackBarStyleHook
继承：TTrackBarStyleHook → TStyleHook → TStyleHook ｜ 单元：Vcl.ComCtrls


## TTrayIcon
继承：TTrayIcon → TCustomTrayIcon → TComponent → TPersistent → TObject ｜ 单元：Vcl.ExtCtrls

property Animate: Boolean;
property AnimateInterval: Cardinal;
property BalloonFlags: TBalloonFlags;
property BalloonHint: string;
property BalloonTimeout: Integer;
property BalloonTitle: string;
property Hint: string;
property Icon: TIcon;
property IconIndex: Integer;
property Icons: TCustomImageList;
property OnAnimate: TNotifyEvent;
property OnBalloonClick: TNotifyEvent;
property OnClick: TNotifyEvent;
property OnDblClick: TNotifyEvent;
property OnMouseDown: TMouseEvent;
property OnMouseMove: TMouseMoveEvent;
property OnMouseUp: TMouseEvent;
property PopupMenu: TPopupMenu;
property Visible: Boolean;

## TTreeNode
继承：TTreeNode → TPersistent → TObject ｜ 单元：Vcl.ComCtrls

property AbsoluteIndex: Integer;  // read-only
property Count: Integer;  // read-only
property Cut: Boolean;
property Data: TCustomData;
property Deleting: Boolean;  // read-only
property DropTarget: Boolean;
property Enabled: Boolean;
property Expanded: Boolean;
property ExpandedImageIndex: TImageIndex;
property Focused: Boolean;
property Handle: HWND;  // read-only
property HasChildren: Boolean;
property ImageIndex: TImageIndex;
property Index: Integer;  // read-only
property IsVisible: Boolean;  // read-only
property Item[Index: ?]: TTreeNode;
property Level: Integer;  // read-only
property OverlayIndex: Integer;
property Owner: TTreeNodes;  // read-only
property Parent: TTreeNode;  // read-only
property Selected: Boolean;
property SelectedIndex: Integer;
property StateIndex: Integer;
property Text: String;
property TreeView: TCustomTreeView;  // read-only
function AlphaSort(ARecurse: Boolean): Boolean;
procedure Collapse(Recurse: Boolean);
procedure Create(AOwner: TTreeNodes);
procedure Delete;
procedure DeleteChildren;
function DisplayRect(TextOnly: Boolean): IDispatch;
function EditText: Boolean;
procedure EndEdit(Cancel: Boolean);
procedure Expand(Recurse: Boolean);
function getFirstChild: TTreeNode;
function GetHandle: HWND;
function GetLastChild: TTreeNode;
function GetNext: TTreeNode;
function GetNextChild(Value: TTreeNode): TTreeNode;
function getNextSibling: TTreeNode;
function GetNextVisible: TTreeNode;
function GetPrev: TTreeNode;
function GetPrevChild(Value: TTreeNode): TTreeNode;
function getPrevSibling: TTreeNode;
function GetPrevVisible: TTreeNode;
function HasAsParent(Value: TTreeNode): Boolean;
function IndexOf(Value: TTreeNode): Integer;
function IsFirstNode: Boolean;
procedure MakeVisible;
procedure MoveTo(Destination: TTreeNode; Mode: TNodeAttachMode);

## TTreeNodes
继承：TTreeNodes → TPersistent → TObject ｜ 单元：Vcl.ComCtrls

property Count: Integer;  // read-only
property Handle: HWND;  // read-only
property Item[Index: ?]: TTreeNode;  // read-only
property Owner: TCustomTreeView;  // read-only
function Add(Sibling: TTreeNode; const S: string): TTreeNode;
function AddChild(Parent: TTreeNode; const S: string): TTreeNode;
function AddChildFirst(Parent: TTreeNode; const S: string): TTreeNode;
function AddChildObject(Parent: TTreeNode; const S: string; Ptr: Pointer): TTreeNode;
function AddChildObjectFirst(Parent: TTreeNode; const S: string; Ptr: Pointer): TTreeNode;
function AddFirst(Sibling: TTreeNode; const S: string): TTreeNode;
function AddNode(Node: TTreeNode; Relative: TTreeNode; const S: string; Ptr: Pointer; Method: TNodeAttachMode): TTreeNode;
function AddObject(Sibling: TTreeNode; const S: string; Ptr: Pointer): TTreeNode;
function AddObjectFirst(Sibling: TTreeNode; const S: string; Ptr: Pointer): TTreeNode;
function AlphaSort(ARecurse: Boolean): Boolean;
procedure BeginUpdate;
procedure Clear;
procedure Create(AOwner: TCustomTreeView);
procedure Delete(Node: TTreeNode);
procedure EndUpdate;
function GetEnumerator: TTreeNodesEnumerator;
function GetFirstNode: TTreeNode;
function Insert(Sibling: TTreeNode; const S: string): TTreeNode;
function InsertNode(Node: TTreeNode; Sibling: TTreeNode; const S: string; Ptr: Pointer): TTreeNode;
function InsertObject(Sibling: TTreeNode; const S: string; Ptr: Pointer): TTreeNode;

## TTreeNodesEnumerator
继承：TTreeNodesEnumerator → TObject ｜ 单元：Vcl.ComCtrls

property Current: TTreeNode;  // read-only
procedure Create(ATreeNodes: TTreeNodes);
function GetCurrent: TTreeNode;
function MoveNext: Boolean;

## TTreeView
继承：TTreeView → TCustomTreeView → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.ComCtrls

property Align: TAlign;
property Anchors: TAnchors;
property AutoExpand: Boolean;
property BevelEdges: TBevelEdges;
property BevelInner: TBevelCut;
property BevelKind: TBevelKind;
property BevelOuter: TBevelCut;
property BevelWidth: TBevelWidth;
property BiDiMode: TBiDiMode;
property BorderStyle: TBorderStyle;
property BorderWidth: TBorderWidth;
property ChangeDelay: Integer;
property Color: TColor;
property Constraints: TSizeConstraints;
property Ctl3D: Boolean;
property DoubleBuffered: Boolean;
property DragCursor: TCursor;
property DragKind: TDragKind;
property DragMode: TDragMode;
property Enabled: Boolean;
property Font: TFont;
property HideSelection: Boolean;
property HotTrack: Boolean;
property Images: TCustomImageList;
property Indent: Integer;
property Items: TTreeNodes;
property MultiSelect: Boolean;
property MultiSelectStyle: TMultiSelectStyle;
property OnAddition: TTVExpandedEvent;
property OnAdvancedCustomDraw: TTVAdvancedCustomDrawEvent;
property OnAdvancedCustomDrawItem: TTVAdvancedCustomDrawItemEvent;
property OnCancelEdit: TTVChangedEvent;
property OnChange: TTVChangedEvent;
property OnChanging: TTVChangingEvent;
property OnClick: TNotifyEvent;
property OnCollapsed: TTVExpandedEvent;
property OnCollapsing: TTVCollapsingEvent;
property OnCompare: TTVCompareEvent;
property OnContextPopup: TContextPopupEvent;
property OnCreateNodeClass: TTVCreateNodeClassEvent;
property OnCustomDraw: TTVCustomDrawEvent;
property OnCustomDrawItem: TTVCustomDrawItemEvent;
property OnDblClick: TNotifyEvent;
property OnDeletion: TTVExpandedEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnEdited: TTVEditedEvent;
property OnEditing: TTVEditingEvent;
property OnEndDock: TEndDragEvent;
property OnEndDrag: TEndDragEvent;
property OnEnter: TNotifyEvent;
property OnExit: TNotifyEvent;
property OnExpanded: TTVExpandedEvent;
property OnExpanding: TTVExpandingEvent;
property OnGesture: TGestureEvent;
property OnGetImageIndex: TTVExpandedEvent;
property OnGetSelectedIndex: TTVExpandedEvent;
property OnHint: TTVHintEvent;
property OnKeyDown: TKeyEvent;
property OnKeyPress: TKeyPressEvent;
property OnKeyUp: TKeyEvent;
property OnMouseActivate: TMouseActivateEvent;
property OnMouseDown: TMouseEvent;
property OnMouseEnter: TNotifyEvent;
property OnMouseLeave: TNotifyEvent;
property OnMouseMove: TMouseMoveEvent;
property OnMouseUp: TMouseEvent;
property OnStartDock: TStartDockEvent;
property OnStartDrag: TStartDragEvent;
property ParentBiDiMode: Boolean;
property ParentColor: Boolean;
property ParentCtl3D: Boolean;
property ParentDoubleBuffered: Boolean;
property ParentFont: Boolean;
property ParentShowHint: Boolean;
property PopupMenu: TPopupMenu;
property ReadOnly: Boolean;
property RightClickSelect: Boolean;
property RowSelect: Boolean;
property ShowButtons: Boolean;
property ShowHint: Boolean;
property ShowLines: Boolean;
property ShowRoot: Boolean;
property SortType: TSortType;
property StateImages: TCustomImageList;
property StyleElements: TStyleElements;
property TabOrder: TTabOrder;
property TabStop: Boolean;
property ToolTips: Boolean;
property Touch: TTouchManager;
property Visible: Boolean;

## TTreeViewStyleHook
继承：TTreeViewStyleHook → TScrollingStyleHook → TMouseTrackControlStyleHook ｜ 单元：Vcl.ComCtrls


## TTypedNotification
继承：TTypedNotification → TDispatchObject → TDispatchObject ｜ 单元：RT_ClientServerInterface

procedure Create(const AType: WideString; ACode: Integer; const AData: IInterface);

## TUnicodeEncoding
继承：TUnicodeEncoding → TEncoding → TObject ｜ 单元：System.SysUtils ｜ 未在类列表里注册，只能通过实例访问

procedure Create;

## TUnsignedAutoIncField
继承：TUnsignedAutoIncField → TLongWordField → TNumericField → TField → TComponent → TPersistent → TObject ｜ 单元：Data.DB


## TUpDown
继承：TUpDown → TCustomUpDown → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.ComCtrls

property AlignButton: TUDAlignButton;
property Anchors: TAnchors;
property ArrowKeys: Boolean;
property Associate: TWinControl;
property Constraints: TSizeConstraints;
property DoubleBuffered: Boolean;
property Enabled: Boolean;
property Hint: string;
property Increment: Integer;
property Max: Integer;
property Min: Integer;
property OnChanging: TUDChangingEvent;
property OnChangingEx: TUDChangingEventEx;
property OnClick: TUDClickEvent;
property OnContextPopup: TContextPopupEvent;
property OnEnter: TNotifyEvent;
property OnExit: TNotifyEvent;
property OnMouseActivate: TMouseActivateEvent;
property OnMouseDown: TMouseEvent;
property OnMouseEnter: TNotifyEvent;
property OnMouseLeave: TNotifyEvent;
property OnMouseMove: TMouseMoveEvent;
property OnMouseUp: TMouseEvent;
property Orientation: TUDOrientation;
property ParentDoubleBuffered: Boolean;
property ParentShowHint: Boolean;
property PopupMenu: TPopupMenu;
property Position: Integer;
property ShowHint: Boolean;
property StyleElements: TStyleElements;
property TabOrder: TTabOrder;
property TabStop: Boolean;
property Thousands: Boolean;
property Visible: Boolean;
property Wrap: Boolean;

## TUpDownStyleHook
继承：TUpDownStyleHook → TMouseTrackControlStyleHook → TMouseTrackControlStyleHook ｜ 单元：Vcl.ComCtrls


## TVarBytesField
继承：TVarBytesField → TBytesField → TBinaryField → TField → TComponent → TPersistent → TObject ｜ 单元：Data.DB


## TVariantField
继承：TVariantField → TField → TComponent → TPersistent → TObject ｜ 单元：Data.DB


## TVaultFileLessDocumentNotification
继承：TVaultFileLessDocumentNotification → TNotificationWithCode → TInterfacedObject → TObject ｜ 单元：RT_ClientServerInterface

procedure Create(ACode: Integer; const AVaultFileLessInfo: IDispatch; const AFileName: WideString);

## TVaultFileLessReleaseNotification
继承：TVaultFileLessReleaseNotification → TInterfacedObject → TObject ｜ 单元：RT_ClientServerInterface

procedure Create(const FileName: WideString; const OriginalVaultGUID: WideString; const OriginalRevisionGUID: WideString; const TargetVaultGUID: WideString; const TargetRevisionGUID: WideString);

## TVCSNotification
继承：TVCSNotification → TNotificationWithCode → TInterfacedObject → TObject ｜ 单元：RT_ClientServerInterface

procedure Create(ACode: Integer; const AVCSFileNames: WideString; const AVCSProjectGUID: WideString; const AData: IInterface);
procedure CreateExt(ACode: Integer; const AVCSFileNames: WideString; const AVCSFileNamesExt: WideString; const AVCSProjectGUID: WideString; const AData: IInterface);
procedure CreateForStatusChanged(ACode: Integer; const AVCSFileNames: WideString; const AVCSRevisionString: WideString; const AData: IInterface);
procedure CreateTyped(AType: Integer; const AVCSProjectGUID: WideString; const AData: IInterface);

## TVFS_Stream
继承：TVFS_Stream → TStream → TObject ｜ 单元：VFSAPI

procedure Create(const AVFSFileName: string; AMode: Integer);
procedure LoadFromFile(const FileName: string);
procedure SaveToFile(const FileName: string);

## TVHDLLibraryUnit
继承：TVHDLLibraryUnit → TObject ｜ 单元：Rt_VHDL

field FileName;
field Kind;
field Name;
field OwnerEntity;

## TViewNotification
继承：TViewNotification → TNotificationWithCode → TInterfacedObject → TObject ｜ 单元：RT_ClientServerInterface

procedure Create(ACode: Integer);

## TWatch
继承：TWatch → TInterfacedObject → TObject ｜ 单元：RT_Debugger

procedure AttachMonitor(aMonitor: IWatchMonitor);
procedure Create(anExpression: WideString; aManager: IDebugger);
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

## TWatchWrapper
继承：TWatchWrapper → TObject ｜ 单元：RT_Debugger

field Watch;
procedure Create(AWatch: IWatch);

## TWaveSimNotification
继承：TWaveSimNotification → TNotificationWithCode → TInterfacedObject → TObject ｜ 单元：RT_ClientServerInterface

procedure Create(ACode: Integer; AUniqueId: Integer);
function GetUniqueId: Integer;

## TWebBrowserNotification
继承：TWebBrowserNotification → TNotificationWithCode → TInterfacedObject → TObject ｜ 单元：RT_ClientServerInterface

procedure Create(ACode: Integer; const AURL: WideString; const ASessionId: WideString; AIsUpdateRequired: Boolean);

## TWICImage
继承：TWICImage → TGraphic → TInterfacedPersistent → TPersistent → TObject ｜ 单元：Vcl.Graphics

property Handle: IWicBitmap;
property ImageFormat: TWICImageFormat;
property ImagingFactory: IWICImagingFactory;  // read-only

## TWideMemoField
继承：TWideMemoField → TBlobField → TField → TComponent → TPersistent → TObject ｜ 单元：Data.DB

property Value: String;

## TWideStringField
继承：TWideStringField → TStringField → TField → TComponent → TPersistent → TObject ｜ 单元：Data.DB

property Value: String;

## TWinControl
继承：TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：Vcl.Controls

property AlignDisabled: Boolean;  // read-only
property Brush: TBrush;  // read-only
property ControlCount: Integer;  // read-only
property Controls[Index: ?]: TControl;  // read-only
property DockClientCount: Integer;  // read-only
property DockClients[Index: ?]: TControl;  // read-only
property DockManager: IDockManager;
property DockSite: Boolean;
property DoubleBuffered: Boolean;
property Handle: HWND;  // read-only
property MouseInClient: Boolean;  // read-only
property Padding: TPadding;
property ParentDoubleBuffered: Boolean;
property ParentWindow: HWND;
property Showing: Boolean;  // read-only
property TabOrder: TTabOrder;
property TabStop: Boolean;
property UseDockManager: Boolean;
property VisibleDockClientCount: Integer;  // read-only
procedure AdjustClientRect(const Rect: IDispatch);
procedure AlignControls(AControl: TControl; const Rect: IDispatch);
procedure Broadcast(var Message);
function CanFocus: Boolean;
function ContainsControl(Control: TControl): Boolean;
function ControlAtPos(const Pos: IDispatch; AllowDisabled: Boolean; AllowWinControls: Boolean; AllLevels: Boolean): TControl;
procedure ControlsAligned;
function CreateDockManager: IDockManager;
procedure CreateHandle;
procedure CreateParams(const Params: IDispatch);
procedure CreateParented(ParentWindow: HWND);
function CreateParentedControl(ParentWindow: HWND): TWinControl;
procedure CreateWindowHandle(const Params: IDispatch);
procedure CreateWnd;
function CustomAlignInsertBefore(C1: TControl; C2: TControl): Boolean;
procedure CustomAlignPosition(Control: TControl; var NewLeft: Integer; var NewTop: Integer; var NewWidth: Integer; var NewHeight: Integer; const AlignRect: IDispatch; const AlignInfo: IDispatch);
procedure DestroyHandle;
procedure DestroyWindowHandle;
procedure DestroyWnd;
procedure DisableAlign;
procedure DoAddDockClient(Client: TControl; const ARect: IDispatch);
procedure DockDrop(Source: TDragDockObject; X: Integer; Y: Integer);
procedure DockOver(Source: TDragDockObject; X: Integer; Y: Integer; State: TDragState; var Accept: Boolean);
function DockReplaceDockClient(Client: TControl; NewDockSite: TWinControl; DropControl: TControl; ControlSide: TAlign; ReplacementClient: TControl): Boolean;
procedure DoDockOver(Source: TDragDockObject; X: Integer; Y: Integer; State: TDragState; var Accept: Boolean);
procedure DoEnter;
procedure DoExit;
procedure DoFlipChildren;
function DoHandleStyleMessage(const Message: IDispatch): Boolean;
procedure DoRemoveDockClient(Client: TControl);
function DoUnDock(NewTarget: TWinControl; Client: TControl): Boolean;
procedure EnableAlign;
function FindChildControl(const ControlName: string): TControl;
procedure FlipChildren(AllLevels: Boolean);
function Focused: Boolean;
function GetControlExtents: IDispatch;
procedure GetSiteInfo(Client: TControl; const InfluenceRect: IDispatch; const MousePos: IDispatch; var CanDock: Boolean);
procedure GetTabControlList(List: TList);
procedure GetTabOrderList(List: TList);
function HandleAllocated: Boolean;
procedure HandleNeeded;
procedure InsertControl(AControl: TControl);
function IsQualifyingSite(const Client: TControl): Boolean;
procedure KeyDown(var Key: Word; Shift: TShiftState);
procedure KeyPress(var Key: Char);
procedure KeyUp(var Key: Word; Shift: TShiftState);
procedure PaintTo(DC: HDC; X: Integer; Y: Integer);
procedure PaintWindow(DC: HDC);
function PreProcessMessage(const Msg: IDispatch): Boolean;
procedure Realign;
procedure ReloadDockedControl(const AControlName: string; var AControl: TControl);
procedure RemoveControl(AControl: TControl);
procedure ScaleBy(M: Integer; D: Integer);
procedure ScrollBy(DeltaX: Integer; DeltaY: Integer);
procedure SetFocus;
procedure SetParentBackground(Value: Boolean);
procedure SetParentDoubleBuffered(Value: Boolean);
procedure ShowControl(AControl: TControl);
procedure UpdateControlOriginalParentSize(AControl: TControl; const AOriginalParentSize: IDispatch);
procedure UpdateControlState;
procedure UpdateTIPStatus;

## TWinControlActionLink
继承：TWinControlActionLink → TControlActionLink → TActionLink → TContainedActionLink ｜ 单元：Vcl.Controls


## TWindowAction
继承：TWindowAction → TAction → TCustomAction → TContainedAction ｜ 单元：Vcl.StdActns

property Form: TCustomForm;
function GetForm(Target: TObject): TForm;

## TWindowArrange
继承：TWindowArrange → TWindowAction → TAction → TCustomAction → TContainedAction ｜ 单元：Vcl.StdActns


## TWindowCascade
继承：TWindowCascade → TWindowAction → TAction → TCustomAction → TContainedAction ｜ 单元：Vcl.StdActns


## TWindowClose
继承：TWindowClose → TWindowAction → TAction → TCustomAction → TContainedAction ｜ 单元：Vcl.StdActns


## TWindowMinimizeAll
继承：TWindowMinimizeAll → TWindowAction → TAction → TCustomAction → TContainedAction ｜ 单元：Vcl.StdActns


## TWindowTileHorizontal
继承：TWindowTileHorizontal → TWindowAction → TAction → TCustomAction → TContainedAction ｜ 单元：Vcl.StdActns


## TWindowTileVertical
继承：TWindowTileVertical → TWindowAction → TAction → TCustomAction → TContainedAction ｜ 单元：Vcl.StdActns


## TWinXPButton
继承：TWinXPButton → TWinXPCustomButton → TWinXPCustomButtonControl → TXPCustomControl → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：WinXPButtons

property Cancel: Boolean;
property Color: TColor;
property CustomImage: TAlphaBitmap;
property Default: Boolean;
property DisabledTextColor: TColor;
property FrameColor: TColor;
property HotColor: TColor;
property HotFrameColor: TColor;
property LookAndFeel: TXPLookAndFeel;
property ModalResult: TModalResult;
property PressedColor: TColor;
property ShowAccelChar: Boolean;
property Style: TXPButtonStyle;
property TabStop: Boolean;
property WordWrap: Boolean;

## TWinXPCustomButton
继承：TWinXPCustomButton → TWinXPCustomButtonControl → TXPCustomControl → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：WinXPButtons

function GetShiftContentIfPressed: Boolean;
function GetSunkenDisabled: Boolean;
procedure ReDrawCaption(const ARect: IDispatch; AFontColor: TColor);
procedure ReDrawInside(const ARect: IDispatch; AFontColor: TColor);

## TWinXPCustomButtonControl
继承：TWinXPCustomButtonControl → TXPCustomControl → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：WinXPButtons

property Action: TBasicAction;
property Align: TAlign;
property Anchors: TAnchors;
property Caption: TCaption;
property Constraints: TSizeConstraints;
property CustomHint: TCustomHint;
property DoubleBuffered: Boolean;
property DragCursor: TCursor;
property DragKind: TDragKind;
property DragMode: TDragMode;
property Enabled: Boolean;
property Font: TFont;
property OnClick: TNotifyEvent;
property OnContextPopup: TContextPopupEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnEndDock: TEndDragEvent;
property OnEndDrag: TEndDragEvent;
property OnEnter: TNotifyEvent;
property OnExit: TNotifyEvent;
property OnKeyDown: TKeyEvent;
property OnKeyPress: TKeyPressEvent;
property OnKeyUp: TKeyEvent;
property OnMouseActivate: TMouseActivateEvent;
property OnMouseDown: TMouseEvent;
property OnMouseEnter: TNotifyEvent;
property OnMouseLeave: TNotifyEvent;
property OnMouseMove: TMouseMoveEvent;
property OnMouseUp: TMouseEvent;
property OnStartDock: TStartDockEvent;
property OnStartDrag: TStartDragEvent;
property ParentFont: Boolean;
property ParentShowHint: Boolean;
property PopupMenu: TPopupMenu;
property ShowHint: Boolean;
property SmoothDraw: Boolean;
property TabOrder: TTabOrder;
property Visible: Boolean;
procedure ButtonMouseDown(X: Integer; Y: Integer);
procedure ButtonMouseMove(X: Integer; Y: Integer);
procedure ButtonMouseUp(X: Integer; Y: Integer);
procedure CompulsoryClick;
procedure DrawTextEvent(ACanvas: TCanvas; const ARect: IDispatch; const ACaption: string; AFont: TFont; AFontColor: TColor; AAlignment: TAlignment; ALayout: TTextLayout; AFlags: TXPDrawCaptionFlags; AEllipsis: TEllipsisPosition);
function GetControlState(AForPainting: Boolean): TThemedButton;
function GetControlState2(APressed: Boolean; AForPainting: Boolean): TThemedButton;

## TWinXPCustomButtonControlAutomation
继承：TWinXPCustomButtonControlAutomation → TControlAutomation → TControlAutomation ｜ 单元：WinXPButtons


## TWinXPCustomTabControl
继承：TWinXPCustomTabControl → TXPCustomControl → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：XPPageControl

property ActiveTabTextColor: TColor;
property Align: TAlign;
property Anchors: TAnchors;
property Canvas: TCanvas;  // read-only
property Constraints: TSizeConstraints;
property CustomHint: TCustomHint;
property DockSite: Boolean;
property DoubleBuffered: Boolean;
property DragCursor: TCursor;
property DragKind: TDragKind;
property DragMode: TDragMode;
property Enabled: Boolean;
property Font: TFont;
property HelpContext: THelpContext;
property Images: TCustomImageList;
property OnChange: TNotifyEvent;
property OnChanging: TTabChangingEvent;
property OnContextPopup: TContextPopupEvent;
property OnDockDrop: TDockDropEvent;
property OnDockOver: TDockOverEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnEndDock: TEndDragEvent;
property OnEndDrag: TEndDragEvent;
property OnEnter: TNotifyEvent;
property OnExit: TNotifyEvent;
property OnGetSiteInfo: TGetSiteInfoEvent;
property OnMouseActivate: TMouseActivateEvent;
property OnMouseDown: TMouseEvent;
property OnMouseEnter: TNotifyEvent;
property OnMouseLeave: TNotifyEvent;
property OnMouseMove: TMouseMoveEvent;
property OnMouseUp: TMouseEvent;
property OnResize: TNotifyEvent;
property OnStartDock: TStartDockEvent;
property OnStartDrag: TStartDragEvent;
property OnUnDock: TUnDockEvent;
property ParentFont: Boolean;
property ParentShowHint: Boolean;
property PassFocusOnChange: Boolean;
property PopupMenu: TPopupMenu;
property ShowHint: Boolean;
property TabIndex: Integer;
property TabOrder: TTabOrder;
property TabPosition: TWinXPTabPosition;
property Tabs: TStrings;
property TabStop: Boolean;
property Visible: Boolean;
function CanChange: Boolean;
function CanShowTab(ATabIndex: Integer): Boolean;
procedure Change;
function Changing: Boolean;
function CreateTabs: TStrings;
procedure DrawTab(ATabIndex: Integer; const ARect: IDispatch; AActive: Boolean);
function GetTabIndex: Integer;
function IndexOfTabAt(X: Integer; Y: Integer): Integer;
function IsTabUseImage(Index: Integer): Boolean;
function IsTabVisible(Index: Integer): Boolean;
procedure ScrollTabs(Delta: Integer);
procedure SelectNextPage(GoForward: Boolean);
procedure SetActiveTabIndex(const Value: Integer);
procedure SetFocusAfterTabChange;
function TabRect(Index: Integer): IDispatch;
procedure UpdateActivePage;

## TWinXPPageControl
继承：TWinXPPageControl → TWinXPCustomTabControl → TXPCustomControl → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：XPPageControl

property ActivePage: TWinXPTabSheet;
property ActivePageIndex: Integer;
property PageCount: Integer;  // read-only
property Pages[Index: ?]: TWinXPTabSheet;  // read-only
property SmoothDraw: Boolean;
property TabIndex: Integer;
function FindNextPage(CurPage: TWinXPTabSheet; GoForward: Boolean; CheckTabVisible: Boolean): TWinXPTabSheet;
procedure InsertPage(Page: TWinXPTabSheet);
procedure InsertPageAt(Index: Integer; Page: TWinXPTabSheet);
procedure RemovePage(Page: TWinXPTabSheet);

## TWinXPTabControl
继承：TWinXPTabControl → TWinXPCustomTabControl → TXPCustomControl → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：XPPageControl

property SmoothDraw: Boolean;
property TabIndex: Integer;
property Tabs: TStrings;

## TWinXPTabControlMetrics
继承：TWinXPTabControlMetrics → TPersistent → TObject ｜ 单元：XPPageControl

property ActivePageBorderToTextIncrease: Integer;
property ActivePageWidthIncrease: Integer;
property BorderToFocusRectAbove: Integer;
property BorderToFocusRectBelow: Integer;
property BorderToFocusRectLeft: Integer;
property BorderToFocusRectRight: Integer;
property BorderToTextAbove: Integer;
property BorderToTextBelow: Integer;
property BorderToTextLeft: Integer;
property BorderToTextRight: Integer;
property BorderUpDownAbove: Integer;
property BorderUpDownBelow: Integer;
property DistanceToInactiveTab: Integer;
property ImageGap: Integer;
property MinTabWidth: Integer;
property RightSpaceAfterRightMostTab: Integer;
property TabSheetBorderSize: Integer;
procedure Create(AOwner: TWinXPCustomTabControl);

## TWinXPTabSheet
继承：TWinXPTabSheet → TXPCustomControl → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：XPPageControl

property BorderWidth: TBorderWidth;
property Caption: TCaption;
property Color: TColor;
property Constraints: TSizeConstraints;
property CustomHint: TCustomHint;
property DoubleBuffered: Boolean;
property DragMode: TDragMode;
property Enabled: Boolean;
property Font: TFont;
property Height: Integer;
property HelpContext: THelpContext;
property ImageIndex: Integer;
property Left: Integer;
property OnAlignInsertBefore: TAlignInsertBeforeEvent;
property OnAlignPosition: TAlignPositionEvent;
property OnContextPopup: TContextPopupEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnEndDrag: TEndDragEvent;
property OnEnter: TNotifyEvent;
property OnExit: TNotifyEvent;
property OnHide: TNotifyEvent;
property OnMouseActivate: TMouseActivateEvent;
property OnMouseDown: TMouseEvent;
property OnMouseEnter: TNotifyEvent;
property OnMouseLeave: TNotifyEvent;
property OnMouseMove: TMouseMoveEvent;
property OnMouseUp: TMouseEvent;
property OnResize: TNotifyEvent;
property OnShow: TNotifyEvent;
property OnStartDrag: TStartDragEvent;
property Padding: TPadding;
property PageControl: TWinXPPageControl;
property PageIndex: Integer;
property ParentColor: Boolean;
property ParentFont: Boolean;
property ParentShowHint: Boolean;
property PopupMenu: TPopupMenu;
property ShowHint: Boolean;
property TabIndex: Integer;  // read-only
property TabVisible: Boolean;
property Top: Integer;
property Visible: Boolean;
property Width: Integer;
procedure DoHide;
procedure DoShow;

## TWordField
继承：TWordField → TIntegerField → TNumericField → TField → TComponent → TPersistent → TObject ｜ 单元：Data.DB


## TWorkArea
继承：TWorkArea → TCollectionItem → TPersistent → TObject ｜ 单元：Vcl.ComCtrls

property Color: TColor;
property Rect: TRect;

## TWorkAreas
继承：TWorkAreas → TOwnedCollection → TCollection → TPersistent → TObject ｜ 单元：Vcl.ComCtrls

property Items[Index: ?]: TWorkArea;
function Add: TWorkArea;
procedure Delete(Index: Integer);
function Insert(Index: Integer): TWorkArea;

## TWriter
继承：TWriter → TFiler → TObject ｜ 单元：System.Classes

property Position: Longint;
property RootAncestor: TComponent;
property UseQualifiedNames: Boolean;
function FindMethodName(const AMethod: IDispatch): string;
procedure Write(const Buffer; Count: Integer);
procedure WriteBoolean(Value: Boolean);
procedure WriteChar(Value: Char);
procedure WriteCollection(const Value: TCollection);
procedure WriteComponent(Component: TComponent);
procedure WriteCurrency(const Value: Currency);
procedure WriteData(Instance: TComponent);
procedure WriteDate(const Value: TDateTime);
procedure WriteDescendent(const Root: TComponent; const AAncestor: TComponent);
procedure WriteDouble(const Value: Double);
procedure WriteFloat(const Value: Extended);
procedure WriteIdent(const Ident: string);
procedure WriteInteger(Value: Integer);
procedure WriteListBegin;
procedure WriteListEnd;
procedure WriteProperties(const Instance: TPersistent);
procedure WriteRootComponent(const Root: TComponent);
procedure WriteSignature;
procedure WriteSingle(const Value: Single);
procedure WriteStr(const Value: AnsiString);
procedure WriteString(const Value: string);
procedure WriteUTF8Str(const Value: string);
procedure WriteVar(const Buffer: AnsiChar; Count: Integer);
procedure WriteVariant(const Value: Variant);
procedure WriteWideChar(Value: Char);
procedure WriteWideString(const Value: string);

## TXCeedZip
继承：TXCeedZip → TObject ｜ 单元：XCeedApi.Stub

property BasePath: TDynamicString;
property EncryptionPassword: TDynamicString;
property PreservePaths: Boolean;
property ProcessSubfolders: Boolean;
property TempFolder: TDynamicString;
property UnzipToFolder: TDynamicString;
property UseTempFile: Boolean;
procedure AddFilesToProcess(AFileNames: string);
procedure Create(ZipFileName: string);
function GetErrorMessage(AError: Integer): string;
function TestZip: Boolean;
function UnZip: Integer;
function Zip: Integer;

## TXPBaseCustomSpeedButton
继承：TXPBaseCustomSpeedButton → TXPCustomTransparentControl → TXPCustomControl → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：XPExtCtrls

procedure AppearanceChanged(AChange: TAppearanceChange);
procedure CalculatePositions(const ARect: IDispatch; const TotalSize: IDispatch; const GlyphPos: IDispatch; const TextBounds: IDispatch);
procedure CopyToImage(AlphaImage: TAlphaBitmap);
procedure DrawFadingImage(Canvas: TCanvas; const ARect: IDispatch);
procedure DrawImage(Canvas: TCanvas; const ARect: IDispatch; AEnabled: Boolean);
function GetBaseButtonState: Integer;
function GetDrawCaptionFlags: TXPDrawCaptionFlags;
function GetEllipsisPosition: TEllipsisPosition;
function GetFadingEnabled: Boolean;
function GetGlyphSize(const GlyphSize: IDispatch; OriginalSize: Boolean): Boolean;
function GetShiftContentIfPressed: Boolean;
procedure KindChanged;
function NeedPaintDropdown: Boolean;
procedure PaintFading(const ARectDrop: IDispatch; APushed: Boolean);
procedure PaintStandard(const ARect: IDispatch; const ARectDrop: IDispatch; APushed: Boolean);
function PushOnClick: Boolean;
procedure RedrawCaption(const ARect: IDispatch; const ACaption: string; AFontColor: TColor);
procedure RedrawImage(const ARect: IDispatch);
procedure RedrawInside(const ARect: IDispatch; AFontColor: TColor; DoFontFading: Boolean);
procedure UpdateExclusive;
procedure VCLClick;

## TXPBaseCustomSpeedButtonAutomation
继承：TXPBaseCustomSpeedButtonAutomation → TControlAutomation → TControlAutomation ｜ 单元：XPExtCtrls


## TXPBitBtn
继承：TXPBitBtn → TXPCustomBitBtn → TWinXPCustomButton → TWinXPCustomButtonControl → TXPCustomControl → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：WinXPButtons

property Cancel: Boolean;
property Color: TColor;
property CustomImage: TAlphaBitmap;
property Default: Boolean;
property DisabledTextColor: TColor;
property FrameColor: TColor;
property Glyph: TPicture;
property HotColor: TColor;
property HotFrameColor: TColor;
property Kind: TBitBtnKind;
property Layout: TButtonLayout;
property LookAndFeel: TXPLookAndFeel;
property Margin: Integer;
property ModalResult: TModalResult;
property NumGlyphs: TNumGlyphs;
property Pressed: Boolean;
property PressedColor: TColor;
property ScaleGlyph: Boolean;
property ShowAccelChar: Boolean;
property ShowShieldIcon: Boolean;
property Spacing: Integer;
property Style: TXPButtonStyle;
property TabStop: Boolean;
property WordWrap: Boolean;

## TXPButton
继承：TXPButton → TXPCustomButton → TXPCustomControl → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：XPButton

property Align: TAlign;
property Alignment: TAlignment;
property Anchors: TAnchors;
property Bitmap: TBitmap;
property CanBeDown: Boolean;
property Cancel: Boolean;
property Canvas: TCanvas;  // read-only
property Caption: TCaption;
property Color: TColor;
property Constraints: TSizeConstraints;
property CustomHint: TCustomHint;
property DarkBitmap: TBitmap;
property Default: Boolean;
property DoubleBuffered: Boolean;
property Down: Boolean;
property DownBitmap: TBitmap;
property DownColor: TColor;
property DragCursor: TCursor;
property DragKind: TDragKind;
property DragMode: TDragMode;
property Enabled: Boolean;
property Font: TFont;
property FrameColor: TColor;
property Hint: string;
property HotBitmap: TBitmap;
property HotColor: TColor;
property HotFrameColor: TColor;
property LightBitmap: TBitmap;
property ModalResult: TModalResult;
property MultilineCaption: Boolean;
property OnClick: TNotifyEvent;
property OnContextPopup: TContextPopupEvent;
property OnCustomDraw: TXPButtonCustomDrawEvent;
property OnDblClick: TNotifyEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnEndDock: TEndDragEvent;
property OnEndDrag: TEndDragEvent;
property OnEnter: TNotifyEvent;
property OnExit: TNotifyEvent;
property OnKeyDown: TKeyEvent;
property OnKeyPress: TKeyPressEvent;
property OnKeyUp: TKeyEvent;
property OnlyDrawBitmap: Boolean;
property OnMouseActivate: TMouseActivateEvent;
property OnMouseDown: TMouseEvent;
property OnMouseEnter: TNotifyEvent;
property OnMouseHover: TXPMouseHoverEvent;
property OnMouseLeave: TNotifyEvent;
property OnMouseMove: TMouseMoveEvent;
property OnMouseUp: TMouseEvent;
property OnStartDock: TStartDockEvent;
property OnStartDrag: TStartDragEvent;
property ParentColor: Boolean;
property ParentFont: Boolean;
property ParentShowHint: Boolean;
property PopupMenu: TPopupMenu;
property PressedBitmap: TBitmap;
property PressedColor: TColor;
property ShiftOnPress: Boolean;
property ShowHint: Boolean;
property SmoothDraw: Boolean;
property TabOrder: TTabOrder;
property TabStop: Boolean;
property Visible: Boolean;

## TXPButtonEdit
继承：TXPButtonEdit → TXPCustomButtonEdit → TCustomXPEdit → TXPCustomControl → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：XPExtEdits

property Align: TAlign;
property Anchors: TAnchors;
property AutoSelect: Boolean;
property AutoSize: Boolean;
property BackImage: TBitmap;
property BorderStyle: TBorderStyle;
property Button2Hint: string;
property Button2Image: TPicture;
property ButtonAlignment: TLeftRight;
property ButtonHint: string;
property ButtonImage: TBitmap;
property CharCase: TEditCharCase;
property Color: TColor;
property Constraints: TSizeConstraints;
property Cursor: TCursor;
property CustomHint: TCustomHint;
property DoubleBuffered: Boolean;
property DragCursor: TCursor;
property DragKind: TDragKind;
property DragMode: TDragMode;
property DropDownGlyph: TBitmap;
property Enabled: Boolean;
property Font: TFont;
property FrameColor: TColor;
property HideSelection: Boolean;
property HotColor: TColor;
property HotTrack: Boolean;
property ImeMode: TImeMode;
property ImeName: TImeName;
property Layout: TTextLayout;
property LookAndFeel: TXPLookAndFeel;
property MaxLength: Integer;
property OEMConvert: Boolean;
property OnButton2Click: TNotifyEvent;
property OnButtonClick: TNotifyEvent;
property OnChange: TNotifyEvent;
property OnClick: TNotifyEvent;
property OnContextPopup: TContextPopupEvent;
property OnDblClick: TNotifyEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnEndDock: TEndDragEvent;
property OnEndDrag: TEndDragEvent;
property OnEnter: TNotifyEvent;
property OnExit: TNotifyEvent;
property OnKeyDown: TKeyEvent;
property OnKeyPress: TKeyPressEvent;
property OnKeyUp: TKeyEvent;
property OnMouseActivate: TMouseActivateEvent;
property OnMouseDown: TMouseEvent;
property OnMouseEnter: TNotifyEvent;
property OnMouseLeave: TNotifyEvent;
property OnMouseMove: TMouseMoveEvent;
property OnMouseUp: TMouseEvent;
property OnStartDock: TStartDockEvent;
property OnStartDrag: TStartDragEvent;
property Padding: TPadding;
property ParentColor: Boolean;
property ParentFont: Boolean;
property ParentShowHint: Boolean;
property PopupMenu: TPopupMenu;
property ReadOnly: Boolean;
property SelectedColor: TColor;
property SelectedTextColor: TColor;
property ShowButton: Boolean;
property ShowButton2: Boolean;
property ShowHint: Boolean;
property StretchButtonImage: Boolean;
property TabOrder: TTabOrder;
property TabStop: Boolean;
property Text: TCaption;
property Transparent: Boolean;
property Visible: Boolean;

## TXPButtonEx
继承：TXPButtonEx → TXPCustomButton → TXPCustomControl → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：XPButton

property Action: TBasicAction;
property Align: TAlign;
property Alignment: TAlignment;
property Anchors: TAnchors;
property BitmapIndex: Integer;
property CanBeDown: Boolean;
property Cancel: Boolean;
property Canvas: TCanvas;  // read-only
property Caption: TCaption;
property Color: TColor;
property Constraints: TSizeConstraints;
property CustomHint: TCustomHint;
property DarkBitmapIndex: Integer;
property Default: Boolean;
property DoubleBuffered: Boolean;
property Down: Boolean;
property DownBitmapIndex: Integer;
property DownColor: TColor;
property DragCursor: TCursor;
property DragKind: TDragKind;
property DragMode: TDragMode;
property Enabled: Boolean;
property Font: TFont;
property FrameColor: TColor;
property Hint: string;
property HotBitmapIndex: Integer;
property HotColor: TColor;
property HotFrameColor: TColor;
property Images: TCustomImageList;
property LightBitmapIndex: Integer;
property ModalResult: TModalResult;
property MultilineCaption: Boolean;
property OnClick: TNotifyEvent;
property OnContextPopup: TContextPopupEvent;
property OnCustomDraw: TXPButtonCustomDrawEvent;
property OnDblClick: TNotifyEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnEndDock: TEndDragEvent;
property OnEndDrag: TEndDragEvent;
property OnEnter: TNotifyEvent;
property OnExit: TNotifyEvent;
property OnKeyDown: TKeyEvent;
property OnKeyPress: TKeyPressEvent;
property OnKeyUp: TKeyEvent;
property OnlyDrawBitmap: Boolean;
property OnMouseActivate: TMouseActivateEvent;
property OnMouseDown: TMouseEvent;
property OnMouseEnter: TNotifyEvent;
property OnMouseHover: TXPMouseHoverEvent;
property OnMouseLeave: TNotifyEvent;
property OnMouseMove: TMouseMoveEvent;
property OnMouseUp: TMouseEvent;
property OnStartDock: TStartDockEvent;
property OnStartDrag: TStartDragEvent;
property ParentColor: Boolean;
property ParentFont: Boolean;
property ParentShowHint: Boolean;
property PopupMenu: TPopupMenu;
property PressedBitmapIndex: Integer;
property PressedColor: TColor;
property ShiftOnPress: Boolean;
property ShowHint: Boolean;
property SmoothDraw: Boolean;
property TabOrder: TTabOrder;
property TabStop: Boolean;
property Transparent: Boolean;
property Visible: Boolean;

## TXPCheckBox
继承：TXPCheckBox → TXPCheckControl → TWinXPCustomButtonControl → TXPCustomControl → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：WinXPButtons

property AllowGrayed: Boolean;
property Checked: Boolean;
property State: TCheckBoxState;

## TXPCheckBoxesControl
继承：TXPCheckBoxesControl → TXPCustomControl → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：XPCheckSet

property Align: TAlign;
property Alignment: TLeftRight;
property Anchors: TAnchors;
property AutoSize: Boolean;
property CBEnabled[Index: ?]: Boolean;
property CheckBoxes: TXPCheckBoxItems;
property Checked[Index: ?]: Boolean;
property Color: TColor;
property Constraints: TSizeConstraints;
property CustomHint: TCustomHint;
property DoubleBuffered: Boolean;
property DragCursor: TCursor;
property DragKind: TDragKind;
property DragMode: TDragMode;
property Enabled: Boolean;
property EqualColumns: Boolean;
property Font: TFont;
property HorizontalGap: Integer;
property OnCanResize: TCanResizeEvent;
property OnClick: TNotifyEvent;
property OnConstrainedResize: TConstrainedResizeEvent;
property OnContextPopup: TContextPopupEvent;
property OnDblClick: TNotifyEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnEndDock: TEndDragEvent;
property OnEndDrag: TEndDragEvent;
property OnEnter: TNotifyEvent;
property OnExit: TNotifyEvent;
property OnGetSiteInfo: TGetSiteInfoEvent;
property OnMouseActivate: TMouseActivateEvent;
property OnMouseDown: TMouseEvent;
property OnMouseEnter: TNotifyEvent;
property OnMouseLeave: TNotifyEvent;
property OnMouseMove: TMouseMoveEvent;
property OnMouseUp: TMouseEvent;
property OnResize: TNotifyEvent;
property OnStartDock: TStartDockEvent;
property OnStartDrag: TStartDragEvent;
property ParentColor: Boolean;
property ParentFont: Boolean;
property ParentShowHint: Boolean;
property PopupMenu: TPopupMenu;
property ShowHint: Boolean;
property SmoothDraw: Boolean;
property TabOrder: TTabOrder;
property TabStop: Boolean;
property VerticalGap: Integer;
property Visible: Boolean;
procedure BeginUpdate;
procedure EndUpdate;

## TXPCheckBoxItem
继承：TXPCheckBoxItem → TCollectionItem → TPersistent → TObject ｜ 单元：XPCheckSet

property Caption: TCaption;
property Checked: Boolean;
property Enabled: Boolean;
property OnClick: TNotifyEvent;
property Tag: Integer;
property Visible: Boolean;

## TXPCheckBoxItems
继承：TXPCheckBoxItems → TOwnedCollection → TCollection → TPersistent → TObject ｜ 单元：XPCheckSet

property Items[Index: ?]: TXPCheckBoxItem;

## TXPCheckControl
继承：TXPCheckControl → TWinXPCustomButtonControl → TXPCustomControl → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：WinXPButtons

property Alignment: TLeftRight;
property Checked: Boolean;
property CheckImage: TPicture;
property Color: TColor;
property DrawFocusRect: Boolean;
property LookAndFeel: TXPLookAndFeel;
property OnDblClick: TNotifyEvent;
property ParentColor: Boolean;
property TabStop: Boolean;
property WordWrap: Boolean;
function GetAlphaImage: TAlphaImage;
function GetChecked: Boolean;
function GetFrameCtrlStateFlags: Integer;
function GetPartId: Integer;
function GetStateBase: TThemedButton;
procedure ReDrawCaption(AColor: TColor; AFontColor: TColor);
procedure SetChecked(Value: Boolean);
procedure Toggle;

## TXPCheckControlAutomation
继承：TXPCheckControlAutomation → TBaseControlAutomation → TBaseControlAutomation ｜ 单元：WinXPButtons

function Get_ToggleState(out pRetVal: TOleEnum): HRESULT;
function Toggle: HRESULT;

## TXPColorsImageList
继承：TXPColorsImageList → TObject ｜ 单元：XPImages

property ColorsImageList: TImageList;  // read-only
procedure Create(Width: Integer; Height: Integer);
function FindOrCreateColorImageIndex(AColor: TColor): Integer;

## TXPComboBox
继承：TXPComboBox → TXPCustomComboBox → TXPCustomButtonEdit → TCustomXPEdit → TXPCustomControl → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：XPCombo

property Align: TAlign;
property AlphaNumericSorting: Boolean;
property Anchors: TAnchors;
property AutoComplete: Boolean;
property AutoCompleteDelay: Cardinal;
property AutoDropDown: Boolean;
property AutoDropWidth: Boolean;
property AutoSelect: Boolean;
property AutoSize: Boolean;
property BackImage: TBitmap;
property BackImageCorner: Integer;
property BodyButtonImage: TBitmap;
property BorderStyle: TBorderStyle;
property Button2Image: TPicture;
property ButtonImage: TBitmap;
property CaseSensitive: Boolean;
property CharCase: TEditCharCase;
property Color: TColor;
property Constraints: TSizeConstraints;
property Ctl3D: Boolean;
property CustomHint: TCustomHint;
property DoubleBuffered: Boolean;
property DragCursor: TCursor;
property DragKind: TDragKind;
property DragMode: TDragMode;
property DrawFocusRect: Boolean;
property DropDownCount: Integer;
property DropDownGlyph: TBitmap;
property Enabled: Boolean;
property Font: TFont;
property FrameColor: TColor;
property HideSelection: Boolean;
property HotColor: TColor;
property HotTrack: Boolean;
property ImeMode: TImeMode;
property ImeName: TImeName;
property ItemHeight: Integer;
property ItemIndex: Integer;
property Items: TStrings;
property LookAndFeel: TXPLookAndFeel;
property MaxLength: Integer;
property NoItemText: TCaption;
property OEMConvert: Boolean;
property OnButton2Click: TNotifyEvent;
property OnButtonClick: TNotifyEvent;
property OnChange: TNotifyEvent;
property OnClick: TNotifyEvent;
property OnCloseUp: TNotifyEvent;
property OnContextPopup: TContextPopupEvent;
property OnDblClick: TNotifyEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnDraw: TDrawEvent;
property OnDrawItem: TDrawItemEvent;
property OnDropDown: TNotifyEvent;
property OnEndDock: TEndDragEvent;
property OnEndDrag: TEndDragEvent;
property OnEnter: TNotifyEvent;
property OnExit: TNotifyEvent;
property OnKeyDown: TKeyEvent;
property OnKeyPress: TKeyPressEvent;
property OnKeyUp: TKeyEvent;
property OnMouseActivate: TMouseActivateEvent;
property OnMouseDown: TMouseEvent;
property OnMouseEnter: TNotifyEvent;
property OnMouseLeave: TNotifyEvent;
property OnMouseMove: TMouseMoveEvent;
property OnMouseUp: TMouseEvent;
property OnSelect: TNotifyEvent;
property OnStartDock: TStartDockEvent;
property OnStartDrag: TStartDragEvent;
property ParentColor: Boolean;
property ParentCtl3D: Boolean;
property ParentFont: Boolean;
property ParentShowHint: Boolean;
property PopupMenu: TPopupMenu;
property ReadOnly: Boolean;
property SelectedColor: TColor;
property SelectedTextColor: TColor;
property ShowButton: Boolean;
property ShowButton2: Boolean;
property ShowHint: Boolean;
property Sorted: Boolean;
property StretchButtonImage: Boolean;
property Style: TXPComboBoxStyle;
property TabOrder: TTabOrder;
property TabStop: Boolean;
property Text: TCaption;
property Transparent: Boolean;
property Visible: Boolean;

## TXPCustomBitBtn
继承：TXPCustomBitBtn → TWinXPCustomButton → TWinXPCustomButtonControl → TXPCustomControl → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：WinXPButtons


## TXPCustomButton
继承：TXPCustomButton → TXPCustomControl → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：XPButton

property MenuDropped: Boolean;
property State: TXPButtonState;
procedure DoMouseHover(State: TMouseState);
procedure InternalPaint(const ARect: IDispatch);
procedure Prepaint(const ARect: IDispatch);

## TXPCustomButtonControlAutomation
继承：TXPCustomButtonControlAutomation → TControlAutomation → TControlAutomation ｜ 单元：XPButton


## TXPCustomButtonEdit
继承：TXPCustomButtonEdit → TCustomXPEdit → TXPCustomControl → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：XPEdits2

property WantsReturn: Boolean;
procedure Button2Click;
procedure ButtonClick;
procedure CtrlEnterClick;
procedure DoAdjustClientRect(const Rect: IDispatch);
function GetButtonDetails(AButton: TXPEditButton): IDispatch;
function GetButtonVisible(AButton: TXPEditButton; AVisible: Boolean): Boolean;
function GetDefaultGlyph: TGraphic;
function GetGlyph(AButton: TXPEditButton): TGraphic;
procedure PaintButton(AButton: TXPEditButton);
procedure PaintGlyph(AButton: TXPEditButton; const ARect: IDispatch);
procedure SetButtonVisibility;

## TXPCustomComboBox
继承：TXPCustomComboBox → TXPCustomButtonEdit → TCustomXPEdit → TXPCustomControl → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：XPCombo

property Canvas: TCanvas;  // read-only
property DroppedDown: Boolean;
property ItemIndex: Integer;
property Items: TStrings;
procedure CloseUp;
procedure DropDown;
function GetPopupItemWidth(Index: Integer): Integer;
function GetPopupPosition: IDispatch;
procedure Select;
function UserCanOpenDropDown: Boolean;

## TXPCustomComboBoxAutomation
继承：TXPCustomComboBoxAutomation → TBaseControlAutomation → TBaseControlAutomation ｜ 单元：XPCombo

function Collapse: HRESULT;
function Expand: HRESULT;
function Get_ExpandCollapseState(out pRetVal: TOleEnum): HRESULT;

## TXPCustomControl
继承：TXPCustomControl → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：XPControls

procedure ClearModified;
function GetModified: Boolean;
procedure UpdateSmoothDraw;

## TXPCustomExtPanel
继承：TXPCustomExtPanel → TXPCustomControl → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：XPPanels

property Canvas: TCanvas;  // read-only
procedure BeginUpdate;
function DoCreateRegion: HRGN;
procedure EndUpdate;
function GetDrawingMode: TXPDrawingMode;
function UseRegion: Boolean;

## TXPCustomGraphicButton
继承：TXPCustomGraphicButton → TGraphicControl → TControl → TComponent → TPersistent → TObject ｜ 单元：XPButton


## TXPCustomGroupBox
继承：TXPCustomGroupBox → TXPCustomControl → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：XPGroups


## TXPCustomLabel
继承：TXPCustomLabel → TCustomLabel → TGraphicControl → TControl → TComponent → TPersistent → TObject ｜ 单元：XPLabels

function CalculateAutoSize(const ACaption: string; AWidth: Integer; AFont: TFont; AWordWrap: Boolean; ASmoothDraw: Boolean; AExpandTabs: Boolean; AEllipsisPosition: TEllipsisPosition; AOrientation: TXPTextOrientation; AShowAccelChar: Boolean; ASunkenDisabled: Boolean; AGlyph: TPicture; AFactor: Integer): IDispatch;
function DoPaintBackground: Boolean;
procedure DrawTextEvent(ACanvas: TCanvas; const ARect: IDispatch; const ACaption: string; AFont: TFont; AFontColor: TColor; AAlignment: TAlignment; ALayout: TTextLayout; AFlags: TXPDrawCaptionFlags; AEllipsis: TEllipsisPosition);
procedure NavigateLink;

## TXPCustomMultiButton
继承：TXPCustomMultiButton → TXPCustomControl → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：XPButtonSet

procedure ReDrawInside(AIndex: Integer; const ARect: IDispatch; AFontColor: TColor);

## TXPCustomMultiImageButton
继承：TXPCustomMultiImageButton → TXPCustomMultiButton → TXPCustomControl → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：XPButtonSet

property Images: TCustomImageList;

## TXPCustomRadioGroup
继承：TXPCustomRadioGroup → TXPCustomGroupBox → TXPCustomControl → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：XPGroups


## TXPCustomSpeedButton
继承：TXPCustomSpeedButton → TXPBaseCustomSpeedButton → TXPCustomTransparentControl → TXPCustomControl → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：XPExtCtrls

procedure GetGlyphInfo(out GlyphToDraw: TGraphic; out NumGlyphsToDraw: Integer);
function GetImageState: Integer;
procedure GlyphChanged(Sender: TObject);

## TXPCustomTransparentControl
继承：TXPCustomTransparentControl → TXPCustomControl → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：XPControls

procedure TransparentChanged;

## TXPDirectoryEdit
继承：TXPDirectoryEdit → TXPCustomButtonEdit → TCustomXPEdit → TXPCustomControl → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：XPExtEdits

property AcceptFiles: Boolean;
property Align: TAlign;
property Anchors: TAnchors;
property AutoSelect: Boolean;
property AutoSize: Boolean;
property BackImage: TBitmap;
property BorderStyle: TBorderStyle;
property ButtonImage: TBitmap;
property CharCase: TEditCharCase;
property Color: TColor;
property Constraints: TSizeConstraints;
property Cursor: TCursor;
property CustomHint: TCustomHint;
property DialogText: string;
property DoubleBuffered: Boolean;
property DragCursor: TCursor;
property DragKind: TDragKind;
property DragMode: TDragMode;
property DropDownGlyph: TBitmap;
property Enabled: Boolean;
property Font: TFont;
property FrameColor: TColor;
property HideSelection: Boolean;
property HotColor: TColor;
property HotTrack: Boolean;
property ImeMode: TImeMode;
property ImeName: TImeName;
property InitialDir: string;
property Layout: TTextLayout;
property LookAndFeel: TXPLookAndFeel;
property MaxLength: Integer;
property MultipleDirs: Boolean;
property OEMConvert: Boolean;
property OnButtonClick: TNotifyEvent;
property OnChange: TNotifyEvent;
property OnClick: TNotifyEvent;
property OnContextPopup: TContextPopupEvent;
property OnDblClick: TNotifyEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnDropFiles: TNotifyEvent;
property OnEndDock: TEndDragEvent;
property OnEndDrag: TEndDragEvent;
property OnEnter: TNotifyEvent;
property OnExit: TNotifyEvent;
property OnKeyDown: TKeyEvent;
property OnKeyPress: TKeyPressEvent;
property OnKeyUp: TKeyEvent;
property OnMouseActivate: TMouseActivateEvent;
property OnMouseDown: TMouseEvent;
property OnMouseEnter: TNotifyEvent;
property OnMouseLeave: TNotifyEvent;
property OnMouseMove: TMouseMoveEvent;
property OnMouseUp: TMouseEvent;
property OnStartDock: TStartDockEvent;
property OnStartDrag: TStartDragEvent;
property Options: TSelectDirExtOpts;
property Padding: TPadding;
property ParentColor: Boolean;
property ParentFont: Boolean;
property ParentShowHint: Boolean;
property PopupMenu: TPopupMenu;
property ReadOnly: Boolean;
property SelectedColor: TColor;
property SelectedTextColor: TColor;
property ShowHint: Boolean;
property StretchButtonImage: Boolean;
property TabOrder: TTabOrder;
property TabStop: Boolean;
property Text: TCaption;
property Transparent: Boolean;
property Visible: Boolean;

## TXPDoubleRect
继承：TXPDoubleRect → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：XPExtCtrls

property Align: TAlign;
property Anchors: TAnchors;
property BottomCaption: string;
property Color: TColor;
property Connection: TXDoubleRectConnection;
property ConnectionColor: TColor;
property ConnectionWidth: Integer;
property Constraints: TSizeConstraints;
property CustomHint: TCustomHint;
property DoubleBuffered: Boolean;
property DragCursor: TCursor;
property DragKind: TDragKind;
property DragMode: TDragMode;
property Enabled: Boolean;
property FillColor: TColor;
property Font: TFont;
property FrameColor: TColor;
property FrameWidth: Integer;
property Margin: Integer;
property OnClick: TNotifyEvent;
property OnConnectionChange: TNotifyEvent;
property OnContextPopup: TContextPopupEvent;
property OnDblClick: TNotifyEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnEndDock: TEndDragEvent;
property OnEndDrag: TEndDragEvent;
property OnEnter: TNotifyEvent;
property OnExit: TNotifyEvent;
property OnMouseActivate: TMouseActivateEvent;
property OnMouseDown: TMouseEvent;
property OnMouseEnter: TNotifyEvent;
property OnMouseLeave: TNotifyEvent;
property OnMouseMove: TMouseMoveEvent;
property OnMouseUp: TMouseEvent;
property OnResize: TNotifyEvent;
property OnStartDock: TStartDockEvent;
property OnStartDrag: TStartDragEvent;
property ParentColor: Boolean;
property ParentFont: Boolean;
property ParentShowHint: Boolean;
property PopupMenu: TPopupMenu;
property ShowHint: Boolean;
property TabOrder: TTabOrder;
property TabStop: Boolean;
property TopCaption: string;
property Visible: Boolean;
procedure DoConnectionChange;

## TXPEdit
继承：TXPEdit → TCustomXPEdit → TXPCustomControl → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：XPEdits2

property Align: TAlign;
property Anchors: TAnchors;
property AutoSelect: Boolean;
property AutoSize: Boolean;
property BackImage: TBitmap;
property BorderStyle: TBorderStyle;
property CharCase: TEditCharCase;
property Color: TColor;
property Constraints: TSizeConstraints;
property Ctl3D: Boolean;
property Cursor: TCursor;
property CustomHint: TCustomHint;
property DisabledColor: TColor;
property DoubleBuffered: Boolean;
property DragCursor: TCursor;
property DragKind: TDragKind;
property DragMode: TDragMode;
property EmptyCaption: string;
property EmptyCaptionFont: TFont;
property Enabled: Boolean;
property Font: TFont;
property FrameColor: TColor;
property HideSelection: Boolean;
property HotTrack: Boolean;
property ImeMode: TImeMode;
property ImeName: TImeName;
property Layout: TTextLayout;
property LookAndFeel: TXPLookAndFeel;
property MaxLength: Integer;
property NumberPrecision: TPrecision;
property NumberRadix: TRadix;
property NumberType: TNumberTypeEx;
property NumberValue: Double;
property OEMConvert: Boolean;
property OnChange: TNotifyEvent;
property OnClick: TNotifyEvent;
property OnContextPopup: TContextPopupEvent;
property OnDblClick: TNotifyEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnEndDock: TEndDragEvent;
property OnEndDrag: TEndDragEvent;
property OnEnter: TNotifyEvent;
property OnExit: TNotifyEvent;
property OnKeyDown: TKeyEvent;
property OnKeyPress: TKeyPressEvent;
property OnKeyUp: TKeyEvent;
property OnMouseActivate: TMouseActivateEvent;
property OnMouseDown: TMouseEvent;
property OnMouseEnter: TNotifyEvent;
property OnMouseLeave: TNotifyEvent;
property OnMouseMove: TMouseMoveEvent;
property OnMouseUp: TMouseEvent;
property OnMouseWheel: TMouseWheelEvent;
property OnMouseWheelDown: TMouseWheelUpDownEvent;
property OnMouseWheelUp: TMouseWheelUpDownEvent;
property OnStartDock: TStartDockEvent;
property OnStartDrag: TStartDragEvent;
property Padding: TPadding;
property ParentColor: Boolean;
property ParentCtl3D: Boolean;
property ParentFont: Boolean;
property ParentShowHint: Boolean;
property PasswordChar: Char;
property PopupMenu: TPopupMenu;
property ReadOnly: Boolean;
property SelectedColor: TColor;
property SelectedTextColor: TColor;
property ShowHint: Boolean;
property TabOrder: TTabOrder;
property TabStop: Boolean;
property Text: TCaption;
property Transparent: Boolean;
property Visible: Boolean;

## TXPEditButton
继承：TXPEditButton → TSpeedButton → TGraphicControl → TControl → TComponent → TPersistent → TObject ｜ 单元：XPEdits2

property Hot: Boolean;

## TXPEditResourceManager
继承：TXPEditResourceManager → TObject ｜ 单元：XPEdits2

function ComboButton: TBitmap;
function ComboButtonGlyph: TBitmap;
function DirectoryGlyph: TBitmap;
function EllipsisGlyph: TBitmap;
function FileNameGlyph: TBitmap;

## TXPExtPanel
继承：TXPExtPanel → TXPCustomExtPanel → TXPCustomControl → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：XPPanels

property Align: TAlign;
property Alignment: TAlignment;
property AlphaBlendValue: Byte;
property Anchors: TAnchors;
property AutoSize: Boolean;
property BeginColor: TColor;
property Bitmap: TBitmap;
property BitmapTransparent: Boolean;
property BorderColor: TColor;
property BorderWidth: TBorderWidth;
property Caption: TCaption;
property Color: TColor;
property Constraints: TSizeConstraints;
property CustomHint: TCustomHint;
property DockSite: Boolean;
property DoubleBuffered: Boolean;
property DragCursor: TCursor;
property DragKind: TDragKind;
property DragMode: TDragMode;
property Enabled: Boolean;
property EndColor: TColor;
property Font: TFont;
property GradientStyle: TGradientPanelStyle;
property Kind: TXPExtPanelKind;
property Layout: TTextLayout;
property OnAlignInsertBefore: TAlignInsertBeforeEvent;
property OnAlignPosition: TAlignPositionEvent;
property OnCanResize: TCanResizeEvent;
property OnClick: TNotifyEvent;
property OnConstrainedResize: TConstrainedResizeEvent;
property OnContextPopup: TContextPopupEvent;
property OnDblClick: TNotifyEvent;
property OnDockDrop: TDockDropEvent;
property OnDockOver: TDockOverEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnEndDock: TEndDragEvent;
property OnEndDrag: TEndDragEvent;
property OnEnter: TNotifyEvent;
property OnExit: TNotifyEvent;
property OnGetSiteInfo: TGetSiteInfoEvent;
property OnMouseActivate: TMouseActivateEvent;
property OnMouseDown: TMouseEvent;
property OnMouseEnter: TNotifyEvent;
property OnMouseLeave: TNotifyEvent;
property OnMouseMove: TMouseMoveEvent;
property OnMouseUp: TMouseEvent;
property OnPaint: TNotifyEvent;
property OnResize: TNotifyEvent;
property OnStartDock: TStartDockEvent;
property OnStartDrag: TStartDragEvent;
property OnUnDock: TUnDockEvent;
property Padding: TPadding;
property ParentColor: Boolean;
property ParentFont: Boolean;
property ParentShowHint: Boolean;
property PopupMenu: TPopupMenu;
property Radius: Integer;
property RoundCorners: Boolean;
property ShowBorder: Boolean;
property ShowBottom: Boolean;
property ShowHint: Boolean;
property ShowLeft: Boolean;
property ShowRight: Boolean;
property ShowTop: Boolean;
property Stretching: TXPGraphicStretching;
property TabOrder: TTabOrder;
property TabStop: Boolean;
property Transparent: Boolean;
property UseDefaultColor: Boolean;
property UseDockManager: Boolean;
property Visible: Boolean;

## TXPFileNameEdit
继承：TXPFileNameEdit → TXPCustomButtonEdit → TCustomXPEdit → TXPCustomControl → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：XPExtEdits

property AcceptFiles: Boolean;
property Align: TAlign;
property Anchors: TAnchors;
property AutoSelect: Boolean;
property AutoSize: Boolean;
property BackImage: TBitmap;
property BorderStyle: TBorderStyle;
property ButtonImage: TBitmap;
property CharCase: TEditCharCase;
property Color: TColor;
property Constraints: TSizeConstraints;
property Cursor: TCursor;
property CustomHint: TCustomHint;
property DefaultExt: string;
property DoubleBuffered: Boolean;
property DragCursor: TCursor;
property DragKind: TDragKind;
property DragMode: TDragMode;
property DropDownGlyph: TBitmap;
property Enabled: Boolean;
property Filter: string;
property FilterIndex: Integer;
property Font: TFont;
property FrameColor: TColor;
property HideSelection: Boolean;
property HotColor: TColor;
property HotTrack: Boolean;
property ImeMode: TImeMode;
property ImeName: TImeName;
property InitialDir: string;
property Layout: TTextLayout;
property LookAndFeel: TXPLookAndFeel;
property MaxLength: Integer;
property OEMConvert: Boolean;
property OnAfterDialog: TAfterDialogEvent;
property OnBeforeDialog: TBeforeDialogEvent;
property OnButtonClick: TNotifyEvent;
property OnChange: TNotifyEvent;
property OnClick: TNotifyEvent;
property OnContextPopup: TContextPopupEvent;
property OnDblClick: TNotifyEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnDropFiles: TNotifyEvent;
property OnEndDock: TEndDragEvent;
property OnEndDrag: TEndDragEvent;
property OnEnter: TNotifyEvent;
property OnExit: TNotifyEvent;
property OnKeyDown: TKeyEvent;
property OnKeyPress: TKeyPressEvent;
property OnKeyUp: TKeyEvent;
property OnMouseActivate: TMouseActivateEvent;
property OnMouseDown: TMouseEvent;
property OnMouseEnter: TNotifyEvent;
property OnMouseLeave: TNotifyEvent;
property OnMouseMove: TMouseMoveEvent;
property OnMouseUp: TMouseEvent;
property OnStartDock: TStartDockEvent;
property OnStartDrag: TStartDragEvent;
property Options: TOpenOptions;
property Padding: TPadding;
property ParentColor: Boolean;
property ParentFont: Boolean;
property ParentShowHint: Boolean;
property PopupMenu: TPopupMenu;
property ReadOnly: Boolean;
property SelectedColor: TColor;
property SelectedTextColor: TColor;
property ShowHint: Boolean;
property StretchButtonImage: Boolean;
property TabOrder: TTabOrder;
property TabStop: Boolean;
property Text: TCaption;
property Title: string;
property Transparent: Boolean;
property UseSaveDialog: Boolean;
property Visible: Boolean;
procedure DoAfterDialog(ADialog: TOpenDialog; ASuccess: Boolean);
procedure DoBeforeDialog(ADialog: TOpenDialog);

## TXPFloatSpinEdit
继承：TXPFloatSpinEdit → TCustomXPFloatSpinEdit → TBaseXPSpinEdit → TCustomXPEdit → TXPCustomControl → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：XPEdits2

property Align: TAlign;
property Anchors: TAnchors;
property AutoSelect: Boolean;
property AutoSize: Boolean;
property BackImage: TBitmap;
property BorderStyle: TBorderStyle;
property Color: TColor;
property Constraints: TSizeConstraints;
property Cursor: TCursor;
property CustomHint: TCustomHint;
property DoubleBuffered: Boolean;
property DragCursor: TCursor;
property DragKind: TDragKind;
property DragMode: TDragMode;
property EditorEnabled: Boolean;
property Enabled: Boolean;
property Font: TFont;
property FrameColor: TColor;
property HideSelection: Boolean;
property HotTrack: Boolean;
property Increment: Double;
property MaxLength: Integer;
property MaxValue: Double;
property MinValue: Double;
property OnChange: TNotifyEvent;
property OnClick: TNotifyEvent;
property OnContextPopup: TContextPopupEvent;
property OnDblClick: TNotifyEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnEndDock: TEndDragEvent;
property OnEndDrag: TEndDragEvent;
property OnEnter: TNotifyEvent;
property OnExit: TNotifyEvent;
property OnKeyDown: TKeyEvent;
property OnKeyPress: TKeyPressEvent;
property OnKeyUp: TKeyEvent;
property OnMouseActivate: TMouseActivateEvent;
property OnMouseDown: TMouseEvent;
property OnMouseEnter: TNotifyEvent;
property OnMouseLeave: TNotifyEvent;
property OnMouseMove: TMouseMoveEvent;
property OnMouseUp: TMouseEvent;
property OnStartDock: TStartDockEvent;
property OnStartDrag: TStartDragEvent;
property ParentColor: Boolean;
property ParentFont: Boolean;
property ParentShowHint: Boolean;
property PopupMenu: TPopupMenu;
property ReadOnly: Boolean;
property SelectedColor: TColor;
property SelectedTextColor: TColor;
property ShowHint: Boolean;
property TabOrder: TTabOrder;
property TabStop: Boolean;
property Transparent: Boolean;
property Value: Double;
property Visible: Boolean;

## TXPGradient
继承：TXPGradient → TOwnedCollection → TCollection → TPersistent → TObject ｜ 单元：InstrumentClasses

procedure Create(AOwner: TPersistent);
function FindColorStopIndex(APosition: TXPPercent): Integer;
procedure InsertColorStop(APosition: TXPPercent; AColor: TColor);
procedure RemoveColorStop(APosition: TXPPercent);
procedure SortColorStops;

## TXPGradientColorStop
继承：TXPGradientColorStop → TXPGradientItem → TCollectionItem → TPersistent → TObject ｜ 单元：InstrumentClasses

property Color: TColor;

## TXPGradientItem
继承：TXPGradientItem → TCollectionItem → TPersistent → TObject ｜ 单元：InstrumentClasses

property Position: TXPPercent;
procedure Changed;

## TXPGraphicButton
继承：TXPGraphicButton → TXPCustomGraphicButton → TGraphicControl → TControl → TComponent → TPersistent → TObject ｜ 单元：XPButton

property Align: TAlign;
property Anchors: TAnchors;
property Caption: TCaption;
property Color: TColor;
property Constraints: TSizeConstraints;
property CustomHint: TCustomHint;
property DragCursor: TCursor;
property DragKind: TDragKind;
property DragMode: TDragMode;
property Enabled: Boolean;
property Font: TFont;
property Glyph: TBitmap;
property Hint: string;
property OnClick: TNotifyEvent;
property OnContextPopup: TContextPopupEvent;
property OnDblClick: TNotifyEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnEndDock: TEndDragEvent;
property OnEndDrag: TEndDragEvent;
property OnMouseActivate: TMouseActivateEvent;
property OnMouseDown: TMouseEvent;
property OnMouseEnter: TNotifyEvent;
property OnMouseLeave: TNotifyEvent;
property OnMouseMove: TMouseMoveEvent;
property OnMouseUp: TMouseEvent;
property OnStartDock: TStartDockEvent;
property OnStartDrag: TStartDragEvent;
property ParentColor: Boolean;
property ParentFont: Boolean;
property ParentShowHint: Boolean;
property PopupMenu: TPopupMenu;
property ShiftOnPress: Boolean;
property ShowHint: Boolean;
property Visible: Boolean;

## TXPGroupBox
继承：TXPGroupBox → TXPCustomGroupBox → TXPCustomControl → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：XPGroups

property Align: TAlign;
property Anchors: TAnchors;
property Caption: TCaption;
property Constraints: TSizeConstraints;
property CustomHint: TCustomHint;
property DockSite: Boolean;
property DoubleBuffered: Boolean;
property DragCursor: TCursor;
property DragKind: TDragKind;
property DragMode: TDragMode;
property Enabled: Boolean;
property Font: TFont;
property FrameColor: TColor;
property HeaderBorderColor: TColor;
property HeaderColor: TColor;
property HeaderTextColor: TColor;
property LookAndFeel: TXPLookAndFeel;
property OnAlignInsertBefore: TAlignInsertBeforeEvent;
property OnAlignPosition: TAlignPositionEvent;
property OnClick: TNotifyEvent;
property OnContextPopup: TContextPopupEvent;
property OnDblClick: TNotifyEvent;
property OnDockDrop: TDockDropEvent;
property OnDockOver: TDockOverEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnEndDock: TEndDragEvent;
property OnEndDrag: TEndDragEvent;
property OnEnter: TNotifyEvent;
property OnExit: TNotifyEvent;
property OnGetSiteInfo: TGetSiteInfoEvent;
property OnMouseActivate: TMouseActivateEvent;
property OnMouseDown: TMouseEvent;
property OnMouseEnter: TNotifyEvent;
property OnMouseLeave: TNotifyEvent;
property OnMouseMove: TMouseMoveEvent;
property OnMouseUp: TMouseEvent;
property OnStartDock: TStartDockEvent;
property OnStartDrag: TStartDragEvent;
property OnUnDock: TUnDockEvent;
property Options: TXPGroupBoxOptions;
property Padding: TPadding;
property ParentFont: Boolean;
property ParentShowHint: Boolean;
property PopupMenu: TPopupMenu;
property ShowHint: Boolean;
property SmoothDraw: Boolean;
property TabOrder: TTabOrder;
property TabStop: Boolean;
property UseDockManager: Boolean;
property Visible: Boolean;

## TXPHistoryEdit
继承：TXPHistoryEdit → TXPCustomComboBox → TXPCustomButtonEdit → TCustomXPEdit → TXPCustomControl → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：XPExtEdits

property AddToHistoryOnExit: Boolean;
property Align: TAlign;
property AlphaNumericSorting: Boolean;
property Anchors: TAnchors;
property AutoComplete: Boolean;
property AutoCompleteDelay: Cardinal;
property AutoDropDown: Boolean;
property AutoDropWidth: Boolean;
property AutoSelect: Boolean;
property AutoSize: Boolean;
property BackImage: TBitmap;
property BorderStyle: TBorderStyle;
property Button2Image: TPicture;
property ButtonImage: TBitmap;
property CaseSensitive: Boolean;
property CharCase: TEditCharCase;
property Color: TColor;
property Constraints: TSizeConstraints;
property CustomHint: TCustomHint;
property DoubleBuffered: Boolean;
property DragCursor: TCursor;
property DragKind: TDragKind;
property DragMode: TDragMode;
property DropDownCount: Integer;
property DropDownGlyph: TBitmap;
property Enabled: Boolean;
property Font: TFont;
property FrameColor: TColor;
property HideSelection: Boolean;
property HotColor: TColor;
property HotTrack: Boolean;
property ImeMode: TImeMode;
property ImeName: TImeName;
property ItemHeight: Integer;
property ItemIndex: Integer;
property Items: TStrings;
property LookAndFeel: TXPLookAndFeel;
property MaxLength: Integer;
property OEMConvert: Boolean;
property OnButton2Click: TNotifyEvent;
property OnButtonClick: TNotifyEvent;
property OnChange: TNotifyEvent;
property OnClick: TNotifyEvent;
property OnCloseUp: TNotifyEvent;
property OnContextPopup: TContextPopupEvent;
property OnDblClick: TNotifyEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnDrawItem: TDrawItemEvent;
property OnDropDown: TNotifyEvent;
property OnEndDock: TEndDragEvent;
property OnEndDrag: TEndDragEvent;
property OnEnter: TNotifyEvent;
property OnEnterHit: TNotifyEvent;
property OnExit: TNotifyEvent;
property OnKeyDown: TKeyEvent;
property OnKeyPress: TKeyPressEvent;
property OnKeyUp: TKeyEvent;
property OnMouseActivate: TMouseActivateEvent;
property OnMouseDown: TMouseEvent;
property OnMouseEnter: TNotifyEvent;
property OnMouseLeave: TNotifyEvent;
property OnMouseMove: TMouseMoveEvent;
property OnMouseUp: TMouseEvent;
property OnSelect: TNotifyEvent;
property OnStartDock: TStartDockEvent;
property OnStartDrag: TStartDragEvent;
property ParentColor: Boolean;
property ParentFont: Boolean;
property ParentShowHint: Boolean;
property PopupMenu: TPopupMenu;
property ReadOnly: Boolean;
property RegKey: string;
property SelectedColor: TColor;
property SelectedTextColor: TColor;
property ShowButton: Boolean;
property ShowButton2: Boolean;
property ShowHint: Boolean;
property Sorted: Boolean;
property Style: TXPComboBoxStyle;
property TabOrder: TTabOrder;
property TabStop: Boolean;
property Text: TCaption;
property Transparent: Boolean;
property Visible: Boolean;
procedure EmptyHistory;
procedure HistoryChanged;
procedure LoadHistory;
procedure SaveHistory;

## TXPHotTrack
继承：TXPHotTrack → TPersistent → TObject ｜ 单元：XPLabels

property HotCursor: TCursor;
property HotFontColor: TColor;
property HotFontStyle: TFontStyles;
property TrackCursor: Boolean;
property TrackFontColor: Boolean;
property TrackFontStyle: Boolean;
procedure Create;

## TXPImageList
继承：TXPImageList → TImageList → TDragImageList → TCustomImageList → TBaseImageList ｜ 单元：XPImages


## TXPLabel
继承：TXPLabel → TXPCustomLabel → TCustomLabel → TGraphicControl → TControl → TComponent → TPersistent → TObject ｜ 单元：XPLabels

property Action: TBasicAction;
property Align: TAlign;
property Alignment: TAlignment;
property Anchors: TAnchors;
property AutoSize: Boolean;
property Caption: TCaption;
property Color: TColor;
property Constraints: TSizeConstraints;
property CustomHint: TCustomHint;
property DisabledFontColor: TColor;
property DragCursor: TCursor;
property DragKind: TDragKind;
property DragMode: TDragMode;
property EllipsisPosition: TEllipsisPosition;
property Enabled: Boolean;
property ExpandTabs: Boolean;
property FocusControl: TWinControl;
property Font: TFont;
property Glyph: TPicture;
property GlyphLayout: TXPGlyphLayout;
property HotTrack: TXPHotTrack;
property Layout: TTextLayout;
property LinkAddress: string;
property LinkStyle: TXPLinkStyle;
property OnClick: TNotifyEvent;
property OnContextPopup: TContextPopupEvent;
property OnDblClick: TNotifyEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnEndDock: TEndDragEvent;
property OnEndDrag: TEndDragEvent;
property OnMouseActivate: TMouseActivateEvent;
property OnMouseDown: TMouseEvent;
property OnMouseEnter: TNotifyEvent;
property OnMouseLeave: TNotifyEvent;
property OnMouseMove: TMouseMoveEvent;
property OnMouseUp: TMouseEvent;
property OnStartDock: TStartDockEvent;
property OnStartDrag: TStartDragEvent;
property Orientation: TXPTextOrientation;
property ParentColor: Boolean;
property ParentFont: Boolean;
property ParentShowHint: Boolean;
property PopupMenu: TPopupMenu;
property RevealCaptionInHint: Boolean;
property ScaleGlyph: Boolean;
property ShowAccelChar: Boolean;
property ShowHint: Boolean;
property SmoothDraw: Boolean;
property SunkenDisabled: Boolean;
property Transparent: Boolean;
property UnicodeText: string;
property Visible: Boolean;
property WordWrap: Boolean;

## TXPListBox
继承：TXPListBox → TCustomXPListBox → TXPCustomControl → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：XPLists

property Align: TAlign;
property AllowGrayed: Boolean;
property AlphaNumericSorting: Boolean;
property Anchors: TAnchors;
property AutoComplete: Boolean;
property AutoCompleteDelay: Cardinal;
property BorderStyle: TBorderStyle;
property Canvas: TCanvas;  // read-only
property Checked[Index: ?]: Boolean;
property Color: TColor;
property Columns: Cardinal;
property Constraints: TSizeConstraints;
property Count: Integer;  // read-only
property CustomHint: TCustomHint;
property DoubleBuffered: Boolean;
property DragCursor: TCursor;
property DragKind: TDragKind;
property DragMode: TDragMode;
property Enabled: Boolean;
property ExtendedSelect: Boolean;
property Font: TFont;
property HideSelection: Boolean;
property ItemHeight: Integer;
property ItemIndex: Integer;
property Items: TStrings;
property MultiSelect: Boolean;
property OnClick: TNotifyEvent;
property OnClickCheck: TNotifyEvent;
property OnContextPopup: TContextPopupEvent;
property OnDblClick: TNotifyEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnDrawItem: TDrawItemEvent;
property OnEndDock: TEndDragEvent;
property OnEndDrag: TEndDragEvent;
property OnEnter: TNotifyEvent;
property OnExit: TNotifyEvent;
property OnKeyDown: TKeyEvent;
property OnKeyPress: TKeyPressEvent;
property OnKeyUp: TKeyEvent;
property OnMouseActivate: TMouseActivateEvent;
property OnMouseDown: TMouseEvent;
property OnMouseEnter: TNotifyEvent;
property OnMouseLeave: TNotifyEvent;
property OnMouseMove: TMouseMoveEvent;
property OnMouseUp: TMouseEvent;
property OnSelectionChanged: TNotifyEvent;
property OnStartDock: TStartDockEvent;
property OnStartDrag: TStartDragEvent;
property ParentColor: Boolean;
property ParentFont: Boolean;
property ParentShowHint: Boolean;
property PopupMenu: TPopupMenu;
property ScrollBars: TXPScrollStyle;
property SelCount: Integer;  // read-only
property Selected[Index: ?]: Boolean;
property ShowHint: Boolean;
property Sorted: Boolean;
property State[Index: ?]: TCheckBoxState;
property Style: TXPListBoxStyle;
property TabOrder: TTabOrder;
property TabStop: Boolean;
property TopIndex: Integer;
property UseCheckBoxes: Boolean;
property Visible: Boolean;

## TXPMultiButton
继承：TXPMultiButton → TXPCustomMultiButton → TXPCustomControl → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：XPButtonSet

property Align: TAlign;
property Anchors: TAnchors;
property Captions: TStrings;
property Color: TColor;
property Constraints: TSizeConstraints;
property CustomHint: TCustomHint;
property DoubleBuffered: Boolean;
property DragCursor: TCursor;
property DragKind: TDragKind;
property DragMode: TDragMode;
property Enabled: Boolean;
property Font: TFont;
property MultilineCaption: Boolean;
property OnButtonClick: TButtonClickEvent;
property OnContextPopup: TContextPopupEvent;
property OnCustomDraw: TDrawEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnEndDock: TEndDragEvent;
property OnEndDrag: TEndDragEvent;
property OnEnter: TNotifyEvent;
property OnExit: TNotifyEvent;
property OnKeyDown: TKeyEvent;
property OnKeyPress: TKeyPressEvent;
property OnKeyUp: TKeyEvent;
property OnMouseActivate: TMouseActivateEvent;
property OnMouseDown: TMouseEvent;
property OnMouseEnter: TNotifyEvent;
property OnMouseLeave: TNotifyEvent;
property OnMouseMove: TMouseMoveEvent;
property OnMouseUp: TMouseEvent;
property OnStartDock: TStartDockEvent;
property OnStartDrag: TStartDragEvent;
property ParentColor: Boolean;
property ParentFont: Boolean;
property ParentShowHint: Boolean;
property PopupMenu: TPopupMenu;
property ShowHint: Boolean;
property SmoothDraw: Boolean;
property TabOrder: TTabOrder;
property TabStop: Boolean;
property Visible: Boolean;

## TXPMultiImageButton
继承：TXPMultiImageButton → TXPCustomMultiImageButton → TXPCustomMultiButton → TXPCustomControl → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：XPButtonSet

property Align: TAlign;
property Anchors: TAnchors;
property Color: TColor;
property Constraints: TSizeConstraints;
property CustomHint: TCustomHint;
property DoubleBuffered: Boolean;
property DragCursor: TCursor;
property DragKind: TDragKind;
property DragMode: TDragMode;
property Enabled: Boolean;
property OnButtonClick: TButtonClickEvent;
property OnContextPopup: TContextPopupEvent;
property OnCustomDraw: TDrawEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnEndDock: TEndDragEvent;
property OnEndDrag: TEndDragEvent;
property OnEnter: TNotifyEvent;
property OnExit: TNotifyEvent;
property OnKeyDown: TKeyEvent;
property OnKeyPress: TKeyPressEvent;
property OnKeyUp: TKeyEvent;
property OnMouseActivate: TMouseActivateEvent;
property OnMouseDown: TMouseEvent;
property OnMouseEnter: TNotifyEvent;
property OnMouseLeave: TNotifyEvent;
property OnMouseMove: TMouseMoveEvent;
property OnMouseUp: TMouseEvent;
property OnStartDock: TStartDockEvent;
property OnStartDrag: TStartDragEvent;
property ParentColor: Boolean;
property ParentFont: Boolean;
property ParentShowHint: Boolean;
property PopupMenu: TPopupMenu;
property ShowHint: Boolean;
property SmoothDraw: Boolean;
property TabOrder: TTabOrder;
property TabStop: Boolean;
property Visible: Boolean;

## TXPNonFlickingControl
继承：TXPNonFlickingControl → TXPCustomTransparentControl → TXPCustomControl → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：XPControls


## TXPPanel
继承：TXPPanel → TPanel → TCustomPanel → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：XPButton

property Canvas: TCanvas;  // read-only
property CaptionPos: TCaptionPos;
property DrawLines: Boolean;
property ShowTab: Boolean;
property Transparent: Boolean;
function IsPointOnCaptionText(X: Integer; Y: Integer): Boolean;

## TXPPopupListBox
继承：TXPPopupListBox → TCustomXPListBox → TXPCustomControl → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：XPCombo

property Canvas: TCanvas;  // read-only
property Items: TStrings;
function CanProcessKey(ACharCode: Word): Boolean;
procedure Close(Success: Boolean);
procedure Popup(X: Integer; Y: Integer);

## TXPProgressBar
继承：TXPProgressBar → TXPCustomControl → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：XPProgress

property Align: TAlign;
property Anchors: TAnchors;
property BackgroundColor: TColor;
property BackImage: TAlphaBitmap;
property BackImageCornerSize: Integer;
property BarColor: TColor;
property BarImage: TAlphaBitmap;
property BarImageCornerSize: Integer;
property BarPadding: Integer;
property Constraints: TSizeConstraints;
property CustomHint: TCustomHint;
property DoubleBuffered: Boolean;
property DragCursor: TCursor;
property DragKind: TDragKind;
property DragMode: TDragMode;
property Enabled: Boolean;
property FrameColor: TColor;
property LookAndFeel: TXPLookAndFeel;
property MarqueeInterval: Integer;
property Max: Integer;
property Min: Integer;
property OnContextPopup: TContextPopupEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnEndDock: TEndDragEvent;
property OnEndDrag: TEndDragEvent;
property OnEnter: TNotifyEvent;
property OnExit: TNotifyEvent;
property OnMouseActivate: TMouseActivateEvent;
property OnMouseDown: TMouseEvent;
property OnMouseEnter: TNotifyEvent;
property OnMouseLeave: TNotifyEvent;
property OnMouseMove: TMouseMoveEvent;
property OnMouseUp: TMouseEvent;
property OnPostPaint: TNotifyEvent;
property OnStartDock: TStartDockEvent;
property OnStartDrag: TStartDragEvent;
property Orientation: TProgressBarOrientation;
property ParentColor: Boolean;
property ParentDoubleBuffered: Boolean;
property ParentShowHint: Boolean;
property PopupMenu: TPopupMenu;
property Position: Integer;
property ShowHint: Boolean;
property Smooth: Boolean;
property State: TProgressBarState;
property Step: Integer;
property Style: TProgressBarStyle;
property TabOrder: TTabOrder;
property TabStop: Boolean;
property Visible: Boolean;
procedure DoPostPaint;
procedure StepBy(Delta: Integer);
procedure StepIt;

## TXPRadioButton
继承：TXPRadioButton → TXPCheckControl → TWinXPCustomButtonControl → TXPCustomControl → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：WinXPButtons

property GroupIndex: Integer;

## TXPRadioGroup
继承：TXPRadioGroup → TXPCustomRadioGroup → TXPCustomGroupBox → TXPCustomControl → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：XPGroups

property Align: TAlign;
property Anchors: TAnchors;
property Buttons[Index: ?]: TXPRadioButton;  // read-only
property Caption: TCaption;
property Columns: Integer;
property Constraints: TSizeConstraints;
property CustomHint: TCustomHint;
property DoubleBuffered: Boolean;
property DragCursor: TCursor;
property DragKind: TDragKind;
property DragMode: TDragMode;
property Enabled: Boolean;
property Font: TFont;
property FrameColor: TColor;
property ItemIndex: Integer;
property Items: TStrings;
property LookAndFeel: TXPLookAndFeel;
property OnClick: TNotifyEvent;
property OnContextPopup: TContextPopupEvent;
property OnDblClick: TNotifyEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnEndDock: TEndDragEvent;
property OnEndDrag: TEndDragEvent;
property OnEnter: TNotifyEvent;
property OnExit: TNotifyEvent;
property OnMouseActivate: TMouseActivateEvent;
property OnMouseDown: TMouseEvent;
property OnMouseEnter: TNotifyEvent;
property OnMouseLeave: TNotifyEvent;
property OnMouseMove: TMouseMoveEvent;
property OnMouseUp: TMouseEvent;
property OnStartDock: TStartDockEvent;
property OnStartDrag: TStartDragEvent;
property Options: TXPGroupBoxOptions;
property ParentFont: Boolean;
property ParentShowHint: Boolean;
property PopupMenu: TPopupMenu;
property ShowHint: Boolean;
property SmoothDraw: Boolean;
property TabOrder: TTabOrder;
property TabStop: Boolean;
property Visible: Boolean;

## TXPScrollBar
继承：TXPScrollBar → TCustomXPScrollBar → TXPCustomControl → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：XPScrolls

property Align: TAlign;
property Anchors: TAnchors;
property ArrowImage: TPicture;
property ButtonColor: TColor;
property ButtonImage: TAlphaBitmap;
property Constraints: TSizeConstraints;
property CustomHint: TCustomHint;
property DisabledDarkColor: TColor;
property DisabledLightColor: TColor;
property DoubleBuffered: Boolean;
property DragCursor: TCursor;
property DragKind: TDragKind;
property DragMode: TDragMode;
property Enabled: Boolean;
property FrameColor: TColor;
property HotButtonColor: TColor;
property Kind: TScrollBarKind;
property LargeChange: TScrollBarInc;
property LookAndFeel: TXPLookAndFeel;
property Max: Integer;
property Min: Integer;
property OnChange: TNotifyEvent;
property OnContextPopup: TContextPopupEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnEndDock: TEndDragEvent;
property OnEndDrag: TEndDragEvent;
property OnEnter: TNotifyEvent;
property OnExit: TNotifyEvent;
property OnKeyDown: TKeyEvent;
property OnKeyPress: TKeyPressEvent;
property OnKeyUp: TKeyEvent;
property OnMouseEnter: TNotifyEvent;
property OnMouseLeave: TNotifyEvent;
property OnScroll: TScrollEvent;
property OnStartDock: TStartDockEvent;
property OnStartDrag: TStartDragEvent;
property PageSize: Integer;
property ParentShowHint: Boolean;
property PopupMenu: TPopupMenu;
property Position: Integer;
property ShaftColor: TColor;
property ShaftImage: TAlphaBitmap;
property ShowButtons: Boolean;
property ShowHint: Boolean;
property SmallChange: TScrollBarInc;
property TabOrder: TTabOrder;
property TabStop: Boolean;
property ThumbImage: TAlphaBitmap;
property Visible: Boolean;

## TXPScrollBox
继承：TXPScrollBox → TScrollingWinControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：XPButton

property Align: TAlign;
property Anchors: TAnchors;
property AutoScroll: Boolean;
property AutoScrollControls: Boolean;
property AutoSize: Boolean;
property BorderStyle: TBorderStyle;
property Color: TColor;
property Constraints: TSizeConstraints;
property CustomHint: TCustomHint;
property DockSite: Boolean;
property DoubleBuffered: Boolean;
property DragCursor: TCursor;
property DragKind: TDragKind;
property DragMode: TDragMode;
property Enabled: Boolean;
property EnableScrollButtons: Boolean;
property Font: TFont;
property OnAlignInsertBefore: TAlignInsertBeforeEvent;
property OnAlignPosition: TAlignPositionEvent;
property OnCanResize: TCanResizeEvent;
property OnClick: TNotifyEvent;
property OnConstrainedResize: TConstrainedResizeEvent;
property OnContextPopup: TContextPopupEvent;
property OnDblClick: TNotifyEvent;
property OnDockDrop: TDockDropEvent;
property OnDockOver: TDockOverEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnEndDock: TEndDragEvent;
property OnEndDrag: TEndDragEvent;
property OnEnter: TNotifyEvent;
property OnExit: TNotifyEvent;
property OnGetSiteInfo: TGetSiteInfoEvent;
property OnMouseActivate: TMouseActivateEvent;
property OnMouseDown: TMouseEvent;
property OnMouseEnter: TNotifyEvent;
property OnMouseLeave: TNotifyEvent;
property OnMouseMove: TMouseMoveEvent;
property OnMouseUp: TMouseEvent;
property OnMouseWheel: TMouseWheelEvent;
property OnMouseWheelDown: TMouseWheelUpDownEvent;
property OnMouseWheelUp: TMouseWheelUpDownEvent;
property OnResize: TNotifyEvent;
property OnScroll: TNotifyEvent;
property OnStartDock: TStartDockEvent;
property OnStartDrag: TStartDragEvent;
property OnUnDock: TUnDockEvent;
property Padding: TPadding;
property ParentColor: Boolean;
property ParentFont: Boolean;
property ParentShowHint: Boolean;
property PopupMenu: TPopupMenu;
property Position: Integer;
property ScrollDelay: Cardinal;
property ScrollDelta: Cardinal;
property ShowHint: Boolean;
property TabOrder: TTabOrder;
property TabStop: Boolean;
property Transparent: Boolean;
property UseDockManager: Boolean;
property Visible: Boolean;
procedure DoScroll;
procedure Reset;
procedure UpdateScrollButtons;

## TXPScrollDownButton
继承：TXPScrollDownButton → TXPButton → TXPCustomButton → TXPCustomControl → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：XPButton


## TXPScrollUpButton
继承：TXPScrollUpButton → TXPButton → TXPCustomButton → TXPCustomControl → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：XPButton


## TXPSpeedButton
继承：TXPSpeedButton → TXPCustomSpeedButton → TXPBaseCustomSpeedButton → TXPCustomTransparentControl → TXPCustomControl → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：XPExtCtrls

property Action: TBasicAction;
property Align: TAlign;
property AllowAllUp: Boolean;
property Anchors: TAnchors;
property Canvas: TCanvas;  // read-only
property Caption: TCaption;
property Color: TColor;
property Constraints: TSizeConstraints;
property CustomHint: TCustomHint;
property DoubleBuffered: Boolean;
property Down: Boolean;
property DragCursor: TCursor;
property DragKind: TDragKind;
property DragMode: TDragMode;
property DropdownMenu: TPopupMenu;
property Enabled: Boolean;
property FadeStrength: TXPFadeStrength;
property Flat: Boolean;
property Font: TFont;
property Glyph: TGraphic;
property GroupIndex: Integer;
property Kind: TXPSpeedKind;
property Layout: TButtonLayout;
property Margin: Integer;
property NumGlyphs: TNumGlyphs;
property OnClick: TNotifyEvent;
property OnContextPopup: TContextPopupEvent;
property OnDblClick: TNotifyEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnEndDock: TEndDragEvent;
property OnEndDrag: TEndDragEvent;
property OnMouseActivate: TMouseActivateEvent;
property OnMouseDown: TMouseEvent;
property OnMouseEnter: TNotifyEvent;
property OnMouseLeave: TNotifyEvent;
property OnMouseMove: TMouseMoveEvent;
property OnMouseUp: TMouseEvent;
property OnPaint: TXPSpeedButtonPaintEvent;
property OnStartDock: TStartDockEvent;
property OnStartDrag: TStartDragEvent;
property ParentColor: Boolean;
property ParentFont: Boolean;
property ParentShowHint: Boolean;
property PopupMenu: TPopupMenu;
property ScaleGlyph: Boolean;
property ShiftContent: Boolean;
property ShowAccelChar: Boolean;
property ShowHint: Boolean;
property SmoothDraw: Boolean;
property Spacing: Integer;
property Style: TXPSpeedStyle;
property Transparent: Boolean;
property Visible: Boolean;

## TXPSpeedButtonActionLink
继承：TXPSpeedButtonActionLink → TControlActionLink → TActionLink → TContainedActionLink ｜ 单元：XPExtCtrls


## TXPSpinEdit
继承：TXPSpinEdit → TCustomXPSpinEdit → TBaseXPSpinEdit → TCustomXPEdit → TXPCustomControl → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：XPEdits2

property Align: TAlign;
property Anchors: TAnchors;
property AutoSelect: Boolean;
property AutoSize: Boolean;
property BackImage: TBitmap;
property BorderStyle: TBorderStyle;
property Color: TColor;
property Constraints: TSizeConstraints;
property Cursor: TCursor;
property CustomHint: TCustomHint;
property DoubleBuffered: Boolean;
property DragCursor: TCursor;
property DragKind: TDragKind;
property DragMode: TDragMode;
property EditorEnabled: Boolean;
property Enabled: Boolean;
property Font: TFont;
property FrameColor: TColor;
property HideSelection: Boolean;
property HotTrack: Boolean;
property Increment: Integer;
property MaxLength: Integer;
property MaxValue: Integer;
property MinValue: Integer;
property OnChange: TNotifyEvent;
property OnClick: TNotifyEvent;
property OnContextPopup: TContextPopupEvent;
property OnDblClick: TNotifyEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnEndDock: TEndDragEvent;
property OnEndDrag: TEndDragEvent;
property OnEnter: TNotifyEvent;
property OnExit: TNotifyEvent;
property OnKeyDown: TKeyEvent;
property OnKeyPress: TKeyPressEvent;
property OnKeyUp: TKeyEvent;
property OnMouseActivate: TMouseActivateEvent;
property OnMouseDown: TMouseEvent;
property OnMouseEnter: TNotifyEvent;
property OnMouseLeave: TNotifyEvent;
property OnMouseMove: TMouseMoveEvent;
property OnMouseUp: TMouseEvent;
property OnStartDock: TStartDockEvent;
property OnStartDrag: TStartDragEvent;
property ParentColor: Boolean;
property ParentFont: Boolean;
property ParentShowHint: Boolean;
property PopupMenu: TPopupMenu;
property ReadOnly: Boolean;
property SelectedColor: TColor;
property SelectedTextColor: TColor;
property ShowHint: Boolean;
property TabOrder: TTabOrder;
property TabStop: Boolean;
property Transparent: Boolean;
property Value: Integer;
property Visible: Boolean;

## TXPSpinnerImage
继承：TXPSpinnerImage → TImage → TGraphicControl → TControl → TComponent → TPersistent → TObject ｜ 单元：XPImages

function CreateGraphic: TGraphic;
procedure LoadSpinnerPicture(APicture: TPicture);

## TXPSplitButton
继承：TXPSplitButton → TXPBitBtn → TXPCustomBitBtn → TWinXPCustomButton → TWinXPCustomButtonControl → TXPCustomControl → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：XPSplitButton

property AutoAddCloseButton: Boolean;
property DropDownMenu: TPopupMenu;
property OnAfterHidePopup: TNotifyEvent;
property OnAfterPopupCreated: TNotifyEvent;
property OnBeforeShowPopup: TNotifyEvent;
property PopupControl: TWinControl;
procedure AfterHidePopup;
procedure AfterPopupCreated;
procedure BeforeShowPopup;
procedure ShowPopup(const ScreenPoint: IDispatch);

## TXPSplitter
继承：TXPSplitter → TSplitter → TGraphicControl → TControl → TComponent → TPersistent → TObject ｜ 单元：XPExtCtrls

property DrawNotch: Boolean;
property IsResizing: Boolean;  // read-only
property NotchColor: TColor;
property NotchCount: Integer;
property NotchGap: Integer;
property NotchShadow: TColor;
property Transparent: Boolean;
property UseDefaultColor: Boolean;

## TXPTrackBar
继承：TXPTrackBar → TXPCustomControl → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：XPTrack

property Align: TAlign;
property Anchors: TAnchors;
property Constraints: TSizeConstraints;
property CustomHint: TCustomHint;
property DoubleBuffered: Boolean;
property DragCursor: TCursor;
property DragKind: TDragKind;
property DragMode: TDragMode;
property DrawFocusRect: Boolean;
property Enabled: Boolean;
property Font: TFont;
property Frequency: Integer;
property LineSize: Integer;
property Max: Integer;
property Metrics: TXPTrackBarMetrics;  // read-only
property Min: Integer;
property OnChange: TNotifyEvent;
property OnContextPopup: TContextPopupEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnEndDock: TEndDragEvent;
property OnEndDrag: TEndDragEvent;
property OnEnter: TNotifyEvent;
property OnExit: TNotifyEvent;
property OnGetPositionToolTipInfo: TGetTextEvent;
property OnGetValueText: TGetValueText;
property OnKeyDown: TKeyEvent;
property OnKeyPress: TKeyPressEvent;
property OnKeyUp: TKeyEvent;
property OnPaintThumb: TXPTrackBarPaintEvent;
property OnPaintTrack: TXPTrackBarPaintEvent;
property OnResize: TNotifyEvent;
property OnStartDock: TStartDockEvent;
property OnStartDrag: TStartDragEvent;
property Orientation: TTrackBarOrientation;
property PageSize: Integer;
property ParentShowHint: Boolean;
property PopupMenu: TPopupMenu;
property Position: Integer;
property PositionToolTip: TPositionToolTip;
property SelEnd: Integer;
property SelStart: Integer;
property ShowHint: Boolean;
property SliderVisible: Boolean;
property TabOrder: TTabOrder;
property TabStop: Boolean;
property ThumbLength: Integer;
property TickColor: TColor;
property TickMarks: TTickMark;
property TickStyle: TTickStyle;
property ValueDisplay: TValueDisplay;
property Visible: Boolean;
procedure ClearTicks;
procedure DoChange;
function GetTickColor: TColor;
procedure SetTick(Value: Integer);

## TXPTrackBarMetrics
继承：TXPTrackBarMetrics → TPersistent → TObject ｜ 单元：XPTrack

property MaxHintWidth: Integer;
property StdBigSize: Integer;
property StdSmallSize: Integer;
property ThumbGap: Integer;
property TickEdge: Integer;
property TickGap: Integer;
property TickNormal: Integer;
property TickWidth: Integer;
property TrackMargin: Integer;
property TrackWidth: Integer;
property ValueGap: Integer;
property XPBigSize: Integer;
property XPSmallSize: Integer;
procedure Create(AOwner: TXPTrackBar);

## TXPTransButton
继承：TXPTransButton → TGraphicControl → TControl → TComponent → TPersistent → TObject ｜ 单元：XPExtCtrls

property Inverted: Boolean;
procedure Create(AOwner: TComponent; const AResName: string; AInversible: Boolean);
procedure UpdateGlyph(const AResName: string);

## TXPUpDown
继承：TXPUpDown → TXPCustomControl → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：XPExtCtrls

property Align: TAlign;
property Anchors: TAnchors;
property Constraints: TSizeConstraints;
property CustomHint: TCustomHint;
property DoubleBuffered: Boolean;
property DownEnabled: Boolean;
property DragCursor: TCursor;
property DragKind: TDragKind;
property DragMode: TDragMode;
property Enabled: Boolean;
property Flat: Boolean;
property Kind: TUpDownKind;
property OnCustomDraw: TXPUpDownCustomDrawEvent;
property OnDownClick: TNotifyEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnEndDock: TEndDragEvent;
property OnEndDrag: TEndDragEvent;
property OnMouseActivate: TMouseActivateEvent;
property OnMouseDown: TMouseEvent;
property OnMouseEnter: TNotifyEvent;
property OnMouseLeave: TNotifyEvent;
property OnMouseMove: TMouseMoveEvent;
property OnMouseUp: TMouseEvent;
property OnStartDock: TStartDockEvent;
property OnStartDrag: TStartDragEvent;
property OnUpClick: TNotifyEvent;
property ParentShowHint: Boolean;
property PopupMenu: TPopupMenu;
property ShowHint: Boolean;
property UpEnabled: Boolean;
property Visible: Boolean;
procedure DownClick;
procedure ReDrawButton(const ARect: IDispatch; APressed: Boolean; AHot: Boolean; AIsUp: Boolean);
procedure UpClick;

## TxpWebBrowser
继承：TxpWebBrowser → TWebBrowser → TWebBrowser ｜ 单元：XPExtCtrls

property OnScriptError: TScriptErrorEvent;

## TXPWideSpinEdit
继承：TXPWideSpinEdit → TCustomXPWideSpinEdit → TBaseXPSpinEdit → TCustomXPEdit → TXPCustomControl → TCustomControl → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：XPEdits2

property Align: TAlign;
property Anchors: TAnchors;
property AutoSelect: Boolean;
property AutoSize: Boolean;
property BackImage: TBitmap;
property BorderStyle: TBorderStyle;
property Color: TColor;
property Constraints: TSizeConstraints;
property Cursor: TCursor;
property CustomHint: TCustomHint;
property DoubleBuffered: Boolean;
property DragCursor: TCursor;
property DragKind: TDragKind;
property DragMode: TDragMode;
property EditorEnabled: Boolean;
property Enabled: Boolean;
property Font: TFont;
property FrameColor: TColor;
property HideSelection: Boolean;
property HotTrack: Boolean;
property Increment: Int64;
property MaxLength: Integer;
property MaxValue: Int64;
property MinValue: Int64;
property OnChange: TNotifyEvent;
property OnClick: TNotifyEvent;
property OnContextPopup: TContextPopupEvent;
property OnDblClick: TNotifyEvent;
property OnDragDrop: TDragDropEvent;
property OnDragOver: TDragOverEvent;
property OnEndDock: TEndDragEvent;
property OnEndDrag: TEndDragEvent;
property OnEnter: TNotifyEvent;
property OnExit: TNotifyEvent;
property OnKeyDown: TKeyEvent;
property OnKeyPress: TKeyPressEvent;
property OnKeyUp: TKeyEvent;
property OnMouseActivate: TMouseActivateEvent;
property OnMouseDown: TMouseEvent;
property OnMouseEnter: TNotifyEvent;
property OnMouseLeave: TNotifyEvent;
property OnMouseMove: TMouseMoveEvent;
property OnMouseUp: TMouseEvent;
property OnStartDock: TStartDockEvent;
property OnStartDrag: TStartDragEvent;
property ParentColor: Boolean;
property ParentFont: Boolean;
property ParentShowHint: Boolean;
property PopupMenu: TPopupMenu;
property ReadOnly: Boolean;
property SelectedColor: TColor;
property SelectedTextColor: TColor;
property ShowHint: Boolean;
property TabOrder: TTabOrder;
property TabStop: Boolean;
property Transparent: Boolean;
property Value: Int64;
property Visible: Boolean;

## TXStatusBar
继承：TXStatusBar → TStatusBar → TCustomStatusBar → TWinControl → TControl → TComponent → TPersistent → TObject ｜ 单元：XPStatus


## TXStatusPanel
继承：TXStatusPanel → TStatusPanel → TCollectionItem → TPersistent → TObject ｜ 单元：XPStatus

property InsideControl: TControl;
property Panel: TPanel;  // read-only
procedure UpdatePanel;

## TXStatusPanels
继承：TXStatusPanels → TStatusPanels → TCollection → TPersistent → TObject ｜ 单元：XPStatus


## UnsafeAttribute
继承：UnsafeAttribute → TCustomAttribute → TObject ｜ 单元：System


## VolatileAttribute
继承：VolatileAttribute → TCustomAttribute → TObject ｜ 单元：System


## WeakAttribute
继承：WeakAttribute → TCustomAttribute → TObject ｜ 单元：System


