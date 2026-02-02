import os
import shutil
from zipfile import ZipFile

def create_duplicate_file(filepath):
    if os.path.exists(filepath):
        src = os.path.realpath(filepath)
        dest = src + ".bak"
        shutil.copy(src, dest)

def rename_file(old_name, new_name):
    if os.path.exists(old_name):
        os.rename(old_name, new_name)

def compress_to_zip():
    root_dir, tail = os.path.split(os.path.realpath("renamed_sample.txt"))
    shutil.make_archive("compressed_sample", 'zip', root_dir  )
    return 0

def compress_fine_zip():
    with ZipFile('compressed_sample.zip', 'w') as newZip:
        newZip.write('renamed_sample.txt')
        newZip.write('sample.txt.bak')
    return 0
def main():
    #Process here
    create_duplicate_file("sample.txt")
    rename_file("sample.txt", "renamed_sample.txt")
    compress_to_zip()
    compress_fine_zip()
    return 0


if __name__ == "__main__":
    main()
