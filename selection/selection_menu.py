from user_auth import validator as valid
from util import util as util

def selection_menu_options(user): #User is an array of username, firstname, lastname
    while True:
        print("\n****** SELECTION MENU ******")
        print("***(1) SEARCH FOR A JOB***")
        print("***(2) FIND SOMEONE YOU KNOW***")
        print("***(3) LEARN A NEW SKILL***")
        print("***(4) LOG OUT***")
        choice = input("Please select which option you would like to do (e.x. \"1\"): ")
        if choice in ['1', '2', '3', '4']:
            if choice == '1':
                job_search(user)
            elif choice == '2':
                print("\nUnder construction, check back later....")
            elif choice == '3':
                skill_selection()
            elif choice == '4':
                return
        else:
            print("\nInvalid option. Please try again.")

def job_search(user): #User is an array of username, firstname, lastname
    jobs = []
    util.file_job_read(jobs)

    while True:
        print("\n****** JOB SEARCH ******")
        print("***(1) FIND JOB***")
        print("***(2) CREATE JOB***")
        print("***(3) RETURN TO SELECTION MENU***")
        job_selection = input("Please select what option would would like to go to (press 1-2): ")
        if job_selection in ['1','2', '3']:
            
            #Search for a Job
            if job_selection == '1':
              print("\nUnder construction, check back later...")
              continue
                
            #Create Job
            elif job_selection == '2':
                if(len(jobs) < 5):
                    title = input("Enter the Job Title: ")
                    description = input("Enter the Job Description: ")
                    employer = input("Enter the Job Employer: ")
                    location = input("Enter the Job Location: ")
                    salary = input("Enter the Job Salary: ")
                    job = {"title" : title, "description" : description, "employer" : employer, "location" : location, "salary" : salary, "first_name" : user[0], "last_name" : user[1]}
                    jobs.append(job)
                    util.file_job_save(jobs)
                else:
                    print("All permitted jobs have been created, please come back later")

            elif job_selection == '3':
                return
                
        else:
            print("\nInvalid option. Please try again.\n")
            continue

        end_search = input("\nEnd your search? (Return to previous menu) (y/n): ")
        while not valid.validate_input_yn(end_search):
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
            print("\nUnder construction, check back later...")
            return 
        elif choice == '6':
            return
        else:
            print("\nInvalid option. Please try again.\n")
