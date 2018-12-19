import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python-password",
    version="0.1.0",
    author="Jaaromy Zierse",
    author_email="",
    description="Secure password implementation using passlib and TinyDB",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jaaromy/python-password.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["passlib", "argon2_cffi", "tinydb"]
)
