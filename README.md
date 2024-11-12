# E-commerce Analysis Project

## Overview
This project provides an in-depth analysis of e-commerce data using Python, SQL, and Power BI. By utilizing advanced SQL queries for detailed analysis and creating an interactive Power BI dashboard, it uncovers valuable insights on customer behavior, sales trends, and product performance. This project was inspired by the [Target Dataset from Kaggle](https://www.kaggle.com/datasets/devarajv88/target-dataset?select=products.csv), which includes essential data about products, sales, and customer demographics.

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
  - ![Schema](https://github.com/user-attachments/assets/345798b9-3e98-435f-9428-d20b965b778e)

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
   - By querying the transaction and product tables, we identified the top-selling products by revenue and quantity sold. These insights enable targeted marketing for popular items and effective inventory management.

2. **Customer Segmentation and Purchase Patterns**  
   - Segmented customers based on their purchase frequency and total spending. This segmentation allows the business to identify high-value customers and understand their purchasing patterns, informing personalized marketing strategies and customer retention efforts.

3. **Sales Trends and Seasonality**  
   - Conducted a time-series analysis on transaction data to uncover monthly, quarterly, and annual sales trends. Seasonal spikes in sales were identified, enabling strategic planning for inventory and staffing during peak periods.

4. **Customer Retention and Churn Analysis**  
   - Analyzed customer transaction frequency to assess retention rates and identify churn. Customers with low transaction frequencies were flagged as potential churn risks, guiding retention strategies.

5. **Revenue Contribution by Region**  
   - Using geographic information from transaction records, we calculated the revenue contribution by region. This breakdown allows for the development of region-specific strategies to maximize market penetration.

6. **Impact of Discounts on Sales and Profit Margins**  
   - Assessed the effectiveness of discount campaigns by comparing sales data before, during, and after promotional periods. This analysis showed the impact of discounts on sales volume and overall revenue, providing insights into the profitability of discount strategies.

7. **Shipping and Order Fulfillment Timeliness**  
   - Analyzed order fulfillment rates and average shipping times to identify bottlenecks in the delivery process. This analysis revealed areas for improvement in logistics, with the goal of reducing delivery times and increasing customer satisfaction.

8. **Product Return Analysis**  
   - Evaluated return rates by product category and reason for returns. This analysis highlighted products with high return rates, enabling the business to adjust product descriptions, quality checks, or customer expectations to reduce returns.

SQL code snippets for these queries are available in the `SQL Queries` folder for easy replication and reference.

## Power BI Dashboard
The Power BI dashboard provides a user-friendly and interactive experience, making it easy to:
- View key performance indicators (KPIs) and metrics.
- Filter data by dimensions such as product category, time period, and region.
- Understand trends and patterns intuitively through visualizations.

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
