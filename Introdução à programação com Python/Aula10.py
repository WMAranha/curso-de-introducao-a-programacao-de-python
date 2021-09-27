from datetime import date, time, datetime, timedelta

def trabalhano_datetime():
    data_atual = datetime.now()
    print(data_atual)
    print(data_atual.strftime('%d/%m/%Y %H:%M:%S'))
    print(data_atual.strftime('%c'))
    print(data_atual.day)
    tupla = ('Segunda','Terça','Quarta','Quinta','Sexta', 'Sábado','Domingo')
    print(tupla[data_atual.weekday()])
    data_criada = datetime(2018, 6, 20, 15, 30, 20)
    print(data_criada)
    print(data_criada.strftime('%c'))
    dats_string = '01/01/2019 12:20:22'
    data_convertida = datetime.strptime(dats_string, '%d/%m/%Y %H:%M:%S')
    print(data_convertida)
    nova_data = data_convertida - timedelta(days=365, hours=2, minutes=15)
    print(nova_data)

def trabalhando_date ():
    data_atual = date.today()
    dats_atual_str = data_atual.strftime('%d/%m/%Y')
    print(type(data_atual))
    print(dats_atual_str)
    print(type(dats_atual_str))

def trabalhando_time ():
    horario = time(hour=15, minute=18, second=30)
    print(horario)
    horario_str = horario.strftime('%H:%M:%S')
    print(horario_str)
    print(type(horario_str))

if __name__ == '__main__':
    #trabalhando_date()
    #trabalhando_time()
    trabalhano_datetime()
