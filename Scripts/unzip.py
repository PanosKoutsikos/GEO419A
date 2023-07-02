import zipfile
import os


def unzip(url, path):
    """
    Function to unzip a file from a given URL to a specified path.

    Parameters
    ----------
    url: str
        The URL of the file to be unzipped.
    path: str
        The path where the unzipped file will be saved.
    --------
    Returns:
        This functions has no return.
    -------
    Example
    -------
        unzip('https://my_URL.uni-jena/my_URL_from_unijena.zip', '/home/user/my_project_folder/')
    """
    
    # make a name from the original file name without the extension
    file_name = url.rsplit('/', 1)[-1]

    # make a folder name from the original file name without the extension
    unzip_folder = file_name.split('.')[0]
    
    # make a new folder for the unziped data
    unzip_folder = os.path.join(path, unzip_folder)
    file_name = os.path.join(path, file_name)

    # unzip data
    try:
        os.mkdir(unzip_folder)
        with zipfile.ZipFile(file_name, 'r') as zip_ref:
            zip_ref.extractall(unzip_folder)
            if not os.path.isfile(unzip_folder):
                print('Unzipping data... This may take a few minutes.')

    
    # checking if a file exists
    except FileExistsError:
        if FileExistsError:
            if len(os.listdir(unzip_folder)) == 0:
                print('This directory is empty.')
                with zipfile.ZipFile(file_name, 'r') as zip_ref:
                    zip_ref.extractall(unzip_folder)
                    if not os.path.isfile(unzip_folder):
                        print('Unzipping data... This may take a few minutes.')
            else:
                print(f'Great! This folder {unzip_folder} and data already exists.')
