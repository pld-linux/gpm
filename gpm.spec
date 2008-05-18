# TODO:
# - make modprobe of kernel mouse modules for 2.5
Summary:	General Purpose Mouse support for Linux
Summary(de.UTF-8):	Allgemeine Mausunterstützung für Linux
Summary(es.UTF-8):	Soporte para ratón en terminales modo texto
Summary(fr.UTF-8):	Gestion générale de la souris pour Linux
Summary(ja.UTF-8):	Linuxコンソールのためのマウス・サーバ。
Summary(pl.UTF-8):	Wsparcie dla myszki w systemie Linux
Summary(pt_BR.UTF-8):	Suporte para mouse em terminais modo texto
Summary(ru.UTF-8):	Сервер работы с мышью для консоли Linux
Summary(tr.UTF-8):	Genel amaçlı fare desteği
Summary(uk.UTF-8):	Сервер роботи з мишою для консолі Linux
Name:		gpm
Version:	1.20.3
Release:	1
Epoch:		1
License:	GPL
Group:		Daemons
Source0:	http://linux.schottelius.org/gpm/archives/%{name}-%{version}.tar.bz2
# Source0-md5:	dd6054c488fc36fec327acc5b1f3e7d6
Source1:	%{name}.init
Source2:	%{name}.sysconfig
Source3:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source3-md5:	893cf1468604523c6e9f9257a5671688
Patch0:		%{name}-info.patch
Patch1:		%{name}-OPEN_MAX.patch
Patch2:		%{name}-DESTDIR.patch
Patch3:		%{name}-root.patch
Patch4:		%{name}-serialconsole.patch
Patch5:		%{name}-gawk.patch
Patch6:		%{name}-mawk.patch
Patch7:		%{name}-nodebug.patch
Patch8:		%{name}-dont_display_stupid_error_messages.patch
Patch9:		%{name}-link.patch
Patch10:	%{name}-lib-segv.patch
Patch11:	%{name}-pmake.patch
Patch12:	%{name}-wheel.patch
URL:		http://linux.schottelius.org/gpm/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	gawk
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRequires:	texinfo
Requires(post,preun):	/sbin/chkconfig
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Requires:	rc-scripts >= 0.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GPM adds mouse support to text-based Linux applications such as emacs,
Midnight Commander, and more. It also provides console cut-and-paste
operations using the mouse. Includes a program to allow pop-up menus
to appear at the click of a mouse button.

%description -l de.UTF-8
GPM ermöglicht Maus-Unterstützung für zeichenorientierte Linux-
Anwendungen wie z.B. emacs und Midnight Commander. Außerdem sind
Ausschneiden und Einfügen mit der Maus auf der Konsole möglich.
Enthält ein Programm, daß bei Mausklick ein Pop-up-Menü aufruft.

%description -l es.UTF-8
Gpm acrecienta soporte a ratón para aplicaciones Linux basadas en modo
texto, como emacs, Midnight Commander, y otros. Ofrece aún, soporte a
pantalla y operaciones de cortar-pegar usando el ratón.

%description -l fr.UTF-8
GPM ajoute un support souris au applications en mode texte de Linux
comme emacs, Midnight Commander, et bien d'autres. Cela fournit aussi
des opérations de copier/coller avec la souris sur les consoles.
Comprend un programme pour permettre l'apparition de menus déroulants
grace à un clic droit avec la souris.

%description -l ja.UTF-8
gpm はemacsエディタやMidnight
Commander等のテキストベースで動作するアプリケーション
に対するマウスサポートを行うパッケージ。

%description -l pl.UTF-8
GPM zapewnia wsparcie dla myszki w systemie Linux na konsoli
systemowej. Dzięki niemu można zaznaczać fragmenty tekstu na konsoli i
wklejać je w obrabiany plik tekstowy. Operacje te są najczęściej
dokonywane przez przytrzymanie lewego klawisza myszki (operacja
zaznaczania fragmentu tekstu) i następnie wciśnięcie środkowego
klawisza myszki (operacja wklejania tekstu).

%description -l pt_BR.UTF-8
Gpm acrescenta suporte a mouse para aplicações Linux baseadas em modo
texto, como emacs, Midnight Commander, e outros. Fornece ainda, para a
console, operações de cortar e colar usando o mouse.

%description -l ru.UTF-8
GPM обеспечивает поддержку мыши в текстовых приложениях Linux, таких
как emacs, Midnight Commander и других. Также обеспечивает операции
вырезки и вставки на консоли с использованием мыши. Включает
программу, позволяющую вызывать всплывающие меню по нажатию кнопки
мыши.

%description -l tr.UTF-8
GPM metin ekranda çalışan Linux uygulamalarına (emacs, Midnight
Commander ve diğerleri gibi) fare desteği sağlar. Ayrıca fare
yardımıyla konsollar arasında kopyalama ve yapıştırma olanağı sunar.
Fare tıklamasıyla pop-up menülerin çıkmasını sağlayan bir program da
içerir.

%description -l uk.UTF-8
GPM забезпечує підтримку миші в текстових програмах Linux, таких як
emacs, Midnight Commander та інших. Також забезпечує операції вирізки
та вставки на консолі з використанням миші. Містить програму, що
дозволяє викликати спливаючі меню натискаючи кнопку миші.

