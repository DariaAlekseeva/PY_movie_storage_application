"""

Enter
- 'add' to add a movie
- 'view' to view your list of movies
- 'find' to find a movie
- 'quit' to quit the app

Tasks:
[x]: decide where to store movies
[x]: what is the format of a movie
[x]: show the user main interface and get their input
[x]: allow users to add movies
[x]: show all movies
[]: find movies
[x]: stop the app

"""

movies = []

"""
movie = {
    'name': ... (str),
    'director': ... (str),
    'year': ... (str)
        }
        
        
Examples: 

movies = [
    {
        'name': 'The Shawshank Redemption',
        'director': 'Darabont',
        'year': '1994'
    },
    {
        'name': 'The Godfather',
        'director': 'Coppola',
        'year': '1972'
    },
    {
        'name': 'The Dark Knight',
        'director': 'Nolan',
        'year': '2008'
    },
    {
        'name': '12 Angry Men',
        'director': 'Lumet',
        'year': '1957'
    },
    {
        'name': 'Schindler"s List',
        'director': 'Spielberg',
        'year': '1993'
    },
    {
        'name': 'Pulp Fiction',
        'director': 'Tarantino',
        'year': '1993'
    }
]
"""

# define user interface
def menu():
    user_input = input('Enter "add" to add a movie, "view" to view your list of movies, "find" to find a movie '
                       'and "quit" to quit the app: ')

    while user_input != 'quit':
        if user_input == 'add':
            add_movie()
        elif user_input == 'view':
            view_movies(movies)
        elif user_input == 'find':
            find_movie()
        else:
            print('Unknown command. Please try again.')

        user_input = input('\nEnter "add" to add a movie, "view" to view your list of movies, "find" to find a movie '
                           'and "quit" to quit the app: ')

    if user_input == 'quit':
        print('Stopping program...')


# add new movie
def add_movie():
    name = input('What is the movie name? ')
    director = input('Who is the director of the movie? ')
    year = input('What is the year of the movie? ')

    movies.append({
        'name': name,
        'director': director,
        'year': year
         })


# view all movies
def view_movies(movie_list):
    if len(movies) > 0:
        for movie in movie_list:
            show_movie_details(movie)
    else:
        print('No movies in your collection.')


# prints out movie details in readable format
def show_movie_details(movie):
    print(f'Name: {movie["name"]}')
    print(f'Director: {movie["director"]}')
    print(f'Year: {movie["year"]}')


# function which asks user about property and value they are looking for
def find_movie():
    property = input('Choose the property: ')
    value = input('Choose the value: ')

    found_movies = find_by_attributes(movies, value, lambda x: x[property])

    view_movies(found_movies)



def find_by_attributes(items, expected, finder):
    requested_movies = []

    for i in items:
        if finder(i) == expected:
            requested_movies.append(i)

    return requested_movies

menu()

