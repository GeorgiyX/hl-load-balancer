from flask import Flask
import time
import math

app = Flask(__name__)


@app.route("/")
def hello():
    return "это api для теста балансировщика" \
           "<br>/factorial/{num} - расчет факториала" \
           "<br>/sleep/{sleep_time}/{answer} - усыпление процесса"


@app.route("/factorial/<int:num>")
def factorial(num):
    try:
        return "factorial of {} is {}".format(num, math.factorial(num))
    except Exception as err:
        return "factorial not defined: {}".format(str(err))


@app.route("/sleep/<int:sleep_time>/<answer>")
def sleep_and_return(sleep_time, answer):
    time.sleep(sleep_time)
    return "You answer: {}".format(answer)
