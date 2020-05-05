import os
import ftplib
from tqdm import tqdm
from decouple import config
import logging

logger = logging.getLogger('app')
hdlr = logging.FileHandler('./app.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr) 
logger.setLevel(logging.INFO)


def list_files(dir):
    session = ftplib.FTP(config('FTP_HOST'),config('FTP_USERNAME'),config('FTP_PASSWORD'))
    r = []
    for root, dirs, files in os.walk(dir):
        for name in files:
            file_name = os.path.join(root, name)
            filesize = os.path.getsize(file_name)
            file = open(file_name,'rb')
            logger.info('Just Started to Upload  ' + file_name)
            with tqdm(unit = 'blocks', unit_scale = True, leave = False, miniters = 1, desc = 'Uploading......', total = filesize) as tqdm_instance:
                session.storbinary('STOR ' + name, file, 2048, callback = lambda sent: tqdm_instance.update(len(sent)))
            logger.info('Finish Download')
            file.close()
    session.quit()

list_files(config('FOLDER_LOCATION_TO_UPLOAD'))