#
# spec file for package cutterff
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


Name:           cutterff
Summary:        Video cutter that uses FFmpeg and GTK+
Version:        1.0.2
Release:        0
URL:            https://cutterff.sourceforge.io/
Source0:        %{name}-%{version}-src.tar.bz2
Source1:        %{name}.desktop
License:        GPL-3.0-only
Group:          Productivity/Multimedia/Video/Editors and Convertors

BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libswscale)

%description
CutterFF is a program for cutting videos using FFmpeg and GTK+.
It does not decode/encode the streams, it only copies them.

Features
 - Selecting which streams written to the output
 - Selecting the format and bitstream filters
 - Choose a program if video contains more than one
 - Set cutpoints everywhere in the video
 - Many formats and codecs supported by FFmpeg
 - Log window for displaying FFmpeg messages

%lang_package

%prep
%autosetup

%build
export CPPFLAGS="%{optflags}"
%configure
%make_build

%install
%make_install
install -D -m644 %{name}.xpm %{buildroot}%{_datadir}/pixmaps/%{name}.xpm
install -D -m644 %{S:1} %{buildroot}%{_datadir}/applications/%{name}.desktop

%find_lang %{name}

%files
%license COPYING
%doc README ChangeLog
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.xpm

%files lang -f %{name}.lang

%changelog
