from my_module.math_module import MathHelper

class TestModule:
    def test_plus(self):
        h = MathHelper()
        assert h.plus(1, 2) == 3
    
    def test_minus(self):
        h = MathHelper()
        assert h.minus(5, 1) == 4
        
    def test_multy(self):
        h = MathHelper()
        assert h.multiply(1, 2) == 2
        
    def test_division(self):
        h = MathHelper()
        assert h.division(10, 2) == 5