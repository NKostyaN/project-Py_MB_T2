from setuptools import setup, find_namespace_packages

setup(
    name="MontyBot",
    version="1",
    description="Personal console assistant",
    url="https://github.com/NKostyaN/project-Py_MB_T2",
    author="Python's Bros",
    license="MIT",
    packages=find_namespace_packages(),
    install_requires=["prompt_toolkit"],
    entry_points={"console_scripts": ["montybot = MontyBot.main:main"]}
    # include_package_data=True,
    # package_data={"": ["*.json"]}
)