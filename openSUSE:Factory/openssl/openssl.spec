#
# spec file for package openssl
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define _sonum  1_1
Name:           openssl
Version:        1.1.1s
Release:        0
Summary:        Secure Sockets and Transport Layer Security
# Yes there is no license. But, to not confuse people, keep it aligned to the pkg
License:        OpenSSL
Group:          Productivity/Networking/Security
URL:            https://www.openssl.org/
Source0:        README.SUSE
Source99:       baselibs.conf
BuildRequires:  libopenssl%{_sonum} = %{version}
Requires:       openssl-%{_sonum} = %{version}
# the debuginfo package is now openssl-%%{_sonum}-debuginfo (boo#1040172)
Obsoletes:      openssl-debuginfo
BuildArch:      noarch
Provides:       openssl(cli)

%description
OpenSSL is a software library to be used in applications that need to
secure communications over computer networks against eavesdropping or
need to ascertain the identity of the party at the other end.
OpenSSL contains an implementation of the SSL and TLS protocols.

%package -n libopenssl-devel
Summary:        Development files for OpenSSL
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       libopenssl%{_sonum} = %{version}
Requires:       libopenssl-%{_sonum}-devel = %{version}
Requires:       pkgconfig
Obsoletes:      openssl-devel < %{version}
Provides:       openssl-devel = %{version}
Provides:       pkgconfig(libssl) = %{version}
Provides:       pkgconfig(libopenssl) = %{version}
Provides:       pkgconfig(libcrypto) = %{version}
Provides:       pkgconfig(openssl) = %{version}

%description -n libopenssl-devel
This package is a dummy package that always depends on the
version of corresponding openssl packages that openSUSE
currently supports.

%prep
cp %{SOURCE0} .

%build
:

%install
:

%files
%doc README.SUSE

%files -n libopenssl-devel
%doc README.SUSE

%changelog
