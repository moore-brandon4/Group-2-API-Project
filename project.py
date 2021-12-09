#python --version
#pip install flask
import requests
import pokepy
import json



# response=requests.get("https://pokeapi.co/api/v2/pokemon/ditto")
# print(response.status_code)

# def jprint(obj):
#     # create a formatted string of the Python JSON object
#     text = json.dumps(obj, sort_keys=True, indent=4)
#     print(text)

# jprint(response.json())


#client = pokepy.V2Client()
#client.get_pokemon()


from flask import Flask, request, jsonify, render_template  
project = Flask(__name__)      



@project.route("/")                          
def index():                    
    return render_template("index.html")

@project.route('/', methods=['POST'])
def index_post():
    variable = request.form['variable']
    urlBeforeString="https://pokeapi.co/api/v2/pokemon/"+variable
    url=str(urlBeforeString)
    print(url)
    response=requests.get(url)
    print(response)
    def jprint(obj):
        text = json.dumps(obj, sort_keys=True, indent=4)
        print(text)
    output=jprint(response.json())
    return render_template("index_post.html")


if __name__=="__main__":
    project.run(debug=True)              