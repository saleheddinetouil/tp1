import streamlit as st
import matplotlib.pyplot as plt

data = {
    "Courbe 1": {
        "Ant1": "wifi",
        "Ant2": "Dipole",
        "Freq cte": "500Mhz",
        "PuissanceEntree": "4 dBm",
        "data": {
            "Distance": [1, 2, 3, 4, 5],
            "Puissance recue": [-10, -15, -20, -25, -30]
        }
    },
    "Courbe 2": {
        "Ant1": "Yagi",
        "Ant2": "Patch",
        "PuissanceEntree cte": "0 dBm",
        "Distance": "1m",
        "data": {
            "Frequence": [400, 450, 500, 550, 600],
            "Puissance recue": [-5, -3, -1, 1, 3]
        }
    },
    # ... Ajoutez d'autres courbes ici ...
}

st.title("Visualisation des données")

fig, ax = plt.subplots()

for courbe_name, courbe_data in data.items():
    legend_label = f"{courbe_name}: "
    for key, value in courbe_data.items():
        if key != "data":
            legend_label += f"{key}={value}, "
    legend_label = legend_label[:-2]  # Supprimer la dernière virgule et l'espace

    x_data = list(courbe_data["data"].values())[0]
    y_data = list(courbe_data["data"].values())[1]
    ax.plot(x_data, y_data, label=legend_label)

ax.set_xlabel(list(courbe_data["data"].keys())[0])
ax.set_ylabel(list(courbe_data["data"].keys())[1])
ax.legend()
ax.grid(True)

st.pyplot(fig)