'''
This file contains all functions that are used for execution
'''

# Import packages
import os
import requests
import zipfile
import os
import glob
import numpy as np
#import rasterio as rio
#from rasterio.plot import show
from matplotlib import pyplot as plt
from matplotlib import colors, cm
from matplotlib.ticker import FormatStrFormatter

def data_download(url, path):
    """
    Function to download data from a given URL to a specified path

    Parameters
    ----------
    url: str
        the online adress from which the data will be downloaded
    path: str
        the local path where the downloaded file and the entire process will be saved
    --------
    Returns:
        this functions has no return
    -------
    Example
    -------
        data_download('https://my_URL_from_unijena.de/file.zip', '/home/user/my_project_folder/')
    """

    file_name = url.rsplit('/', 1)[-1]
    file_path = os.path.join(path, file_name)

    # check if the folder already exist
    if not os.path.isfile(file_path):
        print('the file is being downloaded')
        req = requests.get(url, stream=True)
        with open(file_path, 'wb') as gp:
            for chunk in req.iter_content(chunk_size=128):
                gp.write(chunk)

    else:
        print(f'Download file {file_name} already exists')

def unzip(url, path):
    """
    Function to unzip a file from a given URL to a specified path

    Parameters
    ----------
    url: str
        the URL of the file to be unzipped.
    path: str
        the path where the unzipped file will be saved.
    --------
    Returns:
        this functions has no return
    -------
    Example
    -------
        unzip('https://my_URL.uni-jena/my_URL_from_unijena.zip', '/home/user/my_project_folder/')
    """

    file_name = url.rsplit('/', 1)[-1]
    unzip_folder = file_name.split('.')[0]
    unzip_folder = os.path.join(path, unzip_folder)
    file_name = os.path.join(path, file_name)

    try:
        os.mkdir(unzip_folder)
        with zipfile.ZipFile(file_name, 'r') as zip_ref:
            zip_ref.extractall(unzip_folder)
            if not os.path.isfile(unzip_folder):
                print('Unziping data')

    except FileExistsError:
        if FileExistsError:
            if len(os.listdir(unzip_folder)) == 0:
                print("Directory is empty")
                with zipfile.ZipFile(file_name, 'r') as zip_ref:
                    zip_ref.extractall(unzip_folder)
                    if not os.path.isfile(unzip_folder):
                        print(f'Unziping data')
            else:
                print(f'Folder {unzip_folder} and data already exists')


def contrast(con_img):
    """
    Function for a contrast enhancement to an image represented as a numpy array.

    Parameters
    ----------
    con_img: numpy.ndarray
        the image represented as a numpy array.
    --------
    Returns:
        numpy.ndarray:
            the image represented as a numpy array with a contrast enhancement applied.
    -------
    Example
        contrast(percent_img.ext)
    """

    # calculate min and max values in array
    min = np.nanmin(con_img)
    max = np.nanmax(con_img)

    # calculate percentiles
    percentiles = np.nanpercentile(con_img, (2, 98))
    percent_img = exposure.contrast(con_img,
                                    in_range=tuple(percentiles),
                                    out_range=(min, max))
    return percent_img


def log_scale(path, file_name):
    """
    Function to logarithmically scalling an image represented as a numpy array.

    Parameters
    ----------
    path: str
        the path where the image file is located.
    file_name: str
        the name of the image file.
    --------
    Returns:
        numpy.ndarray (2D of floats): The image represented as a numpy array with a logarithmic scale applied.
    --------
    Example
        log_scale('/home/user/my_project_folder/', 'file_name.ext')
    """

    # read the image as a numpy array
    img_array = img_read(path, file_name)

    # positive-values scale logarithmically
    img_array[img_array != 0] = (np.log10(img_array[img_array > 0])) * 10

    # 0-values represent as nAn
    img_array[img_array == 0] = np.nan
    return img_array


def plot(path):
    """
    Function to plot the data

    path: string: is the local path where the downloaded file and the entire process will be saved
    return:       this functions has no return
    """

    edit_folder = "edited_img"
    raster_path = os.path.join(path, edit_folder)

    file_list = []
    for i, name in enumerate(glob.glob(raster_path + str('/*.tif'))):
        file_list.append(name)
        file_list = [w.replace('\\', '/') for w in file_list]
        file_name = file_list[i].rsplit('/', 1)[-1]

    for j, img in enumerate(file_list):
        raster = rio.open(file_list[j])
        data = raster.read()

        min_per = np.nanpercentile(data, 2)
        max_per = np.nanpercentile(data, 98)

        fig, ax = plt.subplots(figsize=(10, 8))

        title = file_list[j].rsplit('/', 1)[-1]
        title = title[:-4]

        cmap = plt.get_cmap('gist_gray')

        colb = plt.colorbar(cm.ScalarMappable(norm=colors.Normalize(vmin=min_per, vmax=max_per), cmap=cmap))

        ax.set_xlabel('Easting')
        ax.set_ylabel('Northing')
        ax.yaxis.set_major_formatter(FormatStrFormatter('%.0f'))
        colb.set_label('Backscatter in dB')

        show(raster, transform=raster.transform, vmin=min_per, vmax=max_per, ax=ax, cmap=cmap, title=title)
        plt.tight_layout()
        plt.savefig(f'{path}/{title}.pdf', bbox_inches='tight')
        plt.show()

    file_list.clear()


def url_path():
    """
    Prompts the user to enter a URL and a path as strings via the terminal.

    --------
    Returns:
        url: str
            The URL entered by the user.
        path: str
            The path entered by the user.
    --------
    """
    # for the path

    special_characters = "!@#$%^&*()+?=,<>"

    print(f'\nWelcome to our small programme!')
    print(f'First, please define the path of the working directory.')
    print(f'Example path for Windows: "C:/folder_name/"')
    print(f'Note that special characters such as {special_characters} are not allowed in the path name.\n')
    print(f'Type or copy the entire path to the working directory in the terminal/prompt. \n')
    path = input("Enter your folder path: ")

    if any(scpec in special_characters for scpec in path):
        print(f'Path contains special character(s). Please give a new path \n')
        while any(scpec in special_characters for scpec in path):
            path = input()
            if os.path.exists(path):
                print(f'Working directory is valid. \n')
            else:
                if not os.path.exists(path):
                    try:
                        os.makedirs(os.path.dirname(path))
                        print(f'Working directory is created')
                    except FileExistsError:
                        print(f'Working directory already exists.')

    else:
        if os.path.exists(path):
            print(f'Working directory is valid. \n')
        else:
            if not os.path.exists(path):
                try:
                    os.makedirs(os.path.dirname(path))
                    print(f'Working directory is created')
                except FileExistsError:
                    print(f'Working directory already exists.')

    # for the path
    print(f'\nNow please define the URL from which the data will be downloaded!')
    print(f'The URL must ends on ".zip". Otherwise it can not be downloaded. \n')
    url = input("Enter the URL: ")

    return url, path