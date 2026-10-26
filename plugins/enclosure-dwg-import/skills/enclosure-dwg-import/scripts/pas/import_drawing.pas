{ Mechanical-layer drawing from drawing.txt (shell_import.py). Run through run_altium_script, timeout_seconds 600.
  L <mech> <name> <colour as decimal $00BBGGRR or empty> : enable and name the layer, set its colour
  T <mech> x1 y1 x2 y2 width / A <mech> cx cy r a0 a1 width : mm relative to the board origin
  Before adding, every track/arc/text that is not part of a component and lies on one of the L layers is removed:
  those layers belong to the import. }
S1 := '@@PCBDOC@@';
S3 := '@@DATA@@';
Client.ShowDocument(Client.OpenDocument('PCB', S1));
Obj1 := PCBServer.GetCurrentPCBBoard;
if Obj1.FileName <> S1 then ResultText := 'WRONG document: ' + Obj1.FileName
else begin
  SandboxLog('load');
  List1 := TStringList.Create; List1.LoadFromFile(S3);
  Obj5 := TStringList.Create; Obj5.Delimiter := #9; Obj5.StrictDelimiter := True;
  S2 := ',';
  I1 := 0;
  while I1 < List1.Count do begin
    Obj5.DelimitedText := List1[I1];
    if Obj5[0] = 'L' then S2 := S2 + IntToStr(eMechanical1 + StrToInt(Obj5[1]) - 1) + ',';
    I1 := I1 + 1;
  end;

  SandboxLog('collect old');
  Obj4 := TInterfaceList.Create;
  Obj2 := Obj1.BoardIterator_Create;
  Obj2.AddFilter_ObjectSet(MkSet(eTrackObject, eArcObject, eTextObject));
  Obj2.AddFilter_AllLayers;
  Obj2.AddFilter_Method(eProcessAll);
  Obj3 := Obj2.FirstPCBObject;
  while Obj3 <> nil do begin
    if not Obj3.InComponent then
      if Pos(',' + IntToStr(Obj3.Layer) + ',', S2) > 0 then Obj4.Add(Obj3);
    Obj3 := Obj2.NextPCBObject;
  end;
  Obj1.BoardIterator_Destroy(Obj2);
  SandboxLog('remove ' + IntToStr(Obj4.Count));
  PCBServer.PreProcess;
  I3 := 0;
  while I3 < Obj4.Count do begin
    Obj3 := Obj4.Items[I3];
    Obj1.RemovePCBObject(Obj3);
    PCBServer.SendMessageToRobots(Obj1.I_ObjectAddress, c_Broadcast, PCBM_BoardRegisteration, Obj3.I_ObjectAddress);
    I3 := I3 + 1;
  end;
  S2 := 'removed=' + IntToStr(Obj4.Count);
  Obj4.Free;

  SandboxLog('create');
  I1 := 0; I2 := 0;
  while I1 < List1.Count do begin
    Obj5.DelimitedText := List1[I1];
    S1 := Obj5[0];
    if S1 = 'L' then begin
      I3 := eMechanical1 + StrToInt(Obj5[1]) - 1;
      Obj1.LayerStack_V7.LayerObject_V7[I3].MechanicalLayerEnabled := True;
      Obj1.LayerStack_V7.LayerObject_V7[I3].Name := Obj5[2];
      Obj1.LayerIsDisplayed[I3] := True;
      if Obj5.Count > 3 then
        if Obj5[3] <> '' then PCBServer.SystemOptions.LayerColors_V6[I3] := StrToInt(Obj5[3]);
    end else if S1 = 'T' then begin
      Obj2 := PCBServer.PCBObjectFactory(eTrackObject, eNoDimension, eCreate_Default);
      Obj2.X1 := Obj1.XOrigin + MMsToCoord(StrToFloat(Obj5[2]));
      Obj2.Y1 := Obj1.YOrigin + MMsToCoord(StrToFloat(Obj5[3]));
      Obj2.X2 := Obj1.XOrigin + MMsToCoord(StrToFloat(Obj5[4]));
      Obj2.Y2 := Obj1.YOrigin + MMsToCoord(StrToFloat(Obj5[5]));
      Obj2.Width := MMsToCoord(StrToFloat(Obj5[6]));
      Obj2.Layer := eMechanical1 + StrToInt(Obj5[1]) - 1;
      Obj1.AddPCBObject(Obj2);
      PCBServer.SendMessageToRobots(Obj1.I_ObjectAddress, c_Broadcast, PCBM_BoardRegisteration, Obj2.I_ObjectAddress);
      I2 := I2 + 1;
    end else if S1 = 'A' then begin
      Obj2 := PCBServer.PCBObjectFactory(eArcObject, eNoDimension, eCreate_Default);
      Obj2.XCenter := Obj1.XOrigin + MMsToCoord(StrToFloat(Obj5[2]));
      Obj2.YCenter := Obj1.YOrigin + MMsToCoord(StrToFloat(Obj5[3]));
      Obj2.Radius := MMsToCoord(StrToFloat(Obj5[4]));
      Obj2.StartAngle := StrToFloat(Obj5[5]);
      Obj2.EndAngle := StrToFloat(Obj5[6]);
      Obj2.LineWidth := MMsToCoord(StrToFloat(Obj5[7]));
      Obj2.Layer := eMechanical1 + StrToInt(Obj5[1]) - 1;
      Obj1.AddPCBObject(Obj2);
      PCBServer.SendMessageToRobots(Obj1.I_ObjectAddress, c_Broadcast, PCBM_BoardRegisteration, Obj2.I_ObjectAddress);
      I2 := I2 + 1;
    end;
    I1 := I1 + 1;
  end;
  PCBServer.PostProcess;
  Obj5.Free; List1.Free;
  Obj1.ViewManager_FullUpdate;
  ResultText := S2 + ' created=' + IntToStr(I2);
end;
