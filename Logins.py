import streamlit as st
from pymongo import MongoClient
from passlib.hash import pbkdf2_sha256
import subprocess
import webbrowser
from streamlit_option_menu import option_menu

# Your target URL after login
url = 'https://health-horizon.onrender.com/'

# Connect to MongoDB using the provided connection string
client = MongoClient("mongodb+srv://vishaldas571725_db_user:B637JUZlffjtGyrh@cluster0.7q6g4il.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["mydatabase"]
users = db["users"]

# Function to apply custom CSS
def apply_custom_css():
    custom_css = """
    <style>
        body {
            background-color: #f0f2f6;
        }
        .stApp {
            padding: 2rem;
        }
        .stTextInput input {
            border-radius: 5px;
            border: 1px solid #ced4da;
            padding: 0.5rem;
        }
        .stButton>button {
            border-radius: 5px;
            width: 100%; /* Full width */
            background-color: #ffd803;
            color: white;
            padding: 0.5rem 1rem;
            font-size: 1rem;
            border: none;
        }
        .stButton>button:hover {
            background-color: #272343;
            text-color: #ffd803;
        }
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)

# Login Function
def login():
    st.title("Login App")
    apply_custom_css()
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        # Fetch user from DB
        user = users.find_one({"username": username})
        
        # If user exists and password matches
        if user and pbkdf2_sha256.verify(password, user["password"]):
            st.success(f"Logged in as {username}")

            # Open the provided URL if button is pressed
            if st.button('Open browser'):
                webbrowser.open_new_tab(url)

            # Instead of subprocess, we can just provide a link to the other Streamlit app
            st.write("Now, you're redirected to the main app!")
            st.markdown(f"Click [here]({url}) to proceed to the main app.")

            # You can also directly use subprocess to run another Streamlit app (but less common)
            # subprocess.run(["streamlit", "run", "Main.py"])  # Make sure the path is correct for Main.py

        else:
            st.error("Incorrect username or password")

# Signup Function
def signup():
    st.title("Signup App")
    apply_custom_css()
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Signup"):
        # Check if username already exists
        if users.find_one({"username": username}):
            st.error("Username already exists")
        else:
            # Hash the password and store it in MongoDB
            hashed_password = pbkdf2_sha256.hash(password)
            users.insert_one({"username": username, "password": hashed_password})
            st.success("Account created successfully! Please login.")

# Streamlit App
def app():
    with st.sidebar:
        choice = option_menu(None, ["Signup", "Login"], 
                             icons=['house', 'cloud-upload'], 
                             menu_icon="cast", default_index=0,
                             styles={
                                 "container": {"padding": "0!important", "background-color": "#272343"},
                                 "icon": {"color": "orange", "font-size": "20px"}, 
                                 "nav-link": {"font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "#272343"},
                                 "nav-link-selected": {"background-color": "#ffd803"},
                             })
    
    if choice == "Login":
        login()
    elif choice == "Signup":
        signup()

# Run the Streamlit app
if __name__ == "__main__":
    app()
