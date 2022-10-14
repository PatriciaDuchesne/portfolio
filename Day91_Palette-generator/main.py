from flask import Flask, render_template, request
from PIL import Image

from palette_generator import get_img_colors

app = Flask(__name__)


@app.route('/', methods=["GET"])
def home():
    return render_template("index.html")


@app.route('/', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['user_img']
        image = Image.open(f)
        colors = get_img_colors(image)
        print(colors)
        return render_template("index.html", colors=colors)


if __name__ == '__main__':
    app.run(debug=True)
