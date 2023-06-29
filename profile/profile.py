
def edit_profile(user):
    print(user)
    while True:
        print("*** (1) TITLE ***")
        print("*** (2) MAJOR ***")
        print("*** (3) UNIVERSITY NAME ***")
        print("*** (4) ABOUT ***")
        print("*** (5) JOB EXPERIENCE ***")
        print("*** (6) EDUCATION EXPERIENCE ***")
        print("*** (7) VIEW PROFILE ***")

        choice = input("Select which part of your profile you would like to edit or view (e.g. \"1\"): ")
        if choice in ['1', '2', '3', '4', '5', '6', '7']:
            if choice == '1':
                edit_title(user)
            elif choice == '2':
                edit_major(user)
            elif choice == '3':
                edit_university(user)
            elif choice == '4':
                edit_about(user)
            elif choice == '5':
                edit_job(user)
            elif choice == '6':
                edit_education(user)
            elif choice == '7':
                view_profile(user)
            else:
                print("\nInvalid option, please try again.\n")
        else:
            print("\n Invalid option, try again.\n")

def edit_title(user):
    
def edit_major(user):
    
def edit_university(user):
    
def edit_about(user):
    
def edit_job(user):
    
def edit_education(user):
    
def view_profile(user):
