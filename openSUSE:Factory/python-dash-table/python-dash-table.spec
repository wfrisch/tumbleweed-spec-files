#
# spec file for package python-dash-table
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


Name:           python-dash-table
Version:        5.0.0
Release:        0
Summary:        Dash table
License:        MIT
URL:            https://github.com/plotly/dash-table
Source:         https://files.pythonhosted.org/packages/source/d/dash-table/dash_table-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
An interactive DataTable for Dash.

As of Dash 2, the development of dash-table has been moved to the main Dash repo

This package exists for backward compatibility as Dash still lists it as requirement. It
has no further functionality than displaying a deprecation message.

%prep
%setup -q -n dash_table-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/dash_table/
%{python_sitelib}/dash_table-%{version}*-info

%changelog
