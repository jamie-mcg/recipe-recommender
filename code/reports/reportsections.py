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


class ReportRecommendations(ReportSection):
    def __init__(self, path, data, last_recipe, recommendations, user_id):
        self._header = "Recommendations"
        self._data = data
        self._last_recipe = last_recipe
        self._recommendations = recommendations
        self._user_id = user_id
        self._path = path

    @property
    def body(self):
        string = ""
        string += f"## Last Recipe Cooked by User {self._user_id}: \n"
        string += self._data[self._data.id == self._last_recipe]["name"].values[0]
        string += "\n"
        string += self._data[self._data.id == self._last_recipe]["ingredients"].values[0]
        string += "\n\n"
        string += "## Recommendations Based on this are:"
        for rec_id in self._recommendations:
            string += "\n"
            string += self._data[self._data.id == rec_id]["name"].values[0]
            string += "\n"
            string += self._data[self._data.id == rec_id]["ingredients"].values[0]
            string += "\n"
        return string