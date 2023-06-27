import main as main
from user_auth import validator as valid
from util import util as util


def selection_menu_options(user, friend_list, request_list, users): # user is an array of username, firstname, lastname, language\
    print(user)
    while True:

        if len(request_list) > 0:
            print("*** YOU HAVE NEW FRIEND REQUEST(S) ***")

        print("\n****** SELECTION MENU ******")
        print("***(1) SEARCH FOR A JOB***")
        print("***(2) FIND SOMEONE YOU KNOW***")
        print("***(3) LEARN A NEW SKILL***")
        print("***(4) USEFUL LINKS***")
        print("***(5) IMPORTANT LINKS***")
        print("***(6) SHOW MY NETWORK***")
        print("***(7) LOG OUT***")
        
        choice = input("Please select which option you would like to do (e.x. \"1\"): ")
        if choice in ['1', '2', '3', '4', '5', '6', '7']:
            if choice == '1':
                job_search(user)
            elif choice == '2':
                find_friend(users, user)
            elif choice == '3':
                skill_selection()
            elif choice == '4':
                useful_links("logged_in")
            elif choice == '5':
                important_links("logged_in", user)
            elif choice == '6':
                show_network(friend_list, user, users, request_list)
            elif choice == '7':
                return
        else:
            print("\nInvalid option. Please try again.")

def find_friend(users, current_user):
    while True:
        found = 0
        print("\nSearch for other students:")
        search_option = input(
            "Search by (l)ast name, (u)niversity, (m)ajor or (r)eturn: "
        ).lower()
        matching_users = []
        if search_option == "l":
            type = input("Please type the last name: ")
            for user in users:
                if users[user][2] == type:
                    matching_users.append(user)
                    found = 1
        elif search_option == "u":
            type = input("Please type the university: ")
            for user in users:
                if users[user][7] == type and user != current_user[0] :
                    matching_users.append(user)
                    found = 1
        elif search_option == "m":
            type = input("Please type the university: ")
            for user in users:
                if users[user][8] == type and user != current_user[0]:
                    matching_users.append(user)
                    found = 1
        elif search_option == "r":
            return
        else:
            print("\nInvalid option. Please try again.")
            continue

        if found == 0:
            print("Cannot find this person, please try again")
        elif found == 1:
            if current_user[0] in matching_users:
                matching_users.remove(current_user[0])
            while True:
                print("\nHere are the results:\n")
                for friend in matching_users:
                    print(f"{friend}")
                print("\n***(1) ADD FRIEND ***")
                print("***(2) RETURN ***")
                choice = input("Please select which option you would like to do: ")

                if choice == '1':
                    add_friend = input("Please type the username of the person you want to add: ")
                    add = 0
                    with open("data/request.csv", "r") as file:
                        lines = file.readlines()      
                    with open("data/request.csv", "w") as file:
                        for line in lines:
                            data = line.strip().split(',')
                            if data[0] == add_friend:
                                add = 1
                                username = data[0]
                                # Additional data (if available)
                                additional_data = data[1:]
                                additional_data.append(current_user[0])
                                line = ','.join([username] + additional_data) + '\n'
                            file.write(line)
                        if add == 1:
                            print("Already sent the friend request")
                        else:
                            print("Please check if you type correctly or not")  
                elif choice == '2':
                    break       
