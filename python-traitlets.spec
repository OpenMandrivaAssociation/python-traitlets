%global srcname traitlets
%global srcversion 5.0.5

Name:           python-%srcname
Version:        5.0.5
Release:        2
Summary:        A lightweight derivative of Enthought Traits for configuring Python objects
Group:          Development/Python
License:        BSD
URL:            https://github.com/ipython/traitlets
Source0:	https://github.com/ipython/traitlets/archive/%{version}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:	python-setuptools
BuildRequires:	python-devel

%description
A lightweight pure-Python derivative of Enthought Traits, used for
configuring Python objects.

This package powers the config system of IPython and Jupyter.

%prep
%setup -q -n %{srcname}-%{srcversion}

%autopatch -p1

%build
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%files
%doc README.md CONTRIBUTING.md COPYING.md
%{python_sitelib}/*.egg-info
%{python_sitelib}/%srcname
