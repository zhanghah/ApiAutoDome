'''
Author: zhanghah 1915579714@qq.com
Date: 2023-01-31 14:37:25
LastEditors: zhanghah 1915579714@qq.com
LastEditTime: 2023-02-03 08:57:57
FilePath: \ApiAutoDome\conftest.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import pytest

from common.yaml_util import YamlUtil

@pytest.fixture(scope='session', autouse=True)
def clear_yaml():
    YamlUtil().clear_extract_yaml()
    