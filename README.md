# GEO419A
This project was created as part of the Geo 419A - Modular Programming in Remote Sensing: Python Part I module at Friedrich Schiller University Jena by *Panagiotis Koutsikos* and *Gerasimos Papakostopoulos* and is supervised by *Prof. Dr. Christiane Schmullius*, *Martin Habermeyer*, and *Marco Wolsza*.

___
## Quick Info
The aim of this work was to develop a functional and reproducible application that downloads, extracts and visualises a SAR scene from a zipped folder from a given URL. This could be successfully implemented by using the programming language Python and the following libraries:

| Packages    | *Numpy* | *GDAL* |*Rasterio* |*Requests* |*Matplotlib* |
| ----------- |:-------:|:------:|:---------:|:---------:|:-----------:|
| **Version** |`1.21.5` |`3.0.2` |`1.2.10`   |`2.28.1`   |`3.5.3`      |

This repository contains the following functions:
- Fetching data from a URL `url_path.py`
- Downloading data from given URL to the specified folder `data_download.py`
- Unzipping compressed folder `unzip.py`
- Convertion of the SAR acquisition to a NumPy array and logarithmic scaling of its values `log_scale.py`
- Plotting and saving the visualisation as PDF `plot.py`
- Running all funtions `main.py`

___
## Getting Started
In order to smoothly run the code you may use our predefined python environment `env_PK_GP.yml` file by downloading the file from this repository.
- First you need to create a new environment. Open the Anaconda prompt/terminal, make sure that the `env_PK_GP.yml` file is in the specified directory, and enter the following:

```python
conda env create -f env_PK_GP.yml
```
- Then you can activate the created environment by entering:
```python
conda activate env_PK_GP
```
___
## Running the Code
When you're done creating your environment, you can now run the code in your preferred IDE. Make sure that all files contained in this repository are in the same folder. By running the "main.py" file the code should start and the programme should give the expected outcome.
