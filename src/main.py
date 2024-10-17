import time
import random
from controller import fectch_pokemon_data, add_pokemon_to_db

def main():
    while True:
        pokemon_id = random.randint(1, 350)
        pokemon_schema = fectch_pokemon_data(pokemon_id)
        if pokemon_schema:
            print(f'Pokemon {pokemon_schema.name} added to database')
            add_pokemon_to_db(pokemon_schema)

        else:
            print(f'Pokemon {pokemon_id} not found')
        time.sleep(10)

if __name__ == '__main__': 
    main()