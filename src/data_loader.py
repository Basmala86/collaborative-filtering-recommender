import pandas as pd

def load_data(path='data/u.data'):
    column_names = ['user_id', 'item_id', 'rating', 'timestamp']
    return pd.read_csv(path, sep='\t', names=column_names)

def load_item_info(path='data/u.item'):
    column_names = ['item_id', 'title'] + [f'col_{i}' for i in range(22)]
    return pd.read_csv(path, sep='|', names=column_names, encoding='latin-1')[['item_id', 'title']]
