import streamlit as st
import pandas as pd

# Título principal del Dashboard
st.title("Sales Analysis Data Dashboard")

# Carga de datos
df = pd.read_excel('sellers.xlsx')

# 1. TABLA FILTRADA POR REGIÓN
st.subheader('By Region Datatable')

unique_region = df['REGION'].unique().tolist()
unique_region.insert(0, "All")
selected_region = st.selectbox("Select region", unique_region, key="region_select")

if selected_region == "All":
    filtered_df = df
else:
    filtered_df = df[df['REGION'] == selected_region]

st.write(filtered_df)

# 2. SECCIÓN DE GRÁFICOS (MÁS SIMPLE Y SIN MATPLOTLIB)
st.subheader('Sales Analysis')

# Gráficos de Unidades Vendidas
st.markdown("### Units Sold")
st.bar_chart(data=filtered_df, x='NAME', y='SOLD UNITS')
st.bar_chart(data=filtered_df, x='REGION', y='SOLD UNITS')

# Gráficos de Ventas Totales
st.markdown("### Total Sales")
st.bar_chart(data=filtered_df, x='NAME', y='TOTAL SALES')
st.bar_chart(data=filtered_df, x='REGION', y='TOTAL SALES')

# Gráficos de Promedio de Ventas
st.markdown("### Sales Average")
st.bar_chart(data=filtered_df, x='NAME', y='SALES AVERAGE')
st.bar_chart(data=filtered_df, x='REGION', y='SALES AVERAGE')

# 3. TABLA FILTRADA POR VENDEDOR específico
st.subheader('By Vendor Data')
unique_vendors = df['NAME'].unique()
selected_vendor = st.selectbox("Select vendor", unique_vendors, key="vendor_select")

filtered2_df = df[df['NAME'] == selected_vendor]
st.write(filtered2_df)
