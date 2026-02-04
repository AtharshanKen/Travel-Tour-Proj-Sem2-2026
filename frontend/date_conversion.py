import pandas as pd
import numpy as np
def date_conv(df:pd.DataFrame) -> list[dict]:
    df = df.copy()
    datetime_cols_df = df.select_dtypes(include=[np.datetime64])
    datetime_col_names = datetime_cols_df.columns.tolist()  
    for cn in datetime_col_names:
        df[cn] = pd.to_datetime(df["Date"], errors="coerce").dt.strftime("%Y-%m-%d %H:%M:%S")
    return df.to_dict(orient="records")