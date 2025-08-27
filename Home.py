import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import os
import numpy as np
import pickle




st.set_page_config(layout="wide")

# Your Streamlit app code goes here
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
    
def Main():
    Pkl_Filename = 'Models/insurance_model.sav'
    apply_custom_css()
    with open(Pkl_Filename, 'rb') as file:
        model = pickle.load(file)

    

    st.title("Prediction App")

    def predict(features):
        final = np.array(features).reshape((1, 6))
        pred = model.predict(final)[0]
        return pred



    # Input fields
    col1, col2 = st.columns(2)
    
    with col1:
        Age = st.text_input('Age [0]', value=0.0);
        
    with col2:
        Sex = st.text_input('Sex [M:0, F:1]', value=0.0)
    
    with col1:
        BMI = st.text_input('BMI [18.5 - 24.9]', value=0.0)
    
    with col2:
        Children = st.text_input('Children [0]', value=0.0)
    
    with col1:
        Smoker = st.text_input('Smoker [Y:0, N:0]', value=0.0)
    
    with col2:
        Region = st.text_input('Region [SE:0, SW:1, NE:2, NW:3]', value=0.0)
    
    

    

    features = [float(Age), float(Sex), float(BMI), float(Children), float(Smoker), float(Region)]


    if st.button("Predict"):
        input_data_as_numpy_array = np.asarray(features)
        input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
        predict_data = model.predict(input_data_reshaped)
        
        if predict_data < 0:
            st.error("Error calculating Amount!")
        else:
            st.success(f"Expected amount is {predict_data}")


def contact_form():
    st.header(":mailbox: Get In Touch With Me!")
    contact_form = """
    <form action="https://formsubmit.co/manojmahato08779@gmail.com" method="POST">
         <input type="hidden" name="_template" value="table">
         <input type="text" name="name" placeholder="Your name" required>
         <input type="email" name="email" placeholder="Your email" required>
         <textarea name="message" placeholder="Your message here"></textarea>
         <button type="submit">Send</button>
    </form>
    """

    st.markdown(contact_form, unsafe_allow_html=True)

    # Use Local CSS File
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}<Style/style>", unsafe_allow_html=True)


    local_css("Style/style.css")
    
