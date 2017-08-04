import dicom # for reading dicom files
import os # for doing directory operations
import pandas as pd # for some simple data analysis (right now, just to load in the labels data and quickly reference it)
import numpy as np

labels = pd.read_csv('mass-data.csv', usecols=[0,2,3,4,8])
labels['path'] = ("")
for index, row in labels.iterrows():
	labels.iloc[index, labels.columns.get_loc('path')] = 'Mass-Training_'+str(row['patient_id'])+'_'+row['side']+'_'+row['view']+'_'+str(row['abn_num'])
	# row['path'] = 'Mass-Training_'+row['patient_id']+'_'+row['side']+'_'+row['view']+'_'+row['abn_num']
labels.pop('side')
labels.pop('view')
labels.pop('abn_num')
labels.pop('patient_id')
dir = os.walk("DOI")
for index, row in labels.iterrows():
	if(os.path.isdir("DOI/"+row["path"])):
		folder = os.listdir("DOI/"+row["path"])
		folder = [x for x in folder if x != ".DS_Store"]
		if(os.path.isdir("DOI/"+row["path"]+"/"+folder[0])):
			folder2 = os.listdir("DOI/"+row["path"]+"/"+folder[0])
			folder2 = [x for x in folder2 if x != ".DS_Store"]
			ds=dicom.read_file("DOI/"+row["path"]+"/"+folder[0]+"/"+folder2[0]+"/"+"000000.dcm")
			print(ds)
		