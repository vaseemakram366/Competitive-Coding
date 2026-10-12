# Tower of Hanoi (Recursion Tree ke saath)

def hanoi(n, src, helper, dest):
    if n == 0:
        return 0
    moves = hanoi(n - 1, src, dest, helper)
    print(f"Move disk {n} from {src} to {dest}")
    moves += 1
    moves += hanoi(n-1, helper, src, dest)
    return moves
total = hanoi(3, 'A', 'B', 'C')
print("Total moves:", total)

