import argparse
import os
from TTS.api import TTS
import shutil
import logging
<<<<<<< HEAD
from src.utils.common import read_yaml, create_directories, read_text
=======
from src.utils.common import read_yaml, create_directories, read_text, create_dir_file
# from src.utils.common1 import read_txt
>>>>>>> 16b9d55c7ce16ee3d9209987d1a679de3967914a
import random
import subprocess


STAGE = "Data Ingestion" ## <<< change stage name 

create_dir_file("logs","running_logs.log")
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
<<<<<<< HEAD

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
=======
 
    text1 = " ".join(read_text(text_file_path))

    model_name = TTS.list_models()[0]
    # Init TTS
    tts = TTS(model_name)
 
    wav = tts.tts("This is a test! This is also a test!!", speaker=tts.speakers[0], language=tts.languages[0])
    # Text to speech to a file
    return(
    tts.tts_to_file(text=text1, speaker=tts.speakers[0], language=tts.languages[0], file_path=output_file_path))
>>>>>>> 16b9d55c7ce16ee3d9209987d1a679de3967914a


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