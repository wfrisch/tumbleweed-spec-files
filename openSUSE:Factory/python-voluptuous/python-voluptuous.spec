#
# spec file for package python-voluptuous
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
Name:           python-voluptuous
Version:        0.13.1
Release:        0
Summary:        A Python data validation library
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/alecthomas/voluptuous
Source:         https://github.com/alecthomas/voluptuous/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}-gh.tar.gz
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Voluptuous is a Python data validation library. It validates data
coming into Python as JSON, YAML, etc.

%prep
%setup -q -n voluptuous-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license COPYING
%doc README.md
%{python_sitelib}/*

%changelog
