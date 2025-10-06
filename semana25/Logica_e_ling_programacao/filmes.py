#pip install cinemagoer

from imdb import IMDb

ia = IMDb()

nome = input('Digite o nome do filme: ')

movies = ia.search_movie(nome)
movie_id = movies[0].movieID

movie = ia.get_movie(movie_id)

print('Title:', movie['title'])
print('Year:', movie['year'])
print('Kind:', movie['kind'])
print('Info:', movie.current_info)

print('Summary:', movie.summary())

#print(dir(movie))

