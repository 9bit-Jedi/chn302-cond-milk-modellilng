import numpy as np
import matplotlib.pyplot as plt

np.set_printoptions(threshold=np.inf, linewidth=200)

# Constants and parameters
A = 8.07131   # Antoine constant for water
B = 1730.63
C = 233.426

Kb = 0.51     # ebullioscopic constant for water (°C·kg/mol)
i = 1.8       # van't Hoff factor for milk solids

lambda_water = 2257    # Latent heat of vaporization for water at 100C (kJ/kg)
cp = 3.9              # Specific heat capacity of milk (kJ/kg.K)
U = 1.5               # Overall heat transfer coefficient (kW/m2.K)
A_heat = 10           # Heat transfer area (m2)
X0 = 0.12             # Initial concentration (mass fraction of solids)

# Ranges
temps = np.linspace(70, 100, 80)
pressures = np.linspace(10, 50, 80)

# Boiling point elevation (simplified)
def boiling_point_elevation(X):
    m = X * 10  # arbitrary scaling for demonstration
    delta_Tb = Kb * m * i
    return delta_Tb

def antoine_boiling_temp(P_kPa):
    P_mmHg = P_kPa * 7.50062
    return B / (A - np.log10(P_mmHg)) - C

def final_concentration(T_steam, P, F):
    Tb_water = antoine_boiling_temp(P)  # base boiling temp at pressure
    delta_Tb = boiling_point_elevation(X0)  # solute-induced
    T_solution = Tb_water + delta_Tb
    delta_T_LM = T_steam - T_solution

    if delta_T_LM <= 0:
        return X0

    lambda_solution = 0.9 * lambda_water
    m_vapor = (U * A_heat * delta_T_LM) / lambda_solution  # kg/s

    if m_vapor >= F:
        return np.nan  # unphysical

    X_final = X0 / (1 - (m_vapor / F))
    return X_final


# Data for plots
conc_vs_T = [final_concentration(T, 47, 0.5) for T in temps]
conc_vs_P = [final_concentration(80, P, 0.5) for P in pressures]

# Contour data
T_grid, P_grid = np.meshgrid(temps, pressures)
conc_grid = np.zeros_like(T_grid)
for i in range(T_grid.shape[0]):
    for j in range(T_grid.shape[1]):
        conc_grid[i, j] = final_concentration(T_grid[i, j], P_grid[i, j], 1)

# Plot: Concentration vs Temperature
plt.figure()
plt.plot(temps, conc_vs_T, label='Concentration vs Temperature', color='deepskyblue', linewidth=3)
plt.xlabel('Temperature (°C)', fontsize=14)
plt.ylabel('Final Concentration (mass fraction)', fontsize=14)
# plt.title('Final Concentration vs Temperature', fontsize=16)
plt.legend(fontsize=12)
plt.grid(True)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.savefig('conc_vs_temp.png')
plt.close()

# Plot: Concentration vs Pressure
plt.figure()
plt.plot(pressures, conc_vs_P, label='Concentration vs Pressure', color='orange', linewidth=3)
plt.xlabel('Pressure (kPa)', fontsize=14)
plt.ylabel('Final Concentration (mass fraction)', fontsize=14)
# plt.title('Final Concentration vs Pressure', fontsize=16)
plt.legend(fontsize=12)
plt.grid(True)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.savefig('conc_vs_pressure.png')
plt.close()

# Contour plot: Concentration vs Temperature and Pressure
plt.figure()
contour = plt.contourf(T_grid, P_grid, conc_grid, levels=1000, cmap='viridis')
plt.colorbar(contour, label='Final Concentration (mass fraction)')
plt.xlabel('Temperature (°C)')
plt.ylabel('Pressure (kPa)')
# plt.title('Contour Plot of Final Concentration vs Temperature and Pressure')
plt.grid(True)
plt.savefig('conc_grid_contour.png')
plt.close()

# Print results
print("Concentration vs Temperature:")
print(conc_vs_T)

print("\nConcentration vs Pressure:")
print(conc_vs_P)

print("\nConcentration Grid (Contour Data):")
print(conc_grid)