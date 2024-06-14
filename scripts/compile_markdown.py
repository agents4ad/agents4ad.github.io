"""Compile the yaml structure of the papers for the markdown file."""

import pandas as pd
import yaml

# Add the authors to the csv manually (in Excel) prior to using this script

df = pd.read_csv("homepage_output2.csv", delimiter=";")

# Convert the dataframe to a dictionary
df_dict = df.to_dict(orient="records")

# Convert the dictionary to YAML
yaml_data = yaml.dump(df_dict, allow_unicode=True, encoding="utf-8")
yaml_str = yaml_data.decode("utf-8")

with open("homepage_output.yaml", "w", encoding="utf-8") as file:
    file.write(yaml_str)