def home_scr():
    col1, col2 = st.columns([3,1])

    with col1:
        st.write('Machine learning (ML) enables accurate predictions of medical expenses by analyzing historical data on patient characteristics, treatments, and costs.')
        st.write('By preprocessing and engineering features, ML models learn patterns and correlations to estimate future medical costs.')
        st.write('This approach benefits healthcare providers in financial planning and resource allocation, empowers patients with personalized cost predictions, and helps insurers optimize pricing and detect fraud.')
        st.markdown('ML-based predictions revolutionize healthcare finance and improve decision-making.')
        st.markdown(
            """
            <style>
            .footer {
                text-align: center;
                font-size: 24px;
                </style>
            """,
            unsafe_allow_html=True
        )
        st.markdown('<p class="footer">Subscribe for ❤️ Latest Updates</p>', unsafe_allow_html=True)
        News_Latter = """
        <form action="https://formsubmit.co/manojmahato08779@gmail.com" method="POST">
             <input type="hidden" name="_template" value="table">
             <input type="email" name="email" placeholder="Your email" required>
             <button type="submit">Subscribe</button>
        </form>
        """

        st.markdown(News_Latter, unsafe_allow_html=True)

        # Use Local CSS File
        def local_css(file_name):
            with open(file_name) as f:
                st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


        local_css("Style/News_style.css")

        
    with col2:
        image = Image.open('Images/injury-pana.png')
        st.image(image)
        
    st.markdown("""---""")
    
    col1, col2 = st.columns([2, 3])

    with col1:
        image = Image.open('Images/Visualdata-bro.png')
        st.image(image, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
    with col2:
        
        st.header("Project Description")
        st.markdown("The goal of this project is to utilize machine learning techniques to predict future medical expenses. By analyzing historical data and relevant factors, we can provide accurate estimates of healthcare costs for individuals and populations.")
        st.markdown(" Our goal is to leverage the power of machine learning algorithms to accurately predict future medical expenses for individuals and populations. ")
        st.markdown("By analyzing extensive healthcare data, including patient demographics, medical history, procedures, medications, and corresponding expenses, our platform provides valuable insights into healthcare costs.")
        st.markdown('')
        st.markdown('Model Used = > Linear Regression')
        st.markdown('')
        st.markdown('Model Accuracy = > 75.15%')
        
    st.markdown("""---""")
    
    col1, col2 = st.columns([3, 2])

    with col1:
        st.header("How It Works")
        st.markdown("1. **Data Collection:** We gather comprehensive datasets containing patient demographics, medical history, procedures, medications, and corresponding expenses.")
        st.markdown("2. **Data Preprocessing and Feature Engineering** We employ advanced data preprocessing techniques to clean and transform the raw healthcare data into a format suitable for machine learning models. Additionally, we perform feature engineering to extract relevant features and create new variables that capture important patterns and relationships.")
        st.markdown("3. **Machine Learning Models:** Our advanced machine learning models analyze the collected data to identify patterns and relationships that influence healthcare costs.")
        st.markdown("4. **Model Training and Validation:** The machine learning models are trained using the preprocessed data and evaluated through rigorous validation processes. We employ techniques such as cross-validation, hyperparameter tuning, and performance metrics to ensure the models' accuracy, robustness, and generalizability.")
        st.markdown("5. **Predictive Insights:** Our platform generates personalized predictions for medical expenses, helping individuals and organizations make informed decisions.")

    with col2:
        image = Image.open('Images/injury-amico.png')
        st.image(image, width="auto", use_column_width="auto", clamp=True, channels="RGB", output_format="auto")
    
    st.markdown("""---""")
    
    col1, col2 = st.columns([1, 3])

    with col1:
        image = Image.open('Images/Innovation-amico.png')
        st.image(image)
    with col2:
        
        # Display why choose us
        st.header("Why Choose Us")
        st.markdown(":red_circle: **Accurate Predictions:** Our models are trained on vast amounts of data, ensuring accurate estimates of future medical expenses.")
        st.markdown(":red_circle: **Customized Solutions:** We provide personalized predictions tailored to your specific needs.")
        st.markdown(":red_circle: **Data Security:** We prioritize the security and privacy of your data, adhering to strict data protection regulations.")
        st.markdown(":red_circle: **Transparent and Interpretable Results:** Our models provide insights into the factors influencing predicted medical expenses, enabling informed decision-making.")
        
    st.markdown("""---""")
    
    st.markdown(
        """
        <style>
        .foot {
            text-align: center;
            font-size: 24px;
            </style>
        """,
        unsafe_allow_html=True
    )
    st.markdown('<p class="foot">Get Started 🌉 Today</p>', unsafe_allow_html=True)
    st.markdown("Ready to harness the power of machine learning to predict medical expenses? Sign up now to access our platform and gain valuable insights into future healthcare costs.")
    
    st.markdown("""---""")
       
    
selected = option_menu(None, ["Home", "Test",  "About", 'Contact'], 
                icons=['house', 'cloud-upload', "list-task", 'gear'], 
                menu_icon="cast", default_index=0, orientation='horizontal',
                styles={
                    "container": {"padding": "0!important", "background-color": "#272343"},
                    "icon": {"color": "orange", "font-size": "20px"}, 
                    "nav-link": {"font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "#272343"},
                    "nav-link-selected": {"background-color": "#ffd803"},
                })
    
if selected == "About":
    
    st.markdown("""
    ## Our Mission

    Our mission is to leverage the power of machine learning to help individuals and healthcare providers predict medical expenses more accurately. By doing so, we aim to improve financial planning and resource allocation in the healthcare industry.

    ## Our Team

    We are a team of dedicated data scientists, software engineers, and healthcare professionals who are passionate about using technology to improve healthcare outcomes.

    ## Our Values

    - **Innovation:** We are committed to exploring new ideas and technologies to stay at the forefront of machine learning and healthcare.
    - **Collaboration:** We believe in the power of teamwork and open communication to achieve our goals.
    - **Accuracy:** We strive for the highest level of precision in our predictions to ensure reliable results for our users.
    - **User Focus:** We prioritize the needs of our users and work tirelessly to create intuitive and user-friendly tools.
    - **Ethics:** We are dedicated to maintaining the privacy and security of our users' data and adhering to the highest ethical standards in our work.

    

    If you have any questions or would like to learn more about our medical expenses prediction project, please feel free to reach out to us at [sharmadit27.com](mailto:manojmahato08779@gmail.com).
    """)
    
if selected == "Contact":
    contact_form()
    
if selected == "Test":
    Main()
    
if selected == "Home":
    # Display the image in the hero section
   home_scr()
