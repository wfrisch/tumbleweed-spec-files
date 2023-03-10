#
# spec file for package mingw32-cross-breakpad-tools
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


%define _branch_name pecoff-dwarf-2
%define _source_dir google-breakpad-%{_branch_name}
%define _mingw32_target i686-w64-mingw32
Name:           mingw32-cross-breakpad-tools
Version:        20140827
Release:        0
Summary:        An open-source multi-platform crash reporting system
License:        BSD-3-Clause
Group:          Development/Libraries
URL:            https://github.com/jon-turney/
# wget https://github.com/jon-turney/google-breakpad/archive/pecoff-dwarf-2.tar.gz -O google-breakpad-`date +%Y%m%d`.tar.gz
Source0:        google-breakpad-%{version}.tar.gz
Source1:        gen_sym_files.sh
Patch0:         0001-Add-cmake-script-to-build-host-tool.patch
Patch1:         make-canonical-path.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
An open-source multi-platform crash reporting system. The client library is not included
this package only provides the tools.

%prep
%setup -q -n %{_source_dir}
%patch0 -p1
%patch1 -p1

%build
%cmake

make %{?_smp_mflags}

%install
mkdir -p %{buildroot}%{_prefix}/%{_mingw32_target}/bin
mkdir -p %{buildroot}%{_bindir}

install -m 0755 build/dump_syms %{buildroot}%{_prefix}/%{_mingw32_target}/bin/dump_syms
install -m 0755 %{SOURCE1} %{buildroot}%{_prefix}/%{_mingw32_target}/bin/gen_sym_files

# create symlinks
for i in dump_syms gen_sym_files; do
	ln -s -v %{_prefix}/%{_mingw32_target}/bin/$i %{buildroot}%{_bindir}/%{_mingw32_target}-$i;
done

%files
%defattr(-,root,root)
%dir %{_prefix}/%{_mingw32_target}
%dir %{_prefix}/%{_mingw32_target}/bin/

%{_prefix}/%{_mingw32_target}/bin/dump_syms
%{_prefix}/%{_mingw32_target}/bin/gen_sym_files

%{_bindir}/%{_mingw32_target}-dump_syms
%{_bindir}/%{_mingw32_target}-gen_sym_files

%changelog
