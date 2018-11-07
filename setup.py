import os
import re
import io

from setuptools import setup, find_packages


def read(*names, **kwargs):
    with io.open(os.path.join(os.path.dirname(__file__), *names)) as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


entry_points = {
    "console_scripts": ["gwf = gwf.cli:main"],
    "gwf.backends": [
        "slurm = gwf.backends.slurm:SlurmBackend",
        "sge = gwf.backends.sge:SGEBackend",
        "local = gwf.backends.local:LocalBackend",
        "testing = gwf.backends.testing:TestingBackend",
    ],
    "gwf.plugins": [
        "run = gwf.plugins.run:run",
        "config = gwf.plugins.config:config",
        "status = gwf.plugins.status:status",
        "info = gwf.plugins.info:info",
        "logs = gwf.plugins.logs:logs",
        "clean = gwf.plugins.clean:clean",
        "workers = gwf.plugins.workers:workers",
        "cancel = gwf.plugins.cancel:cancel",
        "touch = gwf.plugins.touch:touch",
    ],
}


setup(
    name="gwf",
    version=find_version("src", "gwf", "__init__.py"),
    url="http://gwf.readthedocs.io/",
    license="GPLv3",
    author="Thomas Mailund, Dan Søndergaard",
    author_email="mailund@birc.au.dk, das@birc.au.dk",
    description="A flexible, pragmatic workflow tool.",
    long_description=read("README.rst"),
    packages=find_packages("src"),
    package_dir={"": "src"},
    entry_points=entry_points,
    python_requires=">=3.5",
    setup_requires=[],
    install_requires=["click", "click-plugins"],
    test_suite="tests",
    tests_require=["pytest", "pytest-runner", "pytest-click", "pytest-mock"],
    extras_require={':sys_platform == "win32"': ["colorama"]},
    keywords="grid computing workflow",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Operating System :: OS Independent",
        "Topic :: Utilities",
        "Topic :: System :: Distributed Computing",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
