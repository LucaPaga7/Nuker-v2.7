import sys
import os

print("Installing Python pip modules for LucaPaga")
if sys.platform.startswith("win"):
    "WINDOWS"
    os.system("pip install pystyle")
    os.system("pip install colorama")
    os.system("pip install requests")
    os.system("pip install json")
    os.system("pip install random")
    os.system("pip install string")
    os.system("pip install base64")
    os.system("pip install threading")
    os.system("pip install discord")
    os.system("pip install discord.py")
    os.system("pip install asyncio")
    os.system("python LucaPagaNuker.py")
