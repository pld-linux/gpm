Summary:	General Purpose Mouse support for Linux
Summary(de):	Allgemeine Mausunterst�tzung f�r Linux
Summary(fr):	Gestion g�n�rale de la souris pour Linux
Summary(pl):	Wsparcie dla myszki w systemie Linux
Summary(tr):	Genel ama�l� fare deste�i
Name:		gpm
Version:	1.17.8
Release:	3
Copyright:	GPL
Group:		Daemons
Group(pl):	Serwery
Source:		ftp://animal.unipv.it/pub/gpm/%{name}-%{version}.tar.gz
Source1:	gpm.init
Source2:	gpm.sysconfig
Patch0:		gpm-info.patch
Patch1:		gpm-nops.patch
Patch2:		gpm-non-root.patch
Prereq:		/sbin/chkconfig
Prereq:		/sbin/install-info
Buildroot:	/tmp/%{name}-%{version}-root

%define		_sysconfdir	/etc

%description
GPM adds mouse support to text-based Linux applications such as emacs,
Midnight Commander, and more. It also provides console cut-and-paste
operations using the mouse. Includes a program to allow pop-up menus to
appear at the click of a mouse button.

%description -l de
GPM erm�glicht Maus-Unterst�tzung f�r zeichenorientierte Linux-
Anwendungen wie z.B. emacs und Midnight Commander. Au�erdem sind
Ausschneiden und Einf�gen mit der Maus auf der Konsole m�glich. Enth�lt
ein Programm, da� bei Mausklick ein Pop-up-Men� aufruft.

%description -l fr
GPM ajoute un support souris au applications en mode texte de Linux comme
emacs, Midnight Commander, et bien d'autres. Cela fournit aussi des op�rations
de copier/coller avec la souris sur les consoles. Comprend un programme
pour permettre l'apparition de menus d�roulants grace � un clic droit avec
la souris.

%description -l pl
GPM zapewnia wsparcie dla myszki dla systemu Linux na konsoli systemowej.
Dzi�ki niemu mo�na zaznacza� fragmenty tekstu na konsoli i wkleja�
je w edytowany plik tekstowy. Operacje te s� najcz�ciej dokonywane przez
wci�ni�cie prawego klawisza myszki (operacja zaznaczania fragmentu tekstu)
i nast�pnie wci�ni�cie klawisza <Shift>+�rodkowego klawisza myszki
(operacja wklejania tekstu).

%description -l tr
GPM metin ekranda �al��an Linux uygulamalar�na (emacs, Midnight Commander ve
di�erleri gibi) fare deste�i sa�lar. Ayr�ca fare yard�m�yla konsollar
aras�nda kopyalama ve yap��t�rma olana�� sunar. Fare t�klamas�yla pop-up
men�lerin ��kmas�n� sa�layan bir program da i�erir.

%package devel
Summary:	Header files and documentation for writing mouse driven programs
Summary(pl):	Pliki nag��wkowe i dokumentacja do gpm
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
This package allows you to develop your own text-mode programs that take
advantage of the mouse. 

%description -l de devel
Mit diesem Paket k�nnen Sie Ihre eigenen text-orientierten Programme
mit Mausunterst�tzung entwickeln.

%description -l fr devel
Ce paquetage permet de d�velopper des programmes en mode texte tirant
avantage de la souris.

%description -l pl devel
Pliki nag��wkowe i dokumentacja dla gpm. Dzi�ki nim b�dziesz m�g�
pisa� w�asne programy z wykorzystaniem myszki.

%description -l tr devel
Bu paket, fare kullanan yaz�l�mlar geli�tirmenizi sa�layan dosyalar� i�erir.

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
%setup 	-q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%configure \
	--disable-debug \
	--with-curses
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/{rc.d/init.d,sysconfig}

make install-strip DESTDIR=$RPM_BUILD_ROOT

install gpm-root.conf $RPM_BUILD_ROOT/etc
install mouse-test hltest $RPM_BUILD_ROOT%{_bindir}

strip $RPM_BUILD_ROOT/usr/lib/lib*.so.*.*

install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/gpm
install %{SOURCE2} $RPM_BUILD_ROOT/etc/sysconfig/gpm

%ifarch sparc
(echo MOUSETYPE=\"sun\"; echo XEMU3=no) > $RPM_BUILD_ROOT/etc/sysconfig/mouse
%else
(echo "MOUSETYPE="; echo "XEMU3=") > $RPM_BUILD_ROOT/etc/sysconfig/mouse
%endif

gzip -9nf $RPM_BUILD_ROOT%{_datadir}/{info/gpm.info*,man/man{1,8}/*}

%post
/sbin/ldconfig
/sbin/install-info %{_infodir}/gpm.info.gz /etc/info-dir

/sbin/chkconfig --add gpm

if [ -f /var/lock/subsys/gpm ]; then
	/etc/rc.d/init.d/gpm restart >&2
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

%config(noreplace) %{_sysconfdir}/gpm-root.conf
%config(noreplace) %verify(not size mtime md5) /etc/sysconfig/mouse
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) /etc/sysconfig/gpm

%attr(754,root,root) /etc/rc.d/init.d/gpm
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_sbindir}/*

%{_infodir}/gpm.info*
%{_mandir}/man[18]/*
%attr(755,root,root) %{_libdir}/lib*.so.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/gpm.h

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%changelog
* Mon Jun 07 1999 Jan R�korajski <baggins@pld.org.pl>
  [1.17.8-2]
- prefix=/usr

* Sun May  9 1999 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.17.8-1]
- now package is FHS 2.0 compliant.

* Wed Apr 28 1999 Artur Frysiak <wiget@pld.org.pl>
  [1.17-7-3]
- added BuildPrereq: ncurses-devel.

* Mon Apr 19 1999 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.17.7-2]
- added noreplace parameter to %config files,
- recompiles on new rpm.

* Sat Feb 27 1999 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.17.5-1]
- changed base Source url to ftp://animal.unipv.it/pub/gpm/,
- now libgpm is linked with ncurses as a term library,
- removed man group from man pages.

* Sun Jan 31 1999 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
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

* Wed Sep 30 1998 Wojtek �lusarczyk <wojtek@shadow.eu.org>
  [1.13-9d]
- added pl translation.

* Wed Aug 26 1998 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
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
