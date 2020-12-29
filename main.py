from flask import Flask, render_template, request, redirect
import json

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    # This will be executed by a component with the method='POST' property.
    # a component can be given an id/name like 'content'. request.form['content'] will port the content to python.
    if request.method == 'POST':
        pass
    else:
        return render_template('index.html')


@app.route("/get-data", methods=['GET', 'POST'])
def getdata():
    import rpc
    method_name = request.form.get('de')
    params = json.loads(request.form.get('params'))

    print(method_name)
    print('-' * 40)
    print(params)
    Records = []
    if method_name == "ReturnUsers":
        Records = rpc.returnUsers(method_name, params)
    if method_name == "ReturnCities":
        Records = rpc.returnCities()
    if method_name == "ReturnCitiesSmall":
        Records = rpc.returnCitiesSmall()
    elif method_name == "something":
        Records = []
    response = {'Result': 'OK', 'Records': Records}
    response = json.dumps(response)
    return response


# if(method_name == "ReturnUsers"):
#         Records = rpc.returnUsers(method_name, params)
#     elif(method_name == "something"):
#         Records = []
#     response = {'Result': 'OK', 'Records': Records}
#     response = json.dumps(response)
#     return response

@app.route("/second-page")
def loadSecondPage():
    return render_template('second-page.html')


@app.route("/Controllers")
def Controllers():
    return render_template('Controllers.html')


@app.route("/edit/<data>", methods=['GET', 'POST'])
def editPage(data=None):
    return render_template('edit.html', data=data)


if __name__ == "__main__":
    app.run(debug=True, port=8000)
