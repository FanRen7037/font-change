@echo off
setlocal enabledelayedexpansion

:: Define the base Roblox versions directory
set "roblox_versions_dir=%LOCALAPPDATA%\Roblox\Versions"

:: Define source files
set "source_font=C:\Users\Amogus\Desktop\OpenSans.ttf" rem 將路徑更改為你字體檔案的位置，左側範例為C:\使用者\(使用者名稱)\桌面\字體檔
set "source_sound=C:\Users\Amogus\Desktop\ouch.ogg" rem 將路徑更改為你音訊檔案的位置，左側範例為C:\使用者\(使用者名稱)\桌面\音訊檔

:: Find the latest non-empty Roblox version folder
for /f "delims=" %%D in ('dir /b /ad /o-d "%roblox_versions_dir%"') do (
    if exist "%roblox_versions_dir%\%%D\content" (
        set "roblox_version_folder=%roblox_versions_dir%\%%D"
        goto :found
    )
)

echo No valid Roblox version folder found.
goto :eof

:found
echo Detected Roblox version folder: %roblox_version_folder%

:: Define target directories
set "roblox_fonts_dir=%roblox_version_folder%\content\fonts"
set "roblox_sounds_dir=%roblox_version_folder%\content\sounds"

:: Replace all font files in the fonts folder while keeping original names
if exist "%roblox_fonts_dir%" (
    for %%F in ("%roblox_fonts_dir%\*.ttf" "%roblox_fonts_dir%\*.otf") do (
        copy /y "%source_font%" "%%F"
        echo Replaced font: %%F
    )
)

:: Copy the custom sound file
if exist "%roblox_sounds_dir%" (
    copy /y "%source_sound%" "%roblox_sounds_dir%\ouch.ogg"
    echo Copied sound: %roblox_sounds_dir%\ouch.ogg
)

echo Done.
pause
