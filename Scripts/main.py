from data_download import data_download
from url_path import url_path
from unzip import unzip
from log_scale import edit_tiff
from plot import plot


def main():
    """
    Main function of the program. It calls functions to download, unzip, process and plot raster images.

    Parameters
    ----------
        this functions has no parameters
    --------
    Returns:
        this functions has no return
    --------
    """
    # call the functions 
    url, path = url_path()
    file_name = data_download(url, path)
    unzip(url, path)
    edit_tiff(url, path)
    plot(path)


# check if this file has been called as script
if __name__ == '__main__':
    main()
