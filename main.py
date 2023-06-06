
import streamlit as st
import pandas as pd
from datetime import datetime


###################### Get the Customer Payment History Data here ##############################
# # Sample data
data = pd.DataFrame({
    'Name': ['John', 'Jane', 'Bob', 'Alice', 'trt'],
    'Age': [25, 30, 28, 35, 33],
    'City': ['New York', 'London', 'Paris', 'Tokyo', 'London'],
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Male']
})


# Get current year and month
current_year = 2021
current_month = datetime.now().month

# Generate list of months (From jan 2021 till last month this year)
months_list = []
for i in range(current_year, datetime.now().year + 1):
    if i != datetime.now().year:
        months_list.extend([datetime(i, month, 1).strftime("%B %Y") for month in range(1, 13)])
    else:
        months_list.extend([datetime(i, month, 1).strftime("%B %Y") for month in range(1, current_month)])


###################### Define your Functions here ##############################

# Filter functions
def filter_by_age(df, age):
    return df[df['Age'] == age]

def filter_by_city(df, city):
    return df[df['City'] == city]

st.write('<style>body { font-size: 50px; }</style>', unsafe_allow_html=True)


# Streamlit app
def main():
    st.title("Roll Rate Simulation")
    st.title("Deploy Timestamp - 1327 - Jun6")


    # Dropdown inputs for filtering
    ###################### Add your dropdowns and their values here ##############################
    st.radio("Select Aggregation Level", ('Monthly', '6-Month Period'))
    
    age_filter = st.selectbox("Select Disbursal Month", months_list)
   
    col1, col2 = st.columns(2)
    min_value = 6
    max_value = 24
    # Create columns layout
    col1, col2 = st.columns(2)
    # Slider 1
    with col1:
        value1 = st.slider("TimeFrame 1", min_value=min_value, max_value=max_value, value=min_value)
    # Slider 2
    with col2:
        value2 = st.slider("TimeFrame 2", min_value=value1 + 3, max_value=max_value, value=value1 + 3)

    # Tabs for selecting filter type
    filter_type = st.radio("Select Filter Type", ('Approach1', 'Approach2'))


    if filter_type == 'Approach1':
        filtered_data = filter_by_age(data, age_filter)
    elif filter_type == 'Approach2':
        filtered_data = filter_by_city(data, city_filter)

    # Show output
    st.subheader("Roll-Rate Table")
    st.write(filtered_data)

if __name__ == "__main__":
    main()

