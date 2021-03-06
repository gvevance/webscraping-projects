# helper functions

import requests

from search import search_menu
from product_details import product_details_menu
from price_history import price_history_menu


def getCredentials(credfile):

    with open(credfile) as cfile :
        username = cfile.readline().strip()
        password = cfile.readline().strip()

    return username , password


def login_amazon(session,email,password) :
    ''' login into Amazon. No return object.
        session is an HTTP requests session.
        email and password are the corresponding strings of email/phone number and password.'''

    main_url = "https://www.amazon.in/ap/signin"

    session.headers['user-agent'] = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36'
    res = session.get(main_url)
    cookies = dict(res.cookies)

    payload = {
        'appActionToken': 'j5h9SCJQSGUvVocGUl5pNXtL00gj3D' ,
        'appAction': 'SIGNIN_PWD_COLLECT' ,
        'subPageType': 'SignInClaimCollect' ,
        'openid.return_to': 'ape:aHR0cHM6Ly93d3cuYW1hem9uLmluL2dwL3lvdXJzdG9yZS9ob21lP3BhdGg9JTJGZ3AlMkZ5b3Vyc3RvcmUlMkZob21lJnNpZ25Jbj0xJnVzZVJlZGlyZWN0T25TdWNjZXNzPTEmYWN0aW9uPXNpZ24tb3V0JnJlZl89bmF2X0FjY291bnRGbHlvdXRfc2lnbm91dA==' ,
        'prevRID': 'ape:SjdDOUI2NTk1RE1FRTlQOTBTUFI=' ,
        'workflowState': 'eyJ6aXAiOiJERUYiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiQTI1NktXIn0.z3_n5DAdsj4vYBI8uXgUNyVYAT3tX-1isQYN4m1sGbTydMrT6SIUpw.w8UhOfBTQ3Ka6sGk.dUD1sITM3R2yGVLtA4UR6FGUtL5obVQK6hseonsVJwktxumw9bhYZ2n_k9KRsQJFFc96uPG1V_IFNmRLQ5EURu8XzYpJnkRuCys18C4YYFRuWAyegCMsMW9z-wtBcKPNq2aslunvVH0UYFRVbQ6_7TwT9vm5c_w5uMTEmULMHigMXC_qyFGsFmvDPRIG58-42b_ELgYbY5kpCLM9j-2w8Q-_os87TJ8K-Uli_H8fsX4d3wGQpegUrIDpachFgJEw9e4kmZ62Erv1076fNO_JFUS6770.mPwZUyMlURTkEXR7Hu4QpA' ,
        'email': email ,
        'password': password ,
        'create': '0' ,
        'metadata1':'ECdITeCs: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'
    }

    # login into account
    session.post(main_url,data=payload,cookies=cookies)    # not storing return value


def session_init(menu_choice):

    credfile = "Amazon_ID.txt"
    email,password = getCredentials(credfile)

    with requests.Session() as session :

        # login into amazon. session object is sent as a reference so no need of return object
        print("\nLogging into Amazon.")
        try :
            login_amazon(session,email,password)
            print("Login successful.")

        except :
            continue_nologin = input("Amazon login error. Continue without logging in ? (YES/no) ? ")
            if continue_nologin == "no" :
                exit()

        if menu_choice == '1' :
            search_menu(session)

        elif menu_choice == '2' :
            product_details_menu(session)

        elif menu_choice == '3' :
            price_history_menu(session)

        else :
            print("Error. Aborting ... ")
            exit()
