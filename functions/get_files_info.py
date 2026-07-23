import os

def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
        valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs

        if valid_target_dir == False:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        if os.path.isdir(target_dir):
            dir_contents = os.listdir(target_dir)
            contents_info = ['Result for current directory:']
            for content in dir_contents:
                content_path = target_dir + '/' + content
                try:
                    content_size = os.path.getsize(content_path) 
                except OSError:
                    return f'Error: file does not exist or is inaccessible'
                
                if os.path.isdir(content_path):
                    contents_info.append(f'{content}: file_size={content_size}, is_dir=True')
                else:
                    contents_info.append(f'{content}: file_size={content_size}, is_dir=False')
            
            return '\n'.join(contents_info)


        else:
            return f'Error: "{directory}" is not a directory'
    except ValueError:
        return 'Error: Path contains both absolute and relative pathnames, paths are on different drives, or path is empty'
