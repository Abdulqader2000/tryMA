from flask import Flask, render_template, request, redirect, url_for
import pandas as pd

app = Flask(__name__)

# Dummy dataset storage (you can replace this with your database logic)
uploaded_datasets = []

# Maximum number of rows to display
MAX_ROWS_TO_DISPLAY = 10

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for the dataset upload page
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        if file and file.filename.endswith('.csv'):
            # Read and parse the CSV file using pandas
            df = pd.read_csv(file)
            
            # Sample a limited number of rows
            sampled_data = df.head(MAX_ROWS_TO_DISPLAY).values.tolist()

            # Store the uploaded dataset
            uploaded_datasets.append({
                'file_name': file.filename,
                'data': sampled_data,
            })

            return render_template('upload.html', csv_data=sampled_data)

    return render_template('upload.html', csv_data=None)

# Route for the training page (you can add more logic here)
@app.route('/train', methods=['GET', 'POST'])
def train():
    if request.method == 'POST':
        # Process the form data for model training
        # You can add code to train the model here
        pass
    return render_template('train.html')

if __name__ == '__main__':
    app.run(debug=True)
