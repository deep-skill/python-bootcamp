moves_list = []

def hanoi(n, source, target, other):
    if n == 0:
        return
    
    hanoi(n-1, source, other, target)
    moves_list.append((source, target))
    hanoi(n-1, other, target, source)

if __name__ == "__main__":
    n_disks = int(input("Nº de discos: "))

    hanoi(n_disks, 'A', 'C', 'B')

    print("Cantidad de movimientos: " + str(len(moves_list)))

    for move in moves_list:
        source, target = move
        print('Mover desde ' + str(source) + ' hasta ' + str(target))
