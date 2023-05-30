import sys
import time
import string
import threading


def word_check(word):
    global alphabet1, alphabet2

    if len(word) < 5:
        return False

    for i in range(len(word) - 4):
        if word[i] in alphabet2:
            isit = True
            for j in range(i+1, i+5):
                if word[j] in alphabet1 or word[j] in string.punctuation:
                    isit = False

            if isit:
                if word[i:i+5].isupper():
                    return False
                return True
    return False


alphabet1 = "aeiouyAEIOUY"
alphabet2 = "bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ"


def func():
    while True:
        com = sys.stdin.readline()
        for _ in string.punctuation:
            if _ != '\'':
                com = com.replace(_, ' ')
        while '\'' in com:
            if com[com.index('\'')-1] == ' ':
                com = com[:com.index('\'')-1] + com[com.index('\'')+1:]
        com = com.split()
        if com:
            for word in com:
                if word_check(word):
                    print(word, end=' ')


start_time = time.time()
threading.Thread(target=func, daemon=True).start()
time.sleep(1-(time.time() - start_time))
sys.exit(0)
