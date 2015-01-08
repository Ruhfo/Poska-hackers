#!usr/bin/env python 3
import configparser

def write_config():
#Opening config.ini and writting default values there
    config = configparser.ConfigParser()
    config["DEFAULT"] ={"PORT"  : 12345,
                        "NAME"  : "Default chat server"
                       }
    with open("config.ini", "w") as configfile:
        config.write(configfile)

def read_config(configfile):
#Opening config.ini and reading values from there
    config = configparser.ConfigParser()
    config.read("config.ini")
    
    default = config["DEFAULT"]

    port = default.get("PORT","12345")
    name = default.get("NAME", "Default chat server")
    
    port = int(port) #Converting str to int
    
    return (port, name)

def configurator():
#Read configuration file if possible and create one if needed
    try:
        config = open("config.ini", "r")
    except IOError:
        print("File doesn't exist")
        write_config()
    finally:
        port, name = read_config(config)
        config.close()
        return (port, name)

