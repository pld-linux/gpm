
%define		_rc	rc1
Summary:	General Purpose Mouse support for Linux
Summary(de):	Allgemeine MausunterstЭtzung fЭr Linux
Summary(es):	Soporte para ratСn en terminales modo texto
Summary(fr):	Gestion gИnИrale de la souris pour Linux
Summary(ja):	Linux╔Ё╔С╔╫║╪╔К╓н╓©╓А╓н╔ч╔╕╔╧║╕╔╣║╪╔п║ё
Summary(pl):	Wsparcie dla myszki w systemie Linux
Summary(pt_BR):	Suporte para mouse em terminais modo texto
Summary(ru):	Сервер работы с мышью для консоли Linux
Summary(tr):	Genel amaГlЩ fare desteПi
Summary(uk):	Сервер роботи з мишою для консол╕ Linux
Name:		gpm
Version:	1.20.1
Release:	%{_rc}.2
License:	GPL
Group:		Daemons
Source0:	ftp://arcana.linux.it/pub/gpm/%{name}-%{version}%{_rc}.tar.bz2
Source1:	%{name}.init
Source2:	%{name}.sysconfig
Source3:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
Patch0:		%{name}-info.patch
Patch1:		%{name}-OPEN_MAX.patch
Patch2:		%{name}-DESTDIR.patch
Patch3:		%{name}-root.patch
Patch4:		%{name}-serialconsole.patch
Patch5:		%{name}-gawk.patch
Patch6:		%{name}-mawk.patch
Patch7:		%{name}-nodebug.patch
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	gawk
BuildRequires:	bison
BuildRequires:	autoconf
BuildRequires:	automake
PreReq:		rc-scripts >= 0.2.0
PreReq:		/sbin/chkconfig
Requires:	%{name}-libs = %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc

%description
GPM adds mouse support to text-based Linux applications such as emacs,
Midnight Commander, and more. It also provides console cut-and-paste
operations using the mouse. Includes a program to allow pop-up menus
to appear at the click of a mouse button.

%description -l de
GPM ermЖglicht Maus-UnterstЭtzung fЭr zeichenorientierte Linux-
Anwendungen wie z.B. emacs und Midnight Commander. Auъerdem sind
Ausschneiden und EinfЭgen mit der Maus auf der Konsole mЖglich.
EnthДlt ein Programm, daъ bei Mausklick ein Pop-up-MenЭ aufruft.

%description -l es
Gpm acrecienta soporte a ratСn para aplicaciones Linux basadas en modo
texto, como emacs, Midnight Commander, y otros. Ofrece aЗn, soporte a
pantalla y operaciones de cortar-pegar usando el ratСn.

%description -l fr
GPM ajoute un support souris au applications en mode texte de Linux
comme emacs, Midnight Commander, et bien d'autres. Cela fournit aussi
des opИrations de copier/coller avec la souris sur les consoles.
Comprend un programme pour permettre l'apparition de menus dИroulants
grace Ю un clic droit avec la souris.

%description -l ja
gpm ╓оemacs╔╗╔г╔ё╔©╓ДMidnight
CommanderеЫ╓н╔ф╔╜╔╧╔х╔ы║╪╔╧╓гф╟╨Н╓╧╓К╔╒╔в╔Й╔╠║╪╔╥╔Г╔С
╓кбп╓╧╓К╔ч╔╕╔╧╔╣╔щ║╪╔х╓Р╧т╓╕╔я╔ц╔╠║╪╔╦║ё

%description -l pl
GPM zapewnia wsparcie dla myszki w systemie Linux na konsoli
systemowej. DziЙki niemu mo©na zaznaczaФ fragmenty tekstu na konsoli i
wklejaФ je w edytowany plik tekstowy. Operacje te s╠ najczЙ╤ciej
dokonywane przez przytrzymanie lewego klawisza myszki (operacja
zaznaczania fragmentu tekstu) i nastЙpnie wci╤niЙcie ╤rodkowego
klawisza myszki (operacja wklejania tekstu).

%description -l pt_BR
Gpm acrescenta suporte a mouse para aplicaГУes Linux baseadas em modo
texto, como emacs, Midnight Commander, e outros. Fornece ainda, para a
console, operaГУes de cortar e colar usando o mouse.

%description -l ru
GPM обеспечивает поддержку мыши в текстовых приложениях Linux, таких
как emacs, Midnight Commander и других. Также обеспечивает операции
вырезки и вставки на консоли с использованием мыши. Включает
программу, позволяющую вызывать всплывающие меню по нажатию кнопки
мыши.

%description -l tr
GPM metin ekranda ГalЩЧan Linux uygulamalarЩna (emacs, Midnight
Commander ve diПerleri gibi) fare desteПi saПlar. AyrЩca fare
yardЩmЩyla konsollar arasЩnda kopyalama ve yapЩЧtЩrma olanaПЩ sunar.
Fare tЩklamasЩyla pop-up menЭlerin ГЩkmasЩnЩ saПlayan bir program da
iГerir.

