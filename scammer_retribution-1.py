import time
import requests
import string
import random
from threading import Thread


def retribution(url, thread, real: bool, email_field, pass_field):
    adjective_pool = [i.strip("\n")
                      for i in open("adjectives.txt", "r").readlines()]
    base_username = [i.strip("\n")
                     for i in open("fake_names.txt", "r").readlines()]
    password_pool = base_username + \
        [i.strip("\n") for i in open("fake_pass.txt", "r").readlines()]
    symbols = string.punctuation.strip("'")
    digits = string.digits
    email_handle = ["@gmail.com", "@yahoo.com", "@hotmail.com", "@outlook.com"]
    count = 0
    error = 0
    for name in range(len(base_username)):
        count += 1
        fake_username = random.choice(adjective_pool) + random.choice(base_username) + \
            "".join(random.choices(digits, k=random.randint(1, 5))) + \
            random.choice(email_handle)
        fake_password = random.choice(password_pool) + "".join(random.choices(
            digits, k=random.randint(1, 5)) + random.choices(symbols, k=random.randint(1, 3)))

        if real:
            try:
                requests.post(url, allow_redirects=False, data={
                    f"{email_field}": fake_username,
                    f"{pass_field}": fake_password
                })
                print("Thread: " + str(thread).zfill(2) + " >> Sending fake user [{}/{}] ({} | {})".format(
                    count, len(base_username), fake_username, fake_password))
            except:
                error += 1
                print("Error has occured. {}".format(error), end='\r')
        else:
            time.sleep(0.5)
            print("Thread: " + str(thread).zfill(2) + " >> Sending fake user [{}/{}] ({} | {})".format(
                count, len(base_username), fake_username, fake_password))


if __name__ == "__main__":

    url = input("Input post request url here: [str] >> ")
    username_field = input(
        "What is the field for the username input in the post request? [str] >> ")
    password_field = input(
        "What is the field for the password input in the post request? [str] >> ")
    while True:
        try:
            thread_count = int(
                input("How many threads do you want to run the program? [int]>> "))
            break
        except:
            continue
    while True:
        flood = input(
            "Do you want to run a mock test and not actually send anything? [Y/N] >> ").lower()
        if flood == "y" or flood == "n":
            if flood == "y":
                flood = False
            elif flood == "n":
                flood = True
            break
        else:
            continue
    threads = []
    min_ = 0
    max_ = thread_count
    def clear(): return print("\n" * 150)
    clear()
    while True:
        for i in range(min_, max_):
            t = Thread(target=retribution, args=(
                url, i, flood, username_field, password_field,))
            t.daemon = True
            threads.append(t)
        for i in threads:
            i.start()
        for i in threads:
            i.join()
        threads = []
        min_ = thread_count + 1
        max_ += thread_count
