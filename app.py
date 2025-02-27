from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

# Function to format the joined date
def format_date_joined(date):
    return date.strftime("%B, %Y")

@app.route('/profile')
def profile():
    user = {
        "photo": "ARowe.jpg", 
        "full_name": "Ayesha Rowe",
        "username": "@AyeshaRowe",
        "location": "St. Catherine, Jamaica",
        "date_joined": format_date_joined(datetime(2020, 1, 1)),
        "bio": "My name is Ayesha Rowe and I am a computer science student working on multiple software project like FastPres and PanForge. I like playing card games like uno. Outside of school and games, I have a dog named Oreo and enjoy sweet and spicy foods like ice cream and sweet and spicy chicken.",
        "posts": 7,
        "followers": 250,
        "following": 100
    }
    return render_template("profile.html", user=user)

if __name__ == '__main__':
    app.run(debug=True)