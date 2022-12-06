import yaml

class YamlUtil:

    @classmethod
    def read_yaml(self):
        with open('sxy_open.yaml', mode='r', encoding='utf-8') as f:
            value = yaml.load(stream=f, Loader=yaml.FullLoader)
            return value


if __name__ == '__main__':
    YamlUtil.read_yaml()



