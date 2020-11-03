import time
import random
import os

ALPHABET_SAMPLES = "abcdefghijklmnopqrstuvwxyz"

NUM_SAMPLES = 2000

def random_string(length):
    result = ""
    for i in range(length):
        result += random.choice(ALPHABET_SAMPLES)
    return result

os.popen("mkdir personal_info")
time.sleep(2)

def random_email():
    email = ["naver.com", "google.com", "yahoo.com", "daum.net", "daumkakao.com"]
    return random.choice(email)

def random_salary():
    return random.randint(10, 30) * 10**7

for i in range(NUM_SAMPLES):
    filename = "personal_info/" + random_string(3) + str(time.time()) + ".txt"
    outfile = open(filename, 'w')
    outfile.write("name : " + random_string(5) + "\n")
    outfile.write("age : " + str(time.time())[-2:] + "\n")
    outfile.write("e-mail : " + random_string(8) + "@" + random_email() +"\n")
    outfile.write("telephone : 010-" + str(time.time())[-4:] + "-" + str(time.time())[-6:-2] + '\n')
    outfile.write("sex : " + random.choice(["male", "female", "others"]))
    outfile.close()