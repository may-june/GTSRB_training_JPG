from PIL import Image
import pandas as pd
import os

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)

image_root = './Final_Training/Images/'
image_dst = './Final_Training_JPG/'
for f in range(0,43):
	
    # save folder name as the format: 00042
    folder = format(f, '05d')
    fol = image_dst+ format(f, '05d')
    createFolder(fol)
	
    csv_path = image_root + folder + '/GT-' + folder + '.csv'
    csv = pd.read_csv(csv_path, sep= ';')
    ppm_name = csv['Filename']
    # len(ppm_name) = how many rows in csv file
    for i in range(0, len(ppm_name)):
        im = Image.open(image_root + folder + '/' + csv['Filename'][i])
        im.save(fol+'/'+ csv['Filename'][i].replace('ppm', 'jpg'))
