import textx.metamodel_from_file

meta = metamodel_from_file("parser.tx")
program = meta.metamodel_from_file("text.py")

print(":)")