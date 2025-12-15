%global srcname traitlets

Name:           python-%srcname
Version:        5.14.3
Release:        1
Summary:        A lightweight derivative of Enthought Traits for configuring Python objects
Group:          Development/Python
License:        BSD
URL:            https://github.com/ipython/traitlets
Source0:	https://github.com/ipython/traitlets/releases/download/v%{version}/traitlets-%{version}.tar.gz
BuildArch:      noarch

BuildSystem:	python
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(hatchling)

%description
A lightweight pure-Python derivative of Enthought Traits, used for
configuring Python objects.

This package powers the config system of IPython and Jupyter.

%files
%doc README.md CONTRIBUTING.md
%{python_sitelib}/*.dist-info
%{python_sitelib}/%srcname
