def budget (filmeA, filmeB):
    return funDiff(filmeA, filmeB)

def genres (filmeA, filmeB):
    return funMatches(filmeA, filmeB)
            
def id (filmeA, filmeB):
    return 0
    
def keywords (filmeA, filmeB):
    return funMatches(filmeA, filmeB)

def original_language (filmeA, filmeB):
    return int(filmeA == filmeB)
    
def original_title (filmeA, filmeB):
    return 0

def overview (filmeA, filmeB):
    return 0

def popularity (filmeA, filmeB):
    return funDiff(filmeA, filmeB)

def production_companies (filmeA, filmeB):
    return funMatches(filmeA, filmeB)

def production_countries (filmeA, filmeB):
    return funMatches(filmeA, filmeB)

def release_date (filmeA, filmeB):
    valA = int(filmeA[:4]) 
    valB = int(filmeB[:4])
    
    scale = 4
    
    return round(1/(1+(abs(valA - valB) ** 2/scale)), 2)

def revenue (filmeA, filmeB): 
    return funDiff(filmeA, filmeB)

def runtime (filmeA, filmeB):
    return funDiff(filmeA, filmeB)

def title (filmeA, filmeB):
    return 0

def vote_average (filmeA, filmeB):
    return funDiff(filmeA, filmeB)

def vote_count (filmeA, filmeB):
    return funDiff(filmeA, filmeB)

def funMatches (filmeA, filmeB):
    x = 0
    for item in filmeA:
        if item in filmeB:
            x += 1      
    return x/max(len(filmeA), len(filmeB))

def funDiff(valA, valB, scale = 0):
    x = max(valA, valB)
    y = min(valA, valB)
    return y/x

def comp(filmeA, filmeB, tags, peso, maxPeso):
    x = 0
    for k, tag in enumerate(tags):
        f = eval(tag)
        fA = filmeA[k]
        fB = filmeB[k]
        x += f(fA, fB) * peso[tag]
    return x/maxPeso