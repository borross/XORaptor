# XORaptor - Playing with files and XOR

XORfile3.py
PYTHON programm to XOR with given gamma or key (hardcoded) and binary read strings of files (certain filetypes). <br />
Programm recursively search .pdf and .xlsx files in created XOR foulder in %USERNAME%\Downloads, 
making XOR with given key and secure deleteting files (wrinting random data into file (number of passes is configurable), then delete it) <br />
Mode of encrypting and decryping determined by ENC variable (ENC=0 is decrypting mode). <br />
If something go wrong, files are easily recover by shadow copy feature of MS Windows. <br />
Code is for educational purposes!

pyXORexe.py
PYTHON console programm with the same context as XORfile3.py but more flexible.<br />
Argument Options:
  --version          show program's version number and exit
  -h, --help         show this help message and exit
  --infile=INFILE    Intput file
  --key=KEY          Key for XORing with Input file. Default: password
  --outfile=OUTFILE  Output file (encrypted result)
Code is for educational purposes!
