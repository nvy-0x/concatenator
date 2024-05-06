import os
from os import walk

def combine_files_with_names(file_paths, output_file=None):
    """
    Combines multiple Python files into one continuous string, with each file's content demarcated and
    prefixed with its file name. Each file's content is enclosed in triple apostrophes. Optionally writes to an output file.
    
    Args:
        file_paths (list of str): List of relative paths to the Python files to be combined.
        output_file (str, optional): Path to the output file where the combined contents will be written.
        
    Returns:
        str: The combined contents of all the Python files.
    """
    combined_content = ""
    # Get the directory where the script is running
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    for file_path in file_paths:
        # Construct the full path by combining the base directory and the relative path
        full_path = os.path.join(base_dir, file_path)
        
        if not os.path.exists(full_path):
            print(f"Warning: {full_path} does not exist and will be skipped.")
            continue
        try:
            with open(full_path, 'r', encoding='utf-8') as file:
                # Append file name at the top and demarcate the content
                file_content = file.read()
                combined_content += f"{file_path.split('ez-a-sync/')[1]}\n```\n{file_content}\n```\n\n"
        except IOError as e:
            print(f"Error reading {full_path}: {e}")
    
    if output_file:
        # If an output file is specified, write the combined content to this file
        output_path = os.path.join(base_dir, output_file)
        try:
            with open(output_path, 'w', encoding='utf-8') as file:
                file.write(combined_content)
        except IOError as e:
            print(f"Error writing to {output_path}: {e}")
    
    return combined_content

def get_file_paths(main_dir) :
    f = [f"{dirpath}/{file}" for dirpath, dirnames, filenames in walk(main_dir) for file in filenames]
    print(f)
    return f

my_files = get_file_paths('~/ez-a-sync')