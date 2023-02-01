#
# spec file for package libqt5-qtwebchannel
#
# Copyright (c) 2019 SUSE LLC
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


%define qt5_snapshot 1
%define libname libQt5WebChannel5
%define base_name libqt5
%define real_version 5.15.8
%define so_version 5.15.8
%define tar_version qtwebchannel-everywhere-src-%{version}
Name:           libqt5-qtwebchannel
Version:        5.15.8+kde3
Release:        0
Summary:        Qt 5 WebChannel Addon
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)
Group:          Development/Libraries/X11
URL:            https://www.qt.io
Source:         %{tar_version}.tar.xz
Source1:        baselibs.conf
BuildRequires:  fdupes
BuildRequires:  libqt5-qtbase-private-headers-devel >= %{real_version}
BuildRequires:  libqt5-qtdeclarative-devel >= %{real_version}
BuildRequires:  libqt5-qtwebsockets-devel >= %{real_version}
BuildRequires:  xz
%if %{qt5_snapshot}
#to create the forwarding headers
BuildRequires:  perl
%endif

%description
Qt WebChannel enables peer-to-peer communication between a server
(QML/C++ application) and a client (HTML/JavaScript or QML
application).

The module provides a JavaScript library for seamless integration of
C++ and QML applications with HTML/JavaScript and QML clients. The
clients must use the JavaScript library to access the serialized
QObjects published by the host applications.

%prep
%autosetup -p1 -n %{tar_version}

%package -n %{libname}
Summary:        Qt 5 WebChannel Addon
Group:          Development/Libraries/X11
%requires_ge    libQtQuick5

%description -n %{libname}
Qt WebChannel enables peer-to-peer communication between a server
(QML/C++ application) and a client (HTML/JavaScript or QML
application).

The module provides a JavaScript library for seamless integration of
C++ and QML applications with HTML/JavaScript and QML clients. The
clients must use the JavaScript library to access the serialized
QObjects published by the host applications.

%package -n %{libname}-imports
Summary:        QML imports for the Qt5 WebSockets library
Group:          Development/Libraries/X11
%requires_ge    libQtQuick5
Supplements:    (%{libname} and libQtQuick5)
# imports splited with 5.4.1
Conflicts:      %{libname} < 5.4.1

%description -n %{libname}-imports
The module provides a JavaScript library for seamless integration of
C++ and QML applications with HTML/JavaScript and QML clients.

%package devel
Summary:        Development files for the Qt5 WebChannel library
Group:          Development/Libraries/X11
Requires:       %{libname} = %{version}

%description devel
You need this package if you want to compile programs with qtwebchannel.

%package private-headers-devel
Summary:        Non-ABI stable experimental API for the Qt5 WebChannel library
Group:          Development/Libraries/C and C++
Requires:       %{name}-devel = %{version}
Requires:       libQt5Core-private-headers-devel >= %{real_version}
BuildArch:      noarch

%description private-headers-devel
This package provides private headers of libqt5-qtwebchannel that are normally
not used by application development and that do not have any ABI or
API guarantees. The packages that build against these have to require
the exact Qt version.

%package examples
Summary:        Qt5 WebChannel examples
Group:          Development/Libraries/X11
License:        BSD-3-Clause
Recommends:     %{name}-devel

%description examples
Examples for the libqt5-qtwebchannel module.

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%build
%if %{qt5_snapshot}
#force the configure script to generate the forwarding headers (it checks whether .git directory exists)
mkdir .git
%endif
%qmake5
%make_jobs

%install
%qmake5_install

# kill .la files
rm -f %{buildroot}%{_libqt5_libdir}/lib*.la

%files -n %{libname}
%defattr(-,root,root,755)
%license LICENSE.*
%{_libqt5_libdir}/libQt5WebChannel.so.*

%files -n %{libname}-imports
%defattr(-,root,root,755)
%license LICENSE.*
%{_libqt5_archdatadir}/qml/QtWebChannel/

%files private-headers-devel
%defattr(-,root,root,755)
%license LICENSE.*
%{_libqt5_includedir}/QtWebChannel/%{so_version}

%files devel
%defattr(-,root,root,755)
%license LICENSE.*
%exclude %{_libqt5_includedir}/QtWebChannel/%{so_version}
%{_libqt5_includedir}/QtWebChannel
%{_libqt5_libdir}/cmake/Qt5WebChannel
%{_libqt5_libdir}/libQt5WebChannel.prl
%{_libqt5_libdir}/libQt5WebChannel.so
%{_libqt5_libdir}/pkgconfig/Qt5WebChannel.pc
%{_libqt5_libdir}/qt5/mkspecs/modules/qt_lib_*.pri

%files examples
%defattr(-,root,root,755)
%license LICENSE.*
%{_libqt5_examplesdir}/

%changelog
