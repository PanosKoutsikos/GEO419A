import os
import glob
import numpy as np
import rasterio as rio
from rasterio.plot import show
from matplotlib import pyplot as plt
from matplotlib import colors, cm
from matplotlib.ticker import FormatStrFormatter
import matplotlib.font_manager as fm
from mpl_toolkits.axes_grid1.anchored_artists import AnchoredSizeBar


def plot(path):
    """
    Function to plot the data.

    Parameters
    ----------
    path: str
        The local path where the downloaded file and the entire process will be saved.
    --------
    Returns:
        This functions has no return.
    """
    # make a folder for the final product
    tiff_folder = "edited_folder"
    tiff_path = os.path.join(path, tiff_folder)

    list_data = []
    for i, name in enumerate(glob.glob(tiff_path + str('/*.tif'))):
        list_data.append(name)
        list_data = [w.replace('\\', '/') for w in list_data]
        file_name = list_data[i].rsplit('/', 1)[-1]

    # open and process (contrast) the files
    for c, val in enumerate(list_data):
        raster = rio.open(list_data[c])
        data = raster.read()

        min_per = np.nanpercentile(data, 2)
        max_per = np.nanpercentile(data, 98)

        fig, ax = plt.subplots(figsize=(16, 12))

        title = list_data[c].rsplit('/', 1)[-1]
        title = title[:-4]

        # choose colormap
        cmap = plt.get_cmap('magma')
        colorbar = plt.colorbar(cm.ScalarMappable(norm=colors.Normalize(vmin=min_per, vmax=max_per), cmap=cmap))

        # set axis labels and ticks
        ax.set_xlabel('Easting', fontsize=15)
        ax.set_ylabel('Northing', fontsize=15)
        plt.xticks(fontsize=14)
        plt.yticks(fontsize=14)
        ax.yaxis.set_major_formatter(FormatStrFormatter('%.0f'))
        colorbar.set_label('VH Backscatter [dB]', fontsize=15)
        colorbar.ax.tick_params(labelsize=14)

        # create scalebar
        fontprops = fm.FontProperties(size=18)
        scalebar = AnchoredSizeBar(ax.transData,
                                   100000, '100 km', 'lower left',
                                   pad=0.5,
                                   borderpad=1,
                                   color='black',
                                   frameon=True,
                                   size_vertical=1,
                                   fontproperties=fontprops)
        ax.add_artist(scalebar)

        # plot the data and save the figure
        show(raster, transform=raster.transform, vmin=min_per, vmax=max_per, ax=ax, cmap=cmap, title=title)
        plt.tight_layout()
        plt.savefig(f'{path}/{title}.png', dpi=300, bbox_inches='tight')
        plt.show()
    list_data.clear()
