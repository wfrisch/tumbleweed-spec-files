#
# spec file for package hashlink
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


Name:           hashlink
Version:        1.12
Release:        0
Summary:        A virtual machine for Haxe
License:        MIT
URL:            https://hashlink.haxe.org/
Source0:        https://github.com/HaxeFoundation/%{name}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM
Patch01:        0001-cmake-Link-sdl.hdll-with-OpenGL.patch
# PATCH-FIX-UPSTREAM
Patch02:        0001-cmake-Install-hlc_main.c-with-hl.h-and-hlc.h.patch
# PATCH-FIX-UPSTREAM
Patch03:        0001-Disable-the-JIT-tests-on-arm-architectures.patch
# PATCH-FIX-UPSTREAM
Patch04:        0001-cmake-Don-t-build-the-interpreter-on-ARM.patch
# PATCH-FIX-UPSTREAM
Patch05:        0001-cmake-Don-t-run-the-version-test-if-the-interpreter-.patch
# PATCH-FIX-OPENSUSE
Patch06:        0001-fix-rpath.patch
BuildRequires:  cmake
BuildRequires:  haxe >= 4.0
BuildRequires:  mbedtls-devel
BuildRequires:  cmake(sdl2)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libturbojpeg)
BuildRequires:  pkgconfig(libuv)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(vorbis)
Requires:       %{name}-hdlls = %{version}
Enhances:       haxe

%description
HashLink is a virtual machine for Haxe.
Haxe supports two modes of compilation for HashLink:
* Compilation to HashLink bytecode. This mode has a very fast compilation time,
  so it is suitable for daily development.
* Compilation to HashLink/C code, compiled with a native compiler to a regular
  executable. This mode results in the best performance, so it is suitable for
  final releases.

%package -n libhl1
Summary:        HashLink library

%description -n libhl1
This subpackage provides the libhl library for HashLink.

%package hdlls
Summary:        Hdll libraries for HashLink

%description hdlls
This subpackage provides the hdll libraries for HashLink.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}-hdlls  = %{version}
Requires:       libhl1  = %{version}

%description devel
Contains the files required to compile to a native executable the HashLink/C
code generated by the haxe compiler.

%prep
%autosetup -n hashlink-%{version} -p1

%build
# The build process for the tests uses haxe and requires the hashlink library
haxelib setup ./haxelib
haxelib dev hashlink other/haxelib
%cmake
%cmake_build

%install
%cmake_install

%check
# uvsample.hl fails when run in parallel
%ctest "-j0"

%post   -n libhl1 -p /sbin/ldconfig
%postun -n libhl1 -p /sbin/ldconfig

%files
%ifnarch %{arm} %{arm64}
%{_bindir}/hl
%endif
%license LICENSE
%doc README.md

%files -n libhl1
%license LICENSE
%{_libdir}/*.so.1*

%files hdlls
%license LICENSE
%{_libdir}/*.hdll

%files devel
%license LICENSE
%{_libdir}/*.so
%{_includedir}/*.h
%{_includedir}/hlc_main.c

%changelog
