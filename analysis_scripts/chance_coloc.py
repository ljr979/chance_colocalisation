import os, re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from loguru import logger

input_folder ='raw_data/CHANCE COLOC/'
output_folder = 'results/python_results/'


if not os.path.exists(output_folder):
    os.makedirs(output_folder)


coloc_files =[[f'{root}/{filename}' for filename in files if 'client' and 'colocalisation' in filename] for root, dirs, files in os.walk(f'{input_folder}')]
coloc_files=[item for sublist in coloc_files for item in sublist]
client_coloc = [item for item in coloc_files if 'client' in item]
hsp_coloc=[item for item in coloc_files if 'Hsp' in item]


# this way finds the percent colocalisation of all the spots detected from all the images
client = []
for filepath in client_coloc:


    data = pd.read_csv(filepath)
    data.drop([col for col in data.columns.tolist() if ' ' in col], axis=1, inplace=True)
    data['filepath']=filepath
    client.append(data)
client=pd.concat(client)

client_coloc_blah = client[client['distance']>-1]
count_client_coloc=len(client_coloc_blah)
total_client_molecules = len(client)
percent_colocal = (count_client_coloc/total_client_molecules)*100

#this way finds the colocalisation for each image (and then 10 replicates essentially)
percent_colocalisation =[]
file_number_list=[]
for filepath in client_coloc:

    file_number=int(filepath.split('/')[-2])
    file_number_list.append(file_number)
    data = pd.read_csv(filepath)
    data.drop([col for col in data.columns.tolist() if ' ' in col], axis=1, inplace=True)
    client_coloc_count = data[data['distance']>-1]
    total_coloc_client = len(data)
    client_coloc_count = len(data[data['distance']>-1])
    percent_colocal = (client_coloc_count/total_coloc_client)*100
    percent_colocalisation.append(percent_colocal)
    
client=pd.concat(client)

client_coloc_count = client[client['distance']>-1]
