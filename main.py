import requests
import json

token = 'b120e756e58cd2ec18d7d33125ba336d'
response = requests.post('https://pokemonbattle.me:5000/pokemons', headers={'trainer_token':token}, json ={
    "name": "Крутыш",
    "photo": "https://static.wikia.nocookie.net/pokemon/images/2/21/001Bulbasaur.png"

})
print(response.text)

response_put = requests.put('https://pokemonbattle.me:5000/pokemons', headers={'trainer_token':token}, json ={
    
    "pokemon_id": 1319,
    "name": "Крутышка",
    "photo": "https://pngimg.com/uploads/pokemon/pokemon_PNG3.png"

})
print(response_put.text)

response_post = requests.post('https://pokemonbattle.me:5000/trainers/addPokebol', headers={'trainer_token':token}, json ={
    "pokemon_id": "1319"
})
print(response_post.text)