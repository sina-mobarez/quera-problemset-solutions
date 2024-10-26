k = 6

def show_quera_map_exhibition(number_of_company):
    for i in range(1,10):
        if (i % 2) == 0:
            if (i < number_of_company+2):
                if i-1 == number_of_company:
                    print(f'#ghorfe{i-1}..............#')
                else:
                    print(f'#ghorfe{i-1}.......ghorfe{i}#')
            else:
                print(f'#.....................#')
        elif i == 9:
            print('#######################')
        else:
            print('########.......########')


if __name__ == '__main__':
    show_quera_map_exhibition(k)