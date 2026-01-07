import os

if os.path.exists('sample.txt'):
    with open('sample.txt','r') as f:
        a = f.readlines()
        count = 1
        print('Reading file content:')
        for i in a:
            print(f"Line {count}:{i}")
            count += 1
else:
    print("The file 'sample.txt' was not found.")
            
