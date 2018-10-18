from flask import Flask, render_template, redirect, request

app = Flask(__name__)



tasks = {
    1 :{
        'id': 1,
     'Name': "Vacuum",
     'Description': '10am',
     "urgent": True
    },
    2: {
        'id': 2,
     'Name': "Wash floor",
     'Description': '11am',
     "urgent": True
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
        # urgent_add = request.form["urgent"]
        
        new_item = {
            "id": next_id,
            "Name": name_add,
            "Description": description_add,
            "urgent": "urgent" in request.form
        }
        
        
 
        tasks[next_id]= new_item 
        
        next_id += 1
        return redirect("/")





@app.route("/")
def showHi():
    return render_template("index.html", tasks=tasks.values())





if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080, debug=True)