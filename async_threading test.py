import threading
import time



class asyncwrite(threading.Thread):
    def __init__(self, text, out):
        threading.Thread.__init__(self)
        self.text = text
        self.out = out

    def run(self):
        file1 = open(self.out, 'a')
        file1.write(self.text+'\n')
        file1.close()
        time.sleep(2)
        print('wrote data to '+self.out)
def main():
    message = input('enter string to store:  ')
    backthread = asyncwrite(message, 'out.txt')
    backthread.start()
    print('the program can continue')
    print('100 + 400 =', 100+400)


    backthread.join()
    print('thread is complete')

main()
