from setuptools import setup, find_packages

setup(
    name="glayout",
    version="0.1.0",
    description="A PDK-agnostic layout automation framework for analog circuit design",
    author="OpenFASOC Team",
    author_email="mehdi@umich.edu",
    packages=find_packages(),
    install_requires=[
        "gdsfactory>=6.0.0",
        "numpy>=1.21.0",
        "pandas>=1.3.0",
        "matplotlib>=3.4.0",
        "klayout>=0.28.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=3.0.0",
            "black>=22.0.0",
            "isort>=5.0.0",
            "flake8>=4.0.0",
        ],
        "ml": [
            "torch>=1.10.0",
            "transformers>=4.0.0",
            "scikit-learn>=1.0.0",
        ]
    },
    python_requires=">=3.10",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Electronic Design Automation (EDA)",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
    ],
) 