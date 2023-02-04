import os
import yaml
import logging
import time
import pandas as pd
import json


def read_txt():
    print(os.getcwd())
    path = "TTS_project/data/"
    os.chdir(path=path)
    print(os.listdir())
    # f = open("../../data/sample.txt", "r",encoding="utf8")
    # logging.info(f"reading file done")
    # file = f.readlines()
    # f.close()
    # return file

    # with open(text) as txt_file:
    #     content = yaml.safe_load(yaml_file)
    # logging.info(f"yaml file: {path_to_yaml} loaded successfully")
    # return content
# read_txt()

    # fileObject = open("sample.txt", "r")
    # data = fileObject.read()
    # print(data)