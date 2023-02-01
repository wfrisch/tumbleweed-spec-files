#
# spec file for package python-nocaselist
#
# Copyright (c) 2022 SUSE LLC
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
Name:           python-nocaselist
Version:        1.0.6
Release:        0
Summary:        A case-insensitive list for Python
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/pywbem/nocaselist
Source:         https://files.pythonhosted.org/packages/source/n/nocaselist/nocaselist-%{version}.tar.gz
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Class `NocaseList`_ is a case-insensitive list that preserves the lexical case
of its items.

%prep
%setup -q -n nocaselist-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/nocaselist
%{python_sitelib}/nocaselist-%{version}*info

%changelog
