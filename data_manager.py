import os
import datetime as time

import data_store

def set_file_info_init(file):

    cover = get_cover_init()
    num = get_num_init()
    revision = get_revision_init()    
    created_time = get_created_time(file)
    revised_time = get_modified_time(file)
    title = get_title(parse_path(file))
    file_name = get_file_name(parse_path(file))

    return data_store.DataStore(cover, num, revision, created_time, revised_time, title, file_name)

def get_cover_init():
    cover = None
    return cover

def get_cover(value):
    cover = value
    return cover

def get_num_init():
    num = None
    return num

def get_num(number):
    
    if number is None:
        num = 1
    else:
        num = int(number) + 1

    return num

def get_revision_init():
    revision = None
    return revision

def get_revision(number):

    if number is None:
        revision = 1
    else:
        revision = int(number) + 1

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

def get_file_name(filename):
    file_name = filename + ".html"
    return file_name

def parse_path(path):
    list = path.split('/')
    file_name = list[len(list) - 1]
    name = file_name.split('.')[0]
    return name
