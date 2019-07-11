from flask import Flask
import pandas as pd

app = Flask(__name__)

movies = pd.read_csv('data/movies.csv')


@app.route("/movie-titles")
def movie_titles():
    result = movies['movie_title']
    return serialize(result)


@app.route("/worst")
def worst():
    result = (
        movies.sort_values('imdb_score').head(5)[['movie_title', 'imdb_score']]

    )
    return serialize(result)


@app.route("/best-rated/<int:year>")
def best_rated(year):
    result = (
        movies[movies['title_year'] == year].sort_values('imdb_score', ascending=False)
            .head(10)[['movie_title', 'imdb_score']]
    )
    return serialize(result)


@app.route('/most-expensive')
def most_expensive():
    result = (
        movies.sort_values('budget', ascending=False).head(10)[['movie_title', 'budget']]
    )
    return serialize(result)


@app.route('/most-expensive/<int:year>')
def most_expensive_year(year):
    result = movies[movies['title_year'] == year].sort_values('budget', ascending=False) \
        .head(10)[['movie_title', 'budget']]
    return serialize(result)


def serialize(result):
    return result.to_json(orient='records')


if __name__ == "__main__":
    app.run()
