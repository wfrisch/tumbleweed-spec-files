#
# spec file for package tmon
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


Name:           tmon
# Use this as version when things are in mainline kernel
Version:        1.0.gb61442df748f06e9
Release:        0
Summary:        A Monitoring and Testing Tool for Linux kernel thermal subsystem
License:        GPL-2.0-only
Group:          System/Base
URL:            https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/tools/thermal/tmon
Source:         %{name}-%{version}.tar.xz
Patch0:         remove_external_includes
BuildRequires:  ncurses-devel
BuildRequires:  pkgconfig

%description
This tool is conceived as a tool to help visualize, tune, and test the
complex thermal subsystem.

%prep
%autosetup

%build
CFLAGS="%{optflags}" make %{?_smp_mflags}

%install
make install INSTALL_ROOT=%{buildroot}
install -D -m 644 tmon.8 %{buildroot}%{_mandir}/man8/tmon.8

%files
%{_bindir}/tmon
%{_mandir}/man8/tmon.8%{?ext_man}

%changelog
