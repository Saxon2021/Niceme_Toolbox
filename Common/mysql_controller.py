# !python3
# coding:utf8

from sqlalchemy import create_engine, Column, String
from sqlalchemy.orm import declarative_base, Session

import Common.conf as conf

Base = declarative_base()


class PDD_LINK(Base):
    __tablename__ = "source_link_pdd"
    goods_id = Column(String(20), name="goods_id", primary_key=True)
    goods_name = Column(String(255), name="goods_name", nullable=False)
    goods_link = Column(String(255), name="goods_link", nullable=False)
    goods_image = Column(String(255), name="goods_image", nullable=False)
    goods_video = Column(String(255), name="goods_video", nullable=False)
    shop_name = Column(String(255), name="shop_name", nullable=False)
    brand_name = Column(String(255), name="brand_name", nullable=False)
    location = Column(String(20), name="location", nullable=False)
    upload_time = Column(String(15), name="upload_time", nullable=False)
    uploader = Column(String(255), name="uploader", nullable=False)
    note = Column(String(255), name="note", nullable=False)


class MySql:
    engine = None

    def __init__(self):
        self.engine = create_engine(
            f'mysql+pymysql://{conf.MYSQL_USERNAME}:{conf.MYSQL_PASSWORD}@{conf.MYSQL_HOST}:{conf.MYSQL_PORT}/{conf.MYSQL_DATABASE}?charset=utf8',
            echo=False)

    # 查找数据
    def find_all_links(self):

        # 存储查找的结果
        all_data = [["商品编号", "商品名称", "商品链接", "店铺名称", "品牌名称", "发货地", "商品主图链接", "商品视频链接", "上传人", "首次上传时间", "备注"]]

        try:
            # 查找数据
            session = Session(bind=self.engine)
            rows = session.query(PDD_LINK).all()
            session.close()

            # 处理返回值
            for row in rows:
                all_data.append([
                    row.goods_id,
                    row.goods_name,
                    row.goods_link,
                    row.shop_name,
                    row.brand_name,
                    row.location,
                    row.goods_image,
                    row.goods_video,
                    row.uploader,
                    row.upload_time,
                    row.note
                ])
            # print(all_data)
            return all_data

        except Exception as e:
            return all_data

    # 通过名称查找数据
    def find_link_by_name(self, goods_name):

        # 存储查找的数据
        result_data = {}

        try:
            # 查找数据
            session = Session(bind=self.engine)
            find_result = session.query(PDD_LINK).filter(
                PDD_LINK.goods_name.like("%{goods_name}%".format(goods_name=goods_name))).all()
            session.close()

            # 处理返回值
            for row in find_result:
                result_data[row.goods_id] = {
                    "goods_name": row.goods_name,
                    "goods_link": row.goods_link,
                    "goods_image": row.goods_image,
                    "goods_video": row.goods_video,
                    "shop_name": row.shop_name,
                    "brand_name": row.brand_name,
                    "location": row.location,
                    "uploader": row.uploader,
                    "upload_time": row.upload_time,
                    "note": row.note
                }
            return result_data

        # 异常
        except Exception as e:
            return result_data
