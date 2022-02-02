
def mergeSort(dizi):
    if len(dizi) > 1:


        ort = len(dizi) // 2


        sol = dizi[:ort]


        sag = dizi[ort:]


        mergeSort(sol)


        mergeSort(sag)

        i = j = k = 0


        while i < len(sol) and j < len(sag):
            if sol[i] < sag[j]:
                dizi[k] = sol[i]
                i += 1
            else:
                dizi[k] = sag[j]
                j += 1
            k += 1


        while i < len(sol):
            dizi[k] = sol[i]
            i += 1
            k += 1

        while j < len(sag):
            dizi[k] = sag[j]
            j += 1
            k += 1





def liste(dizi):
    for i in range(len(dizi)):
        print(dizi[i], end=" ")
    print()



dizi = [16,21,11,8,12,22]
print("Mevcut dizi ", end="\n")
liste(dizi)
mergeSort(dizi)
print("Sorted dizimiz: ", end="\n")
liste(dizi)