import streamlit as st 
from pandas import DataFrame
from gspread_pandas import Spread,Client
from google.oauth2 import service_account

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = service_account.Credentials.from_service_account_info(
                st.secrets["gcp_service_account"], scopes = scope)
client = Client(scope=scope,creds=credentials)
spreadsheetname = "司机一周统计表"
spread = Spread(spreadsheetname,client = client)

# Check the connection
st.write(spread.url)

sh = client.open(spreadsheetname)

the_new = st.button('new')
if the_new :
    old_title = "template"
    new_title = "the_new_sheet"
    index = 1  # Insert the new sheet at index 1
    worksheet = sh.get_worksheet_by_name('template')
    worksheet_id = worksheet.id
    sh.duplicate_sheet(worksheet_id, new_title, index)
