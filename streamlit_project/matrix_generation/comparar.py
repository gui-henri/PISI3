def budget (filmeA, filmeB, fun):
    return funDiff(filmeA, filmeB, fun)

def index (filmeA, filmeB, fun):
    return 0

def genres (filmeA, filmeB, fun):
    return funMatches(filmeA, filmeB)
            
def movie_id (filmeA, filmeB, fun):
    return 0
    
def keywords (filmeA, filmeB, fun):
    return funMatches(filmeA, filmeB)

def original_language (filmeA, filmeB, fun):
    return int(filmeA == filmeB)
    
def original_title (filmeA, filmeB, fun):
    return 0

def overview (filmeA, filmeB, fun):
    return 0

def popularity (filmeA, filmeB, fun):
    return funDiff(filmeA, filmeB, fun)

def production_companies (filmeA, filmeB, fun):
    return funMatches(filmeA, filmeB)

def production_countries (filmeA, filmeB, fun):
    return funMatches(filmeA, filmeB)

def release_date (valA, valB, fun):
    return funDiff(valA, valB, fun)

def director (filmeA, filmeB, fun):
    return funMatches(filmeA, filmeB)

def cast (filmeA, filmeB):
    return funMatches(filmeA, filmeB)

def revenue (filmeA, filmeB, fun): 
    return funDiff(filmeA, filmeB, fun)

def runtime (filmeA, filmeB, fun):
    return funDiff(filmeA, filmeB, fun)

def title (filmeA, filmeB, fun):
    return 0

def vote_average (filmeA, filmeB, fun):
    return funDiff(filmeA, filmeB, fun)

def vote_count (filmeA, filmeB, fun):
    return funDiff(filmeA, filmeB, fun)

def funMatches (filmeA, filmeB):
    if filmeA == [] or filmeB == []:
        return 0
    
    x = 0
    
    for item in filmeA:
        if item in filmeB:
            x += 1      
    return x/max(len(filmeA), len(filmeB))

def funDiff (valA, valB, fun):
    f = eval("funDiff" + fun)
    return f(valA, valB)

def funDiffA(valA, valB, scale = 0):
    if valA == valB:
        return 1
    return 0

def funDiffB(valA, valB, scale = 0):
    return abs(abs(valA - valB) - 2)/2

def funDiffC(valA, valB, scale = 0):
    x = max(valA, valB)
    y = min(valA, valB)

    return y/x

def comp(filmeA, filmeB, tags, peso, maxPeso, fun):
    x = 0
    for k, tag in enumerate(tags):
        f = eval(tag)
        fA = filmeA[k]
        fB = filmeB[k]
        x += f(fA, fB, fun) * peso[tag]
    return x/maxPeso
