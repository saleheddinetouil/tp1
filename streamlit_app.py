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
    "Courbe 2": {
        "Ant1": "Thoraya",
        "Ant2": "Dipole",
        "Freq cte": "500 MHz",
        "Distance": "1 m",
        "data": {
            "Puissance (dBm)": [2, 4, 6, 8, 10],
            "Puissance recue (dBm)": [-67, -58, -52, -46, -35]
        }
    },
    "Courbe 3": {
        "Ant1": "Dipole",
        "Ant2": "Dipole",
        "Freq": "550 MHz",
        "Distance": "1 m",
        "data": {
            "Puissance (dBm)": [4, 6, 8, 10],
            "Puissance recue (dBm)": [-52, -43, -38, -31]
        }
    },
    "Courbe 4": {
        "Ant1": "Dipole",
        "Ant2": "Dipole",
        "Freq cte": "550 MHz",
        "Distance": "1 m",
        "data": {
            "Puissance (dBm)": [4, 6, 8, 10],
            "Puissance recue (dBm)": [-52, -43, -38, -31]
        }
    },
    "Courbe 5": {
        "Ant1": "Dipole", 
        "Ant2": "Dipole",
        "Freq cte" : "550 MHz",
        "Distance cte": "1m",
        "data": {
             "PuissanceEntree (dBm)": [4,6,8,10],
             "Puissance recue (dBm)": [-52, -43, -38, -31]
        }
    },
    "Courbe 6": {
        "Ant1": "Dipole", 
        "Ant2": "Dipole",
        "Puissance cte": "4 dBm",
        "Distance cte": "1m",
        "data": {
             "Freq (MHz)": [550, 650, 750, 850],
             "Puissance recue (dBm)": [-33, -38, -39, -35]
        }
    },
    "Courbe 7": {
        "Ant1": "Dipole", 
        "Ant2": "Dipole",
        "Puissance cte": "4 dBm",
        "Freq cte" : "650 MHz",
        "data": {
             "Distance (m)": [1, 0.8, 0.6, 0.4, 0.2],
             "Puissance recue (dBm)": [-43, -35, -25, -20, -18]
        }
    },
    "Courbe 8": {
        "Ant1": "Yagi", 
        "Ant2": "Dipole",
        "Puissance cte": "4 dBm",
        "Distance cte" : "1m",
        "data": {
             "Freq (MHz)": [750, 850, 950],
             "Puissance recue (dBm)": [-45, -38, -34]
        }
    },
    "Courbe 9": {
        "Ant1": "Yagi", 
        "Ant2": "Dipole",
        "Puissance cte": "0 dBm",
        "Distance cte" : "1m",
        "data": {
             "Freq (MHz)": [550, 650, 750, 850, 950],
             "Puissance recue (dBm)": [-48, -43, -40, -42, -35]
        }
    },
    "Courbe 10": {
        "Ant1": "Yagi", 
        "Ant2": "Dipole",
        "Puissance cte": "0 dBm",
        "Freq cte" : "550 MHz",
        "data": {
             "Distance (m)": [1, 0.8, 0.6, 0.4],
             "Puissance recue (dBm)": [-66, -50, -43, -35]
        }
    },
    "Courbe 11": {
        "Ant1": "Helical", 
        "Ant2": "Loop",
        "Puissance cte": "0 dBm",
        "Freq cte" : "6 GHz",
        "data": {
             "Puissance (dBm)": [10,12],
             "Puissance recue (dBm)": [-43, -37]
        }
    },
    "Courbe 12": {
        "Ant1": "Helical", 
        "Ant2": "Loop",
        "Puissance cte": "6 dBm",
        "Freq cte" : "1.6 GHz",
        "data": {
             "Distance (m)": [1, 0.8, 0.6, 0.4, 0.2],
             "Puissance recue (dBm)": [-52, -54, -47, -29, -29]
        }
    },
    "Courbe 13": {
        "Ant1": "Hauraya", 
        "Ant2": "Loop",
        "Puissance cte": "0 dBm",
        "Distance cte" : "1m",
        "data": {
             "Freq (MHz)": [550, 650, 750, 850, 950],
             "Puissance recue (dBm)": [-60, -48, -69, -71, -43]
        }
    },
    "Courbe 14": {
        "Ant1": "Hauraya", 
        "Ant2": "Loop",
        "Puissance cte": "4 dBm",
        "Distance cte" : "1m",
        "data": {
             "Puissance (dBm)": [2, 4, 6, 8, 10],
             "Puissance recue (dBm)": [-60, -47, -40, -38, -35]
        }
    },
    "Courbe 15": {
        "Ant1": "Hauraya", 
        "Ant2": "Loop",
        "Puissance cte": "4 dBm",
        "Distance cte" : "1m",
        "data": {
             "Freq (MHz)": [100, 200, 300, 400, 500],
             "Puissance recue (dBm)": [-37, -36, -35, -37, -33]
        }
    },
    "Courbe 16": {
        "Ant1": "Hauraya", 
        "Ant2": "Loop",
        "Puissance cte": "4 dBm",
        "Freq cte" : "300 MHz",
        "data": {
             "Distance (m)": [1, 0.8, 0.6, 0.4, 0.2],
             "Puissance recue (dBm)": [-43, -35, -39, -34, -29]
        }
    }
}


for courbe_name, courbe_data in data.items():
    fig, ax = plt.subplots()

    ax.set_title("Antennes E: {} vs. R: {}".format(courbe_data["Ant1"], courbe_data["Ant2"]))

    legend_label = f"{courbe_name}: "
    for key, value in courbe_data.items():
        if key != "data" and key != "Ant1" and key != "Ant2":
            legend_label += f"{key}={value}, "
    legend_label = legend_label[:-2]

    x_data = list(courbe_data["data"].values())[0]
    y_data = list(courbe_data["data"].values())[1]
    ax.plot(x_data, y_data, label=legend_label, marker='o')  # Ajout du marqueur 'o'

    ax.set_xlabel(list(courbe_data["data"].keys())[0])
    ax.set_ylabel(list(courbe_data["data"].keys())[1])
    ax.legend()
    ax.grid(True)

    st.pyplot(fig)