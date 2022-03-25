'''
gradeV3.py

016/03/2022
'''
from Student import Student
from Student121V2 import Student121
import fileinput
import sys
  
data = [] # list of Student121 objects

def bubblesort(seq):

    for i in range(len(seq)-1):
        for j in range(len(seq)-1,i,-1):
            if seq[j-1].getName() > seq[j].getName():
                seq[j-1], seq[j] = seq[j], seq[j-1]
    
    return seq
 
def displayFile(datafile):
    for line in fileinput.input(datafile):
        sys.stdout.write(line)

def readData(datafile):
    '''
    readData() to read in student mark data and store in a list
    '''
    fileIn = open(datafile, 'r') # open inputfile using paramepasster datafile

    lines = fileIn.read().splitlines() # read in all transaction lines

    for line in lines:
        data.append(Student121(line)) # append each record to list of student data
            
    if len(lines) == 0:
        raise Exception ('Empty input file')  
    
def menuItem2():
    '''
    menuItem2() to print valid student mark data 
    '''
    print('%-10s%-15s%10s%10s%10s%10s'%('Stud ID','Name','CW1 mark', 'Test mark',
                               'CW2 mark','Exam mark'))
    print('='*65)

    # loop to print out each components
    for e in data:
        print(e)

def menuItem3():
    try:
        studentID = input("studentID: ")
        studentName = input("studentName: ")
        testMark = float(input("testMark: "))
        CW1mark = float(input("CW1mark: "))
        CW2mark = float(input("CW2mark: "))
        examMark = float(input("examMark: ")) 
        
        i = 0
        while i < Student.numStudent and data[i].getStudID() != studentID:
            i  += 1

        if i == Student.numStudent:
            raise Exception ('Invalid student ID')
        
        data[i].setTest(testMark)
        data[i].setIAsgmt(CW1mark)
        data[i].setGAsgmt(CW2mark)
        data[i].setExam(examMark)
        
        
        menuItem4()   

    except Exception as exception:
        sys.stderr.write(str(exception)+'\n')
   
def menuItem4():
    '''
    menuItem4() to print student mark with overall result  
    '''
    print('%-10s%-15s%10s%10s%10s%10s%10s%10s'%('Stud ID','Name','CW1 mark', 'Test mark',
                               'CW2 mark','Exam mark','CW mark','Overall'))
    print('='*85)

    # loop to print out each components
    for e in bubblesort(data):
        print("%65s%10.2f%10.2f"%(e,e.getCoursework(),e.overall()))

def menuItem5():
    '''
    menuItem4() to print student mark with overall result < 40  
    '''
    print('%-10s%-15s%10s%10s%10s%10s%10s%10s'%('Stud ID','Name','CW1 mark', 'Test mark',
                               'CW2 mark','Exam mark','CW mark','Overall'))
    print('='*85)

    # loop to print out each components
    for e in bubblesort(data):
        if e.overall() < 40:
            print("%65s%10.2f%10.2f"%(e,e.getCoursework(),e.overall()))   
  
def menuItem6():  

    fig = plt.figure(figsize=(10,8))    # width x height in inches
    ax1 = fig.add_subplot(111)     
    gradeFeq = {'A':0,'B':0,'C':0,'D':0,'F':0}
    
    for e in data:
        if e.overall() < 40:
            gradeFeq['F'] += 1
        elif e.overall() < 50:
            gradeFeq['D'] += 1            
        elif e.overall() < 65:
            gradeFeq['C'] += 1 
        elif e.overall() < 75:
            gradeFeq['B'] += 1   
        else:
            gradeFeq['A'] += 1                          
    
    ax1.bar(['A','B','C','D','F'],
        [gradeFeq['A'],gradeFeq['B'],gradeFeq['C'],gradeFeq['D'],gradeFeq['F']])
    ax1.set_xlabel('Grade')
    ax1.set_ylabel('Student Numbers')
    ax1.set_title('Grade Distribution')
    plt.show()     
                
def main():
    instructions = """\nEnter one of the following:
       1 to print the contents of input data file
       2 to print all valid input data
         3 enter adjustment marks
       4 to print all students overall mark BSc (Hons) Information Technology for Business
       5 to print all students whose mark less than 40
       6 to plot distribution of grade
       Q to end \n"""
    
    while True:
        sys.stderr.flush()    
        sys.stdout.write (instructions)        
        choice = input( "Enter 1 to 6 " ) 
        sys.stdout.flush()
        
        if choice == "1":
            displayFile(sys.argv[1])
        elif choice == "2":
            menuItem2()          
        elif choice == "3":
            menuItem3()
        elif choice == "4":
            menuItem4()
        elif choice == "5":
            menuItem5()
        elif choice == "6":
            menuItem6()
        elif choice == "Q":
            break

    print ("End Grade Processing App")

if __name__ == "__main__":
    try:
        
        displayFile(sys.argv[1])
        readData(sys.argv[1])
        main()
    
    except IndexError as error:
        sys.stderr.write('Type \"python grade.py filename\" to run program\n')