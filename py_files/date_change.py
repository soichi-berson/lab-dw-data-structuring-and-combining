# Change the type of date

def date_type(df:pd.DataFrame) -> pd.DataFrame:

    '''

    This function change the date types into datetime
    Input: 
    df: pd.DataFrame
    
    Output:
    Another pd.DataFrame

    '''

    df2 = df.copy()
    df2['effective_to_date'] = pd.to_datetime(df2['effective_to_date'], errors='coerce')
    print('date type was changed')

    return df2




# Extract each month
def extract_mt(df:pd.DataFrame, l: list = []) -> list:

    '''

    This function extraxts each month from the column of datetime and create a list.
    Input: 
    df: pd.DataFrame
    l : list
    
    Output:
    Another list

    '''
    df2 = df.copy(0)

    l = df2["effective_to_date"].apply(lambda x: x.month)

    return l 





