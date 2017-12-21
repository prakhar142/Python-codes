import csv
import shutil
from tempfile import NamedTemporaryFile
# tempfile module generates temporary files and directories. It works on all supported platforms.
# NamedTemporaryFile - Return a file-like object that can be used as a temporary storage area. It will be destroyed as soon as it is closed 
def get_length(file_path):
      with open('data.csv') as csvfile:
          reader = csv.reader(csvfile)
          reader_list = list(reader) # This ensure that everything is a lsit , i.e. evrything will become a big list 
          print(reader_list)
          return len(reader_list)
      

def append_data(file_path,name,email):
      fieldnames=['id','name','email']
      next_id = get_length(file_path)
      with open(file_path,'a') as csvfile:
          writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
          writer.writerow({
                   'id': next_id,
                   'name': name,
                   'email':email,
              })
          
#append_data('data.csv','Justin','hello@gmail.com')    
filename = 'data.csv'
temp_file = NamedTemporaryFile(delete=False)
with open(filename,'r') as csvfile , temp_file:
      reader = csv.DictReader(csvfile)
      fieldnames = ['id','name','email','amount','sent']
      writer = csv.DictWriter(temp_file,fieldnames=fieldnames)
      #writer.writeheader()
      for row in reader:
             print(row)
             writer.writerow({
                   'id': row['id'],
                   'name': row['name'],
                   'email': row['email'],
                   'amount': '1293.23',
                   'sent': '',
                 })

#shutil.move(temp_file.name,filename)
#The shutil module offers a number of high-level operations on files and collections of files. In particular, functions are provided which support file copying and removal.
                   
