import time

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"


if __name__ == "__main__":
    app.run()


# Python decorator

def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)

        # do something before
        function()
        function()

    return wrapper_function


@delay_decorator
def say_hello():
    print("Hello")


@delay_decorator
def say_bye():
    print("bye")


@delay_decorator
def greeting():
    print("hello, How are you!!!")
