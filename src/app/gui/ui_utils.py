import subprocess
import os

from src.app.utils import PATH

__all__ = ['compile_ui']


def compile_ui():
    for i in os.scandir(PATH.UI):
        i: os.DirEntry
        if i.name.lower().endswith('.ui'):
            proc = subprocess.run(['pyside6-uic', i.path], capture_output=True, check=True)
            path, _ = os.path.splitext(i.path)
            with open(''.join((path, '.py')), mode='wb') as f:
                f.write(proc.stdout)


if __name__ == '__main__':
    compile_ui()
