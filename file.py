#1
path1='doc1.txt'
path2='doc2.txt'
with open(path1,'r') as file1,open(path2,'r') as file2:
    first=file1.readlines()
    second=file2.readlines()
for first,second in zip(first,second):
    if first!=second:
        print(f'File1:{first.strip()}')
        print(f'File2:{second.strip()}')
if first==second:
        print("Every line match")
#2
path3='doc3.txt'
numberLine=0
numberSymbol=0
numberDigit=0
with open(path1,'r') as dataFile:
    for i in dataFile:
        numberLine+=1
        numberSymbol+=len(i)
        numberDigit+=sum(j.isdigit() for j in i)
with open(path3,'w') as outFile:
    outFile.write(f'Number of symbol:{numberSymbol};\n')
    outFile.write(f'Number of line:{numberLine};\n')
    outFile.write(f'Number of digit:{numberDigit}')
#3
path4='doc4.txt'
with open(path1,'r') as dataFile:
    line=dataFile.readlines()
    line.pop()
    with open(path4,'w') as outFile:
        outFile.writelines(line)
#4
maxLine=0
with open(path1,'r') as file:
    for i in file:
        lineLen=len(i)-i.count('\n')
        maxLine=max(maxLine,lineLen)
print(f'Max line:{maxLine}')
#5
from datetime import datetime
from datetime import date
def addData(diary,newData):
    with open(diary,'a') as file:
        now=datetime.now().strftime("%d.%m.%Y %H:%M:%S")
        file.write(f"Date and time: {now}\n{newData}\n----------------")
def watchData(diary):
    try:
        with open(diary,'r') as file:
            data=file.read()
            if data:
                print(data)
            else:
                print("Write something")
    except FileNotFoundError:
        print("There is no data")
    except Exception:
        print("Can't read!")
diary="diary.txt"
while True:
    print("1.Add diary\n2.Watch diary\n3.Finish")
    choose=int(input("What do you want to do?"))
    if choose==1:
        newData=input("Enter your data:")
        addData(diary,newData)
    elif choose==2:
        watchData(diary)
    elif choose==3:
        open(diary,'w').close()
        print("FINISH!")
        break
