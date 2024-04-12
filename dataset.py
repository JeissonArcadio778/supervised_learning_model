import pandas as pd

data = {
    "ID": [1, 2, 3, 4],
    "Time of Day": ["8:00", "12:00", "18:00", "21:00"],
    "Day of the Week": ["Monday", "Tuesday", "Friday", "Sunday"],
    "Season of the Year": ["Summer", "Winter", "Spring", "Autumn"],
    "Number of Passengers": [250, 150, 300, 100]
}

sample_dataset = pd.DataFrame(data)


knowledge_base = {
    "conexiones": {
        "X": [("Y", 4), ("Z", 2)],
        "Y": [("W", 3)],
        "Z": [("W", 5), ("V", 7)],
        "W": [("T", 6)],
        "V": [("T", 4)],
        "T": []
    }
}
