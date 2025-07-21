import configparser

default_target_file = ""
default_color_list_file = ""
default_result_name = ""
version_ = "0.0.2"

def config_updator(options=None, for_update=False):
    target_file = default_target_file
    color_list_file = default_color_list_file
    result_name = default_result_name
    version = version_
    if for_update:
        target_file = options["target file"]
        try:
            color_list_file = options["color list file"]
        except:
            color_list_file = ""
        result_name = options["result name"]
        
    config_base = """
[Data Info]
# target file : path of target file.  ex) POSCAR or Dataset/POSCAR # Default(blank) is POSCAR
target file = {target_file}

[Color Setting]
# color list file : path of color list file. Default(blank) is blank. It will set color randomly
# IMPORTANT : Number of colors and number of atoms should be a same number
color list file = {color_list_file}

[Result File Option]
# result name : setting name of output file. # Default(blank) is POSCAR.vesta
result name = {result_name}

[Version]
version = {version}
""".format(target_file=target_file, color_list_file=color_list_file, result_name=result_name, version=version)

    return config_base


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

    except:
        with open('gVfP_config.ini', 'w', encoding='utf-8') as configfile:
            configfile.write(config_updator())
        print("Config file is created : gVfP_config.ini")
        print("Set options and then run this script")
        
        exit()
        
    try:
        version_info = config.get("Version", "version")
        version_match = version_ != version_info
    except:
        version_match = False
    options = config_loader(config)
    if version_match:
        with open('gVfP_config.ini', 'w', encoding='utf-8') as configfile:
            configfile.write(config_updator(options, for_update=True))
        print("config file has been updated.")
        print("Please check configurations.")
        exit()
    return options