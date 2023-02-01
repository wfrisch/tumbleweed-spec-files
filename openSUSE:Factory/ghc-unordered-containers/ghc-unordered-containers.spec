#
# spec file for package ghc-unordered-containers
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


%global pkg_name unordered-containers
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        0.2.19.1
Release:        0
Summary:        Efficient hashing-based container types
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/revision/1.cabal#/%{pkg_name}.cabal
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-hashable-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-template-haskell-devel
ExcludeArch:    %{ix86}
%if %{with tests}
BuildRequires:  ghc-ChasingBottoms-devel
BuildRequires:  ghc-HUnit-devel
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-nothunks-devel
BuildRequires:  ghc-random-devel
BuildRequires:  ghc-tasty-devel
BuildRequires:  ghc-tasty-hunit-devel
BuildRequires:  ghc-tasty-quickcheck-devel
%endif

%description
Efficient hashing-based container types. The containers have been optimized for
performance critical use, both in terms of large data quantities and high
speed.

The declared cost of each operation is either worst-case or amortized, but
remains valid even if structures are shared.

/Security/

This package currently provides no defenses against hash collision attacks such
as HashDoS. Users who need to store input from untrusted sources are advised to
use 'Data.Map' or 'Data.Set' from the 'containers' package instead.

%package devel
Summary:        Haskell %{pkg_name} library development files
Requires:       %{name} = %{version}-%{release}
Requires:       ghc-compiler = %{ghc_version}
Requires(post): ghc-compiler = %{ghc_version}
Requires(postun): ghc-compiler = %{ghc_version}

%description devel
This package provides the Haskell %{pkg_name} library development
files.

%prep
%autosetup -n %{pkg_name}-%{version}
cp -p %{SOURCE1} %{pkg_name}.cabal

%build
%ghc_lib_build

%install
%ghc_lib_install

%check
%cabal_test

%post devel
%ghc_pkg_recache

%postun devel
%ghc_pkg_recache

%files -f %{name}.files
%license LICENSE

%files devel -f %{name}-devel.files
%doc CHANGES.md

%changelog
