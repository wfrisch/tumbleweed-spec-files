#
# spec file
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


%global flavor @BUILD_FLAVOR@%{nil}
%global pkgname eigen3
%global srcname eigen

# The OpenGL support test fails
%bcond_with opengl_test

# Tests fail for different reasons within the test-suite itself; disable for now
# See e.g. https://gitlab.com/libeigen/eigen/-/issues/2088, https://gitlab.com/libeigen/eigen/-/issues/2092
# Also balloons the resources required: > 32 GiB disk space + >= 12 GiB memory
%bcond_with tests

%if "%{flavor}" == "docs"
%define pkgsuffix -doc
%endif

Name:           eigen3%{?pkgsuffix}
Version:        3.4.0
Release:        0
Summary:        C++ Template Library for Linear Algebra
License:        BSD-3-Clause AND LGPL-2.1-only AND MPL-2.0 AND LGPL-2.1-or-later
URL:            http://eigen.tuxfamily.org/
Source0:        https://gitlab.com/libeigen/eigen/-/archive/%{version}/%{srcname}-%{version}.tar.bz2
Patch0:         0001-Disable-Altivec-for-ppc64le.patch
Patch1:         0001-Do-stack-allignment-on-ppc.patch
# PATCH-FIX-UPSTREAM -- https://gitlab.com/libeigen/eigen/-/merge_requests/680.patch
Patch2:         fix_ppc64le_always_inline_680.patch
%if %{with tests}
# SECTION Patches to fix tests
# PATCH-FIX-UPSTREAM eigen3-googlehash-detection.patch badshah400@gmail.com -- GoogleHash needs C++11 std to compile test code and be succesfully detected
Patch9:         eigen3-googlehash-detection.patch
# PATCH-FIX-UPSTREAM eigen3-fix-forward_adolc-unit-test.patch badshah400@gmail -- Prevent conflict of std::min/max with eigen's macros by importing eigen test-suite's main.h header only after all system headers have been included
Patch10:        eigen3-fix-forward_adolc-unit-test.patch
# /SECTION
%endif
BuildRequires:  adolc-devel
BuildRequires:  cmake
BuildRequires:  fftw3-devel
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
BuildRequires:  gmp-devel
BuildRequires:  gsl-devel
BuildRequires:  libboost_headers-devel
BuildRequires:  metis-devel
BuildRequires:  mpfr-devel
BuildRequires:  pkg-config
BuildRequires:  sparsehash-devel
BuildRequires:  suitesparse-devel
BuildRequires:  superlu-devel
%if "%{flavor}" == "docs"
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  graphviz
BuildRequires:  graphviz-gd
BuildRequires:  texlive-dvips
BuildRequires:  texlive-latex
BuildRequires:  tex(newunicodechar.sty)
%endif
%if %{with opengl_test}
BuildRequires:  freeglut-devel
BuildRequires:  glew-devel
BuildRequires:  pkgconfig(gl)
%endif
BuildArch:      noarch

%description
Eigen is a C++ template library for linear algebra: matrices, vectors,
numerical solvers, and related algorithms.

%package devel
Summary:        C++ Template Library for Linear Algebra
# libeigen3-devel was last used at openSUSE 13.1 (version 3.2.0)
Provides:       libeigen3-devel = %{version}
Obsoletes:      libeigen3-devel < %{version}

%description devel
Eigen is a C++ template library for linear algebra: matrices, vectors,
numerical solvers, and related algorithms.

%if "%{flavor}" == "docs"
Summary:        Documentation for the Eigen3 C++ Template Library for Linear Algebra

%description
Documentation in HTML format for the Eigen3 C++ Template Library
for Linear Algebra
%endif

%prep
%autosetup -p1 -n %{srcname}-%{version}

# Fix rpmlint warning "wrong-file-end-of-line-encoding"
sed -i 's/\r$//' COPYING.MINPACK

# Remove build time references so build-compare can do its work
echo "HTML_TIMESTAMP = NO" >> doc/Doxyfile.in

%build
%cmake \
 -DINCLUDE_INSTALL_DIR:PATH=include/eigen3 \
 -DCMAKE_SKIP_RPATH:BOOL=OFF \
 -DCMAKE_SKIP_INSTALL_RPATH:BOOL=ON \
 -DEIGEN_TEST_CXX11:Bool=%{?with_tests:ON}%{!?with_tests:OFF} \
 -DEIGEN_TEST_OPENMP:Bool=%{?with_tests:ON}%{!?with_tests:OFF}

%if "%{flavor}" == ""
%cmake_build all %{?with_tests:buildtests}
%else
%cmake_build doc
%endif

rm -f doc/html/*.tgz
find doc -name _formulas.log -print -delete

%install
%if "%{flavor}" == ""
%cmake_install
%else
%fdupes -s build/doc/html/
%endif

%if "%{flavor}" == ""
%if %{with tests}
%check
# Run with a fixed seed to prevent random failures: https://gitlab.com/libeigen/eigen/-/issues/2088
export EIGEN_SEED=100
# Repeat each test once to reduce time spent, since we use a fixed seed anyway
export EIGEN_REPEAT=1
%ctest
%endif
%endif

%if "%{flavor}" == "docs"
%files
%doc build/doc/html/

%else

%files devel
%license COPYING.*
%{_includedir}/eigen3/
%{_datadir}/eigen3/
%{_datadir}/pkgconfig/eigen3.pc

%endif

%changelog
