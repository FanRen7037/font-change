import os
import shutil
from pathlib import Path

# Define the base Roblox versions directory
roblox_versions_dir = Path(os.getenv('LOCALAPPDATA')) / "Roblox" / "Versions"

# Define source files
source_font = Path(r"C:\Users\Amogus\Desktop\OpenSans.ttf") #將路徑更改為你字體檔案的位置，左側範例為C:\使用者\(使用者名稱)\桌面\字體檔
source_sound = Path(r"C:\Users\Amogus\Desktop\ouch.ogg") #將路徑更改為你音訊檔案的位置，左側範例為C:\使用者\(使用者名稱)\桌面\音訊檔

# Find the latest non-empty Roblox version folder
roblox_version_folder = None
for version_folder in sorted(roblox_versions_dir.iterdir(), key=os.path.getmtime, reverse=True):
    if (version_folder / "content").exists() and any(version_folder.iterdir()):  # Ensure it's not an empty old version
        roblox_version_folder = version_folder
        break  # Use the first valid version found

if roblox_version_folder:
    print(f"Detected Roblox version folder: {roblox_version_folder}")

    # Define target directories
    roblox_fonts_dir = roblox_version_folder / "content" / "fonts"
    roblox_sounds_dir = roblox_version_folder / "content" / "sounds"

    # Replace all font files in the fonts folder while keeping original names and extensions
    if roblox_fonts_dir.exists():
        for font_file in roblox_fonts_dir.iterdir():
            if font_file.suffix.lower() in [".ttf", ".otf"]:  # Only replace font files
                shutil.copy2(source_font, font_file)  # Overwrite while keeping the name
                print(f"Replaced font: {font_file}")

    # Copy the custom sound file
    if roblox_sounds_dir.exists():
        target_sound_path = roblox_sounds_dir / source_sound.name
        shutil.copy2(source_sound, target_sound_path)
        print(f"Copied sound: {target_sound_path}")

else:
    print("No valid Roblox version folder found.")
    
