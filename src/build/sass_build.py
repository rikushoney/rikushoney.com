import sass


class SassBuild:
    def __init__(self, styles_path):
        self._styles = styles_path

    def compile_styles(self, target, format="expanded"):
        sass.compile(dirname=(self._styles, target), output_style=format)
