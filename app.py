import json
## Open the JSON file of movie data
movies = open("./movies.json", encoding="utf8")
## create variable "data" that represents the enitre movie list
data = json.load(movies)

genre_filter = input(" genre  (or leave blank): ").lower()
year_filter = input("year to filter (or leave blank): ")
year_filter = int(year_filter) if year_filter else None
title_filter = input(" title (or leave blank) ").lower()

filtered_movies = [
    movie for movie in movies
    if (not genre_filter or movie["genre"].lower() == genre_filter)
    and (not year_filter or movie["year"] >= year_filter)
    and (not title_filter or movie["title"].lower()==title_filter )
]

print("Filtered movies:", filtered_movies)

