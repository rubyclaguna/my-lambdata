from setuptools import find_packages, setup
with open("README.md", "r") as fh:
    long_description = fh.read()
setup(
    name="my-lambdata",
    version="1.1",
    author="rubyclaguna",
    author_email="rubyclaguna@gmail.com",
    description="For example purposes",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    #license="MIT",
    url="https://github.com/rubyclaguna/my-lambdata",
    #keywords="",
    packages=find_packages() # ["my_lambdata"]
)