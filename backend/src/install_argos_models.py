"""
install_argos_models.py

Install all Argos Translate models needed for your app.
This avoids CLI issues on Windows and uses Argos' official Python API.
"""

from argostranslate import package as argos_package
from argostranslate import translate as argos_translate


LANG_PAIRS = [
    ("en", "es"),
    ("es", "en"),
    ("en", "fr"),
    ("fr", "en"),
    ("en", "de"),
    ("de", "en"),
    ("en", "it"),
    ("it", "en"),
]


def install_pair(from_code: str, to_code: str) -> None:
    print(f"\n=== Installing {from_code} -> {to_code} ===")
    argos_package.update_package_index()
    available = argos_package.get_available_packages()

    for p in available:
        if p.from_code == from_code and p.to_code == to_code:
            print("Found package:", p.get_description())
            path = p.download()
            print("Downloaded to:", path)
            argos_package.install_from_path(path)
            print(f"SUCCESS: Installed {from_code} -> {to_code}")
            return

    print(f"ERROR: Could not find {from_code} -> {to_code} in package index!")


if __name__ == "__main__":
    print("Installing ALL language pairs...")

    for src, tgt in LANG_PAIRS:
        install_pair(src, tgt)

    print("\nVerifying installed languages:")
    langs = argos_translate.get_installed_languages()
    for lang in langs:
        print(f" - {lang.code}: {lang.name}")

    print("\nDONE.")
