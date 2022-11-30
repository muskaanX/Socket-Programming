import socket
import time

IP = '127.0.0.1'
PORT = 9778
ADDR = (IP, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

print(f'Connected to server at {IP}.\n')

def getuseremail(): # Get user email as input and send to server
    useremail = input('Enter your Ashoka email: ')
    client.send(useremail.encode())
    data = client.recv(1024).decode()
    if data == 'Email verified.':
        print(data)
        getuser() # If server provides verification that email is valid, proceed to check if user is already registered
    else:
        print(data)
        getuseremail() # If server says that email is invalid, ask for email again


def getuser(): # Check if user is already registered
    data = client.recv(1024).decode()
    if data == 'UserOK':
        getpassword() # If user is registered, proceed to request password from user
    else:
        print('User does not exist. Creating new user.')
        createpassword() # If user is not registered, proceed to create new user


def getpassword(): # Get password from user and send to server
    password = input('Enter your password: ')
    client.send(password.encode())
    data = client.recv(1024).decode()
    if data == 'Password verified.': # If server provides verification that password is correct, proceed to main menu
        print('Password verified.')
        pass # Next func
    else: # If server says that password is incorrect, ask for password again
        print('Password not verified.')
        getpassword()

def createpassword(): # Ask user to set a password if user is not registered
    password = input('Enter a password: ')
    client.send(password.encode())
    data = client.recv(1024).decode()
    print(data)

def service1(): # Service 1
    coursecode = input('Enter Course Code: ')
    client.send(coursecode.encode())
    response = client.recv(1024).decode()
    if response == 'Course not found.':
        print(f'{response} Please ensure you are entering the course code in the following format: CS1101.')
        service1() # If server says that course is not found, ask for course code again
    else:
        print(f'--------------------------------\nCourse: {response}--------------------------------')
        choicefunc() # If server says that course is found and returns results, proceed to main menu

def service2(): # Service 2
    semester = input('Enter Semester: ')
    client.send(semester.encode())
    coursedata = client.recv(2048).decode()
    print(coursedata)
    if coursedata == 'Invalid input. Please try again.':
        service2() # If server says that semester is invalid, ask for semester again
    else:
        choicefunc() # If server says that semester is valid and returns results, proceed to main menu
    
    '''
    if response == 'Semester not found.':
        print(f'{response} Please ensure you are entering the semester in the following format: Monsoon, 2022.')
        service2()
    else:
        print(f'Semester: {semester}\nCourses: \n{response}')
        choicefunc()
    '''

def choicefunc(): # Main menu input function
    msg = client.recv(1024).decode()
    print(msg)
    choice = input('Enter your choice: ')
    client.send(choice.encode())
    response = client.recv(1024).decode()
    if response == 'choice1':
        print('Service 1')
        service1()
    elif response == 'choice2':
        print('Service 2')
        service2()
    elif response == 'choice3':
        client.close()
    else:
        print(response)
        choicefunc()

welcomemsg = client.recv(1024).decode()
print(welcomemsg)

getuseremail()
choicefunc()