def favorite_genres(users, movies, movie_ratings):
    for user in users:
        user_ratings, d = [], {}
        for mr in movie_ratings:
            if user['id'] == mr['user_id']:
                for movie in movies:
                    if mr['movie_id'] == movie['id']:
                        if movie['genre'] in d.keys():
                            d[movie['genre']].append(mr['rating'])
                        else:
                            d[movie['genre']] = [mr['rating']]
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