import pandas as pd
import matplotlib.pyplot as plt

# Load CSV
df = pd.read_excel("HammerTipVelocity_Kpvot_100.xlsx")

# Plot
df["Hammer tip reference bezier velocity [m/s]_x"] = pd.to_numeric(df["Hammer tip reference bezier velocity [m/s]_x"], errors="coerce")
df["Hammer tip reference bezier velocity [m/s]_y"] = pd.to_numeric(df["Hammer tip reference bezier velocity [m/s]_y"], errors="coerce")
df["Hammer tip reference bezier velocity [m/s]_z"] = pd.to_numeric(df["Hammer tip reference bezier velocity [m/s]_z"], errors="coerce")
df["Hammer tip velocity [m/s]_x"] = pd.to_numeric(df["Hammer tip velocity [m/s]_x"], errors="coerce")
df["Hammer tip velocity [m/s]_y"] = pd.to_numeric(df["Hammer tip velocity [m/s]_y"], errors="coerce")
df["Hammer tip velocity [m/s]_z"] = pd.to_numeric(df["Hammer tip velocity [m/s]_z"], errors="coerce")

df = df[df["Hammer tip reference bezier velocity [m/s]_x"] != 0]
df = df[df["Hammer tip reference bezier velocity [m/s]_y"] != 0]
df = df[df["Hammer tip reference bezier velocity [m/s]_z"] != 0]
df = df[df["Hammer tip velocity [m/s]_x"] != 0]
df = df[df["Hammer tip velocity [m/s]_y"] != 0]
df = df[df["Hammer tip velocity [m/s]_z"] != 0]


t = [0.002*i for i in range(508)]
plt.plot(t, df["Hammer tip reference bezier velocity [m/s]_x"], label="Hammer tip reference bezier velocity [m/s]_x")
plt.plot(t, df["Hammer tip reference bezier velocity [m/s]_y"], label="Hammer tip reference bezier velocity [m/s]_y")
plt.plot(t, df["Hammer tip reference bezier velocity [m/s]_z"], label="Hammer tip reference bezier velocity [m/s]_z")
plt.plot(t, df["Hammer tip velocity [m/s]_x"], label="Hammer tip velocity [m/s]_x")
plt.plot(t, df["Hammer tip velocity [m/s]_y"], label="Hammer tip velocity [m/s]_y")
plt.plot(t, df["Hammer tip velocity [m/s]_z"], label="Hammer tip velocity [m/s]_z")



# Labels & title
plt.xlabel("Time [s]")
plt.ylabel("Hammer tip velocity [m/s]")
plt.title("Hammer tip velocity with respect to time, Kp_VOT = 100")

# Rotate x labels if needed
# plt.xticks(rotation=45)
plt.legend()

plt.tight_layout()
plt.grid(True)

plt.show()