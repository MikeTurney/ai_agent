import os
from config import MAX_CHARS

def get_file_content(working_directory: str, file_path: str) -> str:
    try:
        working_dir_abs: str = os.path.abspath(working_directory)
        target_file: str = os.path.normpath(os.path.join(working_dir_abs, file_path))
        valid_target_dir: bool = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs

        if not valid_target_dir:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        if os.path.isfile(target_file):
            with open(target_file, 'r') as file:
                content = file.read(MAX_CHARS)
                if file.read(1):
                    content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
                return content
        else:
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
    except ValueError:
        return f'Error: Invalid file path: "{file_path}"'
    
    except Exception as e:
        return f'Error: {str(e)}'

schema_get_file_content = {
    "type": "function",
    "function": {
        "name": "get_file_content",
        "description": "Retrieves the content of a specified file relative to the working directory, truncated if it exceeds the maximum character limit",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path to the file to retrieve content from, relative to the working directory",
                },
            },
        },
    }
}
