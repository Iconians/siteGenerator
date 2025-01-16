import os
import shutil

def delete_contents(directory):
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isfile(item_path) or os.path.islink(item_path):
            os.unlink(item_path)
        elif os.path.isdir(item_path):
            shutil.rmtree(item_path)

def copy_contents(src, dst):
    if not os.path.exists(dst):
        os.makedirs(dst)
    for item in os.listdir(src):
        src_path = os.path.join(src, item)
        dst_path = os.path.join(dst, item)
        if os.path.isdir(src_path):
            copy_contents(src_path, dst_path)
        else:
            shutil.copy2(src_path, dst_path)
            print(f"Copied: {dst_path}")

def copy_directory(src, dst):
    if os.path.exists(dst):
        delete_contents(dst)
    else:
        os.makedirs(dst)
    copy_contents(src, dst)