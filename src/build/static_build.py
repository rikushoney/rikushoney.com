import os
import pathlib
import shutil


class StaticBuild:
    def __init__(self, static):
        self._static = static

    def copy_content(self, outpath):
        StaticBuild.copy_recursively(self._static, outpath)

    @staticmethod
    def copy_recursively(source, dest):
        """
        Copies content in ``source`` to ``dest`` recursively overwriting existing files
        """
        source = os.path.abspath(source)
        dest = os.path.abspath(dest)

        path = pathlib.Path(dest)
        if not path.exists():
            path.mkdir(parents=True, exist_ok=True)

        for file in os.listdir(source):
            file_abs = os.path.join(source, file)
            if os.path.isdir(file_abs):
                StaticBuild.copy_recursively(
                    file_abs, os.path.join(dest, file))
            else:
                shutil.copy2(file_abs, dest)
