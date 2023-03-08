import os
import zipfile
from kaggle.api.kaggle_api_extended import KaggleApi

dic = {
    'interest-rates': {'username': 'federalreserve', 'slug': 'interest-rates'},
    'store-sales-time-series-forecasting': {'username': 'store-sales-time-series-forecasting', 'slug': 'data'}
}

# Initialize the Kaggle API client
api = KaggleApi()
api.authenticate()

# Download the dataset to a temporary file
dataset_name, dataset_info = next(iter(dic.items()))

api.dataset_download_files(dataset_info['username'] + '/' + dataset_info['slug'])
zip_file_path = os.path.join(os.getcwd(), dataset_info['username'] + '.zip')

# Create the output directory
output_dir = os.path.join(os.getcwd(), 'data', dataset_info['slug'])
os.makedirs(output_dir, exist_ok=True)

# Extract the files from the archive into the output directory
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(output_dir)

# Remove the temporary file
os.remove(zip_file_path)
