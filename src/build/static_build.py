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
        Copies content from ``source`` to ``dest`` recursively overwriting existing files
        """
        path = pathlib.Path(dest)
        if not path.exists():
            path.mkdir(parents=True, exist_ok=True)

        for file in os.scandir(source):
            if file.is_dir():
                StaticBuild.copy_recursively(
                    file.path, os.path.join(dest, file.name))
            else:
                shutil.copy2(file.path, dest)
