from typing import Tuple, List, Set, Dict

"""Type annotations for variables
   are not generally necessary"""
a: int = 100
b: str = "Hello"
c: bool = True
f: float = 1.0


#Function:

def add(a: int, b: int)-> int:
    return a + b

#Tuple:

t: Tuple[int, bool] = (1, True)

def swap(a: int, b: int) -> Tuple[int, int]:
    return (a, b)


#List:

l: List[int] = [1, 2, 3]

def take_half(s: List[int]) -> List[int]:
    return s[:len(s)//2]

#Set:

s: Set[int] = {2, 4, 6}

def dedupe(s: List[int]) -> Set[int]:
    return set(s)

#Dictionary

d: Dict[str, int] = {'foo' : 10, 'bar' : 20}

def zip_pair(k: Tuple[str, str],
             v: Tuple[int, int]) -> Dict[str, int]:
    return dict([(k[0], v[0]), (k[1], v[1])])
