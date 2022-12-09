import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

os.system("dropdb ratings")
os.system('createdb ratings')

model.connect_to_db(server.app)
model.db.create_all()

with open('data/movies.json') as f:
    movie_data = json.loads(f.read())

# create movies and add to the database
movies_in_database = []

for movie in movie_data:
    title, overview, poster_path = (
        movie['title'],
        movie['overview'],
        movie['poster_path'],
    )

    release_date = datetime.strftime(movie['release_date'], '%Y-%m-%d')

    db_movie = crud.create_movie(title, overview, release_date, poster_path)
    movies_in_database.append(db_movie)

model.db.session.add_all(movies_in_database)
model.db.session.commit()

# create10 users and add to database

for n in range(10):
    email = f'User email= user{n}@test.com'
    password = 'test'

    user = crud.create_user(email, password)
    model.db.session.add(user)

    # create 10 ratings per user and add to database
    for _ in range(10):
        random_movie = choice(movies_in_database)
        score = randint(1, 5)

        rating = crud.create_rating(user, random_movie, score)
model.db.session.commit()
