![cool-banner](https://i.ibb.co/gzTV52c/Aternos-Boom-Banner.png)
# AternosBoom! 💣️
AternosBoom! is a small utility for brute-forcing aternos accounts. ![Made with Python](https://img.shields.io/badge/Made%20with-Python-blue) 

## Installation

1. Clone the repo or download zip of the repo on Windows.

```bash
$ git clone https://github.com/jwaxy/aternosboom.git
```
2. Change the directory to the project folder.

```bash
$ cd aternosboom
```

2. Install required libraries using pip.

```bash
$ pip install -r requirements.txt
```

## Usage
1. Prepare your wordlist (a list of possible passwords).

2. Before starting the main (attack) program you should generate a rainbow wordlist using the other small script.

```bash
$ python rainbow.py your-wordlist.txt
```
   A new file called your-wordlist.txt.md5sum will be generated.

3. Start the main program using your new generated rainbow wordlist.

```bash
$ python aternosboom.py -u username-of-target -w your-wordlist.txt.md5sum
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## DISCLAIMER
AternosBoom! is developed with the intension of using this tool only for educational purpose.
I learned using requests, deobfuscating js, making regex patterns ... while writing this tool. This why I'm publishing this in the public.

## License

[GPL-3.0](https://choosealicense.com/licenses/gpl-3.0/)
