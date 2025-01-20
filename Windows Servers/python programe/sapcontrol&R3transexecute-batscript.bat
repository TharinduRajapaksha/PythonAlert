@ECHO OFF

@ECHO Programe came here Checking ----- Test windows oracle SAP Server --------------

@ECHO Programe came here
sapcontrol -nr 00 -function GetProcessList>> sapcontrolresult.txt 
R3trans -d>> R3trans-dresult.txt

//cscript.exe website_Check_textOutput.vbs
//cscript.exe newvbs.vbs



