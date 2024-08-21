print("//////////MEDIA MOBILE//////////\n\n\n")

def medmob(num, n):
    medmob = []
    
    for i in range(1, len(num) + 1):
        window = num[max(0, i -n):i]
        med = sum(window) / len(window)
        medmob.append(med)
        
    return medmob

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = 3 
output = medmob(num, n)
print("La media mobile dei numeri da 1 a 10 e':\n" )
print(output)



