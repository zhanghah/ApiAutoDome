# 解决导包不成功
import json
import os
import sys
path = os.path.dirname(os.path.dirname(__file__))
sys.path.append(path)

from common.yaml_util import YamlUtil
from common.requests_util import RequestsUtil
import pytest


class TestApi:
    # 获取登录测试用例数据
    @pytest.mark.parametrize('caseInfo', YamlUtil().read_case_yaml('test_login.yml'))
    def test_01_login(self, caseInfo):
        method = caseInfo['api_request']['method']
        url = caseInfo['api_request']['url']
        data = caseInfo['api_request']['data']
        headers = caseInfo['api_request']['headers']
        validate = caseInfo['api_validate']

        res = RequestsUtil().send_request(method, url=url, data=data, headers=headers)

        # 登陆成功保存token
        if res.json()['code'] == 200:
            token = res.json()['data']['access_token']
            YamlUtil().write_extract_yaml({'token': token})

        # 断言
        for v in validate:
            if v == 'status_code':
                assert validate[v] == res.status_code, 'code值为200'
            else:
                assert validate[v] == res.json()[v]  
    
    # 获取查询测试用数据
    @pytest.mark.parametrize('caseInfo', YamlUtil().read_case_yaml('test_search.yml'))
    def test_02_search_user(self, caseInfo):
        method = caseInfo['api_request']['method']
        url = caseInfo['api_request']['url']
        data = caseInfo['api_request']['data']
        headers = caseInfo['api_request']['headers']
        validate = caseInfo['api_validate']

        # 获取token并替换
        token = YamlUtil().read_extract_yaml()['token']
        headers['Authorization'] = token

        # 接收响应数据
        res = RequestsUtil().send_request(method, url=url, data=data, headers=headers)

        # 断言
        for v in validate:
            if v == 'status_code':
                assert validate[v] == res.status_code, 'code值为200'
            else: 
                assert validate[v] == res.json()[v], '接口状态码为200'
        assert data['userName'] == res.json()['data']['list'][0]['userName'], '查询后的数据为{}'.format(data['userName'])

if __name__ == '__main__':
    pytest.main(['-vs'])