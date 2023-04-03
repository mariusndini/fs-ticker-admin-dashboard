import streamlit as st
import snowflake.connector

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


st.title('This is a title')
st.title('A title with _italics_ :blue[colors] and emojis :sunglasses:')
