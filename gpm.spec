Summary:	General Purpose Mouse support for Linux
Summary(de):	Allgemeine Mausunterstützung für Linux
Summary(fr):	Gestion générale de la souris pour Linux
Summary(pl):	Wsparcie dla myszki w systemie Linux
Summary(tr):	Genel amaçlý fare desteði
Summary(ru):	óÅÒ×ÅÒ ÒÁÂÏÔÙ Ó ÍÙÛØÀ ÄÌÑ ËÏÎÓÏÌÉ Linux
Summary(uk):	óÅÒ×ÅÒ ÒÏÂÏÔÉ Ú ÍÉÛÏÀ ÄÌÑ ËÏÎÓÏÌ¦ Linux
Name:		gpm
Version:	1.19.4
Release:	3
License:	GPL
Group:		Daemons
Group(de):	Server
Group(pl):	Serwery
Source0:	ftp://arcana.linux.it/pub/gpm/%{name}-%{version}.tar.bz2
Source1:	%{name}.init
Source2:	%{name}.sysconfig
Patch0:		%{name}-info.patch
Patch1:		%{name}-nops.patch
Patch2:		%{name}-non-root.patch
Patch3:		%{name}-DESTDIR.patch
Patch4:		%{name}-info_fixes.patch
Patch5:		%{name}-root.patch
Patch6:		%{name}-mawk.patch
Patch7:		%{name}-OPEN_MAX.patch
Patch8:		%{name}-limits.patch
Patch9:		%{name}-checkdevfsbug.patch
Patch10:	%{name}-serialconsole.patch
Requires:	%{name}-libs = %{version}
Prereq:		rc-scripts >= 0.2.0
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	gawk
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc

%description
GPM adds mouse support to text-based Linux applications such as emacs,
Midnight Commander, and more. It also provides console cut-and-paste
operations using the mouse. Includes a program to allow pop-up menus
to appear at the click of a mouse button.

%description -l de
GPM ermöglicht Maus-Unterstützung für zeichenorientierte Linux-
Anwendungen wie z.B. emacs und Midnight Commander. Außerdem sind
Ausschneiden und Einfügen mit der Maus auf der Konsole möglich.
Enthält ein Programm, daß bei Mausklick ein Pop-up-Menü aufruft.

%description -l fr
GPM ajoute un support souris au applications en mode texte de Linux
comme emacs, Midnight Commander, et bien d'autres. Cela fournit aussi
des opérations de copier/coller avec la souris sur les consoles.
Comprend un programme pour permettre l'apparition de menus déroulants
grace à un clic droit avec la souris.

%description -l pl
GPM zapewnia wsparcie dla myszki dla systemu Linux na konsoli
systemowej. Dziêki niemu mo¿na zaznaczaæ fragmenty tekstu na konsoli i
wklejaæ je w edytowany plik tekstowy. Operacje te s± najczê¶ciej
dokonywane przez wci¶niêcie prawego klawisza myszki (operacja
zaznaczania fragmentu tekstu) i nastêpnie wci¶niêcie klawisza
<Shift>+¶rodkowego klawisza myszki (operacja wklejania tekstu).

%description -l tr
GPM metin ekranda çalýþan Linux uygulamalarýna (emacs, Midnight
Commander ve diðerleri gibi) fare desteði saðlar. Ayrýca fare
yardýmýyla konsollar arasýnda kopyalama ve yapýþtýrma olanaðý sunar.
Fare týklamasýyla pop-up menülerin çýkmasýný saðlayan bir program da
içerir.

%description -l ru
GPM ÏÂÅÓÐÅÞÉ×ÁÅÔ ÐÏÄÄÅÒÖËÕ ÍÙÛÉ × ÔÅËÓÔÏ×ÙÈ ÐÒÉÌÏÖÅÎÉÑÈ Linux, ÔÁËÉÈ
ËÁË emacs, Midnight Commander É ÄÒÕÇÉÈ. ôÁËÖÅ ÏÂÅÓÐÅÞÉ×ÁÅÔ ÏÐÅÒÁÃÉÉ
×ÙÒÅÚËÉ É ×ÓÔÁ×ËÉ ÎÁ ËÏÎÓÏÌÉ Ó ÉÓÐÏÌØÚÏ×ÁÎÉÅÍ ÍÙÛÉ. ÷ËÌÀÞÁÅÔ
ÐÒÏÇÒÁÍÍÕ, ÐÏÚ×ÏÌÑÀÝÕÀ ×ÙÚÙ×ÁÔØ ×ÓÐÌÙ×ÁÀÝÉÅ ÍÅÎÀ ÐÏ ÎÁÖÁÔÉÀ ËÎÏÐËÉ
ÍÙÛÉ.

