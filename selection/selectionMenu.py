def selection_menu_options():
    while True:
        print("\n****** SELECTION MENU ******")
        print("***(1) SEARCH FOR A JOB***")
        print("***(2) FIND SOMEONE YOU KNOW***")
        print("***(3) LEARN A NEW SKILL***")
        choice = input("Please select which option you would like to do (press 1, 2, or 3): ")
        if choice in ['1', '2', '3']:
            if choice == '1' or choice == '2':
                print("Under construction, check back later.")
                break
            elif choice == '3':
                result = skill_selection()
                if result == 'exit':
                    break
                elif result == 'main':
                    continue
        else:
            print("Invalid choice, please try again.")

def skill_selection():
    print("\n****** SKILL SELECTION ******")
    print("***(1) TIME MANAGEMENT SKILLS***")
    print("***(2) CODING LANGUAGE SKILLS***")
    print("***(3) PUBLIC SPEAKING SKILLS***")
    print("***(4) PERSONAL FINANCE MANAGEMENT SKILLS***")
    print("***(5) COLLABORATION SKILLS***")
    print("*(6) RETURN TO PREVIOUS SCREEN*")
    while True:
        choice = input("Please select which skill you would like to develop/work on (press 1-5): ") 
        if choice in ['1', '2', '3', '4', '5']:
            print("Under construction, check back later.")
            return 'exit'
        elif choice == '6':
            return 'main'
        else:
            print("Invalid choice, please try again.\n")