import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Read data from csv file
df = pd.read_excel(r"A4\analysis.xlsx", sheet_name="recirc combined")

grid1 = df[df["Grid Number"] == 1]
grid2 = df[df["Grid Number"] == 2]
grid3 = df[df["Grid Number"] == 3]
grid4 = df[df["Grid Number"] == 4]
grid5 = df[df["Grid Number"] == 5]

# Plot all grids on the same plot
plt.figure()
plt.plot(grid1["x"], grid1["y"], "-", label="Grid 1")
plt.plot(grid2["x"], grid2["y"], "--", label="Grid 2")
plt.plot(grid3["x"], grid3["y"], "-.", label="Grid 3")
plt.plot(grid4["x"], grid4["y"], "-", label="Grid 4")
plt.plot(grid5["x"], grid5["y"], "--", label="Grid 5")

# Set the title and labels
plt.xlabel(r"$x$ (m)")
plt.ylabel(r"$u$ (m/s)")
plt.legend()

# Save the plots
plt.savefig(r"A4\Questions\Figures\recirc_combined.png", dpi=300)

# Read more data
df = pd.read_excel(r"A4\analysis.xlsx", sheet_name="per cells")

# Plot recirculation vs cell count
plt.figure()
plt.plot(
    df["cells"],
    df["length"],
    "-o",
    label="Recirculation Length",
    markersize=6,
    markerfacecolor="none",
)

# Set the title and labels
plt.xlabel(r"Number of Cells")
plt.ylabel(r"$L_r$ Recirculation Length (m)")
plt.legend()

# Save the plots
plt.savefig(r"A4\Questions\Figures\recirc_length_vs_cells.png", dpi=300)

# Plot drag coefficient vs cell count
plt.figure()
plt.plot(
    df["cells"],
    df["drag"],
    "-o",
    label="Drag Coefficient",
    markersize=6,
    markerfacecolor="none",
)

# Set the title and labels
plt.xlabel(r"Number of Cells")
plt.ylabel(r"$C_d$ Drag Coefficient")
plt.legend()

# Save the plots
plt.savefig(r"A4\Questions\Figures\drag_coefficient_vs_cells.png", dpi=300)
