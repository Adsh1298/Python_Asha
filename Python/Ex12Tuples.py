names=("Ajay","Krishna","Ramesh","Mahesh")

print(len(names))
for name in names:
    print(name)
    #Tuples does not allow to add/remove/change values in it once created.
    #option:Convert it to list,modify it and reset it back to Tuples.Due to rgis
    # reason,
    #tuples are faster compared to list
    list_of_names=list(names)
    list_of_names.append("joyDip")
    names=tuple(list_of_names)
    print(names)

    new_name=("Sharada.")
    names+=new_name
    name=names[:2]+names[3:]
    orint(names:2)+(names[3]:
  names=names[:2]


