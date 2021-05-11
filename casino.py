
import socket
import random
import threading
import time


deck=list(range(1,53,1))
cards=random.sample(deck, 9)

host = 'localhost'
port = 5000

server_socket = socket.socket()

server_socket.bind((host, port))
server_socket.listen(33)
conn1, address1 = server_socket.accept()
conn2, address2 = server_socket.accept()
conn3, address3 = server_socket.accept() 
print("Connection from: " + str(address1))
print("Connection from: " + str(address2))
print("Connection from: " + str(address3))


def p1():
    conn1.send(str(d1[0]).encode()) 
    conn2.send(str(d2[0]).encode())
    conn3.send(str(d3[0]).encode())

def p2():    
    conn1.send(str(d1[1]).encode()) 
    conn2.send(str(d2[1]).encode())
    conn3.send(str(d3[1]).encode())

def p3():
    conn1.send(str(d1[2]).encode())
    conn2.send(str(d2[2]).encode())
    conn3.send(str(d3[2]).encode())
    
def p4():
    data1 = conn1.recv(1024).decode()
    data2 = conn2.recv(1024).decode()
    data3 = conn3.recv(1024).decode()
    maxdeck[0]=int(data1)
    maxdeck[1]=int(data2)
    maxdeck[2]=int(data3)

def p6():
    maxa=max(maxdeck[0],maxdeck[1],maxdeck[2])
    print('Winner(s) :')
    i=0
    while i<3:
        if maxdeck[i]==maxa:
            result[i]+=1
            print(i+1)
        i+=1
    print()



def p11():
    conn1.send(str(d1[0]).encode()) 
    conn2.send(str(d2[0]).encode())
    conn3.send(str(d3[0]).encode())

def p21():    
    conn1.send(str(d1[1]).encode()) 
    conn2.send(str(d2[1]).encode())
    conn3.send(str(d3[1]).encode())

def p31():
    conn1.send(str(d1[2]).encode())
    conn2.send(str(d2[2]).encode())
    conn3.send(str(d3[2]).encode())
    
def p41():
    data1 = conn1.recv(1024).decode()
    data2 = conn2.recv(1024).decode()
    data3 = conn3.recv(1024).decode()
    maxdeck[0]=int(data1)
    maxdeck[1]=int(data2)
    maxdeck[2]=int(data3)

def p61():
    maxa=max(maxdeck[0],maxdeck[1],maxdeck[2])
    print('Winner(s) :')
    i=0
    while i<3:
        if maxdeck[i]==maxa:
            result[i]+=1
            print(i+1)
        i+=1
    print()




def p12():
    conn1.send(str(d1[0]).encode()) 
    conn2.send(str(d2[0]).encode())
    conn3.send(str(d3[0]).encode())

def p22():    
    conn1.send(str(d1[1]).encode()) 
    conn2.send(str(d2[1]).encode())
    conn3.send(str(d3[1]).encode())

def p32():
    conn1.send(str(d1[2]).encode())
    conn2.send(str(d2[2]).encode())
    conn3.send(str(d3[2]).encode())
    
def p42():
    data1 = conn1.recv(1024).decode()
    data2 = conn2.recv(1024).decode()
    data3 = conn3.recv(1024).decode()
    maxdeck[0]=int(data1)
    maxdeck[1]=int(data2)
    maxdeck[2]=int(data3)

def p62():
    maxa=max(maxdeck[0],maxdeck[1],maxdeck[2])
    print('Winner(s) :')
    i=0
    while i<3:
        if maxdeck[i]==maxa:
            result[i]+=1
            print(i+1)
        i+=1
    print()



def p13():
    conn1.send(str(d1[0]).encode()) 
    conn2.send(str(d2[0]).encode())
    conn3.send(str(d3[0]).encode())

def p23(): 
    conn1.send(str(d1[1]).encode()) 
    conn2.send(str(d2[1]).encode())
    conn3.send(str(d3[1]).encode())

def p33():
    conn1.send(str(d1[2]).encode())
    conn2.send(str(d2[2]).encode())
    conn3.send(str(d3[2]).encode())

def p43():
    data1 = conn1.recv(1024).decode()
    data2 = conn2.recv(1024).decode()
    data3 = conn3.recv(1024).decode()
    maxdeck[0]=int(data1)
    maxdeck[1]=int(data2)
    maxdeck[2]=int(data3)

def p63():
    maxa=max(maxdeck[0],maxdeck[1],maxdeck[2])
    print('Winner(s) :')
    i=0
    while i<3:
        if maxdeck[i]==maxa:
            result[i]+=1
            print(i+1)
        i+=1
    print()
    time.sleep(2)
    print('The final scores are as follows :')
    print(result)


