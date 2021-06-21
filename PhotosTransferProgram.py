import os
import time
import shutil
import glob
curDir=os.getcwd()
print(curDir)
count_offile_date=[]
count_ofyears=[]
count_ofmonths=[]
count_offiles_processed=[]
count_offiles_processed01=[]
count_of_destination=[]
count_ofcurr_path=[]

def year(file):
	Mod_time= time.ctime(os.path.getctime(file))
	#The mtime refers to last time the file's contents were changed. 
	#The ctime indicates the last time the inode was altered
	split_list=Mod_time.split()
	count_ofyears.append(split_list[4])
	return split_list[4]


def month(file):
	Mod_time= time.ctime(os.path.getctime(file))
	split_list=Mod_time.split()
	count_ofmonths.append(split_list[1])
	return split_list[1]

def unique_elements(count_ofyears):
	u1= set(count_ofyears)
	u1_setconv=(list(u1))
	return u1_setconv

def dest_fldr_name(file):
	var_ofyear=year(file)
	var_ofmonth=month(file)
	dest= "C:\\Users\\RAKESH PATIL\\Desktop\\i2\\"+var_ofyear+"\\"+var_ofmonth+"\\"
	return dest

def rescursive_copy(src, dest,file):
	if file in os.listdir(src):
		file_path= os.path.join(src, file)

		if os.path.isfile(file_path):
			shutil.copy(file_path, dest)

		elif os.path.isdir(file_path):
			new_dest = os.path.join(dest, item)
			os.mkdir(new_dest)
			rescursive_copy(file_path, new_dest)
	return "succesfull"

def number_dest(i):
	return count_of_destination[i-1]


for root,dirs,files in os.walk(curDir):
	for file in files:
		if file.endswith('.jpg'):
			count_offiles_processed.append(file)
			var_ofyear=year(file)
			var_ofmonth=month(file)
			file_date=var_ofyear+" "+var_ofmonth
			count_offile_date.append(file_date)
			unq_count_ofdate=unique_elements(count_offile_date)
			var_ofdestfolder=dest_fldr_name(file)
			count_of_destination.append(var_ofdestfolder)
			
unq_countof_year=unique_elements(count_ofyears)
unq_countof_month=unique_elements(count_ofmonths)
unq_countof_dest=unique_elements(count_of_destination)
print("the number of processed files:{}".format(len(count_offiles_processed)))
print("unique month and year of the list:{}".format(unq_count_ofdate))
print("unique month and year of the list:{}".format(unq_countof_dest))

for y in unq_countof_year:
	for x in unq_count_ofdate:
		split_element=x.split()
		if split_element[0]==y:
			try:
				os.mkdir("C:\\Users\\RAKESH PATIL\\Desktop\\i2\\"+y+"\\")
				for xy in unq_countof_month:
					if split_element[1]==xy:
						try:
							os.mkdir("C:\\Users\\RAKESH PATIL\\Desktop\\i2\\"+y+"\\"+xy+"\\")
						except:
							print("error is stepping stone to success")
							os.chdir("C:\\Users\\RAKESH PATIL\\Desktop\\i2\\"+y+"\\"+xy+"\\")
						else:
							pass
			except:
				print("error is stepping stone to success")
				os.chdir("C:\\Users\\RAKESH PATIL\\Desktop\\i2\\"+y+"\\")
				for xy in unq_countof_month:
					if split_element[1]==xy:
						try:
							os.mkdir("C:\\Users\\RAKESH PATIL\\Desktop\\i2\\"+y+"\\"+xy+"\\")
						except:
							print("error is stepping stone to success")
							os.chdir("C:\\Users\\RAKESH PATIL\\Desktop\\i2\\"+y+"\\"+xy+"\\")
						else:
							pass
			else:
				os.chdir("C:\\Users\\RAKESH PATIL\\Desktop\\i\\"+y+"\\")
		else:
			pass
i=0
for root,dirs,files in os.walk(curDir):
	for file in files:
		if file.endswith('.jpg'):
			i=i+1
			d=number_dest(i)
			ab = rescursive_copy(curDir,d,file)
			count_offiles_processed01.append(ab)
print(len(count_offiles_processed01))
			


