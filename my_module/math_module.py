
class MathHelper:
    """
        Most "useful" ヽ(￣～￣　)ノ  math helper
        Just for practicing with packages, pip, pyproject etc.
    """
    
    def plus(self, a: int, b: int) -> int:
        """Plus function

        Args:
            a (int): int num a
            b (int): int num b

        Returns:
            int: a + b
        """
        return a + b

    def minus(self, a: int, b: int) -> int:
        """Minus function

        Args:
            a (int): int num a
            b (int): int num b

        Returns:
            int: a - b
        """
        return a - b
    
    def multiply(self, a: int, b: int) -> int:
        """Multiply function

        Args:
            a (int): int num a
            b (int): int num b

        Returns:
            int: a + b
        """
        return a * b
    
    def division(self, a: int, b: int) -> float:
        """Division function

        Args:
            a (int): int num a
            b (int): int num b

        Returns:
            float: a / b (and 'Error' if b == 0)
        """
        
        return "Error" if b == 0 else a / b
