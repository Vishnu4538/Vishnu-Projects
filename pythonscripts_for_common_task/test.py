import yaml


#example for createing yaml using
metadate={
     "labels":{
         "app": "webappp",
         "name": "webappp"
     }    
}

spec={
    "template":{
        "spec": {
            "container":["image: docker.io/vishnu4538/nginxapp:8","name: website"]
        }
    }
}

data={

    "metadate":metadate,
    "spec": spec

}

print(data)

f=open("demo.yaml","w")
yaml.safe_dump(data,f)

f=open("demo.yaml", "r")
r=yaml.safe_load(f)

print(r["spec"]["template"]["spec"]["container"][0])