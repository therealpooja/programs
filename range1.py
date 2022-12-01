name=(input(""))
i=0
temp_var= ""
while i< len(name):
          if name[i] not in temp_var:
                    print(f"{name[i]} : {name.count(name[i])}")
          i=i+1