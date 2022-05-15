def SaveContactBook(book):
    try:
        file = open('contactbook.txt', 'w')

        for name in book:
            #print("key:", name, "Value:", book[name])
            file.write("{0};{1};{2}\n".format(name, book[name]["tel"], book[name]["email"]))

        print("\t >>> Contact file saved successfully!")
        file.close()
    except FileNotFoundError as err:
        print('Erro : ', err)
    except Exception as e:
        print(e)

def ReadContactBook():
    BOOK = {}
    try:
        file = open('contactbook.txt', 'r')
        for line in file.readlines():
            info = line.split(';')
            BOOK[info[0]] = {
                "tel" : info[1].replace('\r','').replace('\n', ''),
                "email" : info[2].replace('\r','').replace('\n', ''),
            }
        
        print("\t >>> Contact file read successfully!")
        return BOOK
    except FileNotFoundError as err:
        print('\t >>> Not found contact book file\n')
    except Exception as e:
        pass
