#
# spec file
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2019-2021 Dr. Axel Braun <DocB@opensuse.org>
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
%define skip_python36 1
%define modname beren
Name:           python-%{modname}
Version:        0.7.1
Release:        0
Summary:        Provides a REST client targeted at Orthanc REST API endpoints
License:        GPL-3.0-or-later
URL:            https://github.com/teffalump/beren
Source:         https://files.pythonhosted.org/packages/source/b/%{modname}/%{modname}-%{version}.tar.gz
BuildRequires:  %{python_module apiron}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-apiron

%python_subpackages

%description
python-beren provides a REST client targeted at Orthanc REST API endpoints

%prep
%setup -q -n %{modname}-%{version}
# remove the pinning from the metadata
sed -i 's/apiron==.*$/apiron/' requirements.txt

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

#%%check
# unit tests all test against a live demo server.

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/beren
%{python_sitelib}/beren-%{version}*-info

%changelog
