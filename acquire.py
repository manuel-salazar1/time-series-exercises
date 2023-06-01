# IMPORTS
import pandas as pd
import requests
import math
import os


# Sometimes I forget what is in each file, so here is a reminder

def acquire_info():
    '''
    Need to know what is in here?
    '''
    print(f'''This file houses the following functions:
get_germany_data()
get_swapi_data(endpoint)''')






# ACQUIRING GERMAN ENERGY DATA

def get_germany_data(filename="opsd_germany_daily.csv"):
    """
    This function will:
    - Check local directory for csv file
        - return if exists
    - If csv doesn't exists:
        - create a df
        - write df to csv
    - Output zillow df
    """
    if os.path.exists(filename):
        df = pd.read_csv(filename, index_col=0) 
        print('Found CSV')
        return df
    
    else:
        url = "https://raw.githubusercontent.com/jenfly/opsd/master/opsd_germany_daily.csv"
        df = pd.read_csv(url)
        #want to save to csv
        df.to_csv(filename)
        print('Creating CSV')
        return df






# STAR WARS DATA WE WON'T BE USING

def get_swapi_data(endpoint):
    '''
    
    '''
    
    base_url = "https://swapi.dev/api/"
    
    if os.path.isfile(f"{endpoint}.csv"):
        df = pd.read_csv(f"{endpoint}.csv", index_col=0)
    else:
        response = requests.get(base_url + endpoint + "/")
        data = response.json()
        df = pd.DataFrame(data['results'])
        
        while data['next'] != None:
            print(data['next'])
            response = requests.get(data['next'])
            data = response.json()
            df = pd.concat([df, pd.DataFrame(data['results'])], ignore_index=True)
        df.to_csv(f'{endpoint}.csv')
        
    return df





