#
# spec file for package mate-applet-softupd
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


Name:           mate-applet-softupd
Version:        0.4.8
Release:        0
Summary:        MATE panel applet for software update notifications
License:        GPL-2.0-or-later
Group:          System/GUI/Other
URL:            http://zavedil.com/mate-software-updates-applet
Source:         https://github.com/assen-totin/mate-applet-softupd/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE no-gtk2.patch -- Strip GTK2 from autoconf, we do not use it so no need to require it for autoreconf
Patch0:         no-gtk2.patch
BuildRequires:  PackageKit-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gettext-devel
BuildRequires:  gnome-packagekit
BuildRequires:  hicolor-icon-theme
BuildRequires:  mate-panel-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libnotify)
Requires:       PackageKit
Requires:       gnome-packagekit
Recommends:     %{name}-lang

%description
This is a MATE panel applet to notify when software updates are
available.

The notification is displayed in two ways:
  1) by changing the icon of the applet.
  2) by sending a notification to the notification-daemon.

The information is obtained from PackageKit.

%lang_package

%prep
%autosetup -p1

%build
NO_CONFIGURE=1 sh ./autogen.sh
%configure \
  --enable-gtk=3                       \
  --enable-backend=package-kit         \
  --enable-installer=gpk-update-viewer
%make_build

%install
%make_install

# Fix documentation directory.
mkdir -p %{buildroot}%{_docdir}/
mv %{buildroot}%{_datadir}/doc/%{name} %{buildroot}%{_docdir}/%{name}

# Remove unneeded files.
rm %{buildroot}%{_docdir}/%{name}/{INSTALL,NEWS}

%find_lang %{name}

%if 0%{?suse_version} < 1500
%post
%icon_theme_cache_post

%postun
%icon_theme_cache_postun
%endif

%files
%{_libexecdir}/softupd_applet
%{_datadir}/dbus-1/services/org.mate.panel.applet.SoftupdApplet.service
%{_docdir}/%{name}/
%{_datadir}/icons/hicolor/*/apps/applet_softupd.png
%dir %{_datadir}/mate-panel/
%dir %{_datadir}/mate-panel/applets/
%{_datadir}/mate-panel/applets/org.mate.applets.SoftupdApplet.mate-panel-applet
%{_datadir}/pixmaps/applet_softupd_*.png

%files lang -f %{name}.lang

%changelog
