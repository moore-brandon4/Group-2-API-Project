#python --version
#pip install flask
import requests
#import pokepy
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

@project.route('/', methods=['GET', 'POST'])
def index_post():
    #Form that takes user variable from html and creates the url to send to the api
    variable = request.form['variable']
    urlBeforeString="https://pokeapi.co/api/v2/pokemon/"+variable
    url=str(urlBeforeString)
    print(url)
    #response=requests.get(url)

    #Gets the url data from the api and prints the json data onto the post html page
    r = requests.get(url)
    pretty_json = json.loads(r.text)
    results4 = pretty_json["forms"][0]["name"]
    #print("Results for: " + pretty_json.forms.name)
    #print (json.dumps(pretty_json, sort_keys=True, indent=4))
    # print(response)
    #def jprint(obj):
       #text = json.dumps(obj, sort_keys=True)
       #print(text)
    #jprint(response.json())
    return render_template("index_post.html", pretty_json=pretty_json, results4=results4)


if __name__=="__main__":
    project.run(debug=True)              

   