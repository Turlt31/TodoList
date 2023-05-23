import json
import os

def getlist():
    with open('todos.json', 'r') as f: data = json.load(f)
    return data

def statusChange():
    index = int(input("\t"*6 + "      Index: "))-1
    data = getlist()

    for i in range(len(data['todos'])):
        if i == int(index):
            status = data['todos'][index]['status']
    
    with open('todos.json', 'w') as f:
        status = not status
        data['todos'][index]['status'] = status
        json.dump(data, f)

    main()

def delete():
    index = int(input("\t"*6 + "      Index: "))-1
    data = getlist()

    del data['todos'][index]
    
    with open('todos.json', 'w') as f:
        json.dump(data, f)
    
    main()

def add():
    name = input("\t"*6 + "     Name (Q to quit): ")
    if name == "Q": main()
    status = input("\t"*6 + "     Status (t\\f): ")

    status_map = {"t": True, "f": False}
    status = status_map.get(status, False)

    input("\t"*6 + "     Press ENTER to add ")

    data = getlist()
    data['todos'].append({"name": name, "status": status})
    with open('todos.json', 'w') as f: json.dump(data, f)

    main()

def main():
    os.system('cls')
    data = getlist()
    print()
    print("\t"*5 + "+----+-------------------------------------+--------+")
    print("\t"*5 + "|  # |           Todo List                 | Status |  ")
    print("\t"*5 + "+----+-------------------------------------+--------+")

    if len(data['todos']) != 0: 
        print('\n'.join(["\t"*5 + f"|{i+1:3} | {j['name']:35} | {str(j['status']):6} |" for i, j in enumerate(data['todos'])]))
    else:
        print("\t"*5 + "|    |                                     |        |")
    print("\t"*5 + "+----+-------------------------------------+--------+")
    print()

    print("\t"*5 + "     +-------------------+-----------------+")
    print("\t"*5 + "     | 1. Add todo       |  3. Delete todo |")
    print("\t"*5 + "     | 2. Change status  |  4. Exit        |")
    print("\t"*5 + "     +-------------------+-----------------+\n")

    option = input("\t"*6 + "   # Option: ")
    if option == "1": add()
    elif option == "2": statusChange()
    elif option == "3": delete()
    elif option == "4": os.system('cls'); exit()


main()