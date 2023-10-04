from file_selector import select_txt_files
from file_io_utils import write_to_csv, read_txt_file
from data_processor import process_lines
from tkinter import messagebox

def main():
    file_paths = select_txt_files()
    
    for file_path in file_paths:
        lines = read_txt_file(file_path)
        processed_data = process_lines(lines)
        output_file_path = file_path.replace('.txt', '.csv')
        
        write_to_csv(processed_data, output_file_path)

if __name__ == '__main__':
    main()
