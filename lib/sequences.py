

def print_fibonacci(length):
    if length <= 0:
        print([])
        return
    
    fib_seq = [0,1] if length  > 1 else [0]

    while len(fib_seq) < length:
        following_num = fib_seq[-1] + fib_seq[-2]
        fib_seq.append(following_num)

    print(fib_seq[:length])


     
    