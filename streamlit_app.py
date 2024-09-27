import streamlit as st
import matplotlib.pyplot as plt

data = {
    "Puissance, Puissance recue": [
        {"Puissance emise (dBm)": 0, "Puissance recue (dBm)": -50},
        {"Puissance emise (dBm)": 10, "Puissance recue (dBm)": -40},
        {"Puissance emise (dBm)": 20, "Puissance recue (dBm)": -30},
    ],
    "Frequence, Puissance recue": [
        {"Frequence (GHz)": 2.4, "Puissance recue (dBm)": -60},
        {"Frequence (GHz)": 2.5, "Puissance recue (dBm)": -55},
        {"Frequence (GHz)": 2.6, "Puissance recue (dBm)": -50},
    ],
    "Distance, Frequence recue": [
        {"Distance (m)": 1, "Frequence recue (GHz)": 2.45},
        {"Distance (m)": 2, "Frequence recue (GHz)": 2.44},
        {"Distance (m)": 3, "Frequence recue (GHz)": 2.43},
    ],
}

fig, ax = plt.subplots()

for title, dataset in data.items():
    x_values = [list(row.values())[0] for row in dataset]
    y_values = [list(row.values())[1] for row in dataset]
    
    # Extraire les noms des clés pour la légende
    x_label = list(dataset[0].keys())[0]
    y_label = list(dataset[0].keys())[1]

    ax.plot(x_values, y_values, label=f"{title} ({x_label} vs {y_label})")

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.legend()
ax.grid(True)

st.pyplot(fig)