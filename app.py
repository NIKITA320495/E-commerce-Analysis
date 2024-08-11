import streamlit as st
import pandas as pd
import plotly.express as px

# Load CSV files
customers = pd.read_csv('datasets/customers.csv')
orders = pd.read_csv('datasets/orders.csv')
products = pd.read_csv('datasets/products.csv')
order_items = pd.read_csv('datasets/order_items.csv')
payments = pd.read_csv('datasets/payments.csv')
geolocation = pd.read_csv('datasets/geolocation.csv')
sellers = pd.read_csv('datasets/sellers.csv')

# Streamlit app
st.title('E-commerce Dashboard')

# Dropdown menu for file selection
options = st.selectbox(
    'Select a dataset:',
    ['customers', 'orders', 'products', 'order_items', 'payments', 'geolocation', 'sellers']
)
st.markdown(
    """
    <style>
    .container {
        display: flex;
        flex-direction: row;
        justify-content: flex-start;
    }
    .pie-chart {
        width: 100%;
        position: relative;
        margin-right: 10px;
        
    }
    .data-preview {
        width: 70%;
    }
    </style>
    """,
    unsafe_allow_html=True
)
# Display data based on selection
if options == 'customers':
    df = customers
    fig=px.pie(df, names='customer_state', title='Customer State Distribution')
    st.markdown('<div class="pie-chart">', unsafe_allow_html=True)
    st.plotly_chart(fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
elif options == 'orders':
    df = orders
elif options == 'products':
    df = products
elif options == 'order_items':
    df = order_items
elif options == 'payments':
    df = payments
elif options == 'geolocation':
    df = geolocation
elif options == 'sellers':
    df = sellers

# Display the DataFrame in Streamlit
st.write(f'Data from {options} dataset')
with st.expander("Data Preview"):
        st.markdown(
            """
            <div style='border-bottom: 4px solid lightpink;'>
                <style>
                .stTable { border-bottom:  4px solid lightpink; }
                </style>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.dataframe(df)
