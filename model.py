import sqlite3

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect('flood_reports.db')

# Create a table for the flood reports
conn.execute('''CREATE TABLE IF NOT EXISTS flood_reports
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                street_name TEXT,
                city TEXT,
                state TEXT,
                country TEXT,
                severity TEXT,
                date TEXT,
                time TEXT,
                injuries INTEGER,
                fatalities INTEGER,
                property_damage INTEGER,
                infrastructure_damage INTEGER,
                hazards TEXT,
                mitigation_actions TEXT);''')

# Close the connection to the database
conn.close()
