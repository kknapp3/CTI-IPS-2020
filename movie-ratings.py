# Given:
# - A list of users, by ID
# users = [{id: "923874rksd9293"}]
# 
# - A list of movies, by ID, with their genres attached
# movie_ratings = [
#   {
#     "movie_id": "20jfcf02341kwd",
#     "user_id": "923874rksd9293", 
#     "rating": 5
#   }
# ]
# 
# - A list of movie IDs, with their rating (a number, 1-5), and which userID gave that rating
# movies = [
#   {
#      "id": "20jfcf02341kwd",
#      "genre": "animated"
#   }
# ]
# 
# Return a list of users, with their favorite movie genres based on their submitted movie ratings. "Favorite Genre" means the genre with the highest average rating. If there are multiple with the same average, return the first one you find with a perfect 5.0.
# users = [
#   {
#     "id": "923874rksd9293",
#     "favorite_genre": "animated"
#   }
# ]
# 
# In order to simplify the problem, Movies will always have a single genre, all movies from the movie_ratings list will be in the movies list, and all users from the movie_ratings list will be in the users list.
# 


def favorite_genres(users, movies, movie_ratings):
    for user in users:
        user_ratings, d = [], {}
        for rating in movie_ratings:
            if user['id'] == rating['user_id']:
                for movie in movies:
                    if rating['movie_id'] == movie['id']:
                        if movie['genre'] in d.keys():
                            d[movie['genre']].append(rating['rating'])
                        else:
                            d[movie['genre']] = [rating['rating']]
        mx = max([sum(v) / len(v) for v in d.values()])
        for k,v in d.items():
            if mx == sum(v) / len(v):
                if not user_ratings or (5 in v and 5 not in user_ratings):
                    user_ratings = [k] + v
        user['favorite_genre'] = user_ratings[0]
    return users


users = [{'id': "923874rksd9293"}, {'id': "923874rksd9294"}]

movies = [
  {
     'id': "20jfcf02341kwd",
     'genre': "animated"
  },
  {
     'id': "20jfcf02341kwe",
     'genre': "action"
  },
  {
     'id': "20jfcf02341kwf",
     'genre': "action"
  }
]

movie_ratings = [
  {
    'movie_id': "20jfcf02341kwd",
    'user_id': "923874rksd9293", 
    'rating': 5
  },
  {
    'movie_id': "20jfcf02341kwe",
    'user_id': "923874rksd9293", 
    'rating': 3
  },
  {
    'movie_id': "20jfcf02341kwf",
    'user_id': "923874rksd9293", 
    'rating': 1
  },
  {
    'movie_id': "20jfcf02341kwd",
    'user_id': "923874rksd9294", 
    'rating': 2
  },
  {
    'movie_id': "20jfcf02341kwe",
    'user_id': "923874rksd9294", 
    'rating': 4
  },
  {
    'movie_id': "20jfcf02341kwf",
    'user_id': "923874rksd9294", 
    'rating': 3
  }
]

print(favorite_genres(users, movies, movie_ratings))
