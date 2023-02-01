#
# spec file for package perl-Module-Build-Prereqs-FromCPANfile
#
# Copyright (c) 2020 SUSE LLC
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


Name:           perl-Module-Build-Prereqs-FromCPANfile
Version:        0.02
Release:        0
%define cpan_name Module-Build-Prereqs-FromCPANfile
Summary:        Construct prereq parameters of Module::Build from cpanfile
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOSHIOITO/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(CPAN::Meta::Prereqs) >= 2.132830
BuildRequires:  perl(Module::Build) >= 0.420000
BuildRequires:  perl(Module::CPANfile) >= 1.0000
BuildRequires:  perl(version) >= 0.80
Requires:       perl(CPAN::Meta::Prereqs) >= 2.132830
Requires:       perl(Module::CPANfile) >= 1.0000
Requires:       perl(version) >= 0.80
Recommends:     perl(Module::Build) >= 0.4004
%{perl_requires}

%description
This simple module reads cpanfile and converts its content into valid
prereq parameters for 'new()' method of Module::Build.

Currently it does not support "optional features" specification (See
cpanfile/feature).

%prep
%setup -q -n %{cpan_name}-%{version}

%build
perl Build.PL installdirs=vendor
./Build build flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install destdir=%{buildroot} create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes README

%changelog