def p111():
    conn1.send(str(result[0]).encode()) 
    conn2.send(str(result[0]).encode())
    conn3.send(str(result[0]).encode())

def p112():
    conn1.send(str(result[1]).encode()) 
    conn2.send(str(result[1]).encode())
    conn3.send(str(result[1]).encode())

def p113():
    conn1.send(str(result[2]).encode()) 
    conn2.send(str(result[2]).encode())
    conn3.send(str(result[2]).encode())


def p5():
    conn1.close()
    conn2.close()
    conn3.close()



if __name__ == '__main__':
    
    t1 = threading.Thread(target=p1)
    t2 = threading.Thread(target=p2)
    t3 = threading.Thread(target=p3)
    t4 = threading.Thread(target=p4)
    t5 = threading.Thread(target=p5)
    t6 = threading.Thread(target=p6)

    
    t11 = threading.Thread(target=p11)
    t21 = threading.Thread(target=p21)
    t31 = threading.Thread(target=p31)
    t41 = threading.Thread(target=p41)
    t61 = threading.Thread(target=p61)

    
    t12 = threading.Thread(target=p12)
    t22 = threading.Thread(target=p22)
    t32 = threading.Thread(target=p32)
    t42 = threading.Thread(target=p42)
    t62 = threading.Thread(target=p62)

    
    t13 = threading.Thread(target=p13)
    t23 = threading.Thread(target=p23)
    t33 = threading.Thread(target=p33)
    t43 = threading.Thread(target=p43)
    t63 = threading.Thread(target=p63)


    t111 = threading.Thread(target=p111)
    t112 = threading.Thread(target=p112)
    t113 = threading.Thread(target=p113)


    deck=list(range(1,53,1))
    cards=random.sample(deck, 9)
    print()
    print('Round 1 :')
    time.sleep(1)
    print('Sending cards to each player')
    time.sleep(1)
    print('Receiving max card for each player')

    d1=[cards[0],cards[1],cards[2]]
    d2=[cards[3],cards[4],cards[5]]
    d3=[cards[6],cards[7],cards[8]]
    maxdeck=[0,0,0]
    result=[0,0,0]


    
        
    t1.start()
        
    t2.start()
        
    t3.start()

    t3.join()
        
    t1.join()
       
    t2.join()

    time.sleep(1)   

    t4.start()
    t4.join()

    t6.start()
    t6.join()

    time.sleep(2)

    cards=random.sample(deck, 9)
    print()
    print('Round 2 :')
    time.sleep(1)
    print('Sending cards to each player')
    time.sleep(1)
    print('Receiving max card for each player')
    d1=[cards[0],cards[1],cards[2]]
    d2=[cards[3],cards[4],cards[5]]
    d3=[cards[6],cards[7],cards[8]]


   
        
    t11.start()
        
    t21.start()
        
    t31.start()

    t31.join()
        
    t11.join()
        
    t21.join()

    time.sleep(1)
        

    t41.start()
    t41.join()

    t61.start()
    t61.join()

    time.sleep(2)

    cards=random.sample(deck, 9)
    print()
    print('Round 3 :')
    time.sleep(1)
    print('Sending cards to each player')
    time.sleep(1)
    print('Receiving max card for each player')
    d1=[cards[0],cards[1],cards[2]]
    d2=[cards[3],cards[4],cards[5]]
    d3=[cards[6],cards[7],cards[8]]


    
        
    t12.start()
        
    t22.start()
        
    t32.start()

    t32.join()
        
    t12.join()
        
    t22.join()

    time.sleep(1)
        

    t42.start()
    t42.join()

    t62.start()
    t62.join()

    time.sleep(2)

    cards=random.sample(deck, 9)
    print()
    print('Round 4 :')
    time.sleep(1)
    print('Sending cards to each player')
    time.sleep(1)
    print('Receiving max card for each player')
    d1=[cards[0],cards[1],cards[2]]
    d2=[cards[3],cards[4],cards[5]]
    d3=[cards[6],cards[7],cards[8]]

    
       
    t13.start()
        
    t23.start()
        
    t33.start()

    t33.join()
        
    t13.join()
        
    t23.join()

    time.sleep(1)
        

    t43.start()
    t43.join()

    t63.start()
    t63.join()

    time.sleep(2)

    t111.start()
    t112.start()
    t113.start()
    t111.join()
    t112.join()
    t113.join()


    print()
    print()


    t5.start()
    t5.join()
