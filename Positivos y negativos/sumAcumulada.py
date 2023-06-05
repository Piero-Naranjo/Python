
from typing import List


def sumAcumulada(numeros:List[int]) -> List[int]:
    lista_sumatoria:List[int] = []
    sumatoria = 0
    for n in numeros:
        sumatoria += n
        lista_sumatoria.append(sumatoria)
    return lista_sumatoria

if __name__ == '__main__':
    listado_numeros:list[int] = list(range(1,11))
    print(sumAcumulada(listado_numeros))