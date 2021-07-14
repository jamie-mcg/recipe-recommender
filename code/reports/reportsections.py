from abc import ABC, abstractstaticmethod
import json
import numpy as np

class ReportSection(ABC):
    @property
    def header(self):
        return "## " + self._header

    @property
    @abstractstaticmethod
    def body(self):
        pass

    def __str__(self):
        return self.header + "\n" + self.body + "\n"


class ReportConfig(ReportSection):
    def __init__(self, path, config_file):
        self._header = "Config"
        self._config = config_file
        self._path = path

    @property
    def body(self):
        string = json.dumps(self._config, indent=True)
        return "\n" + string + "\n"