#
# spec file for package perl-Data-Perl
#
# Copyright (c) 2020 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Data-Perl
Version:        0.002011
Release:        0
%define cpan_name Data-Perl
Summary:        Base classes wrapping fundamental Perl data types
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOBYINK/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Class::Method::Modifiers)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Role::Tiny)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::Output)
BuildRequires:  perl(parent)
BuildRequires:  perl(strictures)
Requires:       perl(Class::Method::Modifiers)
Requires:       perl(List::MoreUtils)
Requires:       perl(Module::Runtime)
Requires:       perl(Role::Tiny)
Requires:       perl(parent)
Requires:       perl(strictures)
%{perl_requires}

%description
Data::Perl is a collection of classes that wrap fundamental data types that
exist in Perl. These classes and methods as they exist today are an attempt
to mirror functionality provided by Moose's Native Traits. One important
thing to note is all classes currently do no validation on constructor
input.

Data::Perl is a container class for the following classes:

* * Data::Perl::Collection::Hash

* * Data::Perl::Collection::Array

* * Data::Perl::String

* * Data::Perl::Number

* * Data::Perl::Counter

* * Data::Perl::Bool

* * Data::Perl::Code

%prep
%setup -q -n %{cpan_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes README.mkdn
%license LICENSE

%changelog
