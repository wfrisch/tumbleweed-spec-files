#
# spec file for package orthos2
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


Name:           orthos2
Version:        1.2.77+git.f8950eb
Release:        0
Summary:        Machine administration
URL:            https://github.com/openSUSE/orthos2

Group:          Productivity/Networking/Boot/Servers
%{?systemd_ordering}

License:        GPL-2.0-or-later
Source:         orthos2-%{version}.tar.gz
%if 0%{?suse_version}
Source1:        orthos2.rpmlintrc
%endif
BuildArch:      noarch

BuildRequires:  fdupes
BuildRequires:  systemd-rpm-macros
# For /etc/nginx{,/conf.d} creation
BuildRequires:  nginx
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Requires(post): sudo
%if 0%{?suse_version}
BuildRequires:  python-rpm-macros
%endif

# Finds python dependencies based on egg info generated by setup.py
# Theoretically distro independent and should work this way, but has
# quite some pitfalls. Only works after SLE 15 SP2, due to build service
# restrictions (be careful, there they messed it up and
# python_enable_dependency_generator macro is defined, but does not do
# anything. This check still also needs to explicitly check for SLE 15 SP2...
%if 0%{?sle_version} <= 150200
%undefine python_enable_dependency_generator
%undefine python_disable_dependency_generator
%endif
%{?python_enable_dependency_generator}
%if ! (%{defined python_enable_dependency_generator} || %{defined python_disable_dependency_generator})
Requires:       python3-django >= 3.2
Requires:       python3-django-auth-ldap
Requires:       python3-django-extensions
Requires:       python3-djangorestframework
Requires:       python3-ldap
Requires:       python3-netaddr
Requires:       python3-paramiko
Requires:       python3-psycopg2
Requires:       python3-validators

%endif
# Needed to install /etc/logrotate.d/orthos2
Requires:       logrotate
Requires:       /sbin/service
Requires:       ansible
Requires:       nginx
Requires:       uwsgi
Requires:       uwsgi-python3

Provides:       orthos2-%{version}-%{release}

%description
Orthos is the machine administration tool of the development network at SUSE. It is used for following tasks:

    getting the state of the machine
    overview about the hardware
    overview about the installed software (installations)
    reservation of the machines
    generating the DHCP configuration (via Cobbler)
    reboot the machines remotely
    managing remote (serial) consoles

%package docs
Summary:        HTML documentation for orthos2
#BuildRequires:  python3-django >= 3.2
BuildRequires:  python3-django-auth-ldap
BuildRequires:  python3-Sphinx
BuildRequires:  python3-django-extensions
BuildRequires:  python3-djangorestframework
BuildRequires:  python3-ldap
BuildRequires:  python3-netaddr
BuildRequires:  python3-paramiko
BuildRequires:  python3-sphinx_rtd_theme
BuildRequires:  python3-validators

%define orthos_web_docs /srv/www/orthos2/docs

%description docs
HTML documentation that can be put into a web servers htdocs directory for publishing.

%prep
%setup

%build
%py3_build
cd docs
make html

%install
%py3_install

# docs
mkdir -p %{buildroot}%{orthos_web_docs}

# client is built via separate spec file to reduce build dependencies
rm %{buildroot}/usr/bin/orthos2

