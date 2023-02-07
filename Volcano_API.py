import requests
import pandas as pd

url = "https://public.opendatasoft.com/api/records/1.0/search/?dataset=significant-volcanic-eruption-database&q=deaths&rows=500&sort=vei&facet=year&facet=tsu&facet=eq&facet=name&facet=location&facet=country&facet=type&facet=status&facet=deaths_description&facet=missing_description&facet=injuries_description&facet=damage_description&facet=houses_destroyed_description&facet=total_deaths_description&facet=total_missing_description&facet=total_injuries_description&facet=total_damage_description&facet=total_houses_destroyed_description&facet=houses_damaged_description"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    records = data["records"]
    volcano_df = pd.json_normalize(records)
    volcano_df.to_csv("data/volcano_data.csv", index=False)
else:
    print("Failed to retrieve data")
