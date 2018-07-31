#! /usr/bin/python
# coding:utf-8


import requests


class WebHttpTestSuites:
    """
    没有定义头部，故只支持简单的 HTTP POST JSON 请求
    """

    def __init__(self):
        self.protocol = 'http'
        self.host = ''
        self.port = 8080
        self.location = ''

    @staticmethod
    def do_get():
        web_page = requests.get('http://www.baidu.com')
        print(web_page.text)

    def do_post(self, protocol, host, port, location):
        self.protocol = protocol
        self.host = host
        self.port = port
        self.location = location

        url = self.protocol + '://' + self.host + ':' + str(self.port) + self.location
        print("请求地址为：" + url)
        body_json = {"deviceId": "string_test", "loginName": "85588102450", "smsCode": "123004"}
        print("请求体：" + str(body_json))
        r = requests.post(url, json=body_json)

        rsp_json = r.json()

        print("实际响应体为：" + str(rsp_json))
        print("实际业务返回码：" + rsp_json['rspCd'])
        assert rsp_json['rspCd'] == '00000', '业务返回结果异常'


if __name__ == '__main__':
    brs = WebHttpTestSuites()
    brs.do_post(protocol=brs.protocol, host='192.168.7.130', port=brs.port,
                location='/hd-gateway-web/register/smsToken.do')
