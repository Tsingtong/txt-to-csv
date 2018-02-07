#-*- coding: utf-8 -*-
def get_lines(filepath):
    with open(filepath + '.txt') as file_object:
        lines = list(file_object.readlines())
        return lines

def new_csv(lines, filepath):
    fileindex = 0
    fp = open(filepath + '.csv', 'w')
    count = len(lines)
    print("总行数:" + str(count))
    for index, line in enumerate(lines):
        index += 1
        # print(str(index)+' : '+line)
        oneline = line.strip()  # 逐行读取，剔除空白
        fp.write(oneline)       # 写文件
        fp.write('\n')
    fp.close()

if __name__ == "__main__":
    filepath = "demo_airhistory"
    lines = get_lines(filepath)
    new_csv(lines, filepath)