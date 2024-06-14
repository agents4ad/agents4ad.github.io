"""Extract the relevant data from the openreview export."""

import pandas as pd

# Create an export from openreview, save it as openreview_output.csv or modify the line below

df = pd.read_csv("openreview_output.csv")

# Strip the newlines from the abstracts
df["abstract"] = df["abstract"].str.replace("\n", " ")

# Filter the DataFrame to include only the rows where the "decision" column contains the string "accepted"
accepted_decisions = df[df["decision"].str.contains("accept", case=False)]

# Remove the "accept" from the decision
accepted_decisions["decision"] = (
    accepted_decisions["decision"]
    .str.replace("Accept (Oral)", "Oral")
    .replace("Accept (Poster)", "Poster")
)

# Select the relevant fields from the filtered DataFrame
selected_columns = accepted_decisions[["number", "title", "abstract", "decision"]]

selected_columns.to_csv("homepage_output.csv", index=False)
