#PokeAPI endpoint: https://pokeapi.co/api/v2/pokemon/{pokemon_name}

import requests  # Import the library used to make requests

# Define the base API URL
url = "https://pokeapi.co/api/v2/pokemon/"

# Ask the user to input a Pokémon name
pokemon_name = ________________

# create a variable that stores a url for the pokemone name input according to the PokeAPI endpoint

# Make a GET request to the API
response = _____________

# Check if the request was successful (status code 200)

    # Parse the JSON response
    data = ______
    # Access data from the API and store it into 3 variables
    name = data[_____]  # The Pokémon's name
    height = data[_____]  # The Pokémon's height
    weight = data[_____]  # The Pokémon's weight

    # create a print statement that displays the information gathered about the pokemon

# if the request was not successful, print an error statement

#CONGRATS! You have made your own pokedex!
