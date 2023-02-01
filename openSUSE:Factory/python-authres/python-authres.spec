#
# spec file for package python-authres
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
%define skip_python2 1
Name:           python-authres
Version:        1.2.0
Release:        0
Summary:        authres - Authentication Results Header Module
License:        Apache-2.0
URL:            https://launchpad.net/authentication-results-python
Source:         https://files.pythonhosted.org/packages/source/a/authres/authres-%{version}.tar.gz
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
authres - Authentication Results Header Module

%prep
%setup -q -n authres-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# %%pytest macro does not pass on long options
%pytest --doctest-glob=tests

%files %{python_files}
%doc CHANGES README
%license COPYING
%{python_sitelib}/*

%changelog
