#!usr/bin/env python 3
import configparser

def write_config():
    config = configparser.ConfigParser()
    config["DEFAULT"] ={"PORT"  : 12345,
                        "NAME"  : "Default chat server"
                       }
    with open("config.ini", "w") as configfile:
        config.write(configfile)

#Read existing config file to retrieve settings
def read_config(configfile):
    config = configparser.ConfigParser()
    config.read("config.ini")
    
    global port
    global name

    default = config["DEFAULT"]

    port = default.get("PORT","12345")
    name = default.get("NAME", "Default chat server")
    
    port = int(port) #Converting str to int
    
    return (port, name)

def configurator():
    try:
        config = open("config.ini", "r")
    except IOError:
        print("File doesn't exist")
        write_config()
    finally:
        port, name = read_config(config)
        config.close()
        return (port, name)

