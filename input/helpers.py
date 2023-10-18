import pandas as pd
import numpy as np
from sodapy import Socrata

def get_rat_requests(dataset_id):
    '''
    Retrieves all rat-related requests from 2010-present from the NYC Open data portal. 
    
    Inputs: None
    Returns: pandas DataFrame of all rat-related 311 requests (43 columns, 'unique_key' as unique identifier)
    '''    
    # connect to open data portal and set high timeout limit
    client = Socrata("data.cityofnewyork.us", None)

    # create query for 311 requests that met one of 6 criteria to be considered rat-related
    rat_complaints_query = '''SELECT *
                                WHERE (
                                    (complaint_type == 'School Maintenance' AND descriptor == 'Rodents/Mice') OR
                                    (complaint_type == 'Food Establishment' AND descriptor == 'Rodents/Insects/Garbage') OR
                                    (complaint_type == 'Rodent' AND (descriptor == 'Rat Sighting' OR descriptor == 'Signs of Rodents')) OR
                                    (complaint_type == 'Maintenance or Facility' AND descriptor == 'Rodent Sighting') OR
                                    (complaint_type == 'Dead Animal' AND descriptor == 'Rat or Mouse') OR
                                    (complaint_type == 'UNSANITARY CONDITION' AND descriptor == 'PESTS')
                                    )
                                    AND date_trunc_y(created_date) != "2009"
                                LIMIT 1000000'''

    rat_complaints_json = client.get(dataset_id, 
                                query= rat_complaints_query)

    # read in results as a dataframe
    df = pd.DataFrame.from_records(rat_complaints_json)

    # create new date columns
    df['created_date_dt'] = pd.to_datetime(df['created_date'])
    df.loc[:, 'date'] = df.loc[:,'created_date_dt'].dt.date
    df.loc[:, 'week'] = df.loc[:,'created_date_dt'].dt.isocalendar().week
    df.loc[:, 'month'] = df.loc[:,'created_date_dt'].dt.month
    df.loc[:, 'year'] = df.loc[:,'created_date_dt'].dt.isocalendar().year
    
    return df
    
def socrata_api_query(dataset_id):
    client = Socrata("data.cityofnewyork.us", None)
    client.timeout = 1000
    results = client.get(dataset_id, limit=500000)
    opendata_df = pd.DataFrame.from_records(results)
    return opendata_df