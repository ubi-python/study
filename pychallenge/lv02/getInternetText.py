def getText():
        with open('mess.txt', 'r') as openfile:
            lines = openfile.readlines()
        return lines