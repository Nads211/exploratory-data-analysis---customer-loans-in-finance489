#
import pandas as pd
from scipy import stats
import numpy as np

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
    
    def impute_med(self, dataframe, column):
        dataframe[column] = dataframe[column].fillna(dataframe[column].median())
        return dataframe
    
    def impute_mean(self, dataframe, column):
        dataframe[column] = dataframe[column].fillna(dataframe[column].mean())
        return dataframe
    
    def impute_mode(self, dataframe, column):
        dataframe[column] = dataframe[column].fillna(dataframe[column].mode()[0]) #must index 0 here as column is categorical type so .mode() returns a pandas series
        return dataframe
    
    def yeo_johnson_transform(self, DataFrame, column_name: str):

        '''
        This method is used to apply Yeo-Johnson transformation to normalise a column.

        Parameters:
            DataFrame (pd.DataFrame): The dataframe to which this method will be applied.
            column_name (str): The name of the column which will be transformed.

        Returns:
            yeojohnson_column (pd.Series): The transformed column.
        '''

        yeojohnson_column = stats.yeojohnson(DataFrame[column_name])
        yeojohnson_column = pd.Series(yeojohnson_column[0])
        return yeojohnson_column
    

    def box_cox_transform(self, DataFrame, column_name):

        '''
        This method is used to apply Box-Cox transformation to normalise a column.

        Parameters:
            DataFrame (pd.DataFrame): The dataframe to which this method will be applied.
            column_name (str): The name of the column which will be transformed.

        Returns:
            boxcox_column (pd.Series): The transformed column.
        '''

        boxcox_column = stats.boxcox(DataFrame[column_name])
        boxcox_column = pd.Series(boxcox_column[0])
        return boxcox_column
    

    def drop_outlier_rows(self, DataFrame: pd.DataFrame, column_name: str, z_score_threshold: int):

        '''
        This method is used to remove rows based on the 'z score' of values in a specified column.

        Parameters:
            DataFrame (pd.DataFrame): The dataframe to which this method will be applied.
            column_name(str) : The name of the column which will be transformed.
            z_score_threshold (int)

        Returns:
            DataFrame (pd.DataFrame): The transformed dataframe.
        '''

        mean = np.mean(DataFrame[column_name]) # Identify the mean of the column.
        std = np.std(DataFrame[column_name]) # Identify the standard deviation of the column.
        z_scores = (DataFrame[column_name] - mean) / std # Identofy the 'z score' for each value in the column.
        abs_z_scores = pd.Series(abs(z_scores)) # Create a series with the absolute values of the 'z_score' stored.
        mask = abs_z_scores < z_score_threshold
        DataFrame = DataFrame[mask] # Only keep rows where the 'z score' is below the threshold.        
        return DataFrame