%description -l uk
GPM забезпечу╓ п╕дтримку миш╕ в текстових програмах Linux, таких як
emacs, Midnight Commander та ╕нших. Також забезпечу╓ операц╕╖ вир╕зки
та вставки на консол╕ з використанням миш╕. М╕стить програму, що
дозволя╓ викликати спливаюч╕ меню натискаючи кнопку миш╕.

%package libs
Summary:	GPM libraries
Summary(pl):	Biblioteki GPM
Group:		Libraries
Conflicts:	gpm < 1.19.3-7
Obsoletes:	libgpm1

%description libs
This package contains library files neccessary to run most of
mouse-aware applications.

%description libs -l pl
Ten pakiet zawiera biblioteki potrzebne do uruchomienia wiЙkszo╤ci
programСw ze wsparciem do obsЁugi myszki.

%package devel
Summary:	Header files and documentation for writing mouse driven programs
Summary(es):	Bibliotecas y archivos de inclusiСn para desarrollar programas que utilicen ratСn
Summary(ja):	gpm╓нЁ╚х╞╔И╔╓╔ж╔И╔Й
Summary(pl):	Pliki nagЁСwkowe i dokumentacja do gpm
Summary(pt_BR):	Bibliotecas e arquivos de inclusЦo para desenvolver programas que utilizam mouse
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}
Obsoletes:	libgpm1-devel

%description devel
This package allows you to develop your own text-mode programs that
take advantage of the mouse.

%description devel -l de
Mit diesem Paket kЖnnen Sie Ihre eigenen text-orientierten Programme
mit MausunterstЭtzung entwickeln.

%description devel -l es
Este paquete permite el desarrollo de programas en modo texto que usan
ratСn.

%description devel -l fr
Ce paquetage permet de dИvelopper des programmes en mode texte tirant
avantage de la souris.

%description devel -l ja

gpm-devel╓оgpm╓РмЬмя╓╥╓©╔╒╔в╔Й╔╠║╪╔╥╔Г╔СЁ╚х╞╓ки╛мв╓й╔И╔╓╔ж╔И╔Й╓Д╔ь╔ц╔ю╔у╔║╔╓╔К
╓Р╔я╔ц╔╠║╪╔╦╔С╔╟╓╥╓©╓Б╓н║ё

%description devel -l pl
Pliki nagЁСwkowe i dokumentacja dla gpm. DziЙki nim bЙdziesz mСgЁ
pisaФ wЁasne programy z wykorzystaniem myszki.

%description devel -l pt_BR
Este pacote permite o desenvolvimento de programas em modo texto que
usam mouse.

%description devel -l ru
GPM обеспечивает поддержку мыши в текстовых приложениях Linux, таких
как emacs, Midnight Commander и других. Также обеспечивает операции
вырезки и вставки на консоли с использованием мыши. Включает
программу, позволяющую вызывать всплывающие меню по нажатию кнопки
мыши.

%description devel -l tr
Bu paket, fare kullanan yazЩlЩmlar geliЧtirmenizi saПlayan dosyalarЩ
iГerir.

%description devel -l uk
GPM забезпечу╓ п╕дтримку миш╕ в текстових програмах Linux, таких як
emacs, Midnight Commander та ╕нших. Також забезпечу╓ операц╕╖ вир╕зки
та вставки на консол╕ з використанням миш╕. М╕стить програму, що
дозволя╓ викликати спливаюч╕ меню натискаючи кнопку миш╕.

%package static
Summary:	Static gpm library
Summary(es):	Static library for developing mouse driven programs
Summary(pl):	Biblioteki statyczne gpm
Summary(pt_BR):	Biblioteca de desenvolvimento estАtica do gpm
Summary(ru):	Статическая библиотека для разработки программ, использующих мышь Статическая
Summary(uk):	Статична б╕бл╕отека для розробки програм, що використовують мишу
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static gpm library.

%description static -l es
Este paquete permite el desarrollo de programas en modo texto que usan
ratСn.

%description static -l pl
Biblioteki statyczne gpm.

%description static -l pt_BR
Este pacote contИm uma biblioteca estАtica para ser usada no
desenvolvimento de programas modo texto que usem o mouse e que desejam
linkar a biblioteca gpm estaticamente.

%description static -l ru
Этот пакет позволяет разрабатывать текстовые приложения, использующие
мышь.

%description static -l uk
Цей пакет дозволя╓ розробляти текстов╕ програми, що використовують
мишу.

%prep
%setup -q -n %{name}-cvs
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
#%patch6 -p1
%{!?debug:%patch7 -p1}

%build
aclocal
%{__autoconf}
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

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

/sbin/chkconfig --add gpm
if [ -f /var/lock/subsys/gpm ]; then
	/etc/rc.d/init.d/gpm restart >&2
else
	echo "Run \"/etc/rc.d/init.d/gpm start\" to start gpm daemon."
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

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc BUGS ChangeLog Changes README TODO doc/FAQ doc/README* conf/*.conf
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/gpm-root.conf
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
