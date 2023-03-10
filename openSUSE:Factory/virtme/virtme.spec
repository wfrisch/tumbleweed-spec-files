#
# spec file
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


%define name virtme
%define version 0.1.1
%define skip_python2 1

Name:           %{name}
Version:        %{version}
Release:        0
Summary:        Tools for virtualize the running distro or a rootfs
License:        GPL-2.0-only
Group:          Development/Tools/Other
URL:            https://git.kernel.org/cgit/utils/kernel/virtme/virtme.git
Source0:        https://git.kernel.org/pub/scm/utils/kernel/virtme/virtme.git/snapshot/%{name}-%{version}.tar.gz
Patch1:         0001-Add-save-initramfs-to-save-the-actual-generated-init.patch
Patch2:         0002-Make-save-initramfs-show-command-output-more-useful.patch
Patch3:         0003-Fix-the-error-message-for-mods-misuse.patch
Patch4:         0004-Fix-the-mods-error-even-better.patch
Patch5:         0005-mkinitramfs.py-Search-for-busybox-.-static-first.patch
Patch6:         0006-mkinitramfs-Improve-the-find_busybox-algorithm.patch
Patch7:         0007-Add-util.find_binary-to-find-binaries.patch
Patch8:         0008-modfinder-Use-find_binary_or_raise-to-find-modprobe.patch
Patch9:         0009-Enable-the-Xen-console-when-using-xen.patch
Patch10:        0001-configkernel-Add-CONFIG_INOTIFY_USER-y.patch
Patch11:        0002-Use-fsdev-multidevs-remap-on-QEMU-4.2.patch
Patch12:        0003-Add-more-typing-annotations.patch
Patch13:        0004-run.py-Extract-path-file-sanitizing-into-a-new-funct.patch
Patch14:        0005-run.py-Introduce-blk-disk-argument.patch
Patch15:        0006-Minor-sanitize_disk_args-cleanup.patch
Patch16:        aarch64-Fix-aarch64-support.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
Requires:       busybox-static
Requires:       qemu
BuildArch:      noarch

%description
Virtme is a set of tools to run a virtualized Linux kernel that
uses the host Linux distribution or a rootfs instead of a whole
disk image.

Right now it is not really configurable enough for being useful as a
sort of sandbox.

%prep
%autosetup -n %{name}-%{version} -p1

%build
%py3_build
# remove pycache directories
find . -name __pycache__ -type d -exec rm -fr {} +

%install
export PYTHONDONTWRITEBYTECODE=1 %py3_install

%files
%{_bindir}/virtme-configkernel
%{_bindir}/virtme-mkinitramfs
%{_bindir}/virtme-prep-kdir-mods
%{_bindir}/virtme-run
%{python_sitelib}/%{name}
%{python_sitelib}/%{name}-%{version}-py*.egg-info

%changelog
