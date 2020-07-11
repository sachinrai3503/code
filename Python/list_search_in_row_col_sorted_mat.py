# https://www.geeksforgeeks.org/search-in-row-wise-and-column-wise-sorted-matrix/

def search_in_mat(ip_arr_2d, num):
    i, j = 0, len(ip_arr_2d[0])-1
    while i<len(ip_arr_2d) and j>=0:
        if ip_arr_2d[i][j] == num:
            print(num,'present at', i,",", j)
            break
        elif ip_arr_2d[i][j] < num:
            i+=1
        else:
            j-=1
    else:
        print(num, 'not present')

def main():
    ip_arr_2d = [ [10, 20, 30, 40],
                      [15, 25, 35, 45],
                      [27, 29, 37, 48],
                      [32, 33, 39, 50]]
    num = 0
    print('len(ip_arr_2d) = ',len(ip_arr_2d))
    print('len(ip_arr_2d[0]) = ',len(ip_arr_2d[0]))
    print(ip_arr_2d)
    search_in_mat(ip_arr_2d,num)

if __name__ == '__main__':
    main()
