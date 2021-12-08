#python --version
#pip install flask
import requests
import pokepy

# client = pokepy.V2Client()
# client.get_pokemon()


from flask import Flask, render_template  
project = Flask(__name__)      



@project.route("/")                          
def index():                    
    return render_template("index.html")



if __name__=="__main__":
    project.run(debug=True)              