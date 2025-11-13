import devops_module as dev
import sys

buildid=sys.argv[0]
filepath=sys.argv[1]

dev.update_image(buildid,filepath)