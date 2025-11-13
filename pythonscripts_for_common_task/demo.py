import devops_module as dev
import sys

nuk=int(sys.argv[1])

path=sys.argv[2]


dev.update_image(nuk,path)


