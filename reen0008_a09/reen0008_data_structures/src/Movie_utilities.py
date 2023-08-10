"""
-------------------------------------------------------
CP164 
-------------------------------------------------------
Author:  Gurkarman Reen
ID:      169030008
Email:   reen0008@mylaurier.ca
__updated__ = "2023-02-20"
-------------------------------------------------------
"""
# Imports

# Constants

from Movie import Movie


def get_movie():
    """
    -------------------------------------------------------
    Creates a Movie object by requesting data from a user.
    Use: movie = get_movie()
    -------------------------------------------------------
    Returns:
        movie - a Movie object based upon the user input (Movie).
    -------------------------------------------------------
    """
    title = str(input("Here is title: "))
    Y_o_r = int(input("Here is year of release: "))
    director = str(input("Here is director: "))
    rating = float(input("Here is rating: "))
    genres = read_genres()

    movie = Movie(title, Y_o_r, director, rating,  genres)

    # Your code here

    return movie


def read_movie(line):
    """
    -------------------------------------------------------
    Creates and returns a Movie object from a line of formatted string data.
    Use: movie = read_movie(line)
    -------------------------------------------------------
    Parameters:
        line - a vertical bar-delimited line of movie data in the format
          title|year|director|rating|genre codes (str)
    Returns:
        movie - a Movie object based upon the data from line (Movie)
    -------------------------------------------------------
    """
    movie_s = line.strip().split('|')
    genres = movie_s[4].strip().split(',')

    # Your code here

    genres1 = []

    for i in genres:
        genres1.append(int(i))

    movie = Movie(movie_s[0], int(movie_s[1]),
                  movie_s[2], float(movie_s[3]), genres1)

    return movie


def read_movies(fv):
    """
    -------------------------------------------------------
    Reads a file of string data into a list of Movie objects.
    Use: movies = read_movies(fv)
    -------------------------------------------------------
    Parameters:
        fv - an already open file of movie data (file)
    Returns:
        movies - a list of Movie objects (list of Movie)
    -------------------------------------------------------
    """

    # Your code here

    line = fv.readline()
    movies = []

    while line != "":
        movies.append(read_movie(line))
        line = fv.readline()

    return movies


def read_genres():
    """
    -------------------------------------------------------
    Asks a user to select genres from a list of genres and returns
    an integer list of the genres chosen.
    Use: genres = read_genres()
    -------------------------------------------------------
    Returns:
        genres - sorted numeric list of movie genres (list of int)
    -------------------------------------------------------
    """
    genres = []
    # Your code here
    print(Movie.genres_menu())
    user = str(input("Enter a genre number (ENTER to quit): "))

    while user != "" or len(genres) == 0:

        if user.isdigit() and int(user) >= 0:
            if int(user) <= 10:
                if int(user) in genres:
                    print("Error: genre already chosen")

                else:

                    genres.append(int(user))

            else:
                print("Error: input must be <= 10")

        else:
            if user == "":
                print("Error: must have at least one genre")
            else:
                print("Error: not a positive number")

        user = str(input("Enter a genre number (ENTER to quit): "))

    genres.sort()

    return genres


def write_movies(fv, movies):
    """
    -------------------------------------------------------
    Writes the contents of movies to fv. Overwrites or
    creates a new file of Movie objects converted to strings.
    Use: write_movies(fv, movies)
    -------------------------------------------------------
    Parameters:
        fv - an already open file of movie data (file)
        movies - a list of Movie objects (list of Movie)
    Returns:
        None
    -------------------------------------------------------
    """

    # Your code here

    return


def get_by_year(movies, year):
    """
    -------------------------------------------------------
    Creates a list of Movies from a particular year.
    The original list of movies must be unchanged.
    Use: ymovies = get_by_year(movies, year)
    -------------------------------------------------------
    Parameters:
        movies - a list of Movie objects (list of Movie)
        year - the Movie year to select (int)
    Returns:
        ymovies - Movie objects whose year attribute is
            year (list of Movie)
    -------------------------------------------------------
    """

    # Your code here\
    ymovies = []

    for i in movies:

        if i.year == year:
            ymovies.append(i)

    return ymovies


def get_by_rating(movies, rating):
    """
    -------------------------------------------------------
    Creates a list of Movies whose ratings are equal to or higher
    than rating.
    The original list of movies must be unchanged.
    Use: rmovies = get_by_rating(movies, rating)
    -------------------------------------------------------
    Parameters:
        movies - a list of Movie objects (list of Movie)
        rating - the minimum Movie rating to select (float)
    Returns:
        rmovies - Movie objects whose rating attribute is
            greater than or equal to rating (list of Movie)
    -------------------------------------------------------
    """

    rmovies = []

    for i in movies:
        if i.rating == rating or i.rating > rating:
            rmovies.append(i)
    # Your code here

    return rmovies


def get_by_genre(movies, genre):
    """
    -------------------------------------------------------
    Creates a list of Movies whose list of genres include genre.
    The original list of movies must be unchanged.
    Use: gmovies = get_by_genre(movies, genre)
    -------------------------------------------------------
    Parameters:
        movies - a list of Movie objects (list of Movie)
        genre - the genre code to look for (int)
    Returns:
        gmovies - Movie objects whose genre list includes
            genre (list of Movie)
    -------------------------------------------------------
    """
    gmovies = []

    for i in movies:
        if genre in i.genres:
            gmovies.append(i)

    # Your code here

    return gmovies


def get_by_genres(movies, genres):
    """
    -------------------------------------------------------
    Creates a list of Movies whose list of genres include all the genre
    codes in genres.
    The original list of movies must be unchanged.
    Use: m = get_by_genres(movies, genres)
    -------------------------------------------------------
    Parameters:
        movies - a list of Movie objects (list of Movie)
        genres - the genre codes to look for (list of int)
    Returns:
        gmovies - Movie objects whose genre list includes
            all the genres in genres (list of Movie)
    -------------------------------------------------------
    """

    # Your code here

    gmovies = []

    for i in movies:
        if len(i.genres) <= 2:
            if genres[0] in i.genres and genres[1] in i.genres:
                gmovies.append(i)

    return gmovies


def genre_counts(movies):
    """
    -------------------------------------------------------
    Counts the number of movies in each genre given in Movie.GENRES.
    The original list of movies must be unchanged.
    Use: counts = genre_counts(movies)
    -------------------------------------------------------
    Parameters:
        movies - a list of Movie objects (list of Movie)
    Returns:
        counts - the number of Movies in each genre in Movie.GENRES.
            The index of each number in counts is the index of
            the matching genre in Movie.GENRES. (list of int)
    -------------------------------------------------------
    """

    # Your code here

    counts = []

    for i in range(len(Movie.GENRES)):
        gcount = 0
        for j in movies:
            if i in j.genres:
                gcount = gcount + 1

        counts.append(gcount)

    return counts
