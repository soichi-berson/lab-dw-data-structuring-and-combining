#customer_lifetime_value

def clean_clv(df: pd.DataFrame) -> pd.DataFrame:
    '''
    The percentage(%) of values are removed and the tyoe is changed into numerical type. 
    
    Input: 
    df: pd.DataFrame
    
    Output:
    Another pd.DataFrame
    '''
    df2 = df.copy()
    
    # remove '%'
    df2["customer_lifetime_value"] = df2["customer_lifetime_value"].apply(lambda x: x[: -1] if x is not np.nan else np.nan)
    
    
    #to change values into numerical ones
    df2["customer_lifetime_value"] = pd.to_numeric(df2['customer_lifetime_value'], errors='coerce')
    
    return df2





#number_of_open_complaints

def clean_noc(df: pd.DataFrame) -> pd.DataFrame:
    '''
    '/0/00' of values is removed. 
    
    Input: 
    df: pd.DataFrame
    
    Output:
    Another pd.DataFrame
    '''
    df2 = df.copy()
    
    #get the first digit
    df2["number_of_open_complaints"] = df2["number_of_open_complaints"].apply(lambda x: int(x[0]) if x is not np.nan else np.nan)
    
    #change float type into int64 type
    df2["number_of_open_complaints"] = pd.array(df2["number_of_open_complaints"], dtype=pd.Int64Dtype())
    
    

    return df2





# format data types
def fomatting_data_types(df: pd.DataFrame) -> pd.DataFrame:

    '''

    This function formats the data types of 'customer_lifetime_value' and 'number_of_open_complaints'
    Input: 
    df: pd.DataFrame
    
    Output:
    Another pd.DataFrame

    '''

    df2 = df.copy()

    df3 = clean_clv(df2)
    data = clean_noc(df3)

    print("finished 'fomatting_data_types'")


    return data 
