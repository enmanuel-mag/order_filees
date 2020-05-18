# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'

#!/usr/bin/env python

# %%
import os
import csv
import shutil


# %%
def get_download_path():
    """Returns the default downloads path for linux or windows"""
    if os.name == 'nt':
        import winreg
        sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
        downloads_guid = '{374DE290-123F-4565-9164-39C4925E467B}'
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
            location = winreg.QueryValueEx(key, downloads_guid)[0]
        return location
    else:
        return os.path.join(os.path.expanduser('~'), 'downloads')


# %%
def check_type(file):
    """
    Return the type of file by a fiel as parameter

    Parameters
    --------------
        file: (str): name of the file to check type
    Returns
    --------------
        Return the type of the file
    """
    if file.endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
        return 'img'
    elif file.endswith(('.exe', '.msi', '.jar')):
        return 'prog'
    elif file.endswith(('.pdf', '.docx', '.xlsx', '.zip', '.rar', '.txt')):
        return 'doc'
    elif file.endswith(('.mp3', '.wav')):
        return 'musc'
    elif file.endswith(('.mp4', '.vlc')):
        return 'vid'
    else:
        return 'unkw'


# %%
def load_paths():
    """
    Return a dicctionary with the paths to move the files
    """
    file = open('./paths.csv', 'r', encoding='utf-8')
    reader = csv.reader(file)
    dic_paths = {}

    for line in reader:
        key, value = line
        dic_paths[line[0]] = line[1]
    return dic_paths


def rename_file(name_file, extra):

    ind_extension = name_file.find('.')

    if ind_extension != -1:
        extension = name_file[ind_extension:]
        name_file.replace(extension, extra+extension)
    else:
        name_file += extra

    return name_file


# %%
def move_files(path_downloads):
    dic_paths = load_paths()

    for file in os.listdir(path_downloads):
        src_path = os.path.join(path_downloads, file)
        if os.path.isfile(src_path):
            type_file = check_type(file)
            dest_folder = dic_paths.get(type_file, -1)
            if dest_folder != -1:
                dest_path = os.path.join(dest_folder, file)

                file_moved = False
                extra = 0
                while not file_moved:
                    if not os.path.exists(dest_path):
                        shutil.move(src_path, dest_path)
                        file_moved = True
                    else:
                        dest_path = rename_file(dest_path, str(extra))


# %%
path_downloads = get_download_path()
move_files(path_downloads)


# %%
