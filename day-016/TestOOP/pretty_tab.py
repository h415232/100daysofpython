import prettytable

x = prettytable.PrettyTable()

x.field_names = ["Pokemon Species", "Type"]
x.add_row(["Pickachu","Electric"])
x.add_row(["Squirtle","Water"])
x.add_row(["Charmander","Fire"])
print(x)