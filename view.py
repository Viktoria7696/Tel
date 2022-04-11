def search():
    data = []
    with open("Contacts.txt", 'r', encoding='utf-8') as f:
        for line in f:
            data.append([str(x) for x in line.split()])       
    print(data[0])

search()
