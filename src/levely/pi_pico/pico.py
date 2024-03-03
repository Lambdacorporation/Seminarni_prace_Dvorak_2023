import subprocess

# Start pico1.py on port ACM0
subprocess.Popen(["ampy", "--port", "/dev/ttyACM0", "run", "pico1.py"])
