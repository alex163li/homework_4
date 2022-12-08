# 3 - В файле, содержащем фамилии студентов и их оценки, изменить на буквы в верхнем регистре 
# тех студентов, которые имеют средний балл более «4».Нужно перезаписать файл. 

def return_line_str(file):
    data = open(file, 'r',encoding='UTF8')
    n_list = [] 
    for line in data:
        [n_list.append(line.rstrip())] 
    data.close()  
    return n_list

def line_upper(n_list):
    for i in range(0,len(n_list)):    
        if ('4' in n_list[i]) or ('5' in n_list[i]):
            n_list[i] = n_list[i].upper()
    return n_list         

def write_to_file(n_list,file):
    data = open(file,'w+',encoding='UTF8')
    for i in n_list:    
        data.write(f'{i}\n')
    data.close()

path = '/Users/m1/Desktop/homework_4/file.txt'
full_list = return_line_str(path)
print(write_to_file(line_upper(full_list),path))