%package libs
Summary:	GPM libraries
Summary(pl.UTF-8):	Biblioteki GPM
Group:		Libraries
Obsoletes:	libgpm1
Conflicts:	gpm < 1.19.3-7

%description libs
This package contains library files neccessary to run most of
mouse-aware applications.

%description libs -l pl.UTF-8
Ten pakiet zawiera biblioteki potrzebne do uruchomienia większości
programów ze wsparciem do obsługi myszki.

%package devel
Summary:	Header files and documentation for writing mouse driven programs
Summary(es.UTF-8):	Bibliotecas y archivos de inclusión para desarrollar programas que utilicen ratón
Summary(ja.UTF-8):	gpmの開発ライブラリ
Summary(pl.UTF-8):	Pliki nagłówkowe i dokumentacja do gpm
Summary(pt_BR.UTF-8):	Bibliotecas e arquivos de inclusão para desenvolver programas que utilizam mouse
Group:		Development/Libraries
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Obsoletes:	libgpm1-devel

%description devel
This package allows you to develop your own text-mode programs that
take advantage of the mouse.

%description devel -l de.UTF-8
Mit diesem Paket können Sie Ihre eigenen text-orientierten Programme
mit Mausunterstützung entwickeln.

%description devel -l es.UTF-8
Este paquete permite el desarrollo de programas en modo texto que usan
ratón.

%description devel -l fr.UTF-8
Ce paquetage permet de développer des programmes en mode texte tirant
avantage de la souris.

%description devel -l ja.UTF-8
gpm-develはgpmを利用したアプリケーション開発に必要なライブラリやヘッダファイル
をパッケージングしたもの。

%description devel -l pl.UTF-8
Pliki nagłówkowe i dokumentacja dla gpm. Dzięki nim będziesz mógł
pisać własne programy z wykorzystaniem myszki.

%description devel -l pt_BR.UTF-8
Este pacote permite o desenvolvimento de programas em modo texto que
usam mouse.

%description devel -l ru.UTF-8
GPM обеспечивает поддержку мыши в текстовых приложениях Linux, таких
как emacs, Midnight Commander и других. Также обеспечивает операции
вырезки и вставки на консоли с использованием мыши. Включает
программу, позволяющую вызывать всплывающие меню по нажатию кнопки
мыши.

%description devel -l tr.UTF-8
Bu paket, fare kullanan yazılımlar geliştirmenizi sağlayan dosyaları
içerir.

%description devel -l uk.UTF-8
GPM забезпечує підтримку миші в текстових програмах Linux, таких як
emacs, Midnight Commander та інших. Також забезпечує операції вирізки
та вставки на консолі з використанням миші. Містить програму, що
дозволяє викликати спливаючі меню натискаючи кнопку миші.

%package static
Summary:	Static gpm library
Summary(es.UTF-8):	Static library for developing mouse driven programs
Summary(pl.UTF-8):	Biblioteki statyczne gpm
Summary(pt_BR.UTF-8):	Biblioteca de desenvolvimento estática do gpm
Summary(ru.UTF-8):	Статическая библиотека для разработки программ, использующих мышь Статическая
Summary(uk.UTF-8):	Статична бібліотека для розробки програм, що використовують мишу
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static gpm library.

%description static -l es.UTF-8
Este paquete permite el desarrollo de programas en modo texto que usan
ratón.

%description static -l pl.UTF-8
Biblioteki statyczne gpm.

%description static -l pt_BR.UTF-8
Este pacote contém uma biblioteca estática para ser usada no
desenvolvimento de programas modo texto que usem o mouse e que desejam
linkar a biblioteca gpm estaticamente.

%description static -l ru.UTF-8
Этот пакет позволяет разрабатывать текстовые приложения, использующие
мышь.

%description static -l uk.UTF-8
Цей пакет дозволяє розробляти текстові програми, що використовують
мишу.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
#%patch6 -p1
%{!?debug:%patch7 -p1}
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1

sed -i -e 's#/usr##' doc/manpager

%build
%{__aclocal}
%{__autoconf}
%configure \
	--disable-debug \
	--with-curses
%{__make} \
	LDFLAGS="%{rpmcflags} %{rpmldflags}" \
	DEFS="-DHAVE_CONFIG_H -D_GNU_SOURCE"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/etc/rc.d/init.d,/etc/sysconfig}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install conf/gpm-root.conf $RPM_BUILD_ROOT%{_sysconfdir}
install src/prog/mouse-test src/prog/hltest $RPM_BUILD_ROOT%{_bindir}

install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/gpm
install %{SOURCE2} $RPM_BUILD_ROOT/etc/sysconfig/mouse
bzip2 -dc %{SOURCE3} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

# for rpm autodeps
chmod +x $RPM_BUILD_ROOT%{_libdir}/libgpm.so.*

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

/sbin/chkconfig --add gpm
%service gpm restart "gpm daemon"

%preun
if [ "$1" = "0" ]; then
	%service gpm stop
	/sbin/chkconfig --del gpm
fi

%postun	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc BUGS Changelog Changes README TODO doc/FAQ doc/README* conf/*.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/gpm-root.conf
%attr(754,root,root) /etc/rc.d/init.d/gpm
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/mouse

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
