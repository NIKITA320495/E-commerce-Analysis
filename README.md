# E-commerce Analysis Project

## Overview
This project provides an in-depth analysis of e-commerce data using Python, SQL, and Power BI. By utilizing advanced SQL queries for detailed analysis and creating an interactive Power BI dashboard, it uncovers valuable insights into customer behavior, sales trends, and product performance. The project was inspired by the [Target Dataset from Kaggle](https://www.kaggle.com/datasets/devarajv88/target-dataset?select=products.csv), which includes essential data about products, sales, and customer demographics.

## Table of Contents
- [Overview](#overview)
- [Dataset](#dataset)
- [Project Workflow](#project-workflow)
- [Data Preparation](#data-preparation)
- [SQL Analysis](#sql-analysis)
- [Power BI Dashboard](#power-bi-dashboard)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
- [Conclusion](#conclusion)

## Dataset
- **Source**: [Target Dataset on Kaggle](https://www.kaggle.com/datasets/devarajv88/target-dataset?select=products.csv)
- **Schema**: 
  - The dataset consists of multiple files detailing products, transactions, and customer information.
  - ![image](https://github.com/user-attachments/assets/7a797683-16d8-43c9-8d15-23eeab233d11)


## Project Workflow
1. **Data Preparation**: Converted CSV files to SQL format, enabling efficient querying and data manipulation.
2. **Advanced SQL Queries**: Executed complex SQL queries to derive insights on e-commerce metrics such as top-selling products, customer purchasing patterns, and sales trends.
3. **Data Visualization**: Created a Power BI dashboard for an intuitive, interactive exploration of insights obtained from the data.

## Data Preparation
In the initial step, raw CSV files were converted into SQL tables for easier data handling. This process involved:
- Loading the data into SQL-compatible formats.
- Cleaning and transforming data to ensure consistency and accuracy in analysis.

## SQL Analysis
This project utilizes advanced SQL querying techniques to gain actionable insights into the e-commerce dataset. Each analysis focuses on a different aspect of the business, from customer segmentation to sales performance and operational efficiency. Below are key SQL analyses conducted:

1. **Top-Selling Products and Revenue Analysis**  
   - Identified top-selling products by revenue and quantity sold, providing insights for targeted marketing and effective inventory management.

2. **Customer Segmentation and Purchase Patterns**  
   - Segmented customers based on purchase frequency and spending, helping the business identify high-value customers and understand purchasing behaviors for personalized marketing.

3. **Sales Trends and Seasonality**  
   - Conducted time-series analysis to uncover monthly, quarterly, and annual sales trends, which assists in inventory and staffing planning during peak periods.

4. **Customer Retention and Churn Analysis**  
   - Assessed customer transaction frequency to identify retention rates and churn risks, supporting the development of retention strategies for low-frequency customers.

5. **Revenue Contribution by Region**  
   - Analyzed revenue by region to create data-driven, region-specific strategies for market expansion.

6. **Impact of Discounts on Sales and Profit Margins**  
   - Evaluated the effect of discount campaigns on sales volume and overall revenue, providing insights into the profitability of discount strategies.

7. **Shipping and Order Fulfillment Timeliness**  
   - Assessed order fulfillment rates and shipping times to find logistics bottlenecks, aiming to reduce delivery delays and enhance customer satisfaction.

8. **Product Return Analysis**  
   - Analyzed return rates by category and reason for returns, helping to refine product descriptions and quality control to reduce returns.

SQL code snippets for these queries are available in the `SQL Queries` folder for easy replication and reference.

## Power BI Dashboard
The Power BI dashboard provides a user-friendly, interactive experience, making it easy to:
- View key performance indicators (KPIs) and metrics.
- Filter data by dimensions such as product category, time period, and region.
- Understand trends and patterns intuitively through visualizations.

![Dashboard Page 1](https://github.com/NIKITA320495/E-commerce-Analysis/blob/main/Dashboard/E-commerce%20dashboard1_pages-to-jpg-0001.jpg)
![Dashboard Page 2](https://github.com/NIKITA320495/E-commerce-Analysis/blob/main/Dashboard/E-commerce%20dashboard_pages-to-jpg-0002.jpg)

The Power BI report file is included in the repository.

## Technologies Used
- **Python**: For data cleaning and conversion of CSV files to SQL format.
- **SQL**: Advanced querying for in-depth data analysis.
- **Power BI**: For creating a dynamic dashboard to visualize the analysis results.

## Getting Started
To explore this project:
1. Clone the repository to your local machine.
2. Use the SQL queries provided to recreate the insights in a SQL environment.
3. Open the Power BI report file to interact with the dashboard and explore insights.

## Conclusion
This project demonstrates a comprehensive data analysis workflow using SQL for advanced querying and Power BI for visualization. The insights derived can aid in making data-driven decisions, improving customer targeting, and optimizing product and inventory management.
