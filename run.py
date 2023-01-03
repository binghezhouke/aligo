from aligo import Aligo
import sys
if __name__ == '__main__':
    a = Aligo("binghe")
    print(a.user_name)
    sync_folder = a.get_folder_by_path(sys.argv[1])
    a.sync_folder(sys.argv[2], sync_folder.file_id, False)
