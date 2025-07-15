from bottle import run, route, template, request, response


def check_tally_initialised():
    if request.get_cookie("tally") is None:
        response.set_cookie("tally", "0")


@route("/")
def index():
    check_tally_initialised()

    return template("index")


@route("/increment")
def increment():
    check_tally_initialised()

    current_tally = int(request.get_cookie("tally"))
    current_tally += 1
    incremented_tally = str(current_tally)

    response.set_cookie("tally", incremented_tally)

    return template("<p>Counter value: {{value}}</p>", value=incremented_tally)


@route("/decrement")
def decrement():
    check_tally_initialised()

    current_tally = int(request.get_cookie("tally"))
    current_tally -= 1
    decremented_tally = str(current_tally)

    response.set_cookie("tally", decremented_tally)

    return template("<p>Counter value: {{value}}</p>", value=decremented_tally)


@route("/reset")
def reset():
    check_tally_initialised()

    response.set_cookie("tally", "0")

    return "Counter reset!"


run(host="localhost", port=8080, debug=True)

