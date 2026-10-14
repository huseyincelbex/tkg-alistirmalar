import pytest
from alistirma import ortalama  
def test_ortalama():
  
    assert ortalama([10, 20, 30]) == 20.0
    
    # Ondalıklı sonuç veren bir liste için test
    assert ortalama([1, 2, 3, 4]) == 2.5
    
    # Tek elemanlı liste için test
    assert ortalama([5]) == 5.0
