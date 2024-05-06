import os
import threading
# print('process id',os.getpid())

# def foo():
#     print('thread id',threading.get_native_id())
#     print('process id', os.getpid())
    
# if __name__ =='__main__':
#     print('process id',os.getpid())
#     thread1= threading.Thread(target=foo).start()
#     thread2= threading.Thread(target=foo).start()
#     thread3= threading.Thread(target=foo).start()

#실행결과 :
# process id 19788
# thread id 10324
# process id 19788
# thread id 7792
# process id 19788
# thread id 28180
# process id 19788
# 3개의 다른 스레드가 1개의 프로세스를 공유 중.

import threading
import os
 
def foo():
    print('This is foo')
 
def bar():
    print('This is bar')
  
def baz():
    print('This is baz')
 
if __name__ == '__main__':
    thread1 = threading.Thread(target=foo).start()
    thread2 = threading.Thread(target=bar).start()
    thread3 = threading.Thread(target=baz).start()