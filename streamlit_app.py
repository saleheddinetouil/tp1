import streamlit as st
import matplotlib.pyplot as plt

data = {
    "Courbe 1": {
        "Ant1": "Wifi",
        "Ant2": "Dipole",
        "Freq cte": "500 MHz",
        "PuissanceEntree": "4 dBm",
        "data": {
            "Distance (cm)": [100, 80, 60],
            "Puissance recue (dBm)": [-59, -47, -39]
        }
    },
    # ... Ajoutez d'autres courbes ici ...
}

st.title("Visualisation des données")

fig, ax = plt.subplots()

ax.set_title("Antennes E: Wifi vs. R: Dipole")

for courbe_name, courbe_data in data.items():
    legend_label = f"{courbe_name}: "
    for key, value in courbe_data.items():
        if key != "data":
            legend_label += f"{key}={value}, "
    legend_label = legend_label[:-2]  # Supprimer la dernière virgule et l'espace

    x_data = list(courbe_data["data"].values())[0]
    y_data = list(courbe_data["data"].values())[1]
    ax.plot(x_data, y_data, label=legend_label)

# add constants to the plot to info the user
for courbe_name, courbe_data in data.items():
    for key, value in courbe_data.items():
        if key != "data":
            ax.text(x=0.5, y=0.5, s=f"{key}={value}")
            break

    break

ax.set_xlabel(list(courbe_data["data"].keys())[0])
ax.set_ylabel(list(courbe_data["data"].keys())[1])
ax.legend()
ax.grid(True)

st.pyplot(fig)