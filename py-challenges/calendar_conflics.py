# given a list of calendar events, find all event that conflict
import datetime

class CalendarEvent():
    def __init__(self, start=None, stop=None, title=None):
        self.datetime_start = start
        self.datetime_stop = stop
        self.title = title

    def __str__(self):
        return self.title

class Calendar():
    __events = []
    def add_event(self, event):
        """ Adds the event to the calendar """
        self.__events.append(event)

    def __iter__(self):
        return iter(self.__events)

    def conflicting_meetings(self):
        """ Check for conflicts in the calendar and return them """
        # retunrn a tuple of tuples, each containing the 2 event that conflict
        conflicts = []
        for outer_index, outer_elem in enumerate(self.__events):
            if outer_index < len(self.__events) - 1:
                # no need to scan for the last item, at that point all comparison have happened
                for inner_index, inner_elem in enumerate(self.__events[outer_index+1:]):
                    # compare the 2 events, check if they conflict
                    if (outer_elem.datetime_start <= inner_elem.datetime_stop \
                    and outer_elem.datetime_start >= inner_elem.datetime_start) \
                    or (outer_elem.datetime_stop <= inner_elem.datetime_stop \
                    and outer_elem.datetime_stop >= inner_elem.datetime_start):
                        conflicts.append((outer_elem, inner_elem))

        #return the list of conflicts
        return tuple(conflicts)

# create test calendar
calendar = Calendar()

temaplate = '%b %d %Y %I:%M%p'
test_data= [('Jun 1 2017  1:00PM', 'Jun 1 2017  2:00PM', "Marco"),
            ('Jun 1 2017  1:30PM', 'Jun 1 2017  4:00PM', 'Luigi'),
            ('Jun 1 2017  5:30PM', 'Jun 1 2017  6:00PM', 'Franco'),
            ('Jun 1 2017  3:00PM', 'Jun 1 2017  3:30PM', 'Pippo'),
            ('Jun 1 2017  9:00AM', 'Jun 1 2017  10:00AM', 'Pluto'),
            ('Jun 1 2017  6:00AM', 'Jun 1 2017  7:00AM', 'Anna'),
            ('Jun 1 2017  11:00PM', 'Jun 1 2017  11:30PM', 'Teresa'),
            ('Jun 2 2017  1:00PM', 'Jun 2 2017  3:30PM', 'Gigio'),
            ('Jun 2 2017  3:00PM', 'Jun 2 2017  4:00PM', 'Giorgio'),
            ('Jun 2 2017  4:30PM', 'Jun 2 2017  6:00PM', 'Zappa')]

# create test events and load the calendar
for event in test_data: 
    datatime_start = datetime.datetime.strptime(event[0], temaplate)
    datatime_stop = datetime.datetime.strptime(event[1], temaplate)
    title = event[2]
    event1 = CalendarEvent(datatime_start, datatime_stop, title)
    calendar.add_event(event1)
print("Calendar loaded")

# check for conflicts in this calendar
print("Conflicting meetings:")
cal_conflicts = calendar.conflicting_meetings()
for conflict in cal_conflicts:
    print("{} {}".format(conflict[0], conflict[1]))
