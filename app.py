import streamlit as st
import pandas as pd
import plotly.express as px
import pymysql
# Load CSV files
customers = pd.read_csv('datasets/customers.csv')
orders = pd.read_csv('datasets/orders.csv')
products = pd.read_csv('datasets/products.csv')
order_items = pd.read_csv('datasets/order_items.csv')
payments = pd.read_csv('datasets/payments.csv')
geolocation = pd.read_csv('datasets/geolocation.csv')
sellers = pd.read_csv('datasets/sellers.csv')

########################Functions################################
db=pymysql.connect(
    host="localhost",
    user="root",
    password="123456",
    database="ecommerce"
)
cur=db.cursor()
def get_data(query):
    cur.execute(query)
    data=cur.fetchall()
    df=pd.DataFrame(list(data),columns=[i[0] for i in cur.description])
    return df
def count_plot(data, column, title):
    # Ensure the column is treated as a categorical variable
    data[column] = data[column].astype(str)
    
    # Count the occurrences of each category
    counts = data[column].value_counts()
    
    # Get the top 10 categories
    top_10 = counts.head(10)
    
    # Create a DataFrame for the top 10 categories
    top_10_df = top_10.reset_index()
    top_10_df.columns = [column, 'count']
    
    # Generate the count plot
    fig = px.bar(top_10_df, x=column, y='count', title=title)
    
    return fig











#########################Streamlit################################
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
    fig=px.pie(df, names='customer_state', title='top 10 Customer State Distribution')
    st.plotly_chart(fig)
    fig=count_plot(df, 'customer_city', 'top 10 Customer City Distribution')
    st.plotly_chart(fig)
    fig=count_plot(df,'customer_state','top 10 Customer State Distribution')
    st.plotly_chart(fig)

    
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
####################################33
df1=get_data("""select products.product_category , round(sum(payments.payment_value),2) as total_sales
from products join order_items  
on products.product_id = order_items.product_id 
join payments on payments.order_id = order_items.order_id  
group by products.product_category""")
# Sort by total_sales and get the top 10
df1 = df1.sort_values(by='total_sales', ascending=False).head(10)
# Generate the plot
fig = px.bar(df1, x='product_category', y='total_sales', title='Top 10 Product Categories by Total Sales')
st.plotly_chart(fig)
############################################
df2=get_data("""select count(customer_unique_id) as customer_count, customer_state from customers group by customer_state""")
fig= px.bar(df2,x="customer_state",y="customer_count",title="Total customers in each state")
st.plotly_chart(fig)
############################################
df3=get_data("""select count(order_id),monthname(order_purchase_timestamp) as months from orders where order_purchase_timestamp between '2018-01-01' and '2018-12-31' group by months """)
df3=df3.sort_values(by="count(order_id)",ascending=False)
fig= px.bar(df3,x="months",y="count(order_id)",title="Total orders in each month of 2018")
st.plotly_chart(fig)
############################################
df4=get_data("""with count_per_order as (select orders.order_id ,orders.customer_id , count(order_items.order_id) as OC
from orders join order_items on orders.order_id = order_items.order_id
group by orders.order_id,orders.customer_id) 

select customers.customer_city , round(AVG(count_per_order.OC),2) from
customers join count_per_order on customers.customer_id= count_per_order.customer_id group by customers.customer_city;
""")
df4.columns=["customer_city","average_order_count"]
df4=df4.sort_values(by="average_order_count",ascending=False).head(10)
fig=px.bar(df4,x="customer_city",y="average_order_count",title="Top 10 cities with highest average order count")
st.plotly_chart(fig)
