from collections import deque
def search(text,pattern,history):
    previous_line=deque(maxlen=history)
    for line in text:
        if pattern in line:
            yield line, previous_line
        previous_line.append(line)
line,previous_line=search(["Pedro henrique","um","joao","um"],"um",2)
print(f"{line},{previous_line}")