#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 22 07:05:34 2020

@author: parasn
"""

#Basic String Processing
#Task 1
#print a string that displays 'NLP stands for Natural Language Processinng' 
#using the variables

abr='NLP'
full_text='Natural Languae Processing'
print(f'{abr} stands for {full_text}')
#output=NLP stands for Natural Languae Processing

#Task2
#Create a function which takes N as an argument and return a list repeating the word 
#'NLP' for N number of timnesas string
def repeatString(str,no) :
    return str*no

print(repeatString('NLP',3))

#Task3

