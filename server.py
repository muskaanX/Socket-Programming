import socket
import json

IP = '127.0.0.1'
PORT = 9778
ADDR = (IP, PORT)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

print(f'Server is starting at {IP}:{PORT}')
server.listen()
print(f'Server is now listening')

userslist = {} # Dictionary to store user email and password

try: # Try to open the users.json file and load the data into the userslist dictionary
    with open('./users.json', 'r') as fp:
        userslist = json.load(fp)

except: # If the file doesn't exist, create a new file
    print('No users.json file found. Creating new one.')
    with open('./users.json', 'w') as fp:
        json.dump(userslist, fp)

def checkuseremail(): # Check if the user email is of Ashoka Domain
    useremail = conn.recv(1024).decode()
    useremail = useremail.lower()

    if useremail.endswith('@ashoka.edu.in'):
        conn.send('Email verified.'.encode())
        print('Email verified.')
        checkuser(useremail) # If email is of Ashoka Domain, move to check if user is registered
    else:
        conn.send('Invalid email. Please try again with an Ashoka Email address.'.encode())
        checkuseremail() # If email is not of Ashoka Domain, ask for email again


def checkuser(useremail): # Check if the user is already registered
    if useremail in userslist.keys(): 
        conn.send('UserOK'.encode())
        print('Email already registered.')
        checkpassword(useremail) # If user is registered, move to check password
    else:
        conn.send('noUser'.encode())
        print('Email not registered.')
        createuser(useremail) # If user is not registered, move to create password

def checkpassword(useremail): # Check if the password is correct
    password = conn.recv(1024).decode()
    if password == userslist[useremail]: 
        conn.send('Password verified.'.encode())
        print(f'Password verified. {useremail} logged in.')
        pass # Move to next function
    else:
        conn.send('Incorrect password.'.encode())
        checkpassword(useremail) # If password is incorrect, ask for password again

def createuser(useremail): # Create a new user and let the user set a password
    password = conn.recv(1024).decode()
    userslist[useremail] = password # Add the user and password to the userslist dictionary
    with open('./users.json', 'w') as fp:
        json.dump(userslist, fp) # Write the userslist dictionary to the users.json file
    conn.send('User registered.'.encode())
    print(f'New user with email {useremail} registered.')

def choicefunc(): # Ask the user what service they want to use and call the appropriate function
    conn.send('Please choose your service:\n 1. Service 1: Check Pre-requisites for Core CS Courses\n 2. Service 2: View CS Courses Offered in a Semester\n 3) End and Exit'.encode())
    choice = conn.recv(1024).decode()
    choice = str(choice)
    if choice == '1':
        conn.send('choice1'.encode())
        print('Service 1 selected.')
        service1()
    elif choice == '2':
        conn.send('choice2'.encode())
        print('Service 2 selected.')
        service2()
    elif choice == '3':
        conn.send('choice3'.encode())
        print('User exit.')
    else:
        conn.send('Invalid choice. Please try again.'.encode()) # If the user enters an invalid choice, ask for choice again
        #print('Invalid choice.')
        choicefunc()

def service1():
    courseCode = conn.recv(1024).decode()
    courseCode = courseCode.replace('-',"")
    courseCode = str(courseCode).upper() 
    courseCode = courseCode.replace('CS','')
    if (courseCode == '1101'): # Core Course 1
        conn.send('Introduction to Computer Programming\nThe Pre-requisites are:\n 1) Mathematics in 11th and 12th, or\n 2) Foundations of Computer Programming\n'.encode())
        choicefunc()
    elif (courseCode == '1104'): # Core Course 2
        conn.send('Discrete Mathematics\nThe Pre-requisites are: \nNone\n'.encode())
        choicefunc()
    elif (courseCode == '1202'): # Core Course 3
        conn.send('Data Structures\nThe Pre-requisites are:\n 1) Introduction to Computer Programming\n'.encode())
        choicefunc()
    elif (courseCode == '1208'): # Core Course 4
        conn.send('Probability and Statistics\nThe Pre-requisites:\n None\n'.encode())
        choicefunc()
    elif (courseCode == '1216'): # Core Course 5
        conn.send('Computer Organization and Systems\nThe Pre-requisites are:\n 1) Introduction to Computer Programming\n'.encode())
        choicefunc()
    elif (courseCode == '1205'): # Core Course 6
        conn.send('Algorithm Design and Analysis\nThe Pre-requisites are:\n 1) Data Structures\n'.encode())
        choicefunc()
    elif (courseCode == '1217'): # Core Course 7
        conn.send('Operating Systems\nThe Pre-requisites are:\n 1) Computer Organizations and Systems\n'.encode())
        choicefunc()
    elif (courseCode == '1319'): # Core Course 8
        conn.send('Programming Language Design and Implementation\nThe Pre-requisites are:\n 1) Data Structures\n 2) Computer Organizations and Systems\n'.encode())
        choicefunc()
    elif (courseCode == '1340'): # Core Course 9
        conn.send('Computer Networks\nThe Pre-requisites are:\n 1) Introduction to Computer Programming\n 2) Computer Organizations and Systems\n'.encode())
        choicefunc()
    elif (courseCode == '1390'): # Core Course 10
        conn.send('Introduction to Machine Learning\nThe Pre-requisites:\n 1) Introduction to Computer Programming\n 2) Probability and Statistics\n'.encode())
        choicefunc()
    else:
        conn.send('Course not found.'.encode())
        service1() # If the course code is not found, ask for course code again

