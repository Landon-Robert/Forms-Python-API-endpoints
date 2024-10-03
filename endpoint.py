from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/question", methods=['POST'])
def endpoint():
    data = request.form
    print(data)
    output = f"""
<!doctype html>
<head>
    <title> Form Result </title>
    <style>
        .result {{
        color: blue;
        font-size: 2em;
        }}
    </style>
</head>
<body>
    <h2 style='color:blue;'>Hello, {data['fname']}</h2>"
    You have successfully sent data to a form!
</body>
    """
    return output

@app.route("/", methods=['POST'])
def anotherfunction():
    pass

app.run(port=42069)