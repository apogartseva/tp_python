import pandas as pd

file_path_2018 = "DAT_XLSX_EURUSD_M1_2018.xlsx"
file_path_2019 = "DAT_XLSX_EURUSD_M1_2019.xlsx"

df_2018 = pd.read_excel(file_path_2018)
df_2019 = pd.read_excel(file_path_2019)

df = pd.concat([df_2018, df_2019], ignore_index=True)
csv_file_path = "DAT_XLSX_EURUSD_M1.csv"
df.to_csv(csv_file_path, index=False)
print(f"Données concatenées sont dans {csv_file_path}")
