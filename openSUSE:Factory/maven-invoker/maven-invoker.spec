#
# spec file for package maven-invoker
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


Name:           maven-invoker
Version:        3.1.0
Release:        0
Summary:        An API for firing a maven build in a clean environment
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://maven.apache.org/shared/maven-invoker/
Source0:        https://repo1.maven.org/maven2/org/apache/maven/shared/%{name}/%{version}/%{name}-%{version}-source-release.zip
Source1:        %{name}-build.xml
# Patch rejected upstream
Patch1:         %{name}-MSHARED-279.patch
BuildRequires:  ant
BuildRequires:  atinject
BuildRequires:  fdupes
BuildRequires:  javapackages-local
BuildRequires:  maven-shared-utils >= 3.3.3
BuildRequires:  sisu-inject
BuildRequires:  unzip
Requires:       mvn(org.apache.maven.shared:maven-shared-utils)
Requires:       mvn(org.eclipse.sisu:org.eclipse.sisu.inject)
BuildArch:      noarch

%description
This API is concerned with firing a Maven build in a new JVM. It accomplishes
its task by building up a conventional Maven command line from options given in
the current request, along with those global options specified in the invoker
itself. Once it has the command line, the invoker will execute it, and capture
the resulting exit code or any exception thrown to signal a failure to execute.
Input/output control can be specified using an InputStream and up to two
InvocationOutputHandlers.

This is a replacement package for maven-shared-invoker

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
API documentation for %{name}.

%prep
%setup -q
sed -i 's/\r$//' src/main/java/org/apache/maven/shared/invoker/MavenCommandLineBuilder.java
cp %{SOURCE1} build.xml
%patch1 -p1
%pom_change_dep javax.inject:javax.inject:1  org.eclipse.sisu:org.eclipse.sisu.inject

%pom_remove_parent .
%pom_xpath_inject pom:project "<groupId>org.apache.maven.shared</groupId>" .

%build
mkdir -p lib
build-jar-repository -s lib maven-shared-utils org.eclipse.sisu.inject atinject
%{ant} jar javadoc

%install
# jar
install -dm 0755 %{buildroot}%{_javadir}/%{name}
install -pm 0644 target/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}/%{name}.jar
# pom
install -dm 0755 %{buildroot}%{_mavenpomdir}/%{name}
install -pm 0644 pom.xml %{buildroot}%{_mavenpomdir}/%{name}/%{name}.pom
%add_maven_depmap %{name}/%{name}.pom %{name}/%{name}.jar
# javadoc
install -dm 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}/
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE NOTICE

%files javadoc
%license LICENSE NOTICE
%{_javadocdir}/%{name}

%changelog
