import requests
from bs4 import BeautifulSoup
import pandas as pd

#list of states and territories, list of crime types and list of age ranges
stateList = ["Alabama", "Alaska", "American Samoa", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "District of Columbia", "Florida", "Georgia", "Guam", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Northern Mariana Islands", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Puerto Rico", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "United States Minor Outlying Islands", "Utah", "Vermont", "Virgin Islands", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]
crimeTypeList = ["Advanced Fee", "BEC/EAC", "Charity", "Civil Matter", "Confidence Fraud/Romance", "Corporate Data Breach", "Credit Card Fraud", "Crimes Against Children", "Criminal Forums", "Denial of Service/TDos", "Employment", "Extortion", "Gambling", "Government Impersonation", "Hacktivist", "Harassment/Threats of Violence", "Health Care Related", "IPR/Copyright and Counterfeit", "Identity Theft", "Investment", "Lottery/Sweepstakes/Inheritance", "Malware/Scareware/Virus", "Misrepresentation", "No Lead Value", "Non-payment/Non-Delivery", "Other", "Overpayment", "Personal Data Breach", "Phishing/Vishing/Smishing/Pharming", "Ransomware", "Re-shipping", "Real Estate/Rental", "Spoofing", "Tech Support", "Terrorism", "Social Media", "Virtual Currency" ]
ageRangeList = ["Under 20", "20 - 29", "30 - 39", "40 - 49", "50 - 59", "Over 60"]

#there are 4 years of reports we want to gather from 2017 through 2021
for year in range(17, 21):

  crimeTypeByVictimCount = {}
  crimeTypeByVictimLoss = {}
  crimeTypeBySubjectCount = {}
  crimeTypeBySubjectLoss = {}
  victimsByAgeGroup = {}

#there are 57 states and territories we want to gather data for
  for s in range(1, 58):
      #print the name of each state and the year of the report
      print(f"{stateList[s-1]} 20{year}")
      # Fetch the HTML content of the IC3.gov webpage
      url = f"https://www.ic3.gov/Media/PDF/AnnualReport/20{year}State/stats?s={s}"
      response = requests.get(url)

      # Check if the request was successful (status code 200)
      if response.status_code == 200:
          #Parse the response as json
          data = response.json()

      # Iterate over the data and crimeTypeList
      for i, (sublist, crime_type) in enumerate(zip(data[0][0], crimeTypeList)):
          # Take only the first 35 values from the sublist
          values = sublist[:34]
          # Store the values matched up with the crime type
          crimeTypeByVictimCount[crime_type] = values
      # Append the last two elements to the dictionary for social media and virtual currency
      crimeTypeByVictimCount[crimeTypeList[35]] = data[0][1][0]
      crimeTypeByVictimCount[crimeTypeList[36]] = data[0][1][1]
      # Print the title of the table
      print("Crime Type by Victim Count")
      # Create DataFrame from crimeTypeByVictimLoss dictionary
      df = pd.DataFrame.from_dict(crimeTypeByVictimCount, orient='index', columns=['Victim Count'])
      # Print the DataFrame
      print(df)
      print()

      # Iterate over the data and crimeTypeList
      for i, (sublist, crime_type) in enumerate(zip(data[0][2], crimeTypeList)):
          # Take only the first 35 values from the sublist
          values = sublist[:34]
          # Store the values matched up with the crime type
          crimeTypeByVictimLoss[crime_type] = values
      # Append the last two elements to the dictionary for social media and virtual currency
      crimeTypeByVictimLoss[crimeTypeList[35]] = data[0][3][0]
      crimeTypeByVictimLoss[crimeTypeList[36]] = data[0][3][1]
      # Print the title of the table 
      print("Crime Type by Victim Loss")
      # Create DataFrame from crimeTypeByVictimLoss dictionary
      df = pd.DataFrame.from_dict(crimeTypeByVictimLoss, orient='index', columns=['Loss Amount'])
      # Print the DataFrame
      print(df)
      print()

      # Iterate over the data and crimeTypeList
      for i, (sublist, crime_type) in enumerate(zip(data[0][4], crimeTypeList)):
          # Take only the first 35 values from the sublist
          values = sublist[:34]
          # Store the values matched up with the crime type
          crimeTypeBySubjectCount[crime_type] = values
      # Append the last two elements to the dictionary for social media and virtual currency
      crimeTypeBySubjectCount[crimeTypeList[35]] = data[0][5][0]
      crimeTypeBySubjectCount[crimeTypeList[36]] = data[0][5][1]
      # Print the title of the table 
      print("Crime Type by Subject Count")
      # Create DataFrame from crimeTypeBySubjectCount dictionary
      df = pd.DataFrame.from_dict(crimeTypeBySubjectCount, orient='index', columns=['Subject Count'])
      # Print the DataFrame
      print(df)
      print()

      # Iterate over the data and crimeTypeList
      for i, (sublist, crime_type) in enumerate(zip(data[0][6], crimeTypeList)):
          # Take only the first 35 values from the sublist
          values = sublist[:34]
          # Store the values matched up with the crime type
          crimeTypeBySubjectLoss[crime_type] = values
      # Append the last two elements to the dictionary for social media and virtual currency
      crimeTypeBySubjectLoss[crimeTypeList[35]] = data[0][7][0]
      crimeTypeBySubjectLoss[crimeTypeList[36]] = data[0][7][1]
      # Print the title of the table
      print("Crime Type by Subject Loss")
      # Create DataFrame from crimeTypeBySubjectLoss dictionary
      df = pd.DataFrame.from_dict(crimeTypeBySubjectLoss, orient='index', columns=['Loss Amount'])
      # Print the DataFrame
      print(df)
      print()

      # Iterate through each dictionary in data[1] and pair values with age ranges
      for dictionary, age_range in zip(data[1], ageRangeList):
          # Extract values from the dictionary
          values = list(dictionary.values())
          # Add the values as a list to the corresponding age range key
          victimsByAgeGroup[age_range] = values
      # Print the title of the table
      print("Victims by Age Group:")
      # Create DataFrame from victimsByAgeGroup dictionary
      df = pd.DataFrame.from_dict(victimsByAgeGroup, orient='index', columns=['Count', 'Loss Amount'])
      # Print the DataFrame
      print(df)
      print()

  else:
      print("Failed to fetch the webpage")