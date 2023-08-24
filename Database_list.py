import sqlite3 as sql

db = sql.connect("python_sqlite.db")
db_cursor = db.cursor()


print(dir(sql))

data =[{
    "id":1,
    "name":"priyanka"
    "city":"ahmedabad"
}

data1 = {
    "id":2,
    "name":"Aarvee",
    "city":"surat"

}
]

cmd = 'create table users(id int, name varchar(25), city varchar(25));'
for i in data:
    cmd = f'
    '

    
