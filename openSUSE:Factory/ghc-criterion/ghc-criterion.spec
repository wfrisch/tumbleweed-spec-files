#
# spec file for package ghc-criterion
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


%global pkg_name criterion
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        1.6.0.0
Release:        0
Summary:        Robust, reliable performance measurement and analysis
License:        BSD-2-Clause
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
BuildRequires:  chrpath
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-Glob-devel
BuildRequires:  ghc-aeson-devel
BuildRequires:  ghc-ansi-wl-pprint-devel
BuildRequires:  ghc-base-compat-batteries-devel
BuildRequires:  ghc-binary-devel
BuildRequires:  ghc-binary-orphans-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-cassava-devel
BuildRequires:  ghc-code-page-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-criterion-measurement-devel
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-exceptions-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-js-chart-devel
BuildRequires:  ghc-microstache-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-mwc-random-devel
BuildRequires:  ghc-optparse-applicative-devel
BuildRequires:  ghc-parsec-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-statistics-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-transformers-compat-devel
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-vector-algorithms-devel
BuildRequires:  ghc-vector-devel
ExcludeArch:    %{ix86}
%if %{with tests}
BuildRequires:  ghc-HUnit-devel
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-base-compat-devel
BuildRequires:  ghc-tasty-devel
BuildRequires:  ghc-tasty-hunit-devel
BuildRequires:  ghc-tasty-quickcheck-devel
%endif

%description
This library provides a powerful but simple way to measure software
performance. It provides both a framework for executing and analysing
benchmarks and a set of driver functions that makes it easy to build and run
benchmarks, and to analyse their results.

The fastest way to get started is to read the
<http://www.serpentine.com/criterion/tutorial.html online tutorial>, followed
by the documentation and examples in the "Criterion.Main" module.

For examples of the kinds of reports that criterion generates, see
<http://www.serpentine.com/criterion the home page>.

%package devel
Summary:        Haskell %{pkg_name} library development files
Requires:       %{name} = %{version}-%{release}
Requires:       ghc-compiler = %{ghc_version}
Requires(post): ghc-compiler = %{ghc_version}
Requires(postun): ghc-compiler = %{ghc_version}

%description devel
This package provides the Haskell %{pkg_name} library development files.

%prep
%autosetup -n %{pkg_name}-%{version}

%build
%ghc_lib_build

%install
%ghc_lib_install
%ghc_fix_rpath %{pkg_name}-%{version}

%check
%cabal_test

%post devel
%ghc_pkg_recache

%postun devel
%ghc_pkg_recache

%files -f %{name}.files
%license LICENSE
%{_bindir}/criterion-report
%dir %{_datadir}/%{pkg_name}-%{version}
%dir %{_datadir}/%{pkg_name}-%{version}/templates
%{_datadir}/%{pkg_name}-%{version}/templates/*.css
%{_datadir}/%{pkg_name}-%{version}/templates/*.js
%{_datadir}/%{pkg_name}-%{version}/templates/*.tpl

%files devel -f %{name}-devel.files
%doc README.markdown changelog.md examples

%changelog
