import random
import re

films = [
    'The Godfather (1972)',
    'The Shawshank Redemption (1994)',
    'The Godfather, Part II (1974)',
    'The Dark Knight (2009)',
    '12 Angry Men (1957)',
    'Schindler\'s List (1993)',
    'The Lord of the Rings: The Return of the King (2003)',
    'Pulp Fiction (1994)',
    'The Good, the Bad, and the Ugly (1966)',
    'The Lord of the Rings: The Fellowship of the Ring (2001)',
    'Fight Club (1999)',
    'Forrest Gump (1994)',
    'Inception (2010)',
    'The Lord of the Rings: The Two Towers (2002)',
    'Star Wars: Episode V: The Empire Strikes Back (1980)',
    'The Matrix (1999)',
    'GoodFellas (1990)',
    'One Flew Over The Cuckoo\'s Nest (1975)',
    'The Seven Samurai (1954)',
    'Se7en (1995)',
    'Life is Beautiful (1997)',
    'City of God (2002)',
    'The Silence of the Lambs (1991)',
    'It\'s A Wonderful Life (1946)',
    'Star Wars (1977)',
    'Saving Private Ryan (1998)',
    'Spirited Away (2001)',
    'The Green Mile (1999)',
    'Interstellar (2014)',
    'Parasite (2019)',
    'Leon, aka The Professional (1994)',
    'The Usual Suspects (1995)',
    'Harakiri (1962)',
    'The Lion King (1994)',
    'Back to the Future (1985)',
    'The Pianist (2002)',
    'Terminator 2: Judgment Day (1991)',
    'American History X (1998)',
    'Modern Times (1936)',
    'Psycho (1960)',
    'Gladiator (2000)',
    'City Lights (1931)',
    'The Departed (2006)',
    'The Intouchables (2011)',
    'Whiplash (2014)',
    'The Prestige (2006)',
    'Grave of the Fireflies (1988)',
    'Hamilton (2020)',
    'Once Upon a Time in the West (1969)',
    'Casablanca (1942)',
    'Cinema Paradiso (1988)',
    'Rear Window (1954)',
    'Alien (1979)',
    'Apocalypse Now (1979)',
    'Memento (2000)',
    'The Great Dictator (1940)',
    'Raiders of the Lost Ark (1981)',
    'Django Unchained (2012)',
    'The Lives of Others (2006)',
    'Joker (2019)',
    'Paths of Glory (1957)',
    'WALL-E (2008)',
    'The Shining (1980)',
    'Avengers: Infinity War (2018)',
    'Sunset Boulevard (1950)',
    'Witness For the Prosecution (1957)',
    'Spider-Man: Into the Spider-Verse (2018)',
    'Oldboy (2003)',
    'Princess Mononoke (1997)',
    'Dr. Strangelove or: How I Learned To Stop Worrying and Love the Bomb (1964)',
    'The Dark Knight Rises (2012)',
    'Once Upon a Time in America (1984)',
    'Aliens (1986)',
    'Your Name. (2016)',
    'Avengers: Endgame (2019)',
    'Coco (2017)',
    'American Beauty (1999)',
    'Braveheart (1995)',
    'Das Boot (1981)',
    '3 Idiots (2009)',
    'Toy Story (1995)',
    'High and Low (1963)',
    'Capernaum (2018)',
    'Amadeus (1984)',
    'Inglourious Basterds (2009)',
    'Star Wars: Episode VI - Return of the Jedi (1983)',
    'Like Stars on Earth (2007)',
    'Good Will Hunting (1997)',
    'Reservoir Dogs (1992)',
    '2001: A Space Odyssey (1968)',
    'Requiem for a Dream (2000)',
    'Vertigo (1958)',
    'M (1931)',
    'Eternal Sunshine of the Spotless Mind (2004)',
    'The Hunt (2012)',
    'Dangal (2016)',
    'Citizen Kane (1941)',
    '1917 (2019)',
    'Full Metal Jacket (1987)',
    'The Bicycle Thief (1948)',
]


def main():
    input('\nHello, press enter to play hangman!')
    print('\nEnter -e or --exit to end game')
    print('Enter -r or --retry to restart game with another movie.\n\n')

    
    # select a random movie
    movie, year = select_movie(films)

    # print movie name and year - DEMO
    # print(f'(Demo purpose - Movie name : {movie})\n')
    
    # frame question with blanks
    ques = question(movie)

    # create list of moviename
    movie_list = [letter for letter in movie]

    # run game and get result
    res = game(ques, movie_list, year)

    if res == 'exit':
        print('Game Ended.')
        return
    if res == True or res == False: 
        print(get_result(res))


def select_movie(films):
    movie = random.choices(films)
    
    if search := re.search(r'^([A-Za-z0-9_.-:,\' ]*) \((\d{4})\)$', movie[0]):
        return search.groups()


def question(movie_name):
    q = []
    for letter in movie_name:
        if letter.isalpha() or letter.isnumeric():
            q.append('_')
        else:
            q.append(letter)

    return q


def game(question, movie, year):

    # create moviename in str
    moviename = ''.join(map(str, movie)).strip().lower()

    # copy moviename list 
    moviecp = movie.copy()

    # create a list of all elements of movie in lowercase
    lower_movie = [x.lower() for x in movie]
    
    # initiate counter
    count = 1
    hint = False

    while count < 11 and '_' in question:
        print(*question, '\n')

        if count > 5 and hint == False:
            print('To get hint, enter \'--hint\'\n')

        answer = input(f'Guess a character or the movie name ({11-count} chances left): ').lower().strip()

        if answer == '--hint' and count > 5 and hint == False:
            print(f'The movie was released in {year}\n')
            hint = True
        
        elif answer == '--exit' or answer == '-e' or answer == '--quit':
            return 'exit'

        elif answer == '-r' or answer == '--retry':
            print('\n')
            return main()

        elif answer in lower_movie:
            while answer in lower_movie:
                index = lower_movie.index(answer)
                question[index] =  moviecp[index]
                lower_movie[index] = 'NULL'

        elif answer == moviename:
            question=moviecp.copy()
            break

        else:
            # if wrong guess increase counter
            count+=1
        
    if count < 11:
        print(*question,'\n')
        return True
    return False


def get_result(result):
    if result:
        return 'Correct!'
    else:
        return 'Incorrect, try again!'


if __name__ == "__main__":
    main()