#
# spec file for package python-cerealizer
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-cerealizer
Version:        0.8.3
Release:        0
Summary:        A secure pickle-like module
License:        Python-2.0
Group:          Development/Libraries/Python
URL:            http://pypi.python.org/pypi/Cerealizer
Source:         https://files.pythonhosted.org/packages/source/C/Cerealizer/Cerealizer-%{version}.tar.gz
Source1:        https://spdx.org/licenses/Python-2.0.txt
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
A secure pickle-like module. It support basic types (int, string, unicode,
tuple, list, dict, set,...), old and new-style classes (you need to register
the class for security), object cycles, and it can be extended to support
C-defined type.

%prep
%setup -q -n Cerealizer-%{version}
cp %{SOURCE1} .

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python test/regtest.py

%files %{python_files}
%doc README.rst
%license Python-2.0.txt
%{python_sitelib}/*

%changelog
