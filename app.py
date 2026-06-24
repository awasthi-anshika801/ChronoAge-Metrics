import streamlit as st
from datetime import date
import time

st.title("ChronoAge Metrics🗓️")
st.markdown("Precision *Time-based* Age Analysis")
today= date.today()
min_date= date(today.year-100,1,1)
dob=st.date_input("Enter your date👉",value=date(2000,1,1),min_value=min_date,max_value=today)
if st.button("Calculate Age"):
    if dob:
        with st.spinner("calculate Age, please wait for a while..."):
            time.sleep(5)

        age= today.year-dob.year
        if(today.month,today.day)< (dob.month, dob.day):
            age=age-1

        total_days = (today - dob).days
        approx_months = int(total_days / 30.4375) #Every month has different days like some has 30, some has 31, and feb has 29 so total days of year is 365 and 365 divided by 12 then average is 30.4375
        weeks = int(total_days / 7)

        # count next birthday
        next_birth_year = today.year
        if today > date(today.year, dob.month, dob.day):
            next_birth_year += 1
        next_birthday = date(next_birth_year, dob.month, dob.day)
        days_to_birthday = (next_birthday - today).days

        col1,col2=st.columns(2)
        col1.metric("your current age is:", f"{age} years")
        col2.metric("Days left for your next birthday are:", f"{days_to_birthday} days")


        with st.expander("Detailed Time breakdown📊"):
            st.write(f"**Total Months lived:** {approx_months:} months")
            st.write(f"**Total Weeks lived:** {weeks:} weeks")
            st.write(f"**Total Days lived:** {total_days:} days")


    # success widget implemented inside if block so that it shows only after calculation
        st.success("Age is successfully calculated!🎉")

