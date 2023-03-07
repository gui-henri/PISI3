def budget (k, filmeA, filmeB):
    return funDiff(filmeA[k], filmeB[k])

def genres (k, filmeA, filmeB):
    return funMatches(k, filmeA, filmeB)
            
def id (k, filmeA, filmeB):
    return 0
    
def keywords (k, filmeA, filmeB):
    return funMatches(k, filmeA, filmeB)

def original_language (k, filmeA, filmeB):
    return int(filmeA == filmeB)
    
def original_title (k, filmeA, filmeB):
    return 0

def overview (k, filmeA, filmeB):
    return 0

def popularity (k, filmeA, filmeB):
    return funDiff(filmeA[k], filmeB[k])

def production_companies (k, filmeA, filmeB):
    return funMatches(k, filmeA, filmeB)

def production_countries (k, filmeA, filmeB):
    return funMatches(k, filmeA, filmeB)

def release_date (k, filmeA, filmeB):
    scale = 4
    return funDiff(int(filmeA[k][:4]), int(filmeB[k][:4]), scale)

def revenue (k, filmeA, filmeB): 
    return funDiff(filmeA[k], filmeB[k])

def runtime (k, filmeA, filmeB):
    return funDiff(filmeA[k], filmeB[k])

def title (k, filmeA, filmeB):
    return 0

def vote_average (k, filmeA, filmeB):
    return funDiff(filmeA[k], filmeB[k])

def vote_count (k, filmeA, filmeB):
    return funDiff(filmeA[k], filmeB[k])

def funMatches (k, filmeA, filmeB):
    x = 0
    for genero in filmeA[k]:
        if genero in filmeB[k]:
            x += 1            
    return x/max(len(filmeA[k]), len(filmeB[k]))

def funDiff(valA, valB, scale = 0):
    if scale == 0:
        scale = max(valA, valB)
        
    return 1/(1+(abs(valA - valB)/scale))

def comp(filmeA, filmeB, tags, peso):
    x = 0
    for k, tag in enumerate(tags):
        f = eval(tag)
        x += f(k, filmeA, filmeB) * peso[tag]
    return x