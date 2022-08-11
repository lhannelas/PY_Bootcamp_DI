import datetime

string_date = "1/08/2022"

dt = datetime.datetime.strptime(string_date, "%d/%m/%Y")

in_future = dt + datetime.timedelta(days=45, hours=10, minutes=29, seconds=46)

print(in_future.strftime("%d/%m/%y %H:%M:%S"))