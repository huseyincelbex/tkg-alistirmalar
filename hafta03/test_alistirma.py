
import pytest

from alistirma import kargo_ucreti, bilet_fiyati, ortalama


def test_kargo_buyuk_sipariste_ucretsiz():
    assert kargo_ucreti(800) == 0


def test_ortalama_normal():
    assert ortalama([10, 20, 30]) == 20


def test_ortalama_tek_sayi():
    assert ortalama([5]) == 5


def test_ortalama_negatif_sayilar():
    assert ortalama([-10, 0, 10]) == 0
