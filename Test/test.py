import Common.conf as conf


class Test:

    def ini_file_test(self):
        conf.ini.read(conf.file_path_ini)
        print(conf.ini["user"]["password"])
