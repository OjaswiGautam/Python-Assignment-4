intial_text = input("Enter text to write to the file:")

with open('output.txt','w') as f:

    f.write(intial_text)
    print("Data successfully written to output.txt.")

additional_text = input("Enter additional text to append:")

with open('output.txt','a') as f:

    f.write("\n")
    f.write(additional_text)
    print("Data successfully appended.")
    

with open('output.txt','r') as f:

    a = f.readlines()
    print("Final content of output.txt:")
    for i in a:
        print(i)
    
    

