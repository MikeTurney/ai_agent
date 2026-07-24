import os

def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        working_dir_abs: str = os.path.abspath(working_directory)
        target_dir: str = os.path.normpath(os.path.join(working_dir_abs, directory))
        valid_target_dir: bool = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs

        if valid_target_dir == False:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        if os.path.isdir(target_dir):
            dir_files: list[str] = os.listdir(target_dir)
            file_info: list[str] = ['Result for current directory:']
            for file in dir_files:
                file_path: str = os.path.join(target_dir, file)
                try:
                    file_size = os.path.getsize(file_path) 
                except OSError:
                    return f'Error: file does not exist or is inaccessible'
                
                if os.path.isdir(file_path):
                    file_info.append(f'{file}: file_size={file_size}, is_dir=True')
                else:
                    file_info.append(f'{file}: file_size={file_size}, is_dir=False')
            
            return '\n'.join(file_info)


        else:
            return f'Error: "{directory}" is not a directory'
    except ValueError:
        return 'Error: Path contains both absolute and relative pathnames, paths are on different drives, or path is empty'
