#
# spec file for package python-flake8-blind-except
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
Name:           python-flake8-blind-except
Version:        0.2.1
Release:        0
Summary:        A flake8 extension that checks for blind except: statements
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/elijahandrews/flake8-blind-except
Source:         https://files.pythonhosted.org/packages/source/f/flake8-blind-except/flake8-blind-except-%{version}.tar.gz
Source1:        LICENSE
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
A flake8 extension that checks for blind except: statements

%prep
%setup -q -n flake8-blind-except-%{version}
cp %{SOURCE1} LICENSE

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/flake8_blind_except.py
%{python_sitelib}/flake8_blind_except-%{version}-py*.egg-info
%pycache_only %{python_sitelib}/__pycache__

%changelog
