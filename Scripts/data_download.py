import os
import requests


def data_download(url, path):
    """
    Function to download data from a given URL to a specified path.

    Parameters
    ----------
    url: str
        The online address (URL) from which the data will be downloaded.
    path: str
        The local path where the downloaded file and the entire process will be saved.
    --------
    Returns:
        This function has no return.
    -------
    Example
    -------
        data_download('https://my_URL_from_unijena.de/file.zip', '/home/user/my_project_folder/')
    """
    
    # make a name from the original file name without the extension 
    file_name = url.rsplit('/', 1)[-1]
    file_path = os.path.join(path, file_name)

    # check if the folder already exist
    if not os.path.isfile(file_path):
        print('Your file is being downloaded. Grab some snacks, as this will take some time depending on the file size and your internet connection.')
        
        # read the content of the URL Address with stram=True to avoid reading the content at once into memory
        req = requests.get(url, stream=True)
        
        # save what is being downloaded to a file
        with open(file_path, 'wb') as fp:
            for chunk in req.iter_content(chunk_size=128):
                fp.write(chunk)
    else:
        print(f'Download file {file_name} already exists. We can skip this boring step!')
