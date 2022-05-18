from flask import Flask, render_template
app=Flask(__name__, template_folder='mission-to-mars')
@app.route("/")
def hello():
    return render_template('index.html')
app.run(debug=True)