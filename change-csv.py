import pandas as pd

# Read the CSV file into a pandas DataFrame
df = pd.read_csv("hyd.csv")

# Update Pubchem_status to 0 where Pubchem_cid is blank
df.loc[df['pubchem_cid'].isna(), 'pubchem_status'] = 0
df['pubchem_cid'].fillna('NA', inplace=True)

# Save the updated DataFrame back to the CSV file
df.to_csv("hyd.csv", index=False)

