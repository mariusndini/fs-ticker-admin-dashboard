import streamlit as st
import snowflake.connector
import email.utils



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
    msg = email.message_from_string(data[0][1])
    addr = email.utils.parseaddr(msg['From'])[1]
    domain = addr.split('@')[1]
    if domain == "example.com":
        return True
    else:
        return False

st.title('Ticker Admin Dashboard')
st.text('Please use the inputs below to gain access to the Ticker Snowflake account.')

text_input = st.text_input(
        "Enter your SNOWFLAKE E-Mail👇",
        placeholder = "Only Valid Snowflake E-Mails Allowed"
    )

if st.button('GO!'):
    st.write(text_input)



