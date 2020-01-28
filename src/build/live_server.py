import os

import livereload

from .build import build_website


def start_live_server(port: str, out: str, base: str, config: str):
    server = livereload.Server()

    def rebuild():
        try:
            build_website(out, base, config)
        except Exception as e:
            print(str(e))

    rebuild()

    server.watch(config, func=rebuild)
    server.watch(os.path.join(base, "src"), func=rebuild)
    server.watch(os.path.join(base, "assets"), func=rebuild)
    server.watch(os.path.join(base, "templates"), func=rebuild)
    server.serve(port=port, root=out)
