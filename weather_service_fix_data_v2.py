import os
import sys

import pandas as pd
import numpy as np

from sqlalchemy import create_engine


from config import config
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(str(dir_path) + '/..')


def get_weather_data_from_database():
    engine = create_engine(config.connection_string)
    table_name = 'weather_conditions'
    _df = pd.read_sql('SELECT * FROM ' + table_name, engine)
    _df = _df.sort_values('observation_time_rfc822')
    _df = _df.reset_index(drop=True)
    return _df


def get_missing_data_indices(_df):
    time_diff_sr = _df.loc[:, 'observation_time_rfc822'].diff(periods=-1) * (-1)
    missed_entries = pd.Series(round(time_diff_sr / pd.to_timedelta(30, unit='m')))
    missed_entries.iloc[missed_entries.nonzero()[0]] = missed_entries.iloc[missed_entries.nonzero()[0]] - 1
    _missings = missed_entries.iloc[missed_entries.nonzero()]
    _missings = _missings.loc[_missings.notnull()]
    return _missings


def create_filling_df(_df, _missings):
    adding_df = pd.DataFrame()
    for idx, miss_num in _missings.iteritems():
        print(idx)
        cond1 = _df.loc[:, 'observation_time_rfc822'] <= df.loc[idx, 'observation_time_rfc822']
        cond2 = _df.loc[:, 'observation_time_rfc822'] > (df.loc[idx, 'observation_time_rfc822'] -
                                                        pd.Timedelta(seconds=60 * 30 * 2))
        copy_rows = _df.loc[cond1 & cond2, :].copy()

        for i in np.arange(0, miss_num - 1, 1):
            new_time = copy_rows.loc[copy_rows.index[-1], 'observation_time_rfc822'] + \
                       ((i + 1) * pd.Timedelta(seconds=60 * 30))
            copy_rows.loc[:, 'observation_time_rfc822'] = new_time
            adding_df = adding_df.append(copy_rows)
    return adding_df


def append_to_database(append_df):
    engine = create_engine(config.connection_string)
    table_name = 'weather_conditions'
    append_df.to_sql(table_name, con=engine, if_exists='append', index=False)


def fix_missing_weather_data(n=0):
    df = get_weather_data_from_database()

    # select rows to fix
    if n == 0:
        n = df.shape[0]
    df = df.tail(n=n).reset_index(drop=True)

    missings = get_missing_data_indices(df)
    print(df.loc[87849])
    print(df.loc[87850])
    print(df.loc[87851])
    print(df.loc[87852])
    print(df.loc[87853])
    print(df.loc[87854])
    print(df.loc[87855])
    print(df.loc[87856])
    print(df.loc[87857])
    print(df.loc[87858])
    print(df.columns)
    filling_df = create_filling_df(df, missings)
    append_to_database(filling_df)


if __name__ == '__main__':
    fix_missing_weather_data()
