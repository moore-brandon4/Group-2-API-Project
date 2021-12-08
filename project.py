#python --version
#pip install flask
import requests
import pokepy

response=requests.get("https://pokeapi.co/api/v2/pokemon/ditto")
print(response.status_code)
print(response.json())

#client = pokepy.V2Client()
#client.get_pokemon()


# from flask import Flask, render_template  
# project = Flask(__name__)      



# @project.route("/")                          
# def index():                    
#     return render_template("index.html")



# if __name__=="__main__":
#     project.run(debug=True)              