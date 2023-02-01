# 解决导包不成功
import json
import os
import sys
path = os.path.dirname(os.path.dirname(__file__))
sys.path.append(path)
import json
import requests


from common.logger_util import LogUtil


class RequestsUtil:
    # 实例化日志对象
    logger = LogUtil().getlogger('case.log')

    # 类变量，通过类名访问
    session = requests.session()
    
    # 发送请求
    def send_request(self, method, url, data=None, **kwargs):

        # 转小写
        method = str(method).lower()
        if method == 'get':
            # 写入请求日志
            RequestsUtil().logger.info('----------接口请求开始----------')
            res = RequestsUtil.session.request(method, url=url, params=data, **kwargs)
        else:
            data = json.dumps(data)
            # 写入请求日志
            RequestsUtil().logger.info('----------接口请求开始----------')
            res = RequestsUtil.session.request(method, url=url, data=data, **kwargs)
        # 写入请求日志
        RequestsUtil().logger.info('请求地址:{}'.format(url))
        RequestsUtil().logger.info('请求参数:{}'.format(data))
        RequestsUtil().logger.info('接口返回信息:{}'.format(res.text))
        RequestsUtil().logger.info('--------------------------------------------------------------------接口请求结束--------------------------------------------------------------------')

        return res

        
        

# if __name__ == '__main__':
#     logger = LogUtil().getlogger('case')
#     logger.info('jjj')
        