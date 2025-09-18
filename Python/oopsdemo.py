

with open("practice.txt","w") as f:
    f.write("Hi this is reeja \n iam learning python file handling")
    f.write("using java.\ni like programing in java")

with open("practice.txt","r") as f:
    data = f.read()

new_data = data.replace("java","python")
print(new_data)

with open("practice.txt","w") as f:
    f.write(new_data)

with open("practice.txt","r") as f:
    data = f.read()
    word = "learning"
    if(data.find(word) != -1):
        print("found")
    else:
        print("not found")

    with open("practice.txt","r") as f:
        lines = f.readlines()
        word = "learning"
        data = True
        line_no = 1
        while data:
            data = f.readline()
            if data.find(word) != -1:
                print(f"found in line {line_no}")
            line_no += 1
        else :
            print(-1)
            
        f.close()
f.close()   



