import requests
from bs4 import BeautifulSoup
import pandas as pd

# Initialize an empty list to store table data
all_table_data = []

# Loop through the states from 1 to 57 which includes 50 states + add. territories
for state in range(1, 58):
    # Construct the URL for each state
    url = f'https://www.ic3.gov/Media/PDF/AnnualReport/2017State/StateReport.aspx#?s={state}'

    # Send a GET request to the webpage
    response = requests.get(url)

    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all tables on the webpage
    tables = soup.find_all('table')

    # Initialize an empty list to store table data for this state
    table_data = []

    # Iterate over each table
    for table in tables:
        # Extract data from each row
        rows = table.find_all('tr')
        for row in rows:
            # Extract data from each cell
            cells = row.find_all(['th', 'td'])
            row_data = [cell.text.strip() for cell in cells]
            table_data.append(row_data)

    # Append table data for this state to the list of all table data
    all_table_data.append(table_data)

# Convert all table data into a DataFrame
dfs = [pd.DataFrame(table_data) for table_data in all_table_data]

# Print or manipulate the DataFrames as needed
for state, df in enumerate(dfs, start=1):
    print(f"State {state}:")
    print(df)
    print()