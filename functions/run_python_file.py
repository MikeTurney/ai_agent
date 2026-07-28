import os
import subprocess

def run_python_file(
        working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
        try:
            absolute_working_dir: str = os.path.abspath(working_directory)
            absolute_file_path: str = os.path.normpath(os.path.join(absolute_working_dir, file_path))
            valid_target_dir: bool = os.path.commonpath([absolute_working_dir, absolute_file_path]) == absolute_working_dir

            if not valid_target_dir:
                return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

            if os.path.isfile(absolute_file_path):
                  if absolute_file_path.endswith('.py'):
                       command = ["python", absolute_file_path]
                       command.extend(args or [])
                       subprocess_result = subprocess.run(command, capture_output=True, text=True, timeout=30)
                       result = []
                       if subprocess_result.returncode == 0:
                            result.append(f'Process exited with code {subprocess_result.returncode}')
                       if len(subprocess_result.stdout) == 0 and len(subprocess_result.stderr) == 0:
                            return f'No output produced'
                       else:
                            if len(subprocess_result.stdout) > 0:
                                result.append(f'STDOUT: {subprocess_result.stdout}')
                            if len(subprocess_result.stderr) > 0:
                                result.append(f'STDERR: {subprocess_result.stderr}')
                            return '\n'.join(result)
                  else:
                       return f'Error: "{file_path}" is not a Python file'
            else:
                  return f'Error: "{file_path}" does not exist or is not a regular file'


        except ValueError:
            return f'Error: Invalid file path: "{file_path}"'
        
        except Exception as e:
            return f'Error: executing Python file: {str(e)}'