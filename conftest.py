import pytest

from common.yaml_util import YamlUtil

@pytest.fixture(scope='session', autouse=True)
def clear_yaml():
    YamlUtil().clear_extract_yaml()