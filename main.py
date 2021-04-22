import os
import ctypes # Dialog boxes.
from config import toastnotifications, dpath, limit # User-friendly configuration file.
if toastnotifications == True:
    try:
        from win10toast import ToastNotifier # Modern Win 10 toasts. Requires win10toast dependency.
    except ModuleNotFoundError:
        toastnotifications = False

if dpath == None:
    homepath = os.getenv("homepath")
    path = "C:\\" + homepath + "\Downloads"
else:
    path = dpath

def size(path):
    # https://www.codespeedy.com/get-the-size-of-a-folder-in-python/
    total_size = 0

    # Use the walk() method to navigate through directory tree
    for dirpath, dirnames, filenames in os.walk(path):
        for i in filenames:
            
            # Use join to concatenate all the components of path
            f = os.path.join(dirpath, i)
            
            # Use getsize to generate size in bytes and add it to the total size
            total_size += os.path.getsize(f)

    return total_size

if size(path) >= limit:
    if toastnotifications == False:
        output = ctypes.windll.user32.MessageBoxW(
            0,
            "'Downloads' folder exceeds limit!",
            "File Warning",
            0
        )
        if output == 6:
            deldown()
    elif toastnotifications == True:
        toaster = ToastNotifier()
        toaster.show_toast(
            "File Warning",
            "'Downloads' folder exceeds limit!",
        )