cpu = float(input("Enter CPU usage rate"))

if cpu >= 80:
    print("Send SOS Alert")
elif cpu >= 50 and cpu < 80:
    print("CPU usage is high")
else:
    print("CPU is normal")