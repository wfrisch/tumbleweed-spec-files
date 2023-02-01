#
# spec file for package texlive-specs-s
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


%define texlive_version  2022
%define texlive_previous 2021
%define texlive_release  20220321
%define texlive_noarch   196
%define biber_version    2.17

#!BuildIgnore:          texlive
#!BuildIgnore:          texlive-scripts
#!BuildIgnore:          texlive-scripts-extra
#!BuildIgnore:          texlive-scripts-bin
#!BuildIgnore:          texlive-scripts-extra-bin
#!BuildIgnore:          texlive-gsftopk
#!BuildIgnore:          texlive-gsftopk-bin
#!BuildIgnore:          texlive-kpathsea
#!BuildIgnore:          texlive-kpathsea-bin

%global _varlib         %{_localstatedir}/lib
%global _libexecdir     %{_prefix}/lib

%define _texmfdistdir   %{_datadir}/texmf
%if 0%{texlive_version} >= 2013
%define _texmfmaindir   %{_texmfdistdir}
%define _texmfdirs      %{_texmfdistdir}
%else
%define _texmfmaindir   %{_libexecdir}/texmf
%define _texmfdirs      \{%{_texmfdistdir},%{_texmfmaindir}\}
%endif

%define _texmfconfdir   %{_sysconfdir}/texmf
%define _texmfvardir    %{_varlib}/texmf
%define _texmfcache     %{_localstatedir}/cache/texmf
%define _fontcache      %{_texmfcache}/fonts
#
%define _x11bin         %{_prefix}/bin
%define _x11lib         %{_libdir}
%define _x11data        %{_datadir}/X11
%define _x11inc         %{_includedir}
%define _appdefdir      %{_x11data}/app-defaults

Name:           texlive-specs-s
Version:        2022
Release:        0
BuildRequires:  ed
BuildRequires:  fontconfig
BuildRequires:  fontpackages-devel
BuildRequires:  t1utils
BuildRequires:  texlive-filesystem
BuildRequires:  xz
BuildArch:      noarch
Summary:        Meta package for s
License:        BSD-3-Clause and GPL-2.0-or-later and LGPL-2.1-or-later and LPPL-1.0 and LPPL-1.3c and OFL-1.1 and SUSE-Public-Domain
URL:            https://build.opensuse.org/package/show/Publishing:TeXLive/Meta
Group:          Productivity/Publishing/TeX/Base
Source0:        texlive-specs-s-rpmlintrc

%description
Meta package to build tons of noarch texlive packages.

%package -n texlive-plari
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
License:        GPL-2.0-or-later
Summary:        Typesetting stageplay scripts
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-plari-doc >= %{texlive_version}
Provides:       tex(plari.cls)
Requires:       tex(report.cls)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source1:        plari.tar.xz
Source2:        plari.doc.tar.xz

%description -n texlive-plari
Plari (the name comes from the Finnish usage for the working
copy of a play) is a report-alike class, without section
headings, and with paragraphs vertically separated rather than
indented.

%package -n texlive-plari-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        Documentation for texlive-plari
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/

%description -n texlive-plari-doc
This package includes the documentation for texlive-plari

%post -n texlive-plari
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-plari
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-plari
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-plari-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/plari/COPYING
%{_texmfdistdir}/doc/latex/plari/README
%{_texmfdistdir}/doc/latex/plari/plari.pdf

%files -n texlive-plari
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/plari/plari.cls

%package -n texlive-plates
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1svn15878
Release:        0
License:        LPPL-1.0
Summary:        Arrange for "plates" sections of documents
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-plates-doc >= %{texlive_version}
Provides:       tex(endplate.sty)
Provides:       tex(plates.sty)
Requires:       tex(ifthen.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source3:        plates.tar.xz
Source4:        plates.doc.tar.xz

%description -n texlive-plates
The plates package provides a simple facility for inserting
colour figures in a document when they should be gathered and
printed together as in a book's section of colour plates. The
package provides a plate environment that takes the place of
the figure environment for such colour images.

%package -n texlive-plates-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1svn15878
Release:        0
Summary:        Documentation for texlive-plates
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/

%description -n texlive-plates-doc
This package includes the documentation for texlive-plates

%post -n texlive-plates
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-plates
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-plates
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-plates-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/plates/README
%{_texmfdistdir}/doc/latex/plates/plates.pdf
%{_texmfdistdir}/doc/latex/plates/plates.tex

%files -n texlive-plates
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/plates/endplate.sty
%{_texmfdistdir}/tex/latex/plates/plates.sty

%package -n texlive-platex
Version:        %{texlive_version}.%{texlive_noarch}.svn62387
Release:        0
License:        BSD-3-Clause
Summary:        PLaTeX2e and miscellaneous macros for pTeX
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires:       texlive-atbegshi >= %{texlive_version}
#!BuildIgnore: texlive-atbegshi
Requires:       texlive-atveryend >= %{texlive_version}
#!BuildIgnore: texlive-atveryend
Requires:       texlive-babel >= %{texlive_version}
#!BuildIgnore: texlive-babel
Requires:       texlive-cm >= %{texlive_version}
#!BuildIgnore: texlive-cm
Requires:       texlive-everyshi >= %{texlive_version}
#!BuildIgnore: texlive-everyshi
Requires:       texlive-firstaid >= %{texlive_version}
#!BuildIgnore: texlive-firstaid
Requires:       texlive-hyphen-base >= %{texlive_version}
#!BuildIgnore: texlive-hyphen-base
Requires:       texlive-l3backend >= %{texlive_version}
#!BuildIgnore: texlive-l3backend
Requires:       texlive-l3kernel >= %{texlive_version}
#!BuildIgnore: texlive-l3kernel
Requires:       texlive-l3packages >= %{texlive_version}
#!BuildIgnore: texlive-l3packages
Requires:       texlive-latex >= %{texlive_version}
#!BuildIgnore: texlive-latex
Requires:       texlive-latex-base-dev >= %{texlive_version}
#!BuildIgnore: texlive-latex-base-dev
Requires:       texlive-latex-firstaid-dev >= %{texlive_version}
#!BuildIgnore: texlive-latex-firstaid-dev
Requires:       texlive-latex-fonts >= %{texlive_version}
#!BuildIgnore: texlive-latex-fonts
Requires(pre):  texlive-platex-bin >= %{texlive_version}
#!BuildIgnore: texlive-platex-bin
Requires:       texlive-ptex >= %{texlive_version}
#!BuildIgnore: texlive-ptex
Requires:       texlive-ptex-fonts >= %{texlive_version}
#!BuildIgnore: texlive-ptex-fonts
Requires:       texlive-tex-ini-files >= %{texlive_version}
#!BuildIgnore: texlive-tex-ini-files
Requires:       texlive-unicode-data >= %{texlive_version}
#!BuildIgnore: texlive-unicode-data
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(language.dat)
Requires(post): tex(language.def)
Requires(post): tex(language.dat.lua)
#!BuildIgnore:  tex(language.dat)
#!BuildIgnore:  tex(language.def)
#!BuildIgnore:  tex(language.dat.lua)
Requires(postun):findutils
Requires(postun):grep
Requires(postun):sed
Requires(postun):texlive >= %{texlive_version}
Requires(postun):tex(language.dat)
Requires(postun):tex(language.def)
Requires(postun):tex(language.dat.lua)
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-platex-doc >= %{texlive_version}
Provides:       tex(exppl2e.sty)
Provides:       tex(jarticle.cls)
Provides:       tex(jarticle.sty)
Provides:       tex(jbk10.clo)
Provides:       tex(jbk11.clo)
Provides:       tex(jbk12.clo)
Provides:       tex(jbook.cls)
Provides:       tex(jbook.sty)
Provides:       tex(jltxdoc.cls)
Provides:       tex(jreport.cls)
Provides:       tex(jreport.sty)
Provides:       tex(jsize10.clo)
Provides:       tex(jsize11.clo)
Provides:       tex(jsize12.clo)
Provides:       tex(jt1gt.fd)
Provides:       tex(jt1mc.fd)
Provides:       tex(jy1gt.fd)
Provides:       tex(jy1mc.fd)
Provides:       tex(kinsoku.tex)
Provides:       tex(oldpfont.sty)
Provides:       tex(pfltrace.sty)
Provides:       tex(pl209.def)
Provides:       tex(platexrelease.sty)
Provides:       tex(plexpl3.sty)
Provides:       tex(plext.sty)
Provides:       tex(plnews.cls)
Provides:       tex(ptrace.sty)
Provides:       tex(tarticle.cls)
Provides:       tex(tarticle.sty)
Provides:       tex(tbk10.clo)
Provides:       tex(tbk11.clo)
Provides:       tex(tbk12.clo)
Provides:       tex(tbook.cls)
Provides:       tex(tbook.sty)
Provides:       tex(treport.cls)
Provides:       tex(treport.sty)
Provides:       tex(tsize10.clo)
Provides:       tex(tsize11.clo)
Provides:       tex(tsize12.clo)
Requires:       tex(expl3.sty)
Requires:       tex(fltrace.sty)
Suggests:       man(latex.1)
Requires:       tex(latex209.def)
Requires:       tex(latexrelease.sty)
Requires:       tex(ltxdoc.cls)
Requires:       tex(oldlfont.sty)
Requires:       tex(shortvrb.sty)
Requires:       tex(tracefnt.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source5:        platex.tar.xz
Source6:        platex.doc.tar.xz

%description -n texlive-platex
The bundle provides pLaTeX2e and miscellaneous macros for pTeX
and e-pTeX. This is a community edition forked from the
original ASCII edition (ptex-texmf-2.5).

%package -n texlive-platex-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn62387
Release:        0
Summary:        Documentation for texlive-platex
License:        BSD-3-Clause
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Provides:       locale(texlive-platex-doc:ja)
Provides:       man(platex.1)

%description -n texlive-platex-doc
This package includes the documentation for texlive-platex

%post -n texlive-platex
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
> /var/run/texlive/run-fmtutil.platex
sed -ri 's/^\#\![[= =]]+platex\b.*/platex eptex language.dat *platex.ini/' %{_texmfconfdir}/web2c/fmtutil.cnf || :
> /var/run/texlive/run-fmtutil.platex-dev
sed -ri 's/^\#\![[= =]]+platex-dev\b.*/platex-dev eptex language.dat *platex.ini/' %{_texmfconfdir}/web2c/fmtutil.cnf || :

%postun -n texlive-platex
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    sed -ri 's/^(platex\b)/\#\!\ \1/' %{_texmfconfdir}/web2c/fmtutil.cnf || :
    rm -f %{_texmfvardir}/web2c/eptex/platex.*
    sed -ri 's/^(platex-dev\b)/\#\!\ \1/' %{_texmfconfdir}/web2c/fmtutil.cnf || :
    rm -f %{_texmfvardir}/web2c/eptex/platex-dev.*
    exit 0
fi

%triggerin -n texlive-platex -- texlive-atbegshi
> /var/run/texlive/run-fmtutil.platex
> /var/run/texlive/run-fmtutil.platex-dev

%triggerun -n texlive-platex -- texlive-atbegshi
> /var/run/texlive/run-fmtutil.platex
> /var/run/texlive/run-fmtutil.platex-dev

%triggerin -n texlive-platex -- texlive-atveryend
> /var/run/texlive/run-fmtutil.platex
> /var/run/texlive/run-fmtutil.platex-dev

%triggerun -n texlive-platex -- texlive-atveryend
> /var/run/texlive/run-fmtutil.platex
> /var/run/texlive/run-fmtutil.platex-dev

%triggerin -n texlive-platex -- texlive-babel
> /var/run/texlive/run-fmtutil.platex
> /var/run/texlive/run-fmtutil.platex-dev

%triggerun -n texlive-platex -- texlive-babel
> /var/run/texlive/run-fmtutil.platex
> /var/run/texlive/run-fmtutil.platex-dev

%triggerin -n texlive-platex -- texlive-cm
> /var/run/texlive/run-fmtutil.platex
> /var/run/texlive/run-fmtutil.platex-dev

%triggerun -n texlive-platex -- texlive-cm
> /var/run/texlive/run-fmtutil.platex
> /var/run/texlive/run-fmtutil.platex-dev

%triggerin -n texlive-platex -- texlive-everyshi
> /var/run/texlive/run-fmtutil.platex
> /var/run/texlive/run-fmtutil.platex-dev

%triggerun -n texlive-platex -- texlive-everyshi
> /var/run/texlive/run-fmtutil.platex
> /var/run/texlive/run-fmtutil.platex-dev

%triggerin -n texlive-platex -- texlive-firstaid
> /var/run/texlive/run-fmtutil.platex
> /var/run/texlive/run-fmtutil.platex-dev

%triggerun -n texlive-platex -- texlive-firstaid
> /var/run/texlive/run-fmtutil.platex
> /var/run/texlive/run-fmtutil.platex-dev

%triggerin -n texlive-platex -- texlive-hyphen-base
> /var/run/texlive/run-fmtutil.platex
> /var/run/texlive/run-fmtutil.platex-dev

%triggerun -n texlive-platex -- texlive-hyphen-base
> /var/run/texlive/run-fmtutil.platex
> /var/run/texlive/run-fmtutil.platex-dev

%triggerin -n texlive-platex -- texlive-l3backend
> /var/run/texlive/run-fmtutil.platex
> /var/run/texlive/run-fmtutil.platex-dev

%triggerun -n texlive-platex -- texlive-l3backend
> /var/run/texlive/run-fmtutil.platex
> /var/run/texlive/run-fmtutil.platex-dev

%triggerin -n texlive-platex -- texlive-l3kernel
> /var/run/texlive/run-fmtutil.platex
> /var/run/texlive/run-fmtutil.platex-dev

%triggerun -n texlive-platex -- texlive-l3kernel
> /var/run/texlive/run-fmtutil.platex
> /var/run/texlive/run-fmtutil.platex-dev

%triggerin -n texlive-platex -- texlive-l3packages
> /var/run/texlive/run-fmtutil.platex
> /var/run/texlive/run-fmtutil.platex-dev

%triggerun -n texlive-platex -- texlive-l3packages
> /var/run/texlive/run-fmtutil.platex
> /var/run/texlive/run-fmtutil.platex-dev

%triggerin -n texlive-platex -- texlive-latex
> /var/run/texlive/run-fmtutil.platex
> /var/run/texlive/run-fmtutil.platex-dev

%triggerun -n texlive-platex -- texlive-latex
> /var/run/texlive/run-fmtutil.platex
> /var/run/texlive/run-fmtutil.platex-dev

%triggerin -n texlive-platex -- texlive-latex-base-dev
> /var/run/texlive/run-fmtutil.platex
> /var/run/texlive/run-fmtutil.platex-dev

%triggerun -n texlive-platex -- texlive-latex-base-dev
> /var/run/texlive/run-fmtutil.platex
> /var/run/texlive/run-fmtutil.platex-dev

%triggerin -n texlive-platex -- texlive-latex-firstaid-dev
> /var/run/texlive/run-fmtutil.platex
> /var/run/texlive/run-fmtutil.platex-dev

%triggerun -n texlive-platex -- texlive-latex-firstaid-dev
> /var/run/texlive/run-fmtutil.platex
> /var/run/texlive/run-fmtutil.platex-dev

%triggerin -n texlive-platex -- texlive-latex-fonts
> /var/run/texlive/run-fmtutil.platex
> /var/run/texlive/run-fmtutil.platex-dev

%triggerun -n texlive-platex -- texlive-latex-fonts
> /var/run/texlive/run-fmtutil.platex
> /var/run/texlive/run-fmtutil.platex-dev

%triggerin -n texlive-platex -- texlive-ptex-fonts
> /var/run/texlive/run-fmtutil.platex
> /var/run/texlive/run-fmtutil.platex-dev

%triggerun -n texlive-platex -- texlive-ptex-fonts
> /var/run/texlive/run-fmtutil.platex
> /var/run/texlive/run-fmtutil.platex-dev

%triggerin -n texlive-platex -- texlive-tex-ini-files
> /var/run/texlive/run-fmtutil.platex
> /var/run/texlive/run-fmtutil.platex-dev

%triggerun -n texlive-platex -- texlive-tex-ini-files
> /var/run/texlive/run-fmtutil.platex
> /var/run/texlive/run-fmtutil.platex-dev

%triggerin -n texlive-platex -- texlive-unicode-data
> /var/run/texlive/run-fmtutil.platex
> /var/run/texlive/run-fmtutil.platex-dev

%triggerun -n texlive-platex -- texlive-unicode-data
> /var/run/texlive/run-fmtutil.platex
> /var/run/texlive/run-fmtutil.platex-dev

%posttrans -n texlive-platex
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-platex-doc
%defattr(-,root,root,755)
%{_mandir}/man1/platex.1*
%{_texmfdistdir}/doc/platex/base/LICENSE
%{_texmfdistdir}/doc/platex/base/README.md
%{_texmfdistdir}/doc/platex/base/exppl2e.pdf
%{_texmfdistdir}/doc/platex/base/platex-en.pdf
%{_texmfdistdir}/doc/platex/base/platex.pdf
%{_texmfdistdir}/doc/platex/base/platexrelease.pdf
%{_texmfdistdir}/doc/platex/base/pldoc.pdf

%files -n texlive-platex
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/platex/base/exppl2e.sty
%{_texmfdistdir}/tex/platex/base/jarticle.cls
%{_texmfdistdir}/tex/platex/base/jarticle.sty
%{_texmfdistdir}/tex/platex/base/jbk10.clo
%{_texmfdistdir}/tex/platex/base/jbk11.clo
%{_texmfdistdir}/tex/platex/base/jbk12.clo
%{_texmfdistdir}/tex/platex/base/jbook.cls
%{_texmfdistdir}/tex/platex/base/jbook.sty
%{_texmfdistdir}/tex/platex/base/jltxdoc.cls
%{_texmfdistdir}/tex/platex/base/jreport.cls
%{_texmfdistdir}/tex/platex/base/jreport.sty
%{_texmfdistdir}/tex/platex/base/jsize10.clo
%{_texmfdistdir}/tex/platex/base/jsize11.clo
%{_texmfdistdir}/tex/platex/base/jsize12.clo
%{_texmfdistdir}/tex/platex/base/jt1gt.fd
%{_texmfdistdir}/tex/platex/base/jt1mc.fd
%{_texmfdistdir}/tex/platex/base/jy1gt.fd
%{_texmfdistdir}/tex/platex/base/jy1mc.fd
%{_texmfdistdir}/tex/platex/base/kinsoku.tex
%{_texmfdistdir}/tex/platex/base/oldpfont.sty
%{_texmfdistdir}/tex/platex/base/pfltrace.sty
%{_texmfdistdir}/tex/platex/base/pl209.def
%{_texmfdistdir}/tex/platex/base/platex.ltx
%{_texmfdistdir}/tex/platex/base/platexrelease.sty
%{_texmfdistdir}/tex/platex/base/plcore.ltx
%{_texmfdistdir}/tex/platex/base/pldefs.ltx
%{_texmfdistdir}/tex/platex/base/plexpl3.ltx
%{_texmfdistdir}/tex/platex/base/plexpl3.sty
%{_texmfdistdir}/tex/platex/base/plext.sty
%{_texmfdistdir}/tex/platex/base/plnews.cls
%{_texmfdistdir}/tex/platex/base/ptrace.sty
%{_texmfdistdir}/tex/platex/base/tarticle.cls
%{_texmfdistdir}/tex/platex/base/tarticle.sty
%{_texmfdistdir}/tex/platex/base/tbk10.clo
%{_texmfdistdir}/tex/platex/base/tbk11.clo
%{_texmfdistdir}/tex/platex/base/tbk12.clo
%{_texmfdistdir}/tex/platex/base/tbook.cls
%{_texmfdistdir}/tex/platex/base/tbook.sty
%{_texmfdistdir}/tex/platex/base/treport.cls
%{_texmfdistdir}/tex/platex/base/treport.sty
%{_texmfdistdir}/tex/platex/base/tsize10.clo
%{_texmfdistdir}/tex/platex/base/tsize11.clo
%{_texmfdistdir}/tex/platex/base/tsize12.clo
%{_texmfdistdir}/tex/platex/config/platex.ini

%package -n texlive-platex-tools
Version:        %{texlive_version}.%{texlive_noarch}.svn61272
Release:        0
License:        BSD-3-Clause
Summary:        PLaTeX standard tools bundle
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-platex-tools-doc >= %{texlive_version}
Provides:       tex(plarray.sty)
Provides:       tex(pldocverb.sty)
Provides:       tex(plextarray.sty)
Provides:       tex(plextcolortbl.sty)
Provides:       tex(plextdelarray.sty)
Provides:       tex(pxatbegshi.sty)
Provides:       tex(pxeverysel.sty)
Provides:       tex(pxeveryshi.sty)
Provides:       tex(pxftnright.sty)
Provides:       tex(pxmulticol.sty)
Provides:       tex(pxxspace.sty)
Requires:       tex(array.sty)
Requires:       tex(atbegshi.sty)
Requires:       tex(colortbl.sty)
Requires:       tex(delarray.sty)
Requires:       tex(doc.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(everysel.sty)
Requires:       tex(everyshi.sty)
Requires:       tex(ftnright.sty)
Requires:       tex(multicol.sty)
Requires:       tex(pdftexcmds.sty)
Requires:       tex(plext.sty)
Requires:       tex(ptrace.sty)
Requires:       tex(uptrace.sty)
Requires:       tex(xspace.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source7:        platex-tools.tar.xz
Source8:        platex-tools.doc.tar.xz

%description -n texlive-platex-tools
This bundle is an extended version of the latex-tools bundle
developed by the LaTeX team, mainly intended to support
pLaTeX2e and upLaTeX2e. Currently patches for the latex-tools
bundle and Martin Schroder's ms bundle are included.

%package -n texlive-platex-tools-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn61272
Release:        0
Summary:        Documentation for texlive-platex-tools
License:        BSD-3-Clause
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Provides:       locale(texlive-platex-tools-doc:ja)

%description -n texlive-platex-tools-doc
This package includes the documentation for texlive-platex-tools

%post -n texlive-platex-tools
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-platex-tools
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-platex-tools
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-platex-tools-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/platex-tools/LICENSE
%{_texmfdistdir}/doc/latex/platex-tools/README.md
%{_texmfdistdir}/doc/latex/platex-tools/plarray.pdf
%{_texmfdistdir}/doc/latex/platex-tools/plarray.tex
%{_texmfdistdir}/doc/latex/platex-tools/pldocverb.pdf
%{_texmfdistdir}/doc/latex/platex-tools/pldocverb.tex
%{_texmfdistdir}/doc/latex/platex-tools/plextarray.pdf
%{_texmfdistdir}/doc/latex/platex-tools/plextarray.tex
%{_texmfdistdir}/doc/latex/platex-tools/plextcolortbl.pdf
%{_texmfdistdir}/doc/latex/platex-tools/plextcolortbl.tex
%{_texmfdistdir}/doc/latex/platex-tools/plextdelarray.pdf
%{_texmfdistdir}/doc/latex/platex-tools/plextdelarray.tex
%{_texmfdistdir}/doc/latex/platex-tools/pxatbegshi.pdf
%{_texmfdistdir}/doc/latex/platex-tools/pxatbegshi.tex
%{_texmfdistdir}/doc/latex/platex-tools/pxeverysel.pdf
%{_texmfdistdir}/doc/latex/platex-tools/pxeverysel.tex
%{_texmfdistdir}/doc/latex/platex-tools/pxeveryshi.pdf
%{_texmfdistdir}/doc/latex/platex-tools/pxeveryshi.tex
%{_texmfdistdir}/doc/latex/platex-tools/pxftnright.pdf
%{_texmfdistdir}/doc/latex/platex-tools/pxftnright.tex
%{_texmfdistdir}/doc/latex/platex-tools/pxmulticol.pdf
%{_texmfdistdir}/doc/latex/platex-tools/pxmulticol.tex
%{_texmfdistdir}/doc/latex/platex-tools/pxxspace.pdf
%{_texmfdistdir}/doc/latex/platex-tools/pxxspace.tex

%files -n texlive-platex-tools
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/platex-tools/plarray.sty
%{_texmfdistdir}/tex/latex/platex-tools/pldocverb.sty
%{_texmfdistdir}/tex/latex/platex-tools/plextarray.sty
%{_texmfdistdir}/tex/latex/platex-tools/plextcolortbl.sty
%{_texmfdistdir}/tex/latex/platex-tools/plextdelarray.sty
%{_texmfdistdir}/tex/latex/platex-tools/pxatbegshi.sty
%{_texmfdistdir}/tex/latex/platex-tools/pxeverysel.sty
%{_texmfdistdir}/tex/latex/platex-tools/pxeveryshi.sty
%{_texmfdistdir}/tex/latex/platex-tools/pxftnright.sty
%{_texmfdistdir}/tex/latex/platex-tools/pxmulticol.sty
%{_texmfdistdir}/tex/latex/platex-tools/pxxspace.sty

%package -n texlive-platexcheat
Version:        %{texlive_version}.%{texlive_noarch}.3.1svn49557
Release:        0
License:        LPPL-1.0
Summary:        A LaTeX cheat sheet, in Japanese
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source9:        platexcheat.doc.tar.xz

%description -n texlive-platexcheat
This is a translation to Japanese of Winston Chang's LaTeX
cheat sheet (a reference sheet for writing scientific papers).
It has been adapted to Japanese standards using pLaTeX, and
also attached additional information of "standard LaTeX"
(especially about math-mode).

%post -n texlive-platexcheat
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-platexcheat
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-platexcheat
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-platexcheat
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/platexcheat/LICENSE
%{_texmfdistdir}/doc/latex/platexcheat/README.md
%{_texmfdistdir}/doc/latex/platexcheat/platexsheet-jsclasses.pdf
%{_texmfdistdir}/doc/latex/platexcheat/platexsheet-jsclasses.tex
%{_texmfdistdir}/doc/latex/platexcheat/platexsheet.pdf
%{_texmfdistdir}/doc/latex/platexcheat/platexsheet.tex
%{_texmfdistdir}/doc/latex/platexcheat/sample-jsclasses.pdf
%{_texmfdistdir}/doc/latex/platexcheat/sample-jsclasses.tex
%{_texmfdistdir}/doc/latex/platexcheat/sample.pdf
%{_texmfdistdir}/doc/latex/platexcheat/sample.tex

%package -n texlive-plautopatch
Version:        %{texlive_version}.%{texlive_noarch}.0.0.9qsvn61240
Release:        0
License:        BSD-3-Clause
Summary:        Automated patches for pLaTeX/upLaTeX
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-plautopatch-doc >= %{texlive_version}
Provides:       tex(plarydshln.sty)
Provides:       tex(plautopatch.sty)
Provides:       tex(plcollcell.sty)
Provides:       tex(plextarydshln.sty)
Provides:       tex(plsiunitx.sty)
Provides:       tex(pxpgfrcs.sty)
Provides:       tex(pxstfloats.sty)
Requires:       tex(array.sty)
Requires:       tex(arydshln.sty)
Requires:       tex(collcell.sty)
Requires:       tex(colortbl.sty)
Requires:       tex(delarray.sty)
Requires:       tex(filehook.sty)
Requires:       tex(pgfrcs.sty)
Requires:       tex(plarray.sty)
Requires:       tex(plext.sty)
Requires:       tex(plextarray.sty)
Requires:       tex(plextcolortbl.sty)
Requires:       tex(plextdelarray.sty)
Requires:       tex(pxeveryshi.sty)
Requires:       tex(siunitx.sty)
Requires:       tex(stfloats.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source10:       plautopatch.tar.xz
Source11:       plautopatch.doc.tar.xz

%description -n texlive-plautopatch
Japanese pLaTeX/upLaTeX formats and packages often conflict
with other LaTeX packages which are unaware of pLaTeX/upLaTeX.
In the worst case, such packages throw a fatal error or end up
with a wrong output. The goal of this package is that there
should be no need to worry about such incompatibilities,
because specific patches are loaded automatically whenever
necessary. This helps not only to simplify source files, but
also to make the appearance of working pLaTeX/upLaTeX sources
similar to those of ordinary LaTeX ones.

%package -n texlive-plautopatch-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.9qsvn61240
Release:        0
Summary:        Documentation for texlive-plautopatch
License:        BSD-3-Clause
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Provides:       locale(texlive-plautopatch-doc:ja)

%description -n texlive-plautopatch-doc
This package includes the documentation for texlive-plautopatch

%post -n texlive-plautopatch
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-plautopatch
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-plautopatch
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-plautopatch-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/plautopatch/LICENSE
%{_texmfdistdir}/doc/latex/plautopatch/README.md
%{_texmfdistdir}/doc/latex/plautopatch/plautopatch-ja.pdf
%{_texmfdistdir}/doc/latex/plautopatch/plautopatch-ja.tex
%{_texmfdistdir}/doc/latex/plautopatch/plautopatch.pdf
%{_texmfdistdir}/doc/latex/plautopatch/plautopatch.tex

%files -n texlive-plautopatch
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/plautopatch/plarydshln.sty
%{_texmfdistdir}/tex/latex/plautopatch/plautopatch.sty
%{_texmfdistdir}/tex/latex/plautopatch/plcollcell.sty
%{_texmfdistdir}/tex/latex/plautopatch/plextarydshln.sty
%{_texmfdistdir}/tex/latex/plautopatch/plsiunitx.sty
%{_texmfdistdir}/tex/latex/plautopatch/pxpgfrcs.sty
%{_texmfdistdir}/tex/latex/plautopatch/pxstfloats.sty

%package -n texlive-play
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
License:        LPPL-1.0
Summary:        Typeset drama using LaTeX
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-play-doc >= %{texlive_version}
Provides:       tex(play.cls)
Provides:       tex(play.sty)
Requires:       tex(book.cls)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source12:       play.tar.xz
Source13:       play.doc.tar.xz

%description -n texlive-play
A class and style file that supports the typesetting of plays,
including options for line numbering.

%package -n texlive-play-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        Documentation for texlive-play
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/

%description -n texlive-play-doc
This package includes the documentation for texlive-play

%post -n texlive-play
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-play
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-play
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-play-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/play/README

%files -n texlive-play
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/play/play.cls
%{_texmfdistdir}/tex/latex/play/play.sty

%package -n texlive-playfair
Version:        %{texlive_version}.%{texlive_noarch}.svn56005
Release:        0
License:        OFL-1.1
Summary:        Playfair Display fonts with LaTeX support
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(updmap.cfg)
#!BuildIgnore:  tex(updmap.cfg)
Requires(postun):findutils
Requires(postun):grep
Requires(postun):sed
Requires(postun):texlive >= %{texlive_version}
Requires(postun):tex(updmap.cfg)
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Requires:       texlive-playfair-fonts >= %{texlive_version}
Suggests:       texlive-playfair-doc >= %{texlive_version}
Provides:       tex(LY1PlyfrDisplay-LF.fd)
Provides:       tex(LY1PlyfrDisplay-OsF.fd)
Provides:       tex(LY1PlyfrDisplay-Sup.fd)
Provides:       tex(OT1PlyfrDisplay-LF.fd)
Provides:       tex(OT1PlyfrDisplay-OsF.fd)
Provides:       tex(OT1PlyfrDisplay-Sup.fd)
Provides:       tex(PlayfairDisplay.map)
Provides:       tex(PlayfairDisplay.sty)
Provides:       tex(PlyfrDisplay-Black-lf-ly1--base.tfm)
Provides:       tex(PlyfrDisplay-Black-lf-ly1.tfm)
Provides:       tex(PlyfrDisplay-Black-lf-ly1.vf)
Provides:       tex(PlyfrDisplay-Black-lf-ot1.tfm)
Provides:       tex(PlyfrDisplay-Black-lf-sc-ly1--base.tfm)
Provides:       tex(PlyfrDisplay-Black-lf-sc-ly1.tfm)
Provides:       tex(PlyfrDisplay-Black-lf-sc-ly1.vf)
Provides:       tex(PlyfrDisplay-Black-lf-sc-ot1--base.tfm)
Provides:       tex(PlyfrDisplay-Black-lf-sc-ot1.tfm)
Provides:       tex(PlyfrDisplay-Black-lf-sc-ot1.vf)
Provides:       tex(PlyfrDisplay-Black-lf-sc-t1--base.tfm)
Provides:       tex(PlyfrDisplay-Black-lf-sc-t1.tfm)
Provides:       tex(PlyfrDisplay-Black-lf-sc-t1.vf)
Provides:       tex(PlyfrDisplay-Black-lf-t1--base.tfm)
Provides:       tex(PlyfrDisplay-Black-lf-t1.tfm)
Provides:       tex(PlyfrDisplay-Black-lf-t1.vf)
Provides:       tex(PlyfrDisplay-Black-lf-ts1--base.tfm)
Provides:       tex(PlyfrDisplay-Black-lf-ts1.tfm)
Provides:       tex(PlyfrDisplay-Black-lf-ts1.vf)
Provides:       tex(PlyfrDisplay-Black-osf-ly1--base.tfm)
Provides:       tex(PlyfrDisplay-Black-osf-ly1.tfm)
Provides:       tex(PlyfrDisplay-Black-osf-ly1.vf)
Provides:       tex(PlyfrDisplay-Black-osf-ot1.tfm)
Provides:       tex(PlyfrDisplay-Black-osf-sc-ly1--base.tfm)
Provides:       tex(PlyfrDisplay-Black-osf-sc-ly1.tfm)
Provides:       tex(PlyfrDisplay-Black-osf-sc-ly1.vf)
Provides:       tex(PlyfrDisplay-Black-osf-sc-ot1--base.tfm)
Provides:       tex(PlyfrDisplay-Black-osf-sc-ot1.tfm)
Provides:       tex(PlyfrDisplay-Black-osf-sc-ot1.vf)
Provides:       tex(PlyfrDisplay-Black-osf-sc-t1--base.tfm)
Provides:       tex(PlyfrDisplay-Black-osf-sc-t1.tfm)
Provides:       tex(PlyfrDisplay-Black-osf-sc-t1.vf)
Provides:       tex(PlyfrDisplay-Black-osf-t1--base.tfm)
Provides:       tex(PlyfrDisplay-Black-osf-t1.tfm)
Provides:       tex(PlyfrDisplay-Black-osf-t1.vf)
Provides:       tex(PlyfrDisplay-Black-osf-ts1--base.tfm)
Provides:       tex(PlyfrDisplay-Black-osf-ts1.tfm)
Provides:       tex(PlyfrDisplay-Black-osf-ts1.vf)
Provides:       tex(PlyfrDisplay-Black-sup-ly1--base.tfm)
Provides:       tex(PlyfrDisplay-Black-sup-ly1.tfm)
Provides:       tex(PlyfrDisplay-Black-sup-ly1.vf)
Provides:       tex(PlyfrDisplay-Black-sup-ot1.tfm)
Provides:       tex(PlyfrDisplay-Black-sup-t1--base.tfm)
Provides:       tex(PlyfrDisplay-Black-sup-t1.tfm)
Provides:       tex(PlyfrDisplay-Black-sup-t1.vf)
Provides:       tex(PlyfrDisplay-BlackItalic-lf-ly1--base.tfm)
Provides:       tex(PlyfrDisplay-BlackItalic-lf-ly1.tfm)
Provides:       tex(PlyfrDisplay-BlackItalic-lf-ly1.vf)
Provides:       tex(PlyfrDisplay-BlackItalic-lf-ot1.tfm)
Provides:       tex(PlyfrDisplay-BlackItalic-lf-sc-ly1--base.tfm)
Provides:       tex(PlyfrDisplay-BlackItalic-lf-sc-ly1.tfm)
Provides:       tex(PlyfrDisplay-BlackItalic-lf-sc-ly1.vf)
Provides:       tex(PlyfrDisplay-BlackItalic-lf-sc-ot1--base.tfm)
Provides:       tex(PlyfrDisplay-BlackItalic-lf-sc-ot1.tfm)
Provides:       tex(PlyfrDisplay-BlackItalic-lf-sc-ot1.vf)
Provides:       tex(PlyfrDisplay-BlackItalic-lf-sc-t1--base.tfm)
Provides:       tex(PlyfrDisplay-BlackItalic-lf-sc-t1.tfm)
Provides:       tex(PlyfrDisplay-BlackItalic-lf-sc-t1.vf)
Provides:       tex(PlyfrDisplay-BlackItalic-lf-t1--base.tfm)
Provides:       tex(PlyfrDisplay-BlackItalic-lf-t1.tfm)
Provides:       tex(PlyfrDisplay-BlackItalic-lf-t1.vf)
Provides:       tex(PlyfrDisplay-BlackItalic-lf-ts1--base.tfm)
Provides:       tex(PlyfrDisplay-BlackItalic-lf-ts1.tfm)
Provides:       tex(PlyfrDisplay-BlackItalic-lf-ts1.vf)
Provides:       tex(PlyfrDisplay-BlackItalic-osf-ly1--base.tfm)
Provides:       tex(PlyfrDisplay-BlackItalic-osf-ly1.tfm)
Provides:       tex(PlyfrDisplay-BlackItalic-osf-ly1.vf)
Provides:       tex(PlyfrDisplay-BlackItalic-osf-ot1.tfm)
Provides:       tex(PlyfrDisplay-BlackItalic-osf-sc-ly1--base.tfm)
Provides:       tex(PlyfrDisplay-BlackItalic-osf-sc-ly1.tfm)
Provides:       tex(PlyfrDisplay-BlackItalic-osf-sc-ly1.vf)
Provides:       tex(PlyfrDisplay-BlackItalic-osf-sc-ot1--base.tfm)
Provides:       tex(PlyfrDisplay-BlackItalic-osf-sc-ot1.tfm)
Provides:       tex(PlyfrDisplay-BlackItalic-osf-sc-ot1.vf)
Provides:       tex(PlyfrDisplay-BlackItalic-osf-sc-t1--base.tfm)
Provides:       tex(PlyfrDisplay-BlackItalic-osf-sc-t1.tfm)
Provides:       tex(PlyfrDisplay-BlackItalic-osf-sc-t1.vf)
Provides:       tex(PlyfrDisplay-BlackItalic-osf-t1--base.tfm)
Provides:       tex(PlyfrDisplay-BlackItalic-osf-t1.tfm)
Provides:       tex(PlyfrDisplay-BlackItalic-osf-t1.vf)
Provides:       tex(PlyfrDisplay-BlackItalic-osf-ts1--base.tfm)
Provides:       tex(PlyfrDisplay-BlackItalic-osf-ts1.tfm)
Provides:       tex(PlyfrDisplay-BlackItalic-osf-ts1.vf)
Provides:       tex(PlyfrDisplay-BlackItalic-sup-ly1--base.tfm)
Provides:       tex(PlyfrDisplay-BlackItalic-sup-ly1.tfm)
Provides:       tex(PlyfrDisplay-BlackItalic-sup-ly1.vf)
Provides:       tex(PlyfrDisplay-BlackItalic-sup-ot1.tfm)
Provides:       tex(PlyfrDisplay-BlackItalic-sup-t1--base.tfm)
Provides:       tex(PlyfrDisplay-BlackItalic-sup-t1.tfm)
Provides:       tex(PlyfrDisplay-BlackItalic-sup-t1.vf)
Provides:       tex(PlyfrDisplay-Bold-lf-ly1--base.tfm)
Provides:       tex(PlyfrDisplay-Bold-lf-ly1.tfm)
Provides:       tex(PlyfrDisplay-Bold-lf-ly1.vf)
Provides:       tex(PlyfrDisplay-Bold-lf-ot1.tfm)
Provides:       tex(PlyfrDisplay-Bold-lf-sc-ly1--base.tfm)
Provides:       tex(PlyfrDisplay-Bold-lf-sc-ly1.tfm)
Provides:       tex(PlyfrDisplay-Bold-lf-sc-ly1.vf)
Provides:       tex(PlyfrDisplay-Bold-lf-sc-ot1--base.tfm)
Provides:       tex(PlyfrDisplay-Bold-lf-sc-ot1.tfm)
Provides:       tex(PlyfrDisplay-Bold-lf-sc-ot1.vf)
Provides:       tex(PlyfrDisplay-Bold-lf-sc-t1--base.tfm)
Provides:       tex(PlyfrDisplay-Bold-lf-sc-t1.tfm)
Provides:       tex(PlyfrDisplay-Bold-lf-sc-t1.vf)
Provides:       tex(PlyfrDisplay-Bold-lf-t1--base.tfm)
Provides:       tex(PlyfrDisplay-Bold-lf-t1.tfm)
Provides:       tex(PlyfrDisplay-Bold-lf-t1.vf)
Provides:       tex(PlyfrDisplay-Bold-lf-ts1--base.tfm)
Provides:       tex(PlyfrDisplay-Bold-lf-ts1.tfm)
Provides:       tex(PlyfrDisplay-Bold-lf-ts1.vf)
Provides:       tex(PlyfrDisplay-Bold-osf-ly1--base.tfm)
Provides:       tex(PlyfrDisplay-Bold-osf-ly1.tfm)
Provides:       tex(PlyfrDisplay-Bold-osf-ly1.vf)
Provides:       tex(PlyfrDisplay-Bold-osf-ot1.tfm)
Provides:       tex(PlyfrDisplay-Bold-osf-sc-ly1--base.tfm)
Provides:       tex(PlyfrDisplay-Bold-osf-sc-ly1.tfm)
Provides:       tex(PlyfrDisplay-Bold-osf-sc-ly1.vf)
Provides:       tex(PlyfrDisplay-Bold-osf-sc-ot1--base.tfm)
Provides:       tex(PlyfrDisplay-Bold-osf-sc-ot1.tfm)
Provides:       tex(PlyfrDisplay-Bold-osf-sc-ot1.vf)
Provides:       tex(PlyfrDisplay-Bold-osf-sc-t1--base.tfm)
Provides:       tex(PlyfrDisplay-Bold-osf-sc-t1.tfm)
Provides:       tex(PlyfrDisplay-Bold-osf-sc-t1.vf)
Provides:       tex(PlyfrDisplay-Bold-osf-t1--base.tfm)
Provides:       tex(PlyfrDisplay-Bold-osf-t1.tfm)
Provides:       tex(PlyfrDisplay-Bold-osf-t1.vf)
Provides:       tex(PlyfrDisplay-Bold-osf-ts1--base.tfm)
Provides:       tex(PlyfrDisplay-Bold-osf-ts1.tfm)
Provides:       tex(PlyfrDisplay-Bold-osf-ts1.vf)
Provides:       tex(PlyfrDisplay-Bold-sup-ly1--base.tfm)
Provides:       tex(PlyfrDisplay-Bold-sup-ly1.tfm)
Provides:       tex(PlyfrDisplay-Bold-sup-ly1.vf)
Provides:       tex(PlyfrDisplay-Bold-sup-ot1.tfm)
Provides:       tex(PlyfrDisplay-Bold-sup-t1--base.tfm)
Provides:       tex(PlyfrDisplay-Bold-sup-t1.tfm)
Provides:       tex(PlyfrDisplay-Bold-sup-t1.vf)
Provides:       tex(PlyfrDisplay-BoldItalic-lf-ly1--base.tfm)
Provides:       tex(PlyfrDisplay-BoldItalic-lf-ly1.tfm)
Provides:       tex(PlyfrDisplay-BoldItalic-lf-ly1.vf)
Provides:       tex(PlyfrDisplay-BoldItalic-lf-ot1.tfm)
Provides:       tex(PlyfrDisplay-BoldItalic-lf-sc-ly1--base.tfm)
Provides:       tex(PlyfrDisplay-BoldItalic-lf-sc-ly1.tfm)
Provides:       tex(PlyfrDisplay-BoldItalic-lf-sc-ly1.vf)
Provides:       tex(PlyfrDisplay-BoldItalic-lf-sc-ot1--base.tfm)
Provides:       tex(PlyfrDisplay-BoldItalic-lf-sc-ot1.tfm)
Provides:       tex(PlyfrDisplay-BoldItalic-lf-sc-ot1.vf)
Provides:       tex(PlyfrDisplay-BoldItalic-lf-sc-t1--base.tfm)
Provides:       tex(PlyfrDisplay-BoldItalic-lf-sc-t1.tfm)
Provides:       tex(PlyfrDisplay-BoldItalic-lf-sc-t1.vf)
Provides:       tex(PlyfrDisplay-BoldItalic-lf-t1--base.tfm)
Provides:       tex(PlyfrDisplay-BoldItalic-lf-t1.tfm)
Provides:       tex(PlyfrDisplay-BoldItalic-lf-t1.vf)
Provides:       tex(PlyfrDisplay-BoldItalic-lf-ts1--base.tfm)
Provides:       tex(PlyfrDisplay-BoldItalic-lf-ts1.tfm)
Provides:       tex(PlyfrDisplay-BoldItalic-lf-ts1.vf)
Provides:       tex(PlyfrDisplay-BoldItalic-osf-ly1--base.tfm)
Provides:       tex(PlyfrDisplay-BoldItalic-osf-ly1.tfm)
Provides:       tex(PlyfrDisplay-BoldItalic-osf-ly1.vf)
Provides:       tex(PlyfrDisplay-BoldItalic-osf-ot1.tfm)
Provides:       tex(PlyfrDisplay-BoldItalic-osf-sc-ly1--base.tfm)
Provides:       tex(PlyfrDisplay-BoldItalic-osf-sc-ly1.tfm)
Provides:       tex(PlyfrDisplay-BoldItalic-osf-sc-ly1.vf)
Provides:       tex(PlyfrDisplay-BoldItalic-osf-sc-ot1--base.tfm)
Provides:       tex(PlyfrDisplay-BoldItalic-osf-sc-ot1.tfm)
Provides:       tex(PlyfrDisplay-BoldItalic-osf-sc-ot1.vf)
Provides:       tex(PlyfrDisplay-BoldItalic-osf-sc-t1--base.tfm)
Provides:       tex(PlyfrDisplay-BoldItalic-osf-sc-t1.tfm)
Provides:       tex(PlyfrDisplay-BoldItalic-osf-sc-t1.vf)
Provides:       tex(PlyfrDisplay-BoldItalic-osf-t1--base.tfm)
Provides:       tex(PlyfrDisplay-BoldItalic-osf-t1.tfm)
Provides:       tex(PlyfrDisplay-BoldItalic-osf-t1.vf)
Provides:       tex(PlyfrDisplay-BoldItalic-osf-ts1--base.tfm)
Provides:       tex(PlyfrDisplay-BoldItalic-osf-ts1.tfm)
Provides:       tex(PlyfrDisplay-BoldItalic-osf-ts1.vf)
Provides:       tex(PlyfrDisplay-BoldItalic-sup-ly1--base.tfm)
Provides:       tex(PlyfrDisplay-BoldItalic-sup-ly1.tfm)
Provides:       tex(PlyfrDisplay-BoldItalic-sup-ly1.vf)
Provides:       tex(PlyfrDisplay-BoldItalic-sup-ot1.tfm)
Provides:       tex(PlyfrDisplay-BoldItalic-sup-t1--base.tfm)
Provides:       tex(PlyfrDisplay-BoldItalic-sup-t1.tfm)
Provides:       tex(PlyfrDisplay-BoldItalic-sup-t1.vf)
Provides:       tex(PlyfrDisplay-Italic-lf-ly1--base.tfm)
Provides:       tex(PlyfrDisplay-Italic-lf-ly1.tfm)
Provides:       tex(PlyfrDisplay-Italic-lf-ly1.vf)
Provides:       tex(PlyfrDisplay-Italic-lf-ot1.tfm)
Provides:       tex(PlyfrDisplay-Italic-lf-sc-ly1--base.tfm)
Provides:       tex(PlyfrDisplay-Italic-lf-sc-ly1.tfm)
Provides:       tex(PlyfrDisplay-Italic-lf-sc-ly1.vf)
Provides:       tex(PlyfrDisplay-Italic-lf-sc-ot1--base.tfm)
Provides:       tex(PlyfrDisplay-Italic-lf-sc-ot1.tfm)
Provides:       tex(PlyfrDisplay-Italic-lf-sc-ot1.vf)
Provides:       tex(PlyfrDisplay-Italic-lf-sc-t1--base.tfm)
Provides:       tex(PlyfrDisplay-Italic-lf-sc-t1.tfm)
Provides:       tex(PlyfrDisplay-Italic-lf-sc-t1.vf)
Provides:       tex(PlyfrDisplay-Italic-lf-t1--base.tfm)
Provides:       tex(PlyfrDisplay-Italic-lf-t1.tfm)
Provides:       tex(PlyfrDisplay-Italic-lf-t1.vf)
Provides:       tex(PlyfrDisplay-Italic-lf-ts1--base.tfm)
Provides:       tex(PlyfrDisplay-Italic-lf-ts1.tfm)
Provides:       tex(PlyfrDisplay-Italic-lf-ts1.vf)
Provides:       tex(PlyfrDisplay-Italic-osf-ly1--base.tfm)
Provides:       tex(PlyfrDisplay-Italic-osf-ly1.tfm)
Provides:       tex(PlyfrDisplay-Italic-osf-ly1.vf)
Provides:       tex(PlyfrDisplay-Italic-osf-ot1.tfm)
Provides:       tex(PlyfrDisplay-Italic-osf-sc-ly1--base.tfm)
Provides:       tex(PlyfrDisplay-Italic-osf-sc-ly1.tfm)
Provides:       tex(PlyfrDisplay-Italic-osf-sc-ly1.vf)
Provides:       tex(PlyfrDisplay-Italic-osf-sc-ot1--base.tfm)
Provides:       tex(PlyfrDisplay-Italic-osf-sc-ot1.tfm)
Provides:       tex(PlyfrDisplay-Italic-osf-sc-ot1.vf)
Provides:       tex(PlyfrDisplay-Italic-osf-sc-t1--base.tfm)
Provides:       tex(PlyfrDisplay-Italic-osf-sc-t1.tfm)
Provides:       tex(PlyfrDisplay-Italic-osf-sc-t1.vf)
Provides:       tex(PlyfrDisplay-Italic-osf-t1--base.tfm)
Provides:       tex(PlyfrDisplay-Italic-osf-t1.tfm)
Provides:       tex(PlyfrDisplay-Italic-osf-t1.vf)
Provides:       tex(PlyfrDisplay-Italic-osf-ts1--base.tfm)
Provides:       tex(PlyfrDisplay-Italic-osf-ts1.tfm)
Provides:       tex(PlyfrDisplay-Italic-osf-ts1.vf)
Provides:       tex(PlyfrDisplay-Italic-sup-ly1--base.tfm)
Provides:       tex(PlyfrDisplay-Italic-sup-ly1.tfm)
Provides:       tex(PlyfrDisplay-Italic-sup-ly1.vf)
Provides:       tex(PlyfrDisplay-Italic-sup-ot1.tfm)
Provides:       tex(PlyfrDisplay-Italic-sup-t1--base.tfm)
Provides:       tex(PlyfrDisplay-Italic-sup-t1.tfm)
Provides:       tex(PlyfrDisplay-Italic-sup-t1.vf)
Provides:       tex(PlyfrDisplay-Regular-lf-ly1--base.tfm)
Provides:       tex(PlyfrDisplay-Regular-lf-ly1.tfm)
Provides:       tex(PlyfrDisplay-Regular-lf-ly1.vf)
Provides:       tex(PlyfrDisplay-Regular-lf-ot1.tfm)
Provides:       tex(PlyfrDisplay-Regular-lf-sc-ly1--base.tfm)
Provides:       tex(PlyfrDisplay-Regular-lf-sc-ly1.tfm)
Provides:       tex(PlyfrDisplay-Regular-lf-sc-ly1.vf)
Provides:       tex(PlyfrDisplay-Regular-lf-sc-ot1--base.tfm)
Provides:       tex(PlyfrDisplay-Regular-lf-sc-ot1.tfm)
Provides:       tex(PlyfrDisplay-Regular-lf-sc-ot1.vf)
Provides:       tex(PlyfrDisplay-Regular-lf-sc-t1--base.tfm)
Provides:       tex(PlyfrDisplay-Regular-lf-sc-t1.tfm)
Provides:       tex(PlyfrDisplay-Regular-lf-sc-t1.vf)
Provides:       tex(PlyfrDisplay-Regular-lf-t1--base.tfm)
Provides:       tex(PlyfrDisplay-Regular-lf-t1.tfm)
Provides:       tex(PlyfrDisplay-Regular-lf-t1.vf)
Provides:       tex(PlyfrDisplay-Regular-lf-ts1--base.tfm)
Provides:       tex(PlyfrDisplay-Regular-lf-ts1.tfm)
Provides:       tex(PlyfrDisplay-Regular-lf-ts1.vf)
Provides:       tex(PlyfrDisplay-Regular-osf-ly1--base.tfm)
Provides:       tex(PlyfrDisplay-Regular-osf-ly1.tfm)
Provides:       tex(PlyfrDisplay-Regular-osf-ly1.vf)
Provides:       tex(PlyfrDisplay-Regular-osf-ot1.tfm)
Provides:       tex(PlyfrDisplay-Regular-osf-sc-ly1--base.tfm)
Provides:       tex(PlyfrDisplay-Regular-osf-sc-ly1.tfm)
Provides:       tex(PlyfrDisplay-Regular-osf-sc-ly1.vf)
Provides:       tex(PlyfrDisplay-Regular-osf-sc-ot1--base.tfm)
Provides:       tex(PlyfrDisplay-Regular-osf-sc-ot1.tfm)
Provides:       tex(PlyfrDisplay-Regular-osf-sc-ot1.vf)
Provides:       tex(PlyfrDisplay-Regular-osf-sc-t1--base.tfm)
Provides:       tex(PlyfrDisplay-Regular-osf-sc-t1.tfm)
Provides:       tex(PlyfrDisplay-Regular-osf-sc-t1.vf)
Provides:       tex(PlyfrDisplay-Regular-osf-t1--base.tfm)
Provides:       tex(PlyfrDisplay-Regular-osf-t1.tfm)
Provides:       tex(PlyfrDisplay-Regular-osf-t1.vf)
Provides:       tex(PlyfrDisplay-Regular-osf-ts1--base.tfm)
Provides:       tex(PlyfrDisplay-Regular-osf-ts1.tfm)
Provides:       tex(PlyfrDisplay-Regular-osf-ts1.vf)
Provides:       tex(PlyfrDisplay-Regular-sup-ly1--base.tfm)
Provides:       tex(PlyfrDisplay-Regular-sup-ly1.tfm)
Provides:       tex(PlyfrDisplay-Regular-sup-ly1.vf)
Provides:       tex(PlyfrDisplay-Regular-sup-ot1.tfm)
Provides:       tex(PlyfrDisplay-Regular-sup-t1--base.tfm)
Provides:       tex(PlyfrDisplay-Regular-sup-t1.tfm)
Provides:       tex(PlyfrDisplay-Regular-sup-t1.vf)
Provides:       tex(T1PlyfrDisplay-LF.fd)
Provides:       tex(T1PlyfrDisplay-OsF.fd)
Provides:       tex(T1PlyfrDisplay-Sup.fd)
Provides:       tex(TS1PlyfrDisplay-LF.fd)
Provides:       tex(TS1PlyfrDisplay-OsF.fd)
Provides:       tex(plyfr_3udzka.enc)
Provides:       tex(plyfr_4avjba.enc)
Provides:       tex(plyfr_4srszf.enc)
Provides:       tex(plyfr_b7y4dd.enc)
Provides:       tex(plyfr_chpa4l.enc)
Provides:       tex(plyfr_eb5cw4.enc)
Provides:       tex(plyfr_fmyrgi.enc)
Provides:       tex(plyfr_gb53zg.enc)
Provides:       tex(plyfr_h54wtc.enc)
Provides:       tex(plyfr_he4k5f.enc)
Provides:       tex(plyfr_j7rmxo.enc)
Provides:       tex(plyfr_jk5hji.enc)
Provides:       tex(plyfr_jowrio.enc)
Provides:       tex(plyfr_kdf3ua.enc)
Provides:       tex(plyfr_kzslp6.enc)
Provides:       tex(plyfr_me7kyw.enc)
Provides:       tex(plyfr_q6cjrr.enc)
Provides:       tex(plyfr_qfnkfj.enc)
Provides:       tex(plyfr_vw64ij.enc)
Provides:       tex(plyfr_ygz7pk.enc)
Requires:       tex(fontaxes.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(mweights.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xkeyval.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source14:       playfair.tar.xz
Source15:       playfair.doc.tar.xz

%description -n texlive-playfair
This package provides the PlayFairDisplay family of fonts,
designed by Claus Eggers Sorensen, for use with LaTeX,
pdfLaTeX, XeLaTeX and LuaLaTeX. PlayFairDisplay is well suited
for titling and headlines. It has an extra large x-height and
short descenders. It can be set with no leading if space is
tight, for instance in news headlines, or for stylistic effect
in titles. Capitals are extra short, and only very slightly
heavier than the lowercase characters. This helps achieve a
more even typographical colour when typesetting proper nouns
and initialisms.

%package -n texlive-playfair-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn56005
Release:        0
Summary:        Documentation for texlive-playfair
License:        OFL-1.1
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/

%description -n texlive-playfair-doc
This package includes the documentation for texlive-playfair

%package -n texlive-playfair-fonts
Version:        %{texlive_version}.%{texlive_noarch}.svn56005
Release:        0
Summary:        Severed fonts for texlive-playfair
License:        OFL-1.1
URL:            https://www.tug.org/texlive/
Group:          Productivity/Publishing/TeX/Fonts
%reconfigure_fonts_prereq
Requires(posttrans):fontconfig
Requires(posttrans):ghostscript-fonts-std
Requires(posttrans):mkfontdir
Requires(posttrans):mkfontscale
Requires(posttrans):xorg-x11-fonts-core

%description -n texlive-playfair-fonts
The  separated fonts package for texlive-playfair

%post -n texlive-playfair
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
echo 'addMap PlayfairDisplay.map' >> /var/run/texlive/run-updmap

%postun -n texlive-playfair
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    echo 'deleteMap PlayfairDisplay.map' >> /var/run/texlive/run-updmap
    exit 0
fi

%posttrans -n texlive-playfair
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-playfair-fonts

%files -n texlive-playfair-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/playfair/OFL.txt
%{_texmfdistdir}/doc/fonts/playfair/Playfair_Display_A4_specimen.pdf
%{_texmfdistdir}/doc/fonts/playfair/README
%{_texmfdistdir}/doc/fonts/playfair/playfair-samples.pdf
%{_texmfdistdir}/doc/fonts/playfair/playfair-samples.tex

%files -n texlive-playfair
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/enc/dvips/playfair/plyfr_3udzka.enc
%{_texmfdistdir}/fonts/enc/dvips/playfair/plyfr_4avjba.enc
%{_texmfdistdir}/fonts/enc/dvips/playfair/plyfr_4srszf.enc
%{_texmfdistdir}/fonts/enc/dvips/playfair/plyfr_b7y4dd.enc
%{_texmfdistdir}/fonts/enc/dvips/playfair/plyfr_chpa4l.enc
%{_texmfdistdir}/fonts/enc/dvips/playfair/plyfr_eb5cw4.enc
%{_texmfdistdir}/fonts/enc/dvips/playfair/plyfr_fmyrgi.enc
%{_texmfdistdir}/fonts/enc/dvips/playfair/plyfr_gb53zg.enc
%{_texmfdistdir}/fonts/enc/dvips/playfair/plyfr_h54wtc.enc
%{_texmfdistdir}/fonts/enc/dvips/playfair/plyfr_he4k5f.enc
%{_texmfdistdir}/fonts/enc/dvips/playfair/plyfr_j7rmxo.enc
%{_texmfdistdir}/fonts/enc/dvips/playfair/plyfr_jk5hji.enc
%{_texmfdistdir}/fonts/enc/dvips/playfair/plyfr_jowrio.enc
%{_texmfdistdir}/fonts/enc/dvips/playfair/plyfr_kdf3ua.enc
%{_texmfdistdir}/fonts/enc/dvips/playfair/plyfr_kzslp6.enc
%{_texmfdistdir}/fonts/enc/dvips/playfair/plyfr_me7kyw.enc
%{_texmfdistdir}/fonts/enc/dvips/playfair/plyfr_q6cjrr.enc
%{_texmfdistdir}/fonts/enc/dvips/playfair/plyfr_qfnkfj.enc
%{_texmfdistdir}/fonts/enc/dvips/playfair/plyfr_vw64ij.enc
%{_texmfdistdir}/fonts/enc/dvips/playfair/plyfr_ygz7pk.enc
%{_texmfdistdir}/fonts/map/dvips/playfair/PlayfairDisplay.map
%verify(link) %{_texmfdistdir}/fonts/opentype/public/playfair/PlayfairDisplay-Black.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/playfair/PlayfairDisplay-BlackItalic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/playfair/PlayfairDisplay-Bold.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/playfair/PlayfairDisplay-BoldItalic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/playfair/PlayfairDisplay-Italic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/playfair/PlayfairDisplay-Regular.otf
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Black-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Black-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Black-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Black-lf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Black-lf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Black-lf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Black-lf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Black-lf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Black-lf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Black-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Black-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Black-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Black-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Black-osf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Black-osf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Black-osf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Black-osf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Black-osf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Black-osf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Black-osf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Black-osf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Black-osf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Black-osf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Black-osf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Black-osf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Black-osf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Black-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Black-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Black-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Black-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Black-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-BlackItalic-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-BlackItalic-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-BlackItalic-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-BlackItalic-lf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-BlackItalic-lf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-BlackItalic-lf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-BlackItalic-lf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-BlackItalic-lf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-BlackItalic-lf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-BlackItalic-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-BlackItalic-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-BlackItalic-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-BlackItalic-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-BlackItalic-osf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-BlackItalic-osf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-BlackItalic-osf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-BlackItalic-osf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-BlackItalic-osf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-BlackItalic-osf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-BlackItalic-osf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-BlackItalic-osf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-BlackItalic-osf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-BlackItalic-osf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-BlackItalic-osf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-BlackItalic-osf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-BlackItalic-osf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-BlackItalic-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-BlackItalic-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-BlackItalic-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-BlackItalic-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-BlackItalic-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Bold-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Bold-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Bold-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Bold-lf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Bold-lf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Bold-lf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Bold-lf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Bold-lf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Bold-lf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Bold-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Bold-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Bold-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Bold-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Bold-osf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Bold-osf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Bold-osf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Bold-osf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Bold-osf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Bold-osf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Bold-osf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Bold-osf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Bold-osf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Bold-osf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Bold-osf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Bold-osf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Bold-osf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Bold-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Bold-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Bold-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Bold-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Bold-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-BoldItalic-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-BoldItalic-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-BoldItalic-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-BoldItalic-lf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-BoldItalic-lf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-BoldItalic-lf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-BoldItalic-lf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-BoldItalic-lf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-BoldItalic-lf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-BoldItalic-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-BoldItalic-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-BoldItalic-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-BoldItalic-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-BoldItalic-osf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-BoldItalic-osf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-BoldItalic-osf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-BoldItalic-osf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-BoldItalic-osf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-BoldItalic-osf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-BoldItalic-osf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-BoldItalic-osf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-BoldItalic-osf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-BoldItalic-osf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-BoldItalic-osf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-BoldItalic-osf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-BoldItalic-osf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-BoldItalic-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-BoldItalic-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-BoldItalic-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-BoldItalic-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-BoldItalic-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Italic-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Italic-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Italic-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Italic-lf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Italic-lf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Italic-lf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Italic-lf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Italic-lf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Italic-lf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Italic-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Italic-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Italic-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Italic-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Italic-osf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Italic-osf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Italic-osf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Italic-osf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Italic-osf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Italic-osf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Italic-osf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Italic-osf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Italic-osf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Italic-osf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Italic-osf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Italic-osf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Italic-osf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Italic-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Italic-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Italic-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Italic-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Italic-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Regular-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Regular-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Regular-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Regular-lf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Regular-lf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Regular-lf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Regular-lf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Regular-lf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Regular-lf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Regular-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Regular-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Regular-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Regular-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Regular-osf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Regular-osf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Regular-osf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Regular-osf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Regular-osf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Regular-osf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Regular-osf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Regular-osf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Regular-osf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Regular-osf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Regular-osf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Regular-osf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Regular-osf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Regular-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Regular-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Regular-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Regular-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlyfrDisplay-Regular-sup-t1.tfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/playfair/PlyfrDisplay-Black.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/playfair/PlyfrDisplay-BlackItalic.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/playfair/PlyfrDisplay-Bold.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/playfair/PlyfrDisplay-BoldItalic.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/playfair/PlyfrDisplay-Italic.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/playfair/PlyfrDisplay-Regular.pfb
%{_texmfdistdir}/fonts/vf/public/playfair/PlyfrDisplay-Black-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlyfrDisplay-Black-lf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlyfrDisplay-Black-lf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlyfrDisplay-Black-lf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlyfrDisplay-Black-lf-t1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlyfrDisplay-Black-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlyfrDisplay-Black-osf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlyfrDisplay-Black-osf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlyfrDisplay-Black-osf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlyfrDisplay-Black-osf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlyfrDisplay-Black-osf-t1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlyfrDisplay-Black-osf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlyfrDisplay-Black-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlyfrDisplay-Black-sup-t1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlyfrDisplay-BlackItalic-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlyfrDisplay-BlackItalic-lf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlyfrDisplay-BlackItalic-lf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlyfrDisplay-BlackItalic-lf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlyfrDisplay-BlackItalic-lf-t1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlyfrDisplay-BlackItalic-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlyfrDisplay-BlackItalic-osf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlyfrDisplay-BlackItalic-osf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlyfrDisplay-BlackItalic-osf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlyfrDisplay-BlackItalic-osf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlyfrDisplay-BlackItalic-osf-t1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlyfrDisplay-BlackItalic-osf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlyfrDisplay-BlackItalic-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlyfrDisplay-BlackItalic-sup-t1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlyfrDisplay-Bold-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlyfrDisplay-Bold-lf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlyfrDisplay-Bold-lf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlyfrDisplay-Bold-lf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlyfrDisplay-Bold-lf-t1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlyfrDisplay-Bold-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlyfrDisplay-Bold-osf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlyfrDisplay-Bold-osf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlyfrDisplay-Bold-osf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlyfrDisplay-Bold-osf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlyfrDisplay-Bold-osf-t1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlyfrDisplay-Bold-osf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlyfrDisplay-Bold-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlyfrDisplay-Bold-sup-t1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlyfrDisplay-BoldItalic-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlyfrDisplay-BoldItalic-lf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlyfrDisplay-BoldItalic-lf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlyfrDisplay-BoldItalic-lf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlyfrDisplay-BoldItalic-lf-t1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlyfrDisplay-BoldItalic-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlyfrDisplay-BoldItalic-osf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlyfrDisplay-BoldItalic-osf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlyfrDisplay-BoldItalic-osf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlyfrDisplay-BoldItalic-osf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlyfrDisplay-BoldItalic-osf-t1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlyfrDisplay-BoldItalic-osf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlyfrDisplay-BoldItalic-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlyfrDisplay-BoldItalic-sup-t1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlyfrDisplay-Italic-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlyfrDisplay-Italic-lf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlyfrDisplay-Italic-lf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlyfrDisplay-Italic-lf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlyfrDisplay-Italic-lf-t1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlyfrDisplay-Italic-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlyfrDisplay-Italic-osf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlyfrDisplay-Italic-osf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlyfrDisplay-Italic-osf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlyfrDisplay-Italic-osf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlyfrDisplay-Italic-osf-t1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlyfrDisplay-Italic-osf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlyfrDisplay-Italic-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlyfrDisplay-Italic-sup-t1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlyfrDisplay-Regular-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlyfrDisplay-Regular-lf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlyfrDisplay-Regular-lf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlyfrDisplay-Regular-lf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlyfrDisplay-Regular-lf-t1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlyfrDisplay-Regular-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlyfrDisplay-Regular-osf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlyfrDisplay-Regular-osf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlyfrDisplay-Regular-osf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlyfrDisplay-Regular-osf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlyfrDisplay-Regular-osf-t1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlyfrDisplay-Regular-osf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlyfrDisplay-Regular-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlyfrDisplay-Regular-sup-t1.vf
%{_texmfdistdir}/tex/latex/playfair/LY1PlyfrDisplay-LF.fd
%{_texmfdistdir}/tex/latex/playfair/LY1PlyfrDisplay-OsF.fd
%{_texmfdistdir}/tex/latex/playfair/LY1PlyfrDisplay-Sup.fd
%{_texmfdistdir}/tex/latex/playfair/OT1PlyfrDisplay-LF.fd
%{_texmfdistdir}/tex/latex/playfair/OT1PlyfrDisplay-OsF.fd
%{_texmfdistdir}/tex/latex/playfair/OT1PlyfrDisplay-Sup.fd
%{_texmfdistdir}/tex/latex/playfair/PlayfairDisplay.sty
%{_texmfdistdir}/tex/latex/playfair/T1PlyfrDisplay-LF.fd
%{_texmfdistdir}/tex/latex/playfair/T1PlyfrDisplay-OsF.fd
%{_texmfdistdir}/tex/latex/playfair/T1PlyfrDisplay-Sup.fd
%{_texmfdistdir}/tex/latex/playfair/TS1PlyfrDisplay-LF.fd
%{_texmfdistdir}/tex/latex/playfair/TS1PlyfrDisplay-OsF.fd

%files -n texlive-playfair-fonts
%defattr(-,root,root,755)
%dir %{_datadir}/fonts/texlive-playfair
%{_datadir}/fontconfig/conf.avail/58-texlive-playfair.conf
%{_datadir}/fontconfig/conf.avail/55-texlive-playfair.conf
%config %{_sysconfdir}/fonts/conf.d/55-texlive-playfair.conf
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-playfair/encodings.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-playfair/fonts.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-playfair/fonts.scale
%{_datadir}/fonts/texlive-playfair/PlayfairDisplay-Black.otf
%{_datadir}/fonts/texlive-playfair/PlayfairDisplay-BlackItalic.otf
%{_datadir}/fonts/texlive-playfair/PlayfairDisplay-Bold.otf
%{_datadir}/fonts/texlive-playfair/PlayfairDisplay-BoldItalic.otf
%{_datadir}/fonts/texlive-playfair/PlayfairDisplay-Italic.otf
%{_datadir}/fonts/texlive-playfair/PlayfairDisplay-Regular.otf
%{_datadir}/fonts/texlive-playfair/PlyfrDisplay-Black.pfb
%{_datadir}/fonts/texlive-playfair/PlyfrDisplay-BlackItalic.pfb
%{_datadir}/fonts/texlive-playfair/PlyfrDisplay-Bold.pfb
%{_datadir}/fonts/texlive-playfair/PlyfrDisplay-BoldItalic.pfb
%{_datadir}/fonts/texlive-playfair/PlyfrDisplay-Italic.pfb
%{_datadir}/fonts/texlive-playfair/PlyfrDisplay-Regular.pfb

%package -n texlive-plex
Version:        %{texlive_version}.%{texlive_noarch}.svn54512
Release:        0
License:        OFL-1.1
Summary:        Support for IBM Plex fonts
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(updmap.cfg)
#!BuildIgnore:  tex(updmap.cfg)
Requires(postun):findutils
Requires(postun):grep
Requires(postun):sed
Requires(postun):texlive >= %{texlive_version}
Requires(postun):tex(updmap.cfg)
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Requires:       texlive-plex-fonts >= %{texlive_version}
Suggests:       texlive-plex-doc >= %{texlive_version}
Provides:       tex(IBMPlexMono-Bold-sup-ly1--base.tfm)
Provides:       tex(IBMPlexMono-Bold-sup-ly1.tfm)
Provides:       tex(IBMPlexMono-Bold-sup-ly1.vf)
Provides:       tex(IBMPlexMono-Bold-sup-ot1.tfm)
Provides:       tex(IBMPlexMono-Bold-sup-t1--base.tfm)
Provides:       tex(IBMPlexMono-Bold-sup-t1.tfm)
Provides:       tex(IBMPlexMono-Bold-sup-t1.vf)
Provides:       tex(IBMPlexMono-Bold-tlf-ly1--base.tfm)
Provides:       tex(IBMPlexMono-Bold-tlf-ly1.tfm)
Provides:       tex(IBMPlexMono-Bold-tlf-ly1.vf)
Provides:       tex(IBMPlexMono-Bold-tlf-ot1.tfm)
Provides:       tex(IBMPlexMono-Bold-tlf-t1--base.tfm)
Provides:       tex(IBMPlexMono-Bold-tlf-t1.tfm)
Provides:       tex(IBMPlexMono-Bold-tlf-t1.vf)
Provides:       tex(IBMPlexMono-Bold-tlf-ts1--base.tfm)
Provides:       tex(IBMPlexMono-Bold-tlf-ts1.tfm)
Provides:       tex(IBMPlexMono-Bold-tlf-ts1.vf)
Provides:       tex(IBMPlexMono-BoldItalic-sup-ly1--base.tfm)
Provides:       tex(IBMPlexMono-BoldItalic-sup-ly1.tfm)
Provides:       tex(IBMPlexMono-BoldItalic-sup-ly1.vf)
Provides:       tex(IBMPlexMono-BoldItalic-sup-ot1.tfm)
Provides:       tex(IBMPlexMono-BoldItalic-sup-t1--base.tfm)
Provides:       tex(IBMPlexMono-BoldItalic-sup-t1.tfm)
Provides:       tex(IBMPlexMono-BoldItalic-sup-t1.vf)
Provides:       tex(IBMPlexMono-BoldItalic-tlf-ly1--base.tfm)
Provides:       tex(IBMPlexMono-BoldItalic-tlf-ly1.tfm)
Provides:       tex(IBMPlexMono-BoldItalic-tlf-ly1.vf)
Provides:       tex(IBMPlexMono-BoldItalic-tlf-ot1.tfm)
Provides:       tex(IBMPlexMono-BoldItalic-tlf-t1--base.tfm)
Provides:       tex(IBMPlexMono-BoldItalic-tlf-t1.tfm)
Provides:       tex(IBMPlexMono-BoldItalic-tlf-t1.vf)
Provides:       tex(IBMPlexMono-BoldItalic-tlf-ts1--base.tfm)
Provides:       tex(IBMPlexMono-BoldItalic-tlf-ts1.tfm)
Provides:       tex(IBMPlexMono-BoldItalic-tlf-ts1.vf)
Provides:       tex(IBMPlexMono-ExtraLight-sup-ly1--base.tfm)
Provides:       tex(IBMPlexMono-ExtraLight-sup-ly1.tfm)
Provides:       tex(IBMPlexMono-ExtraLight-sup-ly1.vf)
Provides:       tex(IBMPlexMono-ExtraLight-sup-ot1.tfm)
Provides:       tex(IBMPlexMono-ExtraLight-sup-t1--base.tfm)
Provides:       tex(IBMPlexMono-ExtraLight-sup-t1.tfm)
Provides:       tex(IBMPlexMono-ExtraLight-sup-t1.vf)
Provides:       tex(IBMPlexMono-ExtraLight-tlf-ly1--base.tfm)
Provides:       tex(IBMPlexMono-ExtraLight-tlf-ly1.tfm)
Provides:       tex(IBMPlexMono-ExtraLight-tlf-ly1.vf)
Provides:       tex(IBMPlexMono-ExtraLight-tlf-ot1.tfm)
Provides:       tex(IBMPlexMono-ExtraLight-tlf-t1--base.tfm)
Provides:       tex(IBMPlexMono-ExtraLight-tlf-t1.tfm)
Provides:       tex(IBMPlexMono-ExtraLight-tlf-t1.vf)
Provides:       tex(IBMPlexMono-ExtraLight-tlf-ts1--base.tfm)
Provides:       tex(IBMPlexMono-ExtraLight-tlf-ts1.tfm)
Provides:       tex(IBMPlexMono-ExtraLight-tlf-ts1.vf)
Provides:       tex(IBMPlexMono-ExtraLightItalic-sup-ly1--base.tfm)
Provides:       tex(IBMPlexMono-ExtraLightItalic-sup-ly1.tfm)
Provides:       tex(IBMPlexMono-ExtraLightItalic-sup-ly1.vf)
Provides:       tex(IBMPlexMono-ExtraLightItalic-sup-ot1.tfm)
Provides:       tex(IBMPlexMono-ExtraLightItalic-sup-t1--base.tfm)
Provides:       tex(IBMPlexMono-ExtraLightItalic-sup-t1.tfm)
Provides:       tex(IBMPlexMono-ExtraLightItalic-sup-t1.vf)
Provides:       tex(IBMPlexMono-ExtraLightItalic-tlf-ly1--base.tfm)
Provides:       tex(IBMPlexMono-ExtraLightItalic-tlf-ly1.tfm)
Provides:       tex(IBMPlexMono-ExtraLightItalic-tlf-ly1.vf)
Provides:       tex(IBMPlexMono-ExtraLightItalic-tlf-ot1.tfm)
Provides:       tex(IBMPlexMono-ExtraLightItalic-tlf-t1--base.tfm)
Provides:       tex(IBMPlexMono-ExtraLightItalic-tlf-t1.tfm)
Provides:       tex(IBMPlexMono-ExtraLightItalic-tlf-t1.vf)
Provides:       tex(IBMPlexMono-ExtraLightItalic-tlf-ts1--base.tfm)
Provides:       tex(IBMPlexMono-ExtraLightItalic-tlf-ts1.tfm)
Provides:       tex(IBMPlexMono-ExtraLightItalic-tlf-ts1.vf)
Provides:       tex(IBMPlexMono-Italic-sup-ly1--base.tfm)
Provides:       tex(IBMPlexMono-Italic-sup-ly1.tfm)
Provides:       tex(IBMPlexMono-Italic-sup-ly1.vf)
Provides:       tex(IBMPlexMono-Italic-sup-ot1.tfm)
Provides:       tex(IBMPlexMono-Italic-sup-t1--base.tfm)
Provides:       tex(IBMPlexMono-Italic-sup-t1.tfm)
Provides:       tex(IBMPlexMono-Italic-sup-t1.vf)
Provides:       tex(IBMPlexMono-Italic-tlf-ly1--base.tfm)
Provides:       tex(IBMPlexMono-Italic-tlf-ly1.tfm)
Provides:       tex(IBMPlexMono-Italic-tlf-ly1.vf)
Provides:       tex(IBMPlexMono-Italic-tlf-ot1.tfm)
Provides:       tex(IBMPlexMono-Italic-tlf-t1--base.tfm)
Provides:       tex(IBMPlexMono-Italic-tlf-t1.tfm)
Provides:       tex(IBMPlexMono-Italic-tlf-t1.vf)
Provides:       tex(IBMPlexMono-Italic-tlf-ts1--base.tfm)
Provides:       tex(IBMPlexMono-Italic-tlf-ts1.tfm)
Provides:       tex(IBMPlexMono-Italic-tlf-ts1.vf)
Provides:       tex(IBMPlexMono-Light-sup-ly1--base.tfm)
Provides:       tex(IBMPlexMono-Light-sup-ly1.tfm)
Provides:       tex(IBMPlexMono-Light-sup-ly1.vf)
Provides:       tex(IBMPlexMono-Light-sup-ot1.tfm)
Provides:       tex(IBMPlexMono-Light-sup-t1--base.tfm)
Provides:       tex(IBMPlexMono-Light-sup-t1.tfm)
Provides:       tex(IBMPlexMono-Light-sup-t1.vf)
Provides:       tex(IBMPlexMono-Light-tlf-ly1--base.tfm)
Provides:       tex(IBMPlexMono-Light-tlf-ly1.tfm)
Provides:       tex(IBMPlexMono-Light-tlf-ly1.vf)
Provides:       tex(IBMPlexMono-Light-tlf-ot1.tfm)
Provides:       tex(IBMPlexMono-Light-tlf-t1--base.tfm)
Provides:       tex(IBMPlexMono-Light-tlf-t1.tfm)
Provides:       tex(IBMPlexMono-Light-tlf-t1.vf)
Provides:       tex(IBMPlexMono-Light-tlf-ts1--base.tfm)
Provides:       tex(IBMPlexMono-Light-tlf-ts1.tfm)
Provides:       tex(IBMPlexMono-Light-tlf-ts1.vf)
Provides:       tex(IBMPlexMono-LightItalic-sup-ly1--base.tfm)
Provides:       tex(IBMPlexMono-LightItalic-sup-ly1.tfm)
Provides:       tex(IBMPlexMono-LightItalic-sup-ly1.vf)
Provides:       tex(IBMPlexMono-LightItalic-sup-ot1.tfm)
Provides:       tex(IBMPlexMono-LightItalic-sup-t1--base.tfm)
Provides:       tex(IBMPlexMono-LightItalic-sup-t1.tfm)
Provides:       tex(IBMPlexMono-LightItalic-sup-t1.vf)
Provides:       tex(IBMPlexMono-LightItalic-tlf-ly1--base.tfm)
Provides:       tex(IBMPlexMono-LightItalic-tlf-ly1.tfm)
Provides:       tex(IBMPlexMono-LightItalic-tlf-ly1.vf)
Provides:       tex(IBMPlexMono-LightItalic-tlf-ot1.tfm)
Provides:       tex(IBMPlexMono-LightItalic-tlf-t1--base.tfm)
Provides:       tex(IBMPlexMono-LightItalic-tlf-t1.tfm)
Provides:       tex(IBMPlexMono-LightItalic-tlf-t1.vf)
Provides:       tex(IBMPlexMono-LightItalic-tlf-ts1--base.tfm)
Provides:       tex(IBMPlexMono-LightItalic-tlf-ts1.tfm)
Provides:       tex(IBMPlexMono-LightItalic-tlf-ts1.vf)
Provides:       tex(IBMPlexMono-Medium-sup-ly1--base.tfm)
Provides:       tex(IBMPlexMono-Medium-sup-ly1.tfm)
Provides:       tex(IBMPlexMono-Medium-sup-ly1.vf)
Provides:       tex(IBMPlexMono-Medium-sup-ot1.tfm)
Provides:       tex(IBMPlexMono-Medium-sup-t1--base.tfm)
Provides:       tex(IBMPlexMono-Medium-sup-t1.tfm)
Provides:       tex(IBMPlexMono-Medium-sup-t1.vf)
Provides:       tex(IBMPlexMono-Medium-tlf-ly1--base.tfm)
Provides:       tex(IBMPlexMono-Medium-tlf-ly1.tfm)
Provides:       tex(IBMPlexMono-Medium-tlf-ly1.vf)
Provides:       tex(IBMPlexMono-Medium-tlf-ot1.tfm)
Provides:       tex(IBMPlexMono-Medium-tlf-t1--base.tfm)
Provides:       tex(IBMPlexMono-Medium-tlf-t1.tfm)
Provides:       tex(IBMPlexMono-Medium-tlf-t1.vf)
Provides:       tex(IBMPlexMono-Medium-tlf-ts1--base.tfm)
Provides:       tex(IBMPlexMono-Medium-tlf-ts1.tfm)
Provides:       tex(IBMPlexMono-Medium-tlf-ts1.vf)
Provides:       tex(IBMPlexMono-MediumItalic-sup-ly1--base.tfm)
Provides:       tex(IBMPlexMono-MediumItalic-sup-ly1.tfm)
Provides:       tex(IBMPlexMono-MediumItalic-sup-ly1.vf)
Provides:       tex(IBMPlexMono-MediumItalic-sup-ot1.tfm)
Provides:       tex(IBMPlexMono-MediumItalic-sup-t1--base.tfm)
Provides:       tex(IBMPlexMono-MediumItalic-sup-t1.tfm)
Provides:       tex(IBMPlexMono-MediumItalic-sup-t1.vf)
Provides:       tex(IBMPlexMono-MediumItalic-tlf-ly1--base.tfm)
Provides:       tex(IBMPlexMono-MediumItalic-tlf-ly1.tfm)
Provides:       tex(IBMPlexMono-MediumItalic-tlf-ly1.vf)
Provides:       tex(IBMPlexMono-MediumItalic-tlf-ot1.tfm)
Provides:       tex(IBMPlexMono-MediumItalic-tlf-t1--base.tfm)
Provides:       tex(IBMPlexMono-MediumItalic-tlf-t1.tfm)
Provides:       tex(IBMPlexMono-MediumItalic-tlf-t1.vf)
Provides:       tex(IBMPlexMono-MediumItalic-tlf-ts1--base.tfm)
Provides:       tex(IBMPlexMono-MediumItalic-tlf-ts1.tfm)
Provides:       tex(IBMPlexMono-MediumItalic-tlf-ts1.vf)
Provides:       tex(IBMPlexMono-SemiBold-sup-ly1--base.tfm)
Provides:       tex(IBMPlexMono-SemiBold-sup-ly1.tfm)
Provides:       tex(IBMPlexMono-SemiBold-sup-ly1.vf)
Provides:       tex(IBMPlexMono-SemiBold-sup-ot1.tfm)
Provides:       tex(IBMPlexMono-SemiBold-sup-t1--base.tfm)
Provides:       tex(IBMPlexMono-SemiBold-sup-t1.tfm)
Provides:       tex(IBMPlexMono-SemiBold-sup-t1.vf)
Provides:       tex(IBMPlexMono-SemiBold-tlf-ly1--base.tfm)
Provides:       tex(IBMPlexMono-SemiBold-tlf-ly1.tfm)
Provides:       tex(IBMPlexMono-SemiBold-tlf-ly1.vf)
Provides:       tex(IBMPlexMono-SemiBold-tlf-ot1.tfm)
Provides:       tex(IBMPlexMono-SemiBold-tlf-t1--base.tfm)
Provides:       tex(IBMPlexMono-SemiBold-tlf-t1.tfm)
Provides:       tex(IBMPlexMono-SemiBold-tlf-t1.vf)
Provides:       tex(IBMPlexMono-SemiBold-tlf-ts1--base.tfm)
Provides:       tex(IBMPlexMono-SemiBold-tlf-ts1.tfm)
Provides:       tex(IBMPlexMono-SemiBold-tlf-ts1.vf)
Provides:       tex(IBMPlexMono-SemiBoldItalic-sup-ly1--base.tfm)
Provides:       tex(IBMPlexMono-SemiBoldItalic-sup-ly1.tfm)
Provides:       tex(IBMPlexMono-SemiBoldItalic-sup-ly1.vf)
Provides:       tex(IBMPlexMono-SemiBoldItalic-sup-ot1.tfm)
Provides:       tex(IBMPlexMono-SemiBoldItalic-sup-t1--base.tfm)
Provides:       tex(IBMPlexMono-SemiBoldItalic-sup-t1.tfm)
Provides:       tex(IBMPlexMono-SemiBoldItalic-sup-t1.vf)
Provides:       tex(IBMPlexMono-SemiBoldItalic-tlf-ly1--base.tfm)
Provides:       tex(IBMPlexMono-SemiBoldItalic-tlf-ly1.tfm)
Provides:       tex(IBMPlexMono-SemiBoldItalic-tlf-ly1.vf)
Provides:       tex(IBMPlexMono-SemiBoldItalic-tlf-ot1.tfm)
Provides:       tex(IBMPlexMono-SemiBoldItalic-tlf-t1--base.tfm)
Provides:       tex(IBMPlexMono-SemiBoldItalic-tlf-t1.tfm)
Provides:       tex(IBMPlexMono-SemiBoldItalic-tlf-t1.vf)
Provides:       tex(IBMPlexMono-SemiBoldItalic-tlf-ts1--base.tfm)
Provides:       tex(IBMPlexMono-SemiBoldItalic-tlf-ts1.tfm)
Provides:       tex(IBMPlexMono-SemiBoldItalic-tlf-ts1.vf)
Provides:       tex(IBMPlexMono-Text-sup-ly1--base.tfm)
Provides:       tex(IBMPlexMono-Text-sup-ly1.tfm)
Provides:       tex(IBMPlexMono-Text-sup-ly1.vf)
Provides:       tex(IBMPlexMono-Text-sup-ot1.tfm)
Provides:       tex(IBMPlexMono-Text-sup-t1--base.tfm)
Provides:       tex(IBMPlexMono-Text-sup-t1.tfm)
Provides:       tex(IBMPlexMono-Text-sup-t1.vf)
Provides:       tex(IBMPlexMono-Text-tlf-ly1--base.tfm)
Provides:       tex(IBMPlexMono-Text-tlf-ly1.tfm)
Provides:       tex(IBMPlexMono-Text-tlf-ly1.vf)
Provides:       tex(IBMPlexMono-Text-tlf-ot1.tfm)
Provides:       tex(IBMPlexMono-Text-tlf-t1--base.tfm)
Provides:       tex(IBMPlexMono-Text-tlf-t1.tfm)
Provides:       tex(IBMPlexMono-Text-tlf-t1.vf)
Provides:       tex(IBMPlexMono-Text-tlf-ts1--base.tfm)
Provides:       tex(IBMPlexMono-Text-tlf-ts1.tfm)
Provides:       tex(IBMPlexMono-Text-tlf-ts1.vf)
Provides:       tex(IBMPlexMono-TextItalic-sup-ly1--base.tfm)
Provides:       tex(IBMPlexMono-TextItalic-sup-ly1.tfm)
Provides:       tex(IBMPlexMono-TextItalic-sup-ly1.vf)
Provides:       tex(IBMPlexMono-TextItalic-sup-ot1.tfm)
Provides:       tex(IBMPlexMono-TextItalic-sup-t1--base.tfm)
Provides:       tex(IBMPlexMono-TextItalic-sup-t1.tfm)
Provides:       tex(IBMPlexMono-TextItalic-sup-t1.vf)
Provides:       tex(IBMPlexMono-TextItalic-tlf-ly1--base.tfm)
Provides:       tex(IBMPlexMono-TextItalic-tlf-ly1.tfm)
Provides:       tex(IBMPlexMono-TextItalic-tlf-ly1.vf)
Provides:       tex(IBMPlexMono-TextItalic-tlf-ot1.tfm)
Provides:       tex(IBMPlexMono-TextItalic-tlf-t1--base.tfm)
Provides:       tex(IBMPlexMono-TextItalic-tlf-t1.tfm)
Provides:       tex(IBMPlexMono-TextItalic-tlf-t1.vf)
Provides:       tex(IBMPlexMono-TextItalic-tlf-ts1--base.tfm)
Provides:       tex(IBMPlexMono-TextItalic-tlf-ts1.tfm)
Provides:       tex(IBMPlexMono-TextItalic-tlf-ts1.vf)
Provides:       tex(IBMPlexMono-Thin-sup-ly1--base.tfm)
Provides:       tex(IBMPlexMono-Thin-sup-ly1.tfm)
Provides:       tex(IBMPlexMono-Thin-sup-ly1.vf)
Provides:       tex(IBMPlexMono-Thin-sup-ot1.tfm)
Provides:       tex(IBMPlexMono-Thin-sup-t1--base.tfm)
Provides:       tex(IBMPlexMono-Thin-sup-t1.tfm)
Provides:       tex(IBMPlexMono-Thin-sup-t1.vf)
Provides:       tex(IBMPlexMono-Thin-tlf-ly1--base.tfm)
Provides:       tex(IBMPlexMono-Thin-tlf-ly1.tfm)
Provides:       tex(IBMPlexMono-Thin-tlf-ly1.vf)
Provides:       tex(IBMPlexMono-Thin-tlf-ot1.tfm)
Provides:       tex(IBMPlexMono-Thin-tlf-t1--base.tfm)
Provides:       tex(IBMPlexMono-Thin-tlf-t1.tfm)
Provides:       tex(IBMPlexMono-Thin-tlf-t1.vf)
Provides:       tex(IBMPlexMono-Thin-tlf-ts1--base.tfm)
Provides:       tex(IBMPlexMono-Thin-tlf-ts1.tfm)
Provides:       tex(IBMPlexMono-Thin-tlf-ts1.vf)
Provides:       tex(IBMPlexMono-ThinItalic-sup-ly1--base.tfm)
Provides:       tex(IBMPlexMono-ThinItalic-sup-ly1.tfm)
Provides:       tex(IBMPlexMono-ThinItalic-sup-ly1.vf)
Provides:       tex(IBMPlexMono-ThinItalic-sup-ot1.tfm)
Provides:       tex(IBMPlexMono-ThinItalic-sup-t1--base.tfm)
Provides:       tex(IBMPlexMono-ThinItalic-sup-t1.tfm)
Provides:       tex(IBMPlexMono-ThinItalic-sup-t1.vf)
Provides:       tex(IBMPlexMono-ThinItalic-tlf-ly1--base.tfm)
Provides:       tex(IBMPlexMono-ThinItalic-tlf-ly1.tfm)
Provides:       tex(IBMPlexMono-ThinItalic-tlf-ly1.vf)
Provides:       tex(IBMPlexMono-ThinItalic-tlf-ot1.tfm)
Provides:       tex(IBMPlexMono-ThinItalic-tlf-t1--base.tfm)
Provides:       tex(IBMPlexMono-ThinItalic-tlf-t1.tfm)
Provides:       tex(IBMPlexMono-ThinItalic-tlf-t1.vf)
Provides:       tex(IBMPlexMono-ThinItalic-tlf-ts1--base.tfm)
Provides:       tex(IBMPlexMono-ThinItalic-tlf-ts1.tfm)
Provides:       tex(IBMPlexMono-ThinItalic-tlf-ts1.vf)
Provides:       tex(IBMPlexMono-sup-ly1--base.tfm)
Provides:       tex(IBMPlexMono-sup-ly1.tfm)
Provides:       tex(IBMPlexMono-sup-ly1.vf)
Provides:       tex(IBMPlexMono-sup-ot1.tfm)
Provides:       tex(IBMPlexMono-sup-t1--base.tfm)
Provides:       tex(IBMPlexMono-sup-t1.tfm)
Provides:       tex(IBMPlexMono-sup-t1.vf)
Provides:       tex(IBMPlexMono-tlf-ly1--base.tfm)
Provides:       tex(IBMPlexMono-tlf-ly1.tfm)
Provides:       tex(IBMPlexMono-tlf-ly1.vf)
Provides:       tex(IBMPlexMono-tlf-ot1.tfm)
Provides:       tex(IBMPlexMono-tlf-t1--base.tfm)
Provides:       tex(IBMPlexMono-tlf-t1.tfm)
Provides:       tex(IBMPlexMono-tlf-t1.vf)
Provides:       tex(IBMPlexMono-tlf-ts1--base.tfm)
Provides:       tex(IBMPlexMono-tlf-ts1.tfm)
Provides:       tex(IBMPlexMono-tlf-ts1.vf)
Provides:       tex(IBMPlexSans-Bold-sup-lgr--base.tfm)
Provides:       tex(IBMPlexSans-Bold-sup-lgr.tfm)
Provides:       tex(IBMPlexSans-Bold-sup-lgr.vf)
Provides:       tex(IBMPlexSans-Bold-sup-ly1--base.tfm)
Provides:       tex(IBMPlexSans-Bold-sup-ly1.tfm)
Provides:       tex(IBMPlexSans-Bold-sup-ly1.vf)
Provides:       tex(IBMPlexSans-Bold-sup-ot1.tfm)
Provides:       tex(IBMPlexSans-Bold-sup-t1--base.tfm)
Provides:       tex(IBMPlexSans-Bold-sup-t1.tfm)
Provides:       tex(IBMPlexSans-Bold-sup-t1.vf)
Provides:       tex(IBMPlexSans-Bold-tlf-lgr--base.tfm)
Provides:       tex(IBMPlexSans-Bold-tlf-lgr.tfm)
Provides:       tex(IBMPlexSans-Bold-tlf-lgr.vf)
Provides:       tex(IBMPlexSans-Bold-tlf-ly1--base.tfm)
Provides:       tex(IBMPlexSans-Bold-tlf-ly1.tfm)
Provides:       tex(IBMPlexSans-Bold-tlf-ly1.vf)
Provides:       tex(IBMPlexSans-Bold-tlf-ot1.tfm)
Provides:       tex(IBMPlexSans-Bold-tlf-t1--base.tfm)
Provides:       tex(IBMPlexSans-Bold-tlf-t1.tfm)
Provides:       tex(IBMPlexSans-Bold-tlf-t1.vf)
Provides:       tex(IBMPlexSans-Bold-tlf-ts1--base.tfm)
Provides:       tex(IBMPlexSans-Bold-tlf-ts1.tfm)
Provides:       tex(IBMPlexSans-Bold-tlf-ts1.vf)
Provides:       tex(IBMPlexSans-BoldItalic-sup-lgr--base.tfm)
Provides:       tex(IBMPlexSans-BoldItalic-sup-lgr.tfm)
Provides:       tex(IBMPlexSans-BoldItalic-sup-lgr.vf)
Provides:       tex(IBMPlexSans-BoldItalic-sup-ly1--base.tfm)
Provides:       tex(IBMPlexSans-BoldItalic-sup-ly1.tfm)
Provides:       tex(IBMPlexSans-BoldItalic-sup-ly1.vf)
Provides:       tex(IBMPlexSans-BoldItalic-sup-ot1.tfm)
Provides:       tex(IBMPlexSans-BoldItalic-sup-t1--base.tfm)
Provides:       tex(IBMPlexSans-BoldItalic-sup-t1.tfm)
Provides:       tex(IBMPlexSans-BoldItalic-sup-t1.vf)
Provides:       tex(IBMPlexSans-BoldItalic-tlf-lgr--base.tfm)
Provides:       tex(IBMPlexSans-BoldItalic-tlf-lgr.tfm)
Provides:       tex(IBMPlexSans-BoldItalic-tlf-lgr.vf)
Provides:       tex(IBMPlexSans-BoldItalic-tlf-ly1--base.tfm)
Provides:       tex(IBMPlexSans-BoldItalic-tlf-ly1.tfm)
Provides:       tex(IBMPlexSans-BoldItalic-tlf-ly1.vf)
Provides:       tex(IBMPlexSans-BoldItalic-tlf-ot1.tfm)
Provides:       tex(IBMPlexSans-BoldItalic-tlf-t1--base.tfm)
Provides:       tex(IBMPlexSans-BoldItalic-tlf-t1.tfm)
Provides:       tex(IBMPlexSans-BoldItalic-tlf-t1.vf)
Provides:       tex(IBMPlexSans-BoldItalic-tlf-ts1--base.tfm)
Provides:       tex(IBMPlexSans-BoldItalic-tlf-ts1.tfm)
Provides:       tex(IBMPlexSans-BoldItalic-tlf-ts1.vf)
Provides:       tex(IBMPlexSans-ExtraLight-sup-lgr--base.tfm)
Provides:       tex(IBMPlexSans-ExtraLight-sup-lgr.tfm)
Provides:       tex(IBMPlexSans-ExtraLight-sup-lgr.vf)
Provides:       tex(IBMPlexSans-ExtraLight-sup-ly1--base.tfm)
Provides:       tex(IBMPlexSans-ExtraLight-sup-ly1.tfm)
Provides:       tex(IBMPlexSans-ExtraLight-sup-ly1.vf)
Provides:       tex(IBMPlexSans-ExtraLight-sup-ot1.tfm)
Provides:       tex(IBMPlexSans-ExtraLight-sup-t1--base.tfm)
Provides:       tex(IBMPlexSans-ExtraLight-sup-t1.tfm)
Provides:       tex(IBMPlexSans-ExtraLight-sup-t1.vf)
Provides:       tex(IBMPlexSans-ExtraLight-tlf-lgr--base.tfm)
Provides:       tex(IBMPlexSans-ExtraLight-tlf-lgr.tfm)
Provides:       tex(IBMPlexSans-ExtraLight-tlf-lgr.vf)
Provides:       tex(IBMPlexSans-ExtraLight-tlf-ly1--base.tfm)
Provides:       tex(IBMPlexSans-ExtraLight-tlf-ly1.tfm)
Provides:       tex(IBMPlexSans-ExtraLight-tlf-ly1.vf)
Provides:       tex(IBMPlexSans-ExtraLight-tlf-ot1.tfm)
Provides:       tex(IBMPlexSans-ExtraLight-tlf-t1--base.tfm)
Provides:       tex(IBMPlexSans-ExtraLight-tlf-t1.tfm)
Provides:       tex(IBMPlexSans-ExtraLight-tlf-t1.vf)
Provides:       tex(IBMPlexSans-ExtraLight-tlf-ts1--base.tfm)
Provides:       tex(IBMPlexSans-ExtraLight-tlf-ts1.tfm)
Provides:       tex(IBMPlexSans-ExtraLight-tlf-ts1.vf)
Provides:       tex(IBMPlexSans-ExtraLightItalic-sup-lgr--base.tfm)
Provides:       tex(IBMPlexSans-ExtraLightItalic-sup-lgr.tfm)
Provides:       tex(IBMPlexSans-ExtraLightItalic-sup-lgr.vf)
Provides:       tex(IBMPlexSans-ExtraLightItalic-sup-ly1--base.tfm)
Provides:       tex(IBMPlexSans-ExtraLightItalic-sup-ly1.tfm)
Provides:       tex(IBMPlexSans-ExtraLightItalic-sup-ly1.vf)
Provides:       tex(IBMPlexSans-ExtraLightItalic-sup-ot1.tfm)
Provides:       tex(IBMPlexSans-ExtraLightItalic-sup-t1--base.tfm)
Provides:       tex(IBMPlexSans-ExtraLightItalic-sup-t1.tfm)
Provides:       tex(IBMPlexSans-ExtraLightItalic-sup-t1.vf)
Provides:       tex(IBMPlexSans-ExtraLightItalic-tlf-lgr--base.tfm)
Provides:       tex(IBMPlexSans-ExtraLightItalic-tlf-lgr.tfm)
Provides:       tex(IBMPlexSans-ExtraLightItalic-tlf-lgr.vf)
Provides:       tex(IBMPlexSans-ExtraLightItalic-tlf-ly1--base.tfm)
Provides:       tex(IBMPlexSans-ExtraLightItalic-tlf-ly1.tfm)
Provides:       tex(IBMPlexSans-ExtraLightItalic-tlf-ly1.vf)
Provides:       tex(IBMPlexSans-ExtraLightItalic-tlf-ot1.tfm)
Provides:       tex(IBMPlexSans-ExtraLightItalic-tlf-t1--base.tfm)
Provides:       tex(IBMPlexSans-ExtraLightItalic-tlf-t1.tfm)
Provides:       tex(IBMPlexSans-ExtraLightItalic-tlf-t1.vf)
Provides:       tex(IBMPlexSans-ExtraLightItalic-tlf-ts1--base.tfm)
Provides:       tex(IBMPlexSans-ExtraLightItalic-tlf-ts1.tfm)
Provides:       tex(IBMPlexSans-ExtraLightItalic-tlf-ts1.vf)
Provides:       tex(IBMPlexSans-Italic-sup-lgr--base.tfm)
Provides:       tex(IBMPlexSans-Italic-sup-lgr.tfm)
Provides:       tex(IBMPlexSans-Italic-sup-lgr.vf)
Provides:       tex(IBMPlexSans-Italic-sup-ly1--base.tfm)
Provides:       tex(IBMPlexSans-Italic-sup-ly1.tfm)
Provides:       tex(IBMPlexSans-Italic-sup-ly1.vf)
Provides:       tex(IBMPlexSans-Italic-sup-ot1.tfm)
Provides:       tex(IBMPlexSans-Italic-sup-t1--base.tfm)
Provides:       tex(IBMPlexSans-Italic-sup-t1.tfm)
Provides:       tex(IBMPlexSans-Italic-sup-t1.vf)
Provides:       tex(IBMPlexSans-Italic-tlf-lgr--base.tfm)
Provides:       tex(IBMPlexSans-Italic-tlf-lgr.tfm)
Provides:       tex(IBMPlexSans-Italic-tlf-lgr.vf)
Provides:       tex(IBMPlexSans-Italic-tlf-ly1--base.tfm)
Provides:       tex(IBMPlexSans-Italic-tlf-ly1.tfm)
Provides:       tex(IBMPlexSans-Italic-tlf-ly1.vf)
Provides:       tex(IBMPlexSans-Italic-tlf-ot1.tfm)
Provides:       tex(IBMPlexSans-Italic-tlf-t1--base.tfm)
Provides:       tex(IBMPlexSans-Italic-tlf-t1.tfm)
Provides:       tex(IBMPlexSans-Italic-tlf-t1.vf)
Provides:       tex(IBMPlexSans-Italic-tlf-ts1--base.tfm)
Provides:       tex(IBMPlexSans-Italic-tlf-ts1.tfm)
Provides:       tex(IBMPlexSans-Italic-tlf-ts1.vf)
Provides:       tex(IBMPlexSans-Light-sup-lgr--base.tfm)
Provides:       tex(IBMPlexSans-Light-sup-lgr.tfm)
Provides:       tex(IBMPlexSans-Light-sup-lgr.vf)
Provides:       tex(IBMPlexSans-Light-sup-ly1--base.tfm)
Provides:       tex(IBMPlexSans-Light-sup-ly1.tfm)
Provides:       tex(IBMPlexSans-Light-sup-ly1.vf)
Provides:       tex(IBMPlexSans-Light-sup-ot1.tfm)
Provides:       tex(IBMPlexSans-Light-sup-t1--base.tfm)
Provides:       tex(IBMPlexSans-Light-sup-t1.tfm)
Provides:       tex(IBMPlexSans-Light-sup-t1.vf)
Provides:       tex(IBMPlexSans-Light-tlf-lgr--base.tfm)
Provides:       tex(IBMPlexSans-Light-tlf-lgr.tfm)
Provides:       tex(IBMPlexSans-Light-tlf-lgr.vf)
Provides:       tex(IBMPlexSans-Light-tlf-ly1--base.tfm)
Provides:       tex(IBMPlexSans-Light-tlf-ly1.tfm)
Provides:       tex(IBMPlexSans-Light-tlf-ly1.vf)
Provides:       tex(IBMPlexSans-Light-tlf-ot1.tfm)
Provides:       tex(IBMPlexSans-Light-tlf-t1--base.tfm)
Provides:       tex(IBMPlexSans-Light-tlf-t1.tfm)
Provides:       tex(IBMPlexSans-Light-tlf-t1.vf)
Provides:       tex(IBMPlexSans-Light-tlf-ts1--base.tfm)
Provides:       tex(IBMPlexSans-Light-tlf-ts1.tfm)
Provides:       tex(IBMPlexSans-Light-tlf-ts1.vf)
Provides:       tex(IBMPlexSans-LightItalic-sup-lgr--base.tfm)
Provides:       tex(IBMPlexSans-LightItalic-sup-lgr.tfm)
Provides:       tex(IBMPlexSans-LightItalic-sup-lgr.vf)
Provides:       tex(IBMPlexSans-LightItalic-sup-ly1--base.tfm)
Provides:       tex(IBMPlexSans-LightItalic-sup-ly1.tfm)
Provides:       tex(IBMPlexSans-LightItalic-sup-ly1.vf)
Provides:       tex(IBMPlexSans-LightItalic-sup-ot1.tfm)
Provides:       tex(IBMPlexSans-LightItalic-sup-t1--base.tfm)
Provides:       tex(IBMPlexSans-LightItalic-sup-t1.tfm)
Provides:       tex(IBMPlexSans-LightItalic-sup-t1.vf)
Provides:       tex(IBMPlexSans-LightItalic-tlf-lgr--base.tfm)
Provides:       tex(IBMPlexSans-LightItalic-tlf-lgr.tfm)
Provides:       tex(IBMPlexSans-LightItalic-tlf-lgr.vf)
Provides:       tex(IBMPlexSans-LightItalic-tlf-ly1--base.tfm)
Provides:       tex(IBMPlexSans-LightItalic-tlf-ly1.tfm)
Provides:       tex(IBMPlexSans-LightItalic-tlf-ly1.vf)
Provides:       tex(IBMPlexSans-LightItalic-tlf-ot1.tfm)
Provides:       tex(IBMPlexSans-LightItalic-tlf-t1--base.tfm)
Provides:       tex(IBMPlexSans-LightItalic-tlf-t1.tfm)
Provides:       tex(IBMPlexSans-LightItalic-tlf-t1.vf)
Provides:       tex(IBMPlexSans-LightItalic-tlf-ts1--base.tfm)
Provides:       tex(IBMPlexSans-LightItalic-tlf-ts1.tfm)
Provides:       tex(IBMPlexSans-LightItalic-tlf-ts1.vf)
Provides:       tex(IBMPlexSans-Medium-sup-lgr--base.tfm)
Provides:       tex(IBMPlexSans-Medium-sup-lgr.tfm)
Provides:       tex(IBMPlexSans-Medium-sup-lgr.vf)
Provides:       tex(IBMPlexSans-Medium-sup-ly1--base.tfm)
Provides:       tex(IBMPlexSans-Medium-sup-ly1.tfm)
Provides:       tex(IBMPlexSans-Medium-sup-ly1.vf)
Provides:       tex(IBMPlexSans-Medium-sup-ot1.tfm)
Provides:       tex(IBMPlexSans-Medium-sup-t1--base.tfm)
Provides:       tex(IBMPlexSans-Medium-sup-t1.tfm)
Provides:       tex(IBMPlexSans-Medium-sup-t1.vf)
Provides:       tex(IBMPlexSans-Medium-tlf-lgr--base.tfm)
Provides:       tex(IBMPlexSans-Medium-tlf-lgr.tfm)
Provides:       tex(IBMPlexSans-Medium-tlf-lgr.vf)
Provides:       tex(IBMPlexSans-Medium-tlf-ly1--base.tfm)
Provides:       tex(IBMPlexSans-Medium-tlf-ly1.tfm)
Provides:       tex(IBMPlexSans-Medium-tlf-ly1.vf)
Provides:       tex(IBMPlexSans-Medium-tlf-ot1.tfm)
Provides:       tex(IBMPlexSans-Medium-tlf-t1--base.tfm)
Provides:       tex(IBMPlexSans-Medium-tlf-t1.tfm)
Provides:       tex(IBMPlexSans-Medium-tlf-t1.vf)
Provides:       tex(IBMPlexSans-Medium-tlf-ts1--base.tfm)
Provides:       tex(IBMPlexSans-Medium-tlf-ts1.tfm)
Provides:       tex(IBMPlexSans-Medium-tlf-ts1.vf)
Provides:       tex(IBMPlexSans-MediumItalic-sup-lgr--base.tfm)
Provides:       tex(IBMPlexSans-MediumItalic-sup-lgr.tfm)
Provides:       tex(IBMPlexSans-MediumItalic-sup-lgr.vf)
Provides:       tex(IBMPlexSans-MediumItalic-sup-ly1--base.tfm)
Provides:       tex(IBMPlexSans-MediumItalic-sup-ly1.tfm)
Provides:       tex(IBMPlexSans-MediumItalic-sup-ly1.vf)
Provides:       tex(IBMPlexSans-MediumItalic-sup-ot1.tfm)
Provides:       tex(IBMPlexSans-MediumItalic-sup-t1--base.tfm)
Provides:       tex(IBMPlexSans-MediumItalic-sup-t1.tfm)
Provides:       tex(IBMPlexSans-MediumItalic-sup-t1.vf)
Provides:       tex(IBMPlexSans-MediumItalic-tlf-lgr--base.tfm)
Provides:       tex(IBMPlexSans-MediumItalic-tlf-lgr.tfm)
Provides:       tex(IBMPlexSans-MediumItalic-tlf-lgr.vf)
Provides:       tex(IBMPlexSans-MediumItalic-tlf-ly1--base.tfm)
Provides:       tex(IBMPlexSans-MediumItalic-tlf-ly1.tfm)
Provides:       tex(IBMPlexSans-MediumItalic-tlf-ly1.vf)
Provides:       tex(IBMPlexSans-MediumItalic-tlf-ot1.tfm)
Provides:       tex(IBMPlexSans-MediumItalic-tlf-t1--base.tfm)
Provides:       tex(IBMPlexSans-MediumItalic-tlf-t1.tfm)
Provides:       tex(IBMPlexSans-MediumItalic-tlf-t1.vf)
Provides:       tex(IBMPlexSans-MediumItalic-tlf-ts1--base.tfm)
Provides:       tex(IBMPlexSans-MediumItalic-tlf-ts1.tfm)
Provides:       tex(IBMPlexSans-MediumItalic-tlf-ts1.vf)
Provides:       tex(IBMPlexSans-SemiBold-sup-lgr--base.tfm)
Provides:       tex(IBMPlexSans-SemiBold-sup-lgr.tfm)
Provides:       tex(IBMPlexSans-SemiBold-sup-lgr.vf)
Provides:       tex(IBMPlexSans-SemiBold-sup-ly1--base.tfm)
Provides:       tex(IBMPlexSans-SemiBold-sup-ly1.tfm)
Provides:       tex(IBMPlexSans-SemiBold-sup-ly1.vf)
Provides:       tex(IBMPlexSans-SemiBold-sup-ot1.tfm)
Provides:       tex(IBMPlexSans-SemiBold-sup-t1--base.tfm)
Provides:       tex(IBMPlexSans-SemiBold-sup-t1.tfm)
Provides:       tex(IBMPlexSans-SemiBold-sup-t1.vf)
Provides:       tex(IBMPlexSans-SemiBold-tlf-lgr--base.tfm)
Provides:       tex(IBMPlexSans-SemiBold-tlf-lgr.tfm)
Provides:       tex(IBMPlexSans-SemiBold-tlf-lgr.vf)
Provides:       tex(IBMPlexSans-SemiBold-tlf-ly1--base.tfm)
Provides:       tex(IBMPlexSans-SemiBold-tlf-ly1.tfm)
Provides:       tex(IBMPlexSans-SemiBold-tlf-ly1.vf)
Provides:       tex(IBMPlexSans-SemiBold-tlf-ot1.tfm)
Provides:       tex(IBMPlexSans-SemiBold-tlf-t1--base.tfm)
Provides:       tex(IBMPlexSans-SemiBold-tlf-t1.tfm)
Provides:       tex(IBMPlexSans-SemiBold-tlf-t1.vf)
Provides:       tex(IBMPlexSans-SemiBold-tlf-ts1--base.tfm)
Provides:       tex(IBMPlexSans-SemiBold-tlf-ts1.tfm)
Provides:       tex(IBMPlexSans-SemiBold-tlf-ts1.vf)
Provides:       tex(IBMPlexSans-SemiBoldItalic-sup-lgr--base.tfm)
Provides:       tex(IBMPlexSans-SemiBoldItalic-sup-lgr.tfm)
Provides:       tex(IBMPlexSans-SemiBoldItalic-sup-lgr.vf)
Provides:       tex(IBMPlexSans-SemiBoldItalic-sup-ly1--base.tfm)
Provides:       tex(IBMPlexSans-SemiBoldItalic-sup-ly1.tfm)
Provides:       tex(IBMPlexSans-SemiBoldItalic-sup-ly1.vf)
Provides:       tex(IBMPlexSans-SemiBoldItalic-sup-ot1.tfm)
Provides:       tex(IBMPlexSans-SemiBoldItalic-sup-t1--base.tfm)
Provides:       tex(IBMPlexSans-SemiBoldItalic-sup-t1.tfm)
Provides:       tex(IBMPlexSans-SemiBoldItalic-sup-t1.vf)
Provides:       tex(IBMPlexSans-SemiBoldItalic-tlf-lgr--base.tfm)
Provides:       tex(IBMPlexSans-SemiBoldItalic-tlf-lgr.tfm)
Provides:       tex(IBMPlexSans-SemiBoldItalic-tlf-lgr.vf)
Provides:       tex(IBMPlexSans-SemiBoldItalic-tlf-ly1--base.tfm)
Provides:       tex(IBMPlexSans-SemiBoldItalic-tlf-ly1.tfm)
Provides:       tex(IBMPlexSans-SemiBoldItalic-tlf-ly1.vf)
Provides:       tex(IBMPlexSans-SemiBoldItalic-tlf-ot1.tfm)
Provides:       tex(IBMPlexSans-SemiBoldItalic-tlf-t1--base.tfm)
Provides:       tex(IBMPlexSans-SemiBoldItalic-tlf-t1.tfm)
Provides:       tex(IBMPlexSans-SemiBoldItalic-tlf-t1.vf)
Provides:       tex(IBMPlexSans-SemiBoldItalic-tlf-ts1--base.tfm)
Provides:       tex(IBMPlexSans-SemiBoldItalic-tlf-ts1.tfm)
Provides:       tex(IBMPlexSans-SemiBoldItalic-tlf-ts1.vf)
Provides:       tex(IBMPlexSans-Text-sup-lgr--base.tfm)
Provides:       tex(IBMPlexSans-Text-sup-lgr.tfm)
Provides:       tex(IBMPlexSans-Text-sup-lgr.vf)
Provides:       tex(IBMPlexSans-Text-sup-ly1--base.tfm)
Provides:       tex(IBMPlexSans-Text-sup-ly1.tfm)
Provides:       tex(IBMPlexSans-Text-sup-ly1.vf)
Provides:       tex(IBMPlexSans-Text-sup-ot1.tfm)
Provides:       tex(IBMPlexSans-Text-sup-t1--base.tfm)
Provides:       tex(IBMPlexSans-Text-sup-t1.tfm)
Provides:       tex(IBMPlexSans-Text-sup-t1.vf)
Provides:       tex(IBMPlexSans-Text-tlf-lgr--base.tfm)
Provides:       tex(IBMPlexSans-Text-tlf-lgr.tfm)
Provides:       tex(IBMPlexSans-Text-tlf-lgr.vf)
Provides:       tex(IBMPlexSans-Text-tlf-ly1--base.tfm)
Provides:       tex(IBMPlexSans-Text-tlf-ly1.tfm)
Provides:       tex(IBMPlexSans-Text-tlf-ly1.vf)
Provides:       tex(IBMPlexSans-Text-tlf-ot1.tfm)
Provides:       tex(IBMPlexSans-Text-tlf-t1--base.tfm)
Provides:       tex(IBMPlexSans-Text-tlf-t1.tfm)
Provides:       tex(IBMPlexSans-Text-tlf-t1.vf)
Provides:       tex(IBMPlexSans-Text-tlf-ts1--base.tfm)
Provides:       tex(IBMPlexSans-Text-tlf-ts1.tfm)
Provides:       tex(IBMPlexSans-Text-tlf-ts1.vf)
Provides:       tex(IBMPlexSans-TextItalic-sup-lgr--base.tfm)
Provides:       tex(IBMPlexSans-TextItalic-sup-lgr.tfm)
Provides:       tex(IBMPlexSans-TextItalic-sup-lgr.vf)
Provides:       tex(IBMPlexSans-TextItalic-sup-ly1--base.tfm)
Provides:       tex(IBMPlexSans-TextItalic-sup-ly1.tfm)
Provides:       tex(IBMPlexSans-TextItalic-sup-ly1.vf)
Provides:       tex(IBMPlexSans-TextItalic-sup-ot1.tfm)
Provides:       tex(IBMPlexSans-TextItalic-sup-t1--base.tfm)
Provides:       tex(IBMPlexSans-TextItalic-sup-t1.tfm)
Provides:       tex(IBMPlexSans-TextItalic-sup-t1.vf)
Provides:       tex(IBMPlexSans-TextItalic-tlf-lgr--base.tfm)
Provides:       tex(IBMPlexSans-TextItalic-tlf-lgr.tfm)
Provides:       tex(IBMPlexSans-TextItalic-tlf-lgr.vf)
Provides:       tex(IBMPlexSans-TextItalic-tlf-ly1--base.tfm)
Provides:       tex(IBMPlexSans-TextItalic-tlf-ly1.tfm)
Provides:       tex(IBMPlexSans-TextItalic-tlf-ly1.vf)
Provides:       tex(IBMPlexSans-TextItalic-tlf-ot1.tfm)
Provides:       tex(IBMPlexSans-TextItalic-tlf-t1--base.tfm)
Provides:       tex(IBMPlexSans-TextItalic-tlf-t1.tfm)
Provides:       tex(IBMPlexSans-TextItalic-tlf-t1.vf)
Provides:       tex(IBMPlexSans-TextItalic-tlf-ts1--base.tfm)
Provides:       tex(IBMPlexSans-TextItalic-tlf-ts1.tfm)
Provides:       tex(IBMPlexSans-TextItalic-tlf-ts1.vf)
Provides:       tex(IBMPlexSans-Thin-sup-lgr--base.tfm)
Provides:       tex(IBMPlexSans-Thin-sup-lgr.tfm)
Provides:       tex(IBMPlexSans-Thin-sup-lgr.vf)
Provides:       tex(IBMPlexSans-Thin-sup-ly1--base.tfm)
Provides:       tex(IBMPlexSans-Thin-sup-ly1.tfm)
Provides:       tex(IBMPlexSans-Thin-sup-ly1.vf)
Provides:       tex(IBMPlexSans-Thin-sup-ot1.tfm)
Provides:       tex(IBMPlexSans-Thin-sup-t1--base.tfm)
Provides:       tex(IBMPlexSans-Thin-sup-t1.tfm)
Provides:       tex(IBMPlexSans-Thin-sup-t1.vf)
Provides:       tex(IBMPlexSans-Thin-tlf-lgr--base.tfm)
Provides:       tex(IBMPlexSans-Thin-tlf-lgr.tfm)
Provides:       tex(IBMPlexSans-Thin-tlf-lgr.vf)
Provides:       tex(IBMPlexSans-Thin-tlf-ly1--base.tfm)
Provides:       tex(IBMPlexSans-Thin-tlf-ly1.tfm)
Provides:       tex(IBMPlexSans-Thin-tlf-ly1.vf)
Provides:       tex(IBMPlexSans-Thin-tlf-ot1.tfm)
Provides:       tex(IBMPlexSans-Thin-tlf-t1--base.tfm)
Provides:       tex(IBMPlexSans-Thin-tlf-t1.tfm)
Provides:       tex(IBMPlexSans-Thin-tlf-t1.vf)
Provides:       tex(IBMPlexSans-Thin-tlf-ts1--base.tfm)
Provides:       tex(IBMPlexSans-Thin-tlf-ts1.tfm)
Provides:       tex(IBMPlexSans-Thin-tlf-ts1.vf)
Provides:       tex(IBMPlexSans-ThinItalic-sup-lgr--base.tfm)
Provides:       tex(IBMPlexSans-ThinItalic-sup-lgr.tfm)
Provides:       tex(IBMPlexSans-ThinItalic-sup-lgr.vf)
Provides:       tex(IBMPlexSans-ThinItalic-sup-ly1--base.tfm)
Provides:       tex(IBMPlexSans-ThinItalic-sup-ly1.tfm)
Provides:       tex(IBMPlexSans-ThinItalic-sup-ly1.vf)
Provides:       tex(IBMPlexSans-ThinItalic-sup-ot1.tfm)
Provides:       tex(IBMPlexSans-ThinItalic-sup-t1--base.tfm)
Provides:       tex(IBMPlexSans-ThinItalic-sup-t1.tfm)
Provides:       tex(IBMPlexSans-ThinItalic-sup-t1.vf)
Provides:       tex(IBMPlexSans-ThinItalic-tlf-lgr--base.tfm)
Provides:       tex(IBMPlexSans-ThinItalic-tlf-lgr.tfm)
Provides:       tex(IBMPlexSans-ThinItalic-tlf-lgr.vf)
Provides:       tex(IBMPlexSans-ThinItalic-tlf-ly1--base.tfm)
Provides:       tex(IBMPlexSans-ThinItalic-tlf-ly1.tfm)
Provides:       tex(IBMPlexSans-ThinItalic-tlf-ly1.vf)
Provides:       tex(IBMPlexSans-ThinItalic-tlf-ot1.tfm)
Provides:       tex(IBMPlexSans-ThinItalic-tlf-t1--base.tfm)
Provides:       tex(IBMPlexSans-ThinItalic-tlf-t1.tfm)
Provides:       tex(IBMPlexSans-ThinItalic-tlf-t1.vf)
Provides:       tex(IBMPlexSans-ThinItalic-tlf-ts1--base.tfm)
Provides:       tex(IBMPlexSans-ThinItalic-tlf-ts1.tfm)
Provides:       tex(IBMPlexSans-ThinItalic-tlf-ts1.vf)
Provides:       tex(IBMPlexSans-sup-lgr--base.tfm)
Provides:       tex(IBMPlexSans-sup-lgr.tfm)
Provides:       tex(IBMPlexSans-sup-lgr.vf)
Provides:       tex(IBMPlexSans-sup-ly1--base.tfm)
Provides:       tex(IBMPlexSans-sup-ly1.tfm)
Provides:       tex(IBMPlexSans-sup-ly1.vf)
Provides:       tex(IBMPlexSans-sup-ot1.tfm)
Provides:       tex(IBMPlexSans-sup-t1--base.tfm)
Provides:       tex(IBMPlexSans-sup-t1.tfm)
Provides:       tex(IBMPlexSans-sup-t1.vf)
Provides:       tex(IBMPlexSans-tlf-lgr--base.tfm)
Provides:       tex(IBMPlexSans-tlf-lgr.tfm)
Provides:       tex(IBMPlexSans-tlf-lgr.vf)
Provides:       tex(IBMPlexSans-tlf-ly1--base.tfm)
Provides:       tex(IBMPlexSans-tlf-ly1.tfm)
Provides:       tex(IBMPlexSans-tlf-ly1.vf)
Provides:       tex(IBMPlexSans-tlf-ot1.tfm)
Provides:       tex(IBMPlexSans-tlf-t1--base.tfm)
Provides:       tex(IBMPlexSans-tlf-t1.tfm)
Provides:       tex(IBMPlexSans-tlf-t1.vf)
Provides:       tex(IBMPlexSans-tlf-ts1--base.tfm)
Provides:       tex(IBMPlexSans-tlf-ts1.tfm)
Provides:       tex(IBMPlexSans-tlf-ts1.vf)
Provides:       tex(IBMPlexSansCond-Bold-sup-lgr--base.tfm)
Provides:       tex(IBMPlexSansCond-Bold-sup-lgr.tfm)
Provides:       tex(IBMPlexSansCond-Bold-sup-lgr.vf)
Provides:       tex(IBMPlexSansCond-Bold-sup-ly1--base.tfm)
Provides:       tex(IBMPlexSansCond-Bold-sup-ly1.tfm)
Provides:       tex(IBMPlexSansCond-Bold-sup-ly1.vf)
Provides:       tex(IBMPlexSansCond-Bold-sup-ot1.tfm)
Provides:       tex(IBMPlexSansCond-Bold-sup-t1--base.tfm)
Provides:       tex(IBMPlexSansCond-Bold-sup-t1.tfm)
Provides:       tex(IBMPlexSansCond-Bold-sup-t1.vf)
Provides:       tex(IBMPlexSansCond-Bold-tlf-lgr--base.tfm)
Provides:       tex(IBMPlexSansCond-Bold-tlf-lgr.tfm)
Provides:       tex(IBMPlexSansCond-Bold-tlf-lgr.vf)
Provides:       tex(IBMPlexSansCond-Bold-tlf-ly1--base.tfm)
Provides:       tex(IBMPlexSansCond-Bold-tlf-ly1.tfm)
Provides:       tex(IBMPlexSansCond-Bold-tlf-ly1.vf)
Provides:       tex(IBMPlexSansCond-Bold-tlf-ot1.tfm)
Provides:       tex(IBMPlexSansCond-Bold-tlf-t1--base.tfm)
Provides:       tex(IBMPlexSansCond-Bold-tlf-t1.tfm)
Provides:       tex(IBMPlexSansCond-Bold-tlf-t1.vf)
Provides:       tex(IBMPlexSansCond-Bold-tlf-ts1--base.tfm)
Provides:       tex(IBMPlexSansCond-Bold-tlf-ts1.tfm)
Provides:       tex(IBMPlexSansCond-Bold-tlf-ts1.vf)
Provides:       tex(IBMPlexSansCond-BoldItalic-sup-lgr--base.tfm)
Provides:       tex(IBMPlexSansCond-BoldItalic-sup-lgr.tfm)
Provides:       tex(IBMPlexSansCond-BoldItalic-sup-lgr.vf)
Provides:       tex(IBMPlexSansCond-BoldItalic-sup-ly1--base.tfm)
Provides:       tex(IBMPlexSansCond-BoldItalic-sup-ly1.tfm)
Provides:       tex(IBMPlexSansCond-BoldItalic-sup-ly1.vf)
Provides:       tex(IBMPlexSansCond-BoldItalic-sup-ot1.tfm)
Provides:       tex(IBMPlexSansCond-BoldItalic-sup-t1--base.tfm)
Provides:       tex(IBMPlexSansCond-BoldItalic-sup-t1.tfm)
Provides:       tex(IBMPlexSansCond-BoldItalic-sup-t1.vf)
Provides:       tex(IBMPlexSansCond-BoldItalic-tlf-lgr--base.tfm)
Provides:       tex(IBMPlexSansCond-BoldItalic-tlf-lgr.tfm)
Provides:       tex(IBMPlexSansCond-BoldItalic-tlf-lgr.vf)
Provides:       tex(IBMPlexSansCond-BoldItalic-tlf-ly1--base.tfm)
Provides:       tex(IBMPlexSansCond-BoldItalic-tlf-ly1.tfm)
Provides:       tex(IBMPlexSansCond-BoldItalic-tlf-ly1.vf)
Provides:       tex(IBMPlexSansCond-BoldItalic-tlf-ot1.tfm)
Provides:       tex(IBMPlexSansCond-BoldItalic-tlf-t1--base.tfm)
Provides:       tex(IBMPlexSansCond-BoldItalic-tlf-t1.tfm)
Provides:       tex(IBMPlexSansCond-BoldItalic-tlf-t1.vf)
Provides:       tex(IBMPlexSansCond-BoldItalic-tlf-ts1--base.tfm)
Provides:       tex(IBMPlexSansCond-BoldItalic-tlf-ts1.tfm)
Provides:       tex(IBMPlexSansCond-BoldItalic-tlf-ts1.vf)
Provides:       tex(IBMPlexSansCond-ExtraLight-sup-lgr--base.tfm)
Provides:       tex(IBMPlexSansCond-ExtraLight-sup-lgr.tfm)
Provides:       tex(IBMPlexSansCond-ExtraLight-sup-lgr.vf)
Provides:       tex(IBMPlexSansCond-ExtraLight-sup-ly1--base.tfm)
Provides:       tex(IBMPlexSansCond-ExtraLight-sup-ly1.tfm)
Provides:       tex(IBMPlexSansCond-ExtraLight-sup-ly1.vf)
Provides:       tex(IBMPlexSansCond-ExtraLight-sup-ot1.tfm)
Provides:       tex(IBMPlexSansCond-ExtraLight-sup-t1--base.tfm)
Provides:       tex(IBMPlexSansCond-ExtraLight-sup-t1.tfm)
Provides:       tex(IBMPlexSansCond-ExtraLight-sup-t1.vf)
Provides:       tex(IBMPlexSansCond-ExtraLight-tlf-lgr--base.tfm)
Provides:       tex(IBMPlexSansCond-ExtraLight-tlf-lgr.tfm)
Provides:       tex(IBMPlexSansCond-ExtraLight-tlf-lgr.vf)
Provides:       tex(IBMPlexSansCond-ExtraLight-tlf-ly1--base.tfm)
Provides:       tex(IBMPlexSansCond-ExtraLight-tlf-ly1.tfm)
Provides:       tex(IBMPlexSansCond-ExtraLight-tlf-ly1.vf)
Provides:       tex(IBMPlexSansCond-ExtraLight-tlf-ot1.tfm)
Provides:       tex(IBMPlexSansCond-ExtraLight-tlf-t1--base.tfm)
Provides:       tex(IBMPlexSansCond-ExtraLight-tlf-t1.tfm)
Provides:       tex(IBMPlexSansCond-ExtraLight-tlf-t1.vf)
Provides:       tex(IBMPlexSansCond-ExtraLight-tlf-ts1--base.tfm)
Provides:       tex(IBMPlexSansCond-ExtraLight-tlf-ts1.tfm)
Provides:       tex(IBMPlexSansCond-ExtraLight-tlf-ts1.vf)
Provides:       tex(IBMPlexSansCond-ExtraLightItalic-sup-lgr--base.tfm)
Provides:       tex(IBMPlexSansCond-ExtraLightItalic-sup-lgr.tfm)
Provides:       tex(IBMPlexSansCond-ExtraLightItalic-sup-lgr.vf)
Provides:       tex(IBMPlexSansCond-ExtraLightItalic-sup-ly1--base.tfm)
Provides:       tex(IBMPlexSansCond-ExtraLightItalic-sup-ly1.tfm)
Provides:       tex(IBMPlexSansCond-ExtraLightItalic-sup-ly1.vf)
Provides:       tex(IBMPlexSansCond-ExtraLightItalic-sup-ot1.tfm)
Provides:       tex(IBMPlexSansCond-ExtraLightItalic-sup-t1--base.tfm)
Provides:       tex(IBMPlexSansCond-ExtraLightItalic-sup-t1.tfm)
Provides:       tex(IBMPlexSansCond-ExtraLightItalic-sup-t1.vf)
Provides:       tex(IBMPlexSansCond-ExtraLightItalic-tlf-lgr--base.tfm)
Provides:       tex(IBMPlexSansCond-ExtraLightItalic-tlf-lgr.tfm)
Provides:       tex(IBMPlexSansCond-ExtraLightItalic-tlf-lgr.vf)
Provides:       tex(IBMPlexSansCond-ExtraLightItalic-tlf-ly1--base.tfm)
Provides:       tex(IBMPlexSansCond-ExtraLightItalic-tlf-ly1.tfm)
Provides:       tex(IBMPlexSansCond-ExtraLightItalic-tlf-ly1.vf)
Provides:       tex(IBMPlexSansCond-ExtraLightItalic-tlf-ot1.tfm)
Provides:       tex(IBMPlexSansCond-ExtraLightItalic-tlf-t1--base.tfm)
Provides:       tex(IBMPlexSansCond-ExtraLightItalic-tlf-t1.tfm)
Provides:       tex(IBMPlexSansCond-ExtraLightItalic-tlf-t1.vf)
Provides:       tex(IBMPlexSansCond-ExtraLightItalic-tlf-ts1--base.tfm)
Provides:       tex(IBMPlexSansCond-ExtraLightItalic-tlf-ts1.tfm)
Provides:       tex(IBMPlexSansCond-ExtraLightItalic-tlf-ts1.vf)
Provides:       tex(IBMPlexSansCond-Italic-sup-lgr--base.tfm)
Provides:       tex(IBMPlexSansCond-Italic-sup-lgr.tfm)
Provides:       tex(IBMPlexSansCond-Italic-sup-lgr.vf)
Provides:       tex(IBMPlexSansCond-Italic-sup-ly1--base.tfm)
Provides:       tex(IBMPlexSansCond-Italic-sup-ly1.tfm)
Provides:       tex(IBMPlexSansCond-Italic-sup-ly1.vf)
Provides:       tex(IBMPlexSansCond-Italic-sup-ot1.tfm)
Provides:       tex(IBMPlexSansCond-Italic-sup-t1--base.tfm)
Provides:       tex(IBMPlexSansCond-Italic-sup-t1.tfm)
Provides:       tex(IBMPlexSansCond-Italic-sup-t1.vf)
Provides:       tex(IBMPlexSansCond-Italic-tlf-lgr--base.tfm)
Provides:       tex(IBMPlexSansCond-Italic-tlf-lgr.tfm)
Provides:       tex(IBMPlexSansCond-Italic-tlf-lgr.vf)
Provides:       tex(IBMPlexSansCond-Italic-tlf-ly1--base.tfm)
Provides:       tex(IBMPlexSansCond-Italic-tlf-ly1.tfm)
Provides:       tex(IBMPlexSansCond-Italic-tlf-ly1.vf)
Provides:       tex(IBMPlexSansCond-Italic-tlf-ot1.tfm)
Provides:       tex(IBMPlexSansCond-Italic-tlf-t1--base.tfm)
Provides:       tex(IBMPlexSansCond-Italic-tlf-t1.tfm)
Provides:       tex(IBMPlexSansCond-Italic-tlf-t1.vf)
Provides:       tex(IBMPlexSansCond-Italic-tlf-ts1--base.tfm)
Provides:       tex(IBMPlexSansCond-Italic-tlf-ts1.tfm)
Provides:       tex(IBMPlexSansCond-Italic-tlf-ts1.vf)
Provides:       tex(IBMPlexSansCond-Light-sup-lgr--base.tfm)
Provides:       tex(IBMPlexSansCond-Light-sup-lgr.tfm)
Provides:       tex(IBMPlexSansCond-Light-sup-lgr.vf)
Provides:       tex(IBMPlexSansCond-Light-sup-ly1--base.tfm)
Provides:       tex(IBMPlexSansCond-Light-sup-ly1.tfm)
Provides:       tex(IBMPlexSansCond-Light-sup-ly1.vf)
Provides:       tex(IBMPlexSansCond-Light-sup-ot1.tfm)
Provides:       tex(IBMPlexSansCond-Light-sup-t1--base.tfm)
Provides:       tex(IBMPlexSansCond-Light-sup-t1.tfm)
Provides:       tex(IBMPlexSansCond-Light-sup-t1.vf)
Provides:       tex(IBMPlexSansCond-Light-tlf-lgr--base.tfm)
Provides:       tex(IBMPlexSansCond-Light-tlf-lgr.tfm)
Provides:       tex(IBMPlexSansCond-Light-tlf-lgr.vf)
Provides:       tex(IBMPlexSansCond-Light-tlf-ly1--base.tfm)
Provides:       tex(IBMPlexSansCond-Light-tlf-ly1.tfm)
Provides:       tex(IBMPlexSansCond-Light-tlf-ly1.vf)
Provides:       tex(IBMPlexSansCond-Light-tlf-ot1.tfm)
Provides:       tex(IBMPlexSansCond-Light-tlf-t1--base.tfm)
Provides:       tex(IBMPlexSansCond-Light-tlf-t1.tfm)
Provides:       tex(IBMPlexSansCond-Light-tlf-t1.vf)
Provides:       tex(IBMPlexSansCond-Light-tlf-ts1--base.tfm)
Provides:       tex(IBMPlexSansCond-Light-tlf-ts1.tfm)
Provides:       tex(IBMPlexSansCond-Light-tlf-ts1.vf)
Provides:       tex(IBMPlexSansCond-LightItalic-sup-lgr--base.tfm)
Provides:       tex(IBMPlexSansCond-LightItalic-sup-lgr.tfm)
Provides:       tex(IBMPlexSansCond-LightItalic-sup-lgr.vf)
Provides:       tex(IBMPlexSansCond-LightItalic-sup-ly1--base.tfm)
Provides:       tex(IBMPlexSansCond-LightItalic-sup-ly1.tfm)
Provides:       tex(IBMPlexSansCond-LightItalic-sup-ly1.vf)
Provides:       tex(IBMPlexSansCond-LightItalic-sup-ot1.tfm)
Provides:       tex(IBMPlexSansCond-LightItalic-sup-t1--base.tfm)
Provides:       tex(IBMPlexSansCond-LightItalic-sup-t1.tfm)
Provides:       tex(IBMPlexSansCond-LightItalic-sup-t1.vf)
Provides:       tex(IBMPlexSansCond-LightItalic-tlf-lgr--base.tfm)
Provides:       tex(IBMPlexSansCond-LightItalic-tlf-lgr.tfm)
Provides:       tex(IBMPlexSansCond-LightItalic-tlf-lgr.vf)
Provides:       tex(IBMPlexSansCond-LightItalic-tlf-ly1--base.tfm)
Provides:       tex(IBMPlexSansCond-LightItalic-tlf-ly1.tfm)
Provides:       tex(IBMPlexSansCond-LightItalic-tlf-ly1.vf)
Provides:       tex(IBMPlexSansCond-LightItalic-tlf-ot1.tfm)
Provides:       tex(IBMPlexSansCond-LightItalic-tlf-t1--base.tfm)
Provides:       tex(IBMPlexSansCond-LightItalic-tlf-t1.tfm)
Provides:       tex(IBMPlexSansCond-LightItalic-tlf-t1.vf)
Provides:       tex(IBMPlexSansCond-LightItalic-tlf-ts1--base.tfm)
Provides:       tex(IBMPlexSansCond-LightItalic-tlf-ts1.tfm)
Provides:       tex(IBMPlexSansCond-LightItalic-tlf-ts1.vf)
Provides:       tex(IBMPlexSansCond-Medium-sup-lgr--base.tfm)
Provides:       tex(IBMPlexSansCond-Medium-sup-lgr.tfm)
Provides:       tex(IBMPlexSansCond-Medium-sup-lgr.vf)
Provides:       tex(IBMPlexSansCond-Medium-sup-ly1--base.tfm)
Provides:       tex(IBMPlexSansCond-Medium-sup-ly1.tfm)
Provides:       tex(IBMPlexSansCond-Medium-sup-ly1.vf)
Provides:       tex(IBMPlexSansCond-Medium-sup-ot1.tfm)
Provides:       tex(IBMPlexSansCond-Medium-sup-t1--base.tfm)
Provides:       tex(IBMPlexSansCond-Medium-sup-t1.tfm)
Provides:       tex(IBMPlexSansCond-Medium-sup-t1.vf)
Provides:       tex(IBMPlexSansCond-Medium-tlf-lgr--base.tfm)
Provides:       tex(IBMPlexSansCond-Medium-tlf-lgr.tfm)
Provides:       tex(IBMPlexSansCond-Medium-tlf-lgr.vf)
Provides:       tex(IBMPlexSansCond-Medium-tlf-ly1--base.tfm)
Provides:       tex(IBMPlexSansCond-Medium-tlf-ly1.tfm)
Provides:       tex(IBMPlexSansCond-Medium-tlf-ly1.vf)
Provides:       tex(IBMPlexSansCond-Medium-tlf-ot1.tfm)
Provides:       tex(IBMPlexSansCond-Medium-tlf-t1--base.tfm)
Provides:       tex(IBMPlexSansCond-Medium-tlf-t1.tfm)
Provides:       tex(IBMPlexSansCond-Medium-tlf-t1.vf)
Provides:       tex(IBMPlexSansCond-Medium-tlf-ts1--base.tfm)
Provides:       tex(IBMPlexSansCond-Medium-tlf-ts1.tfm)
Provides:       tex(IBMPlexSansCond-Medium-tlf-ts1.vf)
Provides:       tex(IBMPlexSansCond-MediumItalic-sup-lgr--base.tfm)
Provides:       tex(IBMPlexSansCond-MediumItalic-sup-lgr.tfm)
Provides:       tex(IBMPlexSansCond-MediumItalic-sup-lgr.vf)
Provides:       tex(IBMPlexSansCond-MediumItalic-sup-ly1--base.tfm)
Provides:       tex(IBMPlexSansCond-MediumItalic-sup-ly1.tfm)
Provides:       tex(IBMPlexSansCond-MediumItalic-sup-ly1.vf)
Provides:       tex(IBMPlexSansCond-MediumItalic-sup-ot1.tfm)
Provides:       tex(IBMPlexSansCond-MediumItalic-sup-t1--base.tfm)
Provides:       tex(IBMPlexSansCond-MediumItalic-sup-t1.tfm)
Provides:       tex(IBMPlexSansCond-MediumItalic-sup-t1.vf)
Provides:       tex(IBMPlexSansCond-MediumItalic-tlf-lgr--base.tfm)
Provides:       tex(IBMPlexSansCond-MediumItalic-tlf-lgr.tfm)
Provides:       tex(IBMPlexSansCond-MediumItalic-tlf-lgr.vf)
Provides:       tex(IBMPlexSansCond-MediumItalic-tlf-ly1--base.tfm)
Provides:       tex(IBMPlexSansCond-MediumItalic-tlf-ly1.tfm)
Provides:       tex(IBMPlexSansCond-MediumItalic-tlf-ly1.vf)
Provides:       tex(IBMPlexSansCond-MediumItalic-tlf-ot1.tfm)
Provides:       tex(IBMPlexSansCond-MediumItalic-tlf-t1--base.tfm)
Provides:       tex(IBMPlexSansCond-MediumItalic-tlf-t1.tfm)
Provides:       tex(IBMPlexSansCond-MediumItalic-tlf-t1.vf)
Provides:       tex(IBMPlexSansCond-MediumItalic-tlf-ts1--base.tfm)
Provides:       tex(IBMPlexSansCond-MediumItalic-tlf-ts1.tfm)
Provides:       tex(IBMPlexSansCond-MediumItalic-tlf-ts1.vf)
Provides:       tex(IBMPlexSansCond-SemiBold-sup-lgr--base.tfm)
Provides:       tex(IBMPlexSansCond-SemiBold-sup-lgr.tfm)
Provides:       tex(IBMPlexSansCond-SemiBold-sup-lgr.vf)
Provides:       tex(IBMPlexSansCond-SemiBold-sup-ly1--base.tfm)
Provides:       tex(IBMPlexSansCond-SemiBold-sup-ly1.tfm)
Provides:       tex(IBMPlexSansCond-SemiBold-sup-ly1.vf)
Provides:       tex(IBMPlexSansCond-SemiBold-sup-ot1.tfm)
Provides:       tex(IBMPlexSansCond-SemiBold-sup-t1--base.tfm)
Provides:       tex(IBMPlexSansCond-SemiBold-sup-t1.tfm)
Provides:       tex(IBMPlexSansCond-SemiBold-sup-t1.vf)
Provides:       tex(IBMPlexSansCond-SemiBold-tlf-lgr--base.tfm)
Provides:       tex(IBMPlexSansCond-SemiBold-tlf-lgr.tfm)
Provides:       tex(IBMPlexSansCond-SemiBold-tlf-lgr.vf)
Provides:       tex(IBMPlexSansCond-SemiBold-tlf-ly1--base.tfm)
Provides:       tex(IBMPlexSansCond-SemiBold-tlf-ly1.tfm)
Provides:       tex(IBMPlexSansCond-SemiBold-tlf-ly1.vf)
Provides:       tex(IBMPlexSansCond-SemiBold-tlf-ot1.tfm)
Provides:       tex(IBMPlexSansCond-SemiBold-tlf-t1--base.tfm)
Provides:       tex(IBMPlexSansCond-SemiBold-tlf-t1.tfm)
Provides:       tex(IBMPlexSansCond-SemiBold-tlf-t1.vf)
Provides:       tex(IBMPlexSansCond-SemiBold-tlf-ts1--base.tfm)
Provides:       tex(IBMPlexSansCond-SemiBold-tlf-ts1.tfm)
Provides:       tex(IBMPlexSansCond-SemiBold-tlf-ts1.vf)
Provides:       tex(IBMPlexSansCond-SemiBoldItalic-sup-lgr--base.tfm)
Provides:       tex(IBMPlexSansCond-SemiBoldItalic-sup-lgr.tfm)
Provides:       tex(IBMPlexSansCond-SemiBoldItalic-sup-lgr.vf)
Provides:       tex(IBMPlexSansCond-SemiBoldItalic-sup-ly1--base.tfm)
Provides:       tex(IBMPlexSansCond-SemiBoldItalic-sup-ly1.tfm)
Provides:       tex(IBMPlexSansCond-SemiBoldItalic-sup-ly1.vf)
Provides:       tex(IBMPlexSansCond-SemiBoldItalic-sup-ot1.tfm)
Provides:       tex(IBMPlexSansCond-SemiBoldItalic-sup-t1--base.tfm)
Provides:       tex(IBMPlexSansCond-SemiBoldItalic-sup-t1.tfm)
Provides:       tex(IBMPlexSansCond-SemiBoldItalic-sup-t1.vf)
Provides:       tex(IBMPlexSansCond-SemiBoldItalic-tlf-lgr--base.tfm)
Provides:       tex(IBMPlexSansCond-SemiBoldItalic-tlf-lgr.tfm)
Provides:       tex(IBMPlexSansCond-SemiBoldItalic-tlf-lgr.vf)
Provides:       tex(IBMPlexSansCond-SemiBoldItalic-tlf-ly1--base.tfm)
Provides:       tex(IBMPlexSansCond-SemiBoldItalic-tlf-ly1.tfm)
Provides:       tex(IBMPlexSansCond-SemiBoldItalic-tlf-ly1.vf)
Provides:       tex(IBMPlexSansCond-SemiBoldItalic-tlf-ot1.tfm)
Provides:       tex(IBMPlexSansCond-SemiBoldItalic-tlf-t1--base.tfm)
Provides:       tex(IBMPlexSansCond-SemiBoldItalic-tlf-t1.tfm)
Provides:       tex(IBMPlexSansCond-SemiBoldItalic-tlf-t1.vf)
Provides:       tex(IBMPlexSansCond-SemiBoldItalic-tlf-ts1--base.tfm)
Provides:       tex(IBMPlexSansCond-SemiBoldItalic-tlf-ts1.tfm)
Provides:       tex(IBMPlexSansCond-SemiBoldItalic-tlf-ts1.vf)
Provides:       tex(IBMPlexSansCond-Text-sup-lgr--base.tfm)
Provides:       tex(IBMPlexSansCond-Text-sup-lgr.tfm)
Provides:       tex(IBMPlexSansCond-Text-sup-lgr.vf)
Provides:       tex(IBMPlexSansCond-Text-sup-ly1--base.tfm)
Provides:       tex(IBMPlexSansCond-Text-sup-ly1.tfm)
Provides:       tex(IBMPlexSansCond-Text-sup-ly1.vf)
Provides:       tex(IBMPlexSansCond-Text-sup-ot1.tfm)
Provides:       tex(IBMPlexSansCond-Text-sup-t1--base.tfm)
Provides:       tex(IBMPlexSansCond-Text-sup-t1.tfm)
Provides:       tex(IBMPlexSansCond-Text-sup-t1.vf)
Provides:       tex(IBMPlexSansCond-Text-tlf-lgr--base.tfm)
Provides:       tex(IBMPlexSansCond-Text-tlf-lgr.tfm)
Provides:       tex(IBMPlexSansCond-Text-tlf-lgr.vf)
Provides:       tex(IBMPlexSansCond-Text-tlf-ly1--base.tfm)
Provides:       tex(IBMPlexSansCond-Text-tlf-ly1.tfm)
Provides:       tex(IBMPlexSansCond-Text-tlf-ly1.vf)
Provides:       tex(IBMPlexSansCond-Text-tlf-ot1.tfm)
Provides:       tex(IBMPlexSansCond-Text-tlf-t1--base.tfm)
Provides:       tex(IBMPlexSansCond-Text-tlf-t1.tfm)
Provides:       tex(IBMPlexSansCond-Text-tlf-t1.vf)
Provides:       tex(IBMPlexSansCond-Text-tlf-ts1--base.tfm)
Provides:       tex(IBMPlexSansCond-Text-tlf-ts1.tfm)
Provides:       tex(IBMPlexSansCond-Text-tlf-ts1.vf)
Provides:       tex(IBMPlexSansCond-TextItalic-sup-lgr--base.tfm)
Provides:       tex(IBMPlexSansCond-TextItalic-sup-lgr.tfm)
Provides:       tex(IBMPlexSansCond-TextItalic-sup-lgr.vf)
Provides:       tex(IBMPlexSansCond-TextItalic-sup-ly1--base.tfm)
Provides:       tex(IBMPlexSansCond-TextItalic-sup-ly1.tfm)
Provides:       tex(IBMPlexSansCond-TextItalic-sup-ly1.vf)
Provides:       tex(IBMPlexSansCond-TextItalic-sup-ot1.tfm)
Provides:       tex(IBMPlexSansCond-TextItalic-sup-t1--base.tfm)
Provides:       tex(IBMPlexSansCond-TextItalic-sup-t1.tfm)
Provides:       tex(IBMPlexSansCond-TextItalic-sup-t1.vf)
Provides:       tex(IBMPlexSansCond-TextItalic-tlf-lgr--base.tfm)
Provides:       tex(IBMPlexSansCond-TextItalic-tlf-lgr.tfm)
Provides:       tex(IBMPlexSansCond-TextItalic-tlf-lgr.vf)
Provides:       tex(IBMPlexSansCond-TextItalic-tlf-ly1--base.tfm)
Provides:       tex(IBMPlexSansCond-TextItalic-tlf-ly1.tfm)
Provides:       tex(IBMPlexSansCond-TextItalic-tlf-ly1.vf)
Provides:       tex(IBMPlexSansCond-TextItalic-tlf-ot1.tfm)
Provides:       tex(IBMPlexSansCond-TextItalic-tlf-t1--base.tfm)
Provides:       tex(IBMPlexSansCond-TextItalic-tlf-t1.tfm)
Provides:       tex(IBMPlexSansCond-TextItalic-tlf-t1.vf)
Provides:       tex(IBMPlexSansCond-TextItalic-tlf-ts1--base.tfm)
Provides:       tex(IBMPlexSansCond-TextItalic-tlf-ts1.tfm)
Provides:       tex(IBMPlexSansCond-TextItalic-tlf-ts1.vf)
Provides:       tex(IBMPlexSansCond-Thin-sup-lgr--base.tfm)
Provides:       tex(IBMPlexSansCond-Thin-sup-lgr.tfm)
Provides:       tex(IBMPlexSansCond-Thin-sup-lgr.vf)
Provides:       tex(IBMPlexSansCond-Thin-sup-ly1--base.tfm)
Provides:       tex(IBMPlexSansCond-Thin-sup-ly1.tfm)
Provides:       tex(IBMPlexSansCond-Thin-sup-ly1.vf)
Provides:       tex(IBMPlexSansCond-Thin-sup-ot1.tfm)
Provides:       tex(IBMPlexSansCond-Thin-sup-t1--base.tfm)
Provides:       tex(IBMPlexSansCond-Thin-sup-t1.tfm)
Provides:       tex(IBMPlexSansCond-Thin-sup-t1.vf)
Provides:       tex(IBMPlexSansCond-Thin-tlf-lgr--base.tfm)
Provides:       tex(IBMPlexSansCond-Thin-tlf-lgr.tfm)
Provides:       tex(IBMPlexSansCond-Thin-tlf-lgr.vf)
Provides:       tex(IBMPlexSansCond-Thin-tlf-ly1--base.tfm)
Provides:       tex(IBMPlexSansCond-Thin-tlf-ly1.tfm)
Provides:       tex(IBMPlexSansCond-Thin-tlf-ly1.vf)
Provides:       tex(IBMPlexSansCond-Thin-tlf-ot1.tfm)
Provides:       tex(IBMPlexSansCond-Thin-tlf-t1--base.tfm)
Provides:       tex(IBMPlexSansCond-Thin-tlf-t1.tfm)
Provides:       tex(IBMPlexSansCond-Thin-tlf-t1.vf)
Provides:       tex(IBMPlexSansCond-Thin-tlf-ts1--base.tfm)
Provides:       tex(IBMPlexSansCond-Thin-tlf-ts1.tfm)
Provides:       tex(IBMPlexSansCond-Thin-tlf-ts1.vf)
Provides:       tex(IBMPlexSansCond-ThinItalic-sup-lgr--base.tfm)
Provides:       tex(IBMPlexSansCond-ThinItalic-sup-lgr.tfm)
Provides:       tex(IBMPlexSansCond-ThinItalic-sup-lgr.vf)
Provides:       tex(IBMPlexSansCond-ThinItalic-sup-ly1--base.tfm)
Provides:       tex(IBMPlexSansCond-ThinItalic-sup-ly1.tfm)
Provides:       tex(IBMPlexSansCond-ThinItalic-sup-ly1.vf)
Provides:       tex(IBMPlexSansCond-ThinItalic-sup-ot1.tfm)
Provides:       tex(IBMPlexSansCond-ThinItalic-sup-t1--base.tfm)
Provides:       tex(IBMPlexSansCond-ThinItalic-sup-t1.tfm)
Provides:       tex(IBMPlexSansCond-ThinItalic-sup-t1.vf)
Provides:       tex(IBMPlexSansCond-ThinItalic-tlf-lgr--base.tfm)
Provides:       tex(IBMPlexSansCond-ThinItalic-tlf-lgr.tfm)
Provides:       tex(IBMPlexSansCond-ThinItalic-tlf-lgr.vf)
Provides:       tex(IBMPlexSansCond-ThinItalic-tlf-ly1--base.tfm)
Provides:       tex(IBMPlexSansCond-ThinItalic-tlf-ly1.tfm)
Provides:       tex(IBMPlexSansCond-ThinItalic-tlf-ly1.vf)
Provides:       tex(IBMPlexSansCond-ThinItalic-tlf-ot1.tfm)
Provides:       tex(IBMPlexSansCond-ThinItalic-tlf-t1--base.tfm)
Provides:       tex(IBMPlexSansCond-ThinItalic-tlf-t1.tfm)
Provides:       tex(IBMPlexSansCond-ThinItalic-tlf-t1.vf)
Provides:       tex(IBMPlexSansCond-ThinItalic-tlf-ts1--base.tfm)
Provides:       tex(IBMPlexSansCond-ThinItalic-tlf-ts1.tfm)
Provides:       tex(IBMPlexSansCond-ThinItalic-tlf-ts1.vf)
Provides:       tex(IBMPlexSansCond-sup-lgr--base.tfm)
Provides:       tex(IBMPlexSansCond-sup-lgr.tfm)
Provides:       tex(IBMPlexSansCond-sup-lgr.vf)
Provides:       tex(IBMPlexSansCond-sup-ly1--base.tfm)
Provides:       tex(IBMPlexSansCond-sup-ly1.tfm)
Provides:       tex(IBMPlexSansCond-sup-ly1.vf)
Provides:       tex(IBMPlexSansCond-sup-ot1.tfm)
Provides:       tex(IBMPlexSansCond-sup-t1--base.tfm)
Provides:       tex(IBMPlexSansCond-sup-t1.tfm)
Provides:       tex(IBMPlexSansCond-sup-t1.vf)
Provides:       tex(IBMPlexSansCond-tlf-lgr--base.tfm)
Provides:       tex(IBMPlexSansCond-tlf-lgr.tfm)
Provides:       tex(IBMPlexSansCond-tlf-lgr.vf)
Provides:       tex(IBMPlexSansCond-tlf-ly1--base.tfm)
Provides:       tex(IBMPlexSansCond-tlf-ly1.tfm)
Provides:       tex(IBMPlexSansCond-tlf-ly1.vf)
Provides:       tex(IBMPlexSansCond-tlf-ot1.tfm)
Provides:       tex(IBMPlexSansCond-tlf-t1--base.tfm)
Provides:       tex(IBMPlexSansCond-tlf-t1.tfm)
Provides:       tex(IBMPlexSansCond-tlf-t1.vf)
Provides:       tex(IBMPlexSansCond-tlf-ts1--base.tfm)
Provides:       tex(IBMPlexSansCond-tlf-ts1.tfm)
Provides:       tex(IBMPlexSansCond-tlf-ts1.vf)
Provides:       tex(IBMPlexSerif-Bold-sup-ly1--base.tfm)
Provides:       tex(IBMPlexSerif-Bold-sup-ly1.tfm)
Provides:       tex(IBMPlexSerif-Bold-sup-ly1.vf)
Provides:       tex(IBMPlexSerif-Bold-sup-ot1.tfm)
Provides:       tex(IBMPlexSerif-Bold-sup-t1--base.tfm)
Provides:       tex(IBMPlexSerif-Bold-sup-t1.tfm)
Provides:       tex(IBMPlexSerif-Bold-sup-t1.vf)
Provides:       tex(IBMPlexSerif-Bold-tlf-ly1--base.tfm)
Provides:       tex(IBMPlexSerif-Bold-tlf-ly1.tfm)
Provides:       tex(IBMPlexSerif-Bold-tlf-ly1.vf)
Provides:       tex(IBMPlexSerif-Bold-tlf-ot1.tfm)
Provides:       tex(IBMPlexSerif-Bold-tlf-t1--base.tfm)
Provides:       tex(IBMPlexSerif-Bold-tlf-t1.tfm)
Provides:       tex(IBMPlexSerif-Bold-tlf-t1.vf)
Provides:       tex(IBMPlexSerif-Bold-tlf-ts1--base.tfm)
Provides:       tex(IBMPlexSerif-Bold-tlf-ts1.tfm)
Provides:       tex(IBMPlexSerif-Bold-tlf-ts1.vf)
Provides:       tex(IBMPlexSerif-BoldItalic-sup-ly1--base.tfm)
Provides:       tex(IBMPlexSerif-BoldItalic-sup-ly1.tfm)
Provides:       tex(IBMPlexSerif-BoldItalic-sup-ly1.vf)
Provides:       tex(IBMPlexSerif-BoldItalic-sup-ot1.tfm)
Provides:       tex(IBMPlexSerif-BoldItalic-sup-t1--base.tfm)
Provides:       tex(IBMPlexSerif-BoldItalic-sup-t1.tfm)
Provides:       tex(IBMPlexSerif-BoldItalic-sup-t1.vf)
Provides:       tex(IBMPlexSerif-BoldItalic-tlf-ly1--base.tfm)
Provides:       tex(IBMPlexSerif-BoldItalic-tlf-ly1.tfm)
Provides:       tex(IBMPlexSerif-BoldItalic-tlf-ly1.vf)
Provides:       tex(IBMPlexSerif-BoldItalic-tlf-ot1.tfm)
Provides:       tex(IBMPlexSerif-BoldItalic-tlf-t1--base.tfm)
Provides:       tex(IBMPlexSerif-BoldItalic-tlf-t1.tfm)
Provides:       tex(IBMPlexSerif-BoldItalic-tlf-t1.vf)
Provides:       tex(IBMPlexSerif-BoldItalic-tlf-ts1--base.tfm)
Provides:       tex(IBMPlexSerif-BoldItalic-tlf-ts1.tfm)
Provides:       tex(IBMPlexSerif-BoldItalic-tlf-ts1.vf)
Provides:       tex(IBMPlexSerif-ExtraLight-sup-ly1--base.tfm)
Provides:       tex(IBMPlexSerif-ExtraLight-sup-ly1.tfm)
Provides:       tex(IBMPlexSerif-ExtraLight-sup-ly1.vf)
Provides:       tex(IBMPlexSerif-ExtraLight-sup-ot1.tfm)
Provides:       tex(IBMPlexSerif-ExtraLight-sup-t1--base.tfm)
Provides:       tex(IBMPlexSerif-ExtraLight-sup-t1.tfm)
Provides:       tex(IBMPlexSerif-ExtraLight-sup-t1.vf)
Provides:       tex(IBMPlexSerif-ExtraLight-tlf-ly1--base.tfm)
Provides:       tex(IBMPlexSerif-ExtraLight-tlf-ly1.tfm)
Provides:       tex(IBMPlexSerif-ExtraLight-tlf-ly1.vf)
Provides:       tex(IBMPlexSerif-ExtraLight-tlf-ot1.tfm)
Provides:       tex(IBMPlexSerif-ExtraLight-tlf-t1--base.tfm)
Provides:       tex(IBMPlexSerif-ExtraLight-tlf-t1.tfm)
Provides:       tex(IBMPlexSerif-ExtraLight-tlf-t1.vf)
Provides:       tex(IBMPlexSerif-ExtraLight-tlf-ts1--base.tfm)
Provides:       tex(IBMPlexSerif-ExtraLight-tlf-ts1.tfm)
Provides:       tex(IBMPlexSerif-ExtraLight-tlf-ts1.vf)
Provides:       tex(IBMPlexSerif-ExtraLightItalic-sup-ly1--base.tfm)
Provides:       tex(IBMPlexSerif-ExtraLightItalic-sup-ly1.tfm)
Provides:       tex(IBMPlexSerif-ExtraLightItalic-sup-ly1.vf)
Provides:       tex(IBMPlexSerif-ExtraLightItalic-sup-ot1.tfm)
Provides:       tex(IBMPlexSerif-ExtraLightItalic-sup-t1--base.tfm)
Provides:       tex(IBMPlexSerif-ExtraLightItalic-sup-t1.tfm)
Provides:       tex(IBMPlexSerif-ExtraLightItalic-sup-t1.vf)
Provides:       tex(IBMPlexSerif-ExtraLightItalic-tlf-ly1--base.tfm)
Provides:       tex(IBMPlexSerif-ExtraLightItalic-tlf-ly1.tfm)
Provides:       tex(IBMPlexSerif-ExtraLightItalic-tlf-ly1.vf)
Provides:       tex(IBMPlexSerif-ExtraLightItalic-tlf-ot1.tfm)
Provides:       tex(IBMPlexSerif-ExtraLightItalic-tlf-t1--base.tfm)
Provides:       tex(IBMPlexSerif-ExtraLightItalic-tlf-t1.tfm)
Provides:       tex(IBMPlexSerif-ExtraLightItalic-tlf-t1.vf)
Provides:       tex(IBMPlexSerif-ExtraLightItalic-tlf-ts1--base.tfm)
Provides:       tex(IBMPlexSerif-ExtraLightItalic-tlf-ts1.tfm)
Provides:       tex(IBMPlexSerif-ExtraLightItalic-tlf-ts1.vf)
Provides:       tex(IBMPlexSerif-Italic-sup-ly1--base.tfm)
Provides:       tex(IBMPlexSerif-Italic-sup-ly1.tfm)
Provides:       tex(IBMPlexSerif-Italic-sup-ly1.vf)
Provides:       tex(IBMPlexSerif-Italic-sup-ot1.tfm)
Provides:       tex(IBMPlexSerif-Italic-sup-t1--base.tfm)
Provides:       tex(IBMPlexSerif-Italic-sup-t1.tfm)
Provides:       tex(IBMPlexSerif-Italic-sup-t1.vf)
Provides:       tex(IBMPlexSerif-Italic-tlf-ly1--base.tfm)
Provides:       tex(IBMPlexSerif-Italic-tlf-ly1.tfm)
Provides:       tex(IBMPlexSerif-Italic-tlf-ly1.vf)
Provides:       tex(IBMPlexSerif-Italic-tlf-ot1.tfm)
Provides:       tex(IBMPlexSerif-Italic-tlf-t1--base.tfm)
Provides:       tex(IBMPlexSerif-Italic-tlf-t1.tfm)
Provides:       tex(IBMPlexSerif-Italic-tlf-t1.vf)
Provides:       tex(IBMPlexSerif-Italic-tlf-ts1--base.tfm)
Provides:       tex(IBMPlexSerif-Italic-tlf-ts1.tfm)
Provides:       tex(IBMPlexSerif-Italic-tlf-ts1.vf)
Provides:       tex(IBMPlexSerif-Light-sup-ly1--base.tfm)
Provides:       tex(IBMPlexSerif-Light-sup-ly1.tfm)
Provides:       tex(IBMPlexSerif-Light-sup-ly1.vf)
Provides:       tex(IBMPlexSerif-Light-sup-ot1.tfm)
Provides:       tex(IBMPlexSerif-Light-sup-t1--base.tfm)
Provides:       tex(IBMPlexSerif-Light-sup-t1.tfm)
Provides:       tex(IBMPlexSerif-Light-sup-t1.vf)
Provides:       tex(IBMPlexSerif-Light-tlf-ly1--base.tfm)
Provides:       tex(IBMPlexSerif-Light-tlf-ly1.tfm)
Provides:       tex(IBMPlexSerif-Light-tlf-ly1.vf)
Provides:       tex(IBMPlexSerif-Light-tlf-ot1.tfm)
Provides:       tex(IBMPlexSerif-Light-tlf-t1--base.tfm)
Provides:       tex(IBMPlexSerif-Light-tlf-t1.tfm)
Provides:       tex(IBMPlexSerif-Light-tlf-t1.vf)
Provides:       tex(IBMPlexSerif-Light-tlf-ts1--base.tfm)
Provides:       tex(IBMPlexSerif-Light-tlf-ts1.tfm)
Provides:       tex(IBMPlexSerif-Light-tlf-ts1.vf)
Provides:       tex(IBMPlexSerif-LightItalic-sup-ly1--base.tfm)
Provides:       tex(IBMPlexSerif-LightItalic-sup-ly1.tfm)
Provides:       tex(IBMPlexSerif-LightItalic-sup-ly1.vf)
Provides:       tex(IBMPlexSerif-LightItalic-sup-ot1.tfm)
Provides:       tex(IBMPlexSerif-LightItalic-sup-t1--base.tfm)
Provides:       tex(IBMPlexSerif-LightItalic-sup-t1.tfm)
Provides:       tex(IBMPlexSerif-LightItalic-sup-t1.vf)
Provides:       tex(IBMPlexSerif-LightItalic-tlf-ly1--base.tfm)
Provides:       tex(IBMPlexSerif-LightItalic-tlf-ly1.tfm)
Provides:       tex(IBMPlexSerif-LightItalic-tlf-ly1.vf)
Provides:       tex(IBMPlexSerif-LightItalic-tlf-ot1.tfm)
Provides:       tex(IBMPlexSerif-LightItalic-tlf-t1--base.tfm)
Provides:       tex(IBMPlexSerif-LightItalic-tlf-t1.tfm)
Provides:       tex(IBMPlexSerif-LightItalic-tlf-t1.vf)
Provides:       tex(IBMPlexSerif-LightItalic-tlf-ts1--base.tfm)
Provides:       tex(IBMPlexSerif-LightItalic-tlf-ts1.tfm)
Provides:       tex(IBMPlexSerif-LightItalic-tlf-ts1.vf)
Provides:       tex(IBMPlexSerif-Medium-sup-ly1--base.tfm)
Provides:       tex(IBMPlexSerif-Medium-sup-ly1.tfm)
Provides:       tex(IBMPlexSerif-Medium-sup-ly1.vf)
Provides:       tex(IBMPlexSerif-Medium-sup-ot1.tfm)
Provides:       tex(IBMPlexSerif-Medium-sup-t1--base.tfm)
Provides:       tex(IBMPlexSerif-Medium-sup-t1.tfm)
Provides:       tex(IBMPlexSerif-Medium-sup-t1.vf)
Provides:       tex(IBMPlexSerif-Medium-tlf-ly1--base.tfm)
Provides:       tex(IBMPlexSerif-Medium-tlf-ly1.tfm)
Provides:       tex(IBMPlexSerif-Medium-tlf-ly1.vf)
Provides:       tex(IBMPlexSerif-Medium-tlf-ot1.tfm)
Provides:       tex(IBMPlexSerif-Medium-tlf-t1--base.tfm)
Provides:       tex(IBMPlexSerif-Medium-tlf-t1.tfm)
Provides:       tex(IBMPlexSerif-Medium-tlf-t1.vf)
Provides:       tex(IBMPlexSerif-Medium-tlf-ts1--base.tfm)
Provides:       tex(IBMPlexSerif-Medium-tlf-ts1.tfm)
Provides:       tex(IBMPlexSerif-Medium-tlf-ts1.vf)
Provides:       tex(IBMPlexSerif-MediumItalic-sup-ly1--base.tfm)
Provides:       tex(IBMPlexSerif-MediumItalic-sup-ly1.tfm)
Provides:       tex(IBMPlexSerif-MediumItalic-sup-ly1.vf)
Provides:       tex(IBMPlexSerif-MediumItalic-sup-ot1.tfm)
Provides:       tex(IBMPlexSerif-MediumItalic-sup-t1--base.tfm)
Provides:       tex(IBMPlexSerif-MediumItalic-sup-t1.tfm)
Provides:       tex(IBMPlexSerif-MediumItalic-sup-t1.vf)
Provides:       tex(IBMPlexSerif-MediumItalic-tlf-ly1--base.tfm)
Provides:       tex(IBMPlexSerif-MediumItalic-tlf-ly1.tfm)
Provides:       tex(IBMPlexSerif-MediumItalic-tlf-ly1.vf)
Provides:       tex(IBMPlexSerif-MediumItalic-tlf-ot1.tfm)
Provides:       tex(IBMPlexSerif-MediumItalic-tlf-t1--base.tfm)
Provides:       tex(IBMPlexSerif-MediumItalic-tlf-t1.tfm)
Provides:       tex(IBMPlexSerif-MediumItalic-tlf-t1.vf)
Provides:       tex(IBMPlexSerif-MediumItalic-tlf-ts1--base.tfm)
Provides:       tex(IBMPlexSerif-MediumItalic-tlf-ts1.tfm)
Provides:       tex(IBMPlexSerif-MediumItalic-tlf-ts1.vf)
Provides:       tex(IBMPlexSerif-SemiBold-sup-ly1--base.tfm)
Provides:       tex(IBMPlexSerif-SemiBold-sup-ly1.tfm)
Provides:       tex(IBMPlexSerif-SemiBold-sup-ly1.vf)
Provides:       tex(IBMPlexSerif-SemiBold-sup-ot1.tfm)
Provides:       tex(IBMPlexSerif-SemiBold-sup-t1--base.tfm)
Provides:       tex(IBMPlexSerif-SemiBold-sup-t1.tfm)
Provides:       tex(IBMPlexSerif-SemiBold-sup-t1.vf)
Provides:       tex(IBMPlexSerif-SemiBold-tlf-ly1--base.tfm)
Provides:       tex(IBMPlexSerif-SemiBold-tlf-ly1.tfm)
Provides:       tex(IBMPlexSerif-SemiBold-tlf-ly1.vf)
Provides:       tex(IBMPlexSerif-SemiBold-tlf-ot1.tfm)
Provides:       tex(IBMPlexSerif-SemiBold-tlf-t1--base.tfm)
Provides:       tex(IBMPlexSerif-SemiBold-tlf-t1.tfm)
Provides:       tex(IBMPlexSerif-SemiBold-tlf-t1.vf)
Provides:       tex(IBMPlexSerif-SemiBold-tlf-ts1--base.tfm)
Provides:       tex(IBMPlexSerif-SemiBold-tlf-ts1.tfm)
Provides:       tex(IBMPlexSerif-SemiBold-tlf-ts1.vf)
Provides:       tex(IBMPlexSerif-SemiBoldItalic-sup-ly1--base.tfm)
Provides:       tex(IBMPlexSerif-SemiBoldItalic-sup-ly1.tfm)
Provides:       tex(IBMPlexSerif-SemiBoldItalic-sup-ly1.vf)
Provides:       tex(IBMPlexSerif-SemiBoldItalic-sup-ot1.tfm)
Provides:       tex(IBMPlexSerif-SemiBoldItalic-sup-t1--base.tfm)
Provides:       tex(IBMPlexSerif-SemiBoldItalic-sup-t1.tfm)
Provides:       tex(IBMPlexSerif-SemiBoldItalic-sup-t1.vf)
Provides:       tex(IBMPlexSerif-SemiBoldItalic-tlf-ly1--base.tfm)
Provides:       tex(IBMPlexSerif-SemiBoldItalic-tlf-ly1.tfm)
Provides:       tex(IBMPlexSerif-SemiBoldItalic-tlf-ly1.vf)
Provides:       tex(IBMPlexSerif-SemiBoldItalic-tlf-ot1.tfm)
Provides:       tex(IBMPlexSerif-SemiBoldItalic-tlf-t1--base.tfm)
Provides:       tex(IBMPlexSerif-SemiBoldItalic-tlf-t1.tfm)
Provides:       tex(IBMPlexSerif-SemiBoldItalic-tlf-t1.vf)
Provides:       tex(IBMPlexSerif-SemiBoldItalic-tlf-ts1--base.tfm)
Provides:       tex(IBMPlexSerif-SemiBoldItalic-tlf-ts1.tfm)
Provides:       tex(IBMPlexSerif-SemiBoldItalic-tlf-ts1.vf)
Provides:       tex(IBMPlexSerif-Text-sup-ly1--base.tfm)
Provides:       tex(IBMPlexSerif-Text-sup-ly1.tfm)
Provides:       tex(IBMPlexSerif-Text-sup-ly1.vf)
Provides:       tex(IBMPlexSerif-Text-sup-ot1.tfm)
Provides:       tex(IBMPlexSerif-Text-sup-t1--base.tfm)
Provides:       tex(IBMPlexSerif-Text-sup-t1.tfm)
Provides:       tex(IBMPlexSerif-Text-sup-t1.vf)
Provides:       tex(IBMPlexSerif-Text-tlf-ly1--base.tfm)
Provides:       tex(IBMPlexSerif-Text-tlf-ly1.tfm)
Provides:       tex(IBMPlexSerif-Text-tlf-ly1.vf)
Provides:       tex(IBMPlexSerif-Text-tlf-ot1.tfm)
Provides:       tex(IBMPlexSerif-Text-tlf-t1--base.tfm)
Provides:       tex(IBMPlexSerif-Text-tlf-t1.tfm)
Provides:       tex(IBMPlexSerif-Text-tlf-t1.vf)
Provides:       tex(IBMPlexSerif-Text-tlf-ts1--base.tfm)
Provides:       tex(IBMPlexSerif-Text-tlf-ts1.tfm)
Provides:       tex(IBMPlexSerif-Text-tlf-ts1.vf)
Provides:       tex(IBMPlexSerif-TextItalic-sup-ly1--base.tfm)
Provides:       tex(IBMPlexSerif-TextItalic-sup-ly1.tfm)
Provides:       tex(IBMPlexSerif-TextItalic-sup-ly1.vf)
Provides:       tex(IBMPlexSerif-TextItalic-sup-ot1.tfm)
Provides:       tex(IBMPlexSerif-TextItalic-sup-t1--base.tfm)
Provides:       tex(IBMPlexSerif-TextItalic-sup-t1.tfm)
Provides:       tex(IBMPlexSerif-TextItalic-sup-t1.vf)
Provides:       tex(IBMPlexSerif-TextItalic-tlf-ly1--base.tfm)
Provides:       tex(IBMPlexSerif-TextItalic-tlf-ly1.tfm)
Provides:       tex(IBMPlexSerif-TextItalic-tlf-ly1.vf)
Provides:       tex(IBMPlexSerif-TextItalic-tlf-ot1.tfm)
Provides:       tex(IBMPlexSerif-TextItalic-tlf-t1--base.tfm)
Provides:       tex(IBMPlexSerif-TextItalic-tlf-t1.tfm)
Provides:       tex(IBMPlexSerif-TextItalic-tlf-t1.vf)
Provides:       tex(IBMPlexSerif-TextItalic-tlf-ts1--base.tfm)
Provides:       tex(IBMPlexSerif-TextItalic-tlf-ts1.tfm)
Provides:       tex(IBMPlexSerif-TextItalic-tlf-ts1.vf)
Provides:       tex(IBMPlexSerif-Thin-sup-ly1--base.tfm)
Provides:       tex(IBMPlexSerif-Thin-sup-ly1.tfm)
Provides:       tex(IBMPlexSerif-Thin-sup-ly1.vf)
Provides:       tex(IBMPlexSerif-Thin-sup-ot1.tfm)
Provides:       tex(IBMPlexSerif-Thin-sup-t1--base.tfm)
Provides:       tex(IBMPlexSerif-Thin-sup-t1.tfm)
Provides:       tex(IBMPlexSerif-Thin-sup-t1.vf)
Provides:       tex(IBMPlexSerif-Thin-tlf-ly1--base.tfm)
Provides:       tex(IBMPlexSerif-Thin-tlf-ly1.tfm)
Provides:       tex(IBMPlexSerif-Thin-tlf-ly1.vf)
Provides:       tex(IBMPlexSerif-Thin-tlf-ot1.tfm)
Provides:       tex(IBMPlexSerif-Thin-tlf-t1--base.tfm)
Provides:       tex(IBMPlexSerif-Thin-tlf-t1.tfm)
Provides:       tex(IBMPlexSerif-Thin-tlf-t1.vf)
Provides:       tex(IBMPlexSerif-Thin-tlf-ts1--base.tfm)
Provides:       tex(IBMPlexSerif-Thin-tlf-ts1.tfm)
Provides:       tex(IBMPlexSerif-Thin-tlf-ts1.vf)
Provides:       tex(IBMPlexSerif-ThinItalic-sup-ly1--base.tfm)
Provides:       tex(IBMPlexSerif-ThinItalic-sup-ly1.tfm)
Provides:       tex(IBMPlexSerif-ThinItalic-sup-ly1.vf)
Provides:       tex(IBMPlexSerif-ThinItalic-sup-ot1.tfm)
Provides:       tex(IBMPlexSerif-ThinItalic-sup-t1--base.tfm)
Provides:       tex(IBMPlexSerif-ThinItalic-sup-t1.tfm)
Provides:       tex(IBMPlexSerif-ThinItalic-sup-t1.vf)
Provides:       tex(IBMPlexSerif-ThinItalic-tlf-ly1--base.tfm)
Provides:       tex(IBMPlexSerif-ThinItalic-tlf-ly1.tfm)
Provides:       tex(IBMPlexSerif-ThinItalic-tlf-ly1.vf)
Provides:       tex(IBMPlexSerif-ThinItalic-tlf-ot1.tfm)
Provides:       tex(IBMPlexSerif-ThinItalic-tlf-t1--base.tfm)
Provides:       tex(IBMPlexSerif-ThinItalic-tlf-t1.tfm)
Provides:       tex(IBMPlexSerif-ThinItalic-tlf-t1.vf)
Provides:       tex(IBMPlexSerif-ThinItalic-tlf-ts1--base.tfm)
Provides:       tex(IBMPlexSerif-ThinItalic-tlf-ts1.tfm)
Provides:       tex(IBMPlexSerif-ThinItalic-tlf-ts1.vf)
Provides:       tex(IBMPlexSerif-sup-ly1--base.tfm)
Provides:       tex(IBMPlexSerif-sup-ly1.tfm)
Provides:       tex(IBMPlexSerif-sup-ly1.vf)
Provides:       tex(IBMPlexSerif-sup-ot1.tfm)
Provides:       tex(IBMPlexSerif-sup-t1--base.tfm)
Provides:       tex(IBMPlexSerif-sup-t1.tfm)
Provides:       tex(IBMPlexSerif-sup-t1.vf)
Provides:       tex(IBMPlexSerif-tlf-ly1--base.tfm)
Provides:       tex(IBMPlexSerif-tlf-ly1.tfm)
Provides:       tex(IBMPlexSerif-tlf-ly1.vf)
Provides:       tex(IBMPlexSerif-tlf-ot1.tfm)
Provides:       tex(IBMPlexSerif-tlf-t1--base.tfm)
Provides:       tex(IBMPlexSerif-tlf-t1.tfm)
Provides:       tex(IBMPlexSerif-tlf-t1.vf)
Provides:       tex(IBMPlexSerif-tlf-ts1--base.tfm)
Provides:       tex(IBMPlexSerif-tlf-ts1.tfm)
Provides:       tex(IBMPlexSerif-tlf-ts1.vf)
Provides:       tex(LGRIBMPlexSans-Sup.fd)
Provides:       tex(LGRIBMPlexSans-TLF.fd)
Provides:       tex(LY1IBMPlexMono-Sup.fd)
Provides:       tex(LY1IBMPlexMono-TLF.fd)
Provides:       tex(LY1IBMPlexSans-Sup.fd)
Provides:       tex(LY1IBMPlexSans-TLF.fd)
Provides:       tex(LY1IBMPlexSerif-Sup.fd)
Provides:       tex(LY1IBMPlexSerif-TLF.fd)
Provides:       tex(OT1IBMPlexMono-Sup.fd)
Provides:       tex(OT1IBMPlexMono-TLF.fd)
Provides:       tex(OT1IBMPlexSans-Sup.fd)
Provides:       tex(OT1IBMPlexSans-TLF.fd)
Provides:       tex(OT1IBMPlexSerif-Sup.fd)
Provides:       tex(OT1IBMPlexSerif-TLF.fd)
Provides:       tex(T1IBMPlexMono-Sup.fd)
Provides:       tex(T1IBMPlexMono-TLF.fd)
Provides:       tex(T1IBMPlexSans-Sup.fd)
Provides:       tex(T1IBMPlexSans-TLF.fd)
Provides:       tex(T1IBMPlexSerif-Sup.fd)
Provides:       tex(T1IBMPlexSerif-TLF.fd)
Provides:       tex(TS1IBMPlexMono-TLF.fd)
Provides:       tex(TS1IBMPlexSans-TLF.fd)
Provides:       tex(TS1IBMPlexSerif-TLF.fd)
Provides:       tex(plex-mono.sty)
Provides:       tex(plex-sans.sty)
Provides:       tex(plex-serif.sty)
Provides:       tex(plex.map)
Provides:       tex(plx_2hzyxp.enc)
Provides:       tex(plx_4hck4s.enc)
Provides:       tex(plx_6tuc4c.enc)
Provides:       tex(plx_dzqm4q.enc)
Provides:       tex(plx_errukl.enc)
Provides:       tex(plx_eywvcp.enc)
Provides:       tex(plx_h3p6bl.enc)
Provides:       tex(plx_hrol52.enc)
Provides:       tex(plx_imandq.enc)
Provides:       tex(plx_lfnaaq.enc)
Provides:       tex(plx_lxmhqh.enc)
Provides:       tex(plx_mnk4s5.enc)
Provides:       tex(plx_n2etni.enc)
Provides:       tex(plx_nzsfse.enc)
Provides:       tex(plx_ojqnwd.enc)
Provides:       tex(plx_oqvkyq.enc)
Provides:       tex(plx_qdoxri.enc)
Provides:       tex(plx_sebx3h.enc)
Provides:       tex(plx_tibbib.enc)
Provides:       tex(plx_toaz2j.enc)
Provides:       tex(plx_umrhwx.enc)
Provides:       tex(plx_vf6q7q.enc)
Provides:       tex(plx_wot2a6.enc)
Provides:       tex(plx_x4zmfh.enc)
Provides:       tex(plx_xl2q4z.enc)
Requires:       tex(fontaxes.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(mweights.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xkeyval.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source16:       plex.tar.xz
Source17:       plex.doc.tar.xz

%description -n texlive-plex
The package provides LaTeX, pdfLaTeX, XeLaTeX and LuaLaTeX
support for the IBM Plex families of fonts. Serif, Sans and
Mono families are available in eight weights: Regular, Light,
ExtraLight, Thin, Bold, Text, Medium and SemiBold (with
corresponding italics).

%package -n texlive-plex-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn54512
Release:        0
Summary:        Documentation for texlive-plex
License:        OFL-1.1
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/

%description -n texlive-plex-doc
This package includes the documentation for texlive-plex

%package -n texlive-plex-fonts
Version:        %{texlive_version}.%{texlive_noarch}.svn54512
Release:        0
Summary:        Severed fonts for texlive-plex
License:        OFL-1.1
URL:            https://www.tug.org/texlive/
Group:          Productivity/Publishing/TeX/Fonts
%reconfigure_fonts_prereq
Requires(posttrans):fontconfig
Requires(posttrans):ghostscript-fonts-std
Requires(posttrans):mkfontdir
Requires(posttrans):mkfontscale
Requires(posttrans):xorg-x11-fonts-core

%description -n texlive-plex-fonts
The  separated fonts package for texlive-plex

%post -n texlive-plex
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
echo 'addMap plex.map' >> /var/run/texlive/run-updmap

%postun -n texlive-plex
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    echo 'deleteMap plex.map' >> /var/run/texlive/run-updmap
    exit 0
fi

%posttrans -n texlive-plex
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-plex-fonts

%files -n texlive-plex-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/plex/LICENSE.txt
%{_texmfdistdir}/doc/fonts/plex/README
%{_texmfdistdir}/doc/fonts/plex/plex-samples.pdf
%{_texmfdistdir}/doc/fonts/plex/plex-samples.tex

%files -n texlive-plex
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/enc/dvips/plex/plx_2hzyxp.enc
%{_texmfdistdir}/fonts/enc/dvips/plex/plx_4hck4s.enc
%{_texmfdistdir}/fonts/enc/dvips/plex/plx_6tuc4c.enc
%{_texmfdistdir}/fonts/enc/dvips/plex/plx_dzqm4q.enc
%{_texmfdistdir}/fonts/enc/dvips/plex/plx_errukl.enc
%{_texmfdistdir}/fonts/enc/dvips/plex/plx_eywvcp.enc
%{_texmfdistdir}/fonts/enc/dvips/plex/plx_h3p6bl.enc
%{_texmfdistdir}/fonts/enc/dvips/plex/plx_hrol52.enc
%{_texmfdistdir}/fonts/enc/dvips/plex/plx_imandq.enc
%{_texmfdistdir}/fonts/enc/dvips/plex/plx_lfnaaq.enc
%{_texmfdistdir}/fonts/enc/dvips/plex/plx_lxmhqh.enc
%{_texmfdistdir}/fonts/enc/dvips/plex/plx_mnk4s5.enc
%{_texmfdistdir}/fonts/enc/dvips/plex/plx_n2etni.enc
%{_texmfdistdir}/fonts/enc/dvips/plex/plx_nzsfse.enc
%{_texmfdistdir}/fonts/enc/dvips/plex/plx_ojqnwd.enc
%{_texmfdistdir}/fonts/enc/dvips/plex/plx_oqvkyq.enc
%{_texmfdistdir}/fonts/enc/dvips/plex/plx_qdoxri.enc
%{_texmfdistdir}/fonts/enc/dvips/plex/plx_sebx3h.enc
%{_texmfdistdir}/fonts/enc/dvips/plex/plx_tibbib.enc
%{_texmfdistdir}/fonts/enc/dvips/plex/plx_toaz2j.enc
%{_texmfdistdir}/fonts/enc/dvips/plex/plx_umrhwx.enc
%{_texmfdistdir}/fonts/enc/dvips/plex/plx_vf6q7q.enc
%{_texmfdistdir}/fonts/enc/dvips/plex/plx_wot2a6.enc
%{_texmfdistdir}/fonts/enc/dvips/plex/plx_x4zmfh.enc
%{_texmfdistdir}/fonts/enc/dvips/plex/plx_xl2q4z.enc
%{_texmfdistdir}/fonts/map/dvips/plex/plex.map
%verify(link) %{_texmfdistdir}/fonts/opentype/ibm/plex/IBMPlexMono-Bold.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/ibm/plex/IBMPlexMono-BoldItalic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/ibm/plex/IBMPlexMono-ExtraLight.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/ibm/plex/IBMPlexMono-ExtraLightItalic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/ibm/plex/IBMPlexMono-Italic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/ibm/plex/IBMPlexMono-Light.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/ibm/plex/IBMPlexMono-LightItalic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/ibm/plex/IBMPlexMono-Medium.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/ibm/plex/IBMPlexMono-MediumItalic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/ibm/plex/IBMPlexMono-Regular.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/ibm/plex/IBMPlexMono-SemiBold.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/ibm/plex/IBMPlexMono-SemiBoldItalic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/ibm/plex/IBMPlexMono-Text.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/ibm/plex/IBMPlexMono-TextItalic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/ibm/plex/IBMPlexMono-Thin.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/ibm/plex/IBMPlexMono-ThinItalic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/ibm/plex/IBMPlexSans-Bold.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/ibm/plex/IBMPlexSans-BoldItalic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/ibm/plex/IBMPlexSans-ExtraLight.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/ibm/plex/IBMPlexSans-ExtraLightItalic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/ibm/plex/IBMPlexSans-Italic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/ibm/plex/IBMPlexSans-Light.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/ibm/plex/IBMPlexSans-LightItalic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/ibm/plex/IBMPlexSans-Medium.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/ibm/plex/IBMPlexSans-MediumItalic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/ibm/plex/IBMPlexSans-Regular.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/ibm/plex/IBMPlexSans-SemiBold.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/ibm/plex/IBMPlexSans-SemiBoldItalic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/ibm/plex/IBMPlexSans-Text.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/ibm/plex/IBMPlexSans-TextItalic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/ibm/plex/IBMPlexSans-Thin.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/ibm/plex/IBMPlexSans-ThinItalic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/ibm/plex/IBMPlexSansCondensed-Bold.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/ibm/plex/IBMPlexSansCondensed-BoldItalic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/ibm/plex/IBMPlexSansCondensed-ExtraLight.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/ibm/plex/IBMPlexSansCondensed-ExtraLightItalic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/ibm/plex/IBMPlexSansCondensed-Italic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/ibm/plex/IBMPlexSansCondensed-Light.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/ibm/plex/IBMPlexSansCondensed-LightItalic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/ibm/plex/IBMPlexSansCondensed-Medium.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/ibm/plex/IBMPlexSansCondensed-MediumItalic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/ibm/plex/IBMPlexSansCondensed-Regular.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/ibm/plex/IBMPlexSansCondensed-SemiBold.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/ibm/plex/IBMPlexSansCondensed-SemiBoldItalic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/ibm/plex/IBMPlexSansCondensed-Text.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/ibm/plex/IBMPlexSansCondensed-TextItalic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/ibm/plex/IBMPlexSansCondensed-Thin.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/ibm/plex/IBMPlexSansCondensed-ThinItalic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/ibm/plex/IBMPlexSerif-Bold.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/ibm/plex/IBMPlexSerif-BoldItalic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/ibm/plex/IBMPlexSerif-ExtraLight.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/ibm/plex/IBMPlexSerif-ExtraLightItalic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/ibm/plex/IBMPlexSerif-Italic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/ibm/plex/IBMPlexSerif-Light.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/ibm/plex/IBMPlexSerif-LightItalic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/ibm/plex/IBMPlexSerif-Medium.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/ibm/plex/IBMPlexSerif-MediumItalic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/ibm/plex/IBMPlexSerif-Regular.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/ibm/plex/IBMPlexSerif-SemiBold.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/ibm/plex/IBMPlexSerif-SemiBoldItalic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/ibm/plex/IBMPlexSerif-Text.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/ibm/plex/IBMPlexSerif-TextItalic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/ibm/plex/IBMPlexSerif-Thin.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/ibm/plex/IBMPlexSerif-ThinItalic.otf
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-Bold-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-Bold-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-Bold-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-Bold-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-Bold-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-Bold-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-Bold-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-Bold-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-Bold-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-Bold-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-Bold-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-Bold-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-BoldItalic-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-BoldItalic-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-BoldItalic-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-BoldItalic-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-BoldItalic-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-BoldItalic-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-BoldItalic-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-BoldItalic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-BoldItalic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-BoldItalic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-BoldItalic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-BoldItalic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-ExtraLight-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-ExtraLight-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-ExtraLight-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-ExtraLight-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-ExtraLight-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-ExtraLight-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-ExtraLight-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-ExtraLight-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-ExtraLight-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-ExtraLight-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-ExtraLight-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-ExtraLight-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-ExtraLightItalic-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-ExtraLightItalic-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-ExtraLightItalic-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-ExtraLightItalic-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-ExtraLightItalic-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-ExtraLightItalic-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-ExtraLightItalic-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-ExtraLightItalic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-ExtraLightItalic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-ExtraLightItalic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-ExtraLightItalic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-ExtraLightItalic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-Italic-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-Italic-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-Italic-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-Italic-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-Italic-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-Italic-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-Italic-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-Italic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-Italic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-Italic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-Italic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-Italic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-Light-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-Light-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-Light-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-Light-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-Light-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-Light-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-Light-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-Light-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-Light-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-Light-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-Light-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-Light-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-LightItalic-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-LightItalic-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-LightItalic-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-LightItalic-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-LightItalic-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-LightItalic-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-LightItalic-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-LightItalic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-LightItalic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-LightItalic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-LightItalic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-LightItalic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-Medium-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-Medium-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-Medium-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-Medium-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-Medium-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-Medium-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-Medium-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-Medium-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-Medium-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-Medium-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-Medium-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-Medium-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-MediumItalic-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-MediumItalic-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-MediumItalic-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-MediumItalic-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-MediumItalic-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-MediumItalic-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-MediumItalic-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-MediumItalic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-MediumItalic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-MediumItalic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-MediumItalic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-MediumItalic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-SemiBold-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-SemiBold-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-SemiBold-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-SemiBold-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-SemiBold-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-SemiBold-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-SemiBold-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-SemiBold-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-SemiBold-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-SemiBold-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-SemiBold-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-SemiBold-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-SemiBoldItalic-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-SemiBoldItalic-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-SemiBoldItalic-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-SemiBoldItalic-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-SemiBoldItalic-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-SemiBoldItalic-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-SemiBoldItalic-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-SemiBoldItalic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-SemiBoldItalic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-SemiBoldItalic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-SemiBoldItalic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-SemiBoldItalic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-Text-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-Text-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-Text-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-Text-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-Text-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-Text-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-Text-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-Text-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-Text-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-Text-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-Text-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-Text-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-TextItalic-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-TextItalic-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-TextItalic-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-TextItalic-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-TextItalic-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-TextItalic-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-TextItalic-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-TextItalic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-TextItalic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-TextItalic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-TextItalic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-TextItalic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-Thin-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-Thin-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-Thin-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-Thin-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-Thin-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-Thin-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-Thin-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-Thin-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-Thin-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-Thin-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-Thin-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-Thin-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-ThinItalic-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-ThinItalic-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-ThinItalic-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-ThinItalic-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-ThinItalic-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-ThinItalic-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-ThinItalic-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-ThinItalic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-ThinItalic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-ThinItalic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-ThinItalic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-ThinItalic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexMono-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-Bold-sup-lgr--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-Bold-sup-lgr.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-Bold-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-Bold-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-Bold-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-Bold-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-Bold-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-Bold-tlf-lgr--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-Bold-tlf-lgr.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-Bold-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-Bold-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-Bold-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-Bold-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-Bold-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-Bold-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-Bold-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-BoldItalic-sup-lgr--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-BoldItalic-sup-lgr.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-BoldItalic-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-BoldItalic-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-BoldItalic-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-BoldItalic-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-BoldItalic-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-BoldItalic-tlf-lgr--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-BoldItalic-tlf-lgr.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-BoldItalic-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-BoldItalic-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-BoldItalic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-BoldItalic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-BoldItalic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-BoldItalic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-BoldItalic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-ExtraLight-sup-lgr--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-ExtraLight-sup-lgr.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-ExtraLight-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-ExtraLight-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-ExtraLight-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-ExtraLight-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-ExtraLight-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-ExtraLight-tlf-lgr--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-ExtraLight-tlf-lgr.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-ExtraLight-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-ExtraLight-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-ExtraLight-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-ExtraLight-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-ExtraLight-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-ExtraLight-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-ExtraLight-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-ExtraLightItalic-sup-lgr--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-ExtraLightItalic-sup-lgr.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-ExtraLightItalic-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-ExtraLightItalic-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-ExtraLightItalic-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-ExtraLightItalic-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-ExtraLightItalic-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-ExtraLightItalic-tlf-lgr--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-ExtraLightItalic-tlf-lgr.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-ExtraLightItalic-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-ExtraLightItalic-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-ExtraLightItalic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-ExtraLightItalic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-ExtraLightItalic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-ExtraLightItalic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-ExtraLightItalic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-Italic-sup-lgr--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-Italic-sup-lgr.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-Italic-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-Italic-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-Italic-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-Italic-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-Italic-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-Italic-tlf-lgr--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-Italic-tlf-lgr.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-Italic-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-Italic-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-Italic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-Italic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-Italic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-Italic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-Italic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-Light-sup-lgr--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-Light-sup-lgr.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-Light-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-Light-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-Light-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-Light-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-Light-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-Light-tlf-lgr--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-Light-tlf-lgr.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-Light-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-Light-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-Light-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-Light-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-Light-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-Light-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-Light-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-LightItalic-sup-lgr--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-LightItalic-sup-lgr.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-LightItalic-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-LightItalic-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-LightItalic-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-LightItalic-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-LightItalic-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-LightItalic-tlf-lgr--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-LightItalic-tlf-lgr.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-LightItalic-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-LightItalic-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-LightItalic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-LightItalic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-LightItalic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-LightItalic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-LightItalic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-Medium-sup-lgr--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-Medium-sup-lgr.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-Medium-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-Medium-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-Medium-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-Medium-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-Medium-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-Medium-tlf-lgr--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-Medium-tlf-lgr.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-Medium-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-Medium-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-Medium-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-Medium-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-Medium-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-Medium-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-Medium-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-MediumItalic-sup-lgr--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-MediumItalic-sup-lgr.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-MediumItalic-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-MediumItalic-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-MediumItalic-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-MediumItalic-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-MediumItalic-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-MediumItalic-tlf-lgr--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-MediumItalic-tlf-lgr.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-MediumItalic-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-MediumItalic-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-MediumItalic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-MediumItalic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-MediumItalic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-MediumItalic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-MediumItalic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-SemiBold-sup-lgr--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-SemiBold-sup-lgr.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-SemiBold-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-SemiBold-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-SemiBold-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-SemiBold-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-SemiBold-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-SemiBold-tlf-lgr--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-SemiBold-tlf-lgr.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-SemiBold-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-SemiBold-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-SemiBold-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-SemiBold-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-SemiBold-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-SemiBold-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-SemiBold-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-SemiBoldItalic-sup-lgr--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-SemiBoldItalic-sup-lgr.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-SemiBoldItalic-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-SemiBoldItalic-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-SemiBoldItalic-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-SemiBoldItalic-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-SemiBoldItalic-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-SemiBoldItalic-tlf-lgr--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-SemiBoldItalic-tlf-lgr.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-SemiBoldItalic-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-SemiBoldItalic-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-SemiBoldItalic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-SemiBoldItalic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-SemiBoldItalic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-SemiBoldItalic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-SemiBoldItalic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-Text-sup-lgr--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-Text-sup-lgr.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-Text-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-Text-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-Text-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-Text-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-Text-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-Text-tlf-lgr--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-Text-tlf-lgr.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-Text-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-Text-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-Text-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-Text-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-Text-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-Text-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-Text-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-TextItalic-sup-lgr--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-TextItalic-sup-lgr.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-TextItalic-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-TextItalic-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-TextItalic-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-TextItalic-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-TextItalic-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-TextItalic-tlf-lgr--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-TextItalic-tlf-lgr.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-TextItalic-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-TextItalic-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-TextItalic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-TextItalic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-TextItalic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-TextItalic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-TextItalic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-Thin-sup-lgr--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-Thin-sup-lgr.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-Thin-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-Thin-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-Thin-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-Thin-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-Thin-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-Thin-tlf-lgr--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-Thin-tlf-lgr.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-Thin-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-Thin-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-Thin-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-Thin-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-Thin-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-Thin-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-Thin-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-ThinItalic-sup-lgr--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-ThinItalic-sup-lgr.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-ThinItalic-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-ThinItalic-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-ThinItalic-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-ThinItalic-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-ThinItalic-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-ThinItalic-tlf-lgr--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-ThinItalic-tlf-lgr.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-ThinItalic-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-ThinItalic-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-ThinItalic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-ThinItalic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-ThinItalic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-ThinItalic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-ThinItalic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-sup-lgr--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-sup-lgr.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-tlf-lgr--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-tlf-lgr.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSans-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-Bold-sup-lgr--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-Bold-sup-lgr.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-Bold-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-Bold-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-Bold-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-Bold-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-Bold-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-Bold-tlf-lgr--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-Bold-tlf-lgr.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-Bold-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-Bold-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-Bold-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-Bold-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-Bold-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-Bold-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-Bold-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-BoldItalic-sup-lgr--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-BoldItalic-sup-lgr.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-BoldItalic-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-BoldItalic-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-BoldItalic-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-BoldItalic-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-BoldItalic-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-BoldItalic-tlf-lgr--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-BoldItalic-tlf-lgr.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-BoldItalic-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-BoldItalic-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-BoldItalic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-BoldItalic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-BoldItalic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-BoldItalic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-BoldItalic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-ExtraLight-sup-lgr--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-ExtraLight-sup-lgr.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-ExtraLight-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-ExtraLight-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-ExtraLight-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-ExtraLight-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-ExtraLight-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-ExtraLight-tlf-lgr--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-ExtraLight-tlf-lgr.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-ExtraLight-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-ExtraLight-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-ExtraLight-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-ExtraLight-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-ExtraLight-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-ExtraLight-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-ExtraLight-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-ExtraLightItalic-sup-lgr--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-ExtraLightItalic-sup-lgr.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-ExtraLightItalic-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-ExtraLightItalic-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-ExtraLightItalic-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-ExtraLightItalic-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-ExtraLightItalic-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-ExtraLightItalic-tlf-lgr--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-ExtraLightItalic-tlf-lgr.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-ExtraLightItalic-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-ExtraLightItalic-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-ExtraLightItalic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-ExtraLightItalic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-ExtraLightItalic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-ExtraLightItalic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-ExtraLightItalic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-Italic-sup-lgr--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-Italic-sup-lgr.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-Italic-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-Italic-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-Italic-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-Italic-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-Italic-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-Italic-tlf-lgr--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-Italic-tlf-lgr.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-Italic-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-Italic-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-Italic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-Italic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-Italic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-Italic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-Italic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-Light-sup-lgr--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-Light-sup-lgr.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-Light-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-Light-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-Light-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-Light-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-Light-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-Light-tlf-lgr--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-Light-tlf-lgr.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-Light-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-Light-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-Light-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-Light-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-Light-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-Light-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-Light-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-LightItalic-sup-lgr--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-LightItalic-sup-lgr.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-LightItalic-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-LightItalic-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-LightItalic-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-LightItalic-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-LightItalic-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-LightItalic-tlf-lgr--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-LightItalic-tlf-lgr.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-LightItalic-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-LightItalic-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-LightItalic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-LightItalic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-LightItalic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-LightItalic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-LightItalic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-Medium-sup-lgr--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-Medium-sup-lgr.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-Medium-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-Medium-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-Medium-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-Medium-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-Medium-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-Medium-tlf-lgr--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-Medium-tlf-lgr.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-Medium-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-Medium-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-Medium-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-Medium-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-Medium-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-Medium-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-Medium-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-MediumItalic-sup-lgr--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-MediumItalic-sup-lgr.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-MediumItalic-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-MediumItalic-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-MediumItalic-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-MediumItalic-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-MediumItalic-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-MediumItalic-tlf-lgr--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-MediumItalic-tlf-lgr.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-MediumItalic-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-MediumItalic-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-MediumItalic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-MediumItalic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-MediumItalic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-MediumItalic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-MediumItalic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-SemiBold-sup-lgr--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-SemiBold-sup-lgr.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-SemiBold-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-SemiBold-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-SemiBold-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-SemiBold-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-SemiBold-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-SemiBold-tlf-lgr--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-SemiBold-tlf-lgr.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-SemiBold-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-SemiBold-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-SemiBold-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-SemiBold-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-SemiBold-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-SemiBold-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-SemiBold-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-SemiBoldItalic-sup-lgr--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-SemiBoldItalic-sup-lgr.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-SemiBoldItalic-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-SemiBoldItalic-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-SemiBoldItalic-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-SemiBoldItalic-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-SemiBoldItalic-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-SemiBoldItalic-tlf-lgr--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-SemiBoldItalic-tlf-lgr.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-SemiBoldItalic-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-SemiBoldItalic-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-SemiBoldItalic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-SemiBoldItalic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-SemiBoldItalic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-SemiBoldItalic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-SemiBoldItalic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-Text-sup-lgr--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-Text-sup-lgr.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-Text-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-Text-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-Text-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-Text-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-Text-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-Text-tlf-lgr--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-Text-tlf-lgr.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-Text-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-Text-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-Text-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-Text-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-Text-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-Text-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-Text-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-TextItalic-sup-lgr--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-TextItalic-sup-lgr.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-TextItalic-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-TextItalic-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-TextItalic-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-TextItalic-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-TextItalic-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-TextItalic-tlf-lgr--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-TextItalic-tlf-lgr.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-TextItalic-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-TextItalic-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-TextItalic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-TextItalic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-TextItalic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-TextItalic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-TextItalic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-Thin-sup-lgr--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-Thin-sup-lgr.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-Thin-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-Thin-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-Thin-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-Thin-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-Thin-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-Thin-tlf-lgr--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-Thin-tlf-lgr.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-Thin-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-Thin-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-Thin-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-Thin-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-Thin-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-Thin-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-Thin-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-ThinItalic-sup-lgr--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-ThinItalic-sup-lgr.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-ThinItalic-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-ThinItalic-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-ThinItalic-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-ThinItalic-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-ThinItalic-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-ThinItalic-tlf-lgr--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-ThinItalic-tlf-lgr.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-ThinItalic-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-ThinItalic-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-ThinItalic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-ThinItalic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-ThinItalic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-ThinItalic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-ThinItalic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-sup-lgr--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-sup-lgr.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-tlf-lgr--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-tlf-lgr.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSansCond-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-Bold-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-Bold-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-Bold-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-Bold-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-Bold-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-Bold-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-Bold-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-Bold-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-Bold-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-Bold-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-Bold-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-Bold-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-BoldItalic-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-BoldItalic-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-BoldItalic-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-BoldItalic-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-BoldItalic-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-BoldItalic-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-BoldItalic-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-BoldItalic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-BoldItalic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-BoldItalic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-BoldItalic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-BoldItalic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-ExtraLight-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-ExtraLight-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-ExtraLight-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-ExtraLight-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-ExtraLight-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-ExtraLight-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-ExtraLight-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-ExtraLight-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-ExtraLight-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-ExtraLight-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-ExtraLight-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-ExtraLight-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-ExtraLightItalic-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-ExtraLightItalic-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-ExtraLightItalic-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-ExtraLightItalic-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-ExtraLightItalic-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-ExtraLightItalic-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-ExtraLightItalic-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-ExtraLightItalic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-ExtraLightItalic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-ExtraLightItalic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-ExtraLightItalic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-ExtraLightItalic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-Italic-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-Italic-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-Italic-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-Italic-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-Italic-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-Italic-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-Italic-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-Italic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-Italic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-Italic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-Italic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-Italic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-Light-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-Light-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-Light-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-Light-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-Light-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-Light-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-Light-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-Light-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-Light-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-Light-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-Light-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-Light-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-LightItalic-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-LightItalic-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-LightItalic-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-LightItalic-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-LightItalic-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-LightItalic-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-LightItalic-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-LightItalic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-LightItalic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-LightItalic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-LightItalic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-LightItalic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-Medium-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-Medium-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-Medium-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-Medium-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-Medium-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-Medium-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-Medium-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-Medium-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-Medium-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-Medium-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-Medium-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-Medium-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-MediumItalic-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-MediumItalic-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-MediumItalic-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-MediumItalic-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-MediumItalic-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-MediumItalic-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-MediumItalic-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-MediumItalic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-MediumItalic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-MediumItalic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-MediumItalic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-MediumItalic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-SemiBold-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-SemiBold-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-SemiBold-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-SemiBold-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-SemiBold-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-SemiBold-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-SemiBold-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-SemiBold-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-SemiBold-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-SemiBold-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-SemiBold-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-SemiBold-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-SemiBoldItalic-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-SemiBoldItalic-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-SemiBoldItalic-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-SemiBoldItalic-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-SemiBoldItalic-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-SemiBoldItalic-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-SemiBoldItalic-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-SemiBoldItalic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-SemiBoldItalic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-SemiBoldItalic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-SemiBoldItalic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-SemiBoldItalic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-Text-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-Text-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-Text-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-Text-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-Text-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-Text-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-Text-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-Text-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-Text-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-Text-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-Text-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-Text-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-TextItalic-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-TextItalic-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-TextItalic-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-TextItalic-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-TextItalic-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-TextItalic-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-TextItalic-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-TextItalic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-TextItalic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-TextItalic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-TextItalic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-TextItalic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-Thin-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-Thin-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-Thin-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-Thin-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-Thin-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-Thin-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-Thin-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-Thin-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-Thin-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-Thin-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-Thin-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-Thin-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-ThinItalic-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-ThinItalic-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-ThinItalic-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-ThinItalic-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-ThinItalic-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-ThinItalic-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-ThinItalic-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-ThinItalic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-ThinItalic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-ThinItalic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-ThinItalic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-ThinItalic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/ibm/plex/IBMPlexSerif-tlf-ts1.tfm
%verify(link) %{_texmfdistdir}/fonts/type1/ibm/plex/IBMPlexMono-Bold.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/ibm/plex/IBMPlexMono-BoldItalic.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/ibm/plex/IBMPlexMono-ExtraLight.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/ibm/plex/IBMPlexMono-ExtraLightItalic.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/ibm/plex/IBMPlexMono-Italic.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/ibm/plex/IBMPlexMono-Light.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/ibm/plex/IBMPlexMono-LightItalic.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/ibm/plex/IBMPlexMono-Medium.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/ibm/plex/IBMPlexMono-MediumItalic.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/ibm/plex/IBMPlexMono-SemiBold.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/ibm/plex/IBMPlexMono-SemiBoldItalic.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/ibm/plex/IBMPlexMono-Text.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/ibm/plex/IBMPlexMono-TextItalic.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/ibm/plex/IBMPlexMono-Thin.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/ibm/plex/IBMPlexMono-ThinItalic.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/ibm/plex/IBMPlexMono.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/ibm/plex/IBMPlexSans-Bold.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/ibm/plex/IBMPlexSans-BoldItalic.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/ibm/plex/IBMPlexSans-ExtraLight.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/ibm/plex/IBMPlexSans-ExtraLightItalic.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/ibm/plex/IBMPlexSans-Italic.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/ibm/plex/IBMPlexSans-Light.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/ibm/plex/IBMPlexSans-LightItalic.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/ibm/plex/IBMPlexSans-Medium.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/ibm/plex/IBMPlexSans-MediumItalic.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/ibm/plex/IBMPlexSans-SemiBold.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/ibm/plex/IBMPlexSans-SemiBoldItalic.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/ibm/plex/IBMPlexSans-Text.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/ibm/plex/IBMPlexSans-TextItalic.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/ibm/plex/IBMPlexSans-Thin.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/ibm/plex/IBMPlexSans-ThinItalic.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/ibm/plex/IBMPlexSans.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/ibm/plex/IBMPlexSansCond-Bold.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/ibm/plex/IBMPlexSansCond-BoldItalic.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/ibm/plex/IBMPlexSansCond-ExtraLight.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/ibm/plex/IBMPlexSansCond-ExtraLightItalic.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/ibm/plex/IBMPlexSansCond-Italic.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/ibm/plex/IBMPlexSansCond-Light.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/ibm/plex/IBMPlexSansCond-LightItalic.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/ibm/plex/IBMPlexSansCond-Medium.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/ibm/plex/IBMPlexSansCond-MediumItalic.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/ibm/plex/IBMPlexSansCond-SemiBold.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/ibm/plex/IBMPlexSansCond-SemiBoldItalic.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/ibm/plex/IBMPlexSansCond-Text.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/ibm/plex/IBMPlexSansCond-TextItalic.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/ibm/plex/IBMPlexSansCond-Thin.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/ibm/plex/IBMPlexSansCond-ThinItalic.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/ibm/plex/IBMPlexSansCond.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/ibm/plex/IBMPlexSerif-Bold.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/ibm/plex/IBMPlexSerif-BoldItalic.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/ibm/plex/IBMPlexSerif-ExtraLight.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/ibm/plex/IBMPlexSerif-ExtraLightItalic.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/ibm/plex/IBMPlexSerif-Italic.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/ibm/plex/IBMPlexSerif-Light.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/ibm/plex/IBMPlexSerif-LightItalic.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/ibm/plex/IBMPlexSerif-Medium.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/ibm/plex/IBMPlexSerif-MediumItalic.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/ibm/plex/IBMPlexSerif-SemiBold.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/ibm/plex/IBMPlexSerif-SemiBoldItalic.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/ibm/plex/IBMPlexSerif-Text.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/ibm/plex/IBMPlexSerif-TextItalic.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/ibm/plex/IBMPlexSerif-Thin.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/ibm/plex/IBMPlexSerif-ThinItalic.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/ibm/plex/IBMPlexSerif.pfb
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexMono-Bold-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexMono-Bold-sup-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexMono-Bold-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexMono-Bold-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexMono-Bold-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexMono-BoldItalic-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexMono-BoldItalic-sup-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexMono-BoldItalic-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexMono-BoldItalic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexMono-BoldItalic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexMono-ExtraLight-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexMono-ExtraLight-sup-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexMono-ExtraLight-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexMono-ExtraLight-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexMono-ExtraLight-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexMono-ExtraLightItalic-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexMono-ExtraLightItalic-sup-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexMono-ExtraLightItalic-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexMono-ExtraLightItalic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexMono-ExtraLightItalic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexMono-Italic-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexMono-Italic-sup-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexMono-Italic-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexMono-Italic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexMono-Italic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexMono-Light-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexMono-Light-sup-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexMono-Light-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexMono-Light-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexMono-Light-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexMono-LightItalic-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexMono-LightItalic-sup-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexMono-LightItalic-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexMono-LightItalic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexMono-LightItalic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexMono-Medium-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexMono-Medium-sup-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexMono-Medium-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexMono-Medium-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexMono-Medium-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexMono-MediumItalic-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexMono-MediumItalic-sup-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexMono-MediumItalic-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexMono-MediumItalic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexMono-MediumItalic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexMono-SemiBold-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexMono-SemiBold-sup-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexMono-SemiBold-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexMono-SemiBold-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexMono-SemiBold-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexMono-SemiBoldItalic-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexMono-SemiBoldItalic-sup-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexMono-SemiBoldItalic-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexMono-SemiBoldItalic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexMono-SemiBoldItalic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexMono-Text-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexMono-Text-sup-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexMono-Text-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexMono-Text-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexMono-Text-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexMono-TextItalic-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexMono-TextItalic-sup-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexMono-TextItalic-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexMono-TextItalic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexMono-TextItalic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexMono-Thin-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexMono-Thin-sup-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexMono-Thin-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexMono-Thin-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexMono-Thin-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexMono-ThinItalic-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexMono-ThinItalic-sup-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexMono-ThinItalic-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexMono-ThinItalic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexMono-ThinItalic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexMono-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexMono-sup-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexMono-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexMono-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexMono-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSans-Bold-sup-lgr.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSans-Bold-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSans-Bold-sup-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSans-Bold-tlf-lgr.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSans-Bold-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSans-Bold-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSans-Bold-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSans-BoldItalic-sup-lgr.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSans-BoldItalic-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSans-BoldItalic-sup-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSans-BoldItalic-tlf-lgr.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSans-BoldItalic-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSans-BoldItalic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSans-BoldItalic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSans-ExtraLight-sup-lgr.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSans-ExtraLight-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSans-ExtraLight-sup-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSans-ExtraLight-tlf-lgr.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSans-ExtraLight-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSans-ExtraLight-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSans-ExtraLight-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSans-ExtraLightItalic-sup-lgr.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSans-ExtraLightItalic-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSans-ExtraLightItalic-sup-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSans-ExtraLightItalic-tlf-lgr.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSans-ExtraLightItalic-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSans-ExtraLightItalic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSans-ExtraLightItalic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSans-Italic-sup-lgr.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSans-Italic-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSans-Italic-sup-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSans-Italic-tlf-lgr.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSans-Italic-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSans-Italic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSans-Italic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSans-Light-sup-lgr.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSans-Light-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSans-Light-sup-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSans-Light-tlf-lgr.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSans-Light-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSans-Light-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSans-Light-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSans-LightItalic-sup-lgr.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSans-LightItalic-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSans-LightItalic-sup-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSans-LightItalic-tlf-lgr.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSans-LightItalic-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSans-LightItalic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSans-LightItalic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSans-Medium-sup-lgr.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSans-Medium-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSans-Medium-sup-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSans-Medium-tlf-lgr.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSans-Medium-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSans-Medium-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSans-Medium-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSans-MediumItalic-sup-lgr.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSans-MediumItalic-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSans-MediumItalic-sup-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSans-MediumItalic-tlf-lgr.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSans-MediumItalic-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSans-MediumItalic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSans-MediumItalic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSans-SemiBold-sup-lgr.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSans-SemiBold-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSans-SemiBold-sup-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSans-SemiBold-tlf-lgr.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSans-SemiBold-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSans-SemiBold-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSans-SemiBold-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSans-SemiBoldItalic-sup-lgr.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSans-SemiBoldItalic-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSans-SemiBoldItalic-sup-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSans-SemiBoldItalic-tlf-lgr.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSans-SemiBoldItalic-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSans-SemiBoldItalic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSans-SemiBoldItalic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSans-Text-sup-lgr.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSans-Text-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSans-Text-sup-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSans-Text-tlf-lgr.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSans-Text-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSans-Text-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSans-Text-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSans-TextItalic-sup-lgr.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSans-TextItalic-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSans-TextItalic-sup-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSans-TextItalic-tlf-lgr.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSans-TextItalic-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSans-TextItalic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSans-TextItalic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSans-Thin-sup-lgr.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSans-Thin-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSans-Thin-sup-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSans-Thin-tlf-lgr.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSans-Thin-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSans-Thin-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSans-Thin-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSans-ThinItalic-sup-lgr.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSans-ThinItalic-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSans-ThinItalic-sup-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSans-ThinItalic-tlf-lgr.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSans-ThinItalic-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSans-ThinItalic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSans-ThinItalic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSans-sup-lgr.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSans-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSans-sup-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSans-tlf-lgr.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSans-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSans-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSans-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSansCond-Bold-sup-lgr.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSansCond-Bold-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSansCond-Bold-sup-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSansCond-Bold-tlf-lgr.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSansCond-Bold-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSansCond-Bold-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSansCond-Bold-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSansCond-BoldItalic-sup-lgr.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSansCond-BoldItalic-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSansCond-BoldItalic-sup-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSansCond-BoldItalic-tlf-lgr.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSansCond-BoldItalic-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSansCond-BoldItalic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSansCond-BoldItalic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSansCond-ExtraLight-sup-lgr.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSansCond-ExtraLight-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSansCond-ExtraLight-sup-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSansCond-ExtraLight-tlf-lgr.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSansCond-ExtraLight-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSansCond-ExtraLight-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSansCond-ExtraLight-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSansCond-ExtraLightItalic-sup-lgr.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSansCond-ExtraLightItalic-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSansCond-ExtraLightItalic-sup-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSansCond-ExtraLightItalic-tlf-lgr.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSansCond-ExtraLightItalic-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSansCond-ExtraLightItalic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSansCond-ExtraLightItalic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSansCond-Italic-sup-lgr.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSansCond-Italic-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSansCond-Italic-sup-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSansCond-Italic-tlf-lgr.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSansCond-Italic-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSansCond-Italic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSansCond-Italic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSansCond-Light-sup-lgr.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSansCond-Light-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSansCond-Light-sup-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSansCond-Light-tlf-lgr.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSansCond-Light-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSansCond-Light-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSansCond-Light-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSansCond-LightItalic-sup-lgr.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSansCond-LightItalic-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSansCond-LightItalic-sup-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSansCond-LightItalic-tlf-lgr.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSansCond-LightItalic-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSansCond-LightItalic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSansCond-LightItalic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSansCond-Medium-sup-lgr.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSansCond-Medium-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSansCond-Medium-sup-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSansCond-Medium-tlf-lgr.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSansCond-Medium-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSansCond-Medium-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSansCond-Medium-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSansCond-MediumItalic-sup-lgr.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSansCond-MediumItalic-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSansCond-MediumItalic-sup-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSansCond-MediumItalic-tlf-lgr.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSansCond-MediumItalic-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSansCond-MediumItalic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSansCond-MediumItalic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSansCond-SemiBold-sup-lgr.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSansCond-SemiBold-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSansCond-SemiBold-sup-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSansCond-SemiBold-tlf-lgr.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSansCond-SemiBold-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSansCond-SemiBold-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSansCond-SemiBold-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSansCond-SemiBoldItalic-sup-lgr.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSansCond-SemiBoldItalic-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSansCond-SemiBoldItalic-sup-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSansCond-SemiBoldItalic-tlf-lgr.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSansCond-SemiBoldItalic-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSansCond-SemiBoldItalic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSansCond-SemiBoldItalic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSansCond-Text-sup-lgr.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSansCond-Text-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSansCond-Text-sup-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSansCond-Text-tlf-lgr.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSansCond-Text-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSansCond-Text-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSansCond-Text-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSansCond-TextItalic-sup-lgr.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSansCond-TextItalic-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSansCond-TextItalic-sup-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSansCond-TextItalic-tlf-lgr.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSansCond-TextItalic-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSansCond-TextItalic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSansCond-TextItalic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSansCond-Thin-sup-lgr.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSansCond-Thin-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSansCond-Thin-sup-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSansCond-Thin-tlf-lgr.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSansCond-Thin-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSansCond-Thin-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSansCond-Thin-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSansCond-ThinItalic-sup-lgr.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSansCond-ThinItalic-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSansCond-ThinItalic-sup-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSansCond-ThinItalic-tlf-lgr.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSansCond-ThinItalic-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSansCond-ThinItalic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSansCond-ThinItalic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSansCond-sup-lgr.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSansCond-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSansCond-sup-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSansCond-tlf-lgr.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSansCond-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSansCond-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSansCond-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSerif-Bold-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSerif-Bold-sup-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSerif-Bold-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSerif-Bold-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSerif-Bold-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSerif-BoldItalic-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSerif-BoldItalic-sup-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSerif-BoldItalic-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSerif-BoldItalic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSerif-BoldItalic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSerif-ExtraLight-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSerif-ExtraLight-sup-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSerif-ExtraLight-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSerif-ExtraLight-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSerif-ExtraLight-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSerif-ExtraLightItalic-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSerif-ExtraLightItalic-sup-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSerif-ExtraLightItalic-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSerif-ExtraLightItalic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSerif-ExtraLightItalic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSerif-Italic-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSerif-Italic-sup-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSerif-Italic-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSerif-Italic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSerif-Italic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSerif-Light-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSerif-Light-sup-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSerif-Light-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSerif-Light-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSerif-Light-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSerif-LightItalic-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSerif-LightItalic-sup-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSerif-LightItalic-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSerif-LightItalic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSerif-LightItalic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSerif-Medium-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSerif-Medium-sup-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSerif-Medium-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSerif-Medium-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSerif-Medium-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSerif-MediumItalic-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSerif-MediumItalic-sup-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSerif-MediumItalic-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSerif-MediumItalic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSerif-MediumItalic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSerif-SemiBold-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSerif-SemiBold-sup-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSerif-SemiBold-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSerif-SemiBold-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSerif-SemiBold-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSerif-SemiBoldItalic-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSerif-SemiBoldItalic-sup-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSerif-SemiBoldItalic-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSerif-SemiBoldItalic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSerif-SemiBoldItalic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSerif-Text-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSerif-Text-sup-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSerif-Text-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSerif-Text-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSerif-Text-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSerif-TextItalic-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSerif-TextItalic-sup-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSerif-TextItalic-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSerif-TextItalic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSerif-TextItalic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSerif-Thin-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSerif-Thin-sup-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSerif-Thin-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSerif-Thin-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSerif-Thin-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSerif-ThinItalic-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSerif-ThinItalic-sup-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSerif-ThinItalic-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSerif-ThinItalic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSerif-ThinItalic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSerif-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSerif-sup-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSerif-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSerif-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/ibm/plex/IBMPlexSerif-tlf-ts1.vf
%{_texmfdistdir}/tex/latex/plex/LGRIBMPlexSans-Sup.fd
%{_texmfdistdir}/tex/latex/plex/LGRIBMPlexSans-TLF.fd
%{_texmfdistdir}/tex/latex/plex/LY1IBMPlexMono-Sup.fd
%{_texmfdistdir}/tex/latex/plex/LY1IBMPlexMono-TLF.fd
%{_texmfdistdir}/tex/latex/plex/LY1IBMPlexSans-Sup.fd
%{_texmfdistdir}/tex/latex/plex/LY1IBMPlexSans-TLF.fd
%{_texmfdistdir}/tex/latex/plex/LY1IBMPlexSerif-Sup.fd
%{_texmfdistdir}/tex/latex/plex/LY1IBMPlexSerif-TLF.fd
%{_texmfdistdir}/tex/latex/plex/OT1IBMPlexMono-Sup.fd
%{_texmfdistdir}/tex/latex/plex/OT1IBMPlexMono-TLF.fd
%{_texmfdistdir}/tex/latex/plex/OT1IBMPlexSans-Sup.fd
%{_texmfdistdir}/tex/latex/plex/OT1IBMPlexSans-TLF.fd
%{_texmfdistdir}/tex/latex/plex/OT1IBMPlexSerif-Sup.fd
%{_texmfdistdir}/tex/latex/plex/OT1IBMPlexSerif-TLF.fd
%{_texmfdistdir}/tex/latex/plex/T1IBMPlexMono-Sup.fd
%{_texmfdistdir}/tex/latex/plex/T1IBMPlexMono-TLF.fd
%{_texmfdistdir}/tex/latex/plex/T1IBMPlexSans-Sup.fd
%{_texmfdistdir}/tex/latex/plex/T1IBMPlexSans-TLF.fd
%{_texmfdistdir}/tex/latex/plex/T1IBMPlexSerif-Sup.fd
%{_texmfdistdir}/tex/latex/plex/T1IBMPlexSerif-TLF.fd
%{_texmfdistdir}/tex/latex/plex/TS1IBMPlexMono-TLF.fd
%{_texmfdistdir}/tex/latex/plex/TS1IBMPlexSans-TLF.fd
%{_texmfdistdir}/tex/latex/plex/TS1IBMPlexSerif-TLF.fd
%{_texmfdistdir}/tex/latex/plex/plex-mono.sty
%{_texmfdistdir}/tex/latex/plex/plex-sans.sty
%{_texmfdistdir}/tex/latex/plex/plex-serif.sty

%files -n texlive-plex-fonts
%defattr(-,root,root,755)
%dir %{_datadir}/fonts/texlive-plex
%{_datadir}/fontconfig/conf.avail/58-texlive-plex.conf
%{_datadir}/fontconfig/conf.avail/55-texlive-plex.conf
%config %{_sysconfdir}/fonts/conf.d/55-texlive-plex.conf
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-plex/encodings.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-plex/fonts.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-plex/fonts.scale
%{_datadir}/fonts/texlive-plex/IBMPlexMono-Bold.otf
%{_datadir}/fonts/texlive-plex/IBMPlexMono-BoldItalic.otf
%{_datadir}/fonts/texlive-plex/IBMPlexMono-ExtraLight.otf
%{_datadir}/fonts/texlive-plex/IBMPlexMono-ExtraLightItalic.otf
%{_datadir}/fonts/texlive-plex/IBMPlexMono-Italic.otf
%{_datadir}/fonts/texlive-plex/IBMPlexMono-Light.otf
%{_datadir}/fonts/texlive-plex/IBMPlexMono-LightItalic.otf
%{_datadir}/fonts/texlive-plex/IBMPlexMono-Medium.otf
%{_datadir}/fonts/texlive-plex/IBMPlexMono-MediumItalic.otf
%{_datadir}/fonts/texlive-plex/IBMPlexMono-Regular.otf
%{_datadir}/fonts/texlive-plex/IBMPlexMono-SemiBold.otf
%{_datadir}/fonts/texlive-plex/IBMPlexMono-SemiBoldItalic.otf
%{_datadir}/fonts/texlive-plex/IBMPlexMono-Text.otf
%{_datadir}/fonts/texlive-plex/IBMPlexMono-TextItalic.otf
%{_datadir}/fonts/texlive-plex/IBMPlexMono-Thin.otf
%{_datadir}/fonts/texlive-plex/IBMPlexMono-ThinItalic.otf
%{_datadir}/fonts/texlive-plex/IBMPlexSans-Bold.otf
%{_datadir}/fonts/texlive-plex/IBMPlexSans-BoldItalic.otf
%{_datadir}/fonts/texlive-plex/IBMPlexSans-ExtraLight.otf
%{_datadir}/fonts/texlive-plex/IBMPlexSans-ExtraLightItalic.otf
%{_datadir}/fonts/texlive-plex/IBMPlexSans-Italic.otf
%{_datadir}/fonts/texlive-plex/IBMPlexSans-Light.otf
%{_datadir}/fonts/texlive-plex/IBMPlexSans-LightItalic.otf
%{_datadir}/fonts/texlive-plex/IBMPlexSans-Medium.otf
%{_datadir}/fonts/texlive-plex/IBMPlexSans-MediumItalic.otf
%{_datadir}/fonts/texlive-plex/IBMPlexSans-Regular.otf
%{_datadir}/fonts/texlive-plex/IBMPlexSans-SemiBold.otf
%{_datadir}/fonts/texlive-plex/IBMPlexSans-SemiBoldItalic.otf
%{_datadir}/fonts/texlive-plex/IBMPlexSans-Text.otf
%{_datadir}/fonts/texlive-plex/IBMPlexSans-TextItalic.otf
%{_datadir}/fonts/texlive-plex/IBMPlexSans-Thin.otf
%{_datadir}/fonts/texlive-plex/IBMPlexSans-ThinItalic.otf
%{_datadir}/fonts/texlive-plex/IBMPlexSansCondensed-Bold.otf
%{_datadir}/fonts/texlive-plex/IBMPlexSansCondensed-BoldItalic.otf
%{_datadir}/fonts/texlive-plex/IBMPlexSansCondensed-ExtraLight.otf
%{_datadir}/fonts/texlive-plex/IBMPlexSansCondensed-ExtraLightItalic.otf
%{_datadir}/fonts/texlive-plex/IBMPlexSansCondensed-Italic.otf
%{_datadir}/fonts/texlive-plex/IBMPlexSansCondensed-Light.otf
%{_datadir}/fonts/texlive-plex/IBMPlexSansCondensed-LightItalic.otf
%{_datadir}/fonts/texlive-plex/IBMPlexSansCondensed-Medium.otf
%{_datadir}/fonts/texlive-plex/IBMPlexSansCondensed-MediumItalic.otf
%{_datadir}/fonts/texlive-plex/IBMPlexSansCondensed-Regular.otf
%{_datadir}/fonts/texlive-plex/IBMPlexSansCondensed-SemiBold.otf
%{_datadir}/fonts/texlive-plex/IBMPlexSansCondensed-SemiBoldItalic.otf
%{_datadir}/fonts/texlive-plex/IBMPlexSansCondensed-Text.otf
%{_datadir}/fonts/texlive-plex/IBMPlexSansCondensed-TextItalic.otf
%{_datadir}/fonts/texlive-plex/IBMPlexSansCondensed-Thin.otf
%{_datadir}/fonts/texlive-plex/IBMPlexSansCondensed-ThinItalic.otf
%{_datadir}/fonts/texlive-plex/IBMPlexSerif-Bold.otf
%{_datadir}/fonts/texlive-plex/IBMPlexSerif-BoldItalic.otf
%{_datadir}/fonts/texlive-plex/IBMPlexSerif-ExtraLight.otf
%{_datadir}/fonts/texlive-plex/IBMPlexSerif-ExtraLightItalic.otf
%{_datadir}/fonts/texlive-plex/IBMPlexSerif-Italic.otf
%{_datadir}/fonts/texlive-plex/IBMPlexSerif-Light.otf
%{_datadir}/fonts/texlive-plex/IBMPlexSerif-LightItalic.otf
%{_datadir}/fonts/texlive-plex/IBMPlexSerif-Medium.otf
%{_datadir}/fonts/texlive-plex/IBMPlexSerif-MediumItalic.otf
%{_datadir}/fonts/texlive-plex/IBMPlexSerif-Regular.otf
%{_datadir}/fonts/texlive-plex/IBMPlexSerif-SemiBold.otf
%{_datadir}/fonts/texlive-plex/IBMPlexSerif-SemiBoldItalic.otf
%{_datadir}/fonts/texlive-plex/IBMPlexSerif-Text.otf
%{_datadir}/fonts/texlive-plex/IBMPlexSerif-TextItalic.otf
%{_datadir}/fonts/texlive-plex/IBMPlexSerif-Thin.otf
%{_datadir}/fonts/texlive-plex/IBMPlexSerif-ThinItalic.otf
%{_datadir}/fonts/texlive-plex/IBMPlexMono-Bold.pfb
%{_datadir}/fonts/texlive-plex/IBMPlexMono-BoldItalic.pfb
%{_datadir}/fonts/texlive-plex/IBMPlexMono-ExtraLight.pfb
%{_datadir}/fonts/texlive-plex/IBMPlexMono-ExtraLightItalic.pfb
%{_datadir}/fonts/texlive-plex/IBMPlexMono-Italic.pfb
%{_datadir}/fonts/texlive-plex/IBMPlexMono-Light.pfb
%{_datadir}/fonts/texlive-plex/IBMPlexMono-LightItalic.pfb
%{_datadir}/fonts/texlive-plex/IBMPlexMono-Medium.pfb
%{_datadir}/fonts/texlive-plex/IBMPlexMono-MediumItalic.pfb
%{_datadir}/fonts/texlive-plex/IBMPlexMono-SemiBold.pfb
%{_datadir}/fonts/texlive-plex/IBMPlexMono-SemiBoldItalic.pfb
%{_datadir}/fonts/texlive-plex/IBMPlexMono-Text.pfb
%{_datadir}/fonts/texlive-plex/IBMPlexMono-TextItalic.pfb
%{_datadir}/fonts/texlive-plex/IBMPlexMono-Thin.pfb
%{_datadir}/fonts/texlive-plex/IBMPlexMono-ThinItalic.pfb
%{_datadir}/fonts/texlive-plex/IBMPlexMono.pfb
%{_datadir}/fonts/texlive-plex/IBMPlexSans-Bold.pfb
%{_datadir}/fonts/texlive-plex/IBMPlexSans-BoldItalic.pfb
%{_datadir}/fonts/texlive-plex/IBMPlexSans-ExtraLight.pfb
%{_datadir}/fonts/texlive-plex/IBMPlexSans-ExtraLightItalic.pfb
%{_datadir}/fonts/texlive-plex/IBMPlexSans-Italic.pfb
%{_datadir}/fonts/texlive-plex/IBMPlexSans-Light.pfb
%{_datadir}/fonts/texlive-plex/IBMPlexSans-LightItalic.pfb
%{_datadir}/fonts/texlive-plex/IBMPlexSans-Medium.pfb
%{_datadir}/fonts/texlive-plex/IBMPlexSans-MediumItalic.pfb
%{_datadir}/fonts/texlive-plex/IBMPlexSans-SemiBold.pfb
%{_datadir}/fonts/texlive-plex/IBMPlexSans-SemiBoldItalic.pfb
%{_datadir}/fonts/texlive-plex/IBMPlexSans-Text.pfb
%{_datadir}/fonts/texlive-plex/IBMPlexSans-TextItalic.pfb
%{_datadir}/fonts/texlive-plex/IBMPlexSans-Thin.pfb
%{_datadir}/fonts/texlive-plex/IBMPlexSans-ThinItalic.pfb
%{_datadir}/fonts/texlive-plex/IBMPlexSans.pfb
%{_datadir}/fonts/texlive-plex/IBMPlexSansCond-Bold.pfb
%{_datadir}/fonts/texlive-plex/IBMPlexSansCond-BoldItalic.pfb
%{_datadir}/fonts/texlive-plex/IBMPlexSansCond-ExtraLight.pfb
%{_datadir}/fonts/texlive-plex/IBMPlexSansCond-ExtraLightItalic.pfb
%{_datadir}/fonts/texlive-plex/IBMPlexSansCond-Italic.pfb
%{_datadir}/fonts/texlive-plex/IBMPlexSansCond-Light.pfb
%{_datadir}/fonts/texlive-plex/IBMPlexSansCond-LightItalic.pfb
%{_datadir}/fonts/texlive-plex/IBMPlexSansCond-Medium.pfb
%{_datadir}/fonts/texlive-plex/IBMPlexSansCond-MediumItalic.pfb
%{_datadir}/fonts/texlive-plex/IBMPlexSansCond-SemiBold.pfb
%{_datadir}/fonts/texlive-plex/IBMPlexSansCond-SemiBoldItalic.pfb
%{_datadir}/fonts/texlive-plex/IBMPlexSansCond-Text.pfb
%{_datadir}/fonts/texlive-plex/IBMPlexSansCond-TextItalic.pfb
%{_datadir}/fonts/texlive-plex/IBMPlexSansCond-Thin.pfb
%{_datadir}/fonts/texlive-plex/IBMPlexSansCond-ThinItalic.pfb
%{_datadir}/fonts/texlive-plex/IBMPlexSansCond.pfb
%{_datadir}/fonts/texlive-plex/IBMPlexSerif-Bold.pfb
%{_datadir}/fonts/texlive-plex/IBMPlexSerif-BoldItalic.pfb
%{_datadir}/fonts/texlive-plex/IBMPlexSerif-ExtraLight.pfb
%{_datadir}/fonts/texlive-plex/IBMPlexSerif-ExtraLightItalic.pfb
%{_datadir}/fonts/texlive-plex/IBMPlexSerif-Italic.pfb
%{_datadir}/fonts/texlive-plex/IBMPlexSerif-Light.pfb
%{_datadir}/fonts/texlive-plex/IBMPlexSerif-LightItalic.pfb
%{_datadir}/fonts/texlive-plex/IBMPlexSerif-Medium.pfb
%{_datadir}/fonts/texlive-plex/IBMPlexSerif-MediumItalic.pfb
%{_datadir}/fonts/texlive-plex/IBMPlexSerif-SemiBold.pfb
%{_datadir}/fonts/texlive-plex/IBMPlexSerif-SemiBoldItalic.pfb
%{_datadir}/fonts/texlive-plex/IBMPlexSerif-Text.pfb
%{_datadir}/fonts/texlive-plex/IBMPlexSerif-TextItalic.pfb
%{_datadir}/fonts/texlive-plex/IBMPlexSerif-Thin.pfb
%{_datadir}/fonts/texlive-plex/IBMPlexSerif-ThinItalic.pfb
%{_datadir}/fonts/texlive-plex/IBMPlexSerif.pfb

%package -n texlive-plex-otf
Version:        %{texlive_version}.%{texlive_noarch}.0.0.07asvn47562
Release:        0
License:        LPPL-1.0
Summary:        Support for the OpenType font IBM Plex
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-plex-otf-doc >= %{texlive_version}
Provides:       tex(plex-otf.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xkeyval.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source18:       plex-otf.tar.xz
Source19:       plex-otf.doc.tar.xz

%description -n texlive-plex-otf
This package supports the free otf fonts from the IBM Plex
project which are available from GitHub or already part of your
system (Windows/Linux/...). This package supports only XeLaTeX
or LuaLaTeX; for pdfLaTeX use plex-mono.sty, plex-sans.sty,
and/or plex-serif.sty from the plex package. IBM Plex has no
math symbols. You will have to use one of the existing math
fonts if you need them.

%package -n texlive-plex-otf-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.07asvn47562
Release:        0
Summary:        Documentation for texlive-plex-otf
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/

%description -n texlive-plex-otf-doc
This package includes the documentation for texlive-plex-otf

%post -n texlive-plex-otf
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-plex-otf
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-plex-otf
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-plex-otf-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/plex-otf/Changes
%{_texmfdistdir}/doc/fonts/plex-otf/Examples/plex-otf-1.tex
%{_texmfdistdir}/doc/fonts/plex-otf/Examples/plex-otf-10.tex
%{_texmfdistdir}/doc/fonts/plex-otf/Examples/plex-otf-11.tex
%{_texmfdistdir}/doc/fonts/plex-otf/Examples/plex-otf-2.tex
%{_texmfdistdir}/doc/fonts/plex-otf/Examples/plex-otf-3.tex
%{_texmfdistdir}/doc/fonts/plex-otf/Examples/plex-otf-4.tex
%{_texmfdistdir}/doc/fonts/plex-otf/Examples/plex-otf-5.tex
%{_texmfdistdir}/doc/fonts/plex-otf/Examples/plex-otf-6.tex
%{_texmfdistdir}/doc/fonts/plex-otf/Examples/plex-otf-7.tex
%{_texmfdistdir}/doc/fonts/plex-otf/Examples/plex-otf-8.tex
%{_texmfdistdir}/doc/fonts/plex-otf/Examples/plex-otf-9.tex
%{_texmfdistdir}/doc/fonts/plex-otf/README.md
%{_texmfdistdir}/doc/fonts/plex-otf/plex-otf-doc.bib
%{_texmfdistdir}/doc/fonts/plex-otf/plex-otf-doc.fonts
%{_texmfdistdir}/doc/fonts/plex-otf/plex-otf-doc.pdf
%{_texmfdistdir}/doc/fonts/plex-otf/plex-otf-doc.tex

%files -n texlive-plex-otf
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/plex-otf/plex-otf.sty

%package -n texlive-plimsoll
Version:        %{texlive_version}.%{texlive_noarch}.1svn56605
Release:        0
License:        GPL-2.0-or-later
Summary:        Fonts with the Plimsoll symbol and LaTeX support
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(updmap.cfg)
#!BuildIgnore:  tex(updmap.cfg)
Requires(postun):findutils
Requires(postun):grep
Requires(postun):sed
Requires(postun):texlive >= %{texlive_version}
Requires(postun):tex(updmap.cfg)
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Requires:       texlive-plimsoll-fonts >= %{texlive_version}
Suggests:       texlive-plimsoll-doc >= %{texlive_version}
Provides:       tex(plimsoll-sans.tfm)
Provides:       tex(plimsoll.enc)
Provides:       tex(plimsoll.map)
Provides:       tex(plimsoll.sty)
Provides:       tex(plimsoll.tfm)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source20:       plimsoll.tar.xz
Source21:       plimsoll.doc.tar.xz

%description -n texlive-plimsoll
This package provides access to the Plimsoll symbol for use
with LaTeX. The Plimsoll symbol is sometimes used in chemistry
for denoting standard states and values. The LaTeX package
provides access to this notation as well. The syntax for
denoting the standard state is the same as suggested in the
Comprehensive LaTeX Symbol List for emulating the Plimsoll
mark.

%package -n texlive-plimsoll-doc
Version:        %{texlive_version}.%{texlive_noarch}.1svn56605
Release:        0
Summary:        Documentation for texlive-plimsoll
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/

%description -n texlive-plimsoll-doc
This package includes the documentation for texlive-plimsoll

%package -n texlive-plimsoll-fonts
Version:        %{texlive_version}.%{texlive_noarch}.1svn56605
Release:        0
Summary:        Severed fonts for texlive-plimsoll
License:        GPL-2.0-or-later
URL:            https://www.tug.org/texlive/
Group:          Productivity/Publishing/TeX/Fonts
%reconfigure_fonts_prereq
Requires(posttrans):fontconfig
Requires(posttrans):ghostscript-fonts-std
Requires(posttrans):mkfontdir
Requires(posttrans):mkfontscale
Requires(posttrans):xorg-x11-fonts-core

%description -n texlive-plimsoll-fonts
The  separated fonts package for texlive-plimsoll

%post -n texlive-plimsoll
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
echo 'addMap plimsoll.map' >> /var/run/texlive/run-updmap

%postun -n texlive-plimsoll
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    echo 'deleteMap plimsoll.map' >> /var/run/texlive/run-updmap
    exit 0
fi

%posttrans -n texlive-plimsoll
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-plimsoll-fonts

%files -n texlive-plimsoll-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/plimsoll/LICENSE
%{_texmfdistdir}/doc/fonts/plimsoll/README
%{_texmfdistdir}/doc/fonts/plimsoll/plimsoll.pdf
%{_texmfdistdir}/doc/fonts/plimsoll/plimsoll.tex

%files -n texlive-plimsoll
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/afm/public/plimsoll/plimsoll-sans.afm
%{_texmfdistdir}/fonts/afm/public/plimsoll/plimsoll.afm
%{_texmfdistdir}/fonts/enc/dvips/plimsoll/plimsoll.enc
%{_texmfdistdir}/fonts/map/dvips/plimsoll/plimsoll.map
%{_texmfdistdir}/fonts/tfm/public/plimsoll/plimsoll-sans.tfm
%{_texmfdistdir}/fonts/tfm/public/plimsoll/plimsoll.tfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/plimsoll/plimsoll-sans.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/plimsoll/plimsoll.pfb
%{_texmfdistdir}/tex/latex/plimsoll/plimsoll.sty

%files -n texlive-plimsoll-fonts
%defattr(-,root,root,755)
%dir %{_datadir}/fonts/texlive-plimsoll
%{_datadir}/fontconfig/conf.avail/58-texlive-plimsoll.conf
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-plimsoll/encodings.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-plimsoll/fonts.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-plimsoll/fonts.scale
%{_datadir}/fonts/texlive-plimsoll/plimsoll-sans.pfb
%{_datadir}/fonts/texlive-plimsoll/plimsoll.pfb

%package -n texlive-plipsum
Version:        %{texlive_version}.%{texlive_noarch}.4.3svn30353
Release:        0
License:        LPPL-1.0
Summary:        'Lorem ipsum' for Plain TeX developers
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-plipsum-doc >= %{texlive_version}
Provides:       tex(plipsum.tex)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source22:       plipsum.tar.xz
Source23:       plipsum.doc.tar.xz

%description -n texlive-plipsum
The package provides a paragraph generator designed for use in
Plain TeX documents. The paragraphs generated contain many
'f-groups' (ff, fl etc.) so the text can act as a test of the
ligatures of the font in use.

%package -n texlive-plipsum-doc
Version:        %{texlive_version}.%{texlive_noarch}.4.3svn30353
Release:        0
Summary:        Documentation for texlive-plipsum
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/

%description -n texlive-plipsum-doc
This package includes the documentation for texlive-plipsum

%post -n texlive-plipsum
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-plipsum
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-plipsum
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-plipsum-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/plain/plipsum/README
%{_texmfdistdir}/doc/plain/plipsum/compile.sh
%{_texmfdistdir}/doc/plain/plipsum/plipsum-doc.pdf
%{_texmfdistdir}/doc/plain/plipsum/plipsum.nw
%{_texmfdistdir}/doc/plain/plipsum/pliptest.tex
%{_texmfdistdir}/doc/plain/plipsum/stripc

%files -n texlive-plipsum
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/plain/plipsum/plipsum.tex

%package -n texlive-plnfss
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn15878
Release:        0
License:        LPPL-1.0
Summary:        Font selection for Plain TeX
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-plnfss-doc >= %{texlive_version}
Provides:       tex(MIKmathf.tex)
Provides:       tex(plnfss.tex)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source24:       plnfss.tar.xz
Source25:       plnfss.doc.tar.xz

%description -n texlive-plnfss
Plnfss is a set of macros to provide easy font access (somewhat
similar to NFSS but with some limitations) with Plain TeX.
Plnfss can automatically make use of PSNFSS fd files, i.e.,
when an Adobe Type 1 is used the relevant fd file will be
loaded automatically. For cmr-like fonts (ec, vnr, csr or plr
fonts), a special format called pfd (plain fd) is required and
must be loaded manually. See ot1cmr.pfd for further
information.

%package -n texlive-plnfss-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn15878
Release:        0
Summary:        Documentation for texlive-plnfss
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/

%description -n texlive-plnfss-doc
This package includes the documentation for texlive-plnfss

%post -n texlive-plnfss
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-plnfss
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-plnfss
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-plnfss-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/plain/plnfss/LPPL.txt
%{_texmfdistdir}/doc/plain/plnfss/plnfss.txt
%{_texmfdistdir}/doc/plain/plnfss/test-plnfss.tex

%files -n texlive-plnfss
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/plain/plnfss/MIKmathf.tex
%{_texmfdistdir}/tex/plain/plnfss/ams.pfd
%{_texmfdistdir}/tex/plain/plnfss/il2cm.pfd
%{_texmfdistdir}/tex/plain/plnfss/il2cmr.pfd
%{_texmfdistdir}/tex/plain/plnfss/ly1lm.pfd
%{_texmfdistdir}/tex/plain/plnfss/ot1cm.pfd
%{_texmfdistdir}/tex/plain/plnfss/ot1cmr.pfd
%{_texmfdistdir}/tex/plain/plnfss/ot4cm.pfd
%{_texmfdistdir}/tex/plain/plnfss/plnfss.tex
%{_texmfdistdir}/tex/plain/plnfss/qxlm.pfd
%{_texmfdistdir}/tex/plain/plnfss/t1lm.pfd
%{_texmfdistdir}/tex/plain/plnfss/t5cm.pfd
%{_texmfdistdir}/tex/plain/plnfss/t5cmr.pfd
%{_texmfdistdir}/tex/plain/plnfss/t5lm.pfd
%{_texmfdistdir}/tex/plain/plnfss/ts1lm.pfd

%package -n texlive-plstmary
Version:        %{texlive_version}.%{texlive_noarch}.0.0.5csvn31088
Release:        0
License:        SUSE-Public-Domain
Summary:        St. Mary's Road font support for plain TeX
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-plstmary-doc >= %{texlive_version}
Provides:       tex(stmary.tex)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source26:       plstmary.tar.xz
Source27:       plstmary.doc.tar.xz

%description -n texlive-plstmary
The package provides commands to produce all the symbols of the
St Mary's Road fonts, in a Plain TeX environment.

%package -n texlive-plstmary-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.5csvn31088
Release:        0
Summary:        Documentation for texlive-plstmary
License:        SUSE-Public-Domain
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/

%description -n texlive-plstmary-doc
This package includes the documentation for texlive-plstmary

%post -n texlive-plstmary
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-plstmary
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-plstmary
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-plstmary-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/plain/plstmary/README
%{_texmfdistdir}/doc/plain/plstmary/plstmary-doc.pdf
%{_texmfdistdir}/doc/plain/plstmary/plstmary-doc.tex

%files -n texlive-plstmary
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/plain/plstmary/stmary.tex

%package -n texlive-plweb
Version:        %{texlive_version}.%{texlive_noarch}.3.0svn15878
Release:        0
License:        LPPL-1.0
Summary:        Literate Programming for Prolog with LaTeX
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-plweb-doc >= %{texlive_version}
Provides:       tex(pcode.sty)
Provides:       tex(pl.cfg)
Provides:       tex(pl.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source28:       plweb.tar.xz
Source29:       plweb.doc.tar.xz

%description -n texlive-plweb
Instead of having to transform the common source into program
or documentation, the central idea was to develop a method to
have one common source which can be interpreted by a Prolog
system as well as by LaTeX, whether that Prolog system be
C-Prolog, Quintus-Prolog, or ECLiPSe.

%package -n texlive-plweb-doc
Version:        %{texlive_version}.%{texlive_noarch}.3.0svn15878
Release:        0
Summary:        Documentation for texlive-plweb
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/

%description -n texlive-plweb-doc
This package includes the documentation for texlive-plweb

%post -n texlive-plweb
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-plweb
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-plweb
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-plweb-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/plweb/README
%{_texmfdistdir}/doc/latex/plweb/pl.pdf
%{_texmfdistdir}/doc/latex/plweb/pl.tex
%{_texmfdistdir}/doc/latex/plweb/sample.pl

%files -n texlive-plweb
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/plweb/pcode.sty
%{_texmfdistdir}/tex/latex/plweb/pl.cfg
%{_texmfdistdir}/tex/latex/plweb/pl.sty

%package -n texlive-pm-isomath
Version:        %{texlive_version}.%{texlive_noarch}.1.2.00svn60368
Release:        0
License:        LPPL-1.0
Summary:        Poor man ISO math for pdfLaTeX users
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-pm-isomath-doc >= %{texlive_version}
Provides:       tex(pm-isomath.sty)
Requires:       tex(alphabeta.sty)
Requires:       tex(amsmath.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(iftex.sty)
Requires:       tex(xparse.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source30:       pm-isomath.tar.xz
Source31:       pm-isomath.doc.tar.xz

%description -n texlive-pm-isomath
This small package realizes a poor man approximation of the ISO
regulations for physical sciences and technology. Contrary to
other more elegant solutions, it does not load any math
alphabet, since pdfLaTeX can use only a maximum of such
alphabets. The necessary user macros are defined for typsetting
common math symbols that require special ISO treatment.

%package -n texlive-pm-isomath-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.2.00svn60368
Release:        0
Summary:        Documentation for texlive-pm-isomath
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/

%description -n texlive-pm-isomath-doc
This package includes the documentation for texlive-pm-isomath

%post -n texlive-pm-isomath
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pm-isomath
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pm-isomath
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pm-isomath-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/pm-isomath/README.txt
%{_texmfdistdir}/doc/latex/pm-isomath/pm-isomath.pdf

%files -n texlive-pm-isomath
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/pm-isomath/pm-isomath.sty

%package -n texlive-pmboxdraw
Version:        %{texlive_version}.%{texlive_noarch}.1.4svn53046
Release:        0
License:        LPPL-1.0
Summary:        Poor man's box drawing characters
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-pmboxdraw-doc >= %{texlive_version}
Provides:       tex(pmboxdraw.sty)
Requires:       tex(kvoptions.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source32:       pmboxdraw.tar.xz
Source33:       pmboxdraw.doc.tar.xz

%description -n texlive-pmboxdraw
This package declares box drawing characters of old code pages,
e.g. cp437. It uses rules instead of using a font.

%package -n texlive-pmboxdraw-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.4svn53046
Release:        0
Summary:        Documentation for texlive-pmboxdraw
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/

%description -n texlive-pmboxdraw-doc
This package includes the documentation for texlive-pmboxdraw

%post -n texlive-pmboxdraw
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pmboxdraw
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pmboxdraw
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pmboxdraw-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/pmboxdraw/README.md
%{_texmfdistdir}/doc/latex/pmboxdraw/pmboxdraw.pdf

%files -n texlive-pmboxdraw
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/pmboxdraw/pmboxdraw.sty
%{_texmfdistdir}/tex/latex/pmboxdraw/pmboxdrawenc.dfu

%package -n texlive-pmgraph
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn15878
Release:        0
License:        GPL-2.0-or-later
Summary:        "Poor man's" graphics
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-pmgraph-doc >= %{texlive_version}
Provides:       tex(pmgraph.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source34:       pmgraph.tar.xz
Source35:       pmgraph.doc.tar.xz

%description -n texlive-pmgraph
A set of extensions to LaTeX picture environment, including a
wider range of vectors, and a lot more box frame styles.

%package -n texlive-pmgraph-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn15878
Release:        0
Summary:        Documentation for texlive-pmgraph
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/

%description -n texlive-pmgraph-doc
This package includes the documentation for texlive-pmgraph

%post -n texlive-pmgraph
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pmgraph
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pmgraph
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pmgraph-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/pmgraph/COPYING
%{_texmfdistdir}/doc/latex/pmgraph/README
%{_texmfdistdir}/doc/latex/pmgraph/pmgraph.pdf
%{_texmfdistdir}/doc/latex/pmgraph/pmgraph.tex

%files -n texlive-pmgraph
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/pmgraph/pmgraph.sty

%package -n texlive-pmhanguljamo
Version:        %{texlive_version}.%{texlive_noarch}.0.0.4svn61183
Release:        0
License:        LPPL-1.0
Summary:        Poor man's Hangul Jamo input method
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-pmhanguljamo-doc >= %{texlive_version}
Provides:       tex(pmhanguljamo-rrk.sty)
Provides:       tex(pmhanguljamo.sty)
Requires:       tex(l3keys2e.sty)
Requires:       tex(xparse.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source36:       pmhanguljamo.tar.xz
Source37:       pmhanguljamo.doc.tar.xz

%description -n texlive-pmhanguljamo
This package provides a Hangul transliteration input method
that allows to typeset Korean letters (Hangul) using the proper
fonts. The name is derived from "Poor man's Hangul Jamo Input
Method". The use of XeLaTeX is recommended. pdfTeX is not
supported.

%package -n texlive-pmhanguljamo-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.4svn61183
Release:        0
Summary:        Documentation for texlive-pmhanguljamo
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Provides:       locale(texlive-pmhanguljamo-doc:ko)

%description -n texlive-pmhanguljamo-doc
This package includes the documentation for texlive-pmhanguljamo

%post -n texlive-pmhanguljamo
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pmhanguljamo
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pmhanguljamo
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pmhanguljamo-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/pmhanguljamo/README.md
%{_texmfdistdir}/doc/latex/pmhanguljamo/munjangganghwa.jpg
%{_texmfdistdir}/doc/latex/pmhanguljamo/pmhanguljamo-doc.pdf
%{_texmfdistdir}/doc/latex/pmhanguljamo/pmhanguljamo-doc.tex
%{_texmfdistdir}/doc/latex/pmhanguljamo/pmhanguljamo-kdoc.pdf
%{_texmfdistdir}/doc/latex/pmhanguljamo/pmhanguljamo-kdoc.tex

%files -n texlive-pmhanguljamo
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/pmhanguljamo/pmhanguljamo-rrk.sty
%{_texmfdistdir}/tex/latex/pmhanguljamo/pmhanguljamo.sty

%package -n texlive-pmx
Version:        %{texlive_version}.%{texlive_noarch}.2.98asvn62533
Release:        0
License:        GPL-2.0-or-later
Summary:        Preprocessor for MusiXTeX
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-pmx-bin >= %{texlive_version}
#!BuildIgnore: texlive-pmx-bin
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-pmx-doc >= %{texlive_version}
Provides:       tex(pmx.tex)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source38:       pmx.tar.xz
Source39:       pmx.doc.tar.xz

%description -n texlive-pmx
PMX provides a preprocessor for MusiXTeX. pmxab builds a TeX
input file based on a .pmx input file in a much simpler
language, making most of the layout decisions by itself. It has
most of MusiXTeX's functionality, but it also permits in-line
TeX to give access to virtually all of MusiXTeX. For
proof-listening, pmxab will make a MIDI file of your score.
scor2prt is an auxiliary program that makes parts from a score.

%package -n texlive-pmx-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.98asvn62533
Release:        0
Summary:        Documentation for texlive-pmx
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Provides:       man(pmxab.1)
Provides:       man(scor2prt.1)

%description -n texlive-pmx-doc
This package includes the documentation for texlive-pmx

%post -n texlive-pmx
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pmx
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pmx
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pmx-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/pmx/ChangeLog
%{_texmfdistdir}/doc/generic/pmx/README
%{_texmfdistdir}/doc/generic/pmx/accents.eps
%{_texmfdistdir}/doc/generic/pmx/examples/barsant.pmx
%{_texmfdistdir}/doc/generic/pmx/examples/dyntest.pmx
%{_texmfdistdir}/doc/generic/pmx/examples/most.pmx
%{_texmfdistdir}/doc/generic/pmx/examples/mwalmnd.pmx
%{_texmfdistdir}/doc/generic/pmx/examples/netsoos.pmx
%{_texmfdistdir}/doc/generic/pmx/examples/prad5x.pmx
%{_texmfdistdir}/doc/generic/pmx/examples/staffcrossall.pmx
%{_texmfdistdir}/doc/generic/pmx/file600.eps
%{_texmfdistdir}/doc/generic/pmx/gapxmpl.eps
%{_texmfdistdir}/doc/generic/pmx/gpl.txt
%{_texmfdistdir}/doc/generic/pmx/pmx-install.pdf
%{_texmfdistdir}/doc/generic/pmx/pmx-install.tex
%{_texmfdistdir}/doc/generic/pmx/pmx298.pdf
%{_texmfdistdir}/doc/generic/pmx/pmx298.tex
%{_texmfdistdir}/doc/generic/pmx/pmxab.pdf
%{_texmfdistdir}/doc/generic/pmx/ref298.pdf
%{_texmfdistdir}/doc/generic/pmx/ref298.tex
%{_texmfdistdir}/doc/generic/pmx/scor2prt.pdf
%{_texmfdistdir}/doc/generic/pmx/sjb291.eps
%{_texmfdistdir}/doc/generic/pmx/tremxmpl4.eps
%{_mandir}/man1/pmxab.1*
%{_mandir}/man1/scor2prt.1*

%files -n texlive-pmx
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/pmx/pmx.tex

%package -n texlive-pmxchords
Version:        %{texlive_version}.%{texlive_noarch}.2.0.2svn39249
Release:        0
License:        GPL-2.0-or-later
Summary:        Produce chord information to go with pmx output
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-pmxchords-bin >= %{texlive_version}
#!BuildIgnore: texlive-pmxchords-bin
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-pmxchords-doc >= %{texlive_version}
Provides:       tex(chords.tex)
Provides:       tex(chordsCZ.tex)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source40:       pmxchords.tar.xz
Source41:       pmxchords.doc.tar.xz

%description -n texlive-pmxchords
The bundle supplements pmx, providing the means of typesetting
chords above the notes of a score. The bundle contains: macros
for typing the chords; a Lua script to transpose chord macros
to the required key signature; and support scripts for common
requirements.

%package -n texlive-pmxchords-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.0.2svn39249
Release:        0
Summary:        Documentation for texlive-pmxchords
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Provides:       locale(texlive-pmxchords-doc:en;cs)
Provides:       man(pmxchords.1)

%description -n texlive-pmxchords-doc
This package includes the documentation for texlive-pmxchords

%post -n texlive-pmxchords
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pmxchords
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pmxchords
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pmxchords-doc
%defattr(-,root,root,755)
%{_mandir}/man1/pmxchords.1*
%{_texmfdistdir}/doc/pmxchords/README
%{_texmfdistdir}/doc/pmxchords/chordsRef.pdf
%{_texmfdistdir}/doc/pmxchords/chordsRef.tex
%{_texmfdistdir}/doc/pmxchords/chordsRefCZ.pdf
%{_texmfdistdir}/doc/pmxchords/chordsRefCZ.tex
%{_texmfdistdir}/doc/pmxchords/examples/jazz/misty/misty.pdf
%{_texmfdistdir}/doc/pmxchords/examples/jazz/misty/misty.pmx
%{_texmfdistdir}/doc/pmxchords/examples/jazz/schema/schema.pdf
%{_texmfdistdir}/doc/pmxchords/examples/jazz/schema/schema.pmx
%{_texmfdistdir}/doc/pmxchords/examples/jazz/schema/schema_full.pdf
%{_texmfdistdir}/doc/pmxchords/examples/jazz/schema/schema_full.pmx
%{_texmfdistdir}/doc/pmxchords/examples/noel/aj_co_to_hlasaju/aj_co_to_hlasaju.pdf
%{_texmfdistdir}/doc/pmxchords/examples/noel/aj_co_to_hlasaju/aj_co_to_hlasaju.pmx
%{_texmfdistdir}/doc/pmxchords/examples/noel/pasli_ovce_valasi/README
%{_texmfdistdir}/doc/pmxchords/examples/noel/pasli_ovce_valasi/pasli_ovce_valasi.pdf
%{_texmfdistdir}/doc/pmxchords/examples/noel/pasli_ovce_valasi/pasli_ovce_valasi.pmx
%{_texmfdistdir}/doc/pmxchords/gpl-2.0.txt
%{_texmfdistdir}/doc/pmxchords/pmxchords-install.pdf
%{_texmfdistdir}/doc/pmxchords/pmxchords-install.tex

%files -n texlive-pmxchords
%defattr(-,root,root,755)
%{_texmfdistdir}/scripts/pmxchords/ChordsTr.lua
%{_texmfdistdir}/scripts/pmxchords/pmxchords.lua
%{_texmfdistdir}/tex/generic/pmxchords/chords.tex
%{_texmfdistdir}/tex/generic/pmxchords/chordsCZ.tex

%package -n texlive-pnas2009
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn16287
Release:        0
License:        LPPL-1.0
Summary:        BibTeX style for PNAS (newer version)
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source42:       pnas2009.tar.xz

%description -n texlive-pnas2009
This style produces bibliographies in the format of
"Proceedings of the National Academy of Sciences, USA". The
style was derived from the standard unsrt.bst and adapted to
the new (2009) formatting rules.

%post -n texlive-pnas2009
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pnas2009
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pnas2009
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pnas2009
%defattr(-,root,root,755)
%{_texmfdistdir}/bibtex/bst/pnas2009/pnas2009.bst

%package -n texlive-poemscol
Version:        %{texlive_version}.%{texlive_noarch}.3.1415926svn56082
Release:        0
License:        LPPL-1.0
Summary:        Typesetting Critical Editions of Poetry
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-poemscol-doc >= %{texlive_version}
Provides:       tex(poemscol.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source43:       poemscol.tar.xz
Source44:       poemscol.doc.tar.xz

%description -n texlive-poemscol
The package offers LaTeX macros for typesetting critical
editions of poetry. Its features include automatic
linenumbering, generation of separate endnotes sections for
emendations, textual collations, and explanatory notes, special
marking for cases in which page breaks occur during stanza
breaks, running headers of the form 'Notes to pp. xx-yy' for
the notes sections, index of titles and first lines, and
automatic generation of a table of contents.

%package -n texlive-poemscol-doc
Version:        %{texlive_version}.%{texlive_noarch}.3.1415926svn56082
Release:        0
Summary:        Documentation for texlive-poemscol
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/

%description -n texlive-poemscol-doc
This package includes the documentation for texlive-poemscol

%post -n texlive-poemscol
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-poemscol
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-poemscol
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-poemscol-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/poemscol/README
%{_texmfdistdir}/doc/latex/poemscol/poemscol.pdf
%{_texmfdistdir}/doc/latex/poemscol/poemscolcheatsheet.pdf
%{_texmfdistdir}/doc/latex/poemscol/poemscolcheatsheet.tex

%files -n texlive-poemscol
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/poemscol/poemscol.sty

%package -n texlive-poetry
Version:        %{texlive_version}.%{texlive_noarch}.2.2svn53129
Release:        0
License:        LPPL-1.0
Summary:        Facilities for typesetting poetry and poetical structure
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-poetry-doc >= %{texlive_version}
Provides:       tex(poetry.sty)
Requires:       tex(imakeidx.sty)
Requires:       tex(modulus.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source45:       poetry.tar.xz
Source46:       poetry.doc.tar.xz

%description -n texlive-poetry
This package provides some macros and general doodads for
typesetting poetry. There is, of course, already the excellent
verse package, and the poetrytex package provides some extra
functionality on top of it. But poetry provides much of the
same functionality in a bit of a different way, and with a few
additional abilities, such as facilities for a list of poems,
an index of first lines, and some structural commands.

%package -n texlive-poetry-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.2svn53129
Release:        0
Summary:        Documentation for texlive-poetry
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/

%description -n texlive-poetry-doc
This package includes the documentation for texlive-poetry

%post -n texlive-poetry
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-poetry
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-poetry
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-poetry-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/poetry/CHANGES
%{_texmfdistdir}/doc/latex/poetry/README
%{_texmfdistdir}/doc/latex/poetry/lppl.txt
%{_texmfdistdir}/doc/latex/poetry/poetry.pdf

%files -n texlive-poetry
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/poetry/poetry.sty

%package -n texlive-poetrytex
Version:        %{texlive_version}.%{texlive_noarch}.3.0.1svn39921
Release:        0
License:        LPPL-1.0
Summary:        Typeset anthologies of poetry
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-poetrytex-doc >= %{texlive_version}
Provides:       tex(poetrytex.sty)
Requires:       tex(expl3.sty)
Requires:       tex(tocloft.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source47:       poetrytex.tar.xz
Source48:       poetrytex.doc.tar.xz

%description -n texlive-poetrytex
The package is designed to aid in the management and formatting
of anthologies of poetry and other writings; it does not
concern itself with actually typesettinig the verse itself.

%package -n texlive-poetrytex-doc
Version:        %{texlive_version}.%{texlive_noarch}.3.0.1svn39921
Release:        0
Summary:        Documentation for texlive-poetrytex
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/

%description -n texlive-poetrytex-doc
This package includes the documentation for texlive-poetrytex

%post -n texlive-poetrytex
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-poetrytex
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-poetrytex
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-poetrytex-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/poetrytex/README
%{_texmfdistdir}/doc/latex/poetrytex/poetrytex.pdf
%{_texmfdistdir}/doc/latex/poetrytex/poetrytex.top

%files -n texlive-poetrytex
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/poetrytex/poetrytex.sty

%package -n texlive-poiretone
Version:        %{texlive_version}.%{texlive_noarch}.svn59125
Release:        0
License:        OFL-1.1
Summary:        PoiretOne family of fonts with LaTeX support
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(updmap.cfg)
#!BuildIgnore:  tex(updmap.cfg)
Requires(postun):findutils
Requires(postun):grep
Requires(postun):sed
Requires(postun):texlive >= %{texlive_version}
Requires(postun):tex(updmap.cfg)
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Requires:       texlive-poiretone-fonts >= %{texlive_version}
Suggests:       texlive-poiretone-doc >= %{texlive_version}
Provides:       tex(LY1PoiretOne-LF.fd)
Provides:       tex(OT1PoiretOne-LF.fd)
Provides:       tex(PoiretOne-Bold-lf-ly1--base.tfm)
Provides:       tex(PoiretOne-Bold-lf-ly1.tfm)
Provides:       tex(PoiretOne-Bold-lf-ly1.vf)
Provides:       tex(PoiretOne-Bold-lf-ot1.tfm)
Provides:       tex(PoiretOne-Bold-lf-t1--base.tfm)
Provides:       tex(PoiretOne-Bold-lf-t1.tfm)
Provides:       tex(PoiretOne-Bold-lf-t1.vf)
Provides:       tex(PoiretOne-Bold-lf-ts1--base.tfm)
Provides:       tex(PoiretOne-Bold-lf-ts1.tfm)
Provides:       tex(PoiretOne-Bold-lf-ts1.vf)
Provides:       tex(PoiretOne-Regular-lf-ly1--base.tfm)
Provides:       tex(PoiretOne-Regular-lf-ly1.tfm)
Provides:       tex(PoiretOne-Regular-lf-ly1.vf)
Provides:       tex(PoiretOne-Regular-lf-ot1.tfm)
Provides:       tex(PoiretOne-Regular-lf-t1--base.tfm)
Provides:       tex(PoiretOne-Regular-lf-t1.tfm)
Provides:       tex(PoiretOne-Regular-lf-t1.vf)
Provides:       tex(PoiretOne-Regular-lf-ts1--base.tfm)
Provides:       tex(PoiretOne-Regular-lf-ts1.tfm)
Provides:       tex(PoiretOne-Regular-lf-ts1.vf)
Provides:       tex(PoiretOne.map)
Provides:       tex(PoiretOne.sty)
Provides:       tex(T1PoiretOne-LF.fd)
Provides:       tex(TS1PoiretOne-LF.fd)
Provides:       tex(prtn_2rdbwn.enc)
Provides:       tex(prtn_bjsotj.enc)
Provides:       tex(prtn_nt5tbh.enc)
Provides:       tex(prtn_opucty.enc)
Requires:       tex(fontaxes.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(mweights.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xkeyval.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source49:       poiretone.tar.xz
Source50:       poiretone.doc.tar.xz

%description -n texlive-poiretone
This package provides LaTeX, pdfLaTeX, XeLaTeX and LuaLaTeX
support for the PoiretOne family of fonts, designed by Denis
Masharov. PoiretOne is a decorative geometric grotesque with a
hint of Art Deco and constructivism. There is currently just a
regular weight and an artificially emboldened bold.

%package -n texlive-poiretone-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn59125
Release:        0
Summary:        Documentation for texlive-poiretone
License:        OFL-1.1
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/

%description -n texlive-poiretone-doc
This package includes the documentation for texlive-poiretone

%package -n texlive-poiretone-fonts
Version:        %{texlive_version}.%{texlive_noarch}.svn59125
Release:        0
Summary:        Severed fonts for texlive-poiretone
License:        OFL-1.1
URL:            https://www.tug.org/texlive/
Group:          Productivity/Publishing/TeX/Fonts
%reconfigure_fonts_prereq
Requires(posttrans):fontconfig
Requires(posttrans):ghostscript-fonts-std
Requires(posttrans):mkfontdir
Requires(posttrans):mkfontscale
Requires(posttrans):xorg-x11-fonts-core

%description -n texlive-poiretone-fonts
The  separated fonts package for texlive-poiretone

%post -n texlive-poiretone
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
echo 'addMap PoiretOne.map' >> /var/run/texlive/run-updmap

%postun -n texlive-poiretone
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    echo 'deleteMap PoiretOne.map' >> /var/run/texlive/run-updmap
    exit 0
fi

%posttrans -n texlive-poiretone
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-poiretone-fonts

%files -n texlive-poiretone-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/poiretone/OFL.txt
%{_texmfdistdir}/doc/fonts/poiretone/README
%{_texmfdistdir}/doc/fonts/poiretone/poiret-samples.pdf
%{_texmfdistdir}/doc/fonts/poiretone/poiret-samples.tex

%files -n texlive-poiretone
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/enc/dvips/poiretone/prtn_2rdbwn.enc
%{_texmfdistdir}/fonts/enc/dvips/poiretone/prtn_bjsotj.enc
%{_texmfdistdir}/fonts/enc/dvips/poiretone/prtn_nt5tbh.enc
%{_texmfdistdir}/fonts/enc/dvips/poiretone/prtn_opucty.enc
%{_texmfdistdir}/fonts/map/dvips/poiretone/PoiretOne.map
%{_texmfdistdir}/fonts/tfm/public/poiretone/PoiretOne-Bold-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/poiretone/PoiretOne-Bold-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/poiretone/PoiretOne-Bold-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/poiretone/PoiretOne-Bold-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/poiretone/PoiretOne-Bold-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/poiretone/PoiretOne-Bold-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/poiretone/PoiretOne-Bold-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/poiretone/PoiretOne-Regular-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/poiretone/PoiretOne-Regular-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/poiretone/PoiretOne-Regular-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/poiretone/PoiretOne-Regular-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/poiretone/PoiretOne-Regular-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/poiretone/PoiretOne-Regular-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/poiretone/PoiretOne-Regular-lf-ts1.tfm
%verify(link) %{_texmfdistdir}/fonts/truetype/public/poiretone/PoiretOne-Bold.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/public/poiretone/PoiretOne-Regular.ttf
%verify(link) %{_texmfdistdir}/fonts/type1/public/poiretone/PoiretOne-Bold.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/poiretone/PoiretOne-Regular.pfb
%{_texmfdistdir}/fonts/vf/public/poiretone/PoiretOne-Bold-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/poiretone/PoiretOne-Bold-lf-t1.vf
%{_texmfdistdir}/fonts/vf/public/poiretone/PoiretOne-Bold-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/poiretone/PoiretOne-Regular-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/poiretone/PoiretOne-Regular-lf-t1.vf
%{_texmfdistdir}/fonts/vf/public/poiretone/PoiretOne-Regular-lf-ts1.vf
%{_texmfdistdir}/tex/latex/poiretone/LY1PoiretOne-LF.fd
%{_texmfdistdir}/tex/latex/poiretone/OT1PoiretOne-LF.fd
%{_texmfdistdir}/tex/latex/poiretone/PoiretOne.sty
%{_texmfdistdir}/tex/latex/poiretone/T1PoiretOne-LF.fd
%{_texmfdistdir}/tex/latex/poiretone/TS1PoiretOne-LF.fd

%files -n texlive-poiretone-fonts
%defattr(-,root,root,755)
%dir %{_datadir}/fonts/texlive-poiretone
%{_datadir}/fontconfig/conf.avail/58-texlive-poiretone.conf
%{_datadir}/fontconfig/conf.avail/55-texlive-poiretone.conf
%config %{_sysconfdir}/fonts/conf.d/55-texlive-poiretone.conf
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-poiretone/encodings.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-poiretone/fonts.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-poiretone/fonts.scale
%{_datadir}/fonts/texlive-poiretone/PoiretOne-Bold.ttf
%{_datadir}/fonts/texlive-poiretone/PoiretOne-Regular.ttf
%{_datadir}/fonts/texlive-poiretone/PoiretOne-Bold.pfb
%{_datadir}/fonts/texlive-poiretone/PoiretOne-Regular.pfb

%package -n texlive-polexpr
Version:        %{texlive_version}.%{texlive_noarch}.0.0.8.6svn61559
Release:        0
License:        LPPL-1.0
Summary:        A parser for polynomial expressions
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-polexpr-doc >= %{texlive_version}
Provides:       tex(polexpr-examples.tex)
Provides:       tex(polexpr.sty)
Provides:       tex(polexprcore.tex)
Provides:       tex(polexprexpr.tex)
Provides:       tex(polexprsturm.tex)
Requires:       tex(xintexpr.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source51:       polexpr.tar.xz
Source52:       polexpr.doc.tar.xz

%description -n texlive-polexpr
The package provides a parser \poldef of algebraic polynomial
expressions. As it is based on xintexpr, the coefficients are
allowed to be arbitrary rational numbers. Once defined, a
polynomial is usable by its name either as a numerical function
in \xintexpr/\xinteval, or for additional polynomial
definitions, or as argument to the package macros. The
localization of real roots to arbitrary precision as well as
the determination of all rational roots is implemented via such
macros. Since release 0.8, polexpr extends the xintexpr syntax
to recognize polynomials as a new variable type (and not only
as functions). Functionality which previously was implemented
via macros such as the computation of a greatest common divisor
is now available directly in \xintexpr, \xinteval or \poldef
via infix or functional syntax.

%package -n texlive-polexpr-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.8.6svn61559
Release:        0
Summary:        Documentation for texlive-polexpr
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/

%description -n texlive-polexpr-doc
This package includes the documentation for texlive-polexpr

%post -n texlive-polexpr
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-polexpr
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-polexpr
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-polexpr-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/polexpr/README.md
%{_texmfdistdir}/doc/generic/polexpr/polexpr-examples.pdf
%{_texmfdistdir}/doc/generic/polexpr/polexpr.html

%files -n texlive-polexpr
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/polexpr/polexpr-examples.tex
%{_texmfdistdir}/tex/generic/polexpr/polexpr.sty
%{_texmfdistdir}/tex/generic/polexpr/polexprcore.tex
%{_texmfdistdir}/tex/generic/polexpr/polexprexpr.tex
%{_texmfdistdir}/tex/generic/polexpr/polexprsturm.tex

%package -n texlive-polski
Version:        %{texlive_version}.%{texlive_noarch}.1.3.6svn60322
Release:        0
License:        LPPL-1.0
Summary:        Typeset Polish documents with LaTeX and Polish fonts
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires:       texlive-hyphen-polish >= %{texlive_version}
#!BuildIgnore: texlive-hyphen-polish
Requires:       texlive-pl >= %{texlive_version}
#!BuildIgnore: texlive-pl
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-polski-doc >= %{texlive_version}
Provides:       tex(amigapl.def)
Provides:       tex(mazovia.def)
Provides:       tex(omlplcm.fd)
Provides:       tex(omlplm.fd)
Provides:       tex(omsplsy.fd)
Provides:       tex(omxplex.fd)
Provides:       tex(ot1patch.sty)
Provides:       tex(ot4ccr.fd)
Provides:       tex(ot4cmdh.fd)
Provides:       tex(ot4cmfib.fd)
Provides:       tex(ot4cmfr.fd)
Provides:       tex(ot4cmr.fd)
Provides:       tex(ot4cmss.fd)
Provides:       tex(ot4cmtt.fd)
Provides:       tex(plprefix.sty)
Provides:       tex(polski.sty)
Provides:       tex(qxenc.def)
Requires:       tex(ot4enc.def)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source53:       polski.tar.xz
Source54:       polski.doc.tar.xz

%description -n texlive-polski
Tools to typeset monolingual Polish documents in LaTeX2e
without babel or polyglossia. The package loads Polish
hyphenation patterns, ensures that a font encoding suitable for
Polish is used; in particular it enables Polish adaptation of
Computer Modern fonts (the so-called PL fonts), provides
translations of \today and names like "Bibliography" or
"Chapter", redefines math symbols according to Polish
typographical tradition, provides macros for dashes according
to Polish orthography, provides a historical input method for
"Polish characters", works with traditional TeX as well as with
Unicode aware variants. (This package was previously known as
platex, but has been renamed to resolve a name clash.)

%package -n texlive-polski-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.3.6svn60322
Release:        0
Summary:        Documentation for texlive-polski
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Provides:       locale(texlive-polski-doc:pl)

%description -n texlive-polski-doc
This package includes the documentation for texlive-polski

%post -n texlive-polski
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-polski
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-polski
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-polski-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/polski/README
%{_texmfdistdir}/doc/latex/polski/conowego.txt
%{_texmfdistdir}/doc/latex/polski/czytaj.txt
%{_texmfdistdir}/doc/latex/polski/polski.pdf
%{_texmfdistdir}/doc/latex/polski/sample-polski.pdf
%{_texmfdistdir}/doc/latex/polski/sample-polski.tex
%{_texmfdistdir}/doc/latex/polski/sample-rysunek.mp
%{_texmfdistdir}/doc/latex/polski/sample-rysunek1.mps

%files -n texlive-polski
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/polski/amigapl.def
%{_texmfdistdir}/tex/latex/polski/mazovia.def
%{_texmfdistdir}/tex/latex/polski/omlplcm.fd
%{_texmfdistdir}/tex/latex/polski/omlplm.fd
%{_texmfdistdir}/tex/latex/polski/omsplsy.fd
%{_texmfdistdir}/tex/latex/polski/omxplex.fd
%{_texmfdistdir}/tex/latex/polski/ot1patch.sty
%{_texmfdistdir}/tex/latex/polski/ot4ccr.fd
%{_texmfdistdir}/tex/latex/polski/ot4cmdh.fd
%{_texmfdistdir}/tex/latex/polski/ot4cmfib.fd
%{_texmfdistdir}/tex/latex/polski/ot4cmfr.fd
%{_texmfdistdir}/tex/latex/polski/ot4cmr.fd
%{_texmfdistdir}/tex/latex/polski/ot4cmss.fd
%{_texmfdistdir}/tex/latex/polski/ot4cmtt.fd
%{_texmfdistdir}/tex/latex/polski/plprefix.sty
%{_texmfdistdir}/tex/latex/polski/polski.sty
%{_texmfdistdir}/tex/latex/polski/qxenc.def

%package -n texlive-poltawski
Version:        %{texlive_version}.%{texlive_noarch}.1.101svn20075
Release:        0
License:        LPPL-1.3c
Summary:        Antykwa Poltawskiego Family of Fonts
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(updmap.cfg)
#!BuildIgnore:  tex(updmap.cfg)
Requires(postun):findutils
Requires(postun):grep
Requires(postun):sed
Requires(postun):texlive >= %{texlive_version}
Requires(postun):tex(updmap.cfg)
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Requires:       texlive-poltawski-fonts >= %{texlive_version}
Suggests:       texlive-poltawski-doc >= %{texlive_version}
Provides:       tex(antpolt.sty)
Provides:       tex(ap-cs-sc.enc)
Provides:       tex(ap-cs.enc)
Provides:       tex(ap-cs.map)
Provides:       tex(ap-ec-sc.enc)
Provides:       tex(ap-ec.enc)
Provides:       tex(ap-ec.map)
Provides:       tex(ap-l7x-sc.enc)
Provides:       tex(ap-l7x.enc)
Provides:       tex(ap-l7x.map)
Provides:       tex(ap-qx-sc.enc)
Provides:       tex(ap-qx.enc)
Provides:       tex(ap-qx.map)
Provides:       tex(ap-rm-sc.enc)
Provides:       tex(ap-rm.enc)
Provides:       tex(ap-rm.map)
Provides:       tex(ap-t5-sc.enc)
Provides:       tex(ap-t5.enc)
Provides:       tex(ap-t5.map)
Provides:       tex(ap-texnansi-sc.enc)
Provides:       tex(ap-texnansi.enc)
Provides:       tex(ap-texnansi.map)
Provides:       tex(ap-ts1.enc)
Provides:       tex(ap-ts1.map)
Provides:       tex(ap.map)
Provides:       tex(cs-antpb10-sc.tfm)
Provides:       tex(cs-antpb10.tfm)
Provides:       tex(cs-antpb12-sc.tfm)
Provides:       tex(cs-antpb12.tfm)
Provides:       tex(cs-antpb17-sc.tfm)
Provides:       tex(cs-antpb17.tfm)
Provides:       tex(cs-antpb6-sc.tfm)
Provides:       tex(cs-antpb6.tfm)
Provides:       tex(cs-antpb8-sc.tfm)
Provides:       tex(cs-antpb8.tfm)
Provides:       tex(cs-antpbi10-sc.tfm)
Provides:       tex(cs-antpbi10.tfm)
Provides:       tex(cs-antpbi12-sc.tfm)
Provides:       tex(cs-antpbi12.tfm)
Provides:       tex(cs-antpbi17-sc.tfm)
Provides:       tex(cs-antpbi17.tfm)
Provides:       tex(cs-antpbi6-sc.tfm)
Provides:       tex(cs-antpbi6.tfm)
Provides:       tex(cs-antpbi8-sc.tfm)
Provides:       tex(cs-antpbi8.tfm)
Provides:       tex(cs-antpl10-sc.tfm)
Provides:       tex(cs-antpl10.tfm)
Provides:       tex(cs-antpl12-sc.tfm)
Provides:       tex(cs-antpl12.tfm)
Provides:       tex(cs-antpl17-sc.tfm)
Provides:       tex(cs-antpl17.tfm)
Provides:       tex(cs-antpl6-sc.tfm)
Provides:       tex(cs-antpl6.tfm)
Provides:       tex(cs-antpl8-sc.tfm)
Provides:       tex(cs-antpl8.tfm)
Provides:       tex(cs-antpli10-sc.tfm)
Provides:       tex(cs-antpli10.tfm)
Provides:       tex(cs-antpli12-sc.tfm)
Provides:       tex(cs-antpli12.tfm)
Provides:       tex(cs-antpli17-sc.tfm)
Provides:       tex(cs-antpli17.tfm)
Provides:       tex(cs-antpli6-sc.tfm)
Provides:       tex(cs-antpli6.tfm)
Provides:       tex(cs-antpli8-sc.tfm)
Provides:       tex(cs-antpli8.tfm)
Provides:       tex(cs-antpm10-sc.tfm)
Provides:       tex(cs-antpm10.tfm)
Provides:       tex(cs-antpm12-sc.tfm)
Provides:       tex(cs-antpm12.tfm)
Provides:       tex(cs-antpm17-sc.tfm)
Provides:       tex(cs-antpm17.tfm)
Provides:       tex(cs-antpm6-sc.tfm)
Provides:       tex(cs-antpm6.tfm)
Provides:       tex(cs-antpm8-sc.tfm)
Provides:       tex(cs-antpm8.tfm)
Provides:       tex(cs-antpmi10-sc.tfm)
Provides:       tex(cs-antpmi10.tfm)
Provides:       tex(cs-antpmi12-sc.tfm)
Provides:       tex(cs-antpmi12.tfm)
Provides:       tex(cs-antpmi17-sc.tfm)
Provides:       tex(cs-antpmi17.tfm)
Provides:       tex(cs-antpmi6-sc.tfm)
Provides:       tex(cs-antpmi6.tfm)
Provides:       tex(cs-antpmi8-sc.tfm)
Provides:       tex(cs-antpmi8.tfm)
Provides:       tex(cs-antpr10-sc.tfm)
Provides:       tex(cs-antpr10.tfm)
Provides:       tex(cs-antpr12-sc.tfm)
Provides:       tex(cs-antpr12.tfm)
Provides:       tex(cs-antpr17-sc.tfm)
Provides:       tex(cs-antpr17.tfm)
Provides:       tex(cs-antpr6-sc.tfm)
Provides:       tex(cs-antpr6.tfm)
Provides:       tex(cs-antpr8-sc.tfm)
Provides:       tex(cs-antpr8.tfm)
Provides:       tex(cs-antpri10-sc.tfm)
Provides:       tex(cs-antpri10.tfm)
Provides:       tex(cs-antpri12-sc.tfm)
Provides:       tex(cs-antpri12.tfm)
Provides:       tex(cs-antpri17-sc.tfm)
Provides:       tex(cs-antpri17.tfm)
Provides:       tex(cs-antpri6-sc.tfm)
Provides:       tex(cs-antpri6.tfm)
Provides:       tex(cs-antpri8-sc.tfm)
Provides:       tex(cs-antpri8.tfm)
Provides:       tex(ec-antpb10-sc.tfm)
Provides:       tex(ec-antpb10.tfm)
Provides:       tex(ec-antpb12-sc.tfm)
Provides:       tex(ec-antpb12.tfm)
Provides:       tex(ec-antpb17-sc.tfm)
Provides:       tex(ec-antpb17.tfm)
Provides:       tex(ec-antpb6-sc.tfm)
Provides:       tex(ec-antpb6.tfm)
Provides:       tex(ec-antpb8-sc.tfm)
Provides:       tex(ec-antpb8.tfm)
Provides:       tex(ec-antpbi10-sc.tfm)
Provides:       tex(ec-antpbi10.tfm)
Provides:       tex(ec-antpbi12-sc.tfm)
Provides:       tex(ec-antpbi12.tfm)
Provides:       tex(ec-antpbi17-sc.tfm)
Provides:       tex(ec-antpbi17.tfm)
Provides:       tex(ec-antpbi6-sc.tfm)
Provides:       tex(ec-antpbi6.tfm)
Provides:       tex(ec-antpbi8-sc.tfm)
Provides:       tex(ec-antpbi8.tfm)
Provides:       tex(ec-antpl10-sc.tfm)
Provides:       tex(ec-antpl10.tfm)
Provides:       tex(ec-antpl12-sc.tfm)
Provides:       tex(ec-antpl12.tfm)
Provides:       tex(ec-antpl17-sc.tfm)
Provides:       tex(ec-antpl17.tfm)
Provides:       tex(ec-antpl6-sc.tfm)
Provides:       tex(ec-antpl6.tfm)
Provides:       tex(ec-antpl8-sc.tfm)
Provides:       tex(ec-antpl8.tfm)
Provides:       tex(ec-antpli10-sc.tfm)
Provides:       tex(ec-antpli10.tfm)
Provides:       tex(ec-antpli12-sc.tfm)
Provides:       tex(ec-antpli12.tfm)
Provides:       tex(ec-antpli17-sc.tfm)
Provides:       tex(ec-antpli17.tfm)
Provides:       tex(ec-antpli6-sc.tfm)
Provides:       tex(ec-antpli6.tfm)
Provides:       tex(ec-antpli8-sc.tfm)
Provides:       tex(ec-antpli8.tfm)
Provides:       tex(ec-antpm10-sc.tfm)
Provides:       tex(ec-antpm10.tfm)
Provides:       tex(ec-antpm12-sc.tfm)
Provides:       tex(ec-antpm12.tfm)
Provides:       tex(ec-antpm17-sc.tfm)
Provides:       tex(ec-antpm17.tfm)
Provides:       tex(ec-antpm6-sc.tfm)
Provides:       tex(ec-antpm6.tfm)
Provides:       tex(ec-antpm8-sc.tfm)
Provides:       tex(ec-antpm8.tfm)
Provides:       tex(ec-antpmi10-sc.tfm)
Provides:       tex(ec-antpmi10.tfm)
Provides:       tex(ec-antpmi12-sc.tfm)
Provides:       tex(ec-antpmi12.tfm)
Provides:       tex(ec-antpmi17-sc.tfm)
Provides:       tex(ec-antpmi17.tfm)
Provides:       tex(ec-antpmi6-sc.tfm)
Provides:       tex(ec-antpmi6.tfm)
Provides:       tex(ec-antpmi8-sc.tfm)
Provides:       tex(ec-antpmi8.tfm)
Provides:       tex(ec-antpr10-sc.tfm)
Provides:       tex(ec-antpr10.tfm)
Provides:       tex(ec-antpr12-sc.tfm)
Provides:       tex(ec-antpr12.tfm)
Provides:       tex(ec-antpr17-sc.tfm)
Provides:       tex(ec-antpr17.tfm)
Provides:       tex(ec-antpr6-sc.tfm)
Provides:       tex(ec-antpr6.tfm)
Provides:       tex(ec-antpr8-sc.tfm)
Provides:       tex(ec-antpr8.tfm)
Provides:       tex(ec-antpri10-sc.tfm)
Provides:       tex(ec-antpri10.tfm)
Provides:       tex(ec-antpri12-sc.tfm)
Provides:       tex(ec-antpri12.tfm)
Provides:       tex(ec-antpri17-sc.tfm)
Provides:       tex(ec-antpri17.tfm)
Provides:       tex(ec-antpri6-sc.tfm)
Provides:       tex(ec-antpri6.tfm)
Provides:       tex(ec-antpri8-sc.tfm)
Provides:       tex(ec-antpri8.tfm)
Provides:       tex(il2antp.fd)
Provides:       tex(il2antpl.fd)
Provides:       tex(l7x-antpb10-sc.tfm)
Provides:       tex(l7x-antpb10.tfm)
Provides:       tex(l7x-antpb12-sc.tfm)
Provides:       tex(l7x-antpb12.tfm)
Provides:       tex(l7x-antpb17-sc.tfm)
Provides:       tex(l7x-antpb17.tfm)
Provides:       tex(l7x-antpb6-sc.tfm)
Provides:       tex(l7x-antpb6.tfm)
Provides:       tex(l7x-antpb8-sc.tfm)
Provides:       tex(l7x-antpb8.tfm)
Provides:       tex(l7x-antpbi10-sc.tfm)
Provides:       tex(l7x-antpbi10.tfm)
Provides:       tex(l7x-antpbi12-sc.tfm)
Provides:       tex(l7x-antpbi12.tfm)
Provides:       tex(l7x-antpbi17-sc.tfm)
Provides:       tex(l7x-antpbi17.tfm)
Provides:       tex(l7x-antpbi6-sc.tfm)
Provides:       tex(l7x-antpbi6.tfm)
Provides:       tex(l7x-antpbi8-sc.tfm)
Provides:       tex(l7x-antpbi8.tfm)
Provides:       tex(l7x-antpl10-sc.tfm)
Provides:       tex(l7x-antpl10.tfm)
Provides:       tex(l7x-antpl12-sc.tfm)
Provides:       tex(l7x-antpl12.tfm)
Provides:       tex(l7x-antpl17-sc.tfm)
Provides:       tex(l7x-antpl17.tfm)
Provides:       tex(l7x-antpl6-sc.tfm)
Provides:       tex(l7x-antpl6.tfm)
Provides:       tex(l7x-antpl8-sc.tfm)
Provides:       tex(l7x-antpl8.tfm)
Provides:       tex(l7x-antpli10-sc.tfm)
Provides:       tex(l7x-antpli10.tfm)
Provides:       tex(l7x-antpli12-sc.tfm)
Provides:       tex(l7x-antpli12.tfm)
Provides:       tex(l7x-antpli17-sc.tfm)
Provides:       tex(l7x-antpli17.tfm)
Provides:       tex(l7x-antpli6-sc.tfm)
Provides:       tex(l7x-antpli6.tfm)
Provides:       tex(l7x-antpli8-sc.tfm)
Provides:       tex(l7x-antpli8.tfm)
Provides:       tex(l7x-antpm10-sc.tfm)
Provides:       tex(l7x-antpm10.tfm)
Provides:       tex(l7x-antpm12-sc.tfm)
Provides:       tex(l7x-antpm12.tfm)
Provides:       tex(l7x-antpm17-sc.tfm)
Provides:       tex(l7x-antpm17.tfm)
Provides:       tex(l7x-antpm6-sc.tfm)
Provides:       tex(l7x-antpm6.tfm)
Provides:       tex(l7x-antpm8-sc.tfm)
Provides:       tex(l7x-antpm8.tfm)
Provides:       tex(l7x-antpmi10-sc.tfm)
Provides:       tex(l7x-antpmi10.tfm)
Provides:       tex(l7x-antpmi12-sc.tfm)
Provides:       tex(l7x-antpmi12.tfm)
Provides:       tex(l7x-antpmi17-sc.tfm)
Provides:       tex(l7x-antpmi17.tfm)
Provides:       tex(l7x-antpmi6-sc.tfm)
Provides:       tex(l7x-antpmi6.tfm)
Provides:       tex(l7x-antpmi8-sc.tfm)
Provides:       tex(l7x-antpmi8.tfm)
Provides:       tex(l7x-antpr10-sc.tfm)
Provides:       tex(l7x-antpr10.tfm)
Provides:       tex(l7x-antpr12-sc.tfm)
Provides:       tex(l7x-antpr12.tfm)
Provides:       tex(l7x-antpr17-sc.tfm)
Provides:       tex(l7x-antpr17.tfm)
Provides:       tex(l7x-antpr6-sc.tfm)
Provides:       tex(l7x-antpr6.tfm)
Provides:       tex(l7x-antpr8-sc.tfm)
Provides:       tex(l7x-antpr8.tfm)
Provides:       tex(l7x-antpri10-sc.tfm)
Provides:       tex(l7x-antpri10.tfm)
Provides:       tex(l7x-antpri12-sc.tfm)
Provides:       tex(l7x-antpri12.tfm)
Provides:       tex(l7x-antpri17-sc.tfm)
Provides:       tex(l7x-antpri17.tfm)
Provides:       tex(l7x-antpri6-sc.tfm)
Provides:       tex(l7x-antpri6.tfm)
Provides:       tex(l7x-antpri8-sc.tfm)
Provides:       tex(l7x-antpri8.tfm)
Provides:       tex(l7xantp.fd)
Provides:       tex(l7xantpl.fd)
Provides:       tex(ly1antp.fd)
Provides:       tex(ly1antpl.fd)
Provides:       tex(ot1antp.fd)
Provides:       tex(ot1antpl.fd)
Provides:       tex(ot4antp.fd)
Provides:       tex(ot4antpl.fd)
Provides:       tex(qx-antpb10-sc.tfm)
Provides:       tex(qx-antpb10.tfm)
Provides:       tex(qx-antpb12-sc.tfm)
Provides:       tex(qx-antpb12.tfm)
Provides:       tex(qx-antpb17-sc.tfm)
Provides:       tex(qx-antpb17.tfm)
Provides:       tex(qx-antpb6-sc.tfm)
Provides:       tex(qx-antpb6.tfm)
Provides:       tex(qx-antpb8-sc.tfm)
Provides:       tex(qx-antpb8.tfm)
Provides:       tex(qx-antpbi10-sc.tfm)
Provides:       tex(qx-antpbi10.tfm)
Provides:       tex(qx-antpbi12-sc.tfm)
Provides:       tex(qx-antpbi12.tfm)
Provides:       tex(qx-antpbi17-sc.tfm)
Provides:       tex(qx-antpbi17.tfm)
Provides:       tex(qx-antpbi6-sc.tfm)
Provides:       tex(qx-antpbi6.tfm)
Provides:       tex(qx-antpbi8-sc.tfm)
Provides:       tex(qx-antpbi8.tfm)
Provides:       tex(qx-antpl10-sc.tfm)
Provides:       tex(qx-antpl10.tfm)
Provides:       tex(qx-antpl12-sc.tfm)
Provides:       tex(qx-antpl12.tfm)
Provides:       tex(qx-antpl17-sc.tfm)
Provides:       tex(qx-antpl17.tfm)
Provides:       tex(qx-antpl6-sc.tfm)
Provides:       tex(qx-antpl6.tfm)
Provides:       tex(qx-antpl8-sc.tfm)
Provides:       tex(qx-antpl8.tfm)
Provides:       tex(qx-antpli10-sc.tfm)
Provides:       tex(qx-antpli10.tfm)
Provides:       tex(qx-antpli12-sc.tfm)
Provides:       tex(qx-antpli12.tfm)
Provides:       tex(qx-antpli17-sc.tfm)
Provides:       tex(qx-antpli17.tfm)
Provides:       tex(qx-antpli6-sc.tfm)
Provides:       tex(qx-antpli6.tfm)
Provides:       tex(qx-antpli8-sc.tfm)
Provides:       tex(qx-antpli8.tfm)
Provides:       tex(qx-antpm10-sc.tfm)
Provides:       tex(qx-antpm10.tfm)
Provides:       tex(qx-antpm12-sc.tfm)
Provides:       tex(qx-antpm12.tfm)
Provides:       tex(qx-antpm17-sc.tfm)
Provides:       tex(qx-antpm17.tfm)
Provides:       tex(qx-antpm6-sc.tfm)
Provides:       tex(qx-antpm6.tfm)
Provides:       tex(qx-antpm8-sc.tfm)
Provides:       tex(qx-antpm8.tfm)
Provides:       tex(qx-antpmi10-sc.tfm)
Provides:       tex(qx-antpmi10.tfm)
Provides:       tex(qx-antpmi12-sc.tfm)
Provides:       tex(qx-antpmi12.tfm)
Provides:       tex(qx-antpmi17-sc.tfm)
Provides:       tex(qx-antpmi17.tfm)
Provides:       tex(qx-antpmi6-sc.tfm)
Provides:       tex(qx-antpmi6.tfm)
Provides:       tex(qx-antpmi8-sc.tfm)
Provides:       tex(qx-antpmi8.tfm)
Provides:       tex(qx-antpr10-sc.tfm)
Provides:       tex(qx-antpr10.tfm)
Provides:       tex(qx-antpr12-sc.tfm)
Provides:       tex(qx-antpr12.tfm)
Provides:       tex(qx-antpr17-sc.tfm)
Provides:       tex(qx-antpr17.tfm)
Provides:       tex(qx-antpr6-sc.tfm)
Provides:       tex(qx-antpr6.tfm)
Provides:       tex(qx-antpr8-sc.tfm)
Provides:       tex(qx-antpr8.tfm)
Provides:       tex(qx-antpri10-sc.tfm)
Provides:       tex(qx-antpri10.tfm)
Provides:       tex(qx-antpri12-sc.tfm)
Provides:       tex(qx-antpri12.tfm)
Provides:       tex(qx-antpri17-sc.tfm)
Provides:       tex(qx-antpri17.tfm)
Provides:       tex(qx-antpri6-sc.tfm)
Provides:       tex(qx-antpri6.tfm)
Provides:       tex(qx-antpri8-sc.tfm)
Provides:       tex(qx-antpri8.tfm)
Provides:       tex(qxantp.fd)
Provides:       tex(qxantpl.fd)
Provides:       tex(rm-antpb10-sc.tfm)
Provides:       tex(rm-antpb10.tfm)
Provides:       tex(rm-antpb12-sc.tfm)
Provides:       tex(rm-antpb12.tfm)
Provides:       tex(rm-antpb17-sc.tfm)
Provides:       tex(rm-antpb17.tfm)
Provides:       tex(rm-antpb6-sc.tfm)
Provides:       tex(rm-antpb6.tfm)
Provides:       tex(rm-antpb8-sc.tfm)
Provides:       tex(rm-antpb8.tfm)
Provides:       tex(rm-antpbi10-sc.tfm)
Provides:       tex(rm-antpbi10.tfm)
Provides:       tex(rm-antpbi12-sc.tfm)
Provides:       tex(rm-antpbi12.tfm)
Provides:       tex(rm-antpbi17-sc.tfm)
Provides:       tex(rm-antpbi17.tfm)
Provides:       tex(rm-antpbi6-sc.tfm)
Provides:       tex(rm-antpbi6.tfm)
Provides:       tex(rm-antpbi8-sc.tfm)
Provides:       tex(rm-antpbi8.tfm)
Provides:       tex(rm-antpl10-sc.tfm)
Provides:       tex(rm-antpl10.tfm)
Provides:       tex(rm-antpl12-sc.tfm)
Provides:       tex(rm-antpl12.tfm)
Provides:       tex(rm-antpl17-sc.tfm)
Provides:       tex(rm-antpl17.tfm)
Provides:       tex(rm-antpl6-sc.tfm)
Provides:       tex(rm-antpl6.tfm)
Provides:       tex(rm-antpl8-sc.tfm)
Provides:       tex(rm-antpl8.tfm)
Provides:       tex(rm-antpli10-sc.tfm)
Provides:       tex(rm-antpli10.tfm)
Provides:       tex(rm-antpli12-sc.tfm)
Provides:       tex(rm-antpli12.tfm)
Provides:       tex(rm-antpli17-sc.tfm)
Provides:       tex(rm-antpli17.tfm)
Provides:       tex(rm-antpli6-sc.tfm)
Provides:       tex(rm-antpli6.tfm)
Provides:       tex(rm-antpli8-sc.tfm)
Provides:       tex(rm-antpli8.tfm)
Provides:       tex(rm-antpm10-sc.tfm)
Provides:       tex(rm-antpm10.tfm)
Provides:       tex(rm-antpm12-sc.tfm)
Provides:       tex(rm-antpm12.tfm)
Provides:       tex(rm-antpm17-sc.tfm)
Provides:       tex(rm-antpm17.tfm)
Provides:       tex(rm-antpm6-sc.tfm)
Provides:       tex(rm-antpm6.tfm)
Provides:       tex(rm-antpm8-sc.tfm)
Provides:       tex(rm-antpm8.tfm)
Provides:       tex(rm-antpmi10-sc.tfm)
Provides:       tex(rm-antpmi10.tfm)
Provides:       tex(rm-antpmi12-sc.tfm)
Provides:       tex(rm-antpmi12.tfm)
Provides:       tex(rm-antpmi17-sc.tfm)
Provides:       tex(rm-antpmi17.tfm)
Provides:       tex(rm-antpmi6-sc.tfm)
Provides:       tex(rm-antpmi6.tfm)
Provides:       tex(rm-antpmi8-sc.tfm)
Provides:       tex(rm-antpmi8.tfm)
Provides:       tex(rm-antpr10-sc.tfm)
Provides:       tex(rm-antpr10.tfm)
Provides:       tex(rm-antpr12-sc.tfm)
Provides:       tex(rm-antpr12.tfm)
Provides:       tex(rm-antpr17-sc.tfm)
Provides:       tex(rm-antpr17.tfm)
Provides:       tex(rm-antpr6-sc.tfm)
Provides:       tex(rm-antpr6.tfm)
Provides:       tex(rm-antpr8-sc.tfm)
Provides:       tex(rm-antpr8.tfm)
Provides:       tex(rm-antpri10-sc.tfm)
Provides:       tex(rm-antpri10.tfm)
Provides:       tex(rm-antpri12-sc.tfm)
Provides:       tex(rm-antpri12.tfm)
Provides:       tex(rm-antpri17-sc.tfm)
Provides:       tex(rm-antpri17.tfm)
Provides:       tex(rm-antpri6-sc.tfm)
Provides:       tex(rm-antpri6.tfm)
Provides:       tex(rm-antpri8-sc.tfm)
Provides:       tex(rm-antpri8.tfm)
Provides:       tex(t1antp.fd)
Provides:       tex(t1antpl.fd)
Provides:       tex(t5-antpb10-sc.tfm)
Provides:       tex(t5-antpb10.tfm)
Provides:       tex(t5-antpb12-sc.tfm)
Provides:       tex(t5-antpb12.tfm)
Provides:       tex(t5-antpb17-sc.tfm)
Provides:       tex(t5-antpb17.tfm)
Provides:       tex(t5-antpb6-sc.tfm)
Provides:       tex(t5-antpb6.tfm)
Provides:       tex(t5-antpb8-sc.tfm)
Provides:       tex(t5-antpb8.tfm)
Provides:       tex(t5-antpbi10-sc.tfm)
Provides:       tex(t5-antpbi10.tfm)
Provides:       tex(t5-antpbi12-sc.tfm)
Provides:       tex(t5-antpbi12.tfm)
Provides:       tex(t5-antpbi17-sc.tfm)
Provides:       tex(t5-antpbi17.tfm)
Provides:       tex(t5-antpbi6-sc.tfm)
Provides:       tex(t5-antpbi6.tfm)
Provides:       tex(t5-antpbi8-sc.tfm)
Provides:       tex(t5-antpbi8.tfm)
Provides:       tex(t5-antpl10-sc.tfm)
Provides:       tex(t5-antpl10.tfm)
Provides:       tex(t5-antpl12-sc.tfm)
Provides:       tex(t5-antpl12.tfm)
Provides:       tex(t5-antpl17-sc.tfm)
Provides:       tex(t5-antpl17.tfm)
Provides:       tex(t5-antpl6-sc.tfm)
Provides:       tex(t5-antpl6.tfm)
Provides:       tex(t5-antpl8-sc.tfm)
Provides:       tex(t5-antpl8.tfm)
Provides:       tex(t5-antpli10-sc.tfm)
Provides:       tex(t5-antpli10.tfm)
Provides:       tex(t5-antpli12-sc.tfm)
Provides:       tex(t5-antpli12.tfm)
Provides:       tex(t5-antpli17-sc.tfm)
Provides:       tex(t5-antpli17.tfm)
Provides:       tex(t5-antpli6-sc.tfm)
Provides:       tex(t5-antpli6.tfm)
Provides:       tex(t5-antpli8-sc.tfm)
Provides:       tex(t5-antpli8.tfm)
Provides:       tex(t5-antpm10-sc.tfm)
Provides:       tex(t5-antpm10.tfm)
Provides:       tex(t5-antpm12-sc.tfm)
Provides:       tex(t5-antpm12.tfm)
Provides:       tex(t5-antpm17-sc.tfm)
Provides:       tex(t5-antpm17.tfm)
Provides:       tex(t5-antpm6-sc.tfm)
Provides:       tex(t5-antpm6.tfm)
Provides:       tex(t5-antpm8-sc.tfm)
Provides:       tex(t5-antpm8.tfm)
Provides:       tex(t5-antpmi10-sc.tfm)
Provides:       tex(t5-antpmi10.tfm)
Provides:       tex(t5-antpmi12-sc.tfm)
Provides:       tex(t5-antpmi12.tfm)
Provides:       tex(t5-antpmi17-sc.tfm)
Provides:       tex(t5-antpmi17.tfm)
Provides:       tex(t5-antpmi6-sc.tfm)
Provides:       tex(t5-antpmi6.tfm)
Provides:       tex(t5-antpmi8-sc.tfm)
Provides:       tex(t5-antpmi8.tfm)
Provides:       tex(t5-antpr10-sc.tfm)
Provides:       tex(t5-antpr10.tfm)
Provides:       tex(t5-antpr12-sc.tfm)
Provides:       tex(t5-antpr12.tfm)
Provides:       tex(t5-antpr17-sc.tfm)
Provides:       tex(t5-antpr17.tfm)
Provides:       tex(t5-antpr6-sc.tfm)
Provides:       tex(t5-antpr6.tfm)
Provides:       tex(t5-antpr8-sc.tfm)
Provides:       tex(t5-antpr8.tfm)
Provides:       tex(t5-antpri10-sc.tfm)
Provides:       tex(t5-antpri10.tfm)
Provides:       tex(t5-antpri12-sc.tfm)
Provides:       tex(t5-antpri12.tfm)
Provides:       tex(t5-antpri17-sc.tfm)
Provides:       tex(t5-antpri17.tfm)
Provides:       tex(t5-antpri6-sc.tfm)
Provides:       tex(t5-antpri6.tfm)
Provides:       tex(t5-antpri8-sc.tfm)
Provides:       tex(t5-antpri8.tfm)
Provides:       tex(t5antp.fd)
Provides:       tex(t5antpl.fd)
Provides:       tex(texnansi-antpb10-sc.tfm)
Provides:       tex(texnansi-antpb10.tfm)
Provides:       tex(texnansi-antpb12-sc.tfm)
Provides:       tex(texnansi-antpb12.tfm)
Provides:       tex(texnansi-antpb17-sc.tfm)
Provides:       tex(texnansi-antpb17.tfm)
Provides:       tex(texnansi-antpb6-sc.tfm)
Provides:       tex(texnansi-antpb6.tfm)
Provides:       tex(texnansi-antpb8-sc.tfm)
Provides:       tex(texnansi-antpb8.tfm)
Provides:       tex(texnansi-antpbi10-sc.tfm)
Provides:       tex(texnansi-antpbi10.tfm)
Provides:       tex(texnansi-antpbi12-sc.tfm)
Provides:       tex(texnansi-antpbi12.tfm)
Provides:       tex(texnansi-antpbi17-sc.tfm)
Provides:       tex(texnansi-antpbi17.tfm)
Provides:       tex(texnansi-antpbi6-sc.tfm)
Provides:       tex(texnansi-antpbi6.tfm)
Provides:       tex(texnansi-antpbi8-sc.tfm)
Provides:       tex(texnansi-antpbi8.tfm)
Provides:       tex(texnansi-antpl10-sc.tfm)
Provides:       tex(texnansi-antpl10.tfm)
Provides:       tex(texnansi-antpl12-sc.tfm)
Provides:       tex(texnansi-antpl12.tfm)
Provides:       tex(texnansi-antpl17-sc.tfm)
Provides:       tex(texnansi-antpl17.tfm)
Provides:       tex(texnansi-antpl6-sc.tfm)
Provides:       tex(texnansi-antpl6.tfm)
Provides:       tex(texnansi-antpl8-sc.tfm)
Provides:       tex(texnansi-antpl8.tfm)
Provides:       tex(texnansi-antpli10-sc.tfm)
Provides:       tex(texnansi-antpli10.tfm)
Provides:       tex(texnansi-antpli12-sc.tfm)
Provides:       tex(texnansi-antpli12.tfm)
Provides:       tex(texnansi-antpli17-sc.tfm)
Provides:       tex(texnansi-antpli17.tfm)
Provides:       tex(texnansi-antpli6-sc.tfm)
Provides:       tex(texnansi-antpli6.tfm)
Provides:       tex(texnansi-antpli8-sc.tfm)
Provides:       tex(texnansi-antpli8.tfm)
Provides:       tex(texnansi-antpm10-sc.tfm)
Provides:       tex(texnansi-antpm10.tfm)
Provides:       tex(texnansi-antpm12-sc.tfm)
Provides:       tex(texnansi-antpm12.tfm)
Provides:       tex(texnansi-antpm17-sc.tfm)
Provides:       tex(texnansi-antpm17.tfm)
Provides:       tex(texnansi-antpm6-sc.tfm)
Provides:       tex(texnansi-antpm6.tfm)
Provides:       tex(texnansi-antpm8-sc.tfm)
Provides:       tex(texnansi-antpm8.tfm)
Provides:       tex(texnansi-antpmi10-sc.tfm)
Provides:       tex(texnansi-antpmi10.tfm)
Provides:       tex(texnansi-antpmi12-sc.tfm)
Provides:       tex(texnansi-antpmi12.tfm)
Provides:       tex(texnansi-antpmi17-sc.tfm)
Provides:       tex(texnansi-antpmi17.tfm)
Provides:       tex(texnansi-antpmi6-sc.tfm)
Provides:       tex(texnansi-antpmi6.tfm)
Provides:       tex(texnansi-antpmi8-sc.tfm)
Provides:       tex(texnansi-antpmi8.tfm)
Provides:       tex(texnansi-antpr10-sc.tfm)
Provides:       tex(texnansi-antpr10.tfm)
Provides:       tex(texnansi-antpr12-sc.tfm)
Provides:       tex(texnansi-antpr12.tfm)
Provides:       tex(texnansi-antpr17-sc.tfm)
Provides:       tex(texnansi-antpr17.tfm)
Provides:       tex(texnansi-antpr6-sc.tfm)
Provides:       tex(texnansi-antpr6.tfm)
Provides:       tex(texnansi-antpr8-sc.tfm)
Provides:       tex(texnansi-antpr8.tfm)
Provides:       tex(texnansi-antpri10-sc.tfm)
Provides:       tex(texnansi-antpri10.tfm)
Provides:       tex(texnansi-antpri12-sc.tfm)
Provides:       tex(texnansi-antpri12.tfm)
Provides:       tex(texnansi-antpri17-sc.tfm)
Provides:       tex(texnansi-antpri17.tfm)
Provides:       tex(texnansi-antpri6-sc.tfm)
Provides:       tex(texnansi-antpri6.tfm)
Provides:       tex(texnansi-antpri8-sc.tfm)
Provides:       tex(texnansi-antpri8.tfm)
Provides:       tex(ts1-antpb10.tfm)
Provides:       tex(ts1-antpb12.tfm)
Provides:       tex(ts1-antpb17.tfm)
Provides:       tex(ts1-antpb6.tfm)
Provides:       tex(ts1-antpb8.tfm)
Provides:       tex(ts1-antpbi10.tfm)
Provides:       tex(ts1-antpbi12.tfm)
Provides:       tex(ts1-antpbi17.tfm)
Provides:       tex(ts1-antpbi6.tfm)
Provides:       tex(ts1-antpbi8.tfm)
Provides:       tex(ts1-antpl10.tfm)
Provides:       tex(ts1-antpl12.tfm)
Provides:       tex(ts1-antpl17.tfm)
Provides:       tex(ts1-antpl6.tfm)
Provides:       tex(ts1-antpl8.tfm)
Provides:       tex(ts1-antpli10.tfm)
Provides:       tex(ts1-antpli12.tfm)
Provides:       tex(ts1-antpli17.tfm)
Provides:       tex(ts1-antpli6.tfm)
Provides:       tex(ts1-antpli8.tfm)
Provides:       tex(ts1-antpm10.tfm)
Provides:       tex(ts1-antpm12.tfm)
Provides:       tex(ts1-antpm17.tfm)
Provides:       tex(ts1-antpm6.tfm)
Provides:       tex(ts1-antpm8.tfm)
Provides:       tex(ts1-antpmi10.tfm)
Provides:       tex(ts1-antpmi12.tfm)
Provides:       tex(ts1-antpmi17.tfm)
Provides:       tex(ts1-antpmi6.tfm)
Provides:       tex(ts1-antpmi8.tfm)
Provides:       tex(ts1-antpr10.tfm)
Provides:       tex(ts1-antpr12.tfm)
Provides:       tex(ts1-antpr17.tfm)
Provides:       tex(ts1-antpr6.tfm)
Provides:       tex(ts1-antpr8.tfm)
Provides:       tex(ts1-antpri10.tfm)
Provides:       tex(ts1-antpri12.tfm)
Provides:       tex(ts1-antpri17.tfm)
Provides:       tex(ts1-antpri6.tfm)
Provides:       tex(ts1-antpri8.tfm)
Provides:       tex(ts1antp.fd)
Provides:       tex(ts1antpl.fd)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source55:       poltawski.tar.xz
Source56:       poltawski.doc.tar.xz

%description -n texlive-poltawski
The package contains the Antykwa Poltawskiego family of fonts
in the PostScript Type 1 and OpenType formats. The original
font was designed in the twenties of the XX century by the
Polish typographer Adam Poltawski(1881-1952). Following the
route set out by the Latin Modern and TeX Gyre projects
(http://www.gust.org.pl/projects/e-foundry), the Antykwa
Poltawskiego digitisation project aims at providing a rich
collection of diacritical characters in the attempt to cover as
many Latin-based scripts as possible. To our knowledge, the
repertoire of characters covers all European languages as well
as some other Latin-based alphabets such as Vietnamese and
Navajo; at the request of users, recent extensions (following
the enhancement of the Latin Modern collection) provide glyphs
sufficient for typesetting of romanized transliterations of
Arabic and Sanskrit scripts. The Antykwa Poltawskiego family
consists of 4 weights (light, normal, medium, bold), each
having upright and italic forms and one of 5 design sizes: 6,
8, 10, 12 and 17pt. Altogether, the collection comprises 40
font files, containing the same repertoire of 1126 characters.
The preliminary version of Antykwa Poltawskiego (antp package)
released in 2000 is rendered obsolete by this package.

%package -n texlive-poltawski-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.101svn20075
Release:        0
Summary:        Documentation for texlive-poltawski
License:        LPPL-1.3c
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/

%description -n texlive-poltawski-doc
This package includes the documentation for texlive-poltawski

%package -n texlive-poltawski-fonts
Version:        %{texlive_version}.%{texlive_noarch}.1.101svn20075
Release:        0
Summary:        Severed fonts for texlive-poltawski
License:        LPPL-1.3c
URL:            https://www.tug.org/texlive/
Group:          Productivity/Publishing/TeX/Fonts
%reconfigure_fonts_prereq
Requires(posttrans):fontconfig
Requires(posttrans):ghostscript-fonts-std
Requires(posttrans):mkfontdir
Requires(posttrans):mkfontscale
Requires(posttrans):xorg-x11-fonts-core

%description -n texlive-poltawski-fonts
The  separated fonts package for texlive-poltawski

%post -n texlive-poltawski
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
echo 'addMap ap.map' >> /var/run/texlive/run-updmap

%postun -n texlive-poltawski
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    echo 'deleteMap ap.map' >> /var/run/texlive/run-updmap
    exit 0
fi

%posttrans -n texlive-poltawski
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-poltawski-fonts

%files -n texlive-poltawski-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/poltawski/GUST-FONT-LICENSE.txt
%{_texmfdistdir}/doc/fonts/poltawski/MANIFEST-Antykwa-Poltawskiego.txt
%{_texmfdistdir}/doc/fonts/poltawski/README-Antykwa-Poltawskiego.txt
%{_texmfdistdir}/doc/fonts/poltawski/antpb10.fea
%{_texmfdistdir}/doc/fonts/poltawski/antpb12.fea
%{_texmfdistdir}/doc/fonts/poltawski/antpb17.fea
%{_texmfdistdir}/doc/fonts/poltawski/antpb6.fea
%{_texmfdistdir}/doc/fonts/poltawski/antpb8.fea
%{_texmfdistdir}/doc/fonts/poltawski/antpbi10.fea
%{_texmfdistdir}/doc/fonts/poltawski/antpbi12.fea
%{_texmfdistdir}/doc/fonts/poltawski/antpbi17.fea
%{_texmfdistdir}/doc/fonts/poltawski/antpbi6.fea
%{_texmfdistdir}/doc/fonts/poltawski/antpbi8.fea
%{_texmfdistdir}/doc/fonts/poltawski/antpl10.fea
%{_texmfdistdir}/doc/fonts/poltawski/antpl12.fea
%{_texmfdistdir}/doc/fonts/poltawski/antpl17.fea
%{_texmfdistdir}/doc/fonts/poltawski/antpl6.fea
%{_texmfdistdir}/doc/fonts/poltawski/antpl8.fea
%{_texmfdistdir}/doc/fonts/poltawski/antpli10.fea
%{_texmfdistdir}/doc/fonts/poltawski/antpli12.fea
%{_texmfdistdir}/doc/fonts/poltawski/antpli17.fea
%{_texmfdistdir}/doc/fonts/poltawski/antpli6.fea
%{_texmfdistdir}/doc/fonts/poltawski/antpli8.fea
%{_texmfdistdir}/doc/fonts/poltawski/antpm10.fea
%{_texmfdistdir}/doc/fonts/poltawski/antpm12.fea
%{_texmfdistdir}/doc/fonts/poltawski/antpm17.fea
%{_texmfdistdir}/doc/fonts/poltawski/antpm6.fea
%{_texmfdistdir}/doc/fonts/poltawski/antpm8.fea
%{_texmfdistdir}/doc/fonts/poltawski/antpmi10.fea
%{_texmfdistdir}/doc/fonts/poltawski/antpmi12.fea
%{_texmfdistdir}/doc/fonts/poltawski/antpmi17.fea
%{_texmfdistdir}/doc/fonts/poltawski/antpmi6.fea
%{_texmfdistdir}/doc/fonts/poltawski/antpmi8.fea
%{_texmfdistdir}/doc/fonts/poltawski/antpr10.fea
%{_texmfdistdir}/doc/fonts/poltawski/antpr12.fea
%{_texmfdistdir}/doc/fonts/poltawski/antpr17.fea
%{_texmfdistdir}/doc/fonts/poltawski/antpr6.fea
%{_texmfdistdir}/doc/fonts/poltawski/antpr8.fea
%{_texmfdistdir}/doc/fonts/poltawski/antpri10.fea
%{_texmfdistdir}/doc/fonts/poltawski/antpri12.fea
%{_texmfdistdir}/doc/fonts/poltawski/antpri17.fea
%{_texmfdistdir}/doc/fonts/poltawski/antpri6.fea
%{_texmfdistdir}/doc/fonts/poltawski/antpri8.fea
%{_texmfdistdir}/doc/fonts/poltawski/ap-hist.txt
%{_texmfdistdir}/doc/fonts/poltawski/ap-info.pdf
%{_texmfdistdir}/doc/fonts/poltawski/ap-logo.pdf
%{_texmfdistdir}/doc/fonts/poltawski/goadb100.nam
%{_texmfdistdir}/doc/fonts/poltawski/tstapot1.pdf
%{_texmfdistdir}/doc/fonts/poltawski/tstapot1.tex
%{_texmfdistdir}/doc/fonts/poltawski/tstapot4.pdf
%{_texmfdistdir}/doc/fonts/poltawski/tstapot4.tex
%{_texmfdistdir}/doc/fonts/poltawski/tstapqx.pdf
%{_texmfdistdir}/doc/fonts/poltawski/tstapqx.tex
%{_texmfdistdir}/doc/fonts/poltawski/tstapt1.pdf
%{_texmfdistdir}/doc/fonts/poltawski/tstapt1.tex
%{_texmfdistdir}/doc/fonts/poltawski/tstapts1.pdf
%{_texmfdistdir}/doc/fonts/poltawski/tstapts1.tex

%files -n texlive-poltawski
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/afm/gust/poltawski/antpb10.afm
%{_texmfdistdir}/fonts/afm/gust/poltawski/antpb12.afm
%{_texmfdistdir}/fonts/afm/gust/poltawski/antpb17.afm
%{_texmfdistdir}/fonts/afm/gust/poltawski/antpb6.afm
%{_texmfdistdir}/fonts/afm/gust/poltawski/antpb8.afm
%{_texmfdistdir}/fonts/afm/gust/poltawski/antpbi10.afm
%{_texmfdistdir}/fonts/afm/gust/poltawski/antpbi12.afm
%{_texmfdistdir}/fonts/afm/gust/poltawski/antpbi17.afm
%{_texmfdistdir}/fonts/afm/gust/poltawski/antpbi6.afm
%{_texmfdistdir}/fonts/afm/gust/poltawski/antpbi8.afm
%{_texmfdistdir}/fonts/afm/gust/poltawski/antpl10.afm
%{_texmfdistdir}/fonts/afm/gust/poltawski/antpl12.afm
%{_texmfdistdir}/fonts/afm/gust/poltawski/antpl17.afm
%{_texmfdistdir}/fonts/afm/gust/poltawski/antpl6.afm
%{_texmfdistdir}/fonts/afm/gust/poltawski/antpl8.afm
%{_texmfdistdir}/fonts/afm/gust/poltawski/antpli10.afm
%{_texmfdistdir}/fonts/afm/gust/poltawski/antpli12.afm
%{_texmfdistdir}/fonts/afm/gust/poltawski/antpli17.afm
%{_texmfdistdir}/fonts/afm/gust/poltawski/antpli6.afm
%{_texmfdistdir}/fonts/afm/gust/poltawski/antpli8.afm
%{_texmfdistdir}/fonts/afm/gust/poltawski/antpm10.afm
%{_texmfdistdir}/fonts/afm/gust/poltawski/antpm12.afm
%{_texmfdistdir}/fonts/afm/gust/poltawski/antpm17.afm
%{_texmfdistdir}/fonts/afm/gust/poltawski/antpm6.afm
%{_texmfdistdir}/fonts/afm/gust/poltawski/antpm8.afm
%{_texmfdistdir}/fonts/afm/gust/poltawski/antpmi10.afm
%{_texmfdistdir}/fonts/afm/gust/poltawski/antpmi12.afm
%{_texmfdistdir}/fonts/afm/gust/poltawski/antpmi17.afm
%{_texmfdistdir}/fonts/afm/gust/poltawski/antpmi6.afm
%{_texmfdistdir}/fonts/afm/gust/poltawski/antpmi8.afm
%{_texmfdistdir}/fonts/afm/gust/poltawski/antpr10.afm
%{_texmfdistdir}/fonts/afm/gust/poltawski/antpr12.afm
%{_texmfdistdir}/fonts/afm/gust/poltawski/antpr17.afm
%{_texmfdistdir}/fonts/afm/gust/poltawski/antpr6.afm
%{_texmfdistdir}/fonts/afm/gust/poltawski/antpr8.afm
%{_texmfdistdir}/fonts/afm/gust/poltawski/antpri10.afm
%{_texmfdistdir}/fonts/afm/gust/poltawski/antpri12.afm
%{_texmfdistdir}/fonts/afm/gust/poltawski/antpri17.afm
%{_texmfdistdir}/fonts/afm/gust/poltawski/antpri6.afm
%{_texmfdistdir}/fonts/afm/gust/poltawski/antpri8.afm
%{_texmfdistdir}/fonts/enc/dvips/poltawski/ap-cs-sc.enc
%{_texmfdistdir}/fonts/enc/dvips/poltawski/ap-cs.enc
%{_texmfdistdir}/fonts/enc/dvips/poltawski/ap-ec-sc.enc
%{_texmfdistdir}/fonts/enc/dvips/poltawski/ap-ec.enc
%{_texmfdistdir}/fonts/enc/dvips/poltawski/ap-l7x-sc.enc
%{_texmfdistdir}/fonts/enc/dvips/poltawski/ap-l7x.enc
%{_texmfdistdir}/fonts/enc/dvips/poltawski/ap-qx-sc.enc
%{_texmfdistdir}/fonts/enc/dvips/poltawski/ap-qx.enc
%{_texmfdistdir}/fonts/enc/dvips/poltawski/ap-rm-sc.enc
%{_texmfdistdir}/fonts/enc/dvips/poltawski/ap-rm.enc
%{_texmfdistdir}/fonts/enc/dvips/poltawski/ap-t5-sc.enc
%{_texmfdistdir}/fonts/enc/dvips/poltawski/ap-t5.enc
%{_texmfdistdir}/fonts/enc/dvips/poltawski/ap-texnansi-sc.enc
%{_texmfdistdir}/fonts/enc/dvips/poltawski/ap-texnansi.enc
%{_texmfdistdir}/fonts/enc/dvips/poltawski/ap-ts1.enc
%{_texmfdistdir}/fonts/map/dvips/poltawski/ap-cs.map
%{_texmfdistdir}/fonts/map/dvips/poltawski/ap-ec.map
%{_texmfdistdir}/fonts/map/dvips/poltawski/ap-l7x.map
%{_texmfdistdir}/fonts/map/dvips/poltawski/ap-qx.map
%{_texmfdistdir}/fonts/map/dvips/poltawski/ap-rm.map
%{_texmfdistdir}/fonts/map/dvips/poltawski/ap-t5.map
%{_texmfdistdir}/fonts/map/dvips/poltawski/ap-texnansi.map
%{_texmfdistdir}/fonts/map/dvips/poltawski/ap-ts1.map
%{_texmfdistdir}/fonts/map/dvips/poltawski/ap.map
%verify(link) %{_texmfdistdir}/fonts/opentype/gust/poltawski/antpolt-bold.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/gust/poltawski/antpolt-bolditalic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/gust/poltawski/antpolt-italic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/gust/poltawski/antpolt-regular.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/gust/poltawski/antpoltcond-bold.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/gust/poltawski/antpoltcond-bolditalic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/gust/poltawski/antpoltcond-italic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/gust/poltawski/antpoltcond-regular.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/gust/poltawski/antpoltexpd-bold.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/gust/poltawski/antpoltexpd-bolditalic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/gust/poltawski/antpoltexpd-italic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/gust/poltawski/antpoltexpd-regular.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/gust/poltawski/antpoltlt-bold.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/gust/poltawski/antpoltlt-bolditalic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/gust/poltawski/antpoltlt-italic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/gust/poltawski/antpoltlt-regular.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/gust/poltawski/antpoltltcond-bold.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/gust/poltawski/antpoltltcond-bolditalic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/gust/poltawski/antpoltltcond-italic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/gust/poltawski/antpoltltcond-regular.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/gust/poltawski/antpoltltexpd-bold.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/gust/poltawski/antpoltltexpd-bolditalic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/gust/poltawski/antpoltltexpd-italic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/gust/poltawski/antpoltltexpd-regular.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/gust/poltawski/antpoltltsemicond-bold.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/gust/poltawski/antpoltltsemicond-bolditalic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/gust/poltawski/antpoltltsemicond-italic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/gust/poltawski/antpoltltsemicond-regular.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/gust/poltawski/antpoltltsemiexpd-bold.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/gust/poltawski/antpoltltsemiexpd-bolditalic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/gust/poltawski/antpoltltsemiexpd-italic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/gust/poltawski/antpoltltsemiexpd-regular.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/gust/poltawski/antpoltsemicond-bold.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/gust/poltawski/antpoltsemicond-bolditalic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/gust/poltawski/antpoltsemicond-italic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/gust/poltawski/antpoltsemicond-regular.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/gust/poltawski/antpoltsemiexpd-bold.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/gust/poltawski/antpoltsemiexpd-bolditalic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/gust/poltawski/antpoltsemiexpd-italic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/gust/poltawski/antpoltsemiexpd-regular.otf
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpb10-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpb10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpb12-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpb12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpb17-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpb17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpb6-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpb6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpb8-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpb8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpbi10-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpbi10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpbi12-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpbi12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpbi17-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpbi17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpbi6-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpbi6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpbi8-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpbi8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpl10-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpl10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpl12-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpl12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpl17-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpl17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpl6-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpl6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpl8-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpl8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpli10-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpli10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpli12-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpli12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpli17-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpli17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpli6-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpli6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpli8-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpli8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpm10-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpm10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpm12-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpm12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpm17-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpm17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpm6-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpm6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpm8-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpm8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpmi10-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpmi10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpmi12-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpmi12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpmi17-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpmi17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpmi6-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpmi6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpmi8-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpmi8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpr10-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpr10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpr12-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpr12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpr17-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpr17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpr6-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpr6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpr8-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpr8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpri10-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpri10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpri12-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpri12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpri17-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpri17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpri6-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpri6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpri8-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpri8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpb10-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpb10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpb12-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpb12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpb17-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpb17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpb6-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpb6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpb8-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpb8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpbi10-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpbi10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpbi12-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpbi12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpbi17-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpbi17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpbi6-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpbi6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpbi8-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpbi8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpl10-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpl10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpl12-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpl12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpl17-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpl17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpl6-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpl6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpl8-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpl8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpli10-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpli10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpli12-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpli12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpli17-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpli17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpli6-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpli6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpli8-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpli8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpm10-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpm10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpm12-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpm12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpm17-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpm17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpm6-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpm6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpm8-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpm8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpmi10-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpmi10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpmi12-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpmi12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpmi17-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpmi17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpmi6-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpmi6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpmi8-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpmi8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpr10-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpr10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpr12-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpr12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpr17-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpr17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpr6-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpr6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpr8-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpr8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpri10-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpri10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpri12-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpri12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpri17-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpri17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpri6-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpri6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpri8-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpri8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpb10-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpb10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpb12-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpb12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpb17-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpb17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpb6-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpb6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpb8-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpb8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpbi10-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpbi10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpbi12-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpbi12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpbi17-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpbi17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpbi6-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpbi6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpbi8-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpbi8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpl10-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpl10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpl12-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpl12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpl17-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpl17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpl6-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpl6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpl8-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpl8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpli10-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpli10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpli12-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpli12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpli17-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpli17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpli6-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpli6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpli8-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpli8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpm10-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpm10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpm12-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpm12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpm17-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpm17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpm6-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpm6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpm8-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpm8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpmi10-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpmi10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpmi12-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpmi12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpmi17-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpmi17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpmi6-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpmi6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpmi8-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpmi8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpr10-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpr10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpr12-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpr12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpr17-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpr17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpr6-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpr6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpr8-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpr8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpri10-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpri10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpri12-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpri12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpri17-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpri17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpri6-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpri6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpri8-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpri8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpb10-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpb10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpb12-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpb12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpb17-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpb17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpb6-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpb6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpb8-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpb8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpbi10-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpbi10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpbi12-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpbi12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpbi17-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpbi17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpbi6-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpbi6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpbi8-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpbi8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpl10-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpl10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpl12-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpl12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpl17-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpl17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpl6-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpl6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpl8-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpl8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpli10-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpli10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpli12-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpli12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpli17-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpli17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpli6-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpli6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpli8-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpli8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpm10-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpm10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpm12-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpm12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpm17-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpm17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpm6-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpm6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpm8-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpm8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpmi10-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpmi10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpmi12-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpmi12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpmi17-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpmi17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpmi6-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpmi6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpmi8-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpmi8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpr10-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpr10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpr12-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpr12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpr17-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpr17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpr6-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpr6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpr8-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpr8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpri10-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpri10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpri12-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpri12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpri17-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpri17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpri6-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpri6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpri8-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpri8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpb10-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpb10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpb12-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpb12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpb17-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpb17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpb6-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpb6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpb8-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpb8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpbi10-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpbi10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpbi12-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpbi12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpbi17-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpbi17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpbi6-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpbi6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpbi8-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpbi8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpl10-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpl10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpl12-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpl12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpl17-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpl17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpl6-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpl6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpl8-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpl8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpli10-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpli10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpli12-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpli12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpli17-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpli17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpli6-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpli6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpli8-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpli8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpm10-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpm10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpm12-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpm12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpm17-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpm17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpm6-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpm6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpm8-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpm8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpmi10-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpmi10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpmi12-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpmi12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpmi17-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpmi17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpmi6-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpmi6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpmi8-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpmi8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpr10-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpr10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpr12-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpr12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpr17-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpr17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpr6-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpr6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpr8-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpr8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpri10-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpri10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpri12-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpri12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpri17-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpri17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpri6-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpri6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpri8-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpri8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpb10-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpb10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpb12-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpb12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpb17-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpb17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpb6-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpb6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpb8-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpb8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpbi10-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpbi10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpbi12-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpbi12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpbi17-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpbi17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpbi6-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpbi6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpbi8-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpbi8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpl10-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpl10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpl12-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpl12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpl17-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpl17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpl6-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpl6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpl8-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpl8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpli10-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpli10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpli12-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpli12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpli17-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpli17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpli6-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpli6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpli8-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpli8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpm10-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpm10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpm12-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpm12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpm17-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpm17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpm6-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpm6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpm8-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpm8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpmi10-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpmi10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpmi12-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpmi12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpmi17-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpmi17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpmi6-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpmi6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpmi8-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpmi8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpr10-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpr10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpr12-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpr12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpr17-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpr17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpr6-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpr6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpr8-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpr8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpri10-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpri10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpri12-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpri12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpri17-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpri17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpri6-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpri6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpri8-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpri8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpb10-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpb10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpb12-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpb12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpb17-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpb17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpb6-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpb6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpb8-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpb8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpbi10-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpbi10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpbi12-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpbi12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpbi17-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpbi17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpbi6-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpbi6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpbi8-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpbi8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpl10-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpl10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpl12-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpl12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpl17-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpl17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpl6-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpl6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpl8-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpl8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpli10-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpli10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpli12-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpli12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpli17-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpli17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpli6-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpli6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpli8-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpli8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpm10-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpm10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpm12-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpm12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpm17-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpm17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpm6-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpm6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpm8-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpm8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpmi10-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpmi10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpmi12-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpmi12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpmi17-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpmi17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpmi6-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpmi6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpmi8-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpmi8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpr10-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpr10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpr12-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpr12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpr17-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpr17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpr6-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpr6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpr8-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpr8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpri10-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpri10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpri12-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpri12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpri17-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpri17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpri6-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpri6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpri8-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpri8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ts1-antpb10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ts1-antpb12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ts1-antpb17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ts1-antpb6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ts1-antpb8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ts1-antpbi10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ts1-antpbi12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ts1-antpbi17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ts1-antpbi6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ts1-antpbi8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ts1-antpl10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ts1-antpl12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ts1-antpl17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ts1-antpl6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ts1-antpl8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ts1-antpli10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ts1-antpli12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ts1-antpli17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ts1-antpli6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ts1-antpli8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ts1-antpm10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ts1-antpm12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ts1-antpm17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ts1-antpm6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ts1-antpm8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ts1-antpmi10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ts1-antpmi12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ts1-antpmi17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ts1-antpmi6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ts1-antpmi8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ts1-antpr10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ts1-antpr12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ts1-antpr17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ts1-antpr6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ts1-antpr8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ts1-antpri10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ts1-antpri12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ts1-antpri17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ts1-antpri6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ts1-antpri8.tfm
%verify(link) %{_texmfdistdir}/fonts/type1/gust/poltawski/antpb10.pfb
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpb10.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/gust/poltawski/antpb12.pfb
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpb12.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/gust/poltawski/antpb17.pfb
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpb17.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/gust/poltawski/antpb6.pfb
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpb6.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/gust/poltawski/antpb8.pfb
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpb8.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/gust/poltawski/antpbi10.pfb
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpbi10.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/gust/poltawski/antpbi12.pfb
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpbi12.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/gust/poltawski/antpbi17.pfb
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpbi17.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/gust/poltawski/antpbi6.pfb
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpbi6.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/gust/poltawski/antpbi8.pfb
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpbi8.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/gust/poltawski/antpl10.pfb
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpl10.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/gust/poltawski/antpl12.pfb
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpl12.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/gust/poltawski/antpl17.pfb
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpl17.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/gust/poltawski/antpl6.pfb
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpl6.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/gust/poltawski/antpl8.pfb
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpl8.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/gust/poltawski/antpli10.pfb
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpli10.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/gust/poltawski/antpli12.pfb
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpli12.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/gust/poltawski/antpli17.pfb
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpli17.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/gust/poltawski/antpli6.pfb
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpli6.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/gust/poltawski/antpli8.pfb
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpli8.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/gust/poltawski/antpm10.pfb
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpm10.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/gust/poltawski/antpm12.pfb
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpm12.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/gust/poltawski/antpm17.pfb
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpm17.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/gust/poltawski/antpm6.pfb
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpm6.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/gust/poltawski/antpm8.pfb
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpm8.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/gust/poltawski/antpmi10.pfb
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpmi10.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/gust/poltawski/antpmi12.pfb
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpmi12.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/gust/poltawski/antpmi17.pfb
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpmi17.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/gust/poltawski/antpmi6.pfb
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpmi6.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/gust/poltawski/antpmi8.pfb
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpmi8.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/gust/poltawski/antpr10.pfb
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpr10.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/gust/poltawski/antpr12.pfb
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpr12.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/gust/poltawski/antpr17.pfb
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpr17.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/gust/poltawski/antpr6.pfb
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpr6.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/gust/poltawski/antpr8.pfb
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpr8.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/gust/poltawski/antpri10.pfb
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpri10.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/gust/poltawski/antpri12.pfb
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpri12.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/gust/poltawski/antpri17.pfb
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpri17.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/gust/poltawski/antpri6.pfb
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpri6.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/gust/poltawski/antpri8.pfb
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpri8.pfm
%{_texmfdistdir}/tex/latex/poltawski/antpolt.sty
%{_texmfdistdir}/tex/latex/poltawski/il2antp.fd
%{_texmfdistdir}/tex/latex/poltawski/il2antpl.fd
%{_texmfdistdir}/tex/latex/poltawski/l7xantp.fd
%{_texmfdistdir}/tex/latex/poltawski/l7xantpl.fd
%{_texmfdistdir}/tex/latex/poltawski/ly1antp.fd
%{_texmfdistdir}/tex/latex/poltawski/ly1antpl.fd
%{_texmfdistdir}/tex/latex/poltawski/ot1antp.fd
%{_texmfdistdir}/tex/latex/poltawski/ot1antpl.fd
%{_texmfdistdir}/tex/latex/poltawski/ot4antp.fd
%{_texmfdistdir}/tex/latex/poltawski/ot4antpl.fd
%{_texmfdistdir}/tex/latex/poltawski/qxantp.fd
%{_texmfdistdir}/tex/latex/poltawski/qxantpl.fd
%{_texmfdistdir}/tex/latex/poltawski/t1antp.fd
%{_texmfdistdir}/tex/latex/poltawski/t1antpl.fd
%{_texmfdistdir}/tex/latex/poltawski/t5antp.fd
%{_texmfdistdir}/tex/latex/poltawski/t5antpl.fd
%{_texmfdistdir}/tex/latex/poltawski/ts1antp.fd
%{_texmfdistdir}/tex/latex/poltawski/ts1antpl.fd

%files -n texlive-poltawski-fonts
%defattr(-,root,root,755)
%dir %{_datadir}/fonts/texlive-poltawski
%{_datadir}/fontconfig/conf.avail/58-texlive-poltawski.conf
%{_datadir}/fontconfig/conf.avail/55-texlive-poltawski.conf
%config %{_sysconfdir}/fonts/conf.d/55-texlive-poltawski.conf
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-poltawski/encodings.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-poltawski/fonts.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-poltawski/fonts.scale
%{_datadir}/fonts/texlive-poltawski/antpolt-bold.otf
%{_datadir}/fonts/texlive-poltawski/antpolt-bolditalic.otf
%{_datadir}/fonts/texlive-poltawski/antpolt-italic.otf
%{_datadir}/fonts/texlive-poltawski/antpolt-regular.otf
%{_datadir}/fonts/texlive-poltawski/antpoltcond-bold.otf
%{_datadir}/fonts/texlive-poltawski/antpoltcond-bolditalic.otf
%{_datadir}/fonts/texlive-poltawski/antpoltcond-italic.otf
%{_datadir}/fonts/texlive-poltawski/antpoltcond-regular.otf
%{_datadir}/fonts/texlive-poltawski/antpoltexpd-bold.otf
%{_datadir}/fonts/texlive-poltawski/antpoltexpd-bolditalic.otf
%{_datadir}/fonts/texlive-poltawski/antpoltexpd-italic.otf
%{_datadir}/fonts/texlive-poltawski/antpoltexpd-regular.otf
%{_datadir}/fonts/texlive-poltawski/antpoltlt-bold.otf
%{_datadir}/fonts/texlive-poltawski/antpoltlt-bolditalic.otf
%{_datadir}/fonts/texlive-poltawski/antpoltlt-italic.otf
%{_datadir}/fonts/texlive-poltawski/antpoltlt-regular.otf
%{_datadir}/fonts/texlive-poltawski/antpoltltcond-bold.otf
%{_datadir}/fonts/texlive-poltawski/antpoltltcond-bolditalic.otf
%{_datadir}/fonts/texlive-poltawski/antpoltltcond-italic.otf
%{_datadir}/fonts/texlive-poltawski/antpoltltcond-regular.otf
%{_datadir}/fonts/texlive-poltawski/antpoltltexpd-bold.otf
%{_datadir}/fonts/texlive-poltawski/antpoltltexpd-bolditalic.otf
%{_datadir}/fonts/texlive-poltawski/antpoltltexpd-italic.otf
%{_datadir}/fonts/texlive-poltawski/antpoltltexpd-regular.otf
%{_datadir}/fonts/texlive-poltawski/antpoltltsemicond-bold.otf
%{_datadir}/fonts/texlive-poltawski/antpoltltsemicond-bolditalic.otf
%{_datadir}/fonts/texlive-poltawski/antpoltltsemicond-italic.otf
%{_datadir}/fonts/texlive-poltawski/antpoltltsemicond-regular.otf
%{_datadir}/fonts/texlive-poltawski/antpoltltsemiexpd-bold.otf
%{_datadir}/fonts/texlive-poltawski/antpoltltsemiexpd-bolditalic.otf
%{_datadir}/fonts/texlive-poltawski/antpoltltsemiexpd-italic.otf
%{_datadir}/fonts/texlive-poltawski/antpoltltsemiexpd-regular.otf
%{_datadir}/fonts/texlive-poltawski/antpoltsemicond-bold.otf
%{_datadir}/fonts/texlive-poltawski/antpoltsemicond-bolditalic.otf
%{_datadir}/fonts/texlive-poltawski/antpoltsemicond-italic.otf
%{_datadir}/fonts/texlive-poltawski/antpoltsemicond-regular.otf
%{_datadir}/fonts/texlive-poltawski/antpoltsemiexpd-bold.otf
%{_datadir}/fonts/texlive-poltawski/antpoltsemiexpd-bolditalic.otf
%{_datadir}/fonts/texlive-poltawski/antpoltsemiexpd-italic.otf
%{_datadir}/fonts/texlive-poltawski/antpoltsemiexpd-regular.otf
%{_datadir}/fonts/texlive-poltawski/antpb10.pfb
%{_datadir}/fonts/texlive-poltawski/antpb12.pfb
%{_datadir}/fonts/texlive-poltawski/antpb17.pfb
%{_datadir}/fonts/texlive-poltawski/antpb6.pfb
%{_datadir}/fonts/texlive-poltawski/antpb8.pfb
%{_datadir}/fonts/texlive-poltawski/antpbi10.pfb
%{_datadir}/fonts/texlive-poltawski/antpbi12.pfb
%{_datadir}/fonts/texlive-poltawski/antpbi17.pfb
%{_datadir}/fonts/texlive-poltawski/antpbi6.pfb
%{_datadir}/fonts/texlive-poltawski/antpbi8.pfb
%{_datadir}/fonts/texlive-poltawski/antpl10.pfb
%{_datadir}/fonts/texlive-poltawski/antpl12.pfb
%{_datadir}/fonts/texlive-poltawski/antpl17.pfb
%{_datadir}/fonts/texlive-poltawski/antpl6.pfb
%{_datadir}/fonts/texlive-poltawski/antpl8.pfb
%{_datadir}/fonts/texlive-poltawski/antpli10.pfb
%{_datadir}/fonts/texlive-poltawski/antpli12.pfb
%{_datadir}/fonts/texlive-poltawski/antpli17.pfb
%{_datadir}/fonts/texlive-poltawski/antpli6.pfb
%{_datadir}/fonts/texlive-poltawski/antpli8.pfb
%{_datadir}/fonts/texlive-poltawski/antpm10.pfb
%{_datadir}/fonts/texlive-poltawski/antpm12.pfb
%{_datadir}/fonts/texlive-poltawski/antpm17.pfb
%{_datadir}/fonts/texlive-poltawski/antpm6.pfb
%{_datadir}/fonts/texlive-poltawski/antpm8.pfb
%{_datadir}/fonts/texlive-poltawski/antpmi10.pfb
%{_datadir}/fonts/texlive-poltawski/antpmi12.pfb
%{_datadir}/fonts/texlive-poltawski/antpmi17.pfb
%{_datadir}/fonts/texlive-poltawski/antpmi6.pfb
%{_datadir}/fonts/texlive-poltawski/antpmi8.pfb
%{_datadir}/fonts/texlive-poltawski/antpr10.pfb
%{_datadir}/fonts/texlive-poltawski/antpr12.pfb
%{_datadir}/fonts/texlive-poltawski/antpr17.pfb
%{_datadir}/fonts/texlive-poltawski/antpr6.pfb
%{_datadir}/fonts/texlive-poltawski/antpr8.pfb
%{_datadir}/fonts/texlive-poltawski/antpri10.pfb
%{_datadir}/fonts/texlive-poltawski/antpri12.pfb
%{_datadir}/fonts/texlive-poltawski/antpri17.pfb
%{_datadir}/fonts/texlive-poltawski/antpri6.pfb
%{_datadir}/fonts/texlive-poltawski/antpri8.pfb

%package -n texlive-polyglossia
Version:        %{texlive_version}.%{texlive_noarch}.1.53svn58869
Release:        0
License:        LPPL-1.0
Summary:        An alternative to babel for XeLaTeX and LuaLaTeX
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires:       texlive-etoolbox >= %{texlive_version}
#!BuildIgnore: texlive-etoolbox
Requires:       texlive-filehook >= %{texlive_version}
#!BuildIgnore: texlive-filehook
Requires:       texlive-fontspec >= %{texlive_version}
#!BuildIgnore: texlive-fontspec
Requires:       texlive-iftex >= %{texlive_version}
#!BuildIgnore: texlive-iftex
Requires:       texlive-makecmds >= %{texlive_version}
#!BuildIgnore: texlive-makecmds
Requires:       texlive-xkeyval >= %{texlive_version}
#!BuildIgnore: texlive-xkeyval
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-polyglossia-doc >= %{texlive_version}
Provides:       tex(arabicdigits.map)
Provides:       tex(arabicnumbers.sty)
Provides:       tex(babel-hebrewalph.def)
Provides:       tex(babelsh.def)
Provides:       tex(bengalidigits.map)
Provides:       tex(bengalidigits.sty)
Provides:       tex(cal-util.def)
Provides:       tex(devanagaridigits.map)
Provides:       tex(devanagaridigits.sty)
Provides:       tex(farsical.sty)
Provides:       tex(farsidigits.map)
Provides:       tex(gloss-acadien.ldf)
Provides:       tex(gloss-aeb.ldf)
Provides:       tex(gloss-af.ldf)
Provides:       tex(gloss-afb.ldf)
Provides:       tex(gloss-afrikaans.ldf)
Provides:       tex(gloss-albanian.ldf)
Provides:       tex(gloss-am.ldf)
Provides:       tex(gloss-american.ldf)
Provides:       tex(gloss-amharic.ldf)
Provides:       tex(gloss-apd.ldf)
Provides:       tex(gloss-ar-IQ.ldf)
Provides:       tex(gloss-ar-JO.ldf)
Provides:       tex(gloss-ar-LB.ldf)
Provides:       tex(gloss-ar-MR.ldf)
Provides:       tex(gloss-ar-PS.ldf)
Provides:       tex(gloss-ar-SY.ldf)
Provides:       tex(gloss-ar-YE.ldf)
Provides:       tex(gloss-ar.ldf)
Provides:       tex(gloss-arabic.ldf)
Provides:       tex(gloss-armenian.ldf)
Provides:       tex(gloss-arq.ldf)
Provides:       tex(gloss-ary.ldf)
Provides:       tex(gloss-arz.ldf)
Provides:       tex(gloss-ast.ldf)
Provides:       tex(gloss-asturian.ldf)
Provides:       tex(gloss-australian.ldf)
Provides:       tex(gloss-austrian.ldf)
Provides:       tex(gloss-ayl.ldf)
Provides:       tex(gloss-bahasa.ldf)
Provides:       tex(gloss-bahasai.ldf)
Provides:       tex(gloss-bahasam.ldf)
Provides:       tex(gloss-basque.ldf)
Provides:       tex(gloss-be-tarask.ldf)
Provides:       tex(gloss-be.ldf)
Provides:       tex(gloss-belarusian.ldf)
Provides:       tex(gloss-bengali.ldf)
Provides:       tex(gloss-bg.ldf)
Provides:       tex(gloss-bn.ldf)
Provides:       tex(gloss-bo.ldf)
Provides:       tex(gloss-bosnian.ldf)
Provides:       tex(gloss-br.ldf)
Provides:       tex(gloss-brazil.ldf)
Provides:       tex(gloss-breton.ldf)
Provides:       tex(gloss-british.ldf)
Provides:       tex(gloss-bs.ldf)
Provides:       tex(gloss-bulgarian.ldf)
Provides:       tex(gloss-ca.ldf)
Provides:       tex(gloss-canadian.ldf)
Provides:       tex(gloss-canadien.ldf)
Provides:       tex(gloss-catalan.ldf)
Provides:       tex(gloss-ckb-Arab.ldf)
Provides:       tex(gloss-ckb-Latn.ldf)
Provides:       tex(gloss-ckb.ldf)
Provides:       tex(gloss-cop.ldf)
Provides:       tex(gloss-coptic.ldf)
Provides:       tex(gloss-croatian.ldf)
Provides:       tex(gloss-cy.ldf)
Provides:       tex(gloss-cz.ldf)
Provides:       tex(gloss-czech.ldf)
Provides:       tex(gloss-da.ldf)
Provides:       tex(gloss-danish.ldf)
Provides:       tex(gloss-de-AT-1901.ldf)
Provides:       tex(gloss-de-AT-1996.ldf)
Provides:       tex(gloss-de-AT.ldf)
Provides:       tex(gloss-de-CH-1901.ldf)
Provides:       tex(gloss-de-CH-1996.ldf)
Provides:       tex(gloss-de-CH.ldf)
Provides:       tex(gloss-de-DE-1901.ldf)
Provides:       tex(gloss-de-DE-1996.ldf)
Provides:       tex(gloss-de-DE.ldf)
Provides:       tex(gloss-de-Latf-AT-1901.ldf)
Provides:       tex(gloss-de-Latf-AT-1996.ldf)
Provides:       tex(gloss-de-Latf-AT.ldf)
Provides:       tex(gloss-de-Latf-CH-1901.ldf)
Provides:       tex(gloss-de-Latf-CH-1996.ldf)
Provides:       tex(gloss-de-Latf-CH.ldf)
Provides:       tex(gloss-de-Latf-DE-1901.ldf)
Provides:       tex(gloss-de-Latf-DE-1996.ldf)
Provides:       tex(gloss-de-Latf-DE.ldf)
Provides:       tex(gloss-de-Latf.ldf)
Provides:       tex(gloss-de.ldf)
Provides:       tex(gloss-divehi.ldf)
Provides:       tex(gloss-dsb.ldf)
Provides:       tex(gloss-dutch.ldf)
Provides:       tex(gloss-dv.ldf)
Provides:       tex(gloss-el-monoton.ldf)
Provides:       tex(gloss-el-polyton.ldf)
Provides:       tex(gloss-el.ldf)
Provides:       tex(gloss-en-AU.ldf)
Provides:       tex(gloss-en-CA.ldf)
Provides:       tex(gloss-en-GB.ldf)
Provides:       tex(gloss-en-NZ.ldf)
Provides:       tex(gloss-en-US.ldf)
Provides:       tex(gloss-en.ldf)
Provides:       tex(gloss-english.ldf)
Provides:       tex(gloss-eo.ldf)
Provides:       tex(gloss-es-ES.ldf)
Provides:       tex(gloss-es-MX.ldf)
Provides:       tex(gloss-es.ldf)
Provides:       tex(gloss-esperanto.ldf)
Provides:       tex(gloss-estonian.ldf)
Provides:       tex(gloss-et.ldf)
Provides:       tex(gloss-eu.ldf)
Provides:       tex(gloss-fa.ldf)
Provides:       tex(gloss-farsi.ldf)
Provides:       tex(gloss-fi.ldf)
Provides:       tex(gloss-finnish.ldf)
Provides:       tex(gloss-fr-CA.ldf)
Provides:       tex(gloss-fr-CH.ldf)
Provides:       tex(gloss-fr-FR.ldf)
Provides:       tex(gloss-fr.ldf)
Provides:       tex(gloss-french.ldf)
Provides:       tex(gloss-friulan.ldf)
Provides:       tex(gloss-friulian.ldf)
Provides:       tex(gloss-fur.ldf)
Provides:       tex(gloss-ga.ldf)
Provides:       tex(gloss-gaelic.ldf)
Provides:       tex(gloss-galician.ldf)
Provides:       tex(gloss-gd.ldf)
Provides:       tex(gloss-georgian.ldf)
Provides:       tex(gloss-german.ldf)
Provides:       tex(gloss-germanb.ldf)
Provides:       tex(gloss-gl.ldf)
Provides:       tex(gloss-grc.ldf)
Provides:       tex(gloss-greek.ldf)
Provides:       tex(gloss-he.ldf)
Provides:       tex(gloss-hebrew.ldf)
Provides:       tex(gloss-hi.ldf)
Provides:       tex(gloss-hindi.ldf)
Provides:       tex(gloss-hr.ldf)
Provides:       tex(gloss-hsb.ldf)
Provides:       tex(gloss-hu.ldf)
Provides:       tex(gloss-hungarian.ldf)
Provides:       tex(gloss-hy.ldf)
Provides:       tex(gloss-ia.ldf)
Provides:       tex(gloss-icelandic.ldf)
Provides:       tex(gloss-id.ldf)
Provides:       tex(gloss-interlingua.ldf)
Provides:       tex(gloss-irish.ldf)
Provides:       tex(gloss-is.ldf)
Provides:       tex(gloss-it.ldf)
Provides:       tex(gloss-italian.ldf)
Provides:       tex(gloss-ja.ldf)
Provides:       tex(gloss-japanese.ldf)
Provides:       tex(gloss-ka.ldf)
Provides:       tex(gloss-kannada.ldf)
Provides:       tex(gloss-khmer.ldf)
Provides:       tex(gloss-km.ldf)
Provides:       tex(gloss-kmr-Arab.ldf)
Provides:       tex(gloss-kmr-Latn.ldf)
Provides:       tex(gloss-kmr.ldf)
Provides:       tex(gloss-kn.ldf)
Provides:       tex(gloss-ko.ldf)
Provides:       tex(gloss-korean.ldf)
Provides:       tex(gloss-ku-Arab.ldf)
Provides:       tex(gloss-ku-Latn.ldf)
Provides:       tex(gloss-ku.ldf)
Provides:       tex(gloss-kurdish.ldf)
Provides:       tex(gloss-kurmanji.ldf)
Provides:       tex(gloss-la-x-classic.ldf)
Provides:       tex(gloss-la-x-ecclesia.ldf)
Provides:       tex(gloss-la-x-medieval.ldf)
Provides:       tex(gloss-la.ldf)
Provides:       tex(gloss-lao.ldf)
Provides:       tex(gloss-latex.ldf)
Provides:       tex(gloss-latin.ldf)
Provides:       tex(gloss-latinclassic.ldf)
Provides:       tex(gloss-latinecclesiastic.ldf)
Provides:       tex(gloss-latinmedieval.ldf)
Provides:       tex(gloss-latvian.ldf)
Provides:       tex(gloss-lithuanian.ldf)
Provides:       tex(gloss-lo.ldf)
Provides:       tex(gloss-lowersorbian.ldf)
Provides:       tex(gloss-lsorbian.ldf)
Provides:       tex(gloss-lt.ldf)
Provides:       tex(gloss-lv.ldf)
Provides:       tex(gloss-macedonian.ldf)
Provides:       tex(gloss-magyar.ldf)
Provides:       tex(gloss-malay.ldf)
Provides:       tex(gloss-malayalam.ldf)
Provides:       tex(gloss-marathi.ldf)
Provides:       tex(gloss-mk.ldf)
Provides:       tex(gloss-ml.ldf)
Provides:       tex(gloss-mn.ldf)
Provides:       tex(gloss-mongolian.ldf)
Provides:       tex(gloss-mr.ldf)
Provides:       tex(gloss-naustrian.ldf)
Provides:       tex(gloss-nb.ldf)
Provides:       tex(gloss-newzealand.ldf)
Provides:       tex(gloss-ngerman.ldf)
Provides:       tex(gloss-nko.ldf)
Provides:       tex(gloss-norsk.ldf)
Provides:       tex(gloss-norwegian.ldf)
Provides:       tex(gloss-nswissgerman.ldf)
Provides:       tex(gloss-nynorsk.ldf)
Provides:       tex(gloss-occitan.ldf)
Provides:       tex(gloss-persian.ldf)
Provides:       tex(gloss-piedmontese.ldf)
Provides:       tex(gloss-polish.ldf)
Provides:       tex(gloss-polutonikogreek.ldf)
Provides:       tex(gloss-portuges.ldf)
Provides:       tex(gloss-portuguese.ldf)
Provides:       tex(gloss-romanian.ldf)
Provides:       tex(gloss-romansh.ldf)
Provides:       tex(gloss-russian.ldf)
Provides:       tex(gloss-sami.ldf)
Provides:       tex(gloss-samin.ldf)
Provides:       tex(gloss-sanskrit.ldf)
Provides:       tex(gloss-scottish.ldf)
Provides:       tex(gloss-serbian.ldf)
Provides:       tex(gloss-serbianc.ldf)
Provides:       tex(gloss-slovak.ldf)
Provides:       tex(gloss-slovene.ldf)
Provides:       tex(gloss-slovenian.ldf)
Provides:       tex(gloss-sorbian.ldf)
Provides:       tex(gloss-spanish.ldf)
Provides:       tex(gloss-spanishmx.ldf)
Provides:       tex(gloss-swedish.ldf)
Provides:       tex(gloss-swissgerman.ldf)
Provides:       tex(gloss-syriac.ldf)
Provides:       tex(gloss-tamil.ldf)
Provides:       tex(gloss-telugu.ldf)
Provides:       tex(gloss-thai.ldf)
Provides:       tex(gloss-tibetan.ldf)
Provides:       tex(gloss-turkish.ldf)
Provides:       tex(gloss-turkmen.ldf)
Provides:       tex(gloss-ug.ldf)
Provides:       tex(gloss-ukrainian.ldf)
Provides:       tex(gloss-uppersorbian.ldf)
Provides:       tex(gloss-urdu.ldf)
Provides:       tex(gloss-usorbian.ldf)
Provides:       tex(gloss-uyghur.ldf)
Provides:       tex(gloss-vietnamese.ldf)
Provides:       tex(gloss-welsh.ldf)
Provides:       tex(hebrewcal.sty)
Provides:       tex(hijrical.sty)
Provides:       tex(nkonumbers.sty)
Provides:       tex(polyglossia.sty)
Provides:       tex(thaidigits.map)
Provides:       tex(xgreek-fixes.def)
Provides:       tex(xpg-cyrillicnumbers.sty)
Requires:       tex(bidi.sty)
Requires:       tex(calc.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(expl3.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(iftex.sty)
Requires:       tex(l3keys2e.sty)
Requires:       tex(luabidi.sty)
Requires:       tex(luatexbase.sty)
Requires:       tex(makecmds.sty)
Requires:       tex(xkeyval.sty)
Requires:       tex(xparse.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source57:       polyglossia.tar.xz
Source58:       polyglossia.doc.tar.xz

%description -n texlive-polyglossia
This package provides a complete Babel replacement for users of
LuaLaTeX and XeLaTeX; it relies on the fontspec package,
version 2.0 at least.

%package -n texlive-polyglossia-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.53svn58869
Release:        0
Summary:        Documentation for texlive-polyglossia
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/

%description -n texlive-polyglossia-doc
This package includes the documentation for texlive-polyglossia

%post -n texlive-polyglossia
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-polyglossia
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-polyglossia
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-polyglossia-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/polyglossia/README.md
%{_texmfdistdir}/doc/latex/polyglossia/example-arabic.pdf
%{_texmfdistdir}/doc/latex/polyglossia/example-arabic.tex
%{_texmfdistdir}/doc/latex/polyglossia/example-korean.pdf
%{_texmfdistdir}/doc/latex/polyglossia/example-korean.tex
%{_texmfdistdir}/doc/latex/polyglossia/example-thai.pdf
%{_texmfdistdir}/doc/latex/polyglossia/example-thai.tex
%{_texmfdistdir}/doc/latex/polyglossia/examples.pdf
%{_texmfdistdir}/doc/latex/polyglossia/examples.tex
%{_texmfdistdir}/doc/latex/polyglossia/polyglossia.pdf
%{_texmfdistdir}/doc/latex/polyglossia/polyglossia.tex
%{_texmfdistdir}/doc/latex/polyglossia/test-welsh.pdf
%{_texmfdistdir}/doc/latex/polyglossia/test-welsh.tex

%files -n texlive-polyglossia
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/polyglossia/arabicdigits.map
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/polyglossia/arabicdigits.tec
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/polyglossia/bengalidigits.map
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/polyglossia/bengalidigits.tec
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/polyglossia/devanagaridigits.map
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/polyglossia/devanagaridigits.tec
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/polyglossia/farsidigits.map
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/polyglossia/farsidigits.tec
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/polyglossia/thaidigits.map
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/polyglossia/thaidigits.tec
%{_texmfdistdir}/tex/latex/polyglossia/arabicnumbers.sty
%{_texmfdistdir}/tex/latex/polyglossia/babel-hebrewalph.def
%{_texmfdistdir}/tex/latex/polyglossia/babelsh.def
%{_texmfdistdir}/tex/latex/polyglossia/bengalidigits.sty
%{_texmfdistdir}/tex/latex/polyglossia/cal-util.def
%{_texmfdistdir}/tex/latex/polyglossia/devanagaridigits.sty
%{_texmfdistdir}/tex/latex/polyglossia/farsical.sty
%{_texmfdistdir}/tex/latex/polyglossia/gloss-acadien.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-aeb.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-af.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-afb.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-afrikaans.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-albanian.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-am.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-american.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-amharic.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-apd.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-ar-IQ.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-ar-JO.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-ar-LB.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-ar-MR.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-ar-PS.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-ar-SY.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-ar-YE.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-ar.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-arabic.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-armenian.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-arq.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-ary.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-arz.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-ast.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-asturian.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-australian.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-austrian.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-ayl.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-bahasa.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-bahasai.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-bahasam.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-basque.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-be-tarask.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-be.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-belarusian.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-bengali.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-bg.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-bn.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-bo.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-bosnian.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-br.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-brazil.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-breton.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-british.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-bs.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-bulgarian.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-ca.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-canadian.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-canadien.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-catalan.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-ckb-Arab.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-ckb-Latn.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-ckb.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-cop.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-coptic.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-croatian.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-cy.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-cz.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-czech.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-da.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-danish.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-de-AT-1901.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-de-AT-1996.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-de-AT.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-de-CH-1901.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-de-CH-1996.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-de-CH.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-de-DE-1901.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-de-DE-1996.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-de-DE.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-de-Latf-AT-1901.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-de-Latf-AT-1996.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-de-Latf-AT.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-de-Latf-CH-1901.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-de-Latf-CH-1996.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-de-Latf-CH.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-de-Latf-DE-1901.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-de-Latf-DE-1996.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-de-Latf-DE.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-de-Latf.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-de.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-divehi.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-dsb.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-dutch.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-dv.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-el-monoton.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-el-polyton.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-el.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-en-AU.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-en-CA.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-en-GB.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-en-NZ.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-en-US.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-en.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-english.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-eo.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-es-ES.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-es-MX.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-es.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-esperanto.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-estonian.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-et.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-eu.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-fa.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-farsi.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-fi.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-finnish.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-fr-CA.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-fr-CH.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-fr-FR.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-fr.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-french.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-friulan.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-friulian.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-fur.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-ga.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-gaelic.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-galician.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-gd.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-georgian.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-german.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-germanb.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-gl.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-grc.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-greek.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-he.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-hebrew.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-hi.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-hindi.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-hr.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-hsb.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-hu.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-hungarian.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-hy.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-ia.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-icelandic.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-id.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-interlingua.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-irish.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-is.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-it.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-italian.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-ja.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-japanese.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-ka.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-kannada.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-khmer.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-km.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-kmr-Arab.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-kmr-Latn.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-kmr.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-kn.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-ko.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-korean.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-ku-Arab.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-ku-Latn.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-ku.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-kurdish.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-kurmanji.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-la-x-classic.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-la-x-ecclesia.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-la-x-medieval.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-la.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-lao.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-latex.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-latin.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-latinclassic.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-latinecclesiastic.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-latinmedieval.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-latvian.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-lithuanian.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-lo.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-lowersorbian.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-lsorbian.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-lt.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-lv.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-macedonian.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-magyar.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-malay.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-malayalam.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-marathi.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-mk.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-ml.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-mn.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-mongolian.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-mr.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-naustrian.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-nb.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-newzealand.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-ngerman.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-nko.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-norsk.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-norwegian.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-nswissgerman.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-nynorsk.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-occitan.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-persian.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-piedmontese.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-polish.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-polutonikogreek.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-portuges.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-portuguese.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-romanian.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-romansh.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-russian.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-sami.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-samin.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-sanskrit.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-scottish.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-serbian.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-serbianc.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-slovak.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-slovene.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-slovenian.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-sorbian.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-spanish.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-spanishmx.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-swedish.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-swissgerman.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-syriac.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-tamil.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-telugu.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-thai.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-tibetan.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-turkish.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-turkmen.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-ug.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-ukrainian.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-uppersorbian.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-urdu.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-usorbian.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-uyghur.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-vietnamese.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-welsh.ldf
%{_texmfdistdir}/tex/latex/polyglossia/hebrewcal.sty
%{_texmfdistdir}/tex/latex/polyglossia/hijrical.sty
%{_texmfdistdir}/tex/latex/polyglossia/nkonumbers.sty
%{_texmfdistdir}/tex/latex/polyglossia/polyglossia-french.lua
%{_texmfdistdir}/tex/latex/polyglossia/polyglossia-korean.lua
%{_texmfdistdir}/tex/latex/polyglossia/polyglossia-latin.lua
%{_texmfdistdir}/tex/latex/polyglossia/polyglossia-punct.lua
%{_texmfdistdir}/tex/latex/polyglossia/polyglossia-sanskrit.lua
%{_texmfdistdir}/tex/latex/polyglossia/polyglossia-tibt.lua
%{_texmfdistdir}/tex/latex/polyglossia/polyglossia.lua
%{_texmfdistdir}/tex/latex/polyglossia/polyglossia.sty
%{_texmfdistdir}/tex/latex/polyglossia/xgreek-fixes.def
%{_texmfdistdir}/tex/latex/polyglossia/xpg-cyrillicnumbers.sty

%package -n texlive-polynom
Version:        %{texlive_version}.%{texlive_noarch}.0.0.19svn44832
Release:        0
License:        LPPL-1.0
Summary:        Macros for manipulating polynomials
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-polynom-doc >= %{texlive_version}
Provides:       tex(polynom.sty)
Requires:       tex(keyval.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source59:       polynom.tar.xz
Source60:       polynom.doc.tar.xz

%description -n texlive-polynom
The polynom package implements macros for manipulating
polynomials, for example it can typeset long polynomial
divisions. The main test case and application is the polynomial
ring in one variable with rational coefficients.

%package -n texlive-polynom-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.19svn44832
Release:        0
Summary:        Documentation for texlive-polynom
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/

%description -n texlive-polynom-doc
This package includes the documentation for texlive-polynom

%post -n texlive-polynom
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-polynom
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-polynom
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-polynom-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/polynom/README
%{_texmfdistdir}/doc/latex/polynom/polydemo.pdf
%{_texmfdistdir}/doc/latex/polynom/polydemo.tex
%{_texmfdistdir}/doc/latex/polynom/polynom.pdf

%files -n texlive-polynom
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/polynom/polynom.sty

%package -n texlive-polynomial
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn15878
Release:        0
License:        LPPL-1.0
Summary:        Typeset (univariate) polynomials
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-polynomial-doc >= %{texlive_version}
Provides:       tex(polynomial.sty)
Requires:       tex(keyval.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source61:       polynomial.tar.xz
Source62:       polynomial.doc.tar.xz

%description -n texlive-polynomial
The package offers an easy way to write (univariate)
polynomials and rational functions. It defines two commands,
one for polynomials \polynomial{coeffs} and one for rational
functions \polynomialfrac{Numerator}{Denominator}. Both
commands take lists of coefficients as arguments, and offer
limited optional behaviour.

%package -n texlive-polynomial-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn15878
Release:        0
Summary:        Documentation for texlive-polynomial
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/

%description -n texlive-polynomial-doc
This package includes the documentation for texlive-polynomial

%post -n texlive-polynomial
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-polynomial
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-polynomial
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-polynomial-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/polynomial/README
%{_texmfdistdir}/doc/latex/polynomial/polynomial.pdf

%files -n texlive-polynomial
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/polynomial/polynomial.sty

%package -n texlive-polytable
Version:        %{texlive_version}.%{texlive_noarch}.0.0.8.6svn55837
Release:        0
License:        LPPL-1.0
Summary:        Tabular-like environments with named columns
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-polytable-doc >= %{texlive_version}
Provides:       tex(polytable.sty)
Requires:       tex(array.sty)
Requires:       tex(lazylist.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source63:       polytable.tar.xz
Source64:       polytable.doc.tar.xz

%description -n texlive-polytable
This package implements a variant of tabular-like environments
where columns can be given a name and entries can flexibly be
placed between arbitrary columns. Complex alignment-based
layouts, for example for program code, are possible. The
package depends on lazylist.

%package -n texlive-polytable-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.8.6svn55837
Release:        0
Summary:        Documentation for texlive-polytable
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/

%description -n texlive-polytable-doc
This package includes the documentation for texlive-polytable

%post -n texlive-polytable
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-polytable
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-polytable
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-polytable-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/polytable/README
%{_texmfdistdir}/doc/latex/polytable/polytable.pdf

%files -n texlive-polytable
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/polytable/polytable.sty

%package -n texlive-poormanlog
Version:        %{texlive_version}.%{texlive_noarch}.0.0.06svn61719
Release:        0
License:        LPPL-1.0
Summary:        Logarithms and powers with (almost) 9 digits
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-poormanlog-doc >= %{texlive_version}
Provides:       tex(poormanlog.sty)
Provides:       tex(poormanlog.tex)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source65:       poormanlog.tar.xz
Source66:       poormanlog.doc.tar.xz

%description -n texlive-poormanlog
This small package (usable with Plain e-TeX, LaTeX, or others)
with no dependencies provides two fast expandable macros
computing logarithms in base 10 and fractional powers of 10.
They handle arguments of 9 digit tokens which stand for either
1 <= d.dddddddd < 10 (for the log) or 0.xxxxxxxxx (for powers
of 10). They achieve a precision of 1ulp for the logarithm and
2ulp for fractional powers of ten. Extension to other numerical
ranges has to be done by user, via own macros or some math
engine. The xintexpr package (at 1.3f) imports the poormanlog
macros as core constituents of its log10(), pow10(), log(),
exp() and pow() functions.

%package -n texlive-poormanlog-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.06svn61719
Release:        0
Summary:        Documentation for texlive-poormanlog
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/

%description -n texlive-poormanlog-doc
This package includes the documentation for texlive-poormanlog

%post -n texlive-poormanlog
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-poormanlog
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-poormanlog
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-poormanlog-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/poormanlog/README

%files -n texlive-poormanlog
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/poormanlog/poormanlog.sty
%{_texmfdistdir}/tex/generic/poormanlog/poormanlog.tex

%package -n texlive-postage
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn55920
Release:        0
License:        LPPL-1.0
Summary:        Stamp letters with >>Deutsche Post<<'s service >>Internetmarke<<
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-postage-doc >= %{texlive_version}
Provides:       tex(postage.sty)
Requires:       tex(calc.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(keyval.sty)
Requires:       tex(tikz.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source67:       postage.tar.xz
Source68:       postage.doc.tar.xz

%description -n texlive-postage
The postage package is used for franking letters with
>>Deutsche Post<<'s online postage service >>Internetmarke<<.
Note that in order to print valid stamps you must point to a
valid PDF of >>Deutsche Post<<'s >>Ausdruck 4-spaltig (DIN
A4)<<.

%package -n texlive-postage-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn55920
Release:        0
Summary:        Documentation for texlive-postage
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/

%description -n texlive-postage-doc
This package includes the documentation for texlive-postage

%post -n texlive-postage
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-postage
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-postage
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-postage-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/postage/README.txt
%{_texmfdistdir}/doc/latex/postage/postage.pdf
%{_texmfdistdir}/doc/latex/postage/sample-stamps.pdf

%files -n texlive-postage
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/postage/postage.sty

%package -n texlive-postcards
Version:        %{texlive_version}.%{texlive_noarch}.svn21641
Release:        0
License:        LPPL-1.0
Summary:        Facilitates mass-mailing of postcards (junkmail)
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-postcards-doc >= %{texlive_version}
Provides:       tex(postcards.cls)
Requires:       tex(letter.cls)
Requires:       tex(mailing.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source69:       postcards.tar.xz
Source70:       postcards.doc.tar.xz

%description -n texlive-postcards
A modification of the standard LaTeX letter class which prints
multiple, pre-stamped, 5.5" by 3.5" postcards (a US standard
size) via the envlab and mailing packages. An address database
is employed to address the front side of each postcard and a
message is printed on the back side of all. An illustrative
example is provided.

%package -n texlive-postcards-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn21641
Release:        0
Summary:        Documentation for texlive-postcards
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/

%description -n texlive-postcards-doc
This package includes the documentation for texlive-postcards

%post -n texlive-postcards
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-postcards
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-postcards
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-postcards-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/postcards/README
%{_texmfdistdir}/doc/latex/postcards/datasmp.txt
%{_texmfdistdir}/doc/latex/postcards/pcardsmp.tex

%files -n texlive-postcards
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/postcards/postcards.cls

%package -n texlive-poster-mac
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn18305
Release:        0
License:        LPPL-1.0
Summary:        Make posters and banners with TeX
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-poster-mac-doc >= %{texlive_version}
Provides:       tex(poster.sty)
Provides:       tex(poster.tex)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source71:       poster-mac.tar.xz
Source72:       poster-mac.doc.tar.xz

%description -n texlive-poster-mac
The package offers macros for making posters and banners with
TeX. It is compatible with most TeX macro formats, including
Plain TeX, LaTeX, AmSTeX, and AmS-LaTeX. The package creates a
poster as huge box, which is then distributed over as many
printer pages as necessary. The only special requirement is
that your printer not be bothered by text that lies off the
page. This is true of most printers, including laser printers
and PostScript printers.

%package -n texlive-poster-mac-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn18305
Release:        0
Summary:        Documentation for texlive-poster-mac
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/

%description -n texlive-poster-mac-doc
This package includes the documentation for texlive-poster-mac

%post -n texlive-poster-mac
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-poster-mac
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-poster-mac
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-poster-mac-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/poster-mac/Changes
%{_texmfdistdir}/doc/generic/poster-mac/Makefile
%{_texmfdistdir}/doc/generic/poster-mac/README
%{_texmfdistdir}/doc/generic/poster-mac/poster-doc.pdf
%{_texmfdistdir}/doc/generic/poster-mac/poster-doc.tex
%{_texmfdistdir}/doc/generic/poster-mac/poster1.pdf
%{_texmfdistdir}/doc/generic/poster-mac/poster2.pdf

%files -n texlive-poster-mac
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/poster-mac/poster.sty
%{_texmfdistdir}/tex/generic/poster-mac/poster.tex

%package -n texlive-powerdot
Version:        %{texlive_version}.%{texlive_noarch}.1.7svn59272
Release:        0
License:        LPPL-1.0
Summary:        A presentation class
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-powerdot-doc >= %{texlive_version}
Provides:       tex(powerdot-aggie.sty)
Provides:       tex(powerdot-bframe.sty)
Provides:       tex(powerdot-ciment.sty)
Provides:       tex(powerdot-default.sty)
Provides:       tex(powerdot-elcolors.sty)
Provides:       tex(powerdot-fyma.sty)
Provides:       tex(powerdot-horatio.sty)
Provides:       tex(powerdot-husky.sty)
Provides:       tex(powerdot-ikeda.sty)
Provides:       tex(powerdot-jefka.sty)
Provides:       tex(powerdot-klope.sty)
Provides:       tex(powerdot-paintings.sty)
Provides:       tex(powerdot-pazik.sty)
Provides:       tex(powerdot-sailor.sty)
Provides:       tex(powerdot-simple.sty)
Provides:       tex(powerdot-tycja.sty)
Provides:       tex(powerdot-upen.sty)
Provides:       tex(powerdot.cls)
Requires:       tex(amssymb.sty)
Requires:       tex(article.cls)
Requires:       tex(calc.sty)
Requires:       tex(enumitem.sty)
Requires:       tex(geometry.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(pdfbase.sty)
Requires:       tex(pifont.sty)
Requires:       tex(pst-blur.sty)
Requires:       tex(pst-char.sty)
Requires:       tex(pst-grad.sty)
Requires:       tex(pst-ovl.sty)
Requires:       tex(pst-slpe.sty)
Requires:       tex(pstricks.sty)
Requires:       tex(times.sty)
Requires:       tex(type1cm.sty)
Requires:       tex(verbatim.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xkeyval.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source73:       powerdot.tar.xz
Source74:       powerdot.doc.tar.xz

%description -n texlive-powerdot
Powerdot is a presentation class for LaTeX that allows for the
quick and easy development of professional presentations. It
comes with many tools that enhance presentations and aid the
presenter. Examples are automatic overlays, personal notes and
a handout mode. To view a presentation, DVI, PS or PDF output
can be used. A powerful template system is available to easily
develop new styles. A LyX layout file is provided.

%package -n texlive-powerdot-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.7svn59272
Release:        0
Summary:        Documentation for texlive-powerdot
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Provides:       locale(texlive-powerdot-doc:en;de)

%description -n texlive-powerdot-doc
This package includes the documentation for texlive-powerdot

%post -n texlive-powerdot
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-powerdot
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-powerdot
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-powerdot-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/powerdot/README
%{_texmfdistdir}/doc/latex/powerdot/manifest.txt
%{_texmfdistdir}/doc/latex/powerdot/pdpream.ble
%{_texmfdistdir}/doc/latex/powerdot/powerdot-example.lyx
%{_texmfdistdir}/doc/latex/powerdot/powerdot-example.tex
%{_texmfdistdir}/doc/latex/powerdot/powerdot-example1.tex
%{_texmfdistdir}/doc/latex/powerdot/powerdot-example2.tex
%{_texmfdistdir}/doc/latex/powerdot/powerdot-example3.tex
%{_texmfdistdir}/doc/latex/powerdot/powerdot-styleexample.tex
%{_texmfdistdir}/doc/latex/powerdot/powerdot-styletest.tex
%{_texmfdistdir}/doc/latex/powerdot/powerdot.bib
%{_texmfdistdir}/doc/latex/powerdot/powerdot.layout
%{_texmfdistdir}/doc/latex/powerdot/powerdot.pdf
%{_texmfdistdir}/doc/latex/powerdot/powerdotDE.pdf
%{_texmfdistdir}/doc/latex/powerdot/powerdotDE.tex

%files -n texlive-powerdot
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/powerdot/powerdot-aggie.sty
%{_texmfdistdir}/tex/latex/powerdot/powerdot-bframe.sty
%{_texmfdistdir}/tex/latex/powerdot/powerdot-ciment.sty
%{_texmfdistdir}/tex/latex/powerdot/powerdot-default.ps
%{_texmfdistdir}/tex/latex/powerdot/powerdot-default.sty
%{_texmfdistdir}/tex/latex/powerdot/powerdot-elcolors.sty
%{_texmfdistdir}/tex/latex/powerdot/powerdot-fyma.sty
%{_texmfdistdir}/tex/latex/powerdot/powerdot-horatio.sty
%{_texmfdistdir}/tex/latex/powerdot/powerdot-husky.sty
%{_texmfdistdir}/tex/latex/powerdot/powerdot-ikeda.sty
%{_texmfdistdir}/tex/latex/powerdot/powerdot-jefka.sty
%{_texmfdistdir}/tex/latex/powerdot/powerdot-klope.sty
%{_texmfdistdir}/tex/latex/powerdot/powerdot-paintings.sty
%{_texmfdistdir}/tex/latex/powerdot/powerdot-pazik.sty
%{_texmfdistdir}/tex/latex/powerdot/powerdot-sailor.sty
%{_texmfdistdir}/tex/latex/powerdot/powerdot-simple.sty
%{_texmfdistdir}/tex/latex/powerdot/powerdot-tycja.sty
%{_texmfdistdir}/tex/latex/powerdot/powerdot-upen.sty
%{_texmfdistdir}/tex/latex/powerdot/powerdot.cls

%package -n texlive-powerdot-fuberlin
Version:        %{texlive_version}.%{texlive_noarch}.0.0.02asvn52922
Release:        0
License:        LPPL-1.0
Summary:        Powerdot, using the style of FU Berlin
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-powerdot-fuberlin-doc >= %{texlive_version}
Provides:       tex(FUpowerdot.cls)
Provides:       tex(powerdot-BerlinFU.sty)
Requires:       tex(babel.sty)
Requires:       tex(breakurl.sty)
Requires:       tex(calc.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(helvet.sty)
Requires:       tex(pifont.sty)
Requires:       tex(powerdot.cls)
Requires:       tex(ragged2e.sty)
Requires:       tex(tabularx.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source75:       powerdot-fuberlin.tar.xz
Source76:       powerdot-fuberlin.doc.tar.xz

%description -n texlive-powerdot-fuberlin
The bundle provides a powerdot-derived class and a package for
use with powerdot to provide the corporate design of the Free
University in Berlin. Users may use the class itself
(FUpowerdot) or use the package in the usual way with
\style=BerlinFU as a class option. Examples of using both the
class and the package are provided; the PDF is visually
identical, so the catalogue only lists one; the sources of the
examples do of course differ.

%package -n texlive-powerdot-fuberlin-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.02asvn52922
Release:        0
Summary:        Documentation for texlive-powerdot-fuberlin
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/

%description -n texlive-powerdot-fuberlin-doc
This package includes the documentation for texlive-powerdot-fuberlin

%post -n texlive-powerdot-fuberlin
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-powerdot-fuberlin
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-powerdot-fuberlin
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-powerdot-fuberlin-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/powerdot-fuberlin/Changes
%{_texmfdistdir}/doc/latex/powerdot-fuberlin/README
%{_texmfdistdir}/doc/latex/powerdot-fuberlin/demo-powerdotFU.pdf
%{_texmfdistdir}/doc/latex/powerdot-fuberlin/demo-powerdotFU.tex
%{_texmfdistdir}/doc/latex/powerdot-fuberlin/exampleClass.pdf
%{_texmfdistdir}/doc/latex/powerdot-fuberlin/exampleClass.tex
%{_texmfdistdir}/doc/latex/powerdot-fuberlin/exampleStyle.pdf
%{_texmfdistdir}/doc/latex/powerdot-fuberlin/exampleStyle.tex

%files -n texlive-powerdot-fuberlin
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/powerdot-fuberlin/FUpowerdot.cls
%{_texmfdistdir}/tex/latex/powerdot-fuberlin/powerdot-BerlinFU.sty

%package -n texlive-powerdot-tuliplab
Version:        %{texlive_version}.%{texlive_noarch}.1.0.0svn47963
Release:        0
License:        LPPL-1.0
Summary:        A style package for Powerdot to provide the design of TULIP Lab
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-powerdot-tuliplab-doc >= %{texlive_version}
Provides:       tex(powerdot-tuliplab.sty)
Requires:       tex(pifont.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source77:       powerdot-tuliplab.tar.xz
Source78:       powerdot-tuliplab.doc.tar.xz

%description -n texlive-powerdot-tuliplab
powerdot-tuliplab is the LaTeX package used in TULIP Lab for
presentation drafting. It comes with several sample .tex files
so that you can quickly start working with it.

%package -n texlive-powerdot-tuliplab-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0.0svn47963
Release:        0
Summary:        Documentation for texlive-powerdot-tuliplab
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/

%description -n texlive-powerdot-tuliplab-doc
This package includes the documentation for texlive-powerdot-tuliplab

%post -n texlive-powerdot-tuliplab
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-powerdot-tuliplab
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-powerdot-tuliplab
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-powerdot-tuliplab-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/powerdot-tuliplab/README.md
%{_texmfdistdir}/doc/latex/powerdot-tuliplab/tuliplab-P00.tex
%{_texmfdistdir}/doc/latex/powerdot-tuliplab/tuliplab-P01.tex
%{_texmfdistdir}/doc/latex/powerdot-tuliplab/tuliplab-P02.tex

%files -n texlive-powerdot-tuliplab
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/powerdot-tuliplab/logos/tulip-logo.eps
%{_texmfdistdir}/tex/latex/powerdot-tuliplab/logos/tulip-wordmark.eps
%{_texmfdistdir}/tex/latex/powerdot-tuliplab/logos/tulip.eps
%{_texmfdistdir}/tex/latex/powerdot-tuliplab/logos/tulip/tulip-wordmark0.eps
%{_texmfdistdir}/tex/latex/powerdot-tuliplab/logos/tulip/tulip-wordmark1.eps
%{_texmfdistdir}/tex/latex/powerdot-tuliplab/logos/tulip/tulip0.eps
%{_texmfdistdir}/tex/latex/powerdot-tuliplab/logos/tulip/tulip1.eps
%{_texmfdistdir}/tex/latex/powerdot-tuliplab/logos/tulip/tulip2.eps
%{_texmfdistdir}/tex/latex/powerdot-tuliplab/logos/tulip/tulip3.eps
%{_texmfdistdir}/tex/latex/powerdot-tuliplab/powerdot-tuliplab.sty

%package -n texlive-ppr-prv
Version:        %{texlive_version}.%{texlive_noarch}.0.0.13csvn15878
Release:        0
License:        LPPL-1.0
Summary:        Prosper preview
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-ppr-prv-doc >= %{texlive_version}
Provides:       tex(HAP-ppr-prv.def)
Provides:       tex(ppr-prv.cls)
Requires:       tex(article.cls)
Requires:       tex(float.sty)
Requires:       tex(geometry.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(ifpdf.sty)
Requires:       tex(keyval.sty)
Requires:       tex(pstricks.sty)
Requires:       tex(textcomp.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source79:       ppr-prv.tar.xz
Source80:       ppr-prv.doc.tar.xz

%description -n texlive-ppr-prv
This class is used with LaTeX presentations using the prosper
class. ppr-prv stands for 'Prosper Preview'. The aim of this
class is to produce a printable version of the slides written
with Prosper, with two slides per page.

%package -n texlive-ppr-prv-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.13csvn15878
Release:        0
Summary:        Documentation for texlive-ppr-prv
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/

%description -n texlive-ppr-prv-doc
This package includes the documentation for texlive-ppr-prv

%post -n texlive-ppr-prv
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-ppr-prv
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-ppr-prv
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-ppr-prv-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/ppr-prv/README
%{_texmfdistdir}/doc/latex/ppr-prv/ppr-prv.pdf

%files -n texlive-ppr-prv
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/ppr-prv/HAP-ppr-prv.def
%{_texmfdistdir}/tex/latex/ppr-prv/ppr-prv.cls

%package -n texlive-pracjourn
Version:        %{texlive_version}.%{texlive_noarch}.0.0.4nsvn61719
Release:        0
License:        GPL-2.0-or-later
Summary:        Typeset articles for PracTeX
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-pracjourn-doc >= %{texlive_version}
Provides:       tex(pracjourn.cls)
Requires:       tex(color.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(lmodern.sty)
Requires:       tex(mathpazo.sty)
Requires:       tex(microtype.sty)
Requires:       tex(textcomp.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source81:       pracjourn.tar.xz
Source82:       pracjourn.doc.tar.xz

%description -n texlive-pracjourn
The pracjourn class is used for typesetting articles in the
PracTeX Journal. It is based on the article class with
modifications to allow for more flexible front-matter and
revision control, among other small changes.

%package -n texlive-pracjourn-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.4nsvn61719
Release:        0
Summary:        Documentation for texlive-pracjourn
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/

%description -n texlive-pracjourn-doc
This package includes the documentation for texlive-pracjourn

%post -n texlive-pracjourn
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pracjourn
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pracjourn
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pracjourn-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/pracjourn/README
%{_texmfdistdir}/doc/latex/pracjourn/pjsample.ltx
%{_texmfdistdir}/doc/latex/pracjourn/pjsample.pdf
%{_texmfdistdir}/doc/latex/pracjourn/pracjourn.pdf

%files -n texlive-pracjourn
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/pracjourn/pracjourn.cls

%package -n texlive-practicalreports
Version:        %{texlive_version}.%{texlive_noarch}.2.0.3svn52312
Release:        0
License:        LPPL-1.0
Summary:        Some macros for writing practical reports
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-practicalreports-doc >= %{texlive_version}
Provides:       tex(practicalreports.sty)
Requires:       tex(array.sty)
Requires:       tex(fancyhdr.sty)
Requires:       tex(float.sty)
Requires:       tex(lastpage.sty)
Requires:       tex(longtable.sty)
Requires:       tex(mathtools.sty)
Requires:       tex(pdfpages.sty)
Requires:       tex(pgffor.sty)
Requires:       tex(scrextend.sty)
Requires:       tex(tikzducks.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source83:       practicalreports.tar.xz
Source84:       practicalreports.doc.tar.xz

%description -n texlive-practicalreports
This package provides a handful of macros for writing up
science practical reports.

%package -n texlive-practicalreports-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.0.3svn52312
Release:        0
Summary:        Documentation for texlive-practicalreports
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/

%description -n texlive-practicalreports-doc
This package includes the documentation for texlive-practicalreports

%post -n texlive-practicalreports
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-practicalreports
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-practicalreports
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-practicalreports-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/practicalreports/README
%{_texmfdistdir}/doc/latex/practicalreports/example_figure.jpeg
%{_texmfdistdir}/doc/latex/practicalreports/fancy_footer.png
%{_texmfdistdir}/doc/latex/practicalreports/fancy_header.png
%{_texmfdistdir}/doc/latex/practicalreports/fancy_page.png
%{_texmfdistdir}/doc/latex/practicalreports/new_title_page.png
%{_texmfdistdir}/doc/latex/practicalreports/normal_page.png
%{_texmfdistdir}/doc/latex/practicalreports/practicalreports.pdf
%{_texmfdistdir}/doc/latex/practicalreports/practicalreports.tex

%files -n texlive-practicalreports
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/practicalreports/practicalreports.sty

%package -n texlive-prelim2e
Version:        %{texlive_version}.%{texlive_noarch}.2.00svn57000
Release:        0
License:        LPPL-1.0
Summary:        Allows the marking of preliminary versions of a document
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-prelim2e-doc >= %{texlive_version}
Provides:       tex(prelim2e.sty)
Requires:       tex(scrtime.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source85:       prelim2e.tar.xz
Source86:       prelim2e.doc.tar.xz

%description -n texlive-prelim2e
Puts text below the normal page content (the default text marks
the document as draft and puts a timestamp on it). Can be used
together with e.g. the vrsion, rcs and rcsinfo packages. Uses
the everyshi package and can use the scrtime package from the
koma-script bundle.

%package -n texlive-prelim2e-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.00svn57000
Release:        0
Summary:        Documentation for texlive-prelim2e
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/

%description -n texlive-prelim2e-doc
This package includes the documentation for texlive-prelim2e

%post -n texlive-prelim2e
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-prelim2e
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-prelim2e
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-prelim2e-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/prelim2e/README.md
%{_texmfdistdir}/doc/latex/prelim2e/prelim2e.pdf

%files -n texlive-prelim2e
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/prelim2e/prelim2e.sty

%package -n texlive-preprint
Version:        %{texlive_version}.%{texlive_noarch}.2011svn30447
Release:        0
License:        LPPL-1.0
Summary:        A bundle of packages provided "as is"
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-preprint-doc >= %{texlive_version}
Provides:       tex(authblk.sty)
Provides:       tex(balance.sty)
Provides:       tex(figcaps.sty)
Provides:       tex(fullpage.sty)
Provides:       tex(sublabel.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source87:       preprint.tar.xz
Source88:       preprint.doc.tar.xz

%description -n texlive-preprint
The bundle comprises: authblk, which permits footnote style
author/affiliation input in the \author command, balance, to
balance the end of \twocolumn pages, figcaps, to send figure
captions, etc., to end document, fullpage, to set narrow page
margins and set a fixed page style, and sublabel, which permits
counters to be subnumbered.

%package -n texlive-preprint-doc
Version:        %{texlive_version}.%{texlive_noarch}.2011svn30447
Release:        0
Summary:        Documentation for texlive-preprint
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/

%description -n texlive-preprint-doc
This package includes the documentation for texlive-preprint

%post -n texlive-preprint
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-preprint
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-preprint
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-preprint-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/preprint/README
%{_texmfdistdir}/doc/latex/preprint/authblk.pdf
%{_texmfdistdir}/doc/latex/preprint/balance.pdf
%{_texmfdistdir}/doc/latex/preprint/figcaps.pdf
%{_texmfdistdir}/doc/latex/preprint/fullpage.pdf
%{_texmfdistdir}/doc/latex/preprint/sublabel.pdf

%files -n texlive-preprint
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/preprint/authblk.sty
%{_texmfdistdir}/tex/latex/preprint/balance.sty
%{_texmfdistdir}/tex/latex/preprint/figcaps.sty
%{_texmfdistdir}/tex/latex/preprint/fullpage.sty
%{_texmfdistdir}/tex/latex/preprint/sublabel.sty

%package -n texlive-prerex
Version:        %{texlive_version}.%{texlive_noarch}.svn54512
Release:        0
License:        GPL-2.0-or-later
Summary:        Interactive editor and macro support for prerequisite charts
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-prerex-doc >= %{texlive_version}
Provides:       tex(prerex.sty)
Requires:       tex(calc.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(pgf.sty)
Requires:       tex(relsize.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xcolor.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source89:       prerex.tar.xz
Source90:       prerex.doc.tar.xz

%description -n texlive-prerex
This package consists of prerex.sty, a LaTeX package for
producing charts of course nodes linked by arrows representing
pre- and co-requisites, and prerex, an interactive program for
creating and editing chart descriptions. The implementation of
prerex.sty uses PGF, so that it may be used equally happily
with LaTeX or pdfLaTeX; prerex itself is written in C. The
package includes source code for a previewer application, a
lightweight Qt-4 and poppler-based prerex-enabled PDF viewer.

%package -n texlive-prerex-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn54512
Release:        0
Summary:        Documentation for texlive-prerex
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Provides:       man(prerex.5)

%description -n texlive-prerex-doc
This package includes the documentation for texlive-prerex

%post -n texlive-prerex
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-prerex
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-prerex
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-prerex-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/prerex/README
%{_texmfdistdir}/doc/latex/prerex/chart.pdf
%{_texmfdistdir}/doc/latex/prerex/chart.svg
%{_texmfdistdir}/doc/latex/prerex/chart.tex
%{_texmfdistdir}/doc/latex/prerex/intro.pdf
%{_texmfdistdir}/doc/latex/prerex/intro.tex
%{_texmfdistdir}/doc/latex/prerex/introFonts.png
%{_texmfdistdir}/doc/latex/prerex/introchart1.tex
%{_texmfdistdir}/doc/latex/prerex/introchart2.tex
%{_texmfdistdir}/doc/latex/prerex/prerex-6.8.0.tar.gz
%{_texmfdistdir}/doc/latex/prerex/prerex.pdf
%{_texmfdistdir}/doc/latex/prerex/prerex.sty.7
%{_texmfdistdir}/doc/latex/prerex/prerex.sty.7.pdf
%{_texmfdistdir}/doc/latex/prerex/prerex.tex
%{_texmfdistdir}/doc/latex/prerex/vprerex-6.4.4.tar.gz
%{_texmfdistdir}/doc/latex/prerex/vprerex-6.5.1.tar.gz
%{_mandir}/man5/prerex.5*

%files -n texlive-prerex
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/prerex/prerex.sty

%package -n texlive-present
Version:        %{texlive_version}.%{texlive_noarch}.2.2.1svn50048
Release:        0
License:        LPPL-1.0
Summary:        Presentations with Plain TeX
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-present-doc >= %{texlive_version}
Provides:       tex(present.tex)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source91:       present.tar.xz
Source92:       present.doc.tar.xz

%description -n texlive-present
The package offers a collection of simple macros for preparing
presentations in Plain TeX. Slide colour and text colour may be
set, links between parts of the presentation, to other files,
and to web addresses may be inserted. Images may be included
easily, and code is available to provide transition effects
between slides or frames. The structure of the macros is not
overly complex, so that users should find it easy to adapt the
macros to their specific needs.

%package -n texlive-present-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.2.1svn50048
Release:        0
Summary:        Documentation for texlive-present
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/

%description -n texlive-present-doc
This package includes the documentation for texlive-present

%post -n texlive-present
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-present
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-present
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-present-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/plain/present/HowToTalkTeX.lp
%{_texmfdistdir}/doc/plain/present/HowToTalkTeX.pdf
%{_texmfdistdir}/doc/plain/present/HowToTalkTeX.tex
%{_texmfdistdir}/doc/plain/present/Pfeil1.pdf
%{_texmfdistdir}/doc/plain/present/Pfeil2.pdf
%{_texmfdistdir}/doc/plain/present/Pfeil3.pdf
%{_texmfdistdir}/doc/plain/present/Pfeil4.pdf
%{_texmfdistdir}/doc/plain/present/README
%{_texmfdistdir}/doc/plain/present/Sagnac.pdf
%{_texmfdistdir}/doc/plain/present/Stern.png
%{_texmfdistdir}/doc/plain/present/background.png
%{_texmfdistdir}/doc/plain/present/present-transitions.tex

%files -n texlive-present
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/plain/present/present.tex

%package -n texlive-pressrelease
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn35147
Release:        0
License:        LPPL-1.0
Summary:        A class for typesetting press releases
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-pressrelease-doc >= %{texlive_version}
Provides:       tex(pressrelease-symbols.sty)
Provides:       tex(pressrelease.cls)
Requires:       tex(article.cls)
Requires:       tex(etoolbox.sty)
Requires:       tex(geometry.sty)
Requires:       tex(marvosym.sty)
Requires:       tex(refcount.sty)
Requires:       tex(setspace.sty)
Requires:       tex(tikz.sty)
Requires:       tex(url.sty)
Requires:       tex(xkeyval.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source93:       pressrelease.tar.xz
Source94:       pressrelease.doc.tar.xz

%description -n texlive-pressrelease
A configurable class for writing press releases.

%package -n texlive-pressrelease-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn35147
Release:        0
Summary:        Documentation for texlive-pressrelease
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/

%description -n texlive-pressrelease-doc
This package includes the documentation for texlive-pressrelease

%post -n texlive-pressrelease
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pressrelease
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pressrelease
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pressrelease-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/pressrelease/CHANGES
%{_texmfdistdir}/doc/latex/pressrelease/README
%{_texmfdistdir}/doc/latex/pressrelease/pressrelease.pdf
%{_texmfdistdir}/doc/latex/pressrelease/samples/sample-pressrelease.pdf
%{_texmfdistdir}/doc/latex/pressrelease/samples/sample-pressrelease.tex
%{_texmfdistdir}/doc/latex/pressrelease/samples/sample-pressrelease2.pdf
%{_texmfdistdir}/doc/latex/pressrelease/samples/sample-pressrelease2.tex
%{_texmfdistdir}/doc/latex/pressrelease/samples/sample-pressrelease3.pdf
%{_texmfdistdir}/doc/latex/pressrelease/samples/sample-pressrelease3.tex
%{_texmfdistdir}/doc/latex/pressrelease/samples/sample-pressrelease4.pdf
%{_texmfdistdir}/doc/latex/pressrelease/samples/sample-pressrelease4.tex
%{_texmfdistdir}/doc/latex/pressrelease/samples/sample-pressrelease5.pdf
%{_texmfdistdir}/doc/latex/pressrelease/samples/sample-pressrelease5.tex
%{_texmfdistdir}/doc/latex/pressrelease/samples/sample-pressrelease6.pdf
%{_texmfdistdir}/doc/latex/pressrelease/samples/sample-pressrelease6.tex
%{_texmfdistdir}/doc/latex/pressrelease/samples/sample-pressrelease7.pdf
%{_texmfdistdir}/doc/latex/pressrelease/samples/sample-pressrelease7.tex

%files -n texlive-pressrelease
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/pressrelease/pressrelease-symbols.sty
%{_texmfdistdir}/tex/latex/pressrelease/pressrelease.cls

%package -n texlive-prettyref
Version:        %{texlive_version}.%{texlive_noarch}.3.0svn15878
Release:        0
License:        SUSE-Public-Domain
Summary:        Make label references "self-identify"
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-prettyref-doc >= %{texlive_version}
Provides:       tex(prettyref.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source95:       prettyref.tar.xz
Source96:       prettyref.doc.tar.xz

%description -n texlive-prettyref
Prettyref provides a command \newrefformat, which specifies the
way in which a reference is typeset, according to a label
"identification". The identification is set in the \label
command, by using prefixed label names; so instead of
\label{mysection}, one uses \label{sec:mysection}, and
prettyref interprets the "sec:" part. The package is compatible
with hyperref and with other packages.

%package -n texlive-prettyref-doc
Version:        %{texlive_version}.%{texlive_noarch}.3.0svn15878
Release:        0
Summary:        Documentation for texlive-prettyref
License:        SUSE-Public-Domain
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/

%description -n texlive-prettyref-doc
This package includes the documentation for texlive-prettyref

%post -n texlive-prettyref
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-prettyref
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-prettyref
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-prettyref-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/prettyref/README
%{_texmfdistdir}/doc/latex/prettyref/prettyref.pdf

%files -n texlive-prettyref
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/prettyref/prettyref.sty

%package -n texlive-preview
Version:        %{texlive_version}.%{texlive_noarch}.13.1svn62130
Release:        0
License:        GPL-2.0-or-later
Summary:        Extract bits of a LaTeX source for output
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-preview-doc >= %{texlive_version}
Provides:       tex(prauctex.cfg)
Provides:       tex(prauctex.def)
Provides:       tex(prcounters.def)
Provides:       tex(preview.sty)
Provides:       tex(prfootnotes.def)
Provides:       tex(prlyx.def)
Provides:       tex(prshowbox.def)
Provides:       tex(prshowlabels.def)
Provides:       tex(prtightpage.def)
Provides:       tex(prtracingall.def)
Requires:       tex(luatex85.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source97:       preview.tar.xz
Source98:       preview.doc.tar.xz

%description -n texlive-preview
The package is a free-standing part of the preview-latex
bundle. The package provides the support preview-latex needs,
when it chooses the matter it will preview. The output may
reasonably be expected to have other uses, as in html
translators, etc.

%package -n texlive-preview-doc
Version:        %{texlive_version}.%{texlive_noarch}.13.1svn62130
Release:        0
Summary:        Documentation for texlive-preview
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/

%description -n texlive-preview-doc
This package includes the documentation for texlive-preview

%post -n texlive-preview
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-preview
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-preview
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-preview-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/preview/README
%{_texmfdistdir}/doc/latex/preview/preview.pdf

%files -n texlive-preview
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/preview/prauctex.cfg
%{_texmfdistdir}/tex/latex/preview/prauctex.def
%{_texmfdistdir}/tex/latex/preview/prcounters.def
%{_texmfdistdir}/tex/latex/preview/preview.sty
%{_texmfdistdir}/tex/latex/preview/prfootnotes.def
%{_texmfdistdir}/tex/latex/preview/prlyx.def
%{_texmfdistdir}/tex/latex/preview/prshowbox.def
%{_texmfdistdir}/tex/latex/preview/prshowlabels.def
%{_texmfdistdir}/tex/latex/preview/prtightpage.def
%{_texmfdistdir}/tex/latex/preview/prtracingall.def

%package -n texlive-prftree
Version:        %{texlive_version}.%{texlive_noarch}.1.6svn54080
Release:        0
License:        GPL-2.0-or-later
Summary:        Macros for building proof trees
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-prftree-doc >= %{texlive_version}
Provides:       tex(prftree.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source99:       prftree.tar.xz
Source100:      prftree.doc.tar.xz

%description -n texlive-prftree
A package to typeset proof trees for natural deduction calculi,
sequent-like calculi, and similar.

%package -n texlive-prftree-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.6svn54080
Release:        0
Summary:        Documentation for texlive-prftree
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/

%description -n texlive-prftree-doc
This package includes the documentation for texlive-prftree

%post -n texlive-prftree
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-prftree
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-prftree
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-prftree-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/prftree/README
%{_texmfdistdir}/doc/latex/prftree/prftreedoc.pdf
%{_texmfdistdir}/doc/latex/prftree/prftreedoc.tex

%files -n texlive-prftree
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/prftree/prftree.sty

%package -n texlive-principia
Version:        %{texlive_version}.%{texlive_noarch}.1.3svn58927
Release:        0
License:        LPPL-1.0
Summary:        Notations for typesetting the "Principia Mathematica"
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-principia-doc >= %{texlive_version}
Provides:       tex(principia.sty)
Requires:       tex(amsmath.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(pifont.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source101:      principia.tar.xz
Source102:      principia.doc.tar.xz

%description -n texlive-principia
This package supports typesetting the Peanese notation in
Volume I of Whitehead and Russell's 1910 "Principia
Mathematica".

%package -n texlive-principia-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.3svn58927
Release:        0
Summary:        Documentation for texlive-principia
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/

%description -n texlive-principia-doc
This package includes the documentation for texlive-principia

%post -n texlive-principia
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-principia
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-principia
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-principia-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/principia/README
%{_texmfdistdir}/doc/latex/principia/principia.pdf
%{_texmfdistdir}/doc/latex/principia/principia.tex

%files -n texlive-principia
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/principia/principia.sty

%package -n texlive-printlen
Version:        %{texlive_version}.%{texlive_noarch}.1.1asvn19847
Release:        0
License:        LPPL-1.0
Summary:        Print lengths using specified units
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-printlen-doc >= %{texlive_version}
Provides:       tex(printlen.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source103:      printlen.tar.xz
Source104:      printlen.doc.tar.xz

%description -n texlive-printlen
\printlength{length} prints the value of a LaTeX length in the
units specified by \uselengthunit{unit} ('unit' may be any TeX
length unit except for scaled point, viz., any of: pt, pc, in,
mm, cm, bp, dd or cc). When the unit is pt, the printed length
value will include any stretch or shrink; otherwise these are
not printed. The 'unit' argument may also be PT, in which case
length values will be printed in point units but without any
stretch or shrink values.

%package -n texlive-printlen-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1asvn19847
Release:        0
Summary:        Documentation for texlive-printlen
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/

%description -n texlive-printlen-doc
This package includes the documentation for texlive-printlen

%post -n texlive-printlen
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-printlen
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-printlen
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-printlen-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/printlen/printlen-doc.pdf
%{_texmfdistdir}/doc/latex/printlen/printlen-doc.tex

%files -n texlive-printlen
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/printlen/printlen.sty

%package -n texlive-proba
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
License:        LPPL-1.0
Summary:        Shortcuts commands to symbols used in probability texts
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-proba-doc >= %{texlive_version}
Provides:       tex(proba.sty)
Requires:       tex(amsfonts.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source105:      proba.tar.xz
Source106:      proba.doc.tar.xz

%description -n texlive-proba
This package includes some of the most often used commands in
probability texts, e.g. probability, expectation, variance,
etc. It also includes some short commands for set (blackboard)
or filtrations (calligraphic). It requires LaTeX2e and the
amsfonts package.

%package -n texlive-proba-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        Documentation for texlive-proba
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/

%description -n texlive-proba-doc
This package includes the documentation for texlive-proba

%post -n texlive-proba
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-proba
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-proba
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-proba-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/proba/README
%{_texmfdistdir}/doc/latex/proba/proba.pdf

%files -n texlive-proba
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/proba/proba.sty

%package -n texlive-probsoln
Version:        %{texlive_version}.%{texlive_noarch}.3.05svn44783
Release:        0
License:        LPPL-1.0
Summary:        Generate problem sheets and their solution sheets
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-probsoln-doc >= %{texlive_version}
Provides:       tex(probsoln.sty)
Requires:       tex(amsmath.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(xkeyval.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source107:      probsoln.tar.xz
Source108:      probsoln.doc.tar.xz

%description -n texlive-probsoln
The package is designed for lecturers who have to generate new
problem sheets for their students on a regular basis (e.g.
yearly) by randomly selecting a specified number of problems
defined in another file. The package allows you easily to
generate a new problem sheet that is different from the
previous year, thus alleviating the temptation of students to
seek out the previous year's students and checking out their
answers. The solutions to the problems can be defined along
with the problem, making it easy to generate the solution sheet
from the same source code; problems may be reused within a
document, so that solutions may appear in a different section
of the same document as the problems they cover.

%package -n texlive-probsoln-doc
Version:        %{texlive_version}.%{texlive_noarch}.3.05svn44783
Release:        0
Summary:        Documentation for texlive-probsoln
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/

%description -n texlive-probsoln-doc
This package includes the documentation for texlive-probsoln

%post -n texlive-probsoln
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-probsoln
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-probsoln
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-probsoln-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/probsoln/CHANGES
%{_texmfdistdir}/doc/latex/probsoln/INSTALL
%{_texmfdistdir}/doc/latex/probsoln/README
%{_texmfdistdir}/doc/latex/probsoln/probsoln.pdf
%{_texmfdistdir}/doc/latex/probsoln/samples/prob-1stprncp.tex
%{_texmfdistdir}/doc/latex/probsoln/samples/prob-args.tex
%{_texmfdistdir}/doc/latex/probsoln/samples/prob-easy.tex
%{_texmfdistdir}/doc/latex/probsoln/samples/prob-easy2.tex
%{_texmfdistdir}/doc/latex/probsoln/samples/prob-implicit.tex
%{_texmfdistdir}/doc/latex/probsoln/samples/prob-mchoice.tex
%{_texmfdistdir}/doc/latex/probsoln/samples/prob-mixed.tex
%{_texmfdistdir}/doc/latex/probsoln/samples/prob-newdata.tex
%{_texmfdistdir}/doc/latex/probsoln/samples/prob-nosoln.tex
%{_texmfdistdir}/doc/latex/probsoln/samples/prob-probspaces.tex
%{_texmfdistdir}/doc/latex/probsoln/samples/prob-probspaces2.tex
%{_texmfdistdir}/doc/latex/probsoln/samples/prob-tabmchoice.tex
%{_texmfdistdir}/doc/latex/probsoln/samples/prob-verb.tex
%{_texmfdistdir}/doc/latex/probsoln/samples/sample-exclude.pdf
%{_texmfdistdir}/doc/latex/probsoln/samples/sample-exclude.tex
%{_texmfdistdir}/doc/latex/probsoln/samples/sample.pdf
%{_texmfdistdir}/doc/latex/probsoln/samples/sample.tex
%{_texmfdistdir}/doc/latex/probsoln/samples/sample2.pdf
%{_texmfdistdir}/doc/latex/probsoln/samples/sample2.tex
%{_texmfdistdir}/doc/latex/probsoln/samples/sample3.pdf
%{_texmfdistdir}/doc/latex/probsoln/samples/sample3.tex
%{_texmfdistdir}/doc/latex/probsoln/samples/sample4.pdf
%{_texmfdistdir}/doc/latex/probsoln/samples/sample4.tex
%{_texmfdistdir}/doc/latex/probsoln/samples/sample5.pdf
%{_texmfdistdir}/doc/latex/probsoln/samples/sample5.tex
%{_texmfdistdir}/doc/latex/probsoln/samples/sample6.pdf
%{_texmfdistdir}/doc/latex/probsoln/samples/sample6.tex
%{_texmfdistdir}/doc/latex/probsoln/samples/sample7.pdf
%{_texmfdistdir}/doc/latex/probsoln/samples/sample7.tex
%{_texmfdistdir}/doc/latex/probsoln/samples/sample8.pdf
%{_texmfdistdir}/doc/latex/probsoln/samples/sample8.tex
%{_texmfdistdir}/doc/latex/probsoln/samples/sample9.pdf
%{_texmfdistdir}/doc/latex/probsoln/samples/sample9.tex

%files -n texlive-probsoln
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/probsoln/probsoln.sty

%package -n texlive-procIAGssymp
Version:        %{texlive_version}.%{texlive_noarch}.svn51771
Release:        0
License:        LPPL-1.0
Summary:        Macros for IAG symposium papers
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-procIAGssymp-doc >= %{texlive_version}
Provides:       tex(procIAGssymp.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source109:      procIAGssymp.tar.xz
Source110:      procIAGssymp.doc.tar.xz

%description -n texlive-procIAGssymp
This package provides (re-)definitions of some LaTeX commands
that can be useful for the preparation of a paper with the
style of the proceeding of symposia sponsored by the
'International Association of Geodesy (IAG)' published by
Springer-Verlag.

%package -n texlive-procIAGssymp-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn51771
Release:        0
Summary:        Documentation for texlive-procIAGssymp
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/

%description -n texlive-procIAGssymp-doc
This package includes the documentation for texlive-procIAGssymp

%post -n texlive-procIAGssymp
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-procIAGssymp
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-procIAGssymp
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-procIAGssymp-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/procIAGssymp/TestPaper.tex

%files -n texlive-procIAGssymp
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/procIAGssymp/procIAGssymp.sty

%package -n texlive-prodint
Version:        %{texlive_version}.%{texlive_noarch}.svn21893
Release:        0
License:        OFL-1.1
Summary:        A font that provides the product integral symbol
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(updmap.cfg)
#!BuildIgnore:  tex(updmap.cfg)
Requires(postun):findutils
Requires(postun):grep
Requires(postun):sed
Requires(postun):texlive >= %{texlive_version}
Requires(postun):tex(updmap.cfg)
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Requires:       texlive-prodint-fonts >= %{texlive_version}
Suggests:       texlive-prodint-doc >= %{texlive_version}
Provides:       tex(prodint.map)
Provides:       tex(prodint.sty)
Provides:       tex(prodint.tfm)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source111:      prodint.tar.xz
Source112:      prodint.doc.tar.xz

%description -n texlive-prodint
Product integrals are to products, as integrals are to sums.
They have been around for more than a hundred years, they have
not become part of the standard mathematician's toolbox,
possibly because no-one invented the right mathematical symbol
for them. The authors have remedied that situation by proposing
the symbol and providing this font.

%package -n texlive-prodint-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn21893
Release:        0
Summary:        Documentation for texlive-prodint
License:        OFL-1.1
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/

%description -n texlive-prodint-doc
This package includes the documentation for texlive-prodint

%package -n texlive-prodint-fonts
Version:        %{texlive_version}.%{texlive_noarch}.svn21893
Release:        0
Summary:        Severed fonts for texlive-prodint
License:        OFL-1.1
URL:            https://www.tug.org/texlive/
Group:          Productivity/Publishing/TeX/Fonts
%reconfigure_fonts_prereq
Requires(posttrans):fontconfig
Requires(posttrans):ghostscript-fonts-std
Requires(posttrans):mkfontdir
Requires(posttrans):mkfontscale
Requires(posttrans):xorg-x11-fonts-core

%description -n texlive-prodint-fonts
The  separated fonts package for texlive-prodint

%post -n texlive-prodint
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
echo 'addMap prodint.map' >> /var/run/texlive/run-updmap

%postun -n texlive-prodint
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    echo 'deleteMap prodint.map' >> /var/run/texlive/run-updmap
    exit 0
fi

%posttrans -n texlive-prodint
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-prodint-fonts

%files -n texlive-prodint-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/prodint/README
%{_texmfdistdir}/doc/fonts/prodint/config.prodint
%{_texmfdistdir}/doc/fonts/prodint/prodint.bma
%{_texmfdistdir}/doc/fonts/prodint/prodint.mt1
%{_texmfdistdir}/doc/fonts/prodint/prodint.pdf
%{_texmfdistdir}/doc/fonts/prodint/prodint.pfa
%{_texmfdistdir}/doc/fonts/prodint/prodint.sit.hqx
%{_texmfdistdir}/doc/fonts/prodint/prodint.tex

%files -n texlive-prodint
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/afm/public/prodint/prodint.afm
%{_texmfdistdir}/fonts/map/dvips/prodint/prodint.map
%{_texmfdistdir}/fonts/tfm/public/prodint/prodint.tfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/prodint/prodint.pfb
%{_texmfdistdir}/tex/latex/prodint/prodint.sty

%files -n texlive-prodint-fonts
%defattr(-,root,root,755)
%dir %{_datadir}/fonts/texlive-prodint
%{_datadir}/fontconfig/conf.avail/58-texlive-prodint.conf
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-prodint/encodings.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-prodint/fonts.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-prodint/fonts.scale
%{_datadir}/fonts/texlive-prodint/prodint.pfb

%package -n texlive-productbox
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn20886
Release:        0
License:        LPPL-1.0
Summary:        Typeset a three-dimensional product box
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-productbox-doc >= %{texlive_version}
Provides:       tex(productbox.sty)
Requires:       tex(keyval.sty)
Requires:       tex(tikz.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source113:      productbox.tar.xz
Source114:      productbox.doc.tar.xz

%description -n texlive-productbox
The package enables typesetting of a three-dimensional product
box. This product box can be rendered as it is standing on a
surface and some light is shed onto it. Alternatively it can be
typeset as a wireframe to be cut out and glued together. This
will lead to a physical product box. The package requires pgf
and TikZ.

%package -n texlive-productbox-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn20886
Release:        0
Summary:        Documentation for texlive-productbox
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/

%description -n texlive-productbox-doc
This package includes the documentation for texlive-productbox

%post -n texlive-productbox
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-productbox
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-productbox
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-productbox-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/productbox/Makefile
%{_texmfdistdir}/doc/latex/productbox/README
%{_texmfdistdir}/doc/latex/productbox/productbox.bib
%{_texmfdistdir}/doc/latex/productbox/productbox.pdf

%files -n texlive-productbox
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/productbox/productbox.sty

%package -n texlive-profcollege
Version:        %{texlive_version}.%{texlive_noarch}.0.0.99_msvn62686
Release:        0
License:        LPPL-1.0
Summary:        A LaTeX package for French maths teachers in college
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-profcollege-doc >= %{texlive_version}
Provides:       tex(PfCEquationComposition2.tex)
Provides:       tex(PfCEquationLaurent1.tex)
Provides:       tex(PfCEquationPose1.tex)
Provides:       tex(PfCEquationSoustraction2.tex)
Provides:       tex(PfCEquationSymbole1.tex)
Provides:       tex(PfCEquationTerme1.tex)
Provides:       tex(ProfCollege.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(cancel.sty)
Requires:       tex(datatool.sty)
Requires:       tex(environ.sty)
Requires:       tex(fmtcount.sty)
Requires:       tex(fontawesome5.sty)
Requires:       tex(gmp.sty)
Requires:       tex(hhline.sty)
Requires:       tex(ifoddpage.sty)
Requires:       tex(iftex.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(listofitems.sty)
Requires:       tex(luamplib.sty)
Requires:       tex(mathtools.sty)
Requires:       tex(modulus.sty)
Requires:       tex(multicol.sty)
Requires:       tex(multido.sty)
Requires:       tex(nicematrix.sty)
Requires:       tex(pifont.sty)
Requires:       tex(simplekv.sty)
Requires:       tex(siunitx.sty)
Requires:       tex(stackengine.sty)
Requires:       tex(suffix.sty)
Requires:       tex(tcolorbox.sty)
Requires:       tex(tikz.sty)
Requires:       tex(verbatim.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xfp.sty)
Requires:       tex(xintexpr.sty)
Requires:       tex(xinttools.sty)
Requires:       tex(xlop.sty)
Requires:       tex(xstring.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source115:      profcollege.tar.xz
Source116:      profcollege.doc.tar.xz

%description -n texlive-profcollege
This package provides some commands to help French mathematics
teachers for 11-16 years olds, for example: \Tableau[Metre] to
write the tabular km|hm|... with some facilities,
\Pythagore{ABC}{5}{7} to write the entire calculation of AC
with the Pythagorean theorem, \Trigo[Cosinus]{ABC}{3}{}{60} to
write the entire calculation of AC with cosine, ... and some
others.

%package -n texlive-profcollege-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.99_msvn62686
Release:        0
Summary:        Documentation for texlive-profcollege
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Provides:       locale(texlive-profcollege-doc:fr)

%description -n texlive-profcollege-doc
This package includes the documentation for texlive-profcollege

%post -n texlive-profcollege
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-profcollege
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-profcollege
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-profcollege-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/profcollege/Cafrique.dat
%{_texmfdistdir}/doc/latex/profcollege/Cameriquecentrale.dat
%{_texmfdistdir}/doc/latex/profcollege/Cameriquenord.dat
%{_texmfdistdir}/doc/latex/profcollege/Cameriquesud.dat
%{_texmfdistdir}/doc/latex/profcollege/Casia.dat
%{_texmfdistdir}/doc/latex/profcollege/Casie.dat
%{_texmfdistdir}/doc/latex/profcollege/Ccaraibes.dat
%{_texmfdistdir}/doc/latex/profcollege/Ceurope.dat
%{_texmfdistdir}/doc/latex/profcollege/Ile.dat
%{_texmfdistdir}/doc/latex/profcollege/ProfCollege-doc.pdf
%{_texmfdistdir}/doc/latex/profcollege/ProfCollege-doc.zip
%{_texmfdistdir}/doc/latex/profcollege/README
%{_texmfdistdir}/doc/latex/profcollege/afganistan.dat
%{_texmfdistdir}/doc/latex/profcollege/afriquesud1.dat
%{_texmfdistdir}/doc/latex/profcollege/afriquesud2.dat
%{_texmfdistdir}/doc/latex/profcollege/albanie.dat
%{_texmfdistdir}/doc/latex/profcollege/algerie.dat
%{_texmfdistdir}/doc/latex/profcollege/allemagne1.dat
%{_texmfdistdir}/doc/latex/profcollege/allemagne2.dat
%{_texmfdistdir}/doc/latex/profcollege/andorre.dat
%{_texmfdistdir}/doc/latex/profcollege/angleterre.dat
%{_texmfdistdir}/doc/latex/profcollege/angola.dat
%{_texmfdistdir}/doc/latex/profcollege/arabiesaoudite.dat
%{_texmfdistdir}/doc/latex/profcollege/argentine1.dat
%{_texmfdistdir}/doc/latex/profcollege/argentine2.dat
%{_texmfdistdir}/doc/latex/profcollege/armenie.dat
%{_texmfdistdir}/doc/latex/profcollege/autriche.dat
%{_texmfdistdir}/doc/latex/profcollege/azerbaijan1.dat
%{_texmfdistdir}/doc/latex/profcollege/azerbaijan2.dat
%{_texmfdistdir}/doc/latex/profcollege/bangladesh.dat
%{_texmfdistdir}/doc/latex/profcollege/belarussie.dat
%{_texmfdistdir}/doc/latex/profcollege/belgique.dat
%{_texmfdistdir}/doc/latex/profcollege/belize.dat
%{_texmfdistdir}/doc/latex/profcollege/benin.dat
%{_texmfdistdir}/doc/latex/profcollege/bhutan.dat
%{_texmfdistdir}/doc/latex/profcollege/birmanie.dat
%{_texmfdistdir}/doc/latex/profcollege/bolivie1.dat
%{_texmfdistdir}/doc/latex/profcollege/bolivie2.dat
%{_texmfdistdir}/doc/latex/profcollege/bosnie1.dat
%{_texmfdistdir}/doc/latex/profcollege/bosnie2.dat
%{_texmfdistdir}/doc/latex/profcollege/botswana.dat
%{_texmfdistdir}/doc/latex/profcollege/bresil.dat
%{_texmfdistdir}/doc/latex/profcollege/brunei.dat
%{_texmfdistdir}/doc/latex/profcollege/bulgarie.dat
%{_texmfdistdir}/doc/latex/profcollege/burkinafaso.dat
%{_texmfdistdir}/doc/latex/profcollege/burundi.dat
%{_texmfdistdir}/doc/latex/profcollege/cabinda.dat
%{_texmfdistdir}/doc/latex/profcollege/cambodge.dat
%{_texmfdistdir}/doc/latex/profcollege/cameroun.dat
%{_texmfdistdir}/doc/latex/profcollege/canada.dat
%{_texmfdistdir}/doc/latex/profcollege/capitales.dat
%{_texmfdistdir}/doc/latex/profcollege/chili1.dat
%{_texmfdistdir}/doc/latex/profcollege/chili2.dat
%{_texmfdistdir}/doc/latex/profcollege/chine.dat
%{_texmfdistdir}/doc/latex/profcollege/colombie.dat
%{_texmfdistdir}/doc/latex/profcollege/congo.dat
%{_texmfdistdir}/doc/latex/profcollege/coreenord.dat
%{_texmfdistdir}/doc/latex/profcollege/coreesud.dat
%{_texmfdistdir}/doc/latex/profcollege/costarica.dat
%{_texmfdistdir}/doc/latex/profcollege/coteivoire.dat
%{_texmfdistdir}/doc/latex/profcollege/croatie.dat
%{_texmfdistdir}/doc/latex/profcollege/danemark.dat
%{_texmfdistdir}/doc/latex/profcollege/djibouti.dat
%{_texmfdistdir}/doc/latex/profcollege/ecosse.dat
%{_texmfdistdir}/doc/latex/profcollege/egypte.dat
%{_texmfdistdir}/doc/latex/profcollege/emirats.dat
%{_texmfdistdir}/doc/latex/profcollege/equateur.dat
%{_texmfdistdir}/doc/latex/profcollege/eritre.dat
%{_texmfdistdir}/doc/latex/profcollege/espagne.dat
%{_texmfdistdir}/doc/latex/profcollege/estonie.dat
%{_texmfdistdir}/doc/latex/profcollege/ethiopie.dat
%{_texmfdistdir}/doc/latex/profcollege/finlande.dat
%{_texmfdistdir}/doc/latex/profcollege/fleuveseurope.dat
%{_texmfdistdir}/doc/latex/profcollege/fleuvessup.dat
%{_texmfdistdir}/doc/latex/profcollege/france.dat
%{_texmfdistdir}/doc/latex/profcollege/gabon.dat
%{_texmfdistdir}/doc/latex/profcollege/gambie.dat
%{_texmfdistdir}/doc/latex/profcollege/gaza.dat
%{_texmfdistdir}/doc/latex/profcollege/georgie.dat
%{_texmfdistdir}/doc/latex/profcollege/ghana.dat
%{_texmfdistdir}/doc/latex/profcollege/gibraltar.dat
%{_texmfdistdir}/doc/latex/profcollege/grece.dat
%{_texmfdistdir}/doc/latex/profcollege/guatemala.dat
%{_texmfdistdir}/doc/latex/profcollege/guinee.dat
%{_texmfdistdir}/doc/latex/profcollege/guineebissau.dat
%{_texmfdistdir}/doc/latex/profcollege/guineef.dat
%{_texmfdistdir}/doc/latex/profcollege/guyane.dat
%{_texmfdistdir}/doc/latex/profcollege/haiti.dat
%{_texmfdistdir}/doc/latex/profcollege/honduras.dat
%{_texmfdistdir}/doc/latex/profcollege/hongrie.dat
%{_texmfdistdir}/doc/latex/profcollege/iles.dat
%{_texmfdistdir}/doc/latex/profcollege/iles1.dat
%{_texmfdistdir}/doc/latex/profcollege/inde.dat
%{_texmfdistdir}/doc/latex/profcollege/indonesie1.dat
%{_texmfdistdir}/doc/latex/profcollege/indonesie2.dat
%{_texmfdistdir}/doc/latex/profcollege/irak.dat
%{_texmfdistdir}/doc/latex/profcollege/iran.dat
%{_texmfdistdir}/doc/latex/profcollege/irelande.dat
%{_texmfdistdir}/doc/latex/profcollege/irelandenord.dat
%{_texmfdistdir}/doc/latex/profcollege/israel.dat
%{_texmfdistdir}/doc/latex/profcollege/italie.dat
%{_texmfdistdir}/doc/latex/profcollege/jordanie.dat
%{_texmfdistdir}/doc/latex/profcollege/kazakhstan.dat
%{_texmfdistdir}/doc/latex/profcollege/kenya.dat
%{_texmfdistdir}/doc/latex/profcollege/koweit.dat
%{_texmfdistdir}/doc/latex/profcollege/kyrgyzstan.dat
%{_texmfdistdir}/doc/latex/profcollege/lacs.dat
%{_texmfdistdir}/doc/latex/profcollege/lacssup.dat
%{_texmfdistdir}/doc/latex/profcollege/laos.dat
%{_texmfdistdir}/doc/latex/profcollege/lesotho.dat
%{_texmfdistdir}/doc/latex/profcollege/lettonie.dat
%{_texmfdistdir}/doc/latex/profcollege/liban.dat
%{_texmfdistdir}/doc/latex/profcollege/liberia.dat
%{_texmfdistdir}/doc/latex/profcollege/libye.dat
%{_texmfdistdir}/doc/latex/profcollege/liechtenstein.dat
%{_texmfdistdir}/doc/latex/profcollege/lithuanie1.dat
%{_texmfdistdir}/doc/latex/profcollege/lithuanie2.dat
%{_texmfdistdir}/doc/latex/profcollege/luxembourg.dat
%{_texmfdistdir}/doc/latex/profcollege/macedoine.dat
%{_texmfdistdir}/doc/latex/profcollege/malaisie1.dat
%{_texmfdistdir}/doc/latex/profcollege/malaisie2.dat
%{_texmfdistdir}/doc/latex/profcollege/malawi.dat
%{_texmfdistdir}/doc/latex/profcollege/mali.dat
%{_texmfdistdir}/doc/latex/profcollege/maroc.dat
%{_texmfdistdir}/doc/latex/profcollege/mauritanie.dat
%{_texmfdistdir}/doc/latex/profcollege/mexique.dat
%{_texmfdistdir}/doc/latex/profcollege/moldavie.dat
%{_texmfdistdir}/doc/latex/profcollege/monaco.dat
%{_texmfdistdir}/doc/latex/profcollege/mongolie.dat
%{_texmfdistdir}/doc/latex/profcollege/mozambique.dat
%{_texmfdistdir}/doc/latex/profcollege/namibie.dat
%{_texmfdistdir}/doc/latex/profcollege/nepal.dat
%{_texmfdistdir}/doc/latex/profcollege/nicaragua.dat
%{_texmfdistdir}/doc/latex/profcollege/niger.dat
%{_texmfdistdir}/doc/latex/profcollege/nigeria.dat
%{_texmfdistdir}/doc/latex/profcollege/norvege.dat
%{_texmfdistdir}/doc/latex/profcollege/nvelleguinne.dat
%{_texmfdistdir}/doc/latex/profcollege/oman1.dat
%{_texmfdistdir}/doc/latex/profcollege/oman2.dat
%{_texmfdistdir}/doc/latex/profcollege/ouganda.dat
%{_texmfdistdir}/doc/latex/profcollege/ouzbekistan.dat
%{_texmfdistdir}/doc/latex/profcollege/pakistan.dat
%{_texmfdistdir}/doc/latex/profcollege/panama1.dat
%{_texmfdistdir}/doc/latex/profcollege/panama2.dat
%{_texmfdistdir}/doc/latex/profcollege/paraguay.dat
%{_texmfdistdir}/doc/latex/profcollege/paysbas.dat
%{_texmfdistdir}/doc/latex/profcollege/paysdegalles.dat
%{_texmfdistdir}/doc/latex/profcollege/perou.dat
%{_texmfdistdir}/doc/latex/profcollege/polesud.dat
%{_texmfdistdir}/doc/latex/profcollege/pologne.dat
%{_texmfdistdir}/doc/latex/profcollege/portugal.dat
%{_texmfdistdir}/doc/latex/profcollege/quatar.dat
%{_texmfdistdir}/doc/latex/profcollege/repcentreafrique.dat
%{_texmfdistdir}/doc/latex/profcollege/repdominicaine.dat
%{_texmfdistdir}/doc/latex/profcollege/riomuni.dat
%{_texmfdistdir}/doc/latex/profcollege/rivieres.dat
%{_texmfdistdir}/doc/latex/profcollege/roumanie.dat
%{_texmfdistdir}/doc/latex/profcollege/russie1.dat
%{_texmfdistdir}/doc/latex/profcollege/russie1bis.dat
%{_texmfdistdir}/doc/latex/profcollege/russie2.dat
%{_texmfdistdir}/doc/latex/profcollege/rwanda.dat
%{_texmfdistdir}/doc/latex/profcollege/saharaouest.dat
%{_texmfdistdir}/doc/latex/profcollege/salvador.dat
%{_texmfdistdir}/doc/latex/profcollege/sanmarin.dat
%{_texmfdistdir}/doc/latex/profcollege/senegal.dat
%{_texmfdistdir}/doc/latex/profcollege/sierraleone.dat
%{_texmfdistdir}/doc/latex/profcollege/slovaquie.dat
%{_texmfdistdir}/doc/latex/profcollege/slovenie.dat
%{_texmfdistdir}/doc/latex/profcollege/somalie.dat
%{_texmfdistdir}/doc/latex/profcollege/soudan.dat
%{_texmfdistdir}/doc/latex/profcollege/suede.dat
%{_texmfdistdir}/doc/latex/profcollege/suisse.dat
%{_texmfdistdir}/doc/latex/profcollege/surinam.dat
%{_texmfdistdir}/doc/latex/profcollege/swaziland.dat
%{_texmfdistdir}/doc/latex/profcollege/syrie.dat
%{_texmfdistdir}/doc/latex/profcollege/tajikistan.dat
%{_texmfdistdir}/doc/latex/profcollege/tanzanie.dat
%{_texmfdistdir}/doc/latex/profcollege/tchad.dat
%{_texmfdistdir}/doc/latex/profcollege/tcheque.dat
%{_texmfdistdir}/doc/latex/profcollege/thailande.dat
%{_texmfdistdir}/doc/latex/profcollege/togo.dat
%{_texmfdistdir}/doc/latex/profcollege/tunisie.dat
%{_texmfdistdir}/doc/latex/profcollege/turkmenistan.dat
%{_texmfdistdir}/doc/latex/profcollege/turquie1.dat
%{_texmfdistdir}/doc/latex/profcollege/turquie2.dat
%{_texmfdistdir}/doc/latex/profcollege/ukraine.dat
%{_texmfdistdir}/doc/latex/profcollege/uruguay.dat
%{_texmfdistdir}/doc/latex/profcollege/usa1.dat
%{_texmfdistdir}/doc/latex/profcollege/usa2.dat
%{_texmfdistdir}/doc/latex/profcollege/venezuela.dat
%{_texmfdistdir}/doc/latex/profcollege/vietnam.dat
%{_texmfdistdir}/doc/latex/profcollege/villesFrance.dat
%{_texmfdistdir}/doc/latex/profcollege/villesFranceCycle4.dat
%{_texmfdistdir}/doc/latex/profcollege/villesFranceNord.dat
%{_texmfdistdir}/doc/latex/profcollege/villesFrancesimp.dat
%{_texmfdistdir}/doc/latex/profcollege/villesItalie.dat
%{_texmfdistdir}/doc/latex/profcollege/volcans.dat
%{_texmfdistdir}/doc/latex/profcollege/westbank.dat
%{_texmfdistdir}/doc/latex/profcollege/yemen.dat
%{_texmfdistdir}/doc/latex/profcollege/yougoslavie.dat
%{_texmfdistdir}/doc/latex/profcollege/zaire.dat
%{_texmfdistdir}/doc/latex/profcollege/zambie.dat
%{_texmfdistdir}/doc/latex/profcollege/zimbabwe.dat

%files -n texlive-profcollege
%defattr(-,root,root,755)
%{_texmfdistdir}/metapost/profcollege/PfCAfficheur.mp
%{_texmfdistdir}/metapost/profcollege/PfCArithmetique.mp
%{_texmfdistdir}/metapost/profcollege/PfCCalculatrice.mp
%{_texmfdistdir}/metapost/profcollege/PfCConstantes.mp
%{_texmfdistdir}/metapost/profcollege/PfCGeometrie.mp
%{_texmfdistdir}/metapost/profcollege/PfCLaTeX.mp
%{_texmfdistdir}/metapost/profcollege/PfCLabyNombre.mp
%{_texmfdistdir}/metapost/profcollege/PfCMonde.mp
%{_texmfdistdir}/metapost/profcollege/PfCMosaique.mp
%{_texmfdistdir}/metapost/profcollege/PfCScratch.mp
%{_texmfdistdir}/metapost/profcollege/PfCScratchpdf.mp
%{_texmfdistdir}/metapost/profcollege/PfCSvgnames.mp
%{_texmfdistdir}/tex/latex/profcollege/PfCEquationComposition2.tex
%{_texmfdistdir}/tex/latex/profcollege/PfCEquationLaurent1.tex
%{_texmfdistdir}/tex/latex/profcollege/PfCEquationPose1.tex
%{_texmfdistdir}/tex/latex/profcollege/PfCEquationSoustraction2.tex
%{_texmfdistdir}/tex/latex/profcollege/PfCEquationSymbole1.tex
%{_texmfdistdir}/tex/latex/profcollege/PfCEquationTerme1.tex
%{_texmfdistdir}/tex/latex/profcollege/ProfCollege.sty

%package -n texlive-proflycee
Version:        %{texlive_version}.%{texlive_noarch}.1.0.8svn62740
Release:        0
License:        LPPL-1.0
Summary:        A LaTeX package for French maths teachers in high school
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-proflycee-doc >= %{texlive_version}
Provides:       tex(ProfLycee.sty)
Requires:       tex(fancyvrb.sty)
Requires:       tex(fontawesome5.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(listofitems.sty)
Requires:       tex(mathtools.sty)
Requires:       tex(minted.sty)
Requires:       tex(pgf.sty)
Requires:       tex(pgffor.sty)
Requires:       tex(pythontex.sty)
Requires:       tex(simplekv.sty)
Requires:       tex(tabularray.sty)
Requires:       tex(tcolorbox.sty)
Requires:       tex(tikz.sty)
Requires:       tex(tkz-tab.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xfp.sty)
Requires:       tex(xintexpr.sty)
Requires:       tex(xkeyval.sty)
Requires:       tex(xparse.sty)
Requires:       tex(xstring.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source117:      proflycee.tar.xz
Source118:      proflycee.doc.tar.xz

%description -n texlive-proflycee
This package provides some commands to help French mathematics
teachers for 15-18 years olds, for example: \splinetikz to
create splines with "derivative control"; \paramCF and \ligneCF
in order to create an xcas-windows-like; \envconsolepythontex
and \envcodepythontex to create code presentation and code
execution with pythontex.

%package -n texlive-proflycee-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0.8svn62740
Release:        0
Summary:        Documentation for texlive-proflycee
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Provides:       locale(texlive-proflycee-doc:fr)

%description -n texlive-proflycee-doc
This package includes the documentation for texlive-proflycee

%post -n texlive-proflycee
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-proflycee
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-proflycee
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-proflycee-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/proflycee/ProfLycee-doc.pdf
%{_texmfdistdir}/doc/latex/proflycee/ProfLycee-doc.tex
%{_texmfdistdir}/doc/latex/proflycee/README.md

%files -n texlive-proflycee
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/proflycee/ProfLycee.sty

%package -n texlive-program
Version:        %{texlive_version}.%{texlive_noarch}.3.3.14svn44214
Release:        0
License:        GPL-2.0-or-later
Summary:        Typesetting programs and algorithms
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-program-doc >= %{texlive_version}
Provides:       tex(program.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source119:      program.tar.xz
Source120:      program.doc.tar.xz

%description -n texlive-program
The main offering is a program environment; a programbox
environment is available for fragments that must not break with
the pages.

%package -n texlive-program-doc
Version:        %{texlive_version}.%{texlive_noarch}.3.3.14svn44214
Release:        0
Summary:        Documentation for texlive-program
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/

%description -n texlive-program-doc
This package includes the documentation for texlive-program

%post -n texlive-program
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-program
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-program
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-program-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/program/README
%{_texmfdistdir}/doc/latex/program/gpl-3.0.txt
%{_texmfdistdir}/doc/latex/program/plink.tex
%{_texmfdistdir}/doc/latex/program/program-demo.tex
%{_texmfdistdir}/doc/latex/program/program-doc.pdf
%{_texmfdistdir}/doc/latex/program/program-doc.tex

%files -n texlive-program
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/program/program.sty

%package -n texlive-progress
Version:        %{texlive_version}.%{texlive_noarch}.1.10svn19519
Release:        0
License:        LPPL-1.0
Summary:        Creates an overview of a document's state
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-progress-doc >= %{texlive_version}
Provides:       tex(progress.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source121:      progress.tar.xz
Source122:      progress.doc.tar.xz

%description -n texlive-progress
Progress is a package which. when compiling TeX and LaTeX
documents, generates a HTML file showing an overview of a
document's state (of how finished it is). The report is sent to
file \ProgressReportName, which is by default the \jobname with
the date appended (but is user-modifiable).

%package -n texlive-progress-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.10svn19519
Release:        0
Summary:        Documentation for texlive-progress
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/

%description -n texlive-progress-doc
This package includes the documentation for texlive-progress

%post -n texlive-progress
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-progress
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-progress
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-progress-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/progress/README
%{_texmfdistdir}/doc/latex/progress/progress.pdf
%{_texmfdistdir}/doc/latex/progress/progress.tex
%{_texmfdistdir}/doc/latex/progress/progress20030701.html

%files -n texlive-progress
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/progress/progress.sty

%package -n texlive-progressbar
Version:        %{texlive_version}.%{texlive_noarch}.1.0b_4svn33822
Release:        0
License:        LPPL-1.0
Summary:        Visualize shares of total amounts in the form of a (progress-)bar
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-progressbar-doc >= %{texlive_version}
Provides:       tex(progressbar.sty)
Requires:       tex(calc.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(kvsetkeys.sty)
Requires:       tex(tikz.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source123:      progressbar.tar.xz
Source124:      progressbar.doc.tar.xz

%description -n texlive-progressbar
This package allows you to easily visualize shares of total
amounts in the form of a bar. So basically you can convert any
number between 0 and 1 to a progressbar using the command
\progressbar{<number>}. Also a lot of customizations are
possible, allowing you to create an unique progressbar on your
own. The package uses TikZ to produce its graphics.

%package -n texlive-progressbar-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0b_4svn33822
Release:        0
Summary:        Documentation for texlive-progressbar
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/

%description -n texlive-progressbar-doc
This package includes the documentation for texlive-progressbar

%post -n texlive-progressbar
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-progressbar
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-progressbar
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-progressbar-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/progressbar/README
%{_texmfdistdir}/doc/latex/progressbar/progressbar.pdf
%{_texmfdistdir}/doc/latex/progressbar/progressbar.tex

%files -n texlive-progressbar
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/progressbar/progressbar.sty

%package -n texlive-projlib
Version:        %{texlive_version}.%{texlive_noarch}.svn62900
Release:        0
License:        LPPL-1.0
Summary:        A series of tools to simplify your workflow
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-projlib-doc >= %{texlive_version}
Provides:       tex(ProjLib.sty)
Provides:       tex(projlib-author.sty)
Provides:       tex(projlib-datetime.sty)
Provides:       tex(projlib-draft.sty)
Provides:       tex(projlib-font.sty)
Provides:       tex(projlib-language.sty)
Provides:       tex(projlib-logo.sty)
Provides:       tex(projlib-math.sty)
Provides:       tex(projlib-paper.sty)
Provides:       tex(projlib-theorem.sty)
Provides:       tex(projlib-titlepage.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(amsthm.sty)
Requires:       tex(anyfontsize.sty)
Requires:       tex(babel.sty)
Requires:       tex(biolinum.sty)
Requires:       tex(cfr-lm.sty)
Requires:       tex(create-theorem.sty)
Requires:       tex(csquotes.sty)
Requires:       tex(ebgaramond-maths.sty)
Requires:       tex(ebgaramond.sty)
Requires:       tex(eulervm.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(l3keys2e.sty)
Requires:       tex(lmodern.sty)
Requires:       tex(mathastext.sty)
Requires:       tex(mathpazo.sty)
Requires:       tex(mathrsfs.sty)
Requires:       tex(mathtools.sty)
Requires:       tex(microtype.sty)
Requires:       tex(newpxtext.sty)
Requires:       tex(newtxmath.sty)
Requires:       tex(newtxtext.sty)
Requires:       tex(notomath.sty)
Requires:       tex(regexpatch.sty)
Requires:       tex(scontents.sty)
Requires:       tex(setspace.sty)
Requires:       tex(silence.sty)
Requires:       tex(tikz.sty)
Requires:       tex(ulem.sty)
Requires:       tex(unicode-math.sty)
Requires:       tex(xcolor.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source125:      projlib.tar.xz
Source126:      projlib.doc.tar.xz

%description -n texlive-projlib
ProjLib is a collection of tools to help you write LaTeX
documents. With the main package ProjLib loaded, you no longer
need to set up the theorem-like environments, nor to manually
configure the appropriate multilingual settings. In addition, a
series of auxiliary functionalities are introduced.

%package -n texlive-projlib-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn62900
Release:        0
Summary:        Documentation for texlive-projlib
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Provides:       locale(texlive-projlib-doc:zh;en;fr)

%description -n texlive-projlib-doc
This package includes the documentation for texlive-projlib

%post -n texlive-projlib
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-projlib
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-projlib
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-projlib-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/projlib/LICENSE
%{_texmfdistdir}/doc/latex/projlib/ProjLib-doc-cn.pdf
%{_texmfdistdir}/doc/latex/projlib/ProjLib-doc-cn.tex
%{_texmfdistdir}/doc/latex/projlib/ProjLib-doc-en.pdf
%{_texmfdistdir}/doc/latex/projlib/ProjLib-doc-en.tex
%{_texmfdistdir}/doc/latex/projlib/ProjLib-doc-fr.pdf
%{_texmfdistdir}/doc/latex/projlib/ProjLib-doc-fr.tex
%{_texmfdistdir}/doc/latex/projlib/README.md

%files -n texlive-projlib
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/projlib/ProjLib.sty
%{_texmfdistdir}/tex/latex/projlib/projlib-author.sty
%{_texmfdistdir}/tex/latex/projlib/projlib-datetime.sty
%{_texmfdistdir}/tex/latex/projlib/projlib-draft.sty
%{_texmfdistdir}/tex/latex/projlib/projlib-font.sty
%{_texmfdistdir}/tex/latex/projlib/projlib-language.sty
%{_texmfdistdir}/tex/latex/projlib/projlib-logo.sty
%{_texmfdistdir}/tex/latex/projlib/projlib-math.sty
%{_texmfdistdir}/tex/latex/projlib/projlib-paper.sty
%{_texmfdistdir}/tex/latex/projlib/projlib-theorem.sty
%{_texmfdistdir}/tex/latex/projlib/projlib-titlepage.sty

%package -n texlive-proof-at-the-end
Version:        %{texlive_version}.%{texlive_noarch}.svn61933
Release:        0
License:        LPPL-1.0
Summary:        A package to move proofs to appendix
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-proof-at-the-end-doc >= %{texlive_version}
Provides:       tex(proof-at-the-end.sty)
Requires:       tex(catchfile.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(pgfkeys.sty)
Requires:       tex(thm-restate.sty)
Requires:       tex(thmtools.sty)
Requires:       tex(xparse.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source127:      proof-at-the-end.tar.xz
Source128:      proof-at-the-end.doc.tar.xz

%description -n texlive-proof-at-the-end
This package aims to provide a way to easily move proofs to the
appendix. You can (among other things) move proofs to different
places/sections, create links from theorems to proofs, restate
theorems, add comments in appendix...

%package -n texlive-proof-at-the-end-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn61933
Release:        0
Summary:        Documentation for texlive-proof-at-the-end
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/

%description -n texlive-proof-at-the-end-doc
This package includes the documentation for texlive-proof-at-the-end

%post -n texlive-proof-at-the-end
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-proof-at-the-end
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-proof-at-the-end
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-proof-at-the-end-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/proof-at-the-end/README.md
%{_texmfdistdir}/doc/latex/proof-at-the-end/proof-at-the-end.pdf
%{_texmfdistdir}/doc/latex/proof-at-the-end/proof-at-the-end_demo.pdf
%{_texmfdistdir}/doc/latex/proof-at-the-end/proof-at-the-end_demo.tex

%files -n texlive-proof-at-the-end
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/proof-at-the-end/proof-at-the-end.sty

%package -n texlive-proofread
Version:        %{texlive_version}.%{texlive_noarch}.1.04svn61719
Release:        0
License:        LPPL-1.0
Summary:        Commands for inserting annotations
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-proofread-doc >= %{texlive_version}
Provides:       tex(proofread.sty)
Requires:       tex(marginnote.sty)
Requires:       tex(setspace.sty)
Requires:       tex(soul.sty)
Requires:       tex(tikz.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source129:      proofread.tar.xz
Source130:      proofread.doc.tar.xz

%description -n texlive-proofread
This package defines a few LaTeX commands that may be useful
when you proofread a LaTeX document. They allow you to easily
highlight text and add comments in the margin. Vim escape
sequences are provided for inserting or removing these LaTeX
commands in the source. Options are provided for displaying the
document with extra line spacing, and for displaying it in
either corrected or uncorrected state, both without margin
notes. The package is based on code for a text highlighting
command that was published by Antal Spector-Zabusky on
https://tex.stackexchange.com/questions/5959. The main file,
proofread.dtx, is self-extracting, so you can generate the
style file by compiling proofread.dtx with pdfLaTeX. This
package is based on the soul package; so if you plan to
highlight non-ASCII characters, you must compile your source
with either XeTeX- or LuaTeX-based compilers.

%package -n texlive-proofread-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.04svn61719
Release:        0
Summary:        Documentation for texlive-proofread
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/

%description -n texlive-proofread-doc
This package includes the documentation for texlive-proofread

%post -n texlive-proofread
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-proofread
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-proofread
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-proofread-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/proofread/README
%{_texmfdistdir}/doc/latex/proofread/README.txt
%{_texmfdistdir}/doc/latex/proofread/example.pdf
%{_texmfdistdir}/doc/latex/proofread/example.tex
%{_texmfdistdir}/doc/latex/proofread/proofread.pdf
%{_texmfdistdir}/doc/latex/proofread/proofread.vmb

%files -n texlive-proofread
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/proofread/proofread.sty

%package -n texlive-prooftrees
Version:        %{texlive_version}.%{texlive_noarch}.0.0.7_svn_8641svn52221
Release:        0
License:        LPPL-1.0
Summary:        Forest-based proof trees (symbolic logic)
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-prooftrees-doc >= %{texlive_version}
Provides:       tex(prooftrees.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(forest.sty)
Requires:       tex(svn-prov.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source131:      prooftrees.tar.xz
Source132:      prooftrees.doc.tar.xz

%description -n texlive-prooftrees
The package supports drawing proof trees of the kind often used
in introductory logic classes, especially those aimed at
students without strong mathemtical backgrounds. Hodges (1991)
is one example of a text which uses this system. When teaching
such a system it is especially useful to annotate the tree with
line numbers, justifications and explanations of branch
closures. prooftrees provides a single environment, prooftree,
and a variety of tools for annotating, customising and
highlighting such trees. A cross-referencing system is provided
for trees which cite line numbers in justifications for proof
lines or branch closures. prooftrees is based on forest and,
hence, TikZ. The package requires version 2.0.2 of Forest for
expected results and will not work with version 1.

%package -n texlive-prooftrees-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.7_svn_8641svn52221
Release:        0
Summary:        Documentation for texlive-prooftrees
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/

%description -n texlive-prooftrees-doc
This package includes the documentation for texlive-prooftrees

%post -n texlive-prooftrees
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-prooftrees
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-prooftrees
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-prooftrees-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/prooftrees/README
%{_texmfdistdir}/doc/latex/prooftrees/manifest.txt
%{_texmfdistdir}/doc/latex/prooftrees/prooftrees.pdf
%{_texmfdistdir}/doc/latex/prooftrees/prooftrees.tex
%{_texmfdistdir}/doc/latex/prooftrees/prooftrees_biber.bib

%files -n texlive-prooftrees
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/prooftrees/prooftrees.sty

%package -n texlive-properties
Version:        %{texlive_version}.%{texlive_noarch}.0.0.2svn15878
Release:        0
License:        LPPL-1.0
Summary:        Load properties from a file
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-properties-doc >= %{texlive_version}
Provides:       tex(properties.sty)
Requires:       tex(datatool.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source133:      properties.tar.xz
Source134:      properties.doc.tar.xz

%description -n texlive-properties
The package loads properties (key, value) from a properties
file, e.g. \jobname.properties.

%package -n texlive-properties-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.2svn15878
Release:        0
Summary:        Documentation for texlive-properties
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/

%description -n texlive-properties-doc
This package includes the documentation for texlive-properties

%post -n texlive-properties
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-properties
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-properties
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-properties-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/properties/readme.de
%{_texmfdistdir}/doc/latex/properties/testprop.tex

%files -n texlive-properties
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/properties/properties.sty

%package -n texlive-proposal
Version:        %{texlive_version}.%{texlive_noarch}.svn40538
Release:        0
License:        LPPL-1.0
Summary:        A set of LaTeX classes for preparing proposals for collaborative projects
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-proposal-doc >= %{texlive_version}
Provides:       tex(dfgpdata.sty)
Provides:       tex(dfgproposal.cls)
Provides:       tex(dfgreporting.cls)
Provides:       tex(eupdata.sty)
Provides:       tex(euproposal.cls)
Provides:       tex(eureporting.cls)
Provides:       tex(pdata.sty)
Provides:       tex(proposal.cls)
Provides:       tex(reporting.cls)
Requires:       tex(amssymb.sty)
Requires:       tex(array.sty)
Requires:       tex(babel.sty)
Requires:       tex(biblatex.sty)
Requires:       tex(boxedminipage.sty)
Requires:       tex(chngcntr.sty)
Requires:       tex(colortbl.sty)
Requires:       tex(comment.sty)
Requires:       tex(csquotes.sty)
Requires:       tex(ed.sty)
Requires:       tex(eurosym.sty)
Requires:       tex(fancyhdr.sty)
Requires:       tex(geometry.sty)
Requires:       tex(gitinfo2.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(helvet.sty)
Requires:       tex(longtable.sty)
Requires:       tex(mdframed.sty)
Requires:       tex(paralist.sty)
Requires:       tex(rotating.sty)
Requires:       tex(svninfo.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(tikz.sty)
Requires:       tex(url.sty)
Requires:       tex(wasysym.sty)
Requires:       tex(wrapfig.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xspace.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source135:      proposal.tar.xz
Source136:      proposal.doc.tar.xz

%description -n texlive-proposal
The process of preparing a collaborative proposal, to a major
funding body, involves integration of contributions of a many
people at many sites. It is therefore an ideal application for
a text-based document preparation system such as LaTeX, in
concert with a distributed version control system such as SVN.
The proposal class itself provides a basis for such an
enterprise. The dfgproposal and dfgproposal classes provide two
specialisations of the base class for (respectively) German and
European research proposals. The packages depend on the
author's stex bundle.

%package -n texlive-proposal-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn40538
Release:        0
Summary:        Documentation for texlive-proposal
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/

%description -n texlive-proposal-doc
This package includes the documentation for texlive-proposal

%post -n texlive-proposal
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-proposal
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-proposal
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-proposal-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/proposal/base/README
%{_texmfdistdir}/doc/latex/proposal/dfg/README
%{_texmfdistdir}/doc/latex/proposal/dfg/dfgproposal.pdf
%{_texmfdistdir}/doc/latex/proposal/dfg/proposal/Makefile
%{_texmfdistdir}/doc/latex/proposal/dfg/proposal/funds.tex
%{_texmfdistdir}/doc/latex/proposal/dfg/proposal/preconditions.tex
%{_texmfdistdir}/doc/latex/proposal/dfg/proposal/proposal.pdf
%{_texmfdistdir}/doc/latex/proposal/dfg/proposal/proposal.tex
%{_texmfdistdir}/doc/latex/proposal/dfg/proposal/public.pdf
%{_texmfdistdir}/doc/latex/proposal/dfg/proposal/public.tex
%{_texmfdistdir}/doc/latex/proposal/dfg/proposal/state.tex
%{_texmfdistdir}/doc/latex/proposal/dfg/proposal/submit.pdf
%{_texmfdistdir}/doc/latex/proposal/dfg/proposal/submit.tex
%{_texmfdistdir}/doc/latex/proposal/dfg/proposal/workplan.tex
%{_texmfdistdir}/doc/latex/proposal/dfg/proposal/zusammenfassung.tex
%{_texmfdistdir}/doc/latex/proposal/dfg/report/Makefile
%{_texmfdistdir}/doc/latex/proposal/dfg/report/README
%{_texmfdistdir}/doc/latex/proposal/dfg/report/finalreport.pdf
%{_texmfdistdir}/doc/latex/proposal/dfg/report/finalreport.tex
%{_texmfdistdir}/doc/latex/proposal/dfg/report/letter_submission.pdf
%{_texmfdistdir}/doc/latex/proposal/dfg/report/letter_submission.tex
%{_texmfdistdir}/doc/latex/proposal/dfg/report/progressreport.tex
%{_texmfdistdir}/doc/latex/proposal/dfg/report/progresssummary.tex
%{_texmfdistdir}/doc/latex/proposal/eu/README
%{_texmfdistdir}/doc/latex/proposal/eu/euproposal.pdf
%{_texmfdistdir}/doc/latex/proposal/eu/strep/Makefile
%{_texmfdistdir}/doc/latex/proposal/eu/strep/README
%{_texmfdistdir}/doc/latex/proposal/eu/strep/deliverables.tex
%{_texmfdistdir}/doc/latex/proposal/eu/strep/draft.tex
%{_texmfdistdir}/doc/latex/proposal/eu/strep/final.tex
%{_texmfdistdir}/doc/latex/proposal/eu/strep/grantagreement.tex
%{_texmfdistdir}/doc/latex/proposal/eu/strep/impact.tex
%{_texmfdistdir}/doc/latex/proposal/eu/strep/implementation.tex
%{_texmfdistdir}/doc/latex/proposal/eu/strep/issues.tex
%{_texmfdistdir}/doc/latex/proposal/eu/strep/methodology.tex
%{_texmfdistdir}/doc/latex/proposal/eu/strep/milestones.tex
%{_texmfdistdir}/doc/latex/proposal/eu/strep/objectives.tex
%{_texmfdistdir}/doc/latex/proposal/eu/strep/progress.tex
%{_texmfdistdir}/doc/latex/proposal/eu/strep/propB.pdf
%{_texmfdistdir}/doc/latex/proposal/eu/strep/propB.tex
%{_texmfdistdir}/doc/latex/proposal/eu/strep/public.pdf
%{_texmfdistdir}/doc/latex/proposal/eu/strep/public.tex
%{_texmfdistdir}/doc/latex/proposal/eu/strep/quality.tex
%{_texmfdistdir}/doc/latex/proposal/eu/strep/risks.tex
%{_texmfdistdir}/doc/latex/proposal/eu/strep/site-bar.tex
%{_texmfdistdir}/doc/latex/proposal/eu/strep/site-baz.tex
%{_texmfdistdir}/doc/latex/proposal/eu/strep/site-efo.tex
%{_texmfdistdir}/doc/latex/proposal/eu/strep/site-jacu.tex
%{_texmfdistdir}/doc/latex/proposal/eu/strep/site-templatex.tex
%{_texmfdistdir}/doc/latex/proposal/eu/strep/submit.pdf
%{_texmfdistdir}/doc/latex/proposal/eu/strep/submit.tex
%{_texmfdistdir}/doc/latex/proposal/eu/strep/workplan.tex
%{_texmfdistdir}/doc/latex/proposal/eu/strep/wp-class.tex
%{_texmfdistdir}/doc/latex/proposal/eu/strep/wp-dissem.tex
%{_texmfdistdir}/doc/latex/proposal/eu/strep/wp-management.tex
%{_texmfdistdir}/doc/latex/proposal/eu/strep/wp-temple.tex

%files -n texlive-proposal
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/proposal/base/pdata.sty
%{_texmfdistdir}/tex/latex/proposal/base/proposal.cls
%{_texmfdistdir}/tex/latex/proposal/base/reporting.cls
%{_texmfdistdir}/tex/latex/proposal/dfg/dfgpdata.sty
%{_texmfdistdir}/tex/latex/proposal/dfg/dfgproposal.cls
%{_texmfdistdir}/tex/latex/proposal/dfg/dfgreporting.cls
%{_texmfdistdir}/tex/latex/proposal/eu/eupdata.sty
%{_texmfdistdir}/tex/latex/proposal/eu/euproposal.cls
%{_texmfdistdir}/tex/latex/proposal/eu/eureporting.cls

%package -n texlive-prosper
Version:        %{texlive_version}.%{texlive_noarch}.1.0hsvn33033
Release:        0
License:        LPPL-1.0
Summary:        LaTeX class for high quality slides
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-prosper-doc >= %{texlive_version}
Provides:       tex(PPRalcatel.sty)
Provides:       tex(PPRalienglow.sty)
Provides:       tex(PPRautumn.sty)
Provides:       tex(PPRazure.sty)
Provides:       tex(PPRblends.sty)
Provides:       tex(PPRcapsules.sty)
Provides:       tex(PPRcontemporain.sty)
Provides:       tex(PPRcorners.sty)
Provides:       tex(PPRdarkblue.sty)
Provides:       tex(PPRdefault.sty)
Provides:       tex(PPRframes.sty)
Provides:       tex(PPRfyma.sty)
Provides:       tex(PPRgyom.sty)
Provides:       tex(PPRlignesbleues.sty)
Provides:       tex(PPRmancini.sty)
Provides:       tex(PPRnuancegris.sty)
Provides:       tex(PPRprettybox.sty)
Provides:       tex(PPRrico.sty)
Provides:       tex(PPRserpaggi.sty)
Provides:       tex(PPRthomasd.sty)
Provides:       tex(PPRtroispoints.sty)
Provides:       tex(PPRwhitecross.sty)
Provides:       tex(PPRwinter.sty)
Provides:       tex(PPRwj.sty)
Provides:       tex(prosper.cls)
Requires:       tex(amssymb.sty)
Requires:       tex(fp.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(mathpazo.sty)
Requires:       tex(multido.sty)
Requires:       tex(palatino.sty)
Requires:       tex(pst-grad.sty)
Requires:       tex(pst-slpe.sty)
Requires:       tex(semhelv.sty)
Requires:       tex(seminar.cls)
Requires:       tex(times.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source137:      prosper.tar.xz
Source138:      prosper.doc.tar.xz
Source139:      prosper_utf8.dif

%description -n texlive-prosper
Prosper is a LaTeX class for writing transparencies. It is
written as an extension of the seminar class by Timothy Van
Zandt. Prosper offers a friendly environment for creating
slides for both presentations with an overhead projector and a
video projector. Slides prepared for a presentation with a
computer and a video projector may integrate animation effects,
incremental display, and so on. Various visual styles are
supported (including some that mimic PowerPoint) and others are
being contributed.

%package -n texlive-prosper-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0hsvn33033
Release:        0
Summary:        Documentation for texlive-prosper
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/

%description -n texlive-prosper-doc
This package includes the documentation for texlive-prosper

%post -n texlive-prosper
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-prosper
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-prosper
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-prosper-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/prosper/AUTHORS
%{_texmfdistdir}/doc/latex/prosper/ChangeLog
%{_texmfdistdir}/doc/latex/prosper/Example.tex
%{_texmfdistdir}/doc/latex/prosper/ExampleAlienglow.tex
%{_texmfdistdir}/doc/latex/prosper/ExampleAutumn.tex
%{_texmfdistdir}/doc/latex/prosper/ExampleAzure.tex
%{_texmfdistdir}/doc/latex/prosper/ExampleContemporain.tex
%{_texmfdistdir}/doc/latex/prosper/ExampleDarkblue.tex
%{_texmfdistdir}/doc/latex/prosper/ExampleFrames.tex
%{_texmfdistdir}/doc/latex/prosper/ExampleLignesbleues.tex
%{_texmfdistdir}/doc/latex/prosper/ExampleNuanceGris.tex
%{_texmfdistdir}/doc/latex/prosper/ExampleTroisPoints.tex
%{_texmfdistdir}/doc/latex/prosper/FAQ
%{_texmfdistdir}/doc/latex/prosper/INSTALL
%{_texmfdistdir}/doc/latex/prosper/NEWS
%{_texmfdistdir}/doc/latex/prosper/README
%{_texmfdistdir}/doc/latex/prosper/TODO
%{_texmfdistdir}/doc/latex/prosper/compilation.fig
%{_texmfdistdir}/doc/latex/prosper/green-bullet-on-blue-wc.gif
%{_texmfdistdir}/doc/latex/prosper/green-bullet-on-blue.gif
%{_texmfdistdir}/doc/latex/prosper/green-bullet-on-white.gif
%{_texmfdistdir}/doc/latex/prosper/gyom.tex
%{_texmfdistdir}/doc/latex/prosper/manifest.txt
%{_texmfdistdir}/doc/latex/prosper/prosper-doc.pdf
%{_texmfdistdir}/doc/latex/prosper/prosper-doc.tex
%{_texmfdistdir}/doc/latex/prosper/prosper-structure.fig
%{_texmfdistdir}/doc/latex/prosper/prosper-template.jpg
%{_texmfdistdir}/doc/latex/prosper/prosper-tour.pdf
%{_texmfdistdir}/doc/latex/prosper/prosper-tour.tex
%{_texmfdistdir}/doc/latex/prosper/prosper.png
%{_texmfdistdir}/doc/latex/prosper/prosper.ui
%{_texmfdistdir}/doc/latex/prosper/red-bullet-on-blue-wc.gif
%{_texmfdistdir}/doc/latex/prosper/red-bullet-on-blue.gif
%{_texmfdistdir}/doc/latex/prosper/red-bullet-on-white.gif
%{_texmfdistdir}/doc/latex/prosper/rico.tex
%{_texmfdistdir}/doc/latex/prosper/rotation.tex
%{_texmfdistdir}/doc/latex/prosper/seminar-bg2-lepennec.fix
%{_texmfdistdir}/doc/latex/prosper/yellow-bullet-on-blue-wc.gif
%{_texmfdistdir}/doc/latex/prosper/yellow-bullet-on-blue.gif
%{_texmfdistdir}/doc/latex/prosper/yellow-bullet-on-white.gif

%files -n texlive-prosper
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/prosper/PPRalcatel.sty
%{_texmfdistdir}/tex/latex/prosper/PPRalienglow.sty
%{_texmfdistdir}/tex/latex/prosper/PPRautumn.sty
%{_texmfdistdir}/tex/latex/prosper/PPRazure.sty
%{_texmfdistdir}/tex/latex/prosper/PPRblends.sty
%{_texmfdistdir}/tex/latex/prosper/PPRcapsules.sty
%{_texmfdistdir}/tex/latex/prosper/PPRcontemporain.sty
%{_texmfdistdir}/tex/latex/prosper/PPRcorners.sty
%{_texmfdistdir}/tex/latex/prosper/PPRdarkblue.sty
%{_texmfdistdir}/tex/latex/prosper/PPRdefault.sty
%{_texmfdistdir}/tex/latex/prosper/PPRframes.sty
%{_texmfdistdir}/tex/latex/prosper/PPRfyma.sty
%{_texmfdistdir}/tex/latex/prosper/PPRgyom.sty
%{_texmfdistdir}/tex/latex/prosper/PPRlignesbleues.sty
%{_texmfdistdir}/tex/latex/prosper/PPRmancini.sty
%{_texmfdistdir}/tex/latex/prosper/PPRnuancegris.sty
%{_texmfdistdir}/tex/latex/prosper/PPRprettybox.sty
%{_texmfdistdir}/tex/latex/prosper/PPRrico.sty
%{_texmfdistdir}/tex/latex/prosper/PPRserpaggi.sty
%{_texmfdistdir}/tex/latex/prosper/PPRthomasd.sty
%{_texmfdistdir}/tex/latex/prosper/PPRtroispoints.sty
%{_texmfdistdir}/tex/latex/prosper/PPRwhitecross.sty
%{_texmfdistdir}/tex/latex/prosper/PPRwinter.sty
%{_texmfdistdir}/tex/latex/prosper/PPRwj.sty
%{_texmfdistdir}/tex/latex/prosper/angleHG.ps
%{_texmfdistdir}/tex/latex/prosper/arrow-glow.ps
%{_texmfdistdir}/tex/latex/prosper/barre-rico.ps
%{_texmfdistdir}/tex/latex/prosper/blue-inverted-arrow.ps
%{_texmfdistdir}/tex/latex/prosper/boule-base.eps
%{_texmfdistdir}/tex/latex/prosper/boulebleue-fondblanc.eps
%{_texmfdistdir}/tex/latex/prosper/boulerouge-fondblanc.eps
%{_texmfdistdir}/tex/latex/prosper/bouleverte-fondblanc.eps
%{_texmfdistdir}/tex/latex/prosper/bullet-glow.ps
%{_texmfdistdir}/tex/latex/prosper/compilation.eps
%{_texmfdistdir}/tex/latex/prosper/degrade-base.eps
%{_texmfdistdir}/tex/latex/prosper/degrade-blanc-bleu.eps
%{_texmfdistdir}/tex/latex/prosper/green-bullet-on-blue-wc.ps
%{_texmfdistdir}/tex/latex/prosper/green-bullet-on-blue.ps
%{_texmfdistdir}/tex/latex/prosper/green-bullet-on-white.ps
%{_texmfdistdir}/tex/latex/prosper/green-inverted-arrow.ps
%{_texmfdistdir}/tex/latex/prosper/gyom.ps
%{_texmfdistdir}/tex/latex/prosper/prosper-structure.eps
%{_texmfdistdir}/tex/latex/prosper/prosper.cls
%{_texmfdistdir}/tex/latex/prosper/red-bullet-on-blue-wc.ps
%{_texmfdistdir}/tex/latex/prosper/red-bullet-on-blue.ps
%{_texmfdistdir}/tex/latex/prosper/red-bullet-on-white.ps
%{_texmfdistdir}/tex/latex/prosper/red-inverted-arrow.ps
%{_texmfdistdir}/tex/latex/prosper/rico.ps
%{_texmfdistdir}/tex/latex/prosper/rico_bullet1.ps
%{_texmfdistdir}/tex/latex/prosper/rico_bullet2.ps
%{_texmfdistdir}/tex/latex/prosper/rico_bullet3.ps
%{_texmfdistdir}/tex/latex/prosper/rotation.ps
%{_texmfdistdir}/tex/latex/prosper/rule-glow.ps
%{_texmfdistdir}/tex/latex/prosper/yellow-bullet-on-blue-wc.ps
%{_texmfdistdir}/tex/latex/prosper/yellow-bullet-on-blue.ps
%{_texmfdistdir}/tex/latex/prosper/yellow-bullet-on-white.ps

%package -n texlive-protex
Version:        %{texlive_version}.%{texlive_noarch}.svn41633
Release:        0
License:        LPPL-1.0
Summary:        Literate programming package
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-protex-doc >= %{texlive_version}
Provides:       tex(AlProTex.sty)
Provides:       tex(ProTex.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source140:      protex.tar.xz
Source141:      protex.doc.tar.xz

%description -n texlive-protex
ProTeX is a simple but powerful literate programming tool,
which is designed to generate useful hypertext output (either
PDF, or HTML using TeX4ht).

%package -n texlive-protex-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn41633
Release:        0
Summary:        Documentation for texlive-protex
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/

%description -n texlive-protex-doc
This package includes the documentation for texlive-protex

%post -n texlive-protex
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-protex
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-protex
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-protex-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/protex/ChangeLog
%{_texmfdistdir}/doc/latex/protex/README

%files -n texlive-protex
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/protex/AlProTex.sty
%{_texmfdistdir}/tex/latex/protex/ProTex.sty

%package -n texlive-protocol
Version:        %{texlive_version}.%{texlive_noarch}.1.13svn25562
Release:        0
License:        LPPL-1.0
Summary:        A class for minutes of meetings
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-protocol-doc >= %{texlive_version}
Provides:       tex(protocol.cls)
Requires:       tex(scrartcl.cls)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source142:      protocol.tar.xz
Source143:      protocol.doc.tar.xz

%description -n texlive-protocol
The present version of the class supports German meeting
minutes including vote results and action items. The author has
ambitions to internationalise the code, and would welcome
support in the work.

%package -n texlive-protocol-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.13svn25562
Release:        0
Summary:        Documentation for texlive-protocol
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Provides:       locale(texlive-protocol-doc:en;de)

%description -n texlive-protocol-doc
This package includes the documentation for texlive-protocol

%post -n texlive-protocol
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-protocol
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-protocol
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-protocol-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/protocol/README
%{_texmfdistdir}/doc/latex/protocol/protest.tex
%{_texmfdistdir}/doc/latex/protocol/protocol.pdf

%files -n texlive-protocol
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/protocol/protocol.cls

%package -n texlive-prtec
Version:        %{texlive_version}.%{texlive_noarch}.1.06svn51919
Release:        0
License:        LPPL-1.0
Summary:        A template for PRTEC conference papers
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-prtec-doc >= %{texlive_version}
Provides:       tex(prtec.cls)
Requires:       tex(array.sty)
Requires:       tex(article.cls)
Requires:       tex(bm.sty)
Requires:       tex(booktabs.sty)
Requires:       tex(caption.sty)
Requires:       tex(dcolumn.sty)
Requires:       tex(doi.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(fancyhdr.sty)
Requires:       tex(fnpos.sty)
Requires:       tex(geometry.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(hologo.sty)
Requires:       tex(hyperxmp.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(inputenc.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(kvsetkeys.sty)
Requires:       tex(mathtools.sty)
Requires:       tex(metalogo.sty)
Requires:       tex(multicol.sty)
Requires:       tex(natbib.sty)
Requires:       tex(newtxmath.sty)
Requires:       tex(newtxtext.sty)
Requires:       tex(parskip.sty)
Requires:       tex(subcaption.sty)
Requires:       tex(textcase.sty)
Requires:       tex(titlesec.sty)
Requires:       tex(xcoffins.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xparse.sty)
Requires:       tex(xpatch.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source144:      prtec.tar.xz
Source145:      prtec.doc.tar.xz

%description -n texlive-prtec
This package provides a LaTeX class, a BibTeX style, and a
LaTeX template to format conference papers for the Pacific Rim
Thermal Engineering Conference (PRTEC). The .tex and .cls files
are commented and should be self-explanatory. The package
depends on newtx.

%package -n texlive-prtec-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.06svn51919
Release:        0
Summary:        Documentation for texlive-prtec
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/

%description -n texlive-prtec-doc
This package includes the documentation for texlive-prtec

%post -n texlive-prtec
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-prtec
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-prtec
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-prtec-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/prtec/PRTEC19-template.pdf
%{_texmfdistdir}/doc/latex/prtec/PRTEC19-template.tex
%{_texmfdistdir}/doc/latex/prtec/README.md
%{_texmfdistdir}/doc/latex/prtec/prtec-sample.bib
%{_texmfdistdir}/doc/latex/prtec/sample-figure.pdf

%files -n texlive-prtec
%defattr(-,root,root,755)
%{_texmfdistdir}/bibtex/bst/prtec/prtec.bst
%{_texmfdistdir}/tex/latex/prtec/prtec.cls

%package -n texlive-przechlewski-book
Version:        %{texlive_version}.%{texlive_noarch}.svn23552
Release:        0
License:        LPPL-1.0
Summary:        Examples from Przechlewski's LaTeX book
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-przechlewski-book-doc >= %{texlive_version}
Provides:       tex(upmgr.cls)
Provides:       tex(wkmgr.cls)
Requires:       tex(caption.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(polski.sty)
Requires:       tex(prelim2e.sty)
Requires:       tex(report.cls)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source146:      przechlewski-book.tar.xz
Source147:      przechlewski-book.doc.tar.xz

%description -n texlive-przechlewski-book
The bundle provides machine-readable copies of the examples
from the book "Praca magisterska i dyplomowa z programem
LaTeX".

%package -n texlive-przechlewski-book-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn23552
Release:        0
Summary:        Documentation for texlive-przechlewski-book
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Provides:       locale(texlive-przechlewski-book-doc:en;pl)

%description -n texlive-przechlewski-book-doc
This package includes the documentation for texlive-przechlewski-book

%post -n texlive-przechlewski-book
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-przechlewski-book
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-przechlewski-book
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-przechlewski-book-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/przechlewski-book/LICENSE
%{_texmfdistdir}/doc/latex/przechlewski-book/Makefile
%{_texmfdistdir}/doc/latex/przechlewski-book/README
%{_texmfdistdir}/doc/latex/przechlewski-book/README.pl
%{_texmfdistdir}/doc/latex/przechlewski-book/TAM-pl.pdf
%{_texmfdistdir}/doc/latex/przechlewski-book/b313.bib
%{_texmfdistdir}/doc/latex/przechlewski-book/p21.tex
%{_texmfdistdir}/doc/latex/przechlewski-book/p22.tex
%{_texmfdistdir}/doc/latex/przechlewski-book/p23.tex
%{_texmfdistdir}/doc/latex/przechlewski-book/p24.tex
%{_texmfdistdir}/doc/latex/przechlewski-book/p31.tex
%{_texmfdistdir}/doc/latex/przechlewski-book/p310.tex
%{_texmfdistdir}/doc/latex/przechlewski-book/p311.tex
%{_texmfdistdir}/doc/latex/przechlewski-book/p312.tex
%{_texmfdistdir}/doc/latex/przechlewski-book/p313.tex
%{_texmfdistdir}/doc/latex/przechlewski-book/p313_utf8.tex
%{_texmfdistdir}/doc/latex/przechlewski-book/p32.tex
%{_texmfdistdir}/doc/latex/przechlewski-book/p33.tex
%{_texmfdistdir}/doc/latex/przechlewski-book/p34.tex
%{_texmfdistdir}/doc/latex/przechlewski-book/p35.tex
%{_texmfdistdir}/doc/latex/przechlewski-book/p36.tex
%{_texmfdistdir}/doc/latex/przechlewski-book/p37.tex
%{_texmfdistdir}/doc/latex/przechlewski-book/p38.tex
%{_texmfdistdir}/doc/latex/przechlewski-book/p39.tex
%{_texmfdistdir}/doc/latex/przechlewski-book/p41.tex
%{_texmfdistdir}/doc/latex/przechlewski-book/p42.tex
%{_texmfdistdir}/doc/latex/przechlewski-book/p43.tex
%{_texmfdistdir}/doc/latex/przechlewski-book/p44.tex
%{_texmfdistdir}/doc/latex/przechlewski-book/p45.tex
%{_texmfdistdir}/doc/latex/przechlewski-book/p46.tex
%{_texmfdistdir}/doc/latex/przechlewski-book/rys1_5.tex
%{_texmfdistdir}/doc/latex/przechlewski-book/wkmgr.bib
%{_texmfdistdir}/doc/latex/przechlewski-book/wkmgr.html
%{_texmfdistdir}/doc/latex/przechlewski-book/wkmgr1.pdf
%{_texmfdistdir}/doc/latex/przechlewski-book/wkmgr1.tex
%{_texmfdistdir}/doc/latex/przechlewski-book/wkmgr2.pdf
%{_texmfdistdir}/doc/latex/przechlewski-book/wkmgr2.tex

%files -n texlive-przechlewski-book
%defattr(-,root,root,755)
%{_texmfdistdir}/bibtex/bst/przechlewski-book/papalike.bst
%{_texmfdistdir}/tex/latex/przechlewski-book/upmgr.cls
%{_texmfdistdir}/tex/latex/przechlewski-book/wkmgr.cls

%package -n texlive-ps2eps
Version:        %{texlive_version}.%{texlive_noarch}.1.70svn62856
Release:        0
License:        GPL-2.0-or-later
Summary:        Produce Encapsulated PostScript from PostScript
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Conflicts:      texlive-pstools
Provides:       texlive-pstools:%{_texmfdistdir}/scripts/ps2eps/ps2eps.pl
Requires(pre):  texlive-ps2eps-bin >= %{texlive_version}
#!BuildIgnore: texlive-ps2eps-bin
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-ps2eps-doc >= %{texlive_version}
Requires:       perl(Getopt::Long)
#!BuildIgnore:  perl(Getopt::Long)
Requires:       perl(POSIX)
#!BuildIgnore:  perl(POSIX)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source148:      ps2eps.tar.xz
Source149:      ps2eps.doc.tar.xz

%description -n texlive-ps2eps
Produce Encapsulated PostScript Files (EPS/EPSF) from a
one-page PostScript document, or any PostScript document. A
correct Bounding Box is calculated for the EPS files and some
PostScript command sequences that can produce errorneous
results on printers are filtered. The input is cropped to
include just the image contained in the PostScript file. The
EPS files can then be included into TeX documents. Other
programs like ps2epsi (a script distributed with ghostscript)
don't always calculate the correct bounding box (because the
values are put on the PostScript stack which may get corrupted
by bad PostScript code) or they round it off, resulting in
clipping the image. Therefore ps2eps uses a resolution of 144
dpi to get the correct bounding box. The bundle includes
binaries for Linux, Solaris, Digital Unix or Windows
2000/9x/NT; for other platforms, the user needs perl,
ghostscript and an ANSI-C compiler. Included in the
distribution is the bbox program, an application to produce
Bounding Box values for rawppm or rawpbm format files.

%package -n texlive-ps2eps-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.70svn62856
Release:        0
Summary:        Documentation for texlive-ps2eps
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Conflicts:      texlive-pstools-doc
Provides:       texlive-pstools-doc:%{_mandir}/man1/bbox.1%{?ext_man}
Provides:       texlive-pstools-doc:%{_mandir}/man1/ps2eps.1%{?ext_man}
Provides:       man(bbox.1)
Provides:       man(ps2eps.1)

%description -n texlive-ps2eps-doc
This package includes the documentation for texlive-ps2eps

%post -n texlive-ps2eps
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-ps2eps
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-ps2eps
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-ps2eps-doc
%defattr(-,root,root,755)
%{_mandir}/man1/bbox.1*
%{_mandir}/man1/ps2eps.1*

%files -n texlive-ps2eps
%defattr(-,root,root,755)
%{_texmfdistdir}/scripts/ps2eps/ps2eps.pl

%package -n texlive-ps2pk
Version:        %{texlive_version}.%{texlive_noarch}.svn52851
Release:        0
License:        LPPL-1.0
Summary:        Generate a PK font from an Adobe Type 1 font
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Obsoletes:      texlive-ps2pkm < 2015
Requires(pre):  texlive-ps2pk-bin >= %{texlive_version}
#!BuildIgnore: texlive-ps2pk-bin
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Provides:       man(mag.1)
Provides:       man(pfb2pfa.1)
Provides:       man(pk2bm.1)
Provides:       man(ps2pk.1)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source150:      ps2pk.doc.tar.xz

%description -n texlive-ps2pk
Generates a PK file from an Adobe Type 1 font. PK fonts are (or
used to be) valuable in enabling previewers to view documents
generated that use Type 1 fonts. The program makes use of code
donated to the X consortium by IBM.

%post -n texlive-ps2pk
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-ps2pk
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-ps2pk
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-ps2pk
%defattr(-,root,root,755)
%{_mandir}/man1/mag.1*
%{_mandir}/man1/pfb2pfa.1*
%{_mandir}/man1/pk2bm.1*
%{_mandir}/man1/ps2pk.1*

%package -n texlive-psbao
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn55013
Release:        0
License:        LPPL-1.0
Summary:        Draw Bao diagrams
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-psbao-doc >= %{texlive_version}
Provides:       tex(psbao.sty)
Requires:       tex(calc.sty)
Requires:       tex(cool.sty)
Requires:       tex(etex.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(pstricks.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source151:      psbao.tar.xz
Source152:      psbao.doc.tar.xz

%description -n texlive-psbao
The package draws Bao diagrams in LaTeX. The package is a
development of psgo, and uses PSTricks to draw the diagrams.

%package -n texlive-psbao-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn55013
Release:        0
Summary:        Documentation for texlive-psbao
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/

%description -n texlive-psbao-doc
This package includes the documentation for texlive-psbao

%post -n texlive-psbao
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-psbao
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-psbao
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-psbao-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/psbao/Changes
%{_texmfdistdir}/doc/latex/psbao/README
%{_texmfdistdir}/doc/latex/psbao/psbaomanual.pdf

%files -n texlive-psbao
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/psbao/psbao.sty

%package -n texlive-pseudo
Version:        %{texlive_version}.%{texlive_noarch}.1.1.3svn52582
Release:        0
License:        LPPL-1.0
Summary:        Straightforward pseudocode
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-pseudo-doc >= %{texlive_version}
Provides:       tex(pseudo.sty)
Requires:       tex(aliascnt.sty)
Requires:       tex(array.sty)
Requires:       tex(colortbl.sty)
Requires:       tex(expl3.sty)
Requires:       tex(l3keys2e.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xparse.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source153:      pseudo.tar.xz
Source154:      pseudo.doc.tar.xz

%description -n texlive-pseudo
The package permits writing pseudocode without much fuss and
with quite a bit of configurability. Its main environment
combines aspects of enumeration, tabbing and tabular for
nonintrusive line numbering, indentation and highlighting, and
there is functionality for typesetting common syntactic
elements such as keywords, identifiers, and comments. The
package relies on aliascnt, array, colortbl, expl3, l3keys2e,
xcolor, and xparse.

%package -n texlive-pseudo-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1.3svn52582
Release:        0
Summary:        Documentation for texlive-pseudo
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/

%description -n texlive-pseudo-doc
This package includes the documentation for texlive-pseudo

%post -n texlive-pseudo
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pseudo
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pseudo
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pseudo-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/pseudo/LICENSE
%{_texmfdistdir}/doc/latex/pseudo/Makefile
%{_texmfdistdir}/doc/latex/pseudo/README.md
%{_texmfdistdir}/doc/latex/pseudo/VERSION
%{_texmfdistdir}/doc/latex/pseudo/doc/fig/hilitefig.tex
%{_texmfdistdir}/doc/latex/pseudo/doc/fig/kwfig.tex
%{_texmfdistdir}/doc/latex/pseudo/doc/fig/pausefig.tex
%{_texmfdistdir}/doc/latex/pseudo/doc/fig/readmecode.tex
%{_texmfdistdir}/doc/latex/pseudo/doc/fig/readmefig.svg
%{_texmfdistdir}/doc/latex/pseudo/doc/fig/readmefig.tex
%{_texmfdistdir}/doc/latex/pseudo/doc/pseudo.bib
%{_texmfdistdir}/doc/latex/pseudo/doc/pseudo.pdf
%{_texmfdistdir}/doc/latex/pseudo/doc/pseudo.tex
%{_texmfdistdir}/doc/latex/pseudo/test/pseudotest.tex

%files -n texlive-pseudo
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/pseudo/pseudo.sty

%package -n texlive-pseudocode
Version:        %{texlive_version}.%{texlive_noarch}.svn54080
Release:        0
License:        LPPL-1.0
Summary:        LaTeX environment for specifying algorithms in a natural way
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-pseudocode-doc >= %{texlive_version}
Provides:       tex(pseudocode.sty)
Requires:       tex(fancybox.sty)
Requires:       tex(ifthen.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source155:      pseudocode.tar.xz
Source156:      pseudocode.doc.tar.xz

%description -n texlive-pseudocode
This package provides the environment "pseudocode" for
describing algorithms in a natural manner.

%package -n texlive-pseudocode-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn54080
Release:        0
Summary:        Documentation for texlive-pseudocode
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/

%description -n texlive-pseudocode-doc
This package includes the documentation for texlive-pseudocode

%post -n texlive-pseudocode
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pseudocode
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pseudocode
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pseudocode-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/pseudocode/README
%{_texmfdistdir}/doc/latex/pseudocode/pseudocode.pdf
%{_texmfdistdir}/doc/latex/pseudocode/pseudocode.tex

%files -n texlive-pseudocode
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/pseudocode/pseudocode.sty

%package -n texlive-psfrag
Version:        %{texlive_version}.%{texlive_noarch}.3.04svn15878
Release:        0
License:        LPPL-1.0
Summary:        Replace strings in encapsulated PostScript figures
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-psfrag-doc >= %{texlive_version}
Provides:       tex(psfrag.sty)
Requires:       tex(graphics.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source157:      psfrag.tar.xz
Source158:      psfrag.doc.tar.xz

%description -n texlive-psfrag
Allows LaTeX constructions (equations, picture environments,
etc.) to be precisely superimposed over Encapsulated PostScript
figures, using your own favorite drawing tool to create an EPS
figure and placing simple text 'tags' where each replacement is
to be placed, with PSfrag automatically removing these tags
from the figure and replacing them with a user specified LaTeX
construction, properly aligned, scaled, and/or rotated.

%package -n texlive-psfrag-doc
Version:        %{texlive_version}.%{texlive_noarch}.3.04svn15878
Release:        0
Summary:        Documentation for texlive-psfrag
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Provides:       locale(texlive-psfrag-doc:en)

%description -n texlive-psfrag-doc
This package includes the documentation for texlive-psfrag

%post -n texlive-psfrag
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-psfrag
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-psfrag
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-psfrag-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/psfrag/00readme.txt
%{_texmfdistdir}/doc/latex/psfrag/announce.txt
%{_texmfdistdir}/doc/latex/psfrag/example.eps
%{_texmfdistdir}/doc/latex/psfrag/pfgguide.pdf
%{_texmfdistdir}/doc/latex/psfrag/pfgguide.tex
%{_texmfdistdir}/doc/latex/psfrag/testfig.eps

%files -n texlive-psfrag
%defattr(-,root,root,755)
%{_texmfdistdir}/dvips/psfrag/psfrag.pro
%{_texmfdistdir}/tex/latex/psfrag/psfrag.sty

%package -n texlive-psfrag-italian
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
License:        GPL-2.0-or-later
Summary:        PSfrag documentation in Italian
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source159:      psfrag-italian.doc.tar.xz

%description -n texlive-psfrag-italian
This is a translation of the documentation that comes with the
psfrag documentation.

%post -n texlive-psfrag-italian
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-psfrag-italian
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-psfrag-italian
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-psfrag-italian
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/psfrag-italian/itpfgguide.pdf
%{_texmfdistdir}/doc/latex/psfrag-italian/itpfgguide.tex

%package -n texlive-psfragx
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn26243
Release:        0
License:        LPPL-1.0
Summary:        A psfrag eXtension
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-psfragx-doc >= %{texlive_version}
Provides:       tex(psfragx.cfg)
Provides:       tex(psfragx.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(overpic.sty)
Requires:       tex(psfrag.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source160:      psfragx.tar.xz
Source161:      psfragx.doc.tar.xz

%description -n texlive-psfragx
PSfragX offers a mechanism to embed \psfrag commands, as
provided by the psfrag package, into the EPS file itself. Each
time a graphic is included, the EPS file is scanned. If some
tagged lines are found, they are used to define the psfrag
replacements that should be performed automatically. In
addition, a similar mechanism holds for overpic objects. These
are picture objects superimposed on the included graphic. A
similar mechanism is implemented in psfrag itself (but
deprecated in the documentation), but psfragx offers much more
flexibility. For example, if babel is used, it is possible to
define different replacements corresponding to different
languages. The replacements to take into account will be
selected on the basis of the current language of the document.
A Matlab script (LaPrint) is provided, to export an EPS file
with psfragx annotations ready embedded.

%package -n texlive-psfragx-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn26243
Release:        0
Summary:        Documentation for texlive-psfragx
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/

%description -n texlive-psfragx-doc
This package includes the documentation for texlive-psfragx

%post -n texlive-psfragx
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-psfragx
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-psfragx
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-psfragx-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/psfragx/README
%{_texmfdistdir}/doc/latex/psfragx/README.laprint-3.16
%{_texmfdistdir}/doc/latex/psfragx/laprint.m
%{_texmfdistdir}/doc/latex/psfragx/laprintdoc.ps
%{_texmfdistdir}/doc/latex/psfragx/laprpfx.mat
%{_texmfdistdir}/doc/latex/psfragx/pfxprint.m
%{_texmfdistdir}/doc/latex/psfragx/psfragx.m
%{_texmfdistdir}/doc/latex/psfragx/psfragx.pdf
%{_texmfdistdir}/doc/latex/psfragx/psfragx_example.pdf
%{_texmfdistdir}/doc/latex/psfragx/psfragx_example.tex
%{_texmfdistdir}/doc/latex/psfragx/readmePFX.txt

%files -n texlive-psfragx
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/psfragx/psfragx.cfg
%{_texmfdistdir}/tex/latex/psfragx/psfragx.sty

%package -n texlive-psgo
Version:        %{texlive_version}.%{texlive_noarch}.0.0.17svn15878
Release:        0
License:        LPPL-1.0
Summary:        Typeset go diagrams with PSTricks
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-psgo-doc >= %{texlive_version}
Provides:       tex(psgo.sty)
Requires:       tex(calc.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(pst-node.sty)
Requires:       tex(pstricks.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source162:      psgo.tar.xz
Source163:      psgo.doc.tar.xz

%description -n texlive-psgo
The psgo package

%package -n texlive-psgo-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.17svn15878
Release:        0
Summary:        Documentation for texlive-psgo
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/

%description -n texlive-psgo-doc
This package includes the documentation for texlive-psgo

%post -n texlive-psgo
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-psgo
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-psgo
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-psgo-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/psgo/Changes
%{_texmfdistdir}/doc/latex/psgo/README
%{_texmfdistdir}/doc/latex/psgo/psgomanual.pdf
%{_texmfdistdir}/doc/latex/psgo/psgomanual.tex

%files -n texlive-psgo
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/psgo/psgo.sty

%package -n texlive-psizzl
Version:        %{texlive_version}.%{texlive_noarch}.0.0.35svn15878
Release:        0
License:        LPPL-1.0
Summary:        A TeX format for physics papers
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-psizzl-doc >= %{texlive_version}
Provides:       tex(mypsizzl.tex)
Provides:       tex(psizzl.tex)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source164:      psizzl.tar.xz
Source165:      psizzl.doc.tar.xz

%description -n texlive-psizzl
PSIZZL is a TeX format for physics papers written at SLAC and
used at several other places. It dates from rather early in the
development of TeX82; as a result, some of the descriptions of
limitations look rather quaint to modern eyes.

%package -n texlive-psizzl-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.35svn15878
Release:        0
Summary:        Documentation for texlive-psizzl
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/

%description -n texlive-psizzl-doc
This package includes the documentation for texlive-psizzl

%post -n texlive-psizzl
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-psizzl
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-psizzl
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-psizzl-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/otherformats/psizzl/base/psizzl.commands
%{_texmfdistdir}/doc/otherformats/psizzl/base/psizzl.doc

%files -n texlive-psizzl
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/psizzl/base/chapters.Psizzl
%{_texmfdistdir}/tex/psizzl/base/citation.Psizzl
%{_texmfdistdir}/tex/psizzl/base/fontdefs.Psizzl
%{_texmfdistdir}/tex/psizzl/base/index.Psizzl
%{_texmfdistdir}/tex/psizzl/base/institut.Psizzl
%{_texmfdistdir}/tex/psizzl/base/letter.Psizzl
%{_texmfdistdir}/tex/psizzl/base/lists.Psizzl
%{_texmfdistdir}/tex/psizzl/base/macros.Psizzl
%{_texmfdistdir}/tex/psizzl/base/memo.Psizzl
%{_texmfdistdir}/tex/psizzl/base/mypsizzl.tex
%{_texmfdistdir}/tex/psizzl/base/options.Psizzl
%{_texmfdistdir}/tex/psizzl/base/output.Psizzl
%{_texmfdistdir}/tex/psizzl/base/picture.Psizzl
%{_texmfdistdir}/tex/psizzl/base/psizzl.tex
%{_texmfdistdir}/tex/psizzl/base/publicat.Psizzl
%{_texmfdistdir}/tex/psizzl/base/symbols.Psizzl
%{_texmfdistdir}/tex/psizzl/base/thesis.Psizzl
%{_texmfdistdir}/tex/psizzl/config/psizzl.ini

%package -n texlive-pslatex
Version:        %{texlive_version}.%{texlive_noarch}.1.3svn57434
Release:        0
License:        LPPL-1.0
Summary:        Use PostScript fonts by default
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Provides:       tex(pcrr7tn.tfm)
Provides:       tex(pcrr7tn.vf)
Provides:       tex(pcrr8rn.map)
Provides:       tex(pcrr8rn.tfm)
Provides:       tex(pcrr8tn.tfm)
Provides:       tex(pcrr8tn.vf)
Provides:       tex(pslatex.sty)
Requires:       tex(psyr.tfm)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source166:      pslatex.tar.xz

%description -n texlive-pslatex
A small package that makes LaTeX default to 'standard'
PostScript fonts. It is basically a merger of the times and the
(obsolete) mathptm packages from the psnfss suite. You must
have installed standard LaTeX and the psnfss PostScript fonts
to use this package. The main novel feature is that the pslatex
package tries to compensate for the visual differences between
the Adobe fonts by scaling Helvetica by 90%, and 'condensing'
Courier (i.e. scaling horizontally) by 85%. The package is
supplied with a (unix) shell file for a 'pslatex' command that
allows standard LaTeX documents to be processed, without
needing to edit the file. Note that current psnfss uses a
different technique for scaling Helvetica, and treats Courier
as a lost cause (there are better free fixed-width available
now, than there were when pslatex was designed). As a result,
pslatex is widely considered obsolete.

%post -n texlive-pslatex
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pslatex
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pslatex
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pslatex
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/map/dvips/pslatex/pcrr8rn.map
%{_texmfdistdir}/fonts/tfm/public/pslatex/pcrr7tn.tfm
%{_texmfdistdir}/fonts/tfm/public/pslatex/pcrr8rn.tfm
%{_texmfdistdir}/fonts/tfm/public/pslatex/pcrr8tn.tfm
%{_texmfdistdir}/fonts/vf/public/pslatex/pcrr7tn.vf
%{_texmfdistdir}/fonts/vf/public/pslatex/pcrr8tn.vf
%{_texmfdistdir}/tex/latex/pslatex/pslatex.sty

%package -n texlive-psnfss
Version:        %{texlive_version}.%{texlive_noarch}.9.3svn54694
Release:        0
License:        LPPL-1.0
Summary:        Font support for common PostScript fonts
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires:       texlive-graphics >= %{texlive_version}
#!BuildIgnore: texlive-graphics
Requires:       texlive-symbol >= %{texlive_version}
#!BuildIgnore: texlive-symbol
Requires:       texlive-zapfding >= %{texlive_version}
#!BuildIgnore: texlive-zapfding
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(updmap.cfg)
#!BuildIgnore:  tex(updmap.cfg)
Requires(postun):findutils
Requires(postun):grep
Requires(postun):sed
Requires(postun):texlive >= %{texlive_version}
Requires(postun):tex(updmap.cfg)
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-psnfss-doc >= %{texlive_version}
Provides:       tex(8rbch.fd)
Provides:       tex(8rpag.fd)
Provides:       tex(8rpbk.fd)
Provides:       tex(8rpcr.fd)
Provides:       tex(8rphv.fd)
Provides:       tex(8rpnc.fd)
Provides:       tex(8rppl.fd)
Provides:       tex(8rptm.fd)
Provides:       tex(8rput.fd)
Provides:       tex(8rpzc.fd)
Provides:       tex(avant.sty)
Provides:       tex(bookman.sty)
Provides:       tex(chancery.sty)
Provides:       tex(charter.map)
Provides:       tex(charter.sty)
Provides:       tex(courier.sty)
Provides:       tex(fpls.map)
Provides:       tex(helvet.sty)
Provides:       tex(mathpazo.sty)
Provides:       tex(mathpple.sty)
Provides:       tex(mathptm.sty)
Provides:       tex(mathptmx.sty)
Provides:       tex(newcent.sty)
Provides:       tex(omlbch.fd)
Provides:       tex(omlpag.fd)
Provides:       tex(omlpbk.fd)
Provides:       tex(omlpcr.fd)
Provides:       tex(omlphv.fd)
Provides:       tex(omlpnc.fd)
Provides:       tex(omlppl.fd)
Provides:       tex(omlptm.fd)
Provides:       tex(omlptmcm.fd)
Provides:       tex(omlput.fd)
Provides:       tex(omlpzc.fd)
Provides:       tex(omlzplm.fd)
Provides:       tex(omlzpple.fd)
Provides:       tex(omlztmcm.fd)
Provides:       tex(omsbch.fd)
Provides:       tex(omspag.fd)
Provides:       tex(omspbk.fd)
Provides:       tex(omspcr.fd)
Provides:       tex(omsphv.fd)
Provides:       tex(omspnc.fd)
Provides:       tex(omsppl.fd)
Provides:       tex(omsptm.fd)
Provides:       tex(omsput.fd)
Provides:       tex(omspzc.fd)
Provides:       tex(omspzccm.fd)
Provides:       tex(omszplm.fd)
Provides:       tex(omszpple.fd)
Provides:       tex(omsztmcm.fd)
Provides:       tex(omxpsycm.fd)
Provides:       tex(omxzplm.fd)
Provides:       tex(omxzpple.fd)
Provides:       tex(omxztmcm.fd)
Provides:       tex(ot1bch.fd)
Provides:       tex(ot1pag.fd)
Provides:       tex(ot1pbk.fd)
Provides:       tex(ot1pcr.fd)
Provides:       tex(ot1phv.fd)
Provides:       tex(ot1pnc.fd)
Provides:       tex(ot1ppl.fd)
Provides:       tex(ot1pplj.fd)
Provides:       tex(ot1pplx.fd)
Provides:       tex(ot1ptm.fd)
Provides:       tex(ot1ptmcm.fd)
Provides:       tex(ot1put.fd)
Provides:       tex(ot1pzc.fd)
Provides:       tex(ot1zplm.fd)
Provides:       tex(ot1zpple.fd)
Provides:       tex(ot1ztmcm.fd)
Provides:       tex(palatino.sty)
Provides:       tex(pazo.map)
Provides:       tex(pifont.sty)
Provides:       tex(psnfss.map)
Provides:       tex(t1bch.fd)
Provides:       tex(t1pag.fd)
Provides:       tex(t1pbk.fd)
Provides:       tex(t1pcr.fd)
Provides:       tex(t1phv.fd)
Provides:       tex(t1pnc.fd)
Provides:       tex(t1ppl.fd)
Provides:       tex(t1pplj.fd)
Provides:       tex(t1pplx.fd)
Provides:       tex(t1ptm.fd)
Provides:       tex(t1put.fd)
Provides:       tex(t1pzc.fd)
Provides:       tex(times.sty)
Provides:       tex(ts1bch.fd)
Provides:       tex(ts1pag.fd)
Provides:       tex(ts1pbk.fd)
Provides:       tex(ts1pcr.fd)
Provides:       tex(ts1phv.fd)
Provides:       tex(ts1pnc.fd)
Provides:       tex(ts1ppl.fd)
Provides:       tex(ts1pplj.fd)
Provides:       tex(ts1pplx.fd)
Provides:       tex(ts1ptm.fd)
Provides:       tex(ts1put.fd)
Provides:       tex(ts1pzc.fd)
Provides:       tex(ufplm.fd)
Provides:       tex(ufplmbb.fd)
Provides:       tex(upsy.fd)
Provides:       tex(upzd.fd)
Provides:       tex(utopia.map)
Provides:       tex(utopia.sty)
Requires:       tex(keyval.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source167:      psnfss.tar.xz
Source168:      psnfss.doc.tar.xz

%description -n texlive-psnfss
Font definition files, macros and font metrics for
freely-available Adobe Type 1 fonts. The font set consists of
the 'LaserWriter 35' set (originally 'freely available' because
embedded in PostScript printers), and a variety of other free
fonts, together with some additions. Note that while many of
the fonts are available in PostScript (and other) printers,
most publishers require fonts embedded in documents, which
requires that you have the fonts in your TeX system.
Fortunately, there are free versions of the fonts from URW
(available in the URW base5 bundle). The base set of text fonts
covered by PSNFSS are: AvantGarde, Bookman, Courier, Helvetica,
New Century Schoolbook, Palatino, Symbol, Times Roman and Zapf
Dingbats. In addition, the fonts Bitstream Charter and Adobe
Utopia are covered (those fonts were contributed to the Public
Domain by their commercial foundries). Separate packages are
provided to load each font for use as main text font. The
packages helvet (which allows Helvetica to be loaded with its
size scaled to something more nearly appropriate for its use as
a Sans-Serif font to match Times) and pifont (which provides
the means to select single glyphs from symbol fonts) are
tailored to special requirements of their fonts. Mathematics
are covered by the mathptmx package, which constructs passable
mathematics from a combination of Times Roman, Symbol and some
glyphs from Computer Modern, and by Pazo Math (optionally
extended with the fpl small-caps and old-style figures fonts)
which uses Palatino as base font, with the mathpazo fonts. The
bundle as a whole is part of the LaTeX 'required' set of
packages.

%package -n texlive-psnfss-doc
Version:        %{texlive_version}.%{texlive_noarch}.9.3svn54694
Release:        0
Summary:        Documentation for texlive-psnfss
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/

%description -n texlive-psnfss-doc
This package includes the documentation for texlive-psnfss

%post -n texlive-psnfss
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
echo 'addMap charter.map' >> /var/run/texlive/run-updmap
echo 'addMap fpls.map' >> /var/run/texlive/run-updmap
echo 'addMap pazo.map' >> /var/run/texlive/run-updmap
echo 'addMap utopia.map' >> /var/run/texlive/run-updmap

%postun -n texlive-psnfss
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    echo 'deleteMap charter.map' >> /var/run/texlive/run-updmap
    echo 'deleteMap fpls.map' >> /var/run/texlive/run-updmap
    echo 'deleteMap pazo.map' >> /var/run/texlive/run-updmap
    echo 'deleteMap utopia.map' >> /var/run/texlive/run-updmap
    exit 0
fi

%posttrans -n texlive-psnfss
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-psnfss-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/psnfss/README
%{_texmfdistdir}/doc/latex/psnfss/changes.txt
%{_texmfdistdir}/doc/latex/psnfss/manifest.txt
%{_texmfdistdir}/doc/latex/psnfss/psnfss2e.pdf
%{_texmfdistdir}/doc/latex/psnfss/psnfss2e.tex
%{_texmfdistdir}/doc/latex/psnfss/test/mathtest.tex
%{_texmfdistdir}/doc/latex/psnfss/test/pitest.tex
%{_texmfdistdir}/doc/latex/psnfss/test/test0.tex
%{_texmfdistdir}/doc/latex/psnfss/test/test1.tex
%{_texmfdistdir}/doc/latex/psnfss/test/test2.tex
%{_texmfdistdir}/doc/latex/psnfss/test/test3.tex

%files -n texlive-psnfss
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/map/dvips/psnfss/charter.map
%{_texmfdistdir}/fonts/map/dvips/psnfss/fpls.map
%{_texmfdistdir}/fonts/map/dvips/psnfss/pazo.map
%{_texmfdistdir}/fonts/map/dvips/psnfss/psnfss.map
%{_texmfdistdir}/fonts/map/dvips/psnfss/utopia.map
%{_texmfdistdir}/tex/latex/psnfss/8rbch.fd
%{_texmfdistdir}/tex/latex/psnfss/8rpag.fd
%{_texmfdistdir}/tex/latex/psnfss/8rpbk.fd
%{_texmfdistdir}/tex/latex/psnfss/8rpcr.fd
%{_texmfdistdir}/tex/latex/psnfss/8rphv.fd
%{_texmfdistdir}/tex/latex/psnfss/8rpnc.fd
%{_texmfdistdir}/tex/latex/psnfss/8rppl.fd
%{_texmfdistdir}/tex/latex/psnfss/8rptm.fd
%{_texmfdistdir}/tex/latex/psnfss/8rput.fd
%{_texmfdistdir}/tex/latex/psnfss/8rpzc.fd
%{_texmfdistdir}/tex/latex/psnfss/avant.sty
%{_texmfdistdir}/tex/latex/psnfss/bookman.sty
%{_texmfdistdir}/tex/latex/psnfss/chancery.sty
%{_texmfdistdir}/tex/latex/psnfss/charter.sty
%{_texmfdistdir}/tex/latex/psnfss/courier.sty
%{_texmfdistdir}/tex/latex/psnfss/helvet.sty
%{_texmfdistdir}/tex/latex/psnfss/mathpazo.sty
%{_texmfdistdir}/tex/latex/psnfss/mathpple.sty
%{_texmfdistdir}/tex/latex/psnfss/mathptm.sty
%{_texmfdistdir}/tex/latex/psnfss/mathptmx.sty
%{_texmfdistdir}/tex/latex/psnfss/newcent.sty
%{_texmfdistdir}/tex/latex/psnfss/omlbch.fd
%{_texmfdistdir}/tex/latex/psnfss/omlpag.fd
%{_texmfdistdir}/tex/latex/psnfss/omlpbk.fd
%{_texmfdistdir}/tex/latex/psnfss/omlpcr.fd
%{_texmfdistdir}/tex/latex/psnfss/omlphv.fd
%{_texmfdistdir}/tex/latex/psnfss/omlpnc.fd
%{_texmfdistdir}/tex/latex/psnfss/omlppl.fd
%{_texmfdistdir}/tex/latex/psnfss/omlptm.fd
%{_texmfdistdir}/tex/latex/psnfss/omlptmcm.fd
%{_texmfdistdir}/tex/latex/psnfss/omlput.fd
%{_texmfdistdir}/tex/latex/psnfss/omlpzc.fd
%{_texmfdistdir}/tex/latex/psnfss/omlzplm.fd
%{_texmfdistdir}/tex/latex/psnfss/omlzpple.fd
%{_texmfdistdir}/tex/latex/psnfss/omlztmcm.fd
%{_texmfdistdir}/tex/latex/psnfss/omsbch.fd
%{_texmfdistdir}/tex/latex/psnfss/omspag.fd
%{_texmfdistdir}/tex/latex/psnfss/omspbk.fd
%{_texmfdistdir}/tex/latex/psnfss/omspcr.fd
%{_texmfdistdir}/tex/latex/psnfss/omsphv.fd
%{_texmfdistdir}/tex/latex/psnfss/omspnc.fd
%{_texmfdistdir}/tex/latex/psnfss/omsppl.fd
%{_texmfdistdir}/tex/latex/psnfss/omsptm.fd
%{_texmfdistdir}/tex/latex/psnfss/omsput.fd
%{_texmfdistdir}/tex/latex/psnfss/omspzc.fd
%{_texmfdistdir}/tex/latex/psnfss/omspzccm.fd
%{_texmfdistdir}/tex/latex/psnfss/omszplm.fd
%{_texmfdistdir}/tex/latex/psnfss/omszpple.fd
%{_texmfdistdir}/tex/latex/psnfss/omsztmcm.fd
%{_texmfdistdir}/tex/latex/psnfss/omxpsycm.fd
%{_texmfdistdir}/tex/latex/psnfss/omxzplm.fd
%{_texmfdistdir}/tex/latex/psnfss/omxzpple.fd
%{_texmfdistdir}/tex/latex/psnfss/omxztmcm.fd
%{_texmfdistdir}/tex/latex/psnfss/ot1bch.fd
%{_texmfdistdir}/tex/latex/psnfss/ot1pag.fd
%{_texmfdistdir}/tex/latex/psnfss/ot1pbk.fd
%{_texmfdistdir}/tex/latex/psnfss/ot1pcr.fd
%{_texmfdistdir}/tex/latex/psnfss/ot1phv.fd
%{_texmfdistdir}/tex/latex/psnfss/ot1pnc.fd
%{_texmfdistdir}/tex/latex/psnfss/ot1ppl.fd
%{_texmfdistdir}/tex/latex/psnfss/ot1pplj.fd
%{_texmfdistdir}/tex/latex/psnfss/ot1pplx.fd
%{_texmfdistdir}/tex/latex/psnfss/ot1ptm.fd
%{_texmfdistdir}/tex/latex/psnfss/ot1ptmcm.fd
%{_texmfdistdir}/tex/latex/psnfss/ot1put.fd
%{_texmfdistdir}/tex/latex/psnfss/ot1pzc.fd
%{_texmfdistdir}/tex/latex/psnfss/ot1zplm.fd
%{_texmfdistdir}/tex/latex/psnfss/ot1zpple.fd
%{_texmfdistdir}/tex/latex/psnfss/ot1ztmcm.fd
%{_texmfdistdir}/tex/latex/psnfss/palatino.sty
%{_texmfdistdir}/tex/latex/psnfss/pifont.sty
%{_texmfdistdir}/tex/latex/psnfss/t1bch.fd
%{_texmfdistdir}/tex/latex/psnfss/t1pag.fd
%{_texmfdistdir}/tex/latex/psnfss/t1pbk.fd
%{_texmfdistdir}/tex/latex/psnfss/t1pcr.fd
%{_texmfdistdir}/tex/latex/psnfss/t1phv.fd
%{_texmfdistdir}/tex/latex/psnfss/t1pnc.fd
%{_texmfdistdir}/tex/latex/psnfss/t1ppl.fd
%{_texmfdistdir}/tex/latex/psnfss/t1pplj.fd
%{_texmfdistdir}/tex/latex/psnfss/t1pplx.fd
%{_texmfdistdir}/tex/latex/psnfss/t1ptm.fd
%{_texmfdistdir}/tex/latex/psnfss/t1put.fd
%{_texmfdistdir}/tex/latex/psnfss/t1pzc.fd
%{_texmfdistdir}/tex/latex/psnfss/times.sty
%{_texmfdistdir}/tex/latex/psnfss/ts1bch.fd
%{_texmfdistdir}/tex/latex/psnfss/ts1pag.fd
%{_texmfdistdir}/tex/latex/psnfss/ts1pbk.fd
%{_texmfdistdir}/tex/latex/psnfss/ts1pcr.fd
%{_texmfdistdir}/tex/latex/psnfss/ts1phv.fd
%{_texmfdistdir}/tex/latex/psnfss/ts1pnc.fd
%{_texmfdistdir}/tex/latex/psnfss/ts1ppl.fd
%{_texmfdistdir}/tex/latex/psnfss/ts1pplj.fd
%{_texmfdistdir}/tex/latex/psnfss/ts1pplx.fd
%{_texmfdistdir}/tex/latex/psnfss/ts1ptm.fd
%{_texmfdistdir}/tex/latex/psnfss/ts1put.fd
%{_texmfdistdir}/tex/latex/psnfss/ts1pzc.fd
%{_texmfdistdir}/tex/latex/psnfss/ufplm.fd
%{_texmfdistdir}/tex/latex/psnfss/ufplmbb.fd
%{_texmfdistdir}/tex/latex/psnfss/upsy.fd
%{_texmfdistdir}/tex/latex/psnfss/upzd.fd
%{_texmfdistdir}/tex/latex/psnfss/utopia.sty

%package -n texlive-pspicture
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
License:        LPPL-1.0
Summary:        PostScript picture support
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-pspicture-doc >= %{texlive_version}
Provides:       tex(pspicture.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source169:      pspicture.tar.xz
Source170:      pspicture.doc.tar.xz

%description -n texlive-pspicture
A replacement for LaTeX's picture macros, that uses PostScript
\special commands. The package is now largely superseded by
pict2e.

%package -n texlive-pspicture-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        Documentation for texlive-pspicture
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/

%description -n texlive-pspicture-doc
This package includes the documentation for texlive-pspicture

%post -n texlive-pspicture
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pspicture
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pspicture
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pspicture-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/pspicture/README
%{_texmfdistdir}/doc/latex/pspicture/pspicture.pdf

%files -n texlive-pspicture
%defattr(-,root,root,755)
%{_texmfdistdir}/dvips/pspicture/pspicture.ps
%{_texmfdistdir}/tex/latex/pspicture/pspicture.sty

%package -n texlive-pst-2dplot
Version:        %{texlive_version}.%{texlive_noarch}.1.5svn15878
Release:        0
License:        LPPL-1.0
Summary:        A PSTricks package for drawing 2D curves
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-pst-2dplot-doc >= %{texlive_version}
Provides:       tex(pst-2dplot.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source171:      pst-2dplot.tar.xz
Source172:      pst-2dplot.doc.tar.xz

%description -n texlive-pst-2dplot
Pst-2dplot is a pstricks package that offers an easy-to-use and
intuitive tool for plotting 2-d curves. It defines an
environment with commands similar to MATLAB for plotting.

%package -n texlive-pst-2dplot-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.5svn15878
Release:        0
Summary:        Documentation for texlive-pst-2dplot
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/

%description -n texlive-pst-2dplot-doc
This package includes the documentation for texlive-pst-2dplot

%post -n texlive-pst-2dplot
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pst-2dplot
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pst-2dplot
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pst-2dplot-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/pst-2dplot/README
%{_texmfdistdir}/doc/generic/pst-2dplot/data1.dat
%{_texmfdistdir}/doc/generic/pst-2dplot/data2.dat
%{_texmfdistdir}/doc/generic/pst-2dplot/data3.dat
%{_texmfdistdir}/doc/generic/pst-2dplot/pst-2dplot-doc.pdf
%{_texmfdistdir}/doc/generic/pst-2dplot/pst-2dplot-doc.tex

%files -n texlive-pst-2dplot
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/pst-2dplot/pst-2dplot.sty

%package -n texlive-pst-3d
Version:        %{texlive_version}.%{texlive_noarch}.1.10svn17257
Release:        0
License:        LPPL-1.0
Summary:        A PSTricks package for tilting and other pseudo-3D tricks
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-pst-3d-doc >= %{texlive_version}
Provides:       tex(pst-3d.sty)
Provides:       tex(pst-3d.tex)
Requires:       tex(pstricks.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source173:      pst-3d.tar.xz
Source174:      pst-3d.doc.tar.xz

%description -n texlive-pst-3d
The package provides basic macros that use PSTricks for
shadows, tilting and three dimensional representations of text
or graphical objects.

%package -n texlive-pst-3d-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.10svn17257
Release:        0
Summary:        Documentation for texlive-pst-3d
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/

%description -n texlive-pst-3d-doc
This package includes the documentation for texlive-pst-3d

%post -n texlive-pst-3d
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pst-3d
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pst-3d
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pst-3d-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/pst-3d/Changes
%{_texmfdistdir}/doc/generic/pst-3d/README
%{_texmfdistdir}/doc/generic/pst-3d/pst-3d-doc.bib
%{_texmfdistdir}/doc/generic/pst-3d/pst-3d-doc.pdf
%{_texmfdistdir}/doc/generic/pst-3d/pst-3d-doc.tex

%files -n texlive-pst-3d
%defattr(-,root,root,755)
%{_texmfdistdir}/dvips/pst-3d/pst-3d.pro
%{_texmfdistdir}/tex/generic/pst-3d/pst-3d.tex
%{_texmfdistdir}/tex/latex/pst-3d/pst-3d.sty

%package -n texlive-pst-3dplot
Version:        %{texlive_version}.%{texlive_noarch}.2.07asvn61615
Release:        0
License:        LPPL-1.0
Summary:        Draw 3D objects in parallel projection, using PSTricks
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-pst-3dplot-doc >= %{texlive_version}
Provides:       tex(pst-3dplot.sty)
Provides:       tex(pst-3dplot.tex)
Requires:       tex(multido.sty)
Requires:       tex(pst-3d.sty)
Requires:       tex(pst-node.sty)
Requires:       tex(pst-plot.sty)
Requires:       tex(pstricks.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source175:      pst-3dplot.tar.xz
Source176:      pst-3dplot.doc.tar.xz

%description -n texlive-pst-3dplot
A package using PSTricks to draw a large variety of graphs and
plots, including 3D maths functions. Data can be read from
external data files, making this package a generic tool for
graphing within TeX/LaTeX, without the need for external tools.

%package -n texlive-pst-3dplot-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.07asvn61615
Release:        0
Summary:        Documentation for texlive-pst-3dplot
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/

%description -n texlive-pst-3dplot-doc
This package includes the documentation for texlive-pst-3dplot

%post -n texlive-pst-3dplot
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pst-3dplot
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pst-3dplot
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pst-3dplot-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/pst-3dplot/Changes
%{_texmfdistdir}/doc/generic/pst-3dplot/README
%{_texmfdistdir}/doc/generic/pst-3dplot/pst-3dplot-doc.bib
%{_texmfdistdir}/doc/generic/pst-3dplot/pst-3dplot-doc.dat
%{_texmfdistdir}/doc/generic/pst-3dplot/pst-3dplot-doc.pdf
%{_texmfdistdir}/doc/generic/pst-3dplot/pst-3dplot-doc.tex

%files -n texlive-pst-3dplot
%defattr(-,root,root,755)
%{_texmfdistdir}/dvips/pst-3dplot/pst-3dplot.pro
%{_texmfdistdir}/tex/generic/pst-3dplot/pst-3dplot.tex
%{_texmfdistdir}/tex/latex/pst-3dplot/pst-3dplot.sty

%package -n texlive-pst-abspos
Version:        %{texlive_version}.%{texlive_noarch}.0.0.2svn15878
Release:        0
License:        LPPL-1.0
Summary:        Put objects at an absolute position
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-pst-abspos-doc >= %{texlive_version}
Provides:       tex(pst-abspos.sty)
Provides:       tex(pst-abspos.tex)
Requires:       tex(pstricks.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source177:      pst-abspos.tar.xz
Source178:      pst-abspos.doc.tar.xz

%description -n texlive-pst-abspos
The (PSTricks-related) package provides a command
\pstPutAbs(x,y) to put an object at an arbitrary absolute (or
even a relative) position on the page.

%package -n texlive-pst-abspos-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.2svn15878
Release:        0
Summary:        Documentation for texlive-pst-abspos
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/

%description -n texlive-pst-abspos-doc
This package includes the documentation for texlive-pst-abspos

%post -n texlive-pst-abspos
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pst-abspos
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pst-abspos
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pst-abspos-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/pst-abspos/Changes
%{_texmfdistdir}/doc/generic/pst-abspos/README
%{_texmfdistdir}/doc/generic/pst-abspos/pst-abspos-doc.bib
%{_texmfdistdir}/doc/generic/pst-abspos/pst-abspos-doc.pdf
%{_texmfdistdir}/doc/generic/pst-abspos/pst-abspos-doc.tex

%files -n texlive-pst-abspos
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/pst-abspos/pst-abspos.tex
%{_texmfdistdir}/tex/latex/pst-abspos/pst-abspos.sty

%package -n texlive-pst-am
Version:        %{texlive_version}.%{texlive_noarch}.1.02svn19591
Release:        0
License:        LPPL-1.0
Summary:        Simulation of modulation and demodulation
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-pst-am-doc >= %{texlive_version}
Provides:       tex(pst-am.sty)
Requires:       tex(multido.sty)
Requires:       tex(numprint.sty)
Requires:       tex(pst-node.sty)
Requires:       tex(pst-plot.sty)
Requires:       tex(pst-xkey.sty)
Requires:       tex(pstricks.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source179:      pst-am.tar.xz
Source180:      pst-am.doc.tar.xz

%description -n texlive-pst-am
The package allows the simulation of the modulated and
demodulated amplitude of radio waves. The user may plot curves
of modulated signals, wave carrier, signal modulation, signal
recovery and signal demodulation.

%package -n texlive-pst-am-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.02svn19591
Release:        0
Summary:        Documentation for texlive-pst-am
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/

%description -n texlive-pst-am-doc
This package includes the documentation for texlive-pst-am

%post -n texlive-pst-am
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pst-am
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pst-am
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pst-am-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/pst-am/Changes
%{_texmfdistdir}/doc/generic/pst-am/README
%{_texmfdistdir}/doc/generic/pst-am/index.phtml
%{_texmfdistdir}/doc/generic/pst-am/pst-am-doc.bib
%{_texmfdistdir}/doc/generic/pst-am/pst-am-doc.pdf
%{_texmfdistdir}/doc/generic/pst-am/pst-am-doc.tex

%files -n texlive-pst-am
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/pst-am/pst-am.sty

%package -n texlive-pst-antiprism
Version:        %{texlive_version}.%{texlive_noarch}.0.0.02svn46643
Release:        0
License:        LPPL-1.0
Summary:        A PSTricks related package which draws an antiprism
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-pst-antiprism-doc >= %{texlive_version}
Provides:       tex(pst-antiprism.sty)
Provides:       tex(pst-antiprism.tex)
Requires:       tex(pst-solides3d.sty)
Requires:       tex(pstricks.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source181:      pst-antiprism.tar.xz
Source182:      pst-antiprism.doc.tar.xz

%description -n texlive-pst-antiprism
pst-antiprism is a PSTricks related package which draws an
antiprism, which is a semiregular polyhedron constructed with
2-gons and triangles.

%package -n texlive-pst-antiprism-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.02svn46643
Release:        0
Summary:        Documentation for texlive-pst-antiprism
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/

%description -n texlive-pst-antiprism-doc
This package includes the documentation for texlive-pst-antiprism

%post -n texlive-pst-antiprism
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pst-antiprism
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pst-antiprism
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pst-antiprism-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/pst-antiprism/Changes
%{_texmfdistdir}/doc/generic/pst-antiprism/README.md
%{_texmfdistdir}/doc/generic/pst-antiprism/pst-antiprism-doc.bib
%{_texmfdistdir}/doc/generic/pst-antiprism/pst-antiprism-doc.pdf
%{_texmfdistdir}/doc/generic/pst-antiprism/pst-antiprism-doc.tex

%files -n texlive-pst-antiprism
%defattr(-,root,root,755)
%{_texmfdistdir}/dvips/pst-antiprism/pst-antiprism.pro
%{_texmfdistdir}/tex/generic/pst-antiprism/pst-antiprism.tex
%{_texmfdistdir}/tex/latex/pst-antiprism/pst-antiprism.sty

%package -n texlive-pst-arrow
Version:        %{texlive_version}.%{texlive_noarch}.0.0.05svn61069
Release:        0
License:        LPPL-1.0
Summary:        Special arrows for PSTricks
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-pst-arrow-doc >= %{texlive_version}
Provides:       tex(pst-arrow.sty)
Provides:       tex(pst-arrow.tex)
Requires:       tex(pstricks.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source183:      pst-arrow.tar.xz
Source184:      pst-arrow.doc.tar.xz

%description -n texlive-pst-arrow
This package has all the code from the package pstricks-add
which was related to arrows, like multiple arrows and so on.

%package -n texlive-pst-arrow-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.05svn61069
Release:        0
Summary:        Documentation for texlive-pst-arrow
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/

%description -n texlive-pst-arrow-doc
This package includes the documentation for texlive-pst-arrow

%post -n texlive-pst-arrow
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pst-arrow
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pst-arrow
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pst-arrow-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/pst-arrow/Changes
%{_texmfdistdir}/doc/generic/pst-arrow/README
%{_texmfdistdir}/doc/generic/pst-arrow/pst-arrow-doc.bib
%{_texmfdistdir}/doc/generic/pst-arrow/pst-arrow-doc.pdf
%{_texmfdistdir}/doc/generic/pst-arrow/pst-arrow-doc.tex

%files -n texlive-pst-arrow
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/pst-arrow/pst-arrow.tex
%{_texmfdistdir}/tex/latex/pst-arrow/pst-arrow.sty

%package -n texlive-pst-asr
Version:        %{texlive_version}.%{texlive_noarch}.1.3svn22138
Release:        0
License:        LPPL-1.0
Summary:        Typeset autosegmental representations for linguists
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-pst-asr-doc >= %{texlive_version}
Provides:       tex(pst-asr.sty)
Provides:       tex(pst-asr.tex)
Requires:       tex(pst-xkey.sty)
Requires:       tex(pstricks.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source185:      pst-asr.tar.xz
Source186:      pst-asr.doc.tar.xz

%description -n texlive-pst-asr
The package allows the user to typeset autosegmental
representations. It uses the PStricks, and xkeyval packages.

%package -n texlive-pst-asr-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.3svn22138
Release:        0
Summary:        Documentation for texlive-pst-asr
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/

%description -n texlive-pst-asr-doc
This package includes the documentation for texlive-pst-asr

%post -n texlive-pst-asr
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pst-asr
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pst-asr
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pst-asr-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/pst-asr/README
%{_texmfdistdir}/doc/generic/pst-asr/pst-asr-doc-source.zip
%{_texmfdistdir}/doc/generic/pst-asr/pst-asr-doc.pdf
%{_texmfdistdir}/doc/generic/pst-asr/pst-asr-examples.pdf
%{_texmfdistdir}/doc/generic/pst-asr/pst-asr-examples.tex

%files -n texlive-pst-asr
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/pst-asr/pst-asr.tex
%{_texmfdistdir}/tex/latex/pst-asr/pst-asr.sty

%package -n texlive-pst-bar
Version:        %{texlive_version}.%{texlive_noarch}.0.0.92svn18734
Release:        0
License:        LPPL-1.0
Summary:        Produces bar charts using PSTricks
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-pst-bar-doc >= %{texlive_version}
Provides:       tex(pst-bar.sty)
Provides:       tex(pst-bar.tex)
Requires:       tex(pstricks.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source187:      pst-bar.tar.xz
Source188:      pst-bar.doc.tar.xz

%description -n texlive-pst-bar
The package uses pstricks to draw bar charts from data stored
in a comma-delimited file. Several types of bar charts may be
drawn, and the drawing parameters are highly customizable. No
external packages are required except those that are part of
the standard PSTricks distribution.

%package -n texlive-pst-bar-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.92svn18734
Release:        0
Summary:        Documentation for texlive-pst-bar
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Provides:       locale(texlive-pst-bar-doc:en;de)

%description -n texlive-pst-bar-doc
This package includes the documentation for texlive-pst-bar

%post -n texlive-pst-bar
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pst-bar
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pst-bar
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pst-bar-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/pst-bar/README
%{_texmfdistdir}/doc/generic/pst-bar/pst-bar-doc.bib
%{_texmfdistdir}/doc/generic/pst-bar/pst-bar-doc.pdf
%{_texmfdistdir}/doc/generic/pst-bar/pst-bar-doc.tex
%{_texmfdistdir}/doc/generic/pst-bar/pst-bar-docDE.pdf
%{_texmfdistdir}/doc/generic/pst-bar/pst-bar-docDE.tex

%files -n texlive-pst-bar
%defattr(-,root,root,755)
%{_texmfdistdir}/dvips/pst-bar/pst-bar.pro
%{_texmfdistdir}/tex/generic/pst-bar/pst-bar.tex
%{_texmfdistdir}/tex/latex/pst-bar/pst-bar.sty

%package -n texlive-pst-barcode
Version:        %{texlive_version}.%{texlive_noarch}.0.0.18svn61719
Release:        0
License:        LPPL-1.0
Summary:        Print barcodes using PostScript
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-pst-barcode-doc >= %{texlive_version}
Provides:       tex(pst-barcode.sty)
Provides:       tex(pst-barcode.tex)
Requires:       tex(pstricks.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source189:      pst-barcode.tar.xz
Source190:      pst-barcode.doc.tar.xz

%description -n texlive-pst-barcode
The pst-barcode package allows printing of barcodes, in a huge
variety of formats, including quick-response (qr) codes (see
documentation for details). As a PSTricks package, the package
requires pstricks. The package uses PostScript for calculating
the bars. For PDF output use a multi-pass mechansism such as
pst-pdf.

%package -n texlive-pst-barcode-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.18svn61719
Release:        0
Summary:        Documentation for texlive-pst-barcode
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/

%description -n texlive-pst-barcode-doc
This package includes the documentation for texlive-pst-barcode

%post -n texlive-pst-barcode
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pst-barcode
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pst-barcode
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pst-barcode-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/pst-barcode/Changes
%{_texmfdistdir}/doc/generic/pst-barcode/README.md
%{_texmfdistdir}/doc/generic/pst-barcode/images/auspost-1.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/auspost-2.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/aztec-1.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/aztec-2.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/aztec-3.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/aztec-4.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/aztec-5.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/aztec-6.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/bc412-1.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/bc412-2.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/bc412-3.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/channelcode-1.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/channelcode-2.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/channelcode-3.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/channelcode-4.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/codabar-1.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/codablockf-1.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/codablockf-2.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/codablockf-3.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/code11-1.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/code128-1.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/code16k-1.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/code16k-2.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/code16k-3.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/code25-1.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/code25-2.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/code32-1.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/code39-1.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/code39-2.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/code39-3.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/code39ext-1.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/code39ext-2.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/code49-1.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/code49-2.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/code49-3.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/code93-1.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/code93-2.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/code93ext-1.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/code93ext-2.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/codeone-1.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/codeone-2.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/codeone-3.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/codeone-4.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/daft-1.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/databarexpanded-1.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/databarexpandedcomposite-1.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/databarexpandedstacked-1.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/databarexpandedstackedcomposite-1.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/databarlimited-1.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/databarlimitedcomposite-1.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/databaromni-1.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/databaromnicomposite-1.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/databarstacked-1.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/databarstackedcomposite-1.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/databarstackedomni-1.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/databarstackedomnicomposite-1.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/databartruncated-1.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/databartruncatedcomposite-1.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/datamatrix-1.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/datamatrix-2.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/datamatrix-3.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/ean128-1.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/ean128-2.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/ean128composite-1.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/ean128composite-2.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/ean13-1.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/ean13-2.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/ean13composite-1.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/ean14-1.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/ean2-1.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/ean5-1.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/ean8-1.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/ean8-2.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/ean8composite-1.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/fima-1.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/fimb-1.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/fimc-1.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/fimd-1.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/flattermarken-1.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/gs1composite-1.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/gs1composite-2.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/gs1composite-3.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/gs1datamatrix-1.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/gs1qrcode-1.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/gs1qrcode-2.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/hanxin-1.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/hibccodablockf-1.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/hibccode128-1.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/hibccode39-1.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/hibcdatamatrix-1.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/hibcmicropdf417-1.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/hibcpdf417-1.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/hibcqrcode-1.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/identcode-1.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/isbn-1.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/isbn-2.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/isbn-3.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/isbn-4.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/ismn-1.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/ismn-2.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/ismn-3.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/issn-1.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/issn-2.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/itf-1.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/itf-14-1.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/itf-2.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/japanpost-1.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/kix-1.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/leitcode-1.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/maxicode-1.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/maxicode-2.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/maxicode-3.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/maxicode-4.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/micropdf417-1.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/micropdf417-2.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/msi-1.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/msi-2.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/msi-3.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/onecode-1.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/optborder.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/optcolorcmyk.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/optcolorrgb.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/optguardpos.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/optguardsize.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/optheight.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/optincludecheck.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/optincludecheckintext.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/optincludetext.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/optinkspread.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/optparse.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/optparsefnc.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/optraw.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/opttextfont.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/optwidth.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/pdf417-1.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/pdf417-2.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/pdf417-3.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/pdf417-4.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/pdf417-5.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/pharmacode-1.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/pharmacode2-1.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/planet-1.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/plessey-1.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/plessey-2.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/plessey-3.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/posicode-1.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/posicode-2.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/posicode-3.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/posicode-4.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/posicode-5.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/posicode-6.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/postnet-1.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/pzn-1.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/pzn-2.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/qrcode-1.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/qrcode-2.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/qrcode-5.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/raw-1.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/resize1.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/resize2.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/resize3.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/rm4scc-1.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/sscc18-1.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/telepen-1.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/telepen-2.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/telepen-3.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/telepen-4.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/telepen-5.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/upca-1.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/upca-2.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/upcacomposite-1.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/upce-1.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/upce-2.eps
%{_texmfdistdir}/doc/generic/pst-barcode/images/upcecomposite-1.eps
%{_texmfdistdir}/doc/generic/pst-barcode/pst-barcode-doc.bib
%{_texmfdistdir}/doc/generic/pst-barcode/pst-barcode-doc.ltx
%{_texmfdistdir}/doc/generic/pst-barcode/pst-barcode-doc.pdf
%{_texmfdistdir}/doc/generic/pst-barcode/pst-barcode-doc.tex

%files -n texlive-pst-barcode
%defattr(-,root,root,755)
%{_texmfdistdir}/dvips/pst-barcode/pst-barcode.pro
%{_texmfdistdir}/tex/generic/pst-barcode/pst-barcode.tex
%{_texmfdistdir}/tex/latex/pst-barcode/pst-barcode.sty

%package -n texlive-pst-bezier
Version:        %{texlive_version}.%{texlive_noarch}.0.0.03svn41981
Release:        0
License:        LPPL-1.0
Summary:        Draw Bezier curves
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-pst-bezier-doc >= %{texlive_version}
Provides:       tex(pst-bezier.sty)
Provides:       tex(pst-bezier.tex)
Requires:       tex(expl3.sty)
Requires:       tex(pstricks.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source191:      pst-bezier.tar.xz
Source192:      pst-bezier.doc.tar.xz

%description -n texlive-pst-bezier
The package provides a macro \psbcurve for drawing a Bezier
curve. Provision is made for full control of over all the
control points of the curve.

%package -n texlive-pst-bezier-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.03svn41981
Release:        0
Summary:        Documentation for texlive-pst-bezier
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/

%description -n texlive-pst-bezier-doc
This package includes the documentation for texlive-pst-bezier

%post -n texlive-pst-bezier
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pst-bezier
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pst-bezier
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pst-bezier-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/pst-bezier/Changes
%{_texmfdistdir}/doc/generic/pst-bezier/README.md
%{_texmfdistdir}/doc/generic/pst-bezier/pst-bezier-doc.bib
%{_texmfdistdir}/doc/generic/pst-bezier/pst-bezier-doc.pdf
%{_texmfdistdir}/doc/generic/pst-bezier/pst-bezier-doc.tex

%files -n texlive-pst-bezier
%defattr(-,root,root,755)
%{_texmfdistdir}/dvips/pst-bezier/pst-bezier.pro
%{_texmfdistdir}/tex/generic/pst-bezier/pst-bezier.tex
%{_texmfdistdir}/tex/latex/pst-bezier/pst-bezier.sty

%package -n texlive-pst-blur
Version:        %{texlive_version}.%{texlive_noarch}.2.0svn15878
Release:        0
License:        LPPL-1.0
Summary:        PSTricks package for "blurred" shadows
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-pst-blur-doc >= %{texlive_version}
Provides:       tex(pst-blur.sty)
Provides:       tex(pst-blur.tex)
Requires:       tex(pstricks.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source193:      pst-blur.tar.xz
Source194:      pst-blur.doc.tar.xz

%description -n texlive-pst-blur
Pst-blur is a package built for use with PSTricks. It provides
macros that apply blurring to the normal shadow function of
PSTricks.

%package -n texlive-pst-blur-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.0svn15878
Release:        0
Summary:        Documentation for texlive-pst-blur
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/

%description -n texlive-pst-blur-doc
This package includes the documentation for texlive-pst-blur

%post -n texlive-pst-blur
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pst-blur
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pst-blur
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pst-blur-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/pst-blur/Changes
%{_texmfdistdir}/doc/generic/pst-blur/README
%{_texmfdistdir}/doc/generic/pst-blur/pst-blur.pdf

%files -n texlive-pst-blur
%defattr(-,root,root,755)
%{_texmfdistdir}/dvips/pst-blur/pst-blur.pro
%{_texmfdistdir}/tex/generic/pst-blur/pst-blur.tex
%{_texmfdistdir}/tex/latex/pst-blur/pst-blur.sty

%package -n texlive-pst-bspline
Version:        %{texlive_version}.%{texlive_noarch}.1.62svn40685
Release:        0
License:        LPPL-1.0
Summary:        Draw cubic Bspline curves and interpolations
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-pst-bspline-doc >= %{texlive_version}
Provides:       tex(pst-bspline.sty)
Provides:       tex(pst-bspline.tex)
Requires:       tex(multido.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source195:      pst-bspline.tar.xz
Source196:      pst-bspline.doc.tar.xz

%description -n texlive-pst-bspline
The package draws uniform, cubic B-spline curves, open and
closed, based on a sequence of B-spline control points. There
is also code which permits drawing the open or closed cubic
Bspline curve interpolating a sequence of points. Graphical
output is created using PStricks.

%package -n texlive-pst-bspline-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.62svn40685
Release:        0
Summary:        Documentation for texlive-pst-bspline
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/

%description -n texlive-pst-bspline-doc
This package includes the documentation for texlive-pst-bspline

%post -n texlive-pst-bspline
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pst-bspline
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pst-bspline
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pst-bspline-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/pst-bspline/README
%{_texmfdistdir}/doc/generic/pst-bspline/pst-bspline-doc.pdf
%{_texmfdistdir}/doc/generic/pst-bspline/pst-bspline-doc.tex

%files -n texlive-pst-bspline
%defattr(-,root,root,755)
%{_texmfdistdir}/dvips/pst-bspline/pst-bspline.pro
%{_texmfdistdir}/tex/generic/pst-bspline/pst-bspline.tex
%{_texmfdistdir}/tex/latex/pst-bspline/pst-bspline.sty

%package -n texlive-pst-calculate
Version:        %{texlive_version}.%{texlive_noarch}.0.0.02svn49817
Release:        0
License:        LPPL-1.0
Summary:        Support for floating point operations at LaTeX level
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-pst-calculate-doc >= %{texlive_version}
Provides:       tex(pst-calculate.sty)
Requires:       tex(siunitx.sty)
Requires:       tex(xkeyval.sty)
Requires:       tex(xparse.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source197:      pst-calculate.tar.xz
Source198:      pst-calculate.doc.tar.xz

%description -n texlive-pst-calculate
This package provides an interface to the LaTeX3 floating point
unit (part of expl3), mainly used for PSTricks related packages
to allow math expressions at LaTeX level. siunitx is used for
formatting the calculated number. The package also depends on
xkeyval and xparse.

%package -n texlive-pst-calculate-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.02svn49817
Release:        0
Summary:        Documentation for texlive-pst-calculate
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/

%description -n texlive-pst-calculate-doc
This package includes the documentation for texlive-pst-calculate

%post -n texlive-pst-calculate
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pst-calculate
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pst-calculate
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pst-calculate-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/pst-calculate/Changes
%{_texmfdistdir}/doc/generic/pst-calculate/README.md
%{_texmfdistdir}/doc/generic/pst-calculate/pst-calculate-doc.bib
%{_texmfdistdir}/doc/generic/pst-calculate/pst-calculate-doc.pdf
%{_texmfdistdir}/doc/generic/pst-calculate/pst-calculate-doc.tex

%files -n texlive-pst-calculate
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/pst-calculate/pst-calculate.sty

%package -n texlive-pst-calendar
Version:        %{texlive_version}.%{texlive_noarch}.0.0.48svn60480
Release:        0
License:        LPPL-1.0
Summary:        Plot calendars in "fancy" ways
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-pst-calendar-doc >= %{texlive_version}
Provides:       tex(pst-calendar.sty)
Requires:       tex(fp.sty)
Requires:       tex(multido.sty)
Requires:       tex(pst-3d.sty)
Requires:       tex(pst-xkey.sty)
Requires:       tex(pstricks.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source199:      pst-calendar.tar.xz
Source200:      pst-calendar.doc.tar.xz

%description -n texlive-pst-calendar
The package uses pstricks and pst-3d to draw tabular calendars,
or calendars on dodecahedra with a month to each face (the
package also requires the multido and pst-xkey packages). The
package works for years 2000-2099, and has options for
calendars in French German and English, but the documentation
is not available in English.

%package -n texlive-pst-calendar-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.48svn60480
Release:        0
Summary:        Documentation for texlive-pst-calendar
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/

%description -n texlive-pst-calendar-doc
This package includes the documentation for texlive-pst-calendar

%post -n texlive-pst-calendar
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pst-calendar
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pst-calendar
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pst-calendar-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/pst-calendar/Changes
%{_texmfdistdir}/doc/latex/pst-calendar/README.md
%{_texmfdistdir}/doc/latex/pst-calendar/pst-calendar-doc.pdf
%{_texmfdistdir}/doc/latex/pst-calendar/pst-calendar-doc.tex

%files -n texlive-pst-calendar
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/pst-calendar/pst-calendar.sty

%package -n texlive-pst-cie
Version:        %{texlive_version}.%{texlive_noarch}.1.06bsvn60959
Release:        0
License:        LPPL-1.0
Summary:        CIE color space
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-pst-cie-doc >= %{texlive_version}
Provides:       tex(pst-cie.sty)
Provides:       tex(pst-cie.tex)
Requires:       tex(pstricks.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source201:      pst-cie.tar.xz
Source202:      pst-cie.doc.tar.xz

%description -n texlive-pst-cie
pst-cie is a PSTricks related package to show the different CIE
color spaces: Adobe, CIE, ColorMatch, NTSC, Pal-Secam,
ProPhoto, SMPTE, and sRGB.

%package -n texlive-pst-cie-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.06bsvn60959
Release:        0
Summary:        Documentation for texlive-pst-cie
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/

%description -n texlive-pst-cie-doc
This package includes the documentation for texlive-pst-cie

%post -n texlive-pst-cie
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pst-cie
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pst-cie
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pst-cie-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/pst-cie/Changes
%{_texmfdistdir}/doc/generic/pst-cie/README.md
%{_texmfdistdir}/doc/generic/pst-cie/pst-cie-doc.bib
%{_texmfdistdir}/doc/generic/pst-cie/pst-cie-doc.pdf
%{_texmfdistdir}/doc/generic/pst-cie/pst-cie-doc.tex

%files -n texlive-pst-cie
%defattr(-,root,root,755)
%{_texmfdistdir}/dvips/pst-cie/pst-cie.pro
%{_texmfdistdir}/tex/generic/pst-cie/pst-cie.tex
%{_texmfdistdir}/tex/latex/pst-cie/pst-cie.sty

%package -n texlive-pst-circ
Version:        %{texlive_version}.%{texlive_noarch}.2.19svn60464
Release:        0
License:        LPPL-1.0
Summary:        PSTricks package for drawing electric circuits
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-pst-circ-doc >= %{texlive_version}
Provides:       tex(pst-circ.sty)
Provides:       tex(pst-circ.tex)
Requires:       tex(pstricks.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source203:      pst-circ.tar.xz
Source204:      pst-circ.doc.tar.xz

%description -n texlive-pst-circ
The package is built using PSTricks and in particular pst-node.
It can easily draw current 2-terminal devices and some 3- and
4-terminal devices used in electronic or electric theory. The
package's macros are designed with a view to 'logical'
representation of circuits, as far as possible, so as to
relieve the user of purely graphical considerations when
expressing a circuit.

%package -n texlive-pst-circ-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.19svn60464
Release:        0
Summary:        Documentation for texlive-pst-circ
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/

%description -n texlive-pst-circ-doc
This package includes the documentation for texlive-pst-circ

%post -n texlive-pst-circ
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pst-circ
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pst-circ
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pst-circ-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/pst-circ/Changes
%{_texmfdistdir}/doc/generic/pst-circ/README
%{_texmfdistdir}/doc/generic/pst-circ/pst-circ-doc.bib
%{_texmfdistdir}/doc/generic/pst-circ/pst-circ-doc.pdf
%{_texmfdistdir}/doc/generic/pst-circ/pst-circ-doc.tex

%files -n texlive-pst-circ
%defattr(-,root,root,755)
%{_texmfdistdir}/dvips/pst-circ/pst-circ.pro
%{_texmfdistdir}/tex/generic/pst-circ/pst-circ.tex
%{_texmfdistdir}/tex/latex/pst-circ/pst-circ.sty

%package -n texlive-pst-coil
Version:        %{texlive_version}.%{texlive_noarch}.1.07svn37377
Release:        0
License:        LPPL-1.0
Summary:        A PSTricks package for coils, etcetera
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-pst-coil-doc >= %{texlive_version}
Provides:       tex(pst-coil.sty)
Provides:       tex(pst-coil.tex)
Requires:       tex(pstricks.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source205:      pst-coil.tar.xz
Source206:      pst-coil.doc.tar.xz

%description -n texlive-pst-coil
Pst-coil is a PSTricks based package for coils and zigzags and
for coil and zigzag node connections.

%package -n texlive-pst-coil-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.07svn37377
Release:        0
Summary:        Documentation for texlive-pst-coil
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/

%description -n texlive-pst-coil-doc
This package includes the documentation for texlive-pst-coil

%post -n texlive-pst-coil
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pst-coil
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pst-coil
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pst-coil-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/pst-coil/Changes
%{_texmfdistdir}/doc/generic/pst-coil/README
%{_texmfdistdir}/doc/generic/pst-coil/pst-coil-doc.bib
%{_texmfdistdir}/doc/generic/pst-coil/pst-coil-doc.pdf
%{_texmfdistdir}/doc/generic/pst-coil/pst-coil-doc.tex

%files -n texlive-pst-coil
%defattr(-,root,root,755)
%{_texmfdistdir}/dvips/pst-coil/pst-coil.pro
%{_texmfdistdir}/tex/generic/pst-coil/pst-coil.tex
%{_texmfdistdir}/tex/latex/pst-coil/pst-coil.sty

%package -n texlive-pst-contourplot
Version:        %{texlive_version}.%{texlive_noarch}.0.0.6svn48230
Release:        0
License:        LPPL-1.0
Summary:        Draw implicit functions using the "marching squares" algorithm
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-pst-contourplot-doc >= %{texlive_version}
Provides:       tex(pst-contourplot.sty)
Provides:       tex(pst-contourplot.tex)
Requires:       tex(pstricks.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source207:      pst-contourplot.tar.xz
Source208:      pst-contourplot.doc.tar.xz

%description -n texlive-pst-contourplot
This package allows to draw implicit functions "f(x,y) = 0"
with options for coloring the inside of the surfaces, for
marking the points and arrowing the curve at points chosen by
the user. The package uses the "marching squares" algorithm.

%package -n texlive-pst-contourplot-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.6svn48230
Release:        0
Summary:        Documentation for texlive-pst-contourplot
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Provides:       locale(texlive-pst-contourplot-doc:fr)

%description -n texlive-pst-contourplot-doc
This package includes the documentation for texlive-pst-contourplot

%post -n texlive-pst-contourplot
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pst-contourplot
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pst-contourplot
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pst-contourplot-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/pst-contourplot/README
%{_texmfdistdir}/doc/generic/pst-contourplot/examples/Les-Ovales-de-Descartes.pdf
%{_texmfdistdir}/doc/generic/pst-contourplot/examples/Les-Ovales-de-Descartes.tex
%{_texmfdistdir}/doc/generic/pst-contourplot/examples/README
%{_texmfdistdir}/doc/generic/pst-contourplot/examples/bourke.pdf
%{_texmfdistdir}/doc/generic/pst-contourplot/examples/bourke.tex
%{_texmfdistdir}/doc/generic/pst-contourplot/examples/courbe-du-diable.pdf
%{_texmfdistdir}/doc/generic/pst-contourplot/examples/courbe-du-diable.tex
%{_texmfdistdir}/doc/generic/pst-contourplot/examples/courbes-diverses.tex
%{_texmfdistdir}/doc/generic/pst-contourplot/examples/exemples-2.tex
%{_texmfdistdir}/doc/generic/pst-contourplot/examples/exemples-3.tex
%{_texmfdistdir}/doc/generic/pst-contourplot/examples/exemples-4.tex
%{_texmfdistdir}/doc/generic/pst-contourplot/examples/four-dipoles-lignes.tex
%{_texmfdistdir}/doc/generic/pst-contourplot/examples/four-dipoles-t.tex
%{_texmfdistdir}/doc/generic/pst-contourplot/examples/four-dipoles.tex
%{_texmfdistdir}/doc/generic/pst-contourplot/examples/four-leminscates.pdf
%{_texmfdistdir}/doc/generic/pst-contourplot/examples/four-leminscates.tex
%{_texmfdistdir}/doc/generic/pst-contourplot/examples/hertz.tex
%{_texmfdistdir}/doc/generic/pst-contourplot/examples/pavage.tex
%{_texmfdistdir}/doc/generic/pst-contourplot/examples/trefoil.tex
%{_texmfdistdir}/doc/generic/pst-contourplot/examples/two-metaballs.tex
%{_texmfdistdir}/doc/generic/pst-contourplot/pst-contourplot-docEN.pdf
%{_texmfdistdir}/doc/generic/pst-contourplot/pst-contourplot-docEN.tex
%{_texmfdistdir}/doc/generic/pst-contourplot/pst-contourplot-docFR.pdf
%{_texmfdistdir}/doc/generic/pst-contourplot/pst-contourplot-docFR.tex

%files -n texlive-pst-contourplot
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/pst-contourplot/pst-contourplot.tex
%{_texmfdistdir}/tex/latex/pst-contourplot/pst-contourplot.sty

%package -n texlive-pst-cox
Version:        %{texlive_version}.%{texlive_noarch}.0.0.98_betasvn15878
Release:        0
License:        LGPL-2.1-or-later
Summary:        Drawing regular complex polytopes with PSTricks
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-pst-cox-doc >= %{texlive_version}
Provides:       tex(pst-coxcoor.sty)
Provides:       tex(pst-coxcoor.tex)
Provides:       tex(pst-coxeterp.sty)
Provides:       tex(pst-coxeterp.tex)
Requires:       tex(pstricks.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source209:      pst-cox.tar.xz
Source210:      pst-cox.doc.tar.xz

%description -n texlive-pst-cox
Pst-cox is a PSTricks package for drawing 2-dimensional
projections of complex regular polytopes (after the work of
Coxeter). The package consists of a macro library for drawing
the projections. The complex polytopes appear in the study of
the root systems and play a crucial role in many domains
related to mathematics and physics. These polytopes have been
completely described by Coxeter in his book "Regular Complex
Polytopes". There exist only a finite numbers of exceptional
regular complex polytopes (for example the icosahedron) and
some infinite series (for example, one can construct a
multi-dimensional analogue of the hypercube in any finite
dimension). The library contains two packages. The first,
pst-coxcoor, is devoted to the exceptional complex regular
polytopes whose coordinates have been pre-computed. The second,
pst-coxeterp, is devoted to the infinite series.

%package -n texlive-pst-cox-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.98_betasvn15878
Release:        0
Summary:        Documentation for texlive-pst-cox
License:        LGPL-2.1-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Provides:       locale(texlive-pst-cox-doc:en)

%description -n texlive-pst-cox-doc
This package includes the documentation for texlive-pst-cox

%post -n texlive-pst-cox
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pst-cox
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pst-cox
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pst-cox-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/pst-cox/README
%{_texmfdistdir}/doc/generic/pst-cox/gpl.txt
%{_texmfdistdir}/doc/generic/pst-cox/lgpl.txt
%{_texmfdistdir}/doc/generic/pst-cox/pst-coxcoor/Gallery.tex
%{_texmfdistdir}/doc/generic/pst-cox/pst-coxcoor/pst-coxcoor_doc.pdf
%{_texmfdistdir}/doc/generic/pst-cox/pst-coxcoor/pst-coxcoor_doc.tex
%{_texmfdistdir}/doc/generic/pst-cox/pst-coxeterp/Gallery.tex
%{_texmfdistdir}/doc/generic/pst-cox/pst-coxeterp/pst-coxeterp_doc.pdf
%{_texmfdistdir}/doc/generic/pst-cox/pst-coxeterp/pst-coxeterp_doc.tex

%files -n texlive-pst-cox
%defattr(-,root,root,755)
%{_texmfdistdir}/dvips/pst-cox/pst-coxeter.pro
%{_texmfdistdir}/tex/generic/pst-cox/pst-coxcoor.tex
%{_texmfdistdir}/tex/generic/pst-cox/pst-coxeterp.tex
%{_texmfdistdir}/tex/latex/pst-cox/pst-coxcoor.sty
%{_texmfdistdir}/tex/latex/pst-cox/pst-coxeterp.sty

%package -n texlive-pst-dart
Version:        %{texlive_version}.%{texlive_noarch}.0.0.03svn60476
Release:        0
License:        LPPL-1.0
Summary:        Plotting dart boards
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-pst-dart-doc >= %{texlive_version}
Provides:       tex(pst-dart.sty)
Provides:       tex(pst-dart.tex)
Requires:       tex(multido.sty)
Requires:       tex(pst-xkey.sty)
Requires:       tex(pstricks.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source211:      pst-dart.tar.xz
Source212:      pst-dart.doc.tar.xz

%description -n texlive-pst-dart
pst-dart is a PSTricks related package and draws Dart Boards.
Optional arguments are the unit and the fontsize.

%package -n texlive-pst-dart-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.03svn60476
Release:        0
Summary:        Documentation for texlive-pst-dart
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/

%description -n texlive-pst-dart-doc
This package includes the documentation for texlive-pst-dart

%post -n texlive-pst-dart
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pst-dart
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pst-dart
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pst-dart-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/pst-dart/Changes
%{_texmfdistdir}/doc/generic/pst-dart/README.md
%{_texmfdistdir}/doc/generic/pst-dart/pst-dart-doc.bib
%{_texmfdistdir}/doc/generic/pst-dart/pst-dart-doc.pdf
%{_texmfdistdir}/doc/generic/pst-dart/pst-dart-doc.tex

%files -n texlive-pst-dart
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/pst-dart/pst-dart.tex
%{_texmfdistdir}/tex/latex/pst-dart/pst-dart.sty

%package -n texlive-pst-dbicons
Version:        %{texlive_version}.%{texlive_noarch}.0.0.16svn17556
Release:        0
License:        LPPL-1.0
Summary:        Support for drawing ER diagrams
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-pst-dbicons-doc >= %{texlive_version}
Provides:       tex(pst-dbicons.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source213:      pst-dbicons.tar.xz
Source214:      pst-dbicons.doc.tar.xz

%description -n texlive-pst-dbicons
The package provides some useful macros in the database area.
The package focusses on typesetting ER-Diagrams in a
declarative style, i.e., by positioning some nodes and defining
the position of all other nodes relative to them by using the
standard database terminology. The PSTricks package is required
for using pst-dbicons, but no deep knowledge of PSTricks
commands is required (although such knowledge is useful for
exploiting the full functionality of the package).

%package -n texlive-pst-dbicons-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.16svn17556
Release:        0
Summary:        Documentation for texlive-pst-dbicons
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/

%description -n texlive-pst-dbicons-doc
This package includes the documentation for texlive-pst-dbicons

%post -n texlive-pst-dbicons
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pst-dbicons
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pst-dbicons
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pst-dbicons-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/pst-dbicons/README
%{_texmfdistdir}/doc/generic/pst-dbicons/mondial-ER.tex
%{_texmfdistdir}/doc/generic/pst-dbicons/pst-dbicons.pdf

%files -n texlive-pst-dbicons
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/pst-dbicons/pst-dbicons.sty

%package -n texlive-pst-diffraction
Version:        %{texlive_version}.%{texlive_noarch}.2.03svn15878
Release:        0
License:        LPPL-1.0
Summary:        Print diffraction patterns from various apertures
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-pst-diffraction-doc >= %{texlive_version}
Provides:       tex(pst-diffraction.sty)
Provides:       tex(pst-diffraction.tex)
Requires:       tex(pst-3dplot.sty)
Requires:       tex(pst-xkey.sty)
Requires:       tex(pstricks.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source215:      pst-diffraction.tar.xz
Source216:      pst-diffraction.doc.tar.xz

%description -n texlive-pst-diffraction
The package enables the user to draw (using PSTricks) the
diffraction patterns for different geometric forms of apertures
for monochromatic light (using PSTricks). The aperture stops
can have rectangular, circular or triangular openings. The view
of the diffraction may be planar, or three-dimensional. Options
available are the dimensions of the aperture under
consideration and of the particular optical setting, e.g. the
radius in case of an circular opening. Moreover one can choose
the wavelength of the light (the associated color will be
calculated by the package).

%package -n texlive-pst-diffraction-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.03svn15878
Release:        0
Summary:        Documentation for texlive-pst-diffraction
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Provides:       locale(texlive-pst-diffraction-doc:de;en;fr)

%description -n texlive-pst-diffraction-doc
This package includes the documentation for texlive-pst-diffraction

%post -n texlive-pst-diffraction
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pst-diffraction
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pst-diffraction
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pst-diffraction-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/pst-diffraction/Changes
%{_texmfdistdir}/doc/generic/pst-diffraction/README
%{_texmfdistdir}/doc/generic/pst-diffraction/pst-diffraction-doc.bib
%{_texmfdistdir}/doc/generic/pst-diffraction/pst-diffraction-docDE.pdf
%{_texmfdistdir}/doc/generic/pst-diffraction/pst-diffraction-docDE.tex
%{_texmfdistdir}/doc/generic/pst-diffraction/pst-diffraction-docE.pdf
%{_texmfdistdir}/doc/generic/pst-diffraction/pst-diffraction-docE.tex
%{_texmfdistdir}/doc/generic/pst-diffraction/pst-diffraction-docFR.pdf
%{_texmfdistdir}/doc/generic/pst-diffraction/pst-diffraction-docFR.tex

%files -n texlive-pst-diffraction
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/pst-diffraction/pst-diffraction.tex
%{_texmfdistdir}/tex/latex/pst-diffraction/pst-diffraction.sty

%package -n texlive-pst-electricfield
Version:        %{texlive_version}.%{texlive_noarch}.0.0.14svn29803
Release:        0
License:        LPPL-1.0
Summary:        Draw electric field and equipotential lines with PSTricks
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-pst-electricfield-doc >= %{texlive_version}
Provides:       tex(pst-electricfield.sty)
Provides:       tex(pst-electricfield.tex)
Requires:       tex(pstricks.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source217:      pst-electricfield.tar.xz
Source218:      pst-electricfield.doc.tar.xz

%description -n texlive-pst-electricfield
The package provides macros to plot electric field and
equipotential lines using PStricks. There may be any number of
charges which can be placed in a cartesian coordinate system by
(x,y) values.

%package -n texlive-pst-electricfield-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.14svn29803
Release:        0
Summary:        Documentation for texlive-pst-electricfield
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Provides:       locale(texlive-pst-electricfield-doc:de;en;fr)

%description -n texlive-pst-electricfield-doc
This package includes the documentation for texlive-pst-electricfield

%post -n texlive-pst-electricfield
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pst-electricfield
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pst-electricfield
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pst-electricfield-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/pst-electricfield/Changes
%{_texmfdistdir}/doc/generic/pst-electricfield/README
%{_texmfdistdir}/doc/generic/pst-electricfield/pst-electricfield-doc.bib
%{_texmfdistdir}/doc/generic/pst-electricfield/pst-electricfield-docDE.pdf
%{_texmfdistdir}/doc/generic/pst-electricfield/pst-electricfield-docDE.tex
%{_texmfdistdir}/doc/generic/pst-electricfield/pst-electricfield-docEN.pdf
%{_texmfdistdir}/doc/generic/pst-electricfield/pst-electricfield-docEN.tex
%{_texmfdistdir}/doc/generic/pst-electricfield/pst-electricfield-docFR.pdf
%{_texmfdistdir}/doc/generic/pst-electricfield/pst-electricfield-docFR.tex

%files -n texlive-pst-electricfield
%defattr(-,root,root,755)
%{_texmfdistdir}/dvips/pst-electricfield/pst-electricfield.pro
%{_texmfdistdir}/tex/generic/pst-electricfield/pst-electricfield.tex
%{_texmfdistdir}/tex/latex/pst-electricfield/pst-electricfield.sty

%package -n texlive-pst-eps
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn15878
Release:        0
License:        LPPL-1.0
Summary:        Create EPS files from PSTricks figures
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-pst-eps-doc >= %{texlive_version}
Provides:       tex(pst-eps.sty)
Provides:       tex(pst-eps.tex)
Requires:       tex(pstricks.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source219:      pst-eps.tar.xz
Source220:      pst-eps.doc.tar.xz

%description -n texlive-pst-eps
Pst-eps is a PSTricks-based package for exporting PSTricks
images 'on the fly' to encapsulated PostScript (EPS) image
files, which can then be read into a document in the usual way.

%package -n texlive-pst-eps-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn15878
Release:        0
Summary:        Documentation for texlive-pst-eps
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/

%description -n texlive-pst-eps-doc
This package includes the documentation for texlive-pst-eps

%post -n texlive-pst-eps
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pst-eps
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pst-eps
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pst-eps-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/pst-eps/Changes
%{_texmfdistdir}/doc/generic/pst-eps/README
%{_texmfdistdir}/doc/generic/pst-eps/pst-eps-doc.bib
%{_texmfdistdir}/doc/generic/pst-eps/pst-eps-doc.pdf
%{_texmfdistdir}/doc/generic/pst-eps/pst-eps-doc.tex
%{_texmfdistdir}/doc/generic/pst-eps/spirale.eps

%files -n texlive-pst-eps
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/pst-eps/pst-eps.tex
%{_texmfdistdir}/tex/latex/pst-eps/pst-eps.sty

%package -n texlive-pst-eucl
Version:        %{texlive_version}.%{texlive_noarch}.1.75svn56474
Release:        0
License:        LPPL-1.0
Summary:        Euclidian geometry with PSTricks
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-pst-eucl-doc >= %{texlive_version}
Provides:       tex(pst-eucl.sty)
Provides:       tex(pst-eucl.tex)
Requires:       tex(pst-calculate.sty)
Requires:       tex(pst-node.sty)
Requires:       tex(pst-tools.sty)
Requires:       tex(pstricks.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source221:      pst-eucl.tar.xz
Source222:      pst-eucl.doc.tar.xz

%description -n texlive-pst-eucl
The package allows the drawing of Euclidean geometric figures
using TeX pstricks macros for specifying mathematical
constraints. It is thus possible to build point using common
transformations or intersections. The use of coordinates is
limited to points which controlled the figure.

%package -n texlive-pst-eucl-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.75svn56474
Release:        0
Summary:        Documentation for texlive-pst-eucl
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Provides:       locale(texlive-pst-eucl-doc:en)

%description -n texlive-pst-eucl-doc
This package includes the documentation for texlive-pst-eucl

%post -n texlive-pst-eucl
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pst-eucl
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pst-eucl
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pst-eucl-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/pst-eucl/Changes
%{_texmfdistdir}/doc/generic/pst-eucl/README
%{_texmfdistdir}/doc/generic/pst-eucl/pst-eucl-doc.bib
%{_texmfdistdir}/doc/generic/pst-eucl/pst-eucl-doc.pdf
%{_texmfdistdir}/doc/generic/pst-eucl/pst-eucl-doc.tex

%files -n texlive-pst-eucl
%defattr(-,root,root,755)
%{_texmfdistdir}/dvips/pst-eucl/pst-eucl.pro
%{_texmfdistdir}/tex/generic/pst-eucl/pst-eucl.tex
%{_texmfdistdir}/tex/latex/pst-eucl/pst-eucl.sty

%package -n texlive-pst-eucl-translation-bg
Version:        %{texlive_version}.%{texlive_noarch}.1.3.2svn19296
Release:        0
License:        LPPL-1.0
Summary:        Bulgarian translation of the pst-eucl documentation
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source223:      pst-eucl-translation-bg.doc.tar.xz

%description -n texlive-pst-eucl-translation-bg
The pst-eucl package documentation in Bulgarian language -
Euclidean Geometry with PSTricks.

%post -n texlive-pst-eucl-translation-bg
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pst-eucl-translation-bg
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pst-eucl-translation-bg
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pst-eucl-translation-bg
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/pst-eucl-translation-bg/Exemples/abscur.tex
%{_texmfdistdir}/doc/latex/pst-eucl-translation-bg/Exemples/abscur_in.tex
%{_texmfdistdir}/doc/latex/pst-eucl-translation-bg/Exemples/angle.tex
%{_texmfdistdir}/doc/latex/pst-eucl-translation-bg/Exemples/angle_in.tex
%{_texmfdistdir}/doc/latex/pst-eucl-translation-bg/Exemples/arc.tex
%{_texmfdistdir}/doc/latex/pst-eucl-translation-bg/Exemples/arc_in.log
%{_texmfdistdir}/doc/latex/pst-eucl-translation-bg/Exemples/arc_in.tex
%{_texmfdistdir}/doc/latex/pst-eucl-translation-bg/Exemples/astro.tex
%{_texmfdistdir}/doc/latex/pst-eucl-translation-bg/Exemples/astro_in.tex
%{_texmfdistdir}/doc/latex/pst-eucl-translation-bg/Exemples/bissec.tex
%{_texmfdistdir}/doc/latex/pst-eucl-translation-bg/Exemples/bissec_in.tex
%{_texmfdistdir}/doc/latex/pst-eucl-translation-bg/Exemples/ccirc.tex
%{_texmfdistdir}/doc/latex/pst-eucl-translation-bg/Exemples/ccirc_in.tex
%{_texmfdistdir}/doc/latex/pst-eucl-translation-bg/Exemples/cercle.tex
%{_texmfdistdir}/doc/latex/pst-eucl-translation-bg/Exemples/cercle_in.tex
%{_texmfdistdir}/doc/latex/pst-eucl-translation-bg/Exemples/cinscex.tex
%{_texmfdistdir}/doc/latex/pst-eucl-translation-bg/Exemples/cinscex_in.tex
%{_texmfdistdir}/doc/latex/pst-eucl-translation-bg/Exemples/curvetype.tex
%{_texmfdistdir}/doc/latex/pst-eucl-translation-bg/Exemples/curvetype_in.tex
%{_texmfdistdir}/doc/latex/pst-eucl-translation-bg/Exemples/cyclo.tex
%{_texmfdistdir}/doc/latex/pst-eucl-translation-bg/Exemples/cyclo_in.tex
%{_texmfdistdir}/doc/latex/pst-eucl-translation-bg/Exemples/delto.tex
%{_texmfdistdir}/doc/latex/pst-eucl-translation-bg/Exemples/droite.tex
%{_texmfdistdir}/doc/latex/pst-eucl-translation-bg/Exemples/droite_in.tex
%{_texmfdistdir}/doc/latex/pst-eucl-translation-bg/Exemples/envcardi.tex
%{_texmfdistdir}/doc/latex/pst-eucl-translation-bg/Exemples/envcardi_in.tex
%{_texmfdistdir}/doc/latex/pst-eucl-translation-bg/Exemples/envellipse.tex
%{_texmfdistdir}/doc/latex/pst-eucl-translation-bg/Exemples/envellipse_in.tex
%{_texmfdistdir}/doc/latex/pst-eucl-translation-bg/Exemples/euler.tex
%{_texmfdistdir}/doc/latex/pst-eucl-translation-bg/Exemples/euler_in.tex
%{_texmfdistdir}/doc/latex/pst-eucl-translation-bg/Exemples/fracthom.tex
%{_texmfdistdir}/doc/latex/pst-eucl-translation-bg/Exemples/fracthom_in.tex
%{_texmfdistdir}/doc/latex/pst-eucl-translation-bg/Exemples/gal_biss.tex
%{_texmfdistdir}/doc/latex/pst-eucl-translation-bg/Exemples/gal_biss_in.tex
%{_texmfdistdir}/doc/latex/pst-eucl-translation-bg/Exemples/gauss.tex
%{_texmfdistdir}/doc/latex/pst-eucl-translation-bg/Exemples/gauss_in.tex
%{_texmfdistdir}/doc/latex/pst-eucl-translation-bg/Exemples/gencur.tex
%{_texmfdistdir}/doc/latex/pst-eucl-translation-bg/Exemples/gencur_in.tex
%{_texmfdistdir}/doc/latex/pst-eucl-translation-bg/Exemples/geohyper.tex
%{_texmfdistdir}/doc/latex/pst-eucl-translation-bg/Exemples/geohyper_in.tex
%{_texmfdistdir}/doc/latex/pst-eucl-translation-bg/Exemples/geonode.tex
%{_texmfdistdir}/doc/latex/pst-eucl-translation-bg/Exemples/geonode_in.tex
%{_texmfdistdir}/doc/latex/pst-eucl-translation-bg/Exemples/german_ra.tex
%{_texmfdistdir}/doc/latex/pst-eucl-translation-bg/Exemples/german_ra_in.tex
%{_texmfdistdir}/doc/latex/pst-eucl-translation-bg/Exemples/grav.tex
%{_texmfdistdir}/doc/latex/pst-eucl-translation-bg/Exemples/grav_in.tex
%{_texmfdistdir}/doc/latex/pst-eucl-translation-bg/Exemples/homothetie.tex
%{_texmfdistdir}/doc/latex/pst-eucl-translation-bg/Exemples/homothetie_in.tex
%{_texmfdistdir}/doc/latex/pst-eucl-translation-bg/Exemples/hyperbole.tex
%{_texmfdistdir}/doc/latex/pst-eucl-translation-bg/Exemples/hyperbole_in.tex
%{_texmfdistdir}/doc/latex/pst-eucl-translation-bg/Exemples/hypocyclo.tex
%{_texmfdistdir}/doc/latex/pst-eucl-translation-bg/Exemples/interCC.tex
%{_texmfdistdir}/doc/latex/pst-eucl-translation-bg/Exemples/interCC_bis_in.tex
%{_texmfdistdir}/doc/latex/pst-eucl-translation-bg/Exemples/interCC_in.tex
%{_texmfdistdir}/doc/latex/pst-eucl-translation-bg/Exemples/interDC.tex
%{_texmfdistdir}/doc/latex/pst-eucl-translation-bg/Exemples/interDC_in.tex
%{_texmfdistdir}/doc/latex/pst-eucl-translation-bg/Exemples/interDD.tex
%{_texmfdistdir}/doc/latex/pst-eucl-translation-bg/Exemples/interDD_in.tex
%{_texmfdistdir}/doc/latex/pst-eucl-translation-bg/Exemples/interFC.tex
%{_texmfdistdir}/doc/latex/pst-eucl-translation-bg/Exemples/interFC_in.tex
%{_texmfdistdir}/doc/latex/pst-eucl-translation-bg/Exemples/interFF.tex
%{_texmfdistdir}/doc/latex/pst-eucl-translation-bg/Exemples/interFF_in.tex
%{_texmfdistdir}/doc/latex/pst-eucl-translation-bg/Exemples/interFL.tex
%{_texmfdistdir}/doc/latex/pst-eucl-translation-bg/Exemples/interFL_in.tex
%{_texmfdistdir}/doc/latex/pst-eucl-translation-bg/Exemples/mediator.tex
%{_texmfdistdir}/doc/latex/pst-eucl-translation-bg/Exemples/mediator_in.tex
%{_texmfdistdir}/doc/latex/pst-eucl-translation-bg/Exemples/milieu.tex
%{_texmfdistdir}/doc/latex/pst-eucl-translation-bg/Exemples/milieu_in.tex
%{_texmfdistdir}/doc/latex/pst-eucl-translation-bg/Exemples/oij.tex
%{_texmfdistdir}/doc/latex/pst-eucl-translation-bg/Exemples/oij_in.tex
%{_texmfdistdir}/doc/latex/pst-eucl-translation-bg/Exemples/orthocentre.tex
%{_texmfdistdir}/doc/latex/pst-eucl-translation-bg/Exemples/orthocentre_in.tex
%{_texmfdistdir}/doc/latex/pst-eucl-translation-bg/Exemples/orthoethyper.tex
%{_texmfdistdir}/doc/latex/pst-eucl-translation-bg/Exemples/orthoethyper_in.tex
%{_texmfdistdir}/doc/latex/pst-eucl-translation-bg/Exemples/parabole.tex
%{_texmfdistdir}/doc/latex/pst-eucl-translation-bg/Exemples/parabole_in.tex
%{_texmfdistdir}/doc/latex/pst-eucl-translation-bg/Exemples/projection.tex
%{_texmfdistdir}/doc/latex/pst-eucl-translation-bg/Exemples/projection_in.tex
%{_texmfdistdir}/doc/latex/pst-eucl-translation-bg/Exemples/ptfermat.tex
%{_texmfdistdir}/doc/latex/pst-eucl-translation-bg/Exemples/ptfermat_in.tex
%{_texmfdistdir}/doc/latex/pst-eucl-translation-bg/Exemples/remarq.tex
%{_texmfdistdir}/doc/latex/pst-eucl-translation-bg/Exemples/remarq_in.tex
%{_texmfdistdir}/doc/latex/pst-eucl-translation-bg/Exemples/rotation.tex
%{_texmfdistdir}/doc/latex/pst-eucl-translation-bg/Exemples/rotation_in.tex
%{_texmfdistdir}/doc/latex/pst-eucl-translation-bg/Exemples/segmentmark.tex
%{_texmfdistdir}/doc/latex/pst-eucl-translation-bg/Exemples/segmentmark_in.tex
%{_texmfdistdir}/doc/latex/pst-eucl-translation-bg/Exemples/symcentrale.tex
%{_texmfdistdir}/doc/latex/pst-eucl-translation-bg/Exemples/symcentrale_in.tex
%{_texmfdistdir}/doc/latex/pst-eucl-translation-bg/Exemples/symorthogonale.tex
%{_texmfdistdir}/doc/latex/pst-eucl-translation-bg/Exemples/symorthogonale_in.tex
%{_texmfdistdir}/doc/latex/pst-eucl-translation-bg/Exemples/tg1c.tex
%{_texmfdistdir}/doc/latex/pst-eucl-translation-bg/Exemples/tg1c_in.tex
%{_texmfdistdir}/doc/latex/pst-eucl-translation-bg/Exemples/tg2c.tex
%{_texmfdistdir}/doc/latex/pst-eucl-translation-bg/Exemples/tg2c_in.tex
%{_texmfdistdir}/doc/latex/pst-eucl-translation-bg/Exemples/translation.tex
%{_texmfdistdir}/doc/latex/pst-eucl-translation-bg/Exemples/translation_in.tex
%{_texmfdistdir}/doc/latex/pst-eucl-translation-bg/Exemples/triangle.tex
%{_texmfdistdir}/doc/latex/pst-eucl-translation-bg/Exemples/triangle_in.tex
%{_texmfdistdir}/doc/latex/pst-eucl-translation-bg/README
%{_texmfdistdir}/doc/latex/pst-eucl-translation-bg/README-bulgarian.txt
%{_texmfdistdir}/doc/latex/pst-eucl-translation-bg/euclide_bg.sty
%{_texmfdistdir}/doc/latex/pst-eucl-translation-bg/euclide_macros.ist
%{_texmfdistdir}/doc/latex/pst-eucl-translation-bg/pst-eucl-docBG.cb
%{_texmfdistdir}/doc/latex/pst-eucl-translation-bg/pst-eucl-docBG.pdf
%{_texmfdistdir}/doc/latex/pst-eucl-translation-bg/pst-eucl-docBG.tex

%package -n texlive-pst-exa
Version:        %{texlive_version}.%{texlive_noarch}.0.0.06svn45289
Release:        0
License:        LPPL-1.0
Summary:        Typeset PSTricks examples, with code
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-pst-exa-doc >= %{texlive_version}
Provides:       tex(pst-exa.sty)
Requires:       tex(accsupp.sty)
Requires:       tex(changepage.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(showexpl.sty)
Requires:       tex(tcolorbox.sty)
Requires:       tex(xcolor.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source224:      pst-exa.tar.xz
Source225:      pst-exa.doc.tar.xz

%description -n texlive-pst-exa
The (PSTricks-related) package provides an environment
PSTexample to put code and output side by side or one above the
other.

%package -n texlive-pst-exa-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.06svn45289
Release:        0
Summary:        Documentation for texlive-pst-exa
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/

%description -n texlive-pst-exa-doc
This package includes the documentation for texlive-pst-exa

%post -n texlive-pst-exa
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pst-exa
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pst-exa
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pst-exa-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/pst-exa/Changes
%{_texmfdistdir}/doc/latex/pst-exa/README
%{_texmfdistdir}/doc/latex/pst-exa/pst-exa-doc.bib
%{_texmfdistdir}/doc/latex/pst-exa/pst-exa-doc.inc
%{_texmfdistdir}/doc/latex/pst-exa/pst-exa-doc.pdf
%{_texmfdistdir}/doc/latex/pst-exa/pst-exa-doc.tex

%files -n texlive-pst-exa
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/pst-exa/pst-exa.sty

%package -n texlive-pst-feyn
Version:        %{texlive_version}.%{texlive_noarch}.0.0.01svn48781
Release:        0
License:        LPPL-1.0
Summary:        Draw graphical elements for Feynman diagrams
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-pst-feyn-doc >= %{texlive_version}
Provides:       tex(pst-feyn.sty)
Provides:       tex(pst-feyn.tex)
Requires:       tex(pstricks.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source226:      pst-feyn.tar.xz
Source227:      pst-feyn.doc.tar.xz

%description -n texlive-pst-feyn
pst-feyn is a set of drawing graphical elements which are used
for Feynman diagrams. The package is based on the macros of the
old package axodraw but uses the capabilities of PSTricks.

%package -n texlive-pst-feyn-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.01svn48781
Release:        0
Summary:        Documentation for texlive-pst-feyn
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/

%description -n texlive-pst-feyn-doc
This package includes the documentation for texlive-pst-feyn

%post -n texlive-pst-feyn
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pst-feyn
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pst-feyn
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pst-feyn-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/pst-feyn/Changes
%{_texmfdistdir}/doc/generic/pst-feyn/README.md
%{_texmfdistdir}/doc/generic/pst-feyn/data/data0.dat
%{_texmfdistdir}/doc/generic/pst-feyn/data/data1.dat
%{_texmfdistdir}/doc/generic/pst-feyn/pst-feyn-doc.bib
%{_texmfdistdir}/doc/generic/pst-feyn/pst-feyn-doc.pdf
%{_texmfdistdir}/doc/generic/pst-feyn/pst-feyn-doc.tex

%files -n texlive-pst-feyn
%defattr(-,root,root,755)
%{_texmfdistdir}/dvips/pst-feyn/pst-feyn.pro
%{_texmfdistdir}/tex/generic/pst-feyn/pst-feyn.tex
%{_texmfdistdir}/tex/latex/pst-feyn/pst-feyn.sty

%package -n texlive-pst-fill
Version:        %{texlive_version}.%{texlive_noarch}.1.02svn60671
Release:        0
License:        LPPL-1.0
Summary:        Fill or tile areas with PSTricks
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-pst-fill-doc >= %{texlive_version}
Provides:       tex(pst-fill.sty)
Provides:       tex(pst-fill.tex)
Requires:       tex(pstricks.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source228:      pst-fill.tar.xz
Source229:      pst-fill.doc.tar.xz

%description -n texlive-pst-fill
Pst-fill is a PSTricks-based package for filling and tiling
areas or characters.

%package -n texlive-pst-fill-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.02svn60671
Release:        0
Summary:        Documentation for texlive-pst-fill
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/

%description -n texlive-pst-fill-doc
This package includes the documentation for texlive-pst-fill

%post -n texlive-pst-fill
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pst-fill
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pst-fill
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pst-fill-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/pst-fill/Changes
%{_texmfdistdir}/doc/generic/pst-fill/README
%{_texmfdistdir}/doc/generic/pst-fill/pst-fill-doc.bib
%{_texmfdistdir}/doc/generic/pst-fill/pst-fill-doc.pdf
%{_texmfdistdir}/doc/generic/pst-fill/pst-fill-doc.tex

%files -n texlive-pst-fill
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/pst-fill/pst-fill.tex
%{_texmfdistdir}/tex/latex/pst-fill/pst-fill.sty

%package -n texlive-pst-fit
Version:        %{texlive_version}.%{texlive_noarch}.0.0.02svn45109
Release:        0
License:        LPPL-1.0
Summary:        Macros for curve fitting
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-pst-fit-doc >= %{texlive_version}
Provides:       tex(pst-fit.sty)
Provides:       tex(pst-fit.tex)
Requires:       tex(pstricks-add.sty)
Requires:       tex(pstricks.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source230:      pst-fit.tar.xz
Source231:      pst-fit.doc.tar.xz

%description -n texlive-pst-fit
The package uses PSTricks to fit curves to: Linear Functions;
Power Functions; exp Function; Log_{10} and Log_e functions;
Recip; Kings Law data; Gaussian; and 4th order Polynomial

%package -n texlive-pst-fit-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.02svn45109
Release:        0
Summary:        Documentation for texlive-pst-fit
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/

%description -n texlive-pst-fit-doc
This package includes the documentation for texlive-pst-fit

%post -n texlive-pst-fit
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pst-fit
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pst-fit
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pst-fit-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/pst-fit/Changes
%{_texmfdistdir}/doc/generic/pst-fit/README
%{_texmfdistdir}/doc/generic/pst-fit/pst-fit-doc.bib
%{_texmfdistdir}/doc/generic/pst-fit/pst-fit-doc.data
%{_texmfdistdir}/doc/generic/pst-fit/pst-fit-doc.pdf
%{_texmfdistdir}/doc/generic/pst-fit/pst-fit-doc.tex

%files -n texlive-pst-fit
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/pst-fit/pst-fit.tex
%{_texmfdistdir}/tex/latex/pst-fit/pst-fit.sty

%package -n texlive-pst-fr3d
Version:        %{texlive_version}.%{texlive_noarch}.1.10svn15878
Release:        0
License:        LPPL-1.0
Summary:        Draw 3-dimensional framed boxes using PSTricks
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-pst-fr3d-doc >= %{texlive_version}
Provides:       tex(pst-fr3d.sty)
Provides:       tex(pst-fr3d.tex)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source232:      pst-fr3d.tar.xz
Source233:      pst-fr3d.doc.tar.xz

%description -n texlive-pst-fr3d
A package using PSTricks to draw three dimensional framed boxes
using a macro \PstFrameBoxThreeD. The macro is especially
useful for drawing 3d-seeming buttons.

%package -n texlive-pst-fr3d-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.10svn15878
Release:        0
Summary:        Documentation for texlive-pst-fr3d
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/

%description -n texlive-pst-fr3d-doc
This package includes the documentation for texlive-pst-fr3d

%post -n texlive-pst-fr3d
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pst-fr3d
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pst-fr3d
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pst-fr3d-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/pst-fr3d/Changes
%{_texmfdistdir}/doc/generic/pst-fr3d/README
%{_texmfdistdir}/doc/generic/pst-fr3d/pst-fr3d.pdf

%files -n texlive-pst-fr3d
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/pst-fr3d/pst-fr3d.tex
%{_texmfdistdir}/tex/latex/pst-fr3d/pst-fr3d.sty

%package -n texlive-pst-fractal
Version:        %{texlive_version}.%{texlive_noarch}.0.0.11asvn54376
Release:        0
License:        LPPL-1.0
Summary:        Draw fractal sets using PSTricks
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-pst-fractal-doc >= %{texlive_version}
Provides:       tex(pst-fractal.sty)
Provides:       tex(pst-fractal.tex)
Requires:       tex(pstricks.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source234:      pst-fractal.tar.xz
Source235:      pst-fractal.doc.tar.xz

%description -n texlive-pst-fractal
The package uses PSTricks to draw the Julia and Mandelbrot
sets, the Sierpinski triangle, Koch flake, and Apollonius
Circle as well as fractal trees (which need not be balanced)
with a variety of different parameters (including varying
numbers of iterations). The package uses the pst-xkey package,
part of the xkeyval distribution.

%package -n texlive-pst-fractal-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.11asvn54376
Release:        0
Summary:        Documentation for texlive-pst-fractal
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/

%description -n texlive-pst-fractal-doc
This package includes the documentation for texlive-pst-fractal

%post -n texlive-pst-fractal
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pst-fractal
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pst-fractal
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pst-fractal-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/pst-fractal/Changes
%{_texmfdistdir}/doc/generic/pst-fractal/README
%{_texmfdistdir}/doc/generic/pst-fractal/pst-fractal-doc.bib
%{_texmfdistdir}/doc/generic/pst-fractal/pst-fractal-doc.pdf
%{_texmfdistdir}/doc/generic/pst-fractal/pst-fractal-doc.tex

%files -n texlive-pst-fractal
%defattr(-,root,root,755)
%{_texmfdistdir}/dvips/pst-fractal/pst-fractal.pro
%{_texmfdistdir}/tex/generic/pst-fractal/pst-fractal.tex
%{_texmfdistdir}/tex/latex/pst-fractal/pst-fractal.sty

%package -n texlive-pst-fun
Version:        %{texlive_version}.%{texlive_noarch}.0.0.04svn17909
Release:        0
License:        LPPL-1.0
Summary:        Draw "funny" objects with PSTricks
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-pst-fun-doc >= %{texlive_version}
Provides:       tex(pst-fun.sty)
Provides:       tex(pst-fun.tex)
Requires:       tex(multido.sty)
Requires:       tex(pst-grad.sty)
Requires:       tex(pst-slpe.sty)
Requires:       tex(pstricks.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source236:      pst-fun.tar.xz
Source237:      pst-fun.doc.tar.xz

%description -n texlive-pst-fun
This is a PSTricks related package for drawing funny objects,
like ant, bird, fish, kangaroo, ... Such objects may be useful
for testing other PSTricks macros and/or packages. (Or they can
be used for fun...)

%package -n texlive-pst-fun-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.04svn17909
Release:        0
Summary:        Documentation for texlive-pst-fun
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/

%description -n texlive-pst-fun-doc
This package includes the documentation for texlive-pst-fun

%post -n texlive-pst-fun
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pst-fun
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pst-fun
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pst-fun-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/pst-fun/Changes
%{_texmfdistdir}/doc/generic/pst-fun/README
%{_texmfdistdir}/doc/generic/pst-fun/pst-fun-doc.bib
%{_texmfdistdir}/doc/generic/pst-fun/pst-fun-doc.pdf
%{_texmfdistdir}/doc/generic/pst-fun/pst-fun-doc.tex

%files -n texlive-pst-fun
%defattr(-,root,root,755)
%{_texmfdistdir}/dvips/pst-fun/pst-fun.pro
%{_texmfdistdir}/tex/generic/pst-fun/pst-fun.tex
%{_texmfdistdir}/tex/latex/pst-fun/pst-fun.sty

%package -n texlive-pst-func
Version:        %{texlive_version}.%{texlive_noarch}.0.0.99svn60933
Release:        0
License:        LPPL-1.0
Summary:        PSTricks package for plotting mathematical functions
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-pst-func-doc >= %{texlive_version}
Provides:       tex(pst-func.sty)
Provides:       tex(pst-func.tex)
Requires:       tex(pst-math.sty)
Requires:       tex(pst-plot.sty)
Requires:       tex(pst-tools.sty)
Requires:       tex(pst-xkey.sty)
Requires:       tex(pstricks-add.sty)
Requires:       tex(pstricks.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source238:      pst-func.tar.xz
Source239:      pst-func.doc.tar.xz

%description -n texlive-pst-func
The package is built for use with PSTricks. It provides macros
for plotting and manipulating various mathematical functions:
polynomials and their derivatives
f(x)=an*x^n+an-1*x^(n-1)+...+a0 defined by the coefficients a0
a1 a2 ... and the derivative order; the Fourier sum f(x) =
a0/2+a1cos(omega x)+...+b1sin(omega x)+... defined by the
coefficients a0 a1 a2 ... b1 b2 b3 ...; the Bessel function
defined by its order; the Gauss function defined by sigma and
mu; Bezier curves from order 1 (two control points) to order 9
(10 control points); the superellipse function (the Lame
curve); Chebyshev polynomials of the first and second kind; the
Thomae (or popcorn) function; the Weierstrass function; various
integration-derived functions; normal, binomial, poisson,
gamma, chi-squared, student's t, F, beta, Cauchy and Weibull
distribution functions and the Lorenz curve; the zeroes of a
function, or the intermediate point of two functions; the
Vasicek function for describing the evolution of interest
rates; and implicit functions. The plots may be generated as
volumes of rotation about the X-axis, as well.

%package -n texlive-pst-func-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.99svn60933
Release:        0
Summary:        Documentation for texlive-pst-func
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/

%description -n texlive-pst-func-doc
This package includes the documentation for texlive-pst-func

%post -n texlive-pst-func
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pst-func
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pst-func
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pst-func-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/pst-func/Changes
%{_texmfdistdir}/doc/generic/pst-func/README.md
%{_texmfdistdir}/doc/generic/pst-func/pst-func-doc.bib
%{_texmfdistdir}/doc/generic/pst-func/pst-func-doc.data
%{_texmfdistdir}/doc/generic/pst-func/pst-func-doc.pdf
%{_texmfdistdir}/doc/generic/pst-func/pst-func-doc.tex

%files -n texlive-pst-func
%defattr(-,root,root,755)
%{_texmfdistdir}/dvips/pst-func/pst-func.pro
%{_texmfdistdir}/tex/generic/pst-func/pst-func.tex
%{_texmfdistdir}/tex/latex/pst-func/pst-func.sty

%package -n texlive-pst-gantt
Version:        %{texlive_version}.%{texlive_noarch}.0.0.22asvn35832
Release:        0
License:        LPPL-1.0
Summary:        Draw GANTT charts with PSTricks
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-pst-gantt-doc >= %{texlive_version}
Provides:       tex(pst-gantt.sty)
Provides:       tex(pst-gantt.tex)
Requires:       tex(pstricks.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source240:      pst-gantt.tar.xz
Source241:      pst-gantt.doc.tar.xz

%description -n texlive-pst-gantt
The package uses PSTricks to draw GANTT charts, which are a
kind of bar chart that displays a project schedule. The package
requires the pstricks apparatus, of course.

%package -n texlive-pst-gantt-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.22asvn35832
Release:        0
Summary:        Documentation for texlive-pst-gantt
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/

%description -n texlive-pst-gantt-doc
This package includes the documentation for texlive-pst-gantt

%post -n texlive-pst-gantt
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pst-gantt
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pst-gantt
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pst-gantt-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/pst-gantt/Changes
%{_texmfdistdir}/doc/generic/pst-gantt/README
%{_texmfdistdir}/doc/generic/pst-gantt/pst-gantt-doc.bib
%{_texmfdistdir}/doc/generic/pst-gantt/pst-gantt-doc.pdf
%{_texmfdistdir}/doc/generic/pst-gantt/pst-gantt-doc.tex

%files -n texlive-pst-gantt
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/pst-gantt/pst-gantt.tex
%{_texmfdistdir}/tex/latex/pst-gantt/pst-gantt.sty

%package -n texlive-pst-geo
Version:        %{texlive_version}.%{texlive_noarch}.0.0.07svn60387
Release:        0
License:        LPPL-1.0
Summary:        Geographical Projections
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-pst-geo-doc >= %{texlive_version}
Provides:       tex(Staedte3dJG.tex)
Provides:       tex(africa-bdy_II.dat)
Provides:       tex(africa-cil_II.dat)
Provides:       tex(africa-riv_II.dat)
Provides:       tex(asia-bdy_II.dat)
Provides:       tex(asia-cil_II.dat)
Provides:       tex(asia-isl_II.dat)
Provides:       tex(asia-riv_II.dat)
Provides:       tex(aus.dat)
Provides:       tex(c-cap.dat)
Provides:       tex(c-sub.dat)
Provides:       tex(canada.dat)
Provides:       tex(capitals.dat)
Provides:       tex(capitals.tex)
Provides:       tex(capitals3d.tex)
Provides:       tex(cities.tex)
Provides:       tex(citycapitals.dat)
Provides:       tex(citysub.dat)
Provides:       tex(corse.dat)
Provides:       tex(europe-bdy_II.dat)
Provides:       tex(europe-cil_II.dat)
Provides:       tex(europe-riv_II.dat)
Provides:       tex(france.dat)
Provides:       tex(germany.dat)
Provides:       tex(mexico.dat)
Provides:       tex(northamerica-bdy_II.dat)
Provides:       tex(northamerica-cil_II.dat)
Provides:       tex(northamerica-pby_II.dat)
Provides:       tex(northamerica-riv_II.dat)
Provides:       tex(pborder.dat)
Provides:       tex(pcoast.dat)
Provides:       tex(pisland.dat)
Provides:       tex(plake.dat)
Provides:       tex(pst-geo.sty)
Provides:       tex(pst-geo.tex)
Provides:       tex(rhone.dat)
Provides:       tex(ridge.dat)
Provides:       tex(river.dat)
Provides:       tex(seine.dat)
Provides:       tex(southamerica-arc_II.dat)
Provides:       tex(southamerica-bdy_II.dat)
Provides:       tex(southamerica-cil_II.dat)
Provides:       tex(southamerica-riv_II.dat)
Provides:       tex(transfrm.dat)
Provides:       tex(trench.dat)
Provides:       tex(usa.dat)
Provides:       tex(villesFrance.tex)
Provides:       tex(villesFrance3d.tex)
Provides:       tex(villesItalia.tex)
Provides:       tex(villesItalia3d.tex)
Provides:       tex(wfraczon.dat)
Provides:       tex(wmaglin.dat)
Requires:       tex(pstricks.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source242:      pst-geo.tar.xz
Source243:      pst-geo.doc.tar.xz

%description -n texlive-pst-geo
The package offers a set of PSTricks related packages for
various cartographic projections of the terrestrial sphere. The
package pst-map2d provides conventional projections such as
Mercator, Lambert, cylindrical, etc. The package pst-map3d
treats representation in three dimensions of the terrestrial
sphere. Packages pst-map2dII and pst-map3dII allow use of the
CIA World DataBank II. Various parameters of the packages allow
for choice of the level of the detail and the layouts possible
(cities, borders, rivers etc). Substantial data files are
provided, in an (internally) compressed format. Decompression
happens on-the-fly as a document using the data is displayed,
printed or converted to PDF format. A Perl script is provided
for the user to do the decompression, if the need should arise.

%package -n texlive-pst-geo-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.07svn60387
Release:        0
Summary:        Documentation for texlive-pst-geo
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/

%description -n texlive-pst-geo-doc
This package includes the documentation for texlive-pst-geo

%post -n texlive-pst-geo
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pst-geo
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pst-geo
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pst-geo-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/pst-geo/Changes
%{_texmfdistdir}/doc/generic/pst-geo/README
%{_texmfdistdir}/doc/generic/pst-geo/examples/Africa.tex
%{_texmfdistdir}/doc/generic/pst-geo/examples/Animate0.tex
%{_texmfdistdir}/doc/generic/pst-geo/examples/Animate1.tex
%{_texmfdistdir}/doc/generic/pst-geo/examples/Animate2.tex
%{_texmfdistdir}/doc/generic/pst-geo/examples/AntarticaII.tex
%{_texmfdistdir}/doc/generic/pst-geo/examples/AsiaII.tex
%{_texmfdistdir}/doc/generic/pst-geo/examples/Berlin.tex
%{_texmfdistdir}/doc/generic/pst-geo/examples/D-Karte-3dJG.tex
%{_texmfdistdir}/doc/generic/pst-geo/examples/D-karte-3d.tex
%{_texmfdistdir}/doc/generic/pst-geo/examples/DANTE.tex
%{_texmfdistdir}/doc/generic/pst-geo/examples/Europa.tex
%{_texmfdistdir}/doc/generic/pst-geo/examples/EuropeII.tex
%{_texmfdistdir}/doc/generic/pst-geo/examples/Greek.tex
%{_texmfdistdir}/doc/generic/pst-geo/pst-geo-compress.pl
%{_texmfdistdir}/doc/generic/pst-geo/pst-geo-decompress.pl
%{_texmfdistdir}/doc/generic/pst-geo/pst-geo-doc.bib
%{_texmfdistdir}/doc/generic/pst-geo/pst-geo-doc.pdf
%{_texmfdistdir}/doc/generic/pst-geo/pst-geo-doc.tex

%files -n texlive-pst-geo
%defattr(-,root,root,755)
%{_texmfdistdir}/dvips/pst-geo/pst-geo.pro
%{_texmfdistdir}/tex/generic/pst-geo/data/README.data
%{_texmfdistdir}/tex/generic/pst-geo/data/Staedte3dJG.tex
%{_texmfdistdir}/tex/generic/pst-geo/data/africa-bdy_II.dat
%{_texmfdistdir}/tex/generic/pst-geo/data/africa-cil_II.dat
%{_texmfdistdir}/tex/generic/pst-geo/data/africa-riv_II.dat
%{_texmfdistdir}/tex/generic/pst-geo/data/asia-bdy_II.dat
%{_texmfdistdir}/tex/generic/pst-geo/data/asia-cil_II.dat
%{_texmfdistdir}/tex/generic/pst-geo/data/asia-isl_II.dat
%{_texmfdistdir}/tex/generic/pst-geo/data/asia-riv_II.dat
%{_texmfdistdir}/tex/generic/pst-geo/data/aus.dat
%{_texmfdistdir}/tex/generic/pst-geo/data/c-cap.dat
%{_texmfdistdir}/tex/generic/pst-geo/data/c-sub.dat
%{_texmfdistdir}/tex/generic/pst-geo/data/canada.dat
%{_texmfdistdir}/tex/generic/pst-geo/data/capitals.dat
%{_texmfdistdir}/tex/generic/pst-geo/data/capitals.tex
%{_texmfdistdir}/tex/generic/pst-geo/data/capitals3d.tex
%{_texmfdistdir}/tex/generic/pst-geo/data/cities.data
%{_texmfdistdir}/tex/generic/pst-geo/data/cities.tex
%{_texmfdistdir}/tex/generic/pst-geo/data/citycapitals.dat
%{_texmfdistdir}/tex/generic/pst-geo/data/citysub.dat
%{_texmfdistdir}/tex/generic/pst-geo/data/convert.py
%{_texmfdistdir}/tex/generic/pst-geo/data/corse.dat
%{_texmfdistdir}/tex/generic/pst-geo/data/europe-bdy_II.dat
%{_texmfdistdir}/tex/generic/pst-geo/data/europe-cil_II.dat
%{_texmfdistdir}/tex/generic/pst-geo/data/europe-riv_II.dat
%{_texmfdistdir}/tex/generic/pst-geo/data/france.dat
%{_texmfdistdir}/tex/generic/pst-geo/data/germany.dat
%{_texmfdistdir}/tex/generic/pst-geo/data/mexico.dat
%{_texmfdistdir}/tex/generic/pst-geo/data/northamerica-bdy_II.dat
%{_texmfdistdir}/tex/generic/pst-geo/data/northamerica-cil_II.dat
%{_texmfdistdir}/tex/generic/pst-geo/data/northamerica-pby_II.dat
%{_texmfdistdir}/tex/generic/pst-geo/data/northamerica-riv_II.dat
%{_texmfdistdir}/tex/generic/pst-geo/data/pborder.dat
%{_texmfdistdir}/tex/generic/pst-geo/data/pcoast.dat
%{_texmfdistdir}/tex/generic/pst-geo/data/pisland.dat
%{_texmfdistdir}/tex/generic/pst-geo/data/plake.dat
%{_texmfdistdir}/tex/generic/pst-geo/data/rhone.dat
%{_texmfdistdir}/tex/generic/pst-geo/data/ridge.dat
%{_texmfdistdir}/tex/generic/pst-geo/data/river.dat
%{_texmfdistdir}/tex/generic/pst-geo/data/seine.dat
%{_texmfdistdir}/tex/generic/pst-geo/data/southamerica-arc_II.dat
%{_texmfdistdir}/tex/generic/pst-geo/data/southamerica-bdy_II.dat
%{_texmfdistdir}/tex/generic/pst-geo/data/southamerica-cil_II.dat
%{_texmfdistdir}/tex/generic/pst-geo/data/southamerica-riv_II.dat
%{_texmfdistdir}/tex/generic/pst-geo/data/transfrm.dat
%{_texmfdistdir}/tex/generic/pst-geo/data/trench.dat
%{_texmfdistdir}/tex/generic/pst-geo/data/usa.dat
%{_texmfdistdir}/tex/generic/pst-geo/data/villesFrance.tex
%{_texmfdistdir}/tex/generic/pst-geo/data/villesFrance3d.tex
%{_texmfdistdir}/tex/generic/pst-geo/data/villesItalia.tex
%{_texmfdistdir}/tex/generic/pst-geo/data/villesItalia3d.tex
%{_texmfdistdir}/tex/generic/pst-geo/data/wfraczon.dat
%{_texmfdistdir}/tex/generic/pst-geo/data/wmaglin.dat
%{_texmfdistdir}/tex/generic/pst-geo/pst-geo.tex
%{_texmfdistdir}/tex/latex/pst-geo/pst-geo.sty

%package -n texlive-pst-geometrictools
Version:        %{texlive_version}.%{texlive_noarch}.1.3svn61430
Release:        0
License:        LPPL-1.0
Summary:        A PSTricks package to draw geometric tools
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-pst-geometrictools-doc >= %{texlive_version}
Provides:       tex(pst-geometrictools.sty)
Provides:       tex(pst-geometrictools.tex)
Requires:       tex(pstricks.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source244:      pst-geometrictools.tar.xz
Source245:      pst-geometrictools.doc.tar.xz

%description -n texlive-pst-geometrictools
This PSTricks package facilitates the drawing of protractors,
rulers, compasses and pencils.

%package -n texlive-pst-geometrictools-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.3svn61430
Release:        0
Summary:        Documentation for texlive-pst-geometrictools
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Provides:       locale(texlive-pst-geometrictools-doc:fr)

%description -n texlive-pst-geometrictools-doc
This package includes the documentation for texlive-pst-geometrictools

%post -n texlive-pst-geometrictools
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pst-geometrictools
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pst-geometrictools
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pst-geometrictools-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/pst-geometrictools/Changes
%{_texmfdistdir}/doc/generic/pst-geometrictools/README.md
%{_texmfdistdir}/doc/generic/pst-geometrictools/pst-geometrictools-doc.pdf
%{_texmfdistdir}/doc/generic/pst-geometrictools/pst-geometrictools-doc.tex
%{_texmfdistdir}/doc/generic/pst-geometrictools/pst-geometrictools-fr-doc.pdf
%{_texmfdistdir}/doc/generic/pst-geometrictools/pst-geometrictools-fr-doc.tex

%files -n texlive-pst-geometrictools
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/pst-geometrictools/pst-geometrictools.tex
%{_texmfdistdir}/tex/latex/pst-geometrictools/pst-geometrictools.sty

%package -n texlive-pst-gr3d
Version:        %{texlive_version}.%{texlive_noarch}.1.34svn15878
Release:        0
License:        LPPL-1.0
Summary:        Three dimensional grids with PSTricks
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-pst-gr3d-doc >= %{texlive_version}
Provides:       tex(pst-gr3d.sty)
Provides:       tex(pst-gr3d.tex)
Requires:       tex(pstricks.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source246:      pst-gr3d.tar.xz
Source247:      pst-gr3d.doc.tar.xz

%description -n texlive-pst-gr3d
This PSTricks package provides a command \PstGridThreeD that
will draw a three dimensional grid, offering a number of
options for its appearance.

%package -n texlive-pst-gr3d-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.34svn15878
Release:        0
Summary:        Documentation for texlive-pst-gr3d
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/

%description -n texlive-pst-gr3d-doc
This package includes the documentation for texlive-pst-gr3d

%post -n texlive-pst-gr3d
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pst-gr3d
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pst-gr3d
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pst-gr3d-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/pst-gr3d/Changes
%{_texmfdistdir}/doc/generic/pst-gr3d/README
%{_texmfdistdir}/doc/generic/pst-gr3d/pst-gr3d.pdf

%files -n texlive-pst-gr3d
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/pst-gr3d/pst-gr3d.tex
%{_texmfdistdir}/tex/latex/pst-gr3d/pst-gr3d.sty

%package -n texlive-pst-grad
Version:        %{texlive_version}.%{texlive_noarch}.1.06svn15878
Release:        0
License:        LPPL-1.0
Summary:        Filling with colour gradients, using PSTricks
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-pst-grad-doc >= %{texlive_version}
Provides:       tex(pst-grad.sty)
Provides:       tex(pst-grad.tex)
Requires:       tex(pstricks.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source248:      pst-grad.tar.xz
Source249:      pst-grad.doc.tar.xz

%description -n texlive-pst-grad
The package fills with colour gradients, using PSTricks. The
RGB, CMYK and HSB models are supported. Other colour gradient
mechanisms are to be found in package pst-slpe.

%package -n texlive-pst-grad-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.06svn15878
Release:        0
Summary:        Documentation for texlive-pst-grad
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/

%description -n texlive-pst-grad-doc
This package includes the documentation for texlive-pst-grad

%post -n texlive-pst-grad
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pst-grad
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pst-grad
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pst-grad-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/pst-grad/Changes
%{_texmfdistdir}/doc/generic/pst-grad/pst-grad-doc.bib
%{_texmfdistdir}/doc/generic/pst-grad/pst-grad-doc.pdf
%{_texmfdistdir}/doc/generic/pst-grad/pst-grad-doc.tex

%files -n texlive-pst-grad
%defattr(-,root,root,755)
%{_texmfdistdir}/dvips/pst-grad/pst-grad.pro
%{_texmfdistdir}/tex/generic/pst-grad/pst-grad.tex
%{_texmfdistdir}/tex/latex/pst-grad/pst-grad.sty

%package -n texlive-pst-graphicx
Version:        %{texlive_version}.%{texlive_noarch}.0.0.02svn21717
Release:        0
License:        LPPL-1.0
Summary:        A PSTricks-compatible graphicx for use with Plain TeX
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-pst-graphicx-doc >= %{texlive_version}
Provides:       tex(pst-graphicx.tex)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source250:      pst-graphicx.tar.xz
Source251:      pst-graphicx.doc.tar.xz

%description -n texlive-pst-graphicx
The package provides a version of graphicx that avoids loading
the graphics bundle's (original) keyval package, which clashes
with pstricks' use of xkeyval.

%package -n texlive-pst-graphicx-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.02svn21717
Release:        0
Summary:        Documentation for texlive-pst-graphicx
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/

%description -n texlive-pst-graphicx-doc
This package includes the documentation for texlive-pst-graphicx

%post -n texlive-pst-graphicx
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pst-graphicx
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pst-graphicx
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pst-graphicx-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/pst-graphicx/Changes
%{_texmfdistdir}/doc/generic/pst-graphicx/README
%{_texmfdistdir}/doc/generic/pst-graphicx/demo.tex

%files -n texlive-pst-graphicx
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/pst-graphicx/pst-graphicx.tex

%package -n texlive-pst-hsb
Version:        %{texlive_version}.%{texlive_noarch}.0.0.02svn61322
Release:        0
License:        LPPL-1.0
Summary:        Curves with continuous colours
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Obsoletes:      texlive-pst-ghsb < 2022
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-pst-hsb-doc >= %{texlive_version}
Provides:       tex(pst-hsb.sty)
Provides:       tex(pst-hsb.tex)
Requires:       tex(pstricks.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source252:      pst-hsb.tar.xz
Source253:      pst-hsb.doc.tar.xz

%description -n texlive-pst-hsb
This is a PSTricks-related package. It can plot lines and/or
curves with continuous colours. Only colours defined in the hsb
model are supported

%package -n texlive-pst-hsb-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.02svn61322
Release:        0
Summary:        Documentation for texlive-pst-hsb
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Obsoletes:      texlive-pst-ghsb-doc < 2022

%description -n texlive-pst-hsb-doc
This package includes the documentation for texlive-pst-hsb

%post -n texlive-pst-hsb
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pst-hsb
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pst-hsb
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pst-hsb-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/pst-hsb/Changes
%{_texmfdistdir}/doc/generic/pst-hsb/README
%{_texmfdistdir}/doc/generic/pst-hsb/pst-hsb-doc.bib
%{_texmfdistdir}/doc/generic/pst-hsb/pst-hsb-doc.pdf
%{_texmfdistdir}/doc/generic/pst-hsb/pst-hsb-doc.tex

%files -n texlive-pst-hsb
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/pst-hsb/pst-hsb.tex
%{_texmfdistdir}/tex/latex/pst-hsb/pst-hsb.sty

%package -n texlive-pst-infixplot
Version:        %{texlive_version}.%{texlive_noarch}.0.0.11svn15878
Release:        0
License:        LPPL-1.0
Summary:        Using PSTricks plotting capacities with infix expressions rather than RPN
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-pst-infixplot-doc >= %{texlive_version}
Provides:       tex(infix-RPN.sty)
Provides:       tex(infix-RPN.tex)
Provides:       tex(pst-infixplot.sty)
Provides:       tex(pst-infixplot.tex)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source254:      pst-infixplot.tar.xz
Source255:      pst-infixplot.doc.tar.xz

%description -n texlive-pst-infixplot
Plotting functions with pst-plot is very powerful but sometimes
difficult to learn since the syntax of \psplot and
\parametricplot requires some PostScript knowledge. The
infix-RPN and pst-infixplot styles simplify the usage of
pst-plot for the beginner, providing macro commands that
convert natural mathematical expressions to PostScript syntax.

%package -n texlive-pst-infixplot-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.11svn15878
Release:        0
Summary:        Documentation for texlive-pst-infixplot
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/

%description -n texlive-pst-infixplot-doc
This package includes the documentation for texlive-pst-infixplot

%post -n texlive-pst-infixplot
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pst-infixplot
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pst-infixplot
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pst-infixplot-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/pst-infixplot/README
%{_texmfdistdir}/doc/generic/pst-infixplot/pst-infixplot-doc.ps
%{_texmfdistdir}/doc/generic/pst-infixplot/pst-infixplot-doc.tex
%{_texmfdistdir}/doc/generic/pst-infixplot/pst-infixplot.pdf

%files -n texlive-pst-infixplot
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/pst-infixplot/infix-RPN.tex
%{_texmfdistdir}/tex/generic/pst-infixplot/pst-infixplot.tex
%{_texmfdistdir}/tex/latex/pst-infixplot/infix-RPN.sty
%{_texmfdistdir}/tex/latex/pst-infixplot/pst-infixplot.sty

%package -n texlive-pst-intersect
Version:        %{texlive_version}.%{texlive_noarch}.0.0.4svn33210
Release:        0
License:        LPPL-1.0
Summary:        Compute intersections of arbitrary curves
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-pst-intersect-doc >= %{texlive_version}
Provides:       tex(pst-intersect.sty)
Provides:       tex(pst-intersect.tex)
Requires:       tex(pst-func.sty)
Requires:       tex(pst-node.sty)
Requires:       tex(pst-xkey.sty)
Requires:       tex(pstricks.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source256:      pst-intersect.tar.xz
Source257:      pst-intersect.doc.tar.xz

%description -n texlive-pst-intersect
The package computes the intersections between arbitrary
PostScript paths or Bezier curves, using the Bezier clipping
algorithm.

%package -n texlive-pst-intersect-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.4svn33210
Release:        0
Summary:        Documentation for texlive-pst-intersect
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Provides:       locale(texlive-pst-intersect-doc:de;en)

%description -n texlive-pst-intersect-doc
This package includes the documentation for texlive-pst-intersect

%post -n texlive-pst-intersect
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pst-intersect
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pst-intersect
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pst-intersect-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/pst-intersect/Changes
%{_texmfdistdir}/doc/latex/pst-intersect/README
%{_texmfdistdir}/doc/latex/pst-intersect/pst-intersect-DE.pdf
%{_texmfdistdir}/doc/latex/pst-intersect/pst-intersect.pdf

%files -n texlive-pst-intersect
%defattr(-,root,root,755)
%{_texmfdistdir}/dvips/pst-intersect/pst-intersect.pro
%{_texmfdistdir}/tex/generic/pst-intersect/pst-intersect.tex
%{_texmfdistdir}/tex/latex/pst-intersect/pst-intersect.sty

%package -n texlive-pst-jtree
Version:        %{texlive_version}.%{texlive_noarch}.2.6svn20946
Release:        0
License:        LPPL-1.0
Summary:        Typeset complex trees for linguists
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-pst-jtree-doc >= %{texlive_version}
Provides:       tex(pst-jtree.sty)
Provides:       tex(pst-jtree.tex)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source258:      pst-jtree.tar.xz
Source259:      pst-jtree.doc.tar.xz

%description -n texlive-pst-jtree
jTree uses PSTricks to enable linguists to typeset complex
trees. The package requires use of PStricks (of course) and
xkeyval packages. jTree is a development of, and replacement
for, the jftree package, which is no longer available.

%package -n texlive-pst-jtree-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.6svn20946
Release:        0
Summary:        Documentation for texlive-pst-jtree
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/

%description -n texlive-pst-jtree-doc
This package includes the documentation for texlive-pst-jtree

%post -n texlive-pst-jtree
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pst-jtree
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pst-jtree
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pst-jtree-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/pst-jtree/Doc-source.zip
%{_texmfdistdir}/doc/generic/pst-jtree/README
%{_texmfdistdir}/doc/generic/pst-jtree/pst-jtree-doc-add.pdf
%{_texmfdistdir}/doc/generic/pst-jtree/pst-jtree-doc.pdf
%{_texmfdistdir}/doc/generic/pst-jtree/pst-jtree-examples.tex

%files -n texlive-pst-jtree
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/pst-jtree/pst-jtree.tex
%{_texmfdistdir}/tex/latex/pst-jtree/pst-jtree.sty

%package -n texlive-pst-knot
Version:        %{texlive_version}.%{texlive_noarch}.0.0.2svn16033
Release:        0
License:        LPPL-1.0
Summary:        PSTricks package for displaying knots
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-pst-knot-doc >= %{texlive_version}
Provides:       tex(pst-knot.sty)
Provides:       tex(pst-knot.tex)
Requires:       tex(pstricks.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source260:      pst-knot.tar.xz
Source261:      pst-knot.doc.tar.xz

%description -n texlive-pst-knot
The package can produce a fair range of knot shapes, with all
the standard graphics controls one expects.

%package -n texlive-pst-knot-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.2svn16033
Release:        0
Summary:        Documentation for texlive-pst-knot
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/

%description -n texlive-pst-knot-doc
This package includes the documentation for texlive-pst-knot

%post -n texlive-pst-knot
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pst-knot
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pst-knot
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pst-knot-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/pst-knot/Changes
%{_texmfdistdir}/doc/generic/pst-knot/README
%{_texmfdistdir}/doc/generic/pst-knot/pst-knot-doc.pdf
%{_texmfdistdir}/doc/generic/pst-knot/pst-knot-doc.tex

%files -n texlive-pst-knot
%defattr(-,root,root,755)
%{_texmfdistdir}/dvips/pst-knot/pst-psm.pro
%{_texmfdistdir}/tex/generic/pst-knot/pst-knot.tex
%{_texmfdistdir}/tex/latex/pst-knot/pst-knot.sty

%package -n texlive-pst-labo
Version:        %{texlive_version}.%{texlive_noarch}.2.04svn39077
Release:        0
License:        LPPL-1.0
Summary:        Draw objects for Chemistry laboratories
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-pst-labo-doc >= %{texlive_version}
Provides:       tex(pst-labo.sty)
Provides:       tex(pst-labo.tex)
Provides:       tex(pst-laboObj.tex)
Requires:       tex(pstricks.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source262:      pst-labo.tar.xz
Source263:      pst-labo.doc.tar.xz

%description -n texlive-pst-labo
Pst-labo is a PSTricks related package for drawing basic and
complex chemical objects. The documentation of the package is
illuminated with plenty of illustrations together with their
source code, making it an easy read.

%package -n texlive-pst-labo-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.04svn39077
Release:        0
Summary:        Documentation for texlive-pst-labo
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/

%description -n texlive-pst-labo-doc
This package includes the documentation for texlive-pst-labo

%post -n texlive-pst-labo
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pst-labo
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pst-labo
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pst-labo-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/pst-labo/Changes
%{_texmfdistdir}/doc/generic/pst-labo/Makefile
%{_texmfdistdir}/doc/generic/pst-labo/README
%{_texmfdistdir}/doc/generic/pst-labo/pst-labo-doc.bib
%{_texmfdistdir}/doc/generic/pst-labo/pst-labo-docDE.pdf
%{_texmfdistdir}/doc/generic/pst-labo/pst-labo-docDE.tex
%{_texmfdistdir}/doc/generic/pst-labo/pst-labo-docEN.pdf
%{_texmfdistdir}/doc/generic/pst-labo/pst-labo-docEN.tex
%{_texmfdistdir}/doc/generic/pst-labo/pst-labo-docFR.pdf
%{_texmfdistdir}/doc/generic/pst-labo/pst-labo-docFR.tex
%{_texmfdistdir}/doc/generic/pst-labo/pst-labo8-tab1-DE.tex
%{_texmfdistdir}/doc/generic/pst-labo/pst-labo8-tab1-EN.tex
%{_texmfdistdir}/doc/generic/pst-labo/pst-labo8-tab1-FR.tex

%files -n texlive-pst-labo
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/pst-labo/pst-labo.tex
%{_texmfdistdir}/tex/generic/pst-labo/pst-laboObj.tex
%{_texmfdistdir}/tex/latex/pst-labo/pst-labo.sty

%package -n texlive-pst-layout
Version:        %{texlive_version}.%{texlive_noarch}.0.0.95svn29803
Release:        0
License:        LPPL-1.0
Summary:        Page layout macros based on PSTricks packages
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-pst-layout-doc >= %{texlive_version}
Provides:       tex(pst-layout.sty)
Requires:       tex(arrayjobx.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(ifthen.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source264:      pst-layout.tar.xz
Source265:      pst-layout.doc.tar.xz

%description -n texlive-pst-layout
The package provides a means of creating elaborate
("pseudo-tabular") layouts of material, typically to be
overlaid on an included graphic. The package requires a recent
version of the package pst-node and some other pstricks-related
material.

%package -n texlive-pst-layout-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.95svn29803
Release:        0
Summary:        Documentation for texlive-pst-layout
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/

%description -n texlive-pst-layout-doc
This package includes the documentation for texlive-pst-layout

%post -n texlive-pst-layout
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pst-layout
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pst-layout
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pst-layout-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/pst-layout/README
%{_texmfdistdir}/doc/latex/pst-layout/pst-layout-doc.pdf
%{_texmfdistdir}/doc/latex/pst-layout/pst-layout-doc.tex

%files -n texlive-pst-layout
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/pst-layout/pst-layout.sty

%package -n texlive-pst-lens
Version:        %{texlive_version}.%{texlive_noarch}.1.02svn15878
Release:        0
License:        LPPL-1.0
Summary:        Lenses with PSTricks
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-pst-lens-doc >= %{texlive_version}
Provides:       tex(pst-lens.sty)
Provides:       tex(pst-lens.tex)
Requires:       tex(pstricks.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source266:      pst-lens.tar.xz
Source267:      pst-lens.doc.tar.xz

%description -n texlive-pst-lens
This PSTricks package provides a really rather simple command
\PstLens that will draw a lens. Command parameters provide a
remarkable range of effects.

%package -n texlive-pst-lens-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.02svn15878
Release:        0
Summary:        Documentation for texlive-pst-lens
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/

%description -n texlive-pst-lens-doc
This package includes the documentation for texlive-pst-lens

%post -n texlive-pst-lens
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pst-lens
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pst-lens
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pst-lens-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/pst-lens/Changes
%{_texmfdistdir}/doc/generic/pst-lens/README
%{_texmfdistdir}/doc/generic/pst-lens/pst-lens.pdf

%files -n texlive-pst-lens
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/pst-lens/pst-lens.tex
%{_texmfdistdir}/tex/latex/pst-lens/pst-lens.sty

%package -n texlive-pst-light3d
Version:        %{texlive_version}.%{texlive_noarch}.0.0.12svn15878
Release:        0
License:        LPPL-1.0
Summary:        Three dimensional lighting effects (PSTricks)
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-pst-light3d-doc >= %{texlive_version}
Provides:       tex(pst-light3d.sty)
Provides:       tex(pst-light3d.tex)
Requires:       tex(pstricks.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source268:      pst-light3d.tar.xz
Source269:      pst-light3d.doc.tar.xz

%description -n texlive-pst-light3d
A PSTricks package for three dimensional lighting effects on
characters and PSTricks graphics, like lines, curves, plots,
...

%package -n texlive-pst-light3d-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.12svn15878
Release:        0
Summary:        Documentation for texlive-pst-light3d
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/

%description -n texlive-pst-light3d-doc
This package includes the documentation for texlive-pst-light3d

%post -n texlive-pst-light3d
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pst-light3d
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pst-light3d
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pst-light3d-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/pst-light3d/Changes
%{_texmfdistdir}/doc/generic/pst-light3d/README
%{_texmfdistdir}/doc/generic/pst-light3d/pst-light3d-doc.bib
%{_texmfdistdir}/doc/generic/pst-light3d/pst-light3d-doc.pdf
%{_texmfdistdir}/doc/generic/pst-light3d/pst-light3d-doc.tex

%files -n texlive-pst-light3d
%defattr(-,root,root,755)
%{_texmfdistdir}/dvips/pst-light3d/pst-light3d.pro
%{_texmfdistdir}/tex/generic/pst-light3d/pst-light3d.tex
%{_texmfdistdir}/tex/latex/pst-light3d/pst-light3d.sty

%package -n texlive-pst-lsystem
Version:        %{texlive_version}.%{texlive_noarch}.0.0.02svn49556
Release:        0
License:        LPPL-1.0
Summary:        Create images based on a L-system
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-pst-lsystem-doc >= %{texlive_version}
Provides:       tex(pst-lsystem.sty)
Provides:       tex(pst-lsystem.tex)
Requires:       tex(pstricks.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source270:      pst-lsystem.tar.xz
Source271:      pst-lsystem.doc.tar.xz

%description -n texlive-pst-lsystem
pst-lsystem is a PSTricks based package for creating images
based on a L-system. A L-system (Lindenmayer system) is a set
of rules which can be used to model the morphology of a variety
of organisms or fractals like the Kochflake or Hilbert curve.

%package -n texlive-pst-lsystem-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.02svn49556
Release:        0
Summary:        Documentation for texlive-pst-lsystem
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/

%description -n texlive-pst-lsystem-doc
This package includes the documentation for texlive-pst-lsystem

%post -n texlive-pst-lsystem
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pst-lsystem
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pst-lsystem
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pst-lsystem-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/pst-lsystem/Changes
%{_texmfdistdir}/doc/generic/pst-lsystem/README.md
%{_texmfdistdir}/doc/generic/pst-lsystem/pst-lsystem-doc.bib
%{_texmfdistdir}/doc/generic/pst-lsystem/pst-lsystem-doc.pdf
%{_texmfdistdir}/doc/generic/pst-lsystem/pst-lsystem-doc.tex

%files -n texlive-pst-lsystem
%defattr(-,root,root,755)
%{_texmfdistdir}/dvips/pst-lsystem/pst-lsystem.pro
%{_texmfdistdir}/tex/generic/pst-lsystem/pst-lsystem.tex
%{_texmfdistdir}/tex/latex/pst-lsystem/pst-lsystem.sty

%package -n texlive-pst-magneticfield
Version:        %{texlive_version}.%{texlive_noarch}.1.16svn49780
Release:        0
License:        LPPL-1.0
Summary:        Plotting a magnetic field with PSTricks
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-pst-magneticfield-doc >= %{texlive_version}
Provides:       tex(pst-magneticfield.sty)
Provides:       tex(pst-magneticfield.tex)
Requires:       tex(multido.sty)
Requires:       tex(pst-3d.sty)
Requires:       tex(pstricks.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source272:      pst-magneticfield.tar.xz
Source273:      pst-magneticfield.doc.tar.xz

%description -n texlive-pst-magneticfield
pst-magneticfield is a PSTricks related package to draw the
magnetic field lines of Helmholtz coils in a two or three
dimensional view. There are several parameters to create a
different output. For more informations or some examples read
the documentation of the package.

%package -n texlive-pst-magneticfield-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.16svn49780
Release:        0
Summary:        Documentation for texlive-pst-magneticfield
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/

%description -n texlive-pst-magneticfield-doc
This package includes the documentation for texlive-pst-magneticfield

%post -n texlive-pst-magneticfield
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pst-magneticfield
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pst-magneticfield
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pst-magneticfield-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/pst-magneticfield/Changes
%{_texmfdistdir}/doc/generic/pst-magneticfield/README.md
%{_texmfdistdir}/doc/generic/pst-magneticfield/pst-magneticfield-doc.bib
%{_texmfdistdir}/doc/generic/pst-magneticfield/pst-magneticfield-doc.pdf
%{_texmfdistdir}/doc/generic/pst-magneticfield/pst-magneticfield-doc.tex

%files -n texlive-pst-magneticfield
%defattr(-,root,root,755)
%{_texmfdistdir}/dvips/pst-magneticfield/pst-magneticfield.pro
%{_texmfdistdir}/tex/generic/pst-magneticfield/pst-magneticfield.tex
%{_texmfdistdir}/tex/latex/pst-magneticfield/pst-magneticfield.sty

%package -n texlive-pst-marble
Version:        %{texlive_version}.%{texlive_noarch}.1.6svn50925
Release:        0
License:        LPPL-1.0
Summary:        A PSTricks package to draw marble-like patterns
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-pst-marble-doc >= %{texlive_version}
Provides:       tex(pst-marble.sty)
Provides:       tex(pst-marble.tex)
Requires:       tex(pstricks.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source274:      pst-marble.tar.xz
Source275:      pst-marble.doc.tar.xz

%description -n texlive-pst-marble
This is a PSTricks package to draw marble-like patterns.

%package -n texlive-pst-marble-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.6svn50925
Release:        0
Summary:        Documentation for texlive-pst-marble
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/

%description -n texlive-pst-marble-doc
This package includes the documentation for texlive-pst-marble

%post -n texlive-pst-marble
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pst-marble
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pst-marble
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pst-marble-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/pst-marble/CHANGES.md
%{_texmfdistdir}/doc/generic/pst-marble/Nautilus.eps
%{_texmfdistdir}/doc/generic/pst-marble/README.md
%{_texmfdistdir}/doc/generic/pst-marble/Rollers.eps
%{_texmfdistdir}/doc/generic/pst-marble/Wave.eps
%{_texmfdistdir}/doc/generic/pst-marble/examples/Blendmodes.tex
%{_texmfdistdir}/doc/generic/pst-marble/examples/Bouquet.pdf
%{_texmfdistdir}/doc/generic/pst-marble/examples/Bouquet.tex
%{_texmfdistdir}/doc/generic/pst-marble/examples/BurgWave.pdf
%{_texmfdistdir}/doc/generic/pst-marble/examples/BurgWave.tex
%{_texmfdistdir}/doc/generic/pst-marble/examples/Contour.pdf
%{_texmfdistdir}/doc/generic/pst-marble/examples/Contour.tex
%{_texmfdistdir}/doc/generic/pst-marble/examples/Curl.pdf
%{_texmfdistdir}/doc/generic/pst-marble/examples/Curl.tex
%{_texmfdistdir}/doc/generic/pst-marble/examples/EdgyStirred.pdf
%{_texmfdistdir}/doc/generic/pst-marble/examples/EdgyStirred.tex
%{_texmfdistdir}/doc/generic/pst-marble/examples/Eggcrate.pdf
%{_texmfdistdir}/doc/generic/pst-marble/examples/Eggcrate.tex
%{_texmfdistdir}/doc/generic/pst-marble/examples/Latte.pdf
%{_texmfdistdir}/doc/generic/pst-marble/examples/Latte.tex
%{_texmfdistdir}/doc/generic/pst-marble/examples/Leaves.pdf
%{_texmfdistdir}/doc/generic/pst-marble/examples/Leaves.tex
%{_texmfdistdir}/doc/generic/pst-marble/examples/Moire.pdf
%{_texmfdistdir}/doc/generic/pst-marble/examples/Moire.tex
%{_texmfdistdir}/doc/generic/pst-marble/examples/Nautilus.pdf
%{_texmfdistdir}/doc/generic/pst-marble/examples/Nautilus.tex
%{_texmfdistdir}/doc/generic/pst-marble/examples/Nonpareil.pdf
%{_texmfdistdir}/doc/generic/pst-marble/examples/Nonpareil.tex
%{_texmfdistdir}/doc/generic/pst-marble/examples/Rollers.pdf
%{_texmfdistdir}/doc/generic/pst-marble/examples/Rollers.tex
%{_texmfdistdir}/doc/generic/pst-marble/examples/Stone.pdf
%{_texmfdistdir}/doc/generic/pst-marble/examples/Stone.tex
%{_texmfdistdir}/doc/generic/pst-marble/examples/Transparency.tex
%{_texmfdistdir}/doc/generic/pst-marble/examples/Wave.pdf
%{_texmfdistdir}/doc/generic/pst-marble/examples/Wave.tex
%{_texmfdistdir}/doc/generic/pst-marble/examples/Wreath.pdf
%{_texmfdistdir}/doc/generic/pst-marble/examples/Wreath.tex
%{_texmfdistdir}/doc/generic/pst-marble/pst-marble-commands.pdf
%{_texmfdistdir}/doc/generic/pst-marble/pst-marble-commands.tex
%{_texmfdistdir}/doc/generic/pst-marble/pst-marble-doc.pdf
%{_texmfdistdir}/doc/generic/pst-marble/pst-marble-doc.tex

%files -n texlive-pst-marble
%defattr(-,root,root,755)
%{_texmfdistdir}/dvips/pst-marble/pst-marble.pro
%{_texmfdistdir}/tex/generic/pst-marble/pst-marble.tex
%{_texmfdistdir}/tex/latex/pst-marble/pst-marble.sty

%package -n texlive-pst-math
Version:        %{texlive_version}.%{texlive_noarch}.0.0.65svn49425
Release:        0
License:        LPPL-1.0
Summary:        Enhancement of PostScript math operators to use with PSTricks
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-pst-math-doc >= %{texlive_version}
Provides:       tex(pst-math.sty)
Provides:       tex(pst-math.tex)
Requires:       tex(ifluatex.sty)
Requires:       tex(pst-calculate.sty)
Requires:       tex(xstring.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source276:      pst-math.tar.xz
Source277:      pst-math.doc.tar.xz

%description -n texlive-pst-math
PostScript lacks a lot of basic operators such as tan, acos,
asin, cosh, sinh, tanh, acosh, asinh, atanh, exp (with e base).
Also (oddly) cos and sin use arguments in degrees. Pst-math
provides all those operators in a header file pst-math.pro with
wrappers pst-math.sty and pst-math.tex. In addition, sinc,
gauss, gammaln and bessel are implemented (only partially for
the latter). The package is designed essentially to work with
pst-plot but can be used in whatever PS code (such as PSTricks
SpecialCoor "!", which is useful for placing labels). The
package also provides a routine SIMPSON for numerical
integration and a solver of linear equation systems.

%package -n texlive-pst-math-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.65svn49425
Release:        0
Summary:        Documentation for texlive-pst-math
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/

%description -n texlive-pst-math-doc
This package includes the documentation for texlive-pst-math

%post -n texlive-pst-math
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pst-math
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pst-math
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pst-math-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/pst-math/Changes
%{_texmfdistdir}/doc/generic/pst-math/README
%{_texmfdistdir}/doc/generic/pst-math/pst-math-doc.bib
%{_texmfdistdir}/doc/generic/pst-math/pst-math-doc.pdf
%{_texmfdistdir}/doc/generic/pst-math/pst-math-doc.tex

%files -n texlive-pst-math
%defattr(-,root,root,755)
%{_texmfdistdir}/dvips/pst-math/pst-math.pro
%{_texmfdistdir}/tex/generic/pst-math/pst-math.tex
%{_texmfdistdir}/tex/latex/pst-math/pst-math.sty

%package -n texlive-pst-mirror
Version:        %{texlive_version}.%{texlive_noarch}.1.02svn60506
Release:        0
License:        LPPL-1.0
Summary:        Images on a spherical mirror
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-pst-mirror-doc >= %{texlive_version}
Provides:       tex(pst-mirror.sty)
Provides:       tex(pst-mirror.tex)
Requires:       tex(pstricks.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source278:      pst-mirror.tar.xz
Source279:      pst-mirror.doc.tar.xz

%description -n texlive-pst-mirror
The package provides commands and supporting PostScript
material for drawing images as if reflected by a spherical
mirror.

%package -n texlive-pst-mirror-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.02svn60506
Release:        0
Summary:        Documentation for texlive-pst-mirror
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Provides:       locale(texlive-pst-mirror-doc:fr)

%description -n texlive-pst-mirror-doc
This package includes the documentation for texlive-pst-mirror

%post -n texlive-pst-mirror
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pst-mirror
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pst-mirror
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pst-mirror-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/pst-mirror/Changes
%{_texmfdistdir}/doc/generic/pst-mirror/README
%{_texmfdistdir}/doc/generic/pst-mirror/createEPS/make.sh
%{_texmfdistdir}/doc/generic/pst-mirror/createEPS/make2.sh
%{_texmfdistdir}/doc/generic/pst-mirror/createEPS/script.readme
%{_texmfdistdir}/doc/generic/pst-mirror/createEPS/scripts/filtre.pl
%{_texmfdistdir}/doc/generic/pst-mirror/createEPS/test.pdf
%{_texmfdistdir}/doc/generic/pst-mirror/createEPS/test.sh
%{_texmfdistdir}/doc/generic/pst-mirror/createEPS/test.tex
%{_texmfdistdir}/doc/generic/pst-mirror/createEPS/xa.eps
%{_texmfdistdir}/doc/generic/pst-mirror/createEPS/xa.tex
%{_texmfdistdir}/doc/generic/pst-mirror/createEPS/xb.eps
%{_texmfdistdir}/doc/generic/pst-mirror/createEPS/xc.eps
%{_texmfdistdir}/doc/generic/pst-mirror/pst-mirror-doc.bib
%{_texmfdistdir}/doc/generic/pst-mirror/pst-mirror-doc.pdf
%{_texmfdistdir}/doc/generic/pst-mirror/pst-mirror-doc.tex

%files -n texlive-pst-mirror
%defattr(-,root,root,755)
%{_texmfdistdir}/dvips/pst-mirror/pst-mirror.pro
%{_texmfdistdir}/tex/generic/pst-mirror/pst-mirror.tex
%{_texmfdistdir}/tex/latex/pst-mirror/pst-mirror.sty

%package -n texlive-pst-moire
Version:        %{texlive_version}.%{texlive_noarch}.2.2svn60411
Release:        0
License:        LPPL-1.0
Summary:        A PSTricks package to draw moire patterns
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-pst-moire-doc >= %{texlive_version}
Provides:       tex(pst-moire.sty)
Provides:       tex(pst-moire.tex)
Requires:       tex(pstricks.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source280:      pst-moire.tar.xz
Source281:      pst-moire.doc.tar.xz

%description -n texlive-pst-moire
This is a PSTricks package to draw moire patterns.

%package -n texlive-pst-moire-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.2svn60411
Release:        0
Summary:        Documentation for texlive-pst-moire
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/

%description -n texlive-pst-moire-doc
This package includes the documentation for texlive-pst-moire

%post -n texlive-pst-moire
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pst-moire
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pst-moire
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pst-moire-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/pst-moire/README.md
%{_texmfdistdir}/doc/generic/pst-moire/examples/pattern1.pdf
%{_texmfdistdir}/doc/generic/pst-moire/examples/pattern1.tex
%{_texmfdistdir}/doc/generic/pst-moire/examples/pattern2.pdf
%{_texmfdistdir}/doc/generic/pst-moire/examples/pattern2.tex
%{_texmfdistdir}/doc/generic/pst-moire/examples/pattern3.pdf
%{_texmfdistdir}/doc/generic/pst-moire/examples/pattern3.tex
%{_texmfdistdir}/doc/generic/pst-moire/examples/pattern4.pdf
%{_texmfdistdir}/doc/generic/pst-moire/examples/pattern4.tex
%{_texmfdistdir}/doc/generic/pst-moire/examples/psGlassPattern.pdf
%{_texmfdistdir}/doc/generic/pst-moire/examples/psGlassPattern.tex
%{_texmfdistdir}/doc/generic/pst-moire/pst-cosine.pro
%{_texmfdistdir}/doc/generic/pst-moire/pst-moire-doc.pdf
%{_texmfdistdir}/doc/generic/pst-moire/pst-moire-doc.tex
%{_texmfdistdir}/doc/generic/pst-moire/pst-sin.pro

%files -n texlive-pst-moire
%defattr(-,root,root,755)
%{_texmfdistdir}/dvips/pst-moire/pst-moire.pro
%{_texmfdistdir}/tex/generic/pst-moire/pst-moire.tex
%{_texmfdistdir}/tex/latex/pst-moire/pst-moire.sty

%package -n texlive-pst-node
Version:        %{texlive_version}.%{texlive_noarch}.1.43svn61838
Release:        0
License:        LPPL-1.0
Summary:        Nodes and node connections in PSTricks
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-pst-node-doc >= %{texlive_version}
Provides:       tex(pst-node.sty)
Provides:       tex(pst-node.tex)
Provides:       tex(pst-node97.tex)
Requires:       tex(pstricks.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source282:      pst-node.tar.xz
Source283:      pst-node.doc.tar.xz

%description -n texlive-pst-node
The package enables the user to connect information, and to
place labels, without knowing (in advance) the actual positions
of the items to be connected, or where the connecting line
should go. The macros are useful for making graphs and trees,
mathematical diagrams, linguistic syntax diagrams, and so on.
The package contents were previously distributed as a part of
the pstricks base distribution; the package serves as an
extension to PSTricks.

%package -n texlive-pst-node-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.43svn61838
Release:        0
Summary:        Documentation for texlive-pst-node
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Provides:       locale(texlive-pst-node-doc:en)

%description -n texlive-pst-node-doc
This package includes the documentation for texlive-pst-node

%post -n texlive-pst-node
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pst-node
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pst-node
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pst-node-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/pst-node/Changes
%{_texmfdistdir}/doc/generic/pst-node/README
%{_texmfdistdir}/doc/generic/pst-node/pst-node-doc.bib
%{_texmfdistdir}/doc/generic/pst-node/pst-node-doc.pdf
%{_texmfdistdir}/doc/generic/pst-node/pst-node-doc.tex

%files -n texlive-pst-node
%defattr(-,root,root,755)
%{_texmfdistdir}/dvips/pst-node/pst-node.pro
%{_texmfdistdir}/dvips/pst-node/pst-node97.pro
%{_texmfdistdir}/tex/generic/pst-node/pst-node.tex
%{_texmfdistdir}/tex/generic/pst-node/pst-node97.tex
%{_texmfdistdir}/tex/latex/pst-node/pst-node.sty

%package -n texlive-pst-ob3d
Version:        %{texlive_version}.%{texlive_noarch}.0.0.22svn54514
Release:        0
License:        LPPL-1.0
Summary:        Three dimensional objects using PSTricks
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-pst-ob3d-doc >= %{texlive_version}
Provides:       tex(pst-ob3d.sty)
Provides:       tex(pst-ob3d.tex)
Requires:       tex(pstricks.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source284:      pst-ob3d.tar.xz
Source285:      pst-ob3d.doc.tar.xz

%description -n texlive-pst-ob3d
The package uses PSTricks to provide basic three-dimensional
objects. As yet, only cubes (which can be deformed to
rectangular parallelipipeds) and dies (which are only a special
kind of cubes) are defined.

%package -n texlive-pst-ob3d-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.22svn54514
Release:        0
Summary:        Documentation for texlive-pst-ob3d
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/

%description -n texlive-pst-ob3d-doc
This package includes the documentation for texlive-pst-ob3d

%post -n texlive-pst-ob3d
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pst-ob3d
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pst-ob3d
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pst-ob3d-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/pst-ob3d/Changes
%{_texmfdistdir}/doc/generic/pst-ob3d/README
%{_texmfdistdir}/doc/generic/pst-ob3d/pst-ob3d.pdf

%files -n texlive-pst-ob3d
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/pst-ob3d/pst-ob3d.tex
%{_texmfdistdir}/tex/latex/pst-ob3d/pst-ob3d.sty

%package -n texlive-pst-ode
Version:        %{texlive_version}.%{texlive_noarch}.0.0.15svn58293
Release:        0
License:        LPPL-1.0
Summary:        Solving initial value problems for sets of Ordinary Differential Equations
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-pst-ode-doc >= %{texlive_version}
Provides:       tex(pst-ode.sty)
Provides:       tex(pst-ode.tex)
Requires:       tex(pstricks.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source286:      pst-ode.tar.xz
Source287:      pst-ode.doc.tar.xz

%description -n texlive-pst-ode
The package defines \pstODEsolve for solving initial value
problems for sets of Ordinary Differential Equations (ODE)
using the Runge-Kutta-Fehlberg (RKF45) method with automatic
step size adjustment. The result is stored as a PostScript
object and may be plotted later using macros from other
PSTricks packages, such as \listplot (pst-plot) and
\listplotThreeD (pst-3dplot), or may be further processed by
user-defined PostScript procedures. Optionally, the computed
state vectors can be written as a table to a text file.

%package -n texlive-pst-ode-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.15svn58293
Release:        0
Summary:        Documentation for texlive-pst-ode
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/

%description -n texlive-pst-ode-doc
This package includes the documentation for texlive-pst-ode

%post -n texlive-pst-ode
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pst-ode
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pst-ode
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pst-ode-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/pst-ode/ChangeLog
%{_texmfdistdir}/doc/generic/pst-ode/README.txt
%{_texmfdistdir}/doc/generic/pst-ode/examples/lorenz.tex
%{_texmfdistdir}/doc/generic/pst-ode/examples/ode.tex
%{_texmfdistdir}/doc/generic/pst-ode/examples/particle.tex
%{_texmfdistdir}/doc/generic/pst-ode/pst-ode-doc.pdf
%{_texmfdistdir}/doc/generic/pst-ode/pst-ode-doc.tex

%files -n texlive-pst-ode
%defattr(-,root,root,755)
%{_texmfdistdir}/dvips/pst-ode/pst-ode.pro
%{_texmfdistdir}/tex/generic/pst-ode/pst-ode.tex
%{_texmfdistdir}/tex/latex/pst-ode/pst-ode.sty

%package -n texlive-pst-optexp
Version:        %{texlive_version}.%{texlive_noarch}.6.1svn61917
Release:        0
License:        LPPL-1.0
Summary:        Drawing optical experimental setups
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-pst-optexp-doc >= %{texlive_version}
Provides:       tex(pst-optexp.sty)
Requires:       tex(environ.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(multido.sty)
Requires:       tex(pst-eucl.sty)
Requires:       tex(pst-intersect.sty)
Requires:       tex(pst-node.sty)
Requires:       tex(pst-plot.sty)
Requires:       tex(pst-xkey.sty)
Requires:       tex(pstricks-add.sty)
Requires:       tex(pstricks.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source288:      pst-optexp.tar.xz
Source289:      pst-optexp.doc.tar.xz

%description -n texlive-pst-optexp
The package is a collection of optical components that
facilitate easy sketching of optical experimental setups. The
package uses PSTricks for its output. A wide range of free-ray
and fibre components is provided, the alignment, positioning
and labelling of which can be achieved in very simple and
flexible ways. The components may be connected with fibers or
beams, and realistic raytraced beam paths are also possible.

%package -n texlive-pst-optexp-doc
Version:        %{texlive_version}.%{texlive_noarch}.6.1svn61917
Release:        0
Summary:        Documentation for texlive-pst-optexp
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Provides:       locale(texlive-pst-optexp-doc:de;en)

%description -n texlive-pst-optexp-doc
This package includes the documentation for texlive-pst-optexp

%post -n texlive-pst-optexp
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pst-optexp
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pst-optexp
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pst-optexp-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/pst-optexp/Changes
%{_texmfdistdir}/doc/latex/pst-optexp/README
%{_texmfdistdir}/doc/latex/pst-optexp/pst-optexp-DE.pdf
%{_texmfdistdir}/doc/latex/pst-optexp/pst-optexp-quickref.pdf
%{_texmfdistdir}/doc/latex/pst-optexp/pst-optexp.pdf

%files -n texlive-pst-optexp
%defattr(-,root,root,755)
%{_texmfdistdir}/dvips/pst-optexp/pst-optexp.pro
%{_texmfdistdir}/makeindex/pst-optexp/pst-optexp.ist
%{_texmfdistdir}/tex/latex/pst-optexp/pst-optexp.sty

%package -n texlive-pst-optic
Version:        %{texlive_version}.%{texlive_noarch}.1.02svn41999
Release:        0
License:        LPPL-1.0
Summary:        Drawing optics diagrams
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-pst-optic-doc >= %{texlive_version}
Provides:       tex(pst-optic.sty)
Provides:       tex(pst-optic.tex)
Requires:       tex(pstricks.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source290:      pst-optic.tar.xz
Source291:      pst-optic.doc.tar.xz

%description -n texlive-pst-optic
A package for drawing both reflective and refractive optics
diagrams. The package requires pstricks later than version
1.10.

%package -n texlive-pst-optic-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.02svn41999
Release:        0
Summary:        Documentation for texlive-pst-optic
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/

%description -n texlive-pst-optic-doc
This package includes the documentation for texlive-pst-optic

%post -n texlive-pst-optic
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pst-optic
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pst-optic
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pst-optic-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/pst-optic/Changes
%{_texmfdistdir}/doc/generic/pst-optic/README
%{_texmfdistdir}/doc/generic/pst-optic/pst-optic-doc.bib
%{_texmfdistdir}/doc/generic/pst-optic/pst-optic-doc.pdf
%{_texmfdistdir}/doc/generic/pst-optic/pst-optic-doc.tex

%files -n texlive-pst-optic
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/pst-optic/pst-optic.tex
%{_texmfdistdir}/tex/latex/pst-optic/pst-optic.sty

%package -n texlive-pst-osci
Version:        %{texlive_version}.%{texlive_noarch}.2.82svn15878
Release:        0
License:        LPPL-1.0
Summary:        Oscgons with PSTricks
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-pst-osci-doc >= %{texlive_version}
Provides:       tex(pst-osci.sty)
Provides:       tex(pst-osci.tex)
Requires:       tex(pstricks.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source292:      pst-osci.tar.xz
Source293:      pst-osci.doc.tar.xz

%description -n texlive-pst-osci
This PSTricks package enables you to produce oscilloscope
"screen shots". Three channels can be used to represent the
most common signals (damped or not): namely sinusoidal,
rectangular, triangular, dog's tooth (left and right oriented).
The third channel allows you to add, to subtract or to multiply
the two other signals. Lissajous diagrams (XY-mode) can also be
obtained.

%package -n texlive-pst-osci-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.82svn15878
Release:        0
Summary:        Documentation for texlive-pst-osci
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Provides:       locale(texlive-pst-osci-doc:fr;en)

%description -n texlive-pst-osci-doc
This package includes the documentation for texlive-pst-osci

%post -n texlive-pst-osci
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pst-osci
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pst-osci
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pst-osci-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/pst-osci/Changes
%{_texmfdistdir}/doc/generic/pst-osci/README
%{_texmfdistdir}/doc/generic/pst-osci/oscilloscope.pdf
%{_texmfdistdir}/doc/generic/pst-osci/oscilloscope.tex
%{_texmfdistdir}/doc/generic/pst-osci/pst-osci-doc.pdf
%{_texmfdistdir}/doc/generic/pst-osci/pst-osci-doc.tex

%files -n texlive-pst-osci
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/pst-osci/pst-osci.tex
%{_texmfdistdir}/tex/latex/pst-osci/pst-osci.sty

%package -n texlive-pst-ovl
Version:        %{texlive_version}.%{texlive_noarch}.0.0.07bsvn54963
Release:        0
License:        LPPL-1.0
Summary:        Create and manage graphical overlays
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-pst-ovl-doc >= %{texlive_version}
Provides:       tex(pst-ovl.sty)
Provides:       tex(pst-ovl.tex)
Requires:       tex(pstricks.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source294:      pst-ovl.tar.xz
Source295:      pst-ovl.doc.tar.xz

%description -n texlive-pst-ovl
The package is useful when building an image from assorted
material, as in the slides of a projected presentation. The
package requires pstricks, and shares that package's
restrictions on usage when generating PDF output.

%package -n texlive-pst-ovl-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.07bsvn54963
Release:        0
Summary:        Documentation for texlive-pst-ovl
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/

%description -n texlive-pst-ovl-doc
This package includes the documentation for texlive-pst-ovl

%post -n texlive-pst-ovl
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pst-ovl
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pst-ovl
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pst-ovl-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/pst-ovl/Changes
%{_texmfdistdir}/doc/generic/pst-ovl/README
%{_texmfdistdir}/doc/generic/pst-ovl/pst-ovl-doc.bib
%{_texmfdistdir}/doc/generic/pst-ovl/pst-ovl-doc.pdf
%{_texmfdistdir}/doc/generic/pst-ovl/pst-ovl-doc.tex

%files -n texlive-pst-ovl
%defattr(-,root,root,755)
%{_texmfdistdir}/dvips/pst-ovl/pst-ovl.pro
%{_texmfdistdir}/tex/generic/pst-ovl/pst-ovl.tex
%{_texmfdistdir}/tex/latex/pst-ovl/pst-ovl.sty

%package -n texlive-pst-pad
Version:        %{texlive_version}.%{texlive_noarch}.0.0.3bsvn15878
Release:        0
License:        LPPL-1.0
Summary:        Draw simple attachment systems with PSTricks
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Suggests:       texlive-pst-pad-doc >= %{texlive_version}
Provides:       tex(pst-pad.sty)
Provides:       tex(pst-pad.tex)
Requires:       tex(pstricks.sty)
# Download at ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20220321
Source296:      pst-pad.tar.xz
Source297:      pst-pad.doc.tar.xz

%description -n texlive-pst-pad
The package collects a set of graphical elements based on
PStricks that can be used to facilitate display of attachment
systems such as two differently shaped surfaces with or without
a fluid wedged in between. These macros ease the display of wet
adhesion models and common friction systems such as boundary
lubrication, elastohydrodynamic lubrication and hydrodynamic
lubrication.

%package -n texlive-pst-pad-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.3bsvn15878
Release:        0
Summary:        Documentation for texlive-pst-pad
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Provides:       locale(texlive-pst-pad-doc:en;de)

%description -n texlive-pst-pad-doc
This package includes the documentation for texlive-pst-pad

%post -n texlive-pst-pad
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pst-pad
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pst-pad
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pst-pad-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/pst-pad/CHANGES
%{_texmfdistdir}/doc/generic/pst-pad/README
%{_texmfdistdir}/doc/generic/pst-pad/pst-pad-doc-header.tex
%{_texmfdistdir}/doc/generic/pst-pad/pst-pad-doc.pdf
%{_texmfdistdir}/doc/generic/pst-pad/pst-pad-doc.tex
%{_texmfdistdir}/doc/generic/pst-pad/pst-pad-docDE.pdf
%{_texmfdistdir}/doc/generic/pst-pad/pst-pad-docDE.tex
%{_texmfdistdir}/doc/generic/pst-pad/showexpl.cfg

%files -n texlive-pst-pad
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/pst-pad/pst-pad.tex
%{_texmfdistdir}/tex/latex/pst-pad/pst-pad.sty

%prep
%setup -q -c -T

%build

%install
    rm -rf %{buildroot}
    mkdir -p %{buildroot}%{_texmfdistdir}
    mkdir -p %{buildroot}%{_texmfmaindir}/tlpkg/tlpostcode
    mkdir -p %{buildroot}%{_datadir}/texlive/tlpkg
    mkdir -p %{buildroot}/var/adm/update-scripts
    ln -sf ../../share/texmf        %{buildroot}%{_datadir}/texlive/texmf-dist
    ln -sf ../../share/texmf        %{buildroot}%{_datadir}/texlive/texmf
    ln -sf ../../../share/texmf/tlpkg/tlpostcode \
                                    %{buildroot}%{_datadir}/texlive/tlpkg/tlpostcode
    ln -sf tlpkg/tlpostcode         %{buildroot}%{_texmfmaindir}/tlpostcode
    tar --use-compress-program=xz -xf %{S:1} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:2} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:3} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:4} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:5} -C %{buildroot}%{_datadir}/texlive
    tar --use-compress-program=xz -xf %{S:6} -C %{buildroot}%{_datadir}/texlive
    tar --use-compress-program=xz -xf %{S:7} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:8} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:9} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:10} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:11} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:12} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:13} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:14} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:15} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-playfair
    for font in %{buildroot}/%{_texmfdistdir}/fonts/opentype/public/playfair/*.{pf[ab],[ot]tf} \
		%{buildroot}/%{_texmfdistdir}/fonts/type1/public/playfair/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-playfair
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-playfair/${base} ${font}
    done
    >  %{buildroot}%{_datadir}/fonts/texlive-playfair/encodings.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-playfair/fonts.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-playfair/fonts.scale
    mkdir -p %{buildroot}%{_datadir}/fontconfig/conf.avail
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/58-texlive-playfair.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-playfair    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-playfair/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF

    mkdir -p %{buildroot}%{_sysconfdir}/fonts/conf.d
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/55-texlive-playfair.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Disable plain Type1 font to let fontconfig       -->
	<!-- prefere the OpenType and TrueType fonts          -->
	<!-- ************************************************ -->

	<fontconfig>
	  <selectfont>
	    <rejectfont>
	      <glob>%{_datadir}/fonts/texlive-playfair/*.pf*</glob>
	    </rejectfont>
	  </selectfont>
	</fontconfig>
	EOF
    ln -sf %{_datadir}/fontconfig/conf.avail/55-texlive-playfair.conf %{buildroot}%{_sysconfdir}/fonts/conf.d/55-texlive-playfair.conf
    tar --use-compress-program=xz -xf %{S:16} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:17} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-plex
    for font in %{buildroot}/%{_texmfdistdir}/fonts/opentype/ibm/plex/*.{pf[ab],[ot]tf} \
		%{buildroot}/%{_texmfdistdir}/fonts/type1/ibm/plex/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-plex
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-plex/${base} ${font}
    done
    >  %{buildroot}%{_datadir}/fonts/texlive-plex/encodings.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-plex/fonts.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-plex/fonts.scale
    mkdir -p %{buildroot}%{_datadir}/fontconfig/conf.avail
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/58-texlive-plex.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-plex    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-plex/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF

    mkdir -p %{buildroot}%{_sysconfdir}/fonts/conf.d
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/55-texlive-plex.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Disable plain Type1 font to let fontconfig       -->
	<!-- prefere the OpenType and TrueType fonts          -->
	<!-- ************************************************ -->

	<fontconfig>
	  <selectfont>
	    <rejectfont>
	      <glob>%{_datadir}/fonts/texlive-plex/*.pf*</glob>
	    </rejectfont>
	  </selectfont>
	</fontconfig>
	EOF
    ln -sf %{_datadir}/fontconfig/conf.avail/55-texlive-plex.conf %{buildroot}%{_sysconfdir}/fonts/conf.d/55-texlive-plex.conf
    tar --use-compress-program=xz -xf %{S:18} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:19} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:20} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:21} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-plimsoll
    for font in %{buildroot}/%{_texmfdistdir}/fonts/type1/public/plimsoll/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-plimsoll
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-plimsoll/${base} ${font}
    done
    >  %{buildroot}%{_datadir}/fonts/texlive-plimsoll/encodings.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-plimsoll/fonts.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-plimsoll/fonts.scale
    mkdir -p %{buildroot}%{_datadir}/fontconfig/conf.avail
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/58-texlive-plimsoll.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-plimsoll    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-plimsoll/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF
    tar --use-compress-program=xz -xf %{S:22} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:23} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:24} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:25} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:26} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:27} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:28} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:29} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:30} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:31} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:32} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:33} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:34} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:35} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:36} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:37} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:38} -C %{buildroot}%{_datadir}/texlive
    tar --use-compress-program=xz -xf %{S:39} -C %{buildroot}%{_datadir}/texlive
    tar --use-compress-program=xz -xf %{S:40} -C %{buildroot}%{_datadir}/texlive
    tar --use-compress-program=xz -xf %{S:41} -C %{buildroot}%{_datadir}/texlive
    # Avoid /usr/bin/env <prog>
    for scr in %{_texmfdistdir}/scripts/pmxchords/pmxchords.lua
    do
	test -e %{buildroot}/$scr || continue
	ed %{buildroot}/${scr} <<-'EOF'
		1
		s@/env[[:blank:]]\+@/@
		.
		w
		q
	EOF
    done
    tar --use-compress-program=xz -xf %{S:42} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:43} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:44} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:45} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:46} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:47} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:48} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:49} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:50} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-poiretone
    for font in %{buildroot}/%{_texmfdistdir}/fonts/truetype/public/poiretone/*.{pf[ab],[ot]tf} \
		%{buildroot}/%{_texmfdistdir}/fonts/type1/public/poiretone/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-poiretone
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-poiretone/${base} ${font}
    done
    >  %{buildroot}%{_datadir}/fonts/texlive-poiretone/encodings.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-poiretone/fonts.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-poiretone/fonts.scale
    mkdir -p %{buildroot}%{_datadir}/fontconfig/conf.avail
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/58-texlive-poiretone.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-poiretone    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-poiretone/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF

    mkdir -p %{buildroot}%{_sysconfdir}/fonts/conf.d
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/55-texlive-poiretone.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Disable plain Type1 font to let fontconfig       -->
	<!-- prefere the OpenType and TrueType fonts          -->
	<!-- ************************************************ -->

	<fontconfig>
	  <selectfont>
	    <rejectfont>
	      <glob>%{_datadir}/fonts/texlive-poiretone/*.pf*</glob>
	    </rejectfont>
	  </selectfont>
	</fontconfig>
	EOF
    ln -sf %{_datadir}/fontconfig/conf.avail/55-texlive-poiretone.conf %{buildroot}%{_sysconfdir}/fonts/conf.d/55-texlive-poiretone.conf
    tar --use-compress-program=xz -xf %{S:51} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:52} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:53} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:54} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:55} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:56} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-poltawski
    for font in %{buildroot}/%{_texmfdistdir}/fonts/opentype/gust/poltawski/*.{pf[ab],[ot]tf} \
		%{buildroot}/%{_texmfdistdir}/fonts/type1/gust/poltawski/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-poltawski
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-poltawski/${base} ${font}
    done
    >  %{buildroot}%{_datadir}/fonts/texlive-poltawski/encodings.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-poltawski/fonts.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-poltawski/fonts.scale
    mkdir -p %{buildroot}%{_datadir}/fontconfig/conf.avail
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/58-texlive-poltawski.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-poltawski    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-poltawski/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF

    mkdir -p %{buildroot}%{_sysconfdir}/fonts/conf.d
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/55-texlive-poltawski.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Disable plain Type1 font to let fontconfig       -->
	<!-- prefere the OpenType and TrueType fonts          -->
	<!-- ************************************************ -->

	<fontconfig>
	  <selectfont>
	    <rejectfont>
	      <glob>%{_datadir}/fonts/texlive-poltawski/*.pf*</glob>
	    </rejectfont>
	  </selectfont>
	</fontconfig>
	EOF
    ln -sf %{_datadir}/fontconfig/conf.avail/55-texlive-poltawski.conf %{buildroot}%{_sysconfdir}/fonts/conf.d/55-texlive-poltawski.conf
    tar --use-compress-program=xz -xf %{S:57} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:58} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:59} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:60} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:61} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:62} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:63} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:64} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:65} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:66} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:67} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:68} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:69} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:70} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:71} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:72} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:73} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:74} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:75} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:76} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:77} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:78} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:79} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:80} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:81} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:82} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:83} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:84} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:85} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:86} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:87} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:88} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:89} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:90} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:91} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:92} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:93} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:94} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:95} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:96} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:97} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:98} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:99} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:100} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:101} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:102} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:103} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:104} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:105} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:106} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:107} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:108} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:109} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:110} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:111} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:112} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-prodint
    for font in %{buildroot}/%{_texmfdistdir}/fonts/type1/public/prodint/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-prodint
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-prodint/${base} ${font}
    done
    >  %{buildroot}%{_datadir}/fonts/texlive-prodint/encodings.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-prodint/fonts.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-prodint/fonts.scale
    mkdir -p %{buildroot}%{_datadir}/fontconfig/conf.avail
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/58-texlive-prodint.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-prodint    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-prodint/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF
    tar --use-compress-program=xz -xf %{S:113} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:114} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:115} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:116} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:117} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:118} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:119} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:120} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:121} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:122} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:123} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:124} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:125} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:126} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:127} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:128} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:129} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:130} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:131} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:132} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:133} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:134} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:135} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:136} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:137} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:138} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    pushd %{buildroot}%{_datadir}/texlive/texmf-dist
	patch --reject-format=unified --quoting-style=literal -f -p1 -F0 -T < %{S:139}
    popd
    tar --use-compress-program=xz -xf %{S:140} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:141} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:142} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:143} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:144} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:145} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:146} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:147} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:148} -C %{buildroot}%{_datadir}/texlive
    tar --use-compress-program=xz -xf %{S:149} -C %{buildroot}%{_datadir}/texlive
    # Avoid /usr/bin/env <prog>
    for scr in %{_texmfdistdir}/scripts/ps2eps/ps2eps.pl
    do
	test -e %{buildroot}/$scr || continue
	ed %{buildroot}/${scr} <<-'EOF'
		1
		s@/env[[:blank:]]\+@/@
		.
		w
		q
	EOF
    done
    tar --use-compress-program=xz -xf %{S:150} -C %{buildroot}%{_datadir}/texlive
    tar --use-compress-program=xz -xf %{S:151} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:152} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:153} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:154} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:155} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:156} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:157} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:158} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:159} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:160} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:161} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:162} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:163} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:164} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:165} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:166} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:167} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:168} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:169} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:170} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:171} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:172} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:173} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:174} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:175} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:176} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:177} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:178} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:179} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:180} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:181} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:182} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:183} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:184} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:185} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:186} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:187} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:188} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Remove files
    rm -vf  %{buildroot}%{_texmfdistdir}/doc/generic/pst-bar/pst-bar.orig
    tar --use-compress-program=xz -xf %{S:189} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:190} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:191} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:192} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:193} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:194} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:195} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:196} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:197} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:198} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:199} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:200} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:201} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:202} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:203} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:204} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:205} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:206} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:207} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:208} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:209} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:210} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:211} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:212} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:213} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:214} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:215} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:216} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:217} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:218} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:219} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:220} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:221} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:222} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:223} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:224} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:225} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:226} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:227} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:228} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:229} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:230} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:231} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:232} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:233} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:234} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:235} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:236} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:237} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:238} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:239} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:240} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:241} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:242} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:243} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Make possible scripts usable if any
    for scr in %{_texmfdistdir}/doc/generic/pst-geo/pst-geo-compress.pl \
	       %{_texmfdistdir}/doc/generic/pst-geo/pst-geo-decompress.pl
    do
	test -e %{buildroot}/$scr || continue
	chmod 0755 %{buildroot}/$scr
    done
    # Avoid /usr/bin/env <prog>
    for scr in %{_texmfdistdir}/doc/generic/pst-geo/pst-geo-compress.pl \
	       %{_texmfdistdir}/doc/generic/pst-geo/pst-geo-decompress.pl
    do
	test -e %{buildroot}/$scr || continue
	ed %{buildroot}/${scr} <<-'EOF'
		1
		s@/env[[:blank:]]\+@/@
		.
		w
		q
	EOF
    done
    tar --use-compress-program=xz -xf %{S:244} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:245} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:246} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:247} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:248} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:249} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:250} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:251} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:252} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:253} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:254} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:255} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:256} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:257} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:258} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:259} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:260} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:261} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:262} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:263} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:264} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:265} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:266} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:267} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:268} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:269} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:270} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:271} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:272} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:273} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:274} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:275} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:276} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:277} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:278} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:279} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Add shebang e.g. correct perl wrapper scripts if any
    for scr in %{_texmfdistdir}/doc/generic/pst-mirror/createEPS/make.sh \
	       %{_texmfdistdir}/doc/generic/pst-mirror/createEPS/make2.sh \
	       %{_texmfdistdir}/doc/generic/pst-mirror/createEPS/test.sh
    do
	test -e %{buildroot}/$scr || continue
	ed %{buildroot}/${scr} <<-'EOF'
		1
		i
		#! /bin/sh
		.
		w
		q
	EOF
    done
    tar --use-compress-program=xz -xf %{S:280} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:281} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:282} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:283} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:284} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:285} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:286} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:287} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:288} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:289} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:290} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:291} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:292} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:293} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:294} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:295} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:296} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:297} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Remove this
    rm -vrf %{buildroot}%{_texmfdistdir}/tlpkg/tlpobj
    rm -vrf %{buildroot}%{_texmfmaindir}/tlpkg/tlpobj
    rm -v  %{buildroot}%{_datadir}/texlive/texmf
    rm -v  %{buildroot}%{_datadir}/texlive/texmf-dist
    rm -v  %{buildroot}%{_texmfmaindir}/tlpostcode
    rm -vr %{buildroot}%{_datadir}/texlive
    # Handle manual pages
    rm -vf %{buildroot}%{_texmfmaindir}/doc/man/Makefile
    rm -vf %{buildroot}%{_texmfmaindir}/doc/man/man*/*.pdf
    rm -vf %{buildroot}%{_texmfdistdir}/doc/man/Makefile
    rm -vf %{buildroot}%{_texmfdistdir}/doc/man/man*/*.pdf
    for path in %{buildroot}%{_texmfmaindir}/doc/man/man? \
               %{buildroot}%{_texmfdistdir}/doc/man/man?
    do
        test -d "$path" || continue
        sec=${path##*/}
        mkdir -p %{buildroot}%{_mandir}/${sec}
        for page in ${path}/*.*
        do
            test -e "$page" || continue
            mv -f $page %{buildroot}%{_mandir}/${sec}/
        done
    done
    rm -rf %{buildroot}%{_texmfmaindir}/doc/man
    rm -rf %{buildroot}%{_texmfdistdir}/doc/man
    find %{buildroot}%{_texmfmaindir}/ %{buildroot}%{_texmfdistdir}/ \
        -type f -a -perm /g+w,o+w | xargs --no-run-if-empty chmod g-w,o-w

%changelog
