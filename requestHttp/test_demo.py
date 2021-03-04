# -*- coding: utf-8 -*-
# 创建时间：2021/3/4 21:02
import requests


class TestDemo:
    def test_demo(self):
        r = requests.get('https://httpbin.testing-studio.com/get')
        print("cessssssssss")
        print(r.text)
        print(r.json())
        print(r.status_code)

    def test_get(self):
        print("开始")
        payload = {
            "lever": 1,
            "name": "wangjian"
        }
        r = requests.get('https://httpbin.testing-studio.com/get', params=payload)
        print(r.text)
        print(r.json())

    def test_form(self):
        print("开始")
        payload = {
            "lever": 1,
            "name": "wangjian"
        }
        r = requests.post('https://httpbin.testing-studio.com/post', data=payload)
        print(r.text)
        print(r.json())

    def test_file(self):
        print("开始")
        myfiles = {'file': open('report.xls', 'rb')}
        r = requests.post('https://httpbin.testing-studio.com/post', files=myfiles)
        print(r.text)
        print(r.json())

    def test_headers(self):
        print("开始")
        myheaders = {'user-agent': 'my-app/0.0.1'}
        r = requests.get('https://httpbin.testing-studio.com/get', headers=myheaders)
        print(r.text)
        print(r.json())
        assert r.status_code == 200
        assert r.json()['headers']["User-Agent"] == 'my-app/0.0.1'

    def test_cookies(self):
        print("开始")
        mycookie = dict(cookies_are='working')
        r = requests.get('https://httpbin.testing-studio.com/get', cookies=mycookie)
        print(r.text)
        print(r.json())
