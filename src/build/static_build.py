import os
import shutil


class StaticBuild:
    def __init__(self, static, out):
        self._static = static
        self._out = out

    def copy_content(self):
        StaticBuild.copy_recursively(self._static, self._out)

    @staticmethod
    def copy_recursively(source, dest):
        """
        Copies content in ``source`` to ``dest`` recursively overwriting existing files
        """
        source = os.path.abspath(source)
        dest = os.path.abspath(dest)

        if not os.path.exists(dest):
            os.mkdir(dest)

        for file in os.listdir(source):
            file_abs = os.path.join(source, file)
            if os.path.isdir(file_abs):
                StaticBuild.copy_recursively(
                    file_abs, os.path.join(dest, file))
            else:
                shutil.copy2(file_abs, dest)
