import mysql.connector as mdb


def connect_to_db():
    global conn
    conn = mdb.connect(host="localhost", user="root", password="toor", database="youtube_tutorial")


def create_db():
    cursor = conn.cursor()
    sql = """ create database youtube_tutorial """
    cursor.execute(sql)

def delete_db():
    cursor = conn.cursor()
    sql = """ drop database youtube_tutorial """
    cursor.execute(sql)
    conn.commit()

def delete_value():
    id_ = input("what row to delete?\t")
    cursor = conn.cursor()
    sql = """ delete from profiles where person_id=%s  """
    data = (id_,)
    cursor.execute(sql, data)

    conn.commit()


def show_tables():
    cursor = conn.cursor()
    sql = """ show tables """
    cursor.execute(sql)
    result = cursor.fetchall()

    for r in result:
        print(r)

def show_dbs():
    cursor = conn.cursor()
    sql = """ show databases """
    cursor.execute(sql)
    result = cursor.fetchall()

    for r in result:
        print(r)

def create_table():
    sql =   """ 
                create table profiles (
                    person_id int(11) not null auto_increment,
                    first_name varchar(50) not null, 
                    last_name varchar(50) not null,
                    email varchar(255) not null,
                    home_addr varchar(50) not null,
                    origin varchar(50) not null,
                    primary key (person_id)
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci
            """
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()


def describe_table():
    cursor = conn.cursor()
    table = input("What table to describe ?!\t")
    sql = f""" describe {table} """
    cursor.execute(sql)
    result = cursor.fetchall()
    
    print("**" * 20)
    for r in result:
        print(r)

def insert_data():
    cursor = conn.cursor()
    sql = """ insert into profiles 
                (first_name, last_name, email, home_addr, origin) values 
                ("Ahmed", "Isho", "ishosomething@gmail.com", "Morocco", "Gana")  
          """
    cursor.execute(sql)
    conn.commit()


def get_data():
    cursor = conn.cursor()
    sql = """ select * from profiles  """
    cursor.execute(sql)
    result = cursor.fetchall()
    for r in result:
        print(r)

def main():
    connect_to_db()
    #create_table()
    #delete_db()
    #create_db()
    #show_tables()
    #show_dbs()
    describe_table()
    #insert_data()
    #get_data()
    #delete_value()


if __name__ == "__main__":
    main()