def service2():
    semester = conn.recv(1024).decode()
    semester = str(semester).lower() 
    semester = semester.replace(',', '') # Remove commas from the semester string
    semester = semester.replace(' ', '') # Remove spaces from the semester string

    if semester == 'spring2022':
        conn.send('--------------------------------\n1) CS-1101: Introduction to Computer Programming\n2) CS-1104: Discrete Mathematics\n3) CS-1205: Algorithm Design and Analysis\n4) CS-1217: Operating Systems\n5) CS-2209: Fuzzy Cartographies\n6) CS-2210: Linear Algebra\n7) CS-2349: Theory of Computation\n8) CS-2361: Blockchain and Cryptocurrencies\n9) CS-2362: Computer Security and Privacy\n10) CS-2376: Data Mining and Warehousing\n11) CS-2378: The New Geography of Information Age\n12) CS-2380: Mathematical Foundations of Data Science\n13) CS-2470: Advanced Topics in Probability\n14) CS-2490: Advanced Machine Learning\n15) CS-4999: Capstone Thesis\n16) CS-IS-2006: Human-Computer Interaction\n17) CS-IS-3023: Data Science: Sports\n18) CS-IS-3024: Data Analytics for Air Quality Assessment\n19) CS-IS-3025: Hardware-based Memory Encryption: Primitives, Modules and Intel SGX\n20) CS-IS-3026: Web Exploitation\n21) CS-IS-3028: Quantitative Portfolio Construction\n22) CS-IS-3029: The Internet and CSAM\n23) CS-IS-3030: Human-AI Assisted Sports Coaching: Computer Vision and Transfer Learning\n24) CS-IS-4012: Data Analytics of Air Quality Assessment\n25) CS-IS-4013: Advanced Algorthmic Economics\n26) CS-IS-4014: MLOps\n27) CS-IS-4015: Itemset Placement in Retail\n28) CS-IS-4016: Topics in Quantum Computation and Quantum Information\n29) CS-IS-4017: Machine Learning for Healthcare\n--------------------------------\n'.encode())
        choicefunc() 
    elif semester == 'monsoon2022':
        conn.send('--------------------------------\n1) CS-1101: Introduction to Computer Programming\n2) CS-1203: Data Structures\n3) CS-1207: Statistics for Economists\n4) CS-1208: Probability and Statistics\n5) CS-1216: Computer Organizations and Systems\n6) CS-1390: Introduction to Machine Learning\n7) CS-1319: Programming Language Design and Implementation\n8) CS-2160: Symbolic Logic\n9) CS-2210: Linear Algebra\n10) CS-2250: Algebra 1\n11) CS-2375: Database Management Systems\n12) CS-2446: Advanced Algorithms\n13) CS-2450: Distributed Network Algorithms\n14) CS-2455: Biostatistics and Bioinformatics\n15) CS-2456: Computational/ Mathematical Biology\n16) CS-2462: Information and Coding Theory\n17) CS-2463: An Overview of Usable Privacy and Security\n18) CS-2464: Fairness of AI\n19) CS-2465: Computing in the Cloud\n20) CS-2466: Machine Learning for Finance\n21) CS-2467: Computer Vision\n22) CS-3032: Computational Systems Medicine at Single Cell Resolution\n23) CS-IS-4020: Reading, Reviewing, and Presenting Scientific Papers\n24) CS-IS-4021: Multimodal Analysis for Content Classification\n25) CS-IS-4022: Quantum Complexity Theory\n26) CS-IS-4023: Building a Mental Wellbeing App\n27) CS-IS-4024: Embedded Systems Firmware Security\n28) CS-IS-4025: Advanced Topics in Cryptography\n29) CS-IS-4026: Rapid Prototyping and Experimentation\n30) CS-IS-5005: Use of Approximate Computing in Federated Learning\n--------------------------------\n'.encode())
        choicefunc()
    else:
        conn.send('Invalid input. Please try again.'.encode())
        service2()
      
while True: # While loop to keep the server running
    conn, addr = server.accept() 
    connection = True
    print(f'================================\nConnected to {addr}')
    while connection: # While loop to keep the connection active, only accepts one connection at a time
        try:
            conn.send('Welcome to the server! Please login to continue.'.encode())
            checkuseremail() 
            choicefunc()

        except: # If the connection is lost, the server will wait for a new connection
            connection = False
            conn.close()
            with open('./users.json', 'w') as fp:
                json.dump(userslist, fp) # Save the updated userslist to the users.json file
            print(f'Connection closed with {addr}.\n================================')
            print(f'Waiting for new connection...')
            break