from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    location = request.form['Location']
    timestamp = request.form['timestamp']
    # Here you would put your actual prediction code
    predicted_crime = "Act - 279 Accident"
    return render_template('prediction.html', predicted_crime=predicted_crime)

if __name__ == '__main__':
    app.run(debug=True)
