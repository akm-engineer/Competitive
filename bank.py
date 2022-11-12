import mysql.connector

Mydb = mysql.connector.connect(host='localhost',
                               user='root',
                               password='AsH93095$@&%',
                               database='BANK_MANAGEMENT')


def OpenAcc():
    n = input('Enter the name: ')
    ac = input('enter the account number: ')
    db = input('enter the date of birth: ')
    add = input('enter the address: ')
    cn = int(input('enter the contact number: '))
    ob = int(input('Enter the opening balance: '))
    data1 = (n, ac, db, add, cn, ob)
    data2 = (n, ac, ob)
    sql1 = ('insert into account values (%s,%s,%s,%s,%s,%s)')
    sql2 = ('insert into amount values(%s,%s,%s)')
    x = Mydb.cursor()
    x.execute(sql1, data1)
    x.execute(sql2, data2)
    Mydb.commit()
    print('Data enter Successfully...')
    main()


def depoAmo():
    amount = int(input('Enter the amount you want to deposit :- '))
    ac = input('enter the account number: ')
    a = 'select balance from amount where AccountNO =%s'  #query
    data = (ac, )
    x = Mydb.cursor()
    x.execute(a, data)
    result = x.fetchone()
    t = result[0] + amount
    sql = ('update amount set Balance=%s where AccountNO=%s')#update the amount
    d = (t, ac)
    x.execute(sql, d)
    Mydb.commit()
    main()


def withdrawAmo():
    amount = int(input('Enter the amount to withdraw- '))
    ac = input('enter the account number: ')
    a = 'select balance from amount where AccountNO =%s'
    data = (ac, )
    x = Mydb.cursor()
    x.execute(a, data)
    result = x.fetchone()
    t = result[0] - amount
    sql = ('update amount set balance=%s where AccountNO=%s')
    d = (t, ac)
    x.execute(sql, d)
    Mydb.commit()
    main()


def balEnq():
    ac = input('Enter the account number: ')
    a = 'select * from amount where AccountNO=%s'
    data = (ac, )
    x = Mydb.cursor()
    x.execute(a, data)
    result = x.fetchone()
    print('Balance for account:', ac, ' is ', result[-1])
    main()


def DisCusDetails():
    ac = int(input('ENter the account number: '))
    a = 'select * from account where AccNo=%s'
    data = (ac, )
    x = Mydb.cursor()
    x.execute(a, data)
    result = x.fetchone()
    for i in result:
        print(i)
    main()


def CloseAcc():
    ac = input('ENter the account number: ')
    sql1 = 'delete from amount where AccountNO=%s'
    sql2 = 'delete from account where AccNo=%s'
    data = (ac, )
    x = Mydb.cursor()
    x.execute(sql1, data)
    x.execute(sql2, data)
    Mydb.commit()
    main()


def main():
    print('''          
          1. OPEN NEW ACCOUNT
          2. DEPOSIT AMOUNT
          3. WITHDRAW AMOUNT
          4. BALANCE ENQUIRY
          5. DISPLAY CUSTOMER DETAILS
          6. CLOSE AN ACCOUNT''')
    choice = input('Enter the task you want to perform: ')
    if choice == '1':
        OpenAcc()
    elif choice == '2':
        depoAmo()
    elif choice == '3':
        withdrawAmo()
    elif choice == '4':
        balEnq()
    elif choice == '5':
        DisCusDetails()
    elif choice == '6':
        CloseAcc()
    else:
        print('INVALID!!!')
        main()


main()