%description -l uk
GPM ÚÁÂÅÚÐÅÞÕ¤ Ð¦ÄÔÒÉÍËÕ ÍÉÛ¦ × ÔÅËÓÔÏ×ÉÈ ÐÒÏÇÒÁÍÁÈ Linux, ÔÁËÉÈ ÑË
emacs, Midnight Commander ÔÁ ¦ÎÛÉÈ. ôÁËÏÖ ÚÁÂÅÚÐÅÞÕ¤ ÏÐÅÒÁÃ¦§ ×ÉÒ¦ÚËÉ
ÔÁ ×ÓÔÁ×ËÉ ÎÁ ËÏÎÓÏÌ¦ Ú ×ÉËÏÒÉÓÔÁÎÎÑÍ ÍÉÛ¦. í¦ÓÔÉÔØ ÐÒÏÇÒÁÍÕ, ÝÏ
ÄÏÚ×ÏÌÑ¤ ×ÉËÌÉËÁÔÉ ÓÐÌÉ×ÁÀÞ¦ ÍÅÎÀ ÎÁÔÉÓËÁÀÞÉ ËÎÏÐËÕ ÍÉÛ¦.

%package libs
Summary:	GPM libraries
Summary(pl):	Biblioteki GPM
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	âÉÂÌÉÏÔÅËÉ
Group(uk):	â¦ÂÌ¦ÏÔÅËÉ

%description libs
This package contains library files neccessary to run most of
mouse-aware applications.

%description -l pl libs
Ten pakiet zawiera biblioteki potrzebne do uruchomienia wiêkszo¶ci
programów ze wsparciem do obs³ugi myszki.

%package devel
Summary:	Header files and documentation for writing mouse driven programs
Summary(pl):	Pliki nag³ówkowe i dokumentacja do gpm
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	òÁÚÒÁÂÏÔËÁ/âÉÂÌÉÏÔÅËÉ
Group(uk):	òÏÚÒÏÂËÁ/â¦ÂÌ¦ÏÔÅËÉ
Requires:	%{name}-libs = %{version}

%description devel
This package allows you to develop your own text-mode programs that
take advantage of the mouse.

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
Bu paket, fare kullanan yazýlýmlar geliþtirmenizi saðlayan dosyalarý
içerir.

%description -l ru
GPM ÏÂÅÓÐÅÞÉ×ÁÅÔ ÐÏÄÄÅÒÖËÕ ÍÙÛÉ × ÔÅËÓÔÏ×ÙÈ ÐÒÉÌÏÖÅÎÉÑÈ Linux, ÔÁËÉÈ
ËÁË emacs, Midnight Commander É ÄÒÕÇÉÈ. ôÁËÖÅ ÏÂÅÓÐÅÞÉ×ÁÅÔ ÏÐÅÒÁÃÉÉ
×ÙÒÅÚËÉ É ×ÓÔÁ×ËÉ ÎÁ ËÏÎÓÏÌÉ Ó ÉÓÐÏÌØÚÏ×ÁÎÉÅÍ ÍÙÛÉ. ÷ËÌÀÞÁÅÔ
ÐÒÏÇÒÁÍÍÕ, ÐÏÚ×ÏÌÑÀÝÕÀ ×ÙÚÙ×ÁÔØ ×ÓÐÌÙ×ÁÀÝÉÅ ÍÅÎÀ ÐÏ ÎÁÖÁÔÉÀ ËÎÏÐËÉ
ÍÙÛÉ.

