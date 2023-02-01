#
# spec file for package python-pytest-lazy-fixture
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-pytest-lazy-fixture
Version:        0.6.3
Release:        0
Summary:        Helper to use fixtures in pytest.markparametrize
License:        MIT
URL:            https://github.com/tvorog/pytest-lazy-fixture
Source:         https://files.pythonhosted.org/packages/source/p/pytest-lazy-fixture/pytest-lazy-fixture-%{version}.tar.gz
BuildRequires:  %{python_module pytest >= 3.2.5}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pytest >= 3.2.5
BuildArch:      noarch
%python_subpackages

%description
Helper to use fixtures in pytest.mark.parametrize.

%prep
%setup -q -n pytest-lazy-fixture-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/*

%changelog
