#
# spec file for package sdl-ball
#
# Copyright (c) 2021 SUSE LLC
# Copyright Vincent Petry <PVince81@yahoo.fr>
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


Name:           sdl-ball
Version:        1.04
Release:        0
Summary:        A Free/OpenSource brick-breaking game with pretty graphics
License:        GPL-3.0-only
Group:          Amusements/Games/Action/Breakout
URL:            http://sdl-ball.sourceforge.net/
# Git-Clone:    https://github.com/DusteDdk/SDL-Ball
Source0:        https://sourceforge.net/projects/sdl-ball/files/sdl-ball/%{version}/SDL-Ball_%{version}_src.tar.xz
Source1:        %{name}.sh
BuildRequires:  dos2unix
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(SDL_image)
BuildRequires:  pkgconfig(SDL_mixer)
BuildRequires:  pkgconfig(SDL_ttf)
BuildRequires:  pkgconfig(sdl)
BuildRequires:  update-desktop-files

%description
SDL-Ball is a Free/OpenSource brick-breaking game.
It is written in C++ using SDL and OpenGL.

Your mission: To smash your way through a series of progressively harder
and more tricky levels. Your tools: Ultrakinetic titanium balls and your
trusty Gruntmazter-3000-Paddle edition.

Features:
* 50 levels.
* OpenGL eye candy.
* Lots of powerups and powerdowns.
* Powerup Shop - You get special coins for collecting powerups,
  you can spend them on more powerups.
* Highscores.
* Sound.
* Level editor.
* Themes - Selectable from options menu.
  Themes support loading new gfx,snd and levels.
  A theme can be partial, if a file is missing,
  it will be loaded from the default theme.
  You can even mix between gfx,snd and level themes!
* Controllable with Mouse/Keyboard/Joystick and WiiMote.
* Save and Load games
* Cool Introscreen
* Screenshot function

%prep
%setup -q -n SDL-Ball_src

# Convert to unix line end
find . -name "*.cpp" -exec dos2unix "{}" "+"

# Drop unneeded directories
rm -fr win32

%build
export CFLAGS="%{optflags}"
%make_build

%install
# install wrapper
mkdir -p %{buildroot}%{_bindir}
sed 's|@LIBEXECDIR@|%{_libexecdir}|' %{SOURCE1} > %{buildroot}%{_bindir}/%{name}
chmod 755 %{buildroot}%{_bindir}/%{name}

# install executable
install -Dm 0755 %{name} %{buildroot}%{_libexecdir}/%{name}/%{name}

# install data / themes
mkdir -p %{buildroot}%{_libexecdir}/%{name}/themes
for d in default dio-sound-theme ; do
    cp -a themes/$d %{buildroot}%{_libexecdir}/%{name}/themes/
done

# install icon
install -Dm 0644 themes/default/icon32.png %{buildroot}%{_datadir}/pixmaps/%{name}.png

# install .desktop file
%suse_update_desktop_file -i %{name}

# install meta data
install -Dm 0644 %{name}.appdata.xml %{buildroot}%{_datadir}/metainfo/%{name}.appdata.xml


%files
%license LICENSE.txt
%doc README
%dir %{_datadir}/metainfo
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/metainfo/%{name}.appdata.xml
%{_datadir}/pixmaps/%{name}.png
%{_libexecdir}/%{name}

%changelog
