# --------------
#Code Stars here
import pandas as pd 

# Read the data using pandas module.

df_ipl=pd.read_csv(path)
#print(df_ipl)
df_ipl.shape

# Find the list of unique cities where matches were played

#print('Unique Cities',df_ipl.loc[:,'city'].unique())

print('Unique Cities',df_ipl['city'].unique())

# Find the columns which contains null values if any ?
print(df_ipl.isnull().columns)

# List down top 5 most played venues

print(df_ipl.groupby('venue')[['match_code']].nunique().sort_values(ascending=False, by='match_code').head(5))

# Make a runs count frequency table
print(df_ipl['runs'].value_counts())

# How many seasons were played and in which year they were played 
print(df_ipl['date'].apply(lambda x:x[0:4]).nunique())
print(df_ipl['date'].apply(lambda x:x[0:4]).unique())

# No. of matches played per season

print(df_ipl.groupby(df_ipl['date'].apply(lambda x:x[0:4]))[['match_code']].nunique())

# Total runs across the seasons
print(df_ipl.groupby(df_ipl['date'].apply(lambda x:x[0:4]))[['total']].sum())

# Teams who have scored more than 200+ runs. Show the top 10 results
high_scoring_team = df_ipl.groupby(['match_code','inning','team1','team2'])[['total']].sum().reset_index()
high_scoring_team[high_scoring_team['total']>=200]
print(high_scoring_team.nlargest(10,'total'))

# What are the chances of chasing 200+ target
inn_1_teams = high_scoring_team[(high_scoring_team['inning']==1) & (high_scoring_team['total']>=200)]
inn_2_teams = high_scoring_team[(high_scoring_team['inning']==2) & (high_scoring_team['total']>=200)]

high_scoring = inn_1_teams.merge(inn_2_teams[['match_code','inning','total']], on='match_code')

chance=(high_scoring['total_y']>high_scoring['total_x']).value_counts()
print(chance[True]/(chance[False]+chance[True])*100)


# Which team has the highest win count in their respective seasons ?

df_ipl.drop_duplicates('match_code').groupby(df_ipl['date'].apply(lambda x:x[0:4]))['winner'].value_counts()


