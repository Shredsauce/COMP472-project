from setuptools import setup

setup(
    name="MSN-Challenger-Chess-AI",
    version="1.0",
    py_modules=["MiniChessSkeletonCode", "MiniChessExtended"],
    package_dir={"": "src"},
    entry_points={
        "console_scripts": [
            "play=MiniChessExtended:play",
        ]
    },
)
