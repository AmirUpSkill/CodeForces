def solve():
    s = input()
    s_list = list(map(int, s.split("+")))
    s_list.sort()
    result = "+".join(map(str, s_list))
    print(result)  
solve()
