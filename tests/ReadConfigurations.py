from configparser import ConfigParser


def read_configuration(category,key):
    config = ConfigParser()
    config.read("configurations/config.ini")
    return config.get(category,key)


def update_configuration(category, key, value):
    config = ConfigParser()
    config.read("configurations/config.ini")
    config[category][key] = value
    with open('configurations/config.ini', 'w') as configfile:
        config.write(configfile)


def get_county_list(category):
    config = ConfigParser()
    config.read("configurations/config.ini")
    values = [value.strip() for value in config.get(category, 'list_county').split(',')]
    print(values)
    return values

if __name__ == '__main__':
    #read_configuration("basic info","url")
    get_county_list("basic info")