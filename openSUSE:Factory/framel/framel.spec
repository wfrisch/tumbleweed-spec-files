#
# spec file for package framel
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


%define upstream_name Fr
%define skip_python2 1
# Disable py 3.6: no numpy
%define skip_python36 1
%global shlib lib%{name}8
Name:           framel
Version:        8.42.3
Release:        0
Summary:        Library to manipulate Gravitational Wave Detector data in frame format
License:        LGPL-2.1-or-later
URL:            https://git.ligo.org/virgo/virgoapp/Fr
Source:         %{url}/-/archive/%{version}/Fr-%{version}.tar.bz2
# PATCH-FIX-UPSTREAM framel-fix-pkgconfig.patch badshah400@gmail.com -- Fix include and lib dir paths in pkgconfig file
Patch0:         framel-fix-pkgconfig.patch
# PATCH-FIX-UPSTREAM framel-correct-python-platlib.patch badshah400@gmail.com -- Use sysconfig instead of distutils.sysconfig to correctly set python platlib
Patch1:         framel-correct-python-platlib.patch
BuildRequires:  %{python_module numpy-devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  cmake >= 3.12
BuildRequires:  gcc-c++
BuildRequires:  python-rpm-macros

%python_subpackages

%description
A Common Data Frame Format for Interferometric Gravitational Wave Detector has
been developed by VIRGO and LIGO. The Frame Library is a software in C
language, with interfaces to python and matlab, dedicated to frame data
manipulation including file input/output.

%package -n %{shlib}
Summary:        Shared library for framel - a library for gravitational wave frame data

%description -n %{shlib}
The Frame Library is a software in C language, with interfaces to python and
matlab, dedicated to frame data manipulation including file input/output.

This package provides the shared library for framel.

%package -n %{name}-devel
Summary:        Headers and sources for developing with the gravitational wave frame library
Requires:       %{shlib} = %{version}

%description -n %{name}-devel
The Frame Library is a software in C language, with interfaces to python and
matlab, dedicated to frame data manipulation including file input/output.

This package property the headers and sources needed to develop applications
against the frame library.

%prep
%autosetup -p1 -n %{upstream_name}-%{version}

%build
%{python_expand #for supported py3 flavours
export PYTHON=%{_bindir}/$python
mkdir ../$python
cp -pr ./ ../$python
pushd ../$python
%cmake \
  -DCMAKE_INSTALL_INCLUDEDIR=%{_includedir}/%{name} \
  -DCMAKE_INSTALL_DOCDIR=%{_docdir}/%{name} \
  -DENABLE_PYTHON=yes \
  -DPython3_EXECUTABLE=${PYTHON}
%cmake_build
popd
}

%install
%{python_expand #for supported py3 flavours
export PYTHON=%{_bindir}/$python
pushd ../$python
%cmake_install
popd
}

%post -n %{shlib} -p /sbin/ldconfig
%postun -n %{shlib} -p /sbin/ldconfig

%files -n %{name}
%license LICENSE
%{_bindir}/*

%files -n %{shlib}
%{_libdir}/libframel.so.*

%files -n %{name}-devel
%license LICENSE
%doc %{_docdir}/%{name}
%{_includedir}/%{name}/
%{_libdir}/libframel.so
%{_libdir}/pkgconfig/*.pc

%files %{python_files}
%license LICENSE
%{python_sitearch}/*

%changelog
