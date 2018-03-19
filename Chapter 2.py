import os
import tarfile
import pandas as pd

from six.moves import urllib

downloadRoot = "https://raw.githubusercontent.com/ageron/handson-ml/master/"
housing_Path = os.path.join("datasets", "housing")
housing_URL = downloadRoot + "datasets/housing/housing.tgz"

def fetchHousingData(housingURL = housing_URL, housingPath = housing_Path):
    if not os.path.isdir(housingPath):
        os.makedirs(housingPath)
    tgzPath = os.path.join(housingPath, "housing.tgz")
    urllib.request.urlretrieve(housingURL, tgzPath)
    housingTGZ = tarfile.open(tgzPath)
    housingTGZ.extractall(path=housingPath)
    housingTGZ.close()

def loadHousingData(housingPath = housing_Path):
    csvPath = os.path.join(housingPath, "housing.csv")
    return pd.read_csv(csvPath)

fetchHousingData()
housing = loadHousingData()
print(housing.head())
print(housing.info())
print(housing["ocean_proximity"].value_counts())
print(housing.describe())