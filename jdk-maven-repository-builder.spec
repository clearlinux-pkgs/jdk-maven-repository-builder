#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : jdk-maven-repository-builder
Version  : 1.0
Release  : 2
URL      : http://repo1.maven.org/maven2/org/apache/maven/shared/maven-repository-builder/1.0/maven-repository-builder-1.0-source-release.zip
Source0  : http://repo1.maven.org/maven2/org/apache/maven/shared/maven-repository-builder/1.0/maven-repository-builder-1.0-source-release.zip
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: jdk-maven-repository-builder-data
BuildRequires : apache-maven
BuildRequires : apache-maven2
BuildRequires : javapackages-tools
BuildRequires : jdk-aether
BuildRequires : jdk-aopalliance
BuildRequires : jdk-apache-parent
BuildRequires : jdk-apache-resource-bundles
BuildRequires : jdk-atinject
BuildRequires : jdk-cdi-api
BuildRequires : jdk-commons-cli
BuildRequires : jdk-commons-codec
BuildRequires : jdk-commons-collections
BuildRequires : jdk-commons-compress
BuildRequires : jdk-commons-io
BuildRequires : jdk-commons-lang
BuildRequires : jdk-commons-lang3
BuildRequires : jdk-commons-logging
BuildRequires : jdk-doxia
BuildRequires : jdk-doxia-sitetools
BuildRequires : jdk-guava
BuildRequires : jdk-guice
BuildRequires : jdk-httpcomponents-client
BuildRequires : jdk-httpcomponents-core
BuildRequires : jdk-jdom
BuildRequires : jdk-jsoup
BuildRequires : jdk-jsr-305
BuildRequires : jdk-log4j
BuildRequires : jdk-maven-archiver
BuildRequires : jdk-maven-artifact-resolver
BuildRequires : jdk-maven-common-artifact-filters
BuildRequires : jdk-maven-compiler-plugin
BuildRequires : jdk-maven-filtering
BuildRequires : jdk-maven-invoker
BuildRequires : jdk-maven-jar-plugin
BuildRequires : jdk-maven-javadoc-plugin
BuildRequires : jdk-maven-parent
BuildRequires : jdk-maven-plugin-tools
BuildRequires : jdk-maven-remote-resources-plugin
BuildRequires : jdk-maven-reporting-api
BuildRequires : jdk-maven-resources-plugin
BuildRequires : jdk-maven-shared-components
BuildRequires : jdk-maven-shared-incremental
BuildRequires : jdk-maven-shared-utils
BuildRequires : jdk-objectweb-asm
BuildRequires : jdk-plexus-archiver
BuildRequires : jdk-plexus-build-api
BuildRequires : jdk-plexus-cipher
BuildRequires : jdk-plexus-classworlds
BuildRequires : jdk-plexus-cli
BuildRequires : jdk-plexus-compiler
BuildRequires : jdk-plexus-containers
BuildRequires : jdk-plexus-i18n
BuildRequires : jdk-plexus-interactivity
BuildRequires : jdk-plexus-interpolation
BuildRequires : jdk-plexus-io
BuildRequires : jdk-plexus-resources
BuildRequires : jdk-plexus-sec-dispatcher
BuildRequires : jdk-plexus-utils
BuildRequires : jdk-plexus-velocity
BuildRequires : jdk-qdox
BuildRequires : jdk-sisu
BuildRequires : jdk-slf4j
BuildRequires : jdk-snappy-java
BuildRequires : jdk-surefire
BuildRequires : jdk-velocity
BuildRequires : jdk-wagon
BuildRequires : jdk-xbean
BuildRequires : jdk-xmlunit
BuildRequires : lxml
BuildRequires : openjdk-dev
BuildRequires : python3
BuildRequires : six
BuildRequires : xmvn

%description
No detailed description available

%package data
Summary: data components for the jdk-maven-repository-builder package.
Group: Data

%description data
data components for the jdk-maven-repository-builder package.


%prep
%setup -q -n maven-repository-builder-1.0

find -name 'pom.xml' -exec sed \
-i 's/<artifactId>plexus-maven-plugin<\/artifactId>/<artifactId>plexus-component-metadata<\/artifactId>/' '{}' ';'
find -name 'pom.xml' -exec sed \
-i 's/<goal>descriptor<\/goal>/<goal>generate-metadata<\/goal>/' '{}' ';'
find -iname '*.jar' -delete
python3 /usr/share/java-utils/pom_editor.py pom_remove_dep :maven-project
python3 /usr/share/java-utils/pom_editor.py pom_remove_dep :maven-artifact-manager
python3 /usr/share/java-utils/pom_editor.py pom_add_dep org.apache.maven:maven-compat:3.3.3

%build
python3 /usr/share/java-utils/mvn_build.py -f

%install
xmvn-install  -R .xmvn-reactor -n maven-repository-builder -d %{buildroot}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/maven-repository-builder/maven-repository-builder.jar
/usr/share/maven-metadata/maven-repository-builder.xml
/usr/share/maven-poms/maven-repository-builder/maven-repository-builder.pom
