#
class DataFrameTransform:

    '''
    This class is used to apply transformations to the dataframe in regards to imputing or removing columns with missing data.
    '''

    def remove_null_columns(self, dataframe, column_name):

        '''
        This method is used to remove column(s) containing excess null or missing values.

        Parameters:
            dataframe (pd.dataframe): The dataframe to which this method will be applied.
            Column_name: the name(s) of columns that will be removed.

        Returns:
            dataframe (pd.dataframe): The updated dataframe.
        '''

        dataframe.drop(column_name, axis=1, inplace=True)
        return dataframe

    def remove_null_rows(self, dataframe, column_name):

        '''
        This method is used to remove rows within the dataframe where data points from a specified column are null.

        Parameters:
            dataframe (pd.dataframe): The dataframe to which this method will be applied.
            column_name: The name of the column which will be checked for null values, these rows will be removed.

        Returns:
            dataframe (pd.dataframe): The updated dataframe.
        '''
        dataframe.dropna(subset=column_name, inplace=True)
        return dataframe
    
    def impute_med(dataframe, column):
        dataframe[column] = dataframe[column].fillna(dataframe[column].median())
        return dataframe
    
    def impute_mean(dataframe, column):
        dataframe[column] = dataframe[column].fillna(dataframe[column].mean())
        return dataframe
    
    def impute_mode(dataframe, column):
        dataframe[column] = dataframe[column].fillna(dataframe[column].mode()[0]) #must index 0 here as column is categorical type so .mode() returns a pandas series
        return dataframe