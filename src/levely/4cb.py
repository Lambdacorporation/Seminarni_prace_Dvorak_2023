import paramiko
from concurrent.futures import ThreadPoolExecutor
import subprocess

def run_remote_command(ssh_client, command):
    stdin, stdout, stderr = ssh_client.exec_command(command)
    output = stdout.read().decode("utf-8")
    error = stderr.read().decode("utf-8")
    return output, error

def run_on_device(host, command):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh_client.connect(host, port=ssh_port, username=ssh_username, password=ssh_password)        
        output, error = run_remote_command(ssh_client, command)
        print(f"Výstup z {host}:\n{output}")
        print(f"Chybový výstup z {host}:\n{error}")
    finally:
        ssh_client.close()

# Nastavení připojení SSH
ssh_port = 22
ssh_username = "pi"
ssh_password = "Vmdkm742"

remote_command = "python3 /home/pi/OLED_Module_Code/RaspberryPi/python/example/pizero/ffb.py"

# Seznam IP adres zařízení
device_hosts = ["192.168.0.103"]
# Použijeme ThreadPoolExecutor pro spuštění funkcí na různých zařízeních ve vláknech
with ThreadPoolExecutor() as executor:
    # Pro každé zařízení spustíme funkci run_on_device s odpovídajícím hostem
    futures = [executor.submit(run_on_device, host, remote_command) for host in device_hosts]

    # Počkáme na dokončení všech úloh
    for future in futures:
        future.result()

remote_command = "python3 /home/pi/OLED_Module_Code/RaspberryPi/python/example/pizero/rl.py"

# Seznam IP adres zařízení
device_hosts = ["192.168.0.101"]
# Použijeme ThreadPoolExecutor pro spuštění funkcí na různých zařízeních ve vláknech
with ThreadPoolExecutor() as executor:
    # Pro každé zařízení spustíme funkci run_on_device s odpovídajícím hostem
    futures = [executor.submit(run_on_device, host, remote_command) for host in device_hosts]

    # Počkáme na dokončení všech úloh
    for future in futures:
        future.result()

remote_command = "python3 /home/pi/OLED_Module_Code/RaspberryPi/python/example/pizero/ffb.py"

# Seznam IP adres zařízení
device_hosts = ["192.168.0.101"]
# Použijeme ThreadPoolExecutor pro spuštění funkcí na různých zařízeních ve vláknech
with ThreadPoolExecutor() as executor:
    # Pro každé zařízení spustíme funkci run_on_device s odpovídajícím hostem
    futures = [executor.submit(run_on_device, host, remote_command) for host in device_hosts]

    # Počkáme na dokončení všech úloh
    for future in futures:
        future.result()

remote_command = "python3 /home/pi/OLED_Module_Code/RaspberryPi/python/example/pizero/rl.py"

# Seznam IP adres zařízení
device_hosts = ["192.168.0.105"]
# Použijeme ThreadPoolExecutor pro spuštění funkcí na různých zařízeních ve vláknech
with ThreadPoolExecutor() as executor:
    # Pro každé zařízení spustíme funkci run_on_device s odpovídajícím hostem
    futures = [executor.submit(run_on_device, host, remote_command) for host in device_hosts]

    # Počkáme na dokončení všech úloh
    for future in futures:
        future.result()

remote_command = "python3 /home/pi/OLED_Module_Code/RaspberryPi/python/example/pizero/ffb.py"

# Seznam IP adres zařízení
device_hosts = ["192.168.0.105"]
# Použijeme ThreadPoolExecutor pro spuštění funkcí na různých zařízeních ve vláknech
with ThreadPoolExecutor() as executor:
    # Pro každé zařízení spustíme funkci run_on_device s odpovídajícím hostem
    futures = [executor.submit(run_on_device, host, remote_command) for host in device_hosts]

    # Počkáme na dokončení všech úloh
    for future in futures:
        future.result()

remote_command = "python3 /home/pi/OLED_Module_Code/RaspberryPi/python/example/pizero/rl.py"

# Seznam IP adres zařízení
device_hosts = ["192.168.0.107"]
# Použijeme ThreadPoolExecutor pro spuštění funkcí na různých zařízeních ve vláknech
with ThreadPoolExecutor() as executor:
    # Pro každé zařízení spustíme funkci run_on_device s odpovídajícím hostem
    futures = [executor.submit(run_on_device, host, remote_command) for host in device_hosts]

    # Počkáme na dokončení všech úloh
    for future in futures:
        future.result()

remote_command = "python3 /home/pi/OLED_Module_Code/RaspberryPi/python/example/end.py"

# Seznam IP adres zařízení
device_hosts = ["192.168.0.101", "192.168.0.103", "192.168.0.105", "192.168.0.107"]

# Použijeme ThreadPoolExecutor pro spuštění funkcí na různých zařízeních ve vláknech
with ThreadPoolExecutor() as executor:
    # Pro každé zařízení spustíme funkci run_on_device s odpovídajícím hostem
    futures = [executor.submit(run_on_device, host, remote_command) for host in device_hosts]

    # Počkáme na dokončení všech úloh
    for future in futures:
        future.result()

# Start pico1.py on port ACM0
subprocess.Popen(["ampy", "--port", "/dev/ttyACM0", "run", "nick.py"])