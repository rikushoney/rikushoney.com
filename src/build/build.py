from os.path import join as join_paths

from .config_parser import ConfigParser
from .pygments_build import PygmentsBuild
from .sass_build import SassBuild
from .jinja_build import JinjaBuild
from .script_build import ScriptBuild
from .static_build import StaticBuild


def build_website(out: str, base: str, config: str):
    """
    As the name suggests, build the website.

    ``out`` is the directory where all the rendered and static files of the
    website will be placed.

    ``base`` is the top-level directory for all the source files.

    ``config`` is a YAML-formatted file which contains the recipes for building
    the website
    """
    cfg = ConfigParser(config)

    pygments = PygmentsBuild()
    pygments.make_stylefile(join_paths(out, "styles", "syntax.css"))

    if cfg.has("styles-dir"):
        scss = SassBuild(join_paths(base, cfg["styles-dir"]))
        scss.compile_styles(join_paths(out, "styles"))

    if cfg.has("scripts-dir"):
        scripts = ScriptBuild(join_paths(base, cfg["scripts-dir"]))
        scripts.minify_scripts(join_paths(out, "scripts"))

    if cfg.has("templates-dir"):
        jinja = JinjaBuild(join_paths(base, cfg["templates-dir"]))
        jinja.render_templates(out, cfg["routes"])

    if cfg.has("static-dir"):
        static = StaticBuild(join_paths(base, cfg["static-dir"]))
        static.copy_content(out)
