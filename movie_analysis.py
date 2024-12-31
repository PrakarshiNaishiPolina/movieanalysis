import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# sample movie dataset

data={
'Movie': ['The Shawshank Redemption','The Godfather','The Dark Knight','The Godfather Part 2','12 Angry Men','The Lord of the Rings: The Return of the King','Pulp Fiction','The Lord of the Rings:The Fellowship of the Ring','The Good, the Bad and the Ugly','Forrest Gump'],
'Genre':['Drama','Crime','Action','Crime','Drama','Adventure','Crime','Fantasy','Western','Romance'],
'Year':[1994,1972,2008,1974,1957,2003,1994,2001,1966,1994],
'Rating':[9.3,9.2,9.0,9.0,9.0,9.0,8.9,8.9,8.8,8.8]
}

movies=pd.DataFrame(data)
print(movies)

high_rated_movies=movies[movies['Rating']>9.0]

sorted_movies=movies.sort_values(by='Rating',ascending=False)

print("Movies sorted by Rating:\n",sorted_movies)

average_rating_by_genre=movies.groupby('Genre')['Rating'].mean() # after grouping by the genre and selecting the rating column we calculate only the mean
print("Average Rating by Genre:\n",average_rating_by_genre)

# calculate the mean and std deviation of ratings

mean_rating=np.mean(movies['Rating'])
std_dev_rating=np.std(movies['Rating'])

print(f"Mean Rating: {mean_rating:.2f}")
print(f"Standard Deviation of Rating:{std_dev_rating:.2f}")

# histogram

# for ratings
plt.figure(figsize=(8,4))
plt.hist(movies['Rating'],bins=5,color='skyblue',edgecolor='black') #bins =(1-2,2-3,3-4) like that 5 intervals
plt.title('Distribution of Movie Ratings')
plt.xlabel('Rating')
plt.ylabel('Frequency')
plt.show()

# box plot

plt.figure(figsize=(6,4))
plt.boxplot(movies['Rating'],vert=False,patch_artist=True,boxprops=dict(facecolor='lightgreen'))
plt.title('Box Plot of Movie Ratings')
plt.xlabel('Rating')
plt.show()