seasons = ['Spring', 'Summer', 'Fall', 'Winter']
a =   list(enumerate(seasons))
print(a)
b=enumerate(seasons)
print(dir(b))
print(getattr(b,'__str__'))
