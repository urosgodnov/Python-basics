#Python uses file objects to interact with external files on your computer.

#Python Opening a file - double slashes!!!!!
myfile = open('.\\SampleDataFiles\\bi_product.txt')

# We can now read the file
myfile.read()

#What happens to read it again
myfile.read()

# Seek to the start of file (index 0)
myfile.seek(0)
myfile.read()

#close it
myfile.close()


#Python writing to a file 
#w+ writes, but deletes the original
#a+ appends to existing
myfile = open('.\\SampleDataFiles\\SampleTextTruncates.txt','w+')

myfile.seek(0)
myfile.read()

myfile

# Write to the file
myfile.write('This is a new line')

myfile.seek(0)
myfile.read()

myfile

myfile.close()

# Appending
myfile = open('.\\SampleDataFiles\\SampleTextAppends.txt','a+')

myfile.seek(0)
myfile.read()

myfile

# Write to the file
myfile.write('This is a new line')

myfile.seek(0)
myfile.read()

myfile

myfile.close()


#Python reading csv and defining parameters
#using pandas library
import pandas as pd
df=pd.read_csv(".\\SampleDataFiles\\bi_product.txt", sep=";")

df

del df



#Python reading excel
#using pandas library
#defining sheet
df=pd.read_excel(".\\SampleDataFiles\\norway_new_car_sales_by_model.xlsx")

df

del df


#Python writing csv
#using pandas library
import pandas as pd

raw_data = {'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'], 
        'last_name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze'], 
        'age': [42, 52, 36, 24, 73], 
        'preTestScore': [4, 24, 31, 2, 3],
        'postTestScore': [25, 94, 57, 62, 70]}

df = pd.DataFrame(raw_data, columns = ['first_name', 'last_name', 'age', 'preTestScore', 'postTestScore'])

df

#Cheking if file exists and if exists, delete it
import os 

myfile=".\\SampleDataFiles\\ExportCSV.csv"

if os.path.isfile(myfile):
    os.remove(myfile)
    
df.to_csv(myfile)

#removing file
if os.path.isfile(myfile):
    os.remove(myfile)


#Python writing excel
#using pandas library
import os 

myfile=".\\SampleDataFiles\\ExportXLSX.xlsx"

if os.path.isfile(myfile):
    os.remove(myfile)
    
df.to_excel(myfile)

#removing file
if os.path.isfile(myfile):
    os.remove(myfile)
