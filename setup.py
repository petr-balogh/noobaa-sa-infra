import os
# If you see error: cannot import name find_namespace_packages
# Please update your setuptools:
# pip install -U setuptools
from setuptools import setup, find_namespace_packages

def find_folders_with_yaml_files(path):
    config_dirs = {}
    yaml_folders = set()
    for root, dirs, files in os.walk(path):
        if any(file.endswith('.yaml') for file in files):
            folder_path = os.path.relpath(root)
            yaml_folders.add(folder_path)
    for folder in yaml_folders:
        config_dirs[folder.replace(os.path.sep, '.')] = ["*.yaml"]
    return config_dirs

setup(
    name="noobaa-sa-common",
    version="0.1",
    packages=find_namespace_packages(),
    include_package_data=True,
    package_data=find_folders_with_yaml_files("noobaa_sa_common/config"),
    url="",
    license="MIT",
    author="Noobaa SA QE",
    author_email="ocs-ci@redhat.com",
    description=(
        "Noobaa Standalone(SA) Common contains commonly used functions."
    ),
    install_requires=[
        "jinja2",
        "pyyaml",
        "requests",
    ],
)
