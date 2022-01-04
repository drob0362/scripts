import datetime

start_time = '08:40'
end_time = '15:00'

time_format = '%H:%M'

try:
    start_time_obj = datetime.datetime.strptime(start_time, time_format)
    end_time_obj = datetime.datetime.strptime(end_time, time_format)

except ValueError:
    print("failed to parse input  :-/")


print("start time {}".format(start_time_obj.time()))
print("end time {}".format(end_time_obj.time()))

worked_hrs = end_time_obj - start_time_obj
print("worked hours = {} ".format(worked_hrs))


