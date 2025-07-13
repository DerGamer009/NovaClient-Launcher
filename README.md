# NovaClient Launcher Installer

This repository contains a simple example of an installer for a custom Minecraft launcher called **NovaClientLauncher**. The installer is written in Python using `tkinter` and can be built into a Windows `.exe` using `PyInstaller`.

## Building the Installer

1. Install Python 3.x on your system.
2. Install PyInstaller:
   ```bash
   pip install pyinstaller
   ```
3. Build the executable:
   ```bash
   pyinstaller --onefile --noconsole installer.py
   ```
   The resulting executable will appear in the `dist` folder.

## Running

Execute the generated `installer.exe` to install the launcher. The installer downloads the launcher archive from a predefined URL and extracts it to the user directory.

This code is a minimal example and uses a placeholder download URL. Replace `DOWNLOAD_URL` in `installer.py` with the actual URL to your launcher files.
