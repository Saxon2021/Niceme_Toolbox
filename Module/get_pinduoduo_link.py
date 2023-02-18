import os.path
import time

from Common.mysql_controller import MySql
import Common.file_io as file
import datetime
import Common.conf as conf

i = datetime.datetime.now()


class Pinduoduo:

    def __init__(self):
        self.mysql = MySql()

    def get_all_links(self):
        print("正在查找数据...")
        # 获取查找数据
        data = self.mysql.find_all_links()
        time.sleep(1)

        print("获取数据完成, 获取到[" + str(len(data)) + "]条数据.")
        # 处理导出文件
        file_name = "链接库导出" + str(datetime.datetime.now().strftime('%Y%m%d%H%M%S')) + ".csv"
        if not os.path.exists(conf.file_path_links_export):
            os.mkdir(conf.file_path_links_export)

        print("正在导出数据...")
        # 文件导出
        time.sleep(1.5)
        file.create_csv_file(conf.file_path_links_export + file_name, data)
        print("导出完成.")
        print("导出文件位置: 当前文件夹下/" + os.path.relpath(conf.file_path_links_export + file_name))

    def find_link_by_name(self, goods_name):
        data = self.mysql.find_link_by_name(goods_name)
        for key, values in data.items():
            print(">>>", values["goods_name"], "<<<")
            print("|> 品牌:", values["brand_name"])
            print("|> 店铺:", values["shop_name"])
            print("|> 链接:", values["goods_link"])
            print("|> 图片:", values["goods_image"])
            print("|> 视频:", values["goods_video"])
            print("|> 发货:", values["location"])
            print("|> 时间:", values["upload_time"])
            print("|> 上传:", values["uploader"])
            print("|> 备注:", values["note"])
            print("##########################################################")
            print("")
