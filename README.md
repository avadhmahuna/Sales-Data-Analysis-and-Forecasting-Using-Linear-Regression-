Sales Data Analysis and Forecasting Using Linear 
Regression in a Flask-Based Web Application

INTRODUCTION
Include:
•Importance of sales forecasting 
•Role of mathematical modeling 
•Machine learning in prediction 
•Purpose of project 
Short Points:
•Predict future sales trends 
•Improve business decision-making 
•Web-based analytical system 
OBJECTIVES OF THE STUDY
Objectives:
1.Analyze historical sales data 
2.Apply Linear Regression 
3.Predict future sales 
4.Develop Flask dashboard 
5.Generate Excel reports 
PROBLEM STATEMENT
Explain:
•Businesses need forecasting systems 
•Existing tools are costly/complex 
•Need simple forecasting solution 
Add:
•Real-time analysis 
•User-friendly dashboard
TECHNOLOGIES USED
Add logos/screenshots if possible
Technology
Python
Flask
SQL Server
Pandas
NumPy
Scikit-learn
Purpose
Programming
Web Framework
Database
Data Processing
Numerical Computation
Machine Learning
DATABASE DESIGN
Tables Used
Users Table
users(id, first_name, last_name, email, password)
Sales Table
sales(sale_id, email_id, product_name, quantity, price, 
sale_date)
Explain:
•Primary key 
•Relationship using email
SYSTEM ARCHITECTURE
User Login
↓
SQL Server Database
↓
Data Processing (Pandas)
↓
Linear Regression Model
↓
Forecast Prediction
↓
Dashboard & Excel Report
MATHEMATICAL MODEL
Linear Regression
Where:
•y = predicted sales 
•x = time/month index 
•m = slope 
•c = intercept 
Mention:
•Least Squares Method 
•Error minimization
𝑦 = 𝑚𝑥+𝑐
IMPLEMENTATION
Include screenshots:
Login page
Dashboard
Forecast table
Excel download button
Explain:
•Flask routes 
•User authentication 
•Forecast generation 
DATA ANALYSIS
Add:
•Monthly sales table 
•Trend analysis 
IMPORTANT:
Insert graph:
•Actual Sales vs Predicted Sales 
(Line graph preferred)
RESULTS & DISCUSSION
Mention:
•Forecast successfully generated 
•Dashboard working properly 
•User-specific data handling 
•Excel export successful
LIMITATIONS
Include:
•Only linear trends supported 
•No seasonality 
•Small dataset limitations
FUTURE SCOPE
Add:
•ARIMA forecasting 
•Deep learning models 
•Mobile app integration 
•Real-time analytics 
CONCLUSION
Summary:
•Mathematical forecasting implemented successfully 
•Flask + SQL Server integration completed 
•Real-world application of Linear Regression demonstrated 
THANK YOU
