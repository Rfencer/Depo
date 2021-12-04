from time import sleep
import timeit


class TrafficLight:

    def __init__(self):
        self.__color = 'Red'
        self.times_dict = {'Red': 7, 'Yellow': 2, 'Green': 3}

    def running(self, time):
        seq_tup = ('Red', 'Yellow', 'Green')
        color_count = len(seq_tup)
        start = stop = timeit.default_timer()

        while (stop - start) < time:
            print(f'Color = {self.__color}')
            sleep(self.times_dict[self.__color])
            cur_color_index = seq_tup.index(self.__color)
            if cur_color_index + 1 == color_count:
                self.__color = seq_tup[0]
            else:
                self.__color = seq_tup[cur_color_index + 1]
            stop = timeit.default_timer()
        else:
            print('Светофор сломался!')


new_tl = TrafficLight()
new_tl.running(30)
