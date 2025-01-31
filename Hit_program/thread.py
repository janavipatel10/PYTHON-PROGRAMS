from threading import Thread
class a(Thread):
    def run(self):
        for i in range(5):
            print("Hit ")

class b(Thread):
    def run(self):
        for i in range(5):
            print("Sheladiya")
            
t1=a()
t2=b()

t1.start()
t2.start()