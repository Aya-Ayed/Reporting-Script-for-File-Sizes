import sys
import argparse
from os import walk
from os.path import isdir, getsize,join


file_metadata= {}

def create_help_menu():
    parser = argparse.ArgumentParser(description= '''This program traverse the filesystem finding the largest files in a path.
                                                 You have two options:
                                                 1. Enter a directory path to traverse it.
                                                 2. Don't enter any path and the program will consider your current directory as adefault path.''')

    parser.add_argument('--path',type=str, help= 'path!' )
    args= parser.parse_args()
    return args


def get_file_size(dir_path):
    for root, directories, files in walk(dir_path):
        for _file in files:
            full_path = join(root, _file)
            size = getsize(full_path)/pow(1024,2)
            file_metadata[full_path] = size


def largest_files(metadata):
    file= sorted(metadata.items(), key=lambda x:x[1], reverse= True)
    print(file[1][1])
    for i in range(20):
        print(f"{i+1}. File: {file[i][0]}, Size: {round(file[i][1], 6)} MB")
        


def main():
    
    args = create_help_menu()
    
    if args.path is not None:
        path= args.path
        if(isdir(path)):
            get_file_size(path)
            largest_files(file_metadata)
        else:
            sys.exit("{directory} is not a directory")
            

    else:
        get_file_size('.')
        largest_files(file_metadata)
    
    
if __name__ == '__main__':
    main()
    