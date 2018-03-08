from flask import Flask, render_template, request
import pandas as pd
from StringIO import StringIO

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "/home/keo7/Data/dimspy-web/"


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        metadata_file = request.files["metadata"]
        if metadata_file.filename.endswith(".csv"):
            metadata = pd.read_csv(StringIO(metadata_file.read()), index_col=1)
            print metadata
    return render_template("index.html")
