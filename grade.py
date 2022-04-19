'''
grade.py

This program allows user to load marks information from a file, calculate overall mark, and display grade information

created on march 25, 2022

@author: Young Kai Lam, Hugo 57170546
'''

from Student import Student
from Student121 import Student121
import fileinput
import matplotlib.pyplot as plt
import sys
  
data = [] # list of Student121 objects

def bubblesort(seq):
    '''
    buublesort is to sort record by students name
    '''

    for i in range(len(seq)-1):
        for j in range(len(seq)-1,i,-1):
            if seq[j-1].getName() > seq[j].getName():
                seq[j-1], seq[j] = seq[j], seq[j-1]
    
    return seq
 
def fileDataDisplaying(datafile):
    '''
    fileDataDisplaying is to list out all the data existed inside the .dat file
    '''
    for line in fileinput.input(datafile):
        sys.stdout.write(line)
        sys.stdout.flush()
        
    sys.stdout.write('\n')
    sys.stdout.flush()

def dataReading(datafile):
    '''
    dataReading() to read in student mark data and store in a list, Error will be told to user once invalid data is inside the .dat file
    '''
    fileIn = open(datafile, 'r') # open inputfile using paramepasster datafile

    lines = fileIn.read().splitlines() # read in all transaction lines
    
    if len(lines) == 0: 
        raise Exception ('Empty input file only') #show error when the datafile inputed contain no valid record
    
    for line in lines:
        try:
            studentRec = line.split('_') # convert line to record
            
            i = 0
            while i < Student.numStudent and data[i].getStudID() != studentRec[0]:
                i += 1
                
            if i < Student.numStudent:
                raise ValueError('Repeating student:') # show error when there are two same records inside the datafile
            else:
                data.append(Student121(line)) # append each record to list of student data
        except ValueError as valueError:
            print(str(valueError)+line,file=sys.stderr,flush=True)
              
    
def printingAllValidData():
    '''
    printingAllValidData() to print valid student mark data 
    '''
    #formatting the template
    
    print('%-10s%-15s%10s%10s%10s%10s'%('Stud ID','Name','CW1 mark', 'Test mark',
                               'CW2 mark','Exam mark'))
    print('='*65)

    # loop to print out each components
    for e in data:
        print(e)

def markAdjustment():
    '''
    markAdjustment() allow user to manually change inputted datafile's record
    '''
    try:
        studentID = input("studentID: ") # user are required to input student's id in order to change the record
        studentName = input("studentName: ")
        CW1mark = float(input("CW1mark: ")) # user can input number to change record's CW1mark
        testMark = float(input("testMark: ")) # user can input number to change record's testmark
        CW2mark = float(input("CW2mark: ")) # user can input number to change record's CW2mark
        examMark = float(input("examMark: "))  # user can input number to change record's exammark
        
        i = 0
        while i < Student.numStudent and data[i].getStudID() != studentID:
            i  += 1

        if i == Student.numStudent:
            raise Exception ('Invalid student ID') #if user entered a student number didn't exist in datafile, an error message will be shown
        
        data[i].setIAsgmt(CW1mark) # adjusting record's CW1mark
        data[i].setTest(testMark) # adjusting record's testmark
        data[i].setGAsgmt(CW2mark) # adjusting record's CW2mark
        data[i].setExam(examMark) # adjusting record's exam1mark
        
        #formatting the template
        print('%-10s%-15s%10s%10s%10s%10s'%('Stud ID','Name','CW1 mark', 'Test mark',
                               'CW2 mark','Exam mark'))
        print('='*65)

        # loop to print out each components
        for e in data:
            print(e)
           

    except Exception as exception:
        sys.stderr.write(str(exception)+'\n')
   
def overallMarkOfStudents():
    '''
    overallMarkOfStudents() to print student mark with overall result  
    '''
    #formatting the template
    print('%-10s%-15s%10s%10s%10s%10s%10s%10s'%('Stud ID','Name','CW1 mark', 'Test mark',
                               'CW2 mark','Exam mark','CW mark','Overall'))
    print('='*85)

    # loop to print out each components
    for e in bubblesort(data):
        print("%65s%10.2f%10.2f"%(e,e.getCoursework(),e.overall()))

def failedStudent():
    '''
    failedStudent() to print student mark with overall result < 40  
    '''
    #formatting the template
    print('%-10s%-15s%10s%10s%10s%10s%10s%10s'%('Stud ID','Name','CW1 mark', 'Test mark',
                               'CW2 mark','Exam mark','CW mark','Overall'))
    print('='*85)

    # loop to print out each components
    for e in bubblesort(data):
        if e.overall() < 40:
            print("%65s%10.2f%10.2f"%(e,e.getCoursework(),e.overall()))   
  
def grapghRepresentationOfStudentGrade():  
    '''
    grapghRepresentationOfStudentGrade is to produce a chart and sort student by their grade
    '''

    fig = plt.figure(figsize=(10,8))    # width x height in inches
    ax1 = fig.add_subplot(111)     
    gradeFeq = {'A':0,'B':0,'C':0,'D':0,'F':0}
    
    #sorting grade according to record's mark
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
       4 to print all students overall mark 
       5 to print all students whose mark less than 40
       6 to plot distribution of grade
       Q to end \n"""
    
    while True:
        sys.stderr.flush()    
        sys.stdout.write (instructions)        
        choice = input( "Enter 1 to 6 " ) 
        sys.stdout.flush()
        
        if choice == "1":
            fileDataDisplaying(sys.argv[1])
        elif choice == "2":
            printingAllValidData()          
        elif choice == "3":
            markAdjustment()
        elif choice == "4":
            overallMarkOfStudents()
        elif choice == "5":
            failedStudent()
        elif choice == "6":
            grapghRepresentationOfStudentGrade()
        elif choice == "Q":
            break
        else:
            sys.stderr.write('Please input "1", "2", "3", "4", "5", "6" or "Q" \n')

    print ("End Grade Processing App")

if __name__ == "__main__":
    try:
        
        fileDataDisplaying(sys.argv[1])
        dataReading(sys.argv[1])
        main()
    
    except IndexError as error:
        sys.stderr.write('Type \"python grade.py filename\" to run program\n')
    except Exception as error:
        sys.stderr.write(str(error)+'\n')