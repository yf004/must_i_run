from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from db import culturalQuests

app = Flask(__name__)



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/classic")
def classic():
    return render_template("classic.html")


@app.route("/singaporev")
def singaporev():
    return render_template("singaporev.html")

@app.route("/geoguessrv")
def geoguessrv():
    return render_template("geoguessrv.html")

@app.route("/classicGame")
def classicGame():
    lis = (i[0] for i in culturalQuests)
    return render_template("classicGame.html",
                           tasks=lis)

@app.route("/geoguessrvGame")
def geoguessrvGame():
    return render_template("geoguessrvGame.html")

@app.route("/singaporevGame")
def singaporevGame():
    return render_template("singaporevGame.html")

@app.route("/<task_name>")
def task(task_name):
    print(task_name)
    for i in culturalQuests:
        if i[0] == task_name:
            title = task_name
            typeStr = "Task type: " + i[1]
            desc = i[2]
    return render_template("task.html",
                           title = title,
                           typeStr=typeStr,
                           desc=desc)

@app.route("/quiz/<int:temple_index>/<int:question_index>")
def quiz(temple_index, question_index):
    # Get the temple data
    temple = temples[temple_index]  # Select the temple by index
    
    # Get the question data
    question_data = temple[1][question_index]  # Select the question by index
    question, options, correct_option = question_data  # Unpack the question data
    option1, option2, option3 = options  # Unpack the options
    
    # Render the template with the required data
    return render_template(
        'quiz.html', 
        title=temple[0],  # Name of the temple
        question=question, 
        option1=option1, 
        option2=option2, 
        option3=option3,
        correct_option=correct_option,
        temple_index=temple_index,
        question_index=question_index
    )


@app.route("/riddle")
def riddle():
    return render_template("riddle.html")



if __name__ == "__main__":
    app.run(debug=True)