def show_network(friend_list, user, users, request_list):
    while True:
        print("*** This is your friend list ***")
        if (len(friend_list) == 0):
            print("None")
        else:
            for friend in friend_list:
                print(f'{friend}')
        print("\n***(1) REMOVING FRIEND ***")
        print("***(2) PENDING REQUEST ***")
        print("***(3) RETURN ***")

        choice = input("Please select which option you would like to do: ")
        

        if choice == '1':
            removal_friend = input("Please type the username of the person you want to remove: ")
            with open("data/database.csv", "r") as file:
                lines = file.readlines()
            isnt_friend = 0
        
                    
            with open("data/database.csv", "w") as file:
                for line in lines:
                    data = line.strip().split(',')
                    if data[0] == user[0]:
                        username = data[0]
                        passwd = data[1]
                        f_name = data[2]
                        l_name = data[3]
                        current_language = data[4]
                        email_bool = data[5]
                        sms_bool = data[6]
                        targeted_ads_bool = data[7]
                        university = data[8]
                        major = data[9]
                                        
                        # Additional data (if available)
                        additional_data = data[10:]
                        if removal_friend in additional_data:
                            additional_data.remove(removal_friend)
                            if removal_friend in friend_list:
                                friend_list.remove(removal_friend)
                            else:
                                print("error")
                        else:
                            isnt_friend = 1
                        line = ','.join([username, passwd, f_name, l_name, current_language, email_bool, sms_bool, targeted_ads_bool, university, major] + additional_data) + '\n'
                                
                                
                                
                    if data[0] == removal_friend:
                        username = data[0]
                        passwd = data[1]
                        f_name = data[2]
                        l_name = data[3]
                        current_language = data[4]
                        email_bool = data[5]
                        sms_bool = data[6]
                        targeted_ads_bool = data[7]
                        university = data[8]
                        major = data[9]
                                    
                        # Additional data (if available)
                        additional_data = data[10:]
                        if user[0] in additional_data:
                            additional_data.remove(user[0])
                        line = ','.join([username, passwd, f_name, l_name, current_language, email_bool, sms_bool, targeted_ads_bool, university, major] + additional_data) + '\n'
                    file.write(line)  
                if isnt_friend == 1:
                    print("\nThis friend is not in the list, please try again\n")
                else:
                    print("\nWe have successfully removed the user, please select what you want to do next\n")
        elif choice == '2':
            while True:
                print("*** This is your friend pending list ***")
                if (len(request_list) == 0):
                    print("None")
                else:
                    for pending in request_list:

                        print(f'{pending}')
                print("\n***(1) ACCEPTING FRIEND REQUEST ***")
                print("***(2) REJECTING FRIEND REQUEST ***")
                print("***(3) RETURN ***")
                user_input = input("Please select which option you would like to do: ")
                if user_input == '1' and len(request_list) != 0:
                    accepting_person = input("Please type the username of the person you'd like to add: ")
                    with open("data/database.csv", "r") as file:
                        lines = file.readlines()
                    typo = 0
                    with open("data/database.csv", "w") as file:
                        for line in lines:
                            data = line.strip().split(',')
                            if data[0] == user[0]:
                                username = data[0]
                                passwd = data[1]
                                f_name = data[2]
                                l_name = data[3]
                                current_language = data[4]
                                email_bool = data[5]
                                sms_bool = data[6]
                                targeted_ads_bool = data[7]
                                university = data[8]
                                major = data[9]
                                                
                                # Additional data (if available)
                                additional_data = data[10:]
                                if accepting_person in request_list:
                                    additional_data.append(accepting_person)
                                    
                                    request_list.remove(accepting_person)
                                else:
                                    typo = 1
                                line = ','.join([username, passwd, f_name, l_name, current_language, email_bool, sms_bool, targeted_ads_bool, university, major] + additional_data) + '\n'
                                                   
                                       
                            if data[0] == accepting_person:
                                username = data[0]
                                passwd = data[1]
                                f_name = data[2]
                                l_name = data[3]
                                current_language = data[4]
                                email_bool = data[5]
                                sms_bool = data[6]
                                targeted_ads_bool = data[7]
                                university = data[8]
                                major = data[9]
                                                    
                                # Additional data (if available)
                                additional_data = data[10:]
                                if accepting_person not in additional_data:
                                    additional_data.append(user[0])
                                line = ','.join([username, passwd, f_name, l_name, current_language, email_bool, sms_bool, targeted_ads_bool, university, major] + additional_data) + '\n'
                                    
                            file.write(line)  
                        if typo == '1':
                            print("Maybe there's a typo, can you try again")
                        else:
                            print("You have successfully add this friend")
                            with open("data/request.csv", "r") as file:
                                lines = file.readlines()
                            with open("data/request.csv", "w") as file:
                                for line in lines:
                                    data = line.strip().split(',')
                                    if data[0] == user[0]:
                                        username = data[0]
                                        additional_data = data[1:]
                                        if accepting_person in additional_data:
                                            additional_data.remove(accepting_person)
                                        line = ','.join([username] + additional_data) + '\n'
                                    file.write(line)
                elif user_input == '2' and len(request_list) != 0: 
                    removing_person = input("Please type the username of the person you'd like to remove: ")
                    typo = 0
                    with open("data/request.csv", "r") as file:
                        lines = file.readlines()
                    with open("data/request.csv", "w") as file:
                        for line in lines:
                            data = line.strip().split(',')
                            if data[0] == user[0]:
                                username = data[0]
                                additional_data = data[1:]
                                if removing_person in additional_data:
                                    additional_data.remove(removing_person)
                                    if removing_person in request_list:
                                        request_list.remove(removing_person)
                                else:
                                    typo = 1
                                line = ','.join([username] + additional_data) + '\n'
                            file.write(line)
                    if typo == 1:
                       print("There may be a typo, can you try again")
                    elif typo == 0:
                        print("You have successfully removes this pending friend request")
                elif user_input == '1' or user_input == '2' and  len(request_list) == 0:
                    print("You don't have any pending friend request")       
                elif user_input == '3':
                    return     
        elif choice == '3':
            return
        else:
            print("\nPlease try again\n")
        
    
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
                    job = {"title" : title, "description" : description, "employer" : employer, "location" : location, "salary" : salary, "first_name" : user[1], "last_name" : user[2]}
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

