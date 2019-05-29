# ---comment----
# coding=utf-8

import unittest
import requests
import os, sys
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
from db_fixture import test_data


class AddEventTest(unittest.TestCase):
    """ 添加发布会 """

    def setUp(self):
        self.base_url = "http://127.0.0.1:8001/api/add_event/"

    def tearDown(self):
        print(self.result)

    def test_add_event01_all_null(self):
        """ 所有参数为空 """
        payload = {'id':'','name':"",'limit':'','status':'','address':"",'start_time':''}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        print(payload.get('id'),payload.get('name'),payload.get('limit'),
              payload.get('status'),payload.get('address'),payload.get('start_time'))
        self.assertEqual(self.result['status'], 10021)
        self.assertEqual(self.result['message'], 'parameter error')

    def test_add_event02_eid_exist(self):
        """ id已经存在 """
        payload = {'id':1,'name':"cc发布会",'limit':2000,'status':1,'address':"深圳宝体",'start_time':"2017-05-27"}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        print(payload.get('id'),payload.get('name'),payload.get('limit'),
              payload.get('status'),payload.get('address'),payload.get('start_time'))
        self.assertEqual(self.result['status'], 10022)
        self.assertEqual(self.result['message'], 'event id already exists')

    def test_add_event03_name_exist(self):
        """ 名称已经存在 """
        payload = {'id':13,'name':"红米Pro发布会",'limit':2000,'status':'1','address':"深圳宝体",'start_time':"2017-05-10 12:00:00"}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        print(payload.get('id'), payload.get('name'), payload.get('limit'),
              payload.get('status'), payload.get('address'), payload.get('start_time'))
        self.assertEqual(self.result['status'], 10023)
        self.assertEqual(self.result['message'], 'event name already exists')

    def test_add_event04_data_type_error(self):
        """ 日期格式错误 """
        payload = {'id':13,'name':'cc发布会','limit':2000,'status':'1','address':"深圳宝体",
                   'start_time':'2017'}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        print(payload.get('id'), payload.get('name'), payload.get('limit'),
              payload.get('status'), payload.get('address'), payload.get('start_time'))
        self.assertEqual(self.result['status'], 10024)
        self.assertIn('start_time format error.', self.result['message'])

    def test_add_event05_success(self):
        """ 添加成功 """
        payload = {'id':13,'name':'cc发布会','limit':2000,'status':'1',
                   'address':"深圳宝体",'start_time':'2017-05-10 12:00:00'}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        print(payload.get('id'), payload.get('name'), payload.get('limit'),
              payload.get('status'), payload.get('address'), payload.get('start_time'))
        self.assertEqual(self.result['status'], 200)
        self.assertEqual(self.result['message'], 'add event success')


if __name__ == '__main__':
    test_data.init_data() # 初始化接口测试数据
    unittest.main()
