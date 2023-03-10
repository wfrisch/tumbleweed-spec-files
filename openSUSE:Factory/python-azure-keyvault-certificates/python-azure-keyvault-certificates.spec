#
# spec file for package python-azure-keyvault-certificates
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%if 0%{?suse_version} >= 1500
%define skip_python2 1
%endif
Name:           python-azure-keyvault-certificates
Version:        4.6.0
Release:        0
Summary:        Microsoft Azure Key Vault Certificates Client Library for Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/Azure/azure-sdk-for-python
Source:         https://files.pythonhosted.org/packages/source/a/azure-keyvault-certificates/azure-keyvault-certificates-%{version}.zip
Source1:        LICENSE.txt
BuildRequires:  %{python_module azure-keyvault-nspkg >= 1.0.0}
BuildRequires:  %{python_module azure-nspkg >= 3.0.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Requires:       python-azure-common < 2.0.0
Requires:       python-azure-common >= 1.1
Requires:       python-azure-core < 2.0.0
Requires:       python-azure-core >= 1.20.0
Requires:       python-azure-keyvault-nspkg >= 1.0.0
Requires:       python-azure-nspkg >= 3.0.0
Requires:       python-msrest >= 0.6.21
Requires:       python-six >= 1.11.0
Conflicts:      python-azure-sdk <= 2.0.0

BuildArch:      noarch

%python_subpackages

%description
Azure Key Vault helps solve the following problems:

Certificate management (this library) - create, manage, and deploy public and
private SSL/TLS certificates Cryptographic key management (azure-keyvault-keys)
- create, store, and control access to the keys used to encrypt your data Secrets
management (azure-keyvault-secrets) - securely store and control access to tokens,
passwords, certificates, API keys, and other secrets.

%prep
%setup -q -n azure-keyvault-certificates-%{version}

%build
install -m 644 %{SOURCE1} %{_builddir}/azure-keyvault-certificates-%{version}
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%{python_expand # delete common files
rm -rf %{buildroot}%{$python_sitelib}/azure/keyvault/__init__.*
rm -rf %{buildroot}%{$python_sitelib}/azure/keyvault/__pycache__
rm -rf %{buildroot}%{$python_sitelib}/azure/__init__.*
rm -rf %{buildroot}%{$python_sitelib}/azure/__pycache__
}

%files %{python_files}
%defattr(-,root,root,-)
%doc CHANGELOG.md README.md
%license LICENSE.txt
%{python_sitelib}/azure/keyvault/certificates
%{python_sitelib}/azure_keyvault_certificates-*.egg-info

%changelog
