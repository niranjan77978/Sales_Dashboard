Retail Sales Analysis & Business Intelligence Dashboard
Project Overview

This project demonstrates a complete, end-to-end data analysis workflow. Starting with a raw and messy retail sales dataset (retail_store_sales.csv), the goal is to perform rigorous data cleaning and preparation using Python, and then build a dynamic, interactive business intelligence dashboard in Power BI.

The final dashboard provides key insights into sales performance, product trends, and customer behavior, enabling stakeholders to make informed, data-driven decisions.
Part 1: Data Cleaning & Preparation with Python

The initial dataset contained several common issues that made it unsuitable for direct analysis. The Python script data_cleaning.py was used to address these problems systematically.

Tools Used: Python, Pandas Library
Cleaning Steps Performed:

    Loading the Data: The initial retail_store_sales.csv was loaded into a Pandas DataFrame.

    Handling Missing Values: A multi-step strategy was employed:

        Discount Applied: Missing boolean values were logically imputed as False, assuming no discount was applied if not specified.

        Price, Quantity, and Total Spent: Missing numerical values were intelligently calculated based on the other two available columns (e.g., if Price was missing, it was calculated as Total Spent / Quantity).

        Essential Information: Rows where critical data like Item or Customer ID were missing were dropped to ensure data integrity.

    Correcting Data Types:

        Transaction Date: The date column was stored as an Excel serial number (e.g., 45390.00). This was converted into a standard, human-readable YYYY-MM-DD format.

        Numeric Columns: Ensured that Quantity, Price Per Unit, and Total Spent were correctly formatted as numeric types.

    Removing Inconsistencies:

        Invalid Transactions: Rows with negative Quantity or a Price Per Unit of zero were removed as they represent invalid or returned transactions not suitable for sales analysis.

        Duplicate Records: All duplicate rows were identified and dropped to prevent inflated metrics.

        Unnamed Index Column: The script checks for and removes the common 'Unnamed: 0' column that can be created when reading CSV files.

    Data Validation:

        A final check was performed to ensure the Total Spent column was consistent with Price Per Unit multiplied by Quantity, correcting any floating-point inaccuracies.

    Exporting Clean Data:

        The thoroughly cleaned DataFrame was saved to a new file, cleaned_retail_sales.csv. The index=False parameter was used during saving to prevent creating a new unnamed index column.

Part 2: Dashboard Creation in Power BI

The clean and reliable cleaned_retail_sales.csv file was loaded into Power BI to create the "Retail Store Sales Dashboard".
Dashboard Visualizations

The following charts were created to answer key business questions:

    Summary Cards

        Chart Type: Card

        Metrics Displayed: Average of Total Spent, Maximum of Total Spent, and Sum of Total Spent.

        Business Question: What are the total sales, and what is the typical and maximum transaction value?

    Sales Trend by Month

        Chart Type: Line Chart

        Columns Used: Axis: Transaction Date (Month), Values: Total Spent

        Business Question: How are sales trending on a monthly basis?

    Top 5 Items by Total Spent

        Chart Type: Horizontal Bar Chart

        Columns Used: Axis: Total Spent, Values: Item

        Business Question: Which specific products generate the most revenue?

    Sales by Payment Method

        Chart Type: Donut Chart

        Columns Used: Legend: Payment Method, Values: Total Spent

        Business Question: What is the breakdown of sales across different payment methods?

    Sales by Discount Applied

        Chart Type: Vertical Bar Chart

        Columns Used: X-Axis: Discount Applied, Y-Axis: Total Spent

        Business Question: How much revenue is generated from discounted vs. non-discounted sales?

Final Dashboard

The final result is a user-friendly, interactive dashboard titled "Retail Store Sales Dashboard". It features an interactive slicer for Category, allowing stakeholders to filter all visualizations simultaneously and drill down into specific areas of interest to uncover actionable insights.

![Retail Store Sales Dashboard]([https://raw.githubusercontent.com/niranjan77978/Sales_Dashboard/main/Dashboard.png](https://github.com/niranjan77978/Sales_Dashboard/blob/main/Images/Dashboard.png))
