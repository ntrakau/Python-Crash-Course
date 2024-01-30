#NT Rakau

visit_local = ['cape town','kenya', 'colombia', 'thailand', 'spain']
print(visit_local)
print(sorted(visit_local))#sorted= print list alphabetically without sorting the original list
print(visit_local)

print(sorted(visit_local,reverse=True))#pass list + other func = can take two args
print(visit_local)
#print the list in reverse chronologically
visit_local.reverse()
print(visit_local)
#reverse the above reversed list
visit_local.reverse()
print(visit_local)
#sorting the list alphabetically
visit_local.sort()
print(visit_local)
#using sort to reverse the list in alphabetical order
visit_local.sort(reverse=True)
print(visit_local)