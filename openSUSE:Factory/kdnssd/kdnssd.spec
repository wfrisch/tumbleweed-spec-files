#
# spec file for package kdnssd
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


%define rname kio-zeroconf
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           kdnssd
Version:        22.12.1
Release:        0
Summary:        Zeroconf Support for KIO applications
License:        GPL-2.0-or-later
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{rname}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{rname}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-filesystem
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5DNSSD)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5KIO)

%description
This package adds Zeroconf support to KIO, allowing the use of this protocol
in all applications that are using KIO.

%lang_package

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%ifarch ppc ppc64
export RPM_OPT_FLAGS="%{optflags} -mminimal-toc"
%endif
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --with-man --all-name

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license LICENSES/*
%{_kf5_appstreamdir}/org.kde.kio_zeroconf.metainfo.xml
%{_kf5_dbusinterfacesdir}/org.kde.kdnssd.xml
%dir %{_kf5_plugindir}/kf5/
%dir %{_kf5_plugindir}/kf5/kded
%{_kf5_plugindir}/kf5/kded/dnssdwatcher.so
%{_kf5_plugindir}/kf5/kio/zeroconf.so
%dir %{_kf5_sharedir}/remoteview/
%{_kf5_sharedir}/remoteview/zeroconf.desktop

%files lang -f %{name}.lang

%changelog
