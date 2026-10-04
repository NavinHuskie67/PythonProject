
import time
import random
def character_creation():
    def take_info():
        player_name = input("Please type your desired name: ")

        def choose_gender():
            gender_num = input("Please type 1 if you are a boy and 2 if you are a girl: ")
            if gender_num == "1":
                p_gender = "boy"
                p_possessive = "his"
            elif gender_num == "2":
                p_gender = "girl"
                p_possessive = "her"
            else:
                print("Not a valid option.")
                return choose_gender()
            return p_gender, p_possessive
            
        player_gender, player_possessive = choose_gender()
            
        #Return data cleanly out of the function
        return player_name, player_gender, player_possessive

    def confirm_info(player_name, player_gender, player_possessive):
        print(f"You are a {player_gender} well on in {player_possessive} teen years, and your name is {player_name}.")
        change = input("Do you wish to change any of your information? (y/n) ")
        return (change.lower() == "y" or change.lower() == "yes")


    #Use a main loop to handle choices cleanly
    user_is_changing_mind = True

    while user_is_changing_mind:
        # Get the info from take_info
        player_name, player_gender, player_possessive = take_info()
        
        # Check if they want to change it. 
        # If they type 'y', the loop runs again. If 'n', the loop stops
        user_is_changing_mind = confirm_info(player_name, player_gender, player_possessive)
    return player_name, player_gender, player_possessive
def intro(name, player_possessive):
    print(f"\nHello, fair {name}.")
    print("It has been many years since the inhabitants of Malibrin had any hope at all.")
    time.sleep(3)
    print("""
Since the Fell escaped their prison in the Third Age of the world, 
they have weaved an intricate web around all of the Western Realm of Loren.""")
    time.sleep(5)
    print("""
Now, in the Ninth Age of this world their plans slowly begin to come into fruition.
Even the clueless child has noted the strange occurrences that are swiftly becoming
not so strange after all.""")
    time.sleep(6.5) 
    print("""
Drake attacks in the mountains surrounding Leskelle, poisoned
well water in several towns, and the disappearence of a group of minors heading north to
the Anobaith islands all seem to say that something is astir.""") 
    time.sleep(7)
    print(f"""
Meanwhile, {name} has made
his way from Evernmore to the city of Malibrin, eager to attend the coming festival of
fall, and perhaps even test {player_possessive} mettle at some of the competitions.
""")
def player_creation(name, gender, possessive):
    player = {
        "name" : name,
        "gender" : gender,
        "possessive" : possessive,
        "level" : 1,
        "max_health" : 50,
        "health" : 50,
        "damage" : 10,
        "experience" : 0

    }
    return player
def print_player_status(player_stats):
    
    print("\n" + "=" * 30)
    print(f"       PLAYER STATUS ")
    print("=" * 30)
    print(f"Name:       {player_stats['name'].title()}")
    print(f"Gender:     {player_stats['gender'].capitalize()}")
    print(f"Level:      {player_stats['level']}")
    print(f"HP:         {player_stats['health']}/{player_stats['max_health']}")
    print(f"Attack:     {player_stats['damage']}" + " damage")
    print(f"EXP:        {player_stats['experience']}")
    print("=" * 30 + "\n")
def create_enemy():
    enemy = {
        "name" : "Nordic Warrior",
        "health" : 30,
        "damage" : 10
    }
    return enemy
def road_encounter(name, possessive, enemy):
    print(f"""
As {name} drags {possessive} weary feet on the path, 
suddenly a rustle in the undergrowth catches {possessive} attention.
One {enemy["name"]} springs from the shadows, weapon drawn, bearing
down upon the startled {name}.""")
    time.sleep(6)
    print(f"""
Name: {enemy["name"]}
Health: {enemy["health"]}
""")
def attack_enemy(player, enemy, question):
    total_damage = player["damage"] + question["bonus_damage"]
    enemy["health"] -= total_damage
    #Ensure enemy health does not go below 0
    if enemy["health"] < 0:
        enemy["health"] = 0 

    print(f"{player['name']} dealt {total_damage} to the {enemy['name']}. \n{enemy['name']}'s Health: {enemy['health']} health.")
def enemy_attack(player, enemy):
    player["health"] -= enemy["damage"]
    if player["health"] < 0:
        player["health"] = 0
    print(f"The {enemy['name']} dealt {enemy["damage"]} to {player["name"]}. \n{player['name']}'s Health: {player['health']} health.")
def questions():
    question =[ 
        {
        "question" : "What is 9 * 13?",
        "answer" : "117",
        "time" : 5,
        "bonus_damage" : 0
        },
        {
        "question" : "What is the sum of the solutions to the quadratic equation x^2 - 5x + 6 = 0?",
        "answer" : "5",
        "time" : 20,
        "bonus_damage" : 5
        },
        {
        "question" : "During which phase of mitosis do sister chromatids separate and move toward \nopposite poles of the cell? (type a, b, c, or d): \n(a) - Prophase \n(b) - Metaphase \n(c) - Anaphase \n(d) - Telephase",
        "answer" : "c",
        "time" : 10,
        "bonus_damage" : 10
        },
        {
        "question" : "Which subatomic particle has a negative electrical charge and a mass that \nis approximately 1/1836 the mass of a proton? (type a, b, c, or d): \n(a) - Neutron \n(b) - Positron \n(c) - electron \n(d) - Elentron",
        "answer" : "c",
        "time" : 7,
        "bonus_damage" : 0
        }

    ]
    return question
def create_hard_question():
    hard_question = {
        "question" : "What is x if 9x - 3 = 69?",
        "answer" : "8",
        "time" : 10,
        "bonus_damage" : 5
    }
    return hard_question
def ask_question(question, player, enemy):
    print(question["question"])
    print(f"You have {question['time']} seconds to answer.")
    answer = input("Your answer: ")
    if question["answer"] == answer:
        print("\nCorrect!\n")
        attack_enemy(player, enemy, question)
    else:
        print("\nIncorrect!(haha loser)\n")
        enemy_attack(player, enemy)
def choose_question(question_bank): 
    question = random.choice(question_bank)
    return question
def combat(player, enemy, question_bank):
    while enemy["health"] > 0:
        question = choose_question(question_bank)
        ask_question
def main():
    print("Hello, my dear friend, and welcome to the world of Loren.")
    name, gender, possessive = character_creation()
    print("\nCharacter creation complete! Welcome to the adventure!")
    player = player_creation(name, gender, possessive)
    print_player_status(player)
    time.sleep(6)
    intro(name, possessive)
    time.sleep(6)
    enemy = create_enemy()
    road_encounter(name, possessive, enemy)
    question = choose_question(questions)
    ask_question(question, player, enemy)



main()