Summary:	General Purpose Mouse support for Linux
Summary(de):	Allgemeine Mausunterstützung für Linux
Summary(fr):	Gestion générale de la souris pour Linux
Summary(pl):	Wsparcie dla myszki w systemie Linux
Summary(tr):	Genel amaçlý fare desteði
Name:		gpm
Version:	1.17.8
Release:	4
Copyright:	GPL
Group:		Daemons
Group(pl):	Serwery
Source:		ftp://animal.unipv.it/pub/gpm/%{name}-%{version}.tar.gz
Source1:	gpm.init
Source2:	gpm.sysconfig
Patch0:		gpm-info.patch
Patch1:		gpm-nops.patch
Patch2:		gpm-non-root.patch
Patch3:		gpm-DESTDIR.patch
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
%setup 	-q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
LDFLAGS="-s"; export LDFLAGS
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

strip --strip-unneeded $RPM_BUILD_ROOT/usr/lib/lib*.so.*.*

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
