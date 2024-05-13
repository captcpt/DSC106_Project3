import pandas as pd

df = pd.read_csv('NSDUH_2015-2019.csv')

# Filtering to just include demographic and substance use variables of interest
df = df[['year', 'irsex', 'age2', 'catag6', 'newrace2', 'sexident', 'cigever', 'alcever', 'mjever',
        'cocever','herever', 'hallucevr', 'lsd', 'pcp', 'mesc', 'psilcy', 'ketminesk', 
        'methamevr', 'stmanylif', 'sedanylif']]

# Maps for converting ordinal variables to more readable ones
irsex_map = {1: "Male", 2: "Female"}
catag6_map = {1: "12-17 years old", 2: "18-25 years old", 3: "26-34 years old", 4: "35-49 years old", 5: "50-64 years old", 6: "65+ years old"}
newrace2_map = {1: "White", 2: "Black/African American", 3: "Native American/AK Native", 4: "Native HI/Pacific Islander", 5: "Asian", 6: "More than one race", 7: "Hispanic"}
sexident_map = {1: "Heterosexual", 2: "Lesbian/Gay", 3: "Bisexual"}

df['sexident'] = df['sexident'].apply(lambda x: x if x in [1, 2, 3] else 0)

# Mapping values 
df['irsex'] = df['irsex'].map(irsex_map)
df['catag6'] = df['catag6'].map(catag6_map)
df['newrace2'] = df['newrace2'].map(newrace2_map)
df['sexident'] = df['sexident'].map(sexident_map)
#df['cigever'] = df['cigever'].map(cigever_map)

# Replacing all non-yes responses to 0 so they do not affect sum of people who have tried the substance(s)
cols_to_replace_zero = ['cigever', 'alcever', 'mjever', 'cocever', 'herever', 'hallucevr', 'lsd', 'pcp', 'mesc', 'psilcy', 'ketminesk', 'methamevr', 'stmanylif', 'sedanylif']
df[cols_to_replace_zero] = df[cols_to_replace_zero].applymap(lambda x: 0 if x != 1 else x)

# Outputting to filtered CSV
df.to_csv('nsduh_clean.csv',index=False)