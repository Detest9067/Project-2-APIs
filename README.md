# Project-2- Data Pipelines

## Overview
For this project I wanted to explore the relationship of causation with correlation. I thought it might be interesting to find two completely unrelated data sets and see if I could try and graphically demonstrate some correlations without cause.

### Datasets used:
* Significant Volcanic Eruption Database API: </br>
https://public.opendatasoft.com/explore/dataset/significant-volcanic-eruption-database/api/?sort=vei&dataChart=eyJxdWVyaWVzIjpbeyJjb25maWciOnsiZGF0YXNldCI6InNpZ25pZmljYW50LXZvbGNhbmljLWVydXB0aW9uLWRhdGFiYXNlIiwib3B0aW9ucyI6eyJzb3J0IjoidmVpIn19LCJjaGFydHMiOlt7ImFsaWduTW9udGgiOnRydWUsInR5cGUiOiJjb2x1bW4iLCJmdW5jIjoiQVZHIiwieUF4aXMiOiJ5ZWFyIiwic2NpZW50aWZpY0Rpc3BsYXkiOnRydWUsImNvbG9yIjoiI0ZGNTE1QSJ9XSwieEF4aXMiOiJ0c3UiLCJtYXhwb2ludHMiOjUwLCJzb3J0IjoiIn1dLCJ0aW1lc2NhbGUiOiIiLCJkaXNwbGF5TGVnZW5kIjp0cnVlLCJhbGlnbk1vbnRoIjp0cnVlfQ%3D%3D
* FIFA World Cup Data Set: </br>
https://www.kaggle.com/datasets/iamsouravbanerjee/fifa-football-world-cup-dataset?resource=download

### Languages/Dependencies
This project was written using Python and Jupyter Notebooks.
Required dependencies: </br>
* Seaborn
* Numpy
* Pandas
* Scipy.stats
* Matplotlib.pyplot
* Typing
* Requests
* Json

## Data Processing
I used the Opendatasoft API to create a JSON of the database, and immediately converted the JSON to CSV for easier processing.

Then I trimmed down some of the irrelvant columnns/columns with NaN values and created a separate merged csv to run correlation analysis

## Data Analysis
Using the seaborn and matplotlib libraries, I created a number of visualizations to illustrate the apparent relationship between volcano eruptions and occurances of the world cup. 

I also ran a pearson r statistical analysis and visualized all of the variable relationships that were statistically significant.

## Results
