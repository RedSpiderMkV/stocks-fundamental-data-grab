from setuptools import setup, find_packages


setup(
    name="fundamental-data-grab",
    version="1.0",
    packages=["fundamental_data_grab"],
    install_requires=[
        "yfinance==0.1.55",
        "spyder-kernels==1.10.0",
        "numpy==1.19.4",
        "pandas==1.1.4",
        "cython"]
)
