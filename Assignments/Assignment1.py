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
"""From the string variable provided extract 
Day, Month, year using indexing and print it."""
string= "04-August-2019"
print('Day',string[0:2])
print('Moonth',string[3:9])
print('Year',string[10:14])

#Task4
#Extract Supervisedlearning from the following string.
string_search='Supervisedlearning'
string = "SSuuppeerrvviisseeddlleeaarrnniinng"
print(string[0:len(string):2])


#Task5
#print the length of the string.
file=open('owlcreek.txt','r')
file_data=file.read()
print(len(file_data))

#Task6
"""
In the text after every full stop (.) there are two trailling spaces, 
reduce it to single trailling space and save the changed string 
to a new file "new_owlcreek.txt"
"""
file.seek(0)
print(file.readlines()[:50])


with open('new_owlcreek.txt','w+') as nf:
    file.seek(0)
    for line in file.readlines():
        nf.write(line.replace('.  ','.'))
    nf.close();
    
#Task7
"""
The text is divided into three parts (I, II, III). 
In the text you can see a 'I' character before starting of first part
 and similarly 'II' and 'III' for 2nd and 3rd part.

Create three strings dividing these three parts as
(part_1, part_2, part_3) 
 and print their character length in the format shown below.
"""
print(file_data[:500])

print(file_data.index('I'))
print(file_data.index('II'))

print(file_data.index('III'))

to_search=['I','II','III']

part_1=file_data[file_data.index('\nI'):file_data.index('\nII')-1]
part_2=file_data[file_data.index('\nII'):file_data.index('\nIII')-1]
part_3=file_data[file_data.index('\nIII'):len(file_data)]

print('part_1 length',len(part_1))
print('part_2 length',len(part_2))
print('part_3 length',len(part_3))

print('part_1 ',part_1)
print('part_2 ',part_2)
print('part_3 ',part_3)

