import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")
all_movies = soup.find_all(name="h3")

# top_100_movies = []

# for tag in all_movies:
#     title_name = tag.getText()
#     movie = title_name.split(")")
#
#     if len(movie) != 2:
#         movie = title_name.split(":")
#
#     movie_rank = int(movie[0])
#     movie_title = movie[1]
#
#     top_100_movies.append([movie_rank, movie_title])
#
# print(type(top_100_movies))

movie_titles = [movie.getText() for movie in all_movies]

movies = movie_titles[::-1]

with open("movie.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")