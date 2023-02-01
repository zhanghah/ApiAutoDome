import yaml
import os 

class YamlUtil:
    # 读取extract.yml文件
    def read_extract_yaml(self):
        path = os.getcwd() + '/extract.yml'
        with open(path, 'r', encoding='utf-8') as f:
            value = yaml.load(stream=f, Loader=yaml.FullLoader)
        return value

    # 写入extract.yml文件
    def write_extract_yaml(self, data):
        path = os.getcwd() + '/extract.yml'
        with open(path, 'a', encoding='utf-8') as f:
            yaml.dump(data=data, stream=f, allow_unicode=True)

    # 清除extract.yml文件
    def clear_extract_yaml(self):
        path = os.getcwd() + '/extract.yml'
        with open(path, 'w', encoding='utf-8') as f:
            f.truncate()

    # 读取测试用例模板
    def read_case_yaml(self, path):
        path = os.getcwd() + '/case/' + path
        with open(path, 'r', encoding='utf-8') as f:
            case = yaml.load(stream=f, Loader=yaml.FullLoader)
        return case

    # 写入测试用了
    def write_case_yaml(self, data, path):
        path = os.getcwd() + '/case/' + path
        with open(path, 'a', encoding='utf-8') as f:
            yaml.dump(data, f, allow_unicode=True)



    
if __name__ == '__main__':
    data = YamlUtil().read_case_yaml('test_search.yml')
    YamlUtil().write_case_yaml(data, 'test.yml')