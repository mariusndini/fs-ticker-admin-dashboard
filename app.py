import streamlit as st
import snowflake.connector
import email_validator



# CONNECT TO SNOWFLAKE  
conn = snowflake.connector.connect( user= st.secrets["user"],
                                    password= st.secrets["password"],
                                    account= st.secrets["account"],
                                    role = st.secrets["role"],
                                    warehouse = st.secrets["warehouse"],
                                    session_parameters={
                                        'QUERY_TAG': 'Streamlit',
                                    })

# function to run queries on Snowflake
def run_query(query): 
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

def check_email(e):
    return email_validator.validate_email(email = e, domain = 'snowflake.com')
    

st.title('Ticker Admin Dashboard')
st.text('Please use the inputs below to gain access to the Ticker Snowflake account.')

text_input = st.text_input(
        "Enter your Snowflake E-Mail👇",
        placeholder = "Only Valid Snowflake E-Mails Allowed"
    )

if st.button('GO!'):
    valid_email = check_email(text_input)
    st.write(valid_email)



