# asterisk_odd_even
def main():
    pass
    import math
    inp=input()
    l=[]
    if(len(inp)%2==0):
        even= math.ceil((len(inp)/2))
        rpl=inp.replace(inp[even],"*")
        inp=rpl
        rpl2=inp.replace(inp[even-1],"*")
        print(rpl2)
    else:
        odd= math.ceil((len(inp)/3))
        rpl3=inp.replace(inp[odd],"*")
        print(rpl3)
if __name__ == '__main__':
    main()
