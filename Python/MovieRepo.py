import csv


class MovieRepository:
    def __init__(self, file_name):
        self.file = file_name

    def add_movie(self, movie):
        with open(self.filename, 'a',newline='') as file:
        writer = csv.writer(file)
        writer.writerow([movie.id,movie.title,movie.director,movie.year])
        pass
    def list_movies(self):
        movies = []
        try:
            with open(self.filename,'r',newline='') as file:
                reader=csv.reader(file)
                for row in reader:
                    movies.append(Movie(row[1],(row[2],row[3],row[4])
        except FileNotFoundError as ferr:
            print(f"File Not Found: {ferr}")
        else:
            print("The Total movies", len(movies))
            return movies

    def update_movie(self, movie_id, modified_movie):
        movies=self.list_movies()
        updated=False
        with open(self.filename,'w',newline='') as file:
            writer = csv.writer(file)
            for movie in movies:
                if (movie.id == movie_id):
                    writer.writerow([modified_movie.id,modified_movie.title,modified_movie.director,
                                     modified_movie.year])
                    Updated = True

        pass
    def get_movie_detail(self, movie_title):
        movies = self.list_movies()
        temp = list(filter(lamda movie: movie.title == movie_title, movies))
        return temp[0]
