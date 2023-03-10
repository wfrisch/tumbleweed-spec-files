#
# spec file for package lato-fonts
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


Name:           lato-fonts
Version:        2.015
Release:        0
Summary:        High-Quality Open Source Font Family
License:        OFL-1.1
Group:          System/X11/Fonts
URL:            https://www.latofonts.com/
Source:         https://www.latofonts.com/download/lato2ofl-zip/#/Lato2OFL.zip
BuildRequires:  dos2unix
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
%reconfigure_fonts_prereq
Obsoletes:      google-lato-fonts < %{version}
Provides:       google-lato-fonts = %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Lato is a sanserif typeface family designed in the Summer 2010 by Warsaw-based
designer Łukasz Dziedzic (“Lato” means “Summer” in Polish). In December 2010
the Lato family was published under the open-source Open Font License by his
foundry tyPoland, with support from Google.

In 2013 – 2014, the family was greatly extended to cover 3000+ glyphs per style.
The Lato 2.010 family now supports 100+ Latin-based languages, 50+ Cyrillic-based
languages as well as Greek and IPA phonetics. In the process, the metrics and
kerning of the family have been revised and four additional weights were created.

%prep
%setup -q -n Lato2OFL

%build
find . -type f -exec chmod 0644 \{\} +
dos2unix *.txt

%install
mkdir -p %{buildroot}/%{_datadir}/fonts/truetype
install -m 0644 *.ttf %{buildroot}/%{_datadir}/fonts/truetype

%reconfigure_fonts_scriptlets

%files
%defattr(-,root,root)
%license OFL.txt
%doc README.txt
%{_datadir}/fonts/truetype

%changelog
