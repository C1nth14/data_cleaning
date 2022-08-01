import pandas as pd
import csv
import numpy as np


def read_csv(file):
    al_df = pd.read_csv(file, engine='python')
    return al_df


def drop_columns(al_df):
    to_drop = ['Zscore', 'gender', 'syllabus']

    return al_df.drop(to_drop, axis=1)


'''def valid_date(al_df):
    if al_df[np.logical_and(al_df.birth_month == "February", al_df.birth_year.astype(float) % 400 == 0)]:
        al_df = al_df.drop(al_df[(al_df['birth_day'] > 29)])

    else:
        pass
    return al_df'''
# I couldn't find a suitable solution to tackle the invalid dates but when I will be updating this code.


def birth_date(al_df):
    al_df = al_df.assign(birthday=al_df.birth_day.astype(str) + '/'+al_df.birth_month.astype(str)
                         + '/' + al_df.birth_year.astype(str))
    to_drop = ['birth_day', 'birth_month', 'birth_year']
    al_df = al_df.drop(to_drop, axis=1)

    return al_df


def drop_rows(al_df):
    al_df = al_df[al_df.index != '-']
    al_df = al_df[al_df.stream != '-']
    al_df = al_df[al_df.sub1 != '-']
    al_df = al_df[al_df.sub2 != '-']
    al_df = al_df[al_df.sub3 != '-']
    al_df = al_df[al_df.island_rank != '-']
    al_df = al_df[al_df.district_rank != '-']

    return al_df


def del_absent(al_df):

    al_df = al_df[al_df.sub1_r != 'Absent']
    al_df = al_df[al_df.sub2_r != 'Absent']
    al_df = al_df[al_df.sub3_r != 'Absent']
    al_df = al_df[al_df.cgt_r != 'Absent']
    al_df = al_df[al_df.general_english_r != 'Absent']

    return al_df


while True:
    data = read_csv("al_results_2020.csv")
    data = drop_columns(data)
    #data = valid_date(data)
    data = birth_date(data)
    data = drop_rows(data)
    data = del_absent(data)



    data.to_csv('clean_al_df.csv')
    break


