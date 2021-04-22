# DownloadWarningPy

Get notified whenever your Downloads folder exceeds a certain limit. (Windows only for now)

The script, everytime it's run, checks your Download folder (or whatever folder you have configured) and warns you if it exceeds the limit.

Use config.py to change the settings of the program.

## Dependencies

You obviously need the latest version of Python. 
By default, the warning will be displayed using a dialog box, but by using the 
[win10toast](https://github.com/jithurjacob/Windows-10-Toast-Notifications "Github Project Website") 
module, you can take advantage of the Windows 10 toast notifications.

With toasts: ![Windows 10 toast notification](https://i.imgur.com/iXicLPN.png)  Without: ![Windows 10 dialog box](https://i.imgur.com/16j0Jli.png)

## Thanks to

- https://github.com/jithurjacob/Windows-10-Toast-Notifications
- https://www.codespeedy.com/get-the-size-of-a-folder-in-python/