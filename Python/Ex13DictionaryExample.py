from multiprocessing.connection import address_type

capitals={"USA":"Washington D.C.","India":"New Delhi","China":"Beijing",
          "Japan":"Tokyo"}


###Adding pair to the dictionary####
capitals.update({"Germany":"Berlin"})
capitals["Canada"]="Ottawa"
capitals["India"]="Bhopal"
capitals.pop("China")
print(capitals)
keys=capitals.keys()
#values=capitals.values()
for key in keys:
    print(f"Country:{key},Capital:{capitals[key]}")
for key,value in capitals.items():
    print(f"Country:{key},Capital:{value}")

    # Exercise
employee={}
employee["id"]=123
employee["name"]="asha"
employee["address"]="RR Nagar, Bangalore"
employee["salary"]=100000
print("These are the details of the Employee:")
for key,value in employee.items():
    print(f"{key}:{value}")


