def sierpienski(n):
    if n == 0:
        return ["*"]

    last_fig = sierpienski(n-1)

    fig = []

    for line in last_fig:
        fig.append((" " * (1 << (n-1))) + line + (" " * (1 << (n-1))))
    
    for line in last_fig:
        fig.append(line + " " + line)

    return fig

if __name__ == "__main__":
    n = int(input("Size: "))
    fig = sierpienski(n)

    for line in fig:
        print(line)

