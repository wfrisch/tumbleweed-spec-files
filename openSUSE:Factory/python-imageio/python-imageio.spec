#
# spec file for package python-imageio
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


%{?!python_module:%define python_module() python3-%{**}}
%define skip_python2 1
%bcond_with test_extras
Name:           python-imageio
Version:        2.21.2
Release:        0
Summary:        Python library for reading and writing image, video, and related formats
License:        BSD-2-Clause
URL:            https://imageio.github.io/
Source0:        https://files.pythonhosted.org/packages/source/i/imageio/imageio-%{version}.tar.gz
Source1:        python-imageio-rpmlintrc
BuildRequires:  %{python_module Pillow >= 8.3.2}
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module numpy >= 1.20.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Pillow >= 8.3.2
Requires:       python-numpy >= 1.20.0
Recommends:     python-imageio-ffmpeg
Suggests:       python-astropy
Suggests:       python-tifffile
# not in openSUSE (yet)
Suggests:       python-simpleitk
# alternative is not singlespec
Suggests:       python3-itk
%if "%{python_flavor}" == "python3" || "%{python_provides}" == "python3"
# GDAL is not (yet) singlespec
Suggests:       python3-GDAL
%endif
Requires(post): update-alternatives
Requires(postun):update-alternatives
Recommends:     libfreeimageplus3
# SECTION test requirements
BuildRequires:  %{python_module fsspec}
BuildRequires:  %{python_module pytest}
BuildRequires:  libglvnd-devel
%if %{with test_extras}
BuildRequires:  %{python_module astropy}
BuildRequires:  %{python_module imageio-ffmpeg}
BuildRequires:  %{python_module psutil}
BuildRequires:  %{python_module tifffile}
BuildRequires:  python3-GDAL
# python3-itk does not work on 32-bit, don't bother testing that
%endif
# /SECTION
BuildArch:      noarch
%python_subpackages

%description
Imageio is a Python library that provides an interface to read and
write a wide range of image data, including animated images, volumetric
data, and scientific formats.

%prep
%setup -q -n imageio-%{version}

# Plugins are not executable scripts
for plgpy in imageio/plugins/_*.py ; do
    echo "Fixing $plgpy..."
    sed -i -e '1{/\/usr\/bin.*python/d}' $plgpy
done

%build
export IMAGEIO_NO_INTERNET=1
%python_build

%install
export IMAGEIO_NO_INTERNET=1
%python_install
%python_clone -a %{buildroot}%{_bindir}/imageio_remove_bin
%python_clone -a %{buildroot}%{_bindir}/imageio_download_bin
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export IMAGEIO_NO_INTERNET=1
# plain openSUSE does not have the right codecs to test this ffmpeg
donttest="test_ffmpeg"
# unmarked online tests
donttest="$donttest or test_freeimage"
%pytest -ra -k "not ($donttest)" -m "not needs_internet"

%post
%python_install_alternative imageio_remove_bin
%python_install_alternative imageio_download_bin

%postun
%python_uninstall_alternative imageio_remove_bin
%python_uninstall_alternative imageio_download_bin

%files %{python_files}
%license LICENSE
%doc CONTRIBUTORS.txt README.md
%{python_sitelib}/imageio
%{python_sitelib}/imageio-%{version}*-info
%python_alternative %{_bindir}/imageio_download_bin
%python_alternative %{_bindir}/imageio_remove_bin

%changelog
