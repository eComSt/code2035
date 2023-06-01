import os
current_path = os.path.dirname(os.path.abspath(__file__))
parent_path = os.path.dirname(current_path)
print(current_path)
print(parent_path)
def get_all_files(path):
    try:
        for i in os.listdir(path):
            new = os.path.join(path,i)
            if os.path.isdir(new):
                print(f"Folder {new}")
                get_all_files(new)
            else:
                print(f" -{new}")
    except:pass
get_all_files(parent_path)


def recurs(count):
    print(count)
    if count == 5:return
    recurs(count + 1)
    print(count)

recurs(0)