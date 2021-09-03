import pandas as pd
import numpy as np
import random
import gensim
import argparse
import json
from ast import literal_eval
import os

from models import LDAModel
from reports import ReportManager
from utils import Parser, Recommender

MODELS = {
    "lda": LDAModel
}

if __name__ == "__main__":
    # TO DO:
    # - Load in dataloaders
    # - Run LDA model on data
    # - Add results to report
    # - Save embeddings
    # - Allow extra models
    # - Get rid of most common ingredients

    # Take in command line argument and parse args
    cli_parser = argparse.ArgumentParser(description="Recipe Recommender")
    cli_parser.add_argument('--config', '-c', type=str, help='File containing configuration for experiment.',
                            default='config/test.json')
    args = cli_parser.parse_args()

    # Load in the config file
    if args.config:
        with open(args.config) as json_file:
            config = json.load(json_file)
    else: 
        raise ValueError("JSON config file does not exist.")

    # Parse the arguments
    parser = Parser(config)
    # Unpack the arguments
    exp_args, model_args, recommendation_args = parser.parse()

    # Create a report.
    report = ReportManager(exp_args["save_path"])
    # Add configuration to report.
    report.add_section(section="config", config_file=config)
    report.save()

    # Update the random seeds for reproducible results.
    if exp_args["seed"]:
        # torch.random.manual_seed(exp_args["seed"])
        np.random.seed(exp_args["seed"])
        random.seed(exp_args["seed"])

    raw_recipes = pd.read_csv(os.path.join(exp_args["path"], "RAW_recipes.csv"))

    texts = raw_recipes.ingredients.apply(literal_eval)
    dictionary = gensim.corpora.Dictionary(texts)

    corpus = [dictionary.doc2bow(x) for x in texts]

    model = MODELS[model_args["name"].lower()](**model_args["args"])

    for text in texts:
        model.add_doc(text)

    for i in range(10):
        model.train()

    embeddings = np.zeros((len(texts), model.k))

    for i, doc in enumerate(model.docs):
        embeddings[i, :] = doc.get_topic_dist()

    embeddings_series = pd.Series(embeddings.tolist(), index=raw_recipes.id)

    # Add topics to report.
    report.add_section(section="topics", model=model)
    report.save()

    interactions_train = pd.read_csv(os.path.join(exp_args["path"], "interactions_train.csv"))

    recommender = Recommender(interactions_train, embeddings_series, **recommendation_args["args"])
    last_meal, recommendation_ids = recommender.get_recommendations()

    report.add_section(section="recommendations", data=raw_recipes, last_recipe=last_meal, \
                    recommendations=recommendation_ids, user_id=recommendation_args["args"]["user_id"])
    report.save()


