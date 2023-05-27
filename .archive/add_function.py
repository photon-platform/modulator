from pathlib import Path


def get_module_files(path: Path) -> list[Path]:
    """
    Recursively find all Python module files in the given path.

    Args:
        path (Path): The directory path to search for Python module files.

    Returns:
        list[Path]: A list of Python module file paths.
    """
    module_files = []
    for p in path.glob("**/*.py"):
        if (
            p.name != "__init__.py"
            and p.name != "__main__.py"
            and p.name != "_version.py"
        ):
            module_files.append(p)
    return module_files


def function_name_exists(function_name: str, file_path: Path) -> bool:
    """
    Check if the function name already exists in the given file.

    Args:
        function_name (str): The function name to check for.
        file_path (Path): The path to the file where the function name should be checked.

    Returns:
        bool: True if the function name exists in the file, False otherwise.
    """
    with file_path.open("r") as f:
        content = f.read()

    return f"def {function_name}(" in content


def add_function_to_module() -> None:
    """
    Add a function signature to an existing module in the src directory.
    """
    src_dir = Path("src")
    if not src_dir.exists():
        print("No src directory found.")
        return

    module_files = get_module_files(src_dir)

    if not module_files:
        print("No module files found.")
        return

    print("Select a module to add a function:")
    for i, module_file in enumerate(module_files, start=1):
        print(f"{i}. {module_file}")

    module_choice = int(input("Enter the number of the module: ")) - 1
    module_file = module_files[module_choice]

    function_name = input("Enter the function name: ")

    while function_name_exists(function_name, module_file):
        print(f"Function '{function_name}' already exists in {module_file}.")
        function_name = input("Enter a unique function name: ")

    args = input(
        "Enter the function arguments (comma separated, e.g., arg1: int, arg2: str): "
    )
    return_type = input("Enter the return type (leave blank if None): ")

    # Generate the function docstring with itemized arguments
    args_list = [arg.strip() for arg in args.split(",")]
    docstring_lines = ['"""', f"{function_name} function description."]
    for arg in args_list:
        arg_name, arg_type = [part.strip() for part in arg.split(":")]
        docstring_lines.append(
            f"    {arg_name} ({arg_type}): Description for {arg_name}."
        )
    docstring_lines.append('"""')
    docstring = "\n".join(docstring_lines)

    with module_file.open("a") as f:
        f.write(f"\n{docstring}\n")
        f.write(f"def {function_name}({args})")
        if return_type:
            f.write(f" -> {return_type}")
        f.write(":\n    pass\n")

    print(f"Function '{function_name}' added to {module_file}.")
