import os
import zipfile
from kaggle.api.kaggle_api_extended import KaggleApi


main_dic={'interest-rates':{'username':'federalreserve','slug':'interest-rates'},
    'store-sales-time-series-forecasting':{'username':'store-sales-time-series-forecasting','slug':'data'},
    'time-series-data':{'username':'ryanholbrook','slug':'ts-course-data'}}

main_list=list(main_dic.keys())

# Initialize the Kaggle API client
api = KaggleApi()
api.authenticate()

def scrap(quoi):
    # Download the dataset to a temporary file
    dic = main_dic[quoi]
    print('main_dic is read')

    # Move to the "data" directory
    os.chdir('data')
    print('moved to /data')

    # Create the "quoi" directory
    os.makedirs(quoi, exist_ok=True)
    print('created a new directory')
    # Move into the "test" directory
    os.chdir(quoi)
    print('moved to /data/quoi')

    api.dataset_download_files(dic['username'] + '/' + dic['slug'])
    print('api downloaded the file')
    zip_file_path = os.path.join(os.getcwd(), dic['slug']+'.zip')
    print('the zip path is: '+ str(zip_file_path))
    # Extract the files from the archive
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(os.getcwd())

    # Remove the temporary file
    os.remove(zip_file_path)


if __name__ == '__main__':

    print('test: '+main_list[2])
    scrap(main_list[2])
