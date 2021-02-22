#Ek program likho jo ki dictionaries ki values ko sort(ascending or descending) kar de.
x={'bijender':45, 'deepak':60, 'param':20, 'anjili':30, 'roshini':50}
import operator
m=dict(sorted(x.items(), key=operator.itemgetter(1)))
print(m)
n=dict(sorted(x.items(), key=operator.itemgetter(1),reverse=True))
print(n)