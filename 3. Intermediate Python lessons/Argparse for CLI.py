# -*- coding: utf-8 -*-
"""
Source: https://www.youtube.com/watch?v=0twL6MXCLdQ&list=PLQVvvaa0QuDfju7ADVp5W1GF9jVhjbX-_
&index=3&ab_channel=sentdex
"""
import argparse
import sys

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--x', type=float, default= 1.0, 
                        help= 'What is the first number?')
    parser.add_argument('--y', type=float, default= 1.0, 
                        help= 'What is the second number?')
    parser.add_argument('--x', type=str, default= 'add', 
                        help= 'What operation? (add, sub, mul, or div)')
    args = parser.parse_args()
    sys.stdout.write(str(calc(args)))
    
def calc(args):
    operation = args.operation
    if args.operattion == 'add':
        return args.x + args.y
    elif args.operattion == 'sub':
        return args.x - args.y
    elif args.operattion == 'mul':
        return args.x * args.y
    elif args.operattion == 'div':
        return args.x / args.y

if __name__ == '__main__':
    main()