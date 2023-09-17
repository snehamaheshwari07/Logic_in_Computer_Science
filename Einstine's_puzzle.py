from itertools import combinations
from copy import deepcopy
colors=["R", "G", "W", "Y", "B"]
nationalitys=["Br", "S", "D", "N", "Ge"]
beverages=["T", "C", "M", "Be", "Wa"]
cigars= ["P", "Du", "Bl", "Blu", "Pr"]
pets= ["Do", "Bi", "C", "F", "H"]

variables = []
variable_number=dict()
i=1
for house in range(1, 6):
    for color in ["R", "G", "W", "Y", "B"]:
        var=f"H{house}col{color}"
        variables.append(var) 
        variable_number[var]=i
        i+=1
    for nationality in ["Br", "S", "D", "N", "Ge"]:
        var=f"H{house}na{nationality}"
        variables.append(var) 
        variable_number[var]=i
        i+=1
    for beverage in ["T", "C", "M", "Be", "Wa"]:
        var=f"H{house}bev{beverage}"
        variables.append(var) 
        variable_number[var]=i
        i+=1
    for cigar in ["P", "Du", "Bl", "Blu", "Pr"]:
        var=f"H{house}cig{cigar}"
        variables.append(var) 
        variable_number[var]=i
        i+=1
    for pet in ["Do", "Bi", "C", "F", "H"]:
        var=f"H{house}pet{pet}"
        variables.append(var) 
        variable_number[var]=i
        i+=1
clauses=[]
#atleast one color for each house
for i in range(1,6):
    clausec=[]
    for color in ["R", "G", "W", "Y", "B"]:
        clausec.append(f'H{i}col{color}')
    clauses.append(clausec)
    clausen=[]
    for nationality in ["Br", "S", "D", "N", "Ge"]:
        clausen.append(f'H{i}na{nationality}')
    clauses.append(clausen)
    clauseb=[]
    for beverage in ["T", "C", "M", "Be", "Wa"]:
        clauseb.append(f"H{i}bev{beverage}")
    clauses.append(clauseb)
    clauseci=[]
    for cigar in ["P", "Du", "Bl", "Blu", "Pr"]:
        clauseci.append(f"H{i}cig{cigar}")
    clauses.append(clauseci)
    clausep=[]
    for pet in ["Do", "Bi", "C", "F", "H"]:
        clausep.append(f"H{i}pet{pet}")
    clauses.append(clausep)
        
    
#atmost one color is assigned to each house
rescol = list(combinations(colors, 2))
for i in range(1,6):
    for res in rescol:
        clause=[f'-H{i}col{res[0]}', f'-H{i}col{res[1]}']
        clauses.append(clause)
#atmost one nation is assigned to each house        
resnat = list(combinations(nationalitys, 2))
for i in range(1,6):
    for res in resnat:
        clause=[f'-H{i}na{res[0]}', f'-H{i}na{res[1]}']
        clauses.append(clause)

#atmost one beverage is assigned to each house        
resbev = list(combinations(beverages, 2))
for i in range(1,6):
    for res in resbev:
        clause=[f'-H{i}bev{res[0]}', f'-H{i}bev{res[1]}']
        clauses.append(clause)

#atmost one cigar is assigned to each house        
rescig = list(combinations(cigars, 2))
for i in range(1,6):
    for res in rescig:
        clause=[f'-H{i}cig{res[0]}', f'-H{i}cig{res[1]}']
        clauses.append(clause)
        
#atmost one pet is assigned to each house        
respet = list(combinations(pets, 2))
for i in range(1,6):
    for res in respet:
        clause=[f'-H{i}pet{res[0]}', f'-H{i}pet{res[1]}']
        clauses.append(clause)

#no 2 houses have same catagory value
for i in range(1,6):
    for j in range(i+1,6):
        for col in colors:
            clause=[f'-H{i}col{col}',f'-H{j}col{col}']
            clauses.append(clause)
        for nat in nationalitys:
            clause=[f'-H{i}na{nat}',f'-H{j}na{nat}']
            clauses.append(clause)
        for bev in beverages:
            clause=[f'-H{i}bev{bev}',f'-H{j}bev{bev}']
            clauses.append(clause)
        for cig in cigars:
            clause=[f'-H{i}cig{cig}',f'-H{j}cig{cig}']
            clauses.append(clause)
        for pet in pets:
            clause=[f'-H{i}pet{pet}',f'-H{j}pet{pet}']
            clauses.append(clause)

for i in range(1,6):
    #brit is in the red house
    clause=[f'H{i}naBr',f'-H{i}colR']
    clauses.append(clause)
    clause=[f'-H{i}naBr',f'H{i}colR']
    clauses.append(clause)
    
    #The Swede keeps dogs as pets
    clause=[f'H{i}petDo',f'-H{i}naS']
    clauses.append(clause)
    clause=[f'-H{i}petDo',f'H{i}naS']
    clauses.append(clause)
    
#     The Dane drinks tea
    clause=[f'H{i}naD',f'-H{i}bevT']
    clauses.append(clause)
    clause=[f'-H{i}naD',f'H{i}bevT']
    clauses.append(clause)
    
#     The green house’s owner drinks coffee
    clause=[f'H{i}colG',f'-H{i}bevC']
    clauses.append(clause)
    clause=[f'-H{i}colG',f'H{i}bevC']
    clauses.append(clause)
    
#     The person who smokes Pall Mall rears birds
    clause=[f'H{i}cigP',f'-H{i}petBi']
    clauses.append(clause)
    clause=[f'-H{i}cigP',f'H{i}petBi']
    clauses.append(clause)
    
