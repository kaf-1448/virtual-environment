import importlib


def main() -> None:
    packages = {
        "pandas": "Data manipulation ready",
        "numpy": "Numerical computation ready",
        "matplotlib": "Network access ready",
        "requests": "Visualization ready"
    }

    for package, descreption in packages.items():
        try:
            module = importlib.import_module(package)
            print(f"[OK] {package} ({module.__version__}) - {descreption}")
        except (ImportError, ModuleNotFoundError):
            print(f"[Error] {package} not dowload")


if __name__ == "__main__":
    main()
