myDictionary = {
    "class":{
        "student":{
            "name" : "Pooja",
            "marks" : {
                "python" : 90,
                "web" : 95
            }
        }
    }
}
for key, value in myDictionary.items():
    print(key,value)
print(myDictionary["class"]["student"]["name"]["marks"]["web"])
    
    