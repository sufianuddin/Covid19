@echo off
set CUR_YYYY=%date:~10,5%
set CUR_MM=%date:~4,2%
set CUR_DD=%date:~7,2%
set CUR_HH=%time:~0,2%
if %CUR_HH% lss 10 (set CUR_HH=0%time:~1,1%)

set CUR_NN=%time:~3,2%
set CUR_SS=%time:~6,2%
set CUR_MS=%time:~9,2%

set SUBFILENAME=%CUR_YYYY%%CUR_MM%%CUR_DD%

@REM echo -%CUR_HH%%CUR_NN%%CUR_SS%

@REM echo %SUBFILENAME%

echo Date = %DATE% and Time = %TIME%  > "C:\Users\Sufian.Uddin\Desktop\Covid19\Logs\ProvienceData_%SUBFILENAME%.txt"

@REM echo. >> "C:\Users\Sufian.Uddin\Desktop\Covid19\Logs\ProvienceData_%SUBFILENAME%.txt"

echo 1) Python Script Started >> "C:\Users\Sufian.Uddin\Desktop\Covid19\Logs\ProvienceData_%SUBFILENAME%.txt"

c:

cd C:/Users/Sufian.Uddin/Desktop/Covid19

python GetDataProvinces.py >> "C:\Users\Sufian.Uddin\Desktop\Covid19\Logs\ProvienceData_%SUBFILENAME%.txt"

@REM @TIMEOUT /T 10 /NOBREAK >> "C:\Users\Sufian.Uddin\Desktop\Covid19\Logs\ProvienceData_%SUBFILENAME%.txt"