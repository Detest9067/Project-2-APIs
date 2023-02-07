import requests
import pandas as pd
import json

#Call API, format data to produce CSV
def retrieve_volcano_data(url: str, file_path: str) -> None:
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        records = data["records"]
        volcano_df = pd.json_normalize(records)
        volcano_df.to_csv(file_path, index=False)
    else:
        print("Failed to retrieve data")

url = "https://public.opendatasoft.com/api/records/1.0/search/?dataset=significant-volcanic-eruption-database&q=deaths&rows=500&sort=vei&facet=year&facet=tsu&facet=eq&facet=name&facet=location&facet=country&facet=type&facet=status&facet=deaths_description&facet=missing_description&facet=injuries_description&facet=damage_description&facet=houses_destroyed_description&facet=total_deaths_description&facet=total_missing_description&facet=total_injuries_description&facet=total_damage_description&facet=total_houses_destroyed_description&facet=houses_damaged_description"
file_path = "data/volcano_data.csv"

retrieve_volcano_data(url, file_path)

#load in data for volcano/world cup
def load_world_cup_data():
    # World Cup data into dataframe
    world_cup_df = pd.read_csv("data/FIFA - World Cup Summary.csv")
    # Format YEAR as string with only the year
    world_cup_df["YEAR"] = world_cup_df["YEAR"].astype(str).str[:4]
    return world_cup_df

def load_volcano_data():
    #Volcano data into dataframe
    volcano_df = pd.read_csv("data/volcano_data.csv")
    return volcano_df

def clean_volcano_data(volcano_df):
    volcano_df = pd.read_csv("data/volcano_data.csv")
    #Removing unwanted columns
    volcano_df = volcano_df.drop(columns=["datasetid", "recordid", "record_timestamp", "fields.elevation", "fields.missing", "fields.total_missing","fields.total_houses_destroyed_description", "fields.total_deaths_description", "fields.total_missing_description", "fields.total_injuries","fields.total_damage_millions_dollars","fields.missing_description", "fields.total_houses_destroyed"])
    #dropping NaN values in VEI column
    volcano_df = volcano_df.dropna(subset=["fields.vei"])
    #removing entries before the first world cup
    volcano_df = volcano_df[volcano_df['fields.year'] >= 1930]
    #sort by year ascending
    volcano_df = volcano_df.sort_values(by='fields.year')
    #resetting index
    volcano_df.reset_index(drop=True, inplace=True)
    return volcano_df

def create_world_cup_year_column(volcano_df):
    # List of World Cup years
    world_cup_years = [1930, 1934, 1938, 1950, 1954, 1958, 1962, 1966, 1970, 1974, 1978, 1982, 1986, 1990, 1994, 1998, 2002, 2006, 2010, 2014, 2018, 2022]
    #creating a new column with binary values 
    volcano_df['World_Cup_Year'] = volcano_df['fields.year'].isin(world_cup_years)
    volcano_df.to_csv("data/volcanoes_updated.csv", index=False)

    return volcano_df

def create_new_dataframes(volcano_df):
    #creating new df for true and false WC_YEAR values
    volcano_true_df = volcano_df.loc[volcano_df["World_Cup_Year"] == True]
    volcano_false_df = volcano_df.loc[volcano_df["World_Cup_Year"] == False]
    volcano_true_df.to_csv("data/volcanoes_true.csv", index=False)
    volcano_false_df.to_csv("data/volcanoes_false.csv", index=False)
    
    
    return volcano_true_df, volcano_false_df

def create_merged_dataframe(volcano_df, world_cup_df):
    #adding a key_column with a value of 1 in every row in both data frames to facilitate an inner merge
    volcano_df['key_column'] = volcano_df.notnull().astype(int).sum(axis=1) > 0
    world

    merged_df.to_csv("data/merged_df.csv", index=False)
