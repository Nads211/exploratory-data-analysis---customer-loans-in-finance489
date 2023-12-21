from matplotlib import pyplot
import missingno as msno
import numpy as np
import pandas as pd
#import plotly.express as px
#from scipy import stats
#import seaborn as sns
#from statsmodels.graphics.gofplots import qqplot

class Plotter:

    '''
    This class is used to plot visualisations of the data.
    '''

    def missing_matrix(self, DataFrame: pd.DataFrame):

        '''
        This method plots a matrix displaying missing or null data points within the DataFrame.
        
        Parameters:
            DataFrame (pd.DataFrame): The dataframe to which this method will be applied.

        Returns:
            matplotlib.axes._subplots.AxesSubplot: A matrix plot showing all the missing or null data points in each column in white.
        '''

        return msno.matrix(DataFrame)