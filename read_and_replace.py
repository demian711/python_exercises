#!/usr/bin/env python


file_to_change = "RMS-res_2FBW_A-2H88_N.txt"

def read_file(file, per):
    with open(file, per) as file :
        return file.read()     

def write_file(file, per, content):
    with open(file, per) as file :
        file.write(content)     

def replace_all(content, dic):
    for i, j in dic.iteritems():
        content = content.replace(i, j)
    return content

reps = {'   A':'    ', '   N':'    '}
file_content = read_file(file_to_change, 'r')
pre_modified = replace_all(file_content, reps)
write_file(file_to_change, 'w', pre_modified)
