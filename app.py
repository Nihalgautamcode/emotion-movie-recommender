from flask import Flask, request, render_template
import pandas as pd
import random

app = Flask(__name__)

# Load dataset
df = pd.read_csv('movies.csv')

@app.route('/', methods=['GET', 'POST'])
def home():
    recommendations = []
    if request.method == 'POST':
        emotion = request.form['emotion'].lower()
        if emotion in df['emotion'].unique():
            movies = df[df['emotion'] == emotion]['movie'].tolist()
            recommendations = random.sample(movies, min(3, len(movies)))
        else:
            recommendations = ["Sorry, no recommendations available for that emotion."]
    return render_template('index.html', recommendations=recommendations)

if __name__ == '__main__':
    app.run()
