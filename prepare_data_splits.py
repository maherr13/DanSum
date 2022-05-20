'''
This script prepares train-test-val splits of the data.
'''

# %% LOAD PACKAGES
import pandas as pd
import datasets
from datasets import Dataset
from sklearn.model_selection import train_test_split

# %% ------- MAKE 50K SUBSET:
df_abs = pd.read_json('gpu_files/abs_sums.json') # load all abs data (287205 pairs)
df50k = df_abs[:50000] # make the subset
abs50kds = Dataset.from_pandas(df50k) # make dataset format

# %% make train test val splits
train50k, test50k = abs50kds.train_test_split(test_size=5000).values() # 5000 = absolute size specified
train50k, val50k = train50k.train_test_split(test_size=5000).values()

# %% CHECK SPLIT SIZES
print(len(train50k))
print(len(test50k))
print(len(val50k))

# %% SAVE SPLITS
train50k.to_csv("data/train50k.csv")
test50k.to_csv("data/test50k.csv")
val50k.to_csv("data/val50k.csv")