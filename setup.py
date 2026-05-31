from setuptools import setup, find_packages

setup(
    name="exodus-balance-emulator-tool",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests>=2.25.1",
        "pyyaml>=5.4.1",
    ],
    entry_points={
        "console_scripts": [
            "exodus-emulator=exodus_balance_emulator_tool.cli:main",
        ],
    },
    python_requires=">=3.8",
)