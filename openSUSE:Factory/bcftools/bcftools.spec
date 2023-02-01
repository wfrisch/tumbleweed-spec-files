#
# spec file for package bcftools
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


Name:           bcftools
Version:        1.16
Release:        0
Summary:        Tools for manipulating variant calls in the Variant Call Format (VCF)
License:        MIT
Group:          Productivity/Scientific/Other
URL:            http://www.htslib.org/
# The “Source code” downloads links generated by GitHub and are incomplete as they don't bundle HTSlib and are missing some generated files
Source:         https://github.com/samtools/bcftools/releases/download/%{version}/bcftools-%{version}.tar.bz2
# PATCH-FIX-OPENSUSE use_python3.patch -- Use python3 executable instead of python2
Patch0:         use_python3.patch
BuildRequires:  automake
BuildRequires:  gsl-devel
BuildRequires:  libbz2-devel
BuildRequires:  libhts-devel >= %{version}
BuildRequires:  lzma-devel
BuildRequires:  zlib-devel
Requires:       bgzip
Requires:       htsfile
Requires:       perl
Requires:       python3-base
Requires:       python3-matplotlib
Requires:       tabix

%description
Package for the new BCFtools: a set of utilities that manipulate variant calls in the Variant Call Format (VCF)
and its binary counterpart BCF. It contains all the "vcf..." commands which previously lived in the HTSlib
repository (such as vcfcheck, vcfmerge, vcfisec, etc.) and the samtools BCF calling from bcftools subdirectory
of samtools. BCFtools are meant as a faster replacement for most of the perl VCFtools commands.

%prep
%autosetup -p1

%build
autoreconf -fi
%configure --with-htslib=system
%make_build USE_GSL=1

%install
%make_install prefix=%{_prefix} libexecdir=%{_libdir} libdir=%{_libdir}

# CONVERT env HASHBANGS TO USE DIRECT EXECUTABLE
sed -i "s:/usr/bin/env perl:%{_bindir}/perl:" %{buildroot}/%{_bindir}/*.pl %{buildroot}/%{_bindir}/plot-vcfstats
sed -i -E "s:/usr/bin/env python3?:%{_bindir}/python3:" %{buildroot}/%{_bindir}/*.py

%files
%license LICENSE
%doc AUTHORS README
%{_bindir}/bcftools
%{_bindir}/*.py
%{_bindir}/*.pl
%{_bindir}/plot-vcfstats
%{_libdir}/bcftools/
%{_mandir}/man1/*

%changelog
