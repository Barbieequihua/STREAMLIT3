import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

#Dashboard's main title
st.title("Sales Analysis Data Dashboard")

#Creating an upload section for the file either excel or csv
uploaded_file = st.file_uploader("Choose a file", type=["csv", "xlsx"])

#Checking if the file is uploaded
if uploaded_file is not None:
    #detects csv or excel and transforms it as a dataframe
    if uploaded_file is not None:
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)

    #Create a data table that is filtered by region
    st.subheader('By Region Datatable')

    unique_region = df['REGION'].unique().tolist() #obtain each unique region 
    unique_region.insert(0, "All")  # add the all option as well (consider all regions)
    selected_value = st.selectbox("Select value", unique_region) #select the region or all option

    # Filter according to the selection all or specific region
    if selected_value == "All":
        filtered_df = df  # show entire dataframe (all option)
    else:
        filtered_df = df[df['REGION'] == selected_value]  # filter by region 

    # show the filtered data frame according to the selection 
    st.write(filtered_df)

    #Create the sales graph section

    st.subheader('Sales Analysis')
     
    #Units sold chart per vendor

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    ax1.barh(filtered_df['NAME'], filtered_df['SOLD UNITS'], color='purple')
    ax1.set_title('Units Sold by Vendor')
    ax1.set_xlabel("Units Sold")   # eje X = cantidad
    ax1.set_ylabel("Vendor")       # eje Y = nombres
    ax1.tick_params(axis='y', labelsize=6)
    

    #Units sold chart per region

    ax2.bar(filtered_df['REGION'], filtered_df['SOLD UNITS'], color = 'purple')
    ax2.set_title('Units Sold by Region')
    ax2.set_xlabel("Region")
    ax2.set_ylabel("Units Sold")

    st.pyplot(fig) #show both graphs

    fig2, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

     #Total Sales chart per vendor
    ax1.barh(filtered_df['NAME'], filtered_df['TOTAL SALES'])
    ax1.set_title('Total Sales by Vendor')
    ax1.set_xlabel("Total Sales")   # eje X = cantidad
    ax1.set_ylabel("Vendor")       # eje Y = nombres
    ax1.tick_params(axis='y', labelsize=6)
    
    

    #Total Sales chart per region
    ax2.bar(filtered_df['REGION'], filtered_df['TOTAL SALES'])
    ax2.set_title('Total Sales by Region')
    ax2.set_xlabel("Region")
    ax2.set_ylabel("Total Sales")
    st.pyplot(fig2) #show both graphs

    fig3, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    #Average sales chart per vendor
    ax1.barh(filtered_df['NAME'], filtered_df['SALES AVERAGE'], color='orange')
    ax1.set_title('Average Sales by Vendor')
    ax1.set_xlabel("Average SAles")   # eje X = cantidad
    ax1.set_ylabel("Vendor")       # eje Y = nombres
    ax1.tick_params(axis='y', labelsize=6)
    
    
    
    #Average sales chart per region
    ax2.bar(filtered_df['REGION'], filtered_df['SALES AVERAGE'], color = 'orange')
    ax2.set_title('Sales Average by Region')
    ax2.set_xlabel("Region")
    ax2.set_ylabel("Average Sales")
    st.pyplot(fig3) #show both graphs

    #Create a filtered data table per specific vendor
    st.subheader('By Vendor Data')
    unique_vendors = df['NAME'].unique() #obtain each unique vendor value
    selected_value = st.selectbox("Select value", unique_vendors) #select the vendor

    filtered2_df = df[df['NAME'] == selected_value]#filter by selected vendor
    st.write(filtered2_df)#show the table 

