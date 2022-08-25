from typing import Union, Tuple, List, Dict, Any
a: int = 5
b: float = 10
c: str = "Hello"
d: bool = True

def s(a:int, b:float) -> float:
    return a + b

def main():
    print(s(a, b))

if __name__ == '__main__':
    main()

list : List[int] = [1, 2, 3, 4, 5]
users: Dict[str, str] = {
    "name": "John",
    "lastname": "Doe"
}

coordinates: List[Dict[str,Tuple[int,int]]]
coordinates = [
    {
        "x": (1,2),
        "y": (2,5)
    }]
