#
# spec file for package perl-HTML-FormatText-WithLinks
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-HTML-FormatText-WithLinks
Version:        0.15
Release:        0
%define cpan_name HTML-FormatText-WithLinks
Summary:        HTML to text conversion with links as footnotes
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/HTML-FormatText-WithLinks/
Source:         http://www.cpan.org/authors/id/S/ST/STRUAN/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(HTML::FormatText) >= 2
BuildRequires:  perl(HTML::TreeBuilder)
BuildRequires:  perl(Module::Build) >= 0.38
BuildRequires:  perl(URI::WithBase)
Requires:       perl(HTML::FormatText) >= 2
Requires:       perl(HTML::TreeBuilder)
Requires:       perl(URI::WithBase)
%{perl_requires}

%description
HTML::FormatText::WithLinks takes HTML and turns it into plain text but
prints all the links in the HTML as footnotes. By default, it attempts to
mimic the format of the lynx text based web browser's --dump option.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build build flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install destdir=%{buildroot} create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes examples README

%changelog
