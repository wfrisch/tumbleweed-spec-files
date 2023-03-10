#
# spec file for package fcitx-anthy
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


Name:           fcitx-anthy
Version:        0.2.4
Release:        0
Summary:        Japanese Anthy IME Wrapper for Fcitx
License:        GPL-2.0-or-later
Group:          System/I18n/Japanese
URL:            https://fcitx-im.org/wiki/Anthy
Source:         https://github.com/fcitx/fcitx-anthy/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  anthy-devel
BuildRequires:  cmake
BuildRequires:  fcitx-devel
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  hicolor-icon-theme
BuildRequires:  intltool
Requires:  anthy
%{fcitx_requires}

%description
fcitx-anthy is a Japanese Anthy IME Wrapper for Fcitx.

Anthy is a system for Japanese input method. It converts Hiragana text to Kana Kanji mixed text.

Fcitx is a input method framework with extension support.

%prep
%setup -q

%build
%cmake
%make_build

%install
%cmake_install
%find_lang %{name}
%fdupes %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%license COPYING
%{_fcitx_libdir}/%{name}.so
%{_fcitx_addondir}/%{name}.conf
%{_fcitx_datadir}/anthy
%{_fcitx_descdir}/%{name}.desc
%{_fcitx_imicondir}/anthy.png
%{_fcitx_inputmethoddir}/anthy.conf
%{_datadir}/icons/hicolor/*/status/*.png
%{_datadir}/icons/hicolor/*/status/*.svg

%changelog