cp -r docs/_build/html/* %{buildroot}%{orthos_web_docs}
%fdupes %{buildroot}/%{orthos_web_docs}

#systemd
%if 0%{?suse_version}
mkdir -p %{buildroot}%{_sbindir}
ln -sf service %{buildroot}%{_sbindir}/rcorthos2_taskmanager
ln -sf service %{buildroot}%{_sbindir}/rcorthos2
ln -sf service %{buildroot}%{_sbindir}/rcorthos2_debug
%endif
# This should go into setup.py - but copying tons of non *.py files recursively
# is cumbersome...
cp -r orthos2/frontend/static /%{buildroot}/%{python3_sitelib}/orthos2/frontend
# ToDo: Try to separate the html templates somewhere else
cp -r templates/* %{buildroot}/%{python3_sitelib}/orthos2
ln -sr %{buildroot}%{python3_sitelib}/orthos2 %{buildroot}/usr/lib/orthos2/orthos2
mkdir -p %{buildroot}/usr/share/orthos2/data_migrations
mkdir -p %{buildroot}/usr/share/orthos2/taskmanager_migrations
mkdir -p %{buildroot}/usr/share/orthos2/frontend_migrations
mkdir -p %{buildroot}/usr/share/orthos2/api_migrations
ln -sr %{buildroot}/usr/share/orthos2/data_migrations %{buildroot}%{python3_sitelib}/orthos2/data/migrations
ln -sr %{buildroot}/usr/share/orthos2/taskmanager_migrations %{buildroot}%{python3_sitelib}/orthos2/taskmanager/migrations
ln -sr %{buildroot}/usr/share/orthos2/frontend_migrations %{buildroot}%{python3_sitelib}/orthos2/frontend/migrations
ln -sr %{buildroot}/usr/share/orthos2/api_migrations %{buildroot}%{python3_sitelib}/orthos2/api/migrations

cp -r ansible %{buildroot}/usr/lib/orthos2/ansible

%pre
getent group orthos >/dev/null || groupadd -r orthos
getent passwd orthos >/dev/null || \
    useradd -r -g orthos -d /var/lib/orthos2 -s /bin/bash \
    -c "Useful comment about the purpose of this account" orthos
%service_add_pre orthos2.service orthos2_taskmanager.service orthos2.socket orthos2_debug.service

%post
%tmpfiles_create %{_tmpfilesdir}/%{name}.conf
%service_add_post orthos2.service orthos2_taskmanager.service orthos2.socket orthos2_debug.service

sudo -i -u orthos /usr/lib/orthos2/manage.py makemigrations
sudo -i -u orthos /usr/lib/orthos2/manage.py migrate
sudo -i -u orthos /usr/lib/orthos2/manage.py collectstatic --noinput

%preun
%service_del_preun  orthos2.service orthos2_taskmanager.service orthos2.socket orthos2_debug.service

%postun
%service_del_postun  orthos2.service orthos2_taskmanager.service orthos2.socket orthos2_debug.service

%files
%{python3_sitelib}/orthos2-*
%_unitdir/orthos2_taskmanager.service
%_unitdir/orthos2.service
%_unitdir/orthos2_debug.service
%_unitdir/orthos2.socket
%if 0%{?suse_version}
%{_sbindir}/rcorthos2_taskmanager
%{_sbindir}/rcorthos2
%{_sbindir}/rcorthos2_debug
%endif
%{_tmpfilesdir}/orthos2.conf
%dir %{python3_sitelib}/orthos2/
%{python3_sitelib}/orthos2/*
%dir %{_sysconfdir}/orthos2
%config %{_sysconfdir}/orthos2/orthos2.ini
%config %{_sysconfdir}/orthos2/settings
%config %{_sysconfdir}/logrotate.d/orthos2
%config(noreplace) %{_sysconfdir}/nginx/conf.d/orthos2_docs_nginx.conf
%config(noreplace) %{_sysconfdir}/nginx/conf.d/orthos2_nginx.conf
%dir /usr/lib/orthos2
%dir /usr/lib/orthos2/scripts
%dir /usr/share/orthos2
%dir /usr/share/orthos2/fixtures
/usr/share/orthos2/fixtures/*
# The migrations link has to be owned by orthos user:
# /usr/lib/python3.8/site-packages/orthos2/data ->
#      /usr/share/orthos2/data/migrations
# Like this:
# sudo -u orthos /usr/lib/orthos2/manage.py makemigrations
# has rights to dump migrations into site-packages subdir
%attr(755,orthos,orthos) /usr/share/orthos2/data_migrations
%attr(755,orthos,orthos) /usr/share/orthos2/taskmanager_migrations
%attr(755,orthos,orthos) /usr/share/orthos2/frontend_migrations
%attr(755,orthos,orthos) /usr/share/orthos2/api_migrations
/usr/lib/orthos2/*
%attr(755,orthos,orthos) %dir /srv/www/orthos2
%ghost %dir /run/%{name}
%ghost %dir /run/%{name}/ansible
%ghost %dir /run/%{name}/ansible_lastrun
%ghost %dir /run/%{name}/ansible_archive
%attr(755,orthos,orthos) %dir /var/log/orthos2
%attr(775,orthos,orthos) %dir /var/lib/orthos2
%attr(775,orthos,orthos) %dir /var/lib/orthos2/archiv
%attr(775,orthos,orthos) %dir /var/lib/orthos2/orthos-vm-images
%attr(775,orthos,orthos) %dir /var/lib/orthos2/database
%attr(700,orthos,orthos) %dir /var/lib/orthos2/.ssh

# defattr(fileattr, user, group, dirattr)
# Add whole ansible directory with correct attr for dirs and files
# Always keep this at the end with defattr
%defattr(664, orthos, orthos, 775)
/usr/lib/orthos2/ansible

%files docs
%dir %{orthos_web_docs}
%{orthos_web_docs}/*

%changelog