#
# spec file for package python-PyQRCode
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
%define modname PyQRCode
Name:           python-PyQRCode
Version:        1.3.6
Release:        0
Summary:        Python 3 module to generate QR Codes
License:        MIT
URL:            https://github.com/pyqrcode/pyqrcodeNG
# This is unofficial fork with some additional fixes, the canonical
# upstream repository is dead.
Source:         https://github.com/pyqrcode/pyqrcodeNG/archive/refs/tags/%{version}.tar.gz#/pyqrcodeNG-%{version}.tar.gz
# PATCH-FIX-UPSTREAM https://github.com/pyqrcode/pyqrcodeNG/pull/18
Patch0:         reproducible.patch
BuildRequires:  %{python_module Sphinx}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pypng}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun):update-alternatives
BuildArch:      noarch
%python_subpackages

%description
The PyQRCode module is a QR code generator that is simple to use and written in pure python. The module can automates most of the building process for creating QR codes. Most codes can be created using only two lines of code!

%package -n %{name}-doc
Summary:        Documentation files for %{name}

%description -n %{name}-doc
HTML Documentation for %{name}.

%prep
%autosetup -p1 -n pyqrcodeNG-%{version}

sed -i -e '1{\@^#!%{_bindir}/env python@d}' pyqrcodeng/{cli,qrspecial}.py

%build
%pyproject_wheel
python3 setup.py build_sphinx -v
rm -rvf build/sphinx/html/.buildinfo

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/pyqr
%python_expand %fdupes %{buildroot}/%{$python_sitelib}

%check
%pytest

%post
%python_install_alternative pyqr

%postun
%python_uninstall_alternative pyqr

%files %{python_files}
%license LICENSE
%doc README.rst CHANGES.rst
%{_bindir}/pyqr-%{python_bin_suffix}
%python_alternative %{_bindir}/pyqr
%{python_sitelib}/PyQRCodeNG-%{version}*-info
%{python_sitelib}/pyqrcodeng

%files -n %{name}-doc
%doc build/sphinx/html

%changelog
