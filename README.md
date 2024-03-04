# Python_Scrape_Tables
Python script to scrape IC3 annual report table data for each state and additional US territories. 

The dataset that I will be using for my project can be found here: https://www.ic3.gov/Media/PDF/AnnualReport/2017State/StateReport.aspx#?s=1. This dataset is published by The IC3(Internet Crime Complaint Center). The dataset is made up of several tables of various cyber attack data that is published per state per year. This data will be scraped and stored in a csv. Stretch goal would be to store data in a MySQL database. The data available in each table per state are Crime Type by Victim Count, Crime Type by Victim Loss, Crime Type by Subject Count, Crime Type by Subject Loss, and Victims by Age Group. Within each of these tables are columns for Crime Type and Subject Count, Crime Type and Loss Amount, Crime Type and Victim Count and Age Range Count and Amount Loss.

1. What is the relationship between the number of and types of attacks and where they occurred when comparing 2019 and 2020? How does 2020 compare to 2021? 

2. Which US states had the greatest number of cyber attacks between 2017 and 2021 and which had the least? What is the relationship between those specific states and the types of cyber attacks or the total amount of dollars lost?

3. Can we predict which states will have the greatest number of attacks or dollars lost and which will have the least? This will require using 2023 data that should be available before the end of February. If not then I can use 2017-2021 to see if a model can be used to predict what happened in 2022. 

Bonus Questions: What is the relationship between total number of cyber attacks and average education level in each state or the population density of each state? Is there a similar relationship between age group and education level and population density of each state?