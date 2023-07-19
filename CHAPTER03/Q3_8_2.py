import pickle

with open("test1.pkl", "rb") as f:
    result = pickle.load(f)
    print(result)
# リストの１から１０までが表示された