#     The owner of the yellow house smokes Dunhill.
    clause=[f'H{i}colY',f'-H{i}cigDu']
    clauses.append(clause)
    clause=[f'-H{i}colY',f'H{i}cigDu']
    clauses.append(clause)
    
#     The owner who smokes Bluemasters drinks beer
    clause=[f'H{i}bevBe',f'-H{i}cigBlu']
    clauses.append(clause)
    clause=[f'-H{i}bevBe',f'H{i}cigBlu']
    clauses.append(clause)
    
#     The German smokes Prince
    clause=[f'H{i}naGe',f'-H{i}cigPr']
    clauses.append(clause)
    clause=[f'-H{i}naGe',f'H{i}cigPr']
    clauses.append(clause)
    
    
# The green house is on the left of the white house
for i in range(2,6):
    clause=[f'H{i-1}colG',f'-H{i}colW']
    clauses.append(clause)
    clause=[f'-H{i-1}colG',f'H{i}colW']
    clauses.append(clause)
    
# The man who smokes Blends lives next to the one who keeps cats
for i in range(2,5):
    clause=[f'-H{i}petC',f'H{i+1}cigBl', f'H{i-1}cigBl']
    clauses.append(clause)
    
clause=[f'-H1petC',f'H2cigBl']
clauses.append(clause)
clause=[f'-H5petC',f'H4cigBl']
clauses.append(clause)
    
    
# The man who keeps the horse lives next to the man who smokes Dunhill.
for i in range(2,5):
    clause=[f'-H{i}petH',f'H{i+1}cigDu', f'H{i-1}cigDu']
    clauses.append(clause)
    
clause=[f'-H1petH',f'H2cigDu']
clauses.append(clause)
clause=[f'-H5petH',f'H4cigDu']
clauses.append(clause)


# The Norwegian lives next to the blue house
for i in range(2,5):
    clause=[f'-H{i}colB',f'H{i+1}naN', f'H{i-1}naN']
    clauses.append(clause)
    
clause=[f'-H1colB',f'H2naN']
clauses.append(clause)
clause=[f'-H5colB',f'H4naN']
clauses.append(clause)


# The man who smokes Blends has a neighbor who drinks water
for i in range(2,5):
    clause=[f'-H{i}bevWa',f'H{i+1}cigBl', f'H{i-1}cigBl']
    clauses.append(clause)
    
clause=[f'-H1bevWa',f'H2cigBl']
clauses.append(clause)
clause=[f'-H5bevWa',f'H4cigBl']
clauses.append(clause)

        
# The man living in the center house drinks milk
clause=['H3bevM']
clauses.append(clause)

# The Norwegian lives in the first house.
clause=['H1naN']
clauses.append(clause)

def convert_to_int(cl):
    cl_int=[]
    for c in cl:
        if(c.startswith("-")):
            c=c.replace('-','')
            var_int=-variable_number[c]
            cl_int.append(var_int)
        else:
            var_int=variable_number[c]
            cl_int.append(var_int)
    return cl_int
            
# print(convert_to_int(cl))
clauses_int=[]
for claw in clauses:
    l=convert_to_int(claw)
    clauses_int.append(l)


def unit_clauses(clauses):
    single_clauses=[]
    for cl in clauses:
        if(len(cl)==1):
            single_clauses.append(cl[0])
#     print('UCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC', unit_clauses)
    return single_clauses

def unit_propagation(clauses, UC):
    C=[]
#     print('ssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss')
    for cl in clauses:
        C_=[]
        flag=False
        for li in cl:
            if li in UC:
                flag=True
                break
            if -li in UC:
                continue
            C_.append(li)
        if flag==False:
            C.append(C_)
#             print('cycle',(clause,C_))
    return C


def DPLL_procedure(clauses, assignment):
    if not clauses:
        return True
    if any(len(clause) == 0 for clause in clauses):
        return False

    # Unit Propagation
    unit_clauses_list = unit_clauses(clauses)
    for unit in unit_clauses_list:
        if(-unit in unit_clauses_list):
            return False
    if unit_clauses_list:
        new_list = unit_propagation(clauses, unit_clauses_list)
        for unit in unit_clauses_list:
            assignment[abs(unit)] = unit > 0
#         print('ass3', assignment)
        return DPLL_procedure(new_list, assignment)

    #take out the first literal from clauses
    literal = abs(clauses[0][0])
    assignment1 = deepcopy(assignment)

    # set the first literal to true
#     print('fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff')
    assignment1[literal] = True
    new_list = unit_propagation(clauses, [literal])
    if DPLL_procedure(new_list, assignment1):
        assignment.update(assignment1)
#         print('ass1', assignment)
        return True

    # if the first do not satisfy, set the literal to false
#     print('secsecsecsecsecsecsecsecsecsecsecsecsecsecsecsecsecsecsecsecsecsecsecsecsecsecsecsecsec')
    assignment1 = deepcopy(assignment)
    assignment1[literal] = False
    new_list = unit_propagation(clauses, [-literal])
    if DPLL_procedure(new_list, assignment1):
        assignment.update(assignment1)
#         print('ass2', assignment)
        return True

    return False
if __name__ == "__main__":
    assignment = {}
    result = DPLL_procedure(clauses_int, assignment)
    print("Is satisfiable:", result)
    print("Assignment:", assignment)
    l={k:v for (k,v) in assignment.items() if v==True}
    disct=[k for (k,v) in variable_number.items() if v in l.keys()]
    print('Lierals:',disct)
