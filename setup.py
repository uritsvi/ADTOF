import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ADTOF",
    version="2.0",
    # scripts=glob.glob("bin/*"),
    author="Mickael Zehren",
    description="Additional material for the paper 'High-quality and reproducible automatic drum transcription from crowdsourced data'",
    long_description=long_description,
    url="",
    packages=setuptools.find_packages(),
    package_data={"adtof": ["models/*"]},
    install_requires=[
        "cython==3.0.0",
        "numpy==1.23.0",
        "librosa>=0.8.0",
        "tensorflow>=2.13.0",
        "matplotlib>=3.8.1",
        "pandas>=1.2.4",
        "mir_eval>=0.6",
        "madmom",
        "jellyfish",
        "pyunpack>=0.2.2",
        "ffmpeg-python",
        "pretty_midi>=0.2.9",
        "argparse",
        "beautifulsoup4",
        "scikit-learn>=1.3.2",
    ],
    classifiers=["Programming Language :: Python :: 3", "License :: OSI Approved :: GNU General Public License v3 (GPLv3)"],
)
