# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 09:16:48 2023

@author: Jean-Christophe KOURAJIAN
"""


import json
from linkedin_api import Linkedin

"""Retrieve Linkedin credentials and log in"""
def enter_username():
    LINKEDIN_USERNAME = input("Enter your Linkedin username (email address): ")
    return LINKEDIN_USERNAME

def enter_password():
    LINKEDIN_PASSWORD = input("Enter your Linkedin password: ")
    return LINKEDIN_PASSWORD

def enter_linkedin_profile_name():
    LINKEDIN_PROFILE_NAME = input(
        """Enter your Linkedin profile name (from the URL of your page after "https://www.linkedin.com/in/..."): """
    )
    return LINKEDIN_PROFILE_NAME

LINKEDIN_USERNAME = enter_username()
LINKEDIN_PASSWORD = enter_password()
LINKEDIN_PROFILE_NAME = enter_linkedin_profile_name()
api = Linkedin(LINKEDIN_USERNAME, LINKEDIN_PASSWORD)

def extract_account_info():
    profile = api.get_profile(LINKEDIN_PROFILE_NAME)
    with open('profile.json', 'wb') as f:
        f.write(json.dumps(profile).encode())
    contact_info = api.get_profile_contact_info(LINKEDIN_PROFILE_NAME)
    with open('contact_info.json', 'wb') as f:
        f.write(json.dumps(contact_info).encode())

"""Retrieve Linkedin connections to add"""

def enter_contacts_list():
    input_list = input("""\nEnter the profile names or URLs of your contacts separated by spaces: """)
    contact_list = []

    for item in input_list.split():
        if "linkedin.com/in/" in item:
            profile_name = item.split("/in/")[-1]
            contact_list.append(profile_name.rstrip('/'))
        else:
            contact_list.append(item)

    return contact_list

# Exemple d'utilisation
contacts = enter_contacts_list()
print("Contacts:", contacts)

for contact in contacts:
    response = api.add_connection(contact)
    print(response, "--> "+contact)

"""
https://www.linkedin.com/in/jckourajian/
"""

"""
return False if already a connection
return False if not already a connection but in validation
return True if it's a new request of connection and now pending
"""

#  https://github.com/tomquirk/linkedin-api/blob/e66bb5e217ab3383f4c2a6a25f8cd793b5b20b61/linkedin_api/linkedin.py#L1105


"""
https://github.com/tomquirk/linkedin-api
Caution: This library is not officially supported by LinkedIn. 
Using it might violate LinkedIn's Terms of Service. Use it at your own risk.

https://github.com/tomquirk/linkedin-api#i-keep-getting-a-challenge
linkedin_api.client.ChallengeException: CHALLENGE
--> disable 2FA
"""
