ages = [34,39,20,18,13,54]
adult_ages = list(filter(lambda x:x >= 19, ages))
print(adult_ages)

adult_ages2=[x for x in ages if x>=19]
print(adult_ages2)