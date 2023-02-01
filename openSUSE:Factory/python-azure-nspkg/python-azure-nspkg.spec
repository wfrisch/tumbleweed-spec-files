#
# spec file for package python-azure-nspkg
#
# Copyright (c) 2021 SUSE LLC
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
%if 0%{?suse_version} >= 1500
%define skip_python2 1
%endif
Name:           python-azure-nspkg
Version:        3.0.2
Release:        0
Summary:        Microsoft Azure namespace package
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/Azure/azure-sdk-for-python
Source:         https://files.pythonhosted.org/packages/source/a/azure-nspkg/azure-nspkg-%{version}.zip
Source1:        LICENSE.txt
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Conflicts:      python-azure-sdk <= 2.0.0

BuildArch:      noarch

%python_subpackages

%description
This is the Microsoft Azure namespace package.

This package is not intended to be installed directly by the end user.

It provides the necessary files for other packages to extend the azure namespace.

%prep
%setup -q -n azure-nspkg-%{version}

%build
install -m 644 %{SOURCE1} %{_builddir}/azure-nspkg-%{version}
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_expand mkdir -p %{buildroot}%{$python_sitelib}/azure

%files %{python_files}
%defattr(-,root,root,-)
%doc README.rst
%license LICENSE.txt
%dir %{python_sitelib}/azure
%python2_only %{python_sitelib}/azure
%{python_sitelib}/azure_nspkg-*.egg-info

%changelog