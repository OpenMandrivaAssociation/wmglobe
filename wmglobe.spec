Summary:	A WindowMaker dock.app that displays a rotating Earth in an icon
Name:		wmglobe
Version: 1.3
Release: %mkrel 9
License:	GPL
Group:		Graphical desktop/WindowMaker

Source:		%name-%version.tar.bz2
Source1:	%name-icons.tar.bz2

URL:		https://perso.linuxfr.org/jdumont/wmg/
BuildRequires:	WindowMaker-devel, xpm-devel, libpng-devel, libtiff-devel, libjpeg-devel
BuildRoot:	%_tmppath/%name-%version-%release-root

%description
WMGlobe is a WindowMaker dock.app that displays a rotating Earth in an icon.
It uses a map which is rendered on a sphere by raytracing. It is possible
to spin the Earth, to zoom in and out, etc.

%prep

%setup -q

%build
# Dadou - 1.1.alpha-4mdk - Use LMDK default optimizations
perl -pi -e "s|\-O2|%optflags|g" Makefile

%make

%install
install -d %buildroot/%_miconsdir
install -d %buildroot/%_iconsdir
install -d %buildroot/%_liconsdir
tar xOjf %SOURCE1 16x16.png > %buildroot/%_miconsdir/%name.png
tar xOjf %SOURCE1 32x32.png > %buildroot/%_iconsdir/%name.png
tar xOjf %SOURCE1 48x48.png > %buildroot/%_liconsdir/%name.png

install -d %buildroot/%_bindir
install -d %buildroot/%_mandir/man1
install wmglobe %buildroot/%_bindir
install wmglobe.1 %buildroot/%_mandir/man1

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
cat << EOF > %buildroot%{_datadir}/applications/mandriva-%name.desktop
[Desktop Entry]
Type=Application
Exec=wmglobe -delay 0 -dlong 5 -bord 2
Icon=%{name}
Categories=Science;Astronomy;
Name=WmGlobe
Comment=A dock.app that displays a rotating Earth in an icon
EOF

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%clean
rm -fr %buildroot

%files
%defattr (-,root,root)
%doc README CHANGES
%_bindir/*
%attr(644,root,man) %_mandir/man1/*
%_liconsdir/%name.png
%_miconsdir/%name.png
%_iconsdir/%name.png
%{_datadir}/applications/mandriva-%name.desktop


