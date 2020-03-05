import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name                            = "orquestra",
    version                         = "0.0.1",
    author                          = "Zapata Computing, Inc.",
    author_email                    = "info@zapatacomputing.com",
    description                     = "Welcome message to Orquestra.",
    long_description                = long_description,
    long_description_content_type   = "text/markdown",
    url                             = "https://github.com/zapatacomputing/hello-orquestra",
    packages                        = setuptools.find_packages(where = "python"),
    package_dir                     = {
        "" : "python"
    },
    classifiers                     = (
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ),
)
