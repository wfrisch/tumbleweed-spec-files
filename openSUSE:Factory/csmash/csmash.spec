#
# spec file for package csmash
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


Name:           csmash
Version:        0.6.6
Release:        0
Summary:        3D Table Tennis Game
License:        GPL-2.0-or-later
Group:          Amusements/Games/3D/Other
URL:            http://cannonsmash.sourceforge.net/
Source:         %{name}-%{version}.tar.bz2
Source1:        danslatristesse2-48.ogg
Source2:        %{name}.desktop
Patch0:         %{name}-%{version}.diff
Patch1:         %{name}-%{version}-datadir.diff
Patch2:         %{name}-%{version}-return_value.diff
Patch3:         %{name}-%{version}-qualification.diff
Patch4:         %{name}-%{version}-definitions.diff
Patch5:         %{name}-%{version}-uninitialized.diff
BuildRequires:  SDL_image-devel
BuildRequires:  SDL_mixer-devel
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gtk+-x11-2.0)
BuildRequires:  pkgconfig(sdl)
BuildRequires:  pkgconfig(zlib)

%description
CannonSmash is a 3D table tennis game. The goal of this project is to
represent various table tennis strategies in a computer game.

%prep
%autosetup -p0
mv README README.jp
mv README.en README

%build
%configure \
  --x-includes=%{_includedir} \
  --x-libraries=%{_libdir}
%make_build AM_CFLAGS="%optflags" AM_CPPFLAGS="%optflags"

%install
%make_install
cp %{SOURCE1} %{buildroot}%{_datadir}/csmash
%fdupes %{buildroot}%{_datadir}
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE2}
%find_lang %{name}

%files -f %{name}.lang
%doc README README.jp AUTHORS COPYING CREDITS ChangeLog
%{_bindir}/csmash
%{_datadir}/csmash/
%{_datadir}/applications/%{name}.desktop

%changelog
