from utils import get_movie_by_title, get_movie_by_year, get_movie_by_rating, get_movie_by_genre
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/movies/")
def page_movies():
    title = request.args.get("name")
    movie = get_movie_by_title(title)
    return render_template("movies.html", movie=movie)


@app.route("/movie/year/", methods=["POST"])
def page_movies_year():
    s_year = int(request.form["s_year"])
    po_year = int(request.form["po_year"])
    movie = get_movie_by_year(s_year, po_year)
    return render_template("movies_year.html", movie=movie)


@app.route("/movies/<title>")
def get_json_title(title):
    post_id = get_movie_by_title(title)
    return jsonify(post_id)


@app.route("/movie/<int:s_year>/to/<int:po_year>")
def get_json_years(s_year, po_year):
    post_id = get_movie_by_year(s_year, po_year)
    return jsonify(post_id)


# @app.route("/rating/children")
# def get_json_rating_children():
#     rating_g = get_movie_by_rating("G")
#     return jsonify(rating_g)
#
#
# @app.route("/rating/family")
# def get_json_rating_family():
#     rating_g = get_movie_by_rating("G")
#     rating_pg = get_movie_by_rating("PG")
#     rating_pg_13 = get_movie_by_rating("PG-13")
#     return jsonify(rating_g + rating_pg + rating_pg_13)
#
#
# @app.route("/rating/adult")
# def get_json_rating_adult():
#     rating_r = get_movie_by_rating("R")
#     rating_nc_17 = get_movie_by_rating("NC-17")
#     return jsonify(rating_r + rating_nc_17)

@app.route("/rating/<rating>")
def get_json_rating(rating):
    rating_j = {"children": ["G"], "family": ["G", "PG", "PG-13"], "adult": ["R", "NC-17"]}
    if rating in rating_j:
        rating_sql = '\", \"'.join(rating_j[rating])
        rating_sql = f'\"{rating_sql}\"'
    else:
        return jsonify([])
    return jsonify(get_movie_by_rating(rating_sql))




@app.route("/genre/<genre>")
def get_json_genre(genre):
    genre = get_movie_by_genre(genre)
    return jsonify(genre)


if __name__ == "__main__":
    app.run(debug=True)
