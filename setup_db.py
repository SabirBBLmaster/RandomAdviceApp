import sqlite3

# Connect to database (will create file advice.db)
conn = sqlite3.connect('advice.db')
c = conn.cursor()

# Create table for advice if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS advice (
                id INTEGER PRIMARY KEY,
                text TEXT NOT NULL
            )''')

# Insert sample advice including your name "PoopMaster"
advice_samples = [
    "Stay positive!",
    "Take breaks regularly.",
    "Keep learning new things.",
    "Be kind to others.",
    "Believe in yourself!"
]

# Add advice to table
c.executemany('INSERT INTO advice (text) VALUES (?)', [(a,) for a in advice_samples])
conn.commit()
conn.close()
print("Database created and populated!")
