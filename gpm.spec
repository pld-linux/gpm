Summary:	General Purpose Mouse support for Linux
Summary(de):	Allgemeine Mausunterstützung für Linux
Summary(fr):	Gestion générale de la souris pour Linux
Summary(pl):	Wsparcie dla myszki w systemie Linux
Summary(tr):	Genel amaçlý fare desteði
Name:		gpm
Version:	1.17.8
Release:	1
Copyright:	GPL
Group:		Daemons
Group(pl):	Serwery
Source:		ftp://animal.unipv.it/pub/gpm/%{name}-%{version}.tar.gz
Source1:	gpm.init
Patch0:		gpm-info.patch
Patch1:		gpm-nops.patch
Patch2:		gpm-non-root.patch
Prereq:		/sbin/chkconfig
Prereq:		/sbin/install-info
BuildPrereq:	ncurses-devel
Buildroot:	/tmp/%{name}-%{version}-root

%description
GPM adds mouse support to text-based Linux applications such as emacs,
Midnight Commander, and more. It also provides console cut-and-paste
operations using the mouse. Includes a program to allow pop-up menus to
appear at the click of a mouse button.

%description -l de
GPM ermöglicht Maus-Unterstützung für zeichenorientierte Linux-
Anwendungen wie z.B. emacs und Midnight Commander. Außerdem sind
Ausschneiden und Einfügen mit der Maus auf der Konsole möglich. Enthält
ein Programm, daß bei Mausklick ein Pop-up-Menü aufruft.

%description -l fr
GPM ajoute un support souris au applications en mode texte de Linux comme
emacs, Midnight Commander, et bien d'autres. Cela fournit aussi des opérations
de copier/coller avec la souris sur les consoles. Comprend un programme
pour permettre l'apparition de menus déroulants grace à un clic droit avec
la souris.

%description -l pl
GPM zapewnia wsparcie dla myszki dla systemu Linux na konsoli systemowej.
Dziêki niemu mo¿na zaznaczaæ fragmenty tekstu na konsoli i wklejaæ
je w edytowany plik tekstowy. Operacje te s± najczê¶ciej dokonywane przez
wci¶niêcie prawego klawisza myszki (operacja zaznaczania fragmentu tekstu)
i nastêpnie wci¶niêcie klawisza <Shift>+¶rodkowego klawisza myszki
(operacja wklejania tekstu).

%description -l tr
GPM metin ekranda çalýþan Linux uygulamalarýna (emacs, Midnight Commander ve
diðerleri gibi) fare desteði saðlar. Ayrýca fare yardýmýyla konsollar
arasýnda kopyalama ve yapýþtýrma olanaðý sunar. Fare týklamasýyla pop-up
menülerin çýkmasýný saðlayan bir program da içerir.

%package devel
Summary:	Header files and documentation for writing mouse driven programs
Summary(pl):	Pliki nag³ówkowe i dokumentacja do gpm
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
This package allows you to develop your own text-mode programs that take
advantage of the mouse. 

%description -l de devel
Mit diesem Paket können Sie Ihre eigenen text-orientierten Programme
mit Mausunterstützung entwickeln.

%description -l fr devel
Ce paquetage permet de développer des programmes en mode texte tirant
avantage de la souris.

%description -l pl devel
Pliki nag³ówkowe i dokumentacja dla gpm. Dziêki nim bêdziesz móg³
pisaæ w³asne programy z wykorzystaniem myszki.

%description -l tr devel
Bu paket, fare kullanan yazýlýmlar geliþtirmenizi saðlayan dosyalarý içerir.

%package static
Summary:	Static gpm library
Summary(pl):	Biblioteki statyczne gpm
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Static gpm library.

%description -l pl static
Biblioteki statyczne gpm.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
autoconf
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" SOLDFLAGS="-s" \
./configure %{_target} \
	--sysconfdir=/etc \
	--disable-debug \
	--with-curses
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/{rc.d/init.d,sysconfig}

