# Orquestra Quantum Engine Resource Sample

This respository contains an example resource that shows the structure to be followed by all resource authors.

A resource has ideally two components:
- `templates`: the templates directory contains the Quantum Engine compatible templates to be made available to users.
They ideally inherits from `generic-task` so that the template can be executed on the cloud.
- `src`: the source directory contains your Python files to perform the actual computations you wish to run.
This folder should contain a `setup.py` file that will be called to install your resource as a library to be made
available to resource users.

We encourage you to keep your resources small and independent for ease of debugging and maintance.
