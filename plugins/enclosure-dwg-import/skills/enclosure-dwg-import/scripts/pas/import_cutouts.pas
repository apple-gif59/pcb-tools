{ Board cutouts and non-plated holes from cutouts.txt (shell_import.py). Run through run_altium_script.
  C <n> followed by n lines V x y : one Board Cutout (Multi-Layer), mm relative to the board origin
  H x y d name : free pad, non-plated, pad size = hole size = d
  Removed first: every Board Cutout region that is not part of a component (AD's internal board-shape
  region has an empty Descriptor and is kept), and every free non-plated pad whose name is used by an H line. }
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
    if Obj5[0] = 'H' then S2 := S2 + Obj5[4] + ',';
    I1 := I1 + 1;
  end;

  SandboxLog('collect old');
  Obj4 := TInterfaceList.Create;
  Obj2 := Obj1.BoardIterator_Create;
  Obj2.AddFilter_ObjectSet(MkSet(eRegionObject, ePadObject));
  Obj2.AddFilter_AllLayers;
  Obj2.AddFilter_Method(eProcessAll);
  Obj3 := Obj2.FirstPCBObject;
  while Obj3 <> nil do begin
    if not Obj3.InComponent then begin
      if Obj3.ObjectId = eRegionObject then begin
        if (Obj3.Kind = 3) and (Pos('Board Cutout', Obj3.Descriptor) > 0) then Obj4.Add(Obj3);
      end else begin
        if (not Obj3.Plated) and (Pos(',' + Obj3.Name + ',', S2) > 0) then Obj4.Add(Obj3);
      end;
    end;
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
  S2 := 'removed=' + IntToStr(Obj4.Count) + ';';
  Obj4.Free;

  SandboxLog('create');
  I1 := 0;
  while I1 < List1.Count do begin
    Obj5.DelimitedText := List1[I1];
    S1 := Obj5[0];
    if S1 = 'C' then begin
      I3 := StrToInt(Obj5[1]);
      Obj3 := PCBServer.PCBContourFactory;
      I2 := 0;
      while I2 < I3 do begin
        Obj5.DelimitedText := List1[I1 + 1 + I2];
        Obj3.AddPoint(Obj1.XOrigin + MMsToCoord(StrToFloat(Obj5[1])), Obj1.YOrigin + MMsToCoord(StrToFloat(Obj5[2])));
        I2 := I2 + 1;
      end;
      I1 := I1 + I3;
      Obj2 := PCBServer.PCBObjectFactory(eRegionObject, eNoDimension, eCreate_Default);
      Obj2.Layer := eMultiLayer;
      Obj2.Kind := 3;
      Obj2.SetOutlineContour(Obj3);
      Obj1.AddPCBObject(Obj2);
      PCBServer.SendMessageToRobots(Obj1.I_ObjectAddress, c_Broadcast, PCBM_BoardRegisteration, Obj2.I_ObjectAddress);
      S2 := S2 + ' cutout pts=' + IntToStr(Obj2.MainContour.Count) + ' box=' + FloatToStr(CoordToMMs(Obj2.BoundingRectangle.Left - Obj1.XOrigin)) + ',' + FloatToStr(CoordToMMs(Obj2.BoundingRectangle.Bottom - Obj1.YOrigin)) + ',' + FloatToStr(CoordToMMs(Obj2.BoundingRectangle.Right - Obj1.XOrigin)) + ',' + FloatToStr(CoordToMMs(Obj2.BoundingRectangle.Top - Obj1.YOrigin)) + ';';
    end else if S1 = 'H' then begin
      Obj2 := PCBServer.PCBObjectFactory(ePadObject, eNoDimension, eCreate_Default);
      Obj2.Mode := ePadMode_Simple;
      Obj2.X := Obj1.XOrigin + MMsToCoord(StrToFloat(Obj5[1]));
      Obj2.Y := Obj1.YOrigin + MMsToCoord(StrToFloat(Obj5[2]));
      Obj2.TopShape := eRounded;
      Obj2.TopXSize := MMsToCoord(StrToFloat(Obj5[3])); Obj2.TopYSize := MMsToCoord(StrToFloat(Obj5[3]));
      Obj2.MidXSize := MMsToCoord(StrToFloat(Obj5[3])); Obj2.MidYSize := MMsToCoord(StrToFloat(Obj5[3]));
      Obj2.BotXSize := MMsToCoord(StrToFloat(Obj5[3])); Obj2.BotYSize := MMsToCoord(StrToFloat(Obj5[3]));
      Obj2.HoleSize := MMsToCoord(StrToFloat(Obj5[3]));
      Obj2.Plated := False;
      Obj2.Layer := eMultiLayer;
      Obj2.Name := Obj5[4];
      Obj1.AddPCBObject(Obj2);
      PCBServer.SendMessageToRobots(Obj1.I_ObjectAddress, c_Broadcast, PCBM_BoardRegisteration, Obj2.I_ObjectAddress);
      S2 := S2 + ' hole d=' + FloatToStr(CoordToMMs(Obj2.HoleSize)) + ' @' + FloatToStr(CoordToMMs(Obj2.X - Obj1.XOrigin)) + ',' + FloatToStr(CoordToMMs(Obj2.Y - Obj1.YOrigin)) + ';';
    end;
    I1 := I1 + 1;
  end;
  PCBServer.PostProcess;
  Obj5.Free; List1.Free;
  Obj1.ViewManager_FullUpdate;
  ResultText := S2;
end;
