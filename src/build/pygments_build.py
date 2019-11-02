from pygments.cmdline import main as pygmentize

from contextlib import redirect_stdout

import io
import os
import pathlib
import shutil


class PygmentsBuild:
    def make_stylefile(self, outfile, prefix=".syntax", style="vs"):
        args = [
            "pygmentize",
            "-S", style,
            "-f", "html",
            "-a", prefix
        ]

        outdir = os.path.dirname(outfile)
        path = pathlib.Path(outdir)
        if not path.exists():
            path.mkdir(parents=True, exist_ok=True)

        style_str = io.StringIO()
        with redirect_stdout(style_str):
            pygmentize(args)

        style_str.seek(0, 0)

        with open(outfile, "w") as fsrc:
            shutil.copyfileobj(style_str, fsrc)
