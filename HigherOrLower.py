import random
from os import system
from game_data import data
import art



def random_item_picker():
    rand_item = random.choice(data)
    return rand_item

def check_user_answer(item_comparison, user_answer):
    if user_answer == 'a':
        user_answer = 0
        if item_comparison[user_answer]['follower_count'] > item_comparison[1]['follower_count']:
            return item_comparison[user_answer]
        else:
            return False
    elif user_answer == 'b':
        user_answer = 1
        if item_comparison[user_answer]['follower_count'] > item_comparison[0]['follower_count']:
            return item_comparison[user_answer]
        else:
            return False

def game():

    game_playing = True
    item_to_compare = []
    previous_items = []
    score = 0

    for i in range(2):
        item_to_compare.append(random_item_picker())

    print(art.logo)

    while game_playing:

        print(f"Compare A: {item_to_compare[0]['name']}, {item_to_compare[0]['description']}, {item_to_compare[0]['country']}.")

        print(art.vs)

        print(f"Against B: {item_to_compare[1]['name']}, {item_to_compare[1]['description']}, {item_to_compare[1]['country']}.")
        user_input = input("Who has more followers? Type 'A' or 'B': ").lower()
        
        item_to_compare[0] = check_user_answer(item_to_compare, user_input)
        temp_item = item_to_compare[1]
        previous_items.append(item_to_compare[1])
        item_to_compare.pop(1)
        item_to_compare.append(random_item_picker())

        while temp_item == item_to_compare[1]:
            item_to_compare.pop(1)
            item_to_compare.append(random_item_picker())

            if item_to_compare[0] == item_to_compare[1]:
                item_to_compare.pop(1)
                item_to_compare.append(random_item_picker())
            
        if item_to_compare[0] == False:
            game_playing = False
            system('cls')
            print(art.logo)
            print(f"Sorry, that\'s wrong. Final score: {score}")
        else:
            system('cls')
            score += 1
            print(art.logo)
            print(f"You\'re right! Current score: {score}")
        
game()

