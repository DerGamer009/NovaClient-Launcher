import os
import tkinter as tk
from tkinter import messagebox
import urllib.request
import zipfile
import subprocess

APP_NAME = "NovaClientLauncher"
DOWNLOAD_URL = "https://example.com/NovaClientLauncher.zip"  # placeholder URL
INSTALL_DIR = os.path.join(os.path.expanduser('~'), APP_NAME)

class Installer(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title(APP_NAME + " Installer")
        self.geometry("400x200")

        tk.Label(self, text="Install " + APP_NAME, font=("Arial", 16)).pack(pady=10)
        tk.Button(self, text="Install", command=self.install_launcher).pack(pady=5)
        tk.Button(self, text="Open Launcher", command=self.open_launcher).pack(pady=5)

    def install_launcher(self):
        os.makedirs(INSTALL_DIR, exist_ok=True)
        zip_path = os.path.join(INSTALL_DIR, "launcher.zip")
        try:
            self.download_file(DOWNLOAD_URL, zip_path)
            with zipfile.ZipFile(zip_path, 'r') as zf:
                zf.extractall(INSTALL_DIR)
            messagebox.showinfo("Success", f"Installed to {INSTALL_DIR}")
        except Exception as e:
            messagebox.showerror("Error", str(e))
        finally:
            if os.path.exists(zip_path):
                os.remove(zip_path)

    def download_file(self, url, dest):
        with urllib.request.urlopen(url) as response, open(dest, 'wb') as out_file:
            out_file.write(response.read())

    def open_launcher(self):
        exe_path = os.path.join(INSTALL_DIR, APP_NAME + ".exe")
        if os.path.exists(exe_path):
            subprocess.Popen([exe_path])
        else:
            messagebox.showerror("Not Installed", "Launcher not found. Install first.")

if __name__ == "__main__":
    app = Installer()
    app.mainloop()
