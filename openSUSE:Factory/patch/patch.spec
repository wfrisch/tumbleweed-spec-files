#
# spec file for package patch
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


Name:           patch
Version:        2.7.6
Release:        0
Summary:        GNU patch
License:        GPL-3.0-or-later
Group:          Productivity/Text/Utilities
URL:            http://ftp.gnu.org/gnu/patch/
Source:         http://ftp.gnu.org/gnu/patch/%{name}-%{version}.tar.xz
Source2:        http://ftp.gnu.org/gnu/patch/%{name}-%{version}.tar.xz.sig
# https://savannah.gnu.org/people/viewgpg.php?user_id=15000
Source3:        patch.keyring
Patch1:         fix-segfault-mangled-rename.patch
Patch2:         ed-style-01-missing-input-files.patch
Patch3:         ed-style-02-fix-arbitrary-command-execution.patch
Patch4:         ed-style-03-update-test-Makefile.patch
Patch5:         ed-style-04-invoke-ed-directly.patch
Patch6:         ed-style-05-minor-cleanups.patch
Patch7:         ed-style-06-fix-test-failure.patch
Patch8:         ed-style-07-dont-leak-tmp-file.patch
Patch9:         ed-style-08-dont-leak-tmp-file-multi.patch
Patch10:        fix-swapping-fake-lines-in-pch_swap.patch
Patch11:        abort-when-cleaning-up-fails.patch
Patch12:        dont-follow-symlinks-unless-asked.patch
Patch13:        pass-the-correct-stat-to-backup-files.patch
# See bnc#662957. The fix for CVE-2010-4651 breaks the way interdiff was
# invoking patch, so interdiff had to be fixed too.
Conflicts:      patchutils < 0.3.2
BuildRequires:  ed
%if 0%{?suse_version} < 1220
BuildRequires:  xz
%endif

%description
The GNU patch program is used to apply diffs between original and
changed files (generated by the diff command) to the original files.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1

%build
export CFLAGS="%{optflags} -Wall -O2 -pipe"
%configure
make %{?_smp_mflags}

%check
make %{?_smp_mflags} check

%install
make install DESTDIR=%{buildroot}

%files
%doc AUTHORS NEWS README
%license COPYING
%{_bindir}/patch
%{_mandir}/man1/patch.1%{ext_man}

%changelog
