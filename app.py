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
    try:
        validation = email_validator.validate_email(email = e)
        if(validation.domain == 'snowflake.com'):
            return True
        else:
            st.write("Only Valid Snowflake Accounts are Allowed.")
            return False
        
    except email_validator.EmailNotValidError as e:
          st.write(str(e))
          return False


    

st.title('Ticker Admin Dashboard')
st.text('Please Enter your Email below to gain access to the Ticker Snowflake account.')
st.text('Please note that the script uses CREATE OR REPLACE USER to assign access.')
st.text('After providig your email. Your credentials will be emailed to your Snowflake Email')

email_input = st.text_input(
        "Enter your Snowflake E-Mail👇",
        placeholder = "Only Valid Snowflake E-Mails Allowed"
    )

if st.button('GO!'):
    valid_email = check_email(email_input)
    if valid_email==True:
        run_query( f' CALL admin.public.create_new_user(\'{email_input.upper()}\'); ' )
        st.write('Please Check your E-Mail for access. \n Please do wait 5 minutes for the E-Mail.')
    else:
        st.write(f'VALID EMAIL: {valid_email}')


