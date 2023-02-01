#
# spec file for package sundanese-unicode-fonts
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

Name:           sundanese-unicode-fonts
Version:        1.0.5
Release:        0
Summary:        Sundanese Unicode Font
License:        SUSE-Public-Domain
Group:          System/X11/Fonts
Url:            http://sabilulungan.org/aksara/
Source0:        http://sabilulungan.org/aksara/files/font/SundaneseUnicode-1.0.5.ttf
Source1:        COPYING
BuildRequires:  fontpackages-devel
%reconfigure_fonts_prereq
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
BabelStone latin modern font.

%prep
%setup -q -c -T 
cp -a %{SOURCE0} .

%build
cp -a %{SOURCE1} .

%install
mkdir -p %{buildroot}%{_ttfontsdir}
install -m 0644 *.ttf %{buildroot}%{_ttfontsdir}/

%reconfigure_fonts_scriptlets

%files
%defattr(-,root,root)
%doc COPYING
%{_ttfontsdir}

%changelog

