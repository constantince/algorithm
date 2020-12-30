import re
Palindromic_String = "iWuwi  ,  "
Palindromic_In_String = "pxiwowix"
def is_p_s_for(strs):
    how_long = len(strs)
    for i in range(how_long):
        cur = strs[i]
        qm = strs[how_long - i - 1]
        if i == how_long - i - 1:
            return True
        if cur == qm:
            pass
        else:
            return False
    return True

def is_p_s_while(strs):
    how_long = len(strs)
    i = 0
    limit = (how_long - 1) / 2
    while(i < limit):
        cur = strs[i]
        miror = strs[-1 - i]
        if cur == miror:
            i = i + 1
            continue
        else:
            return False
    
    return True

def is_p_s_native(strs: str) -> bool:
    new_str = re.sub(r"[^\w]|\s", "", strs.lower())
    return new_str[::-1] == new_str

def find_p_s(strs: str) -> bool:
    pass


if __name__ == "__main__":
    print(is_p_s_native(Palindromic_String))