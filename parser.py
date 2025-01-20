# Author : Manoj

from pathlib import Path

def parse_source_files(source_path, delimiter):
    
    # Specify the directory containing .txt files
    directory = Path(source_path)

    # Get all .txt files in the directory
    txt_files = directory.glob('*.txt')

    # Loop through each file and read its content
    for file_path in txt_files:
        with file_path.open('r') as file:
            content = file.read()
            split_data_array = content.split(delimiter)
            print (split_data_array)
    