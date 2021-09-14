from random import randint

def step1():
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️')
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()
    
    if options[option]:
        step2_umbrella()
    else:
        step2_no_umbrella()

def step2_umbrella():
    print('Выберите цвет зонтика')
    color = input()
    print (f'Утка-маляр выходит из дома с зонтиком цвета: {color}')
    
def step2_no_umbrella():
    is_rain = randint (0,1)
    if is_rain == 1:
        print('Пошел дождь и утка промокла')
    else:
        print('Утка успешно добралась до паба')

if __name__ == '__main__':
    step1()
