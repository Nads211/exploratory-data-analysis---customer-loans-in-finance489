from matplotlib import pyplot
import missingno as msno
import numpy as np
import pandas as pd
#import plotly.express as px
from scipy import stats
import seaborn as sns
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
    

    def compare_skewness_transformations(self, DataFrame, column_name):
       
        transformed_df = DataFrame.copy()
        transformed_df['yeo-johnson'] = pd.Series(stats.yeojohnson(DataFrame[column_name])[0]).values # Perform yeo-johnson transformation and add values as new column in dataframe copy.
        transformed_df["log_transformed"] = DataFrame[column_name].map(lambda x: np.log(x) if x > 0 else 0) # Log transformation applied to value in column, if value is 0 then no transformation is done and added to new column in dataframe copy.
            
        fig, axes = pyplot.subplots(nrows=1, ncols=3, figsize=(16, 4)) # Create a 2x3 grid
        pyplot.suptitle(column_name, fontsize='x-large') # Add large title for entire plot.

        axes[0].set_title('Original Histogram')
        axes[1].set_title('Log Transformed Histogram')
        axes[2].set_title('Yeo-Johnson Transformed Histogram')
        
            # Original Histogram
        sns.histplot(DataFrame[column_name], kde=True, ax=axes[0]) 
        axes[0].text(0.5, 0.95, f'Skewness: {DataFrame[column_name].skew():.2f}', ha='center', va='top', transform=axes[0].transAxes) # Add skewness
        # Log transformed Histogram
        sns.histplot(transformed_df['log_transformed'], kde=True, ax=axes[1]) 
        axes[1].text(0.5, 0.95, f'Skewness: {transformed_df["log_transformed"].skew():.2f}', ha='center', va='top', transform=axes[1].transAxes) # Add skewness
        # Yeo Johnson Histogram
        sns.histplot(transformed_df['yeo-johnson'], kde=True, ax=axes[2]) 
        axes[2].text(0.5, 0.95, f'Skewness: {transformed_df["yeo-johnson"].skew():.2f}', ha='center', va='top', transform=axes[2].transAxes) # Add skewness

        return pyplot.show()


    def facet_grid_box_plot(self, DataFrame: pd.DataFrame, column_names: list):

        '''
        This method is used to return a Facet Grid containing box-plots for a list of columns.

        Parameters:
            DataFrame (pd.DataFrame): The dataframe to which this method will be applied.
            column_names (list): A list of names of columns which will be plotted.

        Returns:
            facet_grid (sns.FacetGrid): A facetgrid containing the box-plots of each of the variables.
        '''

        melted_df = pd.melt(DataFrame, value_vars=column_names) # Melt the dataframe to reshape it.
        facet_grid = sns.FacetGrid(melted_df, col="variable",  col_wrap=3, sharex=False, sharey=False) # Create the facet grid
        facet_grid = facet_grid.map(sns.boxplot, "value", flierprops=dict(marker='x', markeredgecolor='red')) # Map box-plot onto each plot on grid.
        return facet_grid
    
    def correlation_matrix(self, dataframe):
        """
        Calculate the correlation matrix for columns in a pandas DataFrame.

        Parameters:
        - dataframe: pandas DataFrame

        Returns:
        - correlation_matrix: pandas DataFrame, the correlation matrix
        """
        correlation_matrix = dataframe.corr()
        styled_correlation_matrix = correlation_matrix.style.background_gradient(cmap='coolwarm')
        return styled_correlation_matrix