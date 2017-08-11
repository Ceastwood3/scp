""""Provides helper functions for pandas DataFrames"""
import pandas as pd
from utils.general_utils import intersect, list_diff, variable_name
from utils.exceptions import PandasUtilsException


def cross_join(df1, df2):
    """caretesian join for df1 and df2"""
    try:
        x = df1.copy()
        y = df2.copy()
        table_1_col = x.columns.tolist()
        table_2_col = y.columns.tolist()
        if intersect(table_1_col, table_2_col):
            raise PandasUtilsException('cross_join has an error because the dataframes. {0} and {1}, '
                                       'share a similar column name. '
                                       'Either change the column name or use a different'
                                       ' join option'.format(variable_name(df1), variable_name(df2)))

        x["key1234"] = 1
        y["key1234"] = 1
        cross_joined_table = x.merge(y, on="key1234")
        cross_joined_table_col = [i for i in cross_joined_table.columns.tolist() if i != "key1234"]
        cross_joined_table = cross_joined_table[cross_joined_table_col]
        del x["key1234"]
        del y["key1234"]
        return cross_joined_table
    except Exception as e:
        raise PandasUtilsException('cross_join failed with the following error - {0}'.format(e))


def add_null_columns(df, add_col_list):
    """ appends new columns (as nulls) to the extract_data frame """
    try:
        tab = df.copy()
        if intersect(tab.columns.tolist(), add_col_list):
            raise ValueError('The null columns you are trying to add already exist in the extract_data frame.')

        df_cols = tab.columns.tolist() + add_col_list
        new_df = pd.concat([tab, pd.DataFrame(columns=add_col_list)])
        new_df = new_df[df_cols]
        return new_df
    except Exception as e:
        raise PandasUtilsException('add_null_columns failed with the following error - {0}'.format(e))


def add_null_columns_not_in_list(df, final_col_list):
    col_diff = list_diff(l1=final_col_list, l2=df.columns.tolist())
    return add_null_columns(df=df, add_col_list=col_diff)


def delete_where_df_joins(df1, df2, on=None, left_on=None, right_on=None):
    """deletes rows from df1 where df1 and df2 join"""
    try:
        t1 = df1.copy()
        t2 = df2.copy()
        t2["df2_join_col"] = 1
        t1 = t1.merge(t2, how="left", on=on, left_on=left_on, right_on=right_on)
        t1 = t1[t1['df2_join_col'].isnull()]
        t1 = t1[df1.columns.tolist()]
        return t1
    except Exception as e:
        raise PandasUtilsException('delete_where_df_joins failed with the following error - {0}'.format(e))


def groupby_agg(df, grp_by_cols, func_dict):
    df = df.groupby(grp_by_cols, as_index=False).agg(func_dict)
    df.columns = [x[0] for x in df.columns.tolist()]
    return df


def delete_column_list(df, col_list=[]):
    dat = df.copy()
    for col in col_list:
        try:
            del dat[col]
        except:
            print("column does not exists in data frame: ", col)
    return dat


def cross_join_with_same_cols(df1, df2):
    intersect_cols = intersect(df1.columns.tolist(), df2.columns.tolist())
    df1.columns = [x + "_x" if x in intersect_cols else x for x in df1.columns.tolist()]
    df2.columns = [y + "_y" if y in intersect_cols else y for y in df2.columns.tolist()]
    return cross_join(df1, df2), intersect_cols