def useful_links(state):
    while True:
        print("\n****** USEFUL LINKS ******")
        print("***(1) GENERAL***")
        print("***(2) BROWSE INCOLLEGE***")
        print("***(3) BUSINESS SOLUTIONS***")
        print("***(4) DIRECTORIES***")
        print("***(5) RETURN***")

        choice = input("Please select one of these useful links (press 1-4): ") # go to the section based on user's choice
        if choice == '1':
            current = general(state)
            if current == "logging_in" or "registering":
                return current
            else:
                pass
        elif choice in ['2','3','4']:
            print("\nUnder construction, check back later ...")
        elif choice == '5':
            return "menu"
        else:
            print("\nInvalid option. Please try again.\n")
            
def important_links(state, user=''):
    if state == "not_logged_in":
        language = "English"
    else:
        language = user[3]
    while True:
        print("\n****** IMPORTANT LINKS ******")
        print("***(1) COPYRIGHT NOTICE ***")
        print("***(2) ABOUT ***")
        print("***(3) ACCESSIBILITY ***")
        print("***(4) USER AGREEMENT ***")
        print("***(5) PRIVACY POLICY ***")
        print("***(6) COOKIE POLICY ***")
        print("***(7) COPYRIGHT POLICY ***")
        print("***(8) BRAND POLICY ***")
        print("***(9) LANGUAGES ***")
        print("***(10) RETURN ***")

        choice = input("Please select one of these useful links (press 1-10): ") #go to the section based on user's choice

        # Copyright Notice
        if choice == '1':
            print("\n****** COPYRIGHT NOTICE ******")
            print(""" 
© 2023 InCollege. All rights reserved.
The content, design, and functionality of this website/application, including but not limited to text, graphics, logos, icons, images, audio, video, and software,
are the property of InCollege or its licensors and are protected by international copyright laws.
The compilation (meaning the collection, arrangement, and assembly) of all content on this site/application is the exclusive property of InCollege and is protected by international copyright laws.
Any unauthorized use, reproduction, modification, distribution, transmission, republication, display, or performance of the content on this site/application is strictly prohibited.
InCollege, the InCollege logo, and all related product and service names, designs, and slogans are trademarks of InCollege or its affiliates or licensors.
You are not authorized to use any such trademarks without the prior written permission of InCollege.
All other trademarks not owned by InCollege or its affiliates that appear on this site/application are the property of their respective owners, who may or may not be affiliated with, connected to, or sponsored by InCollege.
By using this site/application, you acknowledge and agree that the content and materials available on this site/application are protected by
copyrights, trademarks, service marks, patents, trade secrets, or other proprietary rights and laws.
Except as expressly authorized by InCollege, you agree not to sell, license, rent, modify, distribute, copy, reproduce, transmit,
publicly display, publicly perform, publish, adapt, edit, or create derivative works from such materials or content.
InCollege enforces its intellectual property rights to the fullest extent permitted by law.
If you believe that any content on this site/application infringes upon your intellectual property rights, please contact us immediately.
For inquiries regarding permissions or usage of copyrighted material belonging to InCollege, please contact us at <inCollege Email>
By accessing or using this site/application, you agree to comply with all applicable laws and regulations regarding copyright and trademark ownership.
Last updated: 6/19/2023
""")

        #About
        elif choice == '2':
            print("\n****** ABOUT ******")
            print("\nIn College: Welcome to In College, the world's largest college student network with many users in many countries and territories worldwide."
                  "Our purpose is to connect college students to provide greater opportunity for their educational and professional success.")

        #Accessibility
        elif choice == '3':
            print("\n****** ACCESSIBILITY ******")
            print("""
At InCollege, we are committed to ensuring that our website and services are accessible to all individuals, including those with disabilities.
We strive to meet or exceed the requirements of applicable accessibility laws and guidelines to provide an inclusive and user-friendly experience for all users.
This Accessibility Statement outlines our efforts to make InCollege accessible and highlights the accessibility features we have implemented.

1. Web Content Accessibility Guidelines (WCAG) Compliance
We aim to adhere to the Web Content Accessibility Guidelines (WCAG) 2.1 Level AA standards to ensure that our website and services are perceivable,
operable, understandable, and robust. We have implemented various accessibility features and continue to enhance our platform to improve accessibility.

2. Accessibility Assistance
If you encounter any accessibility barriers or have specific accessibility needs while using InCollege, please contact us.
We are committed to providing reasonable accommodations and will work with you to ensure you can access and enjoy our website and services effectively.

3. Contact Us
If you have any questions, concerns, or suggestions regarding the accessibility of InCollege, or if you would like to report any accessibility issues, please reach out
to us at <inCollege Email We value your feedback and are committed to making our platform as accessible as possible.
Last updated: 6/19/2023""")

        #User Agreement
        elif choice == '4':
            print("\n****** USER AGREEMENT ******")
            print("""
Please read this User Agreement ("Agreement") carefully before using InCollege ("we" or "us").
This Agreement sets forth the terms and conditions that govern your access to and use of our website, mobile application, and any related services (collectively, the "Services").
By accessing or using the Services, you agree to be bound by this Agreement. If you do not agree to all the terms and conditions of this Agreement, you may not use the Services.

1. Eligibility
By using the Services, you represent and warrant that you are at least 13 years old and have the legal capacity to enter into this Agreement.
If you are accessing or using the Services on behalf of a company or other legal entity, you represent and warrant that you have the authority to bind that entity to this Agreement.

2. Use of Services
2.1 License: Subject to your compliance with this Agreement, we grant you a limited, non-exclusive, non-transferable, and revocable license to access and use the Services for personal, non-commercial purposes.
2.2 Prohibited Conduct: You agree not to engage in any conduct that violates this Agreement, including but not limited to:
    a. Using the Services for any illegal, unauthorized, or unethical purpose;
    b. Impersonating any person or entity or falsely stating or otherwise misrepresenting your affiliation with a person or entity;
    c. Interfering with or disrupting the operation of the Services or the servers or networks connected to the Services;
    d. Uploading, transmitting, or distributing any viruses, malware, or other harmful or destructive content;
    e. Collecting or storing personal information about other users without their consent;
    f. Violating any applicable laws, regulations, or third-party rights.

3. Intellectual Property
The Services and all related intellectual property rights are the exclusive property of InCollege and its licensors.
You acknowledge that the Services contain proprietary and confidential information protected by copyright, trademark, and other laws.
You agree not to modify, reproduce, distribute, create derivative works, or sell any part of the Services without our prior written consent.

4. Privacy
We collect, use, and disclose your personal information in accordance with our Privacy Policy.
By using the Services, you consent to our collection, use, and disclosure of your information as described in the Privacy Policy.

5. Limitation of Liability
To the fullest extent permitted by law, InCollege and its affiliates, directors, officers, employees, and agents shall not be liable
for any indirect, incidental, special, consequential, or punitive damages arising out of or in connection with your use of the Services.

6. Termination
We may terminate or suspend your access to the Services at any time, with or without cause, and without prior notice or liability.
Upon termination, all rights and licenses granted to you under this Agreement will immediately cease.

7. Governing Law and Dispute Resolution
This Agreement shall be governed by and construed in accordance with the laws of [Jurisdiction].
Any disputes arising out of or relating to this Agreement shall be resolved exclusively through arbitration in accordance with the rules of [Arbitration Institution].

8. Changes to this Agreement
We reserve the right to modify or update this Agreement at any time. Any changes will be effective immediately upon posting of the updated Agreement.
By continuing to use the Services after the posting of any changes, you accept and agree to be bound by the modified Agreement.

9. Contact Us
If you have any questions, comments, or concerns regarding this Agreement, please contact us at <inCollege Email>
Last updated: 6/19/2023
""")
        #Privacy Policy
        elif choice == '5':
            print("\n****** PRIVACY POLICY ******")
            print("""
Privacy Policy
Effective Date: 6/19/2023
Thank you for using InCollege ("we" or "us"). This Privacy Policy describes how we collect, use, and disclose your personal information
when you access or use our website, mobile application, or any related services(collectively, the "Services").

1. Information We Collect
1.1 Information You Provide to Us: We may collect personal information that you voluntarily provide to us when you use our Services,
such as your name, email address, phone number, profile information, and any other information you choose to provide.
1.2 Information We Collect Automatically: When you access or use our Services, we may automatically collect certain information about your device, browsing actions, and patterns.
This information may include your IP address, browser type, operating system, referring/exit pages, and clickstream data.
1.3 Cookies and Similar Technologies: We may use cookies and similar technologies to collect information about your use of our Services.
Cookies are small text files that are stored on your device to enhance your experience. You can manage your cookie preferences through your browser settings.

2. How We Use Your Information
2.1 Provide and Personalize our Services: We use your information to provide and improve our Services, personalize your user experience, and communicate with you about our offerings.
2.2 Analytics and Research: We may use your information for analytics purposes to understand trends, usage patterns, and user preferences to enhance our Services.
2.3 Marketing and Advertising: With your consent, we may use your information to send you promotional materials and targeted advertisements that may be of interest to you.
2.4 Legal Compliance and Protection: We may use your information to comply with applicable laws, regulations, or legal processes and to protect the rights, property, or safety of InCollege, its users, and others.

3. Information Sharing and Disclosure
3.1 Service Providers: We may share your information with trusted third-party service providers who assist us in providing and improving our Services.
These providers are obligated to maintain the confidentiality and security of your information.
3.2 Legal Requirements: We may disclose your information if required to do so by law or in response to a valid legal request, such as a subpoena or court order.
3.3 Business Transfers: If we are involved in a merger, acquisition, or sale of all or a portion of our assets, your information may be transferred as part of that transaction.
We will notify you of any such change in ownership or control of your personal information.

4. Data Security
We employ industry-standard security measures to protect your personal information from unauthorized access, alteration, disclosure, or destruction.
However, please note that no method of transmission over the Internet or electronic storage is completely secure, and we cannot guarantee the absolute security of your information.

5. Your Rights and Choices
You have the right to access, update, and delete the personal information we hold about you.
You may also have the right to restrict or object to certain processing of your information.
Please contact us using the information provided below to exercise these rights or if you have any questions or concerns regarding your privacy.

6. Children's Privacy
Our Services are not intended for individuals under the age of 13. We do not knowingly collect personal information from children under 13 years of age.
If we become aware that we have collected personal information from a child under 13, we will take steps to delete such information promptly.

7. Changes to this Privacy Policy
We may update this Privacy Policy from time to time. Any changes will be effective upon posting of the revised Privacy Policy.
We encourage you to review this Privacy Policy periodically to stay informed about our privacy practices.

8. Contact Us
If you have any questions, comments, or requests regarding this Privacy Policy, please contact us at <inCollege Email>

Last updated: 6/19/2023
""")
            print("***(1) GUEST CONTROLS ***")
            print("***(2) RETURN ***")
            privacy_choice = input("Please select one of these options (press 1-2): ")
            if privacy_choice == '1':
                print("\n****** GUEST CONTROLS ******")
                print("***(1) DISABLE/ENABLE inCollege EMAIL ***")
                print("***(2) DISABLE/ENABLE SMS ***")
                print("***(3) DISABLE/ENABLE TARGETED ADVERTISING ***")
                guest_control_choice = input("Please select one of these options (press 1-3): ")
                if user != '':
                    if guest_control_choice in ['1','2','3']:
                        with open("data/database.csv", "r") as file:
                            lines = file.readlines()
                            new_lines = []
                            for line in lines:
                                if line.count(',') == 7:
                                    username, passwd, f_name, l_name, language, email_bool, sms_bool, targeted_ads_bool = line.strip().split(',')
                                    if username == user[0]:
                                        if guest_control_choice == '1':
                                            if bool(email_bool) == True:
                                                email_bool = False
                                            else:
                                                email_bool = True
                                        elif guest_control_choice == '2':
                                            if bool(sms_bool) == True:
                                                sms_bool = False
                                            else:
                                                sms_bool = True
                                        elif guest_control_choice == '3':
                                            if bool(targeted_ads_bool) == True:
                                                targeted_ads_bool = False
                                            else:
                                                targeted_ads_bool = True
                                    line = ','.join([username, passwd, f_name, l_name, language, str(email_bool), str(sms_bool), str(targeted_ads_bool)]) + '\n'
                                    new_lines.append(line)
                                else:
                                    break
                        with open("data/database.csv", "w") as file:
                            for line in new_lines:
                                file.write(line)
                        print("\nPreference Saved.")
                else:
                    print("\nPlease sign in to use this feature.")
            #return to previous menu otherwise
        #Cookie Policy
        elif choice == '6':
            print("\n****** COOKIE POLICY ******")
            print("""
This Cookie Policy explains how InCollege ("we" or "us") uses cookies and similar technologies when you access or use our
website, mobile application, or any related services (collectively, the "Services").
By using the Services, you consent to the use of cookies and similar technologies as described in this policy.

1. What are Cookies?
Cookies are small text files that are stored on your device when you visit a website.
They are widely used to make websites work or to improve their efficiency, as well as to provide reporting information and personalized experiences.

2. How We Use Cookies
We use cookies and similar technologies for the following purposes:
2.1 Essential Cookies: These cookies are necessary for the operation of our Services.
They enable you to navigate our website and use its features, such as accessing secure areas and making transactions.
2.2 Analytics Cookies: We use analytics cookies to collect information about your use of our Services, such as the pages you visit and the links you click.
This helps us understand how users interact with our website and improve its performance and functionality.
2.3 Advertising Cookies: We may use advertising cookies to deliver targeted advertisements that may be of interest to you.
These cookies collect information about your browsing activities on our website and other websites to provide you with personalized advertising.
2.4 Third-Party Cookies: We may allow third-party service providers to place cookies on our website to enhance its functionality and performance.
These cookies are subject to the respective privacy policies of these third parties.

3. Your Cookie Choices
Most web browsers are set to accept cookies by default. However, you can manage and control the use of cookies through your browser settings.
Please note that if you disable or reject cookies, some features and functionalities of our Services may be affected.

4. Third-Party Websites
Our Services may contain links to third-party websites that are not controlled or operated by us.
This Cookie Policy does not apply to those third-party websites.
We encourage you to review the cookie policies of those websites for information on their use of cookies.

5. Updates to this Cookie Policy
We may update this Cookie Policy from time to time to reflect changes in our practices or applicable laws.
Any updates will be posted on this page with a revised "Last updated" date.
We encourage you to review this policy periodically to stay informed about our use of cookies.

6. Contact Us
If you have any questions or concerns about our use of cookies or this Cookie Policy, please contact us at <inCollege Email>
Last updated: 6/19/2023
""")
        #Copyright Policy
        elif choice == '7':
            print("\n****** COPYRIGHT POLICY ******")
            print("""
InCollege ("we" or "us") respects the intellectual property rights of others and expects users of our website, mobile application, or any related services (collectively, the "Services") to do the same.
This Copyright Policy outlines our procedures for addressing alleged copyright infringement.

1. Reporting Copyright Infringement
If you believe that your copyrighted work has been copied in a way that constitutes copyright infringement, please provide our Copyright Agent with the following information:
1.1 Identification of the copyrighted work claimed to have been infringed or, if multiple copyrighted works are covered by a single notification, a representative list of such works.
1.2 Identification of the material that is claimed to be infringing or to be the subject of infringing activity
and that is to be removed or access to which is to be disabled, and information reasonably sufficient to permit us to locate the material.
1.3 Your contact information, including your name, address, telephone number, and email address.
1.4 A statement that you have a good faith belief that use of the material in the manner complained of is not authorized by the copyright owner, its agent, or the law.
1.5 A statement that the information in the notification is accurate, and under penalty of perjury, that you are authorized to act on behalf of the owner of an exclusive right that is allegedly infringed.

2. Counter-Notification
If you believe that your material has been removed or disabled as a result of a mistaken identification or misidentification,
you may submit a counter-notification to our Copyright Agent. Please provide the following information:
2.1 Identification of the material that has been removed or disabled and the location at which the material appeared before it was removed or disabled.
2.2 A statement under penalty of perjury that you have a good faith belief that the material was removed or disabled as a result of mistake or misidentification.
2.3 Your contact information, including your name, address, telephone number, and email address.
2.4 A statement that you consent to the jurisdiction of the federal district court in which your address is located, or if your address is outside the United States, any judicial district in which we may be found, and that you will accept service of process from the person who provided the original notification of alleged infringement.

3. Copyright Agent Contact Information
Please direct all notifications and counter-notifications regarding copyright infringement to our Copyright Agent at the following address:
Name: [Copyright Agent Name]
Address: [Copyright Agent Address]
Email: [Copyright Agent Email]

4. Removal of Infringing Content
Upon receipt of a valid and complete copyright infringement notification, we will remove or disable access to the allegedly infringing content
and take reasonable steps to notify the user who posted the content. We may also terminate the accounts of repeat infringers in appropriate circumstances.

5. Changes to this Copyright Policy
We reserve the right to modify or update this Copyright Policy at any time. Any changes will be effective upon posting of the revised policy.
By continuing to use the Services after the posting of any changes, you accept and agree to be bound by the modified policy.

6. Contact Us
If you have any questions, comments, or concerns about our Copyright Policy, please contact us at <inCollege Email>

Last updated: 6/19/2023
""")
        #Brand Policy
        elif choice == '8':
                print("\n****** BRAND POLICY ******")
                print("""
InCollege ("we" or "us") values its brand and trademarks, and we appreciate your interest in promoting our brand.
This Brand Policy outlines the guidelines for the use of our brand assets, including trademarks, logos, and other brand elements.

1. Trademarks and Logo Usage
1.1 Trademark Use: InCollege and our associated logos are registered trademarks owned by us.
You may use our trademarks solely for the purpose of accurately referring to our products or services,
provided that such use complies with this Brand Policy and does not create any confusion or misrepresentation.
1.2 Logo Use: You may not use our logos without our prior written consent.
If you would like to use our logos, please contact us at <inCollege Email> for permission and usage guidelines.

2. Prohibited Uses
2.1 Misrepresentation: You may not use our brand assets in a way that implies endorsement, sponsorship, or affiliation with us without our express permission.
2.2 Modification: You may not modify or alter our brand assets in any way, including color, design, or proportion, without our prior written consent.
2.3 Domain Names and Social Media Handles: You may not use our trademarks or brand elements as part of your domain name, social media handle, or any other identifier without our permission.
2.4 Derivative Works: You may not create derivative works or variations of our brand assets without our prior written consent.

3. Fair Use
You may use our brand assets in a manner that constitutes fair use under applicable copyright and trademark laws.
Fair use typically includes non-commercial commentary, criticism, or news reporting.

4. Enforcement
We reserve the right to enforce this Brand Policy and take appropriate action against any unauthorized use of our brand assets.
We may request the modification or removal of any material that violates this policy.

5. Changes to this Brand Policy
We reserve the right to modify or update this Brand Policy at any time. Any changes will be effective upon posting of the revised policy.
By continuing to use our brand assets after the posting of any changes, you accept and agree to be bound by the modified policy.

6. Contact Us
If you have any questions, comments, or concerns about our Brand Policy or the use of our brand assets, please contact us at [email protected]
Last updated: 6/19/2023""")
        #Languages
        elif choice == '9':
            while True:
                print("\n****** LANGUAGES ******")
                print(f"The current language is {language}, What do you want to change it to? ")
                print("***(1) ENGLISH ***")
                print("***(2) SPANISH ***")
                print("***(3) RETURN ***")
                choice = input("Please select one of these languages(press 1-2): ")
                
                if choice in ['1','2']:
                    if state == "not_logged_in":
                        while True:
                            print("\nYou must have an account to change language")
                            print("\n***(1) LOG IN ***")
                            print("***(2) REGISTER ***")
                            print("***(3) RETURN ***")
                            choice = input("Would you like to login or register a new account (press 1-2): ")
                            if choice == '1':
                                return "logging_in"
                            elif choice == '2':
                                return "registering"
                            elif choice == '3':
                                break
                            else:
                                print("Can you try again?")
                        
                    elif state == "logged_in":
                        if language == "English" and choice == '1':
                            print("\nEnglish is already chosen, please choose other option")
                            continue
                        elif language == "Spanish" and choice == '2':
                            print("\nSpanish is alrady chosen, please choose other option")
                        elif language == "English" and choice == '2':
                            with open("data/database.csv", "r") as file:
                                lines = file.readlines()

                            with open("data/database.csv", "w") as file:
                                for line in lines:
                                    data = line.strip().split(',')
                                    if data[0] == user[0]:
                                        username = data[0]
                                        passwd = data[1]
                                        f_name = data[2]
                                        l_name = data[3]
                                        current_language = "Spanish"
                                        email_bool = data[5]
                                        sms_bool = data[6]
                                        targeted_ads_bool = data[7]
                                        university = data[8]
                                        major = data[9]
                                        
                                        # Additional data (if available)
                                        additional_data = data[10:]
                        
                                        line = ','.join([username, passwd, f_name, l_name, current_language, email_bool, sms_bool, targeted_ads_bool, university, major] + additional_data) + '\n'
                                    file.write(line)
                            language = "Spanish"
                            print("Your language has been changed to Spanish")
                            break
                        elif language == "Spanish" and choice == '1':
                            with open("data/database.csv", "r") as file:
                                lines = file.readlines()

                            with open("data/database.csv", "w") as file:
                                for line in lines:
                                    data = line.strip().split(',')
                                    if data[0] == user[0]:
                                        username = data[0]
                                        passwd = data[1]
                                        f_name = data[2]
                                        l_name = data[3]
                                        current_language = "English"
                                        email_bool = data[5]
                                        sms_bool = data[6]
                                        targeted_ads_bool = data[7]
                                        university = data[8]
                                        major = data[9]
                                        
                                        # Additional data (if available)
                                        additional_data = data[10:]
                                        line = ','.join([username, passwd, f_name, l_name, current_language, email_bool, sms_bool, targeted_ads_bool, university, major] + additional_data) + '\n'
                                    
                                    file.write(line)
                            language = "English"
                            print("Your language has been changed to English")
                            break
                        else:
                            print("Please try again")
                if choice == '3':
                    break
        elif choice == '10':
            return "menu"
        else:
            print("Invalid choice. Please try again!")

