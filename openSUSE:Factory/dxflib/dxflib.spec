#
# spec file for package dxflib
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


# Patch1 needs update on version change
%define lname	libdxflib-3_26_4-1
Name:           dxflib
Version:        3.26.4
Release:        0
Summary:        Parser library for the Drawing Exchange Format (DXF)
License:        GPL-2.0-or-later
Group:          Development/Libraries/C and C++
#Git-Clone:	https://github.com/qcad/qcad
URL:            https://qcad.org/en/dxflib-downloads
Source:         https://qcad.org/archives/dxflib/%name-%version-src.tar.gz
Patch1:         dxflib-versioning.diff
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)

%description
dxflib is a C++ library mainly for parsing and writing DXF files.

%package -n %lname
Summary:        Parser library for the Drawing Exchange Format (DXF)
Group:          System/Libraries

%description -n %lname
dxflib is a C++ library mainly for parsing and writing DXF files.
QCAD/LibreCAD uses dxflib to import DXF files.

%package devel
Summary:        Development files for dxflib, a DXF parsing library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
dxflib is a C++ library mainly for parsing and writing DXF files.

This package contains the development library symlink and header
files.

%prep
%autosetup -n %name-%version-src -p1

%build
%qmake5 %name.pro
%make_build

%install
# `make install` does not do anything.
b="%buildroot"
mkdir -p "$b/%_libdir" "$b/%_includedir/%name"
install -pm0644 src/*.h "$b/%_includedir/%name/"
cp -a libdxflib*.so.* "$b/%_libdir/"
ln -Tsfv "libdxflib-%version.so.1" "$b/%_libdir/libdxflib.so"

# creates support file for pkg-config
mkdir -p "$b/%_libdir/pkgconfig"
cat >"$b/%_libdir/pkgconfig/dxflib.pc" <<-"EOF"
prefix=%_prefix
exec_prefix=${prefix}
libdir=${exec_prefix}/%_lib
includedir=${prefix}/include

Name:           dxflib
Description:    Library for reading dxf files
Version:        %version
Libs:           -L${libdir} -ldxflib
Cflags:         -I${includedir}/dxflib
EOF

%check
%make_build check

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%doc gpl-2.0greater.txt
%_libdir/libdxflib-%version.so.1*

%files devel
%_includedir/%name/
%_libdir/libdxflib.so
%_libdir/pkgconfig/%name.pc

%changelog
