import os
import collections
from pprint import pprint

# Most common file types
EXT_AUDIO = ['mp3', 'wav', 'raw', 'wma', 'mid', 'midi']
EXT_VIDEO = ['mp4', 'mpg', 'mpeg', 'avi', 'mov', 'flv', 'mkv', 'mwv', 'm4v', 'h264']
EXT_IMGS  = ['png', 'jpg', 'jpeg', 'gif', 'svg', 'bmp', 'psd', 'svg', 'tiff', 'tif']
EXT_DOCS  = ['txt', 'pdf', 'csv', 'xls', 'xlsx', 'ods', 'doc', 'docx', 'odt', 'tex', 'ppt', 'pptx', 'log']
EXT_COMPR = ['zip', 'z', '7z', 'rar', 'tar', 'gz', 'rpm', 'pkg', 'deb']
EXT_INSTL = ['dmg', 'exe', 'iso']
EXT_CODE  = ['py', 'java', 'c', 'cpp', 'h', 'hpp', 'cs', 'js', 'ts', 'html', 'css', 'php', 'rb', 'swift', 'kt', 'sh', 'bat', 'asm', 's', 'ipynb']


BASE_PATH = os.path.expanduser('~')
DOWNLOADS_PATH = os.path.join(BASE_PATH, 'Downloads')
DEST_DIRS = ['Music', 'Movies', 'Pictures', 'Documents', 'Applications', 'Other', 'CODE']

# Create directories within the Downloads folder if they do not exist
for d in DEST_DIRS:
    dir_path = os.path.join(DOWNLOADS_PATH, d)
    if not os.path.isdir(dir_path):
        os.mkdir(dir_path)

# Mapping files from Downloads folder based on their file extension
files_mapping = collections.defaultdict(list)
files_list = os.listdir(DOWNLOADS_PATH)

for file_name in files_list:
    file_path = os.path.join(DOWNLOADS_PATH, file_name)
    if os.path.isfile(file_path) and file_name[0] != '.':
        file_ext = file_name.split('.')[-1].lower()  # Normalize to lowercase
        files_mapping[file_ext].append(file_name)

pprint(files_mapping)

# Moving all files given a file extension to a target directory within Downloads
for f_ext, f_list in files_mapping.items():
    if f_ext in EXT_INSTL:
        dest_dir = 'Applications'
    elif f_ext in EXT_CODE:
        dest_dir = 'CODE'
    elif f_ext in EXT_AUDIO:
        dest_dir = 'Music'
    elif f_ext in EXT_VIDEO:
        dest_dir = 'Movies'
    elif f_ext in EXT_IMGS:
        dest_dir = 'Pictures'
    elif f_ext in EXT_DOCS or f_ext in EXT_COMPR:
        dest_dir = 'Documents'
    else:
        dest_dir = 'Other'

    # Ensuring the destination directory exists
    dest_path = os.path.join(DOWNLOADS_PATH, dest_dir)
    if not os.path.exists(dest_path):
        os.mkdir(dest_path)

    print(f"Moving files with extension '{f_ext}' to {dest_path}")


    # Executing the move
    for file in f_list:
        src_path = os.path.join(DOWNLOADS_PATH, file)
        dest_file_path = os.path.join(dest_path, file)
        try:
            os.rename(src_path, dest_file_path)
            print(f"Moved {src_path} to {dest_file_path}")
        except Exception as e:
            print(f"Error moving file {file}: {e}")
