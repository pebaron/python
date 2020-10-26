#!/usr/bin/env python3

import numpy as np

import random
import string
import argparse

parser = argparse.ArgumentParser(description="Code generating passwords.")
parser.add_argument('--length', '-l', type=int, default=8)
parser.add_argument('--NumberOfPasswords', '-n', type=int, default=10)
args = parser.parse_args()

def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

def get_random_capitals(length):
    letters = string.ascii_uppercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


def get_random_symbols(length):
    letters = string.punctuation
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

def get_random_numbers(length):
    letters = string.digits
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

# Divide randomly password in 4 segments, letters, capital letters, symbols, numbers

def GeneratePassword():
    for i in range (1):
        MaxInt = args.length
        HalfInt = np.random.randint(2,MaxInt-1)
        LowInt = np.random.randint(1,HalfInt)
        UpInt = np.random.randint(HalfInt+1, MaxInt)
        #print("Segmented: ", LowInt, HalfInt, UpInt, MaxInt)
        LetterLenght = MaxInt - UpInt
        CapitalLetterLenght = UpInt - HalfInt
        SymbolsLenght = HalfInt - LowInt
        NumberLenght = LowInt
        #print("Lenghts numbers-symbols-capitals-letters: ",NumberLenght, SymbolsLenght, CapitalLetterLenght, LetterLenght)
        #print("-----------------------------------")

    Password = get_random_string(LetterLenght) + get_random_capitals(CapitalLetterLenght) + get_random_symbols(SymbolsLenght) + get_random_numbers(NumberLenght)
    #print("Password before shuffle: ", Password)
    Password = list(Password)
    for i in range(10):
        np.random.shuffle(Password)
    Password = ''.join(Password)
    #print("Password after shuffle: ", Password)
    #print(Password)
    return Password

for i in range(args.NumberOfPasswords):
    print(GeneratePassword())
