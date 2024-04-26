from flask import Flask, render_template, request

application = Flask(__name__)
application.config.from_object(__name__)


@application.route('/')
def welcome():
    return render_template('form.html')


@application.route('/result', methods=['POST'])
def result():
    var_1 = request.form.get("var_1", type=int)
    var_2 = request.form.get("var_2", type=int)
    operation = request.form.get("operation")
    if var_1 is None or var_2 is None:
        result = 'Fehler'
    else:
        if(operation == 'Addition'):
            result = var_1 + var_2
        elif(operation == 'Subtraktion'):
            result = var_1 - var_2
        elif(operation == 'Multiplikation'):
            result = var_1 * var_2
        elif(operation == 'Division'):
            result = var_1 / var_2
        else:
            result = 'Es wurden keine Daten eingegeben'
    entry = result
    return render_template('result.html', entry=entry)

if __name__ == '__main__':
    application.run(host='0.0.0.0',port=8080)
