@echo off
:main
cls
q tests\*.py
call TESTS.cmd
pause
goto main
:end
