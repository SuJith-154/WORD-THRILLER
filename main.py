print("Welcome to the Abandoned Mansion!")
print("You are a detective investigating a series of strange disappearances.")
print("The mansion is rumored to have a hidden lab. You walk in the front door.")
print("You hear a faint noise coming from upstairs and notice a draft from a slightly ajar door to the basement.")
print("Do you want to investigate the noise upstairs or explore the basement?")
choice = input("Enter a choice (Basement / Upstairs): ").strip().lower()

if choice == 'upstairs':
    print("As you ascend the creaky staircase, you notice a light under a door at the end of the hallway.")
    print("Do you want to quietly approach the door or look for another way into the room?")
    choice = input("Enter a choice (Door / Look other way): ").strip().lower()

    if choice == 'door':
        print("As you approach the door, you overhear voices discussing an experiment.")
        print("You carefully open the door and find a hidden lab filled with strange equipment and notes.")
        print("Do you want to inspect the PC or read through the notes?")
        choice = input("Enter a choice (Notes / PC): ").strip().lower()

        if choice == 'notes':
            print("The Mansion owner is a Scientist and he is planning to spread a new virus.")
        elif choice == 'pc':
            print(
                "By looking into the PC, \n"
                "you find that the terrorist living in the mansion is planning to respread the coronavirus.")
        else:
            print("Error: Invalid choice.")

    elif choice == 'look other way':
        print("You discover a vent leading into the lab.")
        print("You crawl through the vent and find yourself in a corner of the lab unnoticed.")
        print("Do you want to listen in on the conversation or search the lab for evidence?")
        choice = input("Enter a choice (Listen / Search): ").strip().lower()

        if choice == 'listen':
            print(
                "By listening to the conversation, \n"
                "you learn that the terrorist living in the mansion is planning to respread the coronavirus.")
        elif choice == 'search':
            print(
                "While searching the laboratory, \n"
                "you discover that the Mansion owner is a Scientist and he is planning to spread a new virus.")
        else:
            print("Error: Invalid choice.")

    else:
        print("Error: Invalid choice.")

elif choice == 'basement':
    print("You descend into a dark and musty cellar.")
    print("You find a series of old crates and a locked door.")
    print("Do you want to search the crates for clues or try to pick the lock on the door?")
    choice = input("Enter a choice (Crates / Door): ").strip().lower()

    if choice == 'crates':
        print("You find a hidden drawer containing a key and a map.")
        print("The map shows a hidden passage behind a bookcase in the study.")
        print("Do you want to head to the study or continue searching the cellar?")
        choice = input("Enter a choice (Study / Cellar): ").strip().lower()

        if choice == 'study':
            print("You head to the study and uncover a diary revealing the mansion's dark history.")
            print("Suddenly, the walls start to close in, and you must quickly escape before you're trapped forever.")
        elif choice == 'cellar':
            print("The mansion owner is revealed to be conducting unethical experiments in the hidden lab.")
            print("He is the reason for the recent disappearances in the village.")
        else:
            print("Error: Invalid choice.")

    elif choice == 'door':
        print("You pick the lock on the door and uncover a hidden room with a strange laboratory setup.")
        print("Do you want to inspect the lab equipment or read through the notes scattered on the table?")
        choice = input("Enter a choice (Lab / Notes): ").strip().lower()

        if choice == 'lab':
            print(
                "You discover a device that, when activated,\n"
                " triggers a mechanism revealing a hidden room where an abducted person,\n"
                " missing for weeks, is being held captive.")
        elif choice == 'notes':
            print(
                "The notes outline the owner’s unethical experiments with advanced technology,\n"
                " revealing the horrific methods used to manipulate and control human subjects.")
        else:
            print("Error: Invalid choice.")

    else:
        print("Error: Invalid choice.")

else:
    print("Error: Invalid choice.")
