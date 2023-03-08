import pandas as pd
import joblib
import os
from sklearn.model_selection import train_test_split
from pyts.classification import TimeSeriesForest

def create_sEMG_model():
    """
    Train a time series forest classifer on the time series in the CSV file.
    Checks model has been saved locally.
    Args:
        None
    Returns:
        None
    """
    df = pd.read_csv("SemgHandGenderCh2.csv")
    labels = df['0']
    df = df.drop(columns=['0'])

    x_train, x_test, y_train, y_test = train_test_split(df, labels, random_state=42)
    clf = TimeSeriesForest(random_state=42)
    clf.fit(x_train, y_train)
    
    model_name = "time_series_forest_model.joblib"
    joblib.dump(clf, model_name)
   
    assert os.path.isfile(model_name)
    
if __name__ == '__main__':
    create_sEMG_model()