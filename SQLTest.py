#encoding:utf-8

import sqlite3

conn = sqlite3.connect('test2.db')

cursor = conn.cursor()

#cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')

#cursor.execute('insert into user (id, name) values (\'2\', \'Michael\')')

#print cursor.rowcount

cursor.execute('select * from user where id=?', '1')
values = cursor.fetchall()

print values
#关闭Cursor
cursor.close()

#提交事务
conn.commit()

#关闭connection
conn.close()