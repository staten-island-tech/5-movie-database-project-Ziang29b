genre_filter = input
user_input= input
year_filter = input
user_input= input 

filtered_movies = [
    movie for movie in movies:
    if movie["genre"] == genre_filter and movie["year"] >= year_filter
]

print(filtered_movies)