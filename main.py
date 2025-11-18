config_path = r"C:\Users\Acer\Desktop\simple_analyzer\config\config.txt"

interval = 0
sequence_length = 0

with open(config_path, "r") as f:
    for line in f:
        if "interval" in line:
            interval = int(line.strip().split("=")[1])
        elif "sequence_length" in line:
            sequence_length = int(line.strip().split("=")[1])

print("Interval:", interval)
print("Sequence length:", sequence_length)
