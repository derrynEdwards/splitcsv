# -*- coding: utf-8 -*-
"""
    File name           : web.py
    Author              : Derryn Edwards
    Date Created        : 2020/11/16
    Date Last Modified  : 2020/11/16 09:48:21
    Python Version      : 3.9
"""
# ==================================================================================================
# IMPORTS
# ==================================================================================================
import csv
import sys

try:
    # grabs arguments
    file_name = sys.argv[1]
    output_prefix = sys.argv[2]
    max_line = int(sys.argv[3])
    # opens csv file
    csv_file = open(file_name, 'r')
    csv_data = list(csv.reader(csv_file, delimiter=','))
    # line counters and mappers
    line_count = 0
    line_mapper = 0
    file_count = 1
    # csv header
    header = csv_data[0]

    while line_mapper < (len(csv_data)-1):
        new_list = []
        new_list.append(header)
        # opens new file
        new_file = open(output_prefix + '_' + str(file_count), 'w')

        for row in csv_data[line_mapper+1:]:
            if line_count < max_line:
                new_list.append(row)
                line_count += 1
                line_mapper += 1
            else:
                break
        # writes into new file
        csv.writer(new_file).writerows(new_list)
        new_file.close()
        print(new_list)
        line_count = 0
        file_count += 1
except Exception as e:
    print("Wrong Arguments.")
    print("arg1=csv file, arg2=new file prefix, arg3=max lines")
    print(e)