def general(state):
    while True:
        print("\n****** GENERAL ******")
        print("***(1) SIGN UP***")
        print("***(2) HELP CENTER***")
        print("***(3) ABOUT***")
        print("***(4) PRESS***")
        print("***(5) BLOG***")
        print("***(6) CAREERS***")
        print("***(7) DEVELOPERS***")
        print("***(8) RETURN***")
        choice = input("Please select one of these options to discover more information (press 1-7): ")
        if choice == '1' and state == "not_logged_in": #if not logged in, it will lead to the login section
            while True:
                print("\n***(1) LOG IN***")
                print("***(2) REGISTER***")
                print("***(3) RETURN***")
                choice = input("Would you like to login or register a new account (press 1-2): ")
                if choice == '1':
                    return "logging_in"
                elif choice == '2':
                    return "registering"
                elif choice == '3':
                    break
                else:
                    print("Invalid choice. Please try again!")
        elif choice == '1' and state == "logged_in":
            print("\nYou have already logged in, do not need to relogin")
        elif choice == '2':
            print("\nWe're here to help")
        elif choice == '3':
            print("\nIn College: Welcome to In College, the world's largest college student network with many users in many countries and territories worldwide")
           
        elif choice == '4':
            print("\nIn College Pressroom: Stay on top of the latest news, updates, and reports")
           
        elif choice in ['5','6','7']:
            print("\nUnder Construction")
        elif choice == '8':
            return
        else:
            print("Invalid choice. Please try again!")
