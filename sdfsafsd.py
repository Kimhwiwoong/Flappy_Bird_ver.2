from operator import itemgetter
TOPFIVE=[('kim',0),('kim',0),('kim',0),('kim',0),('kim',0)]
TOPFIVE.append(('lee',1))
TOPFIVE.sort(key=itemgetter(1),reverse=True)
TOPFIVE.pop()
print(TOPFIVE)
