import bootcamp_utils
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Pandas, conventionally imported as pd

# Plotting modules and settings.

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728',
          '#9467bd', '#8c564b', '#e377c2', '#7f7f7f',
          '#bcbd22', '#17becf']

def get_data_clean():
    '''
    get grant data ana clean it for analysis
    '''
    # get data..
    grant1973_df = pd.read_csv('data/grant_1973.csv', comment='#')
    grant1975_df = pd.read_csv('data/grant_1975.csv', comment='#')
    grant1987_df = pd.read_csv('data/grant_1987.csv', comment='#')
    grant1991_df = pd.read_csv('data/grant_1991.csv', comment='#')
    grant2012_df = pd.read_csv('data/grant_2012.csv', comment='#')

    # add year column when missing (all but 1973). np array based on row number
    year_series = pd.Series(np.full(403,75))
    grant1975_df['year'] = year_series
    year_series = pd.Series(np.full(943,87))
    grant1987_df['year'] = year_series
    year_series = pd.Series(np.full(621,91))
    grant1991_df['year'] = year_series
    year_series = pd.Series(np.full(248,12))
    grant2012_df['year'] = year_series

    # verify same column names
    grant1973_df.columns = ['band', 'species', 'year', 'Beak length, mm',
                            'Beak depth, mm']
    grant1987_df.columns = ['band', 'species', 'Beak length, mm', 'Beak depth, mm',
                            'year']
    grant1991_df.columns = ['band', 'species', 'Beak length, mm', 'Beak depth, mm',
                            'year']
    grant2012_df.columns = ['band', 'species', 'Beak length, mm', 'Beak depth, mm',
                            'year']

    return grant1973_df, grant1975_df, grant1987_df, grant1991_df, grant2012_df

#get data into variables
grant1973_df, grant1975_df, grant1987_df, grant1991_df, grant2012_df = get_data_clean()

def concat_dfs(grant1973_df, grant1975_df, grant1987_df, grant1991_df, grant2012_df):
    '''
    concatenate the five datasets
    '''
    concatenated = pd.concat([grant1973_df, grant1975_df, grant1987_df,
        grant1991_df, grant2012_df], ignore_index=True, axis = 0)
    return concatenated

# merge
merged_df = concat_dfs(grant1973_df, grant1975_df, grant1987_df, grant1991_df, grant2012_df)

def drop_duplicates(dataframe):
    '''
    drop duplicate band number by year
    '''
    return merged_df.drop_duplicates(['year','band'])

# drop duplicates by year and band
merged_df = drop_duplicates(merged_df)

#save to csv
merged_df.to_csv('grant_complete_tidy.csv', index=False)

def plot_ECDF():
    '''
    plot ECDF of data
    '''
    df = pd.read_csv('grant_complete_tidy.csv')
    # fig, ax = plt.subplots(1,1)
    # ax.set_xlabel('Beak Depth (mm)')
    #
    # x, y = bootcamp_utils.ecdf(df.loc[(df['year']==87) & (df['species']=='fortis'),'Beak depth, mm'],
    #         formal=True)
    # ax.plot(x,y,marker='.',linestyle='none')
    # plt.show()
    #
    # fig, ax = plt.subplots(1,1)
    # ax.set_xlabel('Beak Depth (mm)')
    #
    # x, y = bootcamp_utils.ecdf(df.loc[(df['year']==87) & (df['species']=='scandens'),'Beak depth, mm'],
    #         formal=True)
    # ax.plot(x,y,marker='.',linestyle='none')
    # plt.show()
    for year in [73, 75, 87, 91, 12]:
        fig, ax = plt.subplots(1,1)
        ax.set_ylim([7,12])
        ax.set_xlabel('Beak Depth (mm)')
        ax.set_ylabel('Beak length (mm)')
        ax.set_title('Sampling year:{}'.format(year))
        scan_length = df.loc[(df['year']==year) & (df['species']=='scandens'),'Beak length, mm']
        scan_depth = df.loc[(df['year']==year) & (df['species']=='scandens'),'Beak depth, mm']
        ax.plot(scan_length,scan_depth,marker='.',linestyle='none', label='scandens')
        fort_length = df.loc[(df['year']==year) & (df['species']=='fortis'),'Beak length, mm']
        fort_depth = df.loc[(df['year']==year) & (df['species']=='fortis'),'Beak depth, mm']
        ax.plot(fort_length,fort_depth,marker='.',linestyle='none', label='fortis')
        ax.legend()
        plt.show()

plot_ECDF()
