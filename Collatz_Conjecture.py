import matplotlib.pyplot as plt

def collatz(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

# Get user input for starting number
start_number = int(input("Enter a positive integer to start the Collatz sequence: "))

# Generate Collatz sequence
collatz_sequence = collatz(start_number)

# Visualize the sequence
plt.plot(collatz_sequence, marker='o', linestyle='-', color='b')
plt.xlabel('Step')
plt.ylabel('Value')
plt.title('Collatz Conjecture Visualization')
plt.grid(True)
plt.show()
