#
# spec file for package noisetorch
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


Name:           noisetorch
Version:        0.12.2
Release:        0
Summary:        Real-time microphone noise suppression on Linux
License:        GPL-3.0-or-later
URL:            https://github.com/NoiseTorch/NoiseTorch
# osc service disabledrun
Source0:        NoiseTorch-%{version}.tar.gz
# osc service disabledrun
Source1:        vendor.tar.gz
BuildRequires:  c++_compiler
BuildRequires:  cmake
BuildRequires:  git-core
BuildRequires:  hicolor-icon-theme
BuildRequires:  golang(API) = 1.18

%description
NoiseTorch is an easy to use open source application for Linux with PulseAudio.
It creates a virtual microphone that suppresses noise, in any application. Use
whichever conferencing or VOIP application you like and simply select the
NoiseTorch Virtual Microphone as input to torch the sound of your mechanical
keyboard, computer fans, trains and the likes.

%prep
%autosetup -p1 -n NoiseTorch-%{version} -a1

%build
pushd c/ladspa
%make_build
ldd rnnoise_ladspa.so
popd
go generate
# -tags release would enable the auto-updater (update.go)

CGO_ENABLED=0 GOOS=linux go build \
%ifnarch ppc64
    -buildmode=pie \
%endif
    -a -ldflags '-w -X main.version=%{version} -X main.distribution=rpm' .

%install
install -D -m 644 assets/icon/noisetorch.png %{buildroot}/%{_datadir}/icons/hicolor/256x256/apps/noisetorch.png
install -D -m 644 assets/noisetorch.desktop %{buildroot}/%{_datadir}/applications/noisetorch.desktop
install -D -m 755 noisetorch %{buildroot}/%{_bindir}/noisetorch

%files
%license LICENSE
%doc README.md
%caps(cap_sys_resource+ep) %{_bindir}/noisetorch
%{_datadir}/applications/noisetorch.desktop
%{_datadir}/icons/hicolor/256x256/apps/noisetorch.png

%changelog
