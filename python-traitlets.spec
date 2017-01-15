%global srcname traitlets
%global srcversion 4.3.1

Name:           python-%srcname
Version:        4.3.1
Release:        1
Summary:        A lightweight derivative of Enthought Traits for configuring Python objects
Group:          Development/Python
License:        BSD
URL:            https://github.com/ipython/traitlets
Source0:	https://github.com/ipython/traitlets/archive/%{version}.tar.gz#/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:	python-setuptools
BuildRequires:	python-devel

BuildRequires:	python2-setuptools
BuildRequires:	python2-devel

%description
A lightweight pure-Python derivative of Enthought Traits, used for
configuring Python objects.

This package powers the config system of IPython and Jupyter.

%package -n python2-%srcname

%prep
%setup -q -n %{srcname}-%{srcversion}

%apply_patches

cp -a . %py2dir

%build
%{__python} setup.py build

pushd %py2dir
%{__python2} setup.py build

%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

pushd %py2dir
%{__python2} setup.py install -O1 --skip-build --root %{buildroot}

%files
%doc README.md CONTRIBUTING.md COPYING.md
%{python_sitelib}/*.egg-info
%{python_sitelib}/%srcname

%files -n python2-%srcname
%doc README.md CONTRIBUTING.md COPYING.md
%{python2_sitelib}/*.egg-info
%{python2_sitelib}/%srcname
