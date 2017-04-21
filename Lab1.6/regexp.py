#!/usr/local/bin/python3

import re
import glob

def classify(s):
    """
    :param s: String to classify 
    :return: Tuple of arguments
    """

    m = re.match("^ ip address ([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+) ([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)", s)
    if m:
        return ("IP", m.group(1), m.group(2))

    m = re.match("^interface (.+)", s)
    if m:
        return ("INT", m.group(1))

    m = re.match("^hostname (.+)", s)
    if m:
        return ("HOST", m.group(1))

    return ("UNCLASSIFIED",)

for current_file_name in glob.glob("/Users/mk/Seafile/p4ne_training/config_files/*.txt"):
    with open(current_file_name) as f:
        for current_line in f:
            c = classify(current_line)
            if c[0] != "UNCLASSIFIED":
                print(c)