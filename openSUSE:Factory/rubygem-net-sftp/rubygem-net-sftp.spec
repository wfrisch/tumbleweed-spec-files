#
# spec file for package rubygem-net-sftp
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


%define mod_name net-sftp
%define mod_full_name %{mod_name}-%{version}
#
# This file was generated with a gem2rpm.yml and not just plain gem2rpm.
# All sections marked as MANUAL, license headers, summaries and descriptions
# can be maintained in that file. Please consult this file before editing any
# of those fields
#
Name:           rubygem-net-sftp
Version:        4.0.0
Release:        0
Summary:        A pure Ruby implementation of the SFTP client protocol
License:        MIT
Group:          Development/Languages/Ruby
URL:            https://github.com/net-ssh/net-sftp
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Source1:        gem2rpm.yml
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  %{ruby}
BuildRequires:  ruby-macros >= 5

%description
A pure Ruby implementation of the SFTP client protocol.

%prep

%build

%install
%gem_install \
  --doc-files="CHANGES.txt LICENSE.txt README.rdoc" \
  -f
# MANUAL
find %{buildroot}/%{_libdir}/ruby/gems/ \( -name '.github' -o -name '.gitignore' \) | xargs rm -rf
# /MANUAL


%gem_packages

%changelog
