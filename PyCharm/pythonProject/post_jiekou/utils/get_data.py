from ruamel import yaml



def get_tags():
    with open("./datas.yml") as f:
        data_tag = yaml.safe_load(f)
        print(data_tag)
    return data_tag