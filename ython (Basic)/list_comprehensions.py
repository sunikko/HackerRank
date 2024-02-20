if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    # create a list of [(x,y,z)]
    grid_list = []
    for ix in range(x+1):
        for iy in range(y+1):
            for iz in range(z+1):
                # filter out sum to n
                if (ix + iy + iz) is not n:
                    grid_list.append([ix, iy, iz])
                    
    # <-> list comprehensions
    grid_list = [[ix, iy, iz] for ix in range(x+1) for iy in range(y+1) for iz in range(z+1) if (ix + iy + iz) != n]
                    
    print(grid_list)
    
