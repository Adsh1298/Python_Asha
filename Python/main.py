import csv
from unittest import case
import MovieRepo as movieRepo
from  Movie update_feature

get_movie_details

movieDb

movieDb


def add_feature():
    id=int(input("Enter a movie ID: "))
    title=input("Enter a movie title: ")
    director=input("Enter a  director Name: ")
    year=int(input("Enter a Year of Release: "))
    new_movie=Movie(id,title,director,year)
    return new_movie
def select_feature():
    title=input("Enter a movie title to search: ")
    found=movieDb.get_movie_details(title)
    if not found:
        print("No Movie found to dislay")
    else:
        print(found)

def add_movie(self,movie):
    with open(self.filename,'a',newline='') as file:
    writer=csv.writer(file)
    writer.writerow([movie.id,movie.title,movie.director,movie.year])
    print(movie)

def view_all_feature():
    movies = movieDb.list_movies()
    if not movies:
        print("No movies are available")
    else:
        for m in movies:
            print(m)


from Ex18EmpRepository import adding_feature
from MovieRepo import MovieRepository as repo
choice = input("Enter your choice: [1-4]")
match choice:
    case "1":
        new_movie= get_movie_details()
        add_feature(new_movie)
    case "2":

        view_all_features()
    case "3":
        print("Enter the Details of for Updating")
        updating_movie = get_movie_details()
        update_feature(updating_movie)
        update_feature()
    case "4":
        select_feature()
    case_:
        print("invalid Choice,Please try again !!!")
#####################TODO####################
'''

'''