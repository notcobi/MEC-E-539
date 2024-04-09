import pandas as pd
import matplotlib.pyplot as plt

# Read the data
xl = pd.ExcelFile(r"Final Project\Results Compiled.xlsx")
xl.sheet_names

# filter out the sheetnames with '5545' in them
Re5545Sheets = [sheet for sheet in xl.sheet_names if '5545' in sheet]
Re4000Sheets = [sheet for sheet in xl.sheet_names if '4000' in sheet]

angles = ['25deg', '27.5deg', '30deg', '32.5deg', '35deg']
# Re 5545 plots
plt.figure()
for i, sheet in enumerate(Re5545Sheets):
    df = xl.parse(sheet)
    # Delete any rows with no numbers in the row at all
    df = df.apply(pd.to_numeric, errors='coerce')
    df = df.dropna(how='all')

    plt.plot(df.iloc[:,0], df.iloc[:,1], label= angles[i])

plt.xlabel("$x$, Displacement Along Wall (m)")
plt.ylabel("$P$, Pressure (Pa)")
plt.legend()
plt.title("Pressure vs Displacement Along Wall for Re = 5545")
plt.savefig(r"Final Project\Re5545_Pressure_vs_Displacement.png", dpi=300)

# Re 4000 plots
plt.clf()
plt.figure()
for i, sheet in enumerate(Re4000Sheets):
    df = xl.parse(sheet)
    # Delete any rows with no numbers in the row at all
    df = df.apply(pd.to_numeric, errors='coerce')
    df = df.dropna(how='all')

    # Sort plot by x values in ascending order
    df = df.sort_values(by=[df.columns[0]])

    # Plot the data
    plt.plot(df.iloc[:,0], df.iloc[:,1], label= angles[i])

plt.xlabel("$x$, Displacement Along Wall (m)")
plt.ylabel("$P$, Pressure (Pa)")
plt.legend()
plt.title("Pressure vs Displacement Along Wall for Re = 4000")
plt.savefig(r"Final Project\Re4000_Pressure_vs_Displacement.png", dpi=300)





# # Read the data
# df = pd.read_excel(r"Final Project\Results Compiled.xlsx")
                   
# print('hello world')
# # Plot the data
# datasets = df["dataset"].unique()
# for i, dataset in enumerate(datasets):
#     df_dataset = df[df["dataset"] == dataset]

#     plt.plot(df_dataset["x"], df_dataset["P"], "-", label=dataset)
#     plt.xlabel("x (m)")
#     plt.ylabel("P (Pa)")
#     plt.legend()

# plt.savefig("pressures_vs_x_inlet.png", dpi=300)

