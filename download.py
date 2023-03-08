import os
import zipfile
from kaggle.api.kaggle_api_extended import KaggleApi

main_dic={'interest-rates':{'username':'federalreserve','slug':'interest-rates'},
    'store-sales-time-series-forecasting':{'username':'store-sales-time-series-forecasting','slug':'data'}}

# Initialize the Kaggle API client
api = KaggleApi()
api.authenticate()

# Download the dataset to a temporary file
quoi, dic = next(iter(main_dic.items()))
print('step 1')

# Move to the "data" directory
os.chdir('data')

# Create the "quoi" directory
os.makedirs(quoi, exist_ok=True)

# Move into the "test" directory
os.chdir(quoi)

api.dataset_download_files(dic['username'] + '/' + dic['slug'])
print('step 2')
zip_file_path = os.path.join(os.getcwd(), dic['slug']+'.zip')
print('step 3')
# Extract the files from the archive
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(os.getcwd())

# Remove the temporary file
os.remove(zip_file_path)
