import pandas as pd

airport_path = 'file:/datasets/AirportForZipsUSA_Augmented.csv'
bostonZip_path = '/datasets/boston_zip.csv'
laZip_path = '/datasets/la_zip.csv'
nycZip_path = '/datasets/nyc_zip.csv'

SUBSET = True # False if you are using the entire datasets, True otherwise

CITY = 'LA'
trTimeThresh = 10
min_sup_fixed = 1095
max_tree_length = 30

if CITY == 'LA':
    zips_to_filter = set(str(x) for x in pd.read_csv(laZip_path)['zip'].tolist())
elif CITY == 'BO':
    zips_to_filter = set(str(x) for x in pd.read_csv(bostonZip_path)['zip'].tolist())
elif CITY == 'NYC':
    zips_to_filter = set(str(x) for x in pd.read_csv(nycZip_path)['zip'].tolist())
