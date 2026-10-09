Café Sales Data Cleaning & Analysis

A data cleaning and exploratory analysis project using Python and Pandas on a deliberately messy café sales dataset.

The main goal of this project was to demonstrate a practical data-cleaning workflow: identifying inconsistent values, handling missing data, reconstructing recoverable financial values, validating the cleaned dataset, and performing a focused exploratory analysis.

Project Overview

The original dataset contains 10,000 café transaction records with information about products, quantities, prices, payment methods, locations, and transaction dates.

The dataset contains various data-quality issues, including:

Missing values
ERROR and UNKNOWN values
Numeric values stored as strings
Invalid or missing dates
Missing financial values
Inconsistent data requiring validation

Rather than simply removing incomplete records, this project focuses on identifying which values can be safely recovered from the available data and which should remain missing.

Dataset

Source: Dirty Cafe Sales Dataset

The dataset contains the following columns:

Column	Description
Transaction ID	Unique transaction identifier
Item	Product purchased
Quantity	Number of items purchased
Price Per Unit	Price of one item
Total Spent	Total transaction amount
Payment Method	Payment method used
Location	Transaction location
Transaction Date	Date of the transaction
Tools & Technologies
Python
Pandas
NumPy
Matplotlib
Jupyter Notebook
VS Code
Project Workflow

The project is divided into two main stages:

1. Data Cleaning & EDA

The cleaning_data_and_eda.ipynb notebook contains the initial data inspection, exploratory analysis, data cleaning, and validation process.

The cleaning process included:

Handling invalid categorical values

ERROR and UNKNOWN values in the Item column were converted to missing values rather than being treated as valid products.

Converting numeric columns

The following columns were converted from strings to numeric values:

Quantity
Price Per Unit
Total Spent

Invalid values were converted to missing values using errors="coerce".

Converting dates

Transaction Date was converted to Pandas datetime format, allowing the data to be analyzed by month.

Recovering missing financial values

The dataset contains a logical relationship between the financial columns:

Quantity × Price Per Unit = Total Spent

Where two of these three values were available, the missing value could be safely calculated.

For example:

Total Spent = Quantity × Price Per Unit

or:

Quantity = Total Spent / Price Per Unit

This allowed recoverable values to be restored without making arbitrary assumptions.

Handling unrecoverable values

Some records contained insufficient information to reconstruct missing financial values.

These values were intentionally left missing rather than being replaced with averages or guesses.

Missing product names were also not inferred when the available information was insufficient to determine the correct product reliably.

Data Validation

After cleaning, the dataset was checked for:

Remaining missing values
Invalid ERROR / UNKNOWN values
Financial consistency
Duplicate records
Unique transaction IDs
Valid numeric values
Valid transaction dates

Of the 10,000 records, 9,942 transactions contained complete financial information after recoverable values were reconstructed.

2. Data Analysis

The data_analysis.ipynb notebook contains the final focused analysis and visualizations.

The analysis was intentionally kept concise and focused on several meaningful business questions.

Product Performance

Product-level performance was analyzed using:

Quantity sold
Revenue generated

Coffee had the highest recorded quantity sold among the products, with 3,534 units.

A revenue-share visualization was also created to compare the contribution of each product to total recorded revenue.

Payment Method

The frequency of payment methods was analyzed.

The three recorded payment methods were:

Digital Wallet
Credit Card
Cash

Digital Wallet was the most frequently recorded payment method, with 2,291 transactions.

Monthly Revenue

Transaction revenue was grouped by month to examine changes in recorded revenue throughout the year.

Monthly Transaction Count

The number of transactions was grouped by month to identify periods with higher or lower transaction activity.

October had the highest recorded transaction count with 838 transactions, while February had the lowest with 727 transactions.

Project Structure
cafe_sales/
│
├── dirty_cafe_sales.csv
├── cleaned_dataset.csv
├── cleaning_data_and_eda.ipynb
├── data_analysis.ipynb
└── README.md
Key Skills Demonstrated

This project demonstrates practical skills in:

Importing and inspecting raw CSV data
Exploratory Data Analysis
Identifying data-quality problems
Handling missing and invalid values
Converting data types
Recovering logically derivable values
Validating relationships between columns
Grouping and aggregating data with Pandas
Creating visualizations with Matplotlib
Producing a cleaned dataset
Documenting a reproducible data-cleaning workflow
Limitations

The dataset contains a significant amount of missing information, so some metrics represent only the available recorded values.

Values that could not be reliably reconstructed were intentionally left missing rather than replaced with assumptions.

The dataset also covers only one year, so the time analysis focuses on monthly patterns rather than year-over-year trends.

Conclusion

This project demonstrates how messy transactional data can be transformed into a cleaner and more usable dataset while preserving data integrity.

The main focus was on defensible data cleaning and validation, followed by a concise exploratory analysis of product performance, payment methods, revenue, and transaction activity.