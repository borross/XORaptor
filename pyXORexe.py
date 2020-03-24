#!/usr/bin/env python3
# coding=utf-8
# borross
__version__ = '001'

from optparse import OptionParser
from sys import exit


def fastXor(inputDATA, key, outputFILE):
    #print("XORing file: " + inputDATA + " with key: " + key + ". Output file is: " + outputFILE)
    #bytearray(open(item, 'rb').read())
    key = r"b'{}'".format(key)
    b_key = list(key.encode('utf-8'))
    inputDATA = bytearray(open(inputDATA, 'rb').read())
    from math import ceil
    DataLen = len(inputDATA)
    #key with same length as file content
    kkey = (b_key*int(ceil(float(DataLen)/float(len(b_key)))))[:DataLen]
    return open(outputFILE, 'wb').write(bytearray(((inputDATA[i] ^ kkey[i]) for i in range(0, DataLen))))


if __name__ == '__main__':
    parser = OptionParser(description='Win XOR Tool. borross (c). Version: {0}'.format(__version__), usage="\n pyXORexe --infile=%input_File% --key=%xor_key%  --outfile=%output_File%", version='KTL lookup v.{0}'.format(__version__))
    parser.add_option('--infile', type="string", help='Intput file')
    parser.add_option('--key', type="string", default="password", help='Key for XORing with Input file. Default: password')
    parser.add_option('--outfile', type="string", help='Output file (encrypted result)')

    args, _ = parser.parse_args()
    
    if args.infile is None or args.outfile is None:
        parser.print_help()
        exit(1)

    fastXor(args.infile, args.key, args.outfile)