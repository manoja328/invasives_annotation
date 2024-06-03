from flask import Flask, request, jsonify, render_template, send_from_directory
import os

app = Flask(__name__)

# Ensure the 'static' folder contains your images
@app.route('/')
def index():
    images = os.listdir('static')
    return render_template('index.html', images=images, total_images=len(images))

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    print(f"Received bounding boxes: {data}")
    return jsonify({'status': 'success', 'data': data})

if __name__ == '__main__':
    app.run(debug=True)
