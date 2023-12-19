# Milestone 3 - Task 2: Create a class to get information from the dataframe
# Create a DataFrameInfo class which will contain methods that generate useful information about your DataFrame.


#Some useful utility methods you might want to create that are often used for EDA tasks are:

#Describe all columns in the DataFrame to check their data types
#Extract statistical values: median, standard deviation and mean from the columns and the DataFrame
#Count distinct values in categorical columns
#Print out the shape of the DataFrame
#Generate a count/percentage count of NULL values in each column
#Any other methods you may find useful


#%%
class DataFrameInfo:
    def __init__(self) -> None:
        pass

    #Describe all columns in the DataFrame to check their data types
def check_dtypes():
    return df.info()
    
def shape(dataframe):
    print(f'The DataFrame has {dataframe.shape[1]} columns and {dataframe.shape[0]} rows.')
    return dataframe.shape
    
def column_info_df(df, column = None):
    #function that returns list of distinct values, the count and datatype of selected column. 
    # if no column is specified returns a dataframe of all colum information
    col_list = df.columns.to_list()
    list = [(x, df[x].unique(), len(df[x].unique()), df[x].dtype, df[x].isna().sum()) for x in col_list]
    list_df = pd.DataFrame(list, columns = ['Column Name', 'Distinct Values', 'Count of Distinct Values', 'Data Type', 'Count of Null Values'], index = col_list)
    if column == None:
        return list_df    
    else:
        return list_df.loc[column]


# %%
