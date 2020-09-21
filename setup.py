from pathlib import Path
import setuptools

project_dir = Path(__file__).parent

requires = ["playsound==1.2.2", "mutagen>=1.45.1", "pyfiglet>=0.8.post1"]


def setup_package():
    metadata = dict(
        name="jazzit",
        version="0.3.0",
        description="Add unwanted jazz to your scripts",
        long_description=project_dir.joinpath("README.md").read_text(encoding="utf-8"),
        long_description_content_type="text/markdown",
        license="Apache 2.0",
        classifiers=[
            "Environment :: Console",
            "Programming Language :: Python",
            "Intended Audience :: Developers",
        ],
        url="https://github.com/sangarshanan/jazzit",
        author="sangarshanan",
        packages=setuptools.find_packages("src"),
        package_dir={"": "src"},
        install_requires=requires,
        python_requires=">=3.6",
        include_package_data=True,
        package_data={"jazzit": ["tracks/*.mp3"]},
    )

    try:
        from setuptools import setup
    except ImportError:
        from distutils.core import setup

    setup(**metadata)


if __name__ == "__main__":
    setup_package()
