### file

file_name = r'info.txt'
log_file = r'log.txt'


def _log_in(mesg):
    with open (log_file,'a') as fh:
        fh.write(mesg)

def log_info(mesg):
    data = f'[Info] : {mesg}'
    _log_in(mesg)


def log_error(mesg):
    data = f'[Error] : {mesg}'
    _log_in(mesg)


def stored_data():
    log_info('Start to enter the information..\n')
    name = input('Enter your name :')
    age = input('Enter your age : ')
    no = input('Enter your phone no :')
    log_info('Information entered\n')
    data = f'{name},{age},{no}\n'
    log_info('Start to enter the data..\n')
    with open (file_name,'a') as fh:
        fh.write(data)

    log_info('Data entered completely..\n')


def user_info():
    no = input('Enter your no :')
    fh = open(file_name)
    for line in fh:
        name,age,pno = line.split(',')
        log_info(f'comparing {no} and {pno}\n')
        if no.strip() == pno.strip():
            print(f'name {name} and age {age}')
            return
    print('Invalid phone no')
    log_error('phone no not found')



stored_data()
user_info()
