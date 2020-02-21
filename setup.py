import os.path
from setuptools import setup

HERE = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(HERE, "README.md")) as fid:
    README = fid.read()

setup(
    name="jobtracker",
    version="0.1",
    description="Add, modify job applications in a DB",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/kc8/jobtracker",
    author="Kyle Cooper",
    author_email="kyle@cooperkyle.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
    ],
    packages=["reader"],
    include_package_data=True,
    install_requires=[
        "alembic", "sqlalchemy", "click"
    ],
    entry_points={"console_scripts": ["tracker=tracker.__main__:main"]},
)