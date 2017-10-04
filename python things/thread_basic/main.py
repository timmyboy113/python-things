import random
import threading
import time

'''
Class inheriting from the higher-level threading interface 
'''
class GhibliMovieChooserThread(threading.Thread):
    # movies to choose
    ghibliMovies = ['Whisper of the Heart', 'Princess Mononoke', 'Spirited Away']
    
    # defining the running count and interval between each of them
    def __init__(self, count, interval):
        threading.Thread.__init__(self)
        self._count = count
        self._interval = interval
    
    # code executed when the Thread is started
    def run(self):
        i = 0
        while i < count:
            # gets an integer index from 0 to 2 to choose a Ghibli movie randomly 
            randomIndex = random.randint(0, len(self.ghibliMovies) - 1)
            print('Let\'s see which movie I choose... Oh! It will be: %s' % self.ghibliMovies[randomIndex])
            # waits for the interval defined in seconds
            time.sleep(self._interval)
            i = i + 1

if __name__ == '__main__':
    count = 10
    interval = 1
    print('Ghibli Movie Chooser, give me %d Ghibli Movies, one each %d seconds!' % (count, interval))
    GhibliMovieChooserThread(count, interval).start()