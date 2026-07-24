import os

def get_file_content(working_directory: str, file_path: str) -> str:
    working_dir_abs: str = os.path.abspath(working_directory)
    target_file: str = os.path.normpath(os.path.join(working_dir_abs, file_path))
    valid_target_dir: bool = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs

    if not valid_target_dir:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    if os.path.isfile(target_file):
        pass
    else:
        return f'Error: File not found or is not a regular file: "{file_path}"'

   