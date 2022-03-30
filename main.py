#!/usr/bin/env python
# -*- coding:utf-8 -*-
from jd_assistant import Assistant

if __name__ == '__main__':
    asst = Assistant()      # 初始化
    asst.login_by_QRcode()  # 扫码登陆
    asst.clear_cart()       # 清空购物车（可选）
    asst.add_item_to_cart(sku_ids='100001324422')  # 根据商品id添加购物车（可选）
    asst.submit_order_by_time(buy_time='2020-02-16 01:17:59.500', retry=4, interval=5)  # 定时提交订单
    # 3个参数：
    # buy_time: 下单时间，例如：'2019-02-16 01:17:59.500'
    # retry: 下单重复执行次数，可选参数，默认4次
    # interval: 下单执行间隔，可选参数，默认5秒
