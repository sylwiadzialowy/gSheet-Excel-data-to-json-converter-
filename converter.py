
#note that the path needs to be updated according to where your data set is located#
file_path = r'...\\dane.csv'

print('{\n\t"users": [\n')
      
with open(file_path,"r") as file:
 
    for line in file:
 
        line = line.replace('\n','')
        userData = line.split(',')
        print('\t\t{\n\t\t\t"id": "%s",\n\t\t\t"firstName": "%s",\n\t\t\t"lastName": "%s",\n\t\t\t"street": "%s",\n\t\t\t"apartment": "%s",\n\t\t\t"city" :"%s",\n\t\t\t"country": "%s",\n\t\t\t"phone": "%s",\n\t\t\t"email": "%s"\n\t\t},\n' % (userData[0],userData[1],userData[2],userData[3],userData[4],userData[5],userData[6],userData[7],userData[8])) 

print('\t]\n}')
