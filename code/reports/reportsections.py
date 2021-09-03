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


class ReportTopics(ReportSection):
    def __init__(self, path, model):
        self._header = "Topics"
        self._model = model
        self._path = path

    @property
    def body(self):
        string = ""
        for i in range(self._model.k):
            string += 'Top 10 words of topic #{}'.format(i+1)
            string += '\n'
            topics = self._model.get_topic_words(i, top_n=10)
            for topic in topics:
                string += f"{topic}, "
            string += '\n'
        return string