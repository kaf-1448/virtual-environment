import importlib


def main() -> None:
    try:

        print("\nLOADING STATUS: Loading programs...\n")

        packages = {
            "pandas": "Data manipulation ready",
            "numpy": "Numerical computation ready",
            "matplotlib": "Visualization ready",
            "requests": "Network access ready"
        }

        modules = {}

        for package, descreption in packages.items():
            try:
                module = importlib.import_module(package)
                modules[package] = module
                print(f"[OK] {package} ({module.__version__}) - {descreption}")
            except ImportError:
                print(f"[Error] {package} not installed")
                print("use this:")
                print("pip install -r requirements.txt")
                print("or use:")
                print("poetry install")
                print("poetry run python loading.py")

        print("\nAnalyzing Matrix data...")
        random_nums = modules["numpy"].random.randint(1, 101, size=1000)

        print("Processing 1000 data points...")
        md = modules["pandas"].DataFrame(
            random_nums, columns=['Matrix_Data'])

        print("Generating visualization...")

        plt = importlib.import_module("matplotlib.pyplot")
        plt.plot(md['Matrix_Data'])
        plt.title("Matrix Numbers")
        plt.savefig("matrix_analysis.png")
        plt.close()

        print("\nAnalysis complete!")
        print("Results saved to: matrix_analysis.png")

    except KeyError as e:
        print(e)


if __name__ == "__main__":
    main()
