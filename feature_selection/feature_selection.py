# %% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
from sklearn.feature_selection import f_regression
from sklearn.feature_selection import RFE
from sklearn.ensemble import RandomForestRegressor
from sklearn import metrics
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
try:
    os.chdir(os.path.join(os.getcwd(), './feature_selection'))
    print(os.getcwd())
except:
    pass

# %%
import os
# os.chdir('???')
os.getcwd()


# %%
get_ipython().run_line_magic('matplotlib', 'inline')


# %%


# %%
orig_df = pd.read_csv("feature_without_outlier.csv")
orig_df.head()

# %%
orig_df.columns

# %%
orig_df.shape

# %% Remove variable have > 20% of missing values
df = orig_df.dropna(1)
df.head()
X = df[[
    'Year', 'Department_of_Local_Administration',
    'Department_of_Provincial_Administration', 'Bangkok'
]]
y = df.Usage
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=99)
lm = LinearRegression()
lm.fit(X_train, y_train)
y_pred = lm.predict(X_test)
[np.sqrt(metrics.mean_squared_error(y_test, y_pred)),
 metrics.r2_score(y_test, y_pred)]

# %%
# use heatmap to visualize missing value (null) positions
df = orig_df
sns.heatmap(df.isnull(), yticklabels=False, cbar=False, cmap='viridis')

# %%
# count missing values in each variable
df.isnull().sum()

# %%
# find missing value percent
null_percent = df.isnull().sum()/len(df)*100
null_percent
# %%
# Replace missing values

new_df = df
new_df['Department_of_Lands'].fillna(
    df['Department_of_Lands'].median(), inplace=True)  # replace with mode
new_df['Community_Development_Department'].fillna(
    df['Community_Development_Department'].median(), inplace=True)  # replace with mode
new_df['Department_of_Disaster_Prevention_and_Mitigation'].fillna(
    df['Department_of_Disaster_Prevention_and_Mitigation'].median(), inplace=True)  # replace with mode
new_df['Pattaya'].fillna(df['Pattaya'].median(),
                         inplace=True)  # replace with mode
new_df['Department_of_Public_Works_and_Town_&_Country_Planning'].fillna(
    df['Department_of_Public_Works_and_Town_&_Country_Planning'].median(), inplace=True)  # replace with mode
new_df['Office_of_the_Permanent_Secretary_for_Interior'].fillna(
    df['Office_of_the_Permanent_Secretary_for_Interior'].median(), inplace=True)  # replace with mode
new_df.shape
# %%
# after replacing missing values, re-check %missing data
new_df.isnull().sum()/len(new_df)*100
new_df.head()
df = new_df.dropna()
df.head()
X = df[['Year', 'Department_of_Local_Administration',
        'Department_of_Provincial_Administration', 'Bangkok',
        'Department_of_Lands', 'Community_Development_Department',
        'Department_of_Disaster_Prevention_and_Mitigation', 'Pattaya',
        'Department_of_Public_Works_and_Town_&_Country_Planning',
        'Office_of_the_Permanent_Secretary_for_Interior']]
y = df.Usage
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=99)
lm = LinearRegression()
lm.fit(X_train, y_train)
y_pred = lm.predict(X_test)
[np.sqrt(metrics.mean_squared_error(y_test, y_pred)),
 metrics.r2_score(y_test, y_pred)]
# %%
orig_df_solved_na = new_df

######################################################################################################
# %% [markdown]
# Low Variance Filtering

# %%
# compute variances of numerical data columns
df = orig_df_solved_na
df.var()

# Item_Visibility has lower variance, compared to other variables

# %%
# remove variables with low variance
temp_df = df[['Year', 'Department_of_Local_Administration',
              'Department_of_Provincial_Administration', 'Bangkok',
              'Department_of_Lands', 'Community_Development_Department',
              'Department_of_Disaster_Prevention_and_Mitigation', 'Pattaya',
              'Department_of_Public_Works_and_Town_&_Country_Planning',
              'Office_of_the_Permanent_Secretary_for_Interior', 'Usage']]
# temp_df = df[['Item_Weight','Item_Visibility','Item_MRP','Outlet_Establishment_Year','Item_Outlet_Sales']]
min_var_threshold = 10
new_variables = []
for i in range(0, len(temp_df.var())):
    # setting the threshold of minimal variance = 10
    if temp_df.var()[i] >= min_var_threshold:
        new_variables.append(temp_df.columns[i])
new_variables

# %%
temp_df2 = temp_df[new_variables].dropna()
X = temp_df2[['Department_of_Local_Administration',
              'Department_of_Provincial_Administration',
              'Bangkok',
              'Department_of_Lands',
              'Community_Development_Department',
              'Department_of_Disaster_Prevention_and_Mitigation',
              'Pattaya',
              'Department_of_Public_Works_and_Town_&_Country_Planning',
              'Office_of_the_Permanent_Secretary_for_Interior',
              ]]
