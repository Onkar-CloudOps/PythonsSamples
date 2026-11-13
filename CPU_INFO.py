import psutil

threashold = float(input("Please enter threashold: "))
for i in range(5):
   if psutil.cpu_percent(interval=1) > threashold:
       #print(psutil.cpu_times_percent)
       print("cpu is unhealthy")
   else :
       #print(psutil.cpu_percent)
       print("cpu is healthy")