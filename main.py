from Test.test import Test
from Module.get_pinduoduo_link import Pinduoduo
import Common.api as api


class Version:
    version = "1.0.0"

    def check_version(self):
        return api.api_check_version(self.version)

    def ui_main_normal(self):
        print("".center(90, "="))
        print("|", "".center(86), "|")
        print("|", "Niceme Toolbox".center(86), "|")
        print("|", "".center(86), "|")
        print("|", ("--version " + str(self.version)).rjust(75), "".center(10), "|")
        print("|", "".center(86), "|")
        print("|", "1.Get Single Link                     2.Get All Links".center(86), "|")
        print("|", "".center(86), "|")
        print("|", "".center(86), "|")
        print("".center(90, "="))
        print()

    def ui_main_upgrade(self):
        print("".center(90, "="))
        print("|", "".center(86), "|")
        print("|", "Niceme Toolbox".center(86), "|")
        print("|", "".center(86), "|")
        print("|", "There is a new version, the current version is obsolete, ".center(86), "|")
        print("|", "please contact the administrator to get the latest version".center(86), "|")
        print("|", "".center(86), "|")
        print("|", "".center(86), "|")
        print("".center(90, "="))
        print()

    def function_get_all_links(self):
        pinduoduo = Pinduoduo()
        pinduoduo.get_all_links()

    def function_get_single_link(self, name):
        pinduoduo = Pinduoduo()
        pinduoduo.find_link_by_name(name)

    def V1_0_0_0(self):
        # 判断是否存在新的版本
        if self.check_version():
            self.ui_main_upgrade()
        else:
            self.ui_main_normal()
            select = input("请输入编号，按下回车键开始: ")
            if select == "1":
                goods_name = input("请输入商品名称: ")
                self.function_get_single_link(goods_name)
            elif select == "2":
                self.function_get_all_links()


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    version = Version()
    version.V1_0_0_0()
