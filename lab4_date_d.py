from datetime import datetime
date1=datetime.strptime('2019-05-02 08:00:00', '%Y-%m-%d %H:%M:%S')
dt=datetime.now()-date1
dt=dt.days*24*3600+dt.seconds
print(dt, "seconds")
