from calmjs.parse import es5
from calmjs.parse.asttypes import ExprStatement, FunctionCall
from calmjs.parse.unparsers.es5 import minify_print

from pathlib import Path

import os


class ScriptBuild:
    def __init__(self, script_dir):
        self._scripts = script_dir

    def minify_scripts(self, target):
        """
        Remove whitespace and obfuscate Javascript files to reduce filesize.

        All files that end with '.js' and does not start with an '_' get minified
        into a smaller file in the target directory.
        Files starting with an '_' gets treated as modules - they are copied into
        other Javascript files using the 'require' function.
        """
        scripts = [f for f in os.scandir(self._scripts)
                   if f.name.endswith(".js")
                   and not f.name.startswith("_")]

        target_dir = Path(target)
        if not target_dir.is_dir():
            target_dir.mkdir(parents=True, exist_ok=True)

        for script in scripts:
            with open(script.path, "r") as f:
                program = es5(f.read())
                self.resolve_imports(program)

                with open(os.path.join(target, script.name), "w") as s:
                    s.write(minify_print(program, obfuscate=True, obfuscate_globals=True))

    def resolve_imports(self, program):
        """
        Walk the AST, look for any 'require' calls and replace them with the
        module specified as the first argument of the function call
        """
        for index, node in enumerate(program.children()):
            if ScriptBuild.is_import(node):
                filename = str(node.expr.args.children()[0]).strip("\"'")
                if not os.path.isfile(filename):
                    filename = filename + ".js"
                if not os.path.isfile(filename):
                    filename = "_" + filename
                with open(os.path.join(self._scripts, filename), "r") as mod:
                    module = es5(mod.read())
                    program.children()[index:index+1] = module.children()

    @staticmethod
    def is_import(node):
        return (isinstance(node, ExprStatement)
                and isinstance(node.expr, FunctionCall)
                and str(node.expr.identifier) == "require")
