#
# spec file for package python-Lektor
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
%bcond_without python2
%define modname Lektor
Name:           python-Lektor
Version:        3.3.7
Release:        0
Summary:        A static content management system
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/lektor/lektor/
Source:         https://files.pythonhosted.org/packages/source/L/%{modname}/%{modname}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM new_version_of_mistune.patch gh#lektor/lektor#944 mcepl@suse.com
# Make package working with mistune 2.*
Patch0:         new_version_of_mistune.patch
BuildRequires:  %{python_module flit-core}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Babel
Requires:       python-ExifRead
Requires:       python-Flask
Requires:       python-Jinja2 >= 2.11
Requires:       python-click >= 6.0
Requires:       python-filetype >= 1.0.7
Requires:       python-inifile
Requires:       python-mistune >= 0.7.0
Requires:       python-python-slugify
Requires:       python-requests
Requires:       python-setuptools
Requires:       python-watchdog
Requires(post): update-alternatives
Requires(postun):update-alternatives
Suggests:       git-core
Suggests:       python-pip
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Babel}
BuildRequires:  %{python_module ExifRead}
BuildRequires:  %{python_module Flask}
BuildRequires:  %{python_module Jinja2 >= 2.11}
BuildRequires:  %{python_module click >= 6.0}
BuildRequires:  %{python_module cryptography >= 1.3.4}
BuildRequires:  %{python_module filetype >= 1.0.7}
BuildRequires:  %{python_module inifile}
BuildRequires:  %{python_module mistune >= 0.7.0}
BuildRequires:  %{python_module pyOpenSSL >= 0.14}
BuildRequires:  %{python_module pylint}
BuildRequires:  %{python_module pytest-click}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-slugify}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module watchdog}
BuildRequires:  git-core
%if %{with python2}
BuildRequires:  python2-functools32
%endif
# /SECTION
%ifpython2
Requires:       python-functools32
%endif
%python_subpackages

%description
A static content management system for building complex websites out
of flat files for people who do not want to make a compromise between
a CMS and a static blog engine.

%prep
%autosetup -p1 -n %{modname}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/lektor
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF8
rm -v tests/test_markdown.py
# Test suite expects a git repo
git init -b master
%pytest -k 'not (requiresinternet or test_resolve_artifact)'

%post
%python_install_alternative lektor

%postun
%python_uninstall_alternative lektor

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/lektor
%{python_sitelib}/*

%changelog
