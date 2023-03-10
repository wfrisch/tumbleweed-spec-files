#
# spec file for package python-pywbem
#
# Copyright (c) 2020 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%{?!python_module:%define python_module() python3-%{**}}
%define skip_python2 1
# cythonized pywbem produces yacc parser errors
%bcond_with cythonize
Name:           python-pywbem
Version:        1.4.1
Release:        0
Summary:        Python module for making CIM operation calls using the WBEM protocol
License:        LGPL-2.1-or-later
Group:          System/Management
URL:            https://pywbem.github.io/
Source0:        https://github.com/pywbem/pywbem/archive/%{version}.tar.gz#/pywbem-%{version}.tar.gz
BuildRequires:  %{python_module FormEncode >= 2.0.0}
BuildRequires:  %{python_module PyYAML > 5.3.1}
BuildRequires:  %{python_module httpretty}
BuildRequires:  %{python_module lxml >= 4.6.4}
BuildRequires:  %{python_module nocasedict >= 1.0.1}
BuildRequires:  %{python_module nocaselist >= 1.0.3}
BuildRequires:  %{python_module ply >= 3.10}
BuildRequires:  %{python_module pytest >= 6.2.5}
BuildRequires:  %{python_module pytz}
BuildRequires:  %{python_module requests >= 2.25.0}
BuildRequires:  %{python_module requests-mock}
BuildRequires:  %{python_module setuptools >= 38.4.1}
BuildRequires:  %{python_module six >= 1.16.0}
BuildRequires:  %{python_module testfixtures}
BuildRequires:  %{python_module urllib3 >= 1.26.5}
BuildRequires:  %{python_module yamlloader >= 0.5.5}
BuildRequires:  %{python_module wheel}
BuildRequires:  %{python_module pip}
%if %{with cythonize}
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module devel}
%else
BuildArch:      noarch
%endif
BuildRequires:  fdupes
BuildRequires:  libxml2-tools
BuildRequires:  python-rpm-macros
Requires:       python-PyYAML >= 5.3.1
Requires:       python-nocasedict >= 1.0.1
Requires:       python-nocaselist >= 1.0.3
Requires:       python-ply >= 3.10
Requires:       python-requests >= 2.25.0
Requires:       python-six >= 1.16.0
Requires:       python-urllib3 >= 1.26.5
Requires:       python-yamlloader >= 0.5.5
Requires(post): update-alternatives
Requires(postun): update-alternatives
Recommends:     python-pywebmtools
%python_subpackages

%description
PyWBEM is a Python module for making CIM operation calls using the WBEM
protocol to query and update managed objects.

%prep
%setup -q -n pywbem-%{version}
%autopatch -p1

%build
%if %{with cythonize}
%{python_expand # build cythonized wheel
$python setup.py bdist_wheel --cythonized
mv dist/pywbem-%{version}-cp%{$python_version_nodots}*.whl build/
}
%else
# build one noarch wheel for all flavor installs
python3 setup.py bdist_wheel
mv dist/pywbem-%{version}-*py3-none-any.whl .
%endif

%install
%pyproject_install
%fdupes %{buildroot}
rm %{buildroot}%{_bindir}/*.bat
%python_clone -a %{buildroot}%{_bindir}/mof_compiler

%check
%{pytest -W default -W ignore::PendingDeprecationWarning -W ignore::ResourceWarning \
         tests/unittest tests/functiontest}

%post
%python_install_alternative mof_compiler

%postun
%python_uninstall_alternative mof_compiler

%files %{python_files}
%doc README.rst
%license LICENSE.txt
%python_alternative %{_bindir}/mof_compiler
%if %{with cythonize}
%{python_sitearch}/pywbem
%{python_sitearch}/pywbem_mock
%{python_sitearch}/pywbem-%{version}*-info
%else
%{python_sitelib}/pywbem
%{python_sitelib}/pywbem_mock
%{python_sitelib}/pywbem-%{version}*-info
%endif

%changelog
