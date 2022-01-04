from flask import Flask, jsonify, request
app = Flask(__name__)
List = [{
    "ID": 1,
    "Name":u "Jas",
    "Contact":u "8377021315",
    "Done": False
        },
    {
    "ID": 2,
    "Name":u "Dipsy",
    "Contact":u "8377021345",
    "Done": False
        }]
@app.route("/")
def hello_word():
    return "hello_word"
@app.route("/add-data",methods = ["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "Status": "Error",
            "Message": "Please provide data"
            }, 400)
    contact = {
        "ID": tasks[-1]["ID"]+1,
        "Name": request.json["Name"],
        "Contact": request.json.get("Contact", ""),
        "Done": False
        }
    List.append(contact)
    return jsonify({
        "Status": "Success",
        "Message": "Contact added successfully"
        })
@app.route("/get-data")
def get_task():
    return jsonify({
        "Data": List,
         
        })
if(__name__=="__main__"):
    app.run(debug = True)
