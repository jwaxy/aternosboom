# By ~Jwaxy~

import hashlib, argparse
from tqdm import tqdm
from sys import argv, exit

parser = argparse.ArgumentParser(
                    prog = 'rainbow.py',
                    description = 'Rainbow! 🌈️ \033[0;36mTurns wordlists to md5 wordlists\033[0m',
                    epilog='\033[35;3mBy ~Jwaxy~\0')

parser.add_argument('wordlist',help='the path of the wordlist', nargs=1)
parser.add_argument('-o', '--out', required=False,help='The filename of new wordlist that will be generated (Default is same name)', nargs=1)

if len(argv)==1:
    parser.print_help()
    exit(1)

args = parser.parse_args()

wordlist_path = args.wordlist[0]
out_path = args.out[0] if args.out else wordlist_path+".md5sum"

src = open(wordlist_path)
out = open(out_path, "w")

for line in tqdm(src.readlines(), desc="\033[0;36mConverting..."):
    line = line.replace("\n", "").replace("\r", "")
    transformed = hashlib.md5(line.encode('utf-8')).hexdigest()
    out.write(f"{transformed} {line}\n")

src.close()
out.close()

print("Done :D")
