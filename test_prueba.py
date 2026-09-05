from pruebas import es_par, saludar, sumar


def test_sumar_dos_numeros() -> None:
    assert sumar(2, 3) == 5


def test_es_par_reconoce_numeros_pares() -> None:
    assert es_par(8) is True
    assert es_par(7) is False


def test_saludar_incluye_el_nombre() -> None:
    assert saludar("Ana") == "Hola, Ana!"