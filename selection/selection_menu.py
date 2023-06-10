from user_auth import validator as valid

def selection_menu_options():
    while True:
        print("\n****** SELECTION MENU ******")
        print("***(1) SEARCH FOR A JOB***")
        print("***(2) FIND SOMEONE YOU KNOW***")
        print("***(3) LEARN A NEW SKILL***")
        print("***(4) LOG OUT***")
        choice = input("Please select which option you would like to do (e.x. \"1\"): ")
        if choice in ['1', '2', '3', '4']:
            if choice == '1':
                job_search()
            elif choice == '2':
                print("\nUnder construction, check back later.")
            elif choice == '3':
                skill_selection()
            elif choice == '4':
                return
        else:
            print("\nInvalid option. Please try again.")

def job_search():
    print("\n*****Job Search*****")
    job_title = input("Job title: ")
    #Insert functionality here

    end_search = input("\nEnd your search? (Return to previous menu) (y/n): ")
    while not valid.validate_input(end_search):
        print("\nInvalid option. Please try again.")
        end_search = input("\nEnd your search? (Return to previous menu) (y/n): ")

    if end_search.lower() == 'y':
        return
    
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
            print("\nUnder construction, check back later.")
            return 
        elif choice == '6':
            return
        else:
            print("\nInvalid option. Please try again.\n")
