from abc import ABC, abstractstaticmethod
from .reportsections import *

import shutil
import os
from datetime import datetime

SECTIONS = {
    "config": ReportConfig,
    "topics": ReportTopics
}

class ReportManager():
    def __init__(self, path_prefix):
        self._path_prefix = path_prefix
        self._sections = []

        dt = datetime.now().strftime("%m%d%Y_%H%M%S")
        if not os.path.exists(self._path_prefix):
            print(self._path_prefix)
            os.mkdir(self._path_prefix, mode=0o777)

        # self._path = os.path.join(self._path_prefix, dt)
        self._path = self._path_prefix

        if not os.path.exists(self._path):
            os.mkdir(self._path, mode=0o777)
        else:
            shutil.rmtree(self._path)
            os.mkdir(self._path, mode=0o777)

    def add_section(self, section, **kwargs):
        new_section = SECTIONS[section.lower()](path=self._path, **kwargs)
        self._sections.append(new_section)

    def save(self):
        with open(os.path.join(self._path, "report.md"), "a") as report_file:
            os.chmod(os.path.join(self._path, "report.md"), 0o777)
            for section in self._sections:
                print(str(section))
                report_file.write(str(section))
        self._sections = []