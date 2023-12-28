#defining the list
data = [10,"501",22,"37",100,"uma",87,351]

#Getting the datatype using lambda fn
checkresult = list(map(lambda x: type(x), data))
print(checkresult)

