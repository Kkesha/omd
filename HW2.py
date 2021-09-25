import csv

def print_hierarchy_of_command ():
    """Печатает название департамента и команды, 
    входящие в каждый департамент"""
    with open('./Corp Summary.csv', 'r',encoding = 'utf-8') as f:
        reader = csv.reader(f, delimiter=';')
        next(reader)
        hierarchy_of_command = {}
        for row in reader:
            department = row[1]
            if department not in hierarchy_of_command.keys():
                hierarchy_of_command[department] = [row[2]]
            else:
                if row[2] not in hierarchy_of_command[department]:
                    hierarchy_of_command[department].append(row[2])
    for key, value in hierarchy_of_command.items():
        str_for_print = ', '.join(value)
        print(f'{key} => {str_for_print}')
        
def make_dict_consolidated_report () -> dict:
    """Собирает отчет по департаментам в словарь"""
    with open('./Corp Summary.csv', 'r',encoding = 'utf-8') as f:
        reader = csv.reader(f, delimiter=';')
        next(reader)
        report_department = {}
        for row in reader:
            department = row[1]
            if department not in report_department.keys():
                report_department[department] = [1, int(row[5])]
            else:
                report_department[department][0] += 1
                report_department[department].append(int(row[5]))
    return report_department
    
def print_consolidated_report ():
    """Печатает отчет по каждому департаменту"""
    report_department = make_dict_consolidated_report()    
    print('Название    Численность Вилка зарплаты Средняя зарплата')    
    for key, value in report_department.items():
        avg_salary = float('{:.2f}'.format(sum(value[1::])/value[0]))
        print(f'{key}     {value[0]}      ({min(value[1::])}, {max(value[1::])})      {avg_salary}')
              
         
def save_consolidated_report ():
    """Сохраняет отчет по каждому департаменту в файл Сonsolidated report.csv"""
    report_department = make_dict_consolidated_report()     
    with open('./Сonsolidated report.csv', 'w', newline="", encoding='utf-8') as f:
        writer = csv.writer(f, delimiter=';')
        writer.writerow(('Название', 'Численность', 'Вилка зарплаты', 'Средняя зарплата'))  
        for key, value in report_department.items():
            avg_salary = float('{:.2f}'.format(sum(value[1::])/value[0]))
            row = (key, value[0], (min(value[1::]), max(value[1::])), avg_salary)
            writer.writerow(row)
    
print('Выберите: 1 - получить иерархию команд\n2 - получить сводный отчет\n3 - сохранить сводный отчет в файл')
user_choice = input()

if user_choice == '1':
    print_hierarchy_of_command ()
elif user_choice == '2':
    print_consolidated_report ()
elif user_choice == '3':
    save_consolidated_report()
else:
    print('Вы выбрали что-то другое')
