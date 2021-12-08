#python --version
#pip install flask
import requests
import pokepy
import json


response=requests.get("https://pokeapi.co/api/v2/pokemon/ditto")
print(response.status_code)

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

jprint(response.json())


#client = pokepy.V2Client()
#client.get_pokemon()


# from flask import Flask, render_template  
# project = Flask(__name__)      



# @project.route("/")                          
# def index():                    
#     return render_template("index.html")



# if __name__=="__main__":
#     project.run(debug=True)              