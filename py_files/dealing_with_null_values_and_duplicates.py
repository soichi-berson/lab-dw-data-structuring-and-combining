#dealing with null values and duplicates.

import numpy as np
import pandas as pd 

def drop_null_id(df: pd.DataFrame) -> pd.DataFrame:
	'''
	Drop the null values of 'id'

	Input: 
    df: pd.DataFrame
    
    Output:
    Another pd.DataFrame


	'''

	df2 = df.copy()

	df2[ df2['id'].isna()==False ]

	return df2


def drop_null_gender(df: pd.DataFrame) -> pd.DataFrame:
	'''
	Drop the null values of 'gender'

	Input: 
    df: pd.DataFrame
    
    Output:
    Another pd.DataFrame


	'''

	df2 = df.copy()

	df2 = df2[ df2['gender'].isna()==False ]

	return df2



def clv_replace(df: pd.DataFrame) -> pd.DataFrame:
	'''
	The null values in 'customer lifetime value' are replaced with the mean

	Input: 
    df: pd.DataFrame
    
    Output:
    Another pd.DataFrame


	'''

	df2 = df.copy()
	#mean
	mean_customer_lifetime_value = df2['customer_lifetime_value'].mean()


	# Round off the mean to 2 decimal places.
	mean = round(mean_customer_lifetime_value, 2)
	# replace null values with the mean.

	df2['customer_lifetime_value'] = df2['customer_lifetime_value'].fillna(mean)

	print("finished 'clv_replace'")
	print("The mean value of the column {} is {}".format('customer_lifetime_value',mean))


	return df2


def drop_duplicates(df: pd.DataFrame) -> pd.DataFrame:
	'''
	The null values in 'customer lifetime value' are replaced with the mean

	Input: 
    df: pd.DataFrame
    
    Output:
    Another pd.DataFrame


	'''

	df2 = df.copy()

	df2 = df2.drop_duplicates()

	print("finished 'drop_duplicates'")
	print('The number of data before dropping duplicates is',(len(df)))
	print( 'The number of data which dropped duplicates is', len(df2))

	return df2



def deal_with_null_and_duplicates(df: pd.DataFrame) -> pd.DataFrame:
	'''
	Dealing with null values and duplicates by using four functions above.

	Input: 
    df: pd.DataFrame
    
    Output:
    Another pd.DataFrame


	'''

	df2 = df.copy()

	df2 = drop_null_id(df2)
	df2 = drop_null_gender(df2)
	df2 = clv_replace(df2)
	df2 = drop_duplicates(df2)
	


	print("finished 'deal_with_null_and_duplicates'")

	return df2

