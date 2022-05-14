from flask import Flask
import time
import math
import datetime
import socket

app = Flask(__name__)


def sign():
    return "<br>date: {}" \
           "<br>host: {}".format(datetime.datetime.now(), socket.gethostname())


@app.route("/")
def hello():
    return "это api для теста балансировщика" \
           "<br>/factorial/{num} - расчет факториала" \
           "<br>/sleep/{sleep_time}/{answer} - усыпление процесса" + sign()


@app.route("/factorial/<int:num>")
def factorial(num):
    try:
        return "factorial of {} is {}".format(num, math.factorial(num)) + sign()
    except Exception as err:
        return "factorial not defined: {}".format(str(err))


@app.route("/sleep/<int:sleep_time>/<answer>")
def sleep_and_return(sleep_time, answer):
    print("")
    time.sleep(sleep_time)
    return "You answer: {}".format(answer) + sign()
