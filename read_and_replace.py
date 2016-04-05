#!/usr/bin/env python

import glob

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


for arch in glob.glob("RMS*"):
    first = arch[13]
    second = arch[20]
    reps = {'   '+first:'    ', '   '+second:'    '}
    file_content = read_file(arch, 'r')
    pre_modified = replace_all(file_content, reps)
    write_file(arch, 'w', pre_modified)

print "ok McKay"
