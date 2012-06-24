Summary:	General Purpose Mouse support for Linux
Summary(de):	Allgemeine Mausunterst�tzung f�r Linux
Summary(fr):	Gestion g�n�rale de la souris pour Linux
Summary(pl):	Wsparcie dla myszki w systemie Linux
Summary(tr):	Genel ama�l� fare deste�i
Summary(ru):	������ ������ � ����� ��� ������� Linux
Summary(uk):	������ ������ � ����� ��� �����̦ Linux
Name:		gpm
Version:	1.19.6
Release:	4
License:	GPL
Group:		Daemons
Group(de):	Server
Group(pl):	Serwery
Source0:	ftp://arcana.linux.it/pub/gpm/%{name}-%{version}.tar.bz2
Source1:	%{name}.init
Source2:	%{name}.sysconfig
Source3:	%{name}-non-english-man-pages.tar.bz2
Patch0:		%{name}-info.patch
Patch1:		%{name}-nops.patch
Patch2:		%{name}-DESTDIR.patch
Patch3:		%{name}-info_fixes.patch
Patch4:		%{name}-root.patch
Patch5:		%{name}-mawk.patch
Patch6:		%{name}-OPEN_MAX.patch
Patch7:		%{name}-limits.patch
Patch8:		%{name}-serialconsole.patch
Patch9:		%{name}-gawk.patch
Requires:	%{name}-libs = %{version}
Prereq:		rc-scripts >= 0.2.0
Prereq:		/sbin/chkconfig
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	gawk
BuildRequires:	bison
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc

%description
GPM adds mouse support to text-based Linux applications such as emacs,
Midnight Commander, and more. It also provides console cut-and-paste
operations using the mouse. Includes a program to allow pop-up menus
to appear at the click of a mouse button.

%description -l de
GPM erm�glicht Maus-Unterst�tzung f�r zeichenorientierte Linux-
Anwendungen wie z.B. emacs und Midnight Commander. Au�erdem sind
Ausschneiden und Einf�gen mit der Maus auf der Konsole m�glich.
Enth�lt ein Programm, da� bei Mausklick ein Pop-up-Men� aufruft.

%description -l fr
GPM ajoute un support souris au applications en mode texte de Linux
comme emacs, Midnight Commander, et bien d'autres. Cela fournit aussi
des op�rations de copier/coller avec la souris sur les consoles.
Comprend un programme pour permettre l'apparition de menus d�roulants
grace � un clic droit avec la souris.

%description -l pl
GPM zapewnia wsparcie dla myszki dla systemu Linux na konsoli
systemowej. Dzi�ki niemu mo�na zaznacza� fragmenty tekstu na konsoli i
wkleja� je w edytowany plik tekstowy. Operacje te s� najcz�ciej
dokonywane przez wci�ni�cie prawego klawisza myszki (operacja
zaznaczania fragmentu tekstu) i nast�pnie wci�ni�cie klawisza
<Shift>+�rodkowego klawisza myszki (operacja wklejania tekstu).

%description -l tr
GPM metin ekranda �al��an Linux uygulamalar�na (emacs, Midnight
Commander ve di�erleri gibi) fare deste�i sa�lar. Ayr�ca fare
yard�m�yla konsollar aras�nda kopyalama ve yap��t�rma olana�� sunar.
Fare t�klamas�yla pop-up men�lerin ��kmas�n� sa�layan bir program da
i�erir.

%description -l ru
GPM ������������ ��������� ���� � ��������� ����������� Linux, �����
��� emacs, Midnight Commander � ������. ����� ������������ ��������
������� � ������� �� ������� � �������������� ����. ��������
���������, ����������� �������� ����������� ���� �� ������� ������
����.

%description -l uk
GPM ��������դ Ц������� ��ۦ � ��������� ��������� Linux, ����� ��
emacs, Midnight Commander �� �����. ����� ��������դ �����æ� ��Ҧ���
�� ������� �� �����̦ � ������������� ��ۦ. ������ ��������, ��
������Ѥ ��������� �������ަ ���� ���������� ������ ��ۦ.

%package libs
Summary:	GPM libraries
Summary(pl):	Biblioteki GPM
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	����������
Group(uk):	��̦�����
Conflicts:	gpm < 1.19.3-7
Obsoletes:	libgpm1

%description libs
This package contains library files neccessary to run most of
mouse-aware applications.

%description -l pl libs
Ten pakiet zawiera biblioteki potrzebne do uruchomienia wi�kszo�ci
program�w ze wsparciem do obs�ugi myszki.

%package devel
Summary:	Header files and documentation for writing mouse driven programs
Summary(pl):	Pliki nag��wkowe i dokumentacja do gpm
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	����������/����������
Group(uk):	��������/��̦�����
Requires:	%{name}-libs = %{version}
Obsoletes:	libgpm1-devel

%description devel
This package allows you to develop your own text-mode programs that
take advantage of the mouse.

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
Bu paket, fare kullanan yaz�l�mlar geli�tirmenizi sa�layan dosyalar�
i�erir.

%description -l ru
GPM ������������ ��������� ���� � ��������� ����������� Linux, �����
��� emacs, Midnight Commander � ������. ����� ������������ ��������
������� � ������� �� ������� � �������������� ����. ��������
���������, ����������� �������� ����������� ���� �� ������� ������
����.

%description -l uk
GPM ��������դ Ц������� ��ۦ � ��������� ��������� Linux, ����� ��
emacs, Midnight Commander �� �����. ����� ��������դ �����æ� ��Ҧ���
�� ������� �� �����̦ � ������������� ��ۦ. ������ ��������, ��
������Ѥ ��������� �������ަ ���� ���������� ������ ��ۦ.

%package static
Summary:	Static gpm library
Summary(pl):	Biblioteki statyczne gpm
Summary(ru):	����������� ���������� ��� ���������� ��������, ������������ ���� �����������
Summary(uk):	�������� ¦�̦����� ��� �������� �������, �� �������������� ����
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	����������/����������
Group(uk):	��������/��̦�����
Requires:	%{name}-devel = %{version}

%description static
Static gpm library.

%description -l pl static
Biblioteki statyczne gpm.

%description -l ru static
���� ����� ��������� ������������� ��������� ����������, ������������
����.

%description -l uk static
��� ����� ������Ѥ ���������� ������צ ��������, �� ��������������
����.

%prep
%setup 	-q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
#%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1

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

install conf/gpm-root.conf $RPM_BUILD_ROOT%{_sysconfdir}
install src/mouse-test src/hltest $RPM_BUILD_ROOT%{_bindir}

install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/gpm
install %{SOURCE2} $RPM_BUILD_ROOT/etc/sysconfig/mouse
bzip2 -dc %{SOURCE3} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

gzip -9nf BUGS ChangeLog Changes README TODO doc/FAQ doc/README* conf/*.conf

%clean
rm -rf $RPM_BUILD_ROOT

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

%files
%defattr(644,root,root,755)
%doc *.gz doc/*.gz conf/*.conf*
%config(noreplace) %{_sysconfdir}/gpm-root.conf
%attr(754,root,root) /etc/rc.d/init.d/gpm
%config(noreplace) %verify(not size mtime md5) /etc/sysconfig/mouse

%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_sbindir}/*

%{_infodir}/gpm.info*
%{_mandir}/man[178]/*
%lang(es) %{_mandir}/es/man[178]/*
%lang(hu) %{_mandir}/hu/man[178]/*
%lang(pl) %{_mandir}/pl/man[178]/*

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
