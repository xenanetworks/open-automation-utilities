import setuptools


def main():
    with open("README.md", "r", encoding="utf-8") as fh:
        long_description = fh.read()

    setuptools.setup(
        name="xoa-utils",
        description=(
            "Xena OpenAutomation Utilities provides a shell-like command-line interface for users to do explorative"
            " tests interactively, such as ANLT test."
        ),
        long_description=long_description,
        long_description_content_type="text/markdown",
        author="Ron Ding, Leonard Yu",
        author_email="rdi@xenanetworks.com, hyu@xenanetworks.com",
        maintainer="Xena Networks",
        maintainer_email="support@xenanetworks.com",
        url="https://github.com/xenanetworks/open-automation-utilities",
        packages=setuptools.find_packages(),
        license='Apache 2.0',
        install_requires=["typing_extensions>=4.3.0", "loguru"],
        classifiers=[
            "Development Status :: 4 - Beta",
            "Intended Audience :: Developers",
            "Topic :: Software Development :: Libraries :: Python Modules",
            "License :: OSI Approved :: Apache Software License",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            "Programming Language :: Python :: 3.10",
            "Programming Language :: Python :: 3.11",
        ],
        python_requires=">=3.8",
    )


if __name__ == '__main__':
    main()
