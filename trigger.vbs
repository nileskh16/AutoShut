Set wshell = WScript.createobject("WScript.Shell")
wshell.run chr(34) & "control.bat" & Chr(34), 0
Set wshell = nothing