import importlib


def main() -> None:

    print("\nLOADING STATUS: Loading programs...\n")

    packages = {
        "pandas": "Data manipulation ready",
        "numpy": "Numerical computation ready",
        "matplotlib": "Visualization ready",
        "requests": "Network access ready"
    }

    for package, descreption in packages.items():
        try:
            module = importlib.import_module(package)
            print(f"[OK] {package} ({module.__version__}) - {descreption}")
        except ImportError:
            print(f"[Error] {package} not installed")
            print("use this:")
            print("pip install -r requirements.txt")
            print("or use:")
            print("poetry install")
            print("poetry run python loading.py")

    print("Analyzing Matrix data...")
    print("Processing 1000 data points...")
    print("Generating visualization...")


if __name__ == "__main__":
    main()
