def patter_match(pattern):
    file=open("/home/vishnu/error.log",'r')
    lines= file.readlines()
    for line in lines:
        if pattern in line:
            print(f"we found the {pattern}  at line number ")
            print('Exactly error line in file is',"","", f"{line}")
            break
        else:
            continue


patter_match("error")
