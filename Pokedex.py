import requests

# Define the base API URL
url = "https://pokeapi.co/api/v2/pokemon/"

# Ask the user to input a Pokémon name
pokemon_name = ____________

# Create the full API URL
full_url = __________________

# Make a GET request to the API
response = __________________

# Check if the request was successful
if response.status_code == 200:

    # Parse the JSON response
    data = __________________

    # Access data from the API
    name = data[__________]
    height = data[__________]
    weight = data[__________]

    # Print Pokémon info
    print(__________________________________)

else:
    print("Error: Pokémon not found!")