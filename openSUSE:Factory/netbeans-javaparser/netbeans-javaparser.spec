#
# spec file for package netbeans-javaparser
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


# Prevent brp-java-repack-jars from being run.
%define __jar_repack %{nil}
Name:           netbeans-javaparser
Version:        6.8
Release:        0
Summary:        NetBeans Java Parser
License:        GPL-2.0-with-classpath-exception
Group:          Development/Libraries/Java
URL:            http://java.netbeans.org/javaparser/
# The source for this package was pulled from upstream's vcs.  Use the
# following commands to generate the tarball:
# hg clone http://hg.netbeans.org/main/nb-javac/
# cd nb-javac/
# hg update -r 1c46268162cd
# tar -czvf ../nb-javac-6.8.tar.gz .
Source0:        nb-javac-%{version}.tar.bz2
BuildRequires:  ant
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-tools
Requires:       java >= 1.8
Requires:       javapackages-tools
BuildArch:      noarch

%description
Java parser to analyse Java source files inside of the NetBeans IDE

%prep
%setup -q -c
# remove all binary libs
find . -name "*.jar" -exec rm -f {} \;

%build
%{ant} \
    -f make/netbeans/nb-javac/build.xml \
    -Djavac.source=1.8 -Djavac.target=1.8 \
    jar

%install
# jar
install -d -m 755 %{buildroot}%{_javadir}
install -m 644 make/netbeans/nb-javac/dist/javac-api.jar %{buildroot}%{_javadir}/%{name}-api.jar
install -m 644 make/netbeans/nb-javac/dist/javac-impl.jar %{buildroot}%{_javadir}/%{name}-impl.jar

%files
%license LICENSE ASSEMBLY_EXCEPTION
%doc ASSEMBLY_EXCEPTION README
%{_javadir}/*

%changelog
