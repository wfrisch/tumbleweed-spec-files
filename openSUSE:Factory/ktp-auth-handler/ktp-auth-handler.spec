#
# spec file for package ktp-auth-handler
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


# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %global _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           ktp-auth-handler
Version:        22.12.1
Release:        0
Summary:        Telepathy auth handler
License:        LGPL-2.1-or-later
URL:            https://community.kde.org/Real-Time_Communication_and_Collaboration
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  fdupes
BuildRequires:  libqca-qt5-devel
BuildRequires:  pkgconfig
BuildRequires:  telepathy-logger-qt5-devel
BuildRequires:  telepathy-qt5-devel
BuildRequires:  cmake(KAccounts)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Wallet)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KTp)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  pkgconfig(accounts-qt5)
BuildRequires:  pkgconfig(libsignon-qt5)
Requires:       libqca-qt5-plugins
Requires:       signon-plugin-oauth2
Obsoletes:      %{name}5 < %{version}
Provides:       %{name}5 = %{version}

%description
Telepathy-auth-handler provides UI/KWallet integration for passwords and
SSL errors on account connect.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --with-man --all-name

%fdupes %{buildroot}

%files
%license COPYING*
%{_kf5_sharedir}/dbus-1/services/org.freedesktop.Telepathy.Client.KTp.*.service
%{_kf5_sharedir}/telepathy/
%{_libexecdir}/ktp-auth-handler

%files lang -f %{name}.lang

%changelog
