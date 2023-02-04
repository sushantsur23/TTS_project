import argparse
import os
import shutil
import logging
from src.utils.common import read_yaml, create_directories, read_text
import random
import subprocess


STAGE = "Data Ingestion" ## <<< change stage name 

logging.basicConfig(
    filename=os.path.join("logs", 'running_logs.log'), 
    level=logging.INFO, 
    format="[%(asctime)s: %(levelname)s: %(module)s]: %(message)s",
    filemode="a"
    )


def main(config_path, params_path):
    ## read config files
    config = read_yaml(config_path)
    params = read_yaml(params_path)

    text_file_path = config['data']["data_file"]

    output_dir = config["data"]["output_dir"]
    create_directories([output_dir])

    log_path = config["data"]["log_dir"]
    log_file_name = config["data"]["log_file_name"]
    create_directories([log_path])

    output_file_name = config["data"]["file_name"]
    output_file_path = os.path.join(output_dir, output_file_name)

    text_dir = config['data']['text_dir']
    text_file = config['data']['text_file']
    text_file_path = os.path.join(text_dir,text_file)

    data = read_text(text_file_path)
    model_name = config["data"]["model_name"]
    model_dir = os.path.join(output_dir,model_name)

    cmd = "!tts --text 'hello world' --model_name 'tts_models/en/ljspeech/glow-tts' --out_path output.wav"
    print(f"cmd is----->> {cmd}")
    subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # if not os.path.isfile(output_file_path):
    #     logging.info("downloading model started...")
    #     # cmd = "tts --text data --model_name tts_models/en/ljspeech/glow-tts --out_path output.wav"
    #     cmd = "tts --text 'hello world' --model_name 'tts_models/en/ljspeech/glow-tts' --out_path output.wav"
    #     print(f"cmd is----->> {cmd}")
    #     subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument("--config", "-c", default="configs/config.yaml")
    args.add_argument("--params", "-p", default="params.yaml")
    parsed_args = args.parse_args()

    try:
        logging.info("\n********************")
        logging.info(f">>>>> stage {STAGE} started <<<<<")
        main(config_path=parsed_args.config, params_path=parsed_args.params)
        logging.info(f">>>>> stage {STAGE} completed!<<<<<\n")
    except Exception as e:
        logging.exception(e)
        raise 