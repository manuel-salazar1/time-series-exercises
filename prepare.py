# IMPORTS   
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



# Sometimes I forget what functions are in each file so here is a reminder

def prep_info():
    '''
    Need to know what is in here?
    '''
    print(f'''This file houses the following functions:
superstore_prep()
opsd_germ_prep()''')




# Prep superstore CSV

def superstore_prep(df):
    '''
    Input: df
    Output: df with updates to sale_date, added month/dayofweek/weekday and sales_total columns
    '''
    # dropping time since it is the exact same for each row
    df.sale_date = df.sale_date.str.replace(' 00:00:00 GMT', '')
    # format date to display yyyy-mm-dd
    df.sale_date = pd.to_datetime(df.sale_date, format='%a, %d %b %Y')
    # reset index to have datetime
    df = df.set_index('sale_date')
    df = df.sort_index()
    # add month and day of week columns
    df['month'] = df.index.month
    df['day_of_week'] = df.index.day_of_week
    df['weekday'] = df.index.day_name()
    # create column for sales_total using sale_amount and item_price
    df['sales_total'] = df.sale_amount * df.item_price
    return df





# Prep germany energy CSV

def opsd_germ_prep(df):
    '''
    locate file here if you don't have it saved already
    url = "https://raw.githubusercontent.com/jenfly/opsd/master/opsd_germany_daily.csv"
    df = pd.read_csv(url)
    Input: df
    Output: df with updates to date, added month/year, filled nulls
    '''
    # convert column names to lower
    df.columns = df.columns.str.lower()
    # convert date column to datetime format
    df.date = pd.to_datetime(df.date, format='%Y-%m-%d')
    # set index to datetime
    df = df.set_index('date')
    df = df.sort_index()
    # add month and year column to df
    df['month'] = df.index.month
    df['year'] = df.index.year
    # fill nulls with 0
    df = df.fillna(0)
    return df

















