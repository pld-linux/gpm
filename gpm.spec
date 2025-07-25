#
# TODO:
# - make modprobe of kernel mouse modules for 2.5 (TODO: revise it)
#
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
Version:	1.20.7
Release:	1
Epoch:		1
License:	GPL v2+
Group:		Daemons
Source0:	http://www.nico.schottelius.org/software/gpm/archives/%{name}-%{version}.tar.lzma
# Source0-md5:	fa8a6fe09826896625ca557ac5e42ed7
Source1:	%{name}.init
Source2:	%{name}.sysconfig
Source3:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source3-md5:	893cf1468604523c6e9f9257a5671688
Source4:	%{name}.service
Patch0:		%{name}-info.patch
Patch1:		%{name}-DESTDIR.patch
Patch2:		%{name}-gawk.patch
Patch3:		%{name}-nodebug.patch
Patch4:		%{name}-dont_display_stupid_error_messages.patch
Patch5:		%{name}-ncursesw.patch
Patch6:		close-fds.patch
Patch7:		format-string.patch
Patch8:		glibc.patch
Patch9:		gcc10.patch
URL:		http://www.nico.schottelius.org/software/gpm/
BuildRequires:	autoconf >= 2.61
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	gawk
BuildRequires:	libtool
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	rpm >= 4.4.9-56
BuildRequires:	rpmbuild(macros) >= 1.626
BuildRequires:	sed >= 4.0
BuildRequires:	tar >= 1:1.22
BuildRequires:	texinfo
BuildRequires:	xz
Requires(post,preun):	/sbin/chkconfig
Requires(post,preun,postun):	systemd-units >= 38
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Requires:	rc-scripts >= 0.4.3.0
Requires:	systemd-units >= 38
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

%package emacs
Summary:	Emacs mode for GPM
Summary(pl.UTF-8):	Tryb GPM dla Emacsa
Group:		Development/Tools
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description emacs
Emacs mode files for GPM.

%description emacs -l pl.UTF-8
Pliki trybu GPM dla Emacsa.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%{!?debug:%patch3 -p1}
%patch -P4 -p1
%patch -P5 -p1
%patch -P6 -p1
%patch -P7 -p1
%patch -P8 -p1
%patch -P9 -p1

%{__sed} -i -e '1s#/usr/bin/awk#/bin/awk#' doc/manpager

# generate configure.ac, but we want to autotoolize ourselves
%{__sed} -i -e '/ACLOCAL/iexit 0' autogen.sh
./autogen.sh

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%configure \
	CPPFLAGS="%{rpmcppflags} -I/usr/include/ncursesw -I headers" \
	--with-curses

%{__make} \
	LDFLAGS="%{rpmcflags} %{rpmldflags}" \
	DEFS="-DHAVE_CONFIG_H -D_GNU_SOURCE"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/etc/{rc.d/init.d,sysconfig},%{systemdunitdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -p conf/gpm-root.conf $RPM_BUILD_ROOT%{_sysconfdir}

# demo program, not really useful
%{__rm} $RPM_BUILD_ROOT%{_bindir}/hltest

install -p %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/gpm
install -p %{SOURCE2} $RPM_BUILD_ROOT/etc/sysconfig/mouse
cp -a %{SOURCE4} $RPM_BUILD_ROOT%{systemdunitdir}/gpm.service

bzip2 -dc %{SOURCE3} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}
%{__rm} $RPM_BUILD_ROOT%{_mandir}/README.gpm-non-english-man-pages
%{__rm} $RPM_BUILD_ROOT%{_mandir}/gpm-man.patch

