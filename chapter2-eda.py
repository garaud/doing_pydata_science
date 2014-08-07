# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# # Doing Data Science -- chapter 2 -- EDA

# <codecell>

from __future__ import print_function 
import urllib2
from StringIO import StringIO

# <codecell>

URL = 'http://stat.columbia.edu/~rachel/datasets/nyt1.csv'

# <codecell>

content = urllib2.urlopen(URL).read()

# <markdowncell>

# Save it to a CSV file.

# <codecell>

with open('nyt1.csv', 'w') as fid:
    fid.write(content)

# <codecell>

!ls

# <markdowncell>

# Extract data with pandas

# <codecell>

import numpy as np
import pandas as pd
print("pandas version {}".format(pd.__version__))

# <codecell>

pd.options.display.mpl_style = "default"

# <codecell>

# Read the file or the 'content'
df = pd.read_csv(StringIO(content))

# <codecell>

df.head()

# <markdowncell>

# The book tells you that `female=0` and `male=1`. I turn these integer values into strings.

# <codecell>

df['Gender'].apply(lambda x: 'male' if x else 'female').head()

# <markdowncell>

# I set these values in the existing `Gender` column.

# <codecell>

df['Gender'] = df['Gender'].apply(lambda x: 'male' if x else 'female')

# <codecell>

df.head(10)

# <markdowncell>

# ## 1. Create 'age_group' that categorizes user by age

# <markdowncell>

# Want to categorize by age `<18, 18-24, 25-34, 35-44, 45-54, 55-64, +65`
# Create bins and labels and user `pd.cut` with `right=False` to not include rightmost edge.

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

df.head(15)

# <headingcell level=3>

# ## For a single day (i.e. one file)
# 
# * Impressions and click-rate distributions according to this age category

# <markdowncell>

# Let's group data by this `Age_group` just for the impressions and clicks columns and count the number of each.

# <codecell>

df.groupby('Age_group')[['Impressions', 'Clicks']].sum()

# <markdowncell>

# Here we are ! I count the number of values for each category for the two columns. Compute the CTR (click-through-rate, i.e. `clicks/impression`) and let's plot some stuff.

# <codecell>

df_age_group = df.groupby('Age_group')[['Impressions', 'Clicks']].sum()

# <codecell>

df_age_group['CRT'] = df_age_group['Clicks'] / df_age_group['Impressions']

# <codecell>

df_age_group[['Impressions', 'CRT']].plot(kind='bar', subplots=True)

