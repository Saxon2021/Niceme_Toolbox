# !python3
# coding:utf8
import codecs
import csv


# 获取csv文件数据
def get_csv_info(path):
    data = []
    with open(path, 'r', encoding="gbk") as csv_f:
        reader = csv.reader(csv_f)
        for row in reader:
            data.append(row)
    csv_f.close()
    return data


# 获取txt文件中的内容
def get_txt_info(path):
    f = open(path, encoding="utf-8", newline="")
    data1 = f.readlines()
    data2 = []
    for line in data1:
        line = line.strip("\n")
        line = line.strip("\r")
        data2.append(line)
    f.close()
    return data2


# 获取txt文件中的内容-作为一个字符串
def get_txt_all(path):
    f = open(path, encoding="utf-8", newline="")
    data1 = f.readlines()
    f.close()
    return "".join(data1)


# 生成CSV文件
def create_csv_file(path, data):
    try:
        f = codecs.open(path, 'wb', "gbk")
        csv_writer = csv.writer(f)
        csv_writer.writerows(data)
        f.close()
        return True
    except Exception as e:
        print(e)
        return False


# 创建csv日志文件
def create_csv_log(path, data):
    try:
        f = codecs.open(path, 'a+', "gbk")
        csv_writer = csv.writer(f)
        csv_writer.writerows(data)
        f.close()
        return True
    except Exception as e:
        print("file io error: ", e)
        return False, e


# 创建txt日志文件
def create_txt_log(path, data):
    try:
        f = codecs.open(path, "a+", "gbk")
        f.write(data + "\n")
    except Exception as e:
        print("file io error: ", e)
        return False, e
