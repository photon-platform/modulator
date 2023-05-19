import sys
from pathlib import Path


def create_src_directory():
    src_path = Path("src")
    src_path.mkdir(parents=True, exist_ok=True)


def prompt_user() -> tuple[str, str]:
    """
    Prompt the user for a module name and a short description.

    Returns:
        tuple: A tuple containing the module name (str) and short description (str).
    """
    module_name = input("Enter the module name (use '.' for nested modules): ")
    description = input("Enter a short description for the module: ")
    return module_name, description


def create_module(module_name: str, description: str) -> None:
    """
    Create the module directories and files based on the provided module_name and description.

    Args:
        module_name (str): The module name with optional nested structure (e.g., parent.child).
        description (str): A short description for the module.
    """
    # Split module_name to get nested directories
    module_parts = module_name.split(".")

    # Create the src directory if it doesn't exist
    src_dir = Path("src")
    src_dir.mkdir(exist_ok=True)

    # Create nested directories and __init__.py files
    current_dir = src_dir
    for part in module_parts:
        # TODO: integrate jinja templates
        current_dir = current_dir / part
        current_dir.mkdir(exist_ok=True)
        init_file = current_dir / "__init__.py"
        init_file.touch(exist_ok=True)

        # Add description as docstring
        with init_file.open("w") as f:
            f.write(f'"""{description}"""\n')

    # If root module, create __main__.py and _version.py
    if len(module_parts) == 1:
        main_file = current_dir / "__main__.py"
        main_file.touch(exist_ok=True)
        with main_file.open("w") as f:
            f.write("def main():\n")
            f.write("    pass\n\n")
            f.write("if __name__ == '__main__':\n")
            f.write("    main()\n")

        version_file = current_dir / "_version.py"
        version_file.touch(exist_ok=True)
        with version_file.open("w") as f:
            f.write("VERSION = '0.1.0'\n")


def main() -> None:
    """
    The main function of the script, which prompts the user and creates the module.
    """
    module_name, description = prompt_user()
    create_module(module_name, description)


if __name__ == "__main__":
    main()
