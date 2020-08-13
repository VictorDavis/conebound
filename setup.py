from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="conebound",
    version="1.0.0",
    description="Tools related to bounding cones.",
    license="MIT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    py_modules=["conebound"],
    author="Victor Davis",
    author_email="vadsql@gmail.com",
    url="https://github.com/VictorDavis/conebound",
    install_requires=["numpy", "scipy"],
    python_requires=">=3.5",
)
