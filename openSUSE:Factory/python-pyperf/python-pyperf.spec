#
# spec file for package python-pyperf
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
%define skip_python2 1
Name:           python-pyperf
Version:        2.5.0
Release:        0
Summary:        Python module to run and analyze benchmarks
License:        MIT
URL:            https://github.com/vstinner/pyperf
Source:         https://files.pythonhosted.org/packages/source/p/pyperf/pyperf-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun):update-alternatives
Recommends:     python-psutil
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module psutil}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
Python module to run and analyze benchmarks.

%prep
%setup -q -n pyperf-%{version}

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/pyperf
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%post
%python_install_alternative pyperf

%postun
%python_uninstall_alternative pyperf

%files %{python_files}
%doc README.rst
%license COPYING
%python_alternative %{_bindir}/pyperf
%{python_sitelib}/*

%changelog
