#
# spec file for package pulseaudio-qt
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


%define soversion 3
%bcond_without lang
Name:           pulseaudio-qt
Version:        1.3
Release:        0
Summary:        Qt bindings for PulseAudio
License:        LGPL-2.1-or-later
Group:          System/GUI/KDE
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/%{name}/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/%{name}/%{name}-%{version}.tar.xz.sig
Source2:        pulseaudio-qt.keyring
%endif
BuildRequires:  extra-cmake-modules >= 5.80.0
BuildRequires:  kf5-filesystem
BuildRequires:  pkgconfig
BuildRequires:  cmake(Qt5Core) >= 5.15
BuildRequires:  cmake(Qt5DBus) >= 5.15
BuildRequires:  cmake(Qt5Gui) >= 5.15
BuildRequires:  cmake(Qt5Qml) >= 5.15
BuildRequires:  cmake(Qt5Test) >= 5.15
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libpulse-mainloop-glib)

%description
Pulseaudio-Qt is a library providing Qt bindings to PulseAudio.

%package -n libKF5PulseAudioQt%{soversion}
Summary:        Qt bindings for PulseAudio
Group:          System/Libraries
Recommends:     %{name}-lang
Provides:       %{name} = %{version}

%description -n libKF5PulseAudioQt%{soversion}
Pulseaudio-Qt is a library providing Qt bindings to PulseAudio.

%package devel
Summary:        Development files for pulseaudio-qt, Qt bindings for PulseAudio
Group:          Development/Libraries/KDE
Requires:       libKF5PulseAudioQt%{soversion} = %{version}

%description devel
Development files for pulseaudio-qt, a library providing Qt bindings to
PulseAudio.

%lang_package

%prep
%setup -q

%build
  %cmake_kf5 -d build
  %cmake_build

%install
  %kf5_makeinstall -C build

%post -n libKF5PulseAudioQt%{soversion} -p /sbin/ldconfig
%postun -n libKF5PulseAudioQt%{soversion} -p /sbin/ldconfig

%files -n libKF5PulseAudioQt%{soversion}
%license LICENSES/*
%doc README.md
%{_kf5_libdir}/libKF5PulseAudioQt.so.%{soversion}
%{_kf5_libdir}/libKF5PulseAudioQt.so.%{version}.0

%files devel
%dir %{_includedir}/KF5/
%dir %{_includedir}/KF5/KF5PulseAudioQt/
%{_includedir}/KF5/pulseaudioqt_version.h
%{_includedir}/KF5/KF5PulseAudioQt/
%{_kf5_cmakedir}/KF5PulseAudioQt/
%{_kf5_libdir}/libKF5PulseAudioQt.so

%changelog
