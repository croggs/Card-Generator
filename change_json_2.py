import json
'''removes unecessary keys from our json files'''
def remove_unnecessary():
    # Load the json file
    with open('Data/card_db.json', 'r') as f:
        data = json.load(f)

    fields_to_remove = ['card_prices', 'card_sets','card_images','id','name','type','frameType','desc']

    filtered_data = [{k:v for k,v in d.items() if k not in fields_to_remove} for d in data['data'] if d['type'] == "Normal Monster"]
    # Save the modified json data
    with open('file.json', 'w') as f:
        json.dump(filtered_data, f)


        
#changes all values to mapped numbers to assure be able to create a neural network
def prepare_for_NN():
    with open('file.json', 'r') as f:
        data = json.load(f)

        race_mapping = {"Aqua": 1, "Beast": 2, "Beast-Warrior": 3, "Cyberse": 4, "Dinosaur": 5, "Divine-Beast": 6, "Dragon": 7, "Fairy": 8, "Fiend": 9, "Fish": 10, "Insect": 11, "Machine": 12, "Plant": 13, "Psychic": 14, "Pyro": 15, "Reptile": 16, "Rock": 17, "Sea Serpent": 18, "Spellcaster": 19, "Thunder": 20, "Warrior": 21, "Winged Beast": 22, "Wyrm": 23, "Zombie": 24}
        attribute_mapping = {"DARK": 1, "LIGHT": 2, "FIRE": 3, "WIND": 4, "WATER": 5, "EARTH": 6, "DIVINE": 7}
        for d in data:
            d["race"] = race_mapping[d["race"]]
            d["attribute"] = attribute_mapping[d["attribute"]]
        with open('output.json', 'w') as f:
            json.dump(data, f)
remove_unnecessary()
prepare_for_NN()