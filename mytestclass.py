








class MyClass:
      number = 0
      name = 'noname'


def main():
    me = MyClass()
    me.number = 1337
    me.name = 'name'

    friend = MyClass()
    friend.number = 3
    friend.name = 'friend'


    empty = MyClass()



    print('name: '+me.name+ ', favorite Number: '+ str(me.number))
    print('name: '+friend.name +', favorite number: '+ str(friend.number))
    print('name: '+empty.name+', favorite number: '+str(empty.number))



if __name__ == '__main__':
    main()
    
