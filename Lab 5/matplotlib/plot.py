import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Read data from csv file
df = pd.read_excel(r"Lab 5\matplotlib\data.xlsx")

# Plot Pressure Data
plt.figure()
x = df[df["Dataset"] == "Pressure"]["Iteration"]
y = df[df["Dataset"] == "Pressure"]["Quantity"]

plt.plot(x, y, "-", label="Pressure", markersize=6, markerfacecolor="none")
plt.xlabel("Iteration")
plt.ylabel("Pressure (Pa)")
plt.savefig(r"Lab 5\Questions\Figures\Pressure.png", dpi=300)

# Plot Y-Velocity Data
plt.figure()
x = df[df["Dataset"] == "Y Velocity"]["Iteration"]
y = df[df["Dataset"] == "Y Velocity"]["Quantity"]

plt.plot(x, y, "-", label="Y-Velocity", markersize=6, markerfacecolor="none")
plt.xlabel("Iteration")
plt.ylabel("Y-Velocity (m/s)")
plt.savefig(r"Lab 5\Questions\Figures\Y-Velocity.png", dpi=300)

# Plot X-Velocity Data
plt.figure()
x = df[df["Dataset"] == "X Velocity"]["Iteration"]
y = df[df["Dataset"] == "X Velocity"]["Quantity"]

plt.plot(x, y, "-", label="X-Velocity", markersize=6, markerfacecolor="none")
plt.xlabel("Iteration")
plt.ylabel("X-Velocity (m/s)")
plt.savefig(r"Lab 5\Questions\Figures\X-Velocity.png", dpi=300)

# Plot TKE Data
plt.figure()
x = df[df["Dataset"] == "TKE"]["Iteration"]
y = df[df["Dataset"] == "TKE"]["Quantity"]

plt.plot(
    x, y, "-", label="Turblent Kinetic Energy", markersize=6, markerfacecolor="none"
)
plt.xlabel("Iteration")
plt.yscale("log")
plt.ylabel("Turblent Kinetic Energy ($m^2/s^2$)")
plt.savefig(r"Lab 5\Questions\Figures\TKE.png", dpi=300)

# # Remove the 'STDEV', 'T-INV (or Z-Inv)' 'Accuracy' columns
# df = df.drop(['STDEV', 'T-INV (or Z-Inv)', 'Accuracy'], axis=1)

# # Sort 'device' == 'Micrometer'
# df_micrometer = df[df['Device'] == 'Micrometer']
# df_vernier = df[df['Device'] == 'Vernier Caliper']
# df_digital = df[df['Device'] == 'Digital Caliper']

# # Plot the data
# plt.plot(df_micrometer['n'], df_micrometer['P'], '-o', label='Micrometer', markersize=6, markerfacecolor='none')
# plt.plot(df_vernier['n'], df_vernier['P'], '-s', label='Vernier Caliper', markersize=6, markerfacecolor='none')
# plt.plot(df_digital['n'], df_digital['P'], '-^', label='Digital Caliper', markersize=6, markerfacecolor='none')


# # Set the title and labels
# plt.xlabel(r'$n$, Number of Measurements')
# plt.ylabel(r'$P_{x}$, Precision (mm)')
# plt.legend()

# # Set x-axis ticks to integer values with tick mark rotation
# plt.xticks(np.arange(df['n'].min(), df['n'].max()+1, 1), rotation=45, ha = 'left')

# # Save the plots
# plt.savefig('Q3_Precision.png', dpi=300)

# # Make new plot
# plt.figure()
# plt.plot(df_micrometer['n'], df_micrometer['U'], '-o', label='Micrometer', markersize=6, markerfacecolor='none')
# plt.plot(df_vernier['n'], df_vernier['U'], '-s', label='Vernier Caliper', markersize=6, markerfacecolor='none')
# plt.plot(df_digital['n'], df_digital['U'], '-^', label='Digital Caliper', markersize=6, markerfacecolor='none')

# # Set the title and labels
# plt.xlabel(r'$n$, Number of Measurements')
# plt.ylabel(r'$U_{x}$, Uncertainty (mm)')
# plt.legend()

# # Set x-axis ticks to integer values with tick mark rotation
# plt.xticks(np.arange(df['n'].min(), df['n'].max()+1, 1), rotation=45, ha = 'left')

# # Save the plots
# plt.savefig('Q3_Uncertainty.png', dpi=300)

# # Show the plot
# plt.show()
