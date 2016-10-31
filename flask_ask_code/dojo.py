import logging

from random import randint

from flask import Flask, render_template

from flask_ask import Ask, statement, question, session


app = Flask(__name__)

ask = Ask(app, "/")

logging.getLogger("flask_ask").setLevel(logging.DEBUG)


@ask.launch

def launch_skill():

    welcome_msg = render_template('welcome')

    return question(welcome_msg)

@ask.intent("DojoInfoIntent")

def dojo_info():
    response = render_template("dojo_info_template")
    return statement(response)

@ask.intent("DojoStaffIntent")

def dojo_staff():
    response = render_template("invalid_city")

    return statement(response)

@ask.intent("DojoStackIntent", convert={'City': str})

def dojo_stacks(City):
    response = ''
    if City == "San Jose":
        response = render_template("san_jose_stacks", city=City)
    elif City == "Seattle":
        response = render_template("seattle_stacks", city=City)
    elif City == "Chicago":
        response = render_template("chicago_stacks", city=City)
    elif City == "Dallas":
        response = render_template("dallas_stacks", city=City)
    elif City == "Burbank":
        response = render_template("burbank_stacks", city=City)
    elif City == "Washington":
        response = render_template("washington_stacks", city=City)
    else:
        response = render_template("invalid_city")

    return statement(response)

@ask.intent("DojoInstructorIntent", convert={'City': str})

def dojo_instructors(City):
    response = ''
    if City == "San Jose":
        response = render_template("san_jose_instructors", city=City)
    elif City == "Seattle":
        response = render_template("seattle_instructors", city=City)
    elif City == "Chicago":
        response = render_template("chicago_instructors", city=City)
    elif City == "Dallas":
        response = render_template("dallas_instructors", city=City)
    elif City == "Burbank":
        response = render_template("burbank_instructors", city=City)
    elif City == "Washington":
        response = render_template("washington_instructors", city=City)
    else:
        response = render_template("invalid_city")

    return statement(response)


@ask.intent("AMAZON.HelpIntent")

def dojo_help():
    response = render_template("help_template")
    return question(response)

@ask.intent("AMAZON.StopIntent")

def dojo_stop():
    response = render_template("stop_template")
    return statement(response)


if __name__ == '__main__':

    app.run(debug=True)
