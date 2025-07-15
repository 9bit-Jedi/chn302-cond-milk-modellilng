import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Create figure and axis
fig, ax = plt.subplots(figsize=(10, 7))

# Draw evaporator
evaporator = patches.Rectangle((3.6, 2.8), 2, 2, edgecolor='black', facecolor='lightblue', label="Evaporator", linewidth=2)
ax.add_patch(evaporator)
ax.text(4.6, 3.8, "Evaporator", ha="center", fontsize=14, fontweight="bold", color="black")

# Draw feed input arrow
ax.arrow(2, 4, 1.3, 0, head_width=0.2, head_length=0.3, fc='darkblue', ec='darkblue', linewidth=1.5)
ax.text(1.5, 4.2, "Milk Feed", fontsize=12, color="darkblue", fontweight="bold")

# Draw steam input arrow
ax.arrow(4.5, 5.8, 0, -0.8, head_width=0.2, head_length=0.3, fc='darkgreen', ec='darkgreen', linewidth=1.5)
ax.text(4.7, 6, "Steam", fontsize=12, color="darkgreen", fontweight="bold")

# Draw evaporated water output arrow
ax.arrow(4.5, 3, 0, -0.8, head_width=0.2, head_length=0.3, fc='darkred', ec='darkred', linewidth=1.5)
ax.text(4.7, 2, "Evaporated Water", fontsize=12, color="darkred", fontweight="bold")

# Draw concentrated milk output arrow
ax.arrow(5.5, 4, 1.3, 0, head_width=0.2, head_length=0.3, fc='purple', ec='purple', linewidth=1.5)
ax.text(6.9, 4.2, "Concentrated Milk", fontsize=12, color="purple", fontweight="bold")

# Labels and styling
ax.set_xlim(0, 8)
ax.set_ylim(0, 7)
ax.set_xticks([])
ax.set_yticks([])
ax.set_frame_on(False)

# Add title
ax.set_title("Evaporator Schematic", fontsize=16, fontweight="bold", color="black", pad=20)

# Save schematic as PDF
plt.savefig("./evaporator_schematic_stylized.pdf", format="pdf", bbox_inches="tight")

# Show the schematic
plt.show()
