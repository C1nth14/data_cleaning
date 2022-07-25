import pandas as pd
import numpy as np


def read_csv(file="al_results_2020.csv"):
    al_df = pd.read_csv(file, engine='python')
    print(al_df.columns)


read_csv()


def drop_columns(file="al_results_2020.csv"):
    al_df = pd.read_csv(file, engine='python')
    to_drop = ['Zscore', 'gender', 'syllabus']
    new_al = al_df.copy()
    new_al.drop(to_drop, axis=1, inplace=True)
    print(new_al.columns)


drop_columns()
