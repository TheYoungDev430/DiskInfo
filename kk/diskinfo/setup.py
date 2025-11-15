from setuptools import setup

setup(
    name="diskinfo",
    version="1.0.0",
    packages=["diskinfo"],
    install_requires=[
        "wmi; platform_system=='Windows'"
    ],
    description="Cross-platform library to fetch SSD/HDD details and SMART health",
    author="Your Name",
    license="MIT",
    python_requires=">=3.7",
)