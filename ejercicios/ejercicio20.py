# from datetime import timedelta, datetime

# def arrival_time(destination, hours=51):
#     now = datetime.now()
#     arrival = now + timedelta(hours=hours)
#     return arrival.strftime(f"{destination} Arrival: %A %H:%M")


def variable_length(*args):
    print(args)
    
variable_length()
()
variable_length("one", "two")
('one', 'two')
variable_length(None)
(None,)



 
def sequence_time(*args):
    total_minutes = sum(args)
    if total_minutes < 60:
        return f"Total time to launch is {total_minutes} minutes"
    else:
        return f"Total time to launch is {total_minutes/60} hours"
    
sequence_time(4, 14, 18)


def variable_length(**kwargs):
    print(kwargs)

variable_length(tanks=1, day="Wednesday", pilots=3)
{'tanks': 1, 'day': 'Wednesday', 'pilots': 3}