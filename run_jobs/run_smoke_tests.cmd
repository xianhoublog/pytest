@echo off
SET MARKER="smoke"
SET SEARCHPATH=%~dp0%..\tests\

cd ..\venv\Scripts\activate
cd %SEARCHPATH%
pytest -m %MARKER%

