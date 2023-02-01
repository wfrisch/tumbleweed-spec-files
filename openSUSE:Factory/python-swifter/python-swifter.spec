#
# spec file for package python-swifter
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


%{?!python_module:%define python_module() python3-%{**}}
%define         skip_python2 1
Name:           python-swifter
Version:        1.1.2
Release:        0
Summary:        Tool to speed up pandas calculations
License:        MIT
URL:            https://github.com/jmcarpenter2/swifter
Source:         https://github.com/jmcarpenter2/swifter/archive/%{version}.tar.gz#/swifter-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-bleach >= 3.1.1
Requires:       python-cloudpickle >= 0.2.2
Requires:       python-dask-dataframe >= 2.10.0
Requires:       python-ipywidgets >= 7.0.0
Requires:       python-pandas >= 1.0
Requires:       python-parso > 0.4
Requires:       python-psutil >= 5.6.6
Requires:       python-tqdm >= 4.33.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module bleach >= 3.1.1}
BuildRequires:  %{python_module cloudpickle >= 0.2.2}
BuildRequires:  %{python_module dask-dataframe >= 2.10.0}
BuildRequires:  %{python_module ipywidgets >= 7.0.0}
BuildRequires:  %{python_module pandas >= 1.0}
BuildRequires:  %{python_module parso > 0.4}
BuildRequires:  %{python_module psutil >= 5.6.6}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module tqdm >= 4.33.0}
# /SECTION
%python_subpackages

%description
A package which efficiently applies any function to a
pandas dataframe or series in the fastest available manner

%prep
%setup -q -n swifter-%{version}
# https://github.com/jmcarpenter2/swifter/commit/bc754088feb97f883794585a7eeb8cb5914e1d4b
sed -i 's/{VERSION}/%{version}/' setup.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# we fail the speedtests on the build service machines. Disable that portion of the tests
sed -i 's/if self.ncores > 1:  # speed test/if False: # no speed test/' swifter/swifter_tests.py
%pytest -n auto swifter/swifter_tests.py

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/swifter
%{python_sitelib}/swifter-%{version}*-info

%changelog
