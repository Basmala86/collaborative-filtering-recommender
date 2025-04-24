from surprise import accuracy
from surprise.model_selection import train_test_split
from collections import defaultdict

def compute_rmse(algo, testset):
    predictions = algo.test(testset)
    return accuracy.rmse(predictions, verbose=False)

def get_top_n(predictions, n=10):
    top_n = defaultdict(list)
    for uid, iid, true_r, est, _ in predictions:
        top_n[uid].append((iid, est))
    for uid, user_ratings in top_n.items():
        user_ratings.sort(key=lambda x: x[1], reverse=True)
        top_n[uid] = user_ratings[:n]
    return top_n
