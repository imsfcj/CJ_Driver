import streamlit as st 
from datetime import date, timedelta, datetime
import sqlite3, os, time, re, pytz
from pytz import timezone
from io import BytesIO
import pandas as pd
from pandas import DataFrame
from gspread_pandas import Spread,Client
from google.oauth2 import service_account
from gsheetsdb import connect
from collections import defaultdict

st.set_page_config(page_title='CJ sheet助手',page_icon = "🛐" ,initial_sidebar_state = 'expanded')
m = st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: #b5a2c8;
    color:#ffffff;
}
div.stButton > button:hover {
    background-color: #C8A2C8;
    color:#ff0000;
    }
</style>""", unsafe_allow_html=True)

st.sidebar.image('./pages/setup/images/aba_icon6.jpg', width=100)
st.sidebar.title("程序运行详情")

def to_excel(df):
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    df.to_excel(writer, encoding='utf-8-sig', index=False, sheet_name='Sheet1')
    workbook = writer.book
    worksheet = writer.sheets['Sheet1']
    format1 = workbook.add_format({'num_format': '0'})
    worksheet.set_column('A:A', None, format1)
    writer.save()
    processed_data = output.getvalue()
    return processed_data
    
toronto_timezone = timezone('America/Toronto')   
now = datetime.now(tz=toronto_timezone)
today = now.date()
today_str = today.strftime('%b%d_%a')
the_day = today.strftime('%a')
if the_day == 'Mon' : the_pick = 1
if the_day == 'Tue' : the_pick = 2
if the_day == 'Wed' : the_pick = 3
if the_day == 'Thu' : the_pick = 4
if the_day == 'Fri' : the_pick = 5
if the_day == 'Sat' : the_pick = 6
if the_day == 'Sun' : the_pick = 0
st.write(today_str)


# Get the day of the week (1-7, where 1 is Monday and 7 is Sunday)
day_of_week = today.isoweekday()

# Calculate the starting and ending dates of the week
start_of_week = today - timedelta(days=day_of_week - 1)
end_of_week = today + timedelta(days=7 - day_of_week)

# Print the starting and ending dates
this_week = "{}-{}".format(start_of_week.strftime("%b%d"), end_of_week.strftime("%b%d"))
#st.write(this_week)

next_week = today + timedelta(days=7)

# Get the day of the week (1-7, where 1 is Monday and 7 is Sunday)
day_of_week = next_week.isoweekday()

# Calculate the starting and ending dates of the week
start_of_week = next_week - timedelta(days=day_of_week - 1)
end_of_week = next_week + timedelta(days=7 - day_of_week)

# Print the starting and ending dates
next_week = "{}-{}".format(start_of_week.strftime("%b%d"), end_of_week.strftime("%b%d"))
#st.write(next_week)



st.title("统计司机助手")
tab1,tab2 = st.tabs(["每日统计","一周统计"])    
form1 = tab1.form(key="Options")
choice = form1.selectbox("想统计哪一天的司机报名情况？",('Mon','Tue','Wed','Thu','Fri','Sat','Sun'),index=the_pick)
form1.header("统计每日司机")
main_container1 = tab1.container()
main_container1.write("")
bt1 = form1.form_submit_button("提交")
dm1,dm2 = tab1.columns(2)
dm1.subheader("司机号")
dm2.subheader("配送地区")   
    
    
    
    
    
    
if bt1 :
    st.write(choice)
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']

    credentials = service_account.Credentials.from_service_account_info(
                    st.secrets["gcp_service_account"], scopes = scope)
    client = Client(scope=scope,creds=credentials)
    spreadsheetname = "司机一周统计表"
    spread = Spread(spreadsheetname,client = client)
    sh = client.open(spreadsheetname)
    #schedule_sheet = sh.worksheet(this_week)
    df = spread.sheet_to_df(index=0,sheet=this_week)
    day_driver = df.loc[:, ['Driver', 'Location', choice]]
    count = dict()
    for index, row in day_driver.iterrows():
        if row[choice] != '1' : continue
        on_board = str(row['Driver'])
        the_area = row['Location'].upper().replace(' ','_')
        count[on_board]=the_area
    df = pd.DataFrame()
    for d,a in count.items() :
        df = df.append({a:d},ignore_index=True)
    df = df.apply(lambda x: pd.Series(x.dropna().values)).fillna(' ').dropna(axis=1, how='all')
    st.write(df)














#
