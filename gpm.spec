Summary:     General Purpose Mouse support for Linux
Summary(de): Allgemeine Mausunterstützung für Linux
Summary(fr): Gestion générale de la souris pour Linux
Summary(tr): Genel amaçlý fare desteði
Name:        gpm
Version:     1.13
Release:     9
Copyright:   GPL
Group:       Daemons
Source:      ftp://iride.unipv.it/pub/gpm/%{name}-%{version}.tar.gz
Source1:     gpm.init
Patch0:      gpm-1.12-emacs.patch
Patch1:      gpm-1.12-make.patch
Patch2:      gpm-1.13-with_slang.patch
Prereq:      /sbin/chkconfig /sbin/ldconfig /sbin/install-info
Buildroot:   /tmp/%{name}-%{version}-root

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

%description -l tr
GPM metin ekranda çalýþan Linux uygulamalarýna (emacs, Midnight Commander ve
diðerleri gibi) fare desteði saðlar. Ayrýca fare yardýmýyla konsollar
arasýnda kopyalama ve yapýþtýrma olanaðý sunar. Fare týklamasýyla pop-up
menülerin çýkmasýný saðlayan bir program da içerir.

%package devel
Summary:     Header files and documentation for writing mouse driven programs
Group:       Development/Libraries
Requires:    %{name} = %{version}

%description devel
This package allows you to develop your own text-mode programs that take
advantage of the mouse. 

%description -l de devel
Mit diesem Paket können Sie Ihre eigenen text-orientierten Programme
mit Mausunterstützung entwickeln.

%description -l fr devel
Ce paquetage permet de développer des programmes en mode texte tirant
avantage de la souris.

%description -l tr devel
Bu paket, fare kullanan yazýlýmlar geliþtirmenizi saðlayan dosyalarý içerir.

%package static
Summary:     Static gpm library
Group:       Development/Libraries
Requires:    %{name}-devel = %{version}

%description static
Static gpm library

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

autoconf

%build
CFLAGS="$RPM_OPT_FLAGS" \
./configure --disable-debug --with-slang --without-curses
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/rc.d/{init.d,rc{0,1,2,3,5,6}.d}

%ifarch sparc
(echo MOUSETYPE=\"sun\"; echo XEMU3=no) > /etc/sysconfig/mouse
%endif

make install prefix=$RPM_BUILD_ROOT/usr
gzip -9nf $RPM_BUILD_ROOT/usr/info/gpm.info*
install gpm-root.conf $RPM_BUILD_ROOT/etc
install mouse-test hltest $RPM_BUILD_ROOT/usr/bin

strip $RPM_BUILD_ROOT/usr/bin/{gpm,mev,gpm-root}

install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/gpm
ln -sf ../init.d/gpm $RPM_BUILD_ROOT/etc/rc.d/rc2.d/S85gpm
ln -sf ../init.d/gpm $RPM_BUILD_ROOT/etc/rc.d/rc3.d/S85gpm
ln -sf ../init.d/gpm $RPM_BUILD_ROOT/etc/rc.d/rc5.d/S85gpm
ln -sf ../init.d/gpm $RPM_BUILD_ROOT/etc/rc.d/rc0.d/K15gpm
ln -sf ../init.d/gpm $RPM_BUILD_ROOT/etc/rc.d/rc1.d/K15gpm
ln -sf ../init.d/gpm $RPM_BUILD_ROOT/etc/rc.d/rc6.d/K15gpm

%post
/sbin/chkconfig --add gpm
/sbin/ldconfig
/sbin/install-info /usr/info/gpm.info.gz /usr/info/dir --entry="* gpm: (gpm).                   Text-mode mouse library."

%preun
if [ "$1" = "0" ]; then
    /sbin/install-info /usr/info/gpm.info.gz --delete /usr/info/dir --entry="* gpm: (gpm).                   Text-mode mouse library."
fi

%postun
/sbin/ldconfig
if [ $1 = 0 ]; then
    /sbin/chkconfig --del gpm
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755)
%config /etc/gpm-root.conf

%ifarch sparc
%config /etc/sysconfig/mouse
%endif

%attr(755, root, root) /usr/bin/*
/usr/share/emacs/site-lisp/*
/usr/info/gpm.info*
%attr(644, root,  man) /usr/man/man1/*
/usr/lib/lib*.so.*.*
%attr(755, root, root) %config /etc/rc.d/init.d/gpm
%attr(755, root, root) %config(missingok) /etc/rc.d/rc[01236].d/*gpm

%files devel
%defattr(644, root, root, 755)
/usr/lib/lib*.so
/usr/include/gpm.h

%files static
%attr(644, root, root) /usr/lib/lib*.a

%changelog
* Wed Aug 26 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.13-9]
- changed Buildroot to /tmp/%%{name}-%%{version}-root,
- added using %%{name} and %%{version} in Source,
- added static subpackage,
- changeded dependences to "Requires: %%{name} = %%{version}" in devel
  subpackage,
- added using $RPM_OPT_FLAGS during compile,
- added striping shared libraries,
- added full %attr description in %files,
- libgpm is now linked with libslang (so.1) as a term library
  (gpm-1.13-with_slang.patch).

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
