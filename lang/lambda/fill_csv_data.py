# -*- coding:utf-8 -*-
import csv

if __name__ == '__main__':
	# open函数第一个参数为文件名称，也可以用绝对路径，如:"D:/csvdata/fill_data.csv"
	with open("test.csv", "w") as csv_file:
		writer = csv.writer(csv_file)
		writer.writerow(["column_a", "column_b"]) # 先写入列名称，然后再写入多行数据

		# range函数中"200"用于控制写多少行数据，第二列值是递加的，先声明个变量；
		# 第一列的规则不确定，就默认先填充"000100"
		column_b = 369008000000001
		for index in range(200):
			writer.writerow(["000100", "'" + column_b])
			column_b = column_b + 1
