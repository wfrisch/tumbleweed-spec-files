#
# spec file for package fcitx-qt5
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

%if 0%{?suse_version} >= 1550
%define build_qt6 1
%else
%define build_qt6 0
%endif

Name:           fcitx-qt5
Version:        1.2.7
Release:        0
Summary:        Fcitx QT5 Input Context
License:        BSD-3-Clause AND GPL-2.0-or-later AND GPL-3.0-or-later
Group:          System/I18n/Chinese
URL:            https://github.com/fcitx/fcitx-qt5
Source:         %{URL}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.xz
Source99:       baselibs.conf
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  fcitx-devel >= 4.2.9.1
BuildRequires:  gcc-c++
BuildRequires:  libicu-devel
BuildRequires:  libqt5-qtbase-devel
BuildRequires:  libqt5-qtbase-private-headers-devel
BuildRequires:  libqt5-qtx11extras-devel
BuildRequires:  libxkbcommon-devel
%if %build_qt6
BuildRequires:  qt6-base-devel
BuildRequires:  qt6-base-private-devel
%endif
# fcitx-qt5 is using private QPA API, which can, and does break BC even in point releases,
# so we need to hardcode libQt5Gui5 version
%requires_eq    libQt5Gui5
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
A QT5 input context plugin of Fcitx IM Framework.

%if %build_qt6
%package -n fcitx-qt6
Summary:        Qt6 IM module for Fcitx
Group:          System/I18n/Chinese
Supplements:    (fcitx and libQt6Core6)

%description -n fcitx-qt6
Qt6 IM module for Fcitx.
%endif

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

%description devel
Development header files for Fcitx input method framework (Qt5).

%prep
%setup

%build
%if %build_qt6
%cmake -DENABLE_QT6=ON
%else
%cmake
%endif
%make_build

%install
%cmake_install

%find_lang fcitx-qt5

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig
%if %build_qt6
%post -n fcitx-qt6 -p /sbin/ldconfig
%postun -n fcitx-qt6 -p /sbin/ldconfig

%files -n fcitx-qt6
%{_libdir}/qt6/plugins/platforminputcontexts/libfcitxplatforminputcontextplugin-qt6.so
%endif

%files -f fcitx-qt5.lang
%license COPYING
%dir %{_libdir}/fcitx/qt
%{_libdir}/fcitx/libexec/fcitx-qt5-gui-wrapper
%{_libdir}/libFcitxQt5*Addons.so.1
%{_libdir}/libFcitxQt5*Addons.so.1.0
%{_libdir}/fcitx/qt/libfcitx-quickphrase-editor5.so
%dir %{_libdir}/qt5/plugins/
%dir %{_libdir}/qt5/plugins/platforminputcontexts/
%{_libdir}/qt5/plugins/platforminputcontexts/libfcitxplatforminputcontextplugin.so

%files devel
%{_includedir}/FcitxQt5
%{_libdir}/libFcitxQt5*Addons.so
%{_libdir}/cmake/FcitxQt5*Addons/

%changelog
