import pandas as pd
import numpy as np

def handle_missing_values(df, strategy='mean', fill_value=None):
    """
    Handle missing values in the DataFrame.

    Parameters:
    - df: pandas DataFrame
    - strategy: str, default 'mean'
        The strategy to use for filling missing values. Options are 'mean', 'median', 'mode', 'constant', 'drop'.
    - fill_value: scalar, default None
        The value to use for filling missing values when strategy is 'constant'.

    Returns:
    - pandas DataFrame with missing values handled.
    """
    if strategy == 'mean':
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        return df.fillna(df[numeric_cols].mean())
    elif strategy == 'median':
        return df.fillna(df.median())
    elif strategy == 'mode':
        return df.fillna(df.mode().iloc[0])
    elif strategy == 'constant':
        if fill_value is not None:
            return df.fillna(fill_value)
        else:
            raise ValueError("fill_value must be provided when strategy is 'constant'")
    elif strategy == 'drop':
        return df.dropna()
    else:
        raise ValueError("Invalid strategy. Options are 'mean', 'median', 'mode', 'constant', 'drop'.")
