"""
modulator
=========

The `modulator` module provides functionality for creating a Python project structure with namespaces,
modules, submodules, classes, functions, and class methods, all organized according to the user's specifications.

This is a part of the PHOTON platform and aims to streamline the process of setting up and managing Python
projects, following standardized patterns and practices. It generates code for these elements from Jinja templates,
allowing for easy customization of the output.

Functions included:
-------------------
- create_namespace: Sets up a namespace directory under 'src', named according to user input.
- create_module: Sets up a new module under a given namespace with necessary files like '__init__.py', '__main__.py',
  'app.py' and '{module_name}.py'.
- create_class: Generates a new class in the specified module.
- create_submodule: Sets up a new submodule under a given module with '__init__.py' and '{submodule_name}.py' files.
- create_module_function: Adds a new function to the existing '{module_name}.py' file in a module.
- create_class_method: Adds a new method to the existing '{class_name}.py' file in a module.

PHOTON platform
---------------
Author: phiarchitect
Maintainer: PHOTON platform
Email: github@phiarchitect.com
Version: 0.1.0
Licence: MIT
"""

from pathlib import Path
from jinja2 import Environment, FileSystemLoader


def create_namespace(namespace_name: str) -> None:
    src_dir = Path("src")
    namespace_dir = src_dir / namespace_name.replace(" ", "_").replace("-", "_")
    namespace_dir.mkdir(parents=True, exist_ok=True)


def create_module(namespace_name: str, module_name: str) -> None:
    src_dir = Path("src")
    namespace_dir = src_dir / namespace_name.replace(" ", "_").replace("-", "_")
    module_dir = namespace_dir / module_name.replace(" ", "_").replace("-", "_")
    module_dir.mkdir(parents=True, exist_ok=True)

    env = Environment(loader=FileSystemLoader("templates/"))
    init_template = env.get_template("__init__.py")
    with (module_dir / "__init__.py").open("w") as f:
        f.write(init_template.render(module_name=module_name, author="phiarchitect"))

    main_template = env.get_template("__main__.py")
    with (module_dir / "__main__.py").open("w") as f:
        f.write(main_template.render())

    app_template = env.get_template("app.py")
    with (module_dir / "app.py").open("w") as f:
        f.write(app_template.render())

    module_template = env.get_template("{module_name}.py")
    with (module_dir / f"{module_name}.py").open("w") as f:
        f.write(module_template.render(module_name=module_name))


def create_class(namespace_name: str, module_name: str, class_name: str) -> None:
    src_dir = Path("src")
    namespace_dir = src_dir / namespace_name.replace(" ", "_").replace("-", "_")
    module_dir = namespace_dir / module_name.replace(" ", "_").replace("-", "_")
    class_file = module_dir / f"{class_name}.py"

    env = Environment(loader=FileSystemLoader("templates/"))
    class_template = env.get_template("{class_name}.py")
    with class_file.open("w") as f:
        f.write(class_template.render(class_name=class_name))


def create_submodule(
    namespace_name: str, module_name: str, submodule_name: str
) -> None:
    src_dir = Path("src")
    namespace_dir = src_dir / namespace_name.replace(" ", "_").replace("-", "_")
    module_dir = namespace_dir / module_name.replace(" ", "_").replace("-", "_")
    submodule_dir = module_dir / submodule_name.replace(" ", "_").replace("-", "_")
    submodule_dir.mkdir(parents=True, exist_ok=True)

    env = Environment(loader=FileSystemLoader("templates/"))
    init_template = env.get_template("__init__.py")
    with (submodule_dir / "__init__.py").open("w") as f:
        f.write(init_template.render(module_name=submodule_name, author="phiarchitect"))

    submodule_template = env.get_template("{module_name}.py")
    with (submodule_dir / f"{submodule_name}.py").open("w") as f:
        f.write(submodule_template.render(module_name=submodule_name))


def create_module_function(
    namespace_name: str,
    module_name: str,
    function_name: str,
    args: str,
    return_type: str,
) -> None:
    src_dir = Path("src")
    namespace_dir = src_dir / namespace_name.replace(" ", "_").replace("-", "_")
    module_dir = namespace_dir / module_name.replace(" ", "_").replace("-", "_")
    function_file = module_dir / f"{module_name}.py"

    env = Environment(loader=FileSystemLoader("templates/"))
    function_template = env.get_template("function.py")
    with function_file.open("a") as f:
        f.write(
            function_template.render(
                function_name=function_name, args=args, return_type=return_type
            )
        )


def create_class_method(
    namespace_name: str,
    module_name: str,
    class_name: str,
    method_name: str,
    args: str,
    return_type: str,
) -> None:
    src_dir = Path("src")
    namespace_dir = src_dir / namespace_name.replace(" ", "_").replace("-", "_")
    module_dir = namespace_dir / module_name.replace(" ", "_").replace("-", "_")
    class_file = module_dir / f"{class_name}.py"

    env = Environment(loader=FileSystemLoader("templates/"))
    method_template = env.get_template("method.py")
    with class_file.open("a") as f:
        f.write(
            method_template.render(
                method_name=method_name, args=args, return_type=return_type
            )
        )
