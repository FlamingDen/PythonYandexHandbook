__storage_history = set()


def modern_print(text):
    global __storage_history
    if text not in __storage_history:
        __storage_history.add(text)
        print(text)
