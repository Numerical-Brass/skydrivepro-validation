Microsoft SkyDrive Pro Validation
======================

Skydrive Pro cannot sync files the names of which contain certain characters.

This is for searching through a directory for invalid folder and file names, so that you can rename the them before syncing through Microsoft SkyDrive Pro.

It looks for folders and files that begin or end with a space, end with a period, include the characters / \ < > : * " ? | or have the following names: AUX, PRN, NUL, CON, COM0, COM1, COM2, COM3, COM4, COM5, COM6, COM7, COM8, COM9, LPT0, LPT1, LPT2, LPT3, LPT4, LPT5, LPT6, LPT7, LPT8, LPT9.

About
=====
If you place files or folders with invalid characters/names into the Skydrive Pro folder, these will fail to sync. Other cloud storage/synchronisation services, like Dropbox, do not have these restrictions. This can become problematic when trying to migrate data from other cloud services to Skydrive Pro, especially with time constraints. 

The only solution is to rename the files and folders. But manually trawling through the files and folders is impractical, and Microsoft does not provide a tool to automate the process. 

This script is designed to find files and folders whose names will be incompatible with Skydrive Pro, so that the user knows in advance which folders and files to rename to ensure a smooth migration.

Usage
=====
python validate_skydrive.py
Specify the directory wrapped in a string (e.g. "/home/user/directory/to/check/")



