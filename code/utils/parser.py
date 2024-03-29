class Parser():
    def __init__(self, config):
        self._config_args = config

    @property
    def experiment_args(self):
        return self._config_args["Experiment"]

    @property
    def model_args(self):
        return self._config_args["Model"]

    @property
    def recommendation_args(self):
        return self._config_args["Recommendations"]

    def parse(self):
        return self.experiment_args, self.model_args, self.recommendation_args