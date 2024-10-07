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
    <p>One day, {data['fname']} left their house and went to the {data['location1']}. While they were there, they {data['pasttenseverb1']} several {data['pluralobject']}. After a {data['Adjective']} day, {data['fname']} went home and {data['verb']}.</p>"
</body>
    """
    return output

@app.route("/", methods=['POST'])
def anotherfunction():
    pass

app.run(port=42069)