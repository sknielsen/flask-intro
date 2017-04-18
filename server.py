"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']

INSULTS = ['stinky', 'crazy', 'wicked', 'ridiculous', 'sassy', 'surly',
    'questionable', 'shady', 'abominable', 'weird']


@app.route('/')
def start_here():
    """Home page."""

    return """<!doctype html><html><p>Hi! This is the home page.</p>
      <a href='/hello'>Generate Greeting</a></html>"""


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    compliment_string = ''
    for compliment in AWESOMENESS:
        compliment_string += '<option value="%s">%s</option>' % (compliment, compliment)

    insult_string = ''
    for insult in INSULTS:
        insult_string += '<option value="%s">%s</option>' % (insult, insult)

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          What's your name? <input type="text" name="person">
          <select name="compliments">
            <option value="" disabled selected>Pick a Compliment</option>
            %s
          </select>
          <input type="submit" value="Submit">
        </form>
        <p>OR...</p>
        <form action="/diss">
          What's your name? <input type="text" name="person">
          <select name="insults">
            <option value="" disabled selected>Pick an Insult</option>
            %s
          </select>
          <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """ % (compliment_string, insult_string)


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = request.args.get("compliments")
    # compliment = choice(AWESOMENESS)

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {compliment}!
      </body>
    </html>
    """.format(player=player, compliment=compliment)


@app.route('/diss')
def diss_person():
    """Insult person by name"""

    player = request.args.get("person")

    insult = request.args.get("insults")

    return """
    <!doctype html>
    <html>
      <head>
        <title>An Insult</title>
      </head>
      <body>
        Hi, {player}! I think you're {insult}!
      </body>
    </html>
    """.format(player=player, insult=insult)



if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True)
