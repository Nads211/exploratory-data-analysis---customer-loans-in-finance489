# Milestone 3 - Task 1: Convery columns to the correct format
# Class to convert columns to the correct format
import pandas as pd

class DataTransform:
    """    
    convert_to_category(self, dataframe, column_name)
        convert_to_timeperiod(self, dataframe, column_name, frequency='M')
        convert_to_integer(self, dataframe, column_name)
        convert_to_string(self, dataframe, column_name)
"""
    
    #convert string to date
    def extract_integer_from_string(self, dataframe, column_name):
        dataframe[column_name] = dataframe[column_name].str.extract('(\d+)').astype('Int32') # The first method extracts any digits from the string in the desired column
        # the second method casts the digits into the 'Int32' data type, this is because this type of integer is a nullable type of integer.
        return dataframe
    
    def replace_string_text(self, dataframe, column_name, original_string, new_string):
        dataframe[column_name] = dataframe[column_name].str.replace(original_string, new_string)
        return dataframe
    
    def convert_to_category(self, dataframe, column_name):
        """
        Convert a column in a pandas DataFrame from data type object to category.

        Parameters:
        - dataframe: pandas DataFrame
        - column_name: str, the name of the column to be converted

        Returns:
        - None (the DataFrame is modified in place)
        """
        dataframe[column_name] = dataframe[column_name].astype('category')
        return dataframe

    def convert_to_timeperiod(self, dataframe, column_name, frequency='M'):
        """
        Convert a column in a pandas DataFrame to the Period data type.

        Parameters:
        - dataframe: pandas DataFrame
        - column_name: str, the name of the column to be converted
        - frequency: str, the frequency of the Period (default is 'M' for monthly)

        Returns:
        - None (the DataFrame is modified in place)
        """
        # Convert the specified column to datetime
        dataframe[column_name] = pd.to_datetime(dataframe[column_name], errors='coerce')

        # Convert datetime to Period with the specified frequency
        dataframe[column_name] = dataframe[column_name].dt.to_period(frequency)
        return dataframe
    
    def convert_string_to_date(self, DataFrame: pd.DataFrame, column_name: str):

        '''
        This method is used to convert a date in string format into a date in period format. The reason for period format is because dates within the loan database only have a resolution of the month and year.

        Parameters:
            column_name (str): The name of the column to which this method will be applied.

        Returns:
            DataFrame (pd.DataFrame): the updated DataFrame.
        '''
            
        DataFrame[column_name] = pd.to_datetime(DataFrame[column_name], errors='coerce').dt.to_period('M') # The first method converts the string in the column to a datetime.
        # The second method converts the datetime to a period (M) which is a date that contains only the month and year since this is the resolution of the data provided.
        return DataFrame
    
    #def convert_to_integer(self, dataframe, column_name):
    #    """
      #  Convert a column in a pandas DataFrame from float to integer data type.

       # Parameters:
       # - dataframe: pandas DataFrame
      #  - column_name: str, the name of the column to be converted

      #  Returns:
     #   - None (the DataFrame is modified in place)
      #  """
     #   dataframe[column_name] = dataframe[column_name].astype(int)
    
    def convert_to_integer(self, dataframe, column_name):
        """
        Convert a column in a pandas DataFrame from float to integer data type,
        ignoring null values.

        Parameters:
        - dataframe: pandas DataFrame
        - column_name: str, the name of the column to be converted

        Returns:
        - None (the DataFrame is modified in place)
        """
        # Use pd.to_numeric with errors='coerce' to handle null values
        dataframe[column_name] = pd.to_numeric(dataframe[column_name], errors='coerce', downcast='integer')
        return dataframe

    
    def convert_to_string(self, dataframe, column_name):
        """
        Convert a column in a pandas DataFrame from integer to string data type.

        Parameters:
        - dataframe: pandas DataFrame
        - column_name: str, the name of the column to be converted

        Returns:
        - None (the DataFrame is modified in place)
        """
        dataframe[column_name] = dataframe[column_name].astype(str)
        return dataframe

