{ Rooms and height rules from rules.txt (shell_import.py). Run through run_altium_script, timeout_seconds 600
  (each room takes seconds in passes 2 and 3).
  D <prefix>                       : first remove every rule whose name starts with <prefix>
  R name layer drc scope comment minx miny n, then n lines V x y : Room (Kind 1), mm relative to the board origin
  H name max min scope comment     : Height rule, preferred = max
  P name                           : after everything, an empty modify in file order (the last one ends at priority 1) }
S1 := '@@PCBDOC@@';
S3 := '@@DATA@@';
Client.ShowDocument(Client.OpenDocument('PCB', S1));
Obj1 := PCBServer.GetCurrentPCBBoard;
if Obj1.FileName <> S1 then ResultText := 'WRONG document: ' + Obj1.FileName
else begin
  SandboxLog('load');
  List1 := TStringList.Create; List1.LoadFromFile(S3);
  Obj5 := TStringList.Create; Obj5.Delimiter := #9; Obj5.StrictDelimiter := True;
  DbDoc := TStringList.Create;      { name prefixes to clean up }
  I1 := 0;
  while I1 < List1.Count do begin
    Obj5.DelimitedText := List1[I1];
    if Obj5[0] = 'D' then DbDoc.Add(Obj5[1]);
    I1 := I1 + 1;
  end;

  // ---------- cleanup: rules a previous run created
  SandboxLog('cleanup');
  Obj4 := TInterfaceList.Create;
  Obj2 := Obj1.BoardIterator_Create;
  Obj2.AddFilter_ObjectSet(MkSet(eRuleObject));
  Obj2.AddFilter_LayerSet(AllLayers); Obj2.AddFilter_Method(eProcessAll);
  Obj3 := Obj2.FirstPCBObject;
  while Obj3 <> nil do begin
    I1 := 0;
    while I1 < DbDoc.Count do begin
      if Pos(DbDoc[I1], Obj3.Name) = 1 then begin Obj4.Add(Obj3); I1 := DbDoc.Count; end;
      I1 := I1 + 1;
    end;
    Obj3 := Obj2.NextPCBObject;
  end;
  Obj1.BoardIterator_Destroy(Obj2);
  DbDoc.Free;
  SandboxLog('remove ' + IntToStr(Obj4.Count));
  PCBServer.PreProcess;
  I3 := 0;
  while I3 < Obj4.Count do begin
    Obj3 := Obj4.Items[I3];
    Obj1.RemovePCBObject(Obj3);
    PCBServer.SendMessageToRobots(Obj1.I_ObjectAddress, c_Broadcast, PCBM_BoardRegisteration, Obj3.I_ObjectAddress);
    I3 := I3 + 1;
  end;
  PCBServer.PostProcess;
  S2 := 'removed rules=' + IntToStr(Obj4.Count);
  Obj4.Free;

  // ---------- pass 1: create everything
  SandboxLog('create');
  Obj4 := TInterfaceList.Create;
  Obj3 := TPolySegment; Obj3.Kind := ePolySegmentLine;
  B1 := 0;
  PCBServer.PreProcess;
  I1 := 0;
  while I1 < List1.Count do begin
    Obj5.DelimitedText := List1[I1];
    S1 := Obj5[0];
    if S1 = 'R' then begin
      Obj2 := PCBServer.PCBRuleFactory(22);
      Obj2.Name := Obj5[1];
      Obj2.Kind := 1;
      Obj2.Layer := StrToInt(Obj5[2]);
      Obj2.DRCEnabled := Obj5[3] = '1';
      Obj2.Scope1Expression := Obj5[4];
      Obj2.Comment := Obj5[5];
      I2 := StrToInt(Obj5[8]);
      Obj2.PointCount := I2;
      I3 := 0;
      while I3 < I2 do begin
        Obj5.DelimitedText := List1[I1 + 1 + I3];
        Obj3.vx := Obj1.XOrigin + MMsToCoord(StrToFloat(Obj5[1]));
        Obj3.vy := Obj1.YOrigin + MMsToCoord(StrToFloat(Obj5[2]));
        Obj2.Segments[I3] := Obj3;
        I3 := I3 + 1;
      end;
      I1 := I1 + I2;
      Obj1.AddPCBObject(Obj2);
      PCBServer.SendMessageToRobots(Obj1.I_ObjectAddress, c_Broadcast, PCBM_BoardRegisteration, Obj2.I_ObjectAddress);
      Obj4.Add(Obj2);
    end else if S1 = 'H' then begin
      Obj2 := PCBServer.PCBRuleFactory(50);
      Obj2.Name := Obj5[1];
      Obj2.MaxHeight := MMsToCoord(StrToFloat(Obj5[2]));
      Obj2.PreferedHeight := MMsToCoord(StrToFloat(Obj5[2]));
      Obj2.MinHeight := MMsToCoord(StrToFloat(Obj5[3]));
      Obj2.Scope1Expression := Obj5[4];
      Obj2.Comment := Obj5[5];
      Obj1.AddPCBObject(Obj2);
      PCBServer.SendMessageToRobots(Obj1.I_ObjectAddress, c_Broadcast, PCBM_BoardRegisteration, Obj2.I_ObjectAddress);
      B1 := B1 + 1;
    end;
    I1 := I1 + 1;
  end;
  PCBServer.PostProcess;
  S2 := S2 + ' | rooms=' + IntToStr(Obj4.Count) + ' hrules=' + IntToStr(B1);

  // ---------- pass 2: room location = polygon min corner (own modify block)
  SandboxLog('pass2');
  PCBServer.PreProcess;
  B1 := 0; I1 := 0;
  while I1 < List1.Count do begin
    Obj5.DelimitedText := List1[I1];
    if Obj5[0] = 'R' then begin
      Obj2 := Obj4.Items[B1]; B1 := B1 + 1;
      PCBServer.SendMessageToRobots(Obj2.I_ObjectAddress, c_Broadcast, PCBM_BeginModify, c_NoEventData);
      Obj2.X := Obj1.XOrigin + MMsToCoord(StrToFloat(Obj5[6]));
      Obj2.Y := Obj1.YOrigin + MMsToCoord(StrToFloat(Obj5[7]));
      PCBServer.SendMessageToRobots(Obj2.I_ObjectAddress, c_Broadcast, PCBM_EndModify, c_NoEventData);
    end;
    I1 := I1 + 1;
  end;
  PCBServer.PostProcess;

  // ---------- pass 3: re-set the outline so the bounding rectangle is recomputed; verify it
  SandboxLog('pass3');
  PCBServer.PreProcess;
  B1 := 0; I1 := 0;
  while I1 < List1.Count do begin
    Obj5.DelimitedText := List1[I1];
    if Obj5[0] = 'R' then begin
      Obj2 := Obj4.Items[B1]; B1 := B1 + 1;
      S1 := Obj5[6] + ' ' + Obj5[7];
      I2 := StrToInt(Obj5[8]);
      PCBServer.SendMessageToRobots(Obj2.I_ObjectAddress, c_Broadcast, PCBM_BeginModify, c_NoEventData);
      Obj2.PointCount := I2;
      I3 := 0;
      while I3 < I2 do begin
        Obj5.DelimitedText := List1[I1 + 1 + I3];
        Obj3.vx := Obj1.XOrigin + MMsToCoord(StrToFloat(Obj5[1]));
        Obj3.vy := Obj1.YOrigin + MMsToCoord(StrToFloat(Obj5[2]));
        Obj2.Segments[I3] := Obj3;
        I3 := I3 + 1;
      end;
      PCBServer.SendMessageToRobots(Obj2.I_ObjectAddress, c_Broadcast, PCBM_EndModify, c_NoEventData);
      Obj5.DelimitedText := List1[I1];
      if (Abs(Obj2.BoundingRectangle.Left - Obj1.XOrigin - MMsToCoord(StrToFloat(Obj5[6]))) > MMsToCoord(0.01))
         or (Abs(Obj2.BoundingRectangle.Bottom - Obj1.YOrigin - MMsToCoord(StrToFloat(Obj5[7]))) > MMsToCoord(0.01)) then
        S2 := S2 + ' | BR-MISMATCH ' + Obj2.Name + ' ' + FloatToStr(CoordToMMs(Obj2.BoundingRectangle.Left - Obj1.XOrigin)) + ',' + FloatToStr(CoordToMMs(Obj2.BoundingRectangle.Bottom - Obj1.YOrigin)) + ' want ' + S1;
      I1 := I1 + I2;
    end;
    I1 := I1 + 1;
  end;
  PCBServer.PostProcess;
  Obj4.Free;

  // ---------- pass 4: priorities (empty modify, file order; the last one ends at priority 1)
  SandboxLog('priorities');
  I1 := 0;
  while I1 < List1.Count do begin
    Obj5.DelimitedText := List1[I1];
    if Obj5[0] = 'P' then begin
      B1 := 0;
      Obj2 := Obj1.BoardIterator_Create;
      Obj2.AddFilter_ObjectSet(MkSet(eRuleObject));
      Obj2.AddFilter_LayerSet(AllLayers); Obj2.AddFilter_Method(eProcessAll);
      Obj3 := Obj2.FirstPCBObject;
      while Obj3 <> nil do begin
        if Obj3.Name = Obj5[1] then begin Obj4 := Obj3; B1 := 1; end;
        Obj3 := Obj2.NextPCBObject;
      end;
      Obj1.BoardIterator_Destroy(Obj2);
      if B1 = 0 then S2 := S2 + ' | no rule ' + Obj5[1]
      else begin
        PCBServer.PreProcess;
        PCBServer.SendMessageToRobots(Obj4.I_ObjectAddress, c_Broadcast, PCBM_BeginModify, c_NoEventData);
        PCBServer.SendMessageToRobots(Obj4.I_ObjectAddress, c_Broadcast, PCBM_EndModify, c_NoEventData);
        PCBServer.PostProcess;
      end;
    end;
    I1 := I1 + 1;
  end;
  Obj5.Free; List1.Free;
  Obj1.ViewManager_FullUpdate;
  ResultText := S2;
end;