%ifarch sparc
(echo MOUSETYPE=\"sun\"; echo XEMU3=no) > $RPM_BUILD_ROOT/etc/sysconfig/mouse
%else
(echo "MOUSETYPE="; echo "XEMU3=") > $RPM_BUILD_ROOT/etc/sysconfig/mouse
%endif

make install-strip \
	prefix=$RPM_BUILD_ROOT/usr \
	sysconfdir=$RPM_BUILD_ROOT/etc \
	lispdir=$RPM_BUILD_ROOT%{_datadir}/emacs/site-lisp

install gpm-root.conf $RPM_BUILD_ROOT/etc
install mouse-test hltest $RPM_BUILD_ROOT/usr/bin

strip $RPM_BUILD_ROOT/usr/{bin/*,lib/lib*.so.*.*}

install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/gpm

gzip -9nf $RPM_BUILD_ROOT%{_datadir}/{info/gpm.info*,man/man{1,8}/*}

%post
/sbin/ldconfig
/sbin/install-info %{_infodir}/gpm.info.gz /etc/info-dir

/sbin/chkconfig --add gpm
if test -r /var/run/gpm.pid; then
	/etc/rc.d/init.d/gpm stop >&2
	/etc/rc.d/init.d/gpm start >&2
else
	echo "Run \"/etc/rc.d/init.d/gpm start\" to start gpm daemon."
fi

%preun
if [ "$1" = "0" ]; then
	/sbin/install-info %{_infodir}/gpm.info.gz --delete /etc/info-dir

	/sbin/chkconfig --del gpm
	/etc/rc.d/init.d/gpm stop >&2
fi

%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)

%config(noreplace) /etc/gpm-root.conf
%config(noreplace) /etc/sysconfig/mouse

%attr(754,root,root) /etc/rc.d/init.d/gpm
%attr(755,root,root) /usr/bin/*
%attr(755,root,root) /usr/sbin/*

%{_infodir}/gpm.info*
%{_mandir}/man[18]/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
/usr/include/gpm.h

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%changelog
* Sun May  9 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.17.8-1]
- now package is FHS 2.0 compliant.

* Wed Apr 28 1999 Artur Frysiak <wiget@pld.org.pl>
  [1.17-7-3]
- added BuildPrereq: ncurses-devel.

* Mon Apr 19 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.17.7-2]
- added noreplace parameter to %config files,
- recompiles on new rpm.

* Sat Feb 27 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.17.5-1]
- changed base Source url to ftp://animal.unipv.it/pub/gpm/,
- now libgpm is linked with ncurses as a term library,
- removed man group from man pages.

* Sun Jan 31 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.17.3-1d]
- added LDFLAGS="-s" to ./configure enviroment,
- added --sysconfdir=/etc to ./configure parameters,
- standarized %post, %preun restarting, stoping service on
  upgrade and uninstall,
- added Group(pl),
- changed perm on lib*.so* to 755,
- removed %config from /etc/rc.d/init.d/gpm and changed perm to 754,
- added striping shared libraries,
- removed /etc/rc.d/rc[01236].d/*gpm symlink (/etc/rc.d/init.d/gpm 
  have chkconfig support),
- standarized {un}registering info pages (added gpm-info.patch),
- added gzipping man pages.

* Wed Sep 30 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [1.13-9d]
- added pl translation.

* Wed Aug 26 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.13-9]
- changed Buildroot to /tmp/%%{name}-%%{version}-root,
- added using %%{name} and %%{version} in Source,
- added static subpackage,
- changed dependencies to "Requires: %%{name} = %%{version}" in devel
  subpackage,
- added using $RPM_OPT_FLAGS during compile,
- added stripping shared libraries,
- added full %attr description in %files,
- libgpm is now linked with libslang (so.1) as a term library
  (gpm-with_slang.patch).

* Tue Aug 11 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Apr 22 1998 Michael K. Johnson <johnsonm@redhat.com>
- enhanced initscript

* Fri Apr 10 1998 Cristian Gafton <gafton@redhat.com>
- recompiled for manhattan

* Wed Apr 08 1998 Erik Troan <ewt@redhat.com>
- updated to 1.13

* Mon Nov 03 1997 Donnie Barnes <djb@redhat.com>
- added patch from Richard to get things to build on the SPARC

* Tue Oct 28 1997 Donnie Barnes <djb@redhat.com>
- fixed the emacs patch to install the emacs files in the right
  place (hopefully).

* Mon Oct 13 1997 Erik Troan <ewt@redhat.com>
- added chkconfig support
- added install-info

* Thu Sep 11 1997 Donald Barnes <djb@redhat.com>
- upgraded from 1.10 to 1.12
- added status/restart functionality to init script
- added define LIBVER 1.11

* Thu Jun 19 1997 Erik Troan <ewt@redhat.com>
- built against glibc
