#Tipo de texto: str
#Tipos numericos: int, float, complex
#Tipos sequanciais: list, tuple, range
#Tipos mapping: dict
#Setar tipos de dados: set, frozenset
#Tipo boleano: bool
#Tipo binario: bytes, bytearray, memoryview
#Sem tipo: NoneType

#Exemplos
xStr = "Hello World"
xInt = 20
xFloatw = 20.5
xComplex = 1j
xList = ["apple", "banana", "cherry"]
xTuple = ("apple", "banana", "cherry")
xRange = range(6)
xDict = {"name" : "John", "age" : 36}
xSet = {"apple", "banana", "cherry"}
xFrozenSet = frozenset({"apple", "banana", "cherry"})
xBool = True
xBytes = b"Hello"
xByteArray = bytearray(5)
xMemoryview = memoryview(bytes(5))
xNone = None

#Se quisermos previamente setar os tipos de dados:
x = str("Hello World")
x = int(20)
x = float(20.5)	
x = complex(1j)	
x = list(("apple", "banana", "cherry"))		
x = tuple(("apple", "banana", "cherry"))		
x = range(6)		
x = dict(name="John", age=36)		
x = set(("apple", "banana", "cherry"))	
x = frozenset(("apple", "banana", "cherry"))	
x = bool(5)	
x = bytes(5)	
x = bytearray(5)		
x = memoryview(bytes(5))
