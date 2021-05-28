# Task 3

# TV controller
# Create a simple prototype of a TV controller in Python.It’ll use
# the following commands:
# first_channel() - turns on the first channel from the list.
# last_channel() - turns on the last channel from the list.
# turn_channel(N) - turns on the N channel. Pay attention that the channel numbers start from 1, not from 0.
# next_channel() - turns on the next channel. If the current channel is the last one, turns on the first channel.
# previous_channel() - turns on the previous channel.
# If the current channel is the first one, turns on the last channel.
# current_channel() - returns the name of the current channel.
# is_exist(N/'name') - gets 1 argument - the number N or the string 'name' and returns "Yes",
# if the channel N or 'name' exists in the list, or "No" - in the other case.
# The default channel turned on before all commands is №1.
# Your task is to create the TVController class and methods described above.

# CHANNELS = ["BBC", "Discovery", "TV1000"]

# class TVController:

# pass

# controller = TVController(CHANNELS)
# controller.first_channel() == "BBC"
# controller.last_channel() == "TV1000"
# controller.turn_channel(1) == "BBC"
# controller.next_channel() == "Discovery"
# controller.previous_channel() == "BBC"
# controller.current_channel() == "BBC"
# controller.is_exist(4) == "No"
# controller.is_exist("BBC") == "Yes"


class TVController:
    def __init__(self, channels):
        self._channels = channels
        self._current_channel = 0

    def first_channel(self):
        first = self._channels[0]
        return first

    def last_channel(self):
        last = self._channels[-1]
        return last

    def turn_channel(self, n):
        if n <= len(self._channels):
            turn = self._channels[n - 1]
            return turn
        else:
            wrong_data = 'No such channel in a list '
            return wrong_data

    def _previous_next(self, num):
        self._current_channel = (self._current_channel + num) % len(self._channels)
        return self.current_channel()

    def next_channel(self):
        return self._previous_next(1)

    def previous_channel(self):
        return self._previous_next(-1)

    def is_exist(self, n):
        if n in self._channels or n <= len(self._channels):
            return 'Yes'
        else:
            return 'No'

    def current_channel(self):
        return self._channels[self._current_channel]


if __name__ == '__main__':

    CHANNELS = ["BBC", "Discovery", "TV1000"]
    controller = TVController(CHANNELS)

    print(controller.first_channel())  # == "BBC"
    print(controller.last_channel())  # == "TV1000"
    print(controller.turn_channel(2))  # == "BBC"

    print(controller.next_channel())  # == "Discovery"
    print(controller.next_channel())
    print(controller.next_channel())

    print(controller.previous_channel())  # "BBC"
    print(controller.previous_channel())
    print(controller.current_channel())  # == "BBC"
    print(controller.is_exist(4))  # == "No"
    print(controller.is_exist("BBC"))  # == "Yes"
