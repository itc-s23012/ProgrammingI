import pickle

with open("test1.pkl", "wb") as f:
    a = list(range(1, 11))
    pickle.dump(a, f)
# test1.pkl に書き込む
