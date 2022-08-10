from ntpath import join
import os
from subprocess import check_output


def qtui_to_py(path, output_filename):
    cwd = os.getcwd()

    ui_path = os.path.join(cwd, path)

    if not os.path.exists(ui_path):
        print(f'"{ui_path}" does not exist!')
        return False

    try:
        os.remove(f'{output_filename}.py')
    except OSError as e:
        print(e)
    except Exception as e:
        print(e)

    command = f'pyuic5 {os.path.join(cwd, path)} -o {output_filename}.py'

    try:
        check_output(command)
        print(f'Created {output_filename}.py')
    except Exception as e:
        print(e)

    return True
