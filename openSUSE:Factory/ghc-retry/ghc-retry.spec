#
# spec file for package ghc-retry
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


%global pkg_name retry
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        0.9.3.0
Release:        0
Summary:        Retry combinators for monadic actions that may fail
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-exceptions-devel
BuildRequires:  ghc-mtl-compat-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-random-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-unliftio-core-devel
ExcludeArch:    %{ix86}
%if %{with tests}
BuildRequires:  ghc-HUnit-devel
BuildRequires:  ghc-hedgehog-devel
BuildRequires:  ghc-stm-devel
BuildRequires:  ghc-tasty-devel
BuildRequires:  ghc-tasty-hedgehog-devel
BuildRequires:  ghc-tasty-hunit-devel
BuildRequires:  ghc-time-devel
%endif

%description
This package exposes combinators that can wrap arbitrary monadic actions.
They run the action and potentially retry running it with some configurable
delay for a configurable number of times. The purpose is to make it easier to
work with IO and especially network IO actions that often experience temporary
failure and warrant retrying of the original action. For example, a database
query may time out for a while, in which case we should hang back for a bit and
retry the query instead of simply raising an exception.

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

%check
%cabal_test

%post devel
%ghc_pkg_recache

%postun devel
%ghc_pkg_recache

%files -f %{name}.files
%license LICENSE

%files devel -f %{name}-devel.files
%doc README.md changelog.md

%changelog
