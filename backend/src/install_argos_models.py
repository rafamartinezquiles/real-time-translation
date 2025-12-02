"""
install_argos_models.py

Small helper script to download and install Argos Translate models
directly from Python (no CLI needed).
"""

from argostranslate import package, translate


def install_pair(from_code: str, to_code: str) -> None:
    print("Updating package index...")
    package.update_package_index()

    print(f"Searching for package {from_code} -> {to_code} ...")
    available_packages = package.get_available_packages()

    for p in available_packages:
        if p.from_code == from_code and p.to_code == to_code:
            print("Found package:", p.get_description())
            package_path = p.download()
            print("Downloaded to:", package_path)
            package.install_from_path(package_path)
            print(f"Successfully installed {from_code} -> {to_code}")
            return

    raise RuntimeError(f"No package found for {from_code} -> {to_code}")


if __name__ == "__main__":
    # Install English -> Spanish
    install_pair("en", "es")

    # If you want Spanish -> English too, uncomment:
    # install_pair("es", "en")

    # Show what is installed (using the *new* API)
    installed_languages = translate.get_installed_languages()
    print("Installed languages:")
    for lang in installed_languages:
        print(" -", lang.code, lang.name)
