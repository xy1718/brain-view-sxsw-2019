from PIL import Image
import numpy as np
import scipy.misc
import pandas as pd
import os

index = 1
for file in os.listdir('csvs'):
    path=os.path.join('csvs', file)
    print(path)
    df = pd.read_csv(path,delim_whitespace=True)
    data = np.array(df)
    print(df.shape)
    data[:,0] += 100
    data[:,0] *= 255/200
    data[:,1] *= 2.5
    data[:,2] *= 2.5
    img = np.reshape(data, (200, 200, 3))
    print(data)
    name = "images/{}{}".format(index, 'img.jpg')
    jpg = scipy.misc.imsave(name, img)
    index += 1



