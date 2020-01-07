from typing import Dict, Union

import copy
import yaml


class ConfigParser:
    def __init__(self, config: Union[str, Dict]):
        """
        Parses a config file/dictionary. Items can be accessed via indexing ``config["key"]``,
        the function :func:``value_for`` or like a class member config.key
        """
        self._config: Dict = {}
        if isinstance(config, str):
            with open(config, "r") as f:
                self._config = yaml.load(f, Loader=yaml.SafeLoader)
        elif isinstance(config, dict):
            self._config = copy.copy(config)
        else:
            raise ValueError("Config should be a filename or dictionary of values")

        for key, value in self._config.items():
            setattr(self, key, value)

    def __getitem__(self, key):
        return self.value_for(key)

    def has(self, key: str) -> bool:
        """
        Check if ``key`` is in the config
        """
        return key in self._config

    def value_for(self, key: str):
        """
        Return the value for ``key`` in the config or ``None`` if ``key`` is not in the config
        """
        return self._config[key] if self.has(key) else None
