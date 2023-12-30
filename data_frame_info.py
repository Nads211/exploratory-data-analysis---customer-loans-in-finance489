# Milestone 3 - Task 2: Create a class to get information from the dataframe
# Create a DataFrameInfo class which will contain methods that generate useful information about your DataFrame.


#Some useful utility methods you might want to create that are often used for EDA tasks are:

#Describe all columns in the DataFrame to check their data types
#Extract statistical values: median, standard deviation and mean from the columns and the DataFrame



#Any other methods you may find useful


#%%
import pandas as pd

class DataFrameInfo:
    """    
    def check_dtypes(self, dataframe):

    shape(self, dataframe, print = None):

    column_list(self, dataframe, print = None)

    def column_info_dataframe(self, dataframe, column = None):
    
    filter_column_info_dataframe(self, dataframe, column_to_filter, vaules_to_filter: list)

    def get_null_percentage(self, dataframe)
    
    column_list(self, dataframe)
    
    """


    #Describe all columns in the DataFrame to check their data types
    def check_dtypes(self, dataframe):
        return dataframe.info()

    #Print out the shape of the DataFrame    
    def shape(self, dataframe, print = None):
        if print == None:
            return dataframe.shape
        else:
            print(f'The DataFrame has {dataframe.shape[1]} columns and {dataframe.shape[0]} rows.')
    
    #get column list
    def column_list(self, dataframe, print = None):
        col_list = dataframe.columns.to_list()
        if print == None:
            return col_list
        else:
            print(f'The DataFrame has column names: {col_list}.')
        

    #Count distinct values in categorical columns    
    def column_info_dataframe(self, dataframe, column = None):
        #function that returns list of distinct values, the count and datatype of selected column. 
        # if no column is specified returns a dataframe of all colum information
        col_list = dataframe.columns.to_list()
        list = [(x, dataframe[x].unique(), len(dataframe[x].unique()), dataframe[x].dtype, dataframe[x].isna().sum()) for x in col_list]
        list_dataframe = pd.DataFrame(list, columns = ['Column Name', 'Distinct Values', 'Distinct Values Count', 'Data Type', 'Null Values Count'], index = col_list)
        if column == None:
            return list_dataframe    
        else:
            return list_dataframe.loc[column]
    
    #filter the above info dataframe
    def filter_column_info_dataframe(self, dataframe, column_to_filter, vaules_to_filter: list):
        column_info = self.column_info_dataframe(dataframe, column = None)
        filtered_df = column_info.loc[column_info[column_to_filter].isin(vaules_to_filter)]
        return filtered_df

    #Generate a count/percentage count of NULL values in each column
    def get_null_percentage(self, dataframe): #takes a dataframe and outputs a dataframe of column names and their percentage of null values
        null_percentage_dict = {}
        for col in dataframe.columns:
            percentage = dataframe[col].isnull().sum()/len(dataframe)*100
            null_percentage_dict[col] = round(percentage, 2) #for each key=col, value=rounded percentage
        null_percentage_dict = sorted(null_percentage_dict.items(), key=lambda x:x[1], reverse=True) # sort with highest %. But returns a list of tuples
        return pd.DataFrame(null_percentage_dict, columns=['Column Name', 'Null Values %']) #display as dataframe for neatness
    # %%
    def numeric_columns(self, dataframe):
        numeric_cols = []
        for col in dataframe.columns:
            #print(df[col].dtype)
            if dataframe[col].dtype in ['int', 'int32', 'int64', 'float', 'float32', 'float64']:
            #    print(col)
                numeric_cols.append(col)
        return numeric_cols
    
    def get_skewed_columns(self, dataframe, col_list, threshold):
        skewed_cols = {}
        for col in col_list:
            skew = dataframe[col].skew()
            if abs(skew) > threshold:
                skewed_cols[col] = round(skew, 2)
        return skewed_cols
    

 