// Closes the Sandbox.pas editor tab left open after a script error, so the
// run_altium_script sandbox runs the file on disk again.
// Template: recover.ps1 replaces @@SANDBOX@@ and @@RESULT@@ with full paths.
procedure Run;
var
    Doc : IServerDocument;
    L   : TStringList;
begin
    L := TStringList.Create;
    L.Add('start');
    L.SaveToFile('@@RESULT@@');
    Doc := Client.GetDocumentByPath('@@SANDBOX@@');
    if Doc = nil then
        L.Add('not open')
    else
    begin
        L.Add('found');
        L.SaveToFile('@@RESULT@@');
        Doc.Modified := False;
        L.Add('unmodified');
        L.SaveToFile('@@RESULT@@');
        Client.CloseDocument(Doc);
        L.Add('closed');
    end;
    L.SaveToFile('@@RESULT@@');
    L.Free;
end;
