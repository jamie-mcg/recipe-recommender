# Recipe Recommender

"What shall we eat this evening?"

"What do you fancy?"

"Something like fajitas? But I had that yesterday for lunch..."

"If only we had some sort of Machine Learning based recommendation system that could help us out here..."

I'm sure we've all had this conversation at some point. So this repo is the answer to all our prayers!

## What is it?

This is a fun repo to give a very simple introduction to recommendation systems based on NLP and Embedding techniques. The API is set up so that any model could be used theoretically, however it is currently using a simple LDA model to find the embeddings.

Feel free to fork this repo and make it your own!

## Data

The data can be downloaded from Kaggle and is the Food.com dataset [here](https://www.kaggle.com/shuyangli94/food-com-recipes-and-user-interactions). Just put all the files into a folder named `data' in the home directory of the repo.

## Recommendations

An example of a recommendation result is below:

### Last Recipe Cooked by User 2046: 
neiman marcus  250 chocolate chip cookies recipe
['butter', 'flour', 'baking soda', 'sugar', 'blended oatmeal', 'chocolate chips', 'brown sugar', 'salt', 'hershey bars', 'eggs', 'baking powder', 'vanilla', 'nuts']

### Recommendations Based on this are:
basbousa   semolina cakes with syrup
['sugar', 'water', 'lemon, juice of', 'honey', 'butter', 'eggs', 'vanilla extract', 'semolina', 'baking powder', 'baking soda', 'whole milk', 'almond halve', 'whipped cream']

neiman marcus  250 chocolate chip cookies recipe
['butter', 'flour', 'baking soda', 'sugar', 'blended oatmeal', 'chocolate chips', 'brown sugar', 'salt', 'hershey bars', 'eggs', 'baking powder', 'vanilla', 'nuts']

buttermilk chocolate cake
['hot water', 'cocoa', 'flour', 'baking soda', 'salt', 'butter', 'sugar', 'eggs', 'vanilla', 'buttermilk', 'powdered sugar', 'smooth peanut butter', 'milk']

epiphany cake
['eggs', 'sugar', 'sour cream', 'vanilla extract', 'lemon extract', 'flour', 'baking powder', 'baking soda', 'salt', 'icing sugar', 'butter', 'lemon juice', 'nuts']

aunt toni s texas sheet cake
['sugar', 'flour', 'salt', 'butter', 'water', 'cocoa powder', 'eggs', 'milk', 'vinegar', 'baking soda', 'vanilla extract', 'nuts', 'powdered sugar']
