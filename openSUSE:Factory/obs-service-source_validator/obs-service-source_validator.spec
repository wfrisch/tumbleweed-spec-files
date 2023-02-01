#
# spec file for package obs-service-source_validator
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


Name:           obs-service-source_validator
Version:        0.28
Release:        0
Summary:        An OBS source service: running all the osc source-validator checks
License:        GPL-2.0-or-later
Group:          Development/Tools/Building
URL:            https://github.com/openSUSE/obs-service-source_validator
# use osc service dr to update
Source:         %{name}-%{version}.tar.zst
BuildRequires:  build
BuildRequires:  zstd
Requires:       %{_bindir}/xmllint
Requires:       build
Requires:       patch
Requires:       perl-TimeDate
Provides:       osc-source_validator = %{version}
Obsoletes:      osc-source_validator <= 0.1
BuildArch:      noarch
%if 0%{?suse_version}
Requires:       gpg2
%else
# Fedora
Requires:       gnupg2
%endif
%if 0%{?suse_version} > 1210 || 0%{?centos_version} > 500
Requires:       rpm-build
%endif

%description
This is a source service for openSUSE Build Service.

This service runs all checks as required by openSUSE:Factory project. This can be used
to guarantee that all checks succeed also on the service side. This plugin can be
used via project wide defined services.

%prep
%setup -q

%build
:

%install
mkdir -p %{buildroot}%{_datadir}/licenses
%make_install

%check
%make_build test

%files
%license COPYING
%if 0%{?suse_version} <= 1320
%dir %{_datadir}/licenses
%endif
%dir %{_prefix}/lib/obs
%{_prefix}/lib/obs/service

%changelog
