from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import requests
import json
app = Flask(__name__)



@app.route("/pokemon")
def server_info():
    cors = CORS(app, resources={"/pokemon/*": {"origins": "*"}})
    idpok = request.args.get("id")
    url = "https://pokeapi.co/api/v2/pokemon/"+idpok
    headers = {
    
    }
    response = requests.request("GET", url, headers=headers)
    persona=[
        {"Hola":"hola"}
    ]
    json_object = json.loads(str((response.text)))
    name = json_object["name"]
    sprites = json.loads(json.dumps(json_object["sprites"]))
    other = json.loads(json.dumps(sprites["other"]))
    dream_world = other["dream_world"]
    urlimage = dream_world["front_default"]
    outv={
        "name":name,
        "image":urlimage
    }
    return outv

if __name__=="__main__":
    app.run()