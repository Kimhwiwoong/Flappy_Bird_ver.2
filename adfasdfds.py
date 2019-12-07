TOPFIVE={'hoho' : 23 , 'jiji' : 33}
def writeScore(score):
    for x in TOPFIVE.values():
        if score>=x :
            TOPFIVE['name']=score
            TOPFIVE.sorted(TOPFIVE.items(),reverse=True)
            TOPFIVE.pop()
            return

writeScore(31)
print(TOPFIVE)
        
