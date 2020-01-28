from calmjs.parse import es5
from calmjs.parse.unparsers.es5 import minify_print

from pathlib import Path

import io
import os


class ScriptBuild:
    def __init__(self, script_dir):
        self._scripts = script_dir

    def minify_scripts(self, target_script):
        scripts = [f.path for f in os.scandir(self._scripts)
                   if f.name.endswith(".js")]

        text = io.StringIO()
        for script in scripts:
            with open(script, "r") as f:
                print(f.read(), file=text)
        text.seek(0)

        target_script = Path(target_script)
        target_dir = target_script.parent
        if not target_dir.is_dir():
            target_dir.mkdir(parents=True, exist_ok=True)

        program = es5(text.getvalue())
        with open(target_script.absolute(), "w") as t:
            t.write(minify_print(program, obfuscate=True, obfuscate_globals=True))
