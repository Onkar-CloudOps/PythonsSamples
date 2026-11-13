import psutil

def get_system_details():
    
      cpu = psutil.cpu_percent(interval=1)
      ram = psutil.virtual_memory().percent
      disk = psutil.disk_usage("/").percent

      system_info = {
      "CPU" : cpu,
      "RAM" : ram,
      "Disk Usage"  : disk
      }
      #print("System Info", system_info)

      return get_system_details()