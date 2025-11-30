from flask import Flask, render_template  # Flask framework and template rendering
import sqlite3                           # SQLite for database
import random                            # Random module to pick advice

app = Flask(__name__)                    # Initialize Flask app

# Function to get a random piece of advice from database
def get_random_advice():
    conn = sqlite3.connect('advice.db')  # Connect to SQLite database
    c = conn.cursor()                    # Cursor to execute SQL
    c.execute("SELECT text FROM advice") # Retrieve all advice
    advice_list = [row[0] for row in c.fetchall()]  # Convert results to list
    conn.close()                         # Close connection
    return random.choice(advice_list)    # Return random advice

# Route for home page
@app.route('/')
def home():
    advice = get_random_advice()                   # Get random advice
    return render_template('index.html', advice=advice)  # Send to HTML template

# Run app directly
if __name__ == '__main__':
    app.run()
