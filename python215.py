#Python – Convert Nested Tuple to Custom Key Dictionary


def Convert(tup, di):
	di = dict(tup)
	return di
tups = [("akash", 10), ("gaurav", 12), ("anand", 14),
	("suraj", 20), ("akhil", 25), ("ashish", 30)]
dictionary = {}
print (Convert(tups, dictionary))


list_1=[("Nakul",93), ("Shivansh",45), ("Samved",65),("Yash",88), ("Vidit",70), ("Pradeep",52)]
dict_1=dict()
for student,score in list_1:
    dict_1.setdefault(student, []).append(score)
print(dict_1)