from setuptools import setup, Extension, find_packages

# Define the C extension
lmcurve_extension = Extension(
    'py_lmcurve_ll5.lmcurve_ll5',  # Fully qualified module name
    sources=['py_lmcurve_ll5/lmcurve_ll5.c']  # Path to the C source file
)

setup(
    name='py_lmcurve_ll5',
    version='0.1.0',
    author='Felix Hammer',
    author_email='fhammer@uos.de',
    python_requires='>=3.6',
    packages=find_packages(),  # Ensure all __init__.py are in place
    ext_modules=[lmcurve_extension],  # Compile the C extension
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: C",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
