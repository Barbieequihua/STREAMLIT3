import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Dashboard's main title
st.title("Sales Analysis Data Dashboard")

df = pd.read_excel('sellers.xlsx')

# Create a data table that is filtered by region
st.subheader('By Region Datatable')

unique_region = df['REGION'].unique().tolist() # obtain each unique region 
unique_region.insert(0, "All")  # add the all option as well (consider all regions)

# Cambié la clave (key) para que no choque con el segundo selectbox posterior
selected_value = st.selectbox("Select region", unique_region, key="region_select") 

# Filter according to the selection all or specific region
if selected_value == "All":
    filtered_df = df  # show entire dataframe (all option)
else:
    filtered_df = df[df['REGION'] == selected_value]  # filter by region 

# show the filtered data frame according to the selection 
st.write(filtered_df)

# Create the sales graph section
st.subheader('Sales Analysis')
     
# ------------------ GRÁFICA 1: UNITS SOLD ------------------
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

ax1.barh(filtered_df['NAME'], filtered_df['SOLD UNITS'], color='purple')
ax1.set_title('Units Sold by Vendor')
ax1.set_xlabel("Units Sold")   # eje X = cantidad
ax1.set_ylabel("Vendor")       # eje Y = nombres
ax1.tick_params(axis='y', labelsize=6)

ax2.bar(filtered_df['REGION'], filtered_df['SOLD UNITS'], color='purple')
ax2.set_title('Units Sold by Region')
ax2.set_xlabel("Region")
ax2.set_ylabel("Units Sold")

# Solución al error: Desactivamos el procesamiento recursivo de Matplotlib
st.pyplot(fig, clear_figure=True) 
plt.close(fig) # Cerramos la figura en memoria

# ------------------ GRÁFICA 2: TOTAL SALES ------------------
fig2, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

ax1.barh(filtered_df['NAME'], filtered_df['TOTAL SALES'])
ax1.set_title('Total Sales by Vendor')
ax1.set_xlabel("Total Sales")   # eje X = cantidad
ax1.set_ylabel("Vendor")       # eje Y = nombres
ax1.tick_params(axis='y', labelsize=6)

ax2.bar(filtered_df['REGION'], filtered_df['TOTAL SALES'])
ax2.set_title('Total Sales by Region')
ax2.set_xlabel("Region")
ax2.set_ylabel("Total Sales")

st.pyplot(fig2, clear_figure=True) 
plt.close(fig2)

# ------------------ GRÁFICA 3: AVERAGE SALES ------------------
fig3, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

ax1.barh(filtered_df['NAME'], filtered_df['SALES AVERAGE'], color='orange')
ax1.set_title('Average Sales by Vendor')
ax1.set_xlabel("Average Sales")   # eje X = cantidad
ax1.set_ylabel("Vendor")       # eje Y = nombres
ax1.tick_params(axis='y', labelsize=6)

ax2.bar(filtered_df['REGION'], filtered_df['SALES AVERAGE'], color='orange')
ax2.set_title('Sales Average by Region')
ax2.set_xlabel("Region")
ax2.set_ylabel("Average Sales")

st.pyplot(fig3, memory_fix=True, clear_figure=True) if hasattr(st, "pyplot") else st.pyplot(fig3)
plt.close(fig3)

# Create a filtered data table per specific vendor
st.subheader('By Vendor Data')
unique_vendors = df['NAME'].unique() 
# Cambié el texto para que Streamlit no se confunda con dos selectbox idénticos
selected_vendor = st.selectbox("Select vendor", unique_vendors, key="vendor_select") 

filtered2_df = df[df['NAME'] == selected_vendor] # filter by selected vendor
st.write(filtered2_df) # show the table
