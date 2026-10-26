List1 := TStringList.Create;
Obj1 := PCBServer.GetCurrentPCBBoard;
Obj2 := Obj1.BoardIterator_Create;
Obj2.AddFilter_ObjectSet(MkSet(eRuleObject));
Obj2.AddFilter_LayerSet(AllLayers);
Obj2.AddFilter_Method(eProcessAll);
Obj3 := Obj2.FirstPCBObject;
while Obj3 <> nil do
begin
  if Obj3.DRCEnabled then S2 := '1' else S2 := '0';
  List1.Add(Obj3.Name + #9 + IntToStr(Obj3.RuleKind) + #9 + IntToStr(Obj3.Priority) + #9 + S2 + #9 + IntToStr(Obj3.NetScope) + #9 + Obj3.Scope1Expression + #9 + Obj3.Scope2Expression + #9 + Obj3.Descriptor);
  Obj3 := Obj2.NextPCBObject;
end;
Obj1.BoardIterator_Destroy(Obj2);
List1.Sort;
List1.SaveToFile('@@OUT@@');
ResultText := IntToStr(List1.Count);
List1.Free;
