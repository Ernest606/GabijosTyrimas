#!/usr/bin/env python
# coding: utf-8

import pandas as pd

# Read the CSV file
df = pd.read_csv('/home/simona/SAMPLE/GPU/GabijosTyrimas/ModelsHYP.csv', delimiter =';', dtype={0: int, 1: int, 2: float, 3: float, 4: float, 5: str}, header=None)

# Write the first row to ApmokytiModeliaiHYP.csv
df.iloc[[0]].to_csv('/home/simona/SAMPLE/GPU/GabijosTyrimas/ApmokytiModeliaiHYP.csv', mode='a', header=False, index=False, sep=';')

# Drop the first row from the original DataFrame
df = df.drop(df.index[0])

# Write the remaining data back to ModelsHYP.csv
df.to_csv('/home/simona/SAMPLE/GPU/GabijosTyrimas/ModelsHYP.csv', header=False, index=False, sep=';')

