import pyrebase

firebaseConfig = {

  "apiKey": "AIzaSyDtL9GBSaF1iHQkE1KZ0VXmHXqR9A2cM3M",

  "authDomain": "authpython-c0162.firebaseapp.com",

  "projectId": "authpython-c0162",

  "storageBucket": "authpython-c0162.firebasestorage.app",

  "messagingSenderId": "63169207974",

  "appId": "1:63169207974:web:0e7a3a529dc9a8e5995e67",

  "databaseURL": "https://authpython-c0162-default-rtdb.firebaseio.com/"
};

firebase = pyrebase.initialize_app(firebaseConfig)

auth = firebase.auth()

def signUp():
    email = input("email: ")
    password = input("password: ")

    auth.create_user_with_email_and_password(email, password)
    print("User created.")

def login():
    email = input("email: ")
    password = input("password: ")

    try: 
        user = auth.sign_in_with_email_and_password(email, password)
        print(user)
        print(auth.get_account_info(user["idToken"]))
        print("Successfully logged in.")
    except:
        print("Incorrect e-mail or password!")

# signUp()
login()
