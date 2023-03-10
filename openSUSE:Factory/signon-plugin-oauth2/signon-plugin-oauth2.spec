#
# spec file for package signon-plugin-oauth2
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


Name:           signon-plugin-oauth2
Version:        0.25
Release:        0
Summary:        Oauth2 plugin for the Single Sign On Framework
License:        LGPL-2.0-only
Group:          System/GUI/Other
URL:            https://gitlab.com/accounts-sso/signon-plugin-oauth2
Source:         %{url}/-/archive/VERSION_%{version}/signon-plugin-oauth2-VERSION_%{version}.tar.bz2
Patch0:         0001_Multilib.patch
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(libsignon-qt5)
BuildRequires:  pkgconfig(signon-plugins)
Requires:       signon-ui
Conflicts:      libproxy1-config-kde4

%description
This package contains the Oauth2 plugin for the Single Sign On Framework.

%package devel
Summary:        Development files for signon-plugin-oauth2
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

%description devel
This package contains the development files for the Oauth2 plugin for the Single
Sign On Framework.

%prep
%setup -q -n signon-plugin-oauth2-VERSION_%{version}

%patch0 -p1 -b .multilib
sed -i 's|@LIB@|%{_lib}|g' src/signon-oauth2plugin.pc src/src.pro

%build
mkdir build
pushd build
%qmake5 \
  PREFIX=%{_prefix} \
  LIBDIR=%{_libdir} \
  QMAKE_CXXFLAGS+="-Wno-error=deprecated-declarations" \
  ..
%make_jobs
popd

%install
pushd build
%qmake5_install
# Remove examples and tests
rm -rf %{buildroot}/%{_bindir} %{buildroot}/%{_datadir}
popd

%files
%license COPYING
%doc README.md
%dir %{_libdir}/signon/
%{_libdir}/signon/liboauth2plugin.so

%files devel
%dir %{_includedir}/signon-plugins/
%{_includedir}/signon-plugins/*.h
%{_libdir}/pkgconfig/signon-oauth2plugin.pc

%changelog
