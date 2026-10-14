def quick_sort(valores):
    
    if len(valores) <= 1:
        return valores

    
    meio = len(valores) // 2
    pivo = valores[meio]

    menores = [x for x in valores if x < pivo]
    iguais = [x for x in valores if x == pivo]
    maiores = [x for x in valores if x > pivo]

    return quick_sort(menores) + iguais + quick_sort(maiores)
