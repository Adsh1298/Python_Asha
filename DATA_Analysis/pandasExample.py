import pandas as pd
import numpy as np
df = pd.read_csv("imdb_top_1000.csv")
data=df.to_numpy()

print("Data Shape:",data.shape)
print("First 5 rows:",data[:5])

my_set={
   'Cars' : ["Honda", "Maruti", "Hunydai", "Toyota"],
    "rating" :[7, 9, 6, 9]
    }
my_def=pd.DataFrame(my_set)
print(my_def)

data=pd.Series([10,12,14,15,16])
print(data)

##################Extracting column#######################
imdb_ratings = df['IMDB_Rating'].to_numpy()
votes=df['No_of_Votes'].to_numpy()
print(imdb_ratings[:10],votes[:10])

min_rating = np.min(imdb_ratings)
max_rating = np.max(imdb_ratings)
print(f"Rating is b/w {min_rating} and {max_rating}")
top_ratings = imdb_ratings>9
top_movies = df['Series_Title'][top_ratings]
print(top_movies[:5])

#Find top 10 Movies with max no votes:
top_ten = np.argsort(votes)[-5:]
top__5_movies = df.iloc[top_ten]
print("Top 10: \n",top__5_movies[['Series_Title','No_of_Votes','Director']])

#Find the max no of movies released based on Year,
movies_per_year = df.groupby('Released_Year').size()
max_year = movies_per_year.idxmax()
max_count = movies_per_year.max()
print(f"In the year of {max_year},{max_count} no of movies were released")

#Get the Top 5 directors with max no of movies
#Get the no of movies directed by each director
movies_per_director = df.groupby('Director').size();
top_5_directors = movies_per_director.sort_values(ascending=False).head(5)
#key on which grouping is done, in this case, the director.
print(top_5_directors)
 #Get Unique Years:
unique_years = df['Released_Year'].unique()
print(unique_years)

#Display actors of Top rated movies that has rating more than 8.
high_rated = df[df['IMDB_Rating']>8.5]['Star1']
print(high_rated)

#Find the highest Gross Movie:
max_gross = df[df["Gross"]==df["Gross"].max()]
print(max_gross['Series_Title'])


# gross=df["Gross"].to_numpy().max()
# highest_gross_idx = np.argmax(gross)
# highest_grossed_movie = df.iloc[highest_gross_idx]
# print("Movie:",highest_grossed_movie[["Series_Title",'Gross']])

#Find the highest no of actor-director colaborations:






