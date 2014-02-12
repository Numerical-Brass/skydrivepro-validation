__author__ = 'Luke Cossey'

import os
import re

def print_list(list):
    for i in list:
        print i

bad_names = ['AUX', 'PRN', 'NUL', 'CON', 'COM0', 'COM1', 'COM2', 'COM3', 'COM4', 'COM5', 'COM6', 'COM7', 'COM8', 'COM9', 'LPT0', 'LPT1', 'LPT2', 'LPT3', 'LPT4', 'LPT5', 'LPT6', 'LPT7', 'LPT8', 'LPT9']
bad_chars = r'[/\\<>:\*"\?\|]'

error_folders_names = list()
error_file_names = list()
error_file_chars = list()
error_file_period = list()
error_file_space_start = list()
error_file_space_end = list()
error_path_long = list()

# Set the directory you want to start from
input_path = input("Enter directory path to search inside quotes e.g. '%s': " % os.path.dirname(os.path.realpath(__file__)))
print ""


if (os.path.exists(input_path)):
    for dirName, subdirList, fileList in os.walk(input_path):
        for dir in subdirList:
            if dir in bad_names:
                error_folders_names.append('%s/%s' % (dirName, dir))
        #print subdirList
        for fname in fileList:
            if fname in bad_names:
                error_file_names.append('%s/%s' % (dirName, fname))
            if re.search(bad_chars, fname):
                error_file_chars.append('%s/%s' % (dirName, fname))
            if fname.endswith('.') or re.search(r'\.\.',fname):
                error_file_period.append('%s/%s' % (dirName, fname))
            if fname.endswith(' '):
                error_file_space_end.append('%s/%s' % (dirName, fname))
            if fname.startswith(' '):
                error_file_space_start.append('%s/%s' % (dirName, fname))
            if len('%s/%s' % (dirName, fname)) >= 442:
                error_path_long.append('%s/%s' % (dirName, fname))

    print "FOLDERS with banned names\n"
    print_list(error_folders_names)
    print "\n Total:",len(error_folders_names)
    print "==============================================================================================================\n"
    print "FILES with banned names\n"
    print_list(error_file_names)
    print "\n Total:",len(error_file_names)
    print "==============================================================================================================\n"
    print "FILES with invalid characters e.g. / \\ < > : * \" ? |\n"
    print_list(error_file_chars)
    print "\n Total:",len(error_file_chars)
    print "==============================================================================================================\n"
    print "FILES with a prefixing space character\n"
    print_list(error_file_space_start)
    print "\n Total:",len(error_file_space_start)
    print "==============================================================================================================\n"
    print "FILES with a suffixing space character\n"
    print_list(error_file_space_end)
    print "\n Total:",len(error_file_space_end)
    print "==============================================================================================================\n"
    print "FILES with a suffixing or double period character\n"
    print_list(error_file_period)
    print "\n Total:",len(error_file_period)
    print "==============================================================================================================\n"
    print "FILES paths not fewer than 442 characters\n"
    print_list(error_path_long)
    print "\n Total:",len(error_path_long)
    print "==============================================================================================================\n"
    print "\n Total errors:",len(error_folders_names)+len(error_file_names)+len(error_file_chars)+len(error_file_space_start)+len(error_file_space_end)+len(error_file_period)+len(error_path_long)
else:
    print "Path '%s' does not exists." % input_path