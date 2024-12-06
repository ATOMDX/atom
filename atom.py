import os
import zlib
import platform

def run():
    bit = platform.architecture()[0]
    os.system("clear")
    print(" [√] Join Whatsapp Group ")
    os.system("xdg-open  https://chat.whatsapp.com/GL7M45fSg0yKrhJPirkNki")
    if "32bit" in bit:
        print(" [•] Your device is 32bit (supported) ")
        __import__("SORRY")
    elif "64bit" in bit:
        print(" [√] device is 64bit ")
        __import__("ATOMAA")
    else:
        print(" [•] Unknown Architecture ")
        print(" [•] Your device dont support this tool ")

run()
