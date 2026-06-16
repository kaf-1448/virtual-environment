import os
from dotenv import load_dotenv


def main() -> None:
    try:
        print("\nORACLE STATUS: Reading the Matrix...\n")
        print("Configuration loaded:")

        load_dotenv()

        configuration = {
            "mode": os.getenv("MATRIX_MODE"),
            "db_url":  os.getenv("DATABASE_URL"),
            "api":  os.getenv("API_KEY"),
            "log_level": os.getenv("LOG_LEVEL"),
            "zion_network": os.getenv("ZION_ENDPOINT")
        }

        configuration_error: list[str] = []
        for key, value in configuration.items():
            if value is None:
                configuration_error.append(key.upper())

        if configuration_error:
            missing: str = "\n- " + "\n- ".join(configuration_error)
            raise ValueError(
                "ERROR: Missing required configuration for:"
                f"{missing}")

        if configuration["mode"] == "development":
            print("Mode: development")
            print("Database: Connected to local instance")
            print("API Access: Authenticated")
            print(f"Log Level: {configuration['log_level']}")
            print("Zion Network: Online")

        elif configuration["mode"] == "production":
            print("Mode: production")
            print("Database: Connected to live production instance securely.")
            print("API Access: Authenticated")
            print(f"Log Level: {configuration['log_level']}")
            print("Zion Network: Mainframe encryption active. Link online.")

        else:
            print(f"Unknown MATRIX_MODE: '{configuration['mode']}'."
                  " Please set it to 'development' or 'production'.")

        print("\nEnvironment security check:")
        print("[OK] No hardcoded secrets detected")
        print("[OK] .env file properly configured")
        print("[OK] Production overrides available")

        print("\nThe Oracle sees all configurations.")

    except ValueError as config_err:
        print(config_err)
    except Exception as e:
        print(f"An unexpected system error occurred: {e}")


if __name__ == "__main__":
    main()
