'''
    TASK 38, COMPULSORY TASK 2: watch_next.py
    AUTHORED BY MO EL-JARAD
    
    This file can be accessed at my GitHub:
    https://github.com/meljarad/HyperionDevSEBootcamp/tree/main/T38
'''

import spacy # Used for NLP capabilities
from tabulate import tabulate # For printing results in user readable format

def import_movies_list():
    '''
    This function returns a list of movies and their descriptions by reading them in from the text file 'movies.txt'.

    Args:
        (None)
    '''
    # Read in the text content from the movies.txt file
    with open('movies.txt', 'r') as file:
        # Uses list comprehension to remove the line breaks from each line
        movies_as_list = [line.strip() for line in file]

    # Converts the list of movies to a list of dicts with the movie name and description stores as values
    movies_as_dicts = []
    for movie in movies_as_list:
        movies_as_dicts.append({'Name': movie.split(":")[0], 'Description': movie.split(":")[1]})

    return movies_as_list, movies_as_dicts

def recommend_movie(last_watched_movie_description, movies_as_dicts):
    '''
    This function returns recommendation scores for a list of movies based on the description of the last watched movie.

    Args:
        last_watched_movie_description (string):    a string description of the last watched movie.
        movies_as_dicts (list):                     a list of dictionaries where each dictionary represents a movie with
                                                    the names and descriptions included as keys.
    '''

    # Reads in the description of Planet Hulk and finds the similarity scores with the other movies
    # Declares data and header lists for the Tabulate table
    headers = ["Movie:", "Similarity:"]
    similarity_data = []
    similarity_dict_list = []
    watched_movie_desc_token = nlp(last_watched_movie_description)
    movie_descriptions_list = [list(movie_dict.values())[0] for movie_dict in movies_as_dicts]

    # Loops through the list of movies and calculates their similarity score based on the description
    for movie in movies_as_dicts:
        movie_similarity_score = round(nlp(movie['Description']).similarity(watched_movie_desc_token)*100,0)
        similarity_data.append([movie['Name'], str(movie_similarity_score) + '%'])
        similarity_dict_list.append({'Name': movie['Name'], 'Similarity': movie_similarity_score})

    # Prints results in user readable table
    print(tabulate(similarity_data, headers=headers, tablefmt="simple_outline"))

    # Extracts movie which is most similar based on description
    max_similarity_score = 0
    recommended_movie_name = ""
    for movie in similarity_dict_list:
        if movie['Similarity'] > max_similarity_score:
            max_similarity_score = movie['Similarity']
            recommended_movie_name = movie['Name']
    return recommended_movie_name, max_similarity_score

# Loads the medium-sized English language model used for NLP capabilities
nlp = spacy.load('en_core_web_md')

watched_movie = {'Name': 'Planet Hulk',
                 'Description': 'Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator.'
                 }

# Import the list of movies
movies_as_list = import_movies_list()[0]
movies_as_dicts = import_movies_list()[1]

recommendation_stats = recommend_movie(watched_movie['Description'], movies_as_dicts)
recommended_movie_name = recommendation_stats[0]
max_similarity_score = recommendation_stats[1]

# Print recommendation to the user
print(f"Based on your last watched movie {watched_movie['Name']}:\nOur algorithm recommends you watch {recommended_movie_name}next, with a recommendation score of {max_similarity_score:.0f}%!")