install -d $RPM_BUILD_ROOT%{_datadir}/emacs/site-lisp
install -p contrib/emacs/*.el $RPM_BUILD_ROOT%{_datadir}/emacs/site-lisp

# for rpm autodeps
chmod +x $RPM_BUILD_ROOT%{_libdir}/libgpm.so.*

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

/sbin/chkconfig --add gpm
%service gpm restart "gpm daemon"
%systemd_post gpm.service

%preun
if [ "$1" = "0" ]; then
	%service gpm stop
	/sbin/chkconfig --del gpm
fi
%systemd_preun gpm.service

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1
%systemd_reload

%triggerpostun -- %{name} < 1:1.20.6-11
if [ -f /etc/sysconfig/mouse ]; then
	. /etc/sysconfig/mouse
	OPTIONS=""
	if [ -n "$DEVICE" ]; then
		OPTIONS="-m $DEVICE"
	else
		OPTIONS="-m /dev/input/mice"
	fi
	if [ -n "$MOUSETYPE" ]; then
		OPTIONS="$OPTIONS -t $MOUSETYPE"
	else
		OPTIONS="$OPTIONS -t imps2"
	fi
	[ -n "$BAUD_RATE" ] && OPTIONS="$OPTIONS -b $BAUD_RATE"
	[ -n "$CLEAR_LINES" ] && OPTIONS="$OPTIONS -o $CLEAR_LINES"
	[ -n "$BUTTON_SEQ" ] && OPTIONS="$OPTIONS -B $BUTTON_SEQ"
	[ -n "$TAP_BUTTON" ] && OPTIONS="$OPTIONS -g $TAP_BUTTON"
	[ -n "$ACCEL" ] && OPTIONS="$OPTIONS -a $ACCEL"
	[ -n "$DELTA" ] && OPTIONS="$OPTIONS -d $DELTA"
	[ -n "$INTERVAL" ] && OPTIONS="$OPTIONS -i $INTERVAL"
	[ -n "$RESP" ] && OPTIONS="$OPTIONS -r $RESP"
	[ -n "$SAMPLE_RATE" ] && OPTIONS="$OPTIONS -s $SAMPLE_RATE"
	[ -n "$CHARSET" ] && OPTIONS="$OPTIONS -l \\\"$(echo "$CHARSET" | sed -e 's,",\\",g')\\\""
	[ "$BUTTON_COUNT" = "2" ] && OPTIONS="$OPTIONS -2"
	[ "$BUTTON_COUNT" = "3" ] && OPTIONS="$OPTIONS -3"
	if [ -n "$POINTER_VIS" ] && [ "$POINTER_VIS" != "no" ]; then
		OPTIONS="$OPTIONS -p"
	fi
	if [ -n "$REPEATER" ] && [ "$REPEATER" != "no" ]; then
		OPTIONS="$OPTIONS -R"
	fi
	%{__cp} -f /etc/sysconfig/mouse{,.rpmsave}
	[ -f /etc/sysconfig/mouse.rpmnew ] && %{__cp} -f /etc/sysconfig/mouse{.rpmnew,}
	echo >>/etc/sysconfig/mouse
	echo "# Added by rpm trigger" >>/etc/sysconfig/mouse
	echo "GPM_OPTIONS=\"$OPTIONS\"" >>/etc/sysconfig/mouse
fi
%systemd_trigger gpm.service

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README README.gpm2 TODO doc/FAQ doc/README* doc/changelog conf/*.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/gpm-root.conf
%attr(754,root,root) /etc/rc.d/init.d/gpm
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/mouse
%{systemdunitdir}/gpm.service

%attr(755,root,root) %{_bindir}/display-buttons
%attr(755,root,root) %{_bindir}/display-coords
%attr(755,root,root) %{_bindir}/disable-paste
%attr(755,root,root) %{_bindir}/get-versions
%attr(755,root,root) %{_bindir}/gpm-root
%attr(755,root,root) %{_bindir}/mev
%attr(755,root,root) %{_bindir}/mouse-test
%attr(755,root,root) %{_sbindir}/gpm

%{_infodir}/gpm.info*
%{_mandir}/man1/gpm-root.1*
%{_mandir}/man1/mev.1*
%{_mandir}/man1/mouse-test.1*
%{_mandir}/man7/gpm-types.7*
%{_mandir}/man8/gpm.8*
%lang(es) %{_mandir}/es/man[178]/*
%lang(hu) %{_mandir}/hu/man[178]/*
%lang(pl) %{_mandir}/pl/man[178]/*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgpm.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgpm.so.2

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgpm.so
%{_includedir}/gpm.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libgpm.a

%files emacs
%defattr(644,root,root,755)
%{_datadir}/emacs/site-lisp/*.el*
