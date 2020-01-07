from os.path import join as join_paths

from .config_parser import ConfigParser
from .pygments_build import PygmentsBuild
from .sass_build import SassBuild
from .jinja_build import JinjaBuild
from .static_build import StaticBuild


def build_website(out: str, base: str, config: str):
    """
    As the name suggests, build the website.

    ``out`` is the directory where the final files of the website will be placed

    ``base`` is the directory where all the source files rely

    ``config`` is a YAML-formatted file which contains all the "routes"
    and directories where different source files are located are defined
    """
    cfg = ConfigParser(config)

    pygments = PygmentsBuild()
    pygments.make_stylefile(join_paths(out, "styles", "syntax.css"))

    scss = SassBuild(join_paths(base, cfg["styles-dir"]))
    scss.compile_styles(join_paths(out, "styles"))

    jinja = JinjaBuild(join_paths(base, cfg["templates-dir"]))
    jinja.render_templates(out, cfg["routes"])

    static = StaticBuild(join_paths(base, cfg["static-dir"]))
    static.copy_content(out)
