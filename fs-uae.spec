#
# Conditional build:
%bcond_with	capsimage	# use capsimage for .IPF, .RAW and .CTR disk image support
%bcond_with	qt		# Qt 5 (not used actually as of 3.0.5)

Summary:	Amiga Emulator with focus on emulating games
Summary(pl.UTF-8):	Emulator Amigi skupiający się na grach
Name:		fs-uae
Version:	3.0.5
Release:	1
License:	GPL v2
Group:		Applications/Emulators
Source0:	https://fs-uae.net/stable/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	14524d7e21a7eb6e3660a8eb1c7ce56b
URL:		https://fs-uae.net/
%{?with_qt:BuildRequires:	Qt5Gui-devel >= 5}
BuildRequires:	OpenAL-devel
BuildRequires:	OpenGL-devel
BuildRequires:	SDL2-devel >= 2.0
BuildRequires:	gettext-tools
BuildRequires:	glew-devel
BuildRequires:	glib2-devel >= 1:2.32
%{?with_capsimage:BuildRequires:	libcapsimage-devel}
BuildRequires:	libmpeg2-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	zlib-devel
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk-update-icon-cache
Requires:	hicolor-icon-theme
Requires:	shared-mime-info
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FS-UAE is an Amiga emulator for Windows, Linux and Mac OS X based on
UAE/WinUAE, with a focus on emulating games.

Features include emulation of Amiga 500, 1200, 4000, CD32 and CDTV,
perfectly smooth scrolling on 50Hz displays, support for floppy images
in ADF%{?with_capsimage: and IPF} formats, CD-ROM images in ISO or BIN/CUE format,
mounting folders on your computer as Amiga hard drives, support for
Picasso 96 drivers for high-color and high-resolution Workbench
displays, and more...

A unique feature is support for cross-platform online play. You can
now play Amiga games against (or with) friends over the Internet.

%description -l pl.UTF-8
FS-UAE to emulator Amigi dla Windows, Linuksa i Mac OS-a X, oparty na
UAE/WinUAE, skupiający się na grach.

Obsługiwana funkcjonalność obejmuje emulację Amig 500, 1200, 4000,
CD32 oraz CDTV, płynne przewijanie na ekranach 50Hz, obrazy dyskietek
w formacie ADF%{?with_capsimage: i IPF}, obrazy CD-ROM w formacie ISO
lub BIN/CUE, montowanie katalogów jako dysków twardych Amigi,
sterowniki Picasso 96 do dużej liczby kolorów i wysokiej
rozdzielczości w Workbenchu itd.

Unikatową funkcją jest obsługa grania online między różnymi
platformami. Teraz można grać w gry z Amigi przeciw kolegom (lub z
nimi) w sieci.

%prep
%setup -q

%build
%configure \
	--with-glew \
	%{?with_qt:--with-qt} \
	--enable-caps%{!?with_capsimage:=no}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/fs-uae

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor
%update_mime_database
%update_desktop_database

%postun
%update_icon_cache hicolor
%update_mime_database
%update_desktop_database

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/fs-uae
%attr(755,root,root) %{_bindir}/fs-uae-device-helper
%{_datadir}/fs-uae
%{_datadir}/mime/packages/fs-uae.xml
%{_desktopdir}/fs-uae.desktop
%{_iconsdir}/hicolor/*x*/apps/fs-uae.png
