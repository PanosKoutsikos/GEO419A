# GEO419A
This project was created as part of the Geo 419A - Modular Programming in Remote Sensing: Python Part I module at Friedrich Schiller University Jena by ***Panagiotis Koutsikos*** and ***Gerasimos Papakostopoulos*** and is supervised by ***Prof. Dr. Christiane Schmullius***, ***Martin Habermeyer***, and ***Marco Wolsza***.

___
## Quick Info
The aim of this work was to develop a functional and reproducible application that downloads, extracts and visualises a SAR scene from a zipped folder from a given URL. This could be successfully implemented by using the programming language Python and the following libraries:

| Packages    | *Numpy* | *GDAL* |*Rasterio* |*Requests* |*Matplotlib* |
| ----------- |:-------:|:------:|:---------:|:---------:|:-----------:|
| **Version** |`1.25.0` |`3.7.0` |`1.3.7`    |`2.31.0`   |`3.7.1`      |

This repository contains the following functions:
- Fetching data from a URL `url_path.py`
- Downloading data from given URL to the specified folder `data_download.py`
- Unzipping compressed folder `unzip.py`
- Convertion of the SAR acquisition to a NumPy array and logarithmic scaling of its values `log_scale.py`
- Plotting and saving the visualisation as PNG `plot.py`
- Running all funtions `main.py`

___
## Getting Started
In order to smoothly run the code you may use our predefined python environment `GEO419A_env.yml` file by downloading the file from this repository.
- First you need to create a new environment. Open the Anaconda prompt/terminal, make sure that the `GEO419A_env.yml` file is in the specified directory, and enter the following:

```python
conda env create -f GEO419A_env.yml
```
- Then you can activate the created environment by entering:
```python
conda activate GEO419A_env
```
___
## Running the Code
When you're done creating your environment, you can now run the code in your preferred IDE. Make sure that all files contained in this repository are in the same folder. By running the "main.py" file the code should start and the programme should produce a visualisation of the data. \
\
Additionally, there is also the possibility of running the code through the terminal. In order to do so, first navigate to the folder where the script is located using the following code:
```python
cd "C:\Your\Path"
```
You can then run the programme by executing the following:
```python
$ python main.py
```
