# Milestone 3 - Task 1: Convery columns to the correct format
# Class to convert columns to the correct format
class DataTransform:
    def __init__(self) -> None:
        pass

    #convert string to date

    def extract_integer_from_string(self, DataFrame: pd.DataFrame, column_name: str):
        DataFrame[column_name] = DataFrame[column_name].str.extract('(\d+)').astype('Int32') # The first method extracts any digits from the string in the desired column
        # the second method casts the digits into the 'Int32' data type, this is because this type of integer is a nullable type of integer.
        return DataFrame

    def replace_string_text(self, DataFrame: pd.DataFrame, column_name: str, original_string: str, new_string: str):
        DataFrame[column_name] = DataFrame[column_name].str.replace(original_string, new_string)
        return DataFrame

    def convert_string_to_date(self, DataFrame: pd.DataFrame, column_name: str):
        DataFrame[column_name] = pd.to_datetime(DataFrame[column_name], errors='coerce').dt.to_period('M') # The first method converts the string in the column to a datetime.
        # The second method converts the datetime to a period (M) which is a date that contains only the month and year since this is the resolution of the data provided.
        return DataFrame