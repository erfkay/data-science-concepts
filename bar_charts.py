import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

%matplotlib inline
#here we use the pokemon data set to graph a bar chart using seaborn and matplotlib

pokemon = pd.read_csv('./data/pokemon.csv')
pokemon.head()
