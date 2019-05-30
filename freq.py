# -*- coding: utf-8 -*- 
import shutil
import re

"""
Fixed some continue running problems.
"""


def copy(file_name):
    for file in file_name:
        try:
            newname = './freq/' + file
            oldname = file
            shutil.copy(oldname, newname)
        except Exception as ret:
            print("Files not enough！")
            break

def read_fort188_lines(file_read):
    with open (file_read, 'r') as f:
        lines = f.readlines()
    line_ori = lines[5].strip()
    fix_line = re.split(r'\s+', line_ori)
    num_1 = fix_line[0]
    num_2 = fix_line[1]
    return (num_1, num_2)

def write_pos_change(first_line, total_line, change1, change2):
    lines =list()
    try:
        with open ('CONTCAR', 'r') as f:
            for i in range(total_line):
                lines.append(f.readline())
    except Exception as ret:
        print('ERROR: CONTCAR not exist, please use "cp CONTCAR POSCAR rather than mv"')
    else:
        for i in range(len(lines)):
            if i == change1 or i == change2 or i < first_line:
                with open('POSCAR1', 'a') as f:
                    f.write(lines[i])
            else:
                list_new = list()
                change_line_list = re.split(r'\s+', lines[i].strip())
                for i in range(3):
                    list_new.append(change_line_list[i])
                list_new.append(' F   F   F')
                with open ('POSCAR1', 'a') as f:
                    for i in list_new:
                        f.write('  ' + i)
                    f.write('\n')

def read_pos(first_line_num, change_lines):
    with open ('POSCAR', 'r') as f:
        lines = f.readlines()
    first_line = lines[first_line_num-1].strip()
    i = 0
    for line in lines:
        if line != ' \n':
            i += 1
        else:
            break
    total_line = i
    change1, change2 = change_lines
    change1_line_num = int(change1) + first_line_num - 1
    change2_line_num = int(change2) + first_line_num - 1
    write_pos_change(first_line_num, total_line, change1_line_num, change2_line_num)

def main():
    # 1. Read the fixed atom number in fort.188
    change_lines = read_fort188_lines('fort.188')
    # 2. The 10th line was defined as the first_line.
    n = 10 - 1
    # 3. Change some T T T lines to F F F lines. 
    read_pos(n, change_lines)
    # 4. Redit INCAR(Shell)


if __name__ == "__main__":
    main()
