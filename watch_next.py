import spacy

def find_similar_movie(input_description):
    # Load the spaCy model
    nlp = spacy.load('en_core_web_md')

    # Read the movie descriptions from the file
    with open('movies.txt', 'r') as file:
        movie_descriptions = file.readlines()

    # Preprocess and tokenize the descriptions
    movie_descriptions = [desc.lower() for desc in movie_descriptions]
    movie_descriptions = [nlp(desc) for desc in movie_descriptions]

    # Tokenize and preprocess the input description
    input_description = input_description.lower()
    input_description = nlp(input_description)

    # Compute similarity scores between the input description and all other descriptions
    similarities = [input_description.similarity(desc) for desc in movie_descriptions]

    # Find the index of the most similar movie
    most_similar_index = similarities.index(max(similarities))

    # Return the title of the most similar movie
    with open('movies.txt', 'r') as file:
        movies = file.readlines()
        return movies[most_similar_index].strip()

# Example usage:
input_description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."
similar_movie = find_similar_movie(input_description)
print("\n",similar_movie,"\n")
