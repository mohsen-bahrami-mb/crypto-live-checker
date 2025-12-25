@echo off
REM Build script for crypto-check executable on Windows

echo Building crypto-check for Windows...

REM Clean previous builds
if exist build rmdir /s /q build
if exist dist rmdir /s /q dist
if exist *.spec del *.spec

REM Install dependencies if needed
pipenv install --dev pyinstaller

REM Build Windows executable
pipenv run pyinstaller main.py ^
    --onefile ^
    --name crypto-check ^
    --console

echo.
echo Build completed successfully!
echo Location: dist\crypto-check.exe
echo.
echo To run the app:
echo   dist\crypto-check.exe ^<symbol^> [limit]
echo.
echo Example:
echo   dist\crypto-check.exe btcusdt
