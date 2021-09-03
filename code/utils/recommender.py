import numpy as np

def cosine(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

SIMILARITY_METRIC = {
    "cosine": cosine
}

class Recommender():
    def __init__(self, data, embeddings, user_id, num_recommendations=5, metric="cosine"):
        self._data = data
        self._user_id = user_id
        self._embeddings = embeddings
        self.metric = SIMILARITY_METRIC[metric]
        self._num_recommendations = num_recommendations

        self.user_history = self.get_user_history()

        self.last_recipe_cooked = self.user_history["recipe_id"].values[0][-1]

        self.last_recipe_embed = embeddings[embeddings.index == self.last_recipe_cooked]

    def get_user_history(self):
        all_user_history = self._data.groupby("user_id")["recipe_id"].apply(list).reset_index()
        return all_user_history[all_user_history.user_id == self._user_id]

    def get_similarities(self):
        sims = []
        for target_embed in self._embeddings:
            sims.append(self.metric(self.last_recipe_embed.values[0], target_embed))
        return sims

    def get_recommendations(self):
        sims = self.get_similarities()
        recommendation_ids = list(self._embeddings.iloc[np.argsort(sims)][-self._num_recommendations:].index)
        return self.last_recipe_cooked, recommendation_ids
        