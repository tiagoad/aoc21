with open('input.txt') as f:
    full_list = list(map(lambda l: list(l.rstrip()), f))

def crit_o2(n0, n1, h0, h1):
    if n0 == n1:
        return h1

    elif n0 > n1:
        return h0

    elif n1 > n0:
        return h1

def crit_co2(n0, n1, h0, h1):
    if n0 == n1:
        return h0

    elif n0 > n1:
        return h1

    elif n1 > n0:
        return h0

def get_rating(nums, crit, bit=0):
    h0 = []
    h1 = []

    if len(nums) == 1:
        return int(''.join(nums[0]), 2)

    for n in nums:
        if n[bit] == '0':
            h0.append(n)
        else:
            h1.append(n)
    
    n0 = len(h0)
    n1 = len(h1)

    return get_rating(
        nums=crit(
            h0=h0,
            h1=h1,
            n0=n0,
            n1=n1
        ), 
        crit=crit, 
        bit=bit+1
    )


o2_rating = get_rating(full_list, crit_o2)
co2_rating = get_rating(full_list, crit_co2)

print(o2_rating * co2_rating)