from pyscript import document, display

# Sets 
Grade_7 = {'Pikachu 025', 'Blastoise 024', 'Charmander 023'}
Grade_8 = {'Charizard 022', 'Psyduck 021', 'Eevee 020'}
Grade_9 = {'Yvetal 019', 'Mew 018', 'Vaporeon 017'}
Grade_10 = {'Duskull 016', 'Rayquaza 015', 'Arceus 014'}

def add_members(e):
    first_name = document.getElementById("firstName").value
    last_name = document.getElementById("lastName").value

    # Combines the names into one variable
    fullname = first_name + " " + last_name

    # Combines all the sets into one master set
    Result = Grade_7.union(Grade_8, Grade_9, Grade_10)

    # Adds the fullname to the set
    Final_result = Result | {fullname}


    display(", ".join(Final_result), target="result")
    # .join() removes the brackets and joins all the members
    display("Total members: " + str(len(Final_result)), target="result")