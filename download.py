# -*- coding: utf-8 -*-
import wget
import json 
import os
import re
from pathlib import Path
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
# The File downloaded from digital ocean is xml 
## Convert XML to JSON using any online converter 
## Save the Converted Json to /digitalocean_space_data
## This Script can be used also with s3 bucket xml .
## am using digital ocean droplet for downloading and uploading the data to another server 
## There is another paid services like transfer in videos website , but for full hd it cost's a lot for service I need .

def folder_manager(path):
    path_to_folder_array = path.split('/')
    if path_to_folder_array[-1] == '':
        path_to_folder_array.pop()
    create_if_not_exist(path_to_folder_array)
 
 
def pass_folder_type(filename):
    print(Path(filename).suffix)
    if Path(filename).suffix == '.mp4' or Path(filename).suffix == '.txt':
        return False
    else:
        return True
    
    
# replacing slashes with dashes for  downloaded folder naming 
def url_to_name(download_url):
    return download_url.replace('/' , '-')
     
    

def download_file(folder , local_location):
    path = local_location[10:]
    url = 'https://example.fra1.digitaloceanspaces.com/' +  path
    download_url = url + folder
    video_folder_name = url_to_name(path) + folder
    try:
        wget.download(download_url , local_location + video_folder_name  )
    except: 
        print('File Failed to download')
        
    
    


## Looping throw folder order , if exist create the subfolder

def create_if_not_exist(folder_arrays):
    path = './folders/'
    for folder in folder_arrays:
        if pass_folder_type(folder) is True:
            path = path + folder
            try:
                ## if folder order 0 and created 
                os.mkdir(path)
                print("Directory " , folder ,  " Created ") 
            except FileExistsError:
                print("Directory " , folder ,  " already exists")
                path = path + '/'
        else:
            download_file(folder , path)
        
            
        
        
    
    
    
with open('./digitalocean_space_data/data.json') as json_file:
    print('Beginning file download with wget module')
    space_data = json.loads(json_file.read())
    space_data_content = space_data['ListBucketResult']['Contents']
    for item in space_data_content:
        folder_manager(item['Key'])
    

    



# url = 'http://i3.ytimg.com/vi/J---aiyznGQ/mqdefault.jpg'
# wget.download(url, './cat4.jpg')