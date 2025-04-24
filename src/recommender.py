from surprise import Dataset, Reader, KNNBasic
from surprise.model_selection import train_test_split

def get_dataset(df):
    reader = Reader(rating_scale=(1, 5))
    return Dataset.load_from_df(df[['user_id', 'item_id', 'rating']], reader)

def train_user_based(trainset):
    sim_options = {'name': 'cosine', 'user_based': True}
    algo = KNNBasic(sim_options=sim_options)
    algo.fit(trainset)
    return algo

def train_item_based(trainset):
    sim_options = {'name': 'cosine', 'user_based': False}
    algo = KNNBasic(sim_options=sim_options)
    algo.fit(trainset)
    return algo