y = temp_df2['Usage']
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=99)
lm = LinearRegression()
lm.fit(X_train, y_train)
y_pred = lm.predict(X_test)
[np.sqrt(metrics.mean_squared_error(y_test, y_pred)),
 metrics.r2_score(y_test, y_pred)]
######################################################################################################

# %% [markdown]
# High Correlation Filtering

# %%
# plot correlation of numerical data
df = orig_df_solved_na
sns.heatmap(df.corr())
df.corr()

# %%
# since Department_of_Local_Administration	 and Usage have high correlation, drop dependent variables
# new_df = df.drop('Usage', 1)
new_df.shape
sns.heatmap(new_df.corr())
new_df.corr()
new_variables = [
    'Year',
    'Department_of_Provincial_Administration',
    'Bangkok',
    'Department_of_Lands',
    'Community_Development_Department',
    'Department_of_Disaster_Prevention_and_Mitigation',
    'Department_of_Public_Works_and_Town_&_Country_Planning',
    'Office_of_the_Permanent_Secretary_for_Interior',
]
temp_df2 = temp_df[new_variables].dropna()
X = temp_df2
y = orig_df['Usage'].dropna()
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=99)
lm = LinearRegression()
lm.fit(X_train, y_train)
y_pred = lm.predict(X_test)
#%%
print([np.sqrt(metrics.mean_squared_error(y_test, y_pred)),
 metrics.r2_score(y_test, y_pred)])
######################################################################################################

# %% [markdown]
# Random Forest

# %%
df = orig_df_solved_na.drop('Usage', 1)  # drop target variables
df.head()

# %%
df.columns

# %%
# since 'Item_Identifier', 'Outlet_Identifier' do not affect target variable, drop them
temp_df = df
temp_df.head()

# %%
# change categorcial data column to numerical data
temp_df = pd.get_dummies(temp_df)
temp_df.shape    # columns of temp_df = 36 (original df = 12)

# %%
model = RandomForestRegressor(random_state=1, max_depth=10)
# run random forest after removing 'Item_Identifier', 'Outlet_Identifier'
model.fit(temp_df, orig_df.Usage)

# plot importance of features
features = temp_df.columns
importances = model.feature_importances_
indices = np.argsort(importances)[-9:]  # sort top 10 features
plt.title('Feature Importances')
plt.barh(range(len(indices)), importances[indices], color='b', align='center')
plt.yticks(range(len(indices)), [features[i] for i in indices])
plt.xlabel('Relative Importance')
plt.show()

# choose top most features

# %%
new_variables = [
    'Year',
    'Department_of_Provincial_Administration',
    'Bangkok',
    'Department_of_Lands',
    'Community_Development_Department',
    'Department_of_Disaster_Prevention_and_Mitigation',
    'Department_of_Public_Works_and_Town_&_Country_Planning',
    'Office_of_the_Permanent_Secretary_for_Interior',
]
temp_df2 = temp_df[new_variables].dropna()
X = temp_df2
y = orig_df['Usage'].dropna()
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=99)
lm = LinearRegression()
lm.fit(X_train, y_train)
y_pred = lm.predict(X_test)
[np.sqrt(metrics.mean_squared_error(y_test, y_pred)),
 metrics.r2_score(y_test, y_pred)]
######################################################################################################

# %% [markdown]
# Backward Feature Elimination

# %%
n_features = 2  # define by yourself to select important features
df = temp_df  # df that changes from categorical data to numerical data
rfe = RFE(LinearRegression(), n_features)
result = rfe.fit(df, orig_df.Usage)

# %%
result.ranking_

# %%
result.support_

# %%
temp_df.columns

# %%
new_variables = temp_df.columns[result.support_]
new_variables

# %%
temp_df2 = temp_df[new_variables].dropna()
X = temp_df2
y = orig_df['Usage'].dropna()
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=99)
lm = LinearRegression()
lm.fit(X_train, y_train)
y_pred = lm.predict(X_test)
[np.sqrt(metrics.mean_squared_error(y_test, y_pred)),
 metrics.r2_score(y_test, y_pred)]
######################################################################################################

# %% [markdown]
# Forward Feature Selection

# %%
df = temp_df  # df that changes from categorical data to numerical data
ffs = f_regression(df, orig_df.Usage)
ffs

# %%
f_value_threshold = 8  # set yourself to adjust
new_variables = []
for i in range(0, len(df.columns)-1):
    if ffs[0][i] >= f_value_threshold:
        new_variables.append(df.columns[i])
new_variables

# %%
temp_df2 = temp_df[new_variables].dropna()
X = temp_df2
y = orig_df['Usage'].dropna()
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=99)
lm = LinearRegression()
lm.fit(X_train, y_train)
y_pred = lm.predict(X_test)

print([np.sqrt(metrics.mean_squared_error(y_test, y_pred)),
       metrics.r2_score(y_test, y_pred)])

print("USE THIS TEST TO CUT FEATURE AND USE WITH REGRESSION")
