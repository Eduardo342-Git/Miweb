from pathlib import Path

from pruebas import Calculator


def test_suma_2_numbers():
    assert Calculator().sumar(2, 2) == 4


def test_resta_2_numbers():
    assert Calculator().resta(5, 3) == 2


def test_ticket1_assets_exist():
    base_dir = Path(__file__).parent
    assert (base_dir / "style.css").exists()
    assert (base_dir / "index.html").exists()
    assert (base_dir / "app.js").exists()


def test_ticket1_feature_flag_is_off_by_default():
    base_dir = Path(__file__).parent
    app_js_content = (base_dir / "app.js").read_text(encoding="utf-8")
    assert 'getValue("dark_mode_enabled", false)' in app_js_content
