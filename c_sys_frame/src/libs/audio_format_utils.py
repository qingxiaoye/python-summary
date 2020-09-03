# -*- coding:utf-8 -*-
import subprocess
import os
from libs.path_utils import get_file_name, get_file_path, get_file_format, get_file_exte, get_date_dir
from libs.cfg_utils import get_config_dict
from libs.global_logger import get_logger
from scipy.io import wavfile
import numpy as np
logger = get_logger(__name__)


def channel_split(wav_file):
    sr, data = wavfile.read(wav_file)
    if np.ndim(data) > 1:
        data_left = data[:,0]
        data_right = data[:,1]
        wav_file_left = wav_file.split(".")[0] + "_1.wav"
        wav_file_right = wav_file.split(".")[0] + "_2.wav"
        print(wav_file_left)
        wavfile.write(wav_file_left, sr, data_left)
        wavfile.write(wav_file_right, sr, data_right)
        return {wav_file_left:1, wav_file_right:2}
    else:
        return {wav_file:0}

def audio_to_wav(audio_file, wav_file):
    try:
        istelaudio = int(get_config_dict().get('AudioFormat', None).get('istelaudio', None) or 0)
        if istelaudio == 1:
            sample_rate = 8000
        elif istelaudio == 2:
            sample_rate = 16000

        wave_cmd = "ffmpeg -i {audio_file} -acodec pcm_s16le -ar {sample_rate} {wav_file}".format(
            audio_file=audio_file, sample_rate=sample_rate, wav_file=wav_file)
        print(wave_cmd)
        cmd_result = subprocess.call([wave_cmd], shell=True)
        if cmd_result == 0:
            return wav_file
        else:
            audio_format = get_file_format(audio_file)
            logger.error("{audio_format} to wav fail，error code：{cmd_result}.".format(audio_format=audio_format, cmd_result=cmd_result))
            return
    except Exception as exp:
        logger.error("error message: %s", exp)


def wav_to_wav(audio_file, wav_file):
    try:
        istelaudio = int(get_config_dict().get('AudioFormat', None).get('istelaudio', None) or 0)
        if istelaudio == 1:
            sample_rate = 8000
        elif istelaudio == 2:
            sample_rate = 16000

        wave_cmd = "sox {audio_file} -r {sample_rate} -b 16 {wav_file} highpass 10".format(
            audio_file=audio_file, wav_file=wav_file, sample_rate=sample_rate)
        print(wave_cmd)
        cmd_result = subprocess.call([wave_cmd], shell=True)
        if cmd_result == 0:
            return wav_file
        else:
            logger.error("wav to wav fail，error code：%s。", cmd_result)
            return
    except Exception as exp:
        logger.error("error message: %s", exp)

def vox_to_wav(audio_file, wav_file):
    try:
        temp_path = os.path.abspath(os.path.join(get_file_path(wav_file), 'temp'))
        vox_file = audio_file
        istelaudio = int(get_config_dict().get('AudioFormat', None).get('istelaudio', None) or 0)
        if istelaudio == 1:
            sample_rate = 8000
        elif istelaudio == 2:
            sample_rate = 16000
        wave_cmd = "sox  -r 8000 {vox_file} -r {sample_rate} -b 16 {wav_file}  highpass 10".format(
            vox_file=vox_file, wav_file=wav_file, sample_rate=sample_rate)
        print(wave_cmd)
        cmd_result = subprocess.call([wave_cmd], shell=True)
        if cmd_result == 0:
            if os.path.exists(temp_path):
                rm_cmd = "rm -rf {temp_path} ".format(temp_path=temp_path)
                cmd_result = subprocess.call([rm_cmd], shell=True)
                if cmd_result != 0:
                    logger.error("删除文件失败，返回码：%s。", cmd_result)
            return wav_file
        else:
            logger.error("vox to wav fail，error code：%s。", cmd_result)
            return
    except Exception as exp:
        logger.error("error message: %s", exp)


def v3_to_wav(audio_file, wav_file):
    try:
        temp_path = os.path.abspath(os.path.join(get_file_path(wav_file), 'temp'))
        audio_file_name = get_file_name(audio_file)
        if not os.path.exists(temp_path):
            os.makedirs(temp_path)
        temp_vox_file = os.path.join(temp_path, audio_file_name + ".vox")

        move_cmd = "cp {audio_file} {temp_vox_file}".format(audio_file=audio_file, temp_vox_file=temp_vox_file)
        cmd_result = subprocess.call([move_cmd], shell=True)
        if cmd_result == 0:
            wav_file = vox_to_wav(temp_vox_file, wav_file)
            return wav_file
        else:
            logger.error("v3 to wav fail，error code：%s。", cmd_result)
            return
    except Exception as exp:
        logger.error("error message: %s", exp)


def pcm_to_wav(audio_file, wav_file):
    try:
        istelaudio = int(get_config_dict().get('AudioFormat', None).get('istelaudio', None) or 0)
        sample_rate = 8000
        if istelaudio == 1:
            sample_rate = 8000
        elif istelaudio == 2:
            sample_rate = 16000

        wave_cmd = "sox -t raw -e signed-integer -b 16 -r {sample_rate} {audio_file} {wav_file}".format(
            audio_file=audio_file, wav_file=wav_file, sample_rate=sample_rate, )

        cmd_result = subprocess.call([wave_cmd], shell=True)
        if cmd_result == 0:
            return wav_file
        else:
            logger.error("pcm to wav fail，error code：%s。", cmd_result)
            return

    except Exception as exp:
        logger.error("error message: %s", exp)


def m4a_to_wav(audio_file, wav_file):
    try:
        wave_cmd = "ffmpeg -i {audio_file} {wav_file}".format(audio_file=audio_file, wav_file=wav_file)
        cmd_result = subprocess.call([wave_cmd], shell=True)
        if cmd_result == 0:
            return wav_file
        else:
            logger.error('m4a to wav fail, error code: %s.', cmd_result)
            return
    except Exception as exp:
        logger.error('error message: %s', exp)


def avi_to_wav(audio_file, wav_file):
    try:
        wave_cmd = "ffmpeg -i {audio_file} {wav_file}".format(audio_file=audio_file, wav_file=wav_file)
        cmd_result = subprocess.call([wave_cmd], shell=True)
        if cmd_result == 0:
            return wav_file
        else:
            logger.error('avi to wav fail, error code: %s.', cmd_result)
            return
    except Exception as exp:
        logger.error('error message: %s', exp)

def mp3_to_wav(audio_file, wav_file):
    try:
        wave_cmd = "ffmpeg -i {audio_file} {wav_file}".format(audio_file=audio_file, wav_file=wav_file)
        cmd_result = subprocess.call([wave_cmd], shell=True)
        if cmd_result == 0:
            return wav_file
        else:
            logger.error('mp3 to wav fail, error code: %s.', cmd_result)
            return
    except Exception as exp:
        logger.error('error message: %s', exp)


def wma_to_wav(audio_file, wav_file):
    try:
        wave_cmd = "ffmpeg -i {audio_file} {wav_file}".format(audio_file=audio_file, wav_file=wav_file)
        cmd_result = subprocess.call([wave_cmd], shell=True)
        if cmd_result == 0:
            return wav_file
        else:
            logger.error('wma to wav fail, error code: %s.', cmd_result)
            return
    except Exception as exp:
        logger.error('error message: %s', exp)


def wav_to_wma(audio_file, wma_file):
    try:
        istelaudio = int(get_config_dict().get('AudioFormat', None).get('istelaudio', None) or 0)
        if istelaudio == 1:
            sample_rate = 8000
        elif istelaudio == 2:
            sample_rate = 16000
        # channels = 1
        bit_rate = 25000
        wma_cmd = "ffmpeg -y  -i {audio_file} -acodec wmav2  -ar {sample_rate}  " \
                  "-ab {bit_rate} {wma_file} -loglevel quiet" \
            .format(audio_file=audio_file,
                    wma_file=wma_file,
                    sample_rate=sample_rate,
                    bit_rate=bit_rate)

        cmd_result = subprocess.call([wma_cmd], shell=True)
        if cmd_result == 0:
            return wma_file
        else:
            logger.error("wav to wma fail，error code：%s。", cmd_result)
            return

    except Exception as exp:
        logger.error("error message: %s", exp)


def wav_to_ogg(audio_file, ogg_file):
    try:
        ogg_cmd = "sox {audio_file} {ogg_file}".format(audio_file=audio_file, ogg_file=ogg_file)
        cmd_result = subprocess.call([ogg_cmd], shell=True)
        if cmd_result == 0:
            return ogg_file
        else:
            logger.error('wav to ogg fail, error code: %s.', cmd_result)
            return
    except Exception as exp:
        logger.error('error message: %s', exp)


def wav_to_mp3(audio_file, mp3_file):
    try:
        ogg_cmd = "lame {audio_file} {mp3_file}".format(audio_file=audio_file, mp3_file=mp3_file)
        cmd_result = subprocess.call([ogg_cmd], shell=True)
        if cmd_result == 0:
            return mp3_file
        else:
            logger.error('wav to mp3 fail, error code: %s.', cmd_result)
            return
    except Exception as exp:
        logger.error('error message: %s', exp)