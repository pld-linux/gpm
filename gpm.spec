Summary:	General Purpose Mouse support for Linux
Summary(de):	Allgemeine Mausunterst�tzung f�r Linux
Summary(fr):	Gestion g�n�rale de la souris pour Linux
Summary(pl):	Wsparcie dla myszki w systemie Linux
Summary(tr):	Genel ama�l� fare deste�i
Name:		gpm
Version:	1.19.1
Release:	3
License:	GPL
Group:		Daemons
Group(pl):	Serwery
Source0:	ftp://animal.unipv.it/pub/gpm/%{name}-%{version}.tar.gz
Source1:	gpm.init
Source2:	gpm.sysconfig
Patch0:		gpm-info.patch
Patch1:		gpm-nops.patch
Patch2:		gpm-non-root.patch
Patch3:		gpm-DESTDIR.patch
Patch4:		gpm-info_fixes.patch
Patch5:		gpm-root.patch
Prereq:		/sbin/chkconfig
Prereq:		/usr/sbin/fix-info-dir
Prereq:		/sbin/ldconfig
Requires:	rc-scripts >= 0.2.0
BuildRequires:	ncurses-devel >= 5.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc

%description
GPM adds mouse support to text-based Linux applications such as emacs,
Midnight Commander, and more. It also provides console cut-and-paste
operations using the mouse. Includes a program to allow pop-up menus to
appear at the click of a mouse button.

%description -l de
GPM erm�glicht Maus-Unterst�tzung f�r zeichenorientierte Linux- Anwendungen
wie z.B. emacs und Midnight Commander. Au�erdem sind Ausschneiden und
Einf�gen mit der Maus auf der Konsole m�glich. Enth�lt ein Programm, da�
bei Mausklick ein Pop-up-Men� aufruft.

%description -l fr
GPM ajoute un support souris au applications en mode texte de Linux comme
emacs, Midnight Commander, et bien d'autres. Cela fournit aussi des
op�rations de copier/coller avec la souris sur les consoles. Comprend un
programme pour permettre l'apparition de menus d�roulants grace � un clic
droit avec la souris.

%description -l pl
GPM zapewnia wsparcie dla myszki dla systemu Linux na konsoli systemowej.
Dzi�ki niemu mo�na zaznacza� fragmenty tekstu na konsoli i wkleja� je w
edytowany plik tekstowy. Operacje te s� najcz�ciej dokonywane przez
wci�ni�cie prawego klawisza myszki (operacja zaznaczania fragmentu tekstu)
i nast�pnie wci�ni�cie klawisza <Shift>+�rodkowego klawisza myszki
(operacja wklejania tekstu).

%description -l tr
GPM metin ekranda �al��an Linux uygulamalar�na (emacs, Midnight Commander
ve di�erleri gibi) fare deste�i sa�lar. Ayr�ca fare yard�m�yla konsollar
aras�nda kopyalama ve yap��t�rma olana�� sunar. Fare t�klamas�yla pop-up
men�lerin ��kmas�n� sa�layan bir program da i�erir.

%package devel
Summary:	Header files and documentation for writing mouse driven programs
Summary(pl):	Pliki nag��wkowe i dokumentacja do gpm
Group:		Development/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
This package allows you to develop your own text-mode programs that take
advantage of the mouse.

%description -l de devel
Mit diesem Paket k�nnen Sie Ihre eigenen text-orientierten Programme mit
Mausunterst�tzung entwickeln.

%description -l fr devel
Ce paquetage permet de d�velopper des programmes en mode texte tirant
avantage de la souris.

%description -l pl devel
Pliki nag��wkowe i dokumentacja dla gpm. Dzi�ki nim b�dziesz m�g� pisa�
w�asne programy z wykorzystaniem myszki.

%description -l tr devel
Bu paket, fare kullanan yaz�l�mlar geli�tirmenizi sa�layan dosyalar�
i�erir.

%package static
Summary:	Static gpm library
Summary(pl):	Biblioteki statyczne gpm
Group:		Development/Libraries
Group(fr):	Development/Librairies
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
%patch4 -p1
%patch5 -p1

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

install gpm-root.conf $RPM_BUILD_ROOT%{_sysconfdir}
install mouse-test hltest $RPM_BUILD_ROOT%{_bindir}

strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/lib*.so.*.*

install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/gpm
install %{SOURCE2} $RPM_BUILD_ROOT/etc/sysconfig/mouse

gzip -9nf $RPM_BUILD_ROOT%{_datadir}/{info/gpm.info*,man/man{1,8}/*} \
	README* *.conf

%post
/sbin/ldconfig
%{_sbindir}/fix-info-dir -c %{_infodir} >/dev/null 2>&1

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
/sbin/ldconfig
/usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

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
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%{_infodir}/gpm.info*
%{_mandir}/man[18]/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
