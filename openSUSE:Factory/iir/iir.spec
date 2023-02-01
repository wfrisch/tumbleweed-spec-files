#
# spec file for package iir
#
# Copyright (c) 2023 SUSE LLC
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


%define sover   1
%define sname   %{name}%{sover}
Name:           iir
Version:        1.9.4
Release:        0
Summary:        DSP infinite impulse response realtime C++ filter library
License:        MIT
URL:            https://github.com/berndporr/%{sname}
Source0:        https://github.com/berndporr/%{sname}/archive/%{version}.tar.gz#/%{sname}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig

%description

An infinite impulse response (IIR) filter library for Linux, Mac OSX and Windows
which implements Butterworth, RBJ, Chebychev filters and can easily import coefficients generated by Python (scipy).
The filter processes the data sample by sample for realtime processing.
It uses templates to allocate the required memory so that it can run without any malloc / new commands.
Memory is allocated at compile time so that there is never the risk of memory leaks.
All realtime filter code is in the header files which guarantees efficient integration into the main program
and the compiler can optimise both filter code and main program at the same time.

%package -n lib%{sname}
Summary:        DSP infinite impulse response realtime C++ filter library

%description -n lib%{sname}

An infinite impulse response (IIR) filter library for Linux, Mac OSX and Windows
which implements Butterworth, RBJ, Chebychev filters and can easily import coefficients generated by Python (scipy).
The filter processes the data sample by sample for realtime processing.
It uses templates to allocate the required memory so that it can run without any malloc / new commands.
Memory is allocated at compile time so that there is never the risk of memory leaks.
All realtime filter code is in the header files which guarantees efficient integration into the main program
and the compiler can optimise both filter code and main program at the same time.

%package -n lib%{name}-devel
Summary:        DSP infinite impulse response realtime C++ filter library
Requires:       lib%{sname} = %{version}

%description -n lib%{name}-devel

An infinite impulse response (IIR) filter library for Linux, Mac OSX and Windows
which implements Butterworth, RBJ, Chebychev filters and can easily import coefficients generated by Python (scipy).
The filter processes the data sample by sample for realtime processing.
It uses templates to allocate the required memory so that it can run without any malloc / new commands.
Memory is allocated at compile time so that there is never the risk of memory leaks.
All realtime filter code is in the header files which guarantees efficient integration into the main program
and the compiler can optimise both filter code and main program at the same time.

%prep
%autosetup -p1 -n %{sname}-%{version}

%build
%cmake -LA
%cmake_build

%install
%cmake_install
rm -r %{buildroot}%{_libdir}/cmake %{buildroot}%{_libdir}/lib%{name}_static.a

%post -n lib%{sname} -p /sbin/ldconfig
%postun -n lib%{sname} -p /sbin/ldconfig

%files -n lib%{sname}
%license COPYING
%doc README.md
%{_libdir}/lib%{name}.so.*

%files -n lib%{name}-devel
%{_includedir}/*.h
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
