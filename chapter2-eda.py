# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# # Doing Data Science: chapter 2 -- EDA
# 
# Exercise on **E**ploratory **D**ata **A**nalysis
# 
# Get input data files from https://github.com/oreillymedia/doing_data_science or http://stat.columbia.edu/~rachel/nytN.csv where `N=[1, .., 31]`.

# <markdowncell>

# ## Retrieve some data
# 
# Quoting:
# 
# > Each file represents one (simulated) day's worth of ads shown and clicks recorded on the NY Times home page in May 2012

# <codecell>

from __future__ import print_function 
from StringIO import StringIO

# <codecell>

import requests

# <codecell>

URL = 'http://stat.columbia.edu/~rachel/datasets/nyt1.csv'

# <codecell>

resp = requests.get(URL)

# <markdowncell>

# Save it to a CSV file.

# <codecell>

with open('nyt1.csv', 'w') as fid:
    fid.write(resp.content)

# <codecell>

!ls *.csv

# <codecell>

!head nyt1.csv

# <markdowncell>

# ## Extract data with pandas

# <codecell>

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
print("pandas version {}".format(pd.__version__))

# <markdowncell>

# For a matplotlib version >= 1.4, you can use `plt.style.use("ggplot")`

# <codecell>

plt.style.use("ggplot")
# pd.options.display.mpl_style = "default"

# <codecell>

# Read the file or the 'content'
df = pd.read_csv(StringIO(resp.content))

# <codecell>

df.head()

# <markdowncell>

# ## Clean up some data

# <markdowncell>

# The book tells you that `female=0` and `male=1`. I turn these integer values into strings.

# <codecell>

df['Gender'].apply(lambda x: 'male' if x else 'female').head()

# <markdowncell>

# I overwrite these values into the existing `Gender` column.

# <codecell>

df['Gender'] = df['Gender'].apply(lambda x: 'male' if x else 'female')

# <codecell>

df.head(10)

# <markdowncell>

# ## Create `age_group` that categorizes user by age

# <markdowncell>

# Want to categorize by age `<18, 18-24, 25-34, 35-44, 45-54, 55-64, +65`.
# 
# Create bins and labels and use `pd.cut` with `right=False` to not include rightmost edge.

# <codecell>

age_range = [0, 19, 25, 35, 45, 55, 65, np.inf]
age_labels = ['18--', '18-24', '25-34', '35-44', '45-54', '55-64', '65++']

# <codecell>

pd.cut(df['Age'], bins=age_range, right=False, labels=age_labels)

# <markdowncell>

# Put this into a new columns.

# <codecell>

df['Age_group'] = pd.cut(df['Age'], bins=age_range, right=False, labels=age_labels)

# <codecell>

df.head(10)

# <markdowncell>

# ## Click-trough-rate aka CRT by age categories
# 
# Impressions and click-rate distributions according to this age category.

# <markdowncell>

# Let's group data by this `Age_group` just for the impressions and clicks columns and count the number of each.
# 
# Simple use the `groupby` function to the column `Age_group`.

# <codecell>

df.groupby('Age_group')[['Impressions', 'Clicks']].sum()

# <markdowncell>

# Here we are ! I count the number of values for each category for the two columns. Compute the CTR (click-through-rate, i.e. `clicks/impression`) and let's plot some stuff.

# <codecell>

df_age_group = df.groupby('Age_group')[['Impressions', 'Clicks']].sum()

# <markdowncell>

# Compute the click rate.

# <codecell>

df_age_group['CTR'] = df_age_group['Clicks'] / df_age_group['Impressions']

# <markdowncell>

# Plotting some data.

# <codecell>

df_age_group[['Impressions', 'CTR']].plot(kind='bar', subplots=True)

# <markdowncell>

# ## New category based on click behavior
# 
# You can take an arbitrary threshold such as median to create two new segments: `low` and  `high` CTRs.

# <codecell>

df_age_group["CTR"].describe()

# <codecell>

threshold = 0.010292
df_age_group["CTR"] > threshold

# <codecell>

df_age_group["High"] = df_age_group["CTR"] > threshold

# <codecell>

df_age_group

# <codecell>

df.head(20)

