def function1():
    global variable
    variable = "I am a global variable"

def function2():
    print(variable)

function1()
function2()