from string import Template

name = input("Please enter the name: ")
part_of_body = input("Please enter the part of the body: ")
type_of_liquid = input("Please enter the type of liquid: ")
substance = input("Please enter the substance: ")

template = Template(
    "$name is sick with the $part_of_body flu. Drink more $type_of_liquid and take $substance as needed")

print("Here is your story:")
print(template.substitute(name=name, part_of_body=part_of_body,
                          type_of_liquid=type_of_liquid, substance=substance))
