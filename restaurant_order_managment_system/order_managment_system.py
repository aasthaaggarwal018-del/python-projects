
order_list=[]
menu={
            'pizza':300,
            'burger':150,
            'pasta':200,
            'noddles':250,
            'cold drinks':50,
            'milkshakes':70
        }

print ('--welcome to our restaurant. we hope you like our services and food---' )

while True :



    print('\n1. show menu \n2. add order \n3. view orders \n4.total bill amount' \
    '\n5. exit \n')

    choice = int(input('entre your choice here :'))

    if choice==1:
        
        print('\n---menu---')
        for item,price in menu.items():
            print(f'{item.capitalize()}:{price}')


    
    elif choice==2:
        item = input('entre your item here:')
        if item in menu:
            quantity=int(input('entre no of quantity of order:'))
            price=menu[item]*quantity

            order={
                'item':item,
                'quantity':quantity,
                'price':price
            }
            order_list.append(order)
            print(f'\nyour total bill is {price}')
            print('\norder added successfully!')
        else:
            print('\nitem not available')


    elif choice==3:
        if len(order_list)==0:
            print('no order yet')
        else:
            count=1
            for i in order_list:
                print(f'item : {i['item']}')
                print(f'quantity : {i['quantity']}')
                print(f'price : {i['price']}')
                count =+1

    elif choice==4:
        total_bill=0
        for i in order_list:
            total_bill=total_bill+i['price']
        print(f'\ntotal bill amount is {total_bill}')

    elif choice==5:
        print('thanks for visit')
        break

    else:
        print('you entred something wrong')