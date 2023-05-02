# Propagation pattern mining algorithm: a parallel approach

The main objective of this project is to re-implement a centralized state-of-the-art algorithm for spatio-temporal patterns extraction using the distributed Apache Spark framework. Spatio-temporal data refers to data that contains information about the location and time in which the event took place. Throughout this thesis, a public dataset containing information related to traffic and weather events in the USA was considered. This dataset contains approximately 37 million events. Traffic events include congestion, accidents, and construction, while weather events include rain, snow, and storms.

The codebase was developed using **PySpark**, a Python library for big data processing that runs on top of the Apache Spark framework. Spark is a powerful open-source framework for big data processing that allows for fast and efficient data processing and analysis.
Our main objective is to discover cause-and-effect relationships from spatio-temporal data by using the well-known tree-mining algorithm, **SLEUTH**. To achieve this, we first must analyze and process the raw input data to construct an appropriate input for SLEUTH, a Tree DataBase.

To give a broad outline of our approach, the algorithm begins with integrating similar weather and traffic events to remove duplicates. This step is essential to ensure that each event is unique and contributes to the final output. The next step is to search for parent-child correlations between the events. This is crucial because we want to encode the spatio-temporal correlation of events in the form of trees in the next step, which can be used to detect frequent patterns by the SLEUTH algorithm.

To extract frequent patterns from the dataset, we are using SLEUTH, a tree mining algorithm, which is able to extract frequent subtrees from a tree database. In this context, spatio-temporal correlation of events is encoded through tree-based structures according to different space and time constraints. SLEUTH is a sequential algorithm that can handle large datasets and extract patterns in a highly efficient manner.

Dataset is [Large-Scale Traffic and Weather Events Dataset](https://smoosavi.org/datasets/lstw).

The code repository is organized as follows:
- `conf.py`: configuration file containing global variables;
- `create_subset.ipynb`: script to create a subset or the entire dataset;
- `Untitled.ipynb`: script to integrate similar traffic/weather events and to find childs and parents between events;
- `Untitled2.ipynb`: script to create relation trees from the child-parent relationships that have been identified;
- `Untitled3.ipynb`: script to extract frequent patterns (SLEUTH);
- `calc_confidence.ipynb`: script to calculate frequent trees confidence;


To create a subset, use the `create_subset.ipynb` script and use the csv file containing the zip codes of the city you want to analyse.
In `conf.py` don't forget to set `SUBSET` flag. Set it to `True` if you want to use a subset, `False` if you want to use the entire dataset.
Remember to set the minimum support (`min_sup_fixed`), the maximum length of the input trees (`max_tree_length`), the city (`CITY`) and the time threshold used to search for the childs and parents (`trTimeThresh`). These variables must be set in the `conf.py` file.
For extracting frequent patterns, use the `Untitled3.ipynb` script. 
The csv files containing the frequent patterns are saved in the `kdd_lstw_extraction` folder.

The code was tested with Python 3.7.9 and PySpark 2.4

Below are listed some configurations (`CITY` and `min_sup_fixed`) with the respective time taken to run SLEUTH:

**BOSTON**
- 100 - 6h
- 90 - 6h
- 75 - 6h
    
**LOS ANGELES**
- 2000 - 3min
- 1500 - 1h 30min
- 1250 - 1h 30min
- 1100 - 1h 30min
- 1095 - 1h 30min
    
**NEW YORK**
- 1500 - 50s
- 1000 - 41min
- 800 - 41min
- 700 - 49min

