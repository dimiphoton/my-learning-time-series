from kaggle.api.kaggle_api_extended import KaggleApi

api = KaggleApi()
api.authenticate()
datasets = api.dataset_list()
print(datasets)