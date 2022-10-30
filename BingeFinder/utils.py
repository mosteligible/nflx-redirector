import yaml


def ReadYamlConfig():
    with open("config.yaml", "r") as fp:
        config = yaml.safe_load(fp)
    return config
