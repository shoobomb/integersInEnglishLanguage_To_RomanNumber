import copy

#Function To Convert From Integer Number To Roman Numerals
def romanConversion(Numb):
    global i
    
    while Numb!=0:
        if Numb >= 1000:
            postdig('m', Numb/1000)
            Numb = Numb - (Numb/1000) * 1000

        elif Numb >= 500:
            if Numb < (500 + 4 * 100):
                postdig('d', Numb/500)
                Numb = Numb - (Numb/500) * 500
            else:
                predig('c','m')
                Numb = Numb - (1000-100)

        elif(Numb >= 100):
            if(Numb < (100 + 3 * 100)):
                postdig('c', Numb/100)
                Numb = Numb - (Numb/100) * 100
            else:
                predig('l','d')
                Numb = Numb - (50-100)

        elif(Numb >= 50):
            if(Numb < (50 + 4 * 10)):
                postdig('l', Numb/50)
                Numb = Numb - (Numb/50) * 50
            else:
                predig('x','c')
                Numb = Numb - (100-10)
        elif(Numb >= 10):
            if(Numb < (10 + 3 * 10)):
                postdig('x', Numb/10)
                Numb = Numb - (Numb/10) * 10
            else:
                predig('x','l')
                Numb = Numb - (50-10)
        elif(Numb >= 5):
            if(Numb < (5 + 4 * 1)):
                postdig('v', Numb/5)
                Numb = Numb - (Numb/5) * 5
            else:
                predig('i','X')
                Numb = Numb - (10-1)
        elif(Numb >= 1):
            if(Numb < 4):
                postdig('i', Numb/1)
                Numb = Numb - (Numb/1) * 1

            else:
                predig('i','v')
                Numb = Numb - (5-1)

    
    print "Roman number is:"
    for j in xrange(i):
        #print romanval[j],
        fileout.append(romanval[j])
    myString = "".join(fileout)
    print myString
    outputFile.write(myString+'\n')
    return 0

#Function to compute for predigits
def predig(num1, num2):
    global i
    romanval.append(num1)
    i+=1
    romanval.append(num2)
    i+=1

#Function to compute for postdigits
def postdig(c,n):
    global i
    for j in xrange(n):
        romanval.append(c)
        i+=1

#Function To Transalte String
def translate_str(Number):
    value=0
    String=""
    String=copy.copy(Number)
    print String
    Ptr = 0
    Ptr = Number.find(" Hundred")
    print Ptr
    if Ptr!=-1:
        n = 0
        Temp = ""
        n = Ptr
        Temp = Number[:n]
        value = 100*get_numeric_value(Temp)
        String=""
        String=Number[(n+9):len(Number)]
    print String
    Atr=""
    l1 = String.split()
    print l1
    if(len(l1)>=1):
        Atr = l1[0]
        print Atr
    

    value+=get_numeric_value(Atr)
    print "Value",value

    Atr = ""

    if(len(l1)>=2):
        Atr=l1[1]
        
    if(Atr is not None):
        value+=get_numeric_value(Atr)
        
    return value

#Function to get the numeric value from English String 
def get_numeric_value(Number):
    value = 0
    if(Number.find("Thousand")==0):
        value=1000
    elif(Number.find("Hundred")==0):
        value=100
    elif(Number.find("Ninety")==0):
        value=90
    elif(Number.find("Eighty")==0):
        value=80
    elif(Number.find("Seventy")==0):
        value=70
    elif(Number.find("Sixty")==0):
        value=60
    elif(Number.find("Fifty")==0):
        value=50
    elif(Number.find("Fourty")==0):
        value=40
    elif(Number.find("Thirty")==0):
        value=30
    elif(Number.find("Twenty")==0):
        value=20
    elif(Number.find("Nineteen")==0):
        value=19
    elif(Number.find("Eighteen")==0):
        value=18
    elif(Number.find("Seventeen")==0):
        value=17
    elif(Number.find("Sixteen")==0):
        value=16
    elif(Number.find("Fifteen")==0):
        value=15
    elif(Number.find("Fourteen")==0):
        value=14
    elif(Number.find("Thirteen")==0):
        value=13
    elif(Number.find("Twelve")==0):
        value=12
    elif(Number.find("Eleven")==0):
        value=11
    elif(Number.find("Ten")==0):
        value=10
    elif(Number.find("Nine")==0):
        value=9
    elif(Number.find("Eight")==0):
        value=8
    elif(Number.find("Seven")==0):
        value=7
    elif(Number.find("Six")==0):
        value=6
    elif(Number.find("Five")==0):
        value=5
    elif(Number.find("Four")==0):
        value=4
    elif(Number.find("Three")==0):
        value=3
    elif(Number.find("Two")==0):
        value=2
    elif(Number.find("One")==0):
        value=1

    return value



##This is the main driver code##
i=0
romanval=[]
fileout=[]
inputFile = open("Q3.in","r")
outputFile = open("Q3.out","a")
numberOfTestCase = inputFile.readline()


#while(numberOfTestCases-=1):
    
Data = ""
Data = inputFile.readline()   #more lines can be added for checking different input test cases from input file
Data = inputFile.readline()
Data = inputFile.readline()


Data.rsplit('\n')

print Data

if Data is None:
    print "Error"    

number=0
Ptr=0

Ptr=Data.find(" Thousand")
print Ptr
if(Ptr!=-1):
    Temp = ""
    n=Ptr
    Temp = Data[:n]
    number += 1000*translate_str(Temp)
    Temp = None

    Temp=Data[(n+10):len(Data)]

    Data=""
    Data=copy.copy(Temp)

number+=translate_str(Data)
print number
romanConversion(number)




        
    
        
        
        

