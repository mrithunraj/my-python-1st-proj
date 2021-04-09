import _thread
import time

class mrithun:
    def raj(self,name,a,b):
        print("start:",name)
        for i in range(a,b+1):
            print(i)
            time.sleep(1)
                       
a=mrithun()
b=mrithun()

_thread.start_new_thread(a.raj,('thread1',1,10))
_thread.start_new_thread(b.raj,('thread2',11,20))


from threading import Thread

class mrithun(Thread):
    def __init__(self,a,b):
       Thread .__init__(self)
       self.a=a
       self.b=b

    def raj(self):
        for i in range(self.a,self.b+1):
            print(i)

s=mrithun(11,20)
s.start()
s2=mrithun(45,56)
s2.start()
s2.join()
s1=mrithun(1,10)
s1

           
                 






























