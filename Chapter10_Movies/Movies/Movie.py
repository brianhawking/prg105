"""
Create a class Movie with the following attributes: title, release_year, story_year.
Create appropriate setter and getter methods.

Download the comma separated data file:  MarvelMovies.csvDownload MarvelMovies.csv

Create a program that reads in the comma separated data file and loads the data from
each line into a Movie object. Each line of data contains title, release year, and story
year in that order. Store the Movie objects in a list. Use try-except as appropriate.

Tip-full-size-gold-1.png Hint: Remember to strip off the newline and split the data
using commas.

Display the movies in alphabetical order. Format the data into columns with appropriate
headings.

Tip-full-size-gold-1.png Hint: Iterate through a sorted list of the movie titles and use
a nested loop to display the details for each movie.
"""

import csv


class Movie:

    def __init__(self, title, release_year, story_year):
        self.__title = title
        self.__release_year = release_year
        self.__story_year = story_year

    def get_title(self):
        return self.__title

    def get_releaseYear(self):
        return self.__release_year

    def get_storyYear(self):
        return self.__story_year

    def set_title(self, title):
        self.__title = title

    def set_releaseYear(self, release_year):
        self.__release_year = release_year

    def set_storyYear(self, story_year):
        self.__story_year = story_year

    def displayRow(self):
        print("{:<36} {:<16} {:<16}".format(
            f"{self.__title}",
            f"{self.__release_year}",
            f"{self.__story_year}"
        ))


movies = []


def sort_movies(movie):
    return movie.title


def main():
    try:
        with open('MarvelMovies.csv', 'r') as file:
            lines = csv.reader(file)
            for row in lines:
                title = row[0]
                release_year = row[1]
                story_year = row[2].rstrip('\n')
                movie = Movie(title, release_year, story_year)
                movies.append(movie)

        # Create table header
        print("{:<36} {:<16} {:<16}".format('Title', 'Release Year', 'Story Year'))

        # Loop through array and create row
        for movie in sorted(movies, key=lambda m: m.get_title()):
            movie.displayRow()

    # called if the file cannot be opened
    except Exception:
        print("SOMETHING WENT WRONG WITH OPENING FILE")


# ========= START ==============
main()
