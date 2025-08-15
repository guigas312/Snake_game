import threading 
import sys
import time
import logging
import msvcrt

sem = threading.Semaphore()
SNAKE_DIR = 'u'

'''
sem.acquire()
print(1)
sem.release()
'''
class body ():
    pass
 
class mapa():
    def __init__(self):
        self.matriz = []
        self.len = 10
        for i in range (0,self.len):
            self.matriz.append([])
            for j in range (0,self.len):
                self.matriz[i].append(0)    
    def put_snake(self,pos_a,pos_b): 
        self.matriz[pos_a][pos_b] = 1
    def pop_snake(self,pos_a,pos_b):
        self.matriz[pos_a][pos_b] = 0
    def show_map(self): 
        for i in range (0,self.len):
            print(self.matriz[i])
        print(' ')    

class snake (): 
    def __init__(self):
        self.head = [5,5]
        self.len = 1
        self.dir = 'U'
        self.comand = []
    def det_dir(self):
        sem.acquire()
        self.dir = SNAKE_DIR
        sem.release()
    def move(self,mp = mapa):
        
        if self.dir == 'U':
           self.head[0] -= 1 
           self.head[1] -= 0
        elif self.dir == 'L':
           self.head[0] += 0 
           self.head[1] -= 1
        elif self.dir == 'R':
           self.head[0] -= 0 
           self.head[1] += 1
        elif self.dir == 'D':
           self.head[0] += 1 
           self.head[1] += 0
        pos_a, pos_b = self.head[0] , self.head[1]   
        mp.pop_snake(pos_a,pos_b)
        mp.put_snake(self.head[0],self.head[1])

def get_char(): 
    global tecla
    while True:
        ch = msvcrt.getch()
        if ch in b'\x00':
            continue
        elif ch in (b'w',b's',b'a',b'd'):
            define_direction(ch)
        elif ch == b'p':
            
           break
        elif ch == b'o':
            tecla = 'o'
        else:
           print(f'Key Pressed: {ch}')
           continue

def define_direction(ply_input):
    global SNAKE_DIR
    sem.acquire()
    if ply_input == b'w':
        SNAKE_DIR = 'W'
    elif ply_input == b's':
        SNAKE_DIR = 'S'
    elif ply_input == b'a':
        SNAKE_DIR = 'A'
    elif ply_input == b'd':
        SNAKE_DIR = 'D'
    sem.release()

def start_game(sk = snake,mp = mapa):
    while True:
        mp.show_map()               
        sk.move(mp)
               
if __name__ == "__main__":
    sk = snake()
    mp = mapa()
    mp.put_snake(sk.head[0],sk.head[1])
    
    # Criação de uma instância de Thread
    thread = threading.Thread(target=get_char)
    # Inicia a thread
    thread.start()
    
 
    start_game(sk,mp)
    # Espera pela thread terminar
    thread.join()
    print("Thread principal finalizada")
    
    
    '''
    mp.pop_snake(pos_a)
    mp.put_snake(sk)
    mp.show_map()
    sk.dir = 'R'
    pos_a = sk.move()
    mp.pop_snake(pos_a)
    mp.put_snake(sk)
    mp.show_map()
    sk.dir = 'R'
    pos_a = sk.move()
    mp.pop_snake(pos_a)
    mp.put_snake(sk)
    mp.show_map()
    sk.dir = 'D'
    pos_a = sk.move()
    mp.pop_snake(pos_a)
    mp.put_snake(sk)
    mp.show_map()
    '''