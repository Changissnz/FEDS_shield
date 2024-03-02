from firing_agent import *
from structure import *
from bi_key import *
from crypt_env import *
from decrypt_env import *

### WARNING: unstable
"""
make a new bikey

EX:
40 12 62 75
0 1\n5 0\n6 1\n7 1
"""
def a_nu_bikey():
    #operands = [20,30,12]
    #opIndex = [(0,1),(4,0),(6,1)]
    print("SO U WAN DA NU BI-KEY,DA NEW-ORDER FREEDOM,RII??")
    print("DO U NEE EXAMPULL? (y) or (*)")
    x = input().lower()
    # EX
    if x == "y":
        print("----")
        print("key has max=8 operands")
        print("each operand is integer in [0,100]")
        print("key has index, a sequence of pairs (x1,x2)")
        print("x1 in range [0,7]")
        print("x2 in range [0,1]")
        print("index is equal to number of operands")
        print("example:")
        print("\tthree operands: 20 30 12")
        print("\toperand index:")
        print("\t0 1\\n4 0\\n6 1")
        print("----")

    print("your key!")
    operand = str(input())
    opIndex = str(input())
    o1,o2 = None,None

    try:

        o1 = list(int(x) for x in operand.split())
    except:
        print("INVALID OPERAND,RE-LOOP")
        return a_nu_bikey()

    try:
        opIndex = opIndex.replace("\\n","\n")
        o2 = [list(int(y) for y in x.split()) for x in opIndex.splitlines()]
        # check values of o2
    except:
        print("INVALID OPERATOR,RE-LOOP")
        return a_nu_bikey()

    print("enter in key modulo (integer)")
    m = input()
    try:
        m = int(m)
    except:
        print("INVALID MODULO,RE-LOOP")
        return a_nu_bikey()

    # make and save the key 
    bk = BiKey(o1,o2,m)
    bk.make_key()
    print("save your bi-key in 2 files!")
    print("\t\t** file names must not contain punctuation")
    fi = input()
    fi2 = input()
    try: 
        bk.save(fi,fi2) 
        print("file saved in:\n{}\n{}".format(modifini(fi),modifini(fi2))) 
    except:
        print("INVALID FILE FOR BI-KEY")

### WARNING: unstable 
"""
make a new shield
"""
def a_nu_shield():
    print("SO U WAN DA NU SHIELD,DA NEW-ORDER DEFENSE,RII??")
    print("DO U NEE EXAMPULL? (y) or (*)")
    x = input().lower()
    # EX
    if x == "y":
        print("shield is sequence of sequences")
        print("each sequence consists of integers")
        print("** recommended that integers lie in range of alphabet")
        print("example:")
        print("\t a shield of 5 layers")
        print("\t [[0,12,32],[10,41],[62,56],[82,89],[100]]")
        print("\t input the following:")
        print("0 12 32\\n10 41\\n62 56\\n82 89\\n100")

    # make the shield
    print("your shield!")
    x = input()
    shield = None
    try:
        x = x.replace("\\n","\n")
        shield = list(list(int(y) for y in x_.split()) for x_ in x.splitlines())
    except:
        print("INVALID SHIELD")
        return 

    # save the shield
    print("save your shield in a file!")
    print("\t\t** file names must not contain punctuation")
    fi = input()
    try:
        save_shield_to_file(shield,fi)
    except:
        print("INVALID FILE FOR SHIELD")
    return

### WARNING: unstable
"""
make a new alphabet into a file
"""
def a_nu_alpha_bet():
    print("----------------------------------")
    print("a nu alpha bet? a nu order?")
    print("eef u wan da cusstomb alphabet,put dict as *.csv file in folder /data")
    print("EX: u wan\n")
    print("ALPHABET = {'A':132314634635, 'FOOL\'S':122312441412, 'SECRET':100001312321}")
    print("\ninput this streng")
    print("A 132314634635\\nFOOLS 122312441412\\nSECRET 100001312321")
    print("----------------------------------")
    print("important: all characters of message must be present in alphabet")
    print("\t\tsee `std_alpha.csv`")
    print("your alphabet!")
    i = input()
    i = i.replace("\\n","\n")
    d = dict(x.split() for x in i.splitlines())

    try:
        for k in d.keys():
            d[k] = int(d[k])
        print("save your alphabet in a file!")
        print("\t\t** file names must not contain punctuation")
        fi = input()
        try: 
            save_alphabet(d,fi) 
            print("file saved in : {}".format(modifini(fi))) 
        except:
            print("INVALID FILE FOR ALPHA")
    except:
        print("INVALID ALPHA")
    return


def input_msg():
    print("no large messages in this interface pls")
    print("")
    print("pls pls hAAhAAhAA")
    print("DO U NEE EXAMPULL? (y) or (*)")
    x = input().lower()
    if x == "y":
        print("---------")
        print("\t\tstore your message as file: data/*.txt")
        print("\t\tor can input message")
        print("---------")

    print("msg en fi (F) ore input (I)?")
    f = input().lower()
    m = ""
    if f == "i":
        print("\t** caution: some characters require backslash")
        m = input()
    elif f == "f":
        try: 
            m_ = input("\t\t* file:\t")
            with open("data/" + m_) as m2:
                m = m2.readlines()
                m = "".join(m) 
        except:
            print("INVALID MSG, RE-LOOP")
            return input_msg()
    else:
        print("INVALID INPUT, RE-LOOP")
        return input_msg()
    return m

def main():
    print("V3IIKVM 2 FEDS shield")
    print("vnp/~0w3n KrYP70Q/~4PN1K P0D")

    # manual
    print("------")
    print("0 -> make alphabet")
    print("1 -> load vars for FEDS shield")
    print("2 -> quit")
    print("------")
    x = input()

    if x == "2":
        return 

    if x == "0":
        a_nu_alpha_bet()
        return main()
    if x != "1":
        print("INVALID INPUT,RE-LOOP")
        return main()

    ed = input("ENCRYPT(e) or DECRYPT(d)").lower()
    if ed not in ["e","d"]:
        print("INVALID INPUT,RE-LOOP")
        return main()

    a = input("\t\t* load alphabet file:\t")
    s = input("\t\t* load shield file:\t")
    bk1 = input("\t\t* load FIRE BiKey files:\n\t** ").split()
    
    if ed == "e":
        bk2 = input("\t\t* load FRIEND-ENEMY BiKey file:\n\t** ").split()
        m = input_msg()
        wf = input("\t\t* load write-file (ex: wf1.txt):\t")
        ce = CryptEnv1(a,s,bk1,bk2,m,wf)
        while ce.encode_one(): continue
    else:
        m = input("enter in encrypted file:\t")
        de = DecryptEnv1(s,m,bk1,a)
        de.decode()
        print("DECODED MSG")
        print(de.deco) 

r = "r = 345drgRE5YERH3498YTIODFIL;LJI;LDFLJ;ERI;OJEAR;IHOGD.KNERKJ;TRGIHERKJOGFRIJ;LI;OJEGT;IHODGIJO;KJL;KDGKJ;LDGKJ;LDGLKJDGKJL;DJ;LDGKJL;DGSKJ;LDFJLDLDKLLKJ;DDS;L;IJ vampire"