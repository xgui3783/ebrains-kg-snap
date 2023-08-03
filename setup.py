from setuptools import setup, find_packages

setup(
    name="ebrains-kg-snap",
    version="0.0.1",
    author="Xiao Gui",
    author_email="xgui3783@gmail.com",
    description="Sync local directory to ebrains dataproxy",
    packages=find_packages(include=["ebrains_kg_snap"]),
    python_requires=">=3.7",
    install_requires=[
        "requests",
    ]
)
