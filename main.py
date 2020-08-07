from flask import Flask, render_template, request
import json
app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/get-data", methods=['GET', 'POST'])
def getdata():
    import rpc
    method_name = request.form.get('de')
    params = json.loads(request.form.get('params'))

    Records = rpc.returnUsers(method_name, params)
    response = {'Result': 'OK', 'Records': Records}
    response = json.dumps(response)
    return response


if __name__ == "__main__":
    app.run(debug=True)