%description -l uk
GPM ÚÁÂÅÚÐÅÞÕ¤ Ð¦ÄÔÒÉÍËÕ ÍÉÛ¦ × ÔÅËÓÔÏ×ÉÈ ÐÒÏÇÒÁÍÁÈ Linux, ÔÁËÉÈ ÑË
emacs, Midnight Commander ÔÁ ¦ÎÛÉÈ. ôÁËÏÖ ÚÁÂÅÚÐÅÞÕ¤ ÏÐÅÒÁÃ¦§ ×ÉÒ¦ÚËÉ
ÔÁ ×ÓÔÁ×ËÉ ÎÁ ËÏÎÓÏÌ¦ Ú ×ÉËÏÒÉÓÔÁÎÎÑÍ ÍÉÛ¦. í¦ÓÔÉÔØ ÐÒÏÇÒÁÍÕ, ÝÏ
ÄÏÚ×ÏÌÑ¤ ×ÉËÌÉËÁÔÉ ÓÐÌÉ×ÁÀÞ¦ ÍÅÎÀ ÎÁÔÉÓËÁÀÞÉ ËÎÏÐËÕ ÍÉÛ¦.

%package static
Summary:	Static gpm library
Summary(pl):	Biblioteki statyczne gpm
Summary(ru):	óÔÁÔÉÞÅÓËÁÑ ÂÉÂÌÉÏÔÅËÁ ÄÌÑ ÒÁÚÒÁÂÏÔËÉ ÐÒÏÇÒÁÍÍ, ÉÓÐÏÌØÚÕÀÝÉÈ ÍÙÛØ óÔÁÔÉÞÅÓËÁÑ
Summary(uk):	óÔÁÔÉÞÎÁ Â¦ÂÌ¦ÏÔÅËÁ ÄÌÑ ÒÏÚÒÏÂËÉ ÐÒÏÇÒÁÍ, ÝÏ ×ÉËÏÒÉÓÔÏ×ÕÀÔØ ÍÉÛÕ
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	òÁÚÒÁÂÏÔËÁ/âÉÂÌÉÏÔÅËÉ
Group(uk):	òÏÚÒÏÂËÁ/â¦ÂÌ¦ÏÔÅËÉ
Requires:	%{name}-devel = %{version}

%description static
Static gpm library.

%description -l pl static
Biblioteki statyczne gpm.

%description -l ru static
üÔÏÔ ÐÁËÅÔ ÐÏÚ×ÏÌÑÅÔ ÒÁÚÒÁÂÁÔÙ×ÁÔØ ÔÅËÓÔÏ×ÙÅ ÐÒÉÌÏÖÅÎÉÑ, ÉÓÐÏÌØÚÕÀÝÉÅ
ÍÙÛØ.

%description -l uk static
ãÅÊ ÐÁËÅÔ ÄÏÚ×ÏÌÑ¤ ÒÏÚÒÏÂÌÑÔÉ ÔÅËÓÔÏ×¦ ÐÒÏÇÒÁÍÉ, ÝÏ ×ÉËÏÒÉÓÔÏ×ÕÀÔØ
ÍÉÛÕ.

%prep
%setup 	-q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
#%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1

%build
aclocal
autoconf
%configure \
	--disable-debug \
	--with-curses
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/etc/rc.d/init.d,/etc/sysconfig}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install gpm-root.conf $RPM_BUILD_ROOT%{_sysconfdir}
install mouse-test hltest $RPM_BUILD_ROOT%{_bindir}

install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/gpm
install %{SOURCE2} $RPM_BUILD_ROOT/etc/sysconfig/mouse

gzip -9nf README* *.conf

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

/sbin/chkconfig --add gpm

if [ -f /var/lock/subsys/gpm ]; then
	/etc/rc.d/init.d/gpm restart >&2
fi

%preun
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/gpm ]; then
		/etc/rc.d/init.d/gpm stop >&2
	fi
	/sbin/chkconfig --del gpm
fi

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%post   libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README*gz *.conf*
%config(noreplace) %{_sysconfdir}/gpm-root.conf
%attr(754,root,root) /etc/rc.d/init.d/gpm
%config(noreplace) %verify(not size mtime md5) /etc/sysconfig/mouse

%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_sbindir}/*

%{_infodir}/gpm.info*
%{_mandir}/man[18]/*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
