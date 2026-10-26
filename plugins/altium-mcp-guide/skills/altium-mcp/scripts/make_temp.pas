Obj1 := PCBServer.GetCurrentPCBBoard;
List1 := TStringList.Create;
List1.LoadFromFile('@@FILE@@');
Obj4 := TStringList.Create;
Obj4.Delimiter := #9;
Obj4.StrictDelimiter := True;
S3 := '';
for I1 := 0 to List1.Count - 1 do
begin
  Obj4.DelimitedText := List1[I1];
  if Obj4.Count >= 7 then
  begin
    S1 := Obj4[0];
    S2 := Obj4[3];
    Obj5 := nil;
    if S2 <> '' then
    begin
      Obj2 := Obj1.BoardIterator_Create;
      Obj2.AddFilter_ObjectSet(MkSet(eNetObject));
      Obj2.AddFilter_LayerSet(AllLayers);
      Obj2.AddFilter_Method(eProcessAll);
      Obj3 := Obj2.FirstPCBObject;
      while Obj3 <> nil do
      begin
        if Obj3.Name = S2 then Obj5 := Obj3;
        Obj3 := Obj2.NextPCBObject;
      end;
      Obj1.BoardIterator_Destroy(Obj2);
    end;
    SandboxLog('make ' + Obj4[1]);
    Obj3 := nil;
    if S1 = 'V' then
    begin
      Obj3 := PCBServer.PCBObjectFactory(eViaObject, eNoDimension, eCreate_Default);
      Obj3.X := Obj1.XOrigin + MMsToCoord(StrToFloat(Obj4[4]));
      Obj3.Y := Obj1.YOrigin + MMsToCoord(StrToFloat(Obj4[5]));
      Obj3.HoleSize := MMsToCoord(StrToFloat(Obj4[6]));
      Obj3.Size := MMsToCoord(StrToFloat(Obj4[7]));
      Obj3.LowLayer := eBottomLayer;
      Obj3.HighLayer := eTopLayer;
    end;
    if S1 = 'T' then
    begin
      Obj3 := PCBServer.PCBObjectFactory(eTrackObject, eNoDimension, eCreate_Default);
      Obj3.Layer := StrToInt(Obj4[2]);
      Obj3.X1 := Obj1.XOrigin + MMsToCoord(StrToFloat(Obj4[4]));
      Obj3.Y1 := Obj1.YOrigin + MMsToCoord(StrToFloat(Obj4[5]));
      Obj3.X2 := Obj1.XOrigin + MMsToCoord(StrToFloat(Obj4[6]));
      Obj3.Y2 := Obj1.YOrigin + MMsToCoord(StrToFloat(Obj4[7]));
      Obj3.Width := MMsToCoord(StrToFloat(Obj4[8]));
    end;
    if S1 = 'P' then
    begin
      Obj3 := PCBServer.PCBObjectFactory(ePadObject, eNoDimension, eCreate_Default);
      Obj3.Mode := ePadMode_Simple;
      Obj3.Layer := StrToInt(Obj4[2]);
      Obj3.X := Obj1.XOrigin + MMsToCoord(StrToFloat(Obj4[4]));
      Obj3.Y := Obj1.YOrigin + MMsToCoord(StrToFloat(Obj4[5]));
      Obj3.TopXSize := MMsToCoord(StrToFloat(Obj4[6]));
      Obj3.TopYSize := MMsToCoord(StrToFloat(Obj4[7]));
      Obj3.MidXSize := MMsToCoord(StrToFloat(Obj4[6]));
      Obj3.MidYSize := MMsToCoord(StrToFloat(Obj4[7]));
      Obj3.BotXSize := MMsToCoord(StrToFloat(Obj4[6]));
      Obj3.BotYSize := MMsToCoord(StrToFloat(Obj4[7]));
      Obj3.HoleSize := MMsToCoord(StrToFloat(Obj4[8]));
      Obj3.Name := 'TMPTEST';
    end;
    if S1 = 'F' then
    begin
      Obj3 := PCBServer.PCBObjectFactory(eFillObject, eNoDimension, eCreate_Default);
      Obj3.Layer := StrToInt(Obj4[2]);
      Obj3.X1Location := Obj1.XOrigin + MMsToCoord(StrToFloat(Obj4[4]));
      Obj3.Y1Location := Obj1.YOrigin + MMsToCoord(StrToFloat(Obj4[5]));
      Obj3.X2Location := Obj1.XOrigin + MMsToCoord(StrToFloat(Obj4[6]));
      Obj3.Y2Location := Obj1.YOrigin + MMsToCoord(StrToFloat(Obj4[7]));
      Obj3.Rotation := 0;
    end;
    if Obj3 <> nil then
    begin
      if Obj5 <> nil then Obj3.Net := Obj5;
      PCBServer.PreProcess;
      Obj1.AddPCBObject(Obj3);
      PCBServer.SendMessageToRobots(Obj1.I_ObjectAddress, c_Broadcast, PCBM_BoardRegisteration, Obj3.I_ObjectAddress);
      PCBServer.PostProcess;
      S2 := '';
      if Obj3.Net <> nil then S2 := Obj3.Net.Name;
      S3 := S3 + Obj4[1] + ' ' + Obj3.Descriptor + ' net=' + S2 + #13#10;
    end;
  end;
end;
Obj4.Free;
List1.Free;
ResultText := S3;
