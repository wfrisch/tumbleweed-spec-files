#
# spec file for package python-unidiff
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
Name:           python-unidiff
Version:        0.7.4
Release:        0
Summary:        Unified diff parsing/metadata extraction library
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/matiasb/python-unidiff
Source:         https://github.com/matiasb/python-unidiff/archive/v%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun):update-alternatives
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
Python library to parse and interact with unified diff data.

%prep
%setup -q -n python-unidiff-%{version}

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/unidiff
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%post
%python_install_alternative unidiff

%postun
%python_uninstall_alternative unidiff

%files %{python_files}
%doc HISTORY README.rst
%license LICENSE
%python_alternative %{_bindir}/unidiff
%{python_sitelib}/*

%changelog
