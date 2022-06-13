<div align="center">

<h1><a href="https://www.github.com/ellsphillips/govsic"><img height=30 src="https://latex.codecogs.com/svg.latex?{\textsf{\bfseries\color[RGB]{233,80,14}govsic}}" alt="govsic"></a></h1>

[![CI status](https://github.com/ellsphillips/sic/actions/workflows/config.yml/badge.svg)](https://github.com/ellsphillips/govsic) [![Supported Python versions](https://img.shields.io/pypi/pyversions/govsic.svg)](https://test.pypi.org/project/govsic/) [![PyPI version](https://img.shields.io/pypi/v/govsic.svg)](https://test.pypi.org/project/govsic/) [![License](https://img.shields.io/pypi/l/pyisic.svg)](https://github.com/ellsphillips/govsic/blob/master/LICENSE)

</div>

A lightweight library to parse and interface Standard Industrial Classification instances using the current UK SIC 2007 methodology.

`govsic` supports the UK SIC 2007 framework by unifying the classification of business establishments and other statistical units by their type of economic activity/engagement into a common structure.

## Data

Data used has been transformed using the [Office for National Statistics](https://www.ons.gov.uk/methodology/classificationsandstandards/ukstandardindustrialclassificationofeconomicactivities/uksic2007)' published opensource SIC structure and volume datasets.

## Installation

The `govsic` package is available on PyPI.

```bash
pip install govsic
```

## Usage

`govsic` provides the `SIC` class to represent Standard Industrial Classifications. Get started by initialising a new `SIC` object to interface, compare, and evaluate UK SIC 2007 codes.

See example usage in the `examples/` repo directory

```python
from govsic import SIC

sic = SIC(8110)

print(f"{sic = }")
# sic = [B] 08.11/0

for label, prop in (
    ("Code value", sic.code),
    ("Is valid?", sic.is_valid),
    ("Section", sic.section),
    ("Component", sic.component),
):
    print(f"{label}:\t{prop}")
# Code value:     08110
# Is valid?:      True
# Section:        B
# Component:      CLASS
```
