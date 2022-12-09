import psycopg2
import psycopg2.extras
import logging
import traceback
from typing import List


class RecipeRepository:
    _connection_string = "postgres://postgres:KD1IG168GauMdAc@preppa-test.internal:5432"

    # TODO: Add id column
    _GET_RECIPES_SQL = "SELECT * from recipes where ingredients @> %s;"
    _GET_ALL_RECIPES_SQL = "SELECT * from recipes;"

    @staticmethod
    def get_recipes_containing(contains: List[str]) -> dict:
        try:
            # Connect to postgres DB and open cursor
            conn = psycopg2.connect(RecipeRepository._connection_string)
            cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

            # Execute a query.
            if contains:
                cur.execute(RecipeRepository._GET_RECIPES_SQL, (contains,))
            else:
                cur.execute(RecipeRepository._GET_ALL_RECIPES_SQL)

            # Retrieve query results. list of tuples
            records = cur.fetchall()
            return records
        except Exception as ex:
            logging.exception(ex)
            return {}

    @staticmethod
    def get_recipes_without(self):
        print("foo")

    # TODO: get recipes containing and without. I.e. include this
