
# me
def item_order(x):
    
    j=x.count('salad')
    k=x.count('water')
    l=x.count('hamburger')
    return "salad:%s water:%s hamburger:%s" %(j,k,l)
    
    
order = "salad water hamburger salad hamburger"
print item_order(order)


#mit
def item_order(order):
    salad = 0
    hamburger = 0
    water = 0
    
    startspace = 0    
    space = 0
    while space > -1:
        space = order.find(' ', startspace)
        if space == -1:
            word = order[startspace:]
        else:
            word = order[startspace:space]
        if word == "salad":
            salad += 1
        if word == "hamburger":
            hamburger += 1
        if word == "water":
            water += 1
        startspace = space+1
    neworder = "salad:"+str(salad)+" hamburger:"+str(hamburger)+" water:"+str(water)
    return neworder
print item_order(order)

