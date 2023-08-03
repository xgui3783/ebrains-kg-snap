from setuptools import setup, find_packages

setup(
    name="ebrains-kg-snap",
    version="0.0.1",
    author="Xiao Gui",
    author_email="xgui3783@gmail.com",
    description="Sync local directory to ebrains dataproxy",
    packages=find_packages(include="ebrains_kg_snap"),
    python_requires=">=3.7",
    install_requires=[
        "requests",

        # waiting for
        # https://github.com/HumanBrainProject/ebrains-drive/pull/22
        # and
        # https://github.com/HumanBrainProject/ebrains-drive/pull/20
        # to merge and release
        # once merged, use ebrains-drive as dependency
        "git+https://github.com/xgui3783/ebrains-drive.git@tmp_fixDeleteUseIO",
    ]
)
