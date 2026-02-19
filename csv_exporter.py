import pandas as pd
from datetime import datetime

def export_to_csv(leads, filename):
    df = pd.DataFrame(leads)
    if 'created_utc' in df.columns:
        df['created_utc'] = df['created_utc'].apply(lambda x: datetime.fromtimestamp(x).strftime('%Y-%m-%d %H:%M:%S'))
    df.to_csv(filename, index=False)
