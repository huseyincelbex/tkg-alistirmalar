# Lab, Bölüm 2: Testleri bu dosyaya SİZ yazacaksınız.
#
# Aşağıda örnek olarak bir test var. Yanına her fonksiyon için kendi testlerinizi ekleyin.
# Çalıştırmak için bu klasörde:  python -m pytest test_bolum2.py test_hatali_surumler.py -v

import pytest

from bolum2 import sifre_gucu, otopark_ucreti, yuzde_degisim


def test_kisa_sifre_zayif():
    assert sifre_gucu("abc") == "zayıf"


@pytest.mark.parametrize(
    ("sifre", "beklenen"),
    [
        ("1234567", "zayıf"),
        ("12345678", "orta"),
        ("12345678901", "orta"),
        ("123456789012", "güçlü"),
    ],
)
def test_sifre_gucu_sinirlar(sifre, beklenen):
    assert sifre_gucu(sifre) == beklenen


def test_bos_sifre_hata_verir():
    with pytest.raises(ValueError):
        sifre_gucu("")


@pytest.mark.parametrize(
    ("dakika", "beklenen"),
    [
        (0, 0),
        (15, 0),
        (16, 20),
        (60, 20),
        (61, 40),
        (180, 40),
        (181, 60),
    ],
)
def test_otopark_ucreti_sinirlar(dakika, beklenen):
    assert otopark_ucreti(dakika) == beklenen


def test_negatif_otopark_suresi_hata_verir():
    with pytest.raises(ValueError):
        otopark_ucreti(-1)


def test_yuzde_degisim_artis_ve_azalis():
    assert yuzde_degisim(200, 250) == 25.0
    assert yuzde_degisim(200, 150) == -25.0


def test_eski_deger_sifirsa_yuzde_degisim_hata_verir():
    with pytest.raises(ValueError):
        yuzde_degisim(0, 100)
