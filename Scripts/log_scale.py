import numpy as np
import os
import rasterio as rio
import glob


def tiff_log(band_1):
    """
        Function to logarithmically scale an image represented as a numpy array.

        Parameters
        ----------
        band_1: numpy.ndarray
            The first channel from the tiff data.
        --------
        Returns: list
            List with the dB values.
        Example
            logar('/home/user/my_project_folder/', 'file_name.ext')
        """
    
    # make a matrix to put the log data
    db_pixel = []
    
    # convert logarithmically the data
    temp_log = np.log10(band_1) * 10
    temp_log[temp_log == -np.inf] = 'NaN'
    temp_log[temp_log == -0] = -1
    db_res = temp_log
    db_pixel.append(db_res)

    return db_pixel


def edit_tiff(url, path):
    """
        Function to process the data
    
        Parameters
        ----------
        url: str
            the URL of the file to be unzipped.
        path: str
            the path where the unzipped file will be saved.
        --------
        Returns:
            this functions has no return
    """
    
    # make a name from the original file name without the extension
    zip_name = url.rsplit('/', 1)[-1]
    
    # make a folder name from the original file name without the extension
    unzip_folder = zip_name.split('.')[0]
    raster_path = os.path.join(path, unzip_folder)

    samples = []
    for i, name in enumerate(glob.glob(raster_path + str('/*.tif'))):
        samples.append(name)
        samples = [w.replace('\\', '/') for w in samples]
        file_name = samples[i].rsplit('/', 1)[-1]

        # read and write the raster data
        for j, file in enumerate(samples):
            with rio.open(samples[i]) as src:
                band_1 = src.read(1)
                print("Array shape:", band_1.shape)
                band_1 = np.array(band_1)

                np.seterr(divide='ignore', invalid='ignore')

                db_pixel = tiff_log(band_1)

                with rio.open(samples[j]) as src:
                    profile = src.profile

                # Raster data settings from function tiff_log
                profile.update(count=1, dtype=rio.float32, crs="EPSG:32736", nodata=np.nan)

                edited_folder = 'edited_folder'
                edited_folder_path = os.path.join(path, edited_folder)

                if not os.path.isdir(edited_folder_path):
                    print('Start processing...')
                    os.makedirs(edited_folder_path)
                else:
                    print('Great! The output folder exists. We can skip this step too.')

                img_out_name = os.path.join(edited_folder_path, str("in_dB_" + file_name))

                if not os.path.isfile(img_out_name):
                    with rio.open(img_out_name, 'w', **profile) as dst:
                        dst.write(db_pixel[j], 1)
                    print('Exporting Image...')
                else:
                    print('Great! The edited image already exists.')
