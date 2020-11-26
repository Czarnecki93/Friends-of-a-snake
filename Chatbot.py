import time

def chatbot(text) :
    for i in text:
        print(i, end='', flush=True)
        time.sleep(0.025)
    print('\n')