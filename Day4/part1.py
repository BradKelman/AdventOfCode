def passwords():
    password_possibilites = []
    for i in range(171309,643604):
        password = password_boolean(i)
        if password == True:
            password_possibilites.append(i)
    print(password_possibilites)
    return len(password_possibilites)




def password_boolean(i):
    array = [int(d) for d in str(i)]
    if array[0] <= array[1] and array[1] <= array[2] and array[2] <= array[3] and array[3] <= array[4] and array[4] <= array[5]:
        if array[0] == array[1] or array[1] == array[2] or array[2] == array[3] or array[3] == array[4] or array[4] == array[5]:
            return True
        else:
            return False
    else:
         return False


print(passwords())
