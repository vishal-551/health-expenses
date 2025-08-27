
import streamlit as st
from pymongo import MongoClient
from passlib.hash import pbkdf2_sha256
import subprocess
import webbrowser
from streamlit_option_menu import option_menu
url = 'https://health-horizon.onrender.com/'

# Connect to MongoDB
#client = MongoClient("mongodb://localhost:27017/")
client = MongoClient("mongodb+srv://manojmahato08779:ManojMahato6969@cluster0.hqts8hc.mongodb.net/?retryWrites=true&w=majority")
db = client["mydatabase"]
users = db["users"]
#my_list = ["streamlit", "run", "Main.py"]  # 👈️ list

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
        user = users.find_one({"username": username})
        if user and pbkdf2_sha256.verify(password, user["password"]):
            st.success("Logged in as {}".format(username))
            
            if st.button('Open browser'):
                webbrowser.open_new_tab(url)

            # Run the Main.py file as a separate process
            subprocess(["streamlit", "run", "Main.py"])
            process = subprocess.run(command, capture_output=True, text=True)

            # Print the output of the Main.py app
            st.write("Output from Main.py:\n{}".format(process.stdout))

            # Exit the current Streamlit app process
            raise SystemExit
        else:
            st.error("Incorrect username or password")


# Signup Function
def signup():
    st.title("Signup App")
    apply_custom_css()
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Signup"):
        if users.find_one({"username": username}):
            st.error("Username already exists")
        else:
            hashed_password = pbkdf2_sha256.hash(password)
            users.insert_one({"username": username, "password": hashed_password})
            st.success("Account created")

# Streamlit App
def app():
    #st.title("Login/Signup App")
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
    if choice == "Signup":
            signup()

if __name__ == "__main__":
    app()