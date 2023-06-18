import numpy as np
import pandas as pd 


#gender
def clean_gender(df: pd.DataFrame) -> pd.DataFrame:
    '''
    The values of 'gender' are chanhed into only 'F','M' and 'U'
    
    Input: 
    df: pd.DataFrame
    
    Output:
    Another pd.DataFrame
    '''

    df2 = df.copy()
    
    #Change the first text in upper case.
    df2["gender"] = df2["gender"].apply(lambda x: x[0].upper() if x is not np.nan else np.nan)
    
    # Divide values into 'F','M' and nan
    df2["gender"] = df2["gender"].apply(lambda x: x if x in ["F","M"] else np.nan)
    
            
    
    return df2





#st
def clean_st(df: pd.DataFrame) -> pd.DataFrame:
    '''
    The values of 'Cali','AZ' and 'WA' are changed into 'California', 'Arizona', 'Washington', respectively
    
    Input: 
    df: pd.DataFrame
    
    Output:
    Another pd.DataFrame
    '''

    df2 = df.copy()
    
    # Change words here.
    df2["st"] = df2["st"].apply(lambda x: 'California' if x == 'Cali' else x)
    df2["st"] = df2["st"].apply(lambda x: 'Arizona' if x == 'AZ' else x)
    df2["st"] = df2["st"].apply(lambda x: 'Washington' if x == 'WA' else x)
    return df2



#education

def clean_education(df: pd.DataFrame) -> pd.DataFrame:
    '''
    The values of 'College', 'Bachelors' are chanhed into 'Bachelor'
    
    Input: 
    df: pd.DataFrame
    
    Output:
    Another pd.DataFrame
    '''
    df2 = df.copy()
    
    # Change words here.
    df2["education"] = df2["education"].apply(lambda x: 'Bachelor' if x == 'Bachelors' else x)
    df2["education"] = df2["education"].apply(lambda x: 'Bachelor' if x == 'College' else x)
    
    return df2






#clean invalid values ('gender', 'st' and 'education')


def clean_invalid_values(df: pd.DataFrame) -> pd.DataFrame:

    '''

	Clean values of 'gender','st' and 'education' using three functions above.

	Input: 
    df: pd.DataFrame
    
    Output:
    Another pd.DataFrame

    '''

    df2 = df.copy()

    df2 = clean_gender(df2)
    df2 = clean_st(df2)
    df2 = clean_education(df2)

    print("finished 'clean_invalid_values'")

    return df2
