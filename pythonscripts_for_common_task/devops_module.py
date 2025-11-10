import yaml


def patter_match(pattern,filename):
    file=open(filename,'r')
    lines= file.readlines()
    for line in lines:
        if pattern in line:
            print(f"we found the {pattern}  at {filename}")
            print('Exactly line in file is' , f"{line}")
            break
        else:
            continue


def update_image(id,filename):
    f = open(filename, "r")
    r = yaml.safe_load(f)
    r["spec"]["template"]["spec"]["containers"][1] = f"image:docker.io/vishnu:{id}"
    f = open(filename, "w")
    yaml.dump(r, f)


update_image(24,"vishnu.yml")
