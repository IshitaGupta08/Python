marks = {
    "Riya":100,
    "Saloni":69,
    "Abhay":99,
    "Rohan":78,
    0:"Ishita"
}
print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"Rohan":99,"Renuka":100})
print(marks)
print(marks.get("Riya")) #prints none if key doesn't exits in dictionary otherwise the output are same for both of them
print(marks["Riya"]) #print or give error if key doesn't exits in dictionary otherwise the output are same for both of them
