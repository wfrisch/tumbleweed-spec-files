#
# spec file for package perl-Unicode-Collate
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


%define cpan_name Unicode-Collate
Name:           perl-Unicode-Collate
Version:        1.31
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Unicode Collation Algorithm
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/S/SA/SADAHIRO/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}
# MANUAL BEGIN
# special case as perl itself provides Unicode-Collate as well, however
# in an older version. we need to rebuild on version updates
# to ensure we are always newer than the perl-core provided version (bsc#1185600)
%requires_eq    perl
# MANUAL END

%description
This module is an implementation of Unicode Technical Standard #10 (a.k.a.
UTS #10) - Unicode Collation Algorithm (a.k.a. UCA).

%prep
%autosetup  -n %{cpan_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes Collate.pmN disableXS enableXS MANIFEST.N mkheader mklocale README

%changelog
