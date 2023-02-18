from configparser import ConfigParser

ini = ConfigParser()
file_path_ini = "./config.ini"

MYSQL_HOST = "sunshen.net.cn"
MYSQL_PORT = "3306"
MYSQL_USERNAME = "niceme"
MYSQL_PASSWORD = "niceme2022"
MYSQL_DATABASE = "niceme"

file_path_links_export = "./Res/"

API_BASE_PATH = "http://sunshen.net.cn:8989/v1"
API_NICEME_CHECK_VERSION = API_BASE_PATH + "/tools/check_version"
