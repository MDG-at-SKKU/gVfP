import configparser


config_base = """
[Data Info]
# target file : path of target file.  ex) POSCAR or Dataset/POSCAR
target file = # Default(blank) is POSCAR

[Result File Option]
result name = # Default(blank) is POSCAR.vesta
"""

def config_loader(config):
    options = dict()
    for section in config.sections():
        # print(section)
        for option in config.options(section):
            options[option] = config.get(section, option)
    
    if options['target file'] == '':
        options['target file'] = "POSCAR"
    if options['result name'] == '':
        options['result name'] = "POSCAR.vesta"

    return options

def config_is_exist():
    config = configparser.ConfigParser(inline_comment_prefixes="#")
    try:
        config.read("gVfP_config.ini")
        config.get("Data Info", "target file")
        options = config_loader(config)
        return options
    except:
        with open('gVfP_config.ini', 'w', encoding='utf-8') as configfile:
            configfile.write(config_base)
        print("Config file is created : gVfP_config.ini")
        print("Set options and then run this script")
        
        exit()