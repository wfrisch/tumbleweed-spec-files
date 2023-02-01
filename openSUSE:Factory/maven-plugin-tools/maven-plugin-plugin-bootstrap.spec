#
# spec file
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


%global base_name maven-plugin-tools
%global artifactId maven-plugin-plugin
Name:           %{artifactId}-bootstrap
Version:        3.6.0
Release:        0
Summary:        Maven Plugin Plugin
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            http://maven.apache.org/plugin-tools/
Source0:        http://repo2.maven.org/maven2/org/apache/maven/plugin-tools/%{base_name}/%{version}/%{base_name}-%{version}-source-release.zip
Source1:        %{base_name}-build.tar.xz
Patch0:         0001-Avoid-duplicate-MOJO-parameters.patch
Patch1:         0002-Deal-with-nulls-from-getComment.patch
Patch2:         0003-Port-to-plexus-utils-3.0.24.patch
# The maven-plugin-plugin is used to generate those descriptors, which
# creates a circular dependency of maven-plugin-plugin on itself.
# We generated those ones outside the rpm build for a bootstrap package.
Patch20:        maven-plugin-plugin-bootstrap-resouces.patch
BuildRequires:  ant
BuildRequires:  javapackages-local
BuildRequires:  maven-doxia-logging-api
BuildRequires:  maven-doxia-sink-api
BuildRequires:  maven-doxia-sitetools
BuildRequires:  maven-lib
BuildRequires:  maven-plugin-annotations
BuildRequires:  maven-plugin-registry
BuildRequires:  maven-plugin-tools-api
BuildRequires:  maven-plugin-tools-generators
BuildRequires:  maven-reporting-api
BuildRequires:  maven-reporting-impl
BuildRequires:  modello >= 2.0.0
BuildRequires:  plexus-containers-container-default
BuildRequires:  plexus-utils
BuildRequires:  plexus-velocity
BuildRequires:  unzip
BuildRequires:  velocity
BuildRequires:  xmvn-install
BuildRequires:  xmvn-resolve
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-tools-annotations)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-tools-java)
BuildRequires:  mvn(org.apache.maven:maven-parent:pom:)
BuildArch:      noarch

%description
The Plugin Plugin is used to create a Maven plugin descriptor for any Mojo's
found in the source tree, to include in the JAR. It is also used to generate
Xdoc files for the Mojos as well as for updating the plugin registry, the
artifact metadata and a generic help goal.

%prep
%setup -q -n %{base_name}-%{version} -a1
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch20 -p1

%pom_remove_plugin -r :maven-enforcer-plugin

%pom_xpath_inject "pom:project/pom:properties" "
    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    <project.reporting.outputEncoding>UTF-8</project.reporting.outputEncoding>"

# Why on the earth is this dependency there ???
%pom_remove_dep :maven-surefire-common maven-plugin-plugin

# Remove test dependencies because tests are skipped anyways.
%pom_xpath_remove "pom:dependency[pom:scope='test']"

%pom_change_dep org.easymock:easymock:: :::test maven-plugin-tools-annotations

# For some reason, this dependency is not generated by javapackages-local
# and for some reasons if we give it a scope 'runtime' it works
%pom_remove_dep :maven-plugin-annotations maven-plugin-plugin
%pom_add_dep org.apache.maven.plugin-tools:maven-plugin-annotations:%{version}:runtime maven-plugin-plugin

%{mvn_package} :maven-plugin-tools __noinstall

%build
mkdir -p lib
build-jar-repository -s lib \
	maven-doxia/doxia-logging-api \
	maven-doxia/doxia-sink-api \
	maven-doxia-sitetools/doxia-site-renderer \
	maven/maven-artifact \
	maven/maven-compat \
	maven/maven-core \
	maven/maven-model \
	maven/maven-plugin-api \
	maven/maven-plugin-registry \
	maven/maven-repository-metadata \
	maven-plugin-tools/maven-plugin-annotations \
	maven-plugin-tools/maven-plugin-tools-api \
	maven-plugin-tools/maven-plugin-tools-generators \
	maven-reporting-api/maven-reporting-api \
	maven-reporting-impl/maven-reporting-impl \
	plexus-containers/plexus-container-default \
	plexus/utils \
	plexus-velocity/plexus-velocity \
	velocity

%{mvn_file} :%{artifactId} %{base_name}/%{artifactId}
pushd %{artifactId}
%ant \
	-Dtest.skip=true \
	jar
popd
%mvn_artifact pom.xml
%mvn_artifact %{artifactId}/pom.xml %{artifactId}/target/%{artifactId}-%{version}.jar

%install
%mvn_install

%files -f .mfiles
%license LICENSE NOTICE

%changelog
