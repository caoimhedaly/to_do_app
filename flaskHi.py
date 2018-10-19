from flask import Flask, render_template, redirect, request
import os


app = Flask(__name__)



tasks = {
    1 :{
        'id': 1,
     'Name': "Vacuum",
     'Description': '10am',
     "urgent": True,
     "done": True
     
    },
    2: {
        'id': 2,
     'Name': "Wash floor",
     'Description': '11am',
     "urgent": True,
     "done": True
    }
    }
 

next_id = 3 
 
@app.route("/add", methods=["GET", "POST"])    
def add_items():
    global next_id
    if request.method == "GET":
        return render_template("todoform.html")
    else:
        
        name_add = request.form["name"]
        description_add = request.form["description"]
        
        
        new_item = {
            "id": next_id,
            "Name": name_add,
            "Description": description_add,
            "urgent": "urgent" in request.form,
            "done": "done" in request.form
        }
        
        
 
        tasks[next_id]= new_item 
        
        next_id += 1
        return redirect("/")



@app.route("/")
def showHi():
    return render_template("index.html", tasks=tasks.values())
    
@app.route("/add", methods = ["POST", "GET"])
def getID():
    id = request.args.get("next_id")
    return redirect("/edit/" + id)
    
    
    
    
@app.route("/edit/<int:id>", methods = ["POST", "GET"])
def showEdit(id):
    if request.method == "POST":
        changed_item = {
            "id": id,
            "Name": request.form["name"] ,
            "Description": request.form["description"],
            "urgent": "urgent" in request.form,
            "done": "done" in request.form
        }
        tasks[id] = changed_item
        return redirect("/")
       
    else:
        return render_template("edit_task_form.html", task= tasks[id])
   



    

    

if __name__ == "__main__":
    app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)))