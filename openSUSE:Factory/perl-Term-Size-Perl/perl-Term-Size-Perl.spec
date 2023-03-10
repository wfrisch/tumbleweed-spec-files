#
# spec file for package perl-Term-Size-Perl
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Term-Size-Perl
Version:        0.031
Release:        0
%define cpan_name Term-Size-Perl
Summary:        Perl extension for retrieving terminal size (Perl version)
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Term-Size-Perl/
Source0:        https://cpan.metacpan.org/authors/id/F/FE/FERREIRA/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
Patch0:         reproducible.patch
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::CBuilder)
%{perl_requires}

%description
Yet another implementation of 'Term::Size'. Now in pure Perl, with the
exception of a C probe run on build time.

%prep
%setup -q -n %{cpan_name}-%{version}
%autopatch -p1

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes README
%license LICENSE

%changelog
