#
# spec file for package capnet-assist
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


Name:           capnet-assist
Version:        2.4.2
Release:        0
Summary:        Captive Portal Assistant
License:        GPL-3.0-only
Group:          Productivity/Networking/Other
URL:            https://elementary.io/
Source:         https://github.com/elementary/capnet-assist/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  vala >= 0.28.0
BuildRequires:  pkgconfig(gcr-3)
BuildRequires:  pkgconfig(gcr-ui-3)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libhandy-1)
BuildRequires:  pkgconfig(webkit2gtk-4.0)
Requires:       NetworkManager
Recommends:     %{name}-lang
Provides:       elementary-capnet-assist = %{version}
Obsoletes:      elementary-capnet-assist < %{version}

%description
Assists users in connective to Captive Portals such as those found on
public access points in train stations, coffee shops, universities, etc.
Upon detection, the assistant appears showing the captive portal. Once a
connection is known to have been established, it dismisses itself. Written
in Vala and using WebkitGtk+.

%lang_package

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install
%suse_update_desktop_file io.elementary.capnet-assist
%find_lang io.elementary.capnet-assist %{name}.lang
%fdupes %{buildroot}%{_datadir}/icons

%files
%license COPYING
%doc README*
%{_bindir}/io.elementary.capnet-assist
%{_datadir}/applications/io.elementary.capnet-assist.desktop
%{_datadir}/glib-2.0/schemas/io.elementary.capnet-assist.gschema.xml
%dir %{_datadir}/icons/hicolor/128x128@2
%dir %{_datadir}/icons/hicolor/128x128@2/apps
%dir %{_datadir}/icons/hicolor/16x16@2
%dir %{_datadir}/icons/hicolor/16x16@2/apps
%dir %{_datadir}/icons/hicolor/24x24@2
%dir %{_datadir}/icons/hicolor/24x24@2/apps
%dir %{_datadir}/icons/hicolor/32x32@2
%dir %{_datadir}/icons/hicolor/32x32@2/apps
%dir %{_datadir}/icons/hicolor/48x48@2
%dir %{_datadir}/icons/hicolor/48x48@2/apps
%dir %{_datadir}/icons/hicolor/64x64@2
%dir %{_datadir}/icons/hicolor/64x64@2/apps
%{_datadir}/icons/hicolor/*/apps/io.elementary.capnet-assist.svg
%{_datadir}/metainfo/io.elementary.capnet-assist.appdata.xml

%files lang -f %{name}.lang

%changelog
