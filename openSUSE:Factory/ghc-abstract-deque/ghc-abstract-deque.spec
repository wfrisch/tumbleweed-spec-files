#
# spec file for package ghc-abstract-deque
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


%global pkg_name abstract-deque
Name:           ghc-%{pkg_name}
Version:        0.3
Release:        0
Summary:        Abstract, parameterized interface to mutable Deques
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-array-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-random-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-time-devel
ExcludeArch:    %{ix86}

%description
An abstract interface to highly-parameterizable queues/deques.

Background: There exists a feature space for queues that extends between:

* simple, single-ended, non-concurrent, bounded queues

* double-ended, threadsafe, growable queues

... with important points inbetween (such as the queues used for
work-stealing).

This package includes an interface for Deques that allows the programmer to use
a single API for all of the above, while using the type-system to select an
efficient implementation given the requirements (using type families).

This package also includes a simple reference implementation based on 'IORef'
and "Data.Sequence".

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

%post devel
%ghc_pkg_recache

%postun devel
%ghc_pkg_recache

%files -f %{name}.files
%license LICENSE

%files devel -f %{name}-devel.files

%changelog
