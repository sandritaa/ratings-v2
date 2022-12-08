from model import db, User, Movie, Rating, connect_to_db


def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

    return user


def create_movie(title, overview, release_data, poster_path):
    # create and return a movie

    movie = Movie(title=title, overview=overview,
                  release_data=release_data, poster_path=poster_path)

    return movie


def create_rating(score, user, movie):

    rating = Rating(score=score, user=user, movie=movie)

    return rating


if __name__ == '__main__':
    from server import app
    connect_to_db(app)
