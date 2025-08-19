import os
import datetime as time

def get_cover(cover):
    return cover

def get_num():
    num = ''
    return num

def get_revision():
    revision = ''
    return revision

def get_created_time(file):
    file_ctime = os.path.getctime(file)
    to_datetime = time.datetime.fromtimestamp(file_ctime)
    return time.datetime.strftime(to_datetime, "%Y-%m-%d %H:%M:%S")

def get_modified_time(file):
    file_mtime = os.path.getmtime(file)
    to_datetime = time.datetime.fromtimestamp(file_mtime)
    return time.datetime.strftime(to_datetime, "%Y-%m-%d %H:%M:%S")

def get_title(filename):
    return filename

def get_label():
    label = ''
    return label

def get_file_name(filename):
    file_name = filename + ".html"
    return file_name

def get_display_flag():
    display_flag = True
    return display_flag