#
# spec file for package jakarta-activation
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


%global artifact_name jakarta.activation-api
Name:           jakarta-activation
Version:        2.1.0
Release:        0
Summary:        Jakarta Activation Specification and Implementation
License:        BSD-3-Clause
URL:            https://eclipse-ee4j.github.io/jaf/
Source0:        https://github.com/eclipse-ee4j/jaf/archive/%{version}/jaf-%{version}.tar.gz
Source1:        %{name}-build.xml
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  java-devel >= 9
BuildRequires:  javapackages-local
BuildArch:      noarch

%description
Jakarta Activation lets you take advantage of standard services to:
determine the type of an arbitrary piece of data; encapsulate access to
it; discover the operations available on it; and instantiate the
appropriate bean to perform the operation(s).

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n jaf-%{version}
cp %{SOURCE1} api/build.xml

%pom_remove_parent api

%build
pushd api
%{ant} package javadoc
popd

%install
pushd api
# jars
mkdir -p %{buildroot}%{_javadir}/%{name}
cp -a target/%{artifact_name}-%{version}.jar %{buildroot}%{_javadir}/%{name}/%{artifact_name}.jar

#pom
install -d -m 755 %{buildroot}%{_mavenpomdir}/%{name}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/%{name}/%{artifact_name}.pom
%add_maven_depmap %{name}/%{artifact_name}.pom %{name}/%{artifact_name}.jar

# javadoc
mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -a target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}
popd

%fdupes -s %{buildroot}%{_javadocdir}

%files -f api/.mfiles
%doc README.md
%license LICENSE.md NOTICE.md

%files javadoc
%{_javadocdir}/%{name}
%license LICENSE.md NOTICE.md

%changelog
