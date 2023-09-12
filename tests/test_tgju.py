from tgju import __version__


def test_version():
    assert __version__ == "0.1.0"


main_func = __import__("./tgju/main.py")

main_func.getdata
