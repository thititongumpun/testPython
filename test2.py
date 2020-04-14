import io

def file_read(fname):
    with open (fname, "r") as myFile:
        data = myFile.read()          

        string = data        
        counter1 = string.count('P')
        counter2 = string.count('y')
        counter3 = string.count('t')
        counter4 = string.count('h')
        counter5 = string.count('o')
        counter6 = string.count('n')
        counter7 = string.count('i')
        counter8 = string.count('s')
        counter9 = string.count('a')
        counter10 = string.count('u')
        counter11 = string.count('l')
        counter12 = string.count('r')
        counter13 = string.count('g')
        counter14 = string.count('m')
        counter15 = string.count('e')
        counter16 = string.count('I')
        counter17 = string.count('w')
        counter18 = string.count('c')
        counter19 = string.count('d')
        counter20 = string.count('b')
        counter21 = string.count('G')
        counter22 = string.count('v')
        counter23 = string.count('R')
        counter24 = string.count('1')
        counter25 = string.count('9')
        counter26 = string.count('.')
        print('P =',str(counter1))
        print('y =',str(counter2))
        print('t =',str(counter3))
        print('h =',str(counter4))
        print('o =',str(counter5))
        print('n =',str(counter6))
        print('i =',str(counter7))
        print('s =',str(counter8))
        print('a =',str(counter9))
        print('u =',str(counter10))
        print('l =',str(counter11))
        print('r =',str(counter12))
        print('g =',str(counter13))
        print('M =',str(counter14))
        print('e =',str(counter15))
        print('I =',str(counter16))
        print('w =',str(counter17))
        print('c =',str(counter18))
        print('d =',str(counter19))
        print('b =',str(counter20))        
        print('G =',str(counter21))
        print('v =',str(counter22))
        print('R =',str(counter23))
        print('1 =',str(counter24))
        print('0 =',str(counter25))
        print('. =',str(counter26))
        # print("P = ", count)
        # for i in string:
        #     if i == 'r':
        #         count = count +1

 # Run
if __name__ == "__main__":
    file_read('test_read.txt')       



# def counter(string,sub_string):
#     l = len(sub_string)
#     count = 0
#     for i in range(len(string) - len(sub_string) + 1):
#         if string[i:i+len(sub_string)] == sub_string:
#             count += 1
#     return count






# ------Test-----------

# string = "Python is a popular programming language. It was created by Guido van Rossum, and released in 1991."
# substring = "P"

# count = string.count(substring)
# # count2 = string.count

# # # print count
# # print("P = ", count)


# for i in string:
#     print(i, count)



