if __name__ == '__main__':
    N = int(input())
    output_list = []
    
    for _ in range(N):
        inputs = input().split()
        match inputs[0]:
            case 'insert':
                output_list.insert(int(inputs[1]), int(inputs[2]))
            case 'print':
                print(output_list)
            case 'append':
                output_list.append(int(inputs[1]))
            case 'remove':
                output_list.remove(int(inputs[1]))
            case 'sort':
                output_list.sort()
            case 'pop':
                output_list.pop()
            case 'reverse':
                output_list.reverse()
