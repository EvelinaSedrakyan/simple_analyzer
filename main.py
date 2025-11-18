import time
import random
from analyzer import Analyzer
config_path = r"C:\Users\Acer\Desktop\simple_analyzer\config\config.txt"

interval = 2
sequence_length = 18

with open(config_path, "r") as f:
    for line in f:
        if "interval" in line:
            interval = int(line.strip().split("=")[1])
        elif "sequence_length" in line:
            sequence_length = int(line.strip().split("=")[1])

print("Interval:", interval)
print("Sequence length:", sequence_length)

analyzer = Analyzer()

try:
    while True:
        num = random.randint(1, 100)
        analyzer.add_number(num)
        if len(analyzer.numbers) > sequence_length:
            analyzer.numbers.pop(0)
        print("Numbers:", analyzer.numbers)
        print("Even:", analyzer.even_count())
        print("Odd:", analyzer.odd_count())
        print("Highest:", analyzer.highest_number())
        print("Increasing pairs:", analyzer.increasing_pairs())

        with open("data.txt", "w") as f:
            f.write(str(analyzer.numbers))

        if len(analyzer.numbers) == sequence_length and time.localtime().tm_sec == 0:
            print("Stopping program.")
            break
        time.sleep(interval)

except KeyboardInterrupt:
    print("\nStopping program")
