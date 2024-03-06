import pandas as pd

def victimCount():
    df = pd.read_csv('./csv_files/crimeTypeByVictimCount.csv')
    victimCountMax = df.sort_values('Victim Count').tail()
    print(f"\nTop 5 crime types by victim count in the US from 2017-2021 \n{victimCountMax}\n")
    victimCount2021 = df[df['Year'] == 2021].sort_values('Victim Count').tail()
    print(f"Total victim count by year \n{victimCount2021}\n")
"""
    victimCountMin = df.sort_values('Victim Count').head()
    print(f"Bottom 5 crime types by victim count in the US from 2017-2021 \n{victimCountMin}\n")
    victimCountMax2021 = df[df['Year'] == 2021].sort_values('Victim Count').tail()
    print(f"Top 5 crime types by victim count in the US in 2021 \n{victimCountMax2021}\n")
    victimCountMax2020 = df[df['Year'] == 2020].sort_values('Victim Count').tail()
    print(f"Top 5 crime types by victim count in the US in 2020 \n{victimCountMax2020}\n")
    victimCountMax2019 = df[df['Year'] == 2019].sort_values('Victim Count').tail()
    print(f"Top 5 crime types by victim count in the US in 2019 \n{victimCountMax2019}\n")
    victimCountMax2018 = df[df['Year'] == 2018].sort_values('Victim Count').tail()
    print(f"Top 5 crime types by victim count in the US in 2018 \n{victimCountMax2018}\n")
    victimCountMax2017 = df[df['Year'] == 2017].sort_values('Victim Count').tail()
    print(f"Top 5 crime types by victim count in the US in 2017 \n{victimCountMax2017}\n")
"""