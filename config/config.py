import yaml


class Config:
    def __init__(self, debug=False):
        self.debug = debug
        # 读取YAML配置文件
        with open('application.yml', 'r') as file:
            self.config = yaml.safe_load(file)


# 示例用法
if __name__ == "__main__":
    # 从环境变量加载配置
    config = Config()
