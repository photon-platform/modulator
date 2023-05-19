from pathlib import Path


def add_class_to_module() -> None:
    """
    Add a class definition to an existing module in the src directory.
    """
    src_dir = Path("src")
    if not src_dir.exists():
        print("No src directory found.")
        return

    module_files = get_module_files(src_dir)

    if not module_files:
        print("No module files found.")
        return

    print("Select a module to add a class:")
    for i, module_file in enumerate(module_files, start=1):
        print(f"{i}. {module_file}")

    module_choice = int(input("Enter the number of the module: ")) - 1
    module_file = module_files[module_choice]

    class_name = input("Enter the class name: ")
    inheritance = input("Enter the base class name (leave blank if None): ")

    # Generate the class docstring
    docstring_lines = ['"""', f"{class_name} class description."]
    docstring_lines.append('"""')
    docstring = "\n".join(docstring_lines)

    with module_file.open("a") as f:
        f.write(f"\n{docstring}\n")
        f.write(f"class {class_name}")
        if inheritance:
            f.write(f"({inheritance})")
        f.write(":\n    pass\n")

    print(f"Class '{class_name}' added to {module_file}.")
