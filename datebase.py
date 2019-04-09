import sqlite3 as sql #подключение библиотеки работы с базой даних

conection= sql.connect('test.sqlite') # подключение к базе даных
q=conection.cursor() #создание курсора

#q.execute('''CREATE TABLE USER (id int auto_increment primary key, name varchar, password varchar)''') #создание таблици в базе
#conection.commit() # применение действий к базе
user_name=input("Ведите имя")
user_paswords=input("Ведите пароль")
q.execute("INSERT INTO user (name,password) VALUES ('%s','%s')"%(user_name,user_paswords)) #передача даних в базу даних
conection.commit()
print("Список пользователей:\n")
q.execute("SELECT * FROM user") #выбираем все даниые с таблици user
row=q.fetchone() #считывание стрички в базе

while row is not None: #цикл для вывода базы даных
    print("Имя:",row[1],"| Пароль",row[2]) #вывод полей где [1] и [2] это номер столбца в базе
    row=q.fetchone() #считывание следующей строки

q.close() #закрытие базы ( обезательно)
conection.close()#закрытие базы ( обезательно)