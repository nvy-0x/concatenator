import os

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

# Usage example
file_paths = ['a_sync/modifiers/__init__.py', 'a_sync/modifiers/limiter.py', 'a_sync/modifiers/manager.py', 'a_sync/modifiers/semaphores.py', 'a_sync/modifiers/cache/__init__.py', 'a_sync/modifiers/cache/memory.py', 'a_sync/__init__.py', 'a_sync/_descriptors.py', 'a_sync/_flags.py', 'a_sync/_helpers.py', 'a_sync/_kwargs.py', 'a_sync/_meta.py', 'a_sync/abstract.py', 'a_sync/base.py', 'a_sync/config.py', 'a_sync/decorator.py', 'a_sync/function.py', 'a_sync/method.py', 'a_sync/property.py', 'a_sync/singleton.py', 'asyncio/__init__.py', 'asyncio/as_completed.py', 'asyncio/create_task.py', 'asyncio/gather.py', 'asyncio/utils.py', 'primitives/__init__.py', 'primitives/_debug.py', 'primitives/_loggable.py', 'primitives/queue.py', 'primitives/locks/__init__.py', 'primitives/locks/counter.py', 'primitives/locks/event.py', 'primitives/locks/prio_semaphore.py', 'primitives/locks/semaphore.py', 'sphinx/__init__.py', 'sphinx/ext.py', 'utils/__init__.py','utils/as_completed.py', 'utils/gather.py', 'utils/iterators.py', '__init__.py', '_smart.py', 'executor.py', '_bound.py', '_descriptor.py', '_flags.py', '_helpers.py', '_kwargs.py', '_meta.py', '_typing.py', 'abstract.py', 'aliases.py', 'base.py', 'config.py', 'decorator.py', 'ENVIRONMENT_VARIABLES.py', 'exceptions.py', 'future.py', 'iter.py', 'modified.py', 'property.py', 'singleton.py', 'task.py']  # Replace with actual relative file paths
file_paths = ['../ez-a-sync/a_sync/' + path for path in file_paths]
  # Replace with actual relative file paths
combined_content = combine_files_with_names(file_paths, 'combined_output.txt')
print("Files combined successfully.")