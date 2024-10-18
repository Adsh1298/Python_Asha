# class Movie:
#     def __init__(self, id, title, director, year):
#         self.id = id
#         self.title = title
#         self.director = director
#         self.year = year
#
#      def __str__(self):
#         return f"Id: {self.id}, Title: {self.title}, Director : {self.director}, Releasing Year: {self.year}"
import MovieRepo as movieRepo
from Movie import Movie
movieDb=movieRepo.MovieRepository("demo.csv")
def get_movie_details():
    id=int(input("Enter movie ID: "))
    title=input("Enter movie title: ")
    director=input("Enter the Director Name: ")
    year=input("Enter the year of release: ")
    return movie
add_feature=lamda movie :movieDb.add_movie(movie)
def update_feature():
    pass
def select_feature():
    pass
def view_all_feature():
   movies=movieDb.list_movies()
   if not movies:
       print("No movies found")
   else for movie in movies:

   for m in movies
choice=input("Enter the Choice:[1-4]")
match choice
case "1":
new_movie=get_movie_details()

