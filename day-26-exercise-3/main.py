with open('file1.txt', mode='r') as file1:
    with open('file2.txt', mode='r') as file2:
        file1Arr = [item.replace('\n', '') for item in file1.readlines()]
        file2Arr = [item.replace('\n', '') for item in file2.readlines()]
        result = [int(item) for item in file1Arr if item in file1Arr and item in file2Arr]
        print(result)


