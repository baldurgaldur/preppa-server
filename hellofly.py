import logging

from flask import Flask, request
from flask_cors import CORS
from preppa.repositories.recipe_repository import RecipeRepository

app = Flask(__name__)
# TODO: Default is allow all everywhere, we may want to revisit and only allow my github domain
CORS(app)


@app.route('/recipes')
def recipes():
    query_params = request.args.to_dict(flat=False)
    logging.debug("Query params: ", query_params)

    contains = query_params.get("contains")
    print("contains values")
    print(contains)
    # If contains and not_contains are empty, below should be unfiltered
    return RecipeRepository.get_recipes_containing(contains)
