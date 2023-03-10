#
# spec file for package jupyter-jupyterlab-latex
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


%define pythons python3
Name:           jupyter-jupyterlab-latex
Version:        3.1.0
Release:        0
Summary:        Jupyter Notebook server extension which acts as an endpoint for LaTeX
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/jupyterlab/jupyterlab-latex
Source:         https://files.pythonhosted.org/packages/py3/j/jupyterlab_latex/jupyterlab_latex-%{version}-py3-none-any.whl
Source99:       jupyter-jupyterlab-latex-rpmlintrc
BuildRequires:  fdupes
BuildRequires:  jupyter-jupyterlab
BuildRequires:  jupyter-notebook
BuildRequires:  python-rpm-macros
BuildRequires:  python3-base >= 3.6
BuildRequires:  python3-pip
Requires:       jupyter-notebook
Requires:       texlive-latex-bin
Provides:       python3-jupyter_jupyterlab_latex = %{version}-%{release}
Obsoletes:      python3-jupyter_jupyterlab_latex < %{version}-%{release}
Provides:       python3-jupyterlab-latex = %{version}-%{release}
BuildArch:      noarch

%description
An extension for JupyterLab which allows for live-editing of LaTeX documents.

%prep
%setup -q -c -T

%build
# Not Needed

%install
cp -a %{SOURCE0} .
%pyproject_install

%{jupyter_move_config}
%fdupes %{buildroot}%{_jupyter_prefix}
%fdupes %{buildroot}%{python3_sitelib}

#%%check
# no python tests

%files
%license %{python3_sitelib}/jupyterlab_latex-*.dist-info/LICENSE
%{python3_sitelib}/jupyterlab_latex-%{version}*.dist-info
%{python3_sitelib}/jupyterlab_latex/
%dir %_jupyter_labextensions_dir3/@jupyterlab
%_jupyter_labextensions_dir3/@jupyterlab/latex
%_jupyter_config %{_jupyter_servextension_confdir}/jupyterlab_latex.json
%_jupyter_config %{_jupyter_server_confdir}/jupyterlab_latex.json

%changelog
