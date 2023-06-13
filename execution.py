'''
This file executes all functions from the main file
'''

# Import packages
from datetime import datetime
from main import *

start_time = datetime.now()

def main():
    """
    Main function of the program. It calls other functions to download, unzip, process and plot raster images.

    Parameters
    ----------
        this functions has no parameters
    --------
    Returns:
        this functions has no return
    --------
    """

    url, path = url_path()
    data_download(url, path)
    unzip(url, path)
    log_scale(path, file_name)
    contrast(con_img)
    plot(path)

    end_time = datetime.now()
    print(f"\n end-time =", end_time - start_time, "Hr:min:sec \n")


# main function
if __name__ == '__main__':
    main()