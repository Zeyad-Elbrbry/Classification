import csv
import numpy as np

with open('E:\Semester10\Machine Learning\Classification Project\clean_2014.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    n_samples = 141246
    n_features = 59
    y = np.zeros(n_samples)
    x = np.zeros((n_samples,n_features))
    #x = [[0 for n in range(59)] for m in range(141246)]
    i = 0
    for line in csv_reader:
         j = 0
         y[i] = float(line[11])
         for k in range(len(line)):
             if (k != 0):
                 if(k != 1):
                     if(k != 11):
                        x[i][j] = float(line[k])
                        j += 1        
         i += 1
n_classes = 3
Y = np.zeros((n_samples,n_classes))
for i in range(n_samples):
    if (y[i] == 0):
        Y[i] = [1,0,0]
    if (y[i] == 1):
        Y[i] = [0,1,0]
    if (y[i] == 2):
        Y[i] = [0,0,1]
   #Y = [[0 for n in range(3)] for m in range(141246)]
zeros = 0
ones = 0
twos = 0
Xzeros = np.zeros((119903,59))
Xones = np.zeros((19792,59))
Xtwos = np.zeros((1551,59))


for i in range(141246):
    if (y[i] == 0):
        Xzeros[zeros] = x[i]
        zeros += 1
        Y[i] = [1,0,0]
    if (y[i] == 1):
        Xones[ones] = x[i]
        ones += 1
        Y[i] = [0,1,0]
    if (y[i] == 2):
        Xtwos[twos] = x[i]
        twos += 1
        Y[i] = [0,0,1]

xtrain = np.zeros((98872,59))
ytrain = np.zeros((98872,3))

for i in range(83932):
    xtrain[i] = Xzeros[i]
    ytrain[i] = [1,0,0]
    
for j in range(83932, 97783):
    i = 0
    xtrain[j] = Xones[i]
    ytrain[j] = [0,1,0]
    i+=1

for k in range(97783, 98872):
    i = 0
    xtrain[k] = Xtwos[i]
    ytrain[k] = [0,0,1]
    i+=1
    
xtest = np.zeros((42374,59))
ytest = np.zeros((42374,3))

for i in range(35971):
    j = 83932
    xtest[i] = Xzeros[j]
    ytest[i] = [1,0,0]
    j += 1
    
for j in range(35971, 41907):
    i = 13851
    xtest[j] = Xones[i]
    ytest[j] = [0,1,0]
    i+=1

for k in range(41907, 42374):
    i = 1089
    xtest[k] = Xtwos[i]
    ytest[k] = [0,0,1]
    i+=1

    
    
    



    #with open('new_names.csv', 'w') as new_file:
     #   fieldnames = ['first_name', 'last_name']

      #  csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')

       # csv_writer.writeheader()

        #for line in csv_reader:
         #   del line['email']
          #  csv_writer.writerow(line)
          
          
