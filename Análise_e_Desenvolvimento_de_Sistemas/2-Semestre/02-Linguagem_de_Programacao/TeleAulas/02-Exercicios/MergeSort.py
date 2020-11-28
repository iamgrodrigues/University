def mergeSort(list):
    print("Divisão ",list)
    if len(list)>1:
        meio = len(list)//2
        esqmet = list[:meio]
        dirmet = list[meio:]

        mergeSort(esqmet)
        mergeSort(dirmet)

        i=0
        j=0
        k=0
        while i < len(esqmet) and j < len(dirmet):
            if esqmet[i] < dirmet[j]:
                list[k]=esqmet[i]
                i=i+1
            else:
                list[k]=dirmet[j]
                j=j+1
            k=k+1

        while i < len(esqmet):
            list[k]=esqmet[i]
            i=i+1
            k=k+1

        while j < len(dirmet):
            list[k]=dirmet[j]
            j=j+1
            k=k+1
    print("Merging ",list)

lista = [54,26,93,17,77,31,44,55,20]
mergeSort(lista)
print(lista)
