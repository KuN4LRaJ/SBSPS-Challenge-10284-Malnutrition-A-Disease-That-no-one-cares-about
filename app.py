from flask import Flask, render_template 

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')



@app.route('/prints')
def prints():
    return hello_world




if __name__ == "__main__":
    app.run(debug=True)