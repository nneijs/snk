import os
import snk

while True:
    text = input("snk > ")
    if text.strip() == "clear":
        os.system('clear' if os.name == 'posix' else 'cls')
        continue
    if text.strip() == "":
        continue
    result, error = snk.run("<stdin>", text)

    if error:
        print(error.as_string())
    elif result:
        if len(result.elements) == 1:
            print(repr(result.elements[0]))
        else:
            print(repr(